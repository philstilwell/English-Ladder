import { COMMUNICATION_ACTIVITIES } from './communication-practice.mjs';
import { codexAuthorized } from './codex-handoff.mjs';
import { FEEDBACK_ID, validateFeedback, validatePracticeEdit } from './feedback.mjs';
import { validateAssessment } from './assessment.mjs';
export { FeedbackStore } from './feedback.mjs';
import { nightlyDate } from './server-quiz-automation.mjs';
export { QuizAutomation } from './server-quiz-automation.mjs';
import { directoryRequest, STUDENT_ID } from './student-directory.mjs';
import { directoryMayContainAccount } from './directory-gate.mjs';
import { runtimeErrorCategory } from './runtime-error.mjs';
import { matchesStudentPassword } from './student-password.mjs';
import vocabularyBank from './vocabulary-bank.json' with { type: 'json' };
import grammarBank from './grammar-bank.json' with { type: 'json' };
import businessTermsBank from './business-terms-bank.json' with { type: 'json' };
export { StudentDirectory } from './student-directory.mjs';

const COOKIE = '__Host-el-session';
const SESSION_SECONDS = 7 * 24 * 60 * 60;
const encoder = new TextEncoder();
const PUBLIC_PATHS = new Set(['/', '/index.html', '/portal.css', '/portal.js', '/practice-prompt.js', '/road-questions.js', '/all-questions.js', '/study-practice.js', '/road-practice.js', '/practice-position.js', '/grammar-practice.js', '/business-terms.js', '/vocabulary-practice.js', '/communication-practice.js', '/ladder-mark.png', '/favicon.png', '/chatgpt-logo.svg', '/gemini-logo.png', '/claude-logo.png', '/copilot-logo.svg', '/robots.txt']);
const STUDENT_API_PATHS = new Set([
  '/api/login', '/api/logout', '/api/account', '/api/account/password', '/api/context', '/api/session',
  '/api/learning-import', '/api/assessment', '/api/feedback', '/api/activities/progress', '/api/activities/questions',
  '/api/grammar-practice', '/api/business-terms', '/api/vocabulary-practice',
  '/api/grammar-practice/state', '/api/business-terms/state', '/api/vocabulary-practice/state',
  '/api/study/state', '/api/study/questions', '/api/road/state', '/api/road/start', '/api/road/answer',
  '/api/road/end', '/api/road/questions', '/api/quiz/state', '/api/quiz/answer', '/api/quiz/results',
  '/api/automation/status', '/api/automation/connect', '/api/automation/verify', '/api/automation/callback', '/api/automation/webhook',
  ...COMMUNICATION_ACTIVITIES.flatMap(activity => ['/api/communication/' + activity.id, '/api/communication/' + activity.id + '/state']),
]);

function studentPathExists(path) {
  return PUBLIC_PATHS.has(path) || STUDENT_API_PATHS.has(path) ||
    path.startsWith('/api/feedback/') && FEEDBACK_ID.test(path.slice('/api/feedback/'.length)) ||
    /^\/api\/quiz\/results\/[a-zA-Z0-9-]{36}$/.test(path);
}
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

async function accountFor(request, env, allowPausedIntegration = false) {
  const host = new URL(request.url).hostname;
  const local = host === 'localhost' || host === '127.0.0.1';
  const match = /^([a-z0-9]+(?:-[a-z0-9]+)*)\.englishladder\.com$/.exec(host);
  const id = local ? env.LOCAL_STUDENT_ID : match?.[1];
  if (!id || ['www', 'students', 'admin', 'phil'].includes(id)) return null;
  const accounts = JSON.parse(env.STUDENT_ACCOUNTS || '{}');
  // Match the same address rule used by registration; preserve explicit legacy IDs.
  if (!STUDENT_ID.test(id) && !Object.hasOwn(accounts, id)) return null;
  let account = Object.hasOwn(accounts, id) ? accounts[id] : null;
  if (env.STUDENT_DIRECTORY) {
    if (!await directoryMayContainAccount(env.STUDENT_DIRECTORY, id)) return null;
    const response = await directoryRequest(env, (allowPausedIntegration ? '/integration-account/' : '/account/') + encodeURIComponent(id));
    if (response.status === 404) return null;
    if (!response.ok) throw new Error('Directory unavailable');
    account = { ...await response.json(), password: account?.password || env.STUDENT_PASSWORD };
  }
  if (!account || typeof account.name !== 'string' || !account.passwordCredential && (typeof account.password !== 'string' || !account.password)) return null;
  return { ...account, id };
}

