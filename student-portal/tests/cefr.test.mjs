import test from 'node:test';
import assert from 'node:assert/strict';
import { validateCefr, groundCefrWindow, cefrOverview, insufficientCefr } from '../cefr.mjs';
import { env, login, call } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
import { saveTranscriptCache } from '../transcript-cache.mjs';
import { cefrReviewContext } from '../cefr-schedule.mjs';
import { nextCalendarMonth } from '../lesson-time.mjs';
import { authorCefr, cefrModelInput } from '../server-cefr-model.mjs';
import { QuizAutomation } from '../server-quiz-automation.mjs';

const exampleCefr = {
  state:'estimated',lower:'B1',upper:'B2',confidence:'moderate',latestSessionId:feedback.id,assessedOn:'2026-10-14',
  rationale:'Connected explanations are clear; complex forms still need support.',
  aspects:['range','accuracy','coherence','interaction'].map(area=>({area,detail:'Some evidence is visible; more independent language is needed.'})),
  evidence:[{sessionId:feedback.id,at:'00:02:00',quote:'I can explain how it works.',note:'An independent explanation.'},
    {sessionId:feedback.id,at:'00:03:00',quote:'Could you explain the last part?',note:'A useful clarification question.'}]
};

test('CEFR estimates require valid adjacent levels, actual dates, four areas and distinct evidence',()=>{
  const result=validateCefr({...exampleCefr,sourceSessions:['invented'],password:'do-not-save'});
  assert.equal(result.confidence,'low');assert.deepEqual(result.sourceSessions,[feedback.id]);assert.equal(result.password,undefined);
  for(const change of [{lower:'B1.7'},{upper:'C2'},{upper:'A2'},{confidence:'high'},{assessedOn:'2026-02-30'},{assessedOn:'2026-09-30'},
    {evidence:[]},{evidence:[exampleCefr.evidence[0],exampleCefr.evidence[0]]},{aspects:exampleCefr.aspects.slice(1)}]) assert.throws(()=>validateCefr({...exampleCefr,...change}));
  const older=exampleCefr.evidence[0];
  const three=validateCefr({...exampleCefr,evidence:[...exampleCefr.evidence,{...older,sessionId:'2026-09-20-1200'},{...older,sessionId:'2026-09-25-1200'}]});
  assert.equal(three.confidence,'moderate');
  assert.doesNotMatch(JSON.stringify(cefrOverview(three)),/quote|rationale|sourceSessions|aspects/);
  assert.deepEqual(cefrOverview(null),{state:'pending'});
  assert.equal(validateCefr({...insufficientCefr(feedback.id,'2026-10-14'),lower:'B1'}).lower,undefined);
});

const internal = (store, path, body) => store.fetch(new Request('https://feedback.internal' + path, body === undefined ? {} : { method: 'POST', body: JSON.stringify(body) }));
async function cache(store, day, options = {}) {
  const record = { privacyVersion: 1, privacyReviewed: true, noteId: 'fictional-note-' + day, meetingId: 'meeting-' + day,
    mappingHash: 'a'.repeat(64), sourceHash: Number(day.replaceAll('-', '')).toString(16).padStart(64, '0'), savedAt: new Date().toISOString(), modifiedAt: null, sourceEventAt: null,
    meeting: { start_time: day + 'T12:00:00Z', end_time: day + 'T13:00:00Z' },
    segments: Array.from({ length: 10 }, (_, i) => ({ index: i, at: '00:' + String(i + 1).padStart(2, '0') + ':00', end: '00:' + String(i + 1).padStart(2, '0') + ':30',
      role: i % 2 ? 'instructor' : 'student', speaker: i % 2 ? 'Instructor' : 'Student', text: i % 2 ? 'A teacher model only.' : 'I can explain how it works.' })), ...options };
  await saveTranscriptCache(store.storage, record); return record;
}
function estimate(context) {
  return { ...exampleCefr, latestSessionId: context.sessions.at(-1).sessionId, assessedOn: context.today,
    evidence: context.sessions.map(s => ({ sessionId: s.sessionId, at: s.segments[0].at, quote: s.segments[0].text, note: 'Independent learner language.' })) };
}
async function publish(store, context, cefr = estimate(context)) {
  return internal(store, '/automation/cefr-publish', { timeZone: 'America/New_York', windowHash: context.windowHash, cefr });
}

