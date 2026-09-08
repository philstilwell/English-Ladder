const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const key = 'english-ladder-vocabulary-language-v1';
const languages = { ja: 'Japanese', ko: 'Korean', 'zh-Hans': 'Simplified Chinese', es: 'Spanish', 'pt-BR': 'Brazilian Portuguese' };
const windows = [];
afterEach(() => windows.splice(0).forEach(dom => dom.window.close()));
const source = name => fs.readFileSync(path.join(root, name), 'utf8');
const settle = () => new Promise(resolve => setImmediate(resolve));

function load(file, { saved, blockedStorage, clipboard } = {}) {
  const dom = new JSDOM(source(file), { url: `https://englishladder.com/${file}`, runScripts: 'outside-only' });
  windows.push(dom);
  const w = dom.window;
  w.HTMLElement.prototype.scrollIntoView = function () {};
  if (saved) w.localStorage.setItem(key, saved);
  if (blockedStorage) Object.defineProperty(w, 'localStorage', { get() { throw new Error('Blocked'); } });
  if (clipboard) Object.defineProperty(w.navigator, 'clipboard', { value: clipboard });
  w.fetch = () => { throw new Error('Language selection must not contact an AI service'); };
  return w;
}
function run(w, ...scripts) { scripts.forEach(name => w.eval(source(name))); }
function externalLanguage(w, value) {
  if (value === null) w.localStorage.clear();
  else w.localStorage.setItem(key, value);
  w.dispatchEvent(new w.StorageEvent('storage', { key: value === null ? null : key }));
}
function clickLanguage(w, value) {
  w.document.querySelector(`button[data-definition-language="${value}"]`).click();
}

test('all five language buttons update every daily prompt, copy exact previews, and restore the originals', async () => {
  const copies = [];
  const w = load('beginner.html', { clipboard: { writeText: async text => copies.push(text) } });
  const d = w.document;
  const nodes = [...d.querySelectorAll('.ai-prompt-text')];
  const originals = nodes.map(node => node.textContent);
  run(w, 'learning.js', 'ai-practice.js');
  for (const [language, name] of Object.entries(languages)) {
    clickLanguage(w, language);
    for (const [i, node] of nodes.entries()) {
      assert.ok(node.textContent.startsWith(originals[i] + '\n\nEXPLANATION LANGUAGE AND DEPTH'));
      assert.ok(node.textContent.includes(`My explanation language is ${name}.`));
      assert.equal(node.textContent.split('EXPLANATION LANGUAGE AND DEPTH').length, 2);
      assert.match(node.textContent, /Deeper explanation must not make the English practice harder/);
      assert.match(node.textContent, /multiple-choice rules where specified, one-question-at-a-time/);
      assert.match(node.textContent, /do not reveal an answer/);
    }
    assert.ok(d.querySelector('[data-ai-language-notice]').textContent.includes(name));
    for (const button of [...d.querySelectorAll('[data-ai-copy-text]')].slice(0, 3)) {
      button.click(); await settle();
      assert.equal(copies.at(-1), d.getElementById(button.dataset.aiCopyText).textContent);
    }
  }
  clickLanguage(w, 'ja'); clickLanguage(w, 'en');
  assert.deepEqual(nodes.map(node => node.textContent), originals);
  assert.equal(d.querySelector('[data-ai-language-notice]').textContent, 'AI explanations in English.');
  assert.equal(w.localStorage.length, 1);
});

test('saved language carries into all three levels and non-story curriculum prompts', () => {
  for (const file of ['news/2026-09-08/beginner.html', 'news/2026-09-08/intermediate.html', 'news/2026-09-08/advanced.html', 'grammar-concepts/concept-35.html', 'us-life.html', 'tools.html']) {
    const w = load(file, { saved: 'zh-Hans' });
    run(w, 'ai-practice.js');
    for (const node of w.document.querySelectorAll('.ai-prompt-text')) {
      assert.match(node.textContent, /My explanation language is Simplified Chinese\./, file);
    }
    externalLanguage(w, 'pt-BR');
    assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Brazilian Portuguese\./);
    w.localStorage.setItem(key, 'ko');
    w.dispatchEvent(new w.PageTransitionEvent('pageshow', { persisted: true }));
    assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Korean\./);
    externalLanguage(w, null);
    assert.doesNotMatch(w.document.querySelector('.ai-prompt-text').textContent, /EXPLANATION LANGUAGE AND DEPTH/);
  }
});

test('blocked storage and either script order keep current-page selection working', () => {
  for (const order of [['learning.js', 'ai-practice.js'], ['ai-practice.js', 'learning.js']]) {
    const w = load('news/2026-09-08/intermediate.html', { blockedStorage: true });
    // This test exercises storage and script order, not a dated translation cache.
    w.document.querySelectorAll('.vocab-definition').forEach(node => {
      node.dataset.translations = JSON.stringify({ es: 'Definición de prueba.' });
    });
    run(w, ...order);
    clickLanguage(w, 'es');
    assert.equal(w.document.querySelector('.vocab-definition').lang, 'es');
    assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Spanish\./);
  }
  const w = load('news/2026-09-08/advanced.html', { blockedStorage: true });
  run(w, 'learning.js');
  clickLanguage(w, 'ja');
  run(w, 'ai-practice.js');
  assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Japanese\./);
});

