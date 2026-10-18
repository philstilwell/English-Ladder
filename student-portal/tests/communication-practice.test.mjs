import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';
import { env, call, login, origin } from './harness.mjs';
import { COMMUNICATION_ACTIVITIES as banks, communicationPrefix } from '../communication-practice.mjs';
const path=id=>'/api/communication/'+id;
const read=(e,cookie,id,state=true)=>call(e,path(id)+(state?'/state':''),{headers:{Cookie:cookie}});
const patch=(e,cookie,id,body)=>call(e,path(id)+'/state',{method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)});
const answer=(bank,value,revision=0,number=1)=>({number,field:'answer',value,revision,version:bank.version});
const flush=async()=>{for(let i=0;i<15;i++)await new Promise(r=>setTimeout(r,1));};

test('300 complete original items have balanced keys, distinct contexts, six sets and traceable story sequences',()=>{
 assert.equal(banks.length,5);
 for(const bank of banks){
  assert.equal(bank.items.length,60);assert.equal(bank.groups.length,6);
  const source=readFileSync(new URL('../content/'+bank.id+'.txt',import.meta.url),'utf8').trim().split('\n').map(l=>l.split('|'));
  assert.equal(source.length,60);assert.equal(new Set(bank.items.map(i=>i.context+'|'+i.prompt)).size,60);
  assert.deepEqual(bank.items.map(i=>i.number),Array.from({length:60},(_,i)=>i+1));
  assert.deepEqual([0,1,2,3].map(k=>bank.items.filter(i=>i.answer===k).length),[15,15,15,15]);
  assert.deepEqual(bank.groups.map(g=>bank.items.filter(i=>i.group===g).length),[10,10,10,10,10,10]);
  assert.deepEqual(['Start','Build','Stretch'].map(s=>bank.items.filter(i=>i.stage===s).length),[20,20,20]);
  for(const item of bank.items){
   assert.equal(item.options.length,4);assert.equal(new Set(item.options).size,4);
   for(const text of [item.context,item.prompt,item.explanation,...item.options])assert.ok(typeof text==='string'&&text.trim()===text&&text.length>8);
   assert.doesNotMatch(JSON.stringify(item),/https?:|<script|\bTODO\b|\bTBD\b|correct answer here/i);
   if(bank.id==='story-builder'){
    const lines=item.context.split('\n');assert.equal(lines.length,4);
    const order=item.options[item.answer].split(' → ').map(letter=>lines[letter.charCodeAt(0)-65].slice(3));
    assert.deepEqual(order,source[item.number-1][2].split('~'));
    for(const choice of item.options)assert.deepEqual(choice.split(' → ').sort(),['A','B','C','D']);
   }else assert.equal(item.options[item.answer],source[item.number-1][3]);
   if(bank.id==='missing-details')assert.ok(item.reply?.length>20);
  }
 }
});

test('all five activities save original and latest answers independently, with idempotent retries and server scoring',async()=>{
 const e=env(),student=await login(e);
 for(const bank of banks){
  assert.equal((await call(e,path(bank.id))).status,401);
  const data=await(await read(e,student.cookie,bank.id,false)).json();assert.equal(data.items.length,60);
  assert.equal((await call(e,'/communication-bank.json',{headers:{Cookie:student.cookie}})).status,404);
  const wrong=(bank.items[0].answer+1)%4;
  let r=await patch(e,student.cookie,bank.id,answer(bank,wrong));assert.equal(r.status,200);let entry=(await r.json()).entry;
  assert.deepEqual([entry.firstChoice,entry.firstCorrect,entry.choice,entry.correct,entry.revision],[wrong,false,wrong,false,1]);
  r=await patch(e,student.cookie,bank.id,answer(bank,wrong));assert.equal(r.status,200);assert.equal((await r.json()).entry.revision,1);
  assert.equal((await patch(e,student.cookie,bank.id,answer(bank,bank.items[0].answer,0))).status,409);
  r=await patch(e,student.cookie,bank.id,answer(bank,bank.items[0].answer,1));entry=(await r.json()).entry;
  assert.deepEqual([entry.firstChoice,entry.firstCorrect,entry.choice,entry.correct,entry.revision],[wrong,false,bank.items[0].answer,true,2]);
  assert.equal(entry.finished,false);assert.equal(entry.question,false);
  r=await patch(e,student.cookie,bank.id,{number:1,field:'question',value:true,revision:2});assert.equal(r.status,200);
  r=await patch(e,student.cookie,bank.id,{number:1,field:'finished',value:true,revision:3});assert.equal(r.status,200);
  const state=await(await read(e,student.cookie,bank.id)).json();assert.equal(state.entries.length,1);assert.equal(state.entries[0].firstChoice,wrong);assert.equal(state.entries[0].question,true);
 }
 const store=e.FEEDBACK_STORE.get('ab26'),overview=await(await store.fetch(new Request('https://feedback.internal/admin/activity-summary'))).json();
 assert.equal(overview.activities.length,9);
 for(const summary of overview.activities.slice(4))assert.deepEqual([summary.total,summary.answered,summary.firstCorrect,summary.finished,summary.questions],[60,1,0,1,1]);
 const questions=await(await store.fetch(new Request('https://feedback.internal/admin/questions'))).json();
 assert.equal(questions.count,5);assert.equal(questions.questions.length,5);
 for(const row of questions.questions){assert.equal(row.item.progress.firstCorrect,false);assert.equal(row.item.progress.correct,true);assert.equal(row.item.progress.finished,true);assert.equal(row.item.options.length,4);}
});

