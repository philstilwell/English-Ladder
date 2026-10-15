import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';
import worker from '../worker.mjs';
import { StudentDirectory, directoryStudents, parseStudentRows, inspectStudentRows, validateStudent } from '../student-directory.mjs';
import { QuizAutomation } from '../server-quiz-automation.mjs';
import { env as baseEnv, login, call, origin } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
import termsBank from '../business-terms-bank.json' with { type: 'json' };
import grammarBank from '../grammar-bank.json' with { type: 'json' };
import { ACTIVITY_TOOLS } from '../activities.mjs';

const admin = 'https://phil.englishladder.com';
const example = { firstName:'Morgan', lastName:'Testperson', nickname:'Morgan the Explorer', studentId:'mt26', status:'active', zoomNames:['Morgan-Zoom'], timeZone:'Asia/Tokyo', email:'private@example.test', notes:'Private administrative note', hoursAuthorized:40 };
function memory() {
  const data=new Map();let queue=Promise.resolve();
  const store={get:async k=>structuredClone(data.get(k)),put:async values=>{for(const[k,v]of Object.entries(values))data.set(k,structuredClone(v));},delete:async k=>data.delete(k),list:async({prefix})=>new Map([...data].filter(([k])=>k.startsWith(prefix)).map(([k,v])=>[k,structuredClone(v)])),
    transaction(fn){const run=queue.then(async()=>{const prior=structuredClone(data);try{return await fn(store);}catch(e){data.clear();for(const[k,v]of prior)data.set(k,v);throw e;}});queue=run.catch(()=>{});return run;}};
  return store;
}
function environment() {
  const e={...baseEnv(),STUDENT_PASSWORD:'default-test-only',STUDENT_PASSWORD_PEPPER:'fictional-pepper-for-password-tests-only',STUDENT_PASSWORD_ENCRYPTION_KEY:'ab'.repeat(32),QUIZ_STUDENTS:JSON.stringify({ab26:{firstName:'Alex',zoomNames:['AlexZoom'],timeZone:'America/New_York',startAfter:'2026-10-14T00:00:00Z'}})};
  const directory=new StudentDirectory({storage:memory()},e);
  e.STUDENT_DIRECTORY={idFromName:id=>id,get:()=>directory};
  return {e,directory};
}
const adminCall=(e,path,options={})=>call(e,path,options,admin);
async function access(e){return (await login(e,'teacher-test',admin)).cookie;}
const write=(cookie,body,method='POST')=>({method,headers:{Cookie:cookie,Origin:admin,'Content-Type':'application/json'},body:JSON.stringify(body)});
async function list(e,cookie){return (await (await adminCall(e,'/api/admin/students',{headers:{Cookie:cookie}})).json()).students;}

test('private retention roster includes paused accounts without sharing names or contacts',async()=>{
  const {e,directory}=environment(),cookie=await access(e),records=await list(e,cookie);
  for(const record of records) await adminCall(e,'/api/admin/students/'+record.key,write(cookie,{...record,status:'paused'},'PUT'));
  assert.deepEqual((await directoryStudents(e)).students,{});
  const response=await directory.fetch(new Request('https://directory.internal/retention-accounts'));
  assert.deepEqual((await response.json()).studentIds.sort(),['ab26','cd26']);
  assert.equal((await adminCall(e,'/api/admin/retention-accounts',{headers:{Cookie:cookie}})).status,404);
  const automation=new QuizAutomation({storage:memory()},e);const seen=[];
  e.FEEDBACK_STORE={idFromName:id=>id,get:id=>({fetch:async()=>{seen.push(id);return Response.json({ok:true});}})};
  await automation.run();assert.deepEqual(seen.sort(),['ab26','cd26']);
});

test('administrator quiz overview is private, reads each account separately, and does not expose answers',async()=>{
  const {e}=environment(),cookie=await access(e),records=await list(e,cookie),student=await login(e),teacher=await login(e,'teacher-test');
  const store=e.FEEDBACK_STORE.get('ab26');await store.storage.put({'assessment:current':{...assessment,quiz}});
  const response=await adminCall(e,'/api/admin/quiz-status',{headers:{Cookie:cookie}});assert.equal(response.status,200);assert.equal(response.headers.get('Cache-Control'),'no-store');
  const result=await response.json();assert.equal(result.statuses[records.find(s=>s.studentId==='ab26').key].state,'not_started');
  assert.equal(result.statuses[records.find(s=>s.studentId==='cd26').key].state,'no_quiz');
  assert.doesNotMatch(JSON.stringify(result),/correctIndex|answers|password|sourceSessions|noteId/);
  assert.equal((await adminCall(e,'/api/admin/quiz-status')).status,401);
  for(const c of [student.cookie,teacher.cookie]){
    assert.equal((await adminCall(e,'/api/admin/quiz-status',{headers:{Cookie:c}})).status,401);
    for(const path of ['/api/admin/quiz-status','/admin/quiz-status','/api/quiz/admin/quiz-status'])assert.equal((await call(e,path,{headers:{Cookie:c}})).status,404);
  }
});
test('quiz overview pages bound storage calls and report a failing account without hiding other students',async()=>{
  const {e,directory}=environment(),cookie=await access(e),records=await list(e,cookie);
  for(let i=0;i<23;i++)await directory.storage.put({['student:00000000-0000-4000-8000-'+String(i).padStart(12,'0')]:{...example,key:'00000000-0000-4000-8000-'+String(i).padStart(12,'0'),studentId:'fictional'+i,activated:true,revision:1}});
  const binding=e.FEEDBACK_STORE;let calls=0;
  e.FEEDBACK_STORE={...binding,get(id){calls++;if(id==='fictional0')throw Error('Temporarily offline');return binding.get(id);}};
  const first=await(await adminCall(e,'/api/admin/quiz-status',{headers:{Cookie:cookie}})).json();assert.equal(Object.keys(first.statuses).length,20);assert.ok(first.nextCursor);assert.equal(calls,20);
  assert.equal(first.statuses['00000000-0000-4000-8000-000000000000'].state,'unavailable');
  assert.equal(first.statuses['00000000-0000-4000-8000-000000000001'].state,'no_quiz');
  const next=await(await adminCall(e,'/api/admin/quiz-status?after='+first.nextCursor,{headers:{Cookie:cookie}})).json();assert.equal(Object.keys(next.statuses).length,5);assert.equal(next.nextCursor,null);
  assert.equal(new Set([...Object.keys(first.statuses),...Object.keys(next.statuses)]).size,25);
  assert.equal((await adminCall(e,'/api/admin/quiz-status?after=bad',{headers:{Cookie:cookie}})).status,400);
  assert.equal((await adminCall(e,'/api/admin/quiz-status',{method:'POST',headers:{Cookie:cookie}})).status,404);
});

test('administrator host accepts only teacher credentials; cookies cannot cross hosts',async()=>{
  const {e}=environment();
  assert.equal((await adminCall(e,'/')).status,200);
  assert.equal((await adminCall(e,'/api/admin/students')).status,401);
  for(const password of ['student-test','default-test-only','wrong']){
    const r=await adminCall(e,'/api/login',write('',{password}));assert.equal(r.status,401);assert.equal(r.headers.get('set-cookie'),null);
  }
  const cookie=await access(e), studentTeacher=(await login(e,'teacher-test')).cookie;
  assert.equal((await adminCall(e,'/api/admin/students',{headers:{Cookie:studentTeacher}})).status,401);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:cookie}})).status,401);
  assert.equal((await adminCall(e,'/api/session',{headers:{Cookie:cookie}})).status,200);
  for(const path of ['/admin.html','/admin.js','/api/admin/students','/directory.internal/students'])assert.equal((await call(e,path,{headers:{Cookie:studentTeacher}})).status,404);
});
test('registration and edits take effect without redeployment; private fields never reach student endpoints',async()=>{
  const {e}=environment(),cookie=await access(e);
  const response=await adminCall(e,'/api/admin/students',write(cookie,example));assert.equal(response.status,201);
  const saved=(await response.json()).student;assert.equal(saved.lastName,'Testperson');assert.ok(saved.startAfter);
  assert.deepEqual(saved.visibleActivities,['english-road','grammar-practice','business-terms']);
  const host='https://mt26.englishladder.com',student=await login(e,'DEFAULT-TEST-ONLY',host);
  assert.equal(student.response.status,200);
  for(const path of ['/api/session','/api/context','/api/feedback','/api/assessment']){
    const r=await call(e,path,{headers:{Cookie:student.cookie}},host);assert.equal(r.status,200);
    assert.doesNotMatch(await r.text(),/Testperson|private@example|Private administrative|Morgan-Zoom|hoursAuthorized/);
  }
  const automation=await directoryStudents(e);assert.deepEqual(automation.students.mt26.zoomNames,['Morgan-Zoom']);assert.equal(automation.students.mt26.firstName,'Morgan');assert.equal(automation.students.mt26.timeZone,'America/New_York');
  const paused=await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...saved,status:'paused'},'PUT'));assert.equal(paused.status,200);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:student.cookie}},host)).status,404);
  assert.equal((await directoryStudents(e)).students.mt26,undefined);
});
test('same-origin checks, bounds, and teacher password rotation protect administrator writes',async()=>{
  const {e}=environment(),cookie=await access(e);
  for(const badOrigin of ['https://ab26.englishladder.com','https://evil.test',null]){
    const options=write(cookie,example);if(badOrigin)options.headers.Origin=badOrigin;else delete options.headers.Origin;
    assert.equal((await adminCall(e,'/api/admin/students',options)).status,403);
  }
  assert.equal((await adminCall(e,'/api/admin/students',write(cookie,{...example,notes:'x'.repeat(20000)}))).status,400);
  e.TEACHER_PASSWORD='rotated-test';assert.equal((await adminCall(e,'/api/admin/students',{headers:{Cookie:cookie}})).status,401);
});
test('duplicate site and Zoom names are rejected atomically; stale edits do not overwrite changes',async()=>{
  const {e}=environment(),cookie=await access(e);
  const outcomes=await Promise.all([1,2].map(()=>adminCall(e,'/api/admin/students',write(cookie,example))));
  assert.deepEqual(outcomes.map(r=>r.status).sort(),[201,409]);
  const saved=(await list(e,cookie)).find(s=>s.studentId==='mt26');
  assert.equal((await adminCall(e,'/api/admin/students',write(cookie,{...example,studentId:'ot26',zoomNames:['mORGAN-zOOM']}))).status,409);
  assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...saved,notes:'Edited'},'PUT'))).status,200);
  assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,saved,'PUT'))).status,409);
  const latest=(await list(e,cookie)).find(s=>s.key===saved.key);
  for(const patch of [{studentId:'mm26'},{status:'draft'}])assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...latest,...patch},'PUT'))).status,400);
});
test('drafts are private and cannot sign in or run automation; activation requires names and mapping',async()=>{
  const {e}=environment(),cookie=await access(e);
  const r=await adminCall(e,'/api/admin/students',write(cookie,{...example,status:'draft',zoomNames:[]}));const draft=(await r.json()).student;
  assert.equal(draft.startAfter,null);
  assert.equal((await call(e,'/api/context',{},'https://mt26.englishladder.com')).status,404);
  assert.equal((await adminCall(e,'/api/admin/students/'+draft.key,write(cookie,{...draft,status:'active'},'PUT'))).status,400);
  assert.equal((await directoryStudents(e)).students.mt26,undefined);
  assert.throws(()=>validateStudent({...example,studentId:'phil'}));
  assert.throws(()=>validateStudent({...example,timeZone:'Bad/Zone'}));
});
const sheetRows=[['Expired','Course Name','Learner/Group Name','Learner Time Zone','Ends On','File No.','Hours Authorized','Hours Used','Hours Upcoming/Pending','Unscheduled Hours','Name','Staff','Gmail','Other EM','Contacted'],
 ['FALSE','Training','Morgan Testperson','Osaka, Sapporo, Tokyo','31-Jan-2027','shared-file','40','2','1','37','Morgan Testperson','Pat','private@example.test','','10/14/2026'],
 ['FALSE','Training','Casey Example','Eastern Time (US & Canada)','31-Jan-2027','shared-file','40','2','1','37','Casey Example']];

