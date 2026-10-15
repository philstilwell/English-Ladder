import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {JSDOM} from 'jsdom';
import {feedback,assessment,quiz} from './fixture.mjs';
const html=readFileSync(new URL('../public/index.html',import.meta.url),'utf8');
const script=readFileSync(new URL('../public/portal.js',import.meta.url),'utf8');
const second={...feedback,id:'2026-09-01-2057',startedAt:'2026-09-02T00:57:01Z',title:'Earlier English lesson'};
const profile={student:{id:'ab26',name:'Alex',nickname:'Alex the Explorer'},role:'student'};
const reply=data=>new Response(JSON.stringify(data));
const flush=async()=>{for(let i=0;i<8;i++)await new Promise(resolve=>setImmediate(resolve));};
function setup(custom,url='https://ab26.englishladder.com/'){
 const dom=new JSDOM(html,{url,runScripts:'outside-only',pretendToBeVisual:true});
 const w=dom.window;w.setInterval=()=>0;
 w.fetch=async(path,options)=>{
  const customResult=custom?.(path,options);if(customResult)return customResult;
  if(path==='/api/context')return reply({id:'ab26'});
  if(path==='/api/session'||path==='/api/login')return reply(profile);
  if(path==='/api/logout')return reply({ok:true});
  if(path==='/api/assessment')return reply({assessment});
  if(path==='/api/feedback')return reply({sessions:[feedback,second],nextCursor:null});
  return reply(path.endsWith(second.id)?second:feedback);
 };
 w.eval(script);return dom;
}
test('deep links open the selected page and show only student-safe content',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#feedback/'+second.id);await flush();
 const d=dom.window.document;
 assert.equal(d.getElementById('feedback-title').textContent,second.title);
 assert.match(d.getElementById('profile-nickname').textContent,/Alex the Explorer/);
 assert.equal(d.querySelectorAll('#session-list a').length,2);
 assert.match(d.getElementById('feedback-page').textContent,/Japan:/);
 assert.equal(d.querySelectorAll('.practice-item details').length,1);
 dom.window.close();
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
test('sign-out clears profile, records, summaries, and late responses',async()=>{
 let resolveFirst;
 const dom=setup(path=>path.endsWith('/'+feedback.id)?new Promise(resolve=>{resolveFirst=resolve;}):null);await flush();
 dom.window.document.getElementById('logout').click();await flush();
 resolveFirst(reply(feedback));await flush();
 const d=dom.window.document;
 assert.equal(d.getElementById('login-view').hidden,false);
 for(const id of ['feedback-page','session-list','session-select','session-summaries','profile-nickname','assessment-content','assessment-source-count','quiz-content'])assert.equal(d.getElementById(id).textContent,'');
 assert.doesNotMatch(d.getElementById('dashboard-view').textContent,/Alex|Clear explanations|Earlier English lesson/);
 dom.window.close();
});
test('expired feedback sessions return to sign-in and clear private content',async()=>{
 const dom=setup(path=>path.startsWith('/api/feedback/')?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null);
 await flush();
 assert.equal(dom.window.document.getElementById('login-view').hidden,false);
 assert.equal(dom.window.document.getElementById('session-list').textContent,'');
 dom.window.close();
});
test('feedback strings render as text, never executable markup',async()=>{
 const data={...feedback,title:'<img src=x onerror=alert(1)>'};
 const dom=setup(path=>path.endsWith('/'+feedback.id)?reply(data):null);await flush();
 assert.equal(dom.window.document.querySelector('#feedback-page img'),null);
 assert.equal(dom.window.document.getElementById('feedback-title').textContent,data.title);
 dom.window.close();
});

test('assessment shows strengths, patterns, next priorities, and only internal evidence links',async()=>{
 const dom=setup(null,'https://ab26.englishladder.com/#assessments');await flush();
 const d=dom.window.document,content=d.getElementById('assessment-content');
 assert.equal(d.getElementById('assessments').hidden,false);
 for(const text of ['What you do well','Things to practice','Your next steps',assessment.summary,assessment.nextLesson])assert.ok(content.textContent.includes(text));
 assert.equal(d.getElementById('assessment-count').textContent,'Overall assessment · Oct 14, 2026');
 assert.equal(d.querySelectorAll('.assessment-evidence').length,3);
 assert.ok([...d.querySelectorAll('.assessment-evidence')].every(a=>a.hash==='#feedback/'+feedback.id));
 assert.equal(d.querySelectorAll('a[href*="mynotes.zoom.us"]').length,0);
 d.querySelector('.assessment-evidence').click();await new Promise(r=>setTimeout(r,10));await flush();
 assert.equal(d.getElementById('feedback-title').textContent,feedback.title);
 assert.equal(d.querySelectorAll('a[href*="mynotes.zoom.us"]').length,0);
 dom.window.close();
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
 assert.equal(dom.window.document.getElementById('assessment-summary').textContent,assessment.title);
 dom.window.close();
});
test('assessment expiry clears records and assessment text cannot inject markup',async()=>{
 const expired=setup(path=>path==='/api/assessment'?new Response(JSON.stringify({error:'Please sign in.'}),{status:401}):null);await flush();
 assert.equal(expired.window.document.getElementById('login-view').hidden,false);
 assert.equal(expired.window.document.getElementById('assessment-content').textContent,'');
 expired.window.close();
 const title='<img src=x onerror=alert(1)>';
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,title}}):null);await flush();
 assert.equal(dom.window.document.querySelector('#assessment-content img'),null);
 assert.equal(dom.window.document.getElementById('assessment-summary').textContent,title);
 dom.window.close();
});

test('quiz gives feedback for every choice, waits for a correct answer, and counts first tries only',async()=>{
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz}}):null,'https://ab26.englishladder.com/#quiz');
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
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz}}):null,'https://ab26.englishladder.com/#quiz');
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
 const empty=setup(null,'https://ab26.englishladder.com/#quiz');await flush();
 assert.match(empty.window.document.getElementById('quiz-content').textContent,/Your teacher can add a quiz/);
 empty.window.close();
 const failed=setup(path=>path==='/api/assessment'?new Response(JSON.stringify({error:'Try again.'}),{status:503}):null,'https://ab26.englishladder.com/#quiz');await flush();
 assert.match(failed.window.document.getElementById('quiz-content').textContent,/could not be loaded/);
 assert.equal(failed.window.document.querySelector('#quiz-content button').textContent,'Try again');
 failed.window.close();
 const q=structuredClone(quiz);q.questions[0].prompt='<img src=x onerror=alert(1)>';
 q.questions[0].options[0].feedback='<script>alert(1)</script>';
 const safe=setup(path=>path==='/api/assessment'?reply({assessment:{...assessment,quiz:q}}):null,'https://ab26.englishladder.com/#quiz');
 await flush();const d=safe.window.document;
 assert.equal(d.getElementById('quiz-question-title').textContent,q.questions[0].prompt);
 d.querySelector('.quiz-option').click();
 assert.ok(d.getElementById('quiz-result').textContent.includes(q.questions[0].options[0].feedback));
 assert.equal(d.querySelector('#quiz-content img, #quiz-content script'),null);
 safe.window.close();
});
test('late quiz data cannot appear after sign-out',async()=>{
 let resolve;
 const dom=setup(path=>path==='/api/assessment'?new Promise(r=>{resolve=r;}):null,'https://ab26.englishladder.com/#quiz');
 await flush();dom.window.document.getElementById('logout').click();await flush();
 resolve(reply({assessment:{...assessment,quiz}}));await flush();
 assert.equal(dom.window.document.getElementById('quiz-content').textContent,'');
 dom.window.close();
});
