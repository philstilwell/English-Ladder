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
