import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {JSDOM} from 'jsdom';
import {feedback} from './fixture.mjs';
const html=readFileSync(new URL('../public/index.html',import.meta.url),'utf8');
const script=readFileSync(new URL('../public/portal.js',import.meta.url),'utf8');
const second={...feedback,id:'2026-09-01-2057',startedAt:'2026-09-02T00:57:01Z',title:'Earlier English lesson'};
const profile={student:{id:'ab26',name:'Alex',nickname:'Alex the Explorer'},role:'student'};
const reply=data=>new Response(JSON.stringify(data));
const flush=async()=>{for(let i=0;i<8;i++)await new Promise(resolve=>setImmediate(resolve));};
function setup(custom,url='https://ab26.englishladder.com/'){
 const dom=new JSDOM(html,{url,runScripts:'outside-only'});
 const w=dom.window;w.setInterval=()=>0;
 w.fetch=async(path,options)=>{
  const customResult=custom?.(path,options);if(customResult)return customResult;
  if(path==='/api/context')return reply({id:'ab26'});
  if(path==='/api/session'||path==='/api/login')return reply(profile);
  if(path==='/api/logout')return reply({ok:true});
  if(path==='/api/feedback')return reply({sessions:[feedback,second],nextCursor:null});
  return reply(path.endsWith(second.id)?second:feedback);
 };
 w.eval(script);return dom;
}
test('deep links open the selected page and show only student-safe content',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#feedback/'+second.id);await flush();
 const d=dom.window.document;
 assert.equal(d.getElementById('feedback-title').textContent,second.title);
 assert.match(d.getElementById('profile-nickname').textContent,/Alex the Explorer/);
 assert.equal(d.querySelectorAll('#session-list a').length,2);
 assert.match(d.getElementById('feedback-page').textContent,/Japan:/);
 assert.equal(d.querySelectorAll('.practice-item details').length,1);
 dom.window.close();
});
test('late page responses cannot overwrite a newer selection',async()=>{
 let resolveFirst;
 const dom=setup(path=>path.endsWith('/'+feedback.id)?new Promise(resolve=>{resolveFirst=resolve;}):null);
 await flush();
 dom.window.location.hash='feedback/'+second.id;await new Promise(r=>setTimeout(r,10));await flush();
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,second.title);
 resolveFirst(reply(feedback));await flush();
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,second.title);
 dom.window.close();
});
test('sign-out clears profile, records, summaries, and late responses',async()=>{
 let resolveFirst;
 const dom=setup(path=>path.endsWith('/'+feedback.id)?new Promise(resolve=>{resolveFirst=resolve;}):null);await flush();
 dom.window.document.getElementById('logout').click();await flush();
 resolveFirst(reply(feedback));await flush();
 const d=dom.window.document;
 assert.equal(d.getElementById('login-view').hidden,false);
 for(const id of ['feedback-page','session-list','session-select','session-summaries','profile-nickname'])assert.equal(d.getElementById(id).textContent,'');
 assert.doesNotMatch(d.getElementById('dashboard-view').textContent,/Alex|Clear explanations|Earlier English lesson/);
 dom.window.close();
});
test('expired feedback sessions return to sign-in and clear private content',async()=>{
 const dom=setup(path=>path.startsWith('/api/feedback/')?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null);
 await flush();
 assert.equal(dom.window.document.getElementById('login-view').hidden,false);
 assert.equal(dom.window.document.getElementById('session-list').textContent,'');
 dom.window.close();
});
test('feedback strings render as text, never executable markup',async()=>{
 const data={...feedback,title:'<img src=x onerror=alert(1)>'};
 const dom=setup(path=>path.endsWith('/'+feedback.id)?reply(data):null);await flush();
 assert.equal(dom.window.document.querySelector('#feedback-page img'),null);
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,data.title);
 dom.window.close();
});
