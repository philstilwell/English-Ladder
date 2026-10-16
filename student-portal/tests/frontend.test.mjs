import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {JSDOM} from 'jsdom';
import {studyTopics} from '../study-progress.mjs';
import {ACTIVITY_TOOLS} from '../activities.mjs';
import {RESOURCE_TOOLS} from '../resources.mjs';
import {feedback,assessment,quiz} from './fixture.mjs';
import {seedQuiz,call,origin} from './harness.mjs';
import grammarBank from '../grammar-bank.json' with { type: 'json' };
import termsBank from '../business-terms-bank.json' with { type: 'json' };
const html=readFileSync(new URL('../public/index.html',import.meta.url),'utf8');
const script=readFileSync(new URL('../public/portal.js',import.meta.url),'utf8');
const studyFixture=(await studyTopics(assessment)).map(topic=>({...topic,progress:{id:topic.id,finished:false,question:false,revision:0,updatedAt:null}}));
const second={...feedback,id:'2026-09-01-2057',startedAt:'2026-09-02T00:57:01Z',title:'Earlier English lesson'};
const profile={student:{id:'ab26',name:'Alex',nickname:'Alex the Explorer'},role:'student'};
const reply=data=>new Response(JSON.stringify(data));
const flush=async()=>{for(let i=0;i<12;i++)await new Promise(resolve=>setTimeout(resolve,1));};
function setup(custom,url='https://ab26.englishladder.com/',role='student'){
 const dom=new JSDOM(html,{url,runScripts:'outside-only',pretendToBeVisual:true});
 const w=dom.window;w.setInterval=()=>0;w.AbortController=AbortController;
 const positions=new Map();
 w.fetch=async(path,options)=>{
  const customResult=custom?.(path,options);if(customResult)return customResult;
  if(path==='/api/context')return reply({id:'ab26'});
  if(path==='/api/session'||path==='/api/login')return reply({...profile,role});
  if(path==='/api/logout')return reply({ok:true});
  if(path==='/api/account')return reply(settingsFixture);
  if(path==='/api/study/state')return reply({topics:studyFixture});
  if(path.startsWith('/api/study/questions'))return reply({questions:[],nextCursor:null});
  if(path==='/api/assessment')return reply({assessment});
  if(path==='/api/quiz/state')return reply({attempt:null});
  if(['/api/business-terms/state','/api/grammar-practice/state'].includes(path)) {
   let position=positions.get(path)||{number:null,revision:0};
   if(options?.method==='PATCH'&&JSON.parse(options.body).field==='position') {
    position={number:JSON.parse(options.body).value,revision:position.revision+1};positions.set(path,position);return reply({position});
   }
   return reply({entries:[],position});
  }
  if(path==='/api/feedback')return reply({sessions:[feedback,second],nextCursor:null});
  return reply(path.endsWith(second.id)?second:feedback);
 };
 w.eval(readFileSync(new URL('../public/practice-prompt.js',import.meta.url),'utf8'));
 w.eval(readFileSync(new URL('../public/study-practice.js',import.meta.url),'utf8'));
 w.eval(readFileSync(new URL('../public/road-practice.js',import.meta.url),'utf8'));
 w.eval(readFileSync(new URL('../public/practice-position.js',import.meta.url),'utf8'));
 w.eval(readFileSync(new URL('../public/grammar-practice.js',import.meta.url),'utf8'));
 w.eval(readFileSync(new URL('../public/business-terms.js',import.meta.url),'utf8'));w.eval(script);return dom;
}
test('deep links open the selected page and show only student-safe content',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#feedback/'+second.id);await flush();
 const d=dom.window.document;
 assert.equal(d.querySelector('.masthead-band .section-nav').hidden,false);
 assert.equal(d.getElementById('feedback-title').textContent,second.title);
 assert.match(d.getElementById('profile-nickname').textContent,/Alex the Explorer/);
 assert.equal(d.querySelectorAll('#session-list a').length,2);
 assert.match(d.getElementById('feedback-page').textContent,/Japan:/);
 assert.doesNotMatch(d.getElementById('feedback-page').textContent,/Lesson time|\d{2}:\d{2}:\d{2}|text covers|Each time shows/);
 assert.equal(d.querySelectorAll('.practice-item details').length,1);
 dom.window.close();
});
test('resources support skill links, history navigation and teacher previews',async()=>{
 for(const role of ['student','teacher']){
  const dom=setup(null,'https://ab26.englishladder.com/#resources/speaking',role);await flush();
  const w=dom.window,d=w.document;
  assert.equal(d.getElementById('resources').hidden,false);
  assert.equal(d.getElementById('feedback').hidden,true);
  assert.equal(d.getElementById('resources-nav').getAttribute('aria-current'),'page');
  assert.equal(d.querySelectorAll('.resource-group:not([hidden])').length,1);
  assert.equal(d.querySelector('.resource-group:not([hidden])').dataset.resourceGroup,'speaking');
  assert.equal(d.title,'English resources · English Ladder');
  d.querySelector('.resource-filters a[href="#resources/reading"]').click();await flush();
  assert.equal(d.querySelector('.resource-group:not([hidden])').dataset.resourceGroup,'reading');
  assert.equal(d.activeElement.id,'resources-title');
  w.location.hash='resources/unknown';await flush();
  assert.equal(d.querySelectorAll('.resource-group[hidden]').length,0);
  assert.equal(d.querySelector('.resource-filters a[aria-current]').hash,'#resources');
  w.location.hash='feedback';await flush();
  assert.equal(d.getElementById('resources').hidden,true);
  assert.equal(d.getElementById('resources-nav').hasAttribute('aria-current'),false);
  dom.window.close();
 }
});
test('resource links open separately without passing student data or a referrer',()=>{
 const dom=new JSDOM(html,{url:'https://ab26.englishladder.com/'}),d=dom.window.document;
 const cards=[...d.querySelectorAll('[data-resource-id]')];
 assert.deepEqual(cards.map(card=>({id:card.dataset.resourceId,name:card.querySelector('h4').textContent.replace(/\s*↗\s*$/, '').trim(),group:card.closest('[data-resource-group]').dataset.resourceGroup})),RESOURCE_TOOLS.map(({id,name,group})=>({id,name,group})));
 assert.ok(cards.every(card=>card.hidden));
 const links=[...d.querySelectorAll('.resource-card a')];
 assert.ok(links.length>0);
 assert.equal(new Set(links.map(link=>link.href)).size,links.length);
 for(const link of links){
  const url=new URL(link.href);
  assert.equal(url.protocol,'https:');
  assert.equal(url.search,'');
  assert.equal(url.hash,'');
  assert.equal(link.target,'_blank');
  assert.ok(link.relList.contains('noopener'));
  assert.ok(link.relList.contains('noreferrer'));
  assert.equal(link.referrerPolicy || link.getAttribute('referrerpolicy'),'no-referrer');
 }
 assert.equal(d.getElementById('dashboard-view').hidden,true);
 assert.equal(d.querySelectorAll('#resources iframe,#resources script,#resources form').length,0);
 dom.window.close();
});
test('resources show only saved choices, hide empty categories, and reload choices on returning',async()=>{
 for(const role of ['student','teacher']) {
  let choices=['elllo','write-and-improve'],writes=0;
  const dom=setup((path,options)=>{
   if(options?.method&&options.method!=='GET')writes++;
   if(path==='/api/account')return reply({...settingsFixture,visibleResources:choices});
  },'https://ab26.englishladder.com/#resources/speaking',role);
  await flush();const w=dom.window,d=w.document;
  const shown=()=>[...d.querySelectorAll('[data-resource-id]:not([hidden])')].map(card=>card.dataset.resourceId);
  assert.deepEqual(shown(),choices);
  assert.equal(d.getElementById('resource-count').textContent,'2 resources');
  assert.equal(d.querySelectorAll('.resource-group:not([hidden])').length,2);
  assert.equal(d.querySelector('.resource-filters a[href="#resources/speaking"]').hidden,true);
  assert.equal(d.querySelector('.resource-filters a[aria-current]').hash,'#resources');
  assert.equal(d.querySelectorAll('#resources input[type="checkbox"]').length,0);
  w.location.hash='overview';await flush();assert.equal(d.getElementById('resource-catalog').hidden,true);assert.deepEqual(shown(),[]);
  choices=['news-in-levels'];w.location.hash='resources';await flush();assert.deepEqual(shown(),choices);
  assert.equal(d.getElementById('resource-count').textContent,'1 resource');
  choices=[];d.dispatchEvent(new w.Event('visibilitychange'));await flush();
  assert.deepEqual(shown(),[]);assert.equal(d.getElementById('resource-catalog').hidden,true);
  assert.match(d.getElementById('resource-status').textContent,/teacher has not selected/);
  assert.equal(writes,0);w.close();
 }
});
test('resource reads fail closed, offer retry, and clear choices on expiry and page hide',async()=>{
 for(const invalid of [null,{}, {revision:1,visibleResources:'all'}, {revision:1,visibleResources:['elllo','elllo']}]) {
  let state='invalid';
  const dom=setup(path=>path==='/api/account' ? state==='expired' ? new Response('{}',{status:401}) : reply(state==='valid'?{...settingsFixture,visibleResources:['elllo']}:invalid) : null,'https://ab26.englishladder.com/#resources');
  await flush();const w=dom.window,d=w.document;
  assert.equal(d.getElementById('resource-catalog').hidden,true);
  assert.match(d.getElementById('resource-status').textContent,/could not be loaded/);
  assert.equal(d.getElementById('retry-resources').hidden,false);
  state='valid';d.getElementById('retry-resources').click();await flush();
  assert.equal(d.getElementById('resource-catalog').hidden,false);
  w.dispatchEvent(new w.Event('pagehide'));assert.equal(d.getElementById('resource-catalog').hidden,true);
  state='expired';d.dispatchEvent(new w.Event('visibilitychange'));await flush();
  assert.equal(d.getElementById('login-view').hidden,false);
  assert.equal(d.querySelectorAll('[data-resource-id]:not([hidden])').length,0);w.close();
 }
});
test('late resource responses cannot restore old choices after navigation or sign-out',async()=>{
 for(const action of ['navigate','logout']) {
  const pending=[];
  const dom=setup(path=>path==='/api/account'?new Promise(resolve=>pending.push(resolve)):null,'https://ab26.englishladder.com/#resources');
  await flush();const w=dom.window,d=w.document;
  assert.equal(d.getElementById('resource-catalog').hidden,true);
  if(action==='logout')d.getElementById('logout').click();else w.location.hash='overview';
  await flush();
  for(const resolve of pending.splice(0))resolve(reply(settingsFixture));await flush();
  assert.equal(d.getElementById('resource-catalog').hidden,true);
  assert.equal(d.querySelectorAll('[data-resource-id]:not([hidden])').length,0);
  if(action==='navigate'){
   w.location.hash='resources';await flush();
   for(const resolve of pending.splice(0))resolve(reply({...settingsFixture,visibleResources:['elllo']}));await flush();
   assert.deepEqual([...d.querySelectorAll('[data-resource-id]:not([hidden])')].map(card=>card.dataset.resourceId),['elllo']);
  }
  w.close();
 }
});
test('late page responses cannot overwrite a newer selection',async()=>{
 let resolveFirst;
 const dom=setup(path=>path.endsWith('/'+feedback.id)?new Promise(resolve=>{resolveFirst=resolve;}):null);
 await flush();
 dom.window.location.hash='feedback/'+second.id;await new Promise(r=>setTimeout(r,10));await flush();
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,second.title);
 resolveFirst(reply(feedback));await flush();
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,second.title);
 dom.window.close();
});
test('assessment highlighting includes the section reached below the combined header',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#assessments/patterns');await flush();
 const w=dom.window,d=w.document;
 Object.defineProperty(w,'innerHeight',{value:720,configurable:true});
 d.querySelector('.masthead-band').getBoundingClientRect=()=>({height:110});
 for(const [key,top] of Object.entries({summary:-1000,strengths:-500,patterns:150,next:900})) {
  d.getElementById('assessment-'+key).getBoundingClientRect=()=>({top});
 }
 w.dispatchEvent(new w.Event('scroll'));
 await new Promise(resolve=>setTimeout(resolve,30));
 assert.equal(d.querySelector('.assessment-outline [aria-current]').hash,'#assessments/patterns');
 w.close();
});
test('sign-out clears profile, records, summaries, and late responses',async()=>{
 let resolveFirst;
 const dom=setup(path=>path.endsWith('/'+feedback.id)?new Promise(resolve=>{resolveFirst=resolve;}):null);await flush();
 dom.window.document.getElementById('logout').click();await flush();
 resolveFirst(reply(feedback));await flush();
 const d=dom.window.document;
 assert.equal(d.getElementById('login-view').hidden,false);
 assert.equal(d.querySelector('.section-nav').hidden,true);
 for(const id of ['feedback-page','session-list','session-select','session-summaries','profile-nickname','assessment-content','assessment-source-count','quiz-content'])assert.equal(d.getElementById(id).textContent,'');
 assert.doesNotMatch(d.getElementById('dashboard-view').textContent,/Alex|Clear explanations|Earlier English lesson/);
 dom.window.close();
});
test('expired feedback sessions return to sign-in and clear private content',async()=>{
 const dom=setup(path=>path.startsWith('/api/feedback/')?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null);
 await flush();
 assert.equal(dom.window.document.getElementById('login-view').hidden,false);
 assert.equal(dom.window.document.querySelector('.section-nav').hidden,true);
 assert.equal(dom.window.document.getElementById('session-list').textContent,'');
 dom.window.close();
});
test('feedback strings render as text, never executable markup',async()=>{
 const data={...feedback,title:'<img src=x onerror=alert(1)>',practice:[{prompt:'<img src=x onerror=alert(1)>',answer:'<script>alert(1)</script>'}]};
 const dom=setup(path=>path.endsWith('/'+feedback.id)?reply(data):null);await flush();
 assert.equal(dom.window.document.querySelector('#feedback-title img, .practice-item > p img, .practice-item details img, #feedback-page script, #feedback-page [onerror]'),null);
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,data.title);
 assert.equal(dom.window.document.querySelector('.practice-item details p').textContent,data.practice[0].answer);
 dom.window.close();
});
test('Feedback practice prompts copy only their own exercise without revealing answers, writing records, or surviving a session change',async()=>{
 const extra={prompt:'New practice. Ask for help with a heavy bag.',answer:'Could you help me carry this bag?'};
 for(const role of ['student','teacher']){
  const copied=[],writes=[];
  const dom=setup((path,options={})=>{
   if(options.method&&options.method!=='GET')writes.push(path);
   if(path.endsWith('/'+feedback.id))return reply({...feedback,practice:[...feedback.practice,extra]});
   if(path.endsWith('/'+second.id))return reply({...second,practice:[extra]});
   return null;
  },origin+'/#feedback/'+feedback.id,role);
  const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>copied.push(text)}});
  await flush();
  const buttons=[...d.querySelectorAll('.practice-item .practice-copy-button')];
  assert.equal(buttons.length,2);
  buttons[0].click();await flush();buttons[1].click();await flush();
  for(const [i,item] of [...feedback.practice,extra].entries()){
   assert.equal(buttons[i].textContent,'AI prompt copied');
   assert.ok(copied[i].includes(item.prompt)&&copied[i].includes(item.answer));
   assert.doesNotMatch(copied[i],/Alex|ab26|2026-10-01|fictional-note-id-only|Your teacher modeled|Clear explanations|00:03:00|https?:/);
  }
  assert.ok(!copied[0].includes(extra.prompt)&&!copied[1].includes(feedback.practice[0].prompt));
  assert.ok([...d.querySelectorAll('.practice-item details')].every(el=>!el.open));
  assert.equal(d.querySelectorAll('.practice-item .practice-ai-link').length,8);
  assert.equal(writes.length,0);
  w.location.hash='feedback/'+second.id;await flush();
  const current=d.querySelector('.practice-item .practice-copy-button');
  assert.equal(current.textContent,'Copy AI prompt');
  buttons[0].click();await flush();assert.equal(copied.length,2);
  current.click();await flush();assert.ok(copied[2].includes(extra.prompt));
  assert.equal(writes.length,0);
  d.getElementById('logout').click();await flush();current.click();await flush();
  assert.equal(copied.length,3);assert.equal(d.getElementById('feedback-page').textContent,'');
  w.close();
 }
});
test('Feedback topic and vocabulary prompts omit lesson evidence and copy independently in student and teacher views',async()=>{
 const topic={...feedback.focus[0],title:'Polite requests',model:'Could you open the window?',explanation:'Use “could you” to ask politely.',observed:'PRIVATE LESSON REMARK'};
 const word={...feedback.vocabulary[0],term:'borrow',meaning:'Use something and return it.',example:'Can I borrow a pencil?'};
 for(const role of ['student','teacher']){
  const copied=[],writes=[];
  const dom=setup((path,options={})=>{
   if(options.method&&options.method!=='GET')writes.push(path);
   if(path.endsWith('/'+feedback.id))return reply({...feedback,focus:[...feedback.focus,topic],vocabulary:[...feedback.vocabulary,word]});
   return null;
  },origin+'/#feedback/'+feedback.id,role);
  const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>copied.push(text)}});
  await flush();
  const buttons=[...d.querySelectorAll('#feedback-page .focus-card .practice-copy-button, #feedback-page .vocabulary-row .practice-copy-button')];
  assert.equal(buttons.length,4);
  const expected=[
   [feedback.focus[0].title,feedback.focus[0].model,feedback.focus[0].explanation],
   [topic.title,topic.model,topic.explanation],
   [feedback.vocabulary[0].term,feedback.vocabulary[0].meaning,feedback.vocabulary[0].example],
   [word.term,word.meaning,word.example]
  ];
  for(const [i,button] of buttons.entries()){
   assert.equal(button.textContent,'Copy AI prompt');button.click();await flush();
   assert.equal(button.textContent,'AI prompt copied');
   for(const text of expected[i])assert.ok(copied[i].includes(text));
   assert.doesNotMatch(copied[i],/Alex|ab26|2026-10-01|fictional-note-id-only|Your teacher modeled|PRIVATE LESSON REMARK|Clear explanations|00:03:00|https?:/);
  }
  assert.ok(!copied[0].includes(topic.model)&&!copied[2].includes(word.example));
  assert.equal(d.querySelectorAll('#feedback-page .focus-card .practice-ai-link, #feedback-page .vocabulary-row .practice-ai-link').length,16);
  assert.equal(d.querySelector('.practice-item .practice-copy-button').textContent,'Copy AI prompt');
  assert.equal(writes.length,0);
  w.location.hash='feedback/'+second.id;await flush();
  buttons[0].click();await flush();assert.equal(copied.length,4);
  const current=[...d.querySelectorAll('#feedback-page .focus-card .practice-copy-button, #feedback-page .vocabulary-row .practice-copy-button')];
  assert.ok(current.every(button=>button.textContent==='Copy AI prompt'));
  let finishCopy;w.navigator.clipboard.writeText=()=>new Promise(resolve=>{finishCopy=resolve;});
  current[0].click();d.getElementById('logout').click();await flush();finishCopy();await flush();
  assert.equal(current[0].textContent,'Copy AI prompt');
  assert.equal(d.getElementById('feedback-page').textContent,'');
  w.close();
 }
});

