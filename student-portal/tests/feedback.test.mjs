import test from 'node:test';
import assert from 'node:assert/strict';
import worker from '../worker.mjs';
import { FeedbackStore, validateFeedback } from '../feedback.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
import { validateAssessment } from '../assessment.mjs';
const origin = 'https://ab26.englishladder.com';
function env() {
 const objects = new Map();
 return {
  STUDENT_ACCOUNTS:JSON.stringify({ab26:{name:'Alex Brown',nickname:'Alex the Explorer',password:'student-test'},cd26:{name:'Casey Drew',password:'other-test'}}),
  TEACHER_PASSWORD:'teacher-test',SESSION_SECRET:'test-session-key-'.repeat(4),
  LOGIN_LIMITER:{limit:async()=>({success:true})},ACCOUNT_LIMITER:{limit:async()=>({success:true})},
  ASSETS:{fetch:async()=>new Response('public shell')},
  FEEDBACK_STORE:{
   idFromName:id=>id,
   get(id){
    if(!objects.has(id)){
     const values = new Map();
     const storage = {
      async get(key){return structuredClone(values.get(key));},
      async put(data){for(const [key,value] of Object.entries(data)) values.set(key,structuredClone(value));},
      async list({prefix,reverse,limit,end}){
       let keys=[...values.keys()].filter(k=>k.startsWith(prefix)&&(!end||k<end)).sort();
       if(reverse)keys.reverse();
       return new Map(keys.slice(0,limit).map(k=>[k,structuredClone(values.get(k))]));
      }
     };
     objects.set(id,new FeedbackStore({storage}));
    }
    return objects.get(id);
   }
  }
 };
}
function call(e,path,options={},host=origin){return worker.fetch(new Request(host+path,options),e);}
async function login(e,password='student-test',host=origin) {
 const r=await call(e,'/api/login',{method:'POST',headers:{Origin:host,'Content-Type':'application/json'},body:JSON.stringify({password})},host);
 return {response:r,cookie:r.headers.get('set-cookie').split(';')[0]};
}
function put(e,cookie,record=feedback,originHeader=origin){
 return call(e,'/api/feedback/'+feedback.id,{method:'PUT',headers:{Cookie:cookie,Origin:originHeader,'Content-Type':'application/json'},body:JSON.stringify(record)});
}
test('all profile responses omit surnames and retain the chosen nickname',async()=>{
 const e=env(),{response,cookie}=await login(e);
 const profile=await response.json();
 assert.deepEqual(profile.student,{id:'ab26',name:'Alex',nickname:'Alex the Explorer'});
 const body=await (await call(e,'/api/session',{headers:{Cookie:cookie}})).text();
 assert.doesNotMatch(body,/Brown/);
});
test('feedback list, detail, and writes require a valid session',async()=>{
 const e=env();
 for(const path of ['/api/feedback','/api/feedback/'+feedback.id,'/api/assessment']){
  for(const method of ['GET','HEAD','PUT']){
   const r=await call(e,path,{method});
   assert.equal(r.status,401);assert.equal(r.headers.get('Cache-Control'),'no-store');
  }
 }
});
test('teacher publishes private feedback; student can read but cannot write',async()=>{
 const e=env(),teacher=await login(e,'teacher-test'),student=await login(e);
 assert.equal((await put(e,student.cookie)).status,403);
 assert.equal((await put(e,teacher.cookie)).status,200);
 const list=await (await call(e,'/api/feedback',{headers:{Cookie:student.cookie}})).json();
 assert.equal(list.sessions.length,1);assert.equal(list.sessions[0].id,feedback.id);
 const read=await (await call(e,'/api/feedback/'+feedback.id,{headers:{Cookie:student.cookie}})).json();
 assert.equal(read.title,feedback.title);assert.equal(read.source.noteId,undefined);
 const teacherRead=await (await call(e,'/api/feedback/'+feedback.id,{headers:{Cookie:teacher.cookie}})).json();
 assert.equal(teacherRead.source.noteId,undefined);
 assert.equal((await call(e,'/api/feedback/2026-09-01-0900',{headers:{Cookie:student.cookie}})).status,404);
});
test('student storage is selected by host; neither IDs nor cookies cross accounts',async()=>{
 const e=env(),teacher=await login(e,'teacher-test');
 await put(e,teacher.cookie);
 const otherHost='https://cd26.englishladder.com', other=await login(e,'teacher-test',otherHost);
 assert.equal((await call(e,'/api/feedback',{headers:{Cookie:teacher.cookie}},otherHost)).status,401);
 const list=await (await call(e,'/api/feedback?student=ab26',{headers:{Cookie:other.cookie}},otherHost)).json();
 assert.equal(list.sessions.length,0);
 assert.equal((await call(e,'/api/feedback/'+feedback.id,{headers:{Cookie:other.cookie}},otherHost)).status,404);
});
test('publishing rejects cross-origin requests and unsafe or unreviewed records',async()=>{
 const e=env(),{cookie}=await login(e,'teacher-test');
 assert.equal((await put(e,cookie,feedback,'https://cd26.englishladder.com')).status,403);
 for(const changes of [
  {scope:'personal'}, {source:{...feedback.source,reviewedFullTranscript:false}},
  {id:'2026-10-01-9999'}, {startedAt:'bad date'},
  {focus:[{...feedback.focus[0],at:'02:00:00'}]},
  {summary:'x'.repeat(70000)}, {source:{...feedback.source,noteId:'https://evil.test'}}
 ]) assert.equal((await put(e,cookie,{...feedback,...changes})).status,400);
 const clean=validateFeedback({...feedback,transcript:'private raw transcript',password:'private password',studentId:'cd26'},feedback.id);
 for(const key of ['transcript','password','studentId'])assert.equal(clean[key],undefined);
});
test('feedback storage failures fail closed and do not affect public login shell',async()=>{
 const e=env(),{cookie}=await login(e);delete e.FEEDBACK_STORE;
 assert.equal((await call(e,'/api/feedback',{headers:{Cookie:cookie}})).status,503);
 assert.equal((await call(e,'/')).status,200);
 for(const path of ['/private/kh26-feedback.json','/feedback.mjs','/api/feedback/../private']) assert.notEqual((await call(e,path)).status,200);
});
test('record replacement updates its index and does not duplicate a session',async()=>{
 const e=env(),{cookie}=await login(e,'teacher-test');
 await put(e,cookie); await put(e,cookie,{...feedback,title:'Updated English feedback'});
 const data=await (await call(e,'/api/feedback',{headers:{Cookie:cookie}})).json();
 assert.equal(data.sessions.length,1);assert.equal(data.sessions[0].title,'Updated English feedback');
});
test('index pagination returns every session once, newest first',async()=>{
 const e=env(),{cookie}=await login(e,'teacher-test'),store=e.FEEDBACK_STORE.get('ab26');
 const rows={};
 for(let i=0;i<103;i++){
  const id='2026-10-01-'+String(i).padStart(4,'0');
  rows['index:'+id]={id,title:'Example'};
 }
 await store.storage.put(rows);
 const first=await (await call(e,'/api/feedback',{headers:{Cookie:cookie}})).json();
 assert.equal(first.sessions.length,100);assert.equal(first.sessions[0].id,'2026-10-01-0102');
 const second=await (await call(e,'/api/feedback?before='+first.nextCursor,{headers:{Cookie:cookie}})).json();
 assert.equal(second.sessions.length,3);assert.equal(second.nextCursor,null);
 assert.equal(new Set([...first.sessions,...second.sessions].map(s=>s.id)).size,103);
});

