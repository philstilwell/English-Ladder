'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {
  currentLessonFiles,
  isAllowedPublicEdgeBlock,
  verifyCurrentLesson,
  waitForCurrentLesson
} = require('../cloudflare/verify-current-lesson.cjs');

const origin = new URL('https://englishladder.example/');
const releaseDate = '2026-09-19';
const levels = ['beginner', 'intermediate', 'advanced'];
const hash = body => crypto.createHash('sha256').update(body).digest('hex');

function jsonBuffer(value) {
  return Buffer.from(JSON.stringify(value));
}

function fixture({badLessonDataHash = false} = {}) {
  const archiveBody = jsonBuffer({
    release_date: releaseDate,
    levels: Object.fromEntries(levels.map(level => [level, {file_path: `${level}.html`}]))
  });
  const lessonDataBody = jsonBuffer(Object.fromEntries(
    levels.map(level => [level, {url: `news/${releaseDate}/${level}.html`}])
  ));
  const responses = new Map([
    ['index.html', Buffer.from(`<a href="news/${releaseDate}">current date</a><script>edge-added</script>`)],
    ['archive.html', Buffer.from(levels.map(level => `<a href="news/${releaseDate}/${level}.html">${level}</a>`).join(''))],
    ['lesson-data.json', lessonDataBody],
    [`archive/lessons/${releaseDate}.json`, archiveBody],
    ['beginner.html', Buffer.from(`<a href="news/${releaseDate}/beginner.html">beginner</a>`)],
    ['intermediate.html', Buffer.from(`<a href="news/${releaseDate}/intermediate.html">intermediate</a>`)],
    ['advanced.html', Buffer.from(`<a href="news/${releaseDate}/advanced.html">advanced</a>`)],
    [`news/${releaseDate}/beginner.html`, Buffer.from(`Beginner lesson ${releaseDate}`)],
    [`news/${releaseDate}/intermediate.html`, Buffer.from(`Intermediate lesson ${releaseDate}`)],
    [`news/${releaseDate}/advanced.html`, Buffer.from(`Advanced lesson ${releaseDate}`)],
    ['/', Buffer.from(`<a href="news/${releaseDate}">root current date</a><script>edge-added</script>`)],
  ]);
  const manifest = {files: {}};
  for (const file of currentLessonFiles(releaseDate)) {
    const body = responses.get(file);
    manifest.files[file] = file.endsWith('.json') ? hash(body) : 'html-can-change-at-the-edge';
  }
  if (badLessonDataHash) {
    manifest.files['lesson-data.json'] = hash(Buffer.from('older lesson data'));
  }
  const request = async url => {
    const file = url.pathname === '/' ? '/' : url.pathname.slice(1);
    if (responses.has(file)) return {status: 200, body: responses.get(file)};
    return {status: 404, body: Buffer.from('Not found')};
  };
  return {manifest, request};
}

test('current lesson verification checks current paths without byte-matching HTML', async () => {
  const {manifest, request} = fixture();
  const result = await verifyCurrentLesson(manifest, {
    origin,
    request,
    releaseDate,
    sleep: async () => {},
  });
  assert.deepEqual(result, {releaseDate, files: currentLessonFiles(releaseDate).length});
});

test('current lesson verification still byte-checks lesson JSON', async () => {
  const {manifest, request} = fixture({badLessonDataHash: true});
  await assert.rejects(verifyCurrentLesson(manifest, {
    origin,
    request,
    releaseDate,
    sleep: async () => {},
  }), /lesson-data\.json: content mismatch/);
});

test('public edge-block warnings require the explicit workflow flag', () => {
  const original = process.env.ALLOW_PUBLIC_EDGE_BLOCK;
  try {
    const blocked = new Error('index.html: expected HTTP 200, got 403');
    const missing = new Error('index.html: expected HTTP 200, got 404');
    delete process.env.ALLOW_PUBLIC_EDGE_BLOCK;
    assert.equal(isAllowedPublicEdgeBlock(blocked), false);
    process.env.ALLOW_PUBLIC_EDGE_BLOCK = '1';
    assert.equal(isAllowedPublicEdgeBlock(blocked), true);
    assert.equal(isAllowedPublicEdgeBlock(missing), false);
  } finally {
    if (original === undefined) delete process.env.ALLOW_PUBLIC_EDGE_BLOCK;
    else process.env.ALLOW_PUBLIC_EDGE_BLOCK = original;
  }
});

function publicationClock() {
  let now = 0;
  const delays = [];
  const messages = [];
  return {
    delays, messages,
    advance: milliseconds => { now += milliseconds; },
    options: {
      origin, releaseDate, timeoutMs: 35_000, intervalMs: 10_000,
      clock: () => now,
      sleep: async milliseconds => { delays.push(milliseconds); now += milliseconds; },
      log: message => messages.push(message),
    },
  };
}

