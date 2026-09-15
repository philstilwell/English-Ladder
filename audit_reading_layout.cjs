/* Browser regression audit. Uses installed Chrome; never calls a paid service. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {chromium} = require('playwright');
const base = (process.env.AUDIT_ORIGIN || 'http://127.0.0.1:8768').replace(/\/$/, '');
const widths = (process.env.AUDIT_WIDTHS || '320,390,768,1280').split(',').map(Number);
const ids = [...fs.readFileSync('beginner.html', 'utf8').matchAll(/id="(lesson-\d{4}-\d{2}-\d{2})"/g)].map(match => match[1]);
const date = ids[0].slice(7);
const paths = ['index.html', 'beginner.html', `beginner.html#${ids[0]}`,
  `intermediate.html#${ids[2]}`, `advanced.html#${ids[4]}`,
  ...['beginner','intermediate','advanced'].map(level => `news/${date}/${level}.html`),
  'stories/city-trees/beginner.html'];
const report = {date: new Date().toISOString(), origin: base, scriptDelayMs: 1500,
  scope: 'Cold navigation with deferred scripts delayed; fresh and returning readers. Separate no-script, failed-download, navigation, and script-scroll checks. Lab measurements, not visitor analytics.',
  measurements: [], fallbacks: [], errors: []};
const output = process.env.AUDIT_REPORT || 'output/playwright/reading-layout.json';

(async () => {
 const browser = await chromium.launch({channel: 'chrome', headless: true});
 try {
  for (const width of widths) for (const saved of [false, true]) {
   for (const path of paths) {
    const context = await browser.newContext({viewport: {width, height: 900}});
    try {
     await context.addInitScript(({saved, ids}) => {
      if (saved) {
       localStorage.setItem('english-ladder-vocabulary-language-v1', 'ja');
       for (const id of ids) for (const level of ['beginner','intermediate','advanced']) {
        localStorage.setItem(`english-ladder-completed-v1:news/${id.slice(7)}/${level}.html`, '1');
       }
      }
      window.layoutShifts = [];
      new PerformanceObserver(list => {
       for (const entry of list.getEntries()) if (!entry.hadRecentInput) {
        window.layoutShifts.push({value: entry.value, time: entry.startTime,
         elements: entry.sources.map(source => source.node?.id || source.node?.className || source.node?.nodeName)});
       }
      }).observe({type: 'layout-shift', buffered: true});
     }, {saved, ids});
     const page = await context.newPage();
     page.on('pageerror', error => report.errors.push({path, width, saved, error: error.message}));
     await page.route('**/*', async route => {
      const url = route.request().url();
      if (!url.startsWith(base+'/')) return route.abort();
      if (/\/(app|learning|site|ai-practice)\.js(?:\?|$)/.test(url)) await new Promise(resolve => setTimeout(resolve, 1500));
      await route.continue();
     });
     await page.goto(base+'/'+path, {waitUntil: 'networkidle'});
     const measured = await page.evaluate(() => {
      let cls=0, sum=0, first=0, last=0;
      for (const entry of window.layoutShifts) {
       if (entry.time-last > 1000 || entry.time-first > 5000) {sum=0; first=entry.time;}
       sum += entry.value; last=entry.time; cls=Math.max(cls,sum);
      }
      return {cls, shifts: window.layoutShifts, overflow: document.documentElement.scrollWidth > innerWidth+1};
     });
     report.measurements.push({path, width, saved, ...measured});
     assert.ok(measured.cls <= 0.1, `${path} at ${width}, saved=${saved}: CLS ${measured.cls}`);
     assert.equal(measured.overflow, false, `${path}: horizontal overflow`);
     const lesson = page.locator('.daily-lesson[open]').first();
     if (await lesson.count()) {
      await lesson.locator('.learning-flow button').nth(1).click();
      assert.equal(await lesson.locator('[data-stage="practice"]').isVisible(), true);
      await lesson.locator('.learning-flow button').nth(2).click();
      assert.equal(await lesson.locator('[data-stage="discuss"]').isVisible(), true);
      await lesson.locator('.learning-flow button').nth(0).click();
      assert.equal(await lesson.locator('[data-stage="read"]').isVisible(), true);
     }
    } finally {await context.close();}
   }
   console.log(`Layout audit: ${width}px, ${saved ? 'saved preferences' : 'fresh reader'} passed.`);
  }
  for (const disabled of [true, false]) {
   const context = await browser.newContext({javaScriptEnabled: !disabled, viewport:{width:390,height:900}});
   try {
    const page = await context.newPage();
    if (!disabled) await page.route('**/learning.js*', route => route.abort());
    await page.goto(base+`/news/${date}/beginner.html`, {waitUntil:'networkidle'});
    for (const stage of ['read','practice','discuss']) assert.equal(await page.locator(`[data-stage="${stage}"]`).isVisible(), true);
    assert.equal(await page.locator('.learning-flow').isVisible(), false);
    report.fallbacks.push({mode:disabled ? 'JavaScript disabled' : 'Interaction download failed', passed:true});
   } finally {await context.close();}
  }
  // Our deferred scripts must not repeat the browser's native fragment navigation.
  const context = await browser.newContext({viewport:{width:390,height:900}});
  try {
   const page=await context.newPage();
   await page.addInitScript(() => {
    window.scriptScrolls=[];
    const original=Element.prototype.scrollIntoView;
    Element.prototype.scrollIntoView=function(...args){window.scriptScrolls.push(this.id);return original.apply(this,args);};
   });
   let release;
   const gate=new Promise(resolve => {release=resolve;});
   await page.route(/\/(app|learning|site|ai-practice)\.js(?:\?.*)?$/, async route=>{await gate;await route.continue();});
   await page.goto(base+`/beginner.html#${ids[0]}`, {waitUntil:'commit'});
   await page.locator('.reading-js .daily-lesson[open] .learning-flow').waitFor({state:'visible'});
   await page.mouse.wheel(0,500);
   await page.waitForTimeout(100);
   const before=await page.evaluate(()=>scrollY);
   release();
   await page.waitForLoadState('networkidle');
   assert.deepEqual(await page.evaluate(()=>window.scriptScrolls), [], 'Deferred scripts repeat fragment scrolling');
   report.fallbacks.push({mode:'No repeated script-driven fragment scroll',passed:true,
    nativeFragmentPosition:{before,after:await page.evaluate(()=>scrollY)}});
  } finally {await context.close();}
  assert.deepEqual(report.errors, []);
  report.maxCLS=Math.max(...report.measurements.map(row=>row.cls));
  report.passed=true;
  console.log(`Passed ${report.measurements.length} layout measurements and ${report.fallbacks.length} fallback/scroll checks. Maximum CLS: ${report.maxCLS.toFixed(4)}.`);
 } finally {
  await browser.close();
  fs.mkdirSync(require('node:path').dirname(output), {recursive:true});
  fs.writeFileSync(output, JSON.stringify(report,null,2)+'\n');
 }
})().catch(error=>{console.error(error);process.exitCode=1;});
