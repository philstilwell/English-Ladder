import { ATTEMPT_ID } from './quiz-results.mjs';

export const ROAD_QUESTION_ID = /^[0-9a-f-]{36}_\d{2}$/;
export const roadQuestionId = (attemptId, index) => attemptId + '_' + String(index).padStart(2, '0');
const empty = id => ({ id, question: false, revision: 0, updatedAt: null });
export const roadQuestionProgress = entry => ({ id: entry.id, question: entry.question, revision: entry.revision, updatedAt: entry.updatedAt });
export async function roadChoice(storage, id) {
  return roadQuestionProgress(await storage.get('road:item:' + id) || empty(id));
}
// The snapshot comes only from the saved attempt, never from browser input or a
// newer question bank. The attempt controls when its answer key is released.
export async function roadQuestionItem(storage, entry) {
  const attempt = await storage.get('road:attempt:' + entry.attemptId);
  const answer = attempt?.answers[entry.questionIndex];
  const { correctIndex, explanation, feedback, ...exercise } = entry.exercise;
  return { id: entry.id, attemptId: entry.attemptId, questionIndex: entry.questionIndex,
    startedAt: entry.startedAt, band: entry.band, topic: entry.topic,
    exercise: answer ? { ...exercise, correctIndex, explanation, feedback } : exercise,
    answer: answer || null, progress: roadQuestionProgress(entry) };
}
export async function handleRoadQuestions(storage, request) {
  const url = new URL(request.url), id = url.searchParams.get('id'), after = url.searchParams.get('after');
  if (request.method === 'GET') {
    if ([id, after].some(value => value !== null && !ROAD_QUESTION_ID.test(value)) || id && after)
      return Response.json({ error: 'Please check the page.' }, { status: 400 });
    return storage.transaction(async txn => {
      if (await txn.get('account:deleted')) return Response.json({ error: 'This account was deleted.' }, { status: 410 });
      if (id) return Response.json({ entry: await roadChoice(txn, id) });
      const rows = [...(await txn.list({ prefix: 'road:question:', limit: 21, ...(after ? { startAfter: 'road:question:' + after } : {}) })).values()];
      return Response.json({ questions: await Promise.all(rows.slice(0, 20).map(entry => roadQuestionItem(txn, entry))),
        nextCursor: rows.length > 20 ? rows[19].id : null });
    });
  }
  if (request.method !== 'PATCH') return Response.json({ error: 'Method not allowed.' }, { status: 405 });
  let input;
  try { input = await request.json(); } catch { /* Validated below. */ }
  if (!input || !ATTEMPT_ID.test(input.attemptId) || !Number.isInteger(input.questionIndex) || input.questionIndex < 0 || input.questionIndex > 24 ||
      typeof input.value !== 'boolean' || !Number.isSafeInteger(input.revision) || input.revision < 0 ||
      Object.keys(input).some(key => !['attemptId', 'questionIndex', 'value', 'revision'].includes(key)))
    return Response.json({ error: 'Please check your choice.' }, { status: 400 });
  return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return Response.json({ error: 'This account was deleted.' }, { status: 410 });
    const attempt = await txn.get('road:attempt:' + input.attemptId), question = attempt?.questions[input.questionIndex];
    if (!question || input.questionIndex > attempt.answers.length)
      return Response.json({ error: 'Open this practice question first.' }, { status: 404 });
    const id = roadQuestionId(input.attemptId, input.questionIndex), key = 'road:item:' + id;
    const entry = await txn.get(key) || { ...empty(id), attemptId: attempt.id, questionIndex: input.questionIndex,
      startedAt: attempt.startedAt, band: attempt.band, topic: question.topic, exercise: question };
    if (entry.question === input.value) return Response.json({ entry: roadQuestionProgress(entry) });
    if (entry.revision !== input.revision) return Response.json({ error: 'This choice changed on another page. Load it again before changing it.' }, { status: 409 });
    const updated = { ...entry, question: input.value, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
    await txn.put({ [key]: updated });
    if (updated.question) await txn.put({ ['road:question:' + id]: updated });
    else await txn.delete('road:question:' + id);
    return Response.json({ entry: roadQuestionProgress(updated) });
  });
}