function putAssessment(e,cookie,record=assessment,host=origin,originHeader=host){
 return call(e,'/api/assessment',{method:'PUT',headers:{Cookie:cookie,Origin:originHeader,'Content-Type':'application/json'},body:JSON.stringify(record)},host);
}
test('assessment publishing is teacher-only, private, same-origin, and replaces the current assessment',async()=>{
 const e=env(),teacher=await login(e,'teacher-test'),student=await login(e);
 assert.deepEqual(await (await call(e,'/api/assessment',{headers:{Cookie:student.cookie}})).json(),{assessment:null});
 await put(e,teacher.cookie);
 assert.equal((await putAssessment(e,student.cookie)).status,403);
 assert.equal((await putAssessment(e,teacher.cookie,assessment,origin,'https://evil.test')).status,403);
 assert.equal((await putAssessment(e,teacher.cookie)).status,200);
 const response=await call(e,'/api/assessment',{headers:{Cookie:student.cookie}});
 assert.equal(response.headers.get('Cache-Control'),'no-store');
 assert.deepEqual(await response.json(),{assessment});
 const revised={...assessment,title:'Updated assessment'};
 assert.equal((await putAssessment(e,teacher.cookie,revised)).status,200);
 assert.deepEqual(await (await call(e,'/api/assessment',{headers:{Cookie:student.cookie}})).json(),{assessment:revised});
 assert.equal((await call(e,'/api/assessment',{method:'DELETE',headers:{Cookie:teacher.cookie}})).status,405);
});
test('assessments cannot reference another account or unavailable transcript evidence',async()=>{
 const e=env(),teacher=await login(e,'teacher-test');
 assert.equal((await putAssessment(e,teacher.cookie)).status,400);
 await put(e,teacher.cookie);
 for(const at of ['00:00:59','01:20:01']){
  const invalid={...assessment,progress:{...assessment.progress,evidence:[{sessionId:feedback.id,at}]}};
  assert.equal((await putAssessment(e,teacher.cookie,invalid)).status,400);
 }
 assert.equal((await putAssessment(e,teacher.cookie)).status,200);
 const otherHost='https://cd26.englishladder.com',other=await login(e,'teacher-test',otherHost);
 assert.equal((await call(e,'/api/assessment',{headers:{Cookie:teacher.cookie}},otherHost)).status,401);
 assert.deepEqual(await (await call(e,'/api/assessment?student=ab26',{headers:{Cookie:other.cookie}},otherHost)).json(),{assessment:null});
 assert.equal((await putAssessment(e,other.cookie,assessment,otherHost)).status,400);
});
test('assessment validation rejects invalid sources and strips unexpected private fields',async()=>{
 const e=env(),{cookie}=await login(e,'teacher-test');await put(e,cookie);
 for(const changes of [
  {scope:'personal'},{assessedOn:'2026-02-30'},{assessedOn:'2026-09-01'},
  {sourceSessions:[feedback.id,feedback.id]},{sourceSessions:[]},
  {strengths:[{...assessment.strengths[0],evidence:[{sessionId:'2026-09-01-2057',at:'00:02:00'}]}]},
  {plan:[]},{summary:'x'.repeat(70000)}
 ])assert.equal((await putAssessment(e,cookie,{...assessment,...changes})).status,400);
 const clean=validateAssessment({...assessment,transcript:'raw speech',noteUrl:'https://mynotes.zoom.us/example',studentId:'cd26'});
 assert.deepEqual(clean,assessment);
 delete e.FEEDBACK_STORE;
 assert.equal((await call(e,'/api/assessment',{headers:{Cookie:cookie}})).status,503);
});

