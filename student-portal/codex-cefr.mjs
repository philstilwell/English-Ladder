// GPT in Codex authors and independently reviews estimates. This service only
// verifies eligibility, sources and evidence; it has no AI calls or transcript writes.
import { readTranscript, sessionId } from './server-quiz-model.mjs';
import { prepareAnonymousTranscript } from './transcript-privacy.mjs';
import { groundCefrWindow } from './cefr.mjs';
import { transcriptHash } from './transcript-cache.mjs';
const json = (value, status = 200) => Response.json(value, { status });
const validStudent = id => typeof id === 'string' && /^[a-z0-9-]{2,40}$/.test(id);
const validAttempt = id => typeof id === 'string' && /^[a-f0-9-]{36}$/.test(id);
const day = () => new Date().toISOString().slice(0, 10);

async function contextFor(c, studentId) {
  const student = (await c.students())[studentId];
  if (!validStudent(studentId) || !student) throw Error('student_changed');
  return { student, context: await c.portal(studentId, '/automation/codex-cefr-context') };
}
async function fullSources(c, studentId, student, context, helpers) {
  const { digest, canonical } = helpers, sources = [], sessions = [], hashes = new Set();
  if (context.references.length < 2 || context.references.length > 4) throw Error('cefr_source_unavailable');
  const instructorNames = JSON.parse(c.env.ZOOM_INSTRUCTOR_NAMES || '["Phil","Phil Stilwell"]');
  for (const ref of context.references) {
    const sourceJob = await c.storage.get('job:' + await transcriptHash(ref.noteId));
    if (sourceJob && (['ignored','skipped'].includes(sourceJob.status) || sourceJob.studentId && sourceJob.studentId !== studentId)) throw Error('cefr_source_unavailable');
    // A published lesson keeps its original local date even if the account moves.
    if (!ref.timeZone || sessionId(ref.startedAt, ref.timeZone) !== ref.sessionId) throw Error('cefr_source_changed');
    const note = await c.zoom('/my_notes/notes/' + encodeURIComponent(ref.noteId) + '/content?include=transcript');
    // Codex reads complete sources in chunks; it does not submit one model payload.
    // Keep a per-source memory bound, independent of the disabled server AI limit.
    const transcript = readTranscript(note, await c.students(), { maxChars: 1000000 });
    if (transcript.studentId !== studentId) throw Error('student_changed');
    const sourceHash = await digest(note.transcript);
    if (hashes.has(sourceHash)) throw Error('cefr_duplicate_sources');
    hashes.add(sourceHash);
    const { segments } = prepareAnonymousTranscript(note, transcript, instructorNames);
    const learnerIds = note.transcript.speakers.filter(s => student.zoomNames.some(n => n.toLowerCase() === s.display_name.toLowerCase())).map(s => s.speaker_id);
    const instructorIds = note.transcript.speakers.filter(s => instructorNames.some(n => n.toLowerCase() === s.display_name.toLowerCase())).map(s => s.speaker_id);
    sources.push({ ...ref, sourceHash, segmentCount: segments.length, coverageStart: segments[0].at,
      coverageEnd: segments.reduce((m, s) => s.end > m ? s.end : m, ''), speakerRoles: { learnerIds, instructorIds } });
    sessions.push({ sessionId: ref.sessionId, segments });
  }
  if (canonical((await c.students())[studentId]) !== canonical(student)) throw Error('student_changed');
  const fresh = await c.portal(studentId, '/automation/codex-cefr-context');
  if (!fresh.due || fresh.windowHash !== context.windowHash) throw Error('cefr_source_changed');
  return { sources, sessions, snapshotHash: await digest({ student, instructorNames, windowHash: context.windowHash, sources }) };
}

async function reserveRecovery(c, studentId, context, recovery) {
  // Only an explicit operator-supplied approval for this exact failed attempt.
  // Ordinary scheduled prepares never create approvals or reset counters.
  await c.storage.transaction(async txn => {
    const attempt = await txn.get('codex-cefr-attempt:' + studentId);
    const error = await txn.get('cefr-error:' + studentId);
    const usage = await txn.get('cefr-usage:' + studentId);
    const usedKey = 'cefr-recovery-used:' + recovery?.attemptId;
    if (recovery?.approved !== true || recovery.studentId !== studentId || recovery.day !== day() ||
        !validAttempt(recovery.attemptId) || attempt?.attemptId !== recovery.attemptId || attempt.day !== day() ||
        !['preparing','failed'].includes(attempt.status) || recovery.windowHash !== context.windowHash || attempt.windowHash !== context.windowHash ||
        !['cefr_window_too_large','transcript_too_large','cefr_source_changed','other_student'].includes(error) ||
        usage?.day !== day() || usage.daily !== 1 || usage.month !== day().slice(0, 7) || usage.monthly >= 2 ||
        await txn.get(usedKey)) throw Error('cefr_limit');
    await txn.put({ [usedKey]: { studentId, day: day(), windowHash: context.windowHash },
      ['cefr-usage:' + studentId]: { ...usage, daily: usage.daily + 1, monthly: usage.monthly + 1 } });
  });
}

