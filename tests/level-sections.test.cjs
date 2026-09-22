const {test, afterEach} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');

const root = path.join(__dirname, '..');
const source = file => fs.readFileSync(path.join(root, file), 'utf8');
const stages = ['read', 'practice', 'discuss'];
const levels = ['beginner', 'intermediate', 'advanced'];
const windows = [];
afterEach(() => windows.splice(0).forEach(window => window.close()));
const feedIds = [...source('beginner.html').matchAll(/id="(lesson-\d{4}-\d{2}-\d{2})"/g)]
  .map(match => match[1]);
const latestDate = feedIds[0]?.slice('lesson-'.length);

function load(file, {hash = '', initialize = true, inline = true, beforeInitialize} = {}) {
  const window = new JSDOM(source(file), {
    url: `https://englishladder.com/${file}${hash}`,
    runScripts: inline ? 'dangerously' : 'outside-only',
    beforeParse(window) {
      window.HTMLElement.prototype.scrollIntoView = function () {};
    },
  }).window;
  windows.push(window);
  beforeInitialize?.(window);
  if (initialize) {
    window.eval(source('app.js'));
    window.eval(source('learning.js'));
    window.eval(source('site.js'));
  }
  return window;
}

function headerButtons(window) {
  const buttons = [...window.document.querySelectorAll(
    '.level-choice.is-current .level-section-controls button[data-lesson-stage]')];
  assert.equal(buttons.length, 3, 'The selected level must have three header section buttons.');
  assert.deepEqual(buttons.map(button => button.dataset.lessonStage), stages);
  return buttons;
}

function assertStage(window, lesson, stage) {
  const panels = stages.map(name => lesson.querySelector(`[data-stage="${name}"]`));
  assert.deepEqual(panels.map(panel => panel.hidden), stages.map(name => name !== stage));
  const header = headerButtons(window);
  const local = [...lesson.querySelectorAll('.learning-flow > button')];
  assert.equal(local.length, 3, 'The lesson retains its own section controls.');
  for (const buttons of [header, local]) {
    assert.deepEqual(buttons.map(button => button.getAttribute('aria-controls')), panels.map(panel => panel.id));
    assert.deepEqual(buttons.map(button => button.getAttribute('aria-current')),
      stages.map(name => name === stage ? 'step' : null));
    assert.ok(buttons.every(button => !button.disabled));
  }
}

function toggle(window, lesson, open) {
  lesson.open = open;
  lesson.dispatchEvent(new window.Event('toggle'));
}

function assertLevelLinks(window, lesson) {
  const links = [...window.document.querySelectorAll('.level-toolbar a[data-level-choice]')];
  assert.equal(links.length, 3);
  for (const link of links) {
    const target = new URL(link.href);
    assert.equal(target.pathname, `/${link.dataset.levelChoice}.html`);
    assert.equal(target.hash, `#${lesson.id}`,
      'Switching level must preserve the lesson controlled by the header.');
  }
  assert.equal(window.location.hash, `#${lesson.id}`,
    'The current address must follow the active open lesson.');
}

test('published level headers put section controls inside only the selected level', () => {
  const files = levels.flatMap(level => [
    `${level}.html`, `stories/city-trees/${level}.html`,
    ...(latestDate ? [`news/${latestDate}/${level}.html`] : []),
  ]);
  for (const file of files) {
    const window = load(file, {initialize: false, inline: false});
    const nav = window.document.querySelector('.level-toolbar .story-levels');
    assert.ok(nav, `${file}: level navigation is present`);
    const choices = [...nav.querySelectorAll('.level-choice')];
    assert.equal(choices.length, 3, file);
    const current = choices.filter(choice => choice.classList.contains('is-current'));
    assert.equal(current.length, 1, file);
    const selectedLevel = path.basename(file, '.html');
    assert.ok(current[0].querySelector(`[data-level-choice="${selectedLevel}"]`), file);
    assert.equal(nav.querySelectorAll('.level-section-controls').length, 1, file);
    headerButtons(window);
    for (const choice of choices.filter(choice => choice !== current[0])) {
      assert.equal(choice.children.length, 1, 'Other levels remain a single level link.');
      assert.equal(choice.firstElementChild.tagName, 'A');
      assert.ok(choice.firstElementChild.hasAttribute('data-level-choice'));
      assert.equal(choice.querySelector('button, .level-range'), null);
    }
    assert.equal(nav.querySelector('a button, button a, a a, button button'), null,
      'Level links and section buttons must be separate interactive elements.');
    assert.equal(nav.querySelector('.level-range'), null);
    const accessibleText = nav.textContent + [...nav.querySelectorAll('[aria-label]')]
      .map(node => node.getAttribute('aria-label')).join(' ');
    assert.doesNotMatch(accessibleText, /A1[–-]A2|B1[–-]B2|C1\+/,
      'The compact level navigation must not retain proficiency ranges.');
  }
});

