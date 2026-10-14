import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { createHmac } from 'node:crypto';
import worker from '../worker.mjs';

const origin = 'https://ab26.englishladder.com';
const pass = 'student-example-only';
const teacherPass = 'teacher-example-only';
function environment(overrides = {}) {
  return {
    STUDENT_ACCOUNTS: JSON.stringify({ ab26: { name: 'Alex Brown', password: pass }, cd26: { name: 'Casey Drew', password: 'different-example-only' } }),
    TEACHER_PASSWORD: teacherPass,
    SESSION_SECRET: 'local-test-key-'.repeat(4),
    LOGIN_LIMITER: { limit: async () => ({ success: true }) },
    ACCOUNT_LIMITER: { limit: async () => ({ success: true }) },
    ASSETS: { fetch: async () => new Response('public sign-in shell') },
    ...overrides,
  };
}
function request(path, options = {}) { return new Request(`${origin}${path}`, options); }
async function login(env, password = pass, host = origin) {
  return worker.fetch(new Request(`${host}/api/login`, { method: 'POST', headers: { Origin: host, 'Content-Type': 'application/json' }, body: JSON.stringify({ password }) }), env);
}
function sessionCookie(response) { return response.headers.get('Set-Cookie').split(';')[0]; }

test('public shell and context never return a personal name or password', async () => {
  const env = environment();
  const home = await worker.fetch(request('/'), env);
  assert.equal(home.status, 200);
  assert.equal(home.headers.get('Cache-Control'), 'no-store');
  assert.match(home.headers.get('Content-Security-Policy'), /frame-ancestors 'none'/);
  assert.match(home.headers.get('X-Robots-Tag'), /noindex/);
  assert.deepEqual(await (await worker.fetch(request('/api/context'), env)).json(), { id: 'ab26' });
  assert.equal((await worker.fetch(request('/api/session'), env)).status, 401);
});

test('student password accepts uppercase and mixed case; session is signed and private', async () => {
  const env = environment();
  for (const password of [pass, pass.toUpperCase(), 'Student-Example-Only']) {
    const response = await login(env, password);
    assert.equal(response.status, 200);
    assert.deepEqual(await response.json(), { student: { id: 'ab26', name: 'Alex Brown' }, role: 'student' });
    const cookie = response.headers.get('Set-Cookie');
    for (const flag of ['__Host-el-session=', 'HttpOnly', 'Secure', 'SameSite=Strict', 'Path=/']) assert.ok(cookie.includes(flag));
    assert.ok(!cookie.includes('Domain='));
    const session = await worker.fetch(request('/api/session', { headers: { Cookie: sessionCookie(response) } }), env);
    assert.equal(session.status, 200);
  }
});

test('universal teacher password works on every configured student host', async () => {
  const env = environment();
  for (const id of ['ab26', 'cd26']) {
    const response = await login(env, teacherPass.toUpperCase(), `https://${id}.englishladder.com`);
    assert.equal(response.status, 200);
    const data = await response.json();
    assert.equal(data.role, 'teacher');
    assert.equal(data.student.id, id);
  }
});

test('incorrect password cannot issue a session or reveal account details', async () => {
  const response = await login(environment(), 'wrong');
  assert.equal(response.status, 401);
  assert.equal(response.headers.get('Set-Cookie'), null);
  assert.doesNotMatch(await response.text(), /Alex|Brown|teacher|student-example/);
});

test('student credential does not work for a different account', async () => {
  assert.equal((await login(environment(), pass, 'https://cd26.englishladder.com')).status, 401);
});

test('cookies cannot be moved across hosts, including teacher cookies', async () => {
  const env = environment();
  for (const password of [pass, teacherPass]) {
    const cookie = sessionCookie(await login(env, password));
    const response = await worker.fetch(new Request('https://cd26.englishladder.com/api/session', { headers: { Cookie: cookie } }), env);
    assert.equal(response.status, 401);
  }
});

test('tampered, expired, and malformed sessions are rejected', async () => {
  const env = environment();
  const valid = sessionCookie(await login(env));
  const [payload, mac] = valid.split('=')[1].split('.');
  const data = JSON.parse(Buffer.from(payload, 'base64url'));
  const altered = Buffer.from(JSON.stringify({ ...data, role: 'teacher' })).toString('base64url');
  const expired = Buffer.from(JSON.stringify({ ...data, expires: 1 })).toString('base64url');
  const expiredMac = createHmac('sha256', env.SESSION_SECRET).update(expired).digest('base64url');
  for (const token of [`${altered}.${mac}`, `${expired}.${expiredMac}`, 'bad.bad', 'x'.repeat(3000)]) {
    assert.equal((await worker.fetch(request('/api/session', { headers: { Cookie: `__Host-el-session=${token}` } }), env)).status, 401);
  }
});

