export const feedback = {
 id:'2026-10-01-2057', scope:'esl', startedAt:'2026-10-02T00:57:01Z', timeZone:'America/New_York',
 title:'Clear explanations', summary:'Practice useful English patterns.', nextStep:'Make three examples.',
 strengths:[{title:'Follow-up questions',detail:'You asked a clear question.',at:'00:02:00'}],
 focus:[{title:'Verb patterns',kind:'teacher-feedback',at:'00:03:00',observed:'Your teacher modeled the pattern.',model:'I can access the file.',explanation:'Access takes an object directly.'}],
 vocabulary:[{term:'access',meaning:'Open or use something.',example:'I can access the file.',at:'00:03:00'}],
 practice:[{prompt:'Make an example.',answer:'I can access the file.'}],
 source:{noteId:'fictional-note-id-only',coverageStart:'00:01:00',coverageEnd:'01:20:00',segmentCount:100,reviewedFullTranscript:true}
};
export const assessment = {
 scope:'esl', assessedOn:'2026-10-14', sourceSessions:[feedback.id],
 title:'Your overall English assessment', summary:'You ask useful questions and can clarify your meaning.',
 mainPriority:'Make familiar verb patterns more consistent.',
 strengths:[{title:'Useful questions',detail:'You asked for more information.',evidence:[{sessionId:feedback.id,at:'00:02:00'}]}],
 progress:{detail:'You reused a phrase later in the lesson.',evidence:[{sessionId:feedback.id,at:'00:03:00'}]},
 patterns:[{title:'Verb patterns',detail:'Practice the full phrase.',practice:'Change the object.',examples:[{sessionId:feedback.id,at:'00:03:00',observed:'Your teacher modeled the pattern.',model:'I can access the file.'}]}],
 plan:[{title:'Recall familiar patterns',activity:'Use them in new sentences.',target:'Eight of ten sentences without prompting.'}],
 nextLesson:'Review, practice, then explain a new example.'
};