test('personal passwords replace the default, revoke only student sessions, and never leave the private account projection',async()=>{
  const {e,directory}=environment(),cookie=await access(e),host='https://mt26.englishladder.com';
  const saved=(await (await adminCall(e,'/api/admin/students',write(cookie,example))).json()).student;
  const oldStudent=await login(e,'default-test-only',host),teacher=await login(e,'teacher-test',host),other=await login(e,'student-test');
  const result=await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...saved,newPassword:'Unique-TEST-Secret',confirmPassword:'unique-test-secret'},'PUT'));
  assert.equal(result.status,200);const responseText=await result.text();assert.doesNotMatch(responseText,/unique-test-secret|passwordCredential|"salt"|"hash"/i);
  const updated=JSON.parse(responseText).student;assert.equal(updated.hasCustomPassword,true);
  const raw=(await directory.records()).find(s=>s.key===saved.key);
  assert.ok(raw.passwordCredential.salt);assert.ok(raw.passwordCredential.hash);assert.doesNotMatch(JSON.stringify(raw),/unique-test-secret/i);
  assert.equal((await call(e,'/api/login',{method:'POST',headers:{Origin:host,'Content-Type':'application/json'},body:JSON.stringify({password:'default-test-only'})},host)).status,401);
  const fresh=await login(e,'UNIQUE-TEST-SECRET',host);assert.equal(fresh.response.status,200);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:oldStudent.cookie}},host)).status,401);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:teacher.cookie}},host)).status,200);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:other.cookie}})).status,200);
  for(const path of ['/api/session','/api/context','/api/feedback','/api/assessment']){
    const r=await call(e,path,{headers:{Cookie:fresh.cookie}},host);assert.equal(r.status,200);assert.doesNotMatch(await r.text(),/passwordCredential|credentialAccountKey|salt|unique-test-secret/i);
  }
  assert.doesNotMatch(JSON.stringify(await list(e,cookie)),/passwordCredential|"salt"|"hash"/);
  assert.doesNotMatch(JSON.stringify(await directoryStudents(e)),/password|salt|hash/i);
  // Empty password fields preserve the verifier, including through other edits.
  const blank=(await (await adminCall(e,'/api/admin/students/'+updated.key,write(cookie,{...updated,newPassword:'',confirmPassword:'',notes:'Changed note'},'PUT'))).json()).student;
  assert.deepEqual((await directory.records()).find(s=>s.key===saved.key).passwordCredential,raw.passwordCredential);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:fresh.cookie}},host)).status,200);
  // Reassigning even the same password issues a fresh salt and revokes old sessions.
  await adminCall(e,'/api/admin/students/'+blank.key,write(cookie,{...blank,newPassword:'unique-test-secret',confirmPassword:'unique-test-secret'},'PUT'));
  assert.equal((await call(e,'/api/session',{headers:{Cookie:fresh.cookie}},host)).status,401);
  assert.notEqual((await directory.records()).find(s=>s.key===saved.key).passwordCredential.salt,raw.passwordCredential.salt);
});
test('password validation is atomic, rejects the teacher password, and permits a custom password without a shared default',async()=>{
  const {e}=environment(),cookie=await access(e);
  for(const patch of [{newPassword:'short',confirmPassword:'short'},{newPassword:'long-enough',confirmPassword:'different'},{newPassword:'TEACHER-TEST',confirmPassword:'teacher-test'},{confirmPassword:'lonely-confirm'},{newPassword:123456,confirmPassword:'123456'},{newPassword:'x'.repeat(129),confirmPassword:'x'.repeat(129)}]){
    assert.equal((await adminCall(e,'/api/admin/students',write(cookie,{...example,...patch}))).status,400);
    assert.ok(!(await list(e,cookie)).some(s=>s.studentId==='mt26'));
  }
  delete e.STUDENT_PASSWORD;
  const response=await adminCall(e,'/api/admin/students',write(cookie,{...example,newPassword:'personal-test',confirmPassword:'personal-test'}));assert.equal(response.status,201);
  assert.equal((await login(e,'personal-test','https://mt26.englishladder.com')).response.status,200);
});
test('password assignment cannot be performed from a student host or with a stale record',async()=>{
  const {e}=environment(),cookie=await access(e),student=await login(e,'student-test');
  const saved=(await (await adminCall(e,'/api/admin/students',write(cookie,example))).json()).student;
  const payload={...saved,newPassword:'private-test',confirmPassword:'private-test'};
  assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(student.cookie,payload,'PUT'))).status,401);
  const cross=write(cookie,payload,'PUT');cross.headers.Origin=origin;assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,cross)).status,403);
  await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...saved,notes:'New version'},'PUT'));
  assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,payload,'PUT'))).status,409);
  assert.equal((await login(e,'default-test-only','https://mt26.englishladder.com')).response.status,200);
});
test('spreadsheet imports preserve separate students sharing a file number, create drafts, and never overwrite edits',async()=>{
  const {e}=environment(),cookie=await access(e);
  const parsed=parseStudentRows(sheetRows);assert.equal(parsed.length,2);assert.equal(parsed[0].timeZone,'Asia/Tokyo');assert.equal(parsed[0].endsOn,'2027-01-31');
  assert.equal((await adminCall(e,'/api/admin/import/preview',write(cookie,{rows:sheetRows}))).status,200);
  assert.equal((await list(e,cookie)).length,2);
  const result=await (await adminCall(e,'/api/admin/import',write(cookie,{rows:sheetRows}))).json();assert.equal(result.imported,2);
  const records=await list(e,cookie);const imported=records.filter(s=>s.source);assert.equal(imported.length,2);assert.ok(imported.every(s=>s.status==='draft'&&s.zoomNames.length===0));
  const second=await (await adminCall(e,'/api/admin/import',write(cookie,{rows:sheetRows}))).json();assert.equal(second.imported,0);assert.equal(second.skipped,2);
  assert.equal((await list(e,cookie)).length,4);
});
test('directory changes retry unmatched notes and use new Zoom names on the next nightly run',async()=>{
  const {e}=environment(),cookie=await access(e),storage=memory(),automation=new QuizAutomation({storage},e);
  await storage.put({'job:test':{status:'needs_attention',lastError:'student_not_matched',tries:2,nextAt:999}});
  await adminCall(e,'/api/admin/students',write(cookie,example));
  await automation.refreshDirectory();
  assert.deepEqual((await automation.students()).mt26.zoomNames,['Morgan-Zoom']);
  assert.equal((await storage.get('job:test')).status,'pending');
});

const html=readFileSync(new URL('../public/admin.html',import.meta.url),'utf8'),script=readFileSync(new URL('../public/admin.js',import.meta.url),'utf8');
const fixture={...example,visibleActivities:['english-road','grammar-practice'],key:'11111111-1111-4111-8111-111111111111',revision:1,activated:true,startAfter:'2026-10-14T12:00:00Z'};
const flush=async()=>{for(let i=0;i<12;i++)await new Promise(r=>setTimeout(r,1));};
function browser(custom){const dom=new JSDOM(html,{url:admin+'/#students',runScripts:'outside-only',pretendToBeVisual:true});dom.window.HTMLDialogElement.prototype.showModal=function(){this.open=true;};dom.window.HTMLDialogElement.prototype.close=function(){this.open=false;};dom.window.fetch=async(path,opts)=>{
  const result=custom?.(path,opts);if(result)return result;
  return Response.json(path==='/api/session'?{administrator:true}:path==='/api/admin/students'?{activities:ACTIVITY_TOOLS,students:[fixture]}:path==='/api/admin/quiz-status'?{statuses:{[fixture.key]:{state:'not_started',title:'Practice',total:2}},nextCursor:null}:path==='/api/admin/automation'?{enabled:true,connected:true}:{});
};dom.window.eval(readFileSync(new URL('../public/business-terms.js',import.meta.url),'utf8'));dom.window.eval(readFileSync(new URL('../public/grammar-practice.js',import.meta.url),'utf8'));dom.window.eval(script);return dom;}
test('administrator list links to editable accounts and has a separate registration form',async()=>{
  const dom=browser();await flush();const w=dom.window,d=w.document;
  assert.match(d.getElementById('student-rows').textContent,/Morgan Testperson/);
  d.querySelector('.student-name').click();await flush();assert.equal(d.getElementById('lastName').value,'Testperson');assert.equal(d.getElementById('studentId').readOnly,true);
  w.location.hash='#register';await flush();assert.equal(d.getElementById('edit-title').textContent,'Register new student');assert.equal(d.getElementById('lastName').value,'');assert.equal(d.getElementById('studentId').readOnly,false);
  assert.equal(d.querySelectorAll('input[type="password"]').length,4);assert.doesNotMatch(script,/localStorage|sessionStorage|innerHTML/);dom.window.close();
});

