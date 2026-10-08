const {test, afterEach} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.join(__dirname, '..');
const windows = [];
const tick = () => new Promise(resolve => setTimeout(resolve, 10));
afterEach(() => windows.splice(0).forEach(w => w.close()));

async function setup({hash = '', copy, fetch} = {}) {
  const w = new JSDOM(fs.readFileSync(path.join(root, 'tools.html'), 'utf8'),
    {url: 'https://englishladder.com/tools.html' + hash, runScripts: 'outside-only'}).window;
  windows.push(w);
  if (copy) Object.defineProperty(w.navigator, 'clipboard', {value: {writeText: copy}});
  w.fetch = fetch || (() => Promise.reject(new Error('Offline test')));
  w.eval(fs.readFileSync(path.join(root, 'tools.js'), 'utf8'));
  await tick();
  return {w, d: w.document};
}

test('repair preserves valid constructions rather than rewriting their meaning', async () => {
  const {d} = await setup();
  for (const text of [
    'The book is interesting in several ways.',
    'They recommended me to the team.',
    'We recommend you to book early.',
    "We discussed this in Monday’s meeting.",
    'We will discuss about ten proposals.',
    'We will discuss about the same number of proposals.',
    'This is a report on 2026.',
    'I know how much people care.',
    'Do not explain me away.',
    'She writes an advice column.',
  ]) {
    d.querySelector('#repair-input').value = text;
    d.querySelector('#repair-run').click();
    const result = d.querySelector('#repair-results');
    assert.match(result.textContent, /None of this tool’s limited patterns matched/, text);
    assert.ok(result.textContent.includes(text));
    assert.equal(d.querySelector('#repair-input').value, text);
    assert.doesNotMatch(result.textContent, /Possible wording/);
  }
});

test('repair explains multiple issues, qualifies meaning, and escapes learner text', async () => {
  const {d} = await setup();
  const input = d.querySelector('#repair-input');
  const result = d.querySelector('#repair-results');
  const examples = [
    ['I am interesting in improve my English.', ['Emotion adjectives', 'Verb after preposition', 'interested in improving']],
    ['She recommended that I to apply.', ['without “to”']],
    ['She suggested me to study.', ['suggested that I apply']],
    ['We discuss about the plan.', ['direct object']],
    ['Please explain me the plan.', ['explain something to someone']],
    ['We meet at Monday.', ['on']],
    ['We meet in Monday.', ['on']],
    ['There are much people.', ['Countable nouns']],
    ['Give me an advice.', ['Uncountable noun']],
    ['Give me an advice about travel.', ['Uncountable noun']],
    ['The little people arrived.', ['Keep “little” if size is your meaning']],
    ['She is interesting in this film.', ['can be correct', 'Choose the meaning you intend']],
  ];
  for (const [text, feedback] of examples) {
    input.value = text; d.querySelector('#repair-run').click();
    for (const expected of feedback) assert.ok(result.textContent.includes(expected), text + ': ' + expected);
    assert.equal(input.value, text);
  }
  input.value = '<img src=x onerror=alert(1)> I am interesting in learn English.';
  d.querySelector('#repair-run').click();
  assert.equal(result.querySelectorAll('img, script').length, 0);
  assert.ok(result.textContent.includes(input.value));
  input.value = ''; d.querySelector('#repair-run').click();
  assert.match(result.textContent, /Enter a sentence first/);
});

test('diagnostic explains every selected answer despite option shuffling', async () => {
  const {d, w} = await setup();
  const result = d.querySelector('#diagnostic-results');
  d.querySelector('#diagnostic-submit').click();
  assert.match(result.textContent, /Answer at least one/);
  d.querySelector('input[name="diagnostic-0"][value="0"]').click();
  d.querySelector('#diagnostic-submit').click();
  assert.match(result.textContent, /1 of 10 answered; 1 correct/);
  for (const option of [0, 1, 2]) {
    for (let q = 0; q < 10; q++) d.querySelector(`input[name="diagnostic-${q}"][value="${option}"]`).click();
    d.querySelector('#diagnostic-submit').click();
    const cards = [...result.querySelectorAll('article')].filter(a => a.querySelector('h4'));
    assert.equal(cards.length, 10);
    for (let q = 0; q < 10; q++) {
      const choice = d.querySelector(`input[name="diagnostic-${q}"]:checked`).nextElementSibling.textContent;
      assert.ok(cards[q].textContent.includes('Your choice: ' + choice));
      assert.ok(cards[q].querySelectorAll('p')[1].textContent.length > 25);
      assert.doesNotMatch(cards[q].textContent, /undefined/);
    }
    assert.match(result.textContent, /not a placement test/);
    if (option === 0) assert.match(result.textContent, /All 10 questions correct/);
    else assert.match(cards[4].textContent, /This is grammatical/);
  }
  d.querySelector('input[name="diagnostic-0"][value="0"]').click();
  assert.match(result.textContent, /Answers changed/);
  assert.equal(result.querySelectorAll('article').length, 0);
  d.querySelector('#diagnostic-reset').click();
  assert.equal(d.querySelectorAll('input:checked').length, 0);
  assert.equal(result.textContent, '');
});

test('phrase copying reports success only after the clipboard accepts text', async () => {
  let resolve, copied;
  const {d} = await setup({copy: text => {copied = text; return new Promise(r => {resolve = r;});}});
  const chip = d.querySelector('.phrase-chip');
  chip.click();
  assert.equal(copied, chip.dataset.copyText);
  assert.equal(d.querySelector('[data-phrase-copy-status]').textContent, '');
  resolve(); await tick();
  assert.match(d.querySelector('[data-phrase-copy-status]').textContent, /Phrase copied/);
});

for (const unavailable of [true, false]) test(`failed copying offers selected text (${unavailable ? 'missing API' : 'denied'})`, async () => {
  const {w, d} = await setup({copy: unavailable ? undefined : () => Promise.reject(new Error('Denied'))});
  const chip = d.querySelector('.phrase-chip'); chip.click(); await tick();
  assert.match(d.querySelector('[data-phrase-copy-status]').textContent, /Automatic copying is unavailable/);
  assert.equal(w.getSelection().toString(), chip.textContent);
  assert.equal(chip.classList.contains('phrase-chip-copied'), false);
});

test('direct tool links open the selected tool and shadowing loads current lesson sentences once', async () => {
  let calls = 0;
  const lesson = Object.fromEntries(['beginner', 'intermediate', 'advanced'].map(level =>
    [level, {headline: 'Current lesson', brief: `This is the current ${level} lesson sentence.`}]));
  const {w, d} = await setup({hash: '#pronunciation-shadowing', fetch: async () => {
    calls++; return {ok: true, json: async () => lesson};
  }});
  await tick();
  assert.equal(d.querySelector('#pronunciation-shadowing').open, true);
  assert.equal(calls, 1);
  assert.match(d.querySelector('#shadow-sentence').textContent, /current beginner lesson/);
  w.location.hash = '#sentence-repair'; await tick();
  assert.equal(d.querySelector('#sentence-repair').open, true);
  assert.equal(d.querySelector('#pronunciation-shadowing').open, false);
  w.location.hash = '#pronunciation-shadowing'; await tick();
  assert.equal(calls, 1);
  w.location.hash = '#%E0%A4%A'; await tick();
  assert.equal(d.querySelector('#pronunciation-shadowing').open, true);
});
