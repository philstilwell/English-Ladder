const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const windows = [];
afterEach(() => { windows.splice(0).forEach(dom => dom.window.close()); });
const key = 'english-ladder-vocabulary-language-v1';
const definitions = { ja: '競技で誰が勝つかを決める人。', ko: '대회에서 누가 이기는지 결정하는 사람.', 'zh-Hans': '决定比赛中谁获胜的人。', es: 'Una persona que decide quién gana una competición.', 'pt-BR': 'Uma pessoa que decide quem vence uma competição.', fr: 'Une personne qui décide qui gagne une compétition.', de: 'Eine Person, die entscheidet, wer einen Wettbewerb gewinnt.' };

function load(saved, options = {}) {
  const fixture = `<details class="daily-lesson"><div class="lesson-content"><div data-stage="read"><div class="section"><p>A <strong>judge</strong> decides.</p></div><div class="vocab-box"><span class="vocab-term">1. judge (noun):</span> <span class="vocab-definition" lang="en">A person who decides who wins.</span></div><p data-word-hint hidden></p></div><div data-stage="practice"><h2>Practice</h2></div><div data-stage="discuss"><h2>Discuss</h2><p class="completion-message" hidden></p></div></div></details>`;
  const dom = new JSDOM(fixture.repeat(2), { url: 'https://englishladder.com/beginner.html', runScripts: 'outside-only' });
  windows.push(dom);
  dom.window.HTMLElement.prototype.scrollIntoView = function () {};
  if (saved) dom.window.localStorage.setItem(key, saved);
  if (options.blockStorage) Object.defineProperty(dom.window, 'localStorage', { get() { throw new Error('blocked'); } });
  dom.window.document.querySelectorAll('.vocab-definition').forEach(span => {
    span.dataset.translations = options.corrupt ? '{bad JSON' : JSON.stringify(definitions);
  });
  dom.window.eval(fs.readFileSync(path.join(root, 'learning.js'), 'utf8'));
  return dom;
}

test('all seven languages switch definitions and already-open word help across lessons, then reset to English', () => {
  const dom = load(); const d = dom.window.document;
  const word = d.querySelector('.word-button'); word.click();
  for (const [language, text] of Object.entries(definitions)) {
    d.querySelector(`[data-definition-language="${language}"]`).click();
    for (const lesson of d.querySelectorAll('.daily-lesson')) {
      assert.equal(lesson.querySelector('.vocab-definition').textContent, text);
      assert.equal(lesson.querySelector('.vocab-definition').lang, language);
      assert.equal(lesson.querySelector('.word-definition').textContent.trim(), `(${text})`);
      assert.equal(lesson.querySelector('.word-definition').lang, language);
      assert.equal(lesson.querySelectorAll('.vocabulary-language[aria-pressed="true"]').length, 1);
      assert.equal(lesson.querySelector('.vocab-term').textContent, '1. judge (noun):');
    }
    assert.equal(dom.window.localStorage.getItem(key), language);
    assert.equal(d.getElementById(word.getAttribute('aria-controls')).hidden, false);
  }
  d.querySelector('[data-definition-language="en"]').click();
  assert.equal(d.querySelector('.vocab-definition').textContent, 'A person who decides who wins.');
  assert.equal(d.querySelector('.vocab-definition').lang, 'en');
  assert.equal(d.querySelector('[data-definition-language="zh-Hans"]').getAttribute('aria-label'), 'Chinese');
  assert.equal(d.querySelector('[data-definition-language="pt-BR"]').getAttribute('aria-label'), 'Portuguese');
});

test('preference restores on another level and follows changes from another tab or restored page', () => {
  const dom = load('ja'); const d = dom.window.document;
  assert.equal(d.querySelector('.vocab-definition').lang, 'ja');
  dom.window.localStorage.setItem(key, 'pt-BR');
  dom.window.dispatchEvent(new dom.window.StorageEvent('storage', { key }));
  assert.equal(d.querySelector('.vocab-definition').lang, 'pt-BR');
  dom.window.localStorage.setItem(key, 'ko');
  dom.window.dispatchEvent(new dom.window.PageTransitionEvent('pageshow', { persisted: true }));
  assert.equal(d.querySelector('.vocab-definition').lang, 'ko');
  dom.window.localStorage.clear();
  dom.window.dispatchEvent(new dom.window.StorageEvent('storage', { key: null }));
  assert.equal(d.querySelector('.vocab-definition').lang, 'en');
});

test('missing translation data explicitly falls back; blocked storage does not break controls', () => {
  const dom = load('ja', { corrupt: true }); const d = dom.window.document;
  assert.equal(d.querySelector('.vocab-definition').lang, 'en');
  assert.match(d.querySelector('.vocabulary-language-status').textContent, /unavailable.*English/);
  const blocked = load(null, { blockStorage: true });
  blocked.window.document.querySelector('[data-definition-language="es"]').click();
  assert.equal(blocked.window.document.querySelector('.vocab-definition').textContent, definitions.es);
});

test('definition content is displayed as text without executing markup', () => {
  const previous = definitions.es;
  definitions.es = '<img src=x onerror="window.unwanted=true">';
  const dom = load('es');
  definitions.es = previous;
  assert.equal(dom.window.document.querySelector('.vocab-definition img'), null);
  assert.match(dom.window.document.querySelector('.vocab-definition').textContent, /^<img/);
  assert.equal(dom.window.unwanted, undefined);
});

test('opening a definition announces its actual language and Escape keeps keyboard focus on the word', () => {
  const dom = load('ko'); const d = dom.window.document;
  const lesson = d.querySelector('.daily-lesson'); lesson.open = true;
  const word = lesson.querySelector('.word-button');
  const announcement = lesson.querySelector('.word-announcement');
  assert.equal(announcement.getAttribute('role'), 'status');
  assert.equal(announcement.textContent, '');
  word.focus(); word.click();
  assert.equal(d.activeElement, word);
  assert.equal(announcement.lang, 'ko');
  assert.ok(announcement.textContent.includes(definitions.ko));
  assert.equal(word.getAttribute('aria-describedby'), word.getAttribute('aria-controls'));
  word.dispatchEvent(new dom.window.KeyboardEvent('keydown', {key: 'Escape'}));
  assert.equal(d.activeElement, word);
  assert.equal(announcement.textContent, '');
  assert.equal(word.hasAttribute('aria-describedby'), false);
  assert.equal(lesson.querySelector('.word-definition').hidden, true);
  word.click();
  d.querySelector('[data-definition-language="en"]').click();
  assert.equal(announcement.textContent, '');
  assert.equal(lesson.querySelector('.word-definition').lang, 'en');
  assert.equal(word.getAttribute('aria-describedby'), word.getAttribute('aria-controls'));
});
