const {test, afterEach} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.join(__dirname, '..');
const windows = [];
afterEach(() => windows.splice(0).forEach(dom => dom.window.close()));

const html = fs.readFileSync(path.join(root, 'beginner.html'), 'utf8');
const lessonIds = [...html.matchAll(/id="(lesson-\d{4}-\d{2}-\d{2})"/g)].map(match => match[1]);
const targetId = lessonIds[2];
const otherId = lessonIds[4];
function load(hash = '#'+targetId) {
  const scrolls = [];
  const dom = new JSDOM(html, {
    url: 'https://englishladder.com/beginner.html'+hash, runScripts: 'dangerously',
    beforeParse(window) {
      window.HTMLElement.prototype.scrollIntoView = function() { scrolls.push(this.id); };
    },
  });
  windows.push(dom);
  return {window: dom.window, document: dom.window.document, scrolls};
}
function run(window, file) { window.eval(fs.readFileSync(path.join(root, file), 'utf8')); }

test('dated links open during HTML parsing before external interactions arrive', () => {
  const {document} = load();
  assert.ok(document.documentElement.classList.contains('reading-js'));
  assert.deepEqual([...document.querySelectorAll('.daily-lesson[open]')].map(x => x.id), [targetId]);
  const lesson = document.getElementById(targetId);
  assert.equal(lesson.querySelectorAll('.learning-flow').length, 1);
  assert.equal(lesson.querySelectorAll('.learning-flow button:disabled').length, 3);
  assert.equal(lesson.querySelectorAll('.vocabulary-language:disabled').length, 6);
  assert.equal(lesson.querySelector('[data-stage="read"] .section').previousElementSibling.dataset.wordHint, '');
  // All content remains in the document; CSS alone selects the initial read view.
  assert.equal(lesson.querySelectorAll('.learning-panel[hidden]').length, 0);
});

test('initialization reuses published controls and does not scroll a preopened lesson again', () => {
  const {window, document, scrolls} = load();
  const lesson = document.getElementById(targetId);
  const nav = lesson.querySelector('.learning-flow');
  const practice = nav.children[1];
  const language = lesson.querySelector('[data-definition-language="ja"]');
  run(window, 'learning.js');
  run(window, 'site.js');
  window.dispatchEvent(new window.Event('load'));
  assert.equal(lesson.querySelector('.learning-flow'), nav);
  assert.equal(lesson.querySelector('.learning-flow').children[1], practice);
  assert.equal(lesson.querySelector('[data-definition-language="ja"]'), language);
  assert.equal(lesson.querySelectorAll('.stage-actions').length, 3);
  assert.equal(lesson.querySelectorAll('button:disabled').length, 0);
  assert.deepEqual(scrolls, []);
  practice.click();
  assert.equal(lesson.querySelector('[data-stage="practice"]').hidden, false);
  window.location.hash = '#'+otherId;
  window.dispatchEvent(new window.HashChangeEvent('hashchange'));
  assert.ok(document.getElementById(otherId).open);
  assert.ok(scrolls.includes(otherId));
});

test('failed interaction downloads restore the plain reading view', () => {
  const {window, document} = load();
  document.querySelector('script[src*="learning.js"]').dispatchEvent(new window.Event('error'));
  assert.equal(document.documentElement.classList.contains('reading-js'), false);
  assert.equal(document.querySelectorAll('.learning-panel[hidden]').length, 0);
  assert.ok(document.querySelector('.learning-flow').hidden);
});

test('malformed fragments do not break parsing or open unrelated lessons', () => {
  const {document} = load('#lesson-%E0%A4%A');
  assert.equal(document.querySelectorAll('.daily-lesson[open]').length, 0);
});
