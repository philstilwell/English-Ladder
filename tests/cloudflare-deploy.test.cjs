'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {deploy, localWrangler, runCommand, PREFLIGHT_TIMEOUT_MS, DEPLOY_TIMEOUT_MS, RETRY_DELAYS_MS} = require('../cloudflare/deploy.cjs');
const revision = '3b4a34fdefc42f3e8b37933935903239bda2443b';
const ok = {code: 0};
const failed = {code: 1};

function harness(t, responses) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'english-ladder-deploy-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  fs.mkdirSync(path.join(root, 'node_modules/wrangler/bin'), {recursive: true});
  fs.mkdirSync(path.join(root, '.cf-site'));
  fs.writeFileSync(path.join(root, 'package.json'), JSON.stringify({devDependencies: {wrangler: '4.136.0'}}));
  fs.writeFileSync(path.join(root, 'node_modules/wrangler/package.json'), JSON.stringify({version: '4.136.0'}));
  fs.writeFileSync(path.join(root, 'node_modules/wrangler/bin/wrangler.js'), '');
  fs.writeFileSync(path.join(root, '.cf-site/deployment.json'), JSON.stringify({revision, files: {'index.html': 'hash'}}));
  const calls = [], pauses = [], logs = [];
  return {
    root, calls, pauses, logs,
    options: {
      root, revision,
      runner: async (command, args, options) => {
        calls.push({command, args, options});
        assert.ok(responses.length, 'Unexpected extra command');
        return responses.shift();
      },
      pause: async ms => { pauses.push(ms); },
      log: message => logs.push(message)
    }
  };
}

test('a failed upload retries the same local tool and succeeds without rebuilding', async t => {
  const fixture = harness(t, [ok, failed, ok]);
  const result = await deploy(fixture.options);
  assert.equal(result.attempts, 2);
  assert.equal(result.revision, revision);
  assert.deepEqual(fixture.pauses, [10_000]);
  assert.deepEqual(fixture.calls[0], {
    command: 'npm', args: ['run', 'build:cloudflare'],
    options: {cwd: fixture.root, timeoutMs: PREFLIGHT_TIMEOUT_MS}
  });
  const upload = {
    command: process.execPath, args: [path.join(fixture.root, 'node_modules/wrangler/bin/wrangler.js'), 'deploy'],
    options: {cwd: fixture.root, timeoutMs: DEPLOY_TIMEOUT_MS}
  };
  assert.deepEqual(fixture.calls.slice(1), [upload, upload]);
  assert.ok(fixture.logs.some(line => line.includes(revision) && line.includes('4.136.0')));
  assert.ok(fixture.logs.some(line => line.includes('still verify the live manifest')));
});

test('persistent upload failures stop after three attempts and give a generation-free recovery path', async t => {
  const fixture = harness(t, [ok, failed, failed, failed]);
  await assert.rejects(deploy(fixture.options), error => {
    assert.match(error.message, /failed after 3 attempts/);
    assert.match(error.message, /deploy_only=true/);
    assert.match(error.message, new RegExp(revision));
    return true;
  });
  assert.equal(fixture.calls.length, 4);
  assert.deepEqual(fixture.pauses, [10_000, 30_000]);
  assert.ok(PREFLIGHT_TIMEOUT_MS + 3 * DEPLOY_TIMEOUT_MS + RETRY_DELAYS_MS.reduce((a, b) => a + b, 0) + 5000 < 10 * 60_000);
});

test('failed preflight prevents every upload and is not retried', async t => {
  const fixture = harness(t, [failed]);
  await assert.rejects(deploy(fixture.options), /preflight exited with status 1.*No upload was attempted/);
  assert.equal(fixture.calls.length, 1);
  assert.deepEqual(fixture.pauses, []);
});