export async function codexCefr(c, action, input, helpers) {
  if (c.env.CEFR_PROCESSOR !== 'codex' || c.env.AUTOMATION_ENABLED === 'true' || c.env.AI) return json({ error: 'codex_cefr_not_enabled' }, 409);
  const { digest } = helpers;
  let reservedAttemptId;
  try {
    if (action === 'cefr-queue') {
      const students = [];
      for (const [studentId, student] of Object.entries(await c.students())) {
        const context = await c.portal(studentId, '/automation/codex-cefr-context');
        const usage = await c.storage.get('cefr-usage:' + studentId);
        const limited = usage?.day === day() && usage.daily >= 1 || usage?.month === day().slice(0, 7) && usage.monthly >= 2;
        students.push({ studentId, firstName: student.firstName, due: context.due, initial: context.initial,
          availableSessions: context.availableSessions, selectedSessions: context.references.length, nextReviewOn: context.nextReviewOn,
          lastReviewOn: context.review?.completedOn || null, deferred: Boolean(context.due && limited), error: await c.storage.get('cefr-error:' + studentId) || null });
      }
      return json({ processor: 'codex', serverAI: false, additionalAiCost: 0, students });
    }
    const { student, context } = await contextFor(c, input.studentId);
    const key = 'codex-cefr-attempt:' + input.studentId;
    if (action === 'cefr-inspect') return json({ studentId: input.studentId, student, context,
      attempt: await c.storage.get(key) || null, usage: await c.storage.get('cefr-usage:' + input.studentId) || null,
      error: await c.storage.get('cefr-error:' + input.studentId) || null });
    if (action === 'cefr-verify' || action === 'cefr-publish') {
      if (!validAttempt(input.attemptId)) throw Error('invalid_cefr_review');
      const { receipt } = await c.portal(input.studentId, '/automation/codex-cefr-receipt/' + input.attemptId);
      if (receipt) {
        if (action === 'cefr-publish' && (receipt.recordsHash !== await digest(input.cefr) || receipt.snapshotHash !== input.snapshotHash)) throw Error('cefr_review_failed');
        return json(receipt);
      }
      if (action === 'cefr-verify') return json({ verified: false, attemptId: input.attemptId });
    }
    if (!context.due) return json({ due: false, nextReviewOn: context.nextReviewOn, availableSessions: context.availableSessions });
    if (action === 'cefr-prepare') {
      if (input.recovery) await reserveRecovery(c, input.studentId, context, input.recovery);
      else await c.reserveGeneration(input.studentId, 'cefr'); // Durable bounds include failed attempts.
      const attemptId = crypto.randomUUID();
      reservedAttemptId = attemptId;
      await c.storage.put({ [key]: { attemptId, day: day(), status: 'preparing', windowHash: context.windowHash } });
      const prepared = await fullSources(c, input.studentId, student, context, helpers);
      await c.storage.put({ [key]: { attemptId, day: day(), status: 'prepared', windowHash: context.windowHash, snapshotHash: prepared.snapshotHash, publicationAttempts: 0 } });
      return json({ studentId: input.studentId, attemptId, snapshotHash: prepared.snapshotHash, initial: context.initial,
        assessedOn: context.today, sources: prepared.sources });
    }
    if (action !== 'cefr-publish') return json({ error: 'not_found' }, 404);
    const attempt = await c.storage.get(key);
    if (!attempt || attempt.attemptId !== input.attemptId || attempt.day !== day() || attempt.status !== 'prepared' ||
        attempt.snapshotHash !== input.snapshotHash || attempt.windowHash !== context.windowHash || attempt.publicationAttempts >= 2) throw Error('invalid_cefr_review');
    await c.storage.put({ [key]: { ...attempt, publicationAttempts: attempt.publicationAttempts + 1 } });
    if (input.review?.approved !== true || input.review?.fullTranscript !== true || input.review?.independent !== true ||
        input.review?.snapshotHash !== input.snapshotHash || input.review?.recordsHash !== await digest(input.cefr)) throw Error('cefr_review_failed');
    const prepared = await fullSources(c, input.studentId, student, context, helpers);
    if (prepared.snapshotHash !== input.snapshotHash) throw Error('cefr_source_changed');
    const cefr = groundCefrWindow(input.cefr, prepared.sessions, context.today);
    const receipt = await c.portal(input.studentId, '/automation/codex-cefr-publish', {
      attemptId: input.attemptId, windowHash: context.windowHash, snapshotHash: input.snapshotHash, recordsHash: await digest(input.cefr), cefr });
    await c.storage.put({ [key]: { ...attempt, status: 'published' } });
    await c.storage.delete('cefr-error:' + input.studentId);
    return json(receipt);
  } catch (error) {
    const allowed = ['student_changed','cefr_source_unavailable','cefr_source_changed','cefr_duplicate_sources','cefr_window_too_large',
      'cefr_limit','cefr_review_failed','invalid_cefr_review','transcript_unusable','transcript_too_large','other_student','ambiguous_student','zoom_reconnect','zoom_unavailable'];
    const code = allowed.includes(error.message) ? error.message : 'cefr_review_failed';
    if (reservedAttemptId) {
      const key = 'codex-cefr-attempt:' + input.studentId, attempt = await c.storage.get(key);
      if (attempt?.attemptId === reservedAttemptId) await c.storage.put({ [key]: { ...attempt, status: 'failed' } });
    }
    if (validStudent(input.studentId) && (reservedAttemptId || action === 'cefr-publish')) await c.storage.put({ ['cefr-error:' + input.studentId]: code });
    return json({ error: code, deferred: true }, 409);
  }
}
