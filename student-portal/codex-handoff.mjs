// Operator-only handoff: Codex reads Zoom directly and sends reviewed results.
// No inference, raw transcript response, account administration, or login access.
import { readTranscript, sessionId } from './server-quiz-model.mjs';
import { validateFeedback } from './feedback.mjs';
import { validateAssessment, assessmentReferences } from './assessment.mjs';
const enc = new TextEncoder();
const json = (data, status = 200) => Response.json(data, { status });
export const canonical = value => JSON.stringify(sort(value));
function sort(value) {
  if (Array.isArray(value)) return value.map(sort);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(k => [k, sort(value[k])]));
  return value;
}
export const digest = async value => [...new Uint8Array(await crypto.subtle.digest('SHA-256', enc.encode(canonical(value))))].map(x => x.toString(16).padStart(2, '0')).join('');
export async function codexAuthorized(request, env) {
  const token = request.headers.get('Authorization')?.replace(/^Bearer /, '');
  if (env.LESSON_PROCESSOR !== 'codex' || !/^[a-f0-9]{64}$/.test(env.CODEX_HANDOFF_SECRET || '') ||
      !/^[a-f0-9]{64}$/.test(token || '') || request.headers.has('Origin') || request.headers.has('Sec-Fetch-Site')) return false;
  const key = await crypto.subtle.importKey('raw', enc.encode(env.CODEX_HANDOFF_SECRET), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
  const expected = await crypto.subtle.sign('HMAC', key, enc.encode(env.CODEX_HANDOFF_SECRET));
  return crypto.subtle.verify('HMAC', key, expected, enc.encode(token));
}
async function prepared(c, id) {
  if (!/^[a-f0-9]{64}$/.test(id || '')) throw new Error('invalid_job');
  const key = 'job:' + id, job = await c.storage.get(key);
  if (!job || ['ignored', 'skipped'].includes(job.status)) throw new Error('job_unavailable');
  const students = await c.students();
  if (job.studentId && !students[job.studentId]) throw new Error('student_changed');
  let context = job.studentId ? await c.portal(job.studentId, '/automation/context') : null;
  const known = context?.sourceNotes.find(s => s.noteId === job.noteId);
  if (known && context.publishedSessions.includes(known.id)) {
    await c.saveJob(key, { ...job, status: 'published', sessionId: known.id, lastError: null, modelIssue: null, modelStage: null, phase: null, recoveryAt: null });
    return { duplicate: true, studentId: job.studentId, sessionId: known.id };
  }
  const note = await c.zoom('/my_notes/notes/' + encodeURIComponent(job.noteId) + '/content?include=transcript');
  const transcript = readTranscript(note, students);
  if (job.studentId && job.studentId !== transcript.studentId) throw new Error('student_changed');
  if (!job.meetingId) throw new Error('meeting_reference_missing');
  const uuid = job.meetingId.startsWith('/') || job.meetingId.includes('//') ? encodeURIComponent(encodeURIComponent(job.meetingId)) : encodeURIComponent(job.meetingId);
  const meeting = await c.zoom('/past_meetings/' + uuid);
  const start = Date.parse(meeting.start_time), end = Date.parse(meeting.end_time);
  if (!Number.isFinite(start) || !Number.isFinite(end) || end <= start || end > Date.now() - 900000 ||
      Date.parse(job.modifiedAt) > Date.now() - 900000 || job.sourceEventAt > Date.now() - 900000) throw new Error('meeting_pending');
  if (start < Date.parse(transcript.student.startAfter)) {
    await c.saveJob(key, { ...job, status: 'skipped', lastError: null });
    return { skipped: true };
  }
  context ||= await c.portal(transcript.studentId, '/automation/context');
  const sid = sessionId(meeting.start_time, transcript.student.timeZone);
  if (context.publishedSessions.includes(sid)) throw new Error('source_changed');
  const { segments } = transcript;
  const source = { noteId: job.noteId, sourceHash: await digest(note.transcript), segmentCount: segments.length,
    coverageStart: segments[0].at, coverageEnd: segments.reduce((m,s) => s.end > m ? s.end : m, ''),
    timestamps: [...new Set(segments.map(s => s.at))] };
  const learnerIds = note.transcript.speakers.filter(s => transcript.student.zoomNames.some(n => n.toLowerCase() === s.display_name.toLowerCase())).map(s => s.speaker_id);
  const instructorNames = JSON.parse(c.env.ZOOM_INSTRUCTOR_NAMES || '["Phil","Phil Stilwell"]');
  const instructorIds = note.transcript.speakers.filter(s => instructorNames.some(n => n.toLowerCase() === s.display_name.toLowerCase())).map(s => s.speaker_id);
  const snapshot = { sourceHash: source.sourceHash, student: transcript.student, priorAssessment: context.assessment,
    attempts: context.attempts, meeting: { start_time: meeting.start_time, end_time: meeting.end_time } };
  const nextJob = { ...job, studentId: transcript.studentId, sessionId: sid, startedAt: meeting.start_time };
  await c.checkSource(key, job);
  if (canonical((await c.students())[transcript.studentId]) !== canonical(transcript.student)) throw new Error('student_changed');
  await c.saveJob(key, nextJob);
  return { id, studentId: transcript.studentId, student: { firstName: transcript.student.firstName, timeZone: transcript.student.timeZone },
    sessionId: sid, meeting: snapshot.meeting, source, speakerRoles: { learnerIds, instructorIds },
    snapshotHash: await digest(snapshot), context: { assessment: context.assessment, attempts: context.attempts },
    _job: nextJob, _student: transcript.student };
}
function validateOutput(input, p) {
  const records = input.records;
  if (input.review?.approved !== true || input.review?.fullTranscript !== true || input.review?.independent !== true ||
      !Array.isArray(records?.feedback) || records.feedback.length !== 1 || !Array.isArray(records.quizzes) || records.quizzes.length !== 1) throw new Error('content_review_failed');
  const f = validateFeedback(records.feedback[0], p.sessionId), a = validateAssessment(records.assessment);
  const q = validateAssessment({ ...a, quiz: records.quizzes[0].quiz }).quiz;
  if (f.source.noteId !== p.source.noteId || f.source.segmentCount !== p.source.segmentCount ||
      f.source.coverageStart !== p.source.coverageStart || f.source.coverageEnd !== p.source.coverageEnd ||
      Date.parse(f.startedAt) !== Date.parse(p.meeting.start_time) || f.timeZone !== p.student.timeZone ||
      q?.questions.length !== 7 || q.generatedForSession !== p.sessionId || canonical(q) !== canonical(a.quiz) || a.plan.some(x => !x.aiPrompt)) throw new Error('invalid_evidence');
  const times = new Set(p.source.timestamps);
  const priorRefs = new Set((p.context.assessment ? assessmentReferences(p.context.assessment) : []).map(r => r.sessionId + ':' + r.at));
  const validRef = r => r.sessionId === p.sessionId ? times.has(r.at) : priorRefs.has(r.sessionId + ':' + r.at);
  if ([...f.strengths, ...f.focus, ...f.vocabulary].some(x => !times.has(x.at)) || !assessmentReferences(a).some(r => r.sessionId === p.sessionId) || assessmentReferences(a).some(r => !validRef(r))) throw new Error('invalid_evidence');
  const evidence = records.quizzes[0].evidence;
  if (!Array.isArray(evidence) || evidence.length !== 7 || evidence.some((e,i) => e.questionIndex !== i || !e.references?.length || e.references.some(r => !validRef(r))) ||
      evidence.filter(e => e.references.some(r => r.sessionId === p.sessionId)).length < 4) throw new Error('invalid_evidence');
  if (/https?:\/\/|mynotes\.zoom|<\/?[a-z]|\bCEFR\b|\b[ABC][12]\b/i.test(JSON.stringify({ f, a }))) throw new Error('unsafe_content');
  return { feedback: [f], assessment: a, quizzes: [{ quiz: q, evidence }], priorAssessment: p.context.assessment };
}
export async function codexHandoff(c, action, input) {
  if (c.env.LESSON_PROCESSOR !== 'codex' || c.env.AUTOMATION_ENABLED === 'true') return json({ error: 'codex_not_enabled' }, 409);
  const lease = crypto.randomUUID();
  const locked = await c.storage.transaction(async txn => {
    if ((await txn.get('run-lock'))?.until > Date.now()) return false;
    await txn.put({ 'run-lock': { lease, until: Date.now() + 900000 } }); return true;
  });
  if (!locked) return json({ error: 'busy' }, 409);
  try {
    // Cancel the obsolete one-time AI alarm as part of the explicit migration.
    const recovery = await c.storage.get('recovery-once');
    if (recovery?.status === 'queued') {
      await c.storage.deleteAlarm();
      await c.storage.put({ 'recovery-once': { ...recovery, status: 'cancelled', reason: 'codex_migration' } });
      const key = 'job:' + recovery.id, job = await c.storage.get(key);
      if (job) await c.saveJob(key, { ...job, recoveryAt: null, nextAt: 0, ...(job.lastError === 'recovery_scheduled' ? { lastError: null } : {}) });
    }
    if (action === 'discover') {
      await c.pruneTranscripts(); await c.storage.put({ 'retention-error': null });
      if (Object.keys(await c.students()).length) {
        await c.accessToken(); await c.refreshDirectory(); await c.discover();
      }
      await c.storage.put({ 'last-check': new Date().toISOString(), 'connection-error': null, 'last-codex-check': new Date().toISOString() });
    }
    if (['discover', 'queue'].includes(action)) {
      const jobs = [...await c.storage.list({ prefix: 'job:' })];
      return json({ processor: 'codex', serverAI: false, jobs: jobs.filter(([,j]) => ['pending','needs_attention'].includes(j.status)).map(([k,j]) => ({ id: k.slice(4), noteId: j.noteId, status: j.status, startedAt: j.startedAt || null, error: j.lastError || null })) });
    }
    if (!['prepare','publish'].includes(action)) return json({ error: 'not_found' }, 404);
    const p = await prepared(c, input.id);
    if (p.duplicate || p.skipped) return json(p);
    if (action === 'prepare') { const { _job, _student, ...result } = p; return json(result); }
    if (input.snapshotHash !== p.snapshotHash) return json({ error: 'source_or_history_changed' }, 409);
    if (input.review?.recordsHash !== await digest(input.records)) return json({ error: 'reviewed_content_changed' }, 409);
    const output = validateOutput(input, p);
    await c.checkSource('job:' + input.id, p._job);
    if (canonical((await c.students())[p.studentId]) !== canonical(p._student)) throw new Error('student_changed');
    const saved = await c.portal(p.studentId, '/learning-import', output);
    const after = await c.portal(p.studentId, '/automation/context');
    if (!after.publishedSessions.includes(p.sessionId)) throw new Error('publish_failed');
    const check = await c.portal(p.studentId, '/' + p.sessionId);
    if (canonical(check) !== canonical(output.feedback[0])) throw new Error('publish_failed');
    if (saved.currentUpdated && canonical(after.assessment) !== canonical(output.assessment)) throw new Error('publish_failed');
    for (const before of p.context.attempts) {
      const now = after.attempts.find(a => a.id === before.id);
      if (!now || before.answers.some((answers,i) => answers.some((v,j) => now.answers[i]?.[j] !== v))) throw new Error('publish_failed');
    }
    await c.saveJob('job:' + input.id, { ...p._job, status: 'published', publishedAt: new Date().toISOString(), publisher: 'codex',
      lastError: null, modelIssue: null, modelStage: null, phase: null, recoveryAt: null });
    return json({ ok: true, verified: true, sessionId: p.sessionId, questions: 7, preservedAttempts: p.context.attempts.length });
  } catch (error) {
    const allowed = ['invalid_job','job_unavailable','student_changed','other_student','ambiguous_student','meeting_reference_missing','meeting_pending','source_changed','transcript_unusable','transcript_too_large','invalid_evidence','content_review_failed','unsafe_content','publish_failed','zoom_reconnect','zoom_unavailable','discovery_incomplete'];
    const code = allowed.includes(error.message) ? error.message : 'handoff_failed';
    if (['prepare','publish'].includes(action) && /^[a-f0-9]{64}$/.test(input.id || '')) {
      const key = 'job:' + input.id, job = await c.storage.get(key);
      if (job && !['ignored','published','skipped'].includes(job.status)) await c.saveJob(key, { ...job, lastError: code === 'other_student' ? 'student_not_matched' : code,
        status: ['other_student','ambiguous_student','meeting_reference_missing'].includes(code) ? 'needs_attention' : 'pending' });
    }
    return json({ error: code }, 409);
  } finally {
    await c.storage.transaction(async txn => { if ((await txn.get('run-lock'))?.lease === lease) await txn.delete('run-lock'); });
  }
}
