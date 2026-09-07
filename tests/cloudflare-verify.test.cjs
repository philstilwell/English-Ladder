'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {createCurlRequest, verifyResponse, verifySite} = require('../cloudflare/verify.cjs');
const origin = new URL('https://englishladder.example/');
const hash = body => crypto.createHash('sha256').update(body).digest('hex');
const current = Buffer.from('Current published lesson');
const stale = Buffer.from('Previous published lesson');
const expectedHash = hash(current);

function harness(responses) {
  const urls = [];
  const delays = [];
  return {
    urls, delays,
    options: {
      origin, expectedHash,
      sleep: async delay => { delays.push(delay); },
      request: async url => {
        urls.push(url);
        const response = responses.shift();
        if (response instanceof Error) throw response;
        assert.ok(response, 'Unexpected extra request');
        return response;
      }
    }
  };
}

test('matching content is checked once without changing the URL', async () => {
  const fixture = harness([{status: 200, body: current}]);
  const response = await verifyResponse('news/2026-09-07/advanced.html', fixture.options);
  assert.strictEqual(response.body, current);
  assert.equal(fixture.urls[0].href, 'https://englishladder.example/news/2026-09-07/advanced.html');
  assert.deepEqual(fixture.delays, []);
});

test('stale content retries the unchanged original URL including its original query', async () => {
  const fixture = harness([{status: 200, body: stale}, {status: 200, body: stale}, {status: 200, body: current}]);
  await verifyResponse('news/lesson.html?language=en', fixture.options);
  assert.deepEqual(fixture.delays, [2000, 4000]);
  assert.deepEqual(fixture.urls.map(url => url.href), Array(3).fill('https://englishladder.example/news/lesson.html?language=en'));
});

test('a fresh cache-busted response cannot conceal a persistently stale public URL', async () => {
  const urls = [];
  await assert.rejects(verifyResponse('lesson.html', {
    origin, expectedHash, sleep: async () => {},
    request: async url => {
      urls.push(url.href);
      return {status: 200, body: url.search ? current : stale};
    }
  }), /lesson\.html: content mismatch/);
  assert.deepEqual(urls, Array(3).fill('https://englishladder.example/lesson.html'));
});

test('persistent mismatches still fail after exactly three byte comparisons', async () => {
  const fixture = harness(Array.from({length: 3}, () => ({status: 200, body: stale})));
  await assert.rejects(verifyResponse('lesson.html', fixture.options), /lesson\.html: content mismatch/);
  assert.equal(fixture.urls.length, 3);
  assert.deepEqual(fixture.delays, [2000, 4000]);
});

test('temporary HTTP and connection failures recover with bounded retries', async () => {
  for (const status of [408, 429, 500, 502, 503, 504]) {
    const fixture = harness([{status, body: Buffer.from('server error')}, {status: 200, body: current}]);
    await verifyResponse('lesson.html', fixture.options);
    assert.equal(fixture.urls.length, 2);
    assert.deepEqual(fixture.delays, [2000]);
  }
  const failure = Object.assign(new Error('private network detail'), {retryable: true});
  const fixture = harness([failure, {status: 200, body: current}]);
  await verifyResponse('lesson.html', fixture.options);
  assert.equal(fixture.urls.length, 2);
});

test('permanent HTTP failures are immediate and cannot be hidden by a later success', async () => {
  for (const status of [301, 400, 401, 403, 404, 422, 501]) {
    const fixture = harness([{status, body: current}, {status: 200, body: current}]);
    await assert.rejects(verifyResponse('lesson.html', fixture.options), new RegExp(`expected HTTP 200, got ${status}`));
    assert.equal(fixture.urls.length, 1);
    assert.deepEqual(fixture.delays, []);
  }
});

test('exhausted connection failures report the file without exposing transport diagnostics', async () => {
  const errors = Array.from({length: 3}, () => Object.assign(new Error('private token'), {retryable: true}));
  const fixture = harness(errors);
  await assert.rejects(verifyResponse('lesson.html', fixture.options), error => {
    assert.equal(error.message, 'lesson.html: could not fetch verified content');
    assert.ok(!error.message.includes('private token'));
    return true;
  });
  assert.equal(fixture.urls.length, 3);
});

test('404 probes retry temporary service errors but never accept a successful protected-file response', async () => {
  const unavailable = harness([{status: 503, body: stale}, {status: 404, body: Buffer.from('Not found')}]);
  await verifyResponse('/.git/config', {...unavailable.options, expectedStatus: 404, expectedHash: undefined});
  assert.equal(unavailable.urls.length, 2);
  const exposed = harness([{status: 200, body: current}, {status: 404, body: current}]);
  await assert.rejects(verifyResponse('/.git/config', {...exposed.options, expectedStatus: 404, expectedHash: undefined}), /expected HTTP 404, got 200/);
  assert.equal(exposed.urls.length, 1);
});

