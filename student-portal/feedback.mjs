import { validateAssessment, assessmentReferences } from './assessment.mjs';
import { handleQuiz } from './quiz-results.mjs';

export const FEEDBACK_ID = /^\d{4}-\d{2}-\d{2}-\d{4}$/;

function text(value, max = 1500) {
  if (typeof value !== 'string' || !value.trim() || value.length > max) throw new Error('Invalid text');
  return value.trim();
}
function items(value, convert, max = 12) {
  if (!Array.isArray(value) || !value.length || value.length > max) throw new Error('Invalid list');
  return value.map(convert);
}
function offset(value) {
  if (typeof value !== 'string' || !/^\d{2}:[0-5]\d:[0-5]\d$/.test(value)) throw new Error('Invalid transcript offset');
  return value;
}

// Whitelist fields: never persist a transcript, credential, or arbitrary profile field.
// The scope is a publishing contract; the author must also review the language-only content.
export function validateFeedback(value, id) {
  if (!value || value.id !== id || !FEEDBACK_ID.test(id) || value.scope !== 'esl') throw new Error('Invalid feedback');
  if (typeof value.startedAt !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/.test(value.startedAt) || !Number.isFinite(Date.parse(value.startedAt))) throw new Error('Invalid session date');
  const timeZone = text(value.timeZone, 64);
  const dateParts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date(value.startedAt)).map(p => [p.type, p.value]));
  if (id !== `${dateParts.year}-${dateParts.month}-${dateParts.day}-${dateParts.hour}${dateParts.minute}`) throw new Error('Date and ID differ');
  const source = value.source;
  if (!source || source.reviewedFullTranscript !== true || !Number.isInteger(source.segmentCount) || source.segmentCount < 1 || source.segmentCount > 100000 || !/^[\w-]{10,80}$/.test(source.noteId)) throw new Error('A full transcript is required');
  const coverageStart = offset(source.coverageStart);
  const coverageEnd = offset(source.coverageEnd);
  if (coverageEnd <= coverageStart) throw new Error('Invalid coverage');
  const at = stamp => { const result = offset(stamp); if (result < coverageStart || result > coverageEnd) throw new Error('Evidence outside transcript'); return result; };
  return {
    id, scope: 'esl', startedAt: value.startedAt, timeZone,
    title: text(value.title, 120), summary: text(value.summary), nextStep: text(value.nextStep),
    strengths: items(value.strengths, s => ({ title: text(s.title, 120), detail: text(s.detail), at: at(s.at) })),
    focus: items(value.focus, f => {
      if (!['teacher-feedback', 'practice-extension'].includes(f.kind)) throw new Error('Invalid evidence type');
      return { title: text(f.title, 120), kind: f.kind, at: at(f.at), observed: text(f.observed), model: text(f.model), explanation: text(f.explanation) };
    }),
    vocabulary: items(value.vocabulary, v => ({ term: text(v.term, 120), meaning: text(v.meaning), example: text(v.example), at: at(v.at) })),
    practice: items(value.practice, p => ({ prompt: text(p.prompt), answer: text(p.answer) })),
    source: { noteId: source.noteId, coverageStart, coverageEnd, segmentCount: source.segmentCount, reviewedFullTranscript: true },
  };
}

const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json' } });

