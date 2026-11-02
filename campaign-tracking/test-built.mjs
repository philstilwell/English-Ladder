// Run against Wrangler's emitted worker, so serialization cannot hide bundler helpers.
import {readFile} from 'node:fs/promises';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const source=await readFile(process.argv[2],'utf8');
const worker=(await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'))).default;
let injection,tick;
globalThis.HTMLRewriter=class {on(_selector,handler){handler.element({prepend(value){injection=value;}});return this;}transform(response){return response;}};
globalThis.fetch=async()=>new Response('<html><head></head><body>Lesson</body></html>',{headers:{'Content-Type':'text/html'}});
const env={DB:{prepare(){return {bind(){return this;},async first(){return {id:'qa-built',site:'englishladder.com',target:'/grammar-concepts/concept-12.html',source:'reddit',status:'test'};},async run(){}};}}};
const response=await worker.fetch(new Request('https://englishladder.com/campaign/qa-built'),env);
assert.equal(response.status,200);
const script=injection.match(/<script data-campaign-tracker>([\s\S]*)<\/script>/)[1];
vm.runInNewContext(script,{URL,location:{origin:'https://englishladder.com',hash:''},history:{state:null,replaceState(){}},performance:{now:()=>0},navigator:{},document:{visibilityState:'visible'},addEventListener(){},setInterval(f){tick=f;return 1;},clearInterval(){},fetch:async()=>({ok:true})});
assert.equal(typeof tick,'function');
console.log('PASS: deployed bundle produces a self-contained browser tracker');
