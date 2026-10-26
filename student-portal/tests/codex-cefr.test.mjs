import test from 'node:test';
import assert from 'node:assert/strict';
import { env, call, login } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
import { QuizAutomation } from '../server-quiz-automation.mjs';
import { cefrPublishedContext } from '../cefr-schedule.mjs';
import { digest } from '../codex-handoff.mjs';
import { transcriptHash } from '../transcript-cache.mjs';
import { sessionId } from '../lesson-time.mjs';

async function fixture(t) {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-26T03:40:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), storage = e.FEEDBACK_STORE.get('coordinator').storage;
  Object.assign(e, { LESSON_PROCESSOR: 'codex', CEFR_PROCESSOR: 'codex', AUTOMATION_ENABLED: 'false', CODEX_HANDOFF_SECRET: 'a'.repeat(64),
    QUIZ_STUDENTS: JSON.stringify({ ab26: { firstName: 'Alex', zoomNames: ['Alex'], timeZone: 'America/New_York', startAfter: '2026-10-14T00:00:00Z' } }) });
  const object = new QuizAutomation({ storage }, e), notes = new Map(); let reads = 0;
  object.zoom = async path => { reads++; const id = decodeURIComponent(path.split('/')[3]); assert.ok(notes.has(id)); return structuredClone(notes.get(id)); };
  e.QUIZ_AUTOMATION = { idFromName: id => id, get: () => object };
  const dispatch = (action, input = {}) => call(e, '/api/codex/' + action, { method: 'POST', headers: { Authorization: 'Bearer ' + e.CODEX_HANDOFF_SECRET, 'Content-Type': 'application/json' }, body: JSON.stringify(input) }, 'https://phil.englishladder.com');
  async function lesson(day, overrides = {}) {
    const id = sessionId(day + 'T12:00:00Z', 'America/New_York'), noteId = 'fictional-note-' + day;
    const record = { ...feedback, id, startedAt: day + 'T12:00:00Z', timeZone: 'America/New_York', source: { ...feedback.source, noteId, reviewedFullTranscript: true }, ...overrides };
    await store.storage.put({ ['feedback:' + id]: record });
    notes.set(noteId, { transcript: { speakers: [{ speaker_id: 's', display_name: 'Alex' }, { speaker_id: 't', display_name: 'Phil' }],
      items: Array.from({ length: 10 }, (_, i) => ({ speaker_id: i % 2 ? 't' : 's', start_time: '00:' + String(i + 1).padStart(2, '0') + ':00.000',
        end_time: '00:' + String(i + 1).padStart(2, '0') + ':30.000', text: i % 2 ? 'Here is a teacher model.' : `I can explain the plan for lesson ${day.slice(-2)}.` })) } });
    return record;
  }
  function estimate(p) { return { state: 'estimated', lower: 'B1', upper: 'B2', confidence: 'moderate', rationale: 'Connected explanations with some support.',
    aspects: ['range','accuracy','coherence','interaction'].map(area => ({ area, detail: 'Independent language is visible in the exchanges.' })),
    evidence: p.sources.map(s => ({ sessionId: s.sessionId, at: '00:01:00', quote: notes.get(s.noteId).transcript.items[0].text, note: 'An independent explanation.' })) }; }
  async function payload(p, cefr = estimate(p)) { return { studentId: 'ab26', attemptId: p.attemptId, snapshotHash: p.snapshotHash, cefr,
    review: { approved: true, fullTranscript: true, independent: true, snapshotHash: p.snapshotHash, recordsHash: await digest(cefr) } }; }
  return { e, store, storage, object, dispatch, lesson, notes, estimate, payload, reads: () => reads };
}

test('Codex CEFR waits for two published full-transcript lessons, ignores old/unreviewed/duplicate sources, and needs no AI binding', async t => {
  const f = await fixture(t);
  const queue = async () => (await (await f.dispatch('cefr-queue')).json()).students[0];
  assert.equal((await queue()).due, false);
  await f.lesson('2026-06-01'); await f.lesson('2026-10-20', { source: { noteId: 'fictional-unreviewed', reviewedFullTranscript: false } });
  assert.equal((await queue()).availableSessions, 0);
  const first = await f.lesson('2026-10-21'); assert.equal((await queue()).due, false);
  await f.lesson('2026-10-22', { source: first.source }); assert.equal((await queue()).availableSessions, 1);
  await f.lesson('2026-10-23'); await f.lesson('2026-10-24');
  const p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  assert.deepEqual(p.sources.map(s => s.sessionId), ['2026-10-23-0800','2026-10-24-0800']);
  assert.doesNotMatch(JSON.stringify(p), /segments|display_name|I can explain/);
  assert.equal((await f.dispatch('cefr-prepare', { studentId: 'ab26' })).status, 409);
  assert.equal((await queue()).deferred, true);
  assert.equal(f.e.AI, undefined);
});