test('assessment shows strengths, patterns, next priorities, and only internal evidence links',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#assessments');await flush();
 const d=dom.window.document,content=d.getElementById('assessment-content');
 assert.equal(d.getElementById('assessments').hidden,false);
 for(const text of ['What you do well','Things to practice','Study on your own',assessment.summary])assert.ok(content.textContent.includes(text));
 assert.equal(d.getElementById('assessment-count').textContent,'Overall assessment · Oct 14, 2026');
 assert.equal(d.querySelectorAll('.assessment-evidence').length,3);
 assert.doesNotMatch(content.textContent,/Lesson time|\d{2}:\d{2}:\d{2}|next three lessons|Our next lesson/);
 assert.ok(!content.textContent.includes(assessment.nextLesson));
 assert.ok([...d.querySelectorAll('.assessment-evidence')].every(a=>a.textContent==='Oct 1, 2026' && !a.getAttribute('aria-label').includes('time')));
 assert.equal(d.querySelectorAll('.study-prompt').length,assessment.plan.length);
 assert.ok([...d.querySelectorAll('.assessment-evidence')].every(a=>a.hash==='#feedback/'+feedback.id));
 assert.equal(d.querySelectorAll('a[href*="mynotes.zoom.us"]').length,0);
 d.querySelector('.assessment-evidence').click();await new Promise(r=>setTimeout(r,10));await flush();
 assert.equal(d.getElementById('feedback-title').textContent,feedback.title);
 assert.equal(d.querySelectorAll('a[href*="mynotes.zoom.us"]').length,0);
 dom.window.close();
});
test('assessment practice prompts include their own model sentences without student evaluations or lesson evidence',async()=>{
 const data=structuredClone(assessment);
 data.patterns[0].detail='PRIVATE STUDENT EVALUATION';
 data.patterns[0].examples.push({...data.patterns[0].examples[0],model:'We can check the list.',observed:'PRIVATE LESSON QUOTE'});
 data.patterns.push({title:'Polite requests',detail:'PRIVATE STUDENT EVALUATION',practice:'Ask for help politely.',examples:[{...data.patterns[0].examples[0],model:'Could you carry this bag?'}]});
 for(const role of ['student','teacher']){
  const copied=[],writes=[];
  const dom=setup((path,options={})=>{
   if(options.method&&options.method!=='GET')writes.push(path);
   return path==='/api/assessment'?reply({assessment:data}):null;
  },origin+'/#assessments/patterns',role);
  const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>copied.push(text)}});
  await flush();
  const buttons=[...d.querySelectorAll('#assessment-content .focus-card .practice-copy-button')];
  assert.equal(buttons.length,2);
  for(const [i,item] of data.patterns.entries()){
   buttons[i].click();await flush();
   assert.equal(buttons[i].textContent,'AI prompt copied');
   for(const text of [item.title,item.practice,...item.examples.map(example=>example.model)])assert.ok(copied[i].includes(text));
   assert.doesNotMatch(copied[i],/PRIVATE|Alex|ab26|2026-10|Your teacher modeled|00:03:00|Your overall English assessment|https?:|#feedback/);
  }
  assert.ok(!copied[0].includes(data.patterns[1].practice)&&!copied[1].includes(data.patterns[0].practice));
  assert.equal(d.querySelectorAll('#assessment-content .focus-card .practice-ai-link').length,8);
  assert.equal(d.querySelector('details.study-prompt, .study-prompt summary'),null);
  assert.ok([...d.querySelectorAll('#assessment-content .assessment-example .assessment-evidence')].every(a=>a.hash==='#feedback/'+feedback.id));
  assert.equal(writes.length,0);
  let finishCopy;w.navigator.clipboard.writeText=()=>new Promise(resolve=>{finishCopy=resolve;});
  buttons[0].click();d.getElementById('logout').click();await flush();finishCopy();await flush();
  assert.equal(buttons[0].textContent,'Copy AI prompt');
  assert.equal(d.getElementById('assessment-content').textContent,'');
  buttons[1].click();await flush();assert.equal(copied.length,2);
  w.close();
 }
});
test('late assessment responses cannot restore private content after sign-out',async()=>{
 let resolveAssessment;
 const dom=setup(path=>path==='/api/assessment'?new Promise(resolve=>{resolveAssessment=resolve;}):null,'https://ab26.englishladder.com/#assessments');
 await flush();dom.window.document.getElementById('logout').click();await flush();
 resolveAssessment(reply({assessment}));await flush();
 assert.equal(dom.window.document.getElementById('assessment-content').textContent,'');
 assert.equal(dom.window.document.getElementById('assessment-sidebar').hidden,true);
 assert.doesNotMatch(dom.window.document.body.textContent,/You ask useful questions/);
 dom.window.close();
});
test('empty assessment and failed requests have distinct states and errors can be retried',async()=>{
 const empty=setup(path=>path==='/api/assessment'?reply({assessment:null}):null);await flush();
 assert.equal(empty.window.document.getElementById('assessment-count').textContent,'No assessments yet');
 assert.equal(empty.window.document.getElementById('assessment-sidebar').hidden,true);
 empty.window.close();
 let fail=true;
 const dom=setup(path=>path==='/api/assessment'?(fail?new Response(JSON.stringify({error:'Please try again.'}),{status:503}):reply({assessment})):null);
 await flush();
 assert.equal(dom.window.document.getElementById('assessment-count').textContent,'Assessment unavailable');
 fail=false;dom.window.document.querySelector('#assessment-content button').click();await flush();
 assert.equal(dom.window.document.getElementById('assessment-title').textContent,assessment.title);
 assert.equal(dom.window.document.getElementById('assessment-summary').textContent,'Your English now');
 dom.window.close();
});
test('assessment expiry clears records and assessment text cannot inject markup',async()=>{
 const expired=setup(path=>path==='/api/assessment'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null);await flush();
 assert.equal(expired.window.document.getElementById('login-view').hidden,false);
 assert.equal(expired.window.document.getElementById('assessment-content').textContent,'');
 expired.window.close();
 const title='<img src=x onerror=alert(1)>';
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,title}}):null);await flush();
 assert.equal(dom.window.document.querySelector('#assessment-title img'),null);
 assert.equal(dom.window.document.querySelector('#assessment-content [onerror]'),null);
 assert.equal(dom.window.document.getElementById('assessment-title').textContent,title);
 dom.window.close();
});

test('quiz gives feedback for every choice, waits for a correct answer, and counts first tries only',async()=>{
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz}}):null,'https://ab26.englishladder.com/#quiz','teacher');
 await flush();const d=dom.window.document;
 const options=()=>[...d.querySelectorAll('.quiz-option')];
 assert.equal(d.getElementById('quiz').hidden,false);
 assert.equal(d.querySelector('.quiz-next').hidden,true);
 d.querySelector('.quiz-next').click();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 1 of 2/);
 options()[1].click();
 assert.match(d.getElementById('quiz-result').textContent,/Not yet/);
 assert.ok(d.getElementById('quiz-result').textContent.includes(quiz.questions[0].options[1].feedback));
 assert.equal(options()[1].disabled,true);
 assert.equal(d.querySelector('.quiz-next').hidden,true);
 options()[0].click();
 assert.match(d.getElementById('quiz-result').textContent,/That’s right!/);
 assert.ok(d.getElementById('quiz-result').textContent.includes(quiz.questions[0].model));
 options()[0].click();
 d.querySelector('.quiz-next').click();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 2 of 2/);
 assert.equal(d.getElementById('quiz-result').textContent,'');
 options()[1].click();d.querySelector('.quiz-next').click();
 assert.match(d.querySelector('.quiz-complete').textContent,/1 out of 2 right on your first try/);
 assert.equal(d.querySelectorAll('.quiz-complete li').length,1);
 d.querySelector('.quiz-complete button').click();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 1 of 2/);
 assert.ok(options().every(b=>!b.disabled));
 assert.equal(d.getElementById('quiz-result').textContent,'');
 dom.window.close();
});
test('quiz progress survives section navigation but sign-out clears it and invalidates old controls',async()=>{
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz}}):null,'https://ab26.englishladder.com/#quiz','teacher');
 await flush();const d=dom.window.document;
 const oldButton=d.querySelector('.quiz-option');
 oldButton.click();d.querySelector('.quiz-next').click();
 dom.window.location.hash='feedback';await new Promise(r=>setTimeout(r,10));await flush();
 dom.window.location.hash='quiz';await new Promise(r=>setTimeout(r,10));await flush();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 2 of 2/);
 d.getElementById('logout').click();await flush();
 assert.equal(d.getElementById('quiz-content').textContent,'');
 oldButton.dispatchEvent(new dom.window.MouseEvent('click',{bubbles:true}));
 assert.equal(d.getElementById('quiz-content').textContent,'');
 dom.window.close();
});
test('quiz handles empty and failed loads, and renders authored text without markup',async()=>{
 const empty=setup(null,'https://ab26.englishladder.com/#quiz','teacher');await flush();
 assert.match(empty.window.document.getElementById('quiz-content').textContent,/Your teacher can add a quiz/);
 empty.window.close();
 const failed=setup(path=>path==='/api/assessment'?new Response(JSON.stringify({error:'Try again.'}),{status:503}):null,'https://ab26.englishladder.com/#quiz','teacher');await flush();
 assert.match(failed.window.document.getElementById('quiz-content').textContent,/could not be loaded/);
 assert.equal(failed.window.document.querySelector('#quiz-content button').textContent,'Try again');
 failed.window.close();
 const q=structuredClone(quiz);q.questions[0].prompt='<img src=x onerror=alert(1)>';
 q.questions[0].options[0].feedback='<script>alert(1)</script>';
 const safe=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz:q}}):null,'https://ab26.englishladder.com/#quiz','teacher');
 await flush();const d=safe.window.document;
 assert.equal(d.getElementById('quiz-question-title').textContent,q.questions[0].prompt);
 d.querySelector('.quiz-option').click();
 assert.ok(d.getElementById('quiz-result').textContent.includes(q.questions[0].options[0].feedback));
 assert.equal(d.querySelector('.quiz-prompt img, .quiz-choices img, #quiz-result img, #quiz-content script, #quiz-content [onerror]'),null);
 safe.window.close();
});
test('late quiz data cannot appear after sign-out',async()=>{
 let resolve;
 const dom=setup(path=>path==='/api/assessment'?new Promise(r=>{resolve=r;}):null,'https://ab26.englishladder.com/#quiz','teacher');
 await flush();dom.window.document.getElementById('logout').click();await flush();
 resolve(reply({assessment:{...assessment,quiz}}));await flush();
 assert.equal(dom.window.document.getElementById('quiz-content').textContent,'');
 dom.window.close();
});

