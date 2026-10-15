import test from 'node:test';
import assert from 'node:assert/strict';
import worker from '../worker.mjs';
import { QuizAutomation, hash, nightlyDate, zoomSignatureValid } from '../server-quiz-automation.mjs';
import { readTranscript, authorQuiz, firstTryReview } from '../server-quiz-model.mjs';
import { seedQuiz, call, origin, env as emptyEnv } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';

const student = { firstName: 'Alex', zoomNames: ['Alex0529'], timeZone: 'America/New_York', startAfter: '2026-10-14T00:00:00Z' };
const note = { transcript: { speakers: [{ speaker_id: 'a', display_name: 'Alex0529' }, { speaker_id: 't', display_name: 'Private Teacher Name' }],
  items: Array.from({ length: 10 }, (_, i) => ({ speaker_id: i % 2 ? 't' : 'a', start_time: '00:' + String(i + 1).padStart(2, '0') + ':00.000',
    end_time: '00:' + String(i + 1).padStart(2, '0') + ':30.000', text: 'We can practice English.' })) } };
const meeting = { start_time: '2026-10-15T00:57:01Z', end_time: '2026-10-15T02:00:00Z' };
const session = '2026-10-14-2057';
const draft = { sufficientEvidence: true, feedback, assessment: { ...assessment, summary: 'You can use “can” in a short sentence.', progress: { detail: 'Keep using “can” in new sentences.', evidence: [{ sessionId: session, at: '00:02:00' }] } }, quiz: { ...quiz, patternTitles: ['Use “can”'],
  questions: [...quiz.questions, ...quiz.questions] },
  evidence: [0, 1, 2, 3].map(questionIndex => ({ questionIndex, segments: [questionIndex], reviewRefs: [] })) };
function memory() {
  const values = new Map(); let queue = Promise.resolve();
  return {
    async get(key) { return structuredClone(values.get(key)); },
    async put(data) { for (const [k, v] of Object.entries(data)) values.set(k, structuredClone(v)); },
    async delete(key) { values.delete(key); },
    async list({ prefix = '', reverse, limit, end }) {
      let keys = [...values.keys()].filter(k => k.startsWith(prefix) && (!end || k < end)).sort();
      if (reverse) keys.reverse();
      return new Map(keys.slice(0, limit ?? keys.length).map(k => [k, structuredClone(values.get(k))]));
    },
    async setAlarm(time) { this.alarmAt = time; },
    async transaction(fn) { const run = queue.then(() => fn(this)); queue = run.catch(() => {}); return run; },
  };
}
function coordinator(base = {}) {
  const storage = memory();
  const env = { ...base, ZOOM_CLIENT_ID: 'test-client', ZOOM_CLIENT_SECRET: 'test-secret', ZOOM_WEBHOOK_SECRET: 'test-webhook',
    QUIZ_STUDENTS: JSON.stringify({ ab26: student }), AUTOMATION_ENABLED: 'true', AI: { run: async () => ({ response: '{}' }) } };
  return { storage, env, object: new QuizAutomation({ storage }, env) };
}
async function signedRequest(payload, secret = 'test-webhook', seconds = Math.floor(Date.now() / 1000)) {
  const body = JSON.stringify(payload), enc = new TextEncoder();
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const bytes = await crypto.subtle.sign('HMAC', key, enc.encode('v0:' + seconds + ':' + body));
  const signature = 'v0=' + [...new Uint8Array(bytes)].map(b => b.toString(16).padStart(2, '0')).join('');
  return new Request('https://automation.internal/webhook', { method: 'POST', body,
    headers: { 'x-zm-request-timestamp': String(seconds), 'x-zm-signature': signature } });
}
const event = { event: 'my_notes.transcript_generated', payload: { account_id: 'account-1', operator_id: 'owner-1',
  object: { note_id: 'fictional-note-123', meeting_id: 'meeting-123' } } };

