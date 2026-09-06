const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const root = path.resolve(__dirname, '..');
const script = fs.readFileSync(path.join(root,'work.js'),'utf8');
const courseFile = 'efsp-manufacturing.html';

function setup(file=courseFile, before=()=>{}) {
  const dom = new JSDOM(fs.readFileSync(path.join(root,file),'utf8'), {url:`https://englishladder.com/${file}`,runScripts:'outside-only'});
  before(dom.window);
  dom.window.eval(script);
  return dom;
}
function change(w, node, value, event='input') {
  node.value=value;
  node.dispatchEvent(new w.Event(event,{bubbles:true}));
}

test('directory search combines words and category; empty state recovers', () => {
  const dom=setup('efsp.html'),w=dom.window,d=w.document;
  const search=d.querySelector('[data-course-search]'),category=d.querySelector('[data-course-category]');
  change(w,search,'nursing');
  assert.equal(d.querySelectorAll('[data-work-course-link]:not([hidden])').length,1);
  change(w,category,'Technology & data','change');
  assert.equal(d.querySelector('[data-course-empty]').hidden,false);
  change(w,search,'');change(w,category,'','change');
  assert.equal(d.querySelectorAll('[data-work-course-link]:not([hidden])').length,41);
  dom.window.close();
});
test('quiz handles no answer, wrong answer, correction, and resets stale feedback', () => {
  const dom=setup(),w=dom.window,d=w.document,q=d.querySelector('[data-work-quiz]');
  const button=q.querySelector('button'),feedback=q.querySelector('[data-quiz-feedback]');
  button.click();assert.match(feedback.textContent,/Choose an answer/);
  const correct=Number(q.dataset.correct),wrong=(correct+1)%3;
  q.querySelectorAll('input')[wrong].click();button.click();
  assert.equal(feedback.dataset.result,'retry');assert.match(feedback.textContent,/Try again/);
  q.querySelectorAll('input')[correct].click();assert.equal(feedback.textContent,'');button.click();
  assert.equal(feedback.dataset.result,'correct');assert.ok(feedback.textContent.length>35);
  dom.window.close();
});
test('drafts are opt-in, restore accurately, and remain isolated by course', () => {
  const dom=setup(),w=dom.window,d=w.document,key='english-ladder-work-v2:manufacturing';
  const note=d.querySelector('[data-work-note]'),save=d.querySelector('[data-save-notes]');
  change(w,note,'These are five sample words.');
  assert.equal(w.localStorage.getItem(key),null);
  assert.match(note.parentElement.querySelector('[data-word-count]').textContent,/5 words/);
  save.click();d.querySelector('[data-work-complete]').click();
  const state=w.localStorage.getItem(key);
  assert.match(state,/These are five/);
  const restored=setup(courseFile,win=>win.localStorage.setItem(key,state));
  assert.equal(restored.window.document.querySelector('[data-work-note]').value,note.value);
  assert.match(restored.window.document.querySelector('[data-work-progress]').textContent,/1 of 8/);
  const other=setup('efsp-law.html',win=>win.localStorage.setItem(key,state));
  assert.equal(other.window.document.querySelector('[data-work-note]').value,'');
  d.querySelector('[data-clear-work]').click();
  assert.equal(w.localStorage.getItem(key),null);assert.equal(note.value,'');assert.equal(save.checked,false);
  [dom,restored,other].forEach(x=>x.window.close());
});
test('blocked or malformed storage does not disable lessons and checks', () => {
  for (const mode of ['blocked','malformed']) {
    const dom=setup(courseFile,w=>{
      if(mode==='blocked')Object.defineProperty(w,'localStorage',{get(){throw new Error('blocked');}});
      else w.localStorage.setItem('english-ladder-work-v2:manufacturing','not-json');
    });
    const d=dom.window.document;
    assert.equal(d.querySelector('[data-check-answer]').hidden,false);
    d.querySelector('[data-save-notes]').click();
    assert.ok(d.querySelector('[data-storage-status]').textContent);
    dom.window.close();
  }
});
test('vocabulary search, lesson expansion, and fragment navigation work', () => {
  const dom=setup(),w=dom.window,d=w.document;
  change(w,d.querySelector('[data-vocabulary-search]'),'downtime');
  assert.equal(d.querySelectorAll('[data-work-term]:not([hidden])').length,1);
  const expand=d.querySelector('[data-expand-lessons]');expand.click();
  assert.equal(d.querySelectorAll('.work-module[open]').length,8);expand.click();
  assert.equal(d.querySelectorAll('.work-module[open]').length,0);
  w.location.hash='#module-4';w.dispatchEvent(new w.Event('hashchange'));
  assert.equal(d.querySelector('#module-4').open,true);
  dom.window.close();
});
test('all 41 course pages initialize every quiz and preserve static model responses', () => {
  const files=fs.readdirSync(root).filter(n=>/^efsp-.*\.html$/.test(n));
  assert.equal(files.length,41);
  for(const file of files){
    const dom=setup(file),d=dom.window.document;
    assert.equal(d.querySelectorAll('[data-check-answer]:not([hidden])').length,16,file);
    assert.equal(d.querySelectorAll('.work-model blockquote').length,8,file);
    dom.window.close();
  }
});
