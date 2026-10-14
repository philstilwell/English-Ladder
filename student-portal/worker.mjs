const COOKIE = '__Host-el-session';
const SESSION_SECONDS = 8 * 60 * 60;
const encoder = new TextEncoder();
const PUBLIC_PATHS = new Set(['/', '/index.html', '/portal.css', '/portal.js', '/ladder-mark.png', '/favicon.png', '/robots.txt']);
const SECURITY_HEADERS = {
  'Cache-Control': 'no-store',
  'X-Robots-Tag': 'noindex, nofollow, noarchive',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
  'X-Frame-Options': 'DENY',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
  'Content-Security-Policy': "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; font-src 'self'; base-uri 'none'; form-action 'self'; frame-ancestors 'none'",
};

function json(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', ...headers } });
}

function protect(response) {
  const headers = new Headers(response.headers);
  for (const [key, value] of Object.entries(SECURITY_HEADERS)) headers.set(key, value);
  return new Response(response.body, { status: response.status, headers });
}

export function normalizePassword(value) {
  return typeof value === 'string' ? value.toLowerCase() : '';
}

function base64url(bytes) {
  return btoa(String.fromCharCode(...new Uint8Array(bytes))).replaceAll('+', '-').replaceAll('/', '_').replace(/=+$/, '');
}

function decode64(value) {
  return Uint8Array.from(atob(value.replaceAll('-', '+').replaceAll('_', '/')), character => character.charCodeAt(0));
}

async function keyFor(secret) {
  return crypto.subtle.importKey('raw', encoder.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
}

async function signature(secret, value) {
  return crypto.subtle.sign('HMAC', await keyFor(secret), encoder.encode(value));
}

async function passwordMatches(secret, expected, provided) {
  // HMAC verification avoids a string comparison whose timing depends on the password.
  const digest = await signature(secret, normalizePassword(expected));
  return crypto.subtle.verify('HMAC', await keyFor(secret), digest, encoder.encode(normalizePassword(provided)));
}

function accountFor(request, env) {
  const host = new URL(request.url).hostname;
  const local = host === 'localhost' || host === '127.0.0.1';
  const match = /^([a-z0-9]+(?:-[a-z0-9]+)*)\.englishladder\.com$/.exec(host);
  const id = local ? env.LOCAL_STUDENT_ID : match?.[1];
  if (!id || ['www', 'students', 'admin'].includes(id)) return null;
  const accounts = JSON.parse(env.STUDENT_ACCOUNTS || '{}');
  const account = Object.hasOwn(accounts, id) ? accounts[id] : null;
  if (!account || typeof account.name !== 'string' || typeof account.password !== 'string' || !account.password) return null;
  return { ...account, id };
}

function configured(env) {
  return typeof env.SESSION_SECRET === 'string' && env.SESSION_SECRET.length >= 32 &&
    typeof env.TEACHER_PASSWORD === 'string' && env.TEACHER_PASSWORD.length > 0 &&
    typeof env.STUDENT_ACCOUNTS === 'string' && env.LOGIN_LIMITER && env.ACCOUNT_LIMITER;
}

async function credentialVersion(env, account, role) {
  const credential = role === 'teacher' ? env.TEACHER_PASSWORD : account.password;
  return base64url(await signature(env.SESSION_SECRET, JSON.stringify([account.id, role, normalizePassword(credential)])));
}

async function issueSession(request, env, account, role) {
  const payload = {
    student: account.id, role, audience: new URL(request.url).host,
    expires: Math.floor(Date.now() / 1000) + SESSION_SECONDS,
    version: await credentialVersion(env, account, role), nonce: crypto.randomUUID(),
  };
  const encoded = base64url(encoder.encode(JSON.stringify(payload)));
  return `${encoded}.${base64url(await signature(env.SESSION_SECRET, encoded))}`;
}

async function readSession(request, env, account) {
  try {
    const cookies = (request.headers.get('Cookie') || '').split(';').map(value => value.trim());
    const value = cookies.find(cookie => cookie.startsWith(`${COOKIE}=`))?.slice(COOKIE.length + 1);
    if (!value || value.length > 2048) return null;
    const parts = value.split('.');
    if (parts.length !== 2) return null;
    const [encoded, mac] = parts;
    if (!await crypto.subtle.verify('HMAC', await keyFor(env.SESSION_SECRET), decode64(mac), encoder.encode(encoded))) return null;
    const session = JSON.parse(new TextDecoder().decode(decode64(encoded)));
    const now = Math.floor(Date.now() / 1000);
    if (session.student !== account.id || session.audience !== new URL(request.url).host ||
        !['student', 'teacher'].includes(session.role) || !Number.isInteger(session.expires) ||
        session.expires <= now || session.expires > now + SESSION_SECONDS ||
        session.version !== await credentialVersion(env, account, session.role)) return null;
    return session;
  } catch { return null; }
}

function cookie(value, maxAge = SESSION_SECONDS) {
  return `${COOKIE}=${value}; Path=/; Max-Age=${maxAge}; HttpOnly; Secure; SameSite=Strict`;
}

function profile(account, role) {
  return { student: { id: account.id, name: account.name }, role };
}

async function smallJson(request) {
  if (!request.headers.get('Content-Type')?.toLowerCase().startsWith('application/json')) return null;
  const reader = request.body?.getReader();
  if (!reader) return null;
  const chunks = [];
  let length = 0;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    length += value.byteLength;
    if (length > 1024) { await reader.cancel(); return null; }
    chunks.push(value);
  }
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  try { return JSON.parse(new TextDecoder().decode(bytes)); } catch { return null; }
}

