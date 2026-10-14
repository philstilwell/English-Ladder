/* Render only the approval edition. Never touches published course assets. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');

const root = __dirname;
const stem = 'cross-cultural-leadership-english-book-revised';
const folder = path.join(root, 'output', 'pdf');

async function main() {
  const browser = await chromium.launch({ headless: true,
    executablePath: process.env.CHROMIUM_EXECUTABLE || undefined });
  try {
    const page = await browser.newPage({ viewport: { width: 1000, height: 1200 } });
    await page.goto(pathToFileURL(path.join(folder, `${stem}.html`)).href);
    await page.emulateMedia({ media: 'print' });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(async () => Promise.all([...document.images].map(img => img.decode())));
    const report = await page.evaluate(() => {
      for (const original of [...document.querySelectorAll('[data-flow]')]) {
        const items = [...original.querySelector('.flow-items').children];
        original.querySelector('.flow-items').replaceChildren();
        let current = original;
        let part = 1;
        for (const item of items) {
          let container = current.querySelector('.flow-items');
          container.append(item);
          const limit = current.querySelector('.page-body').getBoundingClientRect().bottom;
          if (item.getBoundingClientRect().bottom > limit + 0.5) {
            item.remove();
            if (!container.children.length) throw new Error(`Oversized block: ${item.id || item.textContent.slice(0, 100)}`);
            const next = original.cloneNode(true);
            next.id = `${original.id}-continued-${++part}`;
            next.removeAttribute('data-flow');
            next.querySelector('.flow-items').replaceChildren();
            next.querySelector('.flow-heading').textContent = original.querySelector('.flow-heading').textContent + ' / continued';
            current.after(next);
            current = next;
            container = next.querySelector('.flow-items');
            container.append(item);
            if (item.getBoundingClientRect().bottom > next.querySelector('.page-body').getBoundingClientRect().bottom + .5) {
              throw new Error(`Oversized individual key: ${item.id}`);
            }
          }
        }
      }
      const sheets = [...document.querySelectorAll('.sheet')];
      sheets.forEach((sheet, i) => {
        sheet.dataset.page = i + 1;
        sheet.classList.toggle('even', (i + 1) % 2 === 0);
        sheet.querySelector('.page-number').textContent = String(i + 1).padStart(2, '0');
      });
      for (const span of document.querySelectorAll('[data-page-ref]')) {
        const target = document.getElementById(span.dataset.pageRef);
        if (!target) throw new Error(`Missing page-reference target: ${span.dataset.pageRef}`);
        span.textContent = target.closest('.sheet').dataset.page;
      }
      const duplicateIds = [...document.querySelectorAll('[id]')].map(x => x.id).filter((x, i, all) => all.indexOf(x) !== i);
      const invalidLinks = [...document.querySelectorAll('a[href^="#"]')].filter(a => !document.getElementById(a.hash.slice(1))).map(a => a.hash);
      const overflows = [];
      const pageStats = sheets.map(sheet => {
        const body = sheet.querySelector('.page-body');
        const box = body.getBoundingClientRect();
        let bottom = box.top;
        const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT);
        while (walker.nextNode()) {
          const node = walker.currentNode;
          if (!node.textContent.trim()) continue;
          const range = document.createRange();
          range.selectNodeContents(node);
          for (const r of range.getClientRects()) {
            bottom = Math.max(bottom, r.bottom);
            if (r.bottom > box.bottom + .75 || r.left < box.left - 1 || r.right > box.right + 1) {
              overflows.push({ page: +sheet.dataset.page, id: sheet.id, text: node.textContent.slice(0, 100),
                excessBottom: +(r.bottom - box.bottom).toFixed(1), excessRight: +(r.right - box.right).toFixed(1) });
            }
          }
        }
        for (const img of body.querySelectorAll('img')) {
          const r = img.getBoundingClientRect();
          bottom = Math.max(bottom, r.bottom);
          if (r.bottom > box.bottom + .75 || r.left < box.left - 1 || r.right > box.right + 1) {
            overflows.push({ page: +sheet.dataset.page, id: sheet.id, image: img.src });
          }
        }
        return { page: +sheet.dataset.page, id: sheet.id, usedHeight: +(bottom - box.top).toFixed(1), availableHeight: +box.height.toFixed(1), words: body.innerText.split(/\s+/).length };
      });
      const blanks = [...document.querySelectorAll('.blank')].map(b => b.getBoundingClientRect().width);
      return { pages: sheets.length, pageStats, overflows, invalidLinks, duplicateIds,
        blankCount: blanks.length, minBlankWidth: Math.min(...blanks), maxBlankWidth: Math.max(...blanks) };
    });
    fs.writeFileSync(path.join(folder, `${stem}-layout.json`), JSON.stringify(report, null, 2) + '\n');
    if (report.overflows.length || report.invalidLinks.length || report.duplicateIds.length) {
      console.error(JSON.stringify({ overflows: report.overflows, invalidLinks: report.invalidLinks, duplicateIds: report.duplicateIds }, null, 2));
      throw new Error('Layout validation failed; PDF was not replaced.');
    }
    // Save the paginated HTML so the review copy has working page references too.
    await page.evaluate(() => document.querySelectorAll('[data-flow]').forEach(el => el.removeAttribute('data-flow')));
    fs.writeFileSync(path.join(folder, `${stem}.html`), await page.content());
    await page.pdf({ path: path.join(folder, `${stem}.pdf`), preferCSSPageSize: true,
      printBackground: true, tagged: true, outline: true });
    const previewFolder = path.join(root, 'tmp', 'pdfs', 'leadership-pilot');
    fs.mkdirSync(previewFolder, { recursive: true });
    for (const id of ['cover', 'u1-a', 'u1-b1', 'u1-c', 'u2-e', 'u2-e-continued', 'u4-transfer', 'review-4', 'key-u1', 'index']) {
      await page.locator(`#${id}`).screenshot({ path: path.join(previewFolder, `${id}.png`) });
    }
    console.log(JSON.stringify({ pdf: `${stem}.pdf`, pages: report.pages, blanks: report.blankCount, overflows: 0 }));
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