// One private SQLite-backed Durable Object per student. Only the authenticated
// outer Worker can reach this class; no public URL or client-selected student ID.
export class FeedbackStore {
  constructor(state) { this.storage = state.storage; }
  async fetch(request) {
    const url = new URL(request.url);
    const id = url.pathname.slice(1);
    // Internal-only routes: the public Worker never forwards arbitrary paths here.
    if (id === 'automation/context' && request.method === 'GET') {
      const attempts = [], publishedSessions = [], sourceNotes = [];
      for (const [prefix, target] of [['quiz:attempt:', attempts], ['quiz:published:', publishedSessions], ['feedback:', sourceNotes]]) {
        let end;
        while (true) {
          const page = [...await this.storage.list({ prefix, reverse: true, limit: 100, ...(end ? { end } : {}) })];
          target.push(...page.map(([key, value]) => prefix === 'quiz:published:' ? key.slice(prefix.length) : prefix === 'feedback:' ? { noteId: value.source.noteId, id: value.id, startedAt: value.startedAt } : value));
          if (page.length < 100) break;
          end = page.at(-1)[0];
        }
      }
      return json({ assessment: await this.storage.get('assessment:current') || null, attempts, publishedSessions, sourceNotes });
    }
    if (id === 'automation/publish' && request.method === 'POST') {
      const input = await request.json();
      return this.storage.transaction(async txn => {
        const sessionId = input.quiz?.generatedForSession;
        if (!FEEDBACK_ID.test(sessionId || '') || !Array.isArray(input.quiz?.sourceSessions) || !Array.isArray(input.quiz?.patternTitles)) return json({ error: 'Invalid session.' }, 400);
        const current = await txn.get('assessment:current') || null;
        if (await txn.get('quiz:published:' + sessionId) || current?.quiz?.generatedForSession === sessionId) return json({ ok: true, duplicate: true });
        if (JSON.stringify(input.priorAssessment) !== JSON.stringify(current)) return json({ error: 'Assessment changed. Retry with the latest record.' }, 409);
        let record, feedback;
        try {
          feedback = validateFeedback(input.feedback, sessionId);
          record = validateAssessment({ ...input.assessment, quiz: input.quiz });
          if (!record.sourceSessions.includes(sessionId)) throw new Error('Missing latest session');
        } catch { return json({ error: 'Invalid learning record.' }, 400); }
        for (const sourceId of new Set([...record.sourceSessions, ...record.quiz.sourceSessions])) {
          if (sourceId !== sessionId && !(await txn.get('feedback:' + sourceId))?.source?.reviewedFullTranscript) return json({ error: 'Source unavailable.' }, 400);
        }
        for (const ref of assessmentReferences(record)) {
          const source = ref.sessionId === sessionId ? feedback.source : (await txn.get('feedback:' + ref.sessionId)).source;
          if (ref.at < source.coverageStart || ref.at > source.coverageEnd) return json({ error: 'Invalid assessment evidence.' }, 400);
        }
        const existing = await txn.get('feedback:' + sessionId);
        const savedFeedback = existing || feedback;
        const { title, summary, startedAt, timeZone } = savedFeedback;
        const update = {
          ['feedback:' + sessionId]: savedFeedback, ['index:' + sessionId]: { id: sessionId, title, summary, startedAt, timeZone },
          ['assessment:before:' + sessionId]: current,
          ['quiz:published:' + sessionId]: { quiz: record.quiz, assessment: record, evidence: input.evidence, fingerprint: input.fingerprint, publishedAt: new Date().toISOString() },
        };
        // An older delayed event is archived without replacing a newer lesson quiz.
        if (!current?.quiz?.generatedForSession || sessionId > current.quiz.generatedForSession) update['assessment:current'] = record;
        await txn.put(update);
        return json({ ok: true });
      });
    }
    if (id.startsWith('quiz/')) return handleQuiz(this.storage, request);
    if (id === 'assessment') {
      if (request.method === 'GET') return json({ assessment: await this.storage.get('assessment:current') || null });
      if (request.method !== 'PUT') return json({ error: 'Method not allowed.' }, 405);
      let record;
      try { record = validateAssessment(await request.json()); }
      catch { return json({ error: 'Please check the assessment format and session references.' }, 400); }
      const sourceIds = [...new Set([...record.sourceSessions, ...(record.quiz?.sourceSessions || [])])];
      const sources = new Map(await Promise.all(sourceIds.map(async sessionId => [sessionId, await this.storage.get(`feedback:${sessionId}`)])));
      if ([...sources.values()].some(source => !source?.source?.reviewedFullTranscript) || assessmentReferences(record).some(ref => {
        const coverage = sources.get(ref.sessionId).source;
        return ref.at < coverage.coverageStart || ref.at > coverage.coverageEnd;
      })) return json({ error: 'Assessment evidence must refer to this student’s available session transcripts.' }, 400);
      await this.storage.put({ 'assessment:current': record });
      return json({ ok: true });
    }
    if (request.method === 'GET' && !id) {
      const before = url.searchParams.get('before');
      if (before && !FEEDBACK_ID.test(before)) return json({ error: 'Invalid page.' }, 400);
      const rows = await this.storage.list({ prefix: 'index:', reverse: true, limit: 101, ...(before ? { end: `index:${before}` } : {}) });
      const all = [...rows.values()];
      const sessions = all.slice(0, 100);
      return json({ sessions, nextCursor: all.length > 100 ? sessions.at(-1).id : null });
    }
    if (!FEEDBACK_ID.test(id)) return json({ error: 'Session not found.' }, 404);
    if (request.method === 'GET') {
      const record = await this.storage.get(`feedback:${id}`);
      return record ? json(record) : json({ error: 'Session not found.' }, 404);
    }
    if (request.method === 'PUT') {
      let record;
      try { record = validateFeedback(await request.json(), id); }
      catch { return json({ error: 'Please check the feedback format and transcript references.' }, 400); }
      const { title, summary, startedAt, timeZone } = record;
      // A multi-key put commits both values atomically, including replacements.
      await this.storage.put({ [`feedback:${id}`]: record, [`index:${id}`]: { id, title, summary, startedAt, timeZone } });
      return json({ ok: true, id });
    }
    return json({ error: 'Method not allowed.' }, 405);
  }
}