test('administrator checkboxes load saved tools, save subsets and none, and clear on navigation and sign-out', async () => {
  let saved = structuredClone(fixture), body;
  const dom = browser((path, options) => {
    if (path === '/api/admin/students') return Response.json({ activities: ACTIVITY_TOOLS, students: [saved] });
    if (path === '/api/admin/students/' + fixture.key && options?.method === 'PUT') {
      body = JSON.parse(options.body); saved = { ...saved, ...body, revision: saved.revision + 1 };
      return Response.json({ student: saved });
    }
  });
  await flush(); const w = dom.window, d = w.document;
  d.querySelector('.student-name').click(); await flush();
  const chosen = () => [...d.querySelectorAll('#student-activities input:checked')].map(box => box.value);
  assert.deepEqual(chosen(), ['english-road', 'grammar-practice']);
  assert.equal(d.querySelectorAll('#student-activities input').length, ACTIVITY_TOOLS.length);
  for (const box of d.querySelectorAll('#student-activities input')) box.checked = box.value === 'business-terms';
  d.getElementById('student-form').dispatchEvent(new w.Event('submit', { bubbles: true, cancelable: true })); await flush();
  assert.deepEqual(body.visibleActivities, ['business-terms']); assert.deepEqual(chosen(), ['business-terms']);
  d.getElementById('list-nav').click(); await flush(); assert.equal(d.getElementById('student-activities').textContent, '');
  d.querySelector('.student-name').click(); await flush(); assert.deepEqual(chosen(), ['business-terms']);
  for (const box of d.querySelectorAll('#student-activities input')) box.checked = false;
  d.getElementById('student-form').dispatchEvent(new w.Event('submit', { bubbles: true, cancelable: true })); await flush();
  assert.deepEqual(body.visibleActivities, []); assert.deepEqual(chosen(), []);
  d.getElementById('register-nav').click(); await flush(); assert.deepEqual(chosen(), ['english-road', 'grammar-practice', 'business-terms']);
  d.getElementById('sign-out').click(); await flush(); assert.equal(d.getElementById('student-activities').textContent, '');
  w.close();
});

test('a missing activity catalog cannot silently clear selections through an administrator save', async () => {
  let writes = 0;
  const dom = browser((path, options) => {
    if (options?.method === 'PUT' || options?.method === 'POST') writes++;
    if (path === '/api/admin/students') return Response.json({ students: [fixture] });
  });
  await flush(); const w = dom.window, d = w.document;
  d.getElementById('student-form').dispatchEvent(new w.Event('submit', { bubbles: true, cancelable: true })); await flush();
  assert.equal(writes, 0); assert.equal(d.querySelectorAll('#student-activities input').length, 0);
  w.close();
});

test('Technical notes supports direct navigation, clears account details, and stays behind the signed-in view',async()=>{
  const dom=browser(),w=dom.window,d=w.document;
  w.location.hash='#technical-notes';await flush();
  assert.equal(d.getElementById('technical-view').hidden,false);
  assert.equal(d.getElementById('technical-nav').getAttribute('aria-current'),'page');
  assert.equal(d.getElementById('list-view').hidden,true);
  d.getElementById('list-nav').click();await flush();
  assert.equal(d.getElementById('technical-view').hidden,true);
  d.querySelector('.student-name').click();await flush();
  d.getElementById('technical-nav').click();await flush();
  assert.equal(d.getElementById('edit-view').hidden,true);
  assert.equal(d.getElementById('current-password').value,'');
  assert.equal(d.getElementById('cefr-content').textContent,'');
  d.getElementById('sign-out').click();await flush();
  assert.equal(d.getElementById('admin-view').hidden,true);
  assert.equal(d.getElementById('login-view').hidden,false);w.close();
});
test('student list shows latest quiz states, updates after Refresh, and treats lookup failures separately',async()=>{
  let state={state:'in_progress',answered:1,total:2},fail=false;
  const dom=browser(path=>path==='/api/admin/quiz-status'?(fail?Response.json({error:'Unavailable'},{status:503}):Response.json({statuses:{[fixture.key]:state},nextCursor:null})):null);
  await flush();const d=dom.window.document;
  assert.match(d.querySelector('.latest-quiz').textContent,/In progress.*1 of 2 questions answered/);
  state={state:'completed',completedAt:'2026-10-14T14:00:00.000Z'};d.getElementById('refresh').click();await flush();
  assert.match(d.querySelector('.latest-quiz').textContent,/Done.*Finished Oct 14, 2026, 10:00 AM Eastern/);
  for(const [status,label] of [['not_started','Not started'],['no_quiz','No quiz yet']]){state={state:status};d.getElementById('refresh').click();await flush();assert.match(d.querySelector('.latest-quiz').textContent,new RegExp(label));}
  fail=true;d.getElementById('refresh').click();await flush();assert.match(d.querySelector('.latest-quiz').textContent,/Unable to check/);assert.match(d.getElementById('student-rows').textContent,/Morgan Testperson/);
  dom.window.close();
});
test('quiz status follows subsequent pages and a response after sign-out cannot restore the list',async()=>{
  let pending;
  const dom=browser(path=>path==='/api/admin/quiz-status'?Response.json({statuses:{},nextCursor:fixture.key}):path.startsWith('/api/admin/quiz-status?')?new Promise(r=>{pending=r;}):null);
  await flush();const d=dom.window.document;assert.match(d.querySelector('.latest-quiz').textContent,/Checking/);
  d.getElementById('sign-out').click();await flush();pending(Response.json({statuses:{[fixture.key]:{state:'completed',completedAt:'2026-10-14T14:00:00Z'}},nextCursor:null}));await flush();
  assert.equal(d.getElementById('student-rows').textContent,'');assert.equal(d.getElementById('admin-view').hidden,true);dom.window.close();
});
test('sign-out clears form fields and directory; delayed responses cannot restore private data',async()=>{
  let pending;const dom=browser(path=>path==='/api/admin/automation'?new Promise(r=>{pending=r;}):null);await flush();const d=dom.window.document;
  d.querySelector('.student-name').click();await flush();assert.equal(d.getElementById('email').value,'private@example.test');
  d.getElementById('newPassword').value='unsaved-test-secret';d.getElementById('confirmPassword').value='unsaved-test-secret';
  d.getElementById('sign-out').click();await flush();pending(Response.json({enabled:true,connected:true}));await flush();
  assert.equal(d.getElementById('admin-view').hidden,true);assert.equal(d.getElementById('student-rows').textContent,'');
  for(const field of ['email','notes','firstName','lastName','zoomNames','newPassword','confirmPassword'])assert.equal(d.getElementById(field).value,'');
  assert.doesNotMatch(d.getElementById('admin-view').textContent,/Testperson|private@example/);dom.window.close();
});
test('expired administrator sessions clear private data and imported text renders safely',async()=>{
  let expired=false;const dom=browser(path=>path==='/api/admin/students'?(expired?Response.json({error:'Expired'},{status:401}):Response.json({activities:ACTIVITY_TOOLS,students:[{...fixture,firstName:'<img src=x onerror=alert(1)>'}]})):null);await flush();const d=dom.window.document;
  assert.equal(d.querySelector('#student-rows img'),null);expired=true;d.getElementById('refresh').click();await flush();assert.equal(d.getElementById('admin-view').hidden,true);assert.equal(d.getElementById('student-rows').textContent,'');dom.window.close();
});

test('account form checks password confirmation, lowercases input, and clears it after save or navigation',async()=>{
  let body,writes=0;
  const dom=browser((path,opts)=>opts?.method==='PUT'?(writes++,body=JSON.parse(opts.body),Response.json({student:{...fixture,revision:2,hasCustomPassword:true}})):null);
  await flush();const w=dom.window,d=w.document;
  d.querySelector('.student-name').click();await flush();
  const first=d.getElementById('newPassword'),second=d.getElementById('confirmPassword');
  first.value='ABCdef-TEST';first.dispatchEvent(new w.Event('input'));assert.equal(first.value,'abcdef-test');
  second.value='different-test';d.getElementById('student-form').dispatchEvent(new w.Event('submit',{cancelable:true}));await flush();
  assert.equal(writes,0);assert.match(d.getElementById('message').textContent,/do not match/);
  second.value='ABCDEF-TEST';second.dispatchEvent(new w.Event('input'));
  d.getElementById('student-form').dispatchEvent(new w.Event('submit',{cancelable:true}));await flush();
  assert.equal(writes,1);assert.equal(body.newPassword,'abcdef-test');assert.equal(body.confirmPassword,'abcdef-test');
  assert.equal(first.value,'');assert.equal(second.value,'');assert.match(d.getElementById('password-status').textContent,/personal password/);
  first.value='unsaved-test';w.location.hash='#students';await flush();assert.equal(first.value,'');
  dom.window.close();
});

test('imports exclude checked rows and expired course dates, using Eastern calendar dates inclusively',()=>{
  const rows=structuredClone(sheetRows);
  rows[1][4]='14-Oct-2026'; rows[2][4]='13-Oct-2026';
  const checked=structuredClone(rows[1]); checked[0]='TRUE'; checked[2]='Checked Example'; checked[10]='Checked Example'; checked[4]='31-Jan-2027'; rows.push(checked);
  const parsed=inspectStudentRows(rows,Date.parse('2026-10-15T03:30:00Z'));
  assert.equal(parsed.students.length,1);assert.equal(parsed.excluded.length,2);
  assert.equal(parsed.students[0].endsOn,'2026-10-14');
  assert.deepEqual(new Set(parsed.excluded.map(r=>r.reason)),new Set(['expired','checked']));
  assert.throws(()=>parseStudentRows(sheetRows.map(row=>row.slice(1))),/checkbox column/);
  assert.throws(()=>parseStudentRows(sheetRows.map(row=>row.filter((_,i)=>i!==4))),/Ends On/);
});

