'use strict';
const fs = require('node:fs');
const path = require('node:path');
const {createCurlRequest, verifyResponse} = require('./verify.cjs');

const LEVELS = ['beginner', 'intermediate', 'advanced'];
const PRIVATE_PROBES = ['/missing-migration-check-74629.html', '/.git/config', '/README.md', '/cloudflare/build.cjs'];
const PUBLICATION_TIMEOUT_MS = 180_000;
const wait = milliseconds => new Promise(resolve => setTimeout(resolve, milliseconds));

function staleContent(message) {
  return Object.assign(new Error(message), {retryable: true});
}

function latestReleaseDate(root) {
  const archiveDir = path.join(root, 'archive', 'lessons');
  const dates = fs.readdirSync(archiveDir)
    .map(file => /^(\d{4}-\d{2}-\d{2})\.json$/.exec(file)?.[1])
    .filter(Boolean)
    .sort();
  if (!dates.length) throw new Error('No archived lessons are available to verify.');
  return dates.at(-1);
}

function currentLessonFiles(releaseDate) {
  return [
    'index.html',
    'archive.html',
    'lesson-data.json',
    `archive/lessons/${releaseDate}.json`,
    ...LEVELS.map(level => `${level}.html`),
    ...LEVELS.map(level => `news/${releaseDate}/${level}.html`),
  ];
}

function requireManifestFile(manifest, file) {
  const expectedHash = manifest.files[file];
  if (expectedHash === undefined) throw new Error(`Deployment manifest does not include ${file}.`);
  return expectedHash;
}

function requireText(text, needle, label) {
  if (!text.includes(needle)) throw staleContent(`${label}: missing ${needle}`);
}

async function fetchCurrentFile(file, manifest, options) {
  const expectedHash = requireManifestFile(manifest, file);
  const response = await verifyResponse(file, {
    ...options,
    // Cloudflare can add small public-domain scripts to HTML responses. Keep
    // byte-for-byte checks for JSON data and use content checks for pages.
    expectedHash: file.endsWith('.json') ? expectedHash : undefined,
  });
  return response.body.toString('utf8');
}

async function verifyCurrentLesson(manifest, {origin, request, releaseDate, sleep, retryDelaysMs}) {
  const bodies = new Map();
  const options = {origin, request, sleep, retryDelaysMs};
  for (const file of currentLessonFiles(releaseDate)) {
    bodies.set(file, await fetchCurrentFile(file, manifest, options));
  }

  requireManifestFile(manifest, 'index.html');
  const root = await verifyResponse('/', {...options, expectedHash: undefined});
  bodies.set('/', root.body.toString('utf8'));

  const archiveFile = `archive/lessons/${releaseDate}.json`;
  const archive = JSON.parse(bodies.get(archiveFile));
  if (archive.release_date !== releaseDate) {
    throw new Error(`${archiveFile}: expected release_date ${releaseDate}, got ${archive.release_date}`);
  }
  for (const level of LEVELS) {
    if (!archive.levels || !archive.levels[level]) {
      throw new Error(`${archiveFile}: missing ${level} lesson data`);
    }
  }

  const lessonData = JSON.parse(bodies.get('lesson-data.json'));
  for (const file of ['index.html', '/']) {
    requireText(bodies.get(file), `news/${releaseDate}`, file);
  }
  for (const level of LEVELS) {
    const lessonPath = `news/${releaseDate}/${level}.html`;
    const archivePath = archive.levels[level]?.file_path;
    if (![`${level}.html`, lessonPath].includes(archivePath)) {
      throw new Error(`${archiveFile}: ${level} points to ${archivePath || 'nothing'}, not ${level}.html or ${lessonPath}`);
    }
    if (lessonData[level]?.url !== lessonPath) {
      throw new Error(`lesson-data.json: ${level} points to ${lessonData[level]?.url || 'nothing'}, not ${lessonPath}`);
    }
    requireText(bodies.get('archive.html'), lessonPath, 'archive.html');
    requireText(bodies.get(`${level}.html`), lessonPath, `${level}.html`);
    requireText(bodies.get(lessonPath), releaseDate, lessonPath);
  }

  for (const probe of PRIVATE_PROBES) {
    await verifyResponse(probe, {...options, expectedStatus: 404, expectedHash: undefined});
  }

  return {releaseDate, files: currentLessonFiles(releaseDate).length};
}

