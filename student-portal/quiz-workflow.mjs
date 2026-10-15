// Private context export and quiz-only publishing for the scheduled author.
// Credentials arrive on stdin; no student records or passwords are logged.
import { readFile, writeFile, mkdir, chmod } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { once } from 'node:events';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { isDeepStrictEqual } from 'node:util';
import { validateAssessment } from './assessment.mjs';

export async function collectQuizContext(api) {
  const { assessment } = await api('/api/assessment');
  const sessions = [], attempts = [];
  for (const [path, key, target] of [['/api/feedback', 'sessions', sessions], ['/api/quiz/results', 'attempts', attempts]]) {
    let cursor;
    const seen = new Set();
    do {
      const page = await api(path + (cursor ? '?before=' + encodeURIComponent(cursor) : ''));
      target.push(...page[key]);
      cursor = page.nextCursor;
      if (cursor && seen.has(cursor)) throw new Error('Repeated page cursor.');
      seen.add(cursor);
    } while (cursor);
  }
  const history = [];
  for (const summary of attempts) {
    const { attempt } = await api('/api/quiz/results/' + summary.id);
    history.push({
      attempt,
      firstTryMistakes: attempt.answers.flatMap((choices, index) => {
        const question = attempt.quiz.questions[index];
        return choices.length && choices[0] !== question.correctIndex ? [{
          questionNumber: index + 1,
          topic: attempt.patternTitles[question.patternIndex],
          prompt: question.prompt,
          firstChoice: question.options[choices[0]].text,
          correctChoice: question.options[question.correctIndex].text,
          sourceSessions: attempt.sourceSessions,
        }] : [];
      }),
    });
  }
  return { fetchedAt: new Date().toISOString(), assessment, sessions, history };
}

export async function publishQuiz(api, quiz) {
  if (!quiz?.generatedForSession) throw new Error('A trigger session is required.');
  const { assessment } = await api('/api/assessment');
  if (!assessment) throw new Error('An existing assessment is required.');
  if (assessment.quiz?.generatedForSession === quiz.generatedForSession) {
    return { published: false, reason: 'This session already has a quiz.' };
  }
  // Always merge with the live assessment, never an old authoring copy.
  const record = validateAssessment({ ...assessment, quiz });
  await api('/api/assessment', 'PUT', record);
  const saved = (await api('/api/assessment')).assessment;
  if (!isDeepStrictEqual(saved, record)) throw new Error('Published quiz verification failed.');
  return { published: true, sessionId: quiz.generatedForSession };
}

async function main() {
  const [mode, origin, filename] = process.argv.slice(2);
  if (!['context', 'publish'].includes(mode) || !filename) throw new Error('Use context|publish <student-origin> <private-json-file>.');
  const url = new URL(origin);
  if (url.origin !== origin || !((url.protocol === 'https:' && /^[a-z0-9-]+\.englishladder\.com$/.test(url.hostname)) || (url.protocol === 'http:' && ['localhost', '127.0.0.1'].includes(url.hostname)))) throw new Error('Use a student subdomain or local preview.');
  const filenamePath = resolve(filename);
  const privateRoot = fileURLToPath(new URL('./private/', import.meta.url));
  if (!filenamePath.startsWith(privateRoot)) throw new Error('Keep authoring files inside student-portal/private/.');
  const quiz = mode === 'publish' ? JSON.parse(await readFile(filenamePath, 'utf8')) : null;
  console.log('Ready for the teacher password on standard input.');
  const reader = createInterface({ input: process.stdin, terminal: false });
  const [password] = await once(reader, 'line');
  reader.close();
  let cookie;
  async function api(path, method = 'GET', body) {
    const response = await fetch(origin + path, {
      method, redirect: 'error',
      headers: { Origin: origin, 'Content-Type': 'application/json', ...(cookie ? { Cookie: cookie } : {}) },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    });
    if (!response.ok) throw new Error('Request failed: ' + method + ' ' + path + ' (' + response.status + ').');
    if (path === '/api/login') cookie = response.headers.get('set-cookie')?.split(';')[0];
    return response.json();
  }
  try {
    const profile = await api('/api/login', 'POST', { password });
    if (profile.role !== 'teacher' || !cookie) throw new Error('Teacher access is required.');
    if (mode === 'context') {
      const context = await collectQuizContext(api);
      await mkdir(dirname(filenamePath), { recursive: true, mode: 0o700 });
      await chmod(dirname(filenamePath), 0o700);
      await writeFile(filenamePath, JSON.stringify(context, null, 2) + '\n', { mode: 0o600 });
      await chmod(filenamePath, 0o600);
      console.log('Saved private lesson and first-try context. No student records were changed.');
    } else {
      const result = await publishQuiz(api, quiz);
      console.log(result.published ? 'Published and verified the new quiz.' : result.reason);
    }
  } finally {
    if (cookie) await api('/api/logout', 'POST');
  }
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) await main();
