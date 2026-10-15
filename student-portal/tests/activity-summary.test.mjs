import test from 'node:test';
import assert from 'node:assert/strict';
import {env} from './harness.mjs';

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
