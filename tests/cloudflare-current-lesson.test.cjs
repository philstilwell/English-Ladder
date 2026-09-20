'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {currentLessonFiles, verifyCurrentLesson} = require('../cloudflare/verify-current-lesson.cjs');

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
