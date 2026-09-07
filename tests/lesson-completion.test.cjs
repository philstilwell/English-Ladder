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

function assertBadges(container, expectedLevels) {
  const markers = badges(container);
  assert.deepEqual(markers.map(marker => marker.dataset.completedLevel), expectedLevels,
    'Title shows all completed levels once, in Beginner–Intermediate–Advanced order');
  for (const marker of markers) {
    const level = marker.dataset.completedLevel;
    assert.equal(marker.getAttribute('role'), 'img');
    assert.equal(marker.getAttribute('aria-label'), `Completed at ${level[0].toUpperCase() + level.slice(1)} level`);
    const title = container.querySelector('.lesson-title-label, .lesson-title-text, a');
    assert.ok(title, 'The completion badge accompanies the story title');
    assert.ok(marker.compareDocumentPosition(title) & 4, 'Completion badge appears before the title');
  }
}

function assertBadge(container, level) {
  assertBadges(container, [level]);
}

function assertButton(lesson, completed) {
  const button = lesson.querySelector('[data-finish-lesson]');
  assert.equal(button.disabled, false, 'Completion remains reversible');
  assert.equal(button.textContent, completed ? 'Completed ✓' : 'Finish lesson ✓');
  assert.equal(button.getAttribute('aria-pressed'), String(completed));
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
  assertButton(lesson, false);
});

test('Finish marks the feed title immediately and persists to its permanent lesson and archive', () => {
  const feed = load('beginner.html');
  const lesson = lessonAt(feed);
  finish(lesson);
  assertButton(lesson, true);
  assert.equal(lesson.querySelector('.completion-message').hidden, false);
  assertBadge(lesson.querySelector('.lesson-title-group'), 'beginner');
  assert.equal(feed.window.localStorage.getItem(key(dates[0], 'beginner')), '1');

  const permanent = load(newsPath(dates[0], 'beginner'), { stored: storedValues(feed.window) });
  assertBadge(permanent.window.document.querySelector('h1'), 'beginner');
  assertButton(lessonAt(permanent), true);
  assert.equal(lessonAt(permanent).querySelector('.completion-message').hidden, false);

  const archive = load('archive.html', { stored: storedValues(permanent.window) });
  assertBadge(archiveTitle(archive, dates[0]), 'beginner');
  assert.equal(badges(archiveTitle(archive, dates[1])).length, 0);
});

test('all level feeds share a story’s badges while completion buttons remain specific to their level and date', () => {
  let stored = {};
  for (const [index, level] of levels.entries()) {
    const dom = load(`${level}.html`, { stored });
    const lesson = lessonAt(dom);
    assertBadges(lesson.querySelector('.lesson-title-group'), levels.slice(0, index));
    assertButton(lesson, false);
    finish(lesson);
    assertBadges(lesson.querySelector('.lesson-title-group'), levels.slice(0, index + 1));
    assertButton(lesson, true);
    assert.equal(badges(lessonAt(dom, dates[1])).length, 0);
    assertButton(lessonAt(dom, dates[1]), false);
    stored = storedValues(dom.window);
    assert.equal(stored[key(dates[0], level)], '1');
  }
  assert.deepEqual(Object.keys(stored).filter(name => name.startsWith(prefix)).sort(),
    levels.map(level => key(dates[0], level)).sort());
  for (const level of levels) {
    const feed = load(`${level}.html`, { stored });
    assertBadges(lessonAt(feed).querySelector('.lesson-title-group'), levels);
    assertButton(lessonAt(feed), true);
    const permanent = load(newsPath(dates[0], level), { stored });
    assertBadges(permanent.window.document.querySelector('h1'), levels);
    assertButton(lessonAt(permanent), true);
  }
});

