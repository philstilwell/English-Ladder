import test from 'node:test';
import assert from 'node:assert/strict';
import { env, call, login, origin } from './harness.mjs';
import bank from '../english-road-bank.json' with { type: 'json' };
import { createHash } from 'node:crypto';

const get = (e, cookie, path = '/api/road/state', host = origin) => call(e, path, { headers: { Cookie: cookie } }, host);
const post = (e, cookie, action, body, host = origin) => call(e, '/api/road/' + action,
  { method: 'POST', headers: { Cookie: cookie, Origin: host, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }, host);
const startInput = (previousAttemptId = null, topic = 'Articles') => ({ attemptId: crypto.randomUUID(), previousAttemptId, band: 'A1', topic });
async function start(e, cookie, input = startInput()) { const response = await post(e, cookie, 'start', input); assert.equal(response.status, 201); return (await response.json()).attempt; }
const privateAttempt = (e, id) => e.FEEDBACK_STORE.get('ab26').storage.get('road:attempt:' + id);
const history = (e, path = '/road/results') => e.FEEDBACK_STORE.get('ab26').fetch(new Request('https://feedback.internal' + path));
const flag = (e, cookie, body, host = origin) => call(e, '/api/road/questions', { method: 'PATCH', headers: { Cookie: cookie, Origin: host, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }, host);

test('Road Questions preserves attempts, hides unanswered keys, survives new sets and supports safe revisioned undo', async () => {
  const e = env(), student = await login(e), a = await start(e, student.cookie), original = await privateAttempt(e, a.id);
  const input = { attemptId: a.id, questionIndex: 0, value: true, revision: 0 };
  let response = await flag(e, student.cookie, input); assert.equal(response.status, 200);
  const entry = (await response.json()).entry; assert.equal(entry.question, true); assert.equal(entry.revision, 1);
  assert.deepEqual(await privateAttempt(e, a.id), original);
  assert.deepEqual((await (await flag(e, student.cookie, input)).json()).entry, entry);
  let list = await (await get(e, student.cookie, '/api/road/questions')).json();
  assert.equal(list.questions.length, 1); assert.equal(list.questions[0].exercise.prompt, a.questions[0].prompt);
  assert.equal(list.questions[0].exercise.correctIndex, undefined); assert.equal(list.questions[0].exercise.feedback, undefined); assert.equal(list.questions[0].exercise.explanation, undefined);
  assert.equal((await (await get(e, student.cookie)).json()).attempt.questions[0].progress.question, true);
  await post(e, student.cookie, 'answer', { attemptId: a.id, questionIndex: 0, choiceIndex: 0 });
  await post(e, student.cookie, 'end', { attemptId: a.id, revision: 1 });
  const ended = await privateAttempt(e, a.id), next = await start(e, student.cookie, startInput(a.id));
  list = await (await get(e, student.cookie, '/api/road/questions')).json();
  assert.deepEqual(list.questions[0].exercise, original.questions[0]); assert.equal(list.questions[0].answer.choiceIndex, 0);
  assert.equal((await flag(e, student.cookie, { ...input, value: false })).status, 409);
  assert.equal((await flag(e, student.cookie, { ...input, value: false, revision: 1 })).status, 200);
  assert.equal((await flag(e, student.cookie, input)).status, 409);
  assert.deepEqual((await (await get(e, student.cookie, '/api/road/questions')).json()).questions, []);
  assert.equal((await flag(e, student.cookie, { ...input, revision: 2 })).status, 200);
  assert.deepEqual(await privateAttempt(e, a.id), ended); assert.equal((await (await get(e, student.cookie)).json()).attempt.id, next.id);
  const totals = await (await get(e, student.cookie, '/api/activities/progress')).json(); assert.equal(totals.activities[0].questions, 1);
});

test('Road Questions enforces authentication, account isolation, teacher read-only access, input checks and deletion', async () => {
  const e = env(), student = await login(e), teacher = await login(e, 'teacher-test'), a = await start(e, student.cookie);
  const input = { attemptId: a.id, questionIndex: 0, value: true, revision: 0 };
  assert.equal((await call(e, '/api/road/questions')).status, 401);
  assert.equal((await flag(e, teacher.cookie, input)).status, 403);
  assert.equal((await get(e, teacher.cookie, '/api/road/questions')).status, 200);
  const other = await login(e, 'other-test', 'https://cd26.englishladder.com');
  assert.equal((await flag(e, other.cookie, input, 'https://cd26.englishladder.com')).status, 404);
  assert.equal((await get(e, student.cookie, '/api/road/questions', 'https://cd26.englishladder.com')).status, 401);
  for (const method of ['GET', 'PATCH']) assert.equal((await call(e, '/api/road/questions', { method, headers: { Cookie: student.cookie, Origin: 'https://evil.test' }, ...(method === 'PATCH' ? { body: JSON.stringify(input) } : {}) })).status, 403);
  for (const change of [{ questionIndex: -1 }, { questionIndex: 25 }, { value: 'yes' }, { revision: -1 }, { exercise: { prompt: 'Forged' } }]) assert.equal((await flag(e, student.cookie, { ...input, ...change })).status, 400);
  assert.equal((await flag(e, student.cookie, { ...input, questionIndex: 2 })).status, 404);
  assert.equal((await get(e, student.cookie, '/api/road/questions?after=bad')).status, 400);
  assert.equal((await get(e, student.cookie, '/api/road/questions?id=bad')).status, 400);
  await flag(e, student.cookie, input);
  assert.equal((await (await get(e, teacher.cookie, '/api/road/questions')).json()).questions.length, 1);
  assert.equal((await (await get(e, other.cookie, '/api/road/questions', 'https://cd26.englishladder.com')).json()).questions.length, 0);
  const store = e.FEEDBACK_STORE.get('ab26'); await store.fetch(new Request('https://feedback.internal/admin/delete-account', { method: 'POST' }));
  assert.equal((await store.storage.list({ prefix: 'road:' })).size, 0);
  assert.equal((await flag(e, student.cookie, input)).status, 410); assert.equal((await get(e, student.cookie, '/api/road/questions')).status, 410);
});

test('Road Questions lists use stable twenty-item pages and never write on reads', async () => {
  const e = env(), student = await login(e), a = await start(e, student.cookie, startInput(null, ''));
  for (let i = 0; i < 23; i++) {
    await flag(e, student.cookie, { attemptId: a.id, questionIndex: i, value: true, revision: 0 });
    await post(e, student.cookie, 'answer', { attemptId: a.id, questionIndex: i, choiceIndex: 0 });
  }
  const store = e.FEEDBACK_STORE.get('ab26'), before = await store.storage.list();
  const first = await (await get(e, student.cookie, '/api/road/questions')).json();
  const last = await (await get(e, student.cookie, '/api/road/questions?after=' + first.nextCursor)).json();
  assert.equal(first.questions.length, 20); assert.equal(last.questions.length, 3); assert.equal(last.nextCursor, null);
  assert.equal(new Set([...first.questions, ...last.questions].map(q => q.id)).size, 23);
  assert.deepEqual(await store.storage.list(), before);
});

test('reviewed snapshot is complete, consistent, unique and bounded for private attempt storage', () => {
  assert.equal(bank.questions.length, 4200); assert.equal(bank.topics.length, 35);
  assert.equal(new Set(bank.questions.map(q => q.id)).size, 4200);
  assert.equal(createHash('sha256').update(JSON.stringify(bank.questions)).digest('hex'), bank.version);
  for (const band of bank.levels) for (const topic of bank.topics) assert.equal(bank.questions.filter(q => q.band === band && q.topic === topic).length, 20);
  for (const q of bank.questions) {
    assert.equal(q.options.length, 4); assert.equal(new Set(q.options).size, 4); assert(q.correctIndex >= 0 && q.correctIndex <= 3);
    assert.equal(q.feedback.length, 4); assert(q.feedback.every(s => typeof s === 'string' && s.length));
    assert(Buffer.byteLength(JSON.stringify(q)) * 25 + 15000 < 128 * 1024);
  }
});

test('practice requires student authentication, host isolation, exact origins and bounded writes', async () => {
  const e = env(), student = await login(e), teacher = await login(e, 'teacher-test');
  for (const action of ['state', 'start', 'answer', 'end']) assert.equal((await call(e, '/api/road/' + action)).status, 401);
  assert.equal((await get(e, teacher.cookie)).status, 403);
  assert.equal((await post(e, teacher.cookie, 'start', startInput())).status, 403);
  assert.equal((await get(e, student.cookie, '/api/road/state', 'https://cd26.englishladder.com')).status, 401);
  for (const Origin of ['https://evil.test', 'https://cd26.englishladder.com', '']) assert.equal((await call(e, '/api/road/start', { method: 'POST', headers: { Cookie: student.cookie, Origin, 'Content-Type': 'application/json' }, body: JSON.stringify(startInput()) })).status, 403);
  assert.equal((await post(e, student.cookie, 'start', { ...startInput(), extra: 'x'.repeat(2000) })).status, 400);
  for (const change of [{ band: 'C3' }, { topic: 'unknown' }, { previousAttemptId: 'bad' }, { attemptId: 'bad' }]) assert.equal((await post(e, student.cookie, 'start', { ...startInput(), ...change })).status, 400);
  assert.equal((await get(e, student.cookie, '/api/road/results')).status, 404);
  assert.equal((await get(e, teacher.cookie, '/api/road/results')).status, 404);
  assert.equal((await get(e, student.cookie, '/english-road-bank.json')).status, 404);
  e.PRACTICE_LIMITER = { limit: async () => ({ success: false }) };
  assert.equal((await post(e, student.cookie, 'start', startInput())).status, 429);
  delete e.FEEDBACK_STORE; assert.equal((await get(e, student.cookie)).status, 503);
});

test('sets save immediately, resume on another login, and hide unanswered explanations', async () => {
  const e = env(), student = await login(e), input = startInput(null, ''), a = await start(e, student.cookie, input);
  assert.equal(a.total, 25); assert.equal(new Set(a.questions.map(q => q.topic)).size, 25);
  assert.equal(new Set(a.questions.map(q => q.id)).size, 25);
  assert(a.questions.every(q => !('correctIndex' in q) && !('feedback' in q) && !('explanation' in q)));
  const saved = await privateAttempt(e, a.id);
  const counts = [0, 0, 0, 0]; for (const q of saved.questions) counts[q.correctIndex]++; assert(Math.max(...counts) - Math.min(...counts) <= 1);
  const retry = await post(e, student.cookie, 'start', input); assert.equal(retry.status, 200); assert.equal((await retry.json()).attempt.id, a.id);
  const otherLogin = await login(e); assert.deepEqual((await (await get(e, otherLogin.cookie)).json()).attempt, a);
  const other = await login(e, 'other-test', 'https://cd26.englishladder.com');
  assert.equal((await (await get(e, other.cookie, '/api/road/state', 'https://cd26.englishladder.com')).json()).attempt, null);
  assert.equal((await post(e, other.cookie, 'answer', { attemptId: a.id, questionIndex: 0, choiceIndex: 0 }, 'https://cd26.englishladder.com')).status, 409);
});

test('first choices are immutable, server-scored and safe under retries and competing tabs', async () => {
  const e = env(), student = await login(e);
  const inputs = [startInput(), startInput()];
  const starts = await Promise.all(inputs.map(i => post(e, student.cookie, 'start', i)));
  assert.deepEqual(starts.map(r => r.status).sort(), [201, 409]);
  const a = (await starts.find(r => r.status === 201).json()).attempt, saved = await privateAttempt(e, a.id);
  assert.equal(a.total, 20);
  const body = { attemptId: a.id, questionIndex: 0, choiceIndex: (saved.questions[0].correctIndex + 1) % 4 };
  assert.equal((await post(e, student.cookie, 'answer', { ...body, questionIndex: 1 })).status, 409);
  const results = await Promise.all([1, 2].map(() => post(e, student.cookie, 'answer', { ...body, correct: 99, studentId: 'cd26', answeredAt: '2000-01-01' })));
  assert(results.every(r => r.status === 200));
  let current = (await (await get(e, student.cookie)).json()).attempt;
  assert.equal(current.answers.length, 1); assert.equal(current.correct, 0); assert.equal(current.answers[0].choiceIndex, body.choiceIndex);
  assert(Date.parse(current.answers[0].answeredAt) > Date.parse('2000-01-01'));
  assert.equal(current.questions[0].correctIndex, saved.questions[0].correctIndex); assert.equal(current.questions[1].correctIndex, undefined);
  assert.equal((await post(e, student.cookie, 'answer', { ...body, choiceIndex: saved.questions[0].correctIndex })).status, 409);
  assert.equal((await post(e, student.cookie, 'start', startInput(a.id))).status, 409);
  for (let i = 1; i < 20; i++) assert.equal((await post(e, student.cookie, 'answer', { attemptId: a.id, questionIndex: i, choiceIndex: saved.questions[i].correctIndex })).status, 200);
  current = (await (await get(e, student.cookie)).json()).attempt;
  assert.equal(current.correct, 19); assert.equal(current.answered, 20); assert.ok(current.completedAt);
  const rows = (await (await history(e)).json()).attempts; assert.equal(rows[0].correct, 19); assert.ok(rows[0].completedAt);
  const next = await start(e, student.cookie, startInput(a.id));
  assert.notEqual(next.id, a.id);
  assert.deepEqual((await (await history(e, '/road/results/' + a.id)).json()).attempt.questions, saved.questions);
  assert.equal((await post(e, student.cookie, 'answer', body)).status, 409);
});

test('ending a set preserves partial results and stale end requests cannot discard later answers', async () => {
  const e = env(), student = await login(e), a = await start(e, student.cookie);
  await post(e, student.cookie, 'answer', { attemptId: a.id, questionIndex: 0, choiceIndex: 0 });
  assert.equal((await post(e, student.cookie, 'end', { attemptId: a.id, revision: 0 })).status, 409);
  const response = await post(e, student.cookie, 'end', { attemptId: a.id, revision: 1 });
  const ended = (await response.json()).attempt; assert.ok(ended.endedAt); assert.equal(ended.completedAt, null); assert.equal(ended.answered, 1);
  assert.equal((await post(e, student.cookie, 'answer', { attemptId: a.id, questionIndex: 1, choiceIndex: 0 })).status, 409);
  assert.equal((await post(e, student.cookie, 'end', { attemptId: a.id, revision: 1 })).status, 200);
  await start(e, student.cookie, startInput(a.id)); assert.equal((await (await history(e)).json()).attempts.length, 2);
});

test('private practice pagination is stable and account deletion removes all practice history', async () => {
  const e = env(), student = await login(e); let id = null;
  for (let i = 0; i < 23; i++) { const a = await start(e, student.cookie, startInput(id)); id = a.id; await post(e, student.cookie, 'end', { attemptId: id, revision: 0 }); }
  const first = await (await history(e)).json(), second = await (await history(e, '/road/results?before=' + first.nextCursor)).json();
  assert.equal(first.attempts.length, 20); assert.equal(second.attempts.length, 3); assert.equal(second.nextCursor, null);
  assert.equal(new Set([...first.attempts, ...second.attempts].map(a => a.id)).size, 23);
  assert.equal((await history(e, '/road/results?before=bad')).status, 400);
  assert.equal((await history(e, '/road/results/not-an-id')).status, 404);
  const store = e.FEEDBACK_STORE.get('ab26');
  await store.fetch(new Request('https://feedback.internal/admin/delete-account', { method: 'POST' }));
  assert.equal((await store.storage.list({ prefix: 'road:' })).size, 0);
  assert.equal((await post(e, student.cookie, 'start', startInput())).status, 410);
});
