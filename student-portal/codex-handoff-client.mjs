// Local operator helper. Credential and student files stay in ignored private/.
import { readFile, writeFile, mkdir, chmod } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { digest } from './codex-handoff.mjs';
const root = fileURLToPath(new URL('./private/', import.meta.url));
const privatePath = name => {
  const path = resolve(name);
  if (!path.startsWith(root) || path === root.slice(0,-1)) throw Error('Use a file inside student-portal/private/.');
  return path;
};
const read = async name => JSON.parse(await readFile(privatePath(name), 'utf8'));
async function save(name, value) {
  const path = privatePath(name);
  await mkdir(dirname(path), { recursive: true, mode: 0o700 });
  await chmod(dirname(path), 0o700);
  await writeFile(path, JSON.stringify(value, null, 2) + '\n', { mode: 0o600 });
  await chmod(path, 0o600);
}
const [action, ...args] = process.argv.slice(2);
if (!['queue','discover','nightly-discover','prepare','nightly-prepare','publish','verify','cefr-queue','cefr-inspect','cefr-prepare','cefr-publish','cefr-verify'].includes(action)) throw Error('Use queue|discover|nightly-discover|cefr-queue <output>, nightly-prepare <job> <output>, prepare <job> <output> [private-catch-up.json], publish <prepared> <records> <review> <receipt>, verify <prepared>, cefr-inspect|cefr-prepare <student-id> <output>, cefr-publish <prepared> <estimate> <review> <receipt>, or cefr-verify <prepared> [receipt].');
if (action === 'nightly-prepare' && args[2]) throw Error('Scheduled checks cannot approve catch-up.');
const secret = (await readFile(new URL('./private/codex-handoff-secret', import.meta.url), 'utf8')).trim();
if (!/^[a-f0-9]{64}$/.test(secret)) throw Error('Operator credential is unavailable.');
async function api(action, body = {}) {
  const response = await fetch('https://phil.englishladder.com/api/codex/' + action, { method: 'POST', redirect: 'error',
    headers: { Authorization: 'Bearer ' + secret, 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal: AbortSignal.timeout(240000) });
  const result = await response.json();
  if (!response.ok) throw Error('Handoff failed (' + response.status + '): ' + (result.error || 'unknown'));
  return result;
}
if (action === 'cefr-queue') {
  const result = await api(action); await save(args[0], result);
  console.log(JSON.stringify({ processor: result.processor, serverAI: result.serverAI, students: result.students.length,
    due: result.students.filter(s => s.due && !s.deferred).length, additionalAiCost: 0 }));
} else if (action === 'cefr-inspect') {
  const result = await api(action, { studentId: args[0] }); await save(args[1], result);
  console.log(JSON.stringify({ studentId: result.studentId, due: result.context.due, sources: result.context.references.length, error: result.error }));
} else if (action === 'cefr-prepare') {
  const recovery = args[2] ? await read(args[2]) : undefined;
  const result = await api(action, { studentId: args[0], ...(recovery ? { recovery } : {}) }); await save(args[1], result);
  console.log(JSON.stringify({ prepared: Boolean(result.snapshotHash), due: result.due, sources: result.sources?.length || 0 }));
} else if (action === 'cefr-verify') {
  const prepared = await read(args[0]);
  const result = await api(action, { studentId: prepared.studentId, attemptId: prepared.attemptId });
  if (result.verified !== true) throw Error('CEFR publication is not confirmed.');
  if (args[1]) await save(args[1], result);
  console.log(JSON.stringify(result));
} else if (action === 'cefr-publish') {
  const prepared = await read(args[0]), cefr = await read(args[1]), review = await read(args[2]);
  if (review.approved !== true || review.fullTranscript !== true || review.independent !== true ||
      review.snapshotHash !== prepared.snapshotHash || review.recordsHash !== await digest(cefr)) throw Error('The exact CEFR estimate and full source window need independent approval.');
  const result = await api(action, { studentId: prepared.studentId, attemptId: prepared.attemptId, snapshotHash: prepared.snapshotHash, cefr, review });
  if (result.verified !== true) throw Error('CEFR publication is not confirmed; refresh its eligibility.');
  await save(args[3], result); console.log(JSON.stringify(result));
} else if (['queue','discover','nightly-discover'].includes(action)) {
  const result = await api(action); await save(args[0], result);
  console.log(JSON.stringify({ processor: result.processor, serverAI: result.serverAI, jobs: result.jobs.length, catchUpRequired: result.catchUpRequired?.length || 0, discovery: result.discovery || null }));
} else if (['prepare','nightly-prepare'].includes(action)) {
  const catchUp = args[2] ? await read(args[2]) : undefined;
  const result = await api(action, { id: args[0], ...(catchUp ? { catchUp } : {}) }); await save(args[1], result);
  console.log(JSON.stringify({ prepared: Boolean(result.snapshotHash), duplicate: result.duplicate || false, skipped: result.skipped || false, approvalRequired: result.approvalRequired || false, waiting: result.waiting || false, deferred: result.deferred || false, retryAt: result.retryAt || null, error: result.error || null, sessionId: result.sessionId, segments: result.source?.segmentCount }));
} else if (action === 'verify') {
  const prepared = await read(args[0]), result = await api('prepare', { id: prepared.id });
  if (!result.duplicate) throw Error('Publication is not confirmed.');
  console.log(JSON.stringify({ published: true, sessionId: result.sessionId }));
} else {
  const prepared = await read(args[0]), records = await read(args[1]), review = await read(args[2]);
  if (review.approved !== true || review.fullTranscript !== true || review.independent !== true || review.recordsHash !== await digest(records)) throw Error('The exact records need independent approval.');
  const result = await api('publish', { id: prepared.id, snapshotHash: prepared.snapshotHash, records, review, ...(prepared.catchUp ? { catchUp: prepared.catchUp } : {}) });
  await save(args[3], result);
  console.log(JSON.stringify(result));
}
