import test from 'node:test';
import assert from 'node:assert/strict';
import worker from '../worker.mjs';
import { QuizAutomation, hash, nightlyDate, zoomSignatureValid } from '../server-quiz-automation.mjs';
import { readTranscript, authorQuiz, firstTryReview } from '../server-quiz-model.mjs';
import { seedQuiz, call, origin, env as emptyEnv } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
import { runDate, RECHECK_DELAY } from '../codex-nightly.mjs';

const student = { firstName: 'Alex', zoomNames: ['Alex0529'], timeZone: 'America/New_York', startAfter: '2026-10-14T00:00:00Z' };
const note = { transcript: { speakers: [{ speaker_id: 'a', display_name: 'Alex0529' }, { speaker_id: 't', display_name: 'Private Teacher Name' }],
  items: Array.from({ length: 10 }, (_, i) => ({ speaker_id: i % 2 ? 't' : 'a', start_time: '00:' + String(i + 1).padStart(2, '0') + ':00.000',
    end_time: '00:' + String(i + 1).padStart(2, '0') + ':30.000', text: 'We can practice English.' })) } };
const meeting = { start_time: '2026-10-15T00:57:01Z', end_time: '2026-10-15T02:00:00Z' };
const session = '2026-10-14-2057';
const draft = { sufficientEvidence: true, feedback, assessment: { ...assessment, plan: assessment.plan.map(item => ({ ...item, aiPrompt: 'Teach me how to use “can” in simple English. Explain it and give three examples. Ask five questions, one at a time. Wait for each answer and explain any mistake.' })), summary: 'You can use “can” in a short sentence.', progress: { detail: 'Keep using “can” in new sentences.', evidence: [{ sessionId: session, at: '00:02:00' }] } }, quiz: { ...quiz, patternTitles: ['Use “can”'],
  questions: Array.from({ length: 7 }, (_, i) => quiz.questions[i % quiz.questions.length]) },
  evidence: [0, 1, 2, 3, 4, 5, 6].map(questionIndex => ({ questionIndex, segments: [questionIndex], reviewRefs: [] })) };
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

test('administrator nightly diagnostics show bounded safe failure details without source or credential contents', async () => {
  const { object, storage } = coordinator();
  await storage.put({ oauth: { access_token: 'private-token' }, ['job:' + 'a'.repeat(64)]: {
    studentId: 'ab26', noteId: 'private-note', meetingId: 'private-meeting', transcript: 'private-transcript',
    status: 'needs_attention', lastError: 'transcript_privacy_failed', tries: 1, startedAt: '2026-10-15T20:00:00Z',
  }, ['job:' + 'b'.repeat(64)]: { status: 'pending', lastError: 'private-provider-error', tries: 2 } });
  const status = await (await object.fetch(new Request('https://automation.internal/admin-status'))).json();
  assert.equal(status.problems[0].error, 'transcript_privacy_failed');
  assert.equal(status.problems[0].studentId, 'ab26'); assert.equal(status.problems[0].attempts, 1);
  assert.equal(status.problems[1].error, 'generation_failed');
  assert.doesNotMatch(JSON.stringify(status), /private-token|private-note|private-meeting|private-transcript|private-provider-error/);
});

