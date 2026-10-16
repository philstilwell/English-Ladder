import test from 'node:test';
import assert from 'node:assert/strict';
import {env, call, login, origin} from './harness.mjs';

test('students and teacher previews read only their own activity totals without writing or receiving administrator details',async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');
  const storage=e.FEEDBACK_STORE.get('ab26').storage;
  await storage.put({
    'grammar:item:1':{number:1,finished:true,question:true,revision:1,updatedAt:'2026-10-15T10:00:00Z'},
    'vocabulary:item:1':{number:1,finished:true,question:true,answer:'Private answer',sentence:'Private sentence',revision:1},
    'road:index:one':{answered:5,correct:3,total:20,band:'A2',topic:'Articles',updatedAt:'2026-10-15T10:00:00Z'},
  });
  const before=await storage.list();
  for(const user of [student,teacher]){
    const response=await call(e,'/api/activities/progress',{headers:{Cookie:user.cookie}});
    assert.equal(response.status,200);assert.equal(response.headers.get('Cache-Control'),'no-store');
    const data=await response.json();
    assert.deepEqual(data.activities[0],{id:'english-road',setsStarted:1,setsCompleted:0,answered:5,questions:0,currentSet:{answered:5,total:20}});
    assert.deepEqual(data.activities[1],{id:'grammar-practice',total:900,finished:1,questions:1});
    assert.deepEqual(data.activities[3],{id:'vocabulary-practice',total:50,finished:1,questions:1});
    assert.doesNotMatch(JSON.stringify(data),/Private|updatedAt|lastActivityAt|savedPlace|topic|band|2026/);
  }
  const other=await login(e,'other-test','https://cd26.englishladder.com');
  const data=await(await call(e,'/api/activities/progress',{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json();
  assert(data.activities.every(row=>(row.finished??row.answered)===0));
  assert.deepEqual(await storage.list(),before);
});

test('activity progress rejects unauthenticated, cross-account, cross-origin, write and deleted-account requests',async()=>{
  const e=env(),student=await login(e),path='/api/activities/progress';
  assert.equal((await call(e,path)).status,401);
  assert.equal((await call(e,path,{headers:{Cookie:student.cookie}},'https://cd26.englishladder.com')).status,401);
  for(const headers of [{Origin:'https://other.test'},{'Sec-Fetch-Site':'cross-site'}])
    assert.equal((await call(e,path,{headers:{Cookie:student.cookie,...headers}})).status,403);
  for(const method of ['POST','PATCH','PUT','DELETE'])
    assert.equal((await call(e,path,{method,headers:{Cookie:student.cookie,Origin:origin}})).status,405);
  await e.FEEDBACK_STORE.get('ab26').fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await call(e,path,{headers:{Cookie:student.cookie}})).status,410);
});

test('activity summaries count all storage pages and keep latest changes even when selections are undone',async()=>{
  const store=env().FEEDBACK_STORE.get('ab26'),storage=store.storage;
  const saved={};
  for(let n=1;n<=600;n++){
    saved['grammar:item:'+n]={number:n,finished:true,question:n<4,updatedAt:'2026-10-14T10:00:00Z'};
    saved['road:index:'+String(n).padStart(4,'0')]={band:'A1',topic:'Articles',answered:20,correct:15,total:20,completedAt:'2026-10-14T10:00:00Z',updatedAt:'2026-10-14T10:00:00Z'};
  }
  saved['grammar:item:1']={number:1,finished:false,question:false,updatedAt:'2026-10-15T10:00:00Z'};
  saved['grammar:item:99999']={number:99999,finished:true,question:true,updatedAt:'2026-10-20T10:00:00Z'};
  saved['grammar:position']={number:21,updatedAt:'2026-10-15T11:00:00Z'};
  saved['terms:preferences']={hideFinished:true,updatedAt:'2026-10-15T12:00:00Z'};
  saved['road:index:0001'].updatedAt='2026-10-15T13:00:00Z';
  await storage.put(saved);const before=await storage.list();
  const data=await(await store.fetch(new Request('https://feedback.internal/admin/activity-summary'))).json();
  assert.deepEqual([data.activities[0].setsStarted,data.activities[0].setsCompleted,data.activities[0].answered,data.activities[0].correct],[600,600,12000,9000]);
  assert.equal(data.activities[0].lastActivityAt,'2026-10-15T13:00:00Z');
  assert.deepEqual([data.activities[1].finished,data.activities[1].questions,data.activities[1].savedPlace],[599,2,21]);
  assert.equal(data.activities[1].lastActivityAt,'2026-10-15T11:00:00Z');
  assert.equal(data.activities[2].lastActivityAt,'2026-10-15T12:00:00Z');
  assert.deepEqual(await storage.list(),before);
});