test('a matching manifest can precede the public lesson: retry its ordinary URL until available', async () => {
  const {manifest, request} = fixture();
  const timer = publicationClock();
  const lesson = `/news/${releaseDate}/beginner.html`;
  const urls = [];
  let attempts = 0;
  const result = await waitForCurrentLesson(manifest, {
    ...timer.options,
    request: async url => {
      urls.push(url);
      if (url.pathname === lesson && ++attempts < 3) return {status: 404, body: Buffer.from('Not found')};
      return request(url);
    },
  });
  assert.equal(result.releaseDate, releaseDate);
  assert.deepEqual(timer.delays, [10_000, 10_000]);
  assert.equal(attempts, 3);
  assert.ok(urls.every(url => !url.search));
  assert.ok(urls.some(url => url.pathname === '/.git/config'));
  assert.equal(timer.messages.length, 1);
});

test('a permanently missing public lesson still fails at the shared deadline', async () => {
  const {manifest, request} = fixture();
  const timer = publicationClock();
  let attempts = 0;
  await assert.rejects(waitForCurrentLesson(manifest, {
    ...timer.options,
    request: async url => {
      if (url.pathname === `/news/${releaseDate}/beginner.html`) {
        attempts++;
        return {status: 404, body: Buffer.from('Not found')};
      }
      return request(url);
    },
  }), /within 35s: news\/.*\/beginner\.html: expected HTTP 200, got 404/);
  assert.equal(attempts, 4);
  assert.deepEqual(timer.delays, [10_000, 10_000, 10_000, 5000]);
});

test('stale JSON and stale HTML must become correct, not just return HTTP 200', async () => {
  for (const file of ['/lesson-data.json', '/index.html']) {
    const {manifest, request} = fixture();
    const timer = publicationClock();
    let attempts = 0;
    await waitForCurrentLesson(manifest, {
      ...timer.options,
      request: async url => {
        if (url.pathname === file && ++attempts < 3) return {status: 200, body: Buffer.from('old edition')};
        return request(url);
      },
    });
    assert.deepEqual(timer.delays, [10_000, 10_000]);
    const persistent = publicationClock();
    await assert.rejects(waitForCurrentLesson(manifest, {
      ...persistent.options,
      request: async url => url.pathname === file ? {status: 200, body: Buffer.from('old edition')} : request(url),
    }), /did not become available/);
  }
});

test('exposed private files, redirects, authentication and certificate failures are immediate', async () => {
  for (const [file, response] of [
    ['/.git/config', {status: 200, body: Buffer.from('exposed')}],
    ['/index.html', {status: 301, body: Buffer.from('redirect')}],
    ['/index.html', {status: 401, body: Buffer.from('unauthorized')}],
    ['/index.html', Object.assign(new Error('private certificate diagnostic'), {retryable: false})],
  ]) {
    const {manifest, request} = fixture();
    const timer = publicationClock();
    let attempts = 0;
    await assert.rejects(waitForCurrentLesson(manifest, {
      ...timer.options,
      request: async url => {
        if (url.pathname !== file) return request(url);
        attempts++;
        if (response instanceof Error) throw response;
        return response;
      },
    }), error => !error.message.includes('private certificate diagnostic'));
    assert.equal(attempts, 1);
    assert.deepEqual(timer.delays, []);
  }
});

test('temporary transport failures preserve retryability without leaking diagnostics', async () => {
  const {manifest, request} = fixture();
  const timer = publicationClock();
  let attempts = 0;
  await waitForCurrentLesson(manifest, {
    ...timer.options,
    request: async url => {
      if (++attempts === 1) throw Object.assign(new Error('private network detail'), {retryable: true});
      return request(url);
    },
  });
  assert.deepEqual(timer.delays, [10_000]);
  assert.ok(timer.messages.every(message => !message.includes('private network detail')));
});

test('one budget covers requests, waits, and all public files', async () => {
  const {manifest, request} = fixture();
  const timer = publicationClock();
  const timeouts = [];
  await assert.rejects(waitForCurrentLesson(manifest, {
    ...timer.options,
    request: async (url, {timeoutMs}) => {
      timeouts.push(timeoutMs);
      timer.advance(Math.min(20_000, timeoutMs));
      return request(url);
    },
  }), /did not become available within 35s/);
  assert.deepEqual(timeouts, [30_000, 15_000]);
  assert.deepEqual(timer.delays, []);
});

test('a missing saved lesson fails before any request or publication wait', async () => {
  const {manifest} = fixture();
  delete manifest.files[`news/${releaseDate}/beginner.html`];
  const timer = publicationClock();
  await assert.rejects(waitForCurrentLesson(manifest, {
    ...timer.options,
    request: async () => assert.fail('Must not fetch an unsaved edition'),
  }), /Deployment manifest does not include/);
  assert.deepEqual(timer.delays, []);
});