test('manual retry is one job, locked against concurrent runs, and still enforces the existing cost limit', async () => {
  const { object, storage } = coordinator(), id = 'a'.repeat(64), key = 'job:' + id;
  await storage.put({ [key]: { noteId: 'fictional-note-123', studentId: 'ab26', status: 'needs_attention', lastError: 'transcript_privacy_failed', tries: 1 } });
  let finish, calls = 0;
  object.process = async (_key, job) => { calls++; await new Promise(resolve => { finish = resolve; }); job.status = 'published'; job.sessionId = '2026-10-15-2200'; job.lastError = null; };
  const pending = object.retry(id);
  while (!finish) await new Promise(resolve => setTimeout(resolve, 0));
  assert.equal((await object.retry(id)).status, 409); assert.equal(calls, 1);
  finish(); assert.equal((await (await pending).json()).ok, true);
  assert.equal((await (await object.retry(id)).json()).ok, true); assert.equal(calls, 1);
  assert.equal(await storage.get('run-lock'), undefined);
  await storage.put({ [key]: { noteId: 'fictional-note-123', studentId: 'ab26', status: 'needs_attention', tries: 1 } });
  await object.reserveGeneration('ab26'); await object.reserveGeneration('ab26');
  object.process = () => object.reserveGeneration('ab26');
  const limited = await (await object.retry(id)).json(); assert.equal(limited.ok, false); assert.equal(limited.errorCode, 'daily_limit');
  assert.equal((await storage.get(key)).tries, 1); assert.equal(await storage.get('run-lock'), undefined);
  assert.equal((await object.retry('bad')).status, 400);
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

test('AI authoring requires valid evidence and a second approval; no full transcript is saved in output', async () => {
  const transcript = readTranscript(note, { ab26: student }); let calls = 0;
  const ai = { run: async (_model, input) => {
    calls++; assert.ok(JSON.parse(input.input[1].content).segments.length === 10);
    return { response: calls === 1 ? structuredClone(draft) : { approved: true } };
  } };
  const output = await authorQuiz(ai, transcript, meeting, 'fictional-note-123', { assessment, attempts: [] });
  assert.equal(calls, 2); assert.equal(output.quiz.generatedForSession, session);
  assert.equal(output.quiz.questions.length, 7);
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
  env.AI = { run: async (_model, input) => {
    calls++;
    const rules = input.input[0].content;
    assert.doesNotMatch(rules, /You anonymize|independent privacy reviewer/);
    const response = rules.includes('You anonymize') ? (rules.includes('independent privacy reviewer') ? { approved: true } : { redactions: [] }) : (rules.includes('independent editor') ? { approved: true } : structuredClone(draft));
    return { status: 'completed', output: [{ type: 'reasoning', content: [] }, { type: 'message', role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: JSON.stringify(response) }] }] };
  } };
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
    assert.match(input.input[0].content, /initial assessment/);
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

test('new quiz authoring rejects any question count other than seven before editorial review', async () => {
  const transcript = readTranscript(note, { ab26: student });
  for (const count of [4, 6, 8]) {
    const invalid = structuredClone(draft);
    invalid.quiz.questions = Array.from({ length: count }, (_, i) => draft.quiz.questions[i % 7]);
    invalid.evidence = Array.from({ length: count }, (_, questionIndex) => ({ questionIndex, segments: [0], reviewRefs: [] }));
    let calls = 0;
    await assert.rejects(authorQuiz({ run: async () => { calls++; return { response: invalid }; } }, transcript, meeting, 'fictional-note-123', { assessment, attempts: [] }), /invalid_evidence/);
    assert.equal(calls, 1);
  }
});

test('automatic assessments require a self-study AI prompt for every study topic',async()=>{
 const transcript=readTranscript(note,{ab26:student}),missing=structuredClone(draft);
 delete missing.assessment.plan[0].aiPrompt;
 await assert.rejects(authorQuiz({run:async()=>({response:missing})},transcript,meeting,'fictional-note-123',{assessment,attempts:[]}),/invalid_evidence/);
});


test('daily lesson authoring omits CEFR inputs and cannot overwrite the monthly estimate',async()=>{
  const transcript=readTranscript(note,{ab26:student});let calls=0;
  const ai={run:async(_model,input)=>{
    calls++;const data=JSON.parse(input.input[1].content);
    assert.equal(data.priorCefr,undefined);assert.equal(data.sessions,undefined);
    return{response:calls===1?{...structuredClone(draft),cefr:{state:'estimated',lower:'C2'}}:{approved:true}};
  }};
  const result=await authorQuiz(ai,transcript,meeting,'fictional-note-123',{assessment,attempts:[],cefr:{state:'estimated',lower:'B1'}});
  assert.equal(calls,2);assert.equal(result.cefr,undefined);
});

test('CEFR labels accidentally placed in student content are rejected before publication',async()=>{
  const transcript=readTranscript(note,{ab26:student});
  const ai={run:async()=>({response:{...structuredClone(draft),assessment:{...draft.assessment,summary:'Your CEFR level is B1.'}}})};
  await assert.rejects(authorQuiz(ai,transcript,meeting,'fictional-note-123',{assessment,attempts:[]}),/unsafe_content/);
});

test('lesson retries use basic removal without privacy AI or saving unreviewed transcript text', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const seed = await seedQuiz(), { object, storage, env } = coordinator(seed.e);
  const job = { noteId: 'fictional-note-cache', meetingId: 'meeting-123', nextAt: 0, status: 'pending', tries: 0 };
  let downloads = 0, privacyCalls = 0, authorCalls = 0, rejectAuthor = true;
  object.zoom = async path => { downloads++; return path.includes('past_meetings') ? meeting : note; };
  env.AI.run = async (_model, input) => {
    const rules = input.input[0].content, data = JSON.parse(input.input[1].content);
    assert.ok(data.segments.every(s => ['student', 'other'].includes(s.role)));
    if (!rules.includes('You anonymize')) assert.ok(data.segments.every(s => ['Student', 'Speaker 1'].includes(s.speaker)));
    assert.doesNotMatch(input.input[1].content, /Private Teacher Name|Alex0529/);
    if (rules.includes('You anonymize')) {
      privacyCalls++; return { response: rules.includes('independent privacy reviewer') ? { approved: true } : { redactions: [] } };
    }
    authorCalls++;
    if (rejectAuthor) throw new Error('mock author unavailable');
    return { response: rules.includes('independent editor') ? { approved: true } : structuredClone(draft) };
  };
  await assert.rejects(object.process('job:cache', job), error => error.message === 'invalid_model_response' && error.modelIssue === 'provider_error');
  assert.equal(downloads, 2); assert.equal(privacyCalls, 0); assert.equal(authorCalls, 1);
  const storedJob = await storage.get('job:cache'); assert.equal(storedJob.studentId, 'ab26');
  assert.equal((await object.portal('ab26', '/automation/transcript/' + job.noteId)).transcript, null);
  rejectAuthor = false;
  await object.process('job:cache', storedJob);
  assert.equal(downloads, 4); assert.equal(privacyCalls, 0); assert.equal(authorCalls, 3); assert.equal(storedJob.status, 'published');
});

test('changed source revisions are downloaded and never saved as privacy-reviewed text', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const seed = await seedQuiz(), { object, storage, env } = coordinator(seed.e);
  const job = { noteId: 'fictional-note-cache', meetingId: 'meeting-123', nextAt: 0, status: 'pending', tries: 0 };
  let downloads = 0, privacyCalls = 0, currentNote = note;
  object.zoom = async path => { downloads++; return path.includes('past_meetings') ? meeting : currentNote; };
  env.AI.run = async (_model, input) => {
    const rules = input.input[0].content;
    if (!rules.includes('You anonymize')) throw new Error('mock author unavailable');
    privacyCalls++; return { response: rules.includes('independent privacy reviewer') ? { approved: true } : { redactions: [] } };
  };
  await assert.rejects(object.process('job:cache', job), error => error.message === 'invalid_model_response' && error.modelIssue === 'provider_error');
  currentNote = structuredClone(note); currentNote.transcript.items[0].text = 'Now I can use a different word.';
  job.modifiedAt = '2026-10-16T10:00:00Z';
  await storage.put({ 'job:cache': job });
  await assert.rejects(object.process('job:cache', job), error => error.message === 'invalid_model_response' && error.modelIssue === 'provider_error');
  assert.equal(downloads, 4); assert.equal(privacyCalls, 0);
  assert.equal((await object.portal('ab26', '/automation/transcript/' + job.noteId)).transcript, null);
});

