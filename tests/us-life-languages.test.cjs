const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const key = 'english-ladder-vocabulary-language-v1';
const legacyKey = 'englishLadder.usLife.explanationLanguage';
const languages = { ja: 'Japanese', ko: 'Korean', 'zh-Hans': 'Simplified Chinese', es: 'Spanish', 'pt-BR': 'Brazilian Portuguese' };
const windows = [];
afterEach(() => windows.splice(0).forEach(w => w.close()));
const source = file => fs.readFileSync(path.join(root, file), 'utf8');
const settle = () => new Promise(resolve => setImmediate(resolve));

function setup({ saved, legacy, blocked, clipboard, corrupt, reverse } = {}) {
  const w = new JSDOM(source('us-life.html'), { url: 'https://englishladder.com/us-life.html', runScripts: 'outside-only' }).window;
  windows.push(w);
  w.HTMLElement.prototype.scrollIntoView = function () {};
  if (saved) w.localStorage.setItem(key, saved);
  if (legacy) w.localStorage.setItem(legacyKey, legacy);
  if (blocked) Object.defineProperty(w, 'localStorage', { get() { throw new Error('Blocked'); } });
  if (clipboard) Object.defineProperty(w.navigator, 'clipboard', { value: clipboard });
  if (corrupt) w.document.querySelector('[data-us-life-translations]').textContent = corrupt;
  w.fetch = () => { throw new Error('Switching explanation languages must not make a request'); };
  const scripts = reverse ? ['ai-practice.js', 'us-life.js'] : ['us-life.js', 'ai-practice.js'];
  scripts.forEach(file => w.eval(source(file)));
  return w;
}
const choose = (w, language) => w.document.querySelector(`button[data-definition-language="${language}"]`).click();
const external = (w, language) => {
  if (language) w.localStorage.setItem(key, language); else w.localStorage.clear();
  w.dispatchEvent(new w.StorageEvent('storage', { key: language ? key : null }));
};

test('a new visitor sees one inviting language selector in place of How to Study', () => {
  const w = setup(), d = w.document;
  assert.equal(d.querySelector('#life-language-select'), null);
  assert.doesNotMatch(d.querySelector('.us-life-intro').textContent, /How to Study|Use one unit at a time/);
  assert.equal(d.querySelectorAll('[aria-label="Explanation language"]').length, 1);
  assert.equal(d.querySelectorAll('button[data-definition-language]').length, 6);
  assert.equal(d.querySelectorAll('button[data-definition-language]:disabled').length, 0);
  assert.match(d.querySelector('[data-life-language-status]').textContent, /optional.*five languages/);
  assert.match(d.querySelector('.us-life-note').textContent, /official sources/);
  assert.equal(d.querySelectorAll('[data-explanation]:not([hidden])').length, 0);
  assert.equal(d.querySelectorAll('.us-life-module:not([hidden])').length, 1);
  assert.doesNotMatch(d.querySelector('.ai-prompt-text').textContent, /EXPLANATION LANGUAGE AND DEPTH/);
});

test('every language updates all 24 exact reviewed sidebars and AI prompts, preserving English practice and focus', async () => {
  let copied;
  const w = setup({ clipboard: { writeText: async value => { copied = value; } } }), d = w.document;
  const data = JSON.parse(d.querySelector('[data-us-life-translations]').textContent);
  const originalPrompts = [...d.querySelectorAll('.ai-prompt-text')].map(n => n.textContent);
  for (const [language, label] of Object.entries(languages)) {
    const button = d.querySelector(`button[data-definition-language="${language}"]`);
    button.focus(); button.click();
    assert.equal(d.activeElement, button);
    assert.equal(w.localStorage.getItem(key), language);
    assert.equal(d.querySelectorAll('button[data-definition-language][aria-pressed="true"]').length, 1);
    for (const unit of d.querySelectorAll('.us-life-module')) {
      const aside = unit.querySelector('[data-explanation]');
      const content = aside.querySelector('[data-life-explanation-content]');
      assert.equal(aside.hidden, false);
      assert.equal(content.lang, language);
      assert.equal(content.querySelector('h3').textContent, data[unit.id].translations[language].heading);
      assert.deepEqual([...content.querySelectorAll('li')].map(n => n.textContent), data[unit.id].translations[language].points);
      assert.equal(content.querySelector('.language-practice').textContent, data[unit.id].practice);
      assert.equal(content.querySelector('.language-practice').lang, 'en');
      assert.ok(unit.querySelector('.life-practice').textContent.includes(data[unit.id].practice));
      for (const prompt of unit.querySelectorAll('.ai-prompt-text')) {
        assert.ok(prompt.textContent.includes(`My explanation language is ${label}.`));
        assert.equal(prompt.textContent.split('EXPLANATION LANGUAGE AND DEPTH').length, 2);
      }
    }
    d.querySelector('[data-ai-copy-text]').click(); await settle();
    assert.equal(copied, d.querySelector('.ai-prompt-text').textContent);
  }
  choose(w, 'en');
  assert.deepEqual([...d.querySelectorAll('.ai-prompt-text')].map(n => n.textContent), originalPrompts);
  assert.equal(d.querySelectorAll('[data-explanation]:not([hidden])').length, 0);
});