test('changing a password or signing key invalidates existing sessions', async () => {
  const env = environment();
  const studentCookie = sessionCookie(await login(env));
  const teacherCookie = sessionCookie(await login(env, teacherPass));
  const accounts = JSON.parse(env.STUDENT_ACCOUNTS);
  accounts.ab26.password = 'new-example-only';
  const updated = { ...env, STUDENT_ACCOUNTS: JSON.stringify(accounts), TEACHER_PASSWORD: 'new-teacher-example' };
  for (const cookie of [studentCookie, teacherCookie]) assert.equal((await worker.fetch(request('/api/session', { headers: { Cookie: cookie } }), updated)).status, 401);
  assert.equal((await worker.fetch(request('/api/session', { headers: { Cookie: studentCookie } }), { ...env, SESSION_SECRET: 'replacement-key-'.repeat(4) })).status, 401);
});

test('login and logout require POST and exact same-origin requests', async () => {
  const env = environment();
  for (const path of ['/api/login', '/api/logout']) {
    assert.equal((await worker.fetch(request(path), env)).status, 405);
    for (const fakeOrigin of [null, 'https://cd26.englishladder.com', 'https://example.com']) {
      const headers = { 'Content-Type': 'application/json' };
      if (fakeOrigin) headers.Origin = fakeOrigin;
      assert.equal((await worker.fetch(request(path, { method: 'POST', headers, body: '{}' }), env)).status, 403);
    }
  }
});

test('sign out clears the host-only session cookie', async () => {
  const response = await worker.fetch(request('/api/logout', { method: 'POST', headers: { Origin: origin } }), environment());
  assert.equal(response.status, 200);
  assert.match(response.headers.get('Set-Cookie'), /Max-Age=0/);
});

test('missing configuration, missing limiters, and invalid account secrets fail closed', async () => {
  for (const values of [{ SESSION_SECRET: '' }, { TEACHER_PASSWORD: '' }, { STUDENT_ACCOUNTS: 'bad JSON' }, { LOGIN_LIMITER: null }, { ACCOUNT_LIMITER: null }]) {
    assert.equal((await login(environment(values))).status, 503);
  }
});

test('either rate limit blocks password checking', async () => {
  for (const binding of ['LOGIN_LIMITER', 'ACCOUNT_LIMITER']) {
    const response = await login(environment({ [binding]: { limit: async () => ({ success: false }) } }));
    assert.equal(response.status, 429);
    assert.equal(response.headers.get('Retry-After'), '60');
    assert.equal(response.headers.get('Set-Cookie'), null);
  }
});

test('malformed and oversized login requests are rejected', async () => {
  const env = environment();
  for (const body of ['{', '{}', '{"password":null}', JSON.stringify({ password: 'x'.repeat(2000) })]) {
    assert.equal((await worker.fetch(request('/api/login', { method: 'POST', headers: { Origin: origin, 'Content-Type': 'application/json' }, body }), env)).status, 400);
  }
});

test('unknown hosts, source files, and unimplemented endpoints are not served', async () => {
  const env = environment();
  for (const host of ['https://unknown.englishladder.com', 'https://englishladder.com', 'https://englishladder-students.example.workers.dev', 'https://ab26.englishladder.com.evil.test']) {
    assert.equal((await worker.fetch(new Request(host), env)).status, 404);
  }
  for (const path of ['/.dev.vars', '/worker.mjs', '/wrangler.jsonc', '/api/accounts', '/data/students.json']) {
    assert.equal((await worker.fetch(request(path), env)).status, 404);
  }
});

test('local account override is confined to localhost', async () => {
  const env = environment({ LOCAL_STUDENT_ID: 'ab26' });
  assert.equal((await worker.fetch(new Request('http://localhost:8787/api/context'), env)).status, 200);
  assert.equal((await worker.fetch(new Request('https://unknown.englishladder.com/api/context'), env)).status, 404);
});

test('frontend contains no student identities or passwords and uses no local storage', () => {
  const files = readdirSync(new URL('../public/', import.meta.url)).filter(name => /\.(html|js|css)$/.test(name));
  const text = files.map(name => readFileSync(new URL(`../public/${name}`, import.meta.url), 'utf8')).join('\n');
  assert.doesNotMatch(text, /Koji|Hisai|TEACHER_PASSWORD|STUDENT_ACCOUNTS|SESSION_SECRET|localStorage|sessionStorage/);
  assert.match(text, /toLowerCase\(\)/);
});
