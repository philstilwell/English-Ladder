'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {checkDailyPublication} = require('../cloudflare/check-daily-publication.cjs');

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'daily-publication-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  const releaseDate = '2026-10-20';
  const levels = ['beginner', 'intermediate', 'advanced'];
  const image = `assets/news/${releaseDate}-abcdef123456.webp`;
  const bodies = new Map([
    ['index.html', `news/${releaseDate}`],
    ['archive.html', levels.map(level => `news/${releaseDate}/${level}.html`).join(' ')],
    ['lesson-data.json', JSON.stringify(Object.fromEntries(levels.map(level =>
      [level, {url: `news/${releaseDate}/${level}.html`}])))] ,
    [`archive/lessons/${releaseDate}.json`, JSON.stringify({
      release_date: releaseDate,
      levels: Object.fromEntries(levels.map(level => [level, {file_path: `${level}.html`}])),
    })],
    [`assets/news/${releaseDate}.json`, JSON.stringify({path: image})],
    [image, 'saved image bytes'],
  ]);
  for (const level of levels) {
    bodies.set(`${level}.html`, `news/${releaseDate}/${level}.html`);
    bodies.set(`news/${releaseDate}/${level}.html`, `Lesson ${releaseDate}`);
  }
  for (const [file, body] of bodies) {
    fs.mkdirSync(path.dirname(path.join(root, file)), {recursive: true});
    fs.writeFileSync(path.join(root, file), body);
  }
  bodies.set('/', `news/${releaseDate}`);
  const request = async url => {
    const file = url.pathname === '/' ? '/' : url.pathname.slice(1);
    return {status: bodies.has(file) ? 200 : 404, body: Buffer.from(bodies.get(file) || 'Not found')};
  };
  return {options: {root, releaseDate, origin: new URL('https://example.invalid'), request, sleep: async () => {}},
    bodies, image};
}

test('a complete live edition is verified without packaging or rendering any files', async t => {
  const {options} = fixture(t);
  const result = await checkDailyPublication(options);
  assert.equal(result.releaseDate, options.releaseDate);
  assert.equal(fs.existsSync(path.join(options.root, '.cf-site')), false);
});

test('a stale homepage cannot qualify as a published daily edition', async t => {
  const {options, bodies} = fixture(t);
  bodies.set('index.html', 'news/2026-10-19');
  await assert.rejects(checkDailyPublication(options), /missing news\/2026-10-20/);
});

test('a missing lesson level prevents the shortcut', async t => {
  const {options, bodies} = fixture(t);
  bodies.delete('news/2026-10-20/advanced.html');
  await assert.rejects(checkDailyPublication(options), /expected HTTP 200, got 404/);
});

test('different live lesson data prevents the shortcut', async t => {
  const {options, bodies} = fixture(t);
  bodies.set('archive/lessons/2026-10-20.json', '{"release_date":"2026-10-19"}');
  await assert.rejects(checkDailyPublication(options), /content mismatch/);
});

test('a missing or corrupt illustration prevents the shortcut', async t => {
  const {options, bodies, image} = fixture(t);
  bodies.set(image, 'corrupt live image');
  await assert.rejects(checkDailyPublication(options), /content mismatch/);
  bodies.delete(image);
  await assert.rejects(checkDailyPublication(options), /expected HTTP 200, got 404/);
});

test('a blocked host is inconclusive, never a shortcut success', async t => {
  const {options} = fixture(t);
  options.request = async () => ({status: 403, body: Buffer.from('Blocked')});
  await assert.rejects(checkDailyPublication(options), /expected HTTP 200, got 403/);
});