test('quiz stays inside the private assessment, requires teacher writes, and has valid answer and pattern references',async()=>{
 const e=env(),teacher=await login(e,'teacher-test'),student=await login(e);
 await put(e,teacher.cookie);
 const record={...assessment,quiz};
 assert.equal((await putAssessment(e,student.cookie,record)).status,403);
 assert.equal((await putAssessment(e,teacher.cookie,record)).status,200);
 assert.deepEqual(await (await call(e,'/api/assessment',{headers:{Cookie:student.cookie}})).json(),{assessment:record});
 const otherHost='https://cd26.englishladder.com',other=await login(e,'teacher-test',otherHost);
 assert.deepEqual(await (await call(e,'/api/assessment',{headers:{Cookie:other.cookie}},otherHost)).json(),{assessment:null});
 assert.equal((await call(e,'/api/assessment')).status,401);
 for(const changes of [
  {correctIndex:-1},{correctIndex:2},{correctIndex:0.5},{patternIndex:-1},{patternIndex:1},
  {options:[quiz.questions[0].options[0]]},
  {options:[quiz.questions[0].options[0],quiz.questions[0].options[0]]},
  {model:''},{prompt:'x'.repeat(301)}
 ]){
  const invalid={...record,quiz:{...quiz,questions:[{...quiz.questions[0],...changes}]}};
  assert.equal((await putAssessment(e,teacher.cookie,invalid)).status,400);
 }
 const clean=validateAssessment({...record,quiz:{...quiz,studentName:'Private Name',questions:quiz.questions.map(q=>({...q,rawTranscript:'private',options:q.options.map(o=>({...o,password:'secret'}))}))}});
 assert.deepEqual(clean,record);
});