function configured(env) {
  return typeof env.SESSION_SECRET === 'string' && env.SESSION_SECRET.length >= 32 &&
    typeof env.TEACHER_PASSWORD === 'string' && env.TEACHER_PASSWORD.length > 0 &&
    typeof env.STUDENT_ACCOUNTS === 'string' && env.LOGIN_LIMITER && env.ACCOUNT_LIMITER;
}

async function credentialVersion(env, account, role) {
  if (role === 'student' && account.passwordCredential) return base64url(await signature(env.SESSION_SECRET, JSON.stringify([account.id, role, account.passwordCredential])));
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
  const name = account.name.trim().split(/\s+/)[0];
  return { student: { id: account.id, name, nickname: account.nickname || name }, role };
}

async function smallJson(request, maxBytes = 1024) {
  if (!request.headers.get('Content-Type')?.toLowerCase().startsWith('application/json')) return null;
  const reader = request.body?.getReader();
  if (!reader) return null;
  const chunks = [];
  let length = 0;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    length += value.byteLength;
    if (length > maxBytes) { await reader.cancel(); return null; }
    chunks.push(value);
  }
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  try { return JSON.parse(new TextDecoder().decode(bytes)); } catch { return null; }
}

async function handleAdmin(request, env) {
  const url = new URL(request.url), account = { id: 'phil' };
  if (url.pathname.startsWith('/api/codex/')) {
    if (!await codexAuthorized(request, env)) return json({ error: 'Operator authorization required.' }, 401);
    if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405);
    const action = url.pathname.slice('/api/codex/'.length);
    if (!['discover','nightly-discover','queue','prepare','nightly-prepare','publish','cefr-queue','cefr-prepare','cefr-publish','cefr-verify'].includes(action)) return json({ error: 'Page not found.' }, 404);
    const body = await smallJson(request, action.endsWith('publish') ? 524288 : 1024);
    if (!body || typeof body !== 'object' || Array.isArray(body)) return json({ error: 'Invalid input.' }, 400);
    if (!env.QUIZ_AUTOMATION) return json({ error: 'Updates are unavailable.' }, 503);
    return env.QUIZ_AUTOMATION.get(env.QUIZ_AUTOMATION.idFromName('zoom')).fetch(new Request('https://automation.internal/codex/' + action, { method: 'POST', body: JSON.stringify(body) }));
  }
  if (['/api/login', '/api/logout'].includes(url.pathname)) {
    if (request.method !== 'POST') return json({ error: 'Please use the sign-in form.' }, 405);
    if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload and try again.' }, 403);
    if (url.pathname === '/api/logout') return json({ ok: true }, 200, { 'Set-Cookie': cookie('', 0) });
    const ip = request.headers.get('CF-Connecting-IP') || 'local';
    const [perIP, perAccount] = await Promise.all([env.LOGIN_LIMITER.limit({ key: 'phil:' + ip }), env.ACCOUNT_LIMITER.limit({ key: 'phil' })]);
    if (!perIP.success || !perAccount.success) return json({ error: 'Too many attempts. Please wait one minute.' }, 429, { 'Retry-After': '60' });
    const input = await smallJson(request);
    if (typeof input?.password !== 'string' || !input.password || input.password.length > 128) return json({ error: 'Enter your teacher password.' }, 400);
    if (!await passwordMatches(env.SESSION_SECRET, env.TEACHER_PASSWORD, input.password)) return json({ error: 'That password did not match.' }, 401);
    return json({ role: 'teacher', administrator: true }, 200, { 'Set-Cookie': cookie(await issueSession(request, env, account, 'teacher')) });
  }
  if (url.pathname.startsWith('/api/')) {
    const session = await readSession(request, env, account);
    if (!session || session.role !== 'teacher') return json({ error: 'Please sign in with your teacher password.' }, 401);
    if (url.pathname === '/api/session' && request.method === 'GET') return json({ role: 'teacher', administrator: true });
    if (['/api/admin/quiz-status', '/api/admin/cefr-status', '/api/admin/questions-status'].includes(url.pathname) && request.method === 'GET') {
      if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const isQuestions = url.pathname.endsWith('/questions-status');
      const isCefr = url.pathname.endsWith('/cefr-status');
      const after = url.searchParams.get('after');
      if (after && !/^[0-9a-f-]{36}$/.test(after)) return json({ error: 'Invalid page.' }, 400);
      const directory = await directoryRequest(env, '/students');
      if (!directory.ok) return json({ error: 'Student status is temporarily unavailable.' }, 503);
      const records = (await directory.json()).students.sort((a, b) => a.key.localeCompare(b.key)).filter(s => !after || s.key > after);
      // Bound each request's fan-out, including on Workers' free plan. Keep the
      // student list usable if one account's private history is unavailable.
      const page = records.slice(0, 20), statuses = {};
      for (let offset = 0; offset < page.length; offset += 4) {
        await Promise.all(page.slice(offset, offset + 4).map(async student => {
          if (student.deletionPending || !student.activated || !student.studentId) { statuses[student.key] = isQuestions ? { state: 'ready', count: 0 } : { state: isCefr ? 'pending' : 'no_quiz' }; return; }
          try {
            if (!env.FEEDBACK_STORE) throw new Error('Store unavailable');
            const response = await env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(student.studentId)).fetch(new Request('https://feedback.internal/admin/' + (isQuestions ? 'questions-status' : isCefr ? 'cefr-status' : 'quiz-status')));
            if (!response.ok) throw new Error('Status unavailable');
            statuses[student.key] = await response.json();
          } catch { statuses[student.key] = { state: 'unavailable' }; }
        }));
      }
      return json({ statuses, nextCursor: records.length > 20 ? page.at(-1).key : null });
    }
    const resolveAccount = /^\/api\/admin\/students\/([0-9a-f-]{36})\/questions\/(resolve|undo)$/.exec(url.pathname);
    if (resolveAccount) {
      if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405, { Allow: 'POST' });
      if (request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const input = await smallJson(request, 1024);
      if (!input) return json({ error: 'Please check the question.' }, 400);
      const directory = await directoryRequest(env, '/students');
      if (!directory.ok) return json({ error: 'Student records are temporarily unavailable.' }, 503);
      const student = (await directory.json()).students.find(s => s.key === resolveAccount[1]);
      if (!student || student.deletionPending || !student.activated || !student.studentId) return json({ error: 'Student not found.' }, 404);
      if (!env.FEEDBACK_STORE) return json({ error: 'Practice is temporarily unavailable.' }, 503);
      try {
        return await env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(student.studentId)).fetch(new Request('https://feedback.internal/admin/questions/' + resolveAccount[2],
          { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(input) }));
      } catch { return json({ error: 'The question could not be updated. Please try again.' }, 503); }
    }
    const selfCheckAccount = /^\/api\/admin\/students\/([0-9a-f-]{36})\/(business-terms|grammar-practice|study-practice|activity-summary|questions)$/.exec(url.pathname);
    if (selfCheckAccount && request.method === 'GET') {
      if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const response = await directoryRequest(env, '/students');
      if (!response.ok) return json({ error: 'Student records are temporarily unavailable.' }, 503);
      const student = (await response.json()).students.find(s => s.key === selfCheckAccount[1]);
      if (!student || student.deletionPending || !student.activated || !student.studentId) return json({ error: 'Student not found.' }, 404);
      if (!env.FEEDBACK_STORE) return json({ error: 'Practice is temporarily unavailable.' }, 503);
      const internalPath = ['activity-summary', 'questions'].includes(selfCheckAccount[2]) ? 'admin/' + selfCheckAccount[2] : (selfCheckAccount[2] === 'study-practice' ? 'study' : selfCheckAccount[2] === 'grammar-practice' ? 'grammar' : 'terms') + '/questions';
      try {
        const internalUrl = new URL('https://feedback.internal/' + internalPath);
        if (url.searchParams.has('after')) internalUrl.searchParams.set('after', url.searchParams.get('after'));
        return await env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(student.studentId)).fetch(new Request(internalUrl));
      } catch { return json({ error: 'Activity records are temporarily unavailable. Please try again.' }, 503); }
    }
    const roadAccount = /^\/api\/admin\/students\/([0-9a-f-]{36})\/road(?:\/([0-9a-f-]{36}))?$/.exec(url.pathname);
    if (roadAccount && request.method === 'GET') {
      if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const response = await directoryRequest(env, '/students');
      if (!response.ok) return json({ error: 'Student records are temporarily unavailable.' }, 503);
      const student = (await response.json()).students.find(s => s.key === roadAccount[1]);
      if (!student || student.deletionPending || !student.activated || !student.studentId) return json({ error: 'Student not found.' }, 404);
      if (!env.FEEDBACK_STORE) return json({ error: 'Practice results are temporarily unavailable.' }, 503);
      const target = new URL('https://feedback.internal/road/results' + (roadAccount[2] ? '/' + roadAccount[2] : ''));
      if (url.searchParams.has('before')) target.searchParams.set('before', url.searchParams.get('before'));
      return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(student.studentId)).fetch(new Request(target));
    }
    const cefrAccount = /^\/api\/admin\/students\/([0-9a-f-]{36})\/cefr$/.exec(url.pathname);
    if (cefrAccount && request.method === 'GET') {
      if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const response = await directoryRequest(env, '/students');
      if (!response.ok) return json({ error: 'Student records are temporarily unavailable.' }, 503);
      const student = (await response.json()).students.find(s => s.key === cefrAccount[1]);
      if (!student || student.deletionPending) return json({ error: 'Student not found.' }, 404);
      if (!student.activated || !student.studentId) return json({ cefr: null });
      try {
        const result = await env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(student.studentId)).fetch(new Request('https://feedback.internal/admin/cefr' + (env.CEFR_PROCESSOR === 'codex' ? '?processor=codex' : '')));
        if (!result.ok) throw new Error('Unavailable');
        return json(await result.json());
      } catch { return json({ error: 'The CEFR estimate is temporarily unavailable. Please try again.' }, 503); }
    }
    if (['/api/admin/automation/retry', '/api/admin/automation/ignore'].includes(url.pathname)) {
      if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405, { Allow: 'POST' });
      if (request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      const input = await smallJson(request, 1024);
      if (!input || Object.keys(input).length !== 1 || typeof input.id !== 'string' || !/^[a-f0-9]{64}$/.test(input.id)) return json({ error: 'Choose an update from the list.' }, 400);
      if (!env.QUIZ_AUTOMATION) return json({ error: 'Automatic updates are unavailable.' }, 503);
      return env.QUIZ_AUTOMATION.get(env.QUIZ_AUTOMATION.idFromName('zoom')).fetch(new Request('https://automation.internal/' + url.pathname.split('/').at(-1), { method: 'POST', body: JSON.stringify(input) }));
    }
    if (url.pathname === '/api/admin/automation' && request.method === 'GET') {
      if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Open this from your administrator page.' }, 403);
      if (!env.QUIZ_AUTOMATION) return json({ enabled: false, connected: false });
      return env.QUIZ_AUTOMATION.get(env.QUIZ_AUTOMATION.idFromName('zoom')).fetch(new Request('https://automation.internal/admin-status'));
    }
    const path = url.pathname.slice('/api/admin'.length);
    const loginDetails = /^\/students\/[\w-]{36}\/login-details$/.test(path);
    if (!url.pathname.startsWith('/api/admin/') || !['/students', '/import', '/import/preview'].includes(path) && !/^\/students\/[\w-]{36}$/.test(path) && !loginDetails) return json({ error: 'Page not found.' }, 404);
    if (loginDetails && (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site')) return json({ error:'Please open this account from your administrator page.' }, 403);
    const method = loginDetails ? ['GET', 'PUT'] : path === '/students' ? ['GET', 'POST'] : path.startsWith('/students/') ? ['PUT', 'DELETE'] : ['POST'];
    if (!method.includes(request.method)) return json({ error: 'Method not allowed.' }, 405);
    let body;
    if (request.method !== 'GET') {
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload and try again.' }, 403);
      body = await smallJson(request, path.startsWith('/import') ? 250000 : 16384);
      if (!body) return json({ error: 'Please check the form.' }, 400);
    }
    return directoryRequest(env, path, body, request.method);
  }
  if (!['GET', 'HEAD'].includes(request.method)) return json({ error: 'Method not allowed.' }, 405);
  const assets = new Set(['/', '/admin.html', '/admin.js', '/admin.css', '/portal.css', '/practice-prompt.js', '/road-questions.js', '/study-practice.js', '/chatgpt-logo.svg', '/gemini-logo.png', '/claude-logo.png', '/copilot-logo.svg', '/business-terms.js', '/vocabulary-practice.js', '/communication-practice.js', '/grammar-practice.js', '/ladder-mark.png', '/favicon.png', '/robots.txt']);
  if (!assets.has(url.pathname)) return json({ error: 'Page not found.' }, 404);
  if (url.pathname === '/robots.txt') return new Response('User-agent: *\nDisallow: /\n');
  if (url.pathname === '/') url.pathname = '/admin.html';
  return env.ASSETS.fetch(new Request(url, request));
}

