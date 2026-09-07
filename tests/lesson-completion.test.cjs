const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');
const prefix = 'english-ladder-completed-v1:';
const levels = ['beginner', 'intermediate', 'advanced'];
const windows = new Set();
const html = file => fs.readFileSync(path.join(root, file), 'utf8');
const feedSource = html('beginner.html');
const dates = [...feedSource.matchAll(/data-lesson-key="(\d{4}-\d{2}-\d{2})"/g)].map(match => match[1]);
assert.ok(dates.length > 1, 'Generated feed needs two dates for completion isolation checks');
const newsPath = (date, level) => `news/${date}/${level}.html`;
const key = (date, level) => prefix + newsPath(date, level);
const badges = container => [...container.querySelectorAll('.lesson-completion-mark')];

afterEach(() => {
  for (const dom of windows) dom.window.close();
  windows.clear();
});

function load(file, { stored = {}, beforeScripts } = {}) {
  const dom = new JSDOM(html(file), {
    url: `https://englishladder.com/${file}`, runScripts: 'dangerously',
  });
  windows.add(dom);
  const { window } = dom;
  window.HTMLElement.prototype.scrollIntoView = function () {};
  for (const [name, value] of Object.entries(stored)) window.localStorage.setItem(name, value);
  beforeScripts?.(window);
  for (const script of ['app.js', 'learning.js', 'site.js']) window.eval(html(script));
  return dom;
}

function storedValues(window) {
  return Object.fromEntries(Array.from({ length: window.localStorage.length }, (_, index) => {
    const name = window.localStorage.key(index);
    return [name, window.localStorage.getItem(name)];
  }));
}

function lessonAt(dom, date = dates[0]) {
  const lesson = dom.window.document.querySelector(`.daily-lesson[data-lesson-key="${date}"]`);
  assert.ok(lesson, `Generated page includes lesson ${date}`);
  return lesson;
}

function finish(lesson) {
  lesson.open = true;
  lesson.querySelector('.learning-flow button:last-child').click();
  const button = lesson.querySelector('[data-finish-lesson]');
  assert.ok(button, 'Discussion step exposes its Finish lesson button');
  button.click();
  return button;
}

function assertBadge(container, level) {
  const markers = badges(container);
  assert.equal(markers.length, 1, 'Exactly one completion badge belongs to this title');
  const marker = markers[0];
  assert.equal(marker.dataset.completedLevel, level);
  assert.equal(marker.getAttribute('role'), 'img');
  assert.equal(marker.getAttribute('aria-label'), `Completed at ${level[0].toUpperCase() + level.slice(1)} level`);
  const title = container.querySelector('.lesson-title-label, .lesson-title-text, a');
  assert.ok(title, 'The completion badge accompanies the story title');
  assert.ok(marker.compareDocumentPosition(title) & 4, 'Completion badge appears before the title');
}

function archiveTitle(dom, date) {
  const link = dom.window.document.querySelector(`h2 a[href*="news/${date}/"]`);
  assert.ok(link, `Archive includes ${date}`);
  return link.closest('h2');
}

test('reading and answering a question do not silently mark a lesson completed', () => {
  const dom = load('beginner.html');
  const lesson = lessonAt(dom);
  lesson.open = true;
  lesson.querySelector('.learning-flow button:nth-child(2)').click();
  lesson.querySelector('[data-bg="#e6ffe6"]').click();
  assert.equal(badges(dom.window.document).length, 0);
  assert.equal(Object.keys(storedValues(dom.window)).some(name => name.startsWith(prefix)), false);
  assert.equal(lesson.querySelector('[data-finish-lesson]').disabled, false);
});

test('Finish marks the feed title immediately and persists to its permanent lesson and archive', () => {
  const feed = load('beginner.html');
  const lesson = lessonAt(feed);
  const button = finish(lesson);
  assert.equal(button.textContent, 'Completed ✓');
  assert.equal(button.disabled, true);
  assert.equal(lesson.querySelector('.completion-message').hidden, false);
  assertBadge(lesson.querySelector('.lesson-title-group'), 'beginner');
  assert.equal(feed.window.localStorage.getItem(key(dates[0], 'beginner')), '1');

  const permanent = load(newsPath(dates[0], 'beginner'), { stored: storedValues(feed.window) });
  assertBadge(permanent.window.document.querySelector('h1'), 'beginner');
  const restored = lessonAt(permanent).querySelector('[data-finish-lesson]');
  assert.equal(restored.textContent, 'Completed ✓');
  assert.equal(restored.disabled, true);
  assert.equal(lessonAt(permanent).querySelector('.completion-message').hidden, false);

  const archive = load('archive.html', { stored: storedValues(permanent.window) });
  assertBadge(archiveTitle(archive, dates[0]), 'beginner');
  assert.equal(badges(archiveTitle(archive, dates[1])).length, 0);
});