test('archive shows all completed levels in level order regardless of the preferred level', () => {
  const stored = Object.fromEntries([...levels].reverse().map(level => [key(dates[0], level), '1']));
  stored['english-ladder-level'] = 'advanced';
  const dom = load('archive.html', { stored });
  const title = archiveTitle(dom, dates[0]);
  assertBadges(title, levels);
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

test('unmarking and restoring a lesson persists across feed, permalink and archive without changing sibling levels or dates', () => {
  const stored = Object.fromEntries(levels.map(level => [key(dates[0], level), '1']));
  stored[key(dates[1], 'intermediate')] = '1';
  const permanent = load(newsPath(dates[0], 'intermediate'), { stored });
  const lesson = lessonAt(permanent);
  assertButton(lesson, true);
  finish(lesson);
  assertButton(lesson, false);
  assertBadges(permanent.window.document.querySelector('h1'), ['beginner', 'advanced']);
  assert.equal(permanent.window.localStorage.getItem(key(dates[0], 'intermediate')), null);
  const afterRemoval = storedValues(permanent.window);
  for (const level of ['beginner', 'advanced']) assert.equal(afterRemoval[key(dates[0], level)], '1');
  assert.equal(afterRemoval[key(dates[1], 'intermediate')], '1');

  const archive = load('archive.html', { stored: afterRemoval });
  assertBadges(archiveTitle(archive, dates[0]), ['beginner', 'advanced']);
  assertBadge(archiveTitle(archive, dates[1]), 'intermediate');
  const feed = load('intermediate.html', { stored: afterRemoval });
  assertBadges(lessonAt(feed).querySelector('.lesson-title-group'), ['beginner', 'advanced']);
  assertButton(lessonAt(feed), false);
  assertButton(lessonAt(feed, dates[1]), true);
  finish(lessonAt(feed));
  assertButton(lessonAt(feed), true);
  const restored = load(newsPath(dates[0], 'intermediate'), { stored: storedValues(feed.window) });
  assertBadges(restored.window.document.querySelector('h1'), levels);
  assertButton(lessonAt(restored), true);
  const restoredArchive = load('archive.html', { stored: storedValues(feed.window) });
  assertBadges(archiveTitle(restoredArchive, dates[0]), levels);
});

test('evergreen headings share level badges only for the same story and keep separate completion buttons', () => {
  const story = load('stories/city-trees/intermediate.html');
  finish(lessonAt(story, 'city-trees'));
  assert.equal(story.window.localStorage.getItem(prefix + 'stories/city-trees/intermediate.html'), '1');
  assertBadge(story.window.document.querySelector('h1'), 'intermediate');
  const stored = storedValues(story.window);
  const reopened = load('stories/city-trees/intermediate.html', { stored });
  assertButton(lessonAt(reopened, 'city-trees'), true);
  for (const level of ['beginner', 'advanced']) {
    const other = load(`stories/city-trees/${level}.html`, { stored });
    assertBadge(other.window.document.querySelector('h1'), 'intermediate');
    assertButton(lessonAt(other, 'city-trees'), false);
  }
  const otherStory = load('stories/food-market/intermediate.html', { stored });
  assert.equal(badges(otherStory.window.document).length, 0);
  assertButton(lessonAt(otherStory, 'food-market'), false);
});

test('evergreen completion toggles only the current level of the current story', () => {
  const stored = Object.fromEntries(levels.map(level => [prefix + `stories/city-trees/${level}.html`, '1']));
  stored[prefix + 'stories/food-market/beginner.html'] = '1';
  const story = load('stories/city-trees/beginner.html', { stored });
  assertBadges(story.window.document.querySelector('h1'), levels);
  finish(lessonAt(story, 'city-trees'));
  assertBadges(story.window.document.querySelector('h1'), ['intermediate', 'advanced']);
  assertButton(lessonAt(story, 'city-trees'), false);
  assert.equal(story.window.localStorage.getItem(prefix + 'stories/city-trees/beginner.html'), null);
  const afterRemoval = storedValues(story.window);
  const sibling = load('stories/city-trees/advanced.html', { stored: afterRemoval });
  assertBadges(sibling.window.document.querySelector('h1'), ['intermediate', 'advanced']);
  assertButton(lessonAt(sibling, 'city-trees'), true);
  const otherStory = load('stories/food-market/beginner.html', { stored: afterRemoval });
  assertBadge(otherStory.window.document.querySelector('h1'), 'beginner');
  assertButton(lessonAt(otherStory, 'food-market'), true);
});

test('malformed completion values cannot mark a lesson as complete', () => {
  for (const value of ['0', 'true', '{"completed":true}', '<img src=x onerror=alert(1)>']) {
    const dom = load(newsPath(dates[0], 'beginner'), { stored: { [key(dates[0], 'beginner')]: value } });
    assert.equal(badges(dom.window.document).length, 0, `Reject malformed stored value ${value}`);
    assertButton(lessonAt(dom), false);
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

test('repeated completion toggles and page restores never duplicate completion badges', () => {
  const dom = load('intermediate.html');
  const lesson = lessonAt(dom);
  const button = finish(lesson);
  button.click();
  assert.equal(badges(lesson).length, 0);
  assertButton(lesson, false);
  button.click();
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assertBadge(lesson.querySelector('.lesson-title-group'), 'intermediate');
  assertButton(lesson, true);
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
  assertButton(lesson, true);
  finish(lesson);
  assert.equal(badges(dom.window.document).length, 0);
  assertButton(lesson, false);
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assert.equal(badges(dom.window.document).length, 0);
  finish(lesson);
  assertBadge(dom.window.document.querySelector('h1'), 'beginner');
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

test('blocked removal hides only the current level on this page and a later successful retry persists', () => {
  const stored = Object.fromEntries(levels.map(level => [key(dates[0], level), '1']));
  let restoreRemoval;
  const dom = load(newsPath(dates[0], 'intermediate'), {
    stored,
    beforeScripts(window) {
      const removeItem = window.Storage.prototype.removeItem;
      window.Storage.prototype.removeItem = function () { throw new Error('Removal blocked'); };
      restoreRemoval = () => { window.Storage.prototype.removeItem = removeItem; };
    },
  });
  const lesson = lessonAt(dom);
  finish(lesson);
  assertButton(lesson, false);
  assertBadges(dom.window.document.querySelector('h1'), ['beginner', 'advanced']);
  assert.equal(dom.window.localStorage.getItem(key(dates[0], 'intermediate')), '1', 'Failed removal leaves stored data intact');
  const message = lesson.querySelector('.completion-message');
  assert.equal(message.hidden, false);
  assert.match(message.textContent, /(?:this|current) page/i);
  assert.match(message.textContent, /(?:only|cannot|unavailable|blocked|not saved|could not)/i);
  dom.window.dispatchEvent(new dom.window.Event('pageshow'));
  assertBadges(dom.window.document.querySelector('h1'), ['beginner', 'advanced']);
  assertButton(lesson, false);
  const separatePage = load(newsPath(dates[0], 'intermediate'), { stored: storedValues(dom.window) });
  assertBadges(separatePage.window.document.querySelector('h1'), levels);
  assertButton(lessonAt(separatePage), true);

  restoreRemoval();
  finish(lesson);
  assertButton(lesson, true);
  assertBadges(dom.window.document.querySelector('h1'), levels);
  finish(lesson);
  assertButton(lesson, false);
  assertBadges(dom.window.document.querySelector('h1'), ['beginner', 'advanced']);
  assert.equal(dom.window.localStorage.getItem(key(dates[0], 'intermediate')), null);
  const reopened = load(newsPath(dates[0], 'intermediate'), { stored: storedValues(dom.window) });
  assertBadges(reopened.window.document.querySelector('h1'), ['beginner', 'advanced']);
  assertButton(lessonAt(reopened), false);
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

test('a completion click honors the visible button state even if another tab changed storage first', () => {
  const dom = load(newsPath(dates[0], 'beginner'));
  const lesson = lessonAt(dom);
  assertButton(lesson, false);
  // Simulate another tab saving immediately before its storage event reaches this page.
  dom.window.localStorage.setItem(key(dates[0], 'beginner'), '1');
  finish(lesson);
  assertButton(lesson, true);
  assert.equal(dom.window.localStorage.getItem(key(dates[0], 'beginner')), '1');
  assertBadge(dom.window.document.querySelector('h1'), 'beginner');
  dom.window.localStorage.removeItem(key(dates[0], 'beginner'));
  finish(lesson);
  assertButton(lesson, false);
  assert.equal(dom.window.localStorage.getItem(key(dates[0], 'beginner')), null);
  assert.equal(badges(dom.window.document).length, 0);
});

test('live storage updates refresh all visible level badges without changing the current level’s completion', () => {
  const dom = load(newsPath(dates[0], 'intermediate'), { stored: { [key(dates[0], 'beginner')]: '1' } });
  const { window } = dom;
  const lesson = lessonAt(dom);
  assertBadge(window.document.querySelector('h1'), 'beginner');
  assertButton(lesson, false);
  window.localStorage.setItem(key(dates[0], 'advanced'), '1');
  window.dispatchEvent(new window.StorageEvent('storage', { key: key(dates[0], 'advanced'), storageArea: window.localStorage }));
  assertBadges(window.document.querySelector('h1'), ['beginner', 'advanced']);
  assertButton(lesson, false);
  window.localStorage.setItem(key(dates[0], 'intermediate'), '1');
  window.dispatchEvent(new window.Event('pageshow'));
  assertBadges(window.document.querySelector('h1'), levels);
  assertButton(lesson, true);
  window.localStorage.removeItem(key(dates[0], 'intermediate'));
  window.dispatchEvent(new window.StorageEvent('storage', { key: key(dates[0], 'intermediate'), storageArea: window.localStorage }));
  assertBadges(window.document.querySelector('h1'), ['beginner', 'advanced']);
  assertButton(lesson, false);
});

test('clearing stored completion removes the indicator and restores the Finish button', () => {
  const dom = load(newsPath(dates[0], 'intermediate'), { stored: { [key(dates[0], 'intermediate')]: '1' } });
  const { window } = dom;
  const lesson = lessonAt(dom);
  assertBadge(window.document.querySelector('h1'), 'intermediate');
  window.localStorage.clear();
  window.dispatchEvent(new window.StorageEvent('storage', { key: null, storageArea: window.localStorage }));
  assert.equal(badges(window.document).length, 0);
  assertButton(lesson, false);
  assert.equal(lesson.querySelector('.completion-message').hidden, true);
  finish(lesson);
  assertBadge(window.document.querySelector('h1'), 'intermediate');
  window.localStorage.removeItem(key(dates[0], 'intermediate'));
  window.dispatchEvent(new window.Event('pageshow'));
  assert.equal(badges(window.document).length, 0, 'Returning from browser history rechecks completion');
  assertButton(lesson, false);
});

test('Finish stores only a completion marker and does not save quiz answers or restore a writing box', () => {
  const dom = load(newsPath(dates[0], 'beginner'));
  const lesson = lessonAt(dom);
  assert.equal(lesson.querySelector('textarea'), null);
  lesson.querySelector('[data-bg="#e6ffe6"]').click();
  finish(lesson);
  const stored = storedValues(dom.window);
  assert.deepEqual(Object.keys(stored).sort(), ['english-ladder-level', key(dates[0], 'beginner')].sort());
  assert.doesNotMatch(JSON.stringify(stored), /notes|quiz|answer/);
  const reopened = load(newsPath(dates[0], 'beginner'), { stored });
  assert.equal(reopened.window.document.querySelector('textarea'), null);
  assert.match(reopened.window.document.querySelector('.practice-progress').textContent, /^0 of \d+ questions answered/);
});