async function handle(request, env) {
  const url = new URL(request.url);
  if (!configured(env)) return json({ error: 'This student space is being set up. Please try again later.' }, 503);
  const account = accountFor(request, env);
  if (!account) return json({ error: 'This student space could not be found.' }, 404);

  if (url.pathname === '/api/login' || url.pathname === '/api/logout') {
    if (request.method !== 'POST') return json({ error: 'Please use the sign-in form.' }, 405, { Allow: 'POST' });
    // Exact-origin checks also reject requests from another student subdomain.
    if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
    if (url.pathname === '/api/logout') return json({ ok: true }, 200, { 'Set-Cookie': cookie('', 0) });
    const ip = request.headers.get('CF-Connecting-IP') || 'local';
    const attempts = await env.LOGIN_LIMITER.limit({ key: `${account.id}:${ip}` });
    const accountAttempts = await env.ACCOUNT_LIMITER.limit({ key: account.id });
    if (!attempts.success || !accountAttempts.success) return json({ error: 'Too many sign-in attempts. Please wait one minute and try again.' }, 429, { 'Retry-After': '60' });
    const body = await smallJson(request);
    if (typeof body?.password !== 'string' || !body.password || body.password.length > 128) return json({ error: 'Please enter your password.' }, 400);
    // Always check both credentials. The universal password selects teacher access.
    const [teacher, student] = await Promise.all([
      passwordMatches(env.SESSION_SECRET, env.TEACHER_PASSWORD, body.password),
      passwordMatches(env.SESSION_SECRET, account.password, body.password),
    ]);
    if (!teacher && !student) return json({ error: 'That password did not match. Please try again.' }, 401);
    const role = teacher ? 'teacher' : 'student';
    return json(profile(account, role), 200, { 'Set-Cookie': cookie(await issueSession(request, env, account, role)) });
  }

  if (!['GET', 'HEAD'].includes(request.method)) return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET, HEAD' });
  if (url.pathname === '/api/context') return json({ id: account.id });
  if (url.pathname === '/api/session') {
    const session = await readSession(request, env, account);
    return session ? json(profile(account, session.role)) : json({ error: 'Please sign in to continue.' }, 401);
  }
  if (!PUBLIC_PATHS.has(url.pathname)) return json({ error: 'Page not found.' }, 404);
  if (url.pathname === '/robots.txt') return new Response('User-agent: *\nDisallow: /\n', { headers: { 'Content-Type': 'text/plain' } });
  if (url.pathname === '/') url.pathname = '/index.html';
  return env.ASSETS.fetch(new Request(url, request));
}

export default {
  async fetch(request, env) {
    try { return protect(await handle(request, env)); }
    catch {
      // Never log passwords, secret configuration, or request bodies.
      return protect(json({ error: 'Sign-in is temporarily unavailable. Please try again shortly.' }, 503));
    }
  },
};