function savedSetup(seed,role='student',custom=null,hash='quiz'){
 const cookie=seed[role].cookie;
 return setup((path,options={})=>custom?.(path,options)||call(seed.e,path,{...options,headers:{...options.headers,Cookie:cookie,Origin:origin}}),origin+'/#'+hash,role);
}
test('quiz AI prompts copy only the current exercise without saving choices or changing first-try results',async()=>{
 for(const role of ['student','teacher']){
  const seed=await seedQuiz(),copied=[];let answerWrites=0;
  const dom=savedSetup(seed,role,(path,options)=>{if(path==='/api/quiz/answer'&&options.method==='POST')answerWrites++;return null;});
  const w=dom.window,d=w.document;
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>copied.push(text)}});
  await flush();
  const oldCopy=d.querySelector('#quiz-content .practice-copy-button');
  oldCopy.click();await flush();
  assert.equal(oldCopy.textContent,'AI prompt copied');
  assert.ok(copied[0].includes(quiz.questions[0].prompt));
  for(const option of quiz.questions[0].options)assert.ok(copied[0].includes(option.text));
  assert.ok(copied[0].includes(quiz.questions[0].options[0].feedback));
  assert.ok(copied[0].includes(quiz.questions[0].model));
  assert.doesNotMatch(copied[0],/Alex|ab26|2026-10-01|fictional-note-id-only|first try|score|https?:/i);
  assert.equal(d.querySelector('#quiz-result').textContent,'');
  assert.ok([...d.querySelectorAll('.quiz-option')].every(b=>!b.disabled));
  assert.equal(answerWrites,0);
  assert.equal((await (await call(seed.e,'/api/quiz/state',{headers:{Cookie:seed.student.cookie}})).json()).attempt,null);
  const links=[...d.querySelectorAll('#quiz-content .practice-ai-link')];
  assert.deepEqual(links.map(a=>a.href),['https://chatgpt.com/','https://gemini.google.com/app','https://claude.ai/','https://copilot.microsoft.com/']);
  assert.ok(links.every(a=>a.target==='_blank'&&a.rel==='noopener noreferrer'&&a.referrerPolicy==='no-referrer'&&a.getAttribute('aria-label')));
  d.querySelectorAll('.quiz-option')[0].click();await flush();d.querySelector('.quiz-next').click();
  const nextCopy=d.querySelector('#quiz-content .practice-copy-button');
  assert.equal(nextCopy.textContent,'Copy AI prompt');
  nextCopy.click();await flush();
  assert.ok(copied[1].includes(quiz.questions[1].prompt));
  assert.ok(!copied[1].includes(quiz.questions[0].prompt));
  oldCopy.click();await flush();assert.equal(copied.length,2);
  assert.equal(answerWrites,role==='student'?1:0);
  d.querySelectorAll('.quiz-option')[1].click();await flush();d.querySelector('.quiz-next').click();
  assert.match(d.querySelector('.quiz-complete').textContent,/2 out of 2 right on your first try/);
  d.querySelector('.quiz-complete button').click();await flush();
  const afterRestart=d.querySelector('#quiz-content .practice-copy-button');
  assert.equal(afterRestart.textContent,'Copy AI prompt');
  d.getElementById('logout').click();await flush();afterRestart.click();await flush();
  assert.equal(copied.length,2);assert.equal(d.getElementById('quiz-content').textContent,'');
  w.close();
 }
});
test('teacher preview shows plain source dates without links and keeps quiz topic labels',async()=>{
 const next={...quiz,sourceSessions:[second.id],patternTitles:['Use “can”'],generatedForSession:second.id};
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz:next}}):null,origin+'/#quiz','teacher');
 await flush();const d=dom.window.document;
 assert.equal(d.querySelector('.quiz-header a'),null);
 assert.equal(d.querySelector('.quiz-header').textContent.includes('Teacher practice'),false);
 assert.match(d.querySelector('.quiz-sources').textContent,/Sep 1, 2026/);
 assert.match(d.querySelector('.quiz-sources').textContent,/Based on your lesson:/);
 d.querySelectorAll('.quiz-option')[1].click();d.querySelectorAll('.quiz-option')[0].click();
 d.querySelector('.quiz-next').click();d.querySelectorAll('.quiz-option')[1].click();d.querySelector('.quiz-next').click();
 assert.equal(d.querySelector('.quiz-complete li').textContent,'Use “can”');
 assert.equal(d.querySelector('#assessment-title').textContent,assessment.title);
 dom.window.close();
});
test('automatic quiz setup is teacher-only and late status responses clear on sign-out',async()=>{
 let resolve;
 const seed=await seedQuiz();
 const dom=savedSetup(seed,'teacher',path=>path==='/api/automation/status'?new Promise(r=>{resolve=r;}):null,'quiz-results');
 await flush();const d=dom.window.document;
 d.getElementById('logout').click();await flush();
 resolve(reply({configured:true,connected:true,enabled:true}));await flush();
 assert.equal(d.getElementById('quiz-automation').textContent,'');
 assert.equal(d.getElementById('quiz-automation').hidden,true);dom.window.close();
 const teacher=savedSetup(seed,'teacher',path=>path==='/api/automation/status'?reply({configured:true,connected:true,enabled:true}):null,'quiz-results');
 await flush();assert.match(teacher.window.document.getElementById('quiz-automation').textContent,/Your computer can be off/);teacher.window.close();
 const student=savedSetup(seed,'student',null,'quiz-results');await flush();
 assert.equal(student.window.document.getElementById('quiz-automation').hidden,true);student.window.close();
});
test('student answers save immediately, resume after reopening, and finish with a saved first-try score',async()=>{
 const seed=await seedQuiz();let dom=savedSetup(seed);await flush();let d=dom.window.document;
 assert.equal(d.querySelector('.quiz-header a'),null);
 assert.equal(d.querySelector('.quiz-header .quiz-save-note'),null);
 assert.equal(d.getElementById('quiz-nav').hidden,false);
 assert.equal(d.querySelector('.quiz-sources a'),null);
 assert.match(d.querySelector('.quiz-sources').textContent,/Oct 1, 2026/);
 d.querySelectorAll('.quiz-option')[1].click();
 assert.match(d.getElementById('quiz-result').textContent,/Not yet/);
 assert.ok([...d.querySelectorAll('.quiz-option')].every(b=>b.disabled));
 await flush();assert.equal(d.querySelector('.quiz-save-status').textContent,'Saved.');
 dom.window.close();dom=savedSetup(seed);await flush();d=dom.window.document;
 assert.match(d.getElementById('quiz-result').textContent,/Not yet/);
 assert.equal(d.querySelectorAll('.quiz-option')[1].disabled,true);
 d.querySelectorAll('.quiz-option')[0].click();await flush();d.querySelector('.quiz-next').click();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 2/);
 dom.window.close();dom=savedSetup(seed);await flush();d=dom.window.document;
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 2/);
 d.querySelectorAll('.quiz-option')[1].click();await flush();d.querySelector('.quiz-next').click();
 assert.match(d.querySelector('.quiz-complete').textContent,/1 out of 2 right on your first try/);
 assert.match(d.querySelector('.quiz-complete').textContent,/Saved. Phil can see/);
 d.querySelector('.quiz-complete button').click();await flush();
 assert.match(d.querySelector('.quiz-counter').textContent,/Question 1/);
 assert.ok([...d.querySelectorAll('.quiz-option')].every(b=>!b.disabled));
 dom.window.close();
});
test('a lost save response blocks advancement and safely retries the same first answer',async()=>{
 const seed=await seedQuiz();let loseResponse=true;
 const dom=savedSetup(seed,'student',(path,options)=>{
  if(path!=='/api/quiz/answer'||!loseResponse)return null;
  loseResponse=false;
  return call(seed.e,path,{...options,headers:{...options.headers,Cookie:seed.student.cookie,Origin:origin}}).then(()=>{throw new Error('Network interrupted');});
 });await flush();const d=dom.window.document;
 d.querySelectorAll('.quiz-option')[1].click();await flush();
 assert.match(d.querySelector('.quiz-save-status').textContent,/may not be saved/);
 assert.ok([...d.querySelectorAll('.quiz-option')].every(b=>b.disabled));
 [...d.querySelectorAll('#quiz-content button')].find(b=>b.textContent==='Save my answer again').click();await flush();
 assert.equal(d.querySelector('.quiz-save-status').textContent,'Saved.');
 const state=await (await call(seed.e,'/api/quiz/state',{headers:{Cookie:seed.student.cookie}})).json();
 assert.deepEqual(state.attempt.answers,[[1],[]]);
 dom.window.close();
});
test('expired quiz saves clear private content; late writes cannot restore it after sign-out',async()=>{
 const seed=await seedQuiz();
 const expired=savedSetup(seed,'student',path=>path==='/api/quiz/answer'?new Response(JSON.stringify({error:'Sign in.'}),{status:401}):null);
 await flush();expired.window.document.querySelector('.quiz-option').click();await flush();
 assert.equal(expired.window.document.getElementById('quiz-content').textContent,'');
 assert.equal(expired.window.document.getElementById('login-view').hidden,false);expired.window.close();
 let resolve;
 const dom=savedSetup(seed,'student',path=>path==='/api/quiz/answer'?new Promise(r=>{resolve=r;}):null);await flush();const d=dom.window.document;
 d.querySelector('.quiz-option').click();d.getElementById('logout').click();await flush();
 resolve(reply({attempt:{answers:[[0],[]]}}));await flush();
 assert.equal(d.getElementById('quiz-content').textContent,'');dom.window.close();
});
test('teacher sees saved first answers and dated progress; teacher preview creates no attempts',async()=>{
 const seed=await seedQuiz(),id=crypto.randomUUID();
 for(const [questionIndex,choiceIndex] of [[0,1],[0,0],[1,1]])await call(seed.e,'/api/quiz/answer',{method:'POST',headers:{Cookie:seed.student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({attemptId:id,version:seed.state.version,questionIndex,choiceIndex})});
 const dom=savedSetup(seed,'teacher',null,'quiz-results');await flush();const d=dom.window.document;
 assert.equal(d.querySelector('.section-nav a[href="#quiz-results"]'),null);
 assert.match(d.getElementById('quiz-history').textContent,/Progress over time/);
 assert.match(d.getElementById('quiz-history').textContent,/Wrong on the first try: Q1/);
 assert.equal(d.querySelector('.quiz-trend-list progress').value,1);
 d.querySelector('#quiz-history details').open=true;await new Promise(r=>setTimeout(r,10));await flush();
 assert.match(d.querySelector('.quiz-answer-history').textContent,/First answer: I can opens this file./);
 assert.match(d.querySelector('.quiz-answer-history').textContent,/Later choices: I can open this file./);
 dom.window.location.hash='quiz';await new Promise(r=>setTimeout(r,10));await flush();
 assert.equal(d.getElementById('teacher-banner').hidden,false);
 assert.equal(d.querySelector('.quiz-header a'),null);
 d.querySelectorAll('.quiz-option')[0].click();d.querySelector('.quiz-next').click();d.querySelectorAll('.quiz-option')[1].click();d.querySelector('.quiz-next').click();
 const history=await (await call(seed.e,'/api/quiz/results',{headers:{Cookie:seed.teacher.cookie}})).json();assert.equal(history.attempts.length,1);
 d.getElementById('logout').click();await flush();
 assert.equal(d.getElementById('quiz-history').textContent,'');assert.equal(d.querySelector('.section-nav a[href="#quiz-results"]'),null);dom.window.close();
});
test('Quiz is hidden from the menu until a quiz is available, including accounts without enough lesson material',async()=>{
 for(const role of ['student','teacher']){
  const dom=setup(null,origin+'/#overview',role);await flush();
  assert.equal(dom.window.document.getElementById('quiz-nav').hidden,true);
  assert.equal(dom.window.document.querySelector('.assessment-quiz-link'),null);dom.window.close();
 }
});
test('history stays teacher-only, handles load failure, and ignores a response after sign-out',async()=>{
 const seed=await seedQuiz();let calls=0;
 const student=savedSetup(seed,'student',path=>{if(path.startsWith('/api/quiz/results'))calls++;return null;},'quiz-results');await flush();
 assert.equal(student.window.document.querySelector('.section-nav a[href="#quiz-results"]'),null);assert.equal(calls,0);student.window.close();
 let fail=true;
 const teacher=savedSetup(seed,'teacher',path=>path==='/api/quiz/results'&&fail?new Response(JSON.stringify({error:'Unavailable.'}),{status:503}):null,'quiz-results');await flush();
 assert.match(teacher.window.document.getElementById('quiz-results-status').textContent,/could not be loaded/);
 fail=false;teacher.window.document.getElementById('refresh-quiz-results').click();await flush();
 assert.match(teacher.window.document.getElementById('quiz-results-status').textContent,/No saved attempts/);teacher.window.close();
 let resolve;
 const late=savedSetup(seed,'teacher',path=>path==='/api/quiz/results'?new Promise(r=>{resolve=r;}):null,'quiz-results');await flush();
 late.window.document.getElementById('logout').click();await flush();resolve(reply({attempts:[],nextCursor:null}));await flush();
 assert.equal(late.window.document.getElementById('quiz-history').textContent,'');assert.equal(late.window.document.getElementById('quiz-results-status').textContent,'');late.window.close();
});

test('self-study controls are directly available and copy the hidden prompt exactly with a clipboard fallback',async()=>{
 const aiPrompt='Teach me “access a file” and “have access to a file”. <img src=x> Explain them simply, then ask one question at a time.';
 const record={...assessment,plan:[{...assessment.plan[0],aiPrompt}]};
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:record}):null,origin+'/#assessments/next');await flush();
 const d=dom.window.document;let copied;
 Object.defineProperty(dom.window.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
 assert.equal(d.querySelector('details.study-prompt, .study-prompt summary'),null);
 assert.equal(d.querySelector('.study-prompt').tagName,'DIV');
 const button=d.querySelector('.study-prompt .practice-copy-button');
 button.click();await flush();
 assert.equal(copied,aiPrompt);assert.equal(button.textContent,'AI prompt copied');
 assert.match(d.querySelector('.study-prompt-status').textContent,/Choose an AI chat/);
 assert.equal(d.querySelector('.study-prompt-text'),null);
 assert.ok(!d.getElementById('assessment-content').textContent.includes(aiPrompt));
 dom.window.navigator.clipboard.writeText=async()=>{throw Error('Denied');};
 copied=null;d.execCommand=()=>{copied=d.querySelector('.practice-copy-buffer').value;return true;};
 button.click();await flush();
 assert.equal(copied,aiPrompt);assert.equal(button.textContent,'AI prompt copied');assert.equal(d.querySelector('.practice-copy-buffer'),null);
 d.execCommand=()=>false;button.click();await flush();
 assert.equal(button.textContent,'Copy AI prompt');
 assert.match(d.querySelector('.study-prompt-status').textContent,/could not be copied/);
 assert.ok(!d.getElementById('assessment-content').textContent.includes(aiPrompt));
 let finish;dom.window.navigator.clipboard.writeText=()=>new Promise(resolve=>{finish=resolve;});
 button.click();d.getElementById('logout').click();await flush();finish();await flush();
 assert.equal(d.getElementById('assessment-content').textContent,'');
 dom.window.close();
});

