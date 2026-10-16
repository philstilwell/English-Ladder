import test from 'node:test';
import assert from 'node:assert/strict';
import {env, call, login, origin} from './harness.mjs';
import {studyTopics} from '../study-progress.mjs';
import {COMMUNICATION_ACTIVITIES, communicationPrefix} from '../communication-practice.mjs';
import {assessment} from './fixture.mjs';

const path='/api/activities/questions';
const get=(e,cookie,suffix='',host=origin)=>call(e,path+suffix,{headers:{Cookie:cookie}},host);
test('All Questions combines every source, preserves old snapshots and pages read-only across twenty items',async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test'),store=e.FEEDBACK_STORE.get('ab26');
  const [topic]=await studyTopics(assessment),records={};
  for(let number=1;number<=23;number++)records['grammar:item:'+number]={number,finished:true,question:true,revision:1};
  records['terms:item:1']={number:1,question:true,finished:false,revision:1};
  records['vocabulary:item:1']={number:1,question:true,finished:false,revision:1,answer:'recruiter',sentence:'Our fictional café will recruit two people.'};
  records['study:question:'+topic.id]={id:topic.id,topic,question:true,finished:false,revision:1};
  for(const activity of COMMUNICATION_ACTIVITIES)records[communicationPrefix(activity)+':item:1']={number:1,question:true,finished:false,revision:1,choice:0,firstChoice:0,firstCorrect:activity.items[0].answer===0};
  records['assessment:current']={...assessment,plan:[]};
  // Administrator-only records must never leak through the student's list.
  records['cefr:current']={secret:'private teacher assessment'}; records['transcript:cache']={secret:'private transcript'};
  await store.storage.put(records);
  const attemptId=crypto.randomUUID(),write=(route,method,body)=>call(e,route,{method,headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)});
  assert.equal((await write('/api/road/start','POST',{attemptId,previousAttemptId:null,band:'A1',topic:'Articles'})).status,201);
  assert.equal((await write('/api/road/questions','PATCH',{attemptId,questionIndex:0,value:true,revision:0})).status,200);
  const before=await store.storage.list();
  for(const user of [student,teacher]){
    const response=await get(e,user.cookie);assert.equal(response.status,200);assert.equal(response.headers.get('Cache-Control'),'no-store');
    const first=await response.json(),second=await(await get(e,user.cookie,'?after='+encodeURIComponent(first.nextCursor))).json();
    assert.equal(first.count,32);assert.equal(first.questions.length,20);assert.equal(second.questions.length,12);assert.equal(second.nextCursor,null);
    assert.equal(first.activityCounts.length,10);assert.equal(first.activityCounts.reduce((sum,activity)=>sum+activity.count,0),32);
    assert.deepEqual(first.activityCounts.find(activity=>activity.id==='grammar-practice'),{id:'grammar-practice',label:'Grammar practice',count:23});
    assert.deepEqual(second.activityCounts,first.activityCounts);
    const all=[...first.questions,...second.questions];assert.equal(new Set(all.map(row=>row.id)).size,32);
    assert.equal(new Set(all.map(row=>row.source)).size,10);
    assert.equal(all.find(row=>row.source==='study-practice').item.current,false);
    assert.equal(all.find(row=>row.source==='vocabulary-practice').item.studentAnswer,'recruiter');
    const road=all.find(row=>row.source==='english-road').item;
    assert.equal(road.exercise.correctIndex,undefined);assert.equal(road.exercise.explanation,undefined);assert.equal(road.exercise.feedback,undefined);
    assert.doesNotMatch(JSON.stringify(all),/private teacher assessment|private transcript|password|Alex Brown/);
  }
  assert.deepEqual(await store.storage.list(),before);
  const other=await login(e,'other-test','https://cd26.englishladder.com');
  const empty=await(await get(e,other.cookie,'','https://cd26.englishladder.com')).json();assert.equal(empty.count,0);assert.deepEqual(empty.questions,[]);
  assert.deepEqual(empty.activityCounts,[]);
  const resolved=await store.fetch(new Request('https://feedback.internal/admin/questions/resolve',{method:'POST',body:JSON.stringify({id:'grammar-practice:00000001',revision:1})}));
  assert.equal(resolved.status,200);
  const refreshed=await(await get(e,student.cookie)).json();assert.equal(refreshed.count,31);assert.equal(refreshed.counts['grammar-practice'],22);
  assert.equal(refreshed.activityCounts.find(activity=>activity.id==='grammar-practice').count,22);
  assert(!refreshed.questions.some(row=>row.id==='grammar-practice:00000001'));
  assert.equal((await store.storage.get('grammar:item:1')).finished,true);
});

test('All Questions rejects unauthenticated, cross-account, cross-origin, invalid-page and write requests',async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');
  assert.equal((await call(e,path)).status,401);
  assert.equal((await get(e,student.cookie,'','https://cd26.englishladder.com')).status,401);
  assert.equal((await get(e,student.cookie,'','https://phil.englishladder.com')).status,401);
  for(const headers of [{Origin:'https://other.test'},{'Sec-Fetch-Site':'cross-site'}])assert.equal((await call(e,path,{headers:{Cookie:student.cookie,...headers}})).status,403);
  for(const user of [student,teacher])for(const method of ['POST','PATCH','PUT','DELETE'])assert.equal((await call(e,path,{method,headers:{Cookie:user.cookie,Origin:origin}})).status,405);
  assert.equal((await get(e,student.cookie,'?after=bad')).status,400);
  const store=e.FEEDBACK_STORE.get('ab26');await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await get(e,student.cookie)).status,410);
  const unavailable=env(),loginResult=await login(unavailable);delete unavailable.FEEDBACK_STORE;
  assert.equal((await get(unavailable,loginResult.cookie)).status,503);
});