test('Zoom events require a fresh valid signature and matching authorized owner; duplicates queue once', async () => {
  const { object, storage } = coordinator();
  await storage.put({ oauth: { userId: 'owner-1', accountId: 'account-1' } });
  const request = await signedRequest(event);
  assert.equal(await zoomSignatureValid('test-webhook', request, await request.clone().text()), true);
  assert.equal((await object.fetch(await signedRequest(event, 'wrong'))).status, 401);
  assert.equal((await object.fetch(await signedRequest(event, 'test-webhook', Math.floor(Date.now() / 1000) - 301))).status, 401);
  assert.equal((await object.fetch(await signedRequest({ ...event, payload: { ...event.payload, operator_id: 'someone-else' } }))).status, 403);
  assert.equal((await object.fetch(await signedRequest(event))).status, 200);
  assert.equal((await object.fetch(await signedRequest(event))).status, 200);
  assert.equal((await storage.list({ prefix: 'job:' })).size, 1);
  const challenge = await object.fetch(await signedRequest({ event: 'endpoint.url_validation', payload: { plainToken: 'example' } }));
  const answer = await challenge.json();
  assert.equal(answer.plainToken, 'example'); assert.match(answer.encryptedToken, /^[a-f0-9]{64}$/);
  assert.equal(storage.alarmAt, undefined);
});

test('only the teacher can inspect or start server setup; public internal routes stay inaccessible', async () => {
  const { e, teacher, student: login } = await seedQuiz();
  assert.equal((await call(e, '/api/automation/status')).status, 401);
  assert.equal((await call(e, '/api/automation/status', { headers: { Cookie: login.cookie } })).status, 403);
  assert.equal((await call(e, '/api/automation/connect', { method: 'POST', headers: { Cookie: teacher.cookie, Origin: 'https://other.test' } })).status, 403);
  assert.equal((await call(e, '/api/automation/verify', { method: 'POST', headers: { Cookie: login.cookie, Origin: origin } })).status, 403);
  assert.equal((await call(e, '/api/automation/run', { method: 'POST', headers: { Cookie: teacher.cookie, Origin: origin } })).status, 404);
  assert.equal((await call(e, '/api/feedback/automation/publish', { method: 'PUT', headers: { Cookie: teacher.cookie } })).status, 404);
  const response = await call(e, '/api/automation/status', { headers: { Cookie: teacher.cookie } });
  assert.deepEqual(await response.json(), { configured: false, connected: false, enabled: false });
  assert.equal(response.headers.get('Cache-Control'), 'no-store');
  let dispatched = 0;
  e.QUIZ_AUTOMATION = { idFromName: id => id, get: () => ({ fetch: async () => { dispatched++; return Response.json({ ok: true }); } }) };
  await worker.scheduled({}, e); assert.equal(dispatched, 0);
  e.AUTOMATION_ENABLED = 'true'; await worker.scheduled({scheduledTime: Date.parse('2026-07-01T05:00:00Z')}, e); assert.equal(dispatched, 1);
  await worker.scheduled({scheduledTime: Date.parse('2026-07-01T06:00:00Z')}, e); assert.equal(dispatched, 1);
});

test('OAuth state is single-use, expires, and is tied to the originating student host', async () => {
  const { object, storage } = coordinator();
  const response = await object.connect(origin, 'ab26'), link = new URL((await response.json()).url);
  assert.equal(link.origin, 'https://zoom.us'); assert.equal(link.searchParams.get('redirect_uri'), origin + '/api/automation/callback');
  const state = link.searchParams.get('state');
  assert.equal((await object.callback(new URL('https://other.englishladder.com/api/automation/callback?code=test&state=' + state))).status, 400);
  const oldFetch = globalThis.fetch; let exchanges = 0;
  globalThis.fetch = async (url, options) => {
    assert.equal(options.redirect, 'manual');
    if (String(url).includes('/oauth/token')) { exchanges++; return Response.json({ access_token: 'secret-access', refresh_token: 'secret-refresh', expires_in: 3600 }); }
    return Response.json({ id: 'owner-1', account_id: 'account-1' });
  };
  try {
    const callback = new URL(origin + '/api/automation/callback?code=test&state=' + state);
    assert.equal((await object.callback(callback)).status, 303);
    assert.equal((await object.callback(callback)).status, 400); assert.equal(exchanges, 1);
    const status = await (await object.fetch(new Request('https://automation.internal/status', { headers: { 'X-Student-ID': 'ab26' } }))).text();
    assert.doesNotMatch(status, /secret-access|secret-refresh|owner-1|account-1/);
    const again = new URL((await (await object.connect(origin, 'ab26')).json()).url);
    const key = 'state:' + await hash(again.searchParams.get('state'));
    await storage.put({ [key]: { origin, studentId: 'ab26', expiresAt: Date.now() - 1 } });
    assert.equal((await object.callback(new URL(origin + '/api/automation/callback?code=test&state=' + again.searchParams.get('state')))).status, 400);
  } finally { globalThis.fetch = oldFetch; }
});

