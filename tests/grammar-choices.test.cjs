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
test('the reported childhood-ability question grades will and could differently',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');
 assert.match(q.textContent,/When I was seven/);assert.equal(doc.querySelector('textarea'),null);
 choice(q,'will').click();const feedback=q.querySelector('.choice-feedback');assert.match(feedback.textContent,/^Not quite\. Will refers to the future/);assert.equal(feedback.dataset.result,'incorrect');assert.match(doc.querySelector('[data-choice-progress]').textContent,/0 of 4 correct/);
 choice(q,'could').click();assert.match(feedback.textContent,/^Correct\. Could describes a general past ability/);assert.equal(feedback.dataset.result,'correct');assert.match(doc.querySelector('[data-choice-progress]').textContent,/1 of 4 correct/);
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
test('selections are saved only after opt-in, restore with matching feedback, and ignore old text answers',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');choice(q,'will').click();assert.equal(d.window.localStorage.getItem(key),null);
 doc.querySelector('[data-save-study]').click();const raw=d.window.localStorage.getItem(key);const data=JSON.parse(raw);assert.equal(Object.keys(data.choices).length,1);
 const next=load(35,raw);const restored=next.window.document.querySelector('[data-choice-question]');assert.equal(choice(restored,'will').checked,true);assert.match(restored.querySelector('.choice-feedback').textContent,/^Not quite/);
 data.choices={};data.drafts={'/grammar-concepts/concept-35.html:grammar-35-1':'will'};
 const old=load(35,JSON.stringify(data));assert.equal(old.window.document.querySelector('input[type="radio"]:checked'),null);assert.equal(old.window.document.querySelector('textarea'),null);
 doc.querySelector('[data-save-study]').click();assert.equal(d.window.localStorage.getItem(key),null);assert.equal(choice(q,'will').checked,true);
});
test('unknown saved options cannot create a correct answer or unlock completion',()=>{
 const d=load();const doc=d.window.document;const q=doc.querySelector('[data-choice-question]');
 const stored={enabled:true,history:[],words:[],drafts:{},choices:{[d.window.location.pathname+':'+q.dataset.studyChoice]:'999'}};
 const next=load(35,JSON.stringify(stored));assert.equal(next.window.document.querySelector('input[type="radio"]:checked'),null);assert.equal(next.window.document.querySelector('[data-complete-study]').disabled,true);
});