test('private state requires correct host and student identity; teacher preview and foreign origins cannot write',async()=>{
 const e=env(),student=await login(e),teacher=await login(e,'teacher-test'),other=await login(e,'other-test','https://cd26.englishladder.com');
 for(const bank of banks){
  const p=path(bank.id)+'/state',body=answer(bank,bank.items[0].answer);
  assert.equal((await call(e,p)).status,401);
  assert.equal((await patch(e,teacher.cookie,bank.id,body)).status,403);
  assert.equal((await call(e,p,{headers:{Cookie:other.cookie}})).status,401);
  for(const headers of [{Origin:'https://evil.test'}, {'Sec-Fetch-Site':'cross-site'}])assert.equal((await call(e,p,{headers:{Cookie:student.cookie,...headers}})).status,403);
  for(const Origin of ['https://evil.test','null',''])assert.equal((await call(e,p,{method:'PATCH',headers:{Cookie:student.cookie,Origin,'Content-Type':'application/json'},body:JSON.stringify(body)})).status,403);
  assert.equal((await patch(e,student.cookie,bank.id,body)).status,200);
  const otherState=await(await call(e,p,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json();assert.deepEqual(otherState.entries,[]);
  const preview=await read(e,teacher.cookie,bank.id);assert.equal(preview.status,200);assert.match(preview.headers.get('Cache-Control'),/no-store/);
 }
});

test('invalid fields, stale versions, unknown items, oversized requests and rate limits never create practice records',async()=>{
 const e=env(),student=await login(e),bank=banks[0],body=answer(bank,0),p=path(bank.id)+'/state';
 for(const input of [{...body,number:61},{...body,number:1.5},{...body,number:'1'},{...body,value:4},{...body,value:-1},{...body,value:'0'},{...body,version:2},{...body,revision:-1},{...body,correct:true},{...body,firstChoice:0},null,[],{field:'position',value:61,revision:0},{field:'hideFinished',value:'true',revision:0}])assert.equal((await patch(e,student.cookie,bank.id,input)).status,400);
 assert.equal((await call(e,p,{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:'x'.repeat(2000)})).status,400);
 assert.equal((await call(e,p,{method:'POST',headers:{Cookie:student.cookie}})).status,405);
 assert.equal((await call(e,'/api/communication/unknown',{headers:{Cookie:student.cookie}})).status,404);
 e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await patch(e,student.cookie,bank.id,body)).status,429);
 assert.deepEqual((await(await read(e,student.cookie,bank.id)).json()).entries,[]);
});

test('independent filters and bookmarks survive reloads; deletion removes every activity and prevents delayed saves',async()=>{
 const e=env(),student=await login(e);
 for(const [i,bank] of banks.entries()){
  assert.equal((await patch(e,student.cookie,bank.id,{field:'position',value:11+i,revision:0})).status,200);
  assert.equal((await patch(e,student.cookie,bank.id,{field:'hideFinished',value:i%2===0,revision:0})).status,200);
  const data=await(await read(e,student.cookie,bank.id)).json();assert.equal(data.position.number,11+i);assert.equal(data.preferences.hideFinished,i%2===0);
 }
 const store=e.FEEDBACK_STORE.get('ab26');await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
 assert.equal((await store.storage.list({prefix:'communication:'})).size,0);
 for(const bank of banks)assert.equal((await patch(e,student.cookie,bank.id,answer(bank,0))).status,410);
});