test('missing vocabulary translations keep English definitions while honoring the AI explanation language', () => {
  const w = load('news/2026-09-08/intermediate.html');
  w.document.querySelectorAll('.vocab-definition').forEach(node => { node.dataset.translations = '{}'; });
  run(w, 'learning.js', 'ai-practice.js');
  clickLanguage(w, 'es');
  assert.equal(w.document.querySelector('.vocab-definition').lang, 'en');
  assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Spanish\./);
});

test('manual copying selects the full adapted prompt when clipboard access fails', async () => {
  for (const clipboard of [undefined, { writeText: async () => { throw new Error('Denied'); } }]) {
    const w = load('grammar-concepts/concept-35.html', { saved: 'pt-BR', clipboard });
    run(w, 'ai-practice.js');
    w.document.querySelector('[data-ai-copy-text]').click(); await settle();
    const node = w.document.querySelector('.ai-prompt-text');
    assert.equal(w.getSelection().toString(), node.textContent);
    assert.match(w.getSelection().toString(), /My explanation language is Brazilian Portuguese\./);
    assert.equal(node.closest('details').open, true);
  }
});

test('changing language during clipboard permission identifies the earlier copied prompt', async () => {
  let complete, copied;
  const w = load('grammar-concepts/concept-35.html', { saved: 'ja', clipboard: {
    writeText: text => { copied = text; return new Promise(resolve => { complete = resolve; }); }
  } });
  run(w, 'ai-practice.js');
  w.document.querySelector('[data-ai-copy-text]').click();
  externalLanguage(w, 'ko');
  complete(); await settle();
  assert.match(copied, /My explanation language is Japanese\./);
  assert.match(w.document.querySelector('[data-ai-copy-status]').textContent, /earlier prompt/);
  assert.match(w.document.querySelector('.ai-prompt-text').textContent, /My explanation language is Korean\./);
});

test('workplace chooser, complete cards, printing and text downloads share the chosen language in either script order', async () => {
  for (const order of [['work-ai.js', 'work-ready.js', 'ai-practice.js'], ['ai-practice.js', 'work-ai.js', 'work-ready.js']]) {
    const copies = [];
    const w = load('efsp-manufacturing.html', { saved: 'ja', clipboard: { writeText: async text => copies.push(text) } });
    const d = w.document;
    const original = d.querySelector('[data-ai-prompt]').value;
    const fixed = d.querySelector('[data-copy-finished]');
    const originalFixed = d.getElementById(fixed.dataset.copyFinished).textContent;
    run(w, ...order);
    d.querySelector('[data-work-note]').value = 'PRIVATE NOTES MUST NOT BE COPIED';
    for (const [language, name] of Object.entries(languages)) {
      externalLanguage(w, language);
      const control = d.querySelector('[data-ai-mode]');
      control.value = 'grammar'; control.dispatchEvent(new w.Event('change'));
      const text = d.querySelector('[data-ai-prompt]').value;
      assert.match(text, /TASK: Grammar that changes the meaning/);
      assert.ok(text.includes(`My explanation language is ${name}.`));
      assert.doesNotMatch(text, /PRIVATE NOTES/);
      assert.equal(d.querySelector('[data-ai-print]').textContent, text);
      assert.equal(decodeURIComponent(d.querySelector('[data-ai-download]').href.split(',').slice(1).join(',')), text);
      d.querySelector('[data-ai-copy]').click(); await settle();
      assert.equal(copies.at(-1), text);
      fixed.click(); await settle();
      assert.equal(copies.at(-1), d.getElementById(fixed.dataset.copyFinished).textContent);
      assert.ok(copies.at(-1).includes(`My explanation language is ${name}.`));
    }
    externalLanguage(w, 'en');
    const control = d.querySelector('[data-ai-mode]');
    control.value = 'roleplay'; control.dispatchEvent(new w.Event('change'));
    assert.equal(d.querySelector('[data-ai-prompt]').value, original);
    assert.equal(d.getElementById(fixed.dataset.copyFinished).textContent, originalFixed);
  }
});

test('unsupported or malicious preferences fall back to the unmodified English prompt', () => {
  for (const saved of ['__proto__', 'toString', '<img src=x onerror=alert(1)>', 'fr']) {
    const w = load('grammar-concepts/concept-35.html', { saved });
    const original = w.document.querySelector('.ai-prompt-text').textContent;
    run(w, 'ai-practice.js');
    assert.equal(w.document.querySelector('.ai-prompt-text').textContent, original);
  }
});
