import test from 'node:test';
import assert from 'node:assert/strict';
import bank from '../grammar-bank.json' with { type: 'json' };
import { env, call, login, origin } from './harness.mjs';
import { ACTIVITY_TOOLS, visibleActivities, validateActivities } from '../activities.mjs';

test('grammar snapshot has all 900 ranked items and the source answer in each set of choices', () => {
  assert.equal(bank.source.range, 'Grammar!A11:E910');
  assert.equal(bank.items.length, 900);
  bank.items.forEach((item, index) => {
    assert.deepEqual(Object.keys(item), ['number', 'prompt', 'answer', 'options']);
    assert.equal(item.number, index + 1);
    assert.equal(item.options.length, 4); assert.equal(new Set(item.options).size, 4);
    assert(item.options.includes(item.answer));
    for (const text of [item.prompt, ...item.options]) assert.equal(typeof text, 'string');
  });
  assert.equal(bank.items[0].answer, 'is much more intelligent');
  assert.equal(bank.items[899].prompt, 'I recommend you take a camera _______ your trip to Africa.');
  assert.equal(bank.items[899].answer, 'on');
});

test('grammar content requires a host-bound login, permits teacher preview and offers no write method', async () => {
  const e = env(), student = await login(e), teacher = await login(e, 'teacher-test');
  assert.equal((await call(e, '/api/grammar-practice')).status, 401);
  assert.equal((await call(e, '/grammar-bank.json')).status, 404);
  assert.equal((await call(e, '/api/grammar-practice', { headers: { Cookie: student.cookie } }, 'https://cd26.englishladder.com')).status, 401);
  // Practice reads do not need the learning-history store or an AI binding.
  e.FEEDBACK_STORE = { get() { throw new Error('Grammar must not access learning history'); } };
  for (const cookie of [student.cookie, teacher.cookie]) {
    const response = await call(e, '/api/grammar-practice', { headers: { Cookie: cookie } });
    assert.equal(response.status, 200); assert.equal(response.headers.get('Cache-Control'), 'no-store');
    const data = await response.json(); assert.deepEqual(data, { items: bank.items });
    assert(!JSON.stringify(data).includes('docs.google.com'));
    for (const method of ['POST', 'PUT', 'DELETE']) {
      const rejected = await call(e, '/api/grammar-practice', { method, headers: { Cookie: cookie, Origin: origin }, body: '{}' });
      assert.equal(rejected.status, 405); assert.equal(rejected.headers.get('Allow'), 'GET');
    }
  }
});

test('grammar visibility is available without changing existing saved activity choices', () => {
  assert(ACTIVITY_TOOLS.some(tool => tool.id === 'grammar-practice'));
  assert(visibleActivities({}).includes('grammar-practice'));
  assert.deepEqual(visibleActivities({ visibleActivities: ['english-road'] }), ['english-road']);
  assert.deepEqual(visibleActivities({ visibleActivities: [] }), []);
  assert.deepEqual(validateActivities(['grammar-practice']), ['grammar-practice']);
});

const statePath='/api/grammar-practice/state';
const change=(cookie,body,extra={})=>({method:'PATCH',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...extra},body:JSON.stringify(body)});
test('saved Grammar choices require student writes, exact origin, known items and isolated sessions', async()=>{
  const e=env(),student=await login(e),teacher=await login(e,'teacher-test'),other=await login(e,'other-test','https://cd26.englishladder.com');
  const input={number:1,field:'finished',value:true,revision:0};
  assert.equal((await call(e,statePath)).status,401);
  assert.equal((await call(e,statePath,change(teacher.cookie,input))).status,403);
  assert.equal((await call(e,statePath,change(student.cookie,input,{Origin:'https://evil.test'}))).status,403);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie}},'https://cd26.englishladder.com')).status,401);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie,Origin:'https://evil.test'}})).status,403);
  assert.equal((await call(e,statePath,{method:'DELETE',headers:{Cookie:student.cookie}})).status,405);
  for(const body of [{...input,number:901},{...input,number:'1'},{...input,field:'answers'},{...input,value:'true'},{...input,revision:-1},{...input,studentId:'cd26'}]) {
    assert.equal((await call(e,statePath,change(student.cookie,body))).status,400);
  }
  const saved=await call(e,statePath,change(student.cookie,input));assert.equal(saved.status,200);assert.equal(saved.headers.get('cache-control'),'no-store');
  const entry=(await saved.json()).entry;assert.equal(entry.finished,true);assert.equal(entry.question,false);assert.equal(entry.revision,1);assert(!Number.isNaN(Date.parse(entry.updatedAt)));
  assert.deepEqual((await(await call(e,statePath,{headers:{Cookie:teacher.cookie}})).json()).entries,[entry]);
  assert.deepEqual((await(await call(e,statePath,{headers:{Cookie:other.cookie}},'https://cd26.englishladder.com')).json()).entries,[]);
  e.PRACTICE_LIMITER={limit:async()=>({success:false})};assert.equal((await call(e,statePath,change(student.cookie,{...input,value:false,revision:1}))).status,429);
});

test('Grammar saves retry safely, reject conflicting updates, undo independently, and delete with the account', async()=>{
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
  let questions=(await(await store.fetch(new Request('https://feedback.internal/grammar/questions'))).json()).questions;
  assert.equal(questions.length,1);assert.deepEqual(questions[0].prompt,bank.items[0].prompt);assert.equal(questions[0].progress.finished,true);
  entry=(await(await call(e,statePath,change(student.cookie,{number:1,field:'question',value:false,revision:entry.revision}))).json()).entry;
  assert.equal(entry.finished,true);assert.equal(entry.question,false);
  assert.deepEqual((await(await store.fetch(new Request('https://feedback.internal/grammar/questions'))).json()).questions,[]);
  await store.fetch(new Request('https://feedback.internal/admin/delete-account',{method:'POST'}));
  assert.equal((await store.storage.list({prefix:'grammar:'})).size,0);
  assert.equal((await call(e,statePath,change(student.cookie,input))).status,410);
  assert.equal((await call(e,statePath,{headers:{Cookie:student.cookie}})).status,410);
});

test('Grammar and Business terms use separate saved choices even for identical item numbers',async()=>{
  const e=env(),student=await login(e);
  const grammar={number:1,field:'finished',value:true,revision:0},terms={...grammar,field:'question'};
  assert.equal((await call(e,statePath,change(student.cookie,grammar))).status,200);
  assert.equal((await call(e,'/api/business-terms/state',change(student.cookie,terms))).status,200);
  const a=(await(await call(e,statePath,{headers:{Cookie:student.cookie}})).json()).entries[0];
  const b=(await(await call(e,'/api/business-terms/state',{headers:{Cookie:student.cookie}})).json()).entries[0];
  assert.equal(a.finished,true);assert.equal(a.question,false);assert.equal(b.finished,false);assert.equal(b.question,true);
  const store=e.FEEDBACK_STORE.get('ab26');assert.deepEqual((await(await store.fetch(new Request('https://feedback.internal/grammar/questions'))).json()).questions,[]);
  assert.equal((await(await store.fetch(new Request('https://feedback.internal/terms/questions'))).json()).questions.length,1);
});
