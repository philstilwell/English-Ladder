import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';
import { env, call, login, origin } from './harness.mjs';
import bank from '../vocabulary-bank.json' with { type: 'json' };
import reserve from '../vocabulary-reserve.json' with { type: 'json' };
const path = '/api/vocabulary-practice/state';
const read = (e, cookie, p = path) => call(e, p, { headers: { Cookie: cookie } });
const patch = (e, cookie, body) => call(e, path, { method: 'PATCH', headers: { Cookie: cookie, Origin: origin, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
const batch = (revision = 0) => ({ field: 'batch', batch: 1, entries: bank.items.slice(0,10).map(i => ({ number:i.number, revision, answer: 'Practice answer ' + i.number, sentence: 'Fictional sentence using ' + i.term + '.' })) });

test('only fifty authored words are served; reserve preserves all distinct words in source order', async () => {
  assert.equal(bank.items.length,50); assert.equal(reserve.items.length,5184); assert.equal(reserve.duplicates.length,297);
  assert.deepEqual(bank.items.map(i=>i.term),reserve.items.slice(0,50).map(i=>i.term));
  for(const item of bank.items) for(const field of ['term','meaning','phrases','forms','prompt','answer','task']) assert.ok(item[field]?.trim());
  const e=env(),student=await login(e);
  assert.equal((await call(e,'/api/vocabulary-practice')).status,401);
  const data=await(await read(e,student.cookie,'/api/vocabulary-practice')).json(); assert.equal(data.items.length,50);
  assert.doesNotMatch(JSON.stringify(data),/sourceRow|sourceUrl|duplicates/);
  for(const p of ['/vocabulary-reserve.json','/vocabulary-bank.json','/api/vocabulary-reserve'])assert.equal((await read(e,student.cookie,p)).status,404);
});

test('batch saves are atomic, isolated, retry-safe, and preserve independent question choices', async () => {
  const e=env(),student=await login(e),other=await login(e,'other-test','https://cd26.englishladder.com');
  const input=batch();assert.equal((await patch(e,student.cookie,input)).status,200);
  assert.equal((await patch(e,student.cookie,input)).status,200);
  let data=await(await read(e,student.cookie)).json();assert.equal(data.entries.length,10);assert(data.entries.every(i=>i.revision===1));
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json()).entries,[]);
  assert.equal((await call(e,path,{headers:{Cookie:other.cookie}})).status,401);
  assert.equal((await patch(e,student.cookie,{number:2,field:'question',value:true,revision:1})).status,200);
  const stale=batch(1);stale.entries.forEach(i=>i.sentence+=' Changed.');assert.equal((await patch(e,student.cookie,stale)).status,409);
  data=await(await read(e,student.cookie)).json();assert(!data.entries.some(i=>i.sentence.includes('Changed')));
  stale.entries[1].revision=2;assert.equal((await patch(e,student.cookie,stale)).status,200);
  data=await(await read(e,student.cookie)).json();assert.equal(data.entries.find(i=>i.number===2).question,true);
  assert(data.entries.every(i=>i.sentence.includes('Changed')));
});

test('teacher previews, cross-origin requests, malformed batches and deleted accounts cannot write', async () => {
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');
  assert.equal((await patch(e,teacher.cookie,batch())).status,403);
  assert.equal((await call(e,path,{method:'PATCH',headers:{Cookie:student.cookie,Origin:'https://other.test','Content-Type':'application/json'},body:JSON.stringify(batch())})).status,403);
  for(const body of [{...batch(),batch:6},{...batch(),entries:batch().entries.slice(0,9)},{...batch(),entries:batch().entries.map(i=>({...i,sentence:'x'.repeat(1001)}))},{...batch(),entries:batch().entries.map(i=>({...i,finished:true}))}]) assert.equal((await patch(e,student.cookie,body)).status,400);
  assert.deepEqual((await(await read(e,student.cookie)).json()).entries,[]);
  await patch(e,student.cookie,batch());
  await e.FEEDBACK_STORE.get('ab26').fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await e.FEEDBACK_STORE.get('ab26').storage.list({prefix:'vocabulary:'})).size,0);
  assert.equal((await patch(e,student.cookie,batch())).status,410);
});

const flush=async()=>{for(let i=0;i<15;i++)await new Promise(r=>setTimeout(r,1));};
async function browser(custom, teacher=false) {
  const e=env(),user=await login(e,teacher?'teacher-test':'student-test');
  const dom=new JSDOM('<div id="root"></div>',{url:origin,runScripts:'outside-only',pretendToBeVisual:true}),w=dom.window;
  w.AbortController=AbortController;const requests=[];let copied='';
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
  for(const name of ['practice-prompt','practice-position','vocabulary-practice'])w.eval(readFileSync(new URL('../public/'+name+'.js',import.meta.url),'utf8'));
  const api=async(p,options={})=>{requests.push({path:p,...options});const result=await(custom?.(p,options)||call(e,p,{...options,headers:{Cookie:user.cookie,...(options.method?{Origin:origin}:{}),...options.headers}}));const data=await result.json();if(!result.ok)throw Object.assign(new Error(data.error),{status:result.status});return data;};
  const root=w.document.getElementById('root'),view=w.VocabularyPractice.create({root,api,expired:error=>{if(error.status===401){view.clear();return true;}return false;}});
  await view.open(teacher);return {e,w,root,view,requests,get copied(){return copied;}};
}
const type=(b,selector,text)=>{const node=b.root.querySelector(selector);node.value=text;node.dispatchEvent(new b.w.Event('input',{bubbles:true}));};
const clickText=(b,text)=>[...b.root.querySelectorAll('button')].find(n=>n.textContent===text).click();