test('full transcripts are identified by speaker, never silently truncated, and redact display names', () => {
  const read = readTranscript(note, { ab26: student });
  assert.equal(read.segments.length, 10); assert.equal(read.studentId, 'ab26');
  assert.doesNotMatch(JSON.stringify(read.segments), /Private Teacher Name|Alex0529/);
  assert.throws(() => readTranscript(note, { cd26: { ...student, zoomNames: ['Somebody else'] } }), /other_student/);
  assert.throws(() => readTranscript(note, { ab26: student, cd26: student }), /ambiguous_student/);
  assert.throws(() => readTranscript({ transcript: { ...note.transcript, items: [] } }, { ab26: student }), /transcript_unusable/);
  const large = structuredClone(note); large.transcript.items[9].text = 'x'.repeat(180001);
  assert.throws(() => readTranscript(large, { ab26: student }), /transcript_too_large/);
});

test('first-try review retains misses after successful retries and ignores unanswered questions', () => {
  const attempts = [{ id: 'example-attempt', version: 'version', quiz, patternTitles: ['Use “can”'], sourceSessions: [feedback.id],
    startedAt: '2026-10-14T12:00:00Z', answers: [[1, 0], []] }];
  assert.equal(firstTryReview(attempts)[0].misses, 1);
  assert.equal(firstTryReview(attempts)[0].examples[0].firstChoice, quiz.questions[0].options[1].text);
});

test('AI authoring requires valid evidence and a second approval; no transcript text is saved in output', async () => {
  const transcript = readTranscript(note, { ab26: student }); let calls = 0;
  const ai = { run: async (_model, input) => {
    calls++; assert.ok(JSON.parse(input.messages[1].content).segments.length === 10);
    return { response: calls === 1 ? structuredClone(draft) : { approved: true } };
  } };
  const output = await authorQuiz(ai, transcript, meeting, 'fictional-note-123', { assessment, attempts: [] });
  assert.equal(calls, 2); assert.equal(output.quiz.generatedForSession, session);
  assert.ok(output.quiz.sourceSessions.includes(feedback.id));
  assert.equal(output.feedback.source.segmentCount, 10);
  assert.equal(output.transcript, undefined);
  const reject = { run: async () => ({ response: { ...structuredClone(draft), approved: false } }) };
  await assert.rejects(authorQuiz(reject, transcript, meeting, 'fictional-note-123', { assessment, attempts: [] }), /content_review_failed/);
});

test('nightly server run publishes all pages atomically and does not regenerate a completed job', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const seed = await seedQuiz(), { object, storage, env } = coordinator(seed.e);
  await storage.put({ oauth: { access: 'access', refresh: 'refresh', expiresAt: Date.now() + 3600000, userId: 'owner-1', accountId: 'account-1' } });
  const key = 'job:' + await hash(event.payload.object.note_id);
  await storage.put({ [key]: { noteId: event.payload.object.note_id, meetingId: 'meeting-123', receivedAt: Date.now() - 1000000,
    nextAt: 0, status: 'pending', tries: 0 } });
  const oldFetch = globalThis.fetch; let calls = 0;
  object.discover = async () => {};
  globalThis.fetch = async url => Response.json(String(url).includes('/past_meetings/') ? meeting : note);
  env.AI = { run: async () => ({ response: ++calls % 2 ? structuredClone(draft) : { approved: true } }) };
  try {
    await object.run(); let job = await storage.get(key);
    assert.equal(job.status, 'published'); assert.equal(calls, 2);
    const saved = await (await call(seed.e, '/api/assessment', { headers: { Cookie: seed.teacher.cookie } })).json();
    assert.equal(saved.assessment.quiz.generatedForSession, session);
    assert.equal(saved.assessment.summary, draft.assessment.summary);
    const prior = await seed.e.FEEDBACK_STORE.get('ab26').storage.get('assessment:before:' + session);
    assert.deepEqual(prior, { ...assessment, quiz });
    const recorded = await seed.e.FEEDBACK_STORE.get('ab26').storage.get('feedback:' + session);
    assert.equal(recorded.summary, feedback.summary);
    const conflict = await object.portal('ab26', '/automation/context');
    const duplicate = await object.portal('ab26', '/automation/publish', { quiz: saved.assessment.quiz });
    assert.equal(duplicate.duplicate, true);
    await object.run(); assert.equal(calls, 2);
    // A repeated Zoom note for the same meeting also cannot regenerate the quiz.
    await storage.put({ ['job:second']: { ...job, status: 'pending', nextAt: 0 } });
    await object.run(); assert.equal(calls, 2);
    const history = await (await call(seed.e, '/api/quiz/results', { headers: { Cookie: seed.teacher.cookie } })).json();
    assert.equal(history.attempts.length, 0);
    assert.doesNotMatch(JSON.stringify([...await storage.list({ prefix: 'job:' })]), /We can practice English/);
  } finally { globalThis.fetch = oldFetch; }
});