async function waitForCurrentLesson(manifest, {origin, request, releaseDate,
  timeoutMs = PUBLICATION_TIMEOUT_MS, intervalMs = 10_000,
  clock = () => performance.now(), sleep = wait, log = console.log}) {
  if (![timeoutMs, intervalMs].every(value => Number.isFinite(value) && value > 0)) {
    throw new Error('Publication timeout and interval must be finite and positive.');
  }
  // A missing saved edition is a generation problem, not deployment propagation.
  for (const file of currentLessonFiles(releaseDate)) requireManifestFile(manifest, file);
  const deadline = clock() + timeoutMs;
  let lastError;
  let lastMessage;
  const boundedRequest = url => {
    const remaining = deadline - clock();
    if (remaining <= 0) throw staleContent('Publication verification deadline reached');
    return request(url, {timeoutMs: Math.min(30_000, remaining)});
  };
  while (clock() < deadline) {
    try {
      // One shared deadline covers all files and attempts, including requests.
      // Keep the quick preflight and general site verifier's existing behavior.
      const result = await verifyCurrentLesson(manifest, {
        origin, request: boundedRequest, releaseDate, retryDelaysMs: [],
      });
      if (clock() <= deadline) return result;
      lastError = new Error('Publication verification deadline reached');
      break;
    } catch (error) {
      // Only expected public files may recover from a 404. An exposed private
      // file, redirect, authentication error, or certificate failure is final.
      const missingPublicFile = error.expectedStatus === 200 && error.status === 404;
      if (!missingPublicFile && error.retryable !== true) throw error;
      lastError = error;
      if (error.message !== lastMessage) {
        log(`Waiting for public lesson URLs: ${error.message} (up to ${timeoutMs / 1000}s total).`);
        lastMessage = error.message;
      }
    }
    const remaining = deadline - clock();
    if (remaining > 0) await sleep(Math.min(intervalMs, remaining));
  }
  throw new Error(`Current lesson did not become available within ${timeoutMs / 1000}s: ${lastError?.message || 'verification deadline reached'}`);
}

async function main(argv = process.argv.slice(2)) {
  const root = path.resolve(__dirname, '..');
  const origin = new URL(argv[0]);
  if (!['https:', 'http:'].includes(origin.protocol) || origin.pathname !== '/') {
    throw new Error('Provide a site origin without a path.');
  }
  const releaseDate = process.env.RELEASE_DATE || latestReleaseDate(root);
  const manifest = JSON.parse(fs.readFileSync(path.join(root, '.cf-site/deployment.json'), 'utf8'));
  const result = await waitForCurrentLesson(manifest, {
    origin,
    request: createCurlRequest(origin),
    releaseDate,
  });
  console.log(`Verified current ${result.releaseDate} lesson, feeds, archive, homepage, and private-path 404s at ${origin.origin}.`);
}

function isAllowedPublicEdgeBlock(error) {
  return process.env.ALLOW_PUBLIC_EDGE_BLOCK === '1' && /expected HTTP \d{3}, got 403/.test(error.message);
}

module.exports = {currentLessonFiles, isAllowedPublicEdgeBlock, latestReleaseDate, verifyCurrentLesson, waitForCurrentLesson};
if (require.main === module) {
  main().catch(error => {
    if (isAllowedPublicEdgeBlock(error)) {
      console.warn(`Public-domain verification was blocked by Cloudflare edge protection from this runner: ${error.message}`);
      return;
    }
    console.error(error.message);
    process.exitCode = 1;
  });
}
