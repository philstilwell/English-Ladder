// Generates reviewed SQL; never publishes a post or alters a remote database.
import {randomBytes} from 'node:crypto';
import {validTarget} from './worker.mjs';
const [command,...args]=process.argv.slice(2);
const quote=s=>`'${String(s).replaceAll("'","''")}'`;
const idOK=id=>/^[a-z0-9][a-z0-9-]{5,99}$/.test(id);
function fail(message){console.error(message);process.exit(1);}
if(command==='new'){
  const [site,source,community,title,target]=args;
  if(!validTarget(site,target)||!['facebook','reddit'].includes(source)||!community||!title) fail('Usage: node campaign.mjs new SITE facebook|reddit COMMUNITY TITLE /public-resource-path');
  if(site==='slugfester.com'&&source==='reddit') fail('Slugfester Reddit promotion is outside the approved scope.');
  const prefix=site==='englishladder.com'?'el':'sf';
  const id=`${prefix}-${source}-${new Date().toISOString().slice(0,10).replaceAll('-','')}-${randomBytes(4).toString('hex')}`;
  console.log(`-- Link: https://${site}/campaign/${id}`);
  console.log(`INSERT INTO campaigns(id,site,source,community,title,target,status) VALUES(${[id,site,source,community,title,target,'draft'].map(quote).join(',')});`);
}else if(command==='activate'){
  if(!idOK(args[0]||'')) fail('Supply the reserved campaign ID.');
  console.log(`UPDATE campaigns SET status='active' WHERE id=${quote(args[0])} AND status='draft';`);
}else if(command==='published'){
  const [id,url,time]=args;
  if(!idOK(id||'')||!/^https:\/\/(?:www\.)?(?:reddit|facebook)\.com\//.test(url||'')||!time||!Number.isFinite(Date.parse(time))) fail('Supply ID, verified Facebook/Reddit post permalink and publication time in ISO format.');
  console.log(`UPDATE campaigns SET status='published',post_url=${quote(url)},published_at=${quote(new Date(time).toISOString())} WHERE id=${quote(id)} AND status IN ('active','published');`);
}else if(command==='report'){
  console.log('SELECT site,title,source,community,post_url,published_at,browser_arrivals,engaged_visits,internal_arrivals,test_arrivals,bot_arrivals FROM campaign_results ORDER BY published_at DESC,post_id;');
}else fail('Commands: new, activate, published, report. See README.md.');