test('reconciling exclusions removes only untouched imported drafts and preserves edited or active accounts',async()=>{
  const {e}=environment(),cookie=await access(e);
  await adminCall(e,'/api/admin/import',write(cookie,{rows:sheetRows}));
  let records=await list(e,cookie);const edited=records.find(s=>s.source?.name==='Casey Example');
  await adminCall(e,'/api/admin/students/'+edited.key,write(cookie,{...edited,notes:'Owner edited this record'},'PUT'));
  const rows=structuredClone(sheetRows);rows[1][0]='TRUE';rows[2][0]='TRUE';
  const response=await (await adminCall(e,'/api/admin/import',write(cookie,{rows,reconcileExcluded:true}))).json();
  assert.equal(response.removed,1);assert.equal(response.excluded,2);
  records=await list(e,cookie);assert.ok(!records.some(s=>s.source?.name==='Morgan Testperson'));assert.ok(records.some(s=>s.key===edited.key));
  assert.ok(records.some(s=>s.studentId==='ab26'&&s.status==='active'));
});

test('pausing the original student does not disable the signed Zoom notification endpoint for other students',async()=>{
  const {e}=environment(),cookie=await access(e);const original=(await list(e,cookie)).find(s=>s.studentId==='ab26');
  await adminCall(e,'/api/admin/students/'+original.key,write(cookie,{...original,status:'paused'},'PUT'));
  let forwarded=false;e.QUIZ_AUTOMATION={idFromName:id=>id,get:()=>({fetch:async req=>{forwarded=new URL(req.url).pathname==='/webhook';return Response.json({error:'Invalid signature'},{status:401});}})};
  assert.equal((await call(e,'/api/automation/webhook',{method:'POST',body:'{}'})).status,401);assert.equal(forwarded,true);
  assert.equal((await call(e,'/api/context')).status,404);
});

test('login details reveal only on the administrator host, with encrypted storage and no cached responses',async()=>{
  const {e,directory}=environment(),cookie=await access(e);
  const saved=(await(await adminCall(e,'/api/admin/students',write(cookie,{...example,newPassword:'Copy-TEST-Only',confirmPassword:'copy-test-only'}))).json()).student;
  const path='/api/admin/students/'+saved.key+'/login-details';
  const r=await adminCall(e,path,{headers:{Cookie:cookie}});assert.equal(r.status,200);assert.equal(r.headers.get('Cache-Control'),'no-store');assert.equal(r.headers.get('Access-Control-Allow-Origin'),null);
  assert.deepEqual(await r.json(),{firstName:'Morgan',studentId:'mt26',url:'https://mt26.englishladder.com/',active:true,password:'copy-test-only',message:null});
  const raw=(await directory.records()).find(x=>x.key===saved.key);assert.equal(raw.passwordCopy.scheme,'aes-256-gcm-v1');assert.doesNotMatch(JSON.stringify(raw),/copy-test-only/i);
  assert.doesNotMatch(JSON.stringify(await list(e,cookie)),/copy-test-only|passwordCopy|ciphertext|passwordCredential|salt|hash/i);
  assert.doesNotMatch(JSON.stringify(await directoryStudents(e)),/password|ciphertext/i);
  const account=await(await directory.fetch(new Request('https://directory.internal/account/mt26'))).json();assert.equal(account.passwordCopy,undefined);
  assert.equal((await adminCall(e,path)).status,401);
  const student=await login(e,'copy-test-only','https://mt26.englishladder.com'),teacher=await login(e,'teacher-test','https://mt26.englishladder.com');
  for(const c of [student.cookie,teacher.cookie]){
    assert.equal((await adminCall(e,path,{headers:{Cookie:c}})).status,401);
    assert.equal((await call(e,path,{headers:{Cookie:c}},'https://mt26.englishladder.com')).status,404);
  }
  for(const headers of [{Origin:origin},{Origin:'https://outside.example'},{'Sec-Fetch-Site':'cross-site'}])assert.equal((await adminCall(e,path,{headers:{Cookie:cookie,...headers}})).status,403);
  e.TEACHER_PASSWORD='changed-teacher-test';assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,401);
});

test('known existing passwords can gain an encrypted copy without changing student sessions; stale or wrong copies are rejected',async()=>{
  const {e,directory}=environment(),cookie=await access(e),host='https://mt26.englishladder.com';
  const saved=(await(await adminCall(e,'/api/admin/students',write(cookie,{...example,newPassword:'Known-test-only',confirmPassword:'known-test-only'}))).json()).student;
  const raw=(await directory.records()).find(x=>x.key===saved.key);delete raw.passwordCopy;
  await directory.storage.put({['student:'+saved.key]:raw});
  const student=await login(e,'known-test-only',host),path='/api/admin/students/'+saved.key+'/login-details';
  const missing=await(await adminCall(e,path,{headers:{Cookie:cookie}})).json();assert.equal(missing.password,null);assert.match(missing.message,/older password/);
  assert.equal((await adminCall(e,path,write(cookie,{revision:saved.revision,password:'wrong-test'},'PUT'))).status,400);
  const badOrigin=write(cookie,{revision:saved.revision,password:'known-test-only'},'PUT');badOrigin.headers.Origin=origin;assert.equal((await adminCall(e,path,badOrigin)).status,403);
  assert.equal((await adminCall(e,path,write(cookie,{revision:saved.revision-1,password:'known-test-only'},'PUT'))).status,409);
  const restore=await adminCall(e,path,write(cookie,{revision:saved.revision,password:'KNOWN-TEST-ONLY'},'PUT'));assert.equal(restore.status,200);assert.deepEqual(await restore.json(),{saved:true});
  const updated=(await directory.records()).find(x=>x.key===saved.key);assert.deepEqual(updated.passwordCredential,raw.passwordCredential);assert.ok(updated.passwordCopy);assert.equal(updated.revision,saved.revision+1);
  assert.equal((await call(e,'/api/session',{headers:{Cookie:student.cookie}},host)).status,200);
  assert.equal((await(await adminCall(e,path,{headers:{Cookie:cookie}})).json()).password,'known-test-only');
  const record=(await list(e,cookie)).find(s=>s.key===saved.key);
  await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{...record,notes:'Other edit'},'PUT'));
  assert.deepEqual((await directory.records()).find(x=>x.key===saved.key).passwordCopy,updated.passwordCopy);
});

test('password copies are bound to account and credential; missing encryption settings cannot partially change a password',async()=>{
  const {e,directory}=environment(),cookie=await access(e);
  const make=async values=>(await(await adminCall(e,'/api/admin/students',write(cookie,{...values,newPassword:'Same-test-only',confirmPassword:'same-test-only'}))).json()).student;
  const a=await make(example),b=await make({...example,studentId:'mn26',zoomNames:['OtherZoom']});
  const records=await directory.records(),rawA=records.find(s=>s.key===a.key),rawB=records.find(s=>s.key===b.key);
  const path='/api/admin/students/'+b.key+'/login-details';
  await directory.storage.put({['student:'+b.key]:{...rawB,passwordCopy:rawA.passwordCopy}});
  assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,503);
  await directory.storage.put({['student:'+b.key]:{...rawB,passwordCredential:rawA.passwordCredential}});
  assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,503);
  await directory.storage.put({['student:'+b.key]:rawB});
  delete e.STUDENT_PASSWORD_ENCRYPTION_KEY;
  assert.equal((await adminCall(e,'/api/admin/students/'+b.key,write(cookie,{...b,newPassword:'Changed-test-only',confirmPassword:'changed-test-only'},'PUT'))).status,400);
  assert.deepEqual((await directory.records()).find(s=>s.key===b.key),rawB);
  assert.equal((await login(e,'same-test-only','https://mn26.englishladder.com')).response.status,200);
  assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,503);
});

test('default and legacy passwords are visible only in login details, with inactive sites and universal credentials handled safely',async()=>{
  const {e}=environment(),cookie=await access(e);
  const legacy=(await list(e,cookie)).find(s=>s.studentId==='ab26');
  const get=async key=>adminCall(e,'/api/admin/students/'+key+'/login-details',{headers:{Cookie:cookie}});
  assert.equal((await(await get(legacy.key)).json()).password,'student-test');
  const draft=(await(await adminCall(e,'/api/admin/students',write(cookie,{...example,status:'draft',studentId:'',zoomNames:[]}))).json()).student;
  assert.deepEqual(await(await get(draft.key)).json(),{firstName:'Morgan',studentId:'',url:null,active:false,password:'default-test-only',message:null});
  e.STUDENT_PASSWORD=e.TEACHER_PASSWORD;assert.equal((await get(draft.key)).status,409);
  assert.equal((await get('00000000-0000-4000-8000-000000000000')).status,404);
});

const loginFixture={firstName:'Morgan',studentId:'mt26',url:'https://mt26.englishladder.com/',active:true,password:'fictional-copy-secret',message:null};
test('administrator can reveal and copy fresh login details; navigation and sign-out clear every secret field',async()=>{
  let password=loginFixture.password,copied;
  const dom=browser(path=>path.endsWith('/login-details')?Response.json({...loginFixture,password}):null);await flush();const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async value=>{copied=value;}}});
  d.querySelector('.student-name').click();await flush();
  assert.equal(d.getElementById('current-password').value,password);assert.equal(d.getElementById('current-password').type,'password');
  d.getElementById('reveal-password').click();assert.equal(d.getElementById('current-password').type,'text');assert.equal(d.getElementById('reveal-password').getAttribute('aria-pressed'),'true');
  password='newer-fictional-secret';d.getElementById('copy-login-details').click();await flush();
  assert.equal(copied,'English Ladder — Morgan\nSign in: https://mt26.englishladder.com/\nStudent ID: mt26\nPassword: newer-fictional-secret');assert.match(d.getElementById('login-details-status').textContent,/copied/);
  w.location.hash='#students';await flush();assert.equal(d.getElementById('current-password').value,'');assert.equal(d.getElementById('current-password').type,'password');assert.equal(d.getElementById('login-url').value,'');
  d.querySelector('.student-name').click();await flush();d.getElementById('sign-out').click();await flush();
  for(const id of ['current-password','login-url','copy-login-text'])assert.equal(d.getElementById(id).value,'');assert.equal(d.getElementById('login-details-panel').hidden,true);dom.window.close();
});

