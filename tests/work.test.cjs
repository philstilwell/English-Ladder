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
  assert.equal(d.querySelectorAll('[data-work-course-link]:not([hidden])').length,66);
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
test('course activities never save answers, drafts, progress, or orientation state', () => {
  const dom=setup(),w=dom.window,d=w.document;
  w.Storage.prototype.setItem=()=>assert.fail('Work activities must not save browser records.');
  const orientation=d.querySelector('details.work-orientation');
  assert.equal(orientation.open,false);
  orientation.querySelector('summary').click();
  assert.equal(orientation.open,true);
  const quiz=d.querySelector('[data-work-quiz]');
  quiz.querySelector(`input[value="${quiz.dataset.correct}"]`).click();
  quiz.querySelector('[data-check-answer]').click();
  assert.equal(quiz.querySelector('[data-quiz-feedback]').dataset.result,'correct');
  d.querySelector('[data-expand-lessons]').click();
  change(w,d.querySelector('[data-vocabulary-search]'),'downtime');
  w.dispatchEvent(new w.Event('scroll'));
  assert.equal(w.localStorage.length,0);
  assert.equal(w.sessionStorage.length,0);
  const fresh=setup();
  assert.equal(fresh.window.document.querySelector('details.work-orientation').open,false);
  assert.equal(fresh.window.document.querySelector('input:checked'),null);
  [dom,fresh].forEach(x=>x.window.close());
});
test('every occupation question accepts its one answer and explains each distractor', () => {
  const sources=fs.readdirSync(path.join(root,'content/work/occupations')).filter(n=>n.endsWith('.json'));
  assert.equal(sources.length,25);
  let fourthAnswers=0;
  for(const source of sources){
    const dom=setup(`efsp-${source.replace('.json','')}.html`),d=dom.window.document;
    for(const quiz of d.querySelectorAll('[data-work-quiz]')){
      const inputs=[...quiz.querySelectorAll('input[type="radio"]')];
      assert.equal(inputs.length,4,source);
      const correct=Number(quiz.dataset.correct),feedback=quiz.querySelector('[data-quiz-feedback]');
      if(correct===3)fourthAnswers++;
      for(let index=0;index<4;index++){
        inputs[index].click();
        assert.equal(feedback.textContent,'');
        quiz.querySelector('[data-check-answer]').click();
        assert.equal(feedback.dataset.result,index===correct?'correct':'retry',source);
        assert.ok(feedback.textContent.length>30,source);
      }
    }
    dom.window.close();
  }
  assert.ok(fourthAnswers>0,'The fourth answer position must be used and checked.');
});
test('course, directory, and category pages retire all work records but preserve unrelated preferences', () => {
  const records={
    'english-ladder-work-v2:manufacturing':JSON.stringify({notes:{'module-1':'Old fictional draft'},complete:['module-1']}),
    'english-ladder-work-v2:law':'not-json',
    'english-ladder-work-v2:finance':'{}',
  };
  const preserved={
    'english-ladder-vocabulary-language-v1':'ja',
    'english-ladder-level':'advanced',
    'english-ladder-everyday-completed-v1:arrival':'1',
    'english-ladder-completed-v1:stories/food-market/beginner.html':'1',
    'unrelated':'keep',
  };
  for(const file of [courseFile,'efsp.html','english-for-work/business-professional.html']){
    const dom=setup(file,w=>{
      for(const [key,value] of Object.entries({...records,...preserved}))w.localStorage.setItem(key,value);
      w.Storage.prototype.getItem=()=>assert.fail('Retirement must not read saved drafts or answers.');
      w.Storage.prototype.setItem=()=>assert.fail('Retirement must not create another saved record.');
    }),w=dom.window;
    for(const key of Object.keys(records))assert.equal(Object.hasOwn(w.localStorage,key),false,file);
    assert.deepEqual(Object.fromEntries(Object.entries(w.localStorage)),preserved,file);
    dom.window.close();
  }
});
test('blocked storage and failed removal never disable lessons, navigation, or the accordion', () => {
  for (const mode of ['blocked','failed-removal']) {
    const dom=setup(courseFile,w=>{
      if(mode==='blocked')Object.defineProperty(w,'localStorage',{get(){throw new Error('blocked');}});
      else {
        w.localStorage.setItem('english-ladder-work-v2:manufacturing','not-json');
        w.Storage.prototype.removeItem=()=>{throw new Error('blocked removal');};
      }
    });
    const d=dom.window.document;
    assert.equal(d.querySelector('[data-check-answer]').hidden,false);
    d.querySelector('[data-check-answer]').click();
    assert.match(d.querySelector('[data-quiz-feedback]').textContent,/Choose an answer/);
    d.querySelector('[data-expand-lessons]').click();
    assert.equal(d.querySelectorAll('.work-module[open]').length,8);
    d.querySelector('.work-orientation>summary').click();
    assert.equal(d.querySelector('.work-orientation').open,true);
    assert.equal(d.querySelector('[data-storage-status]'),null);
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
test('all 66 course pages initialize every quiz and preserve static model responses', () => {
  const files=fs.readdirSync(root).filter(n=>/^efsp-.*\.html$/.test(n));
  assert.equal(files.length,66);
  for(const file of files){
    const dom=setup(file),d=dom.window.document;
    assert.equal(d.querySelectorAll('[data-check-answer]:not([hidden])').length,16,file);
    assert.equal(d.querySelectorAll('.work-model blockquote').length,8,file);
    assert.equal(d.querySelectorAll('.work-jump a .work-section-dots').length,8,file);
    assert.equal(d.querySelectorAll('.work-section-dot').length,48,file);
    assert.equal(d.querySelectorAll('[data-work-step]').length,48,file);
    assert.equal(d.querySelector('input[type="checkbox"], [data-work-complete], [data-work-progress], [data-storage-controls], [data-save-notes], [data-clear-work], [data-work-note]'),null,file);
    const orientation=d.querySelector('details.work-orientation');
    assert.ok(orientation,file);
    assert.equal(orientation.open,false,file);
    assert.deepEqual([...orientation.querySelectorAll('h2')].map(h=>h.textContent),['What you will practice','Choose your pace'],file);
    assert.equal(orientation.querySelectorAll('ul li').length,5,file);
    const toolbar=d.querySelector('.work-lesson-tools');
    const main=d.querySelector('main[data-work-course]');
    assert.equal(toolbar.parentElement,main,file);
    assert.equal(d.querySelector('#finished-dialogue-prompts').parentElement,main,file);
    const links=[...toolbar.querySelectorAll('a')];
    assert.equal(links.length,9,file);
    assert.equal(links[7].hash,'#module-8',file);
    assert.equal(links[8].textContent,'Prompts',file);
    assert.equal(links[8].hash,'#finished-dialogue-prompts',file);
    const icon=toolbar.querySelector('.work-lesson-icon .work-card-icon');
    const headingIcon=d.querySelector('.work-hero .work-card-icon');
    assert.ok(icon,file);
    assert.equal(toolbar.firstElementChild,icon.parentElement,file);
    assert.equal(icon.getAttribute('class'),headingIcon.getAttribute('class'),file);
    assert.equal(icon.getAttribute('style'),headingIcon.getAttribute('style'),file);
    assert.equal(icon.parentElement.getAttribute('aria-hidden'),'true',file);
    dom.window.close();
  }
});
