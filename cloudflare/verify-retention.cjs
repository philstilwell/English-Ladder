'use strict';
// Check the live package and a small, fixed set of expired public addresses.
const {createCurlRequest, verifyResponse} = require('./verify.cjs');
const {isAllowedPublicEdgeBlock} = require('./verify-current-lesson.cjs');

const DAY_MS = 24 * 60 * 60 * 1000;
const FIXED_EST_OFFSET_MS = -5 * 60 * 60 * 1000;
const LEVELS = ['beginner', 'intermediate', 'advanced'];

function retentionWindow(now = new Date()) {
  if (!(now instanceof Date) || !Number.isFinite(now.getTime())) {
    throw new Error('The retention clock must be a valid Date.');
  }
  const date = new Date(now.getTime() + FIXED_EST_OFFSET_MS).toISOString().slice(0, 10);
  const midnight = Date.parse(`${date}T00:00:00Z`);
  return {
    asOf: date,
    oldestAllowed: new Date(midnight - 49 * DAY_MS).toISOString().slice(0, 10),
    expiredProbeDate: new Date(midnight - 50 * DAY_MS).toISOString().slice(0, 10),
  };
}

function dailyNewsDate(file) {
  // Match the same dated source, page, and image families as lesson_retention.py.
  const match = /^news\/(\d{4}-\d{2}-\d{2})\/(?:beginner|intermediate|advanced)\.html$/.exec(file)
    || /^archive\/lessons\/(\d{4}-\d{2}-\d{2})\.json$/.exec(file)
    || /^assets\/news\/(\d{4}-\d{2}-\d{2})(?:-[a-f0-9]{12})?\.(?:json|webp)(?:\.tmp)?$/.exec(file);
  if (!match) return null;
  const date = new Date(`${match[1]}T00:00:00Z`);
  if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== match[1]) {
    throw new Error(`deployment.json: invalid dated daily-news path ${file}`);
  }
  return match[1];
}

function assertRetainedManifest(manifest, oldestAllowed) {
  if (!manifest || typeof manifest !== 'object' || !manifest.files
      || typeof manifest.files !== 'object' || Array.isArray(manifest.files)) {
    throw new Error('deployment.json: invalid deployment manifest');
  }
  const expired = Object.keys(manifest.files).filter(file => {
    const date = dailyNewsDate(file);
    return date !== null && date < oldestAllowed;
  });
  if (expired.length) {
    throw new Error(`deployment.json: ${expired.length} expired daily-news files remain before ${oldestAllowed}: ${expired.slice(0, 5).join(', ')}`);
  }
}

function expiredProbes(date) {
  return [
    ...LEVELS.map(level => `/news/${date}/${level}.html`),
    `/news/${date}/beginner`,
    `/archive/lessons/${date}.json`,
  ];
}

async function verifyRetention({origin, request, now = new Date(), sleep}) {
  const window = retentionWindow(now);
  const response = await verifyResponse('deployment.json', {origin, request, sleep});
  let manifest;
  try {
    manifest = JSON.parse(response.body.toString('utf8'));
  } catch {
    throw new Error('deployment.json: invalid deployment manifest');
  }
  assertRetainedManifest(manifest, window.oldestAllowed);
  const probes = expiredProbes(window.expiredProbeDate);
  for (const file of probes) {
    await verifyResponse(file, {origin, request, sleep, expectedStatus: 404});
  }
  return {...window, probes: probes.length};
}

async function main(argv = process.argv.slice(2)) {
  const origin = new URL(argv[0]);
  if (!['https:', 'http:'].includes(origin.protocol) || origin.pathname !== '/'
      || origin.search || origin.hash || origin.username || origin.password) {
    throw new Error('Provide a site origin without credentials, a path, query, or fragment.');
  }
  const result = await verifyRetention({origin, request: createCurlRequest(origin)});
  console.log(`Verified no expired daily-news files before ${result.oldestAllowed} in the live manifest and ${result.probes} real 404s for ${result.expiredProbeDate} at ${origin.origin} (50 fixed-EST calendar days).`);
}

module.exports = {retentionWindow, dailyNewsDate, assertRetainedManifest, expiredProbes, verifyRetention};
if (require.main === module) {
  main().catch(error => {
    if (isAllowedPublicEdgeBlock(error)) {
      console.warn(`Public-domain retention verification was blocked by Cloudflare edge protection from this runner: ${error.message}`);
      return;
    }
    console.error(error.message);
    process.exitCode = 1;
  });
}