test('late login-detail responses cannot restore passwords after navigation or expiry, or copy another account',async()=>{
  let pending,copyCount=0;
  const dom=browser(path=>path.endsWith('/login-details')?new Promise(r=>{pending=r;}):null);await flush();const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async()=>{copyCount++;}}});
  d.querySelector('.student-name').click();await flush();w.location.hash='#register';await flush();pending(Response.json(loginFixture));await flush();assert.equal(d.getElementById('current-password').value,'');
  w.location.hash='#students/'+fixture.key;await flush();pending(Response.json(loginFixture));await flush();
  d.getElementById('copy-login-details').click();await flush();w.location.hash='#register';await flush();pending(Response.json(loginFixture));await flush();assert.equal(copyCount,0);
  w.location.hash='#students/'+fixture.key;await flush();pending(Response.json({error:'Expired'},{status:401}));await flush();assert.equal(d.getElementById('admin-view').hidden,true);assert.equal(d.getElementById('current-password').value,'');assert.equal(copyCount,0);dom.window.close();
});

test('manual copy fallback stays private and clears on leaving; inactive or unavailable passwords cannot be copied',async()=>{
  let data=loginFixture;
  const dom=browser(path=>path.endsWith('/login-details')?Response.json(data):null);await flush();const w=dom.window,d=w.document;
  d.querySelector('.student-name').click();await flush();d.getElementById('copy-login-details').click();await flush();
  assert.equal(d.getElementById('copy-fallback').hidden,false);assert.match(d.getElementById('copy-login-text').value,/fictional-copy-secret/);
  w.location.hash='#students';await flush();assert.equal(d.getElementById('copy-login-text').value,'');assert.equal(d.getElementById('copy-fallback').hidden,true);
  data={...loginFixture,active:false};d.querySelector('.student-name').click();await flush();assert.equal(d.getElementById('copy-login-details').disabled,true);
  data={...loginFixture,password:null,message:'No copy available.'};d.getElementById('refresh-login-details').click();await flush();assert.equal(d.getElementById('copy-login-details').disabled,true);assert.equal(d.getElementById('reveal-password').disabled,true);assert.match(d.getElementById('login-details-status').textContent,/No copy available/);dom.window.close();
});

test('paused accounts are collapsed below the main list, remain editable, and are found by search',async()=>{
  const paused={...fixture,key:'22222222-2222-4222-8222-222222222222',firstName:'Taylor',studentId:'tt26',status:'paused'};
  const dom=browser(path=>path==='/api/admin/students'?Response.json({activities:ACTIVITY_TOOLS,students:[fixture,paused]}):undefined);await flush();const w=dom.window,d=w.document;
  const section=d.getElementById('paused-students');assert.equal(section.open,false);assert.equal(section.hidden,false);
  assert.match(d.getElementById('student-rows').textContent,/Morgan/);assert.doesNotMatch(d.getElementById('student-rows').textContent,/Taylor/);
  assert.match(d.getElementById('paused-student-rows').textContent,/Taylor/);assert.equal(d.getElementById('paused-count').textContent,'1');
  section.open=true;await flush();assert.equal(section.open,true);
  const search=d.getElementById('search');search.value='Taylor';search.dispatchEvent(new w.Event('input'));
  assert.equal(section.open,true);assert.equal(d.getElementById('main-student-table').hidden,true);
  d.querySelector('#paused-student-rows .student-name').click();await flush();assert.equal(d.getElementById('status').value,'paused');
  d.getElementById('sign-out').click();await flush();assert.equal(section.open,false);assert.equal(d.getElementById('paused-student-rows').textContent,'');dom.window.close();
});

test('deletion requires a current administrator session, exact origin, revision, and typed confirmation',async()=>{
  const {e}=environment(),cookie=await access(e),saved=(await list(e,cookie)).find(s=>s.studentId==='ab26');
  const path='/api/admin/students/'+saved.key,body={revision:saved.revision,confirmation:'ab26'};
  const student=await login(e),teacher=await login(e,'teacher-test');
  for(const unauthorized of ['',student.cookie,teacher.cookie])assert.equal((await adminCall(e,path,write(unauthorized,body,'DELETE'))).status,401);
  const cross=write(cookie,body,'DELETE');cross.headers.Origin='https://elsewhere.test';assert.equal((await adminCall(e,path,cross)).status,403);
  assert.equal((await call(e,path,{...write(student.cookie,body,'DELETE'),headers:{Cookie:student.cookie,Origin:origin}})).status,405);
  for(const invalid of [{revision:1},{revision:1,confirmation:'wrong'},null])assert.equal((await adminCall(e,path,write(cookie,invalid,'DELETE'))).status,400);
  assert.equal((await adminCall(e,path,write(cookie,{...body,revision:999},'DELETE'))).status,409);
  assert.equal((await list(e,cookie)).length,2);
});

test('deletion removes only the confirmed account and all its saved learning records, blocks old sessions, and retires the address',async()=>{
  const {e,directory}=environment(),cookie=await access(e);
  const created=await adminCall(e,'/api/admin/students',write(cookie,{...example,newPassword:'fictional-test',confirmPassword:'fictional-test'}));
  const saved=(await created.json()).student,path='/api/admin/students/'+saved.key,body={revision:saved.revision,confirmation:' MT26 '};
  const student=await login(e,'fictional-test','https://mt26.englishladder.com'),teacher=await login(e,'teacher-test','https://mt26.englishladder.com');
  const store=e.FEEDBACK_STORE.get('mt26'),other=e.FEEDBACK_STORE.get('ab26');
  await store.storage.put({'assessment:current':{...assessment,quiz},'feedback:one':feedback,'quiz:attempt:one':{private:'answers'},'quiz:active':'one',...Object.fromEntries(Array.from({length:270},(_,i)=>['archive:'+i,{private:'history'}]))});
  await other.storage.put({'untouched':{private:'other student'}});
  const response=await adminCall(e,path,write(cookie,body,'DELETE'));assert.equal(response.status,200);assert.deepEqual(await response.json(),{deleted:true});
  assert.equal(await directory.storage.get('student:'+saved.key),undefined);
  assert.deepEqual([...await store.storage.list()], [['account:deleted',true]]);
  assert.deepEqual(await other.storage.get('untouched'),{private:'other student'});
  assert.equal((await list(e,cookie)).length,2);assert.equal((await adminCall(e,path+'/login-details',{headers:{Cookie:cookie}})).status,404);
  for(const session of [student,teacher])assert.equal((await call(e,'/api/session',{headers:{Cookie:session.cookie}},'https://mt26.englishladder.com')).status,404);
  assert.equal((await directory.fetch(new Request('https://directory.internal/integration-account/mt26'))).status,404);
  assert.equal((await directoryStudents(e)).students.mt26,undefined);
  assert.equal((await adminCall(e,path,write(cookie,body,'DELETE'))).status,200,'lost response can be retried safely');
  assert.equal((await adminCall(e,path,write(cookie,{...body,confirmation:'someone-else'},'DELETE'))).status,404);
  assert.equal((await adminCall(e,'/api/admin/students',write(cookie,example))).status,409,'address cannot be reused');
  assert.doesNotMatch(JSON.stringify([...await directory.storage.list({prefix:'deleted-'})]),/Testperson|private@example|fictional-test|passwordCredential/);
  for(const [route,method]of [['/learning-import','POST'],['/automation/publish','POST'],['/assessment','PUT'],['/'+feedback.id,'PUT'],['/quiz/answer','POST'],['/automation/context','GET']]){
    assert.equal((await store.fetch(new Request('https://feedback.internal'+route,{method,...(method!=='GET'?{body:'{}'}:{})}))).status,410);
  }
  const rows=[['','Course Name','Learner/Group Name','Name','Ends On'],['FALSE','English','Morgan Testperson','Morgan Testperson','']];
  const imported=await adminCall(e,'/api/admin/import',write(cookie,{rows}));assert.equal(imported.status,200);assert.equal((await imported.json()).imported,0,'spreadsheet cannot resurrect a deleted account');
});

test('failed deletion closes access, blocks edits, stays visible as paused, and safely resumes cleanup',async()=>{
  const {e,directory}=environment(),cookie=await access(e),saved=(await list(e,cookie)).find(s=>s.studentId==='ab26');
  const store=e.FEEDBACK_STORE.get('ab26'),original=store.storage.delete;let fail=true;
  await store.storage.put({'feedback:one':feedback});store.storage.delete=async key=>{if(fail)throw Error('Fictional storage outage');return original(key);};
  const path='/api/admin/students/'+saved.key,body={revision:saved.revision,confirmation:'ab26'};
  const first=await adminCall(e,path,write(cookie,body,'DELETE'));assert.equal(first.status,503);assert.equal((await first.json()).deletionPending,true);
  const pending=(await list(e,cookie)).find(s=>s.key===saved.key);assert.equal(pending.status,'paused');assert.equal(pending.deletionPending,true);
  assert.equal((await directory.fetch(new Request('https://directory.internal/account/ab26'))).status,404);
  assert.equal((await directory.fetch(new Request('https://directory.internal/integration-account/ab26'))).status,404);
  assert.equal((await adminCall(e,path,write(cookie,{...pending,lastName:'Brown'},'PUT'))).status,409);
  assert.equal((await adminCall(e,path+'/login-details',write(cookie,{revision:pending.revision,password:'student-test'},'PUT'))).status,409);
  assert.equal((await adminCall(e,path+'/login-details',{headers:{Cookie:cookie}})).status,404);
  assert.equal((await directoryStudents(e)).students.ab26,undefined);
  fail=false;assert.equal((await adminCall(e,path,write(cookie,body,'DELETE'))).status,200);assert.deepEqual([...await store.storage.list()],[['account:deleted',true]]);
});

test('drafts without an address require their name and can be removed without accessing learning storage',async()=>{
  const {e}=environment(),cookie=await access(e);const saved=(await (await adminCall(e,'/api/admin/students',write(cookie,{...example,studentId:'',status:'draft',zoomNames:[]}))).json()).student;
  e.FEEDBACK_STORE.get=()=>{throw Error('Draft has no learning store');};
  assert.equal((await adminCall(e,'/api/admin/students/'+saved.key,write(cookie,{revision:saved.revision,confirmation:'Morgan Testperson'},'DELETE'))).status,200);
});