test('AI study logos open four sites without sending prompts or changing the clipboard',async()=>{
 const aiPrompt='Explain “a & an”, “50%” and “#1”.\nAsk: Is 2 + 2 = 4? <b>Use simple English.</b>';
 const record={...assessment,plan:[{...assessment.plan[0],title:'First topic',aiPrompt},{...assessment.plan[0],title:'Second topic'}]};
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:record}):null,origin+'/#assessments/next');await flush();
 const d=dom.window.document;let copied;
 Object.defineProperty(dom.window.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
 const boxes=[...d.querySelectorAll('.study-prompt')];
 for(const box of boxes){
  assert.equal(box.querySelector('summary, details, .study-prompt-text'),null);
  assert.equal(box.querySelectorAll('.practice-copy-button').length,1);
  assert.equal(box.querySelector('.practice-copy-button').textContent,'Copy AI prompt');
  const links=[...box.querySelectorAll('a')];assert.equal(links.length,4);
  assert.deepEqual(links.map(link=>link.href),['https://chatgpt.com/','https://gemini.google.com/app','https://claude.ai/','https://copilot.microsoft.com/']);
  for(const link of links){
   assert.equal(link.target,'_blank');assert.equal(link.rel,'noopener noreferrer');
   assert.equal(link.referrerPolicy,'no-referrer');assert.match(link.getAttribute('aria-label'),/new tab/);
   assert.ok(link.title);assert.equal(link.textContent,'');
   const image=link.querySelector('img');assert.ok(image);assert.equal(image.alt,'');
   assert.equal(image.width,14);assert.equal(image.height,14);
   assert.equal(new URL(image.src).origin,new URL(origin).origin);
   link.addEventListener('click',event=>event.preventDefault());
   link.click();
  }
 }
 await flush();
 assert.equal(copied,undefined);
 boxes[0].querySelector('.practice-copy-button').click();await flush();assert.equal(copied,aiPrompt);
 boxes[1].querySelector('.practice-copy-button').click();await flush();
 assert.ok(!boxes[1].textContent.includes(copied));
 assert.match(copied,/Second topic/);
 d.getElementById('logout').click();await flush();
 assert.equal(d.querySelectorAll('.study-prompt-actions').length,0);
 assert.equal(d.getElementById('assessment-content').textContent,'');
 dom.window.close();
});

test('repeated assessment references to one lesson show one date and no elapsed time',async()=>{
 const record={...assessment,strengths:[{...assessment.strengths[0],evidence:[{sessionId:feedback.id,at:'00:02:00'},{sessionId:feedback.id,at:'00:03:00'}]}]};
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:record}):null,origin+'/#assessments');await flush();
 const links=dom.window.document.querySelectorAll('.feedback-strengths .assessment-evidence');
 assert.equal(links.length,1);assert.equal(links[0].textContent,'Oct 1, 2026');
 assert.doesNotMatch(links[0].getAttribute('aria-label'),/00:02|00:03|time/);
 dom.window.close();
});

const settingsFixture = { visibleResources: RESOURCE_TOOLS.map(r => r.id), nickname: 'Alex the Explorer', revision: 1, visibleActivities: ACTIVITY_TOOLS.map(a => a.id), activities: ACTIVITY_TOOLS };
const submitForm = (dom, id) => dom.window.document.getElementById(id).dispatchEvent(new dom.window.Event('submit', { bubbles: true, cancelable: true }));
test('Account saves only a nickname, has no activity picker, and keeps teacher preview read-only', async () => {
  let saved = structuredClone(settingsFixture), writes = 0;
  const mock = (path, options) => {
    if (path !== '/api/account') return null;
    if (options.method === 'PUT') { const body = JSON.parse(options.body); assert.deepEqual(Object.keys(body).sort(), ['nickname', 'revision']); writes++; saved = { ...saved, ...body, revision: saved.revision + 1 }; }
    return reply(saved);
  };
  const dom = setup(mock, 'https://ab26.englishladder.com/#account'); await flush(); const d = dom.window.document;
  assert.equal(d.querySelector('.section-nav [aria-current]').hash, '#account');
  assert.equal(d.querySelector('.section-nav a[href="#activities"]').textContent, 'Activities');
  assert.equal(d.getElementById('account').hidden, false); assert.equal(d.getElementById('activity-options'), null);
  d.getElementById('nickname').value = '<b>New nickname</b>';
  submitForm(dom, 'settings-form'); await flush(); assert.equal(writes, 1);
  assert.deepEqual(saved.visibleActivities, settingsFixture.visibleActivities); assert.equal(d.getElementById('profile-nickname').textContent, '<b>New nickname</b>');
  assert.equal(d.querySelector('#profile-nickname b'), null); assert.match(d.getElementById('settings-message').textContent, /saved/);
  dom.window.location.hash = 'overview'; await flush(); assert.equal(d.getElementById('nickname').value, '');
  dom.window.location.hash = 'account'; await flush(); assert.equal(d.getElementById('nickname').value, '<b>New nickname</b>');
  assert.equal(d.querySelectorAll('#activity-options input:checked').length, 0); dom.window.close();
  const preview = setup(mock, 'https://ab26.englishladder.com/#account', 'teacher'); await flush();
  assert.equal(preview.window.document.getElementById('settings-fields').disabled, true);
  assert.equal(preview.window.document.getElementById('password-form').hidden, true);
  submitForm(preview, 'settings-form'); await flush(); assert.equal(writes, 1); preview.window.close();
});
test('password form signs out after success and clears secrets on navigation and sign-out', async () => {
  let sent;
  const dom = setup((path, options) => path === '/api/account' ? reply(settingsFixture) : path === '/api/account/password' ? (sent = JSON.parse(options.body), reply({ saved: true })) : null, 'https://ab26.englishladder.com/#account');
  await flush(); const d = dom.window.document;
  d.getElementById('current-password').value = 'current-test'; d.getElementById('new-password').value = 'new-test'; d.getElementById('confirm-password').value = 'new-test';
  submitForm(dom, 'password-form'); await flush();
  assert.equal(sent.currentPassword, 'current-test'); assert.equal(d.getElementById('login-view').hidden, false);
  assert.match(d.getElementById('login-notice').textContent, /password has changed/);
  for (const id of ['nickname', 'current-password', 'new-password', 'confirm-password']) assert.equal(d.getElementById(id).value, '');
  assert.equal(d.querySelectorAll('#activity-options input').length, 0); dom.window.close();
  for (const action of ['navigate', 'logout', 'pagehide']) {
    const page = setup(path => path === '/api/account' ? reply(settingsFixture) : null, 'https://ab26.englishladder.com/#account'); await flush();
    const doc = page.window.document; doc.getElementById('new-password').value = 'private-test';
    if (action === 'navigate') page.window.location.hash = 'feedback';
    else if (action === 'logout') doc.getElementById('logout').click();
    else page.window.dispatchEvent(new page.window.Event('pagehide'));
    await flush(); assert.equal(doc.getElementById('new-password').value, ''); assert.equal(doc.getElementById('nickname').value, ''); page.window.close();
  }
});
test('late account reads and writes cannot restore fields after navigation or logout', async () => {
  for (const operation of ['read', 'write']) for (const leave of ['navigation', 'logout']) {
    let complete;
    const dom = setup((path, options) => {
      if (path !== '/api/account') return null;
      if (operation === 'read' || options.method === 'PUT') return new Promise(resolve => { complete = resolve; });
      return reply(settingsFixture);
    }, 'https://ab26.englishladder.com/#account'); await flush();
    if (operation === 'write') submitForm(dom, 'settings-form');
    await flush();
    if (leave === 'navigation') dom.window.location.hash = 'feedback'; else dom.window.document.getElementById('logout').click();
    await flush(); complete(reply(settingsFixture)); await flush();
    assert.equal(dom.window.document.getElementById('nickname').value, ''); assert.equal(dom.window.document.querySelectorAll('#activity-options input').length, 0);
    if (leave === 'logout') assert.equal(dom.window.document.getElementById('profile-nickname').textContent, '');
    dom.window.close();
  }
});
test('account load failures can retry, stale saves request a reload, and expiry clears private forms', async () => {
  let state = 'fail';
  const dom = setup((path, options) => path === '/api/account' ? (state === 'fail' ? new Response(JSON.stringify({ error: 'Please try again.' }), { status: 503 }) : options.method === 'PUT' ? new Response(JSON.stringify({ error: 'Reload your account.' }), { status: state === 'expired' ? 401 : 409 }) : reply(settingsFixture)) : null, 'https://ab26.englishladder.com/#account');
  await flush(); const d = dom.window.document; assert.equal(d.getElementById('reload-settings').hidden, false);
  state = 'ready'; d.getElementById('reload-settings').click(); await flush(); assert.equal(d.getElementById('settings-fields').disabled, false);
  submitForm(dom, 'settings-form'); await flush(); assert.equal(d.getElementById('settings-fields').disabled, true); assert.equal(d.getElementById('reload-settings').hidden, false);
  d.getElementById('reload-settings').click(); await flush(); state = 'expired'; submitForm(dom, 'settings-form'); await flush();
  assert.equal(d.getElementById('login-view').hidden, false); assert.equal(d.getElementById('nickname').value, ''); dom.window.close();
});