test('editor rejection and exhausted budgets cannot save raw text or publish learner pages', async t => {
  t.mock.timers.enable({ apis: ['Date'], now: new Date('2026-10-16T12:00:00Z') });
  const seed = await seedQuiz(), { object, storage, env } = coordinator(seed.e);
  object.zoom = async path => path.includes('past_meetings') ? meeting : note;
  const job = { noteId: 'fictional-note-cache', meetingId: 'meeting-123', nextAt: 0, status: 'pending', tries: 0 };
  let calls = 0;
  env.AI.run = async () => ({ response: ++calls === 1 ? structuredClone(draft) : { approved: false } });
  await assert.rejects(object.process('job:cache', job), /content_review_failed/);
  assert.equal(calls, 2);
  assert.equal((await seed.e.FEEDBACK_STORE.get('ab26').storage.list({ prefix: 'transcript:' })).size, 0);
  await storage.put({ 'usage:ab26': { day: '2026-10-16', month: '2026-10', daily: 2, monthly: 2 } });
  await assert.rejects(object.process('job:cache', job), /daily_limit/);
  assert.equal(calls, 2);
  assert.equal((await seed.e.FEEDBACK_STORE.get('ab26').storage.get('assessment:current')).summary, assessment.summary);
});

test('new notifications during processing are preserved and block publication from an outdated source', async () => {
  const { object, storage } = coordinator();
  const original = { noteId: 'fictional-note-cache', meetingId: 'meeting-123', sourceEventAt: 1000, status: 'pending', tries: 1, nextAt: 1000 };
  await storage.put({ 'job:cache': { ...original, sourceEventAt: 2000 } });
  await assert.rejects(object.checkSource('job:cache', original), /source_changed/);
  await object.saveJob('job:cache', original);
  assert.equal((await storage.get('job:cache')).sourceEventAt, 2000);
  assert.equal((await storage.get('job:cache')).nextAt, 0);
});

test('retention runs with publishing disabled or Zoom disconnected and reports cleanup failures', async () => {
  const { object, storage, env } = coordinator(emptyEnv()); let cleaned = [], zoomCalls = 0;
  const stores = env.FEEDBACK_STORE;
  env.FEEDBACK_STORE = { ...stores, get(id) { const store = stores.get(id); return { fetch(request) { if (new URL(request.url).pathname === '/automation/prune-transcripts') cleaned.push(id); return store.fetch(request); } }; } };
  env.AUTOMATION_ENABLED = 'false'; object.accessToken = async () => { zoomCalls++; throw Error('zoom_reconnect'); };
  await object.run();
  assert.deepEqual(cleaned.sort(), ['ab26', 'cd26']); assert.equal(zoomCalls, 0); assert.ok(await storage.get('last-retention'));
  env.AUTOMATION_ENABLED = 'true'; cleaned = []; await object.run();
  assert.deepEqual(cleaned.sort(), ['ab26', 'cd26']); assert.equal(zoomCalls, 1);
  env.FEEDBACK_STORE.get = () => ({ fetch: async () => new Response('', { status: 503 }) });
  await object.run();
  const status = await (await object.fetch(new Request('https://automation.internal/admin-status'))).json();
  assert.equal(status.retentionError, 'transcript_retention_failed');
  let dispatched = 0;
  await worker.scheduled({ scheduledTime: Date.parse('2026-10-16T05:00:00Z') }, { AUTOMATION_ENABLED: 'false', QUIZ_AUTOMATION: { idFromName: id => id, get: () => ({ fetch: async () => { dispatched++; return Response.json({ ok: true }); } }) } });
  assert.equal(dispatched, 1);
});


test('an approved recovery grant permits only one extra attempt for one job on one UTC day',async()=>{
  const {object,storage,env}=coordinator(),id='a'.repeat(64),day=new Date().toISOString().slice(0,10);
  await object.reserveGeneration('ab26');await object.reserveGeneration('ab26');
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day:'2000-01-01'});
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day});
  await assert.rejects(object.reserveGeneration('ab26','lesson','b'.repeat(64)),/daily_limit/);
  await object.reserveGeneration('ab26','lesson',id);
  assert.equal((await storage.get('usage:ab26')).daily,3);assert.equal((await storage.get('usage:ab26')).monthly,3);
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  await storage.put({'usage:ab26':{day,month:day.slice(0,7),daily:2,monthly:12}});
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/monthly_limit/);
  delete env.LESSON_RECOVERY_GRANT;
});


test('ignoring an unmatched session preserves its source, survives duplicate events, and never generates content',async()=>{
  const {object,storage,env}=coordinator(),id=await hash(event.payload.object.note_id),key='job:'+id;
  await storage.put({oauth:{userId:'owner-1',accountId:'account-1'},[key]:{noteId:event.payload.object.note_id,meetingId:'meeting-123',status:'needs_attention',lastError:'student_not_matched',tries:0}});
  const ignore=()=>object.fetch(new Request('https://automation.internal/ignore',{method:'POST',body:JSON.stringify({id})}));
  await storage.put({'run-lock':{until:Date.now()+10000}});assert.equal((await ignore()).status,409);await storage.delete('run-lock');
  assert.equal((await ignore()).status,200);assert.equal((await ignore()).status,200);
  assert.equal((await storage.get(key)).noteId,event.payload.object.note_id);
  await object.webhook(await signedRequest(event));assert.equal((await storage.get(key)).status,'ignored');
  object.discover=async()=>{};object.accessToken=async()=>{};object.reviewCefr=async()=>{};
  object.process=async()=>assert.fail('Ignored sessions must never generate');await object.run();
  assert.equal((await storage.get(key)).status,'ignored');
  const status=await(await object.fetch(new Request('https://automation.internal/admin-status'))).json();assert.equal(status.needsAttention,0);assert.equal(status.problems.length,0);
});