test('ten-word batches save drafts, copy current answers only, and resume the saved batch',async()=>{
  const b=await browser();assert.equal(b.root.querySelectorAll('.vocabulary-item').length,10);assert.equal(b.requests.filter(r=>r.method).length,0);
  type(b,'#vocabulary-answer-1','recruiter');type(b,'#vocabulary-sentence-1','Our café will recruit two people.');
  clickText(b,'Copy AI prompt');await flush();assert.match(b.copied,/Our café will recruit two people/);assert.equal((b.copied.match(/"word":/g)||[]).length,10);assert.doesNotMatch(b.copied,/Alex|ab26|sourceRow|session|password/i);
  assert.equal(b.requests.filter(r=>r.method).length,0);
  type(b,'#vocabulary-sentence-1','We recruit kind workers.');assert.equal(b.root.querySelector('.practice-copy-button').textContent,'Copy AI prompt');
  clickText(b,'Save batch');await flush();assert.match(b.root.textContent,/Your batch is saved/);
  b.root.querySelector('[data-number="1"][data-field="question"]').click();await flush();assert.match(b.root.textContent,/Questions \(1\)/);
  clickText(b,'Next batch');await flush();assert.equal(b.root.querySelectorAll('.vocabulary-item').length,10);assert.ok(b.root.querySelector('#vocabulary-answer-11'));
  b.view.clear();await b.view.open();assert.ok(b.root.querySelector('#vocabulary-answer-11'));
  assert.equal(b.root.firstElementChild.textContent,'Last saved place: Batch 2 · Words 11–20');
  clickText(b,'Previous batch');await flush();assert.equal(b.root.querySelector('#vocabulary-sentence-1').value,'We recruit kind workers.');
  b.view.clear();assert.equal(b.root.textContent,'');assert.equal(b.root.hidden,true);b.w.close();
});

test('failed batch saves preserve drafts and stop navigation; conflicts require an explicit retry',async()=>{
  let fail=true;const b=await browser((p,o)=>o.method==='PATCH'&&JSON.parse(o.body).field==='batch'&&fail?Response.json({error:'offline'},{status:503}):null);
  type(b,'#vocabulary-sentence-1','We recruit helpers.');clickText(b,'Next batch');await flush();assert.ok(b.root.querySelector('#vocabulary-answer-1'));assert.equal(b.root.querySelector('#vocabulary-sentence-1').value,'We recruit helpers.');assert.match(b.root.textContent,/could not be saved/);
  fail=false;clickText(b,'Save batch');await flush();
  const store=b.e.FEEDBACK_STORE.get('ab26'),saved=await store.storage.get('vocabulary:item:1');await store.storage.put({'vocabulary:item:1':{...saved,sentence:'Work from another tab.',revision:saved.revision+1}});
  type(b,'#vocabulary-sentence-1','My newer draft.');clickText(b,'Save batch');await flush();assert.match(b.root.textContent,/changed on another page/);assert.equal((await store.storage.get('vocabulary:item:1')).sentence,'Work from another tab.');
  clickText(b,'Next batch');await flush();assert.ok(b.root.querySelector('#vocabulary-answer-1'));
  clickText(b,'Save batch');await flush();assert.equal((await store.storage.get('vocabulary:item:1')).sentence,'My newer draft.');b.view.clear();b.w.close();
});

test('teacher preview is read-only and late loads cannot restore cleared content',async()=>{
  const b=await browser(null,true);assert(b.root.querySelector('#vocabulary-answer-1').disabled);clickText(b,'Next batch');await flush();clickText(b,'Copy AI prompt');await flush();assert.equal(b.requests.filter(r=>r.method).length,0);b.view.clear();b.w.close();
  let release,delay=false;const c=await browser((p,o)=>delay&&p==='/api/vocabulary-practice'?new Promise(r=>{release=r;}):null);c.view.clear();delay=true;const pending=c.view.open();await flush();c.view.clear();release(Response.json({items:bank.items}));await pending;assert.equal(c.root.textContent,'');assert(c.root.hidden);c.w.close();
});

test('hide-finished keeps fixed batches and includes hidden words in the AI prompt',async()=>{
 const b=await browser();b.root.querySelector('[data-number="1"][data-field="finished"]').click();await flush();
 const box=[...b.root.querySelectorAll('label')].find(n=>n.textContent==='Hide finished words').querySelector('input');box.click();await flush();assert.equal(b.root.querySelectorAll('.vocabulary-item').length,9);
 clickText(b,'Copy AI prompt');await flush();assert.equal((b.copied.match(/"word":/g)||[]).length,10);assert.match(b.copied,/recruit/);
 b.view.clear();await b.view.open();assert.equal(b.root.querySelectorAll('.vocabulary-item').length,9);
 b.view.clear();b.w.close();
});
