const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const prefix = 'english-ladder-everyday-completed-v1:';
const windows = [];
afterEach(() => windows.splice(0).forEach(w => w.close()));

function setup(saved = {}, configure = () => {}) {
  const w = new JSDOM(fs.readFileSync(path.join(root, 'us-life.html'), 'utf8'), {
    url: 'https://englishladder.com/us-life.html', runScripts: 'outside-only',
  }).window;
  windows.push(w);
  w.HTMLElement.prototype.scrollIntoView = () => {};
  Object.entries(saved).forEach(([key, value]) => w.localStorage.setItem(key, value));
  w.fetch = () => { throw new Error('Completion must not send a network request'); };
  configure(w);
  w.eval(fs.readFileSync(path.join(root, 'us-life.js'), 'utf8'));
  return w;
}
const button = (w, id) => w.document.querySelector(`[data-life-complete="${id}"]`);
const marks = (w, id) => [...w.document.querySelectorAll(`[data-unit-icon="${id}"]`)]
  .map(icon => icon.parentElement.querySelector('.life-completion-mark'));
function assertState(w, id, done) {
  assert.equal(button(w, id).textContent, done ? 'Completed' : 'Mark as completed');
  assert.equal(button(w, id).getAttribute('aria-pressed'), String(done));
  assert.equal(marks(w, id).length, 2);
  marks(w, id).forEach(mark => {
    assert.equal(mark.hidden, !done);
    assert.equal(mark.getAttribute('aria-label'), 'Completed');
  });
}
const saved = w => Object.fromEntries(Object.keys(w.localStorage).map(key => [key, w.localStorage.getItem(key)]));

test('all 24 units toggle both marks, persist on reload, and undo independently', () => {
  const w = setup({ 'english-ladder-completed-v1:news/example': '1' });
  const ids = [...w.document.querySelectorAll('.us-life-module')].map(unit => unit.id);
  assert.equal(ids.length, 24);
  assert.equal(w.document.querySelectorAll('[data-life-complete]').length, 24);
  for (const id of ids) {
    assertState(w, id, false);
    const unit = w.document.getElementById(id);
    assert.ok(unit.lastElementChild.contains(button(w, id)), 'Button is at the end of the unit');
    button(w, id).focus();
    button(w, id).click();
    assert.equal(w.document.activeElement, button(w, id));
    assertState(w, id, true);
    assert.equal(w.localStorage.getItem(prefix + id), '1');
  }
  const reloaded = setup(saved(w));
  ids.forEach(id => assertState(reloaded, id, true));
  button(reloaded, 'money').click();
  assertState(reloaded, 'money', false);
  assertState(reloaded, 'shopping', true);
  assert.equal(reloaded.localStorage.getItem(prefix + 'money'), null);
  assert.equal(reloaded.localStorage.getItem('english-ladder-completed-v1:news/example'), '1');
  assert.equal(reloaded.document.querySelectorAll('.life-completion-mark').length, 48);
  assertState(setup(saved(reloaded)), 'money', false);
});

test('navigation and explanation languages do not mark a unit or reset completion', () => {
  const w = setup({ [prefix + 'money']: '1' });
  const navigate = id => {
    w.history.replaceState(null, '', '#' + id);
    w.dispatchEvent(new w.HashChangeEvent('hashchange'));
  };
  navigate('shopping');
  assertState(w, 'shopping', false);
  assertState(w, 'money', true);
  w.document.querySelector('[data-definition-language="fr"]').click();
  navigate('money');
  assertState(w, 'money', true);
  assert.equal(w.document.querySelector('.us-life-module:not([hidden])').id, 'money');
});

test('other tabs and browser history refresh both marks without losing another unit', () => {
  const w = setup({ [prefix + 'money']: '1' });
  w.localStorage.setItem(prefix + 'shopping', '1');
  w.dispatchEvent(new w.StorageEvent('storage', { key: prefix + 'shopping', newValue: 'stale' }));
  assertState(w, 'shopping', true);
  button(w, 'money').click();
  assertState(w, 'money', false);
  assert.equal(w.localStorage.getItem(prefix + 'shopping'), '1');
  w.localStorage.removeItem(prefix + 'shopping');
  w.dispatchEvent(new w.PageTransitionEvent('pageshow', { persisted: true }));
  assertState(w, 'shopping', false);
  button(w, 'money').click();
  w.localStorage.clear();
  w.dispatchEvent(new w.StorageEvent('storage', { key: null }));
  assertState(w, 'money', false);
});

test('blocked storage still toggles for this page and explains that it cannot save', () => {
  const w = setup({}, w => Object.defineProperty(w, 'localStorage', {
    get() { throw new Error('Blocked'); },
  }));
  for (const done of [true, false, true]) {
    button(w, 'arrival').click();
    w.dispatchEvent(new w.PageTransitionEvent('pageshow', { persisted: true }));
    assertState(w, 'arrival', done);
    assert.match(w.document.querySelector('#arrival .life-completion-status').textContent, /could not save.*only on this page/);
  }
  assertState(w, 'money', false);
});

test('failed saves and removals preserve the visible choice until storage works again', () => {
  const w = setup({ [prefix + 'money']: '1' });
  const originalSet = w.Storage.prototype.setItem, originalRemove = w.Storage.prototype.removeItem;
  w.Storage.prototype.setItem = w.Storage.prototype.removeItem = () => { throw new Error('Quota'); };
  button(w, 'money').click();
  button(w, 'shopping').click();
  w.dispatchEvent(new w.StorageEvent('storage', { key: null }));
  assertState(w, 'money', false);
  assertState(w, 'shopping', true);
  assert.equal(w.localStorage.getItem(prefix + 'money'), '1');
  assert.equal(w.localStorage.getItem(prefix + 'shopping'), null);
  w.Storage.prototype.setItem = originalSet;
  w.Storage.prototype.removeItem = originalRemove;
  button(w, 'money').click();
  button(w, 'money').click();
  assert.equal(w.localStorage.getItem(prefix + 'money'), null);
  assert.doesNotMatch(w.document.querySelector('#money .life-completion-status').textContent, /could not save/);
});

test('invalid stored values cannot create completion marks', () => {
  const w = setup(Object.fromEntries(['arrival', 'money', 'shopping', 'food'].map((id, index) =>
    [prefix + id, ['true', '0', '{}', '<img src=x>'][index]])));
  ['arrival', 'money', 'shopping', 'food'].forEach(id => assertState(w, id, false));
  assert.equal(w.document.querySelectorAll('.life-completion-mark:not([hidden])').length, 0);
});