test('generation reservations survive retries and enforce daily and monthly limits before AI use', async () => {
  const { object, storage } = coordinator();
  await Promise.all([object.reserveGeneration('ab26'), object.reserveGeneration('ab26')]);
  await assert.rejects(object.reserveGeneration('ab26'), /daily_limit/);
  const day = new Date().toISOString().slice(0, 10);
  await storage.put({ 'usage:ab26': { day, month: day.slice(0, 7), daily: 0, monthly: 12 } });
  await assert.rejects(object.reserveGeneration('ab26'), /monthly_limit/);
  await object.reserveGeneration('cd26'); // One student's cap cannot block another account.
});


test('1 a.m. Eastern follows daylight saving and runs once on the repeated autumn hour', async () => {
  assert.equal(nightlyDate(Date.parse('2026-01-01T06:00:00Z')), '2026-01-01');
  assert.equal(nightlyDate(Date.parse('2026-07-01T05:00:00Z')), '2026-07-01');
  assert.equal(nightlyDate(Date.parse('2026-07-01T06:00:00Z')), null);
  assert.equal(nightlyDate(Date.parse('2026-03-08T06:00:00Z')), '2026-03-08');
  const {object, storage} = coordinator(); let runs = 0;
  object.accessToken = async () => 'test'; object.discover = async () => { runs++; };
  await object.run(Date.parse('2026-11-01T05:00:00Z'));
  await object.run(Date.parse('2026-11-01T06:00:00Z'));
  assert.equal(runs, 1); assert.equal(await storage.get('nightly-date'), '2026-11-01');
});

test('nightly discovery follows every search page, resolves dates, overlaps late transcripts, and never advances on failure', async () => {
  const {object, storage} = coordinator();
  await storage.put({oauth:{userId:'owner',pmi:1234567890}});
  let searches = [], lists = 0;
  object.zoom = async (path, _token, body) => {
    if (path === '/docs/file_search') { searches.push(body); return {files:[{file_id: body.next_page_token ? 'second-note-123' : 'fictional-note-123'}],next_page_token:body.next_page_token ? '' : 'page2'}; }
    if (path.startsWith('/users/me/meetings?')) { lists++; return lists % 2 ? {meetings:[],next_page_token:'more'} : {meetings:[]}; }
    if (path === '/past_meetings/1234567890/instances') return {meetings:[{uuid:'meeting',start_time:meeting.start_time}]};
    if (path.startsWith('/my_notes/notes?')) return {notes:[{note_id:'fictional-note-123',modified_time:meeting.end_time}]};
    throw Error('Unexpected path');
  };
  await object.discover();
  assert.equal(searches.length,2); assert.equal(lists,2);
  assert.equal(searches[1].next_page_token,'page2');
  assert.equal(searches[0].modified_time_from,searches[1].modified_time_from);
  const jobs = [...(await storage.list({prefix:'job:'})).values()];
  assert.equal(jobs.length,2); assert.equal(jobs.find(j=>j.noteId==='fictional-note-123').meetingId,'meeting');
  const checkpoint = await storage.get('discovery-since');
  object.zoom = async () => { throw Error('zoom_unavailable'); };
  await assert.rejects(object.discover(),/zoom_unavailable/);
  assert.equal(await storage.get('discovery-since'),checkpoint);
});

