import {readFile} from 'node:fs/promises';
import {createInterface} from 'node:readline';
import {once} from 'node:events';
import {isDeepStrictEqual} from 'node:util';
import {validateFeedback} from './feedback.mjs';
import {validateAssessment} from './assessment.mjs';

const [origin, filename, mode] = process.argv.slice(2);
if (mode && mode !== '--assessment') throw new Error('Unknown publishing mode.');
const assessmentMode = mode === '--assessment';
const url = new URL(origin);
if (url.origin !== origin || !((url.protocol === 'https:' && /^[a-z0-9-]+\.englishladder\.com$/.test(url.hostname)) || (url.protocol === 'http:' && ['localhost','127.0.0.1'].includes(url.hostname)))) throw new Error('Use a student subdomain or a local preview.');
const input = JSON.parse(await readFile(filename,'utf8'));
if (!assessmentMode && (!Array.isArray(input) || !input.length)) throw new Error('Expected a list of feedback records.');
const records = assessmentMode ? [validateAssessment(input)] : input.map(r=>validateFeedback(r,r.id));
if (new Set(records.map(r=>r.id)).size !== records.length) throw new Error('Duplicate session IDs.');
console.log('Records validated. Ready for the teacher password on standard input.');
const reader = createInterface({input:process.stdin,terminal:false});
const [password] = await once(reader,'line');
reader.close();
let cookie;
async function api(path,method='GET',body) {
 const response = await fetch(origin+path,{method,redirect:'error',headers:{Origin:origin,'Content-Type':'application/json',...(cookie?{Cookie:cookie}:{})},...(body?{body:JSON.stringify(body)}:{})});
 if (!response.ok) throw new Error('Request failed: '+method+' '+path+' ('+response.status+').');
 return response;
}
try {
 const login = await api('/api/login','POST',{password});
 cookie=login.headers.get('set-cookie')?.split(';')[0];
 const profile=await login.json();
 if(profile.role!=='teacher'||!cookie)throw new Error('Teacher access is required.');
 for(const record of records) {
  const path = assessmentMode ? '/api/assessment' : '/api/feedback/'+record.id;
  await api(path,'PUT',record);
  const result=await (await api(path)).json();
  const saved=assessmentMode ? result.assessment : result;
  const expected=structuredClone(record);
  if(expected.source)delete expected.source.noteId;
  if(!isDeepStrictEqual(saved,expected))throw new Error('Saved record verification failed.');
  console.log('Published and verified '+(assessmentMode ? 'overall assessment' : record.id));
 }
 console.log('Published '+records.length+' learning record(s).');
} finally {
 if(cookie)await api('/api/logout','POST');
}
