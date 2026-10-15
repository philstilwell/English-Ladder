import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';
const script=readFileSync(new URL('../public/practice-position.js',import.meta.url),'utf8');
const tick=()=>new Promise(resolve=>setTimeout(resolve,0));
function create(api,expired=()=>false) {
 const dom=new JSDOM('',{runScripts:'outside-only'});dom.window.eval(script);
 const bookmark=dom.window.PracticePosition.create({api,expired,path:'/api/grammar-practice/state'});
 dom.window.document.body.append(bookmark.notice);bookmark.read(undefined,true);
 return {dom,bookmark};
}
test('rapid moves save the latest requested place in order and finish after leaving without restoring the view',async()=>{
 const calls=[],resolvers=[];
 const {dom,bookmark}=create((path,options)=>{calls.push(options);return new Promise(resolve=>resolvers.push(resolve));});
 bookmark.remember(11);bookmark.remember(21);bookmark.remember(31);
 assert.equal(calls.length,1);assert.equal(JSON.parse(calls[0].body).value,11);assert.equal(calls[0].keepalive,true);assert(calls[0].signal);
 bookmark.clear();assert(bookmark.notice.hidden);
 resolvers.shift()({position:{number:11,revision:1}});await tick();
 assert.equal(calls.length,2);assert.deepEqual(JSON.parse(calls[1].body),{field:'position',value:31,revision:1});assert(bookmark.notice.hidden);
 let settled=false;bookmark.settled().then(()=>{settled=true;});await tick();assert(!settled);
 resolvers.shift()({position:{number:31,revision:2}});await bookmark.settled();assert(settled);assert(bookmark.notice.hidden);
 bookmark.read({number:31,revision:2},true);bookmark.remember(31);await bookmark.settled();assert.equal(calls.length,2);dom.window.close();
});
test('failed saves offer a safe retry and conflicts require a new user action before replacing a newer place',async()=>{
 const calls=[];let fail=true,conflict=false;
 const {dom,bookmark}=create(async(path,options)=>{
  if(!options.method)return {position:{number:61,revision:4}};
  const body=JSON.parse(options.body);calls.push(body);
  if(fail){fail=false;throw Error('Response lost');}
  if(conflict){conflict=false;throw Object.assign(Error('Changed'),{status:409});}
  return {position:{number:body.value,revision:body.revision+1}};
 });
 bookmark.remember(11);await bookmark.settled();assert.match(bookmark.notice.textContent,/could not be saved/);
 bookmark.notice.querySelector('button').click();await bookmark.settled();assert.deepEqual(calls[0],calls[1]);assert(bookmark.notice.hidden);
 conflict=true;bookmark.remember(21);await bookmark.settled();assert.equal(calls.length,3);assert.match(bookmark.notice.textContent,/changed on another page/);
 assert.equal(bookmark.notice.querySelector('button').textContent,'Save this place');
 bookmark.notice.querySelector('button').click();await bookmark.settled();assert.deepEqual(calls[3],{field:'position',value:21,revision:4});assert(bookmark.notice.hidden);dom.window.close();
});
test('teacher navigation does not save and late errors do not affect a cleared activity',async()=>{
 let reject,expired=0,writes=0;
 const {dom,bookmark}=create(()=>{writes++;return new Promise((resolve,no)=>{reject=no;});},()=>{expired++;return true;});
 bookmark.read({number:11,revision:2},false);bookmark.remember(21);await bookmark.settled();assert.equal(writes,0);
 bookmark.read({number:11,revision:2},true);bookmark.remember(21);bookmark.clear();reject(Object.assign(Error('Expired'),{status:401}));await bookmark.settled();
 assert.equal(expired,0);assert(bookmark.notice.hidden);assert.equal(bookmark.notice.querySelector('span').textContent,'');dom.window.close();
});