test('a later recovery requires a new explicit attempt number and cannot skip or repeat reservations',async()=>{
  const {object,storage,env}=coordinator(),id='b'.repeat(64),day=new Date().toISOString().slice(0,10);
  await storage.put({'usage:ab26':{day,month:day.slice(0,7),daily:3,monthly:3}});
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day});await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day,attempt:5});await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day,attempt:4});await object.reserveGeneration('ab26','lesson',id);
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  assert.equal((await storage.get('usage:ab26')).daily,4);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day,attempt:6});await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  for (const attempt of [5,6]) {
    env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day,attempt});
    await object.reserveGeneration('ab26','lesson',id);
    await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
  }
  assert.equal((await storage.get('usage:ab26')).daily,6);
  assert.equal((await storage.get('usage:ab26')).monthly,6);
  env.LESSON_RECOVERY_GRANT=JSON.stringify({jobId:id,day,attempt:13});
  await assert.rejects(object.reserveGeneration('ab26','lesson',id),/daily_limit/);
});

test('one-time server recovery waits without AI, publishes only its job after reset, and ignores duplicate alarms', async t => {
  t.mock.timers.enable({apis:['Date'],now:new Date('2026-10-16T13:00:00Z')});
  const seed=await seedQuiz(),{object,storage,env}=coordinator(seed.e),id='c'.repeat(64),key='job:'+id;
  const at='2026-10-17T00:05:00Z';
  const job={studentId:'ab26',noteId:'fictional-note-recovery',meetingId:'meeting-123',status:'needs_attention',tries:7,lastError:'invalid_model_response'};
  await storage.put({[key]:job,'job:unrelated':{...job,noteId:'fictional-other-note',status:'pending',nextAt:0}});
  env.LESSON_RECOVERY_SCHEDULE=JSON.stringify({jobId:id,at});
  object.zoom=async path=>path.includes('past_meetings')?meeting:note;
  let calls=0;env.AI.run=async(_model,input)=>{calls++;assert.doesNotMatch(input.input[0].content,/You anonymize/);return {response:input.input[0].content.includes('independent editor')?{approved:true}:structuredClone(draft)}};
  const queued=await(await object.retry(id)).json();assert.equal(Date.parse(queued.recoveryAt),Date.parse(at));assert.equal(calls,0);
  assert.equal(storage.alarmAt,Date.parse(at));assert.equal((await storage.get(key)).tries,7);
  await object.alarm();assert.equal(calls,0);assert.equal((await storage.get('recovery-once')).status,'queued');
  delete env.LESSON_RECOVERY_SCHEDULE;
  t.mock.timers.setTime(Date.parse(at));await object.alarm();
  assert.equal(calls,2);assert.equal((await storage.get(key)).status,'published');
  assert.equal((await storage.get('job:unrelated')).status,'pending');
  assert.equal((await storage.get('recovery-once')).published,true);
  assert.equal((await storage.get('usage:ab26')).daily,1);
  assert.equal((await seed.e.FEEDBACK_STORE.get('ab26').storage.list({prefix:'transcript:'})).size,0);
  await object.alarm();assert.equal(calls,2);
});

test('one-time recovery respects a busy lease and cannot generate for a paused account',async t=>{
  t.mock.timers.enable({apis:['Date'],now:new Date('2026-10-17T00:05:00Z')});
  const {object,storage,env}=coordinator(),id='d'.repeat(64),at=Date.now();
  await storage.put({'recovery-once':{id,at,status:'queued'},['job:'+id]:{studentId:'ab26',status:'pending',nextAt:at},'run-lock':{until:at+10000}});
  object.process=()=>assert.fail('Must not generate');
  await object.alarm();assert.equal(storage.alarmAt,at+60000);assert.equal((await storage.get('recovery-once')).status,'queued');
  await storage.delete('run-lock');env.QUIZ_STUDENTS='{}';
  await object.alarm();assert.equal((await storage.get('recovery-once')).published,false);
  assert.equal((await storage.get('recovery-once')).status,'finished');
});

test('free-account AI quota exhaustion stops later jobs and monthly work but keeps the job pending',async()=>{
  const {object,storage}=coordinator(),key='job:'+ 'e'.repeat(64);
  await storage.put({[key]:{studentId:'ab26',status:'pending',nextAt:0,tries:7},'job:other':{studentId:'ab26',status:'pending',nextAt:0,tries:0}});
  object.pruneTranscripts=async()=>{};object.accessToken=async()=>{};object.discover=async()=>{};
  let calls=0;object.process=async()=>{calls++;throw Object.assign(Error('invalid_model_response'),{modelIssue:'provider_quota',modelStage:'lesson_author'})};
  object.reviewCefr=()=>assert.fail('Do not spend another request after account quota failure');
  await object.run();assert.equal(calls,1);assert.equal((await storage.get(key)).status,'pending');
  assert.equal((await storage.get(key)).modelIssue,'provider_quota');
  assert.equal((await storage.get('job:other')).tries,0);
});