test('queued publishing cannot restore records after deletion begins',async()=>{
  const e=baseEnv(),store=e.FEEDBACK_STORE.get('fictional'),original=store.storage.transaction;
  let release,entered;const waiting=new Promise(r=>entered=r);let hold=true;
  store.storage.transaction=async fn=>{if(hold){hold=false;entered();await new Promise(r=>release=r);}return original(fn);};
  const publish=store.fetch(new Request('https://feedback.internal/'+feedback.id,{method:'PUT',body:JSON.stringify(feedback)}));
  await waiting;assert.equal((await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}))).status,200);
  release();assert.equal((await publish).status,410);assert.deepEqual([...await store.storage.list()],[['account:deleted',true]]);
});

test('delete window requires typed confirmation, cancels without requests, prevents double submission, and clears after success',async()=>{
  let deletes=0,resolveDelete;
  const dom=browser((path,opts)=>{if(opts?.method==='DELETE'){deletes++;assert.equal(path,'/api/admin/students/'+fixture.key);assert.deepEqual(JSON.parse(opts.body),{revision:1,confirmation:'MT26'});return new Promise(r=>resolveDelete=r);}});
  await flush();const w=dom.window,d=w.document,$=id=>d.getElementById(id);d.querySelector('.student-name').click();await flush();
  $('open-delete').click();assert.equal($('delete-dialog').open,true);assert.match($('delete-student-name').textContent,/Morgan Testperson/);assert.equal($('confirm-delete').disabled,true);
  $('delete-form').dispatchEvent(new w.Event('submit',{cancelable:true}));assert.equal(deletes,0);
  $('cancel-delete').click();assert.equal($('delete-dialog').open,false);assert.equal(deletes,0);
  $('open-delete').click();$('delete-dialog').dispatchEvent(new w.Event('cancel',{cancelable:true}));assert.equal($('delete-dialog').open,false);
  $('open-delete').click();$('delete-confirmation').value='wrong';$('delete-confirmation').dispatchEvent(new w.Event('input'));assert.equal($('confirm-delete').disabled,true);
  $('delete-confirmation').value='MT26';$('delete-confirmation').dispatchEvent(new w.Event('input'));assert.equal($('confirm-delete').disabled,false);
  $('confirm-delete').click();$('delete-form').dispatchEvent(new w.Event('submit',{cancelable:true}));assert.equal(deletes,1);assert.equal($('cancel-delete').disabled,true);
  resolveDelete(Response.json({deleted:true}));await flush();assert.equal($('delete-dialog').open,false);assert.equal($('delete-confirmation').value,'');assert.equal($('delete-student-name').textContent,'');assert.equal(d.querySelectorAll('.student-name').length,0);assert.match($('message').textContent,/deleted/);
  w.location.hash='#register';await flush();assert.equal($('delete-account-panel').hidden,true);w.close();
});

test('unfinished deletion can be retried, and session expiry clears the confirmation window',async()=>{
  let tries=0;const dom=browser((path,opts)=>opts?.method==='DELETE'?Response.json(++tries===1?{error:'Cleanup not finished. Retry.',deletionPending:true}:{error:'Please sign in.'},{status:tries===1?503:401}):undefined);
  await flush();const w=dom.window,d=w.document,$=id=>d.getElementById(id);d.querySelector('.student-name').click();await flush();$('open-delete').click();
  $('delete-confirmation').value='mt26';$('delete-confirmation').dispatchEvent(new w.Event('input'));$('confirm-delete').click();await flush();
  assert.match($('delete-error').textContent,/Retry/);assert.equal($('save-student').disabled,true);assert.equal($('confirm-delete').disabled,false);assert.equal($('status').value,'paused');
  $('confirm-delete').click();await flush();assert.equal(tries,2);assert.equal($('delete-dialog').open,false);assert.equal($('delete-student-name').textContent,'');assert.equal($('delete-confirmation').value,'');assert.equal($('admin-view').hidden,true);w.close();
});

test('quiz results open from the private administrator account and clear for new accounts and sign-out', async () => {
  const dom=browser(); await flush(); const w=dom.window,d=w.document;
  d.querySelector('.student-name').click(); await flush();
  assert.equal(d.getElementById('open-quiz-results').hidden,false);
  assert.equal(d.getElementById('open-quiz-results').href,'https://mt26.englishladder.com/#quiz-results');
  w.location.hash='#register'; await flush();
  assert.equal(d.getElementById('open-quiz-results').hidden,true);
  assert.equal(d.getElementById('open-quiz-results').hasAttribute('href'),false);
  w.location.hash='#students/'+fixture.key; await flush();
  d.getElementById('sign-out').click(); await flush();
  assert.equal(d.getElementById('open-quiz-results').hasAttribute('href'),false);
  dom.window.close();
});


test('CEFR overview and evidence require the admin host session and isolate student records',async()=>{
  const {e}=environment(),cookie=await access(e),records=await list(e,cookie),account=records.find(s=>s.studentId==='ab26');
  const cefr={state:'estimated',lower:'B1',upper:'B2',confidence:'low',assessedOn:'2026-10-14',latestSessionId:feedback.id,sourceSessions:[feedback.id],rationale:'Private language evidence',evidence:[{quote:'Private learner quote'}],aspects:[]};
  await e.FEEDBACK_STORE.get('ab26').storage.put({'cefr:current':cefr});
  const paths=['/api/admin/cefr-status','/api/admin/students/'+account.key+'/cefr'];
  for(const path of paths){
    const response=await adminCall(e,path,{headers:{Cookie:cookie}});assert.equal(response.status,200);assert.equal(response.headers.get('Cache-Control'),'no-store');
    assert.equal((await adminCall(e,path)).status,401);
    for(const password of ['student-test','teacher-test']){
      const other=await login(e,password);assert.equal((await adminCall(e,path,{headers:{Cookie:other.cookie}})).status,401);
      assert.equal((await call(e,path,{headers:{Cookie:other.cookie}})).status,404);
    }
  }
  const result=await(await adminCall(e,paths[0],{headers:{Cookie:cookie}})).json();
  assert.equal(result.statuses[account.key].lower,'B1');assert.equal(result.statuses[records.find(s=>s.studentId==='cd26').key].state,'pending');
  assert.doesNotMatch(JSON.stringify(result),/quote|rationale|Private/);
  assert.deepEqual((await(await adminCall(e,paths[1],{headers:{Cookie:cookie}})).json()).cefr,cefr);
  assert.equal((await adminCall(e,paths[1],{headers:{Cookie:cookie,Origin:origin}})).status,403);
  assert.equal((await adminCall(e,'/api/admin/students/00000000-0000-4000-8000-000000000000/cefr',{headers:{Cookie:cookie}})).status,404);
  assert.equal((await adminCall(e,'/api/admin/cefr-status?after=invalid',{headers:{Cookie:cookie}})).status,400);
});

test('CEFR details render safely, clear on navigation and logout, and ignore delayed responses',async()=>{
  const cefr={state:'estimated',lower:'B1',upper:'B2',confidence:'low',assessedOn:'2026-10-14',latestSessionId:feedback.id,sourceSessions:[feedback.id],rationale:'A provisional estimate.',aspects:[{area:'range',detail:'Uses connected explanations.'}],evidence:[{sessionId:feedback.id,at:'00:02:00',quote:'<img src=x onerror=alert(1)>',note:'Learner evidence.'}]};
  let resolveDetail;
  const dom=browser(path=>path==='/api/admin/cefr-status'?Response.json({statuses:{[fixture.key]:cefr},nextCursor:null}):path.endsWith('/cefr')?new Promise(resolve=>{resolveDetail=resolve;}):null);
  await flush();const w=dom.window,d=w.document;assert.match(d.querySelector('.cefr-cell').textContent,/B1–B2/);
  d.querySelector('.student-name').click();await flush();resolveDetail(Response.json({cefr,schedule:{nextReviewOn:'2026-11-14',lastReviewState:'insufficient'}}));await flush();
  assert.match(d.getElementById('cefr-content').textContent,/Low confidence/);assert.equal(d.querySelector('#cefr-content img'),null);
  assert.match(d.getElementById('cefr-content').textContent,/after two recorded sessions/);
  assert.match(d.getElementById('cefr-content').textContent,/Nov 14, 2026/);
  assert.match(d.getElementById('cefr-content').textContent,/earlier estimate is retained/);
  assert.match(d.getElementById('cefr-content').textContent,/<img/);
  w.location.hash='#students';await flush();assert.equal(d.getElementById('cefr-content').textContent,'');
  d.querySelector('.student-name').click();await flush();w.location.hash='#register';await flush();resolveDetail(Response.json({cefr}));await flush();assert.equal(d.getElementById('cefr-content').textContent,'');
  w.location.hash='#students/'+fixture.key;await flush();resolveDetail(Response.json({cefr}));await flush();d.getElementById('sign-out').click();await flush();
  assert.equal(d.getElementById('cefr-content').textContent,'');assert.equal(d.getElementById('cefr-panel').hidden,true);assert.equal(d.getElementById('student-rows').textContent,'');w.close();
});

test('CEFR overview distinguishes missing evidence from failures and clears after session expiry',async()=>{
  let state={state:'pending'},fail=false,expire=false;
  const dom=browser(path=>path==='/api/admin/cefr-status'?(fail?Response.json({error:'Unavailable'},{status:503}):Response.json({statuses:{[fixture.key]:state},nextCursor:null})):path.endsWith('/cefr')?(expire?Response.json({error:'Expired'},{status:401}):Response.json({cefr:null})):null);
  await flush();const d=dom.window.document;assert.match(d.querySelector('.cefr-cell').textContent,/Not assessed yet/);
  state={state:'insufficient'};d.getElementById('refresh').click();await flush();assert.match(d.querySelector('.cefr-cell').textContent,/More evidence needed/);
  fail=true;d.getElementById('refresh').click();await flush();assert.match(d.querySelector('.cefr-cell').textContent,/Unable to check/);
  d.querySelector('.student-name').click();await flush();assert.match(d.getElementById('cefr-content').textContent,/next eligible nightly/);
  dom.window.location.hash='#students';await flush();expire=true;d.querySelector('.student-name').click();await flush();
  assert.equal(d.getElementById('admin-view').hidden,true);assert.equal(d.getElementById('cefr-content').textContent,'');dom.window.close();
});

