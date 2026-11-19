const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {JSDOM}=require('jsdom');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'grammar-concepts.html'),'utf8');
const script=fs.readFileSync(path.join(root,'power-grammar.js'),'utf8');
test('shared exercise links open the containing set without revealing its answer',()=>{
 const dom=new JSDOM(html,{url:'https://englishladder.com/grammar-concepts.html#power-grammar-157',runScripts:'outside-only'});
 try {
  dom.window.requestAnimationFrame=fn=>fn();
  dom.window.HTMLElement.prototype.scrollIntoView=()=>{};
  dom.window.eval(script);
  const doc=dom.window.document;
  assert.equal(doc.querySelector('#power-grammar-set-16').open,true);
  assert.equal(doc.querySelector('#power-grammar-157 .pg-answer').open,false);
  assert.equal(doc.querySelectorAll('.pg-set[open]').length,1);
  dom.window.location.hash='#power-grammar-set-20';
  dom.window.dispatchEvent(new dom.window.Event('hashchange'));
  assert.equal(doc.querySelector('#power-grammar-set-20').open,true);
  dom.window.location.hash='#power-grammar-999';
  assert.doesNotThrow(()=>dom.window.dispatchEvent(new dom.window.Event('hashchange')));
 } finally {dom.window.close();}
});