test('the news language preference applies on arrival, across tabs, and on browser Back restores', () => {
  const w = setup({ saved: 'pt-BR' }), d = w.document;
  assert.equal(d.querySelector('[data-life-explanation-content]').lang, 'pt-BR');
  external(w, 'ko');
  assert.equal(d.querySelector('[data-life-explanation-content]').lang, 'ko');
  assert.match(d.querySelector('.ai-prompt-text').textContent, /My explanation language is Korean\./);
  w.localStorage.setItem(key, 'zh-Hans');
  w.dispatchEvent(new w.PageTransitionEvent('pageshow', { persisted: true }));
  assert.equal(d.querySelector('[data-life-explanation-content]').lang, 'zh-Hans');
  external(w, null);
  assert.equal(d.querySelector('[data-explanation]').hidden, true);
  assert.doesNotMatch(d.querySelector('.ai-prompt-text').textContent, /EXPLANATION LANGUAGE AND DEPTH/);
});

test('legacy Japanese and Mandarin choices migrate without overriding a newer sitewide preference', () => {
  for (const [legacy, expected] of [['ja', 'ja'], ['zh', 'zh-Hans'], ['en', 'en']]) {
    const w = setup({ legacy });
    assert.equal(w.localStorage.getItem(key), expected);
    assert.equal(w.document.querySelector(`button[data-definition-language="${expected}"]`).getAttribute('aria-pressed'), 'true');
  }
  const w = setup({ saved: 'es', legacy: 'ja' });
  assert.equal(w.document.querySelector('[data-life-explanation-content]').lang, 'es');
});

test('blocked storage and either script order preserve the sidebar and prompt connection', () => {
  for (const reverse of [false, true]) {
    const w = setup({ blocked: true, reverse });
    choose(w, 'ja');
    assert.equal(w.document.querySelector('[data-life-explanation-content]').lang, 'ja');
    assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Japanese\./);
    choose(w, 'en');
    assert.doesNotMatch(w.document.querySelector('.ai-prompt-text').textContent, /EXPLANATION LANGUAGE AND DEPTH/);
  }
});

test('missing or corrupt translations explain the problem without showing a different foreign language', () => {
  for (const corrupt of ['{bad JSON', '{}', 'null', '[]']) {
    const w = setup({ saved: 'ko', corrupt }), d = w.document;
    assert.match(d.querySelector('[data-life-explanation-content]').textContent, /Korean explanations are unavailable/);
    assert.equal(d.querySelector('[data-life-explanation-content]').lang, 'en');
    assert.match(d.querySelector('.ai-prompt-text').textContent, /My explanation language is Korean\./);
    assert.equal(d.querySelectorAll('.us-life-module:not([hidden])').length, 1);
  }
  const w = setup({ saved: '__proto__' });
  assert.equal(w.document.querySelector('button[data-definition-language="en"]').getAttribute('aria-pressed'), 'true');
});

test('unit navigation keeps the chosen language and manual copying selects the adapted prompt', async () => {
  const w = setup({ saved: 'es' }), d = w.document;
  const select = d.querySelector('[aria-label="Study unit"]');
  const navigated = new Promise(resolve => w.addEventListener('hashchange', resolve, { once: true }));
  select.value = 'dry-cleaning'; select.dispatchEvent(new w.Event('change'));
  await navigated;
  const unit = d.querySelector('#dry-cleaning');
  assert.equal(unit.hidden, false);
  assert.equal(unit.querySelector('[data-life-explanation-content]').lang, 'es');
  unit.querySelector('[data-ai-copy-text]').click(); await settle();
  assert.equal(w.getSelection().toString(), unit.querySelector('.ai-prompt-text').textContent);
  assert.match(w.getSelection().toString(), /My explanation language is Spanish\./);
});


test('skip and language-section links do not reset the selected unit', async () => {
  const w = setup(), d = w.document;
  async function navigate(hash) {
    const moved = new Promise(resolve => w.addEventListener('hashchange', resolve, { once: true }));
    w.location.hash = hash;
    await moved;
  }
  await navigate('shopping');
  assert.equal(d.querySelector('.us-life-module:not([hidden])').id, 'shopping');
  await navigate('life-language-controls');
  assert.equal(d.querySelector('.us-life-module:not([hidden])').id, 'shopping');
  await navigate('main-content');
  assert.equal(d.querySelector('.us-life-module:not([hidden])').id, 'shopping');
  assert.equal(d.querySelector('[data-life-start]').getAttribute('href'), '#life-language-controls');
});
