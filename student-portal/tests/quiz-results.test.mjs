import test from 'node:test';
import assert from 'node:assert/strict';
import {env,call,login,origin,seedQuiz} from './harness.mjs';
import {assessment,quiz} from './fixture.mjs';
const headers=cookie=>({Cookie:cookie,Origin:origin,'Content-Type':'application/json'});
const get=(e,cookie,path='/api/quiz/state')=>call(e,path,{headers:{Cookie:cookie}});
const answer=(e,cookie,input,extra={})=>call(e,'/api/quiz/answer',{method:'POST',headers:headers(cookie),body:JSON.stringify(input),...extra});
const input=(state,id=crypto.randomUUID(),questionIndex=0,choiceIndex=1)=>({attemptId:id,version:state.version,questionIndex,choiceIndex});

test('quiz results require the right account and role; writes reject cross-origin and malformed requests',async()=>{
 const {e,student,teacher,state}=await seedQuiz(),data=input(state);
 for(const path of ['/api/quiz/state','/api/quiz/results','/api/quiz/results/'+data.attemptId,'/api/quiz/answer']) assert.equal((await call(e,path)).status,401);
 assert.equal((await get(e,student.cookie,'/api/quiz/results')).status,403);
 assert.equal((await answer(e,teacher.cookie,data)).status,403);
 assert.equal((await get(e,teacher.cookie)).status,403);
 assert.equal((await answer(e,student.cookie,data,{headers:{...headers(student.cookie),Origin:'https://evil.test'}})).status,403);
 for(const invalid of [{...data,attemptId:'bad'},{...data,version:'old'},{...data,choiceIndex:9},{...data,questionIndex:-1},{...data,choiceIndex:0.5},null]) assert.notEqual((await answer(e,student.cookie,invalid)).status,200);
 assert.equal((await answer(e,student.cookie,data,{body:'x'.repeat(1025)})).status,400);
 assert.equal((await call(e,'/api/quiz/results',{method:'DELETE',headers:headers(teacher.cookie)})).status,405);
 assert.equal((await answer(e,student.cookie,data)).status,200);
 const otherHost='https://cd26.englishladder.com',other=await login(e,'teacher-test',otherHost);
 assert.equal((await call(e,'/api/quiz/results',{headers:{Cookie:teacher.cookie}},otherHost)).status,401);
 assert.deepEqual((await (await call(e,'/api/quiz/results?student=ab26',{headers:{Cookie:other.cookie}},otherHost)).json()).attempts,[]);
 assert.equal((await call(e,'/api/quiz/results/'+data.attemptId,{headers:{Cookie:other.cookie}},otherHost)).status,404);
 assert.equal((await get(e,teacher.cookie,'/api/quiz/results')).headers.get('Cache-Control'),'no-store');
 delete e.FEEDBACK_STORE;
 assert.equal((await get(e,teacher.cookie,'/api/quiz/results')).status,503);
});

test('first answers persist across requests and logins; scores and dates are computed on the server',async()=>{
 const {e,student,teacher,state}=await seedQuiz(),data=input(state);
 let response=await answer(e,student.cookie,{...data,firstTryCorrect:99,startedAt:'2000-01-01',studentId:'cd26',transcript:'private'});
 let record=(await response.json()).attempt;
 assert.deepEqual(record.answers,[[1],[]]);assert.equal(record.completedAt,null);
 assert.ok(Date.parse(record.startedAt)>Date.parse('2000-01-01'));assert.equal(record.transcript,undefined);assert.equal(record.firstTryCorrect,undefined);
 const again=await login(e);assert.deepEqual((await (await get(e,again.cookie)).json()).attempt,record);
 const duplicate=(await (await answer(e,student.cookie,data)).json()).attempt;
 assert.deepEqual(duplicate,record);
 assert.equal((await answer(e,student.cookie,{...data,questionIndex:1})).status,409);
 await answer(e,student.cookie,{...data,choiceIndex:0});
 response=await answer(e,student.cookie,{...data,questionIndex:1,choiceIndex:1});record=(await response.json()).attempt;
 assert.ok(record.completedAt);assert.deepEqual(record.answers,[[1,0],[1]]);
 assert.equal((await answer(e,student.cookie,{...data,questionIndex:1,choiceIndex:0})).status,409);
 const history=await (await get(e,teacher.cookie,'/api/quiz/results')).json();
 assert.equal(history.attempts.length,1);assert.equal(history.attempts[0].firstTryCorrect,1);assert.deepEqual(history.attempts[0].missedQuestions,[1]);
 assert.equal(history.attempts[0].total,2);assert.equal(history.attempts[0].answered,2);
 assert.deepEqual((await (await get(e,teacher.cookie,'/api/quiz/results/'+data.attemptId)).json()).attempt,record);
 assert.equal((await (await get(e,student.cookie,'/api/quiz/state?new=1')).json()).attempt,null);
 const next=input(state,crypto.randomUUID(),0,0);await answer(e,student.cookie,next);
 assert.equal((await (await get(e,teacher.cookie,'/api/quiz/results')).json()).attempts.length,2);
});

