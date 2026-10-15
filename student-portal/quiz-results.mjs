// Private practice history. The server owns timestamps, scoring, and the first
// answer; a retry can add a choice but can never replace an earlier choice.
export const ATTEMPT_ID = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
const VERSION = /^[0-9a-f]{64}$/;
const CURSOR = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z_[0-9a-f-]{36}$/;
const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json' } });
const conflict = () => json({ error: 'Your saved quiz has changed. Load it again to continue.' }, 409);

async function currentQuiz(storage) {
  const assessment = await storage.get('assessment:current');
  if (!assessment?.quiz) return null;
  const quiz = assessment.quiz, patternTitles = assessment.patterns.map(p => p.title), sourceSessions = assessment.sourceSessions;
  const bytes = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(JSON.stringify({ quiz, patternTitles, sourceSessions })));
  const version = Array.from(new Uint8Array(bytes), byte => byte.toString(16).padStart(2, '0')).join('');
  return { version, quiz, patternTitles, sourceSessions };
}

export function attemptSummary(attempt) {
  const { id, version, startedAt, updatedAt, completedAt, quiz, answers } = attempt;
  return {
    id, version, title: quiz.title, startedAt, updatedAt, completedAt,
    total: quiz.questions.length, answered: answers.filter(a => a.length).length,
    firstTryCorrect: answers.filter((a, i) => a[0] === quiz.questions[i].correctIndex).length,
    missedQuestions: answers.flatMap((a, i) => a.length && a[0] !== quiz.questions[i].correctIndex ? [i + 1] : []),
  };
}

export async function handleQuiz(storage, request) {
  const url = new URL(request.url), route = url.pathname;
  if (route === '/quiz/state' && request.method === 'GET') {
    const activeId = await storage.get('quiz:active');
    const attempt = activeId ? await storage.get(`quiz:attempt:${activeId}`) : null;
    // An unfinished attempt keeps its original questions even if the teacher
    // publishes a new quiz. A new attempt uses the current assessment.
    if (attempt && (!attempt.completedAt || url.searchParams.get('new') !== '1')) {
      return json({ version: attempt.version, quiz: attempt.quiz, patternTitles: attempt.patternTitles, sourceSessions: attempt.sourceSessions, attempt });
    }
    return json({ ...await currentQuiz(storage), attempt: null });
  }
  if (route === '/quiz/results' && request.method === 'GET') {
    const before = url.searchParams.get('before');
    if (before && !CURSOR.test(before)) return json({ error: 'Invalid page.' }, 400);
    const entries = [...await storage.list({ prefix: 'quiz:index:', reverse: true, limit: 21, ...(before ? { end: `quiz:index:${before}` } : {}) })];
    const page = entries.slice(0, 20);
    return json({ attempts: page.map(([, value]) => value), nextCursor: entries.length > 20 ? page.at(-1)[0].slice('quiz:index:'.length) : null });
  }
  if (route.startsWith('/quiz/results/') && request.method === 'GET') {
    const id = route.slice('/quiz/results/'.length);
    if (!ATTEMPT_ID.test(id)) return json({ error: 'Quiz result not found.' }, 404);
    const attempt = await storage.get(`quiz:attempt:${id}`);
    return attempt ? json({ attempt }) : json({ error: 'Quiz result not found.' }, 404);
  }
  if (route !== '/quiz/answer' || request.method !== 'POST') return json({ error: 'Page not found.' }, 404);
  let input;
  try { input = await request.json(); } catch { return json({ error: 'Please choose an answer.' }, 400); }
  const { attemptId, version, questionIndex, choiceIndex } = input || {};
  if (!ATTEMPT_ID.test(attemptId) || !VERSION.test(version) || !Number.isInteger(questionIndex) || !Number.isInteger(choiceIndex)) return json({ error: 'Please choose an answer.' }, 400);
  // Transactions prevent simultaneous tabs and network retries from replacing
  // a first answer or creating two active attempts.
  return storage.transaction(async txn => {
    let attempt = await txn.get(`quiz:attempt:${attemptId}`);
    if (!attempt) {
      if (questionIndex !== 0) return conflict();
      const activeId = await txn.get('quiz:active');
      const active = activeId ? await txn.get(`quiz:attempt:${activeId}`) : null;
      if (active && !active.completedAt) return conflict();
      const current = await currentQuiz(txn);
      if (!current || current.version !== version) return conflict();
      attempt = {
        id: attemptId, ...current, startedAt: new Date().toISOString(), updatedAt: null, completedAt: null,
        answers: current.quiz.questions.map(() => []),
      };
    }
    if (attempt.version !== version) return conflict();
    const question = attempt.quiz.questions[questionIndex];
    if (!question || choiceIndex < 0 || choiceIndex >= question.options.length) return json({ error: 'Please choose an answer.' }, 400);
    const answers = attempt.answers[questionIndex];
    // A lost response may cause an identical request to be resent. Return the
    // original saved state without changing the score or timestamps.
    if (answers.includes(choiceIndex)) return json({ attempt });
    const pendingIndex = attempt.answers.findIndex((a, i) => !a.includes(attempt.quiz.questions[i].correctIndex));
    if (attempt.completedAt || questionIndex !== pendingIndex) return conflict();
    answers.push(choiceIndex);
    attempt.updatedAt = new Date().toISOString();
    if (attempt.answers.every((a, i) => a.includes(attempt.quiz.questions[i].correctIndex))) attempt.completedAt = attempt.updatedAt;
    await txn.put({
      [`quiz:attempt:${attemptId}`]: attempt,
      [`quiz:index:${attempt.startedAt}_${attemptId}`]: attemptSummary(attempt),
      'quiz:active': attemptId,
    });
    return json({ attempt });
  });
}