async function handle(request, env) {
  const url = new URL(request.url);
  if (!configured(env)) return json({ error: 'This student space is being set up. Please try again later.' }, 503);
  if (url.hostname === 'phil.englishladder.com' || ['localhost', '127.0.0.1'].includes(url.hostname) && env.LOCAL_STUDENT_ID === 'phil') return handleAdmin(request, env);
  // Scanner paths must not spend private-directory requests, even during an outage.
  if (!studentPathExists(url.pathname)) {
    if (!/^\/api\/(?:codex|automation|feedback|quiz|road|communication)\//.test(url.pathname) && !['GET', 'HEAD'].includes(request.method))
      return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET, HEAD' });
    return json({ error: 'Page not found.' }, 404);
  }
  const account = await accountFor(request, env, ['/api/automation/webhook', '/api/automation/callback'].includes(url.pathname));
  if (!account) return json({ error: 'This student space could not be found.' }, 404);

  if (url.pathname.startsWith('/api/automation/')) {
    const route = url.pathname.slice('/api/automation'.length);
    if (!['/status', '/connect', '/verify', '/callback', '/webhook'].includes(route)) return json({ error: 'Page not found.' }, 404);
    const method = ['/connect', '/verify', '/webhook'].includes(route) ? 'POST' : 'GET';
    if (request.method !== method) return json({ error: 'Method not allowed.' }, 405);
    if (!['/callback', '/webhook'].includes(route)) {
      const session = await readSession(request, env, account);
      if (!session) return json({ error: 'Please sign in to continue.' }, 401);
      if (session.role !== 'teacher') return json({ error: 'Only your teacher can manage automatic quizzes.' }, 403);
      if (method === 'POST' && request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload and try again.' }, 403);
    }
    if (!env.QUIZ_AUTOMATION) return json({ configured: false, connected: false, enabled: false }, route === '/status' ? 200 : 503);
    const coordinator = env.QUIZ_AUTOMATION.get(env.QUIZ_AUTOMATION.idFromName('zoom'));
    const headers = new Headers();
    headers.set('X-Student-ID', account.id); headers.set('X-Student-Origin', url.origin);
    if (route === '/callback') headers.set('X-Callback-URL', url.href);
    if (route === '/webhook') for (const name of ['x-zm-signature', 'x-zm-request-timestamp']) {
      if (request.headers.has(name)) headers.set(name, request.headers.get(name));
    }
    return coordinator.fetch(new Request('https://automation.internal' + route, { method, headers, redirect: 'manual',
      ...(route === '/webhook' ? { body: request.body, duplex: 'half' } : {}) }));
  }

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
      account.passwordCredential ? matchesStudentPassword(env, account.passwordCredential, account.credentialAccountKey, body.password) : passwordMatches(env.SESSION_SECRET, account.password, body.password),
    ]);
    if (!teacher && !student) return json({ error: 'That password did not match. Please try again.' }, 401);
    const role = teacher ? 'teacher' : 'student';
    return json(profile(account, role), 200, { 'Set-Cookie': cookie(await issueSession(request, env, account, role)) });
  }

  if (['/api/account', '/api/account/password'].includes(url.pathname)) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    const passwordChange = url.pathname.endsWith('/password');
    if (!(passwordChange ? ['POST'] : ['GET', 'PUT']).includes(request.method)) return json({ error: 'Method not allowed.' }, 405);
    if (!env.STUDENT_DIRECTORY) return json({ error: 'Account settings are not available. Please try again later.' }, 503);
    if (request.method === 'GET') return directoryRequest(env, '/self/' + account.id);
    if (session.role !== 'student') return json({ error: 'Sign in as the student to change these settings.' }, 403);
    if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
    const ip = request.headers.get('CF-Connecting-IP') || 'local';
    const [attempts, accountAttempts] = await Promise.all([
      env.LOGIN_LIMITER.limit({ key: `${account.id}:${ip}` }), env.ACCOUNT_LIMITER.limit({ key: account.id }),
    ]);
    if (!attempts.success || !accountAttempts.success) return json({ error: 'Too many changes. Please wait one minute and try again.' }, 429, { 'Retry-After': '60' });
    const input = await smallJson(request, 4096);
    if (!input || !Number.isInteger(input.revision)) return json({ error: 'Please reload the account page and try again.' }, 400);
    if (Object.hasOwn(input, 'visibleActivities')) return json({ error: 'Your teacher chooses the activities in your menu.' }, 403);
    if (Object.hasOwn(input, 'visibleResources')) return json({ error: 'Your teacher chooses the resources on your page.' }, 403);
    if (passwordChange) {
      if (typeof input.currentPassword !== 'string' || !input.currentPassword || input.currentPassword.length > 128)
        return json({ error: 'Enter your current password.' }, 400);
      const matches = account.passwordCredential
        ? await matchesStudentPassword(env, account.passwordCredential, account.credentialAccountKey, input.currentPassword)
        : await passwordMatches(env.SESSION_SECRET, account.password, input.currentPassword);
      if (!matches) return json({ error: 'Your current password did not match. Please try again.' }, 400);
    }
    // Choose the target from the authenticated host. Never forward extra fields.
    const body = { revision: input.revision, expectedAccountRevision: account.directoryRevision,
      ...(passwordChange ? { newPassword: input.newPassword, confirmPassword: input.confirmPassword }
        : { nickname: input.nickname }) };
    const response = await directoryRequest(env, '/self/' + account.id + (passwordChange ? '/password' : ''), body, request.method);
    return json(await response.json(), response.status, passwordChange && response.ok ? { 'Set-Cookie': cookie('', 0) } : {});
  }

  if (url.pathname === '/api/learning-import') {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    if (session.role !== 'teacher') return json({ error: 'Only your teacher can import learning records.' }, 403);
    if (request.method !== 'POST') return json({ error: 'Method not allowed.' }, 405);
    if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload and try again.' }, 403);
    const body = await smallJson(request, 524288);
    if (!body) return json({ error: 'Please check the learning records.' }, 400);
    if (!env.FEEDBACK_STORE) return json({ error: 'Learning records are temporarily unavailable.' }, 503);
    return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id)).fetch(new Request('https://feedback.internal/learning-import', { method: 'POST', body: JSON.stringify(body) }));
  }

  if (['/api/activities/progress', '/api/activities/questions'].includes(url.pathname)) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    if (request.method !== 'GET') return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET' });
    if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Please open this from your student page.' }, 403);
    if (!env.FEEDBACK_STORE) return json({ error: 'Progress is temporarily unavailable. Please try again.' }, 503);
    const internal = new URL('https://feedback.internal' + url.pathname.slice(4));
    if (url.searchParams.has('after')) internal.searchParams.set('after', url.searchParams.get('after'));
    return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id)).fetch(new Request(internal));
  }

  const communication = /^\/api\/communication\/([a-z-]+)(?:\/(state))?$/.exec(url.pathname);
  if (communication) {
    const activity = COMMUNICATION_ACTIVITIES.find(item => item.id === communication[1]);
    if (!activity) return json({ error: 'Activity not found.' }, 404);
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    const methods = communication[2] ? ['GET', 'PATCH'] : ['GET'];
    if (!methods.includes(request.method)) return json({ error: 'Method not allowed.' }, 405, { Allow: methods.join(', ') });
    let body;
    if (request.method === 'PATCH') {
      if (session.role !== 'student') return json({ error: 'Teacher view is read-only. Only the student can save choices.' }, 403);
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload and try again.' }, 403);
      if (!(await (env.PRACTICE_LIMITER || env.ACCOUNT_LIMITER).limit({ key: account.id })).success) return json({ error: 'Please wait a minute, then try again.' }, 429, { 'Retry-After': '60' });
      body = await smallJson(request, 1024);
      if (!body) return json({ error: 'Please check your choice.' }, 400);
    } else if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Please open this from your student page.' }, 403);
    if (!communication[2]) return json(activity);
    if (!env.FEEDBACK_STORE) return json({ error: 'Practice is temporarily unavailable.' }, 503);
    return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id)).fetch(new Request('https://feedback.internal/communication/' + activity.id + '/state', { method: request.method, ...(body ? { body: JSON.stringify(body) } : {}) }));
  }

  if (['/api/grammar-practice', '/api/business-terms', '/api/vocabulary-practice'].includes(url.pathname)) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    if (request.method !== 'GET') return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET' });
    // Shared exercise content only. No learner answers, attempts, or progress writes.
    return json({ items: url.pathname === '/api/vocabulary-practice' ? vocabularyBank.items : url.pathname === '/api/business-terms' ? businessTermsBank.items : grammarBank.items });
  }

  if (['/api/vocabulary-practice/state', '/api/business-terms/state', '/api/grammar-practice/state', '/api/study/state', '/api/study/questions'].includes(url.pathname)) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    if (url.pathname === '/api/study/questions' && request.method !== 'GET') return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET' });
    if (!['GET', 'PATCH'].includes(request.method)) return json({ error: 'Method not allowed.' }, 405, { Allow: 'GET, PATCH' });
    let body;
    if (request.method === 'PATCH') {
      if (session.role !== 'student') return json({ error: 'Only the student can change these choices. Teacher view is read-only.' }, 403);
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
      const limit = await (env.PRACTICE_LIMITER || env.ACCOUNT_LIMITER).limit({ key: account.id });
      if (!limit.success) return json({ error: 'Please wait a minute, then try saving again.' }, 429, { 'Retry-After': '60' });
      body = await smallJson(request, url.pathname === '/api/vocabulary-practice/state' ? 65536 : 1024);
      if (!body) return json({ error: 'Please check your choice.' }, 400);
    } else if (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site') return json({ error: 'Please open this from your student page.' }, 403);
    if (!env.FEEDBACK_STORE) return json({ error: 'Practice is temporarily unavailable. Please try again.' }, 503);
    const internalUrl = new URL('https://feedback.internal/' + (url.pathname.startsWith('/api/study/') ? url.pathname.slice(5) : (url.pathname === '/api/vocabulary-practice/state' ? 'vocabulary' : url.pathname === '/api/grammar-practice/state' ? 'grammar' : 'terms') + '/state'));
    if (url.searchParams.has('after')) internalUrl.searchParams.set('after', url.searchParams.get('after'));
    return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id)).fetch(new Request(internalUrl, {
      method: request.method, ...(body ? { body: JSON.stringify(body) } : {}),
    }));
  }

  if (url.pathname.startsWith('/api/road/')) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    const route = url.pathname.slice('/api'.length);
    if (!['/road/state', '/road/start', '/road/answer', '/road/end', '/road/questions'].includes(route)) return json({ error: 'Page not found.' }, 404);
    if (session.role !== 'student' && !(['/road/state', '/road/questions'].includes(route) && request.method === 'GET')) return json({ error: 'Teacher previews do not save student practice.' }, 403);
    const method = route === '/road/questions' ? (request.method === 'GET' ? 'GET' : 'PATCH') : route === '/road/state' ? 'GET' : 'POST';
    if (request.method !== method) return json({ error: 'Method not allowed.' }, 405, { Allow: method });
    let body;
    if (method !== 'GET') {
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
      const limit = await (env.PRACTICE_LIMITER || env.ACCOUNT_LIMITER).limit({ key: account.id });
      if (!limit.success) return json({ error: 'Please wait a minute, then try saving again.' }, 429, { 'Retry-After': '60' });
      body = await smallJson(request);
      if (!body) return json({ error: 'Please check your choice.' }, 400);
    }
    if (method === 'GET' && (request.headers.has('Origin') && request.headers.get('Origin') !== url.origin || request.headers.get('Sec-Fetch-Site') === 'cross-site')) return json({ error: 'Please open this from your student page.' }, 403);
    if (!env.FEEDBACK_STORE) return json({ error: 'Practice is temporarily unavailable. Please try again.' }, 503);
    return env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id)).fetch(new Request('https://feedback.internal' + route + (route === '/road/questions' ? url.search : ''),
      { method, ...(body ? { body: JSON.stringify(body) } : {}) }));
  }
  if (url.pathname.startsWith('/api/quiz/')) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    const route = url.pathname.slice('/api'.length);
    const history = route === '/quiz/results' || route.startsWith('/quiz/results/');
    if (!history && !['/quiz/state', '/quiz/answer'].includes(route)) return json({ error: 'Page not found.' }, 404);
    if (history ? session.role !== 'teacher' : session.role !== 'student') return json({ error: history ? 'Only your teacher can open quiz history.' : 'Teacher practice does not save student results.' }, 403);
    const method = route === '/quiz/answer' ? 'POST' : 'GET';
    if (request.method !== method) return json({ error: 'Method not allowed.' }, 405, { Allow: method });
    let body;
    if (method === 'POST') {
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
      body = await smallJson(request, 1024);
      if (!body) return json({ error: 'Please choose an answer.' }, 400);
    }
    if (!env.FEEDBACK_STORE) return json({ error: 'Quiz results are temporarily unavailable.' }, 503);
    const store = env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id));
    const internalUrl = new URL('https://feedback.internal' + route);
    for (const name of ['before', 'new']) if (url.searchParams.has(name)) internalUrl.searchParams.set(name, url.searchParams.get(name));
    return store.fetch(new Request(internalUrl, { method, ...(body ? { body: JSON.stringify(body) } : {}) }));
  }

  const isAssessment = url.pathname === '/api/assessment';
  if (isAssessment || url.pathname === '/api/feedback' || url.pathname.startsWith('/api/feedback/')) {
    const session = await readSession(request, env, account);
    if (!session) return json({ error: 'Please sign in to continue.' }, 401);
    const id = isAssessment ? 'assessment' : url.pathname === '/api/feedback' ? '' : url.pathname.slice('/api/feedback/'.length);
    if (!isAssessment && ((id && !FEEDBACK_ID.test(id)) || (!id && url.pathname.endsWith('/')))) return json({ error: 'Session not found.' }, 404);
    if (!['GET', 'HEAD', 'PUT', 'PATCH'].includes(request.method) || request.method === 'PATCH' && (isAssessment || !id)) return json({ error: 'Method not allowed.' }, 405);
    let body;
    if (['PUT', 'PATCH'].includes(request.method)) {
      if (session.role !== 'teacher') return json({ error: 'Only your teacher can publish learning records.' }, 403);
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Please reload the page and try again.' }, 403);
      try {
        const input = await smallJson(request, 65536);
        body = request.method === 'PATCH' ? validatePracticeEdit(input) : isAssessment ? validateAssessment(input) : validateFeedback(input, id);
        if (isAssessment && Object.hasOwn(input, 'priorAssessment')) body.priorAssessment = input.priorAssessment === null ? null : validateAssessment(input.priorAssessment);
      }
      catch { return json({ error: 'Please check the record format and transcript references.' }, 400); }
    }
    if (!env.FEEDBACK_STORE) return json({ error: 'Learning records are temporarily unavailable.' }, 503);
    const store = env.FEEDBACK_STORE.get(env.FEEDBACK_STORE.idFromName(account.id));
    const internalUrl = new URL(`https://feedback.internal/${id}`);
    if (!id && url.searchParams.has('before')) internalUrl.searchParams.set('before', url.searchParams.get('before'));
    const response = await store.fetch(new Request(internalUrl, body ? { method: request.method, body: JSON.stringify(body) } : {}));
    const data = await response.json();
    // Keep source-note identifiers on the server; neither role needs a Zoom link.
    if (data.source) delete data.source.noteId;
    return json(data, response.status);
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
  async scheduled(event, env) {
    if (!env.QUIZ_AUTOMATION || !nightlyDate(event.scheduledTime)) return;
    await env.QUIZ_AUTOMATION.get(env.QUIZ_AUTOMATION.idFromName('zoom')).fetch(new Request('https://automation.internal/run', { method: 'POST', body: JSON.stringify({ scheduledTime: event.scheduledTime }) }));
  },
  async fetch(request, env) {
    try { return protect(await handle(request, env)); }
    catch (error) {
      const category = runtimeErrorCategory(error);
      console.error('Student service unavailable:', category);
      if (category === 'request_allowance') {
        const reset = new Date((Math.floor(Date.now() / 86400000) + 1) * 86400000);
        const resetTime = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', month: 'long', day: 'numeric', hour: 'numeric', minute: '2-digit' }).format(reset);
        return protect(json({ error: 'The daily hosting request allowance has been reached. Please try again after ' + resetTime + ' Eastern.', retryAt: reset.toISOString() }, 503,
          { 'Retry-After': String(Math.max(1, Math.ceil((reset.getTime() - Date.now()) / 1000))) }));
      }
      const directory = new URL(request.url).pathname === '/api/admin/students';
      return protect(json({ error: directory ? 'The student directory is temporarily unavailable. Please try Refresh shortly.' : 'Sign-in is temporarily unavailable. Please try again shortly.' }, 503));
    }
  },
};