test('initial CEFR waits for two distinct retained sessions and uses the two latest full transcripts', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26');
  assert.equal((await cefrReviewContext(store.storage)).due, false);
  const first = await cache(store, '2026-10-10');
  assert.equal((await cefrReviewContext(store.storage)).due, false);
  await cache(store, '2026-10-10', { ...first, noteId: 'fictional-duplicate-note' });
  assert.equal((await cefrReviewContext(store.storage)).availableSessions, 1);
  await cache(store, '2026-10-12');
  let context = await cefrReviewContext(store.storage);
  assert.equal(context.due, true); assert.equal(context.sessions.length, 2);
  assert.ok(context.sessions.every(s => s.segments.length === 10));
  await cache(store, '2026-10-14');
  context = await cefrReviewContext(store.storage);
  assert.deepEqual(context.sessions.map(s => s.sessionId.slice(0, 10)), ['2026-10-12', '2026-10-14']);
  assert.equal((await publish(store, context)).status, 200);
  assert.equal((await store.storage.get('cefr:current')).confidence, 'low');
  assert.equal((await publish(store, context)).status, 409);
});

test('monthly reviews use the latest four retained sessions and do not run before the anniversary or on unchanged evidence', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26');
  await cache(store, '2026-10-10'); await cache(store, '2026-10-14');
  await publish(store, await cefrReviewContext(store.storage));
  t.mock.timers.setTime(Date.parse('2026-11-15T12:00:00Z'));
  for (const day of ['2026-10-20', '2026-10-25', '2026-11-01', '2026-11-10', '2026-11-14']) await cache(store, day);
  let context = await cefrReviewContext(store.storage);
  assert.equal(context.due, false); assert.equal(context.nextReviewOn, '2026-11-16');
  t.mock.timers.setTime(Date.parse('2026-11-16T12:00:00Z'));
  context = await cefrReviewContext(store.storage);
  assert.equal(context.due, true);
  assert.deepEqual(context.sessions.map(s => s.sessionId.slice(0, 10)), ['2026-10-25', '2026-11-01', '2026-11-10', '2026-11-14']);
  assert.equal((await publish(store, context)).status, 200);
  assert.equal((await store.storage.get('cefr:current')).sourceSessions.length, 4);
  t.mock.timers.setTime(Date.parse('2026-12-16T12:00:00Z'));
  assert.equal((await cefrReviewContext(store.storage)).due, false);
  assert.equal(nextCalendarMonth('2026-01-31'), '2026-02-28');
  assert.equal(nextCalendarMonth('2028-01-31'), '2028-02-29');
  assert.equal(nextCalendarMonth('2026-12-31'), '2027-01-31');
});

test('retention can reduce a monthly window to two or three, and fewer than two defers it', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-07-16T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26');
  await cache(store, '2026-07-01'); await cache(store, '2026-07-10');
  await publish(store, await cefrReviewContext(store.storage));
  t.mock.timers.setTime(Date.parse('2026-10-16T12:00:00Z'));
  await cache(store, '2026-10-01');
  assert.equal((await cefrReviewContext(store.storage)).due, false);
  await cache(store, '2026-10-05');
  const context = await cefrReviewContext(store.storage);
  assert.equal(context.due, true); assert.equal(context.sessions.length, 2);
  assert.ok(context.sessions.every(s => s.sessionId.startsWith('2026-10')));
});

