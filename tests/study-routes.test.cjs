const {test, afterEach} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.join(__dirname, '..');
const source = file => fs.readFileSync(path.join(root, file), 'utf8');
const windows = [];
afterEach(() => windows.splice(0).forEach(w => w.close()));

function setup(file, suffix = '', scripts = []) {
  const w = new JSDOM(source(file), {url: `https://englishladder.com/${file}${suffix}`, runScripts: 'outside-only'}).window;
  windows.push(w);
  w.HTMLElement.prototype.scrollIntoView = function () {};
  w.fetch = () => { throw new Error('Routes must not fetch content'); };
  scripts.forEach(script => w.eval(source(script)));
  w.eval(source('study-routes.js'));
  return w;
}
const next = w => w.document.querySelector('.study-route-next a');
const progress = w => w.document.querySelector('.study-route-progress');
function move(w, hash) {
  w.history.replaceState(null, '', hash);
  w.dispatchEvent(new w.HashChangeEvent('hashchange'));
}

test('reading routes follow every level and retain the route when the student changes level', () => {
  for (const level of ['beginner', 'intermediate', 'advanced']) {
    const w = setup(`stories/food-market/${level}.html`, '?route=reading', ['site.js']);
    assert.match(progress(w).textContent, /Activity 1 of 3/);
    assert.equal(next(w).href, `https://englishladder.com/stories/city-trees/${level}.html?route=reading`);
    for (const a of w.document.querySelectorAll('[data-level-choice]')) {
      assert.equal(new URL(a.href).searchParams.get('route'), 'reading');
    }
    assert.equal(w.localStorage.getItem('route'), null);
  }
});

test('the second reading leads to published news and older bookmarked final readings stay usable', () => {
  const w = setup('stories/city-trees/advanced.html', '?route=reading');
  assert.match(progress(w).textContent, /Activity 2 of 3/);
  const url = new URL(next(w).href);
  assert.match(url.pathname, /^\/news\/\d{4}-\d{2}-\d{2}\/advanced.html$/);
  assert.ok(fs.existsSync(path.join(root, url.pathname)));
  const end = setup('news/2026-09-06/advanced.html', '?route=reading');
  assert.match(progress(end).textContent, /Activity 3 of 3/);
  assert.match(next(end).href, /study-routes.html#reading$/);
  assert.match(end.document.querySelector('.study-route-next').textContent, /last activity/);
});

test('the guide uses the existing reading-level choice without altering everyday or work links', () => {
  const w = setup('study-routes.html', '', ['site.js']);
  const input = w.document.querySelector('input[value="advanced"]');
  input.checked = true; input.dispatchEvent(new w.Event('change'));
  const links = [...w.document.querySelectorAll('#reading ol a')];
  assert.equal(links.length, 3);
  links.forEach(a => assert.match(a.href, /advanced.html\?route=reading$/));
  assert.match(w.document.querySelector('#everyday ol a').href, /us-life.html\?route=everyday#arrival$/);
  assert.match(w.document.querySelector('#work ol a').href, /efsp-project-management.html\?route=work#module-1$/);
});

test('ordinary browsing, unknown routes and unrelated lessons get no route navigation', () => {
  for (const suffix of ['', '?route=unknown', '?route=constructor', '?route=work']) {
    const w = setup('stories/city-trees/beginner.html', suffix);
    assert.equal(progress(w), null);
    assert.equal(next(w), null);
    assert.equal(w.localStorage.length, 0);
  }
});

test('US-life next steps follow the route, skip links preserve it, and ordinary units restore their own next step', () => {
  const w = setup('us-life.html', '?route=everyday#arrival', ['us-life.js']);
  assert.match(next(w).href, /#shopping$/);
  assert.equal(w.document.querySelector('#arrival .life-practice > a').hidden, true);
  move(w, '#shopping');
  assert.equal(w.document.querySelector('#shopping').hidden, false);
  assert.match(progress(w).textContent, /Activity 2 of 3/);
  assert.match(next(w).href, /#transportation$/);
  move(w, '#life-language-controls');
  assert.match(progress(w).textContent, /Activity 2 of 3/);
  assert.equal(w.document.querySelector('#shopping').hidden, false);
  move(w, '#[]'); // Arbitrary fragments cannot become invalid selectors.
  assert.match(progress(w).textContent, /Activity 2 of 3/);
  move(w, '#housing');
  assert.equal(progress(w), null);
  assert.equal(w.document.querySelector('#shopping .life-practice > a').hidden, false);
  move(w, '#transportation');
  assert.match(progress(w).textContent, /Activity 3 of 3/);
  assert.equal(w.document.querySelectorAll('.study-route-next').length, 1);
});

test('work route opens the selected lessons and points from module 2 to module 7 without marking completion', () => {
  const w = setup('efsp-project-management.html', '?route=work#module-1', ['work.js']);
  assert.equal(w.document.querySelector('#module-1').open, true);
  assert.match(next(w).href, /#module-2$/);
  move(w, '#module-2');
  assert.equal(w.document.querySelector('#module-2').open, true);
  assert.match(next(w).href, /#module-7$/);
  move(w, '#module-7');
  assert.match(progress(w).textContent, /Activity 3 of 3/);
  assert.equal(w.document.querySelectorAll('[data-work-complete]:checked').length, 0);
});

test('a damaged route catalog leaves the lesson available', () => {
  const w = setup('stories/city-trees/beginner.html');
  w.history.replaceState(null, '', '?route=reading');
  w.document.querySelector('[data-study-routes]').textContent = 'invalid';
  assert.doesNotThrow(() => w.eval(source('study-routes.js')));
  assert.equal(progress(w), null);
  assert.ok(w.document.querySelector('.daily-lesson'));
});