test('Activities main link opens a guide to selected tools without starting practice or writing progress', async () => {
  for (const role of ['student', 'teacher']) {
    let saved = { ...settingsFixture }, writes = 0; const calls = [];
    const dom = setup((path, options) => {
      calls.push(path); if (options?.method && options.method !== 'GET') writes++;
      if (path === '/api/account') return reply(saved);
    }, 'https://ab26.englishladder.com/#overview', role);
    await flush(); const d = dom.window.document;
    d.getElementById('activities-toggle').click(); await flush();
    assert.equal(dom.window.location.hash, '#overview');
    d.getElementById('activities-link').click(); await flush();
    assert.equal(dom.window.location.hash, '#activities');
    assert.equal(d.getElementById('activities-submenu').hidden, true);
    assert.equal(d.getElementById('activities').hidden, false);
    assert.equal(d.getElementById('activity-title').textContent, 'Activities');
    assert.deepEqual([...d.querySelectorAll('.activity-guide h3')].map(n => n.textContent), ACTIVITY_TOOLS.map(a => a.name));
    for (const card of d.querySelectorAll('.activity-guide')) {
      assert.match(card.textContent, /Why try it\?/); assert(card.querySelectorAll('ol li').length >= 3);
      assert.match(card.querySelector('a').hash, /^#activities\//);
    }
    assert.equal(calls.some(p => /^\/api\/(road|grammar-practice|business-terms|vocabulary-practice)/.test(p)), false);
    assert.equal(writes, 0);
    dom.window.location.hash = '#overview'; await flush();
    assert.equal(d.getElementById('activity-catalog').textContent, '');
    saved = { ...saved, revision: 2, visibleActivities: ['vocabulary-practice'] };
    d.getElementById('activities-link').click(); await flush();
    assert.deepEqual([...d.querySelectorAll('.activity-guide h3')].map(n => n.textContent), ['Vocabulary practice']);
    d.querySelector('.activity-guide a').click(); await flush();
    assert.equal(dom.window.location.hash, '#activities/vocabulary-practice');
    assert.equal(d.getElementById('activity-catalog').hidden, true);
    d.getElementById('activities-link').click(); await flush();
    saved = { ...saved, revision: 3, visibleActivities: [] };
    d.getElementById('activities-toggle').click(); await flush();
    assert.equal(d.getElementById('activity-catalog').textContent, '');
    assert.match(d.getElementById('activity-message').textContent, /ask your teacher/);
    d.getElementById('logout').click(); await flush();
    assert.equal(d.getElementById('activity-catalog').textContent, '');
    dom.window.close();
  }
});
test('Activities follows administrator selections when reopened, including none, without a student picker', async () => {
  let saved = { ...settingsFixture, visibleActivities: ['english-road', 'business-terms'] };
  const mock = path => path === '/api/account' ? reply(saved) : path === '/api/business-terms' ? reply({items:termsBank.items}) : null;
  const dom = setup(mock, 'https://ab26.englishladder.com/#activities/business-terms'); await flush();
  const d = dom.window.document, labels = () => [...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent);
  assert.deepEqual(labels(), ['English Road Practice', 'Business terms']);
  assert.equal(d.getElementById('activity-title').textContent, 'Business terms');
  saved = { ...saved, revision: 2, visibleActivities: ['grammar-practice'] };
  d.getElementById('activities-toggle').click(); await flush();
  assert.deepEqual(labels(), ['Grammar practice']);
  assert.equal(d.getElementById('activity-title').textContent, 'Activities');
  assert.match(d.getElementById('activity-message').textContent, /teacher has not selected/);
  saved = { ...saved, revision: 3, visibleActivities: [] };
  d.getElementById('activities-toggle').click(); d.getElementById('activities-toggle').click(); await flush();
  assert.equal(d.querySelectorAll('#activities-submenu a').length, 0);
  assert.match(d.getElementById('activities-submenu').textContent, /ask your teacher/);
  dom.window.location.hash = 'account'; await flush();
  assert.equal(d.querySelectorAll('#account input[type="checkbox"]').length, 0); dom.window.close();
  const preview = setup(mock, 'https://ab26.englishladder.com/#overview', 'teacher'); await flush();
  assert.match(preview.window.document.getElementById('activities-submenu').textContent, /ask your teacher/); preview.window.close();
});
test('a delayed activity read cannot replace a newer administrator choice or restore choices after sign-out', async () => {
  let complete, reads = 0;
  const dom = setup((path, options) => {
    if (path !== '/api/account') return null;
    if (++reads === 1) return new Promise(resolve => { complete = resolve; });
    return reply({ ...settingsFixture, revision: 2, visibleActivities: ['grammar-practice'] });
  }, 'https://ab26.englishladder.com/#account'); await flush(); const d = dom.window.document;
  complete(reply(settingsFixture)); await flush();
  assert.deepEqual([...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent), ['Grammar practice']);
  d.getElementById('logout').click(); await flush(); assert.equal(d.getElementById('activities-submenu').textContent, ''); dom.window.close();
  let late;
  const signedOut = setup(path => path === '/api/account' ? new Promise(resolve => { late = resolve; }) : null, 'https://ab26.englishladder.com/#overview'); await flush();
  signedOut.window.document.getElementById('logout').click(); await flush(); late(reply(settingsFixture)); await flush();
  assert.equal(signedOut.window.document.getElementById('activities-submenu').textContent, ''); signedOut.window.close();
});
test('failed activity loading never substitutes defaults and can retry; expiry clears activities', async () => {
  let unavailable = true;
  const dom = setup(path => path === '/api/account' ? unavailable ? new Response(JSON.stringify({ error: 'Unavailable' }), { status: 503 }) : reply({ ...settingsFixture, visibleActivities: ['business-terms'] }) : null, 'https://ab26.englishladder.com/#activities');
  await flush(); const d = dom.window.document;
  assert.equal(d.querySelectorAll('#activities-submenu a').length, 0); assert.match(d.getElementById('activities-submenu').textContent, /could not be loaded/);
  assert.equal(d.getElementById('activity-catalog').hidden, true); assert.equal(d.getElementById('retry-activities').hidden, false);
  unavailable = false; d.getElementById('retry-activities').click(); await flush();
  assert.deepEqual([...d.querySelectorAll('.activity-guide h3')].map(n => n.textContent), ['Business terms']);
  assert.deepEqual([...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent), ['Business terms']); dom.window.close();
  const expired = setup(path => path === '/api/account' ? new Response(JSON.stringify({ error: 'Please sign in.' }), { status: 401 }) : null, 'https://ab26.englishladder.com/#overview');
  await flush(); assert.equal(expired.window.document.getElementById('login-view').hidden, false); assert.equal(expired.window.document.getElementById('activities-submenu').textContent, ''); expired.window.close();
});

const roadSettings = { ...settingsFixture, visibleActivities:['english-road'] };
const grammarSettings = { ...settingsFixture, visibleActivities:['grammar-practice'] };
const grammarRoute = origin + '/#activities/grammar-practice';
const termsSettings={...settingsFixture,visibleActivities:['business-terms']};
const termsRoute=origin+'/#activities/business-terms';
const termsMock=path=>path==='/api/account'?reply(termsSettings):path==='/api/business-terms'?reply({items:termsBank.items}):null;

test('business terms preserve answer highlights and save navigation without saving reveals', async () => {
  const calls=[];const dom=setup((path,options)=>{calls.push({path,method:options?.method||'GET',body:options?.body&&JSON.parse(options.body)});return termsMock(path);},termsRoute);
  await flush();const w=dom.window,d=w.document,root=d.getElementById('business-terms');
  w.Storage.prototype.setItem=()=>{throw Error('Self-check must not use browser storage');};
  assert.equal(d.querySelector('#activities-submenu a[aria-current]').textContent,'Business terms');
  assert.equal(root.querySelectorAll('.terms-words li').length,6);assert.equal(root.querySelectorAll('.terms-sentences li').length,3);
  const before=root.querySelector('.terms-sentences').textContent,count=calls.length;
  root.querySelector('.terms-reveal input').click();
  assert(root.querySelector('.terms-sentences').classList.contains('is-revealed'));
  assert.deepEqual([...root.querySelectorAll('.terms-answer')].map(el=>el.textContent),termsBank.items[0].answers);
  assert.equal(root.querySelector('.terms-sentences q').firstChild.nodeType,w.Node.TEXT_NODE);
  assert.deepEqual([...root.querySelectorAll('.terms-sentences q')].map(q=>q.textContent),[
    'She organized the plates in a neat stack.','A stack of reports awaited his review.','The library featured a stack of classic novels.'
  ]);
  root.querySelector('.terms-reveal input').click();assert.equal(root.querySelector('.terms-sentences').textContent,before);
  assert.equal(root.querySelectorAll('.terms-answer').length,0);
  assert(!root.querySelector('.terms-sentences').classList.contains('is-revealed'));assert.equal(calls.length,count);
  const jump=value=>{d.getElementById('terms-number').value=String(value);root.querySelector('form').dispatchEvent(new w.Event('submit',{bubbles:true,cancelable:true}));};
  jump(4);assert.equal([...root.querySelectorAll('.terms-words q')].filter(q=>q.textContent==='are').length,2);
  root.querySelector('.terms-reveal input').click();assert.match(root.querySelectorAll('.terms-sentences q')[1].textContent,/"Do Not Enter\."/);
  jump(5);root.querySelector('.terms-reveal input').click();assert.equal(root.querySelectorAll('.terms-sentences q')[1].textContent,'An electrical receptacle is another term for an outlet.');
  jump(17);jump(18);assert.match(d.getElementById('terms-jump-status').textContent,/not available/);assert.match(root.querySelector('h4').textContent,/Item 17/);
  [...root.querySelectorAll('button')].find(b=>b.textContent==='Next').click();assert.match(root.querySelector('h4').textContent,/Item 19/);assert.equal(root.querySelector('.terms-reveal input').checked,false);
  jump(2961);assert.equal([...root.querySelectorAll('button')].find(b=>b.textContent==='Next').disabled,true);
  assert.equal(d.activeElement.className,'terms-heading');await flush();assert(calls.filter(c=>c.method!=='GET').every(c=>c.body.field==='position'));assert.equal(calls.at(-1).body.value,2961);
  root.querySelector('.terms-reveal input').click();w.location.hash='overview';await flush();assert.equal(root.textContent,'');
  w.location.hash='activities/business-terms';await flush();assert.match(root.querySelector('h4').textContent,/Item 2961 ·/);assert.equal(root.querySelector('.terms-reveal input').checked,false);
  assert.equal(w.localStorage.length,0);assert.equal(w.sessionStorage.length,0);w.close();
});

test('business terms respect visibility, allow teacher previews and safely display source text', async () => {
  let calls=0;
  const hidden=setup(path=>path==='/api/account'?reply({...termsSettings,visibleActivities:[]}):path==='/api/business-terms'?(calls++,reply({items:termsBank.items})):null,termsRoute);
  await flush();assert.equal(calls,0);assert.equal(hidden.window.document.getElementById('business-terms').hidden,true);hidden.window.close();
  const text='<img src=x onerror=alert(1)>',item={...termsBank.items[0],term:text,answers:[text,...termsBank.items[0].answers.slice(1)],options:[text,...termsBank.items[0].answers.slice(1)]};
  const teacher=setup(path=>path==='/api/account'?reply(termsSettings):path==='/api/business-terms'?reply({items:[item]}):null,termsRoute,'teacher');
  await flush();const root=teacher.window.document.getElementById('business-terms');root.querySelector('.terms-reveal input').click();
  assert(root.textContent.includes(text));assert.equal(root.querySelector('.terms-heading img,.terms-words img,.terms-sentences img'),null);assert.equal(root.querySelector('[onerror]'),null);teacher.window.close();
});

test('business terms clear late loads after leaving the activity, sign-out and page hide', async () => {
  for(const action of ['navigation','sign-out','pagehide']) {
    let resolve;const dom=setup(path=>path==='/api/account'?reply(termsSettings):path==='/api/business-terms'?new Promise(r=>{resolve=r;}):null,termsRoute);
    await flush();const w=dom.window;
    if(action==='navigation')w.location.hash='account';else if(action==='sign-out')w.document.getElementById('logout').click();else w.dispatchEvent(new w.Event('pagehide'));
    await flush();resolve(reply({items:termsBank.items}));await flush();
    assert.equal(w.document.getElementById('business-terms').textContent,'');assert.equal(w.document.getElementById('business-terms').hidden,true);w.close();
  }
});

test('business terms retry bad content without exposing incomplete keys and clear on session expiry', async () => {
  let invalid=true;
  const dom=setup(path=>path==='/api/account'?reply(termsSettings):path==='/api/business-terms'?reply({items:invalid?[{...termsBank.items[0],answers:['incomplete']}]:termsBank.items}):null,termsRoute);
  await flush();const root=dom.window.document.getElementById('business-terms');assert.match(root.textContent,/could not load/);assert.equal(root.querySelector('.terms-sentences'),null);
  invalid=false;root.querySelector('button').click();await flush();assert.equal(root.querySelectorAll('.terms-sentences li').length,3);dom.window.close();
  const expiredDom=setup(path=>path==='/api/account'?reply(termsSettings):path==='/api/business-terms'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null,termsRoute);
  await flush();assert.equal(expiredDom.window.document.getElementById('login-view').hidden,false);assert.equal(expiredDom.window.document.getElementById('business-terms').textContent,'');expiredDom.window.close();
});

test('grammar preserves unsaved reveals and remembers the selected group', async () => {
  const calls=[];
  const dom=setup((path,options)=>{calls.push({path,method:options?.method||'GET',body:options?.body&&JSON.parse(options.body)});return path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?reply({items:grammarBank.items}):null;},grammarRoute);
  await flush();const w=dom.window,d=w.document,root=d.getElementById('grammar-practice');
  w.Storage.prototype.setItem=()=>{throw Error('Practice must not write browser storage');};
  assert.equal(d.querySelector('#activities-submenu a[aria-current]').textContent,'Grammar practice');
  assert.equal(root.querySelectorAll('.grammar-item').length,10);
  assert.equal(root.querySelectorAll('input:checked').length,0);
  const count=calls.length,checkbox=root.querySelector('.grammar-reveal input'),answer=d.getElementById(checkbox.getAttribute('aria-controls'));
  assert.equal(answer.textContent,grammarBank.items[0].prompt);
  checkbox.click();assert.equal(answer.textContent,'Tom is much more intelligent than Mike.');assert(answer.parentElement.classList.contains('is-revealed'));
  checkbox.click();assert.equal(answer.textContent,grammarBank.items[0].prompt);assert(!answer.parentElement.classList.contains('is-revealed'));assert.equal(calls.length,count);
  const picker=d.getElementById('grammar-group');picker.value='89';picker.dispatchEvent(new w.Event('change'));
  assert.equal(root.querySelector('ol').start,891);assert.equal(root.querySelectorAll('.grammar-item').length,10);
  assert.equal(root.querySelector('.grammar-item:last-child .grammar-prompt q').textContent,grammarBank.items[899].prompt);
  assert.equal([...root.querySelectorAll('button')].find(b=>b.textContent==='Next 10').disabled,true);
  assert.equal(d.activeElement.className,'grammar-heading');
  [...root.querySelectorAll('button')].find(b=>b.textContent==='Previous 10').click();assert.equal(root.querySelector('ol').start,881);
  await flush();assert(calls.filter(c=>c.method!=='GET').every(c=>c.body.field==='position'));assert.equal(calls.at(-1).body.value,881);
  root.querySelector('.grammar-reveal input').click();w.location.hash='overview';await flush();assert.equal(root.textContent,'');
  w.location.hash='activities/grammar-practice';await flush();assert.equal(root.querySelector('ol').start,881);assert.equal(root.querySelectorAll('input:checked').length,0);
  root.querySelector('.grammar-reveal input').click();w.dispatchEvent(new w.Event('pagehide'));assert.equal(root.textContent,'');assert.equal(root.hidden,true);
  assert.equal(w.localStorage.length,0);assert.equal(w.sessionStorage.length,0);dom.window.close();
});

test('grammar completes single blanks, multiple blanks and sentence items, and restores all 900 originals', async () => {
  const dom=setup(path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?reply({items:grammarBank.items}):null,grammarRoute);
  await flush();const w=dom.window,d=w.document;
  const examples=new Map([
    [5,'This is the end of my speech. Are there any questions?'],
    [116,'It is almost 2 pm now.'],
    [134,'I used to live in Osaka several years ago.'],
    [249,'I hope to live a long life.'],
    [316,'If your parents want you to clean your room, you had better do it.'],
    [463,'I will have been working here ten years come Monday.'],
  ]);
  let checked=0;
  for(let group=0;group<90;group++){
    const picker=d.getElementById('grammar-group');picker.value=String(group);picker.dispatchEvent(new w.Event('change'));
    for(const checkbox of d.querySelectorAll('#grammar-practice .grammar-reveal input')){
      const item=grammarBank.items[checked++],sentence=d.getElementById(checkbox.getAttribute('aria-controls'));
      checkbox.click();assert.doesNotMatch(sentence.textContent,/_+|undefined|\{|\}/);assert(sentence.parentElement.classList.contains('is-revealed'));
      if(examples.has(item.number))assert.equal(sentence.textContent,examples.get(item.number));
      checkbox.click();assert.equal(sentence.textContent,item.prompt);assert(!sentence.parentElement.classList.contains('is-revealed'));
    }
  }
  assert.equal(checked,900);w.close();
});

test('grammar obeys saved visibility and renders source strings safely in student and teacher views', async () => {
  let requests=0;
  const hidden=setup(path=>path==='/api/account'?reply({...grammarSettings,visibleActivities:[]}):path==='/api/grammar-practice'?(requests++,reply({items:grammarBank.items})):null,grammarRoute);
  await flush();assert.equal(requests,0);assert.equal(hidden.window.document.getElementById('grammar-practice').hidden,true);hidden.window.close();
  const text='<img src=x onerror=alert(1)>',item={number:1,prompt:text,answer:text,options:[text,'two','three','four']};
  const teacher=setup(path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?reply({items:[item]}):null,grammarRoute,'teacher');
  await flush();const root=teacher.window.document.getElementById('grammar-practice');root.querySelector('.grammar-reveal input').click();
  assert(root.textContent.includes(text));assert.equal(root.querySelector('.grammar-prompt img,.grammar-options img'),null);assert.equal(root.querySelector('[onerror]'),null);teacher.window.close();
});

test('grammar discards late loads after navigation, sign-out and page hide', async () => {
  for (const action of ['navigation','sign-out','pagehide']) {
    let resolve;
    const dom=setup(path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?new Promise(r=>{resolve=r;}):null,grammarRoute);
    await flush();const w=dom.window;
    if(action==='navigation')w.location.hash='account';
    else if(action==='sign-out')w.document.getElementById('logout').click();
    else w.dispatchEvent(new w.Event('pagehide'));
    await flush();resolve(reply({items:grammarBank.items}));await flush();
    assert.equal(w.document.getElementById('grammar-practice').textContent,'');assert.equal(w.document.getElementById('grammar-practice').hidden,true);w.close();
  }
});

test('grammar load errors can retry, empty data fails clearly, and expiry clears the view', async () => {
  let failure=true;
  const dom=setup(path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?(failure?reply({items:[]}):reply({items:grammarBank.items})):null,grammarRoute);
  await flush();const root=dom.window.document.getElementById('grammar-practice');assert.match(root.textContent,/could not load/);
  failure=false;root.querySelector('button').click();await flush();assert.equal(root.querySelectorAll('.grammar-item').length,10);dom.window.close();
  const expiredDom=setup(path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null,grammarRoute);
  await flush();assert.equal(expiredDom.window.document.getElementById('login-view').hidden,false);assert.equal(expiredDom.window.document.getElementById('grammar-practice').textContent,'');expiredDom.window.close();
});
const roadRoute = 'https://ab26.englishladder.com/#activities/english-road';
const roadSubmit = dom => dom.window.document.querySelector('#road-practice form').dispatchEvent(new dom.window.Event('submit', { bubbles:true, cancelable:true }));
const roadButton = (d, text) => [...d.querySelectorAll('#road-practice button')].find(b => b.textContent === text);

test('English Road saves actual student answers and resumes the next question on a new page', async () => {
  const {e,student} = await seedQuiz();
  const mock = (path, options={}) => path === '/api/account' ? reply(roadSettings) : path.startsWith('/api/road/') ? call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method ? {Origin:origin}: {})}}) : null;
  const dom=setup(mock,roadRoute);await flush();const d=dom.window.document;
  assert.equal(d.querySelector('#activities-submenu a').textContent,'English Road Practice');
  d.getElementById('road-topic').value='Articles';roadSubmit(dom);await flush();
  assert.equal(d.querySelector('#road-question-title').textContent,'Question 1 of 20');
  const option=d.querySelector('.road-options input');option.checked=true;option.dispatchEvent(new dom.window.Event('change',{bubbles:true}));roadSubmit(dom);await flush();
  assert.match(d.querySelector('.road-answer').textContent,/Your answer:/);
  assert.equal(dom.window.localStorage.length,0);assert.equal(dom.window.sessionStorage.length,0);
  const saved=await(await call(e,'/api/road/state',{headers:{Cookie:student.cookie}})).json();assert.equal(saved.attempt.answered,1);
  dom.window.close();const resumed=setup(mock,roadRoute);await flush();
  assert.equal(resumed.window.document.querySelector('#road-question-title').textContent,'Question 2 of 20');
  resumed.window.document.getElementById('logout').click();await flush();assert.equal(resumed.window.document.getElementById('road-practice').textContent,'');
  resumed.window.close();
});

