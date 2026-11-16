'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const root = path.resolve(__dirname, '..');

test('packaged PDF canonicals preserve downloads, cache policy, and query-independent paths', () => {
  cp.execFileSync(process.execPath, ['cloudflare/build.cjs'], {cwd: root});
  const headers = fs.readFileSync(path.join(root, '.cf-site/_headers'), 'utf8');
  const redirects = fs.readFileSync(path.join(root, '.cf-site/_redirects'), 'utf8');
  const domain = fs.readFileSync(path.join(root, 'CNAME'), 'utf8').trim();
  const slugs = ['banking-operations', 'medical-assistants', 'marketing', 'sports-medicine'];
  assert.equal((headers.match(/rel="canonical"/g) || []).length, 4);
  for (const slug of slugs) {
    const file = `pdf/efsp/${slug}-english-book.pdf`;
    assert.ok(headers.includes(`/${file}\n  Link: <https://${domain}/${file}>; rel="canonical"\n`));
    assert.deepEqual(fs.readFileSync(path.join(root, '.cf-site', file)), fs.readFileSync(path.join(root, file)));
    assert.ok(!redirects.includes(file));
  }
  assert.ok(headers.includes('Cache-Control: public, max-age=0, must-revalidate'));
  assert.ok(!headers.includes('Content-Disposition'));
  assert.ok(!headers.includes('?'));
  assert.ok(headers.includes('https://:worker.philstilwell.workers.dev/*\n  X-Robots-Tag: noindex, nofollow'));
});