const selfWrite = (cookie, body, method = 'PUT') => ({ method, headers: { Cookie: cookie, Origin: origin, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
const selfProfile = async (e, cookie) => (await call(e, '/api/account', { headers: { Cookie: cookie } })).json();
test('only the administrator changes activity selections; nickname edits preserve them and learning progress', async () => {
  const { e, directory } = environment(), student = await login(e), teacher = await login(e, 'teacher-test'), adminCookie = await access(e);
  assert.equal((await call(e, '/api/account')).status, 401);
  const initial = await selfProfile(e, student.cookie);
  assert.deepEqual(initial.visibleActivities, ACTIVITY_TOOLS.map(a => a.id));
  assert.deepEqual(Object.keys(initial).sort(), ['activities', 'nickname', 'revision', 'visibleActivities']);
  for (const visibleActivities of [[], ['english-road'], ['unknown'], 'all']) {
    assert.equal((await call(e, '/api/account', selfWrite(student.cookie, { revision: initial.revision, nickname: 'Blocked', visibleActivities }))).status, 403);
  }
  const direct = await directory.selfAccount('ab26', { ...initial, expectedAccountRevision: initial.revision, nickname: 'Blocked' });
  assert.equal(direct.status, 403);
  const response = await call(e, '/api/account', selfWrite(student.cookie, { revision: initial.revision, nickname: 'New nickname', studentId: 'cd26', status: 'paused', firstName: 'Changed', newPassword: 'injected-test' }));
  assert.equal(response.status, 200);
  const saved = await response.json(); assert.deepEqual(saved.visibleActivities, initial.visibleActivities);
  const session = await (await call(e, '/api/session', { headers: { Cookie: student.cookie } })).json();
  assert.equal(session.student.nickname, 'New nickname'); assert.equal(session.student.name, 'Alex');
  const record = (await list(e, adminCookie)).find(s => s.studentId === 'ab26');
  const storage = e.FEEDBACK_STORE.get('ab26').storage;
  await storage.put({ 'road:sample-history': { answers: [1, 0] }, 'terms:item:1': { finished: true, questions: true } });
  const learningBefore = await storage.list({ limit: 100 });
  const edited = await adminCall(e, '/api/admin/students/' + record.key, write(adminCookie, { ...record, lastName: 'Brown', visibleActivities: ['grammar-practice'] }, 'PUT'));
  assert.equal(edited.status, 200);
  assert.deepEqual((await selfProfile(e, student.cookie)).visibleActivities, ['grammar-practice']);
  let updated = (await edited.json()).student;
  assert.deepEqual(updated.visibleActivities, ['grammar-practice']);
  const { visibleActivities, ...unrelated } = updated;
  const courseEdit = await adminCall(e, '/api/admin/students/' + updated.key, write(adminCookie, { ...unrelated, course: 'Updated course' }, 'PUT'));
  assert.equal(courseEdit.status, 200); updated = (await courseEdit.json()).student;
  assert.deepEqual(updated.visibleActivities, ['grammar-practice']);
  const empty = await adminCall(e, '/api/admin/students/' + updated.key, write(adminCookie, { ...updated, visibleActivities: [] }, 'PUT'));
  assert.equal(empty.status, 200); assert.deepEqual((await selfProfile(e, student.cookie)).visibleActivities, []);
  assert.deepEqual(await storage.list({ limit: 100 }), learningBefore);
  const another = await login(e, 'other-test', 'https://cd26.englishladder.com');
  const other = await (await call(e, '/api/account', { headers: { Cookie: another.cookie } }, 'https://cd26.englishladder.com')).json();
  assert.equal(other.nickname, 'Casey'); assert.equal(other.visibleActivities.length, ACTIVITY_TOOLS.length);
  assert.equal((await call(e, '/api/account', selfWrite(student.cookie, { revision: saved.revision, nickname: 'Stale' }))).status, 409);
  assert.equal((await call(e, '/api/account', selfWrite(teacher.cookie, { revision: saved.revision, nickname: 'Blocked' }))).status, 403);
  for (const path of ['/self/ab26', '/api/self/ab26', '/api/account/cd26']) assert.equal((await call(e, path, { headers: { Cookie: student.cookie } })).status, 404);
});

test('administrator activity saves reject invalid selections, stale records and untrusted callers', async () => {
  const { e } = environment(), cookie = await access(e), student = await login(e), teacher = await login(e, 'teacher-test');
  const record = (await list(e, cookie)).find(s => s.studentId === 'ab26'), path = '/api/admin/students/' + record.key;
  const input = { ...record, lastName: 'Brown', visibleActivities: ['grammar-practice'] };
  for (const caller of ['', student.cookie, teacher.cookie]) assert.equal((await adminCall(e, path, write(caller, input, 'PUT'))).status, 401);
  const foreign = write(cookie, input, 'PUT'); foreign.headers.Origin = origin;
  assert.equal((await adminCall(e, path, foreign)).status, 403);
  assert.equal((await call(e, path, selfWrite(teacher.cookie, input))).status, 405);
  for (const visibleActivities of [['unknown'], ['grammar-practice', 'grammar-practice'], 'all', null]) {
    assert.equal((await adminCall(e, path, write(cookie, { ...input, visibleActivities }, 'PUT'))).status, 400);
  }
  const saves = await Promise.all([adminCall(e, path, write(cookie, input, 'PUT')), adminCall(e, path, write(cookie, { ...input, visibleActivities: [] }, 'PUT'))]);
  assert.deepEqual(saves.map(r => r.status).sort(), [200, 409]);
  const fresh = await adminCall(e, '/api/admin/students', write(cookie, { ...example, visibleActivities: ['business-terms'] }));
  assert.equal(fresh.status, 201); assert.deepEqual((await fresh.json()).student.visibleActivities, ['business-terms']);
});

test('student nickname settings reject foreign origins, cookies, invalid input and limits', async () => {
  const { e } = environment(), student = await login(e), profile = await selfProfile(e, student.cookie);
  const initial = { revision: profile.revision, nickname: profile.nickname };
  for (const fake of [null, 'https://cd26.englishladder.com', 'https://evil.test']) {
    const options = selfWrite(student.cookie, initial); if (fake) options.headers.Origin = fake; else delete options.headers.Origin;
    assert.equal((await call(e, '/api/account', options)).status, 403);
  }
  assert.equal((await call(e, '/api/account', { headers: { Cookie: student.cookie } }, 'https://cd26.englishladder.com')).status, 401);
  for (const changes of [{ nickname: '' }, { nickname: 'x'.repeat(101) }, { nickname: 'Two\nlines' }, { revision: null }]) {
    assert.equal((await call(e, '/api/account', selfWrite(student.cookie, { ...initial, ...changes }))).status, 400);
  }
  assert.equal((await call(e, '/api/account', selfWrite(student.cookie, { ...initial, extra: 'x'.repeat(5000) }))).status, 400);
  for (const binding of ['LOGIN_LIMITER', 'ACCOUNT_LIMITER']) {
    const old = e[binding]; e[binding] = { limit: async () => ({ success: false }) };
    assert.equal((await call(e, '/api/account', selfWrite(student.cookie, initial))).status, 429); e[binding] = old;
  }
  assert.equal((await selfProfile(e, student.cookie)).revision, initial.revision);
});

test('own-password change requires current password and revokes only student sessions with recoverable updated copy', async () => {
  const { e } = environment(), student = await login(e), teacher = await login(e, 'teacher-test'), adminCookie = await access(e);
  const other = await login(e, 'other-test', 'https://cd26.englishladder.com'), initial = await selfProfile(e, student.cookie);
  const body = { revision: initial.revision, currentPassword: 'STUDENT-TEST', newPassword: 'New-Test-Password', confirmPassword: 'new-test-password' };
  for (const changes of [{ currentPassword: 'wrong' }, { currentPassword: 'teacher-test' }, { newPassword: '' }, { newPassword: 'short', confirmPassword: 'short' }, { confirmPassword: 'different' }, { newPassword: 'teacher-test', confirmPassword: 'teacher-test' }]) {
    assert.equal((await call(e, '/api/account/password', selfWrite(student.cookie, { ...body, ...changes }, 'POST'))).status, 400);
  }
  assert.equal((await call(e, '/api/account/password', selfWrite(teacher.cookie, body, 'POST'))).status, 403);
  const options = selfWrite(student.cookie, body, 'POST'); options.headers.Origin = 'https://cd26.englishladder.com';
  assert.equal((await call(e, '/api/account/password', options)).status, 403);
  const limiter = e.ACCOUNT_LIMITER; e.ACCOUNT_LIMITER = { limit: async () => ({ success: false }) };
  assert.equal((await call(e, '/api/account/password', selfWrite(student.cookie, body, 'POST'))).status, 429); e.ACCOUNT_LIMITER = limiter;
  const result = await call(e, '/api/account/password', selfWrite(student.cookie, body, 'POST'));
  assert.equal(result.status, 200); assert.deepEqual(await result.json(), { saved: true }); assert.match(result.headers.get('set-cookie'), /Max-Age=0/);
  assert.equal((await call(e, '/api/session', { headers: { Cookie: student.cookie } })).status, 401);
  assert.equal((await call(e, '/api/session', { headers: { Cookie: teacher.cookie } })).status, 200);
  assert.equal((await call(e, '/api/session', { headers: { Cookie: other.cookie } }, 'https://cd26.englishladder.com')).status, 200);
  assert.equal((await call(e, '/api/login', selfWrite('', { password: 'student-test' }, 'POST'))).status, 401);
  const fresh = await login(e, 'NEW-TEST-PASSWORD'); assert.equal(fresh.response.status, 200);
  const row = (await list(e, adminCookie)).find(s => s.studentId === 'ab26');
  const details = await (await adminCall(e, '/api/admin/students/' + row.key + '/login-details', { headers: { Cookie: adminCookie } })).json();
  assert.equal(details.password, 'new-test-password');
  assert.doesNotMatch(JSON.stringify(await selfProfile(e, fresh.cookie)), /password|salt|ciphertext|credential|Brown|AlexZoom/);
  // Exercise the custom-password verification path as well as the original legacy path.
  const next = await selfProfile(e, fresh.cookie);
  assert.equal((await call(e, '/api/account/password', selfWrite(fresh.cookie, { ...body, revision: next.revision, currentPassword: 'new-test-password' }, 'POST'))).status, 200);
  assert.equal((await call(e, '/api/session', { headers: { Cookie: fresh.cookie } })).status, 401);
});

test('account saves recheck authenticated revision, pause and deletion inside the directory', async () => {
  for (const change of ['revision', 'paused', 'deletionPending']) {
    const { e, directory } = environment(), student = await login(e), initial = await selfProfile(e, student.cookie), binding = e.STUDENT_DIRECTORY;
    e.STUDENT_DIRECTORY = { ...binding, get: () => ({ fetch: async request => {
      if (new URL(request.url).pathname === '/self/ab26' && request.method === 'PUT') {
        const row = (await directory.records()).find(r => r.studentId === 'ab26');
        const changed = change === 'revision' ? { revision: row.revision + 1 } : change === 'paused' ? { status: 'paused' } : { deletionPending: true };
        await directory.storage.put({ ['student:' + row.key]: { ...row, ...changed } });
      }
      return directory.fetch(request);
    } }) };
    const response = await call(e, '/api/account', selfWrite(student.cookie, { revision: initial.revision, nickname: 'Must not save' }));
    assert.equal(response.status, change === 'revision' ? 409 : 404);
    assert.notEqual((await directory.records()).find(r => r.studentId === 'ab26').nickname, 'Must not save');
  }
});

test('English Road results are available only on the administrator host and remain isolated by student', async () => {
  const {e}=environment(),adminCookie=await access(e),records=await list(e,adminCookie),student=await login(e),teacher=await login(e,'teacher-test');
  const id=crypto.randomUUID(), record=records.find(s=>s.studentId==='ab26'), other=records.find(s=>s.studentId==='cd26');
  const started=await call(e,'/api/road/start',{method:'POST',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({attemptId:id,previousAttemptId:null,band:'A1',topic:'Articles'})});assert.equal(started.status,201);
  const path='/api/admin/students/'+record.key+'/road';
  for(const cookie of ['',student.cookie,teacher.cookie])assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:teacher.cookie}})).status,404);
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie,Origin:'https://evil.test'}})).status,403);
  const results=await adminCall(e,path,{headers:{Cookie:adminCookie}});assert.equal(results.headers.get('Cache-Control'),'no-store');
  const rows=(await results.json()).attempts;assert.equal(rows.length,1);assert.equal(rows[0].id,id);assert.equal(rows[0].answered,0);
  const detail=await adminCall(e,path+'/'+id,{headers:{Cookie:adminCookie}});assert.equal(detail.status,200);assert.equal((await detail.json()).attempt.questions.length,20);
  const otherPath='/api/admin/students/'+other.key+'/road';
  assert.deepEqual((await(await adminCall(e,otherPath,{headers:{Cookie:adminCookie}})).json()).attempts,[]);
  assert.equal((await adminCall(e,otherPath+'/'+id,{headers:{Cookie:adminCookie}})).status,404);
  await adminCall(e,'/api/admin/students/'+record.key,write(adminCookie,{...record,status:'paused'},'PUT'));
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie}})).status,200);
  assert.equal((await call(e,'/api/road/state',{headers:{Cookie:student.cookie}})).status,404);
});