test('CEFR evidence requires exact Student quotes from every selected session and rejects older or teacher evidence', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26'); await cache(store, '2026-10-10'); await cache(store, '2026-10-14');
  const context = await cefrReviewContext(store.storage), valid = estimate(context);
  assert.equal(groundCefrWindow(valid, context.sessions, context.today).state, 'estimated');
  for (const ref of [{ ...valid.evidence[0], quote: 'Invented language' }, { ...valid.evidence[0], at: '00:02:00', quote: 'A teacher model only.' }, { ...valid.evidence[0], sessionId: '2026-09-01-0800' }]) {
    assert.throws(() => groundCefrWindow({ ...valid, evidence: [ref, valid.evidence[1]] }, context.sessions, context.today));
  }
  assert.throws(() => groundCefrWindow(valid, context.sessions.slice(1), context.today));
  let calls = 0;
  const result = await authorCefr({ run: async (_model, input) => {
    calls++; const data = JSON.parse(input.messages[1].content);
    assert.equal(data.sessions.length, 2); assert.ok(data.sessions.every(s => s.segments.length === 10));
    assert.equal(data.priorCefr, undefined); assert.doesNotMatch(input.messages[1].content, /sourceHash|noteId|mappingHash/);
    return { response: calls === 1 ? { cefr: valid } : { approved: true } };
  } }, context);
  assert.equal(calls, 2); assert.equal(result.confidence, 'low');
  calls = 0;
  await assert.rejects(authorCefr({ run: async () => ({ response: ++calls === 1 ? { cefr: valid } : { approved: false } }) }, context), /cefr_review_failed/);
  assert.throws(() => cefrModelInput({ sessions: [{ sessionId: 'example', segments: [{ text: 'x'.repeat(300001) }] }] }), /cefr_window_too_large/);
});

test('monthly publication rechecks the window, isolates accounts and leaves lesson pages and quiz history intact', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), student = await login(e);
  await cache(store, '2026-10-10'); await cache(store, '2026-10-14');
  const context = await cefrReviewContext(store.storage);
  assert.equal((await publish(e.FEEDBACK_STORE.get('cd26'), context)).status, 409);
  await cache(store, '2026-10-15');
  assert.equal((await publish(store, context)).status, 409);
  await store.storage.put({ 'assessment:current': { ...assessment, quiz }, 'quiz:attempt:example': { answers: [[1, 0]] } });
  const fresh = await cefrReviewContext(store.storage);
  assert.equal((await publish(store, fresh)).status, 200);
  assert.deepEqual(await store.storage.get('assessment:current'), { ...assessment, quiz });
  assert.deepEqual(await store.storage.get('quiz:attempt:example'), { answers: [[1, 0]] });
  assert.equal((await store.storage.list({ prefix: 'cefr:history:' })).size, 1);
  const current = await store.storage.get('cefr:current');
  assert.equal((await internal(store, '/automation/publish', { cefr: current, quiz: { ...quiz, generatedForSession: feedback.id, sourceSessions: [feedback.id], patternTitles: ['Test'] }, priorAssessment: { ...assessment, quiz } })).status, 400);
  for (const path of ['/api/assessment', '/api/feedback', '/api/quiz/state']) {
    const response = await call(e, path, { headers: { Cookie: student.cookie } });
    assert.equal(response.status, 200); assert.doesNotMatch(await response.text(), /CEFR|cefr|Connected explanations|Independent learner language/);
  }
  for (const path of ['/api/automation/cefr-context', '/api/automation/cefr-publish']) assert.equal((await call(e, path, { method: 'POST', headers: { Cookie: student.cookie }, body: '{}' })).status, 404);
  const detail = await (await internal(store, '/admin/cefr')).json();
  assert.equal(detail.schedule.nextReviewOn, '2026-11-16'); assert.equal(detail.schedule.initialAfter, 2);
  assert.doesNotMatch(JSON.stringify(detail), /segments|mappingHash|sourceHash/);
  await internal(store, '/admin/delete-account', {});
  assert.equal((await publish(store, fresh)).status, 410);
  assert.equal((await store.storage.list({ prefix: 'cefr:' })).size, 0);
});