test('completion at each level stays isolated from other levels and dates', () => {
  let stored = {};
  for (const level of levels) {
    const dom = load(`${level}.html`, { stored });
    const lesson = lessonAt(dom);
    assert.equal(badges(lesson).length, 0, `Finishing another level does not finish ${level}`);
    assert.equal(lesson.querySelector('[data-finish-lesson]').disabled, false);
    finish(lesson);
    assertBadge(lesson.querySelector('.lesson-title-group'), level);
    assert.equal(badges(lessonAt(dom, dates[1])).length, 0);
    stored = storedValues(dom.window);
    assert.equal(stored[key(dates[0], level)], '1');
  }
  assert.deepEqual(Object.keys(stored).filter(name => name.startsWith(prefix)).sort(),
    levels.map(level => key(dates[0], level)).sort());
});

test('archive shows all completed levels in level order regardless of the preferred level', () => {
  const stored = Object.fromEntries([...levels].reverse().map(level => [key(dates[0], level), '1']));
  stored['english-ladder-level'] = 'advanced';
  const dom = load('archive.html', { stored });
  const title = archiveTitle(dom, dates[0]);
  assert.deepEqual(badges(title).map(marker => marker.dataset.completedLevel), levels);
  assert.match(title.querySelector('a').href, /\/advanced\.html$/);
  for (const marker of badges(title)) assert.ok(marker.compareDocumentPosition(title.querySelector('a')) & 4);
  assert.equal(badges(archiveTitle(dom, dates[1])).length, 0);
});

test('finishing a permanent news page restores the same completion in the dated feed', () => {
  const permanent = load(newsPath(dates[1], 'advanced'));
  finish(lessonAt(permanent, dates[1]));
  const feed = load('advanced.html', { stored: storedValues(permanent.window) });
  assertBadge(lessonAt(feed, dates[1]).querySelector('.lesson-title-group'), 'advanced');
  assert.equal(badges(lessonAt(feed, dates[0])).length, 0);
});

test('evergreen stories use independent story and level identities and restore the visible title', () => {
  const story = load('stories/city-trees/intermediate.html');
  finish(lessonAt(story, 'city-trees'));
  assert.equal(story.window.localStorage.getItem(prefix + 'stories/city-trees/intermediate.html'), '1');
  assertBadge(story.window.document.querySelector('h1'), 'intermediate');
  const stored = storedValues(story.window);
  const reopened = load('stories/city-trees/intermediate.html', { stored });
  assert.equal(lessonAt(reopened, 'city-trees').querySelector('[data-finish-lesson]').disabled, true);
  for (const file of ['stories/city-trees/beginner.html', 'stories/food-market/intermediate.html']) {
    const other = load(file, { stored });
    assert.equal(badges(other.window.document).length, 0);
    assert.equal(other.window.document.querySelector('[data-finish-lesson]').disabled, false);
  }
});

test('malformed completion values cannot mark a lesson as complete', () => {
  for (const value of ['0', 'true', '{"completed":true}', '<img src=x onerror=alert(1)>']) {
    const dom = load(newsPath(dates[0], 'beginner'), { stored: { [key(dates[0], 'beginner')]: value } });
    assert.equal(badges(dom.window.document).length, 0, `Reject malformed stored value ${value}`);
    assert.equal(dom.window.document.querySelector('[data-finish-lesson]').disabled, false);
  }
});

test('invalid dates and a lesson key that disagrees with its permanent URL cannot save completion', () => {
  for (const [file, invalidKey] of [
    ['beginner.html', '2026-02-31'],
    [newsPath(dates[0], 'beginner'), dates[1]],
    ['stories/city-trees/beginner.html', 'food-market'],
  ]) {
    const dom = load(file, {
      beforeScripts(window) { window.document.querySelector('.daily-lesson').dataset.lessonKey = invalidKey; },
    });
    finish(dom.window.document.querySelector('.daily-lesson'));
    assert.equal(badges(dom.window.document).length, 0);
    assert.equal(Object.keys(storedValues(dom.window)).some(name => name.startsWith(prefix)), false);
  }
});

test('repeated finish clicks and page restores never duplicate completion badges', () => {
  const dom = load('intermediate.html');
  const lesson = lessonAt(dom);
  const button = finish(lesson);
  button.click();
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assertBadge(lesson.querySelector('.lesson-title-group'), 'intermediate');
  assert.equal(Object.keys(storedValues(dom.window)).filter(name => name.startsWith(prefix)).length, 1);
});

