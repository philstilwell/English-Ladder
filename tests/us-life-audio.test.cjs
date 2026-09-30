const {test, afterEach} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.join(__dirname, '..');
const windows = [];
afterEach(() => windows.splice(0).forEach(w => w.close()));
function setup(play) {
  const w = new JSDOM(fs.readFileSync(path.join(root, 'us-life.html'), 'utf8'),
    {url: 'https://englishladder.com/us-life.html', runScripts: 'outside-only'}).window;
  windows.push(w);
  const played = [], paused = [];
  w.HTMLMediaElement.prototype.play = function() { played.push(this); return play ? play() : Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause = function() { paused.push(this); };
  w.eval(fs.readFileSync(path.join(root, 'us-life-audio.js'), 'utf8'));
  return {w, d: w.document, played, paused};
}
test('all 288 links have real files and no audio starts or downloads on page load', () => {
  const {d, played} = setup();
  assert.equal(d.querySelectorAll('[data-pronunciation]').length, 288);
  assert.equal(played.length, 0);
  for (const link of d.querySelectorAll('[data-pronunciation]')) {
    assert.ok(fs.existsSync(path.join(root, link.getAttribute('href'))));
    assert.equal(link.type, 'audio/mpeg');
  }
  assert.equal(d.querySelectorAll('audio[src], audio[autoplay]').length, 0);
});
test('Listen starts the selected file, replaces previous audio, and stops on unit navigation', () => {
  const {w, d, played, paused} = setup();
  const a = d.querySelector('#arrival [data-pronunciation]');
  const b = d.querySelector('#car-care [data-pronunciation]');
  a.click();
  assert.equal(played[0].src, a.href);
  assert.equal(played[0].closest('[data-pronunciation-player]').hidden, false);
  b.click();
  assert.equal(paused[0], played[0]);
  assert.equal(played[0].closest('[data-pronunciation-player]').hidden, true);
  assert.equal(played[1].src, b.href);
  assert.equal(d.querySelector('#car-care [data-pronunciation-fallback]').href, b.href);
  w.dispatchEvent(new w.HashChangeEvent('hashchange'));
  assert.equal(paused[1], played[1]);
  assert.equal(d.querySelectorAll('[data-pronunciation-player]:not([hidden])').length, 0);
});
test('blocked playback offers the direct file and stale failures do not replace the current status', async () => {
  const rejects = [];
  const {d} = setup(() => new Promise((resolve, reject) => rejects.push(reject)));
  const links = d.querySelectorAll('#car-care [data-pronunciation]');
  links[0].click(); links[1].click();
  rejects[0](new Error('stale'));
  await new Promise(resolve => setImmediate(resolve));
  const status = d.querySelector('#car-care [data-pronunciation-status]');
  assert.equal(status.textContent, `Listen: ${links[1].dataset.pronunciation}`);
  rejects[1](new Error('blocked'));
  await new Promise(resolve => setImmediate(resolve));
  assert.match(status.textContent, /Try Open audio file/);
  assert.equal(d.querySelector('#car-care [data-pronunciation-fallback]').href, links[1].href);
});
test('modified clicks retain normal browser behavior', () => {
  const {w,d,played} = setup();
  const event = new w.MouseEvent('click', {button: 0, ctrlKey: true, cancelable: true});
  d.querySelector('[data-pronunciation]').dispatchEvent(event);
  assert.equal(event.defaultPrevented, false);
  assert.equal(played.length, 0);
});