test('an insufficient monthly review preserves the last estimate and waits another month', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26');
  await cache(store, '2026-10-10'); await cache(store, '2026-10-14'); await publish(store, await cefrReviewContext(store.storage));
  const original = await store.storage.get('cefr:current');
  t.mock.timers.setTime(Date.parse('2026-11-16T12:00:00Z')); await cache(store, '2026-11-10');
  const context = await cefrReviewContext(store.storage);
  assert.equal((await publish(store, context, { state: 'insufficient', rationale: 'Too little independent learner language.' })).status, 200);
  assert.deepEqual(await store.storage.get('cefr:current'), original);
  const detail = await (await internal(store, '/admin/cefr')).json();
  assert.equal(detail.schedule.lastReviewState, 'insufficient'); assert.equal(detail.schedule.nextReviewOn, '2026-12-16');
});

function automation(e) {
  const storage = e.FEEDBACK_STORE.get('coordinator').storage;
  const student = { firstName: 'Alex', zoomNames: ['Alex'], timeZone: 'America/New_York', startAfter: '2026-07-01T00:00:00Z' };
  const config = { ...e, AUTOMATION_ENABLED: 'true', QUIZ_STUDENTS: JSON.stringify({ ab26: student }), ZOOM_CLIENT_ID: 'test', ZOOM_CLIENT_SECRET: 'test', AI: {} };
  return { object: new QuizAutomation({ storage }, config), storage, config };
}

test('a due review runs from cached sessions even with Zoom unavailable and no new lesson job', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), { object, storage, config } = automation(e);
  await cache(store, '2026-10-10'); await cache(store, '2026-10-14');
  const context = await cefrReviewContext(store.storage); let calls = 0;
  config.AI.run = async () => ({ response: ++calls === 1 ? { cefr: estimate(context) } : { approved: true } });
  object.accessToken = async () => { throw Error('zoom_reconnect'); };
  object.zoom = async () => { throw Error('No transcript downloads allowed'); };
  await object.run(); assert.equal(calls, 2); assert.equal((await store.storage.get('cefr:current')).state, 'estimated');
  await object.run(); assert.equal(calls, 2);
  assert.equal(await storage.get('usage:ab26'), undefined);
  assert.equal((await storage.get('cefr-usage:ab26')).monthly, 1);
});

test('CEFR attempts respect spending caps and student pauses during generation', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), { object, storage, config } = automation(e);
  await cache(store, '2026-10-10'); await cache(store, '2026-10-14');
  const context = await cefrReviewContext(store.storage); let calls = 0;
  config.AI.run = async () => { calls++; config.QUIZ_STUDENTS = '{}'; return { response: calls === 1 ? { cefr: estimate(context) } : { approved: true } }; };
  await object.reviewCefr(Date.now() + 10000);
  assert.equal(calls, 2); assert.equal(await store.storage.get('cefr:current'), undefined);
  assert.equal(await storage.get('cefr-error:ab26'), 'student_changed');
  await assert.rejects(object.reserveGeneration('ab26', 'cefr'), /cefr_limit/);
  t.mock.timers.setTime(Date.parse('2026-10-17T12:00:00Z')); await object.reserveGeneration('ab26', 'cefr');
  t.mock.timers.setTime(Date.parse('2026-10-18T12:00:00Z')); await assert.rejects(object.reserveGeneration('ab26', 'cefr'), /cefr_limit/);
  await storage.put({ 'usage:cd26': { day: '2026-10-18', month: '2026-10', daily: 0, monthly: 12 } });
  await object.reserveGeneration('cd26', 'cefr'); // Ordinary lesson cap cannot block a monthly review.
  assert.equal((await storage.get('usage:cd26')).monthly, 12);
});