test('Codex publishes reviewed evidence atomically, verifies retries without source reads, and preserves lesson/quiz records', async t => {
  const f = await fixture(t); await f.lesson('2026-10-20'); await f.lesson('2026-10-24');
  await f.store.storage.put({ 'assessment:current': assessment, 'quiz:current': quiz, 'quiz:attempt:one': { answers: [[1,0]] } });
  const p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json(), input = await f.payload(p);
  const saved = await (await f.dispatch('cefr-publish', input)).json();
  assert.equal(saved.verified, true); assert.equal(saved.nextReviewOn, '2026-11-25');
  assert.equal((await f.store.storage.get('cefr:current')).confidence, 'low');
  const reads = f.reads(); assert.deepEqual(await (await f.dispatch('cefr-publish', input)).json(), saved);
  assert.equal((await f.dispatch('cefr-publish', { ...input, cefr: { ...input.cefr, rationale: 'A different draft.' } })).status, 409);
  assert.deepEqual(await (await f.dispatch('cefr-verify', p)).json(), saved); assert.equal(f.reads(), reads);
  assert.deepEqual(await f.store.storage.get('assessment:current'), assessment);
  assert.deepEqual(await f.store.storage.get('quiz:current'), quiz);
  assert.deepEqual(await f.store.storage.get('quiz:attempt:one'), { answers: [[1,0]] });
  assert.equal((await f.store.storage.list({ prefix: 'transcript:' })).size, 0);
  assert.equal((await f.store.storage.list({ prefix: 'cefr:history:' })).size, 1);
  const allCoordinatorData = JSON.stringify([...await f.storage.list()]);
  assert.doesNotMatch(allCoordinatorData, /I can explain|teacher model|segments|display_name/);
});

test('duplicate full sources and mismatched speaker identities defer instead of inventing evidence', async t => {
  const f = await fixture(t); const a = await f.lesson('2026-10-20'), b = await f.lesson('2026-10-24');
  const original = structuredClone(f.notes.get(b.source.noteId));
  f.notes.set(b.source.noteId, structuredClone(f.notes.get(a.source.noteId)));
  assert.equal((await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json()).error, 'cefr_duplicate_sources');
  t.mock.timers.setTime(Date.parse('2026-10-27T18:00:00Z'));
  original.transcript.speakers[0].display_name = 'Someone else'; f.notes.set(b.source.noteId, original);
  assert.equal((await f.dispatch('cefr-prepare', { studentId: 'ab26' })).status, 409);
  assert.equal(await f.store.storage.get('cefr:current'), undefined);
});

test('monthly Codex review waits a calendar month, selects latest four, and retains an earlier estimate on insufficient evidence', async t => {
  const f = await fixture(t); await f.lesson('2026-10-20'); await f.lesson('2026-10-24');
  let p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  await f.dispatch('cefr-publish', await f.payload(p)); const old = await f.store.storage.get('cefr:current');
  for (const date of ['2026-10-26','2026-11-01','2026-11-10','2026-11-20','2026-11-23']) await f.lesson(date);
  t.mock.timers.setTime(Date.parse('2026-11-24T18:00:00Z'));
  assert.equal((await cefrPublishedContext(f.store.storage)).due, false);
  t.mock.timers.setTime(Date.parse('2026-11-25T18:00:00Z'));
  p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  assert.equal(p.sources.length, 4); assert.equal(p.sources[0].sessionId, '2026-11-01-0700');
  assert.ok(p.attemptId);
  const result = await f.dispatch('cefr-publish', await f.payload(p, { state: 'insufficient', rationale: 'Too little independent learner language.' }));
  assert.equal(result.status, 200); assert.deepEqual(await f.store.storage.get('cefr:current'), old);
  assert.equal((await cefrPublishedContext(f.store.storage)).nextReviewOn, '2026-12-25');
  t.mock.timers.setTime(Date.parse('2026-12-25T18:00:00Z'));
  assert.equal((await cefrPublishedContext(f.store.storage)).due, false);
});

