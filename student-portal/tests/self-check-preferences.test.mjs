import test from 'node:test';
import assert from 'node:assert/strict';
import { env, call, login, origin } from './harness.mjs';
const patch=(cookie,body,extra={})=>({method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...extra},body:JSON.stringify(body)});
const defaults={hideFinished:false,revision:0,updatedAt:null};
for(const [activity,prefix] of [['grammar-practice','grammar'],['business-terms','terms']]) {
 const path='/api/'+activity+'/state';
 test(activity+' preferences persist per student and activity, with safe retries and separate item revisions',async()=>{
  const e=env(),student=await login(e),other=await login(e,'other-test','https://cd26.englishladder.com');
  const read=async cookie=>(await(await call(e,path,{headers:{Cookie:cookie}})).json());
  assert.deepEqual((await read(student.cookie)).preferences,defaults);
  const body={field:'hideFinished',value:true,revision:0};
  const response=await call(e,path,patch(student.cookie,body));assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'no-store');
  const {preferences}=await response.json();assert.equal(preferences.hideFinished,true);assert.equal(preferences.revision,1);assert(!Number.isNaN(Date.parse(preferences.updatedAt)));
  assert.deepEqual((await(await call(e,path,patch(student.cookie,body))).json()).preferences,preferences);
  const secondLogin=await login(e);assert.deepEqual((await read(secondLogin.cookie)).preferences,preferences);
  assert.deepEqual((await read(student.cookie)).entries,[]);
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json()).preferences,defaults);
  const otherActivity=activity==='grammar-practice'?'business-terms':'grammar-practice';
  assert.deepEqual((await(await call(e,'/api/'+otherActivity+'/state',{headers:{Cookie:student.cookie}})).json()).preferences,defaults);
  assert.equal((await call(e,path,patch(student.cookie,{number:1,field:'finished',value:true,revision:0}))).status,200);
  assert.equal((await call(e,path,patch(student.cookie,{...body,value:false}))).status,409);
  const changed=await call(e,path,patch(student.cookie,{...body,value:false,revision:1}));assert.equal(changed.status,200);
  assert.equal((await read(student.cookie)).preferences.hideFinished,false);assert.equal((await read(student.cookie)).entries[0].revision,1);
  const store=e.FEEDBACK_STORE.get('ab26');await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await store.storage.list({prefix:prefix+':'})).size,0);
  assert.equal((await call(e,path,patch(student.cookie,body))).status,410);
 });
 test(activity+' preferences reject unauthenticated, teacher, cross-account, malformed and rate-limited writes',async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');const body={field:'hideFinished',value:true,revision:0};
  assert.equal((await call(e,path,patch('',body))).status,401);
  assert.equal((await call(e,path,patch(teacher.cookie,body))).status,403);
  assert.equal((await call(e,path,patch(student.cookie,body,{Origin:'https://evil.test'}))).status,403);
  assert.equal((await call(e,path,patch(student.cookie,body),'https://cd26.englishladder.com')).status,401);
  for(const invalid of [{...body,value:'true'},{...body,revision:-1},{...body,revision:0.5},{...body,number:1},{...body,studentId:'cd26'},{...body,field:'other'}])assert.equal((await call(e,path,patch(student.cookie,invalid))).status,400);
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:teacher.cookie}})).json()).preferences,defaults);
  e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await call(e,path,patch(student.cookie,body))).status,429);
  assert.deepEqual((await(await call(e,path,{headers:{Cookie:student.cookie}})).json()).preferences,defaults);
 });
}
