'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const {retentionWindow, assertRetainedManifest, expiredProbes, verifyRetention} = require('../cloudflare/verify-retention.cjs');
const origin = new URL('https://englishladder.example/');
const now = new Date('2026-09-22T15:00:00Z');
const retained = {files: {
  'index.html': 'hash',
  'news/2026-08-04/beginner.html': 'hash',
  'archive/lessons/2026-09-22.json': 'hash',
  'assets/news/2026-09-22-aabbccddeeff.webp': 'hash',
}};

function harness(manifest = retained, statuses = {}) {
  const urls = [], delays = [];
  return {
    urls, delays,
    options: {
      origin, now,
      sleep: async delay => { delays.push(delay); },
      request: async url => {
        urls.push(url.href);
        const values = statuses[url.pathname];
        const status = values?.length ? values.shift() : url.pathname === '/deployment.json' ? 200 : 404;
        return {status, body: Buffer.from(url.pathname === '/deployment.json' ? JSON.stringify(manifest) : 'Not found')};
      },
    },
  };
}

test('the 50-day September 22 window keeps August 4 and probes August 3', () => {
  assert.deepEqual(retentionWindow(now), {
    asOf: '2026-09-22', oldestAllowed: '2026-08-04', expiredProbeDate: '2026-08-03',
  });
});

test('the retention date changes at fixed EST midnight, including during daylight saving time', () => {
  assert.deepEqual(retentionWindow(new Date('2026-09-22T04:59:59.999Z')), {
    asOf: '2026-09-21', oldestAllowed: '2026-08-03', expiredProbeDate: '2026-08-02',
  });
  assert.deepEqual(retentionWindow(new Date('2026-09-22T05:00:00Z')), retentionWindow(now));
  assert.throws(() => retentionWindow(new Date('invalid')), /valid Date/);
});

test('the live manifest and all five ordinary expired addresses are checked without cache-busting', async () => {
  const fixture = harness();
  assert.deepEqual(await verifyRetention(fixture.options), {
    ...retentionWindow(now), probes: 5,
  });
  assert.deepEqual(fixture.urls, [
    'https://englishladder.example/deployment.json',
    ...expiredProbes('2026-08-03').map(file => origin.origin + file),
  ]);
  assert.equal(fixture.urls.length, 6);
  assert.deepEqual(fixture.delays, []);
});

test('expired lesson pages, archives, image metadata and illustrations block verification before probing', async () => {
  for (const file of [
    'news/2026-08-03/advanced.html',
    'archive/lessons/2026-08-03.json',
    'assets/news/2026-07-01.json',
    'assets/news/2026-08-03-aabbccddeeff.webp',
  ]) {
    const fixture = harness({files: {...retained.files, [file]: 'hash'}});
    await assert.rejects(verifyRetention(fixture.options), /expired daily-news files remain before 2026-08-04/);
    assert.equal(fixture.urls.length, 1);
  }
});

test('an empty news archive, boundary date, future date, and evergreen assets are allowed', () => {
  assert.doesNotThrow(() => assertRetainedManifest({files: {'index.html': 'hash'}}, '2026-08-04'));
  assert.doesNotThrow(() => assertRetainedManifest({files: {
    ...retained.files,
    'archive/lessons/2026-09-23.json': 'hash',
    'assets/editorial/2026-07-01.webp': 'hash',
    'stories/city-trees/beginner.html': 'hash',
  }}, '2026-08-04'));
});

test('malformed manifests and invalid calendar dates cannot be reported as retained', async () => {
  for (const manifest of [null, [], {}, {files: []}, {files: {'news/2026-02-30/beginner.html': 'hash'}}]) {
    const fixture = harness(manifest);
    await assert.rejects(verifyRetention(fixture.options), /deployment.json: invalid/);
    assert.equal(fixture.urls.length, 1);
  }
  await assert.rejects(verifyRetention({origin, now, request: async () => ({status: 200, body: Buffer.from('invalid JSON')})}), /invalid deployment manifest/);
});

test('expired routes must return real 404s, never a stale page or redirect', async () => {
  for (const status of [200, 301, 302]) {
    const fixture = harness(retained, {'/news/2026-08-03/beginner.html': [status]});
    await assert.rejects(verifyRetention(fixture.options), new RegExp(`expected HTTP 404, got ${status}`));
    assert.equal(fixture.urls.length, 2);
  }
});

test('a temporary failure retries only its route and persistent edge blocks remain bounded', async () => {
  const fixture = harness(retained, {'/news/2026-08-03/beginner': [503, 404]});
  await verifyRetention(fixture.options);
  assert.equal(fixture.urls.length, 7);
  assert.deepEqual(fixture.delays, [2000]);
  const blocked = harness(retained, {'/deployment.json': [403, 403, 403]});
  await assert.rejects(verifyRetention(blocked.options), /expected HTTP 200, got 403/);
  assert.equal(blocked.urls.length, 3);
  assert.deepEqual(blocked.delays, [2000, 4000]);
});
