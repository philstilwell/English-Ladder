const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.resolve(__dirname, '..');
const script = fs.readFileSync(path.join(root, 'work.js'), 'utf8');

function setup(hash = '') {
  const dom = new JSDOM(fs.readFileSync(path.join(root, 'efsp-manufacturing.html'), 'utf8'), {
    url: `https://englishladder.com/efsp-manufacturing.html${hash}`, runScripts: 'outside-only',
  });
  const w = dom.window, d = w.document, frames = [], observers = [];
  let position = 0, menuHeight = 80, toolbarHeight = 65;
  const rect = (top, height) => ({top, bottom: top + height, height});
  w.requestAnimationFrame = callback => { frames.push(callback); return frames.length; };
  w.ResizeObserver = class {
    constructor(callback) { observers.push(callback); }
    observe() {}
  };
  d.querySelector('.site-masthead').getBoundingClientRect = () => rect(0, menuHeight);
  d.querySelector('.work-lesson-tools').getBoundingClientRect = () => rect(menuHeight, toolbarHeight);
  d.querySelector('#finished-dialogue-prompts').getBoundingClientRect = () => rect(33600 - position, 2000);
  d.querySelector('#ai-practice').getBoundingClientRect = () => rect(36000 - position, 2500);
  const modules = [...d.querySelectorAll('.work-module')];
  const selectors = ['.work-case', '.work-module-body > .work-two-column > section:nth-child(2)',
    '.work-language', '.work-checks', '.work-conversations', '.work-speaking'];
  modules.forEach((module, index) => {
    const start = 800 + index * 4000;
    module.getBoundingClientRect = () => rect(start - position, module.open ? 3500 : 90);
    selectors.forEach((selector, step) => {
      // The first two subsections share a row on desktop.
      const top = start + [200, 200, 800, 1200, 1600, 2000][step];
      module.querySelector(selector).getBoundingClientRect = () => rect(top - position, module.open ? 300 : 0);
    });
    module.scrollIntoView = () => { module.dataset.scrolled = 'true'; };
  });
  w.eval(script);
  const flush = () => { while (frames.length) frames.shift()(); };
  return {dom, w, d, modules, flush,
    scroll(value) { position = value; w.dispatchEvent(new w.Event('scroll')); flush(); },
    resize(menu, toolbar) { menuHeight = menu; toolbarHeight = toolbar; observers.forEach(callback => callback()); flush(); },
    count(index = 0) { return d.querySelectorAll(`.work-jump a[href="#module-${index + 1}"] .is-reached`).length; },
  };
}

test('six outlined markers follow reading position in both directions without recording completion', () => {
  const f = setup();
  assert.equal(f.d.querySelectorAll('.work-section-dot').length, 48);
  assert.equal(f.d.querySelectorAll('[data-work-step]').length, 48);
  assert.deepEqual([...f.d.querySelectorAll('.work-lesson-links a:first-child .work-section-dot')].map(dot => dot.title),
    ['A. Read the situation', 'B. Find the words', 'C. Notice the language',
      'D. Check your understanding', 'E. Conversations', 'F. Say it']);
  assert.equal(f.count(), 0);
  assert.equal(f.d.querySelector('.work-lesson-tools [data-expand-lessons]'), null);
  f.scroll(850);
  assert.equal(f.count(), 2);
  assert.equal(f.d.querySelector('.work-jump [aria-current]').hash, '#module-1');
  f.scroll(1900);
  assert.equal(f.count(), 4);
  assert.match(f.d.querySelector('[data-work-scroll-status]').textContent, /4 of 6/);
  f.scroll(3000);
  assert.equal(f.count(), 6);
  f.scroll(850);
  assert.equal(f.count(), 2);
  f.scroll(0);
  assert.equal(f.count(), 0);
  assert.equal(f.d.querySelector('.work-jump [aria-current]'), null);
  assert.equal(f.d.querySelector('[data-work-complete]'), null);
  assert.equal(f.w.localStorage.length, 0);
  f.dom.window.close();
});

test('collapsed lessons retain their last position and skipped lessons are not marked as reached', () => {
  const f = setup();
  f.scroll(1900);
  f.modules[0].open = false;
  f.modules[0].dispatchEvent(new f.w.Event('toggle'));
  f.scroll(13000);
  assert.equal(f.count(), 4);
  for (let index = 1; index < 8; index++) assert.equal(f.count(index), 0);
  assert.equal(f.d.querySelector('.work-jump [aria-current]'), null);
  f.modules[0].open = true;
  f.modules[0].dispatchEvent(new f.w.Event('toggle'));
  f.scroll(0);
  assert.equal(f.count(), 0);
  f.dom.window.close();
});

test('same-lesson links reopen and scroll, deep links work, and resized menus update the reading line', () => {
  const f = setup('#module-3');
  assert.equal(f.modules[2].open, true);
  f.modules[2].open = false;
  f.d.querySelector('.work-jump a[href="#module-3"]').click();
  f.flush();
  assert.equal(f.modules[2].open, true);
  assert.equal(f.modules[2].dataset.scrolled, 'true');
  f.scroll(750);
  assert.equal(f.count(), 0);
  f.resize(180, 100);
  assert.equal(f.count(), 2);
  assert.equal(f.d.querySelector('[data-work-course]').style.getPropertyValue('--work-navigation-height'), '100px');
  f.dom.window.close();
});

test('the navigation spans the entire page and Prompts follows lesson 08 without lesson markers', () => {
  const f = setup('#finished-dialogue-prompts');
  const toolbar = f.d.querySelector('.work-lesson-tools');
  const main = f.d.querySelector('main[data-work-course]');
  assert.equal(toolbar.parentElement, main);
  assert.equal(f.d.querySelector('#finished-dialogue-prompts').parentElement, main);
  assert.equal(f.d.querySelector('.site-footer').parentElement, main);
  assert.equal(toolbar.closest('#lessons'), null);
  const links = [...toolbar.querySelectorAll('a')];
  assert.equal(links.length, 9);
  assert.equal(links[7].hash, '#module-8');
  assert.equal(links[8].textContent, 'Prompts');
  assert.equal(links[8].hash, '#finished-dialogue-prompts');
  assert.equal(links[8].querySelector('.work-section-dots'), null);
  f.dom.window.close();
});

test('Prompts stays active across both prompt sections without opening or marking skipped lessons', () => {
  const f = setup();
  f.modules.forEach(module => { module.open = false; });
  const link = f.d.querySelector('.work-prompts-link');
  link.click();
  f.flush();
  f.scroll(34000);
  assert.equal(f.d.querySelector('.work-jump [aria-current]'), link);
  f.scroll(36500);
  assert.equal(link.getAttribute('aria-current'), 'location');
  assert.equal(f.d.querySelectorAll('.work-module[open]').length, 0);
  assert.equal(f.d.querySelectorAll('.work-section-dot.is-reached').length, 0);
  f.scroll(0);
  assert.equal(link.hasAttribute('aria-current'), false);
  f.scroll(39000);
  assert.equal(link.hasAttribute('aria-current'), false);
  assert.equal(f.w.localStorage.length, 0);
  f.dom.window.close();
});
