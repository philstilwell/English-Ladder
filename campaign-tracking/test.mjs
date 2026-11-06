import {test} from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import worker,{validTarget,bucketFor} from './worker.mjs';
import {browserTracker} from './client.mjs';
const published={status:'published'};
const req=(options={})=>new Request('https://englishladder.com/campaign/el-nov02-test',options);
test('campaign destinations exclude administration, malformed URLs, external redirects and PDFs',()=>{
 assert(validTarget('englishladder.com','/grammar-concepts/concept-12.html'));
 assert(validTarget('englishladder.com','/efsp-hospitality-tourism.html'));
 assert(validTarget('slugfester.com','/debate/swinburne-ehrman-god-suffering-2009/'));
 assert(validTarget('slugfester.com','/'));
 assert(!validTarget('englishladder.com','/'));
 assert(!validTarget('slugfester.com','/interlocutor/private/'));
 for(const path of ['/backend/','//evil.com','/debate/test/The','/debate/../backend/','/debate/a/?x=1','/debate/a/%2e']) assert(!validTarget('slugfester.com',path));
 assert(!validTarget('evil.com','/debate/a/'));
});
test('internal, test and known bots cannot enter the audience bucket',()=>{
 assert.equal(bucketFor(req(),published),'audience');
 assert.equal(bucketFor(req({headers:{Cookie:'campaign_traffic=internal'}}),published),'internal');
 assert.equal(bucketFor(req({headers:{Cookie:'campaign_traffic=test'}}),published),'test');
 assert.equal(bucketFor(req({headers:{'User-Agent':'facebookexternalhit/1.1'}}),published),'bot');
 assert.equal(bucketFor(req({headers:{'Sec-Purpose':'prefetch'}}),published),'bot');
 assert.equal(bucketFor(req(),{status:'draft'}),'test');
 assert.equal(bucketFor(req(),{status:'test'}),'test');
 assert.equal(bucketFor(req(),{status:'ended'}),'audience');
});
test('collector rejects unknown host, cross-origin posts and invalid events before database access',async()=>{
 const env={DB:{prepare(){throw Error('DB should not be read');}}};
 assert.equal((await worker.fetch(new Request('https://evil.com/campaign/event'),env)).status,404);
 assert.equal((await worker.fetch(new Request('https://englishladder.com/campaign/event',{method:'POST',headers:{Origin:'https://evil.com'}}),env)).status,403);
 assert.equal((await worker.fetch(new Request('https://englishladder.com/campaign/event',{method:'POST',headers:{Origin:'https://englishladder.com','Content-Type':'application/json'},body:'{"visit":"bad","event":"engaged"}'}),env)).status,400);
});
test('client counts visibility, requires trusted interaction, and sends each stage once',async()=>{
 let now=0,tick;const events={},sent=[];
 const context={URL,location:{origin:'https://englishladder.com',hash:''},history:{state:null,replaceState(){}},performance:{now:()=>now},navigator:{webdriver:false},document:{visibilityState:'hidden'},addEventListener:(t,f)=>{events[t]=f;},setInterval:f=>{tick=f;return 1;},clearInterval(){},fetch:async(_u,o)=>{sent.push(JSON.parse(o.body));return {ok:true};}};
 vm.runInNewContext(`(${browserTracker.toString()})(${JSON.stringify({visit:'v',campaign:'c',target:'/grammar-concepts/concept-12.html',source:'reddit'})})`,context);
 for(let i=0;i<15;i++){now+=1000;await tick();}assert.equal(sent.length,0);
 context.document.visibilityState='visible';now+=1000;await tick();assert.equal(sent[0].event,'arrival');
 events.pointerdown({isTrusted:false});for(let i=0;i<15;i++){now+=1000;await tick();}assert.equal(sent.length,1);
 events.keydown({isTrusted:true});now+=1000;await tick();assert.equal(sent[1].event,'engaged');
 now+=1000;await tick();assert.equal(sent.length,2);
});
test('collector requires a recent same-site visit and elapsed visible interaction before engagement',async()=>{
 const visit='12345678-1234-4234-8234-123456789012';
 let row={id:visit,site:'englishladder.com',bucket:'audience',created_at:Date.now()-15000,arrived:1};
 const writes=[];
 const env={DB:{prepare(sql){return {bind(){return this;},async first(){return row;},async run(){writes.push(sql);}};}}};
 const send=data=>worker.fetch(new Request('https://englishladder.com/campaign/event',{method:'POST',headers:{Origin:'https://englishladder.com','Content-Type':'application/json'},body:JSON.stringify({visit,event:'engaged',visibleMs:15000,interacted:true,...data})}),env);
 assert.equal((await send({interacted:false})).status,400);
 assert.equal((await send({visibleMs:9000})).status,400);
 row.arrived=0;assert.equal((await send({})).status,400);
 row.arrived=1;row.created_at=Date.now()-8000000;assert.equal((await send({})).status,400);
 row.created_at=Date.now()-15000;row.site='slugfester.com';assert.equal((await send({})).status,400);
 row.site='englishladder.com';assert.equal((await send({})).status,204);
 assert.equal(writes.length,1);
 assert.match(writes[0],/AND engaged=0/);
});
test('privacy opt-outs disable browser events and network failures have a bounded retry budget',async()=>{
 for(const privacy of [{doNotTrack:'1'},{globalPrivacyControl:true},{}]){
  let now=0,tick,stopped=false,sends=0;
  const context={URL,location:{origin:'https://englishladder.com',hash:''},history:{state:null,replaceState(){}},performance:{now:()=>now},navigator:privacy,document:{visibilityState:'visible'},addEventListener(){},setInterval:f=>{tick=f;return 1;},clearInterval(){stopped=true;},fetch:async()=>{sends++;throw Error('offline');}};
  vm.runInNewContext(`(${browserTracker.toString()})({target:'/grammar-concepts/concept-12.html',source:'reddit',campaign:'c',visit:'v'})`,context);
  if(Object.keys(privacy).length){assert.equal(tick,undefined);continue;}
  for(let i=0;i<12&&!stopped;i++){now+=1000;await tick();}
  assert(stopped);assert.equal(sends,6);
 }
});
