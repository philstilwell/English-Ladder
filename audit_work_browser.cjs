/* Read-only browser audit of the work directory, categories, and every course.
   Start a local server first. Uses the existing Playwright/Chrome installation. */
const fs = require('node:fs');
const assert = require('node:assert/strict');
const {chromium} = require('playwright');
const base = process.env.AUDIT_ORIGIN || 'http://127.0.0.1:8878';
const output = process.env.AUDIT_OUTPUT || 'output/playwright/work-books-audit';
const medical = ['general-practitioners', 'oncologists', 'cardiologists', 'x-ray-technicians', 'pediatricians', 'obstetricians'];
const medicalPages = medical.map(slug => `efsp-${slug}.html`);
const specialists = ['nutrition-dietetics', 'sports-medicine', 'international-law', 'patent-law', 'university-professors', 'investment-management-banking', 'cross-border-ma-integration', 'localization-qa'];
const illustratedPages = [...medicalPages, ...specialists.map(slug => `efsp-${slug}.html`)];
const bookProofPages = ['cultural-leadership-us-branches', 'ai-development', 'pharmaceutical', 'cybersecurity', 'baristas-cafe-staff'].map(slug => `efsp-${slug}.html`);
const courses = fs.readdirSync('.').filter(name => /^efsp-.*\.html$/.test(name)).sort();
const categories = fs.readdirSync('english-for-work').filter(name => name.endsWith('.html')).map(name => `english-for-work/${name}`);
const paths = ['efsp.html', ...categories, ...courses];
const report = {
  date: new Date().toISOString().slice(0, 10), pages: paths.length,
  widths: [320, 390, 768, 1280], layouts: 0, expandedLayouts: 0,
  courseInteractions: 0, clozeInteractions: 0, noScriptPages: 0, medicalArtChecks: 0, bookArtChecks: 0, reviewInteractions: 0, titleSizes: [], errors: [],
  scope: 'All work pages at four widths, all lesson disclosures expanded, course interaction samples, keyboard navigation, deep links, and no-JavaScript reading. External requests blocked. Not a full accessibility or professional-content certification.',
};
fs.mkdirSync(output, {recursive: true});

async function geometry(page, path, width, expanded) {
  const result = await page.evaluate(() => ({
    overflow: document.documentElement.scrollWidth > innerWidth + 2,
    images: [...document.images].filter(image => image.getAttribute('src') && image.complete && !image.naturalWidth).map(image => image.src),
    headings: document.querySelectorAll('h1').length,
    // Native scrollers (prompt previews and the narrow lesson menu) may overflow internally.
    clipped: [...document.querySelectorAll('main h1, main h2, main h3, main h4, main p, main label, main summary')]
      .filter(node => node.checkVisibility() && node.scrollWidth > node.clientWidth + 2 && getComputedStyle(node).overflowX === 'visible')
      .map(node => node.textContent.slice(0, 100)).slice(0, 8),
  }));
  if (result.overflow || result.images.length || result.headings !== 1 || result.clipped.length) {
    report.errors.push({path, width, expanded, ...result});
  }
  report[expanded ? 'expandedLayouts' : 'layouts']++;
}

