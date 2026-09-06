const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.join(__dirname,'..');
const script = fs.readFileSync(path.join(root,'ai-practice.js'),'utf8');

function setup(clipboard) {
  const dom = new JSDOM(fs.readFileSync(path.join(root,'grammar-concepts/concept-35.html'),'utf8'), {url:'https://englishladder.com/grammar-concepts/concept-35.html',runScripts:'outside-only'});
  if (clipboard) Object.defineProperty(dom.window.navigator,'clipboard',{value:clipboard});
  dom.window.eval(script);
  return dom;
}
const settle = () => new Promise(resolve => setImmediate(resolve));

test('copying uses the exact chosen published prompt, with no answer or draft fields', async () => {
  let copied;
  const dom = setup({writeText:async value => {copied=value;}});
  const doc=dom.window.document;
  const button=doc.querySelectorAll('[data-ai-copy]')[1];
  const prompt=doc.getElementById(button.dataset.aiCopy);
  assert.equal(button.hidden,false);
  button.click(); await settle();
  assert.equal(copied,prompt.textContent);
  assert.match(copied,/six-line exchange/);
  assert.match(copied,/Could commonly describes a general past ability/);
  assert.match(button.closest('[data-ai-card]').querySelector('[data-ai-status]').textContent,/Prompt copied/);
  assert.equal(doc.querySelectorAll('textarea,input[type="text"]').length,0);
  dom.window.close();
});

for (const denied of [false,true]) test(`manual selection works when the clipboard is ${denied?'blocked':'unavailable'}`, async () => {
  const dom = setup(denied?{writeText:async()=>{throw new Error('Denied');}}:undefined);
  const doc=dom.window.document,button=doc.querySelector('[data-ai-copy]');
  const prompt=doc.getElementById(button.dataset.aiCopy);
  button.click(); await settle();
  assert.equal(prompt.closest('details').open,true);
  assert.equal(dom.window.getSelection().toString(),prompt.textContent);
  assert.equal(doc.activeElement,prompt);
  assert.equal(button.disabled,false);
  assert.match(button.closest('[data-ai-card]').querySelector('[data-ai-status]').textContent,/Automatic copying is unavailable/);
  dom.window.close();
});

test('copy status stays with the selected card and repeated copying does not change a prompt', async () => {
  const copies=[];
  const dom=setup({writeText:async text=>copies.push(text)}),doc=dom.window.document;
  const buttons=[...doc.querySelectorAll('[data-ai-copy]')];
  buttons[0].click(); await settle(); buttons[2].click(); await settle(); buttons[0].click(); await settle();
  assert.equal(copies[0],copies[2]); assert.notEqual(copies[0],copies[1]);
  assert.equal(buttons[1].closest('[data-ai-card]').querySelector('[data-ai-status]').textContent,'');
  dom.window.close();
});
