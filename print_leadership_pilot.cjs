/* Render only the approval edition. Never touches published course assets. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');

const root = __dirname;
const stem = process.argv[2] || 'cross-cultural-leadership-english-book-revised';
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
            next.dataset.continuedFrom = original.id;
            next.querySelector('.flow-items').replaceChildren();
            // Keep the cloned heading's circular letter and other inline formatting.
            next.querySelector('.flow-heading').append(' / continued');
            current.after(next);
            current = next;
            container = next.querySelector('.flow-items');
            container.append(item);
            if (item.getBoundingClientRect().bottom > next.querySelector('.page-body').getBoundingClientRect().bottom + .5) {
              throw new Error(`Oversized individual key: ${item.id}`);
            }
          }
        }
        // Avoid a nearly empty continuation page after a single long block.
        if (current !== original) {
          const previous = current.previousElementSibling;
          const lastItems = current.querySelector('.flow-items');
          const previousItems = previous.querySelector('.flow-items');
          while (lastItems.getBoundingClientRect().height < 240 && previousItems.children.length > 1) {
            const candidate = previousItems.lastElementChild;
            lastItems.prepend(candidate);
            if (lastItems.getBoundingClientRect().bottom > current.querySelector('.page-body').getBoundingClientRect().bottom + .5) {
              previousItems.append(candidate);
              break;
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
      const headingErrors = [];
      const continuationHeadings = [...document.querySelectorAll('[data-continued-from]')].map(sheet => {
        const source = document.getElementById(sheet.dataset.continuedFrom);
        const heading = sheet.querySelector('.flow-heading');
        const expected = source.querySelector('.flow-heading').cloneNode(true);
        expected.append(' / continued');
        if (heading.innerHTML !== expected.innerHTML) headingErrors.push(sheet.id);
        return { id: sheet.id, source: source.id, page: +sheet.dataset.page,
          letter: heading.querySelector('.section-letter')?.textContent || null };
      });
      const sectionLetters = [...document.querySelectorAll('.page-body h2 .section-letter')].map(letter => {
        const sheet = letter.closest('.sheet');
        const rect = letter.getBoundingClientRect();
        const pageRect = sheet.getBoundingClientRect();
        const style = getComputedStyle(letter);
        if (style.borderRadius !== '50%' || style.color !== 'rgb(255, 255, 255)' ||
            Math.abs(rect.width - 36) > .1 || Math.abs(rect.height - 36) > .1 ||
            style.backgroundColor === 'rgba(0, 0, 0, 0)') headingErrors.push(sheet.id);
        return { id: sheet.id, page: +sheet.dataset.page, letter: letter.textContent,
          x: +(rect.left - pageRect.left).toFixed(3), y: +(rect.top - pageRect.top).toFixed(3),
          width: rect.width, height: rect.height, color: style.backgroundColor };
      });
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
      const anchors = Object.fromEntries([...document.querySelectorAll('[id]')]
        .filter(el => el.closest('.sheet')).map(el => [el.id, +el.closest('.sheet').dataset.page]));
      return { pages: sheets.length, pageStats, anchors, overflows, invalidLinks, duplicateIds,
        continuationHeadings, sectionLetters, headingErrors,
        blankCount: blanks.length, minBlankWidth: Math.min(...blanks), maxBlankWidth: Math.max(...blanks) };
    });
    fs.writeFileSync(path.join(folder, `${stem}-layout.json`), JSON.stringify(report, null, 2) + '\n');
    if (report.overflows.length || report.invalidLinks.length || report.duplicateIds.length || report.headingErrors.length) {
      console.error(JSON.stringify({ overflows: report.overflows, invalidLinks: report.invalidLinks, duplicateIds: report.duplicateIds, headingErrors: report.headingErrors }, null, 2));
      throw new Error('Layout validation failed; PDF was not replaced.');
    }
    // Save the paginated HTML so the review copy has working page references too.
    await page.evaluate(() => document.querySelectorAll('[data-flow]').forEach(el => el.removeAttribute('data-flow')));
    fs.writeFileSync(path.join(folder, `${stem}.html`), await page.content());
    await page.pdf({ path: path.join(folder, `${stem}.pdf`), preferCSSPageSize: true,
      printBackground: true, tagged: true, outline: true });
    const previewFolder = path.join(root, 'tmp', 'pdfs', stem);
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
