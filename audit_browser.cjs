const fs = require('fs');
const {chromium} = require(process.cwd() + '/node_modules/playwright');
const {execFileSync} = require('child_process');
const date = new Date().toISOString().slice(0,10);
const base = process.env.AUDIT_ORIGIN || 'http://127.0.0.1:8878';
const output = 'output/playwright';
fs.mkdirSync(output,{recursive:true});
(async () => {
 const paths=JSON.parse(execFileSync('python3',['-c','import json;from seo import published_pages,ROOT;print(json.dumps([str(p.relative_to(ROOT)) for p in published_pages()]))'],{encoding:'utf8'}));
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const report={date, scope:'Every published page at four widths; first feed lesson opened; empty, uninitialized lightbox image placeholders excluded. External requests blocked. Not a full accessibility certification.', pages:paths.length, widths:[320,390,768,1280], checks:0, overflow:[], errors:[], failedImages:[], samples:[]};
 try {
 for(const width of report.widths){
  const context=await browser.newContext({viewport:{width,height:900}});
  const page=await context.newPage();
  await page.route('**/*',route=>route.request().url().startsWith(base)?route.continue():route.abort());
  let current='';page.on('pageerror',e=>report.errors.push({path:current,width,error:e.message}));
  for(const path of paths){
   current=path;await page.goto(base+'/'+path,{waitUntil:'load'});
   const closed=page.locator('.daily-lesson:not([open]) > summary').first();
   if(await closed.count()) await closed.click();
   const result=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,overflow:[...document.querySelectorAll('main *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+2||r.left< -2)}).slice(0,8).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.slice(0,80)})),images:[...document.images].filter(e=>e.getAttribute('src')&&e.complete&&e.naturalWidth===0).map(e=>e.getAttribute('src')),bytes:document.documentElement.outerHTML.length,header:document.querySelector('.site-masthead')?.getBoundingClientRect().height}));
   report.checks++;if(result.scrollWidth>width+2)report.overflow.push({path,width,...result});if(result.images.length)report.failedImages.push({path,width,images:result.images});
   if(['index.html','beginner.html','grammar-concepts.html','us-life.html','tools.html','efsp.html','grammar-concepts/concept-05.html'].includes(path)&&[390,1280].includes(width)){
    await page.screenshot({path:'output/playwright/audit-'+path.replaceAll('/','-')+'-'+width+'.png',fullPage:false});report.samples.push({path,width,bytes:result.bytes,header:result.header});
   }
  }
  console.log('Checked width',width,'pages',paths.length);await context.close();
 }
 fs.writeFileSync('docs/browser-audit-'+date+'.json',JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({checks:report.checks,overflow:report.overflow.length,errors:report.errors.length,failedImages:report.failedImages.length}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
