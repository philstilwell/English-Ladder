const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'efsp-manufacturing.html'), 'utf8');
const script = fs.readFileSync(path.join(root, 'work-ready.js'), 'utf8');
const tick = () => new Promise(resolve => setImmediate(resolve));

test('each copy button copies its complete visible prompt with no learner draft', async () => {
  const dom = new JSDOM(html, { url: 'https://englishladder.com/efsp-manufacturing.html', runScripts: 'outside-only' });
  try {
    const w = dom.window, d = w.document;
    let copied;
    Object.defineProperty(w.navigator, 'clipboard', { value: { writeText: async text => { copied = text; } } });
    d.querySelector('[data-work-note]').value = 'PRIVATE LEARNER DRAFT';
    w.eval(script);
    for (const button of d.querySelectorAll('[data-copy-finished]')) {
      assert.equal(button.hidden, false);
      button.click();
      await tick();
      const pre = d.getElementById(button.dataset.copyFinished);
      assert.equal(copied, pre.textContent);
      assert.ok(copied.startsWith('TASK:'));
      assert.ok(copied.endsWith('END REFERENCE'));
      assert.ok(!copied.includes('PRIVATE LEARNER DRAFT'));
      assert.match(button.nextElementSibling.textContent, /Complete prompt copied/);
    }
  } finally { dom.window.close(); }
});

for (const clipboard of [undefined, { writeText: async () => { throw new Error('Permission denied'); } }]) {
  test(`complete text can still be selected when the clipboard is ${clipboard ? 'denied' : 'unavailable'}`, async () => {
    const dom = new JSDOM(html, { runScripts: 'outside-only' });
    try {
      const w = dom.window, d = w.document;
      Object.defineProperty(w.navigator, 'clipboard', { value: clipboard });
      w.eval(script);
      const button = [...d.querySelectorAll('[data-copy-finished]')].at(-1);
      button.closest('.finished-prompt').open = true;
      button.click();
      await tick();
      const pre = d.getElementById(button.dataset.copyFinished);
      assert.equal(w.getSelection().toString(), pre.textContent);
      assert.equal(d.activeElement, pre);
      assert.match(button.nextElementSibling.textContent, /complete prompt is selected/);
    } finally { dom.window.close(); }
  });
}