// Codex never receives a server transcript or calls a Worker AI binding.
async function codexFixture() {
  const base = emptyEnv(), c = coordinator(base);
  c.env.LESSON_PROCESSOR = 'codex'; c.env.AUTOMATION_ENABLED = 'false';
  c.env.AI = { run() { throw Error('Unexpected Cloudflare AI call'); } };
  c.storage.deleteAlarm = async () => { c.storage.alarmAt = null; };
  c.object.zoom = async path => path.startsWith('/my_notes/') ? structuredClone(note) : structuredClone(meeting);
  const id = await hash('fictional-note-123');
  await c.storage.put({ ['job:' + id]: { noteId: 'fictional-note-123', meetingId: 'meeting-123', status: 'pending', tries: 7 },
    'recovery-once': { id, at: Date.now()+10000, status: 'queued' } });
  const dispatch = (action, body = {}) => c.object.fetch(new Request('https://automation.internal/codex/' + action, { method: 'POST', body: JSON.stringify(body) }));
  const p = await (await dispatch('prepare', { id })).json();
  const f = { ...feedback, id: session, startedAt: meeting.start_time, source: { ...feedback.source, noteId:'fictional-note-123', coverageStart:'00:01:00', coverageEnd:'00:10:30', segmentCount:10 } };
  const q = { ...draft.quiz, sourceSessions:[session], generatedForSession:session };
  const a = { ...draft.assessment, sourceSessions:[session], quiz:q,
    strengths:assessment.strengths.map(s=>({...s,evidence:s.evidence.map(e=>({...e,sessionId:session}))})),
    patterns:assessment.patterns.map(p=>({...p,examples:p.examples.map(e=>({...e,sessionId:session}))})) };
  const records={feedback:[f],assessment:a,quizzes:[{quiz:q,evidence:q.questions.map((_,i)=>({questionIndex:i,references:[{sessionId:session,at:'00:03:00'}]}))}]};
  const {digest}=await import('../codex-handoff.mjs');
  const payload=async value=>({id,snapshotHash:p.snapshotHash,records:value,review:{approved:true,fullTranscript:true,independent:true,recordsHash:await digest(value)}});
  return {...c,id,p,records,dispatch,payload};
}

test('Codex handoff publishes an exact reviewed bundle, verifies it, cancels recovery and safely repeats', async()=>{
  const {object,storage,id,p,records,dispatch,payload}=await codexFixture();
  assert.equal(p.source.segmentCount,10);assert.deepEqual(p.speakerRoles.learnerIds,['a']);
  assert.doesNotMatch(JSON.stringify(p),/We can practice English|test-secret|test-client/);
  assert.equal((await storage.get('recovery-once')).status,'cancelled');
  const result=await dispatch('publish',await payload(records));
  assert.equal(result.status,200);assert.equal((await result.json()).verified,true);
  assert.equal((await storage.get('job:'+id)).publisher,'codex');
  assert.equal((await (await dispatch('publish',await payload(records))).json()).duplicate,true);
  assert.equal(await storage.get('usage:lesson:ab26'),undefined);
});

test('nightly readiness waits fifteen minutes and permits only one recheck across restart and midnight', async()=>{
  const {storage,env,id,dispatch,object}=await codexFixture();
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:50:00Z'),reads=0;
  Date.now=()=>now;
  try {
    const pendingMeeting={...meeting,end_time:new Date(now-60000).toISOString()};
    object.zoom=async path=>{reads++;return path.startsWith('/my_notes/')?note:pendingMeeting;};
    const first=await (await dispatch('nightly-prepare',{id})).json();
    assert.equal(first.waiting,true);assert.equal(Date.parse(first.retryAt),now+RECHECK_DELAY);assert.equal(reads,2);
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).waiting,true);assert.equal(reads,2);
    now+=RECHECK_DELAY;
    const resumed=new QuizAutomation({storage},env);resumed.zoom=object.zoom;
    const again=()=>resumed.fetch(new Request('https://automation.internal/codex/nightly-prepare',{method:'POST',body:JSON.stringify({id})}));
    assert.ok((await (await again()).json()).snapshotHash);assert.equal(reads,4);
    assert.equal((await (await again()).json()).deferred,true);assert.equal(reads,4);
    assert.equal((await storage.get('job:'+id)).codexCheck.checks,2);
  } finally { Date.now=originalNow; }
});

test('empty transcripts get one recheck, then wait for a Zoom change; ordinary failures do not retry', async()=>{
  const {storage,id,dispatch,object}=await codexFixture();
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:35:00Z'),reads=0;
  Date.now=()=>now;
  try {
    object.zoom=async()=>{reads++;return {transcript:{speakers:note.transcript.speakers,items:[]}};};
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).waiting,true);
    now+=RECHECK_DELAY;
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);assert.equal(reads,2);
    now+=86400000;
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);assert.equal(reads,2);
    await storage.put({['job:'+id]:{...await storage.get('job:'+id),sourceEventAt:now-3600000}});
    object.zoom=async()=>{reads++;throw Error('zoom_reconnect');};
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).error,'zoom_reconnect');
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);assert.equal(reads,3);
  } finally { Date.now=originalNow; }
});

