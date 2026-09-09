const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.resolve(__dirname, '..');
const script = fs.readFileSync(path.join(root, 'work-ai.js'), 'utf8');

function setup(query = '', before = () => {}, file = 'efsp-manufacturing.html') {
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), 'utf8'), {
    url: `https://englishladder.com/${file}${query}`, runScripts: 'outside-only'
  });
  before(dom.window);
  dom.window.eval(script);
  return dom;
}
function choose(w, selector, value) {
  const element = w.document.querySelector(selector);
  element.value = value;
  element.dispatchEvent(new w.Event('change', { bubbles: true }));
}
const prompt = d => d.querySelector('[data-ai-prompt]').value;
const tick = () => new Promise(resolve => setImmediate(resolve));

test('all courses preserve the static prompt and expose every complete dialogue', () => {
  for (const file of fs.readdirSync(root).filter(n => /^efsp-.*\.html$/.test(n))) {
    const dom = setup('', () => {}, file), w = dom.window, d = w.document;
    const area = d.querySelector('[data-ai-prompt]');
    assert.equal(area.value, area.textContent, file);
    assert.equal(d.querySelector('[data-ai-controls]').hidden, false);
    const data = JSON.parse(d.querySelector('[data-ai-data]').textContent);
    for (const [i, context] of data.contexts.entries()) {
      choose(w, '[data-ai-context]', context.id);
      choose(w, '[data-ai-mode]', data.modes[i % 8].id);
      assert.ok(prompt(d).includes(context.text), `${file}: ${context.id}`);
      assert.ok(prompt(d).includes(data.course));
      assert.equal(d.querySelector('[data-ai-print]').textContent, prompt(d));
    }
    dom.window.close();
  }
});

test('deep links restore goal, dialogue and support; malformed options safely fall back', () => {
  let dom = setup('?ai=dialogues&context=dialogue-8&level=C1#ai-practice'), d = dom.window.document;
  assert.equal(d.querySelector('[data-ai-mode]').value, 'dialogues');
  assert.equal(d.querySelector('[data-ai-context]').value, 'dialogue-8');
  assert.match(prompt(d), /C1 stretch/);
  assert.match(prompt(d), /12-18 substantial speaking turns/);
  dom.window.close();
  dom = setup('?ai=invalid&context=dialogue-999&level=__proto__'); d = dom.window.document;
  assert.equal(d.querySelector('[data-ai-mode]').value, 'roleplay');
  assert.equal(d.querySelector('[data-ai-context]').value, 'module-1');
  assert.match(prompt(d), /B2 independent/);
  dom.window.close();
});

test('copy and downloadable text contain the selected prompt and never learner drafts', async () => {
  let copied = '';
  const dom = setup('', w => Object.defineProperty(w.navigator, 'clipboard', {value: {writeText: async text => { copied = text; }}}));
  const w = dom.window, d = w.document;
  const legacyNote = d.createElement('textarea');
  legacyNote.dataset.workNote = 'module-1'; legacyNote.value = 'PRIVATE LEARNER DRAFT MUST STAY HERE';
  d.body.append(legacyNote);
  choose(w, '[data-ai-mode]', 'writing');
  choose(w, '[data-ai-context]', 'module-5');
  choose(w, '[data-ai-level]', 'B1');
  d.querySelector('[data-ai-copy]').click(); await tick();
  assert.equal(copied, prompt(d));
  assert.ok(!copied.includes('PRIVATE LEARNER'));
  assert.match(copied, /B1 support/);
  assert.match(copied, /Stop and wait/);
  const download = d.querySelector('[data-ai-download]');
  assert.equal(decodeURIComponent(download.href.split(',').slice(1).join(',')), copied);
  assert.match(download.download, /module-5-writing-B1-prompt\.txt$/);
  assert.match(d.querySelector('[data-ai-status]').textContent, /Prompt copied/);
  const link = new URL(d.querySelector('[data-ai-link]').href);
  assert.equal(link.searchParams.get('context'), 'module-5');
  assert.equal(link.searchParams.get('level'), 'B1');
  assert.equal(w.localStorage.length, 0);
  dom.window.close();
});

test('denied or unavailable clipboard selects the prompt and gives a usable alternative', async () => {
  for (const denied of [false, true]) {
    const dom = setup('', w => {
      if (denied) Object.defineProperty(w.navigator, 'clipboard', {value: {writeText: async () => {throw new Error('denied');}}});
    });
    const d = dom.window.document;
    d.querySelector('.work-ai-preview').open = false;
    d.querySelector('[data-ai-copy]').click(); await tick();
    const area = d.querySelector('[data-ai-prompt]');
    assert.equal(d.activeElement, area);
    assert.equal(area.selectionStart, 0);
    assert.equal(area.selectionEnd, area.value.length);
    assert.equal(d.querySelector('.work-ai-preview').open, true);
    assert.match(d.querySelector('[data-ai-status]').textContent, /save it as text/);
    dom.window.close();
  }
});

test('lesson links select their exact case; browser Back restores the previous selection', () => {
  const dom = setup('?ai=review&context=dialogue-2&level=C1#ai-practice'), w = dom.window, d = w.document;
  d.querySelector('#module-6 [data-ai-preset]').click();
  assert.equal(d.querySelector('[data-ai-mode]').value, 'vocabulary');
  assert.equal(d.querySelector('[data-ai-context]').value, 'module-6');
  assert.match(w.location.href, /context=module-6/);
  assert.equal(d.activeElement, d.querySelector('[data-ai-mode]'));
  w.history.replaceState(null, '', '?ai=review&context=dialogue-2&level=C1#ai-practice');
  w.dispatchEvent(new w.PopStateEvent('popstate'));
  assert.equal(d.querySelector('[data-ai-mode]').value, 'review');
  assert.equal(d.querySelector('[data-ai-context]').value, 'dialogue-2');
  dom.window.close();
});

test('a changed selection during clipboard permission does not claim the new prompt was copied', async () => {
  let complete;
  const dom = setup('', w => Object.defineProperty(w.navigator, 'clipboard', {value: {writeText: () => new Promise(resolve => {complete = resolve;})}}));
  const d = dom.window.document;
  d.querySelector('[data-ai-copy]').click();
  choose(dom.window, '[data-ai-mode]', 'grammar');
  complete(); await tick();
  assert.match(d.querySelector('[data-ai-status]').textContent, /earlier prompt/);
  dom.window.close();
});

test('all tasks and support settings produce distinct prompts without requesting a service', () => {
  const dom = setup('', w => {
    w.fetch = () => { throw new Error('Unexpected network request'); };
    Object.defineProperty(w, 'localStorage', {get() { throw new Error('Unexpected storage access'); }});
  }), w = dom.window, d = w.document, outputs = new Set();
  for (const option of d.querySelectorAll('[data-ai-mode] option')) {
    for (const level of ['B1', 'B2', 'C1']) {
      choose(w, '[data-ai-mode]', option.value); choose(w, '[data-ai-level]', level);
      outputs.add(prompt(d));
    }
  }
  assert.equal(outputs.size, 24);
  dom.window.close();
});