test('failed English Road saves retry the identical answer; only confirmed saves reveal feedback', async () => {
  const {e,student} = await seedQuiz();let drop=false,bodySeen=null;
  const dom=setup((path,options={})=>{
    if(path==='/api/account')return reply(roadSettings);
    if(!path.startsWith('/api/road/'))return null;
    if(path==='/api/road/answer' && drop) {drop=false;bodySeen=options.body;return Promise.reject(new Error('Connection lost'));}
    if(path==='/api/road/answer' && bodySeen)assert.equal(options.body,bodySeen);
    return call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}});
  },roadRoute);await flush();roadSubmit(dom);await flush();const d=dom.window.document;
  drop=true;const option=d.querySelector('.road-options input');option.checked=true;option.dispatchEvent(new dom.window.Event('change'));roadSubmit(dom);await flush();
  assert.match(d.getElementById('road-practice').textContent,/Not saved yet/);assert.equal(d.querySelector('.road-answer'),null);
  roadButton(d,'Try saving again').click();await flush();assert.ok(d.querySelector('.road-answer'));
  assert.equal((await(await call(e,'/api/road/state',{headers:{Cookie:student.cookie}})).json()).attempt.answered,1);
  dom.window.close();
});

test('English Road clears late responses on navigation, sign-out and expiry and teacher previews never write', async () => {
  let resolve;
  const dom=setup(path=>path==='/api/account'?reply(roadSettings):path==='/api/road/state'?new Promise(r=>{resolve=r;}):null,roadRoute);
  await flush();dom.window.location.hash='account';await flush();
  resolve(reply({catalog:{levels:['A1'],topics:['Articles']},attempt:null}));await flush();
  assert.equal(dom.window.document.getElementById('road-practice').textContent,'');dom.window.close();
  const expiredDom=setup(path=>path==='/api/account'?reply(roadSettings):path==='/api/road/state'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null,roadRoute);
  await flush();assert.equal(expiredDom.window.document.getElementById('login-view').hidden,false);assert.equal(expiredDom.window.document.getElementById('road-practice').textContent,'');expiredDom.window.close();
  let requests=0;
  const teacher=setup(path=>{if(path==='/api/account')return reply(roadSettings);if(path.startsWith('/api/road/')){requests++;return reply({});}},roadRoute,'teacher');await flush();
  assert.match(teacher.window.document.getElementById('road-practice').textContent,/Teacher view does not save/);assert.equal(requests,0);teacher.window.close();
  const hidden=setup(path=>path==='/api/account'?reply({...roadSettings,visibleActivities:[]}):null,roadRoute);await flush();assert.equal(hidden.window.document.getElementById('road-practice').hidden,true);hidden.window.close();
});

test('Business terms saves Finished and Questions, restores them on return, and permits independent undo', async()=>{
  const {e,student}=await seedQuiz();
  const dom=setup((path,options={})=>path==='/api/business-terms/state'?call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}}):termsMock(path),termsRoute);
  await flush();const w=dom.window,root=w.document.getElementById('business-terms');
  const button=name=>[...root.querySelectorAll('button')].find(b=>b.textContent===name);
  assert.match(root.textContent,/Later questions are harder/);
  w.Storage.prototype.setItem=()=>{throw Error('Do not save private choices in browser storage');};
  button('Finish').click();await flush();assert(root.querySelector('.terms-item').classList.contains('is-finished'));assert.equal(button('Finished').getAttribute('aria-pressed'),'true');
  button('Questions').click();await flush();assert.equal(root.querySelector('.terms-questions summary').textContent,'Questions list (1)');
  root.querySelector('.terms-reveal input').click();assert.equal(root.querySelectorAll('.terms-answer').length,6);
  button('Next').click();assert.equal(button('Finish').getAttribute('aria-pressed'),'false');
  root.querySelector('.terms-question-links button').click();assert.match(root.querySelector('h4').textContent,/Item 1/);assert(root.querySelector('.terms-item').classList.contains('is-finished'));
  w.location.hash='overview';await flush();w.location.hash='activities/business-terms';await flush();
  assert.equal(button('Saved to Questions').getAttribute('aria-pressed'),'true');assert.equal(button('Finished').getAttribute('aria-pressed'),'true');assert.equal(root.querySelector('.terms-reveal input').checked,false);
  button('Finished').click();await flush();assert(!root.querySelector('.terms-item').classList.contains('is-finished'));assert.equal(button('Saved to Questions').getAttribute('aria-pressed'),'true');
  button('Saved to Questions').click();await flush();assert.equal(root.querySelector('.terms-questions summary').textContent,'Questions list (0)');
  w.document.getElementById('logout').click();await flush();assert.equal(root.textContent,'');w.close();
});

test('Business terms never pretend a failed save succeeded, recover conflicts, and keep teacher choices read-only', async()=>{
  let fail=true,reads=0;
  const entry={number:1,finished:true,question:false,revision:1,updatedAt:'2026-10-15T12:00:00Z'};
  const dom=setup((path,options)=>path==='/api/business-terms/state'?(options?.method?new Response(JSON.stringify({error:'This item changed. Try again.'}),{status:fail?503:409}):reply({entries:reads++?[entry]:[]})):termsMock(path),termsRoute);
  await flush();const root=dom.window.document.getElementById('business-terms'),finished=[...root.querySelectorAll('button')].find(b=>b.textContent==='Finish');
  finished.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'false');assert.match(root.querySelector('#terms-save-status').textContent,/could not be saved/);assert(!finished.disabled);
  fail=false;finished.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'true');assert.match(root.querySelector('#terms-save-status').textContent,/changed/);dom.window.close();
  let writes=0;const teacher=setup((path,options)=>path==='/api/business-terms/state'?(options?.method?(writes++,reply({})):reply({entries:[{...entry,question:true}]})):termsMock(path),termsRoute,'teacher');
  await flush();const teacherRoot=teacher.window.document.getElementById('business-terms');
  assert.equal(teacherRoot.querySelector('.terms-questions summary').textContent,'Questions list (1)');
  for(const button of teacherRoot.querySelectorAll('.terms-actions button[aria-pressed]')){assert(button.disabled);button.click();}assert.equal(writes,0);teacher.window.close();
});

test('Business terms discards pending saved choices on leaving, logout, page hide and expiry', async()=>{
  for(const action of ['navigation','sign-out','pagehide','expiry']) {
    let resolve;const dom=setup((path,options)=>path==='/api/business-terms/state'?(options?.method?new Promise(r=>{resolve=r;}):reply({entries:[]})):termsMock(path),termsRoute);
    await flush();const w=dom.window,root=w.document.getElementById('business-terms');
    [...root.querySelectorAll('button')].find(b=>b.textContent==='Questions').click();await flush();
    if(action==='navigation')w.location.hash='overview';else if(action==='sign-out')w.document.getElementById('logout').click();else if(action==='pagehide')w.dispatchEvent(new w.Event('pagehide'));
    await flush();resolve(action==='expiry'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):reply({entry:{number:1,question:true,finished:false,revision:1}}));await flush();
    assert.equal(root.textContent,'');assert.equal(root.hidden,true);w.close();
  }
});

const grammarMock=path=>path==='/api/account'?reply(grammarSettings):path==='/api/grammar-practice'?reply({items:grammarBank.items}):null;
test('Grammar saves and independently undoes choices, restores them on return, and jumps to the exact question',async()=>{
  const {e,student}=await seedQuiz();
  const dom=setup((path,options={})=>path==='/api/grammar-practice/state'?call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}}):grammarMock(path),grammarRoute);
  await flush();const w=dom.window,d=w.document,root=d.getElementById('grammar-practice');
  const button=(number,name)=>[...d.getElementById('grammar-item-'+number).querySelectorAll('button')].find(b=>b.textContent===name);
  const group=page=>{const picker=d.getElementById('grammar-group');picker.value=String(page);picker.dispatchEvent(new w.Event('change'));};
  w.Storage.prototype.setItem=()=>{throw Error('Choices must not enter browser storage');};
  button(1,'Finish').click();await flush();assert(d.getElementById('grammar-item-1').classList.contains('is-finished'));assert(!d.getElementById('grammar-item-2').classList.contains('is-finished'));
  group(1);button(12,'Questions').click();await flush();button(12,'Finish').click();await flush();
  group(0);root.querySelector('.grammar-question-links button').click();assert.equal(d.activeElement.id,'grammar-item-12');assert.equal(d.getElementById('grammar-group').value,'1');
  assert.equal(button(12,'Saved to Questions').getAttribute('aria-pressed'),'true');assert.equal(button(12,'Finished').getAttribute('aria-pressed'),'true');
  d.querySelector('#grammar-item-12 input').click();assert(d.querySelector('#grammar-item-12 .grammar-prompt').classList.contains('is-revealed'));
  w.location.hash='overview';await flush();w.location.hash='activities/grammar-practice';await flush();
  assert.equal(button(12,'Finished').getAttribute('aria-pressed'),'true');assert.equal(root.querySelectorAll('input:checked').length,0);assert.equal(d.getElementById('grammar-group').value,'1');
  group(0);assert.equal(button(1,'Finished').getAttribute('aria-pressed'),'true');
  root.querySelector('.grammar-question-links button').click();button(12,'Finished').click();await flush();
  assert(!d.getElementById('grammar-item-12').classList.contains('is-finished'));assert.equal(button(12,'Saved to Questions').getAttribute('aria-pressed'),'true');
  button(12,'Saved to Questions').click();await flush();assert.equal(root.querySelector('.grammar-questions summary').textContent,'Questions list (0)');
  assert.equal(w.localStorage.length,0);assert.equal(w.sessionStorage.length,0);w.close();
});