test('site verification retries only the failing file and homepage while keeping every 404 check', async () => {
  const calls = new Map();
  const delays = [];
  const manifest = {files: {'index.html': expectedHash, 'lesson.html': expectedHash}};
  const count = await verifySite(manifest, {
    origin, sleep: async delay => delays.push(delay),
    request: async url => {
      const seen = (calls.get(url.pathname) || 0) + 1;
      calls.set(url.pathname, seen);
      if (['/index.html', '/lesson.html', '/'].includes(url.pathname)) {
        return {status: 200, body: (seen === 1 && url.pathname !== '/index.html') ? stale : current};
      }
      return {status: 404, body: Buffer.from('Not found')};
    }
  });
  assert.equal(count, 2);
  assert.equal(calls.get('/index.html'), 1);
  assert.equal(calls.get('/lesson.html'), 2);
  assert.equal(calls.get('/'), 2);
  for (const file of ['/missing-migration-check-74629.html', '/.git/config', '/README.md', '/cloudflare/build.cjs']) {
    assert.equal(calls.get(file), 1);
  }
  assert.deepEqual(delays, [2000, 2000]);
});

test('site verification fails if the homepage remains stale', async () => {
  const counts = new Map();
  const request = async url => {
    counts.set(url.pathname, (counts.get(url.pathname) || 0) + 1);
    if (url.pathname === '/index.html') return {status: 200, body: current};
    if (url.pathname === '/') return {status: 200, body: stale};
    return {status: 404, body: Buffer.from('Not found')};
  };
  await assert.rejects(verifySite({files: {'index.html': expectedHash}}, {origin, request, sleep: async () => {}}), /\/: content mismatch/);
  assert.equal(counts.get('/'), 3);
  assert.equal(counts.get('/index.html'), 1);
});

test('curl parser preserves binary bytes and certificate verification', async () => {
  const body = Buffer.from([0, 255, 128, 10, 50, 48, 48]);
  const request = createCurlRequest(origin, '192.0.2.1', (program, arguments_, options, callback) => {
    assert.equal(program, 'curl');
    assert.ok(arguments_.includes('--resolve'));
    assert.ok(arguments_.includes('englishladder.example:443:192.0.2.1'));
    assert.ok(!arguments_.includes('--insecure'));
    assert.ok(!arguments_.includes('-k'));
    assert.equal(arguments_[arguments_.indexOf('--max-time') + 1], '30');
    assert.equal(options.encoding, 'buffer');
    callback(null, Buffer.concat([body, Buffer.from('\n200')]));
  });
  const response = await request(new URL('/image.png', origin));
  assert.equal(response.status, 200);
  assert.deepEqual(response.body, body);
});

test('curl timeouts are retryable while certificate and command failures are permanent', async () => {
  for (const [code, retryable] of [[28, true], [56, true], [6, true], [60, false], [3, false], ['ENOENT', false]]) {
    const request = createCurlRequest(origin, undefined, (program, arguments_, options, callback) => callback({code}));
    await assert.rejects(request(origin), error => {
      assert.equal(error.retryable, retryable);
      return true;
    });
  }
});

test('partial transfers retain permanent HTTP failures instead of accepting a later success', async () => {
  for (const [status, expectedStatus, file] of [
    [401, 200, 'lesson.html'], [403, 200, 'lesson.html'], [404, 200, 'lesson.html'],
    [200, 404, '/.git/config'],
  ]) {
    let calls = 0;
    const delays = [];
    const request = createCurlRequest(origin, undefined, (program, arguments_, options, callback) => {
      calls++;
      if (calls === 1) callback({code: 18}, Buffer.from(`partial response\n${status}`));
      else callback(null, Buffer.concat([current, Buffer.from(`\n${expectedStatus}`)]));
    });
    await assert.rejects(verifyResponse(file, {
      origin, request, expectedStatus, expectedHash: expectedStatus === 200 ? expectedHash : undefined,
      sleep: async delay => delays.push(delay),
    }), new RegExp(`expected HTTP ${expectedStatus}, got ${status}`));
    assert.equal(calls, 1);
    assert.deepEqual(delays, []);
  }
});

test('partial transfers with the expected status retry and require a complete response', async () => {
  for (const expectedStatus of [200, 404]) {
    let calls = 0;
    const delays = [];
    const request = createCurlRequest(origin, undefined, (program, arguments_, options, callback) => {
      calls++;
      if (calls === 1) callback({code: 18}, Buffer.from(`partial\n${expectedStatus}`));
      else callback(null, Buffer.concat([current, Buffer.from(`\n${expectedStatus}`)]));
    });
    await verifyResponse(expectedStatus === 200 ? 'lesson.html' : '/.git/config', {
      origin, request, expectedStatus, expectedHash: expectedStatus === 200 ? expectedHash : undefined,
      sleep: async delay => delays.push(delay),
    });
    assert.equal(calls, 2);
    assert.deepEqual(delays, [2000]);
  }
});