test('changed transcripts, forged review hashes, and teacher quotations cannot replace an estimate', async t => {
  const f = await fixture(t); await f.lesson('2026-10-20'); await f.lesson('2026-10-24');
  const p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  let input = await f.payload(p); input.review.recordsHash = 'f'.repeat(64);
  assert.equal((await f.dispatch('cefr-publish', input)).status, 409);
  input = await f.payload(p); input.cefr.evidence[0].at = '00:02:00'; input.cefr.evidence[0].quote = 'Here is a teacher model.'; input.review.recordsHash = await digest(input.cefr);
  assert.equal((await f.dispatch('cefr-publish', input)).status, 409);
  assert.equal(await f.store.storage.get('cefr:current'), undefined);
  t.mock.timers.setTime(Date.parse('2026-10-27T18:00:00Z'));
  const fresh = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  f.notes.get(fresh.sources[0].noteId).transcript.items[0].text += ' Changed source.';
  assert.equal((await f.dispatch('cefr-publish', await f.payload(fresh))).status, 409);
  t.mock.timers.setTime(Date.parse('2026-10-28T18:00:00Z'));
  assert.equal((await f.dispatch('cefr-prepare', { studentId: 'ab26' })).status, 409);
});

test('paused/deleted accounts, ignored sources, and changed source windows cannot receive Codex estimates', async t => {
  const f = await fixture(t); const first = await f.lesson('2026-10-20'); await f.lesson('2026-10-24');
  await f.storage.put({ ['job:' + await transcriptHash(first.source.noteId)]: { status: 'ignored' } });
  assert.equal((await f.dispatch('cefr-prepare', { studentId: 'ab26' })).status, 409);
  await f.storage.delete('job:' + await transcriptHash(first.source.noteId));
  t.mock.timers.setTime(Date.parse('2026-10-27T18:00:00Z'));
  const p = await (await f.dispatch('cefr-prepare', { studentId: 'ab26' })).json();
  const roster = f.e.QUIZ_STUDENTS; f.e.QUIZ_STUDENTS = '{}';
  assert.equal((await f.dispatch('cefr-publish', await f.payload(p))).status, 409);
  assert.deepEqual((await (await f.dispatch('cefr-queue')).json()).students, []); f.e.QUIZ_STUDENTS = roster;
  await f.lesson('2026-10-26'); assert.equal((await f.dispatch('cefr-publish', await f.payload(p))).status, 409);
  await f.store.fetch(new Request('https://feedback.internal/admin/delete-account', { method: 'POST', body: '{}' }));
  assert.equal((await f.dispatch('cefr-publish', await f.payload(p))).status, 409);
  assert.equal((await f.store.storage.list({ prefix: 'cefr:' })).size, 0);
});

test('CEFR operator actions reject browser/student/cross-host access and require separately enabled Codex with paid AI disabled', async t => {
  const f = await fixture(t), student = await login(f.e), teacher = await login(f.e, 'teacher-test');
  for (const action of ['cefr-queue','cefr-prepare','cefr-publish','cefr-verify']) {
    for (const headers of [{}, { Cookie: student.cookie }, { Cookie: teacher.cookie }, { Authorization: 'Bearer ' + f.e.CODEX_HANDOFF_SECRET, Origin: 'https://phil.englishladder.com' }]) {
      assert.equal((await call(f.e, '/api/codex/' + action, { method: 'POST', headers, body: '{}' }, 'https://phil.englishladder.com')).status, 401);
    }
    assert.equal((await call(f.e, '/api/codex/' + action, { method: 'POST', headers: { Authorization: 'Bearer ' + f.e.CODEX_HANDOFF_SECRET }, body: '{}' })).status, 404);
  }
  f.e.AI = { run: () => assert.fail('No paid inference') }; assert.equal((await f.dispatch('cefr-queue')).status, 409); delete f.e.AI;
  f.e.CEFR_PROCESSOR = 'disabled'; assert.equal((await f.dispatch('cefr-queue')).status, 409);
});
