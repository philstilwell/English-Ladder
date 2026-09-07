'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const cp = require('node:child_process');
const path = require('node:path');

const RETRY_DELAYS_MS = [2000, 4000];
const TRANSIENT_HTTP = new Set([408, 429, 500, 502, 503, 504]);
// DNS/connection failures, partial transfers, timeouts, and interrupted streams.
// Certificate validation (60), bad URLs (3), and missing curl remain failures.
const TRANSIENT_CURL = new Set([5, 6, 7, 18, 28, 52, 55, 56, 92]);
const wait = milliseconds => new Promise(resolve => setTimeout(resolve, milliseconds));
const hash = body => crypto.createHash('sha256').update(body).digest('hex');
const statusMismatch = (file, expected, actual) => {
  const error = new Error(`${file}: expected HTTP ${expected}, got ${actual}`);
  error.retryable = TRANSIENT_HTTP.has(actual);
  return error;
};

function createCurlRequest(origin, ip, execFile = cp.execFile) {
  // An optional IP verifies the real domain before old DNS caches expire.
  // curl still validates the domain's HTTPS certificate.
  const connection = ip ? ['--resolve', `${origin.hostname}:${origin.port || (origin.protocol === 'https:' ? 443 : 80)}:${ip}`] : [];
  return url => new Promise((resolve, reject) => {
    execFile('curl', [...connection, '--silent', '--show-error', '--max-time', '30',
      '--user-agent', 'English-family-deploy-check', '--write-out', '\n%{http_code}', url.href],
    {encoding: 'buffer', maxBuffer: 30 * 1024 * 1024}, (error, output) => {
      const hasStatus = Buffer.isBuffer(output) && /^\n\d{3}$/.test(output.subarray(-4).toString('ascii'));
      const status = hasStatus ? Number(output.subarray(-3).toString('ascii')) : undefined;
      if (error) {
        const failure = new Error('Request failed');
        failure.retryable = TRANSIENT_CURL.has(error.code);
        // A partial transfer may still identify the actual HTTP response.
        // Preserve it so transport retries cannot hide authentication errors
        // or an exposed file that should have returned 404.
        failure.status = status;
        reject(failure);
        return;
      }
      // The status trailer is separate from the response bytes: PDFs, images,
      // and HTML must retain their exact bytes for the deployment comparison.
      if (!hasStatus) {
        reject(new Error('Request returned an invalid HTTP status'));
        return;
      }
      resolve({status, body: output.subarray(0, -4)});
    });
  });
}

async function verifyResponse(file, {origin, request, expectedHash, expectedStatus = 200,
  sleep = wait}) {
  for (let attempt = 0; attempt <= RETRY_DELAYS_MS.length; attempt++) {
    // Verify the URL students actually receive. A cache-busted copy may be
    // current while this original public URL still serves the previous page.
    const url = new URL(file, origin);
    try {
      const response = await request(url);
      if (response.status !== expectedStatus) {
        throw statusMismatch(file, expectedStatus, response.status);
      }
      if (expectedHash !== undefined && hash(response.body) !== expectedHash) {
        const error = new Error(`${file}: content mismatch`);
        error.retryable = true;
        throw error;
      }
      return response;
    } catch (error) {
      if (Number.isInteger(error.status) && error.status >= 100 && error.status <= 599
          && error.status !== expectedStatus) {
        error = statusMismatch(file, expectedStatus, error.status);
      }
      if (attempt === RETRY_DELAYS_MS.length || error.retryable !== true) {
        // Request diagnostics can contain server details. Only report the
        // checked file or a locally constructed validation message.
        if (!error.message.startsWith(`${file}: `)) {
          const failure = new Error(`${file}: could not fetch verified content`);
          failure.cause = error;
          throw failure;
        }
        throw error;
      }
      await sleep(RETRY_DELAYS_MS[attempt]);
    }
  }
}

async function verifySite(manifest, {origin, request, sleep}) {
  const errors = [];
  const entries = Object.entries(manifest.files);
  const options = {origin, request, sleep};
  let next = 0;
  await Promise.all(Array.from({length: 8}, async () => {
    while (next < entries.length) {
      const [file, expectedHash] = entries[next++];
      try {
        await verifyResponse(file, {...options, expectedHash});
      } catch (error) {
        errors.push(error.message);
      }
    }
  }));
  try {
    await verifyResponse('/', {...options, expectedHash: manifest.files['index.html']});
  } catch (error) {
    errors.push(error.message);
  }
  for (const missing of ['/missing-migration-check-74629.html', '/.git/config', '/README.md', '/cloudflare/build.cjs']) {
    try {
      await verifyResponse(missing, {...options, expectedStatus: 404});
    } catch (error) {
      errors.push(error.message);
    }
  }
  if (errors.length) throw new Error(errors.join('\n'));
  return entries.length;
}

async function main(argv = process.argv.slice(2)) {
  const root = path.resolve(__dirname, '..');
  const origin = new URL(argv[0]);
  if (!['https:', 'http:'].includes(origin.protocol) || origin.pathname !== '/') {
    throw new Error('Provide a site origin without a path.');
  }
  const manifest = JSON.parse(fs.readFileSync(path.join(root, '.cf-site/deployment.json'), 'utf8'));
  const count = await verifySite(manifest, {origin, request: createCurlRequest(origin, argv[1])});
  console.log(`Verified ${count} files byte for byte, homepage, and real 404 responses at ${origin.origin}.`);
}

module.exports = {createCurlRequest, verifyResponse, verifySite, main};
if (require.main === module) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
