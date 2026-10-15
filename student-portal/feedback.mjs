import { validateAssessment, assessmentReferences } from './assessment.mjs';
import { handleQuiz, latestQuizStatus } from './quiz-results.mjs';
import { validateCefr, cefrOverview } from './cefr.mjs';

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

function normalizedWords(value) {
  return value.normalize('NFKC').toLowerCase().replace(/[’‘']/gu, '').replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
}

export function validateFeedbackPractice(value, feedback = {}) {
  const practice = items(value, p => ({ prompt: text(p.prompt), answer: text(p.answer) }));
  const models = [...new Set([...(feedback.focus || []).map(f => f.model), ...(feedback.vocabulary || []).map(v => v.example)]
    .flatMap(example => [example, ...example.split(/[.!?]+/u)])
    .map(normalizedWords).filter(example => example.split(' ').length >= 2))];
  for (const exercise of practice) {
    for (const part of [exercise.prompt, exercise.answer]) {
      const words = normalizedWords(part);
      // Short target phrases may recur. Complete examples (including a sentence
      // inside a longer answer) must be new; punctuation changes do not count.
      if (models.some(model => words === model || model.split(' ').length >= 4 && ` ${words} `.includes(` ${model} `))) {
        throw new Error('Practice must use a new example, not repeat a teaching example');
      }
    }
    const tasks = exercise.prompt.replace(/_{2,}|\.{3}|…/gu, ' practicegap ').split(/[.!?;:\n“”"]/u)
      .map(part => ` ${normalizedWords(part)} `).filter(part => part.includes(' practicegap '));
    if (!tasks.length) continue;
    // Catch a copied gap-fill even when its answer contains only the missing word.
    for (const model of models) {
      const words = model.split(' ');
      for (let start = 0; start < words.length; start++) {
        for (let count = 1; count <= Math.min(8, words.length - start, words.length - 3); count++) {
          const gap = ` ${[...words.slice(0, start), 'practicegap', ...words.slice(start + count)].join(' ')} `;
          if (tasks.some(task => task.includes(gap) && (start > 0 || task.startsWith(gap)) &&
              (start + count < words.length || task.endsWith(gap)))) throw new Error('Practice must use a new example, not a gap in a teaching example');
        }
      }
    }
  }
  return practice;
}

export function validatePracticeEdit(value) {
  if (!value || Object.keys(value).some(key => !['practice', 'priorFeedback'].includes(key)) ||
      !value.priorFeedback || typeof value.priorFeedback !== 'object' || Array.isArray(value.priorFeedback)) throw new Error('Invalid practice edit');
  return { practice: validateFeedbackPractice(value.practice), priorFeedback: value.priorFeedback };
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
  const record = {
    id, scope: 'esl', startedAt: value.startedAt, timeZone,
    title: text(value.title, 120), summary: text(value.summary), nextStep: text(value.nextStep),
    strengths: items(value.strengths, s => ({ title: text(s.title, 120), detail: text(s.detail), at: at(s.at) })),
    focus: items(value.focus, f => {
      if (!['teacher-feedback', 'practice-extension'].includes(f.kind)) throw new Error('Invalid evidence type');
      return { title: text(f.title, 120), kind: f.kind, at: at(f.at), observed: text(f.observed), model: text(f.model), explanation: text(f.explanation) };
    }),
    vocabulary: items(value.vocabulary, v => ({ term: text(v.term, 120), meaning: text(v.meaning), example: text(v.example), at: at(v.at) })),
    source: { noteId: source.noteId, coverageStart, coverageEnd, segmentCount: source.segmentCount, reviewedFullTranscript: true },
  };
  record.practice = validateFeedbackPractice(value.practice, record);
  return record;
}

const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json' } });

// One private SQLite-backed Durable Object per student. Only the authenticated
// outer Worker can reach this class; no public URL or client-selected student ID.
export class FeedbackStore {
  constructor(state) { this.storage = state.storage; }
  activeTransaction(fn) {
    return this.storage.transaction(async txn => await txn.get('account:deleted') ? json({ error: 'This account was deleted.' }, 410) : fn(txn));
  }
  async removeAccount() {
    // Commit a permanent write barrier before bounded cleanup. Retries resume
    // cleanup; queued quiz answers or publishing calls cannot recreate records.
    await this.storage.transaction(async txn => { await txn.put({ 'account:deleted': true }); });
    let remaining;
    do {
      remaining = await this.storage.transaction(async txn => {
        const keys = [...(await txn.list({ prefix: '', limit: 128 })).keys()].filter(key => key !== 'account:deleted');
        for (const key of keys) await txn.delete(key);
        return keys.length;
      });
    } while (remaining);
    return json({ deleted: true });
  }
  async fetch(request) {
    const url = new URL(request.url);
    const id = url.pathname.slice(1);
    // Internal-only routes: the public Worker never forwards arbitrary paths here.
    if (id === 'admin/delete-account' && request.method === 'POST') return this.removeAccount();
    if (await this.storage.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    if (id === 'admin/quiz-status' && request.method === 'GET') return json(await latestQuizStatus(this.storage));
    if (id === 'admin/cefr-status' && request.method === 'GET') return json(cefrOverview(await this.storage.get('cefr:current')));
    if (id === 'admin/cefr' && request.method === 'GET') return json({ cefr: await this.storage.get('cefr:current') || null });
    if (id === 'learning-import' && request.method === 'POST') {
      const input = await request.json();
      let feedback, assessment, quizzes;
      try {
        if (!Array.isArray(input.feedback) || !input.feedback.length || input.feedback.length > 100 ||
            !Array.isArray(input.quizzes) || input.quizzes.length !== input.feedback.length) throw new Error('Invalid import');
        feedback = input.feedback.map(f => validateFeedback(f, f.id));
        if (new Set(feedback.map(f => f.id)).size !== feedback.length || new Set(feedback.map(f => f.source.noteId)).size !== feedback.length) throw new Error('Duplicate session');
        assessment = validateAssessment(input.assessment);
        quizzes = input.quizzes.map(q => {
          const quiz = validateAssessment({ ...assessment, quiz: q.quiz }).quiz;
          if (!feedback.some(f => f.id === quiz.generatedForSession) || !quiz.sourceSessions?.includes(quiz.generatedForSession) ||
              !Array.isArray(q.evidence) || q.evidence.length !== quiz.questions.length) throw new Error('Invalid quiz');
          const evidence = q.evidence.map((e, i) => {
            if (e.questionIndex !== i || !Array.isArray(e.references) || !e.references.length || e.references.length > 12) throw new Error('Invalid quiz evidence');
            return { questionIndex: i, references: e.references.map(ref => {
              if (!quiz.sourceSessions.includes(ref.sessionId) || !FEEDBACK_ID.test(ref.sessionId) || !/^\d{2}:[0-5]\d:[0-5]\d$/.test(ref.at)) throw new Error('Invalid reference');
              return { sessionId: ref.sessionId, at: ref.at };
            }) };
          });
          return { quiz, evidence };
        });
        if (new Set(quizzes.map(q => q.quiz.generatedForSession)).size !== quizzes.length || feedback.some(f => !assessment.sourceSessions.includes(f.id))) throw new Error('Missing session');
        const latest = [...quizzes].sort((a,b) => a.quiz.generatedForSession.localeCompare(b.quiz.generatedForSession)).at(-1).quiz;
        if (JSON.stringify(assessment.quiz) !== JSON.stringify(latest)) throw new Error('Latest quiz differs');
      } catch { return json({ error: 'Please check the learning records and source references.' }, 400); }
      const canonical = JSON.stringify({ feedback, assessment, quizzes });
      const digest = [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(canonical)))].map(x => x.toString(16).padStart(2,'0')).join('');
      return this.activeTransaction(async txn => {
        if (await txn.get('import:history:' + digest)) return json({ ok: true, duplicate: true });
        const current = await txn.get('assessment:current') || null;
        if (JSON.stringify(input.priorAssessment ?? null) !== JSON.stringify(current)) return json({ error: 'The assessment changed. Review the latest account before importing.' }, 409);
        const sources = new Map(feedback.map(f => [f.id, f]));
        for (const record of feedback) {
          const existing = await txn.get('feedback:' + record.id);
          if (existing && JSON.stringify(existing) !== JSON.stringify(record)) return json({ error: 'An existing session differs. It has been preserved.' }, 409);
          if (await txn.get('quiz:published:' + record.id)) return json({ error: 'A quiz for this session already exists. It has been preserved.' }, 409);
        }
        const allIds = new Set([...assessment.sourceSessions, ...quizzes.flatMap(q => q.quiz.sourceSessions)]);
        for (const sourceId of allIds) if (!sources.has(sourceId)) sources.set(sourceId, await txn.get('feedback:' + sourceId));
        if ([...sources.values()].some(s => !s?.source?.reviewedFullTranscript)) return json({ error: 'A source session is unavailable in this account.' }, 400);
        const refs = [...assessmentReferences(assessment), ...quizzes.flatMap(q => q.evidence.flatMap(e => e.references))];
        if (refs.some(ref => ref.at < sources.get(ref.sessionId).source.coverageStart || ref.at > sources.get(ref.sessionId).source.coverageEnd)) return json({ error: 'Evidence is outside its source transcript.' }, 400);
        const importedAt = new Date().toISOString(), update = {};
        for (const f of feedback) {
          update['feedback:' + f.id] = f;
          update['index:' + f.id] = { id: f.id, title: f.title, summary: f.summary, startedAt: f.startedAt, timeZone: f.timeZone };
        }
        for (const q of quizzes) update['quiz:published:' + q.quiz.generatedForSession] = { ...q, historicalImport: true, publishedAt: importedAt };
        update['assessment:before:import:' + digest] = current;
        const currentLatest = current?.sourceSessions?.slice().sort().at(-1);
        if (!currentLatest || assessment.sourceSessions.slice().sort().at(-1) >= currentLatest) update['assessment:current'] = assessment;
        update['import:history:' + digest] = { importedAt, sessions: feedback.length, quizzes: quizzes.length };
        await txn.put(update);
        return json({ ok: true, sessions: feedback.length, quizzes: quizzes.length, currentUpdated: Boolean(update['assessment:current']) });
      });
    }
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
      return json({ assessment: await this.storage.get('assessment:current') || null, cefr: await this.storage.get('cefr:current') || null, attempts, publishedSessions, sourceNotes });
    }
    if (id === 'automation/publish' && request.method === 'POST') {
      const input = await request.json();
      return this.activeTransaction(async txn => {
        const sessionId = input.quiz?.generatedForSession;
        if (!FEEDBACK_ID.test(sessionId || '') || !Array.isArray(input.quiz?.sourceSessions) || !Array.isArray(input.quiz?.patternTitles)) return json({ error: 'Invalid session.' }, 400);
        const current = await txn.get('assessment:current') || null;
        if (await txn.get('quiz:published:' + sessionId) || current?.quiz?.generatedForSession === sessionId) return json({ ok: true, duplicate: true });
        if (JSON.stringify(input.priorAssessment) !== JSON.stringify(current)) return json({ error: 'Assessment changed. Retry with the latest record.' }, 409);
        let record, feedback, cefr;
        try {
          feedback = validateFeedback(input.feedback, sessionId);
          record = validateAssessment({ ...input.assessment, quiz: input.quiz });
          if (!record.sourceSessions.includes(sessionId)) throw new Error('Missing latest session');
          if (input.cefr !== undefined) {
            cefr = validateCefr(input.cefr);
            if (cefr.latestSessionId !== sessionId || cefr.assessedOn !== record.assessedOn ||
                cefr.sourceSessions?.some(id => !record.sourceSessions.includes(id))) throw new Error('Invalid CEFR source');
          }
        } catch { return json({ error: 'Invalid learning record.' }, 400); }
        for (const sourceId of new Set([...record.sourceSessions, ...record.quiz.sourceSessions])) {
          if (sourceId !== sessionId && !(await txn.get('feedback:' + sourceId))?.source?.reviewedFullTranscript) return json({ error: 'Source unavailable.' }, 400);
        }
        for (const ref of [...assessmentReferences(record), ...(cefr?.evidence || [])]) {
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
        if (cefr) {
          const previousCefr = await txn.get('cefr:current') || null;
          update['cefr:history:' + sessionId] = cefr;
          if (!previousCefr || sessionId > previousCefr.latestSessionId) update['cefr:current'] = cefr;
        }
        await txn.put(update);
        return json({ ok: true });
      });
    }
    if (id.startsWith('quiz/')) return handleQuiz(this.storage, request);
    if (id === 'assessment') {
      if (request.method === 'GET') return json({ assessment: await this.storage.get('assessment:current') || null });
      if (request.method !== 'PUT') return json({ error: 'Method not allowed.' }, 405);
      let record, input;
      try { input = await request.json(); record = validateAssessment(input); }
      catch { return json({ error: 'Please check the assessment format and session references.' }, 400); }
      const sourceIds = [...new Set([...record.sourceSessions, ...(record.quiz?.sourceSessions || [])])];
      const sources = new Map(await Promise.all(sourceIds.map(async sessionId => [sessionId, await this.storage.get(`feedback:${sessionId}`)])));
      if ([...sources.values()].some(source => !source?.source?.reviewedFullTranscript) || assessmentReferences(record).some(ref => {
        const coverage = sources.get(ref.sessionId).source;
        return ref.at < coverage.coverageStart || ref.at > coverage.coverageEnd;
      })) return json({ error: 'Assessment evidence must refer to this student’s available session transcripts.' }, 400);
      return this.activeTransaction(async txn => {
        if (Object.hasOwn(input, 'priorAssessment')) {
          const current = await txn.get('assessment:current') || null;
          if (JSON.stringify(input.priorAssessment) !== JSON.stringify(current)) return json({ error: 'The assessment changed. Review the latest version before saving.' }, 409);
          if (current) await txn.put({ ['assessment:before:edit:' + crypto.randomUUID()]: current });
        }
        await txn.put({ 'assessment:current': record });
        return json({ ok: true });
      });
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
    if (request.method === 'PATCH') {
      let input;
      try { input = validatePracticeEdit(await request.json()); }
      catch { return json({ error: 'Please check the practice edit.' }, 400); }
      return this.activeTransaction(async txn => {
        const current = await txn.get(`feedback:${id}`);
        if (!current) return json({ error: 'Session not found.' }, 404);
        const visible = { ...current, source: { ...current.source } };
        delete visible.source.noteId;
        if (JSON.stringify(input.priorFeedback) !== JSON.stringify(visible)) return json({ error: 'The feedback changed. Review the latest version before saving.' }, 409);
        let practice;
        try { practice = validateFeedbackPractice(input.practice, current); }
        catch { return json({ error: 'Use fresh practice examples based on this lesson.' }, 400); }
        await txn.put({
          ['practice:before:' + id + ':' + crypto.randomUUID()]: current.practice,
          [`feedback:${id}`]: { ...current, practice },
        });
        return json({ ok: true, id });
      });
    }
    if (request.method === 'PUT') {
      let record;
      try { record = validateFeedback(await request.json(), id); }
      catch { return json({ error: 'Please check the feedback format and transcript references.' }, 400); }
      const { title, summary, startedAt, timeZone } = record;
      return this.activeTransaction(async txn => {
        await txn.put({ [`feedback:${id}`]: record, [`index:${id}`]: { id, title, summary, startedAt, timeZone } });
        return json({ ok: true, id });
      });
    }
    return json({ error: 'Method not allowed.' }, 405);
  }
}
