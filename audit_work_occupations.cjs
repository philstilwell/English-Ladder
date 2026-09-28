// Inspect every occupation page in a real browser at narrow and desktop widths.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const {chromium} = require('playwright');

const root = __dirname;
const base = process.env.AUDIT_ORIGIN || 'http://127.0.0.1:8878';
const output = path.join(root, 'tmp/occupation-review');
const slugs = JSON.parse(execFileSync('python3', ['-c',
  'import json; from work_occupations import OCCUPATION_SLUGS; print(json.dumps(OCCUPATION_SLUGS))'],
  {cwd:root, encoding:'utf8'}));

(async () => {
  fs.mkdirSync(output, {recursive:true});
  const browser = await chromium.launch({channel:'chrome', headless:true});
  const contentHash = execFileSync('python3', ['-c',
    'from work_curriculum import content_hash; print(content_hash())'], {cwd:root, encoding:'utf8'}).trim();
  const report = {edition:'2026-09-28', contentHash, courses:slugs.length, widths:[320,390,1280], checks:0, failures:[], samples:[]};
  try {
    for (const width of report.widths) {
      const context = await browser.newContext({viewport:{width,height:900}});
      const page = await context.newPage();
      let current = '';
      page.on('pageerror', error => report.failures.push({width,course:current,error:error.message}));
      await page.route('**/*', route => route.request().url().startsWith(base) ? route.continue() : route.abort());
      for (const slug of slugs) {
        current = slug;
        try {
          const response = await page.goto(`${base}/efsp-${slug}.html`, {waitUntil:'load'});
          assert.equal(response.status(), 200);
          assert.equal(await page.locator('.work-module').count(), 8);
          assert.equal(await page.locator('.work-conversation').count(), 24);
          assert.equal(await page.locator('.work-conversation[open]').count(), 0);
          assert.equal(await page.locator('.work-speaking-scenario').count(), 16);
          assert.equal(await page.locator('.work-download').count(), 4);
          const icon = page.locator('.work-hero .work-occupation-icon');
          assert.equal(await icon.count(), 1);
          assert.ok(await icon.evaluate(async element => {
            const url = getComputedStyle(element).backgroundImage.match(/url\(["']?(.*?)["']?\)/)[1];
            const image = new Image(); image.src = url; await image.decode();
            return image.naturalWidth > 0;
          }));
          const conversation = page.locator('.work-conversation').first();
          await conversation.locator('summary').click();
          assert.equal(await conversation.locator('ol > li').count(), 10);
          assert.equal(await conversation.getAttribute('open'), '');
          await conversation.locator('summary').click();
          const quiz = page.locator('[data-work-quiz]').first();
          const inputs = quiz.locator('input[type=radio]');
          const correct = Number(await quiz.getAttribute('data-correct'));
          assert.equal(await inputs.count(), 4);
          for (let index=0; index<4; index++) {
            await inputs.nth(index).check();
            await quiz.locator('[data-check-answer]').click();
            assert.equal(await quiz.locator('[data-quiz-feedback]').getAttribute('data-result'), index===correct ? 'correct' : 'retry');
          }
          await page.locator('[data-expand-lessons]').click();
          assert.equal(await page.locator('.work-module[open]').count(), 8);
          const geometry = await page.evaluate(() => ({
            width:innerWidth, scrollWidth:document.documentElement.scrollWidth,
            overflow:[...document.querySelectorAll('.work-module *, .work-hero *, .work-downloads *')]
              .filter(element => {const r=element.getBoundingClientRect();return r.width>0 && (r.left < -2 || r.right>innerWidth+2);})
              .slice(0,8).map(element=>({tag:element.tagName,class:element.className,text:element.textContent.slice(0,80)})),
            failedImages:[...document.images].filter(image=>image.getAttribute('src') && image.complete && !image.naturalWidth).map(image=>image.src),
          }));
          assert.ok(geometry.scrollWidth <= width+2 && geometry.overflow.length===0, JSON.stringify(geometry));
          assert.equal(geometry.failedImages.length, 0);
          if (width!==320) {
            await page.evaluate(()=>scrollTo(0,0));
            const name=`${slug}-${width}.png`;
            await page.screenshot({path:path.join(output,name)});
            report.samples.push(name);
          }
          report.checks++;
        } catch(error) {
          report.failures.push({course:slug,width,error:error.message});
        }
      }
      current = 'directory';
      await page.goto(`${base}/efsp.html`,{waitUntil:'load'});
      assert.equal(await page.locator('[data-work-course-link]').count(),66);
      await page.locator('[data-course-search]').fill('carpentry');
      assert.ok(await page.locator('[data-work-course-link]:visible').count()>0);
      await page.locator('[data-course-search]').fill('zz-no-such-occupation');
      assert.equal(await page.locator('[data-course-empty]').isVisible(),true);
      await context.close();
      console.log(`Occupation pages checked at ${width}px.`);
    }
  } finally {
    await browser.close();
  }
  fs.writeFileSync(path.join(root,'docs/occupation-browser-audit-2026-09-28.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  if(report.failures.length)process.exitCode=1;
})().catch(error=>{console.error(error);process.exitCode=1;});
