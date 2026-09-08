const {test,afterEach}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');const path=require('node:path');const {JSDOM}=require('jsdom');
const root=path.join(__dirname,'..');const open=[];const key='english-ladder-study-v1';
afterEach(()=>open.splice(0).forEach(d=>d.window.close()));
function load(number=35,stored){
 const file=`grammar-concepts/concept-${String(number).padStart(2,'0')}.html`;
 const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{url:`https://englishladder.com/${file}`,runScripts:'dangerously'});open.push(dom);
 if(stored)dom.window.localStorage.setItem(key,stored);
 dom.window.eval(fs.readFileSync(path.join(root,'site.js'),'utf8'));
 return dom;
}
function choice(question,text){return [...question.querySelectorAll('input')].find(input=>input.closest('label').textContent.trim()===text);}
test('original graphics enlarge, keep keyboard focus, and retain a direct image link',()=>{
 for(const number of [1,5,35,44]){
  const d=load(number);const doc=d.window.document;
  d.window.eval(fs.readFileSync(path.join(root,'app.js'),'utf8'));
  const trigger=doc.querySelector('.grammar-image-trigger');const box=doc.querySelector('.image-lightbox');
  const close=box.querySelector('.image-lightbox-close');const fullImage=box.querySelector('a');
  assert.equal(box.hidden,true);assert.match(trigger.href,new RegExp(`concept-${String(number).padStart(2,'0')}\\.png$`));
  const click=new d.window.MouseEvent('click',{bubbles:true,cancelable:true});trigger.dispatchEvent(click);
  assert.equal(click.defaultPrevented,true);assert.equal(box.hidden,false);
  assert.equal(box.querySelector('img').src,trigger.href);assert.equal(box.querySelector('img').alt,trigger.querySelector('img').alt);
  assert.equal(doc.activeElement,close);assert.equal(doc.querySelector('.page-hero').inert,true);
  assert.equal(fullImage.href,trigger.href);assert.equal(fullImage.target,'_blank');
  close.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Tab',shiftKey:true,bubbles:true,cancelable:true}));assert.equal(doc.activeElement,fullImage);
  fullImage.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Tab',bubbles:true,cancelable:true}));assert.equal(doc.activeElement,close);
  close.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Escape',bubbles:true}));
  assert.equal(box.hidden,true);assert.equal(doc.activeElement,trigger);assert.ok(!doc.querySelector('.page-hero').inert);
  assert.equal(box.querySelector('img').getAttribute('src'),null);
 }
});
test('the reported childhood-ability question grades will and could differently',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');
 assert.match(q.textContent,/When I was seven/);assert.equal(doc.querySelector('textarea'),null);
 choice(q,'will').click();const feedback=q.querySelector('.choice-feedback');assert.match(feedback.textContent,/^Not quite\. “Will” refers to the future/);assert.equal(feedback.dataset.result,'incorrect');assert.match(doc.querySelector('[data-choice-progress]').textContent,/0 of 4 correct/);
 choice(q,'could').click();assert.match(feedback.textContent,/^Correct\. “Could” describes a general past ability/);assert.equal(feedback.dataset.result,'correct');assert.match(doc.querySelector('[data-choice-progress]').textContent,/1 of 4 correct/);
 assert.equal(q.querySelectorAll('input:checked').length,1);
 assert.ok(![...q.querySelectorAll('[data-choice-correct="false"]')].some(o=>/was able/.test(o.closest('label').textContent)));
});
test('wanting or trying to get tickets is not graded as an actual success',()=>{
 const d=load();const q=d.window.document.querySelectorAll('[data-choice-question]')[1];
 for(const text of ['hoped to','tried to']){choice(q,text).click();assert.equal(q.querySelector('.choice-feedback').dataset.result,'incorrect');}
 choice(q,'managed to').click();assert.equal(q.querySelector('.choice-feedback').dataset.result,'correct');
});
test('all 44 grammar lessons expose only choices and all 528 options report the selected explanation',()=>{
 let count=0;
 for(let n=1;n<=44;n++){
  const d=load(n);const doc=d.window.document;
  assert.equal(doc.querySelector('textarea,input[type="text"],[contenteditable="true"]'),null,`concept ${n}`);
  const qs=[...doc.querySelectorAll('[data-choice-question]')];assert.equal(qs.length,4);
  for(const q of qs){
   const inputs=[...q.querySelectorAll('input[type="radio"]')];assert.equal(inputs.length,3);assert.equal(inputs.filter(i=>i.dataset.choiceCorrect==='true').length,1);
   assert.equal(q.querySelector('.choice-feedback').hidden,true);
   for(const input of inputs){input.click();const feedback=q.querySelector('.choice-feedback');assert.equal(feedback.hidden,false);assert.ok(feedback.textContent.includes(input.dataset.choiceFeedback));assert.equal(feedback.dataset.result,input.dataset.choiceCorrect==='true'?'correct':'incorrect');count++;}
  }
  d.window.close();open.pop();
 }
 assert.equal(count,528);
});
test('completion waits for all four correct choices and a changed answer updates the count',()=>{
 const d=load();const doc=d.window.document;const complete=doc.querySelector('[data-complete-study]');const qs=[...doc.querySelectorAll('[data-choice-question]')];
 assert.equal(complete.disabled,true);
 for(const q of qs.slice(0,3))q.querySelector('[data-choice-correct="true"]').click();
 assert.equal(complete.disabled,true);qs[3].querySelector('[data-choice-correct="false"]').click();assert.equal(complete.disabled,true);
 qs[3].querySelector('[data-choice-correct="true"]').click();assert.equal(complete.disabled,false);assert.match(doc.querySelector('[data-choice-progress]').textContent,/4 of 4 correct/);
 qs[0].querySelector('[data-choice-correct="false"]').click();assert.equal(complete.disabled,true);assert.match(doc.querySelector('[data-choice-progress]').textContent,/3 of 4 correct/);
});
test('grammar choices are page-only even when a previous saved record is present',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');
 choice(q,'will').click();assert.equal(d.window.localStorage.getItem(key),null);
 assert.equal(doc.querySelector('[data-save-study]'),null);
 const choices=Object.fromEntries([...doc.querySelectorAll('[data-choice-question]')].map(question=>[
  d.window.location.pathname+':'+question.dataset.studyChoice,question.querySelector('[data-choice-correct="true"]').value
 ]));
 const raw=JSON.stringify({enabled:true,history:[],words:[],drafts:{},choices});
 const next=load(35,raw);const nextDoc=next.window.document;
 assert.equal(nextDoc.querySelector('input[type="radio"]:checked'),null);assert.equal(nextDoc.querySelector('[data-complete-study]').disabled,true);
 assert.ok([...nextDoc.querySelectorAll('.choice-feedback')].every(feedback=>feedback.hidden));
 choice(nextDoc.querySelector('[data-choice-question]'),'could').click();
 assert.match(nextDoc.querySelector('[data-choice-progress]').textContent,/1 of 4 correct/);
 assert.equal(next.window.localStorage.getItem(key),raw);
});
test('unknown saved options cannot create a correct answer or unlock completion',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');
 const stored={enabled:true,history:[],words:[],drafts:{},choices:{[d.window.location.pathname+':'+q.dataset.studyChoice]:'999'}};
 const next=load(35,JSON.stringify(stored));assert.equal(next.window.document.querySelector('input[type="radio"]:checked'),null);assert.equal(next.window.document.querySelector('[data-complete-study]').disabled,true);
});