test('a timed-out upload retries, but a timed-out preflight never uploads', async t => {
  const timedOut = {code: null, signal: 'SIGKILL', timedOut: true};
  const fixture = harness(t, [ok, timedOut, ok]);
  assert.equal((await deploy(fixture.options)).attempts, 2);
  assert.ok(fixture.logs.some(line => line.includes('timed out after 120 seconds')));
  const preflight = harness(t, [timedOut]);
  await assert.rejects(deploy(preflight.options), /preflight timed out after 180 seconds/);
  assert.equal(preflight.calls.length, 1);
});

test('an interrupted upload aborts without retries', async t => {
  const fixture = harness(t, [ok, {code: null, interrupted: 'SIGTERM'}]);
  await assert.rejects(deploy(fixture.options), /Publishing stopped: interrupted by SIGTERM/);
  assert.equal(fixture.calls.length, 2);
  assert.deepEqual(fixture.pauses, []);
});

test('missing or different installed Wrangler fails before any command can auto-install a tool', async t => {
  const fixture = harness(t, []);
  fs.rmSync(path.join(fixture.root, 'node_modules/wrangler/bin/wrangler.js'));
  await assert.rejects(deploy(fixture.options), /Run npm ci.*automatic tool installation is disabled/);
  assert.equal(fixture.calls.length, 0);
  fs.writeFileSync(path.join(fixture.root, 'node_modules/wrangler/bin/wrangler.js'), '');
  fs.writeFileSync(path.join(fixture.root, 'node_modules/wrangler/package.json'), JSON.stringify({version: '4.137.0'}));
  assert.throws(() => localWrangler(fixture.root), /does not match pinned version/);
  fs.writeFileSync(path.join(fixture.root, 'package.json'), JSON.stringify({devDependencies: {wrangler: '^4.136.0'}}));
  assert.throws(() => localWrangler(fixture.root), /must be pinned to an exact version/);
});

test('a stale package manifest cannot be uploaded', async t => {
  const fixture = harness(t, [ok]);
  fs.writeFileSync(path.join(fixture.root, '.cf-site/deployment.json'), JSON.stringify({revision: 'e'.repeat(40), files: {'index.html': 'hash'}}));
  await assert.rejects(deploy(fixture.options), /manifest does not describe commit/);
  assert.equal(fixture.calls.length, 1);
});

test('the real runner terminates an unresponsive command within its timeout', async () => {
  const started = Date.now();
  const result = await runCommand(process.execPath, ['-e', 'setInterval(() => {}, 1000)'], {
    timeoutMs: 80, stdio: 'ignore'
  });
  assert.equal(result.timedOut, true);
  assert.equal(result.signal, 'SIGKILL');
  assert.ok(Date.now() - started < 3000, 'The timed-out process did not stop promptly');
});

test('the real runner reports missing executables as failures', async () => {
  const result = await runCommand('/definitely-missing-english-ladder-command', [], {timeoutMs: 1000, stdio: 'ignore'});
  assert.equal(result.error.code, 'ENOENT');
  assert.equal(result.timedOut, false);
});

test('a timed-out launcher also stops the upload child before a retry can start', {skip: process.platform === 'win32'}, async t => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'english-ladder-deploy-child-'));
  t.after(() => fs.rmSync(directory, {recursive: true, force: true}));
  const heartbeat = path.join(directory, 'heartbeat.txt');
  const childScript = `const fs = require('node:fs'); setInterval(() => fs.appendFileSync(${JSON.stringify(heartbeat)}, '.'), 20);`;
  const launcher = `require('node:child_process').spawn(process.execPath, ['-e', ${JSON.stringify(childScript)}], {stdio: 'inherit'}); setInterval(() => {}, 1000);`;
  const result = await runCommand(process.execPath, ['-e', launcher], {timeoutMs: 1000, stdio: 'ignore'});
  assert.equal(result.timedOut, true);
  const stopped = fs.readFileSync(heartbeat, 'utf8');
  assert.ok(stopped.length > 0, 'The child must start before testing its termination');
  await new Promise(resolve => setTimeout(resolve, 100));
  assert.equal(fs.readFileSync(heartbeat, 'utf8'), stopped, 'The upload child continued working after its launcher timed out');
});