test('evergreen header buttons, lesson buttons, and next/back actions stay synchronized', () => {
  const window = load('stories/city-trees/beginner.html');
  const lesson = window.document.querySelector('.daily-lesson');
  const header = headerButtons(window);
  assertStage(window, lesson, 'read');
  header[1].click();
  assertStage(window, lesson, 'practice');
  lesson.querySelector('[data-stage="practice"] .stage-actions .primary-button').click();
  assertStage(window, lesson, 'discuss');
  lesson.querySelector('[data-stage="discuss"] .stage-actions .secondary-button').click();
  assertStage(window, lesson, 'practice');
  lesson.querySelector('.learning-flow button').click();
  assertStage(window, lesson, 'read');
  lesson.querySelector('[data-stage="read"] .stage-actions .primary-button').click();
  assertStage(window, lesson, 'practice');
  header[2].click();
  assertStage(window, lesson, 'discuss');
});

test('a dated feed link selects that lesson for header navigation, including later hashes',
  {skip: feedIds.length < 3}, () => {
    const window = load('beginner.html', {hash: `#${feedIds[2]}`});
    const linked = window.document.getElementById(feedIds[2]);
    const newest = window.document.getElementById(feedIds[0]);
    assert.ok(linked.open);
    assertStage(window, linked, 'read');
    headerButtons(window)[1].click();
    assertStage(window, linked, 'practice');
    assert.equal(newest.querySelector('[data-stage="practice"]').hidden, true,
      'The header must not move an unrelated lesson to Practice.');
    window.history.replaceState(null, '', `#${newest.id}`);
    window.dispatchEvent(new window.HashChangeEvent('hashchange'));
    assert.ok(newest.open);
    assertStage(window, newest, 'read');
    headerButtons(window)[2].click();
    assertStage(window, newest, 'discuss');
    assert.equal(linked.querySelector('[data-stage="practice"]').hidden, false,
      'Switching the active lesson must preserve the other lesson’s current section.');
  });

test('an already-open feed lesson is selected before the newest closed lesson',
  {skip: feedIds.length < 2}, () => {
    const window = load('beginner.html', {beforeInitialize(window) {
      window.document.querySelectorAll('.daily-lesson').forEach(lesson => { lesson.open = false; });
      window.document.getElementById(feedIds[1]).open = true;
    }});
    const opened = window.document.getElementById(feedIds[1]);
    assertStage(window, opened, 'read');
    headerButtons(window)[2].click();
    assertStage(window, opened, 'discuss');
    assert.equal(window.document.getElementById(feedIds[0]).open, false);
  });

test('interacting with either of two open lessons changes the header’s active lesson',
  {skip: feedIds.length < 2}, () => {
    const window = load('beginner.html');
    const first = window.document.getElementById(feedIds[0]);
    const second = window.document.getElementById(feedIds[1]);
    headerButtons(window)[1].click();
    assert.ok(first.open);
    assertStage(window, first, 'practice');
    toggle(window, second, true);
    assert.ok(first.open, 'Opening another lesson must not close the first one.');
    assertStage(window, second, 'read');
    second.querySelectorAll('.learning-flow button')[2].click();
    assertStage(window, second, 'discuss');
    first.querySelector('[data-stage="practice"] .quiz-question button').click();
    assertStage(window, first, 'practice');
    assertLevelLinks(window, first);
    headerButtons(window)[0].click();
    assertStage(window, first, 'read');
    assert.equal(second.querySelector('[data-stage="discuss"]').hidden, false);
    assert.ok(first.open && second.open);
    second.querySelector('[data-stage="discuss"] .stage-actions .secondary-button').focus();
    assertStage(window, second, 'discuss');
    assertLevelLinks(window, second);
  });

