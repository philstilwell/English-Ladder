'use strict';
// Publish an already-generated lesson, with a fixed toolchain and bounded retries.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');

const ROOT = path.resolve(__dirname, '..');
// Cloudflare needed more than a minute for the full site/search audit in the
// first live validation; reserve three minutes before the upload retry budget.
const PREFLIGHT_TIMEOUT_MS = 180_000;
const DEPLOY_TIMEOUT_MS = 120_000;
const RETRY_DELAYS_MS = Object.freeze([10_000, 30_000]);
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

function localWrangler(root) {
  const declared = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8')).devDependencies?.wrangler;
  if (!/^\d+\.\d+\.\d+$/.test(declared || '')) {
    throw new Error('Wrangler must be pinned to an exact version in package.json.');
  }
  const directory = path.join(root, 'node_modules', 'wrangler');
  let installed;
  try {
    installed = JSON.parse(fs.readFileSync(path.join(directory, 'package.json'), 'utf8')).version;
    fs.accessSync(path.join(directory, 'bin', 'wrangler.js'), fs.constants.R_OK);
  } catch {
    throw new Error('The pinned local Wrangler is missing. Run npm ci before publishing; automatic tool installation is disabled.');
  }
  if (installed !== declared) {
    throw new Error(`Installed Wrangler ${installed} does not match pinned version ${declared}. Run npm ci before publishing.`);
  }
  return {version: installed, bin: path.join(directory, 'bin', 'wrangler.js')};
}

// A timed-out command and its children must stop before the next attempt starts.
// Wrangler's launcher and npm can both spawn children, so kill the process group
// on Linux/macOS instead of leaving an upload running after its launcher exits.
function runCommand(command, args, {cwd, env = process.env, timeoutMs, stdio = 'inherit'} = {}) {
  return new Promise(resolve => {
    const grouped = process.platform !== 'win32';
    const child = cp.spawn(command, args, {cwd, env, stdio, detached: grouped});
    let timedOut = false;
    let interrupted = null;
    let error = null;
    let settled = false;
    function stop() {
      try {
        if (grouped && child.pid) process.kill(-child.pid, 'SIGKILL');
        else child.kill('SIGKILL');
      } catch (failure) {
        if (failure.code !== 'ESRCH') error = failure;
      }
    }
    function onInterrupt(signal) {
      interrupted = signal;
      stop();
    }
    const onSigint = () => onInterrupt('SIGINT');
    const onSigterm = () => onInterrupt('SIGTERM');
    process.once('SIGINT', onSigint);
    process.once('SIGTERM', onSigterm);
    const timer = setTimeout(() => {
      timedOut = true;
      stop();
    }, timeoutMs);
    function finish(code, signal) {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      process.removeListener('SIGINT', onSigint);
      process.removeListener('SIGTERM', onSigterm);
      resolve({code, signal, timedOut, interrupted, error});
    }
    child.once('error', failure => {
      error = failure;
      finish(null, null);
    });
    child.once('close', finish);
  });
}

function failureDescription(result, timeoutMs) {
  if (result.interrupted) return `interrupted by ${result.interrupted}`;
  if (result.timedOut) return `timed out after ${timeoutMs / 1000} seconds`;
  if (result.error) return `could not run (${result.error.code || result.error.message})`;
  if (result.signal) return `terminated by ${result.signal}`;
  return `exited with status ${result.code}`;
}

function succeeded(result) {
  return result.code === 0 && !result.timedOut && !result.interrupted && !result.error;
}

async function deploy({root = ROOT, runner = runCommand, pause = sleep, log = console.log, revision} = {}) {
  const wrangler = localWrangler(root);
  const commit = revision || cp.execFileSync('git', ['rev-parse', 'HEAD'], {
    cwd: root, encoding: 'utf8', timeout: 5000
  }).trim();
  if (!/^[a-f0-9]{40}$/.test(commit)) throw new Error('Cannot identify the exact commit to publish.');
  log(`Publishing commit ${commit} with pinned local Wrangler ${wrangler.version}.`);
  log(`Preflight: check and package public files once (limit ${PREFLIGHT_TIMEOUT_MS / 1000}s).`);
  const preflight = await runner('npm', ['run', 'build:cloudflare'], {
    cwd: root, timeoutMs: PREFLIGHT_TIMEOUT_MS
  });
  if (!succeeded(preflight)) {
    throw new Error(`Publishing preflight ${failureDescription(preflight, PREFLIGHT_TIMEOUT_MS)}. No upload was attempted. Fix the reported checks before retrying.`);
  }
  const manifest = JSON.parse(fs.readFileSync(path.join(root, '.cf-site', 'deployment.json'), 'utf8'));
  if (manifest.revision !== commit || !manifest.files || !Object.keys(manifest.files).length) {
    throw new Error(`The public-file manifest does not describe commit ${commit}. No upload was attempted.`);
  }
  log(`Prepared ${Object.keys(manifest.files).length} public files for commit ${commit}.`);
  const attempts = RETRY_DELAYS_MS.length + 1;
  for (let attempt = 1; attempt <= attempts; attempt++) {
    log(`Cloudflare deployment attempt ${attempt}/${attempts}, commit ${commit} (limit ${DEPLOY_TIMEOUT_MS / 1000}s).`);
    // build:cloudflare already ran. wrangler.jsonc intentionally has no custom
    // build command: --no-bundle does not disable a configured custom build.
    const result = await runner(process.execPath, [wrangler.bin, 'deploy'], {
      cwd: root, timeoutMs: DEPLOY_TIMEOUT_MS
    });
    if (succeeded(result)) {
      log(`Cloudflare accepted commit ${commit} on attempt ${attempt}/${attempts}. The publishing workflow must still verify the live manifest and current lesson.`);
      return {revision: commit, version: wrangler.version, attempts: attempt};
    }
    const reason = failureDescription(result, DEPLOY_TIMEOUT_MS);
    log(`Cloudflare deployment attempt ${attempt}/${attempts} ${reason}.`);
    if (result.interrupted) throw new Error(`Publishing stopped: ${reason}. No further upload was attempted.`);
    if (attempt < attempts) {
      const delay = RETRY_DELAYS_MS[attempt - 1];
      log(`Retrying the same prepared commit in ${delay / 1000}s; lesson generation will not run again.`);
      await pause(delay);
    }
  }
  throw new Error(`Cloudflare deployment failed after ${attempts} attempts for commit ${commit}. Inspect the detailed Wrangler output above, then retry this existing Cloudflare build. After deployment succeeds, rerun only the failed publishing job, or run the GitHub workflow with deploy_only=true, to verify without paid lesson, translation, or image generation.`);
}

if (require.main === module) {
  deploy().catch(error => {
    console.error(`Publishing failed: ${error.message}`);
    process.exitCode = 1;
  });
}

module.exports = {deploy, localWrangler, runCommand, PREFLIGHT_TIMEOUT_MS, DEPLOY_TIMEOUT_MS, RETRY_DELAYS_MS};