test('Grammar Questions lists page through saved items and teacher views cannot write choices',async()=>{
  const entries=[...Array.from({length:20},(_,i)=>i+1),900].map(number=>({number,finished:false,question:true,revision:1}));let writes=0;
  const dom=setup((path,options)=>path==='/api/grammar-practice/state'?(options?.method?(writes++,reply({})):reply({entries})):grammarMock(path),grammarRoute,'teacher');
  await flush();const d=dom.window.document,root=d.getElementById('grammar-practice');
  assert.equal(root.querySelectorAll('.grammar-question-links button').length,20);
  for(const button of root.querySelectorAll('.grammar-actions button[aria-pressed]')) {assert(button.disabled);button.click();}
  [...root.querySelectorAll('button')].find(b=>b.textContent==='More questions').click();assert.equal(root.querySelectorAll('.grammar-question-links button').length,1);
  root.querySelector('.grammar-question-links button').click();assert.equal(d.activeElement.id,'grammar-item-900');assert.equal(d.getElementById('grammar-group').value,'89');
  d.querySelector('#grammar-item-900 input').click();assert(d.querySelector('#grammar-item-900 .grammar-prompt').classList.contains('is-revealed'));assert.equal(writes,0);dom.window.close();
});

test('Grammar reports failed saves, reloads conflicts, and safely retries a lost save response',async()=>{
  const {e,student}=await seedQuiz();let mode='failure',drop=true;
  const dom=setup(asyncMock,grammarRoute);
  function asyncMock(path,options={}) {
    if(path!=='/api/grammar-practice/state')return grammarMock(path);
    if(options.method&&mode==='failure')return new Response(JSON.stringify({error:'Unavailable'}),{status:503});
    return (async()=>{
      const response=await call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}});
      if(options.method&&mode==='lost'&&drop){drop=false;throw Error('Response lost');}
      return response;
    })();
  }
  await flush();const root=dom.window.document.getElementById('grammar-practice'),row=root.querySelector('.grammar-item');
  const finished=row.querySelector('button'),question=row.querySelectorAll('button')[1];
  finished.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'false');assert.match(row.querySelector('.grammar-save-status').textContent,/could not be saved/);
  mode='lost';finished.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'false');finished.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'true');
  await call(e,'/api/grammar-practice/state',{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({number:1,field:'finished',value:false,revision:1})});
  mode='normal';question.click();await flush();assert.equal(finished.getAttribute('aria-pressed'),'false');assert.equal(question.getAttribute('aria-pressed'),'false');assert.match(row.querySelector('.grammar-save-status').textContent,/changed/);
  question.click();await flush();assert.equal(question.getAttribute('aria-pressed'),'true');dom.window.close();
});

test('Grammar discards pending saves on navigation, sign-out, page hide and session expiry',async()=>{
  for(const action of ['navigation','sign-out','pagehide','expiry']) {
    let resolve;const dom=setup((path,options)=>path==='/api/grammar-practice/state'?(options?.method?new Promise(r=>{resolve=r;}):reply({entries:[]})):grammarMock(path),grammarRoute);
    await flush();const w=dom.window,root=w.document.getElementById('grammar-practice');root.querySelector('.grammar-actions button').click();await flush();
    if(action==='navigation')w.location.hash='overview';else if(action==='sign-out')w.document.getElementById('logout').click();else if(action==='pagehide')w.dispatchEvent(new w.Event('pagehide'));
    await flush();resolve(action==='expiry'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):reply({entry:{number:1,finished:true,question:false,revision:1}}));await flush();
    assert.equal(root.textContent,'');assert.equal(root.hidden,true);w.close();
  }
});

function filteredPractice(kind, bank, entries, saveOverride) {
  const grammar=kind==='grammar',activity=grammar?'grammar-practice':'business-terms',prefix=grammar?'grammar':'terms';
  const saved=new Map(entries.map(entry=>[entry.number,{revision:1,question:false,...entry}]));let writes=0,preferences={hideFinished:false,revision:0},position={number:null,revision:0};
  const dom=setup((path,options)=>{
    if(path==='/api/account')return reply(grammar?grammarSettings:termsSettings);
    if(path==='/api/'+activity)return reply({items:bank});
    if(path==='/api/'+activity+'/state') {
      if(!options?.method)return reply({entries:[...saved.values()],preferences,position});
      const body=JSON.parse(options.body);
      if(body.field==='position'){position={number:body.value,revision:position.revision+1};return reply({position});}
      if(body.field==='hideFinished'){preferences={hideFinished:body.value,revision:preferences.revision+1};return reply({preferences});}
      writes++;
      if(saveOverride)return saveOverride(body,saved);
      const entry={finished:false,question:false,...saved.get(body.number),number:body.number,[body.field]:body.value,revision:(saved.get(body.number)?.revision||0)+1};
      saved.set(body.number,entry);return reply({entry});
    }
  },'https://ab26.englishladder.com/#activities/'+activity);
  const d=dom.window.document,root=d.getElementById(activity);
  return {dom,d,root,saved,writes:()=>writes,filter:()=>d.getElementById(prefix+'-hide-finished'),button:name=>[...root.querySelectorAll('button')].find(b=>b.textContent===name)};
}

test('Grammar filters before grouping while retaining original numbers and finished discussion links',async()=>{
  const f=filteredPractice('grammar',grammarBank.items.slice(0,23),[1,4,13].map(number=>({number,finished:true,question:number===13})));await flush();
  const numbers=()=>[...f.root.querySelectorAll('.grammar-item')].map(row=>row.value);
  f.filter().click();await flush();assert.deepEqual(numbers(),[2,3,5,6,7,8,9,10,11,12]);assert.equal(f.d.activeElement,f.filter());
  assert.deepEqual([...f.d.getElementById('grammar-group').options].map(o=>o.textContent),['2–12','14–23']);
  f.button('Next 10').click();assert.deepEqual(numbers(),[14,15,16,17,18,19,20,21,22,23]);assert(f.button('Next 10').disabled);
  f.button('Previous 10').click();assert.equal(numbers()[0],2);
  f.root.querySelector('.grammar-question-links button').click();assert(!f.filter().checked);assert.equal(f.d.activeElement.id,'grammar-item-13');assert.match(f.root.textContent,/Showing all items/);
  assert.equal(f.writes(),0);f.dom.window.close();
  const last=filteredPractice('grammar',grammarBank.items.slice(0,12),[]);await flush();last.filter().click();await flush();last.button('Next 10').click();
  last.button('Finish').click();await flush();assert.equal(last.d.querySelector('.grammar-item').value,12);
  last.button('Finish').click();await flush();assert.equal(last.d.getElementById('grammar-group').value,'0');assert.equal(last.root.querySelectorAll('.grammar-item').length,10);assert(last.button('Next 10').disabled);last.dom.window.close();
});

test('Business terms skips finished items in both directions and restores requested finished items',async()=>{
  const f=filteredPractice('terms',termsBank.items.slice(0,4),[{number:1,finished:true},{number:3,finished:true,question:true}]);await flush();
  const current=()=>Number(f.d.getElementById('terms-number').value);
  f.filter().click();await flush();assert.equal(current(),2);assert(f.button('Previous').disabled);
  f.button('Next').click();assert.equal(current(),4);assert(f.button('Next').disabled);
  f.button('Previous').click();assert.equal(current(),2);
  f.button('Finish').click();await flush();assert.equal(current(),4);
  const number=f.d.getElementById('terms-number');number.value='1';number.form.dispatchEvent(new f.dom.window.Event('submit',{bubbles:true,cancelable:true}));
  assert.equal(current(),1);assert(!f.filter().checked);assert.match(f.root.textContent,/Showing all items/);
  f.filter().click();await flush();f.root.querySelector('.terms-question-links button').click();assert.equal(current(),3);assert(!f.filter().checked);
  assert.equal(f.writes(),1);f.dom.window.close();
});

test('Both filters advance after saved completion, handle the final item, and remember the filter without changing item choices',async()=>{
  for(const kind of ['grammar','terms']) {
    const bank=(kind==='grammar'?grammarBank:termsBank).items.slice(0,11);
    const f=filteredPractice(kind,bank,bank.slice(0,10).map(item=>({number:item.number,finished:true,question:item.number===1})));await flush();
    f.filter().click();await flush();f.button('Finish').click();await flush();
    assert.equal(f.saved.get(11).finished,true);assert(f.filter().checked);assert.match(f.root.querySelector('.practice-empty').textContent,/All items are finished/);
    assert.equal(f.root.querySelectorAll('.grammar-item,.terms-item').length,0);assert.match(f.root.querySelector('summary').textContent,/Questions list \(1\)/);
    f.filter().click();await flush();assert(f.button('Finished'));assert.equal(f.writes(),1);
    f.filter().click();await flush();f.dom.window.location.hash='overview';await flush();f.dom.window.location.hash='activities/'+(kind==='grammar'?'grammar-practice':'business-terms');await flush();
    assert(f.filter().checked);assert(f.root.querySelector('.practice-empty'));assert.equal(f.saved.size,11);assert.equal(f.dom.window.localStorage.length,0);assert.equal(f.dom.window.sessionStorage.length,0);f.dom.window.close();
  }
});

test('Neither filter hides unsaved work and both recover when a concurrent saved choice hides the current item',async()=>{
  for(const kind of ['grammar','terms']) {
    let resolve;
    const bank=(kind==='grammar'?grammarBank:termsBank).items.slice(0,2);
    const f=filteredPractice(kind,bank,[],()=>new Promise(r=>{resolve=r;}));await flush();
    f.filter().click();await flush();f.button('Finish').click();await flush();assert(f.filter().disabled);
    resolve(new Response(JSON.stringify({error:'Unavailable'}),{status:503}));await flush();
    assert(!f.filter().disabled);assert(f.button('Finish'));assert.match(f.root.textContent,/could not be saved/);assert.equal(f.saved.size,0);
    f.button('Finish').click();await flush();f.saved.set(1,{number:1,finished:true,question:false,revision:1});
    resolve(new Response(JSON.stringify({error:'This item changed.'}),{status:409}));await flush();
    assert(f.filter().checked);assert.match(f.root.textContent,/saved choices have changed/);
    if(kind==='grammar')assert(!f.d.getElementById('grammar-item-1'));else assert.equal(f.d.getElementById('terms-number').value,'2');
    f.dom.window.close();
  }
});

for(const [activity,prefix,bank,settings] of [['grammar-practice','grammar',grammarBank,grammarSettings],['business-terms','terms',termsBank,termsSettings]]) {
 test(activity+' remembers the filter across visits and page loads without letting teacher previews change it',async()=>{
  const {e,student}=await seedQuiz();const path='/api/'+activity+'/state';let writes=0,drop=true;
  await call(e,path,{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({number:1,field:'finished',value:true,revision:0})});
  const mock=(url,options={})=>{
    if(url==='/api/account')return reply(settings);
    if(url==='/api/'+activity)return reply({items:bank.items.slice(0,2)});
    if(url===path)return(async()=>{
      if(options.method)writes++;
      const response=await call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}});
      if(options.method&&drop){drop=false;throw Error('Response lost');}return response;
    })();
  };
  const route='https://ab26.englishladder.com/#activities/'+activity;
  const first=setup(mock,route);await flush();const root=first.window.document.getElementById(activity),filter=()=>root.querySelector('.practice-filter input');
  assert(!filter().checked);filter().click();await flush();assert(!filter().checked);assert.match(root.textContent,/could not be saved/);
  filter().click();await flush();assert(filter().checked);
  first.window.location.hash='overview';await flush();first.window.location.hash='activities/'+activity;await flush();assert(filter().checked);
  assert.equal(first.window.localStorage.length,0);assert.equal(first.window.sessionStorage.length,0);first.window.close();
  const next=setup(mock,route);await flush();assert(next.window.document.getElementById(prefix+'-hide-finished').checked);next.window.close();
  const teacher=setup(mock,route,'teacher');await flush();const teacherFilter=()=>teacher.window.document.getElementById(prefix+'-hide-finished');
  const before=writes;teacherFilter().click();await flush();assert(!teacherFilter().checked);assert.equal(writes,before);teacher.window.close();
  const last=setup(mock,route);await flush();const lastFilter=()=>last.window.document.getElementById(prefix+'-hide-finished');assert(lastFilter().checked);lastFilter().click();await flush();assert(!lastFilter().checked);last.window.close();
  assert.equal((await(await call(e,path,{headers:{Cookie:student.cookie}})).json()).preferences.hideFinished,false);
 });
 test(activity+' keeps the saved filter on failure, reloads conflicts, and discards late preference responses',async()=>{
  const path='/api/'+activity+'/state';let resolve,preferences={hideFinished:false,revision:0};
  const mock=(url,options)=>url==='/api/account'?reply(settings):url==='/api/'+activity?reply({items:bank.items.slice(0,2)}):url===path?(options?.method?new Promise(r=>{resolve=r;}):reply({entries:[{number:1,finished:true,question:false,revision:1}],preferences})):null;
  const route='https://ab26.englishladder.com/#activities/'+activity;
  const dom=setup(mock,route);await flush();const root=dom.window.document.getElementById(activity),filter=()=>root.querySelector('.practice-filter input');
  filter().click();await flush();assert(filter().disabled);resolve(new Response(JSON.stringify({error:'Unavailable'}),{status:503}));await flush();assert(!filter().checked);assert(!filter().disabled);assert.match(root.textContent,/could not be saved/);
  filter().click();await flush();preferences={hideFinished:true,revision:1};resolve(new Response(JSON.stringify({error:'Changed elsewhere'}),{status:409}));await flush();assert(filter().checked);assert.match(root.textContent,/saved choice is shown/);dom.window.close();
  for(const action of ['navigation','sign-out','pagehide','expiry']) {
    const late=setup(mock,route);await flush();const w=late.window,r=w.document.getElementById(activity);r.querySelector('.practice-filter input').click();await flush();
    if(action==='navigation')w.location.hash='overview';else if(action==='sign-out')w.document.getElementById('logout').click();else if(action==='pagehide')w.dispatchEvent(new w.Event('pagehide'));
    await flush();resolve(action==='expiry'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):reply({preferences:{hideFinished:false,revision:2}}));await flush();
    assert.equal(r.textContent,'');assert(r.hidden);w.close();
  }
 });
}

