import test from 'node:test';
import assert from 'node:assert/strict';
import { env } from './harness.mjs';
import { validateCefr } from '../cefr.mjs';
import { pruneTranscriptCache } from '../transcript-cache.mjs';

const snapshot = day => validateCefr({ state: 'estimated', lower: 'A2', upper: 'B1', confidence: 'low',
  assessedOn: day, latestSessionId: day + '-1200', rationale: 'Independent everyday questions with some support.',
  aspects: ['range','accuracy','coherence','interaction'].map(area => ({ area, detail: 'A brief observed language pattern.' })),
  evidence: ['00:01:00','00:02:00'].map(at => ({ sessionId: day + '-1200', at, quote: 'Could you explain that?', note: 'Asks for clarification.' })) });
const key = day => 'cefr:history:' + day + ':' + 'a'.repeat(64);
const read = (store, suffix = '') => store.fetch(new Request('https://feedback.internal/admin/cefr/history' + suffix));

test('history pages preserve original dated snapshots, strip non-estimate data, bound reads and do not write', async () => {
  const store = env().FEEDBACK_STORE.get('ab26');
  const records = Object.fromEntries(Array.from({length:15}, (_,i) => {
    const day = '2025-' + String(Math.floor(i / 2) + 1).padStart(2, '0') + (i % 2 ? '-26' : '-25');
    return [key(day), { ...snapshot(day), transcript: 'Never return a full transcript', password: 'Never return this' }];
  }));
  await store.storage.put(records);
  const before = await store.storage.list();
  const originalList = store.storage.list; const reads = [];
  store.storage.list = async options => { reads.push(options); return originalList(options); };
  const first = await (await read(store)).json();
  assert.equal(first.history.length, 12); assert.equal(first.history[0].assessedOn, '2025-08-25');
  assert.equal(reads.length, 1); assert.equal(reads[0].limit, 13); assert.equal(reads[0].reverse, true);
  assert.doesNotMatch(JSON.stringify(first), /transcript|password/);
  const second = await (await read(store, '?before=' + encodeURIComponent(first.nextCursor))).json();
  assert.equal(second.history.length, 3); assert.equal(second.nextCursor, null);
  assert.equal(new Set([...first.history, ...second.history].map(row => row.assessedOn)).size, 15);
  assert.equal(second.history.at(-1).assessedOn, '2025-01-25');
  assert.deepEqual(await store.storage.list(), before);
  for (const cursor of ['', '../assessment:current', '2026-02-30:' + 'a'.repeat(64), '2026-10-26:bad']) {
    assert.equal((await read(store, '?before=' + encodeURIComponent(cursor))).status, 400);
  }
});

test('history supports an existing baseline, includes insufficient reviews and survives transcript expiry', async () => {
  const store = env().FEEDBACK_STORE.get('ab26'), current = snapshot('2026-01-25');
  assert.deepEqual(await (await read(store)).json(), {history:[],nextCursor:null});
  await store.storage.put({'cefr:current':current});
  assert.deepEqual((await (await read(store)).json()).history, [current]);
  assert.equal((await store.storage.list({prefix:'cefr:history:'})).size, 0);
  await store.storage.put({[key('2026-01-25')]:current, [key('2026-02-25')]:{
    state:'insufficient',assessedOn:'2026-02-25',latestSessionId:'2026-02-20-1200',rationale:'More independent language is needed.'}});
  await pruneTranscriptCache(store.storage);
  const history = (await (await read(store)).json()).history;
  assert.deepEqual(history.map(row => row.state), ['insufficient','estimated']);
  assert.deepEqual(history[1], current); assert.deepEqual(await store.storage.get('cefr:current'), current);
  await store.fetch(new Request('https://feedback.internal/admin/delete-account', {method:'POST'}));
  assert.equal((await read(store)).status, 410);
  assert.equal((await store.storage.list({prefix:'cefr:'})).size, 0);
});
