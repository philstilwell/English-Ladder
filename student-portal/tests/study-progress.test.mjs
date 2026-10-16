import test from 'node:test';
import assert from 'node:assert/strict';
import { seedQuiz, call, login, origin } from './harness.mjs';
import { assessment } from './fixture.mjs';
import { studyTopics } from '../study-progress.mjs';
const statePath='/api/study/state', questionsPath='/api/study/questions';
const patch=(cookie,body,headers={})=>({method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...headers},body:JSON.stringify(body)});
const read=(e,cookie,path=statePath)=>call(e,path,{headers:{Cookie:cookie}});
const topic=async(e,cookie)=>(await(await read(e,cookie)).json()).topics[0];

test('study choices are private, student-only, exact-origin and validated against authored topics',async()=>{
 const {e,student,teacher}=await seedQuiz(),otherHost='https://cd26.englishladder.com';
 const other=await login(e,'other-test',otherHost),item=await topic(e,student.cookie);
 const input={id:item.id,field:'finished',value:true,revision:0};
 for(const path of [statePath,questionsPath]){
  assert.equal((await call(e,path)).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:student.cookie}},otherHost)).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:student.cookie,Origin:otherHost}})).status,403);
  assert.equal((await call(e,path,{headers:{Cookie:student.cookie,'Sec-Fetch-Site':'cross-site'}})).status,403);
  const response=await read(e,teacher.cookie,path);assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'no-store');
 }
 assert.equal((await call(e,statePath,patch(teacher.cookie,input))).status,403);
 assert.equal((await call(e,statePath,patch(student.cookie,input,{Origin:otherHost}))).status,403);
 for(const change of [{field:'score'},{value:1},{revision:-1},{revision:1.1},{id:'bad'},{studentId:'cd26'},{topic:assessment.plan[0]}]) assert.equal((await call(e,statePath,patch(student.cookie,{...input,...change}))).status,400);
 assert.equal((await call(e,statePath,patch(student.cookie,{...input,id:'0'.repeat(64)}))).status,409);
 assert.equal((await call(e,questionsPath,patch(student.cookie,input))).status,405);
 assert.equal((await call(e,statePath,{...patch(student.cookie,input),method:'DELETE'})).status,405);
 e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await call(e,statePath,patch(student.cookie,input))).status,429);delete e.PRACTICE_LIMITER;
 assert.equal((await call(e,statePath,patch(student.cookie,input))).status,200);
 assert.deepEqual(await(await call(e,statePath,{headers:{Cookie:other.cookie}},otherHost)).json(),{topics:[]});
 assert.doesNotMatch(JSON.stringify(await(await read(e,student.cookie)).json()),/observed|sourceSessions|noteId|password|nextLesson|Alex Brown/);
});

test('study choices save independently, retry safely and reject conflicting changes',async()=>{
 const {e,student,teacher}=await seedQuiz(),item=await topic(e,student.cookie);
 const save=body=>call(e,statePath,patch(student.cookie,{id:item.id,...body}));
 const first=await(await save({field:'finished',value:true,revision:0})).json();
 assert.equal(first.entry.revision,1);assert.ok(Date.parse(first.entry.updatedAt));
 assert.deepEqual(await(await save({field:'finished',value:true,revision:0})).json(),first);
 assert.equal((await save({field:'question',value:true,revision:0})).status,409);
 await save({field:'question',value:true,revision:1});
 let questions=(await(await read(e,teacher.cookie,questionsPath)).json()).questions;
 assert.equal(questions.length,1);assert.equal(questions[0].progress.finished,true);assert.equal(questions[0].current,true);
 await save({field:'finished',value:false,revision:2});
 questions=(await(await read(e,student.cookie,questionsPath)).json()).questions;assert.equal(questions[0].progress.finished,false);assert.equal(questions[0].progress.question,true);
 await save({field:'question',value:false,revision:3});assert.deepEqual((await(await read(e,student.cookie,questionsPath)).json()).questions,[]);
 const reopened=await login(e);assert.equal((await topic(e,reopened.cookie)).progress.revision,4);
});

test('study questions retain exact topic snapshots across replacement, reordering and assessment revisions',async()=>{
 const {e,student,publish}=await seedQuiz(),item=await topic(e,student.cookie);
 await call(e,statePath,patch(student.cookie,{id:item.id,field:'question',value:true,revision:0}));
 const second={...assessment.plan[0],title:'Second topic'};
 await publish('/api/assessment',{...assessment,assessedOn:'2026-10-15',plan:[second,assessment.plan[0]]});
 let topics=(await(await read(e,student.cookie)).json()).topics;assert.equal(topics[1].id,item.id);assert.equal(topics[1].progress.question,true);
 await publish('/api/assessment',{...assessment,plan:[{...assessment.plan[0],target:'New practice task.'}]});
 topics=(await(await read(e,student.cookie)).json()).topics;assert.notEqual(topics[0].id,item.id);assert.equal(topics[0].progress.question,false);assert.equal(topics[0].progress.finished,false);
 const old=(await(await read(e,student.cookie,questionsPath)).json()).questions[0];assert.equal(old.current,false);assert.equal(old.target,assessment.plan[0].target);
 assert.equal((await call(e,statePath,patch(student.cookie,{id:item.id,field:'question',value:false,revision:1}))).status,200);
 assert.deepEqual((await(await read(e,student.cookie,questionsPath)).json()).questions,[]);
});

test('study Questions list pages bound reads and keep all earlier topics available',async()=>{
 const {e,student,publish}=await seedQuiz();
 for(let i=0;i<23;i++){
  await publish('/api/assessment',{...assessment,plan:[{...assessment.plan[0],title:'Topic '+i}]});
  const item=await topic(e,student.cookie);await call(e,statePath,patch(student.cookie,{id:item.id,field:'question',value:true,revision:0}));
 }
 const first=await(await read(e,student.cookie,questionsPath)).json();assert.equal(first.questions.length,20);assert.ok(first.nextCursor);
 const second=await(await read(e,student.cookie,questionsPath+'?after='+first.nextCursor)).json();assert.equal(second.questions.length,3);assert.equal(second.nextCursor,null);
 assert.equal(new Set([...first.questions,...second.questions].map(q=>q.id)).size,23);
 assert.equal((await read(e,student.cookie,questionsPath+'?after=bad')).status,400);
});

test('deleting an account removes study choices and blocks delayed writes',async()=>{
 const {e,student}=await seedQuiz(),item=await topic(e,student.cookie),store=e.FEEDBACK_STORE.get('ab26');
 await call(e,statePath,patch(student.cookie,{id:item.id,field:'question',value:true,revision:0}));
 await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
 assert.equal((await store.storage.list({prefix:'study:'})).size,0);
 assert.equal((await call(e,statePath,patch(student.cookie,{id:item.id,field:'finished',value:true,revision:1}))).status,410);
 assert.equal((await read(e,student.cookie,questionsPath)).status,410);
});

test('topic IDs ignore assessment dates and position but include the whole exercise and prompt',async()=>{
 const [original]=await studyTopics(assessment);
 for(const key of ['title','activity','target','aiPrompt']){
  const [changed]=await studyTopics({...assessment,plan:[{...assessment.plan[0],[key]:'Changed content'}]});assert.notEqual(original.id,changed.id);
 }
 assert.equal((await studyTopics({...assessment,assessedOn:'2026-10-15'}))[0].id,original.id);
});
