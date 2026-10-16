import test from 'node:test';
import assert from 'node:assert/strict';
import { env, call, login } from './harness.mjs';
import { readTranscript } from '../server-quiz-model.mjs';
import { prepareAnonymousTranscript, applyTranscriptRedactions, anonymizeTranscript } from '../transcript-privacy.mjs';
import { saveTranscriptCache, readTranscriptCache, pruneTranscriptCache, reusableTranscript, transcriptRetentionDay } from '../transcript-cache.mjs';

const student = { firstName: 'Alex', zoomNames: ['Alex Brown'] };
const note = { transcript: {
  speakers: [{ speaker_id: 'a', display_name: 'Alex Brown' }, { speaker_id: 't', display_name: 'Phil' }, { speaker_id: 'x', display_name: 'Casey' }, { speaker_id: 'y', display_name: 'Morgan' }],
  items: Array.from({ length: 10 }, (_, i) => ({ speaker_id: ['a', 't', 'x', 'y'][i % 4], start_time: '00:' + String(i + 1).padStart(2, '0') + ':00.000', end_time: '00:' + String(i + 1).padStart(2, '0') + ':30.000', text: 'I can use this word.' })),
} };
const anonymous = () => prepareAnonymousTranscript(note, readTranscript(note, { ab26: student })).segments;
const record = (start = '2026-10-14T12:00:00Z', extra = {}) => ({ privacyVersion: 1, privacyReviewed: true, noteId: 'fictional-note-123', meetingId: 'meeting-123', mappingHash: 'a'.repeat(64), sourceHash: 'b'.repeat(64), savedAt: '2026-10-15T12:00:00Z', modifiedAt: null, sourceEventAt: null,
  meeting: { start_time: start, end_time: new Date(Date.parse(start) + 3600000).toISOString() }, segments: anonymous(), ...extra });
const request = (store, path, body) => store.fetch(new Request('https://feedback.internal' + path, body ? { method: 'POST', body: JSON.stringify(body) } : {}));

test('known identities are removed before AI and trusted roles survive every turn', async () => {
  const input = structuredClone(note);
  input.transcript.items[0].text = 'Alex Brown and Phil email alex@example.test at https://example.test or +1 (555) 123-4567. Casey called Morgan.';
  const prepared = prepareAnonymousTranscript(input, readTranscript(input, { ab26: student }));
  assert.doesNotMatch(JSON.stringify(prepared.segments), /Alex|Brown|Phil|Casey|Morgan|example|555/);
  assert.deepEqual(prepared.segments.slice(0, 4).map(s => [s.role, s.speaker]), [['student', 'Student'], ['instructor', 'Instructor'], ['other', 'Speaker 1'], ['other', 'Speaker 2']]);
  let calls = 0;
  const result = await anonymizeTranscript({ run: async (_model, input) => {
    calls++; assert.doesNotMatch(input.input[1].content, /Alex|Brown|Phil|Casey|Morgan|example|555/);
    return { response: calls === 1 ? { redactions: [] } : { approved: true } };
  } }, input, readTranscript(input, { ab26: student }));
  assert.equal(calls, 2); assert.deepEqual(result, prepared.segments);
});

test('redaction removes exact sensitive spans without fixing language or changing attribution', () => {
  const segments = anonymous();
  segments[0].text = 'Yesterday I go to Riverton. I meet Renée in Riverton.';
  const result = applyTranscriptRedactions(segments, { redactions: [
    { segmentIndex: 0, text: 'Riverton', category: 'PLACE', entity: 1 },
    { segmentIndex: 0, text: 'Renée', category: 'PERSON', entity: 2 },
  ] });
  assert.equal(result[0].text, 'Yesterday I go to [PLACE_1]. I meet [PERSON_2] in [PLACE_1].');
  assert.deepEqual(result.map(({ text, ...rest }) => rest), segments.map(({ text, ...rest }) => rest));
  assert.equal(applyTranscriptRedactions(segments, { redactions: [{ segmentIndex: 0, text: 'invented', category: 'PERSON', entity: 1 }] })[0].text, '[PRIVATE_DETAIL]');
  assert.equal(applyTranscriptRedactions(segments, { redactions: [{ segmentIndex: 0, text: 'Ren', category: 'PERSON', entity: 1 }] })[0].text, '[PRIVATE_DETAIL]');
  assert.throws(() => applyTranscriptRedactions(segments, { segments: [] }), /transcript_redaction_format/);
});

