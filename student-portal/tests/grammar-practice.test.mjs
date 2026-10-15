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