test('partial Zoom discovery recovers meeting details and publishes on the one nightly recheck', async()=>{
  const {object,storage,env,id,dispatch,records,payload}=await codexFixture();
  await storage.delete('job:'+id);
  await storage.put({oauth:{userId:'owner',pmi:1234567890}});
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:50:00Z'),failed=true,searches=0,sourceReads=0;
  Date.now=()=>now;
  const zoom=async path=>{
    if(path==='/docs/file_search'){searches++;return {files:searches===1?[{file_id:'fictional-note-123'}]:[]};}
    if(path.startsWith('/users/me/meetings?')){if(failed)throw Error('zoom_unavailable');return {meetings:[]};}
    if(path.endsWith('/instances'))return {meetings:[{uuid:'meeting-123',start_time:meeting.start_time}]};
    if(path.startsWith('/my_notes/notes?'))return {notes:[{note_id:'fictional-note-123',modified_time:meeting.end_time}]};
    if(path.includes('/content?')){sourceReads++;return structuredClone(note);}
    if(path==='/past_meetings/meeting-123')return structuredClone(meeting);
    throw Error('Unexpected path: '+path);
  };
  try {
    object.zoom=zoom;object.accessToken=async()=>{};object.pruneTranscripts=async()=>{};
    assert.equal((await (await dispatch('nightly-discover')).json()).error,'zoom_unavailable');
    assert.equal(await storage.get('discovery-since'),undefined);
    const queue=await (await dispatch('queue')).json();
    assert.equal(queue.jobs.length,1);assert.equal(queue.discovery.checks,1);
    const first=await (await dispatch('nightly-prepare',{id})).json();
    assert.equal(first.error,'meeting_reference_missing');assert.equal(first.waiting,true);
    assert.equal(first.retryAt,queue.discovery.recheckAt);
    assert.equal((await storage.get('job:'+id)).status,'pending');
    now+=RECHECK_DELAY-1;
    assert.equal((await (await dispatch('nightly-prepare',{id})).json()).waiting,true);assert.equal(sourceReads,1);
    now++;failed=false;
    const resumed=new QuizAutomation({storage},env);resumed.zoom=zoom;resumed.accessToken=async()=>{};resumed.pruneTranscripts=async()=>{};
    const again=(action,body={})=>resumed.fetch(new Request('https://automation.internal/codex/'+action,{method:'POST',body:JSON.stringify(body)}));
    const recovered=await (await again('nightly-discover')).json();
    assert.equal(recovered.discovery.checks,2);assert.equal(recovered.jobs[0].startedAt,meeting.start_time);
    assert.equal(recovered.jobs[0].waiting,false);
    assert.equal((await storage.get('job:'+id)).codexCheck.checks,1);
    const p=await (await again('nightly-prepare',{id})).json();assert.ok(p.snapshotHash);assert.equal(sourceReads,2);
    assert.equal((await (await again('nightly-prepare',{id})).json()).deferred,true);assert.equal(sourceReads,2);
    const published=await (await again('publish',{...await payload(records),snapshotHash:p.snapshotHash})).json();
    assert.equal(published.verified,true);assert.equal(published.questions,7);assert.equal(published.preservedAttempts,0);
    assert.equal((await (await again('prepare',{id})).json()).duplicate,true);
    await again('nightly-discover');assert.equal(searches,2);
    assert.equal(await storage.get('usage:lesson:ab26'),undefined);
  } finally {Date.now=originalNow;}
});

test('temporary Zoom preparation failures get one recheck but reconnect and matching failures do not',async()=>{
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:50:00Z');Date.now=()=>now;
  try {
    for(const failure of ['zoom_unavailable','meeting_reference_missing']){
      const {object,storage,env,id,dispatch}=await codexFixture();let reads=0;
      object.zoom=async()=>{reads++;throw Error(failure);};
      assert.equal((await (await dispatch('nightly-prepare',{id})).json()).waiting,true);
      now+=RECHECK_DELAY;
      assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);assert.equal(reads,2);
      // A later metadata update and process restart cannot grant a third check.
      await storage.put({['job:'+id]:{...await storage.get('job:'+id),status:'pending',modifiedAt:meeting.end_time,meetingId:'recovered-meeting'}});
      const resumed=new QuizAutomation({storage},env);resumed.zoom=()=>assert.fail('Third readiness attempt');
      const result=await resumed.fetch(new Request('https://automation.internal/codex/nightly-prepare',{method:'POST',body:JSON.stringify({id})}));
      assert.equal((await result.json()).deferred,true);assert.equal((await storage.get('job:'+id)).codexCheck.checks,2);
    }
    for(const failure of ['zoom_reconnect','other_student','ambiguous_student','transcript_too_large']){
      const {object,id,dispatch}=await codexFixture();let reads=0;
      object.zoom=async()=>{reads++;throw Error(failure);};
      assert.equal((await dispatch('nightly-prepare',{id})).status,409);
      now+=RECHECK_DELAY;
      assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);assert.equal(reads,1);
    }
  } finally {Date.now=originalNow;}
});

test('a temporary Zoom meeting fetch failure can prepare and publish after recovery',async()=>{
  const {object,id,dispatch,records,payload}=await codexFixture();
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:50:00Z'),unavailable=true;Date.now=()=>now;
  object.zoom=async path=>{if(path.startsWith('/my_notes/'))return note;if(unavailable)throw Error('zoom_unavailable');return meeting;};
  try {
    const first=await (await dispatch('nightly-prepare',{id})).json();assert.equal(first.waiting,true);assert.equal(first.error,'zoom_unavailable');
    now+=RECHECK_DELAY;unavailable=false;
    const p=await (await dispatch('nightly-prepare',{id})).json();assert.ok(p.snapshotHash);
    assert.equal((await (await dispatch('publish',{...await payload(records),snapshotHash:p.snapshotHash})).json()).verified,true);
  } finally {Date.now=originalNow;}
});

test('completed-meeting lookup recovers old unresolved status without resetting readiness reservations',async()=>{
  const {object,storage,id,dispatch}=await codexFixture();
  const check={runDate:runDate(),checks:2,sourceVersion:'old',retryAt:null};
  await storage.put({oauth:{userId:'owner',pmi:1234567890},['job:'+id]:{noteId:'fictional-note-123',status:'needs_attention',lastError:'meeting_reference_missing',codexCheck:check}});
  object.zoom=async path=>{
    if(path==='/docs/file_search')return {files:[]};
    if(path.startsWith('/users/me/meetings?'))return {meetings:[]};
    if(path.endsWith('/instances'))return {meetings:[{uuid:'meeting-123',start_time:meeting.start_time}]};
    if(path.startsWith('/my_notes/notes?'))return {notes:[{note_id:'fictional-note-123',modified_time:meeting.end_time}]};
    throw Error('Unexpected source fetch');
  };
  await object.discover();
  const job=await storage.get('job:'+id);assert.equal(job.status,'pending');assert.deepEqual(job.codexCheck,check);
  assert.equal((await (await dispatch('nightly-prepare',{id})).json()).deferred,true);
});