test('failed or malformed privacy review never yields a storable transcript', async () => {
  for (const result of [{ approved: false }, { approved: 'true' }, 'invalid JSON']) {
    let calls = 0;
    await assert.rejects(anonymizeTranscript({ run: async () => ({ response: ++calls === 1 ? { redactions: [] } : result }) }, note, readTranscript(note, { ab26: student })), /transcript_privacy_rejected|invalid_model_response/);
  }
  const duplicate = structuredClone(note); duplicate.transcript.speakers[1].speaker_id = 'a';
  assert.throws(() => readTranscript(duplicate, { ab26: student }), /transcript_unusable/);
  assert.throws(() => prepareAnonymousTranscript(note, readTranscript(note, { ab26: student }), ['Alex Brown']), /ambiguous_student/);
});

test('large sanitized records are chunked, isolated, integrity checked, and omitted from ordinary context', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), input = record();
  input.segments[0].text = 'We can practice. '.repeat(9000);
  input.rawTranscript = 'MUST NOT BE STORED'; input.meeting.topic = 'PRIVATE TOPIC';
  assert.equal((await request(store, '/automation/transcript/' + input.noteId, input)).status, 200);
  const loaded = (await (await request(store, '/automation/transcript/' + input.noteId)).json()).transcript;
  assert.equal(loaded.segments[0].text, input.segments[0].text);
  const entries = [...await store.storage.list({ prefix: 'transcript:' })];
  assert.ok(entries.filter(([k]) => k.startsWith('transcript:data:')).length > 10);
  assert.doesNotMatch(JSON.stringify(entries), /MUST NOT BE STORED|PRIVATE TOPIC/);
  for (const [key, value] of entries) if (key.startsWith('transcript:data:')) assert.ok(new TextEncoder().encode(JSON.stringify(value)).length < 128000);
  assert.equal(await readTranscriptCache(e.FEEDBACK_STORE.get('cd26').storage, input.noteId), null);
  assert.doesNotMatch(await (await request(store, '/automation/context')).text(), /We can practice|transcript:data|mappingHash/);
  await store.storage.put({ [entries.find(([k]) => k.startsWith('transcript:data:'))[0]]: 'corrupted' });
  assert.equal(await readTranscriptCache(store.storage, input.noteId), null);
});

test('cache freshness respects source revision, speaker mapping, and unknown-revision refresh', () => {
  const input = record(), job = { noteId: input.noteId, meetingId: input.meetingId }, now = Date.parse('2026-10-16T12:00:00Z');
  assert.equal(reusableTranscript(input, job, input.mappingHash, now), true);
  assert.equal(reusableTranscript(input, job, 'c'.repeat(64), now), false);
  assert.equal(reusableTranscript(input, { ...job, sourceEventAt: now }, input.mappingHash, now), false);
  assert.equal(reusableTranscript(input, { ...job, modifiedAt: '2026-10-16T00:00:00Z' }, input.mappingHash, now), false);
  assert.equal(reusableTranscript(input, job, input.mappingHash, now + 8 * 86400000), false);
  input.modifiedAt = '2026-10-15T12:00:00Z'; job.modifiedAt = input.modifiedAt;
  assert.equal(reusableTranscript(input, job, input.mappingHash, now + 8 * 86400000), true);
  assert.equal(reusableTranscript(input, job, input.mappingHash, Date.parse('2027-02-01T12:00:00Z')), false);
});

test('retention uses three calendar months, Eastern dates, and month-end clamping', () => {
  assert.equal(transcriptRetentionDay(Date.parse('2026-10-15T12:00:00Z')), '2026-07-15');
  assert.equal(transcriptRetentionDay(Date.parse('2026-10-15T02:00:00Z')), '2026-07-14');
  assert.equal(transcriptRetentionDay(Date.parse('2026-05-31T12:00:00Z')), '2026-02-28');
  assert.equal(transcriptRetentionDay(Date.parse('2028-05-31T12:00:00Z')), '2028-02-29');
  assert.equal(transcriptRetentionDay(Date.parse('2027-01-31T12:00:00Z')), '2026-10-31');
});

