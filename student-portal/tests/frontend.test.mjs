import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {JSDOM} from 'jsdom';
import {feedback,assessment,quiz} from './fixture.mjs';
import {seedQuiz,call,origin} from './harness.mjs';
const html=readFileSync(new URL('../public/index.html',import.meta.url),'utf8');
const script=readFileSync(new URL('../public/portal.js',import.meta.url),'utf8');
const second={...feedback,id:'2026-09-01-2057',startedAt:'2026-09-02T00:57:01Z',title:'Earlier English lesson'};
const profile={student:{id:'ab26',name:'Alex',nickname:'Alex the Explorer'},role:'student'};
const reply=data=>new Response(JSON.stringify(data));
const flush=async()=>{for(let i=0;i<12;i++)await new Promise(resolve=>setTimeout(resolve,1));};
function setup(custom,url='https://ab26.englishladder.com/',role='student'){
 const dom=new JSDOM(html,{url,runScripts:'outside-only',pretendToBeVisual:true});
 const w=dom.window;w.setInterval=()=>0;
 w.fetch=async(path,options)=>{
  const customResult=custom?.(path,options);if(customResult)return customResult;
  if(path==='/api/context')return reply({id:'ab26'});
  if(path==='/api/session'||path==='/api/login')return reply({...profile,role});
  if(path==='/api/logout')return reply({ok:true});
  if(path==='/api/assessment')return reply({assessment});
  if(path==='/api/quiz/state')return reply({attempt:null});
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
 assert.doesNotMatch(d.getElementById('feedback-page').textContent,/Lesson time|\d{2}:\d{2}:\d{2}|text covers|Each time shows/);
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
 assert.equal(d.querySelector('#quiz-content img, #quiz-content script'),null);
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

test('self-study prompts copy exactly, stay plain text, and offer a manual-copy fallback',async()=>{
 const aiPrompt='Teach me “access a file” and “have access to a file”. <img src=x> Explain them simply, then ask one question at a time.';
 const record={...assessment,plan:[{...assessment.plan[0],aiPrompt}]};
 const dom=setup(path=>path==='/api/assessment'?reply({assessment:record}):null,origin+'/#assessments/next');await flush();
 const d=dom.window.document;let copied;
 Object.defineProperty(dom.window.navigator,'clipboard',{value:{writeText:async text=>{copied=text;}}});
 d.querySelector('.study-prompt summary').click();
 const button=d.querySelector('.study-prompt button');
 button.click();await flush();
 assert.equal(copied,aiPrompt);assert.match(d.querySelector('.study-prompt-status').textContent,/Copied/);
 assert.equal(d.querySelector('.study-prompt-text img'),null);
 dom.window.navigator.clipboard.writeText=async()=>{throw Error('Denied');};
 button.click();await flush();
 assert.match(d.querySelector('.study-prompt-status').textContent,/Select the prompt above/);
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
  box.querySelector('summary').click();
  assert.equal(box.querySelectorAll('button').length,1);
  assert.equal(box.querySelector('button').textContent,'Copy AI prompt');
  const links=[...box.querySelectorAll('a')];assert.equal(links.length,4);
  assert.deepEqual(links.map(link=>link.href),['https://chatgpt.com/','https://gemini.google.com/app','https://claude.ai/','https://copilot.microsoft.com/']);
  for(const link of links){
   assert.equal(link.target,'_blank');assert.equal(link.rel,'noopener noreferrer');
   assert.equal(link.referrerPolicy,'no-referrer');assert.match(link.getAttribute('aria-label'),/new tab/);
   assert.ok(link.title);assert.equal(link.textContent,'');
   const image=link.querySelector('img');assert.ok(image);assert.equal(image.alt,'');
   assert.equal(new URL(image.src).origin,new URL(origin).origin);
   link.addEventListener('click',event=>event.preventDefault());
   link.click();
  }
 }
 await flush();
 assert.equal(copied,undefined);
 boxes[0].querySelector('button').click();await flush();assert.equal(copied,aiPrompt);
 boxes[1].querySelector('button').click();await flush();
 assert.equal(copied,boxes[1].querySelector('.study-prompt-text').textContent);
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

const settingsFixture = { nickname: 'Alex the Explorer', revision: 1, visibleActivities: ['placeholder-1', 'placeholder-2', 'placeholder-3'], activities: [1, 2, 3].map(n => ({ id: 'placeholder-' + n, name: 'Activity ' + n, description: 'A sample activity.' })) };
const submitForm = (dom, id) => dom.window.document.getElementById(id).dispatchEvent(new dom.window.Event('submit', { bubbles: true, cancelable: true }));
test('Account menu loads saved choices, saves a nickname and empty selection, and keeps teacher preview read-only', async () => {
  let saved = structuredClone(settingsFixture), writes = 0;
  const mock = (path, options) => {
    if (path !== '/api/account') return null;
    if (options.method === 'PUT') { const body = JSON.parse(options.body); writes++; saved = { ...saved, ...body, revision: saved.revision + 1 }; }
    return reply(saved);
  };
  const dom = setup(mock, 'https://ab26.englishladder.com/#account'); await flush(); const d = dom.window.document;
  assert.equal(d.querySelector('.section-nav [aria-current]').hash, '#account');
  assert.equal(d.querySelector('.section-nav a[href="#activities"]'), null);
  assert.equal(d.getElementById('account').hidden, false); assert.equal(d.querySelectorAll('#activity-options input:checked').length, 3);
  d.getElementById('nickname').value = '<b>New nickname</b>';
  for (const box of d.querySelectorAll('#activity-options input')) box.checked = false;
  submitForm(dom, 'settings-form'); await flush(); assert.equal(writes, 1);
  assert.deepEqual(saved.visibleActivities, []); assert.equal(d.getElementById('profile-nickname').textContent, '<b>New nickname</b>');
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

test('Activities uses saved choices before visiting Account and updates only after a successful save', async () => {
  let saved = { ...settingsFixture, visibleActivities: ['placeholder-1', 'placeholder-3'] };
  const mock = (path, options) => {
    if (path !== '/api/account') return null;
    if (options.method === 'PUT') saved = { ...saved, ...JSON.parse(options.body), revision: saved.revision + 1 };
    return reply(saved);
  };
  const dom = setup(mock, 'https://ab26.englishladder.com/#activities/placeholder-3'); await flush();
  const d = dom.window.document;
  const labels = () => [...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent);
  assert.deepEqual(labels(), ['Activity 1', 'Activity 3']);
  assert.equal(d.getElementById('activity-title').textContent, 'Activity 3');
  assert.match(d.getElementById('activity-message').textContent, /sample activity/);
  dom.window.location.hash = 'account'; await flush();
  for (const input of d.querySelectorAll('#activity-options input')) input.checked = input.value === 'placeholder-2';
  assert.deepEqual(labels(), ['Activity 1', 'Activity 3']);
  submitForm(dom, 'settings-form'); await flush(); assert.deepEqual(labels(), ['Activity 2']);
  dom.window.location.hash = 'activities/placeholder-1'; await flush();
  assert.equal(d.getElementById('activity-title').textContent, 'Activities');
  assert.match(d.getElementById('activity-message').textContent, /not selected/);
  dom.window.location.hash = 'account'; await flush();
  for (const input of d.querySelectorAll('#activity-options input')) input.checked = false;
  submitForm(dom, 'settings-form'); await flush();
  assert.equal(d.querySelectorAll('#activities-submenu a[href^="#activities/"]').length, 0);
  assert.match(d.getElementById('activities-submenu').textContent, /No activities selected/);
  assert.equal(d.querySelector('#activities-submenu a').hash, '#account'); dom.window.close();
  const preview = setup(mock, 'https://ab26.englishladder.com/#overview', 'teacher'); await flush();
  assert.match(preview.window.document.getElementById('activities-submenu').textContent, /No activities selected/); preview.window.close();
});
test('a delayed activity read cannot replace a newer saved choice or restore choices after sign-out', async () => {
  let complete, reads = 0;
  const dom = setup((path, options) => {
    if (path !== '/api/account') return null;
    if (options.method === 'PUT') return reply({ ...settingsFixture, ...JSON.parse(options.body), revision: 2 });
    if (++reads === 1) return new Promise(resolve => { complete = resolve; });
    return reply(settingsFixture);
  }, 'https://ab26.englishladder.com/#account'); await flush(); const d = dom.window.document;
  for (const input of d.querySelectorAll('#activity-options input')) input.checked = input.value === 'placeholder-2';
  submitForm(dom, 'settings-form'); await flush(); complete(reply(settingsFixture)); await flush();
  assert.deepEqual([...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent), ['Activity 2']);
  d.getElementById('logout').click(); await flush(); assert.equal(d.getElementById('activities-submenu').textContent, ''); dom.window.close();
  let late;
  const signedOut = setup(path => path === '/api/account' ? new Promise(resolve => { late = resolve; }) : null, 'https://ab26.englishladder.com/#overview'); await flush();
  signedOut.window.document.getElementById('logout').click(); await flush(); late(reply(settingsFixture)); await flush();
  assert.equal(signedOut.window.document.getElementById('activities-submenu').textContent, ''); signedOut.window.close();
});
test('failed activity loading never substitutes defaults and can retry; expiry clears activities', async () => {
  let unavailable = true;
  const dom = setup(path => path === '/api/account' ? unavailable ? new Response(JSON.stringify({ error: 'Unavailable' }), { status: 503 }) : reply({ ...settingsFixture, visibleActivities: ['placeholder-3'] }) : null, 'https://ab26.englishladder.com/#overview');
  await flush(); const d = dom.window.document;
  assert.equal(d.querySelectorAll('#activities-submenu a').length, 0); assert.match(d.getElementById('activities-submenu').textContent, /could not be loaded/);
  unavailable = false; d.querySelector('#activities-submenu button').click(); await flush();
  assert.deepEqual([...d.querySelectorAll('#activities-submenu a')].map(a => a.textContent), ['Activity 3']); dom.window.close();
  const expired = setup(path => path === '/api/account' ? new Response(JSON.stringify({ error: 'Please sign in.' }), { status: 401 }) : null, 'https://ab26.englishladder.com/#overview');
  await flush(); assert.equal(expired.window.document.getElementById('login-view').hidden, false); assert.equal(expired.window.document.getElementById('activities-submenu').textContent, ''); expired.window.close();
});
