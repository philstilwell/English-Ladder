import test from 'node:test';
import assert from 'node:assert/strict';
import { collectQuizContext, publishQuiz } from '../quiz-workflow.mjs';
import { seedQuiz, call, origin } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';

const lesson = { ...feedback, id: '2026-10-15-2057', startedAt: '2026-10-16T00:57:01Z' };
const nextQuiz = {
  ...quiz, title: 'Practice from your new lesson',
  sourceSessions: [lesson.id], patternTitles: ['Use “can”', 'Use “want to”'],
  generatedForSession: lesson.id,
  questions: quiz.questions.map((q, i) => ({ ...q, patternIndex: i })),
};
const apiFor = (e, cookie) => async (path, method = 'GET', body) => {
  const response = await call(e, path, {
    method, headers: { Cookie: cookie, Origin: origin, 'Content-Type': 'application/json' },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
  if (!response.ok) throw new Error('HTTP ' + response.status);
  return response.json();
};

test('new lesson quizzes keep the earlier assessment and require private reviewed sources', async () => {
  const { e, teacher, student, publish } = await seedQuiz();
  const teacherApi = apiFor(e, teacher.cookie), studentApi = apiFor(e, student.cookie);
  await assert.rejects(publishQuiz(teacherApi, nextQuiz), /400/);
  await publish('/api/feedback/' + lesson.id, lesson);
  assert.equal((await publishQuiz(teacherApi, nextQuiz)).published, true);
  const saved = (await teacherApi('/api/assessment')).assessment;
  assert.deepEqual({ ...saved, quiz: undefined }, { ...assessment, quiz: undefined });
  assert.deepEqual(saved.quiz, nextQuiz);
  const current = await studentApi('/api/quiz/state');
  assert.deepEqual(current.sourceSessions, [lesson.id]);
  assert.deepEqual(current.patternTitles, nextQuiz.patternTitles);
  assert.equal((await publishQuiz(teacherApi, { ...nextQuiz, title: 'Duplicate' })).published, false);
  assert.equal((await teacherApi('/api/assessment')).assessment.quiz.title, nextQuiz.title);
  for (const invalid of [
    { sourceSessions: [] }, { sourceSessions: [lesson.id, lesson.id] },
    { generatedForSession: feedback.id }, { patternTitles: [] },
    { patternTitles: ['One topic'] },
  ]) {
    assert.equal((await publish('/api/assessment', { ...assessment, quiz: { ...nextQuiz, ...invalid } })).status, 400);
  }
});

test('completed attempts yield to a new quiz while old answers and lesson references stay intact', async () => {
  const { e, teacher, student, state, publish } = await seedQuiz();
  const studentApi = apiFor(e, student.cookie), teacherApi = apiFor(e, teacher.cookie);
  const attemptId = crypto.randomUUID();
  const answer = (questionIndex, choiceIndex) => studentApi('/api/quiz/answer', 'POST', { attemptId, version: state.version, questionIndex, choiceIndex });
  await answer(0, 1);
  await publish('/api/feedback/' + lesson.id, lesson);
  await publishQuiz(teacherApi, nextQuiz);
  assert.equal((await studentApi('/api/quiz/state')).attempt.id, attemptId);
  await answer(0, 0); await answer(1, 1);
  const fresh = await studentApi('/api/quiz/state');
  assert.equal(fresh.attempt, null);
  assert.equal(fresh.quiz.title, nextQuiz.title);
  const context = await collectQuizContext(teacherApi);
  assert.equal(context.history.length, 1);
  assert.deepEqual(context.history[0].attempt.sourceSessions, assessment.sourceSessions);
  assert.deepEqual(context.history[0].firstTryMistakes.map(m => [m.questionNumber, m.firstChoice, m.correctChoice]), [
    [1, quiz.questions[0].options[1].text, quiz.questions[0].options[0].text],
  ]);
  assert.equal(context.sessions.length, 2);
});

test('context export reads every history page, including first-try mistakes in unfinished attempts', async () => {
  const { e, teacher, student, state } = await seedQuiz();
  const studentApi = apiFor(e, student.cookie), teacherApi = apiFor(e, teacher.cookie);
  for (let i = 0; i < 22; i++) {
    const attemptId = crypto.randomUUID();
    const answer = (questionIndex, choiceIndex) => studentApi('/api/quiz/answer', 'POST', { attemptId, version: state.version, questionIndex, choiceIndex });
    await answer(0, 1);
    if (i < 21) { await answer(0, 0); await answer(1, 1); }
  }
  const context = await collectQuizContext(teacherApi);
  assert.equal(context.history.length, 22);
  assert.ok(context.history.every(h => h.firstTryMistakes.length === 1));
  assert.equal(context.history.filter(h => !h.attempt.completedAt).length, 1);
  assert.ok(context.history.every(h => !h.firstTryMistakes.some(m => m.questionNumber === 2)));
});