test('nightly pruning removes every expired revision while preserving the cutoff day and learning history', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-07-15T12:00:00Z') });
  const store = env().FEEDBACK_STORE.get('ab26');
  const older = record('2026-07-14T12:00:00Z');
  await saveTranscriptCache(store.storage, older);
  // More than one page of old versions must all be removed.
  for (let i = 0; i < 52; i++) await saveTranscriptCache(store.storage, { ...older, savedAt: new Date(Date.now() + i * 1000).toISOString() });
  const recent = record('2026-07-15T12:00:00Z');
  await saveTranscriptCache(store.storage, recent);
  await store.storage.put({ 'assessment:current': { summary: 'Preserve assessment' }, 'cefr:current': { state: 'insufficient' }, 'feedback:example': { summary: 'Preserve feedback' }, 'attempt:example': { answers: [[1, 0]] } });
  t.mock.timers.setTime(Date.parse('2026-10-15T12:00:00Z'));
  const result = await pruneTranscriptCache(store.storage);
  assert.equal(result.removed, 53); assert.equal(result.cutoff, '2026-07-15');
  assert.deepEqual(await readTranscriptCache(store.storage, recent.noteId), recent);
  assert.equal((await store.storage.list({ prefix: 'transcript:version:' })).size, 1);
  assert.deepEqual(await store.storage.get('attempt:example'), { answers: [[1, 0]] });
  assert.equal((await store.storage.get('assessment:current')).summary, 'Preserve assessment');
  assert.ok(await store.storage.get('cefr:current')); assert.ok(await store.storage.get('feedback:example'));
  assert.deepEqual(await saveTranscriptCache(store.storage, older), { ok: true, retained: false });
  t.mock.timers.setTime(Date.parse('2026-10-16T12:00:00Z'));
  assert.equal(await readTranscriptCache(store.storage, recent.noteId), null);
  await pruneTranscriptCache(store.storage);
  assert.equal((await store.storage.list({ prefix: 'transcript:' })).size, 0);
});

test('transcript routes stay internal and account deletion prevents delayed cache writes', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const e = env(), store = e.FEEDBACK_STORE.get('ab26'), input = record();
  const studentLogin = await login(e), teacherLogin = await login(e, 'teacher-test');
  for (const user of [studentLogin, teacherLogin]) for (const path of ['/api/feedback/automation/transcript/' + input.noteId, '/api/automation/transcript/' + input.noteId, '/automation/prune-transcripts']) {
    assert.equal((await call(e, path, { headers: { Cookie: user.cookie } })).status, 404);
  }
  assert.equal((await request(store, '/automation/transcript/' + input.noteId, { ...input, privacyReviewed: false })).status, 400);
  await request(store, '/automation/transcript/' + input.noteId, input);
  await request(store, '/admin/delete-account', {});
  assert.equal((await request(store, '/automation/transcript/' + input.noteId, input)).status, 410);
  assert.equal((await request(store, '/automation/transcript/' + input.noteId)).status, 410);
  assert.equal((await store.storage.list({ prefix: 'transcript:' })).size, 0);
});


test('privacy review can request one exact repair but a fresh approval is still required',async()=>{
  const input=structuredClone(note);input.transcript.items[0].text='I go to Riverton.';
  const removal={segmentIndex:0,text:'Riverton',category:'PLACE',entity:1};
  for(const approved of [true,false]){
    let calls=0;const ai={run:async(_model,request)=>{
      calls++;const segments=JSON.parse(request.input[1].content).segments;
      if(calls===1)return {response:{redactions:[]}};
      if(calls===2)return {response:{approved:false,redactions:[removal]}};
      assert.equal(segments[0].text,'I go to [PLACE_1].');return {response:{approved,redactions:[removal]}};
    }};
    const result=anonymizeTranscript(ai,input,readTranscript(input,{ab26:student}));
    if(approved)assert.equal((await result)[0].text,'I go to [PLACE_1].');else await assert.rejects(result,/transcript_privacy_rejected/);
    assert.equal(calls,3);
  }
});

test('invalid redaction plans get only one repair and still require a separate review',async()=>{
  for(const fixed of [true,false]){
    let calls=0;const ai={run:async()=>({response:++calls===1||calls===2&&!fixed?{redactions:[{segmentIndex:99,text:'invented',category:'PERSON',entity:1}]}:calls===2?{redactions:[]}:{approved:true}})};
    const result=anonymizeTranscript(ai,note,readTranscript(note,{ab26:student}));
    if(fixed)assert.deepEqual(await result,anonymous());else await assert.rejects(result,/transcript_redaction_index/);
    assert.equal(calls,fixed?3:2);
  }
});


test('a misquoted removal hides the whole identified turn and still cannot bypass independent review',async()=>{
  for(const approved of [true,false]){
    let calls=0;const ai={run:async(_model,request)=>{
      calls++;const segments=JSON.parse(request.input[1].content).segments;
      if(calls===1)return {response:{redactions:[{segmentIndex:0,text:'a misquoted personal detail',category:'PRIVATE_DETAIL',entity:1}]}};
      assert.equal(segments[0].text,'[PRIVATE_DETAIL]');assert.equal(segments[0].role,'student');assert.equal(segments[0].at,'00:01:00');
      return {response:{approved}};
    }};
    const result=anonymizeTranscript(ai,note,readTranscript(note,{ab26:student}));
    if(approved){const saved=await result;assert.equal(saved.length,10);assert.deepEqual(saved.slice(1),anonymous().slice(1));}
    else await assert.rejects(result,/transcript_privacy_rejected/);
    assert.equal(calls,2);
  }
});