test('scrolling between open lessons updates the header without resetting either section',
  {skip: feedIds.length < 2}, () => {
    const frames = [];
    const window = load('beginner.html', {beforeInitialize(window) {
      window.requestAnimationFrame = callback => { frames.push(callback); return frames.length; };
    }});
    const first = window.document.getElementById(feedIds[0]);
    const second = window.document.getElementById(feedIds[1]);
    toggle(window, first, true);
    first.querySelectorAll('.learning-flow button')[1].click();
    toggle(window, second, true);
    second.querySelectorAll('.learning-flow button')[2].click();
    let firstVisible = true;
    window.document.querySelector('.site-masthead').getBoundingClientRect = () => ({bottom: 100});
    first.getBoundingClientRect = () => firstVisible
      ? {top: 105, bottom: 700, height: 595}
      : {top: -600, bottom: 90, height: 690};
    second.getBoundingClientRect = () => firstVisible
      ? {top: 900, bottom: 1500, height: 600}
      : {top: 105, bottom: 700, height: 595};
    window.dispatchEvent(new window.Event('scroll'));
    window.dispatchEvent(new window.Event('scroll'));
    assert.equal(frames.length, 1, 'Repeated scroll events share one pending screen update.');
    frames.shift()();
    assertStage(window, first, 'practice');
    assertLevelLinks(window, first);
    assert.equal(second.querySelector('[data-stage="discuss"]').hidden, false);
    let addressWrites = 0;
    const replaceState = window.history.replaceState.bind(window.history);
    window.history.replaceState = (...args) => { addressWrites += 1; return replaceState(...args); };
    for (let frame = 0; frame < 120; frame += 1) {
      window.dispatchEvent(new window.Event('scroll'));
      frames.shift()();
    }
    assert.equal(addressWrites, 0,
      'Scrolling within one lesson must not repeatedly write history and trigger browser rate limits.');
    firstVisible = false;
    window.dispatchEvent(new window.Event('scroll'));
    frames.shift()();
    assertStage(window, second, 'discuss');
    assertLevelLinks(window, second);
    assert.equal(first.querySelector('[data-stage="practice"]').hidden, false);
    assert.ok(first.open && second.open);
  });

test('closing the final open feed lesson lets a header button reopen the newest lesson',
  {skip: feedIds.length < 2}, () => {
    const window = load('beginner.html', {hash: `#${feedIds[1]}`});
    const older = window.document.getElementById(feedIds[1]);
    const newest = window.document.getElementById(feedIds[0]);
    headerButtons(window)[2].click();
    assertStage(window, older, 'discuss');
    toggle(window, older, false);
    assert.equal(window.document.querySelectorAll('.daily-lesson[open]').length, 0);
    const header = headerButtons(window);
    assert.equal(header[1].getAttribute('aria-controls'), newest.querySelector('[data-stage="practice"]').id);
    header[1].click();
    assert.ok(newest.open);
    assert.equal(older.open, false);
    assertStage(window, newest, 'practice');
  });

test('header section controls remain ordinary focusable buttons with keyboard-style activation', () => {
  const window = load('stories/food-market/advanced.html');
  const lesson = window.document.querySelector('.daily-lesson');
  const header = headerButtons(window);
  for (const [index, button] of header.entries()) {
    assert.equal(button.tagName, 'BUTTON');
    assert.equal(button.type, 'button');
    assert.equal(button.tabIndex, 0);
    assert.equal(button.getAttribute('role'), null, 'These are buttons, not a custom tab widget.');
    button.focus();
    assert.equal(window.document.activeElement, button);
    // Browsers dispatch a click with detail=0 for keyboard activation. jsdom
    // does not implement native Enter/Space default actions itself.
    button.dispatchEvent(new window.MouseEvent('click', {bubbles: true, detail: 0}));
    assertStage(window, lesson, stages[index]);
  }
});

test('before JavaScript arrives or when it is unavailable, all content remains readable and header buttons are inert', () => {
  for (const inline of [false, true]) {
    const window = load('stories/city-trees/intermediate.html', {initialize: false, inline});
    const lesson = window.document.querySelector('.daily-lesson');
    const header = headerButtons(window);
    assert.ok(header.every(button => button.disabled));
    assert.ok(lesson.open);
    assert.deepEqual([...lesson.querySelectorAll('.learning-panel')].map(panel => panel.hidden),
      [false, false, false]);
    header[2].click();
    assert.equal(lesson.querySelector('[data-stage="read"]').hidden, false);
    assert.equal(lesson.querySelector('[data-stage="discuss"]').hidden, false);
    assert.equal(window.document.querySelectorAll('.story-levels a[data-level-choice]').length, 3);
    if (inline) {
      window.document.querySelector('script[src*="learning.js"]')
        .dispatchEvent(new window.Event('error'));
      assert.equal(window.document.documentElement.classList.contains('reading-js'), false);
      assert.ok(header.every(button => button.disabled));
    }
  }
});