test('administrator practice panel shows original choices safely and discards late detail after navigation', async () => {
  const id='22222222-2222-4222-8222-222222222222';let resolveDetail;
  const row={id,band:'A1',topic:'Articles',startedAt:'2026-10-15T10:00:00Z',completedAt:null,endedAt:null,answered:1,total:20,correct:0};
  const dom=browser(path=>path==='/api/admin/students/'+fixture.key+'/road'?Response.json({attempts:[row],nextCursor:null}):path.endsWith('/road/'+id)?new Promise(r=>{resolveDetail=r;}):null);
  const w=dom.window,d=w.document;await flush();w.location.hash='students/'+fixture.key;await flush();
  assert.equal(d.getElementById('road-results-panel').hidden,false);d.getElementById('load-road-results').click();await flush();
  assert.match(d.getElementById('road-results').textContent,/In progress.*0 correct out of 1 answered/);
  const details=d.querySelector('#road-results details');details.open=true;await flush();w.location.hash='students';await flush();
  resolveDetail(Response.json({attempt:{questions:[{setup:'Read this.',prompt:'<img src=x onerror=alert(1)>',topic:'Articles',options:['a','an','the','some'],correctIndex:1,feedback:['Try an.','Correct.','',''],explanation:'Use an.'}],answers:[{choiceIndex:0,answeredAt:row.startedAt}]}}));await flush();
  assert.equal(d.getElementById('road-results').textContent,'');assert.equal(d.querySelector('#road-results img'),null);dom.window.close();
});

test('Business terms Questions list is private to the administrator and selected student, including paused accounts',async()=>{
  const {e}=environment(),adminCookie=await access(e),records=await list(e,adminCookie),student=await login(e),teacher=await login(e,'teacher-test');
  const record=records.find(s=>s.studentId==='ab26'),other=records.find(s=>s.studentId==='cd26');
  const saved=await call(e,'/api/business-terms/state',{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({number:1,field:'question',value:true,revision:0})});assert.equal(saved.status,200);
  const path='/api/admin/students/'+record.key+'/business-terms';
  for(const cookie of ['',student.cookie,teacher.cookie])assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:teacher.cookie}})).status,404);
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie,Origin:'https://evil.test'}})).status,403);
  const response=await adminCall(e,path,{headers:{Cookie:adminCookie}});assert.equal(response.headers.get('Cache-Control'),'no-store');
  const {questions}=await response.json();assert.equal(questions.length,1);assert.equal(questions[0].number,1);assert.equal(questions[0].progress.question,true);assert.deepEqual(questions[0].answers,termsBank.items[0].answers);
  assert.deepEqual((await(await adminCall(e,'/api/admin/students/'+other.key+'/business-terms',{headers:{Cookie:adminCookie}})).json()).questions,[]);
  await adminCall(e,'/api/admin/students/'+record.key,write(adminCookie,{...record,status:'paused'},'PUT'));
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie}})).status,200);assert.equal((await call(e,'/api/business-terms/state',{headers:{Cookie:student.cookie}})).status,404);
});

test('administrator Questions list reveals answer terms safely, refreshes, and clears late responses',async()=>{
  let delayed=false,resolve;const content={questions:[{...termsBank.items[0],progress:{finished:true}}]};
  const dom=browser(path=>path.endsWith('/business-terms')?(delayed?new Promise(r=>{resolve=r;}):Response.json(content)):null);
  const w=dom.window,d=w.document;await flush();w.location.hash='students/'+fixture.key;await flush();
  d.getElementById('load-terms-questions').click();await flush();
  assert.match(d.getElementById('terms-questions-content').textContent,/Item 1.*Finished/);
  assert(d.querySelector('#terms-questions-content .terms-item').classList.contains('is-finished'));
  d.querySelector('#terms-questions-content [type=checkbox]').click();assert.equal(d.querySelectorAll('#terms-questions-content .terms-answer').length,6);
  delayed=true;d.getElementById('load-terms-questions').click();await flush();w.location.hash='students';await flush();resolve(Response.json(content));await flush();
  assert.equal(d.getElementById('terms-questions-content').textContent,'');assert.equal(d.getElementById('terms-questions-panel').hidden,true);w.close();
});

test('Grammar Questions list is private to the administrator and selected student, including paused accounts',async()=>{
  const {e}=environment(),adminCookie=await access(e),records=await list(e,adminCookie),student=await login(e),teacher=await login(e,'teacher-test');
  const record=records.find(s=>s.studentId==='ab26'),other=records.find(s=>s.studentId==='cd26');
  const saved=await call(e,'/api/grammar-practice/state',{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({number:1,field:'question',value:true,revision:0})});assert.equal(saved.status,200);
  const path='/api/admin/students/'+record.key+'/grammar-practice';
  for(const cookie of ['',student.cookie,teacher.cookie])assert.equal((await adminCall(e,path,{headers:{Cookie:cookie}})).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:teacher.cookie}})).status,404);
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie,Origin:'https://evil.test'}})).status,403);
  const response=await adminCall(e,path,{headers:{Cookie:adminCookie}});assert.equal(response.headers.get('Cache-Control'),'no-store');
  const {questions}=await response.json();assert.equal(questions.length,1);assert.equal(questions[0].number,1);assert.equal(questions[0].progress.question,true);assert.deepEqual(questions[0].answer,grammarBank.items[0].answer);
  assert.deepEqual((await(await adminCall(e,'/api/admin/students/'+other.key+'/grammar-practice',{headers:{Cookie:adminCookie}})).json()).questions,[]);
  await adminCall(e,'/api/admin/students/'+record.key,write(adminCookie,{...record,status:'paused'},'PUT'));
  assert.equal((await adminCall(e,path,{headers:{Cookie:adminCookie}})).status,200);assert.equal((await call(e,'/api/grammar-practice/state',{headers:{Cookie:student.cookie}})).status,404);
});

test('administrator grammar Questions list reveals sentences safely, refreshes, and clears late responses',async()=>{
  let delayed=false,resolve;const content={questions:[{...grammarBank.items[0],progress:{finished:true}}]};
  const dom=browser(path=>path.endsWith('/grammar-practice')?(delayed?new Promise(r=>{resolve=r;}):Response.json(content)):null);
  const w=dom.window,d=w.document;await flush();w.location.hash='students/'+fixture.key;await flush();
  d.getElementById('load-grammar-questions').click();await flush();
  assert.match(d.getElementById('grammar-questions-content').textContent,/Item 1[\s\S]*Finished/);
  assert(d.querySelector('#grammar-questions-content .grammar-item').classList.contains('is-finished'));
  d.querySelector('#grammar-questions-content [type=checkbox]').click();assert.equal(d.querySelector('#grammar-questions-content .grammar-prompt.is-revealed q').textContent,'Tom is much more intelligent than Mike.');
  delayed=true;d.getElementById('load-grammar-questions').click();await flush();w.location.hash='students';await flush();resolve(Response.json(content));await flush();
  assert.equal(d.getElementById('grammar-questions-content').textContent,'');assert.equal(d.getElementById('grammar-questions-panel').hidden,true);w.close();
});
