import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';
import worker from '../worker.mjs';
import { StudentDirectory, directoryStudents, parseStudentRows, inspectStudentRows, validateStudent } from '../student-directory.mjs';
import { QuizAutomation } from '../server-quiz-automation.mjs';
import { env as baseEnv, login, call, origin } from './harness.mjs';
import { assessment, quiz } from './fixture.mjs';

const admin = 'https://phil.englishladder.com';
const example = { firstName:'Morgan', lastName:'Testperson', nickname:'Morgan the Explorer', studentId:'mt26', status:'active', zoomNames:['Morgan-Zoom'], timeZone:'Asia/Tokyo', email:'private@example.test', notes:'Private administrative note', hoursAuthorized:40 };
function memory() {
  const data=new Map();let queue=Promise.resolve();
  const store={get:async k=>structuredClone(data.get(k)),put:async values=>{for(const[k,v]of Object.entries(values))data.set(k,structuredClone(v));},delete:async k=>data.delete(k),list:async({prefix})=>new Map([...data].filter(([k])=>k.startsWith(prefix)).map(([k,v])=>[k,structuredClone(v)])),
    transaction(fn){const run=queue.then(async()=>{const prior=structuredClone(data);try{return await fn(store);}catch(e){data.clear();for(const[k,v]of prior)data.set(k,v);throw e;}});queue=run.catch(()=>{});return run;}};
  return store;
}
function environment() {
  const e={...baseEnv(),STUDENT_PASSWORD:'default-test-only',STUDENT_PASSWORD_PEPPER:'fictional-pepper-for-password-tests-only',QUIZ_STUDENTS:JSON.stringify({ab26:{firstName:'Alex',zoomNames:['AlexZoom'],timeZone:'America/New_York',startAfter:'2026-10-14T00:00:00Z'}})};
  const directory=new StudentDirectory({storage:memory()},e);
  e.STUDENT_DIRECTORY={idFromName:id=>id,get:()=>directory};
  return {e,directory};
}
const adminCall=(e,path,options={})=>call(e,path,options,admin);
async function access(e){return (await login(e,'teacher-test',admin)).cookie;}
const write=(cookie,body,method='POST')=>({method,headers:{Cookie:cookie,Origin:admin,'Content-Type':'application/json'},body:JSON.stringify(body)});
async function list(e,cookie){return (await (await adminCall(e,'/api/admin/students',{headers:{Cookie:cookie}})).json()).students;}

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
const fixture={...example,key:'11111111-1111-4111-8111-111111111111',revision:1,activated:true,startAfter:'2026-10-14T12:00:00Z'};
const flush=async()=>{for(let i=0;i<12;i++)await new Promise(r=>setTimeout(r,1));};
function browser(custom){const dom=new JSDOM(html,{url:admin+'/#students',runScripts:'outside-only',pretendToBeVisual:true});dom.window.fetch=async(path,opts)=>{
  const result=custom?.(path,opts);if(result)return result;
  return Response.json(path==='/api/session'?{administrator:true}:path==='/api/admin/students'?{students:[fixture]}:path==='/api/admin/quiz-status'?{statuses:{[fixture.key]:{state:'not_started',title:'Practice',total:2}},nextCursor:null}:path==='/api/admin/automation'?{enabled:true,connected:true}:{});
};dom.window.eval(script);return dom;}
test('administrator list links to editable accounts and has a separate registration form',async()=>{
  const dom=browser();await flush();const w=dom.window,d=w.document;
  assert.match(d.getElementById('student-rows').textContent,/Morgan Testperson/);
  d.querySelector('.student-name').click();await flush();assert.equal(d.getElementById('lastName').value,'Testperson');assert.equal(d.getElementById('studentId').readOnly,true);
  w.location.hash='#register';await flush();assert.equal(d.getElementById('edit-title').textContent,'Register new student');assert.equal(d.getElementById('lastName').value,'');assert.equal(d.getElementById('studentId').readOnly,false);
  assert.equal(d.querySelectorAll('input[type="password"]').length,3);assert.doesNotMatch(script,/localStorage|sessionStorage|innerHTML/);dom.window.close();
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
  let expired=false;const dom=browser(path=>path==='/api/admin/students'?(expired?Response.json({error:'Expired'},{status:401}):Response.json({students:[{...fixture,firstName:'<img src=x onerror=alert(1)>'}]})):null);await flush();const d=dom.window.document;
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