(async () => {
  const browser = await chromium.launch({channel: 'chrome', headless: true});
  try {
    for (const width of report.widths) {
      const context = await browser.newContext({viewport: {width, height: 900}, reducedMotion: 'reduce'});
      await context.route('**/*', route => route.request().url().startsWith(base) ? route.continue() : route.abort());
      const page = await context.newPage();
      let current = '';
      page.on('pageerror', error => report.errors.push({path: current, width, error: error.message}));
      const titleSizes = [];
      for (const path of ['efsp.html', 'us-life.html', 'grammar-concepts.html']) {
        current = path;
        await page.goto(`${base}/${path}`);
        titleSizes.push(await page.locator('h1').evaluate(node => getComputedStyle(node).fontSize));
      }
      report.titleSizes.push({width, work: titleSizes[0], everyday: titleSizes[1], grammar: titleSizes[2]});
      assert.equal(new Set(titleSizes).size, 1, `Shared title size at ${width}px`);
      for (const path of paths) {
        current = path;
        await page.goto(`${base}/${path}`);
        await page.evaluate(() => document.fonts.ready);
        await geometry(page, path, width, false);
        if (path === 'efsp.html') {
          const cells = await page.locator('.work-collage-cell').evaluateAll(nodes => nodes.map(node => {
            const {width, height, x, y} = node.getBoundingClientRect();
            return [width, height, x, y];
          }));
          assert.equal(cells.length, courses.length);
          assert.ok(cells.every(([w, h]) => Math.abs(w - cells[0][0]) < 1 && Math.abs(h - cells[0][1]) < 1));
          assert.equal(cells.length, 8 * 10, 'Eight columns and ten rows');
          assert.ok(cells.every(([w, h]) => Math.abs(w - h) < 1), 'Square, equally spaced cells');
          for (const [index, [w, h, x, y]] of cells.entries()) {
            assert.ok(Math.abs(x - cells[0][2] - (index % 8) * w) < 1, 'Even horizontal spacing');
            assert.ok(Math.abs(y - cells[0][3] - Math.floor(index / 8) * h) < 1, 'Even vertical spacing');
          }
        }
        const art = await page.locator('.work-medical-icon,.work-specialist-icon').evaluateAll(async nodes => {
          return Promise.all(nodes.map(async node => {
            const url = getComputedStyle(node).backgroundImage.match(/url\(["']?(.*?)["']?\)/)?.[1];
            const image = new Image();
            image.src = url || '';
            try { await image.decode(); } catch { return false; }
            return image.naturalWidth > 0 && image.naturalHeight > 0;
          }));
        });
        assert.ok(art.every(Boolean), `Profession illustrations load on ${path}`);
        if (illustratedPages.includes(path)) {
          assert.equal(art.length, 2, 'Both the course and sticky-menu illustration must load');
          report.medicalArtChecks += art.length;
          assert.equal(await page.locator('.work-conversation[open]').count(), 0);
        }
        if (['efsp.html', 'english-for-work/health-life-sciences.html', ...illustratedPages, ...bookProofPages].includes(path) && [390,1280].includes(width)) {
          await page.screenshot({path: `${output}/after-${path.replaceAll('/', '-')}-${width}.png`});
        }
        if (!courses.includes(path)) continue;
        const cover = page.locator('.work-book-art img');
        await cover.evaluate(image => image.decode());
        assert.ok(await cover.evaluate(image => {
          const box = image.getBoundingClientRect();
          // srcset reports density-corrected natural dimensions, not file pixels.
          return image.naturalWidth > 0 && box.width > 150 && Math.abs(box.width / box.height - image.naturalWidth / image.naturalHeight) < .01;
        }), 'Book artwork loads without stretching or cropping');
        report.bookArtChecks++;
        assert.equal(await page.locator('[data-work-quiz]').count(), 140);
        assert.equal(await page.locator('.work-review[open]').count(), 0);
        assert.equal(await page.locator('.work-accuracy[open],.work-second-take[open],.work-context-focus[open]').count(), 0);
        await page.locator('[data-expand-lessons]').click();
        assert.equal(await page.locator('.work-module[open]').count(), 8);
        // Reveal nested conversations, models, and complete prompt text too.
        await page.evaluate(() => document.querySelectorAll('main details').forEach(node => { node.open = true; }));
        await geometry(page, path, width, true);
        if (illustratedPages.includes(path) && [390,1280].includes(width)) {
          await page.locator('#module-1-cloze').scrollIntoViewIfNeeded();
          await page.screenshot({path: `${output}/dialogue-${path}-${width}.png`});
          await page.locator('#ai-practice').scrollIntoViewIfNeeded();
          assert.ok(await page.locator('.work-lesson-tools').evaluate(node => {
            const rect = node.getBoundingClientRect();
            return rect.top >= 0 && rect.bottom < innerHeight;
          }), 'Lesson menu remains visible at the prompts');
        }
        if (width === 390) {
          for (const selector of ['#review-1', '#module-1 .work-accuracy', '#module-1 .work-second-take']) {
            const question = page.locator(`${selector} [data-work-quiz]`).first();
            await question.locator(`input[value="${await question.getAttribute('data-correct')}"]`).check();
            await question.locator('[data-check-answer]').click();
            assert.equal(await question.locator('[data-quiz-feedback]').getAttribute('data-result'), 'correct');
            report.reviewInteractions++;
          }
          if (bookProofPages.includes(path)) {
            await page.locator('#review-1').evaluate(node => node.scrollIntoView({block: 'start'}));
            await page.screenshot({path: `${output}/review-${path}-${width}.png`});
          }
          const quiz = page.locator('[data-work-quiz]').first();
          const correct = await quiz.getAttribute('data-correct');
          await quiz.locator('[data-check-answer]').click();
          assert.match(await quiz.locator('[data-quiz-feedback]').innerText(), /Choose an answer/);
          await quiz.locator(`input[value="${correct}"]`).check();
          await quiz.locator('[data-check-answer]').click();
          assert.equal(await quiz.locator('[data-quiz-feedback]').getAttribute('data-result'), 'correct');
          for (const selector of ['#module-1-cloze', '#additional-1-cloze']) {
            const cloze = page.locator(selector);
            const answers = JSON.parse(await cloze.locator('[data-cloze-answers]').textContent());
            await cloze.locator('[data-check-cloze]').click();
            assert.match(await cloze.locator('[data-cloze-status]').innerText(), /unanswered/);
            for (let index = 0; index < answers.length; index++) {
              await cloze.locator('[data-cloze-gap]').nth(index).selectOption(answers[index].answer);
            }
            await cloze.locator('[data-check-cloze]').click();
            assert.equal(await cloze.locator('[data-cloze-status]').getAttribute('data-result'), 'correct');
            await cloze.locator('[data-reset-cloze]').click();
            assert.equal(await cloze.locator('[data-cloze-gap]').first().inputValue(), '');
            assert.equal(await cloze.locator('[data-cloze-gap]').first().evaluate(node => node === document.activeElement), true);
            report.clozeInteractions++;
          }
          await page.locator('[data-vocabulary-search]').fill('zzzz-no-matching-term');
          assert.equal(await page.locator('[data-work-term]:visible').count(), 0);
          await page.locator('[data-vocabulary-search]').fill('');
          assert.ok(await page.locator('[data-work-term]:visible').count());
          report.courseInteractions++;
        }
      }
      await context.close();
      console.log(`Checked ${paths.length} work pages at ${width}px, with all course disclosures expanded.`);
    }
    const context = await browser.newContext({viewport: {width: 390, height: 900}, reducedMotion: 'reduce'});
    await context.route('**/*', route => route.request().url().startsWith(base) ? route.continue() : route.abort());
    const page = await context.newPage();
    await page.goto(`${base}/efsp.html`);
    await page.locator('.work-directory-hero .work-button').click();
    assert.equal(new URL(page.url()).hash, '#courses');
    await page.locator('[data-course-search]').fill('CAFÉ-staff');
    assert.equal(await page.locator('[data-work-course-link]:visible').count(), 1);
    await page.locator('[data-course-category]').selectOption({label: 'Technology & data'});
    assert.equal(await page.locator('[data-course-empty]').isVisible(), true);
    await page.locator('[data-course-reset]').click();
    assert.equal(await page.locator('[data-work-course-link]:visible').count(), courses.length);
    assert.equal(await page.locator('[data-course-search]').evaluate(node => node === document.activeElement), true);
    await page.goto(`${base}/efsp-manufacturing.html`);
    await page.locator('.work-lesson-links a[href="#module-4"]').focus();
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('#module-4').getAttribute('open'), '');
    for (const id of ['module-8', 'module-4-cloze', 'review-1', 'review-4', 'professional-notes', 'additional-2', 'vocabulary', 'finished-module-4-roleplay', 'finished-dialogue-prompts', 'ai-practice']) {
      await page.goto(`${base}/efsp-manufacturing.html#${id}`);
      await page.evaluate(() => document.fonts.ready);
      await page.waitForFunction(id => {
        const node = document.getElementById(id);
        const top = node.getBoundingClientRect().top;
        const toolbar = document.querySelector('.work-lesson-tools').getBoundingClientRect();
        const masthead = document.querySelector('.site-masthead').getBoundingClientRect().bottom;
        const obstruction = toolbar.top <= masthead + 1 ? toolbar.bottom : masthead;
        return node.checkVisibility() && top >= obstruction && top < innerHeight;
      }, id).catch(error => { throw new Error(`Deep link #${id}: ${error.message}`); });
      if (id === 'vocabulary') assert.equal(await page.locator('#vocabulary').getAttribute('open'), '');
      if (id.startsWith('finished-module')) assert.equal(await page.locator('#module-4').getAttribute('open'), '');
    }
    // Exercise actual copying, then the manual selection fallback.
    await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
    await page.goto(`${base}/efsp-manufacturing.html#finished-module-1-roleplay`);
    const prompt = page.locator('#finished-module-1-roleplay');
    const copy = page.locator('[data-copy-finished="finished-module-1-roleplay"]');
    await copy.click();
    await page.waitForFunction(() => document.querySelector('[data-finished-status="finished-module-1-roleplay"]').textContent.includes('copied'));
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), await prompt.innerText());
    await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', {value: undefined, configurable: true}));
    await copy.click();
    assert.equal(await page.evaluate(() => getSelection().toString()), await prompt.innerText());
    await context.close();
    const noScript = await browser.newContext({javaScriptEnabled: false, viewport: {width: 390, height: 900}});
    await noScript.route('**/*', route => route.request().url().startsWith(base) ? route.continue() : route.abort());
    const staticPage = await noScript.newPage();
    for (const path of paths) {
      await staticPage.goto(`${base}/${path}`);
      if (path === 'efsp.html') {
        assert.equal(await staticPage.locator('[data-work-course-link]:visible').count(), courses.length);
        assert.equal(await staticPage.locator('[data-course-search]').isVisible(), false);
      }
      if (courses.includes(path)) {
        await staticPage.locator('#module-2 > summary').click();
        assert.equal(await staticPage.locator('#module-2 .work-case').isVisible(), true);
        await staticPage.locator('#module-2 .work-briefing-checks > summary').click();
        await staticPage.locator('#module-2 .work-answer > summary').first().click();
        assert.equal(await staticPage.locator('#module-2 .work-answer p').first().isVisible(), true);
        await staticPage.locator('#module-2 .work-extended-conversation > summary').click();
        await staticPage.locator('#module-2 .work-completed-script > summary').click();
        assert.equal(await staticPage.locator('#module-2 .work-completed-script li:visible').count(), 20);
        await staticPage.locator('#vocabulary > summary').click();
        assert.equal(await staticPage.locator('[data-vocabulary-search]').isVisible(), false);
        assert.ok(await staticPage.locator('[data-work-term]:visible').count());
        await staticPage.locator('#review-1 > summary').click();
        await staticPage.locator('#review-1 .work-answer > summary').first().click();
        assert.equal(await staticPage.locator('#review-1 .work-answer p').first().isVisible(), true);
      }
      report.noScriptPages++;
    }
    await noScript.close();
  } catch (error) {
    report.errors.push({error: error.stack});
  } finally {
    await browser.close();
    fs.writeFileSync(process.env.AUDIT_REPORT || `docs/work-browser-audit-${report.date}.json`, JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify(report, null, 2));
    if (report.errors.length) process.exitCode = 1;
  }
})();
