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
