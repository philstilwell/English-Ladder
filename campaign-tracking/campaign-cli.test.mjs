import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const cli=fileURLToPath(new URL('./campaign.mjs',import.meta.url));
function run(...args){return spawnSync(process.execPath,[cli,...args],{encoding:'utf8'});}
test('both approved sites can reserve a fresh Reddit campaign without activating it',()=>{
 for(const site of ['englishladder.com','slugfester.com']){
  const target=site==='slugfester.com'?'/':'/grammar-concepts/concept-12.html';
  const result=run('new',site,'reddit','r/SideProject','Test title',target);
  assert.equal(result.status,0,result.stderr);
  assert.match(result.stdout,/INSERT INTO campaigns/);
  assert.match(result.stdout,/'draft'/);
  assert.ok(result.stdout.includes(`https://${site}/campaign/`));
  assert.doesNotMatch(result.stdout,/UPDATE campaigns|published_at/);
 }
});
test('new scope preserves target and source restrictions',()=>{
 for(const args of [
  ['new','example.com','reddit','community','title','/'],
  ['new','slugfester.com','email','community','title','/'],
  ['new','slugfester.com','reddit','community','title','/backend/']
 ]) assert.notEqual(run(...args).status,0);
});