for(const [activity,prefix,bank,settings] of [['grammar-practice','grammar',grammarBank,grammarSettings],['business-terms','terms',termsBank,termsSettings]]) {
 test(activity+' restores its private place on a new page, respects hidden items, and leaves teacher navigation unsaved',async()=>{
  const {e,student}=await seedQuiz(),path='/api/'+activity+'/state',route=origin+'/#activities/'+activity,grammar=prefix==='grammar';let writes=0;
  const read=async()=>(await(await call(e,path,{headers:{Cookie:student.cookie}})).json());
  const save=async body=>{const r=await call(e,path,{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)});assert.equal(r.status,200);};
  const mock=(url,options={})=>{
   if(url==='/api/account')return reply(settings);
   if(url==='/api/'+activity)return reply({items:bank.items.slice(0,60)});
   if(url===path){if(options.method)writes++;return call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}});}
  };
  const number=dom=>grammar?dom.window.document.querySelector('.grammar-item').value:Number(dom.window.document.getElementById('terms-number').value);
  const go=(dom,value)=>{
   const d=dom.window.document;
   if(grammar){const picker=d.getElementById('grammar-group');picker.value=String((value-1)/10);picker.dispatchEvent(new dom.window.Event('change'));}
   else {const input=d.getElementById('terms-number');input.value=String(value);input.form.dispatchEvent(new dom.window.Event('submit',{bubbles:true,cancelable:true}));}
  };
  await save({number:31,field:'question',value:true,revision:0});
  const first=setup(mock,route);await flush();assert.equal(writes,0);assert.equal(number(first),1);
  const firstRoot=first.window.document.getElementById(activity);
  firstRoot.querySelector('.'+prefix+'-reveal input').click();await flush();assert.equal(writes,0);
  firstRoot.querySelector('.'+prefix+'-question-links button').click();await flush();assert.equal((await read()).position.number,31);
  go(first,21);await flush();assert.equal((await read()).position.number,21);
  first.window.location.hash='overview';await flush();first.window.location.hash='activities/'+activity;await flush();assert.equal(number(first),21);
  assert.equal(first.window.document.querySelector('.'+prefix+'-reveal input').checked,false);first.window.close();
  const before=writes,second=setup(mock,route);await flush();assert.equal(number(second),21);assert.equal(writes,before);second.window.close();
  for(const item of bank.items.filter(item=>item.number<=21))await save({number:item.number,field:'finished',value:true,revision:0});
  await save({field:'hideFinished',value:true,revision:0});
  const hidden=setup(mock,route);await flush();assert.equal(number(hidden),22);assert.equal(writes,before);assert.equal((await read()).position.number,21);hidden.window.close();
  const teacher=setup(mock,route,'teacher');await flush();const teacherRoot=teacher.window.document.getElementById(activity);
  [...teacherRoot.querySelectorAll('button')].find(b=>b.textContent===(grammar?'Next 10':'Next')).click();await flush();assert.equal(writes,before);assert.equal((await read()).position.number,21);teacher.window.close();
  const last=setup(mock,route);await flush();const lastRoot=last.window.document.getElementById(activity);
  [...lastRoot.querySelectorAll('button')].find(b=>b.textContent===(grammar?'Next 10':'Next')).click();await flush();
  assert.equal((await read()).position.number,number(last));assert.equal((await read()).preferences.hideFinished,true);last.window.close();
 });
}

for(const [activity,prefix,settings,bank] of [['grammar-practice','grammar',grammarSettings,grammarBank],['business-terms','terms',termsSettings,termsBank]]) {
 test(activity+' copies only its exercise into a hidden explanation prompt without saving or revealing answers',async()=>{
  const calls=[],copies=[];
  const dom=setup((path,options)=>{
   calls.push({path,method:options?.method||'GET'});
   if(path==='/api/account')return reply(settings);
   if(path==='/api/'+activity)return reply({items:bank.items});
  },origin+'/#activities/'+activity);await flush();
  const w=dom.window,d=w.document,root=d.getElementById(activity);
  Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>copies.push(text)}});
  const initial=calls.length,button=root.querySelector('.practice-copy-button');
  assert.equal(button.textContent,'Copy AI prompt');assert(!root.textContent.includes('Help me understand this English practice item'));
  assert.equal(copies.length,0);button.click();await flush();
  assert.equal(button.textContent,'AI prompt copied');assert.equal(button.getAttribute('aria-label'),'AI prompt copied for item 1');
  assert.equal(calls.length,initial);assert.equal(root.querySelector('.'+prefix+'-reveal input').checked,false);assert.equal(copies.length,1);
  assert.match(copies[0],/short, simple English/);assert.match(copies[0],/Wait for my reply/);assert.match(copies[0],/Answer key/);
  for(const option of bank.items[0].options)assert(copies[0].includes(option));
  if(prefix==='grammar')assert(copies[0].includes('Completed sentence: “Tom is much more intelligent than Mike.”'));
  else {assert.match(copies[0],/1: “plates”/);assert.match(copies[0],/6: “novels”/);assert.match(copies[0],/____ \(6\)/);}
  assert.doesNotMatch(copies[0],/Alex|ab26|student-test|https:|Finished|Saved to Questions/);
  assert.equal(root.querySelectorAll('.practice-copy-buffer,textarea').length,0);assert.equal(w.localStorage.length,0);assert.equal(w.sessionStorage.length,0);
  [...root.querySelectorAll('button')].find(b=>b.textContent===(prefix==='grammar'?'Next 10':'Next')).click();await flush();
  const next=root.querySelector('.practice-copy-button');assert.equal(next.textContent,'Copy AI prompt');next.click();await flush();assert.notEqual(copies[0],copies[1]);w.close();
 });
}

test('English Road explanation prompts work before answering, after feedback, and in review without altering attempts',async()=>{
 const {e,student}=await seedQuiz();let writes=0,copied='';
 const dom=setup((path,options={})=>{
  if(path==='/api/account')return reply(roadSettings);
  if(path.startsWith('/api/road/')){if(options.method)writes++;return call(e,path,{...options,headers:{...options.headers,Cookie:student.cookie,...(options.method?{Origin:origin}:{})}});}
 },roadRoute);await flush();const w=dom.window,d=w.document,root=d.getElementById('road-practice');
 Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
 roadSubmit(dom);await flush();const before=writes;
 const read=async()=>(await(await call(e,'/api/road/state',{headers:{Cookie:student.cookie}})).json()).attempt;
 const original=await read();root.querySelector('.practice-copy-button').click();await flush();
 assert.equal(root.querySelector('.practice-copy-button').textContent,'AI prompt copied');assert.equal(writes,before);assert.deepEqual(await read(),original);
 assert(copied.includes(original.questions[0].prompt));assert.doesNotMatch(copied,/Answer key:|Exercise explanation:|Your answer:|Alex|ab26|student-test/);
 const option=d.querySelector('.road-options input');option.checked=true;option.dispatchEvent(new w.Event('change'));roadSubmit(dom);await flush();
 const answered=await read(),answeredWrites=writes;root.querySelector('.practice-copy-button').click();await flush();
 assert.equal(writes,answeredWrites);assert.deepEqual(await read(),answered);assert(copied.includes(answered.questions[0].explanation));assert.match(copied,/Answer key:/);assert.doesNotMatch(copied,/Your answer:|correct out of/);
 roadButton(d,'Next question').click();assert.equal(root.querySelector('.practice-copy-button').textContent,'Copy AI prompt');
 w.confirm=()=>true;roadButton(d,'End this set').click();await flush();const ended=await read(),endedWrites=writes;
 root.querySelector('.road-review .practice-copy-button').click();await flush();assert.equal(writes,endedWrites);assert.deepEqual(await read(),ended);assert(copied.includes(answered.questions[0].prompt));w.close();
});

test('practice copy buttons fall back safely, report failure honestly, and ignore clipboard results after navigation',async()=>{
 const dom=setup(grammarMock,grammarRoute);await flush();const w=dom.window,d=w.document,root=d.getElementById('grammar-practice');
 let copied='';d.execCommand=command=>{assert.equal(command,'copy');copied=d.querySelector('.practice-copy-buffer').value;return true;};
 let button=root.querySelector('.practice-copy-button');button.focus();button.click();await flush();
 assert.match(copied,/Tom _______/);assert.equal(button.textContent,'AI prompt copied');assert.equal(d.activeElement,button);assert.equal(d.querySelector('.practice-copy-buffer'),null);
 d.execCommand=()=>false;button.click();await flush();assert.equal(button.textContent,'Copy AI prompt');assert.match(root.querySelector('.practice-copy-status').textContent,/could not be copied/);assert.equal(d.querySelector('.practice-copy-buffer'),null);
 let finish;Object.defineProperty(w.navigator,'clipboard',{value:{writeText:()=>new Promise(resolve=>{finish=resolve;})}});
 button.click();w.location.hash='overview';await flush();assert.equal(root.textContent,'');finish();await flush();assert.equal(root.textContent,'');
 w.location.hash='activities/grammar-practice';await flush();button=root.querySelector('.practice-copy-button');assert.equal(button.textContent,'Copy AI prompt');assert(root.querySelector('.practice-copy-status').hidden);w.close();
});

test('study topics save Finish and Questions independently and restore choices on reopening',async()=>{
 const {e,student}=await seedQuiz();let writes=0;
 const dom=setup((path,options)=>{
  if(!path.startsWith('/api/study/'))return null;
  if(options?.method)writes++;
  return call(e,path,{...options,headers:{Cookie:student.cookie,Origin:origin,...options?.headers}});
 },origin+'/#assessments/next');await flush();const w=dom.window,d=w.document;
 const root=()=>d.getElementById('study-topics'),row=()=>root().querySelector('.study-current .assessment-plan-card');
 const finish=()=>row().querySelector('.study-finish'),question=()=>row().querySelector('.question-button');
 assert.equal(writes,0);assert(!finish().disabled);finish().click();await flush();
 assert.equal(finish().textContent,'Finished');assert(row().classList.contains('is-finished'));
 question().click();await flush();assert.equal(question().textContent,'Saved to Questions');assert.equal(root().querySelectorAll('.study-question-items .assessment-plan-card').length,1);
 const before=writes;w.location.hash='overview';await flush();assert.equal(root().textContent,'');w.location.hash='assessments/next';await flush();
 assert.equal(writes,before);assert.equal(finish().getAttribute('aria-pressed'),'true');assert.equal(question().getAttribute('aria-pressed'),'true');
 finish().click();await flush();assert(!row().classList.contains('is-finished'));assert.equal(question().textContent,'Saved to Questions');
 root().querySelector('.study-question-items .question-button').click();await flush();assert.equal(question().textContent,'Questions');assert.equal(root().querySelectorAll('.study-question-items .assessment-plan-card').length,0);
 assert.equal(w.localStorage.length,0);assert.equal(w.sessionStorage.length,0);w.close();
});

test('study saves handle failures, lost responses and conflicting changes without false success',async()=>{
 const {e,student}=await seedQuiz();let mode='failed';
 const mock=(path,options)=>{
  if(!path.startsWith('/api/study/'))return null;
  if(options?.method && mode==='failed')return Promise.resolve(new Response(JSON.stringify({error:'Unavailable'}),{status:503}));
  return call(e,path,{...options,headers:{Cookie:student.cookie,Origin:origin,...options?.headers}}).then(response=>{if(options?.method&&mode==='lost'){mode='normal';throw Error('Lost response');}return response;});
 };
 const page=setup(mock,origin+'/#assessments/next');await flush();const d=page.window.document;
 const button=()=>d.querySelector('.study-current .study-finish'),question=()=>d.querySelector('.study-current .question-button');
 button().click();await flush();assert.equal(button().textContent,'Finish');assert.match(d.querySelector('.study-save-status').textContent,/could not be saved/);
 mode='lost';button().click();await flush();assert.equal(button().textContent,'Finish');button().click();await flush();assert.equal(button().textContent,'Finished');
 const id=studyFixture[0].id;await call(e,'/api/study/state',{method:'PATCH',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({id,field:'finished',value:false,revision:1})});
 question().click();await flush();assert.equal(button().textContent,'Finish');assert.equal(question().textContent,'Questions');assert.match(d.querySelector('.study-save-status').textContent,/changed on another page/);
 question().click();await flush();assert.equal(question().textContent,'Saved to Questions');page.window.close();
});

test('study teacher previews and old questions are readable without writes',async()=>{
 const old={...studyFixture[0],title:'Earlier topic',id:'a'.repeat(64),current:false,progress:{id:'a'.repeat(64),question:true,finished:true,revision:2}};let writes=0;
 const dom=setup((path,options)=>{if(options?.method)writes++;return path.startsWith('/api/study/questions')?reply({questions:[old],nextCursor:null}):null;},origin+'/#assessments/next','teacher');await flush();
 const d=dom.window.document;assert.match(d.querySelector('.study-question-items').textContent,/Earlier topic/);assert.match(d.querySelector('.study-question-items').textContent,/From an earlier assessment/);
 assert(d.querySelector('.study-question-items .assessment-plan-card').classList.contains('is-finished'));
 for(const b of d.querySelectorAll('.study-finish,.study-actions .question-button')){assert(b.disabled);b.click();}
 assert.equal(writes,0);dom.window.close();
});

test('study choices and late responses clear on leaving, page hide, logout and expiry',async()=>{
 for(const action of ['leave','pagehide','logout','expiry']){
  let resolve;const dom=setup((path,options)=>path==='/api/study/state'&&options?.method?new Promise(r=>{resolve=r;}):null,origin+'/#assessments/next');await flush();
  const w=dom.window,d=w.document;d.querySelector('.study-current .study-finish').click();await flush();
  if(action==='leave')w.location.hash='overview';else if(action==='pagehide')w.dispatchEvent(new w.Event('pagehide'));else if(action==='logout')d.getElementById('logout').click();
  await flush();resolve(action==='expiry'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):reply({entry:{...studyFixture[0].progress,finished:true,revision:1}}));await flush();
  assert.equal(d.querySelectorAll('.study-finish').length,0);assert.equal(d.querySelectorAll('.study-question-items .assessment-plan-card').length,0);
  if(['logout','expiry'].includes(action))assert.equal(d.getElementById('login-view').hidden,false);w.close();
 }
});

test('failed study state loading preserves reading and copy controls, and offers retry',async()=>{
 let failed=true;const dom=setup(path=>path==='/api/study/state'&&failed?new Response(JSON.stringify({error:'Offline'}),{status:503}):null,origin+'/#assessments/next');await flush();
 const d=dom.window.document;assert(d.querySelector('.study-current .study-finish').disabled);assert(!d.querySelector('.study-current .practice-copy-button').disabled);
 const retry=[...d.querySelectorAll('#study-topics button')].find(b=>b.textContent==='Try again');assert(!retry.hidden);failed=false;retry.click();await flush();assert(!d.querySelector('.study-current .study-finish').disabled);dom.window.close();
});
