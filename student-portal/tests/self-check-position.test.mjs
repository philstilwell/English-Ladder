import test from 'node:test';
import assert from 'node:assert/strict';
import { env, call, login, origin } from './harness.mjs';
const patch=(cookie,body,extra={})=>({method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...extra},body:JSON.stringify(body)});
const defaults={number:null,revision:0,updatedAt:null};
for(const [activity,prefix,invalidNumber] of [['grammar-practice','grammar',901],['business-terms','terms',18]]) {
 const path='/api/'+activity+'/state';
 test(activity+' saves a private place across sessions independently of filters, item choices and other accounts',async()=>{
  const e=env(),student=await login(e),other=await login(e,'other-test','https://cd26.englishladder.com');
  const read=async cookie=>(await(await call(e,path,{headers:{Cookie:cookie}})).json());
  assert.deepEqual((await read(student.cookie)).position,defaults);
  const body={field:'position',value:21,revision:0};
  const response=await call(e,path,patch(student.cookie,body));assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'no-store');
  const {position}=await response.json();assert.equal(position.number,21);assert.equal(position.revision,1);assert(!Number.isNaN(Date.parse(position.updatedAt)));
  assert.deepEqual((await(await call(e,path,patch(student.cookie,body))).json()).position,position);
  const secondLogin=await login(e);assert.deepEqual((await read(secondLogin.cookie)).position,position);
  assert.deepEqual((await read(student.cookie)).entries,[]);assert.equal((await read(student.cookie)).preferences.hideFinished,false);
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json()).position,defaults);
  const otherActivity=activity==='grammar-practice'?'business-terms':'grammar-practice';
  assert.deepEqual((await(await call(e,'/api/'+otherActivity+'/state',{headers:{Cookie:student.cookie}})).json()).position,defaults);
  assert.equal((await call(e,path,patch(student.cookie,{number:1,field:'question',value:true,revision:0}))).status,200);
  assert.equal((await call(e,path,patch(student.cookie,{field:'hideFinished',value:true,revision:0}))).status,200);
  assert.equal((await read(student.cookie)).position.revision,1);
  const conflicting=await Promise.all([31,41].map(value=>call(e,path,patch(student.cookie,{...body,value,revision:1}))));
  assert.deepEqual(conflicting.map(r=>r.status).sort(),[200,409]);assert.equal((await read(student.cookie)).position.revision,2);
  const store=e.FEEDBACK_STORE.get('ab26');assert.equal((await(await store.fetch(new Request('https://feedback.internal/'+prefix+'/questions'))).json()).questions.length,1);
  await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));assert.equal((await store.storage.list({prefix:prefix+':'})).size,0);
  assert.equal((await call(e,path,patch(student.cookie,body))).status,410);
 });
 test(activity+' position writes require the student, the correct origin, valid items, and the existing rate limit',async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');const body={field:'position',value:21,revision:0};
  assert.equal((await call(e,path,patch('',body))).status,401);assert.equal((await call(e,path,patch(teacher.cookie,body))).status,403);
  assert.equal((await call(e,path,patch(student.cookie,body,{Origin:'https://evil.test'}))).status,403);
  assert.equal((await call(e,path,patch(student.cookie,body),'https://cd26.englishladder.com')).status,401);
  for(const invalid of [{...body,value:'21'},{...body,value:null},{...body,value:invalidNumber},{...body,value:0},{...body,value:1.5},{...body,revision:-1},{...body,number:1},{...body,studentId:'cd26'}])assert.equal((await call(e,path,patch(student.cookie,invalid))).status,400);
  e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await call(e,path,patch(student.cookie,body))).status,429);
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:teacher.cookie}})).json()).position,defaults);
 });
}
