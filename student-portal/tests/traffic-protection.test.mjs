import test from 'node:test';
import assert from 'node:assert/strict';
import { directoryMayContainAccount, clearDirectoryHint } from '../directory-gate.mjs';
import { env, call } from './harness.mjs';

test('scanner paths and invalid hostnames use no private-directory requests, even during an outage', async () => {
  const e = env(); let calls = 0;
  e.STUDENT_DIRECTORY = { idFromName: id => id, get: () => ({ fetch: async () => { calls++; throw new Error('Daily Durable Object requests limit exceeded.'); } }) };
  for (const host of ['ab26', 'redmine', 'test', 'harbor', 'kanban', 'dev2', 'de', 'keycloak']) {
    for (const path of ['/.env', '/@fs/.env', '/wp-login.php', '/__vite_rsc_findSourceMapURL', '/api/unknown', '/account-ids', '/api/account-ids']) {
      const response = await call(e, path, {}, `https://${host}.englishladder.com`);
      assert.equal(response.status, 404, host + path);
      assert.equal(response.headers.get('Cache-Control'), 'no-store');
    }
    if (host !== 'ab26') assert.equal((await call(e, '/', {}, `https://${host}.englishladder.com`)).status, 404);
  }
  assert.equal(calls, 0);
});

test('different guessed valid addresses share one lookup; real accounts are rechecked every time', async () => {
  const e = env(); const paths = [];
  e.STUDENT_DIRECTORY = { idFromName: id => id, get: () => ({ fetch: async request => {
    const path = new URL(request.url).pathname; paths.push(path);
    if (path === '/account-ids') return Response.json({ studentIds: ['ab26'] });
    return Response.json({ id: 'ab26', name: 'Alex' });
  } }) };
  await Promise.all(Array.from({ length: 100 }, (_, i) => call(e, '/', {}, `https://zz26-${i}.englishladder.com`)));
  assert.deepEqual(paths, ['/account-ids']);
  assert.equal((await call(e, '/')).status, 200);
  assert.equal((await call(e, '/api/session')).status, 401);
  assert.deepEqual(paths, ['/account-ids', '/account/ab26', '/account/ab26']);
});

test('address hints expire, deduplicate simultaneous reads, and never grant access', async () => {
  let time = 0, calls = 0, ids = ['ab26'];
  const binding = { idFromName: id => id, get: () => ({ fetch: async () => { calls++; return Response.json({ studentIds: ids }); } }) };
  const check = id => directoryMayContainAccount(binding, id, () => time);
  assert.deepEqual(await Promise.all([check('ab26'), check('zz26'), check('cd26')]), [true, false, false]);
  assert.equal(calls, 1);
  ids = ['ab26', 'cd26']; time = 59_999;
  assert.equal(await check('cd26'), false);
  time = 60_000;
  assert.equal(await check('cd26'), true); assert.equal(calls, 2);
  clearDirectoryHint(binding);
  assert.equal(await check('ab26'), true); assert.equal(calls, 3);
});

test('failed hint refreshes are not cached as an empty directory and retries are bounded', async () => {
  let time = 0, calls = 0, fail = false;
  const binding = { idFromName: id => id, get: () => ({ fetch: async () => {
    calls++; if (fail) throw new Error('Daily Durable Object requests limit exceeded.');
    return Response.json({ studentIds: ['ab26'] });
  } }) };
  const check = () => directoryMayContainAccount(binding, 'ab26', () => time);
  assert.equal(await check(), true);
  time = 60_000; fail = true;
  await assert.rejects(check(), /requests limit/);
  await assert.rejects(check(), /requests limit/); assert.equal(calls, 2);
  time += 5_000; fail = false;
  assert.equal(await check(), true); assert.equal(calls, 3);
});

test('hint failures and contents are never exposed through a public roster endpoint', async () => {
  const e = env(); let calls = 0;
  e.STUDENT_DIRECTORY = { idFromName: id => id, get: () => ({ fetch: async () => { calls++; return Response.json({ studentIds: ['ab26'] }); } }) };
  for (const host of ['https://phil.englishladder.com', 'https://ab26.englishladder.com']) {
    for (const path of ['/account-ids', '/api/account-ids', '/api/admin/account-ids']) {
      const response = await call(e, path, {}, host);
      assert.ok([401, 404].includes(response.status));
      assert.doesNotMatch(await response.text(), /studentIds|ab26/);
    }
  }
  assert.equal(calls, 0);
});