test('concurrent answers and competing tabs preserve exactly one active attempt',async()=>{
 const {e,student,state}=await seedQuiz(),data=input(state);
 const starts=await Promise.all([answer(e,student.cookie,data),answer(e,student.cookie,input(state))]);
 assert.deepEqual(starts.map(r=>r.status).sort(),[200,409]);
 const responses=await Promise.all([answer(e,student.cookie,{...data,choiceIndex:0}),answer(e,student.cookie,{...data,choiceIndex:0})]);
 assert.ok(responses.every(r=>r.status===200));
 const record=(await (await get(e,student.cookie)).json()).attempt;
 assert.deepEqual(record.answers,[[1,0],[]]);
 // Starting again, including with ?new=1, cannot discard an unfinished attempt.
 assert.equal((await (await get(e,student.cookie,'/api/quiz/state?new=1')).json()).attempt.id,data.attemptId);
});

test('quiz updates preserve historical wording and allow unfinished attempts to finish the original set',async()=>{
 const {e,student,teacher,state,publish}=await seedQuiz(),data=input(state);
 await answer(e,student.cookie,data);
 const changed=structuredClone(quiz);changed.questions[0].prompt='A revised question.';
 await publish('/api/assessment',{...assessment,quiz:changed});
 let saved=await (await get(e,student.cookie)).json();assert.equal(saved.quiz.questions[0].prompt,quiz.questions[0].prompt);
 await answer(e,student.cookie,{...data,choiceIndex:0});await answer(e,student.cookie,{...data,questionIndex:1,choiceIndex:1});
 saved=await (await get(e,student.cookie,'/api/quiz/state?new=1')).json();
 assert.notEqual(saved.version,state.version);assert.equal(saved.quiz.questions[0].prompt,changed.questions[0].prompt);
 assert.equal((await answer(e,student.cookie,input(state))).status,409);
 const historical=(await (await get(e,teacher.cookie,'/api/quiz/results/'+data.attemptId)).json()).attempt;
 assert.equal(historical.quiz.questions[0].prompt,quiz.questions[0].prompt);
 assert.deepEqual(historical.sourceSessions,assessment.sourceSessions);
});

test('quiz history pagination has stable boundaries, including attempts started in the same millisecond',async()=>{
 const {e,student,teacher,state}=await seedQuiz();
 for(let i=0;i<23;i++){
  const data=input(state,crypto.randomUUID(),0,0);await answer(e,student.cookie,data);await answer(e,student.cookie,{...data,questionIndex:1,choiceIndex:1});
 }
 const first=await (await get(e,teacher.cookie,'/api/quiz/results')).json();
 const second=await (await get(e,teacher.cookie,'/api/quiz/results?before='+encodeURIComponent(first.nextCursor))).json();
 assert.equal(first.attempts.length,20);assert.equal(second.attempts.length,3);assert.equal(second.nextCursor,null);
 assert.equal(new Set([...first.attempts,...second.attempts].map(a=>a.id)).size,23);
 assert.equal((await get(e,teacher.cookie,'/api/quiz/results?before=bad')).status,400);
 assert.equal((await get(e,teacher.cookie,'/api/quiz/results/not-an-id')).status,404);
});

test('accounts without a quiz have no saved state and cannot invent a quiz',async()=>{
 const e=env(),{cookie}=await login(e);
 assert.deepEqual(await (await get(e,cookie)).json(),{attempt:null});
 assert.equal((await answer(e,cookie,input({version:'a'.repeat(64)}))).status,409);
});