test('nightly run dates follow New York wall-clock time through midnight and daylight saving',()=>{
  for(const [instant,date] of [['2026-10-17T03:35:00Z','2026-10-16'],['2026-10-17T04:05:00Z','2026-10-16'],['2026-11-01T05:55:00Z','2026-10-31'],['2026-11-01T06:05:00Z','2026-10-31'],['2026-11-02T04:35:00Z','2026-11-01']]) assert.equal(runDate(Date.parse(instant)),date);
});

test('nightly discovery allows one follow-up even with an empty first queue and survives restart',async()=>{
  const {object,storage,env,dispatch,id}=await codexFixture();await storage.delete('job:'+id);
  const originalNow=Date.now;let now=Date.parse('2026-10-17T03:50:00Z'),searches=0;Date.now=()=>now;
  try {
    object.pruneTranscripts=async()=>{};object.accessToken=async()=>{};object.discover=async()=>{searches++;};
    const first=await (await dispatch('nightly-discover')).json();assert.equal(first.jobs.length,0);assert.equal(first.discovery.checks,1);
    assert.equal(Date.parse(first.discovery.recheckAt),now+RECHECK_DELAY);await dispatch('nightly-discover');assert.equal(searches,1);
    now+=RECHECK_DELAY;
    const resumed=new QuizAutomation({storage},env);resumed.pruneTranscripts=object.pruneTranscripts;resumed.accessToken=object.accessToken;
    resumed.discover=async()=>{searches++;await storage.put({['job:'+id]:{noteId:'fictional-note-123',status:'pending'}});};
    const again=()=>resumed.fetch(new Request('https://automation.internal/codex/nightly-discover',{method:'POST',body:'{}'}));
    const second=await (await again()).json();assert.equal(second.discovery.checks,2);assert.equal(second.discovery.recheckAt,null);assert.equal(second.jobs.length,1);
    await again();assert.equal(searches,2);
  } finally { Date.now=originalNow; }
});

test('pre-activation warnings identify the exact lesson, remain administrator-only, and clear after approved publication',async()=>{
  const {storage,env,id,records,dispatch,payload,object}=await codexFixture();
  const config=JSON.parse(env.QUIZ_STUDENTS);config.ab26.startAfter='2026-10-15T03:00:00Z';env.QUIZ_STUDENTS=JSON.stringify(config);
  const result=await (await dispatch('nightly-prepare',{id})).json();assert.equal(result.approvalRequired,true);
  const status=()=>object.fetch(new Request('https://automation.internal/admin-status')).then(r=>r.json());
  assert.deepEqual((await status()).catchUpRequired,[{id,studentId:'ab26',startedAt:meeting.start_time}]);
  assert.equal((await (await dispatch('queue')).json()).jobs.length,0);
  const studentStatus=await (await object.fetch(new Request('https://automation.internal/status',{headers:{'X-Student-ID':'ab26'}}))).json();
  assert.equal(studentStatus.catchUpRequired,undefined);
  assert.equal(await env.FEEDBACK_STORE.get('ab26').storage.get('feedback:'+session),undefined);
  env.QUIZ_STUDENTS='{}';assert.deepEqual((await status()).catchUpRequired,[]);env.QUIZ_STUDENTS=JSON.stringify(config);
  const job=await storage.get('job:'+id);await storage.put({['job:'+id]:{...job,status:'ignored'}});assert.deepEqual((await status()).catchUpRequired,[]);await storage.put({['job:'+id]:job});
  const catchUp={studentId:'ab26',noteId:job.noteId,startedAt:meeting.start_time};
  assert.equal((await (await dispatch('nightly-prepare',{id,catchUp})).json()).error,'invalid_catch_up');
  const p=await (await dispatch('prepare',{id,catchUp})).json();
  assert.equal((await (await dispatch('publish',{...await payload(records),snapshotHash:p.snapshotHash,catchUp})).json()).verified,true);
  assert.deepEqual((await status()).catchUpRequired,[]);assert.equal(JSON.parse(env.QUIZ_STUDENTS).ab26.startAfter,config.ab26.startAfter);
});

test('Codex discovery looks back one day for activation warnings without opening older history',async()=>{
  const {object,storage,env}=coordinator();env.LESSON_PROCESSOR='codex';env.AUTOMATION_ENABLED='false';
  env.QUIZ_STUDENTS=JSON.stringify({ab26:{...student,startAfter:'2026-10-15T03:00:00Z'}});
  await storage.put({oauth:{userId:'owner',pmi:1234567890}});const lookedUp=[];
  object.zoom=async(path,_token,body)=>{
    if(path==='/docs/file_search'){assert.equal(body.modified_time_from,'2026-10-14T03:00:00.000Z');return {files:[]};}
    if(path.startsWith('/users/me/meetings?'))return {meetings:[]};
    if(path.endsWith('/instances'))return {meetings:[{uuid:'recent',start_time:meeting.start_time},{uuid:'old',start_time:'2026-10-13T00:00:00Z'}]};
    if(path.startsWith('/my_notes/notes?')){lookedUp.push(path);return {notes:[{note_id:'fictional-note-123',modified_time:meeting.end_time}]};}
    throw Error('Unexpected lookup');
  };
  await object.discover();assert.equal(lookedUp.length,1);assert.match(lookedUp[0],/recent/);
  assert.equal((await storage.list({prefix:'job:'})).size,1);
});

