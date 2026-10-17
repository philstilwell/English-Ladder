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
if (!['queue','discover','prepare','publish','verify'].includes(action)) throw Error('Use queue|discover <output>, prepare <job> <output> [private-catch-up.json], publish <prepared> <records> <review> <receipt>, or verify <prepared>.');
const secret = (await readFile(new URL('./private/codex-handoff-secret', import.meta.url), 'utf8')).trim();
if (!/^[a-f0-9]{64}$/.test(secret)) throw Error('Operator credential is unavailable.');
async function api(action, body = {}) {
  const response = await fetch('https://phil.englishladder.com/api/codex/' + action, { method: 'POST', redirect: 'error',
    headers: { Authorization: 'Bearer ' + secret, 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal: AbortSignal.timeout(240000) });
  const result = await response.json();
  if (!response.ok) throw Error('Handoff failed (' + response.status + '): ' + (result.error || 'unknown'));
  return result;
}
if (['queue','discover'].includes(action)) {
  const result = await api(action); await save(args[0], result);
  console.log(JSON.stringify({ processor: result.processor, serverAI: result.serverAI, jobs: result.jobs.length }));
} else if (action === 'prepare') {
  const catchUp = args[2] ? await read(args[2]) : undefined;
  const result = await api('prepare', { id: args[0], ...(catchUp ? { catchUp } : {}) }); await save(args[1], result);
  console.log(JSON.stringify({ prepared: Boolean(result.snapshotHash), duplicate: result.duplicate || false, skipped: result.skipped || false, sessionId: result.sessionId, segments: result.source?.segmentCount }));
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