test('combined questions paginate across five new sources and never change saved work',async()=>{
 const store=env().FEEDBACK_STORE.get('ab26'),records={};
 for(const bank of banks)for(let number=1;number<=6;number++)records[communicationPrefix(bank)+':item:'+number]={number,finished:false,question:true,revision:1,firstChoice:0,choice:1,firstCorrect:false,correct:false};
 await store.storage.put(records);const before=await store.storage.list();
 const first=await(await store.fetch(new Request('https://feedback.internal/admin/questions'))).json();assert.equal(first.count,30);assert.equal(first.questions.length,20);
 const next=await(await store.fetch(new Request('https://feedback.internal/admin/questions?after='+encodeURIComponent(first.nextCursor)))).json();assert.equal(next.questions.length,10);assert.equal(next.nextCursor,null);
 assert.equal(new Set([...first.questions,...next.questions].map(q=>q.id)).size,30);assert.deepEqual(await store.storage.list(),before);
});

async function browser(custom,teacher=false,id=banks[0].id){
 const e=env(),user=await login(e,teacher?'teacher-test':'student-test');
 const dom=new JSDOM('<div id="root"></div>',{url:origin,runScripts:'outside-only',pretendToBeVisual:true}),w=dom.window,root=w.document.getElementById('root'),requests=[];w.AbortController=AbortController;let copied='';
 Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
 for(const name of ['practice-prompt','practice-position','communication-practice'])w.eval(readFileSync(new URL('../public/'+name+'.js',import.meta.url),'utf8'));
 const api=async(p,options={})=>{requests.push({path:p,...options});const response=await(custom?.(p,options)||call(e,p,{...options,headers:{Cookie:user.cookie,...(options.method?{Origin:origin}:{}),...options.headers}}));const data=await response.json();if(!response.ok)throw Object.assign(new Error(data.error),{status:response.status});return data;};
 const view=w.CommunicationPractice.create({root,api,expired:error=>{if(error.status===401){view.clear();return true;}return false;}});await view.open(id,teacher);
 return {e,w,root,view,requests,get copied(){return copied;}};
}
const click=(b,text)=>{const button=[...b.root.querySelectorAll('button')].find(n=>n.textContent===text);assert.ok(button,'Missing button '+text);button.click();};
const select=(b,selector,value)=>{const input=b.root.querySelector(selector);input.value=value;input.dispatchEvent(new b.w.Event('change',{bubbles:true}));};

test('students answer, reveal, copy, flag, finish, filter and resume each activity with separate saved places',async()=>{
 const b=await browser();
 for(const bank of banks){
  await b.view.open(bank.id);assert.equal(b.root.querySelectorAll('.communication-option').length,4);
  assert.equal(b.root.querySelectorAll('.practice-ai-link').length,4);
  const wrong=(bank.items[0].answer+1)%4;b.root.querySelectorAll('.communication-option')[wrong].click();await flush();assert.match(b.root.textContent,/Not quite/);
  b.root.querySelectorAll('.communication-option')[bank.items[0].answer].click();await flush();assert.match(b.root.textContent,/Correct/);
  click(b,'Copy AI prompt');await flush();assert.equal(b.root.querySelector('.practice-copy-button').textContent,'AI prompt copied');assert.match(b.copied,/Answer key:/);assert.doesNotMatch(b.copied,/Alex|ab26|firstChoice|studentAnswer|password|https?:/i);
  click(b,'Questions');await flush();click(b,'Finish');await flush();assert.match(b.root.textContent,/Saved to Questions/);assert.ok(b.root.querySelector('.is-finished'));
  b.root.querySelector('.practice-filter input').click();await flush();assert.match(b.root.querySelector('h3').textContent,/Item 2/);
  select(b,'#communication-group',bank.groups[2]);await flush();assert.match(b.root.querySelector('h3').textContent,/Item 21/);
  b.view.clear();await b.view.open(bank.id);assert.match(b.root.querySelector('h3').textContent,/Item 21/);assert.equal(b.root.querySelector('.practice-filter input').checked,true);
  assert.equal(b.root.firstElementChild.textContent,'Last saved place: Item 21');
  b.root.querySelector('.grammar-question-links button').click();await flush();assert.match(b.root.querySelector('h3').textContent,/Item 1\b/);assert.equal(b.root.querySelector('.practice-filter input').checked,false);assert.equal(b.root.querySelectorAll('.communication-option')[bank.items[0].answer].getAttribute('aria-pressed'),'true');
  assert.equal((await b.e.FEEDBACK_STORE.get('ab26').storage.get(communicationPrefix(bank)+':preferences')).hideFinished,true);
 }
 b.view.clear();assert.equal(b.root.textContent,'');assert.equal(b.root.hidden,true);assert.equal(b.w.localStorage.length,0);assert.equal(b.w.sessionStorage.length,0);b.w.close();
});

