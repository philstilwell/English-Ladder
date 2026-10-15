import test from 'node:test';
import assert from 'node:assert/strict';
import { validateCefr, groundCefr, cefrOverview, insufficientCefr } from '../cefr.mjs';
import { env, login, call } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';

const exampleCefr = {
  state:'estimated',lower:'B1',upper:'B2',confidence:'moderate',latestSessionId:feedback.id,assessedOn:'2026-10-14',
  rationale:'Connected explanations are clear; complex forms still need support.',
  aspects:['range','accuracy','coherence','interaction'].map(area=>({area,detail:'Some evidence is visible; more independent language is needed.'})),
  evidence:[{sessionId:feedback.id,at:'00:02:00',quote:'I can explain how it works.',note:'An independent explanation.'},
    {sessionId:feedback.id,at:'00:03:00',quote:'Could you explain the last part?',note:'A useful clarification question.'}]
};

test('CEFR estimates require valid adjacent levels, actual dates, four areas and distinct evidence',()=>{
  const result=validateCefr({...exampleCefr,sourceSessions:['invented'],password:'do-not-save'});
  assert.equal(result.confidence,'low');assert.deepEqual(result.sourceSessions,[feedback.id]);assert.equal(result.password,undefined);
  for(const change of [{lower:'B1.7'},{upper:'C2'},{upper:'A2'},{confidence:'high'},{assessedOn:'2026-02-30'},{assessedOn:'2026-09-30'},
    {evidence:[]},{evidence:[exampleCefr.evidence[0],exampleCefr.evidence[0]]},{aspects:exampleCefr.aspects.slice(1)}]) assert.throws(()=>validateCefr({...exampleCefr,...change}));
  const older=exampleCefr.evidence[0];
  const three=validateCefr({...exampleCefr,evidence:[...exampleCefr.evidence,{...older,sessionId:'2026-09-20-1200'},{...older,sessionId:'2026-09-25-1200'}]});
  assert.equal(three.confidence,'moderate');
  assert.doesNotMatch(JSON.stringify(cefrOverview(three)),/quote|rationale|sourceSessions|aspects/);
  assert.deepEqual(cefrOverview(null),{state:'pending'});
  assert.equal(validateCefr({...insufficientCefr(feedback.id,'2026-10-14'),lower:'B1'}).lower,undefined);
});

test('CEFR quotes must be exact learner language, with older quotes verified previously',()=>{
  const segments=exampleCefr.evidence.map(ref=>({at:ref.at,speaker:'Alex',text:ref.quote}));
  assert.equal(groundCefr(exampleCefr,feedback.id,'2026-10-14',segments,'Alex',null).state,'estimated');
  assert.throws(()=>groundCefr(exampleCefr,feedback.id,'2026-10-14',segments,'Teacher',null));
  assert.throws(()=>groundCefr({...exampleCefr,evidence:[{...exampleCefr.evidence[0],quote:'I speak perfect English.'},exampleCefr.evidence[1]]},feedback.id,'2026-10-14',segments,'Alex',null));
  const older={...exampleCefr.evidence[0],sessionId:'2026-09-20-1200'},withPrior={...exampleCefr,evidence:[...exampleCefr.evidence,older]};
  assert.throws(()=>groundCefr(withPrior,feedback.id,'2026-10-14',segments,'Alex',null));
  assert.equal(groundCefr(withPrior,feedback.id,'2026-10-14',segments,'Alex',{evidence:[older]}).sourceSessions.length,2);
});

test('CEFR publishes atomically in separate private storage and is absent from student data',async()=>{
  const e=env(),store=e.FEEDBACK_STORE.get('ab26'),student=await login(e);
  const publish=body=>store.fetch(new Request('https://internal/automation/publish',{method:'POST',body:JSON.stringify(body)}));
  const input={feedback,assessment,quiz:{...quiz,sourceSessions:[feedback.id],generatedForSession:feedback.id,patternTitles:['Verb patterns']},priorAssessment:null,cefr:exampleCefr};
  assert.equal((await publish({...input,cefr:{...exampleCefr,latestSessionId:'2026-09-20-1200'}})).status,400);
  assert.equal(await store.storage.get('assessment:current'),undefined);
  assert.equal((await publish({...input,cefr:{...exampleCefr,evidence:[{...exampleCefr.evidence[0],at:'09:00:00'},exampleCefr.evidence[1]]}})).status,400);
  assert.equal((await publish(input)).status,200);
  const current=await store.storage.get('cefr:current');assert.equal(current.confidence,'low');
  assert.deepEqual(current,await store.storage.get('cefr:history:'+feedback.id));
  const context=await(await store.fetch(new Request('https://internal/automation/context'))).json();assert.deepEqual(context.cefr,current);
  for(const path of ['/api/assessment','/api/feedback','/api/feedback/'+feedback.id,'/api/quiz/state']){
    const result=await call(e,path,{headers:{Cookie:student.cookie}});assert.equal(result.status,200);assert.doesNotMatch(await result.text(),/cefr|CEFR|Connected explanations|B1|B2|independent explanation/);
  }
  assert.equal((await e.FEEDBACK_STORE.get('cd26').fetch(new Request('https://internal/admin/cefr'))).status,200);
  assert.deepEqual(await(await e.FEEDBACK_STORE.get('cd26').fetch(new Request('https://internal/admin/cefr'))).json(),{cefr:null});
  const oldId='2026-09-20-2057',old={...input,feedback:{...feedback,id:oldId,startedAt:'2026-09-21T00:57:01Z'},assessment:{...assessment,sourceSessions:[feedback.id,oldId]},quiz:{...input.quiz,sourceSessions:[feedback.id,oldId],generatedForSession:oldId},priorAssessment:context.assessment,cefr:insufficientCefr(oldId,'2026-10-14')};
  assert.equal((await publish(old)).status,200);assert.deepEqual(await store.storage.get('cefr:current'),current);
  await store.fetch(new Request('https://internal/admin/delete-account',{method:'POST'}));
  assert.equal(await store.storage.get('cefr:current'),undefined);assert.equal(await store.storage.get('cefr:history:'+feedback.id),undefined);
  assert.equal((await publish(input)).status,410);
});