test('Codex rejects changed, unreviewed and wrongly grounded results before saving', async()=>{
  const {id,p,records,dispatch,payload,env}=await codexFixture();
  const body=await payload(records);body.records.feedback[0].summary='Changed after review.';
  assert.equal((await (await dispatch('publish',body)).json()).error,'reviewed_content_changed');
  const unreviewed=await payload(records);unreviewed.review.independent=false;
  assert.equal((await (await dispatch('publish',unreviewed)).json()).error,'content_review_failed');
  const bad=structuredClone(records);bad.feedback[0].focus[0].at='00:03:01';
  assert.equal((await (await dispatch('publish',await payload(bad))).json()).error,'invalid_evidence');
  const stale=await payload(records);stale.snapshotHash='f'.repeat(64);
  assert.equal((await (await dispatch('publish',stale)).json()).error,'source_or_history_changed');
  const store=env.FEEDBACK_STORE.get('ab26');
  assert.equal(await store.storage.get('feedback:'+session),undefined);
});

test('Codex never restores ignored or inactive students and rejects a changed source', async()=>{
  const {storage,env,id,p,records,dispatch,payload,object}=await codexFixture();
  await storage.put({['job:'+id]:{...await storage.get('job:'+id),status:'ignored'}});
  assert.equal((await (await dispatch('prepare',{id})).json()).error,'job_unavailable');
  await storage.put({['job:'+id]:{...await storage.get('job:'+id),status:'pending'}});
  const config=env.QUIZ_STUDENTS;env.QUIZ_STUDENTS='{}';
  assert.equal((await (await dispatch('prepare',{id})).json()).error,'student_changed');
  env.QUIZ_STUDENTS=config;
  const changed=structuredClone(note);changed.transcript.items[0].text='A new source revision.';
  object.zoom=async path=>path.startsWith('/my_notes/')?changed:meeting;
  assert.equal((await (await dispatch('publish',await payload(records))).json()).error,'source_or_history_changed');
});

test('Codex handoff requires its narrow credential on the administrator host, never a browser session', async()=>{
  const e=emptyEnv();e.LESSON_PROCESSOR='codex';e.AUTOMATION_ENABLED='false';e.CODEX_HANDOFF_SECRET='a'.repeat(64);
  let calls=0;e.QUIZ_AUTOMATION={idFromName:x=>x,get:()=>({fetch:async()=>{calls++;return Response.json({ok:true});}})};
  const options={method:'POST',headers:{Authorization:'Bearer '+'a'.repeat(64),'Content-Type':'application/json'},body:'{}'};
  const admin='https://phil.englishladder.com';
  assert.equal((await call(e,'/api/codex/queue',{...options,headers:{'Content-Type':'application/json'}},admin)).status,401);
  assert.equal((await call(e,'/api/codex/queue',{...options,headers:{...options.headers,Authorization:'Bearer '+'b'.repeat(64)}},admin)).status,401);
  assert.equal((await call(e,'/api/codex/queue',{...options,headers:{...options.headers,Origin:admin}},admin)).status,401);
  assert.equal((await call(e,'/api/codex/queue',options,origin)).status,404);
  assert.equal((await call(e,'/api/codex/queue',options,admin)).status,200);assert.equal(calls,1);
  for(const route of ['nightly-prepare','nightly-discover']) {
    assert.equal((await call(e,'/api/codex/'+route,options,origin)).status,404);
    assert.equal((await call(e,'/api/codex/'+route,{...options,headers:{...options.headers,Origin:admin}},admin)).status,401);
    assert.equal((await call(e,'/api/codex/'+route,options,admin)).status,200);
  }
  assert.equal((await call(e,'/api/codex/delete-account',options,admin)).status,404);
  e.LESSON_PROCESSOR='cloudflare';assert.equal((await call(e,'/api/codex/queue',options,admin)).status,401);
});


test('explicit single-lesson catch-up preserves activation cutoff and cannot include ignored or mismatched sources', async()=>{
  const {storage,env,id,records,dispatch,payload}=await codexFixture();
  const config=JSON.parse(env.QUIZ_STUDENTS);config.ab26.startAfter='2026-10-16T00:00:00Z';env.QUIZ_STUDENTS=JSON.stringify(config);
  assert.equal((await (await dispatch('prepare',{id})).json()).skipped,true);
  const catchUp={studentId:'ab26',noteId:'fictional-note-123',startedAt:meeting.start_time};
  assert.equal((await (await dispatch('prepare',{id,catchUp:{...catchUp,noteId:'different-note-123'}})).json()).error,'invalid_catch_up');
  assert.equal((await (await dispatch('prepare',{id,catchUp:{...catchUp,startedAt:'2026-10-13T00:00:00Z'}})).json()).error,'invalid_catch_up');
  assert.equal((await (await dispatch('prepare',{id,catchUp:{...catchUp,studentId:'other'}})).json()).error,'student_changed');
  await storage.put({['job:'+id]:{...await storage.get('job:'+id),status:'ignored'}});
  assert.equal((await (await dispatch('prepare',{id,catchUp})).json()).error,'job_unavailable');
  await storage.put({['job:'+id]:{...await storage.get('job:'+id),status:'skipped'}});
  const p=await (await dispatch('prepare',{id,catchUp})).json();
  assert.deepEqual(p.catchUp,catchUp);assert.ok(p.snapshotHash);
  const body={...await payload(records),snapshotHash:p.snapshotHash,catchUp};
  const result=await dispatch('publish',body);assert.equal(result.status,200);assert.equal((await result.json()).verified,true);
  assert.equal(JSON.parse(env.QUIZ_STUDENTS).ab26.startAfter,'2026-10-16T00:00:00Z');
  assert.equal((await (await dispatch('prepare',{id})).json()).duplicate,true);
  const other=await hash('another-fictional-note');
  await storage.put({['job:'+other]:{noteId:'another-fictional-note',meetingId:'meeting-123',status:'pending'}});
  assert.equal((await (await dispatch('prepare',{id:other,catchUp})).json()).error,'invalid_catch_up');
});