test('blocked browser storage still marks the current page and explains its temporary scope', () => {
  const dom = load(newsPath(dates[0], 'beginner'), {
    beforeScripts(window) {
      Object.defineProperty(window, 'localStorage', { get() { throw new Error('Storage blocked'); } });
    },
  });
  const lesson = lessonAt(dom);
  assert.doesNotThrow(() => finish(lesson));
  assertBadge(dom.window.document.querySelector('h1'), 'beginner');
  assert.match(lesson.querySelector('.completion-message').textContent, /(?:this|current) page/i);
  assert.match(lesson.querySelector('.completion-message').textContent, /(?:only|cannot|unavailable|blocked|not saved)/i);
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assertBadge(dom.window.document.querySelector('h1'), 'beginner');
  assert.equal(lesson.querySelector('[data-finish-lesson]').disabled, true);
});

test('storage quota failure preserves immediate completion without claiming it was saved', () => {
  const dom = load(newsPath(dates[0], 'advanced'), {
    beforeScripts(window) {
      window.Storage.prototype.setItem = function () { throw new Error('Storage quota exhausted'); };
    },
  });
  const lesson = lessonAt(dom);
  finish(lesson);
  assertBadge(dom.window.document.querySelector('h1'), 'advanced');
  assert.equal(dom.window.localStorage.getItem(key(dates[0], 'advanced')), null);
  assert.match(lesson.querySelector('.completion-message').textContent, /(?:this|current) page/i);
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assertBadge(dom.window.document.querySelector('h1'), 'advanced');
});

test('cross-tab completion updates read current storage and preserve another completed level', () => {
  const dom = load('archive.html', { stored: { [key(dates[0], 'beginner')]: '1' } });
  const { window } = dom;
  window.localStorage.setItem(key(dates[0], 'advanced'), '1');
  window.dispatchEvent(new window.StorageEvent('storage', {
    key: key(dates[0], 'advanced'), oldValue: null, newValue: '1', storageArea: window.localStorage,
  }));
  assert.deepEqual(badges(archiveTitle(dom, dates[0])).map(marker => marker.dataset.completedLevel), ['beginner', 'advanced']);
  assert.equal(window.localStorage.getItem(key(dates[0], 'beginner')), '1');
  window.localStorage.removeItem(key(dates[0], 'advanced'));
  window.dispatchEvent(new window.StorageEvent('storage', {
    // A delayed event must not resurrect an entry that has since been removed.
    key: key(dates[0], 'advanced'), oldValue: null, newValue: '1', storageArea: window.localStorage,
  }));
  assertBadge(archiveTitle(dom, dates[0]), 'beginner');
  assert.equal(window.localStorage.getItem(key(dates[0], 'advanced')), null);
});

test('clearing stored completion removes the indicator and restores the Finish button', () => {
  const dom = load(newsPath(dates[0], 'intermediate'), { stored: { [key(dates[0], 'intermediate')]: '1' } });
  const { window } = dom;
  const lesson = lessonAt(dom);
  assertBadge(window.document.querySelector('h1'), 'intermediate');
  window.localStorage.clear();
  window.dispatchEvent(new window.StorageEvent('storage', { key: null, storageArea: window.localStorage }));
  assert.equal(badges(window.document).length, 0);
  assert.equal(lesson.querySelector('[data-finish-lesson]').textContent, 'Finish lesson ✓');
  assert.equal(lesson.querySelector('[data-finish-lesson]').disabled, false);
  assert.equal(lesson.querySelector('.completion-message').hidden, true);
  finish(lesson);
  assertBadge(window.document.querySelector('h1'), 'intermediate');
  window.localStorage.removeItem(key(dates[0], 'intermediate'));
  window.dispatchEvent(new window.Event('pageshow'));
  assert.equal(badges(window.document).length, 0, 'Returning from browser history rechecks completion');
  assert.equal(lesson.querySelector('[data-finish-lesson]').disabled, false);
});

test('Finish stores only a completion marker and leaves discussion notes and quiz answers private', () => {
  const dom = load(newsPath(dates[0], 'beginner'));
  const lesson = lessonAt(dom);
  const note = lesson.querySelector('textarea');
  note.value = 'PRIVATE_DISCUSSION_NOTE';
  note.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
  lesson.querySelector('[data-bg="#e6ffe6"]').click();
  finish(lesson);
  const stored = storedValues(dom.window);
  assert.deepEqual(Object.keys(stored).sort(), ['english-ladder-level', key(dates[0], 'beginner')].sort());
  assert.doesNotMatch(JSON.stringify(stored), /PRIVATE_DISCUSSION_NOTE|quiz|answer/);
  const reopened = load(newsPath(dates[0], 'beginner'), { stored });
  assert.equal(reopened.window.document.querySelector('textarea').value, '');
  assert.match(reopened.window.document.querySelector('.practice-progress').textContent, /^0 of \d+ questions answered/);
});
