import test from 'node:test';
import assert from 'node:assert/strict';
import { env, login, call, origin, seedQuiz } from './harness.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';

function input(record = feedback, priorAssessment = null) {
  const q = { ...quiz, patternTitles: ['Use “can”'], sourceSessions: [record.id], generatedForSession: record.id };
  const a = { ...assessment, sourceSessions: [...new Set([feedback.id, record.id])], quiz: q };
  return { feedback: [record], assessment: a, priorAssessment,
    quizzes: [{ quiz: q, evidence: q.questions.map((_,questionIndex) => ({ questionIndex, references: [{ sessionId: record.id, at: '00:03:00' }] })) }] };
}
const post = (e,cookie,body,extra = {}) => call(e,'/api/learning-import',{ method:'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json',...extra},body:JSON.stringify(body) });

test('historical imports require the teacher, same origin and account; source details stay private', async () => {
  const e = env(), teacher = await login(e,'teacher-test'), student = await login(e);
  assert.equal((await post(e,'',input())).status,401);
  assert.equal((await post(e,student.cookie,input())).status,403);
  assert.equal((await post(e,teacher.cookie,input(),{Origin:'https://cd26.englishladder.com'})).status,403);
  assert.equal((await call(e,'/api/learning-import',{method:'POST',headers:{Cookie:teacher.cookie,Origin:'https://cd26.englishladder.com'},body:JSON.stringify(input())},'https://cd26.englishladder.com')).status,401);
  assert.equal((await post(e,teacher.cookie,input())).status,200);
  const visible = await call(e,'/api/feedback/'+feedback.id,{headers:{Cookie:student.cookie}});
  assert.equal(visible.headers.get('Cache-Control'),'no-store');
  assert.doesNotMatch(await visible.text(),/fictional-note-id-only/);
  assert.equal((await call(e,'/api/feedback/learning-import',{headers:{Cookie:student.cookie}})).status,404);
  assert.equal((await call(e,'/api/learning-import',{headers:{Cookie:teacher.cookie}})).status,405);
});

test('imports save all assets atomically, archive quizzes and are idempotent', async () => {
  const e = env(), teacher = await login(e,'teacher-test');
  const body = input();
  const failed = structuredClone(body); failed.quizzes[0].evidence[0].references[0].at = '02:00:00';
  assert.equal((await post(e,teacher.cookie,failed)).status,400);
  assert.equal((await (await call(e,'/api/feedback',{headers:{Cookie:teacher.cookie}})).json()).sessions.length,0);
  assert.deepEqual(await (await post(e,teacher.cookie,body)).json(),{ok:true,sessions:1,quizzes:1,currentUpdated:true});
  assert.deepEqual(await (await post(e,teacher.cookie,body)).json(),{ok:true,duplicate:true});
  const storage = e.FEEDBACK_STORE.get('ab26').storage;
  assert.equal((await storage.get('quiz:published:'+feedback.id)).historicalImport,true);
  assert.equal((await storage.list({prefix:'import:history:',limit:10})).size,1);
  assert.deepEqual(await storage.get('assessment:current'),body.assessment);
  const changed = structuredClone(body); changed.feedback[0].summary = 'An unrelated replacement.'; changed.priorAssessment = body.assessment;
  assert.equal((await post(e,teacher.cookie,changed)).status,409);
  assert.equal((await storage.get('feedback:'+feedback.id)).summary,feedback.summary);
});

test('imports preserve first choices, reject stale assessments and require all references in this account', async () => {
  const { e, teacher, student, state } = await seedQuiz();
  await call(e,'/api/quiz/answer',{method:'POST',headers:{Cookie:student.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({attemptId:crypto.randomUUID(),version:state.version,questionIndex:0,choiceIndex:1})});
  const storage = e.FEEDBACK_STORE.get('ab26').storage;
  const history = [...await storage.list({prefix:'quiz:attempt:',limit:100})];
  assert.equal(history.length,1);
  const current = await storage.get('assessment:current');
  const newer = {...feedback,id:'2026-10-05-2057',startedAt:'2026-10-06T00:57:01Z',source:{...feedback.source,noteId:'another-fictional-note'}};
  const body = input(newer,current);
  assert.equal((await post(e,teacher.cookie,{...body,priorAssessment:null})).status,409);
  const bad = structuredClone(body);bad.assessment.sourceSessions.push('2026-09-01-1200');
  assert.equal((await post(e,teacher.cookie,bad)).status,400);
  assert.equal((await post(e,teacher.cookie,body)).status,200);
  assert.deepEqual([...await storage.list({prefix:'quiz:attempt:',limit:100})],history);
  assert.equal((await storage.list({prefix:'assessment:before:import:',limit:100})).size,1);
});

test('an older historical set cannot replace a newer assigned quiz or assessment', async () => {
  const {e,teacher,publish} = await seedQuiz();
  const newer = {...feedback,id:'2026-10-05-2057',startedAt:'2026-10-06T00:57:01Z',source:{...feedback.source,noteId:'newer-fictional-note'}};
  await publish('/api/feedback/'+newer.id,newer);
  await publish('/api/assessment',input(newer).assessment);
  const current = await e.FEEDBACK_STORE.get('ab26').storage.get('assessment:current');
  const result = await post(e,teacher.cookie,input(feedback,current));
  assert.equal(result.status,200);
  assert.equal((await result.json()).currentUpdated,false);
  assert.deepEqual(await e.FEEDBACK_STORE.get('ab26').storage.get('assessment:current'),current);
});