test('failed saves preserve work and allow retry; conflicts reload choices and require another click',async()=>{
 let fail=true;const b=await browser((p,o)=>fail&&o.method==='PATCH'?Response.json({error:'Offline'},{status:503}):null);
 click(b,'Questions');await flush();assert.match(b.root.textContent,/could not be saved/);assert.ok([...b.root.querySelectorAll('button')].some(n=>n.textContent==='Questions'&&!n.disabled));
 fail=false;click(b,'Questions');await flush();assert.match(b.root.textContent,/Saved to Questions/);
 const bank=banks[0],key=communicationPrefix(bank)+':item:1',store=b.e.FEEDBACK_STORE.get('ab26'),entry=await store.storage.get(key);await store.storage.put({[key]:{...entry,choice:0,firstChoice:0,revision:entry.revision+1}});
 click(b,'Finish');await flush();assert.match(b.root.textContent,/changed on another page/);assert.equal((await store.storage.get(key)).finished,false);
 click(b,'Finish');await flush();assert.equal((await store.storage.get(key)).finished,true);b.view.clear();b.w.close();
});

test('teacher preview can explore without saving and admin review preserves first and latest choices',async()=>{
 const b=await browser(null,true);
 b.root.querySelector('.communication-option').click();click(b,'Next item');b.root.querySelector('.practice-filter input').click();await flush();
 assert.equal(b.requests.filter(r=>r.method).length,0);assert.ok([...b.root.querySelectorAll('button')].find(n=>n.textContent==='Finish').disabled);
 const item=structuredClone(banks[0].items[0]);item.context='<img src=x onerror=alert(1)>';item.progress={firstChoice:0,firstCorrect:false,choice:2,finished:true};
 const card=b.w.CommunicationPractice.review(item);b.root.replaceChildren(card);assert.match(card.textContent,/First saved choice/);assert.match(card.textContent,/Latest saved choice/);assert.equal(card.querySelector('img:not(.practice-ai-link img),script,[onerror]'),null);
 card.querySelectorAll('.communication-option')[1].click();assert.equal(b.requests.filter(r=>r.method).length,0);b.view.clear();b.w.close();
});

test('late loads and saves cannot restore a cleared view; reopen waits for a pending saved place',async()=>{
 let release,delay=false;const b=await browser((p,o)=>delay&&!o.method&&p===path(banks[0].id)?new Promise(r=>{release=r;}):null);
 b.view.clear();delay=true;const open=b.view.open(banks[0].id);await flush();b.view.clear();release(Response.json(banks[0]));await open;assert.equal(b.root.textContent,'');b.w.close();
 let finish;const c=await browser((p,o)=>o.method==='PATCH'&&JSON.parse(o.body).field==='position'?new Promise(r=>{finish=r;}):null);
 click(c,'Next item');await flush();c.view.clear();const reopen=c.view.open(banks[0].id);await flush();assert.match(c.root.textContent,/Loading/);
 await c.e.FEEDBACK_STORE.get('ab26').storage.put({[communicationPrefix(banks[0])+':position']:{number:2,revision:1}});finish(Response.json({position:{number:2,revision:1}}));await reopen;assert.match(c.root.querySelector('h3').textContent,/Item 2/);c.view.clear();c.w.close();
 let resolve;const d=await browser((p,o)=>o.method==='PATCH'?new Promise(r=>{resolve=r;}):null);click(d,'Finish');await flush();d.view.clear();resolve(Response.json({entry:{number:1,finished:true,question:false,revision:1}}));await flush();assert.equal(d.root.textContent,'');d.w.close();
});

test('expired saves clear content and an all-finished filter retains a way back',async()=>{
 const b=await browser((p,o)=>o.method==='PATCH'?Response.json({error:'Expired'},{status:401}):null);click(b,'Questions');await flush();assert.equal(b.root.textContent,'');assert.equal(b.root.hidden,true);b.w.close();
 const bank=banks[0],c=await browser((p,o)=>p===path(bank.id)+'/state'&&!o.method?Response.json({entries:bank.items.map(i=>({number:i.number,finished:true,question:false,revision:1})),preferences:{hideFinished:true,revision:1},position:{number:60,revision:1}}):null);
 assert.match(c.root.textContent,/All items are finished/);assert.equal(c.root.querySelector('.practice-filter input').checked,true);assert.equal(c.root.firstElementChild.textContent,'Last saved place: Item 60');c.view.clear();c.w.close();
});
