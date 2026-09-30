const { test, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.join(__dirname, '..');
const windows = [];
afterEach(() => windows.splice(0).forEach(w => w.close()));

function setup(run = true) {
  const w = new JSDOM(fs.readFileSync(path.join(root, 'us-life.html'), 'utf8'), {
    url: 'https://englishladder.com/us-life.html#car-care', runScripts: 'outside-only',
  }).window;
  windows.push(w);
  w.HTMLElement.prototype.scrollIntoView = () => {};
  w.fetch = () => { throw new Error('Dialogue selection must not make a network request'); };
  if (run) w.eval(fs.readFileSync(path.join(root, 'us-life.js'), 'utf8'));
  return w;
}

function assertSelected(block, selected) {
  const tabs = [...block.querySelectorAll('[role="tab"]')];
  const panels = [...block.querySelectorAll('[role="tabpanel"]')];
  assert.equal(tabs.length, 3);
  assert.equal(panels.length, 3);
  tabs.forEach((tab, i) => {
    assert.equal(tab.textContent, String(i + 1));
    assert.equal(tab.getAttribute('aria-selected'), String(i === selected));
    assert.equal(tab.tabIndex, i === selected ? 0 : -1);
    assert.equal(panels[i].hidden, i !== selected);
    assert.equal(tab.getAttribute('aria-controls'), panels[i].id);
    assert.equal(panels[i].getAttribute('aria-labelledby'), tab.id);
  });
}

test('numbered buttons show one complete conversation at a time, starting with the original', () => {
  const w = setup(), d = w.document;
  const blocks = [...d.querySelectorAll('.life-dialogue')].filter(b => b.querySelector('[role="tab"]'));
  assert.ok(blocks.length > 0);
  for (const block of blocks) {
    assertSelected(block, 0);
    assert.ok(block.firstElementChild.classList.contains('life-dialogue-header'));
    const tabs = [...block.querySelectorAll('[role="tab"]')];
    const panels = [...block.querySelectorAll('[role="tabpanel"]')];
    assert.equal(new Set(panels.map(p => p.textContent)).size, 3);
    for (const index of [1, 2, 0]) {
      tabs[index].focus(); tabs[index].click();
      assertSelected(block, index);
      assert.equal(d.activeElement, tabs[index]);
      assert.equal(panels[index].querySelectorAll('.life-dialogue-lines p').length, 10);
    }
  }
  assert.match(d.querySelector('#car-care [role="tabpanel"]').textContent, /can I pay for gas inside/);
  assert.equal(d.querySelectorAll('[data-life-complete][aria-pressed="true"]').length, 0);
});

test('arrow keys wrap between dialogues; Home and End move focus and selection together', () => {
  const w = setup(), block = w.document.querySelector('#car-care .life-dialogue');
  const tabs = [...block.querySelectorAll('[role="tab"]')];
  let index = 0;
  tabs[0].focus();
  for (const [key, next] of [['ArrowLeft', 2], ['ArrowRight', 0], ['End', 2], ['Home', 0], ['ArrowRight', 1]]) {
    const event = new w.KeyboardEvent('keydown', { key, bubbles: true, cancelable: true });
    tabs[index].dispatchEvent(event);
    assert.equal(event.defaultPrevented, true);
    assertSelected(block, next);
    assert.equal(w.document.activeElement, tabs[next]);
    index = next;
  }
});

test('unit and language changes preserve the selected conversation without changing progress', () => {
  const w = setup(), d = w.document, block = d.querySelector('#car-care .life-dialogue');
  block.querySelectorAll('[role="tab"]')[2].click();
  d.querySelector('[data-definition-language="fr"]').click();
  assertSelected(block, 2);
  for (const id of ['arrival', 'car-care']) {
    w.history.replaceState(null, '', '#' + id);
    w.dispatchEvent(new w.HashChangeEvent('hashchange'));
  }
  assertSelected(block, 2);
  assert.equal(d.querySelector('.us-life-module:not([hidden])').id, 'car-care');
  assert.equal(d.querySelector('[data-life-complete="car-care"]').getAttribute('aria-pressed'), 'false');
});

test('all three conversations are readable if JavaScript is unavailable', () => {
  const w = setup(false), block = w.document.querySelector('#car-care .life-dialogue');
  const panels = [...block.querySelectorAll('[data-life-dialogue]')];
  assert.equal(panels.length, 3);
  panels.forEach(panel => assert.equal(panel.hidden, false));
  assert.equal(block.querySelectorAll('[role="tab"]').length, 0);
});
