import test from 'node:test';
import assert from 'node:assert/strict';
import { validateFeedback, validateFeedbackPractice } from '../feedback.mjs';
import { feedback } from './fixture.mjs';
import { env, call, login, origin, seedQuiz } from './harness.mjs';

const fresh = [{ prompt: 'New practice. Fix: “Can guests access to the map?”', answer: 'Can guests access the map?' }];
const headers = cookie => ({ Cookie: cookie, Origin: origin, 'Content-Type': 'application/json' });
const read = async (e, cookie) => (await call(e, '/api/feedback/' + feedback.id, { headers: headers(cookie) })).json();
const patch = (e, cookie, body, extra = {}, host = origin, path = '/api/feedback/' + feedback.id) => call(e, path, {
  method: 'PATCH', headers: headers(cookie), body: JSON.stringify(body), ...extra,
}, host);

test('practice rejects copied models, vocabulary examples and embedded sentences, allowing new uses of target phrases', () => {
  const record = { ...feedback, vocabulary: [{ ...feedback.vocabulary[0], example: 'They have access to the garden.' }] };
  for (const answer of ['I can access the file.', "'I can access the file.'", '“I CAN access the file!”', 'For example: I can access the file. Then I can read it.', 'They have access to the garden.']) {
    assert.throws(() => validateFeedback({ ...record, practice: [{ prompt: 'Complete the gap.', answer }] }, record.id), /new example/);
  }
  assert.throws(() => validateFeedbackPractice([{ prompt: 'Change this: “I can access the file.”', answer: 'Can I access the file?' }], record), /new example/);
  assert.throws(() => validateFeedbackPractice([{ prompt: 'Complete: “I can ___ the file.”', answer: 'access' }], record), /new example/);
  assert.throws(() => validateFeedbackPractice([{ prompt: 'Complete: “They have access to the …”', answer: 'garden' }], record), /new example/);
  assert.throws(() => validateFeedbackPractice([{ prompt: 'Make a sentence.', answer: 'We arrived early.' }], { focus: [{ model: 'We arrived early. We left late.' }] }), /new example/);
  assert.throws(() => validateFeedbackPractice([{ prompt: 'Write the words.', answer: 'one hundred and five' }], { focus: [{ model: 'one hundred and five' }] }), /new example/);
  assert.deepEqual(validateFeedbackPractice(fresh, record), fresh);
  assert.doesNotThrow(() => validateFeedbackPractice([{ prompt: 'Complete: “It is a ___ bus ride.”', answer: 'It is a twelve-minute bus ride.' }], { focus: [{ model: 'It is a three-minute walk.' }] }));
  assert.deepEqual(validateFeedbackPractice([{ prompt: 'Fill the gap: “Guests have ___ to the pool.”', answer: 'access' }], record)[0].answer, 'access');
});

test('practice repairs enforce teacher, origin, account, route and input restrictions', async () => {
  const e = env(), teacher = await login(e, 'teacher-test'), student = await login(e);
  await call(e, '/api/feedback/' + feedback.id, { method: 'PUT', headers: headers(teacher.cookie), body: JSON.stringify(feedback) });
  const input = { practice: fresh, priorFeedback: await read(e, teacher.cookie) };
  assert.equal((await patch(e, '', input)).status, 401);
  assert.equal((await patch(e, student.cookie, input)).status, 403);
  assert.equal((await patch(e, teacher.cookie, input, { headers: { ...headers(teacher.cookie), Origin: 'https://evil.test' } })).status, 403);
  const otherHost = 'https://cd26.englishladder.com', other = await login(e, 'teacher-test', otherHost);
  assert.equal((await patch(e, teacher.cookie, input, {}, otherHost)).status, 401);
  assert.equal((await patch(e, other.cookie, input, { headers: { ...headers(other.cookie), Origin: otherHost } }, otherHost)).status, 404);
  for (const path of ['/api/assessment', '/api/feedback']) assert.equal((await patch(e, teacher.cookie, input, {}, origin, path)).status, 405);
  assert.equal((await patch(e, teacher.cookie, input, {}, origin, '/api/feedback/admin/delete-account')).status, 404);
  for (const bad of [null, { practice: fresh }, { ...input, title: 'Overwrite title' }, { ...input, practice: [] }, { ...input, practice: [{ prompt: 'x'.repeat(65536), answer: 'x' }] }]) {
    assert.equal((await patch(e, teacher.cookie, bad)).status, 400);
  }
  assert.equal((await patch(e, teacher.cookie, { ...input, practice: [{ prompt: 'Fill the gap.', answer: feedback.focus[0].model }] })).status, 400);
  assert.deepEqual(await read(e, teacher.cookie), input.priorFeedback);
});

test('practice repair archives old exercises and preserves all other records including real first choices', async () => {
  const { e, teacher, student, state } = await seedQuiz();
  await call(e, '/api/quiz/answer', { method: 'POST', headers: headers(student.cookie), body: JSON.stringify({ attemptId: crypto.randomUUID(), version: state.version, questionIndex: 0, choiceIndex: 1 }) });
  const storage = e.FEEDBACK_STORE.get('ab26').storage;
  const before = await storage.list({ limit: 1000 });
  const input = { practice: fresh, priorFeedback: await read(e, teacher.cookie) };
  const response = await patch(e, teacher.cookie, input);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get('Cache-Control'), 'no-store');
  const after = await storage.list({ limit: 1000 });
  for (const [key, value] of before) assert.deepEqual(after.get(key), key === 'feedback:' + feedback.id ? { ...value, practice: fresh } : value);
  const backups = [...after].filter(([key]) => key.startsWith('practice:before:'));
  assert.equal(backups.length, 1); assert.deepEqual(backups[0][1], feedback.practice);
  const visible = await read(e, student.cookie);
  assert.deepEqual(visible, { ...input.priorFeedback, practice: fresh });
  assert.equal(visible.source.noteId, undefined);
  assert.equal((await patch(e, teacher.cookie, input)).status, 409);
});

test('competing practice edits cannot overwrite each other or a changed teaching note', async () => {
  const { e, teacher } = await seedQuiz();
  const input = { practice: fresh, priorFeedback: await read(e, teacher.cookie) };
  const results = await Promise.all([patch(e, teacher.cookie, input), patch(e, teacher.cookie, input)]);
  assert.deepEqual(results.map(r => r.status).sort(), [200, 409]);
  const latest = await read(e, teacher.cookie);
  const storage = e.FEEDBACK_STORE.get('ab26').storage;
  await storage.put({ ['feedback:' + feedback.id]: { ...await storage.get('feedback:' + feedback.id), summary: 'A newer teaching note.' } });
  assert.equal((await patch(e, teacher.cookie, { practice: feedback.practice, priorFeedback: latest })).status, 409);
  await storage.put({ 'account:deleted': true });
  assert.equal((await patch(e, teacher.cookie, { practice: fresh, priorFeedback: latest })).status, 410);
});