test('unmatched student notes cannot be published under a guessed date', async () => {
  const {object,env} = coordinator(); let aiCalls = 0;
  object.zoom = async () => note; object.portal = async () => ({sourceNotes:[]}); env.AI.run = async () => { aiCalls++; };
  await assert.rejects(object.process('job:test',{noteId:'fictional-note-123'}),/meeting_reference_missing/);
  assert.equal(aiCalls,0);
});


test('publication rejects stale assessment inputs and cannot reference another student', async () => {
  const seed = await seedQuiz();
  const store = seed.e.FEEDBACK_STORE.get('ab26');
  const input = {priorAssessment:{...assessment,quiz}, feedback:{...feedback,id:session,startedAt:meeting.start_time},
    assessment:{...assessment,sourceSessions:[feedback.id,session]},quiz:{...quiz,patternTitles:['Use “can”'],sourceSessions:[feedback.id,session],generatedForSession:session}};
  await seed.publish('/api/assessment',{...assessment,summary:'A teacher edit.',quiz});
  const stale = await store.fetch(new Request('https://feedback.internal/automation/publish',{method:'POST',body:JSON.stringify(input)}));
  assert.equal(stale.status,409);
  assert.equal(await store.storage.get('feedback:'+session),undefined);
  assert.equal((await store.storage.get('assessment:current')).summary,'A teacher edit.');
  const other = seed.e.FEEDBACK_STORE.get('cd26');
  assert.equal((await other.fetch(new Request('https://feedback.internal/automation/publish',{method:'POST',body:JSON.stringify(input)}))).status,409);
});


test('the worker returns the OAuth browser redirect instead of following it inside the private service', async () => {
  const {e}=await seedQuiz();
  e.QUIZ_AUTOMATION={idFromName:id=>id,get:()=>({fetch:async request=>{
    assert.equal(request.redirect,'manual');
    return new Response(null,{status:303,headers:{Location:origin+'/#quiz-results'}});
  }})};
  const response=await call(e,'/api/automation/callback?code=example&state=example');
  assert.equal(response.status,303);assert.equal(response.headers.get('Location'),origin+'/#quiz-results');
});


test('notes for unregistered students are flagged for the teacher without guessing or publishing', async () => {
 const {object,storage}=coordinator();
 object.accessToken=async()=> 'test'; object.discover=async()=> {};
 object.zoom=async()=>({...note,transcript:{...note.transcript,speakers:[{speaker_id:'a',display_name:'Unknown student'},{speaker_id:'t',display_name:'Teacher'}]}});
 await storage.put({'job:unmatched':{noteId:'fictional-note-123',status:'pending',nextAt:0,tries:0}});
 await object.run();
 const job=await storage.get('job:unmatched');
 assert.equal(job.status,'needs_attention');assert.equal(job.lastError,'student_not_matched');
});


test('a first full lesson can create the initial assessment and quiz in an empty account', async () => {
  const initial = JSON.parse(JSON.stringify(draft).replaceAll(feedback.id, session));
  let calls = 0;
  const ai = { run: async (_model, input) => {
    assert.match(input.messages[0].content, /initial assessment/);
    return { response: ++calls % 2 ? structuredClone(initial) : { approved: true } };
  } };
  const result = await authorQuiz(ai, readTranscript(note, { ab26: student }), meeting, 'fictional-note-first', { assessment: null, attempts: [] });
  assert.equal(result.priorAssessment, null);
  assert.deepEqual(result.assessment.sourceSessions, [session]);
  const e = emptyEnv(), store = e.FEEDBACK_STORE.get('ab26');
  const response = await store.fetch(new Request('https://feedback.internal/automation/publish', { method: 'POST', body: JSON.stringify(result) }));
  assert.equal(response.status, 200);
  assert.equal((await store.storage.get('assessment:current')).quiz.generatedForSession, session);
  assert.equal((await store.storage.get('feedback:' + session)).source.reviewedFullTranscript, true);
});
