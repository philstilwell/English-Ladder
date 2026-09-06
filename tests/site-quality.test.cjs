const {test,afterEach}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');const path=require('node:path');const {JSDOM}=require('jsdom');
const root=path.join(__dirname,'..');const open=[];
afterEach(()=>{open.splice(0).forEach(d=>d.window.close());});
function load(file,{scripts=['site.js'],stored={},hash=''}={}){
 const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{url:`https://englishladder.com/${file}${hash}`,runScripts:'dangerously'});open.push(dom);
 dom.window.HTMLElement.prototype.scrollIntoView=function(){};
 dom.window.fetch=async()=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,'lesson-data.json'),'utf8'))});
 for(const [k,v]of Object.entries(stored))dom.window.localStorage.setItem(k,v);
 scripts.forEach(script=>dom.window.eval(fs.readFileSync(path.join(root,script),'utf8')));
 return dom;
}
const change=(dom,el)=>el.dispatchEvent(new dom.window.Event('change',{bubbles:true}));
test('a selected level persists through Discover, its evergreen stories and main navigation',()=>{
 const d=load('index.html');const doc=d.window.document;doc.querySelector('input[value="advanced"]').click();
 assert.equal(d.window.localStorage.getItem('english-ladder-level'),'advanced');
 for(const link of doc.querySelectorAll('[data-level-link],.explore-story'))assert.match(link.href,/advanced\.html/);
 const next=load('index.html',{stored:{'english-ladder-level':'advanced'}});
 assert.equal(next.window.document.querySelector('input[value="advanced"]').checked,true);
 assert.match(next.window.document.querySelector('#feature-start').href,/advanced\.html#lesson-/);
});
test('level switches preserve the story date',()=>{
 const d=load('beginner.html',{hash:'#lesson-2026-09-03'});
 assert.ok([...d.window.document.querySelectorAll('[data-level-choice]')].every(a=>a.hash==='#lesson-2026-09-03'));
});
test('invalid feature data cannot replace a local lesson link',()=>{
 const d=load('index.html');const doc=d.window.document;const before=doc.querySelector('#feature-start').href;
 const input=doc.querySelector('input[value="advanced"]');input.dataset.lessonHref='https://example.com/';input.click();assert.equal(doc.querySelector('#feature-start').href,before);
});
test('grammar topic search and level filter work together',()=>{
 const d=load('grammar-concepts.html');const doc=d.window.document;const search=doc.querySelector('[data-library-search]');search.value='recently';search.dispatchEvent(new d.window.Event('input'));
 assert.equal(doc.querySelectorAll('[data-library-item]:not([hidden])').length,1);
 const select=doc.querySelector('[data-library-level]');select.value='A1';change(d,select);assert.equal(doc.querySelectorAll('[data-library-item]:not([hidden])').length,0);assert.equal(doc.querySelector('[data-library-empty]').hidden,false);
});
test('drafts are optional, restore when opted in, and remain on page after saving is disabled',()=>{
 const d=load('grammar-concepts/concept-05.html');const doc=d.window.document;const note=doc.querySelector('[data-study-draft]');
 note.value='I saved time by booking online.';note.dispatchEvent(new d.window.Event('input'));assert.equal(d.window.localStorage.length,0);
 const toggle=doc.querySelector('[data-save-study]');toggle.click();
 const raw=d.window.localStorage.getItem('english-ladder-study-v1');assert.match(raw,/booking online/);
 const next=load('grammar-concepts/concept-05.html',{stored:{'english-ladder-study-v1':raw}});assert.equal(next.window.document.querySelector('[data-study-draft]').value,note.value);
 toggle.click();assert.equal(d.window.localStorage.getItem('english-ladder-study-v1'),null);assert.equal(note.value,'I saved time by booking online.');
});
test('saved-word review uses the selected word and its own definition',()=>{
 const d=load('beginner.html',{stored:{'english-ladder-study-v1':JSON.stringify({enabled:true,history:[],words:[],drafts:{}})}});const doc=d.window.document;doc.querySelector('.save-word').click();
 const data=JSON.parse(d.window.localStorage.getItem('english-ladder-study-v1'));assert.equal(data.words.length,1);assert.ok(!/^\d/.test(data.words[0].term));assert.ok(data.words[0].definition.length>5);assert.doesNotMatch(data.words[0].definition,/Save word/);
});
test('daily lesson notes follow the learner into the permanent archive page',()=>{
 const d=load('beginner.html');const doc=d.window.document;
 doc.querySelector('[data-save-study]').click();
 const note=doc.querySelector('[data-study-draft]');note.value='While I wait, I can read.';note.dispatchEvent(new d.window.Event('input'));
 const date=note.closest('.daily-lesson').dataset.lessonKey;
 const raw=d.window.localStorage.getItem('english-ladder-study-v1');
 const next=load(`news/${date}/beginner.html`,{stored:{'english-ladder-study-v1':raw}});
 assert.equal(next.window.document.querySelector('[data-study-draft]').value,note.value);
});
test('clearing saved learning has an undo action',()=>{
 const raw=JSON.stringify({enabled:true,history:[{url:'/grammar-concepts/concept-05.html',title:'By and through'}],words:[],drafts:{}});
 const d=load('continue.html',{stored:{'english-ladder-study-v1':raw}});const doc=d.window.document;doc.querySelector('[data-clear-study]').click();assert.equal(d.window.localStorage.getItem('english-ladder-study-v1'),null);doc.querySelector('[data-undo-study]').click();assert.match(d.window.localStorage.getItem('english-ladder-study-v1'),/By and through/);
});
test('a partial diagnostic does not imply proficiency or recommend a higher level',()=>{
 const d=load('tools.html',{scripts:['tools.js']});d.window.document.dispatchEvent(new d.window.Event('DOMContentLoaded'));
 const doc=d.window.document;doc.querySelector('input[name="diagnostic-0"][value="0"]').checked=true;doc.querySelector('#diagnostic-submit').click();
 assert.match(doc.querySelector('#diagnostic-results').textContent,/1 of 10 answered/);assert.doesNotMatch(doc.querySelector('#diagnostic-results').textContent,/higher|Strong diagnostic/);
});
test('news practice labels its offline sample and avoids demanding invented details',async()=>{
 const d=load('tools.html',{scripts:['tools.js']});d.window.fetch=async()=>{throw Error('offline');};d.window.document.dispatchEvent(new d.window.Event('DOMContentLoaded'));
 const doc=d.window.document;doc.querySelector('#news-build').click();await new Promise(resolve=>setImmediate(resolve));
 const text=doc.querySelector('#news-results').textContent;assert.match(text,/fictional scenario/);assert.match(text,/Use only information in the story/);assert.doesNotMatch(text,/AUKUS|naval/i);
});
test('sentence suggestions preserve size meaning and custom tone input keeps names and obligation',()=>{
 const d=load('tools.html',{scripts:['tools.js']});d.window.document.dispatchEvent(new d.window.Event('DOMContentLoaded'));const doc=d.window.document;
 doc.querySelector('#repair-input').value='The little people in the story built a tiny village.';doc.querySelector('#repair-run').click();assert.match(doc.querySelector('#repair-results').textContent,/original text is unchanged/);assert.match(doc.querySelector('#repair-results').textContent,/size is your meaning/);
 doc.querySelector('#register-input').value='I work in London. Our team must not disclose names.';doc.querySelector('#register-target').value='academic';doc.querySelector('#register-run').click();const result=doc.querySelector('#register-results').textContent;assert.match(result,/I work in London. Our team must not disclose names./);assert.doesNotMatch(result,/further analysis and revision/);
});
test('everyday units default to English only and keep direct unit links',()=>{
 const d=load('us-life.html',{scripts:['us-life.js']});const doc=d.window.document;assert.equal(doc.querySelector('#life-language-select').value,'en');assert.equal(doc.querySelectorAll('.us-life-module:not([hidden])').length,1);
 d.window.location.hash='#shopping';d.window.dispatchEvent(new d.window.HashChangeEvent('hashchange'));assert.equal(doc.querySelector('.us-life-module:not([hidden])').id,'shopping');assert.ok(doc.querySelector('#shopping .life-practice'));
});
test('legacy diagram modal keeps keyboard focus inside and restores the background',()=>{
 const d=load('tools.html',{scripts:[]});const doc=d.window.document;
 doc.body.innerHTML='<main><button class="grammar-image-trigger" data-lightbox-src="diagram.png">Open</button><a href="#">Background link</a><div class="image-lightbox" hidden><button class="image-lightbox-backdrop" data-lightbox-close>Dismiss</button><div role="dialog" aria-modal="true"><button class="image-lightbox-close" data-lightbox-close>Close</button><img class="image-lightbox-image"></div></div></main>';
 d.window.eval(fs.readFileSync(path.join(root,'app.js'),'utf8'));d.window.setupConceptImageLightbox();
 const trigger=doc.querySelector('.grammar-image-trigger');const close=doc.querySelector('.image-lightbox-close');trigger.click();assert.equal(doc.activeElement,close);assert.equal(doc.querySelector('main>a').inert,true);
 close.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Tab',bubbles:true,cancelable:true}));assert.equal(doc.activeElement,close);
 close.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Tab',shiftKey:true,bubbles:true,cancelable:true}));assert.equal(doc.activeElement,close);
 close.dispatchEvent(new d.window.KeyboardEvent('keydown',{key:'Escape',bubbles:true}));assert.equal(doc.activeElement,trigger);assert.equal(doc.querySelector('.image-lightbox').hidden,true);assert.ok(!doc.querySelector('main>a').inert);
});
test('permanent stories open directly and omit repeated introductory headings',()=>{
 const d=load('news/2026-09-06/beginner.html');const doc=d.window.document;assert.equal(doc.querySelector('.daily-lesson').open,true);assert.equal(doc.querySelector('.daily-lesson>summary').hidden,true);assert.equal(doc.querySelector('.lesson-content>.header'),null);
});
