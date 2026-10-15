import test from 'node:test';
import assert from 'node:assert/strict';
import bank from '../business-terms-bank.json' with { type: 'json' };
import { env, call, login, origin } from './harness.mjs';
import { ACTIVITY_TOOLS, visibleActivities, validateActivities } from '../activities.mjs';

test('business terms preserve the complete source exercises and exclude three incomplete keys', () => {
  assert.equal(bank.source.total, 2961); assert.equal(bank.items.length, 2958);
  assert.deepEqual(bank.withheld.map(i => i.number), [18, 155, 1563]);
  const numbers = [...bank.items, ...bank.withheld].map(i => i.number).sort((a,b) => a-b);
  assert.deepEqual(numbers, Array.from({length:2961}, (_,i) => i+1));
  for (const [index, item] of bank.items.entries()) {
    assert.deepEqual(Object.keys(item), ['number', 'term', 'sentences', 'answers', 'options']);
    if(index) assert(item.number > bank.items[index-1].number);
    assert.equal(item.sentences.length, 3); assert.equal(item.answers.length, 6); assert.equal(item.options.length, 6);
    const matches = item.sentences.flatMap(s => [...s.matchAll(/⎛#(\d+)⎞/g)]);
    assert.deepEqual(matches.map(m => Number(m[1])).sort(), [1,2,3,4,5,6]);
    assert(item.answers.every(s => typeof s === 'string' && s.length));
    assert.deepEqual(item.options, [...item.options].sort((a,b) => a.localeCompare(b,'en',{sensitivity:'base'})));
    assert.deepEqual(item.options.map(s=>s.toLowerCase()).sort(), item.answers.map(s=>s.toLowerCase()).sort());
    for(const sentence of item.sentences) assert.doesNotMatch(sentence.replace(/⎛#(\d+)⎞/g, (_,id)=>item.answers[Number(id)-1]), /⎛#|undefined/);
  }
  assert.deepEqual(bank.items[0].answers, ['plates','stack','of','review','featured','novels']);
  assert.equal(bank.items.at(-1).term, 'zoning');
  assert.equal(bank.items.filter(i=>new Set(i.options).size<6).length, 707);
  assert.equal(bank.items.find(i=>i.number===4).options.filter(s=>s==='are').length, 2);
});

test('business terms require a host-bound session, allow teacher self-check and never write history', async () => {
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test');
  assert.equal((await call(e,'/api/business-terms')).status,401);
  assert.equal((await call(e,'/business-terms-bank.json')).status,404);
  assert.equal((await call(e,'/api/business-terms',{headers:{Cookie:student.cookie}},'https://cd26.englishladder.com')).status,401);
  e.FEEDBACK_STORE={get(){throw Error('Self-check must not access saved learning records');}};
  for(const cookie of [student.cookie,teacher.cookie]) {
    const response=await call(e,'/api/business-terms',{headers:{Cookie:cookie}});
    assert.equal(response.status,200);assert.equal(response.headers.get('Cache-Control'),'no-store');
    assert.deepEqual(await response.json(),{items:bank.items});
    for(const method of ['POST','PUT','DELETE']) {
      const response=await call(e,'/api/business-terms',{method,headers:{Cookie:cookie,Origin:origin},body:'{}'});
      assert.equal(response.status,405);assert.equal(response.headers.get('Allow'),'GET');
    }
  }
});

test('business terms visibility preserves all prior explicit activity choices', () => {
  assert(ACTIVITY_TOOLS.some(i=>i.id==='business-terms'));
  assert(visibleActivities({}).includes('business-terms'));
  assert.deepEqual(visibleActivities({visibleActivities:['english-road','grammar-practice']}),['english-road','grammar-practice']);
  assert.deepEqual(visibleActivities({visibleActivities:[]}),[]);
  assert.deepEqual(validateActivities(['business-terms']),['business-terms']);
});

const statePath='/api/business-terms/state';
const change=(cookie,body,extra={})=>({method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...extra},body:JSON.stringify(body)});
test('saved Business terms choices require student writes, exact origin, known items and isolated sessions', async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test'),other=await login(e,'other-test','https://cd26.englishladder.com');
  const input={number:1,field:'finished',value:true,revision:0};
  assert.equal((await call(e,statePath)).status,401);
  assert.equal((await call(e,statePath,change(teacher.cookie,input))).status,403);
  assert.equal((await call(e,statePath,change(student.cookie,input,{Origin:'https://evil.test'}))).status,403);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie}},'https://cd26.englishladder.com')).status,401);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie,Origin:'https://evil.test'}})).status,403);
  assert.equal((await call(e,statePath,{method:'DELETE',headers:{Cookie:student.cookie}})).status,405);
  for(const body of [{...input,number:18},{...input,number:'1'},{...input,field:'answers'},{...input,value:'true'},{...input,revision:-1},{...input,studentId:'cd26'}]) {
    assert.equal((await call(e,statePath,change(student.cookie,body))).status,400);
  }
  const saved=await call(e,statePath,change(student.cookie,input));assert.equal(saved.status,200);assert.equal(saved.headers.get('cache-control'),'no-store');
  const entry=(await saved.json()).entry;assert.equal(entry.finished,true);assert.equal(entry.question,false);assert.equal(entry.revision,1);assert(!Number.isNaN(Date.parse(entry.updatedAt)));
  assert.deepEqual((await(await call(e,statePath,{headers:{Cookie:teacher.cookie}})).json()).entries,[entry]);
  assert.deepEqual((await(await call(e,statePath,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json()).entries,[]);
  e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await call(e,statePath,change(student.cookie,{...input,value:false,revision:1}))).status,429);
});

test('Business terms saves retry safely, reject conflicting updates, undo independently, and delete with the account', async()=>{
  const e=env(),student=await login(e),store=e.FEEDBACK_STORE.get('ab26');
  const input={number:1,field:'finished',value:true,revision:0};
  const saved=(await(await call(e,statePath,change(student.cookie,input))).json()).entry;
  assert.deepEqual((await(await call(e,statePath,change(student.cookie,input))).json()).entry,saved);
  assert.equal((await call(e,statePath,change(student.cookie,{...input,field:'question'}))).status,409);
  const outcomes=await Promise.all([false,true].map(value=>call(e,statePath,change(student.cookie,{...input,field:value?'question':'finished',value,revision:1}))));
  assert.deepEqual(outcomes.map(r=>r.status).sort(),[200,409]);
  let entry=(await(await call(e,statePath,{headers:{Cookie:student.cookie}})).json()).entries[0];
  for(const field of ['finished','question']) {
    entry=(await(await call(e,statePath,change(student.cookie,{number:1,field,value:true,revision:entry.revision}))).json()).entry;
  }
  let questions=(await(await store.fetch(new Request('https://feedback.internal/terms/questions'))).json()).questions;
  assert.equal(questions.length,1);assert.deepEqual(questions[0].sentences,bank.items[0].sentences);assert.equal(questions[0].progress.finished,true);
  entry=(await(await call(e,statePath,change(student.cookie,{number:1,field:'question',value:false,revision:entry.revision}))).json()).entry;
  assert.equal(entry.finished,true);assert.equal(entry.question,false);
  assert.deepEqual((await(await store.fetch(new Request('https://feedback.internal/terms/questions'))).json()).questions,[]);
  await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await store.storage.list({prefix:'terms:'})).size,0);
  assert.equal((await call(e,statePath,change(student.cookie,input))).status,410);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie}})).status,410);
});
