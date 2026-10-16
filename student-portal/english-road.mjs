import bank from './english-road-bank.json' with { type: 'json' };
import { handleRoadQuestions, roadChoice, roadQuestionId } from './road-questions.mjs';
import { ATTEMPT_ID } from './quiz-results.mjs';

const CURSOR = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z_[0-9a-f-]{36}$/;
const json = (data, status = 200) => Response.json(data, { status });
const conflict = () => json({ error: 'Your practice changed in another tab or device. Load it again to continue.' }, 409);
export const roadCatalog = { levels: bank.levels, topics: bank.topics, questionCount: bank.questions.length, version: bank.version };

function shuffle(items) {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const j = crypto.getRandomValues(new Uint32Array(1))[0] % (i + 1);
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}
function chooseQuestions(band, topic) {
  const pool = bank.questions.filter(q => q.band === band && (!topic || q.topic === topic));
  // A mixed set covers 25 distinct topics. A focused set uses its 20 authored items.
  const chosen = topic ? shuffle(pool) : shuffle(bank.topics).slice(0, 25).map(t => shuffle(pool.filter(q => q.topic === t))[0]);
  const positions = shuffle(chosen.map((_, i) => i % 4));
  return chosen.map((q, i) => {
    const order = shuffle([0, 1, 2, 3].filter(n => n !== q.correctIndex));
    order.splice(positions[i], 0, q.correctIndex);
    return { ...q, options: order.map(n => q.options[n]), feedback: order.map(n => q.feedback[n]), correctIndex: positions[i] };
  });
}
export function roadSummary(a) {
  return { id: a.id, band: a.band, topic: a.topic, startedAt: a.startedAt, updatedAt: a.updatedAt,
    completedAt: a.completedAt, endedAt: a.endedAt, total: a.questions.length, answered: a.answers.length,
    correct: a.answers.filter((answer, i) => answer.choiceIndex === a.questions[i].correctIndex).length };
}
async function studentAttempt(a, txn) {
  if (!a) return null;
  return { ...roadSummary(a), version: a.version, revision: a.revision, answers: a.answers,
    questions: await Promise.all(a.questions.map(async (q, i) => {
      const { correctIndex, explanation, feedback, ...visible } = q;
      visible.progress = await roadChoice(txn, roadQuestionId(a.id, i));
      return i < a.answers.length ? { ...visible, correctIndex, explanation, feedback } : visible;
    })) };
}
async function save(txn, a) {
  await txn.put({ [`road:attempt:${a.id}`]: a, [`road:index:${a.startedAt}_${a.id}`]: roadSummary(a), 'road:active': a.id });
}
export async function handleRoad(storage, request) {
  const url = new URL(request.url), route = url.pathname;
  if (route === '/road/questions') return handleRoadQuestions(storage, request);
  if (route === '/road/state' && request.method === 'GET') return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    const id = await txn.get('road:active');
    return json({ catalog: roadCatalog, attempt: await studentAttempt(id ? await txn.get(`road:attempt:${id}`) : null, txn) });
  });
  if (route === '/road/results' && request.method === 'GET') {
    const before = url.searchParams.get('before');
    if (before && !CURSOR.test(before)) return json({ error: 'Invalid page.' }, 400);
    const entries = [...await storage.list({ prefix: 'road:index:', reverse: true, limit: 21, ...(before ? { end: 'road:index:' + before } : {}) })];
    return json({ attempts: entries.slice(0, 20).map(([, a]) => a), nextCursor: entries.length > 20 ? entries[19][0].slice('road:index:'.length) : null });
  }
  if (route.startsWith('/road/results/') && request.method === 'GET') {
    const id = route.slice('/road/results/'.length);
    if (!ATTEMPT_ID.test(id)) return json({ error: 'Practice not found.' }, 404);
    const attempt = await storage.get('road:attempt:' + id);
    return attempt ? json({ attempt }) : json({ error: 'Practice not found.' }, 404);
  }
  if (!['/road/start', '/road/answer', '/road/end'].includes(route) || request.method !== 'POST') return json({ error: 'Page not found.' }, 404);
  let input;
  try { input = await request.json(); } catch { return json({ error: 'Please check your choice.' }, 400); }
  if (!input || !ATTEMPT_ID.test(input.attemptId)) return json({ error: 'Invalid practice request.' }, 400);
  return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    const activeId = await txn.get('road:active') || null;
    const active = activeId ? await txn.get('road:attempt:' + activeId) : null;
    if (route === '/road/start') {
      if (!bank.levels.includes(input.band) || typeof input.topic !== 'string' || input.topic && !bank.topics.includes(input.topic) ||
          input.previousAttemptId !== null && !ATTEMPT_ID.test(input.previousAttemptId)) return json({ error: 'Choose a practice band and topic.' }, 400);
      if (activeId === input.attemptId) {
        if (active.band !== input.band || active.topic !== input.topic) return conflict();
        return json({ attempt: await studentAttempt(active, txn) }); // A lost response must not start another set.
      }
      if (input.previousAttemptId !== activeId || active && !active.completedAt && !active.endedAt || await txn.get('road:attempt:' + input.attemptId)) return conflict();
      const now = new Date().toISOString();
      const attempt = { id: input.attemptId, band: input.band, topic: input.topic, version: bank.version,
        sourceCommit: bank.sourceCommit, startedAt: now, updatedAt: now, completedAt: null, endedAt: null,
        revision: 0, questions: chooseQuestions(input.band, input.topic), answers: [] };
      await save(txn, attempt);
      return json({ attempt: await studentAttempt(attempt, txn) }, 201);
    }
    if (!active || active.id !== input.attemptId) return conflict();
    if (route === '/road/end') {
      if (active.completedAt || active.endedAt) return json({ attempt: await studentAttempt(active, txn) });
      if (input.revision !== active.revision) return conflict();
      active.endedAt = active.updatedAt = new Date().toISOString(); active.revision++;
    } else {
      const { questionIndex, choiceIndex } = input;
      if (!Number.isInteger(questionIndex) || questionIndex < 0 || questionIndex >= active.questions.length ||
          !Number.isInteger(choiceIndex) || choiceIndex < 0 || choiceIndex > 3) return json({ error: 'Choose an answer.' }, 400);
      if (active.answers[questionIndex]) return active.answers[questionIndex].choiceIndex === choiceIndex
        ? json({ attempt: await studentAttempt(active, txn) }) : conflict();
      if (active.completedAt || active.endedAt || questionIndex !== active.answers.length) return conflict();
      const now = new Date().toISOString();
      active.answers.push({ choiceIndex, answeredAt: now }); active.updatedAt = now; active.revision++;
      if (active.answers.length === active.questions.length) active.completedAt = now;
    }
    await save(txn, active);
    return json({ attempt: await studentAttempt(active, txn) });
  });
}
