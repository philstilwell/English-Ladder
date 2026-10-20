'use strict';
// Read and hash only the daily release files. Do not rebuild or package the site.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {currentLessonFiles, verifyCurrentLesson} = require('./verify-current-lesson.cjs');
const {createCurlRequest, verifyResponse} = require('./verify.cjs');

async function checkDailyPublication({root, releaseDate, origin, request, sleep}) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(releaseDate)) throw new Error('A release date is required.');
  const image = JSON.parse(fs.readFileSync(path.join(root, 'assets/news', `${releaseDate}.json`), 'utf8'));
  if (!new RegExp(`^assets/news/${releaseDate}-[a-f0-9]{12}\\.webp$`).test(image.path)) {
    throw new Error('The daily illustration path is invalid.');
  }
  const files = [...currentLessonFiles(releaseDate), image.path];
  const manifest = {files: Object.fromEntries(files.map(file => [
    file, crypto.createHash('sha256').update(fs.readFileSync(path.join(root, file))).digest('hex'),
  ]))};
  await verifyCurrentLesson(manifest, {origin, request, releaseDate, sleep});
  await verifyResponse(image.path, {origin, request, expectedHash: manifest.files[image.path], sleep});
  return {releaseDate, files: files.length};
}

module.exports = {checkDailyPublication};
if (require.main === module) {
  const origin = new URL('https://englishladder.philstilwell.workers.dev');
  checkDailyPublication({
    root: path.resolve(__dirname, '..'), releaseDate: process.argv[2],
    origin, request: createCurlRequest(origin),
  }).then(result => {
    console.log(`Verified the saved ${result.releaseDate} edition and illustration on the live host.`);
  }).catch(error => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
