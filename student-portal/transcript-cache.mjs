// Internal-only, per-student archive. No raw Zoom response is accepted here.
export const TRANSCRIPT_PRIVACY_VERSION = 1;
export const validNoteId = value => typeof value === 'string' && /^[\w-]{10,80}$/.test(value);
const stamp = value => typeof value === 'string' && /^\d{2}:[0-5]\d:[0-5]\d$/.test(value);
const iso = value => typeof value === 'string' && Number.isFinite(Date.parse(value));
const hashPattern = /^[a-f0-9]{64}$/;
export const transcriptHash = async value => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value)))].map(n => n.toString(16).padStart(2, '0')).join('');
const invalid = () => { throw new Error('invalid_transcript_cache'); };
export const transcriptLessonDay = time => {
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(new Date(time)).map(p => [p.type, p.value]));
  return `${parts.year}-${parts.month}-${parts.day}`;
};
export function transcriptRetentionDay(now = Date.now()) {
  const [year, month, day] = transcriptLessonDay(now).split('-').map(Number);
  const target = new Date(Date.UTC(year, month - 4, 1));
  const lastDay = new Date(Date.UTC(target.getUTCFullYear(), target.getUTCMonth() + 1, 0)).getUTCDate();
  target.setUTCDate(Math.min(day, lastDay));
  return target.toISOString().slice(0, 10);
}

export function validateTranscriptCache(value) {
  if (!value || value.privacyVersion !== TRANSCRIPT_PRIVACY_VERSION || value.privacyReviewed !== true || !validNoteId(value.noteId) ||
      typeof value.meetingId !== 'string' || !value.meetingId || value.meetingId.length > 128 ||
      !hashPattern.test(value.mappingHash) || !hashPattern.test(value.sourceHash) || !iso(value.savedAt) ||
      value.modifiedAt !== null && !iso(value.modifiedAt) ||
      value.sourceEventAt !== null && (!Number.isSafeInteger(value.sourceEventAt) || value.sourceEventAt < 0) ||
      !iso(value.meeting?.start_time) || !iso(value.meeting?.end_time) || Date.parse(value.meeting.end_time) <= Date.parse(value.meeting.start_time)) invalid();
  if (!Array.isArray(value.segments) || value.segments.length < 10 || value.segments.length > 20000) invalid();
  let previous = '';
  const segments = value.segments.map((s, index) => {
    if (s.index !== index || !stamp(s.at) || !stamp(s.end) || s.end < s.at || s.at < previous ||
        typeof s.text !== 'string' || !['student', 'instructor', 'other'].includes(s.role) ||
        (s.role === 'student' ? s.speaker !== 'Student' : s.role === 'instructor' ? s.speaker !== 'Instructor' : !/^Speaker \d{1,3}$/.test(s.speaker))) invalid();
    previous = s.at;
    return { index, at: s.at, end: s.end, role: s.role, speaker: s.speaker, text: s.text };
  });
  if (!segments.some(s => s.role === 'student' && s.text.trim()) || JSON.stringify(segments).length > 240000) invalid();
  return { privacyVersion: TRANSCRIPT_PRIVACY_VERSION, privacyReviewed: true, noteId: value.noteId,
    meetingId: value.meetingId, mappingHash: value.mappingHash, sourceHash: value.sourceHash, savedAt: value.savedAt,
    modifiedAt: value.modifiedAt, sourceEventAt: value.sourceEventAt,
    meeting: { start_time: value.meeting.start_time, end_time: value.meeting.end_time }, segments };
}

export async function saveTranscriptCache(storage, input) {
  const record = validateTranscriptCache(input), lessonDay = transcriptLessonDay(record.meeting.start_time);
  if (lessonDay < transcriptRetentionDay()) return { ok: true, retained: false };
  const body = JSON.stringify(record), version = await transcriptHash(body);
  // 12,000 UTF-16 code units fit comfortably under a value's byte limit even
  // with Unicode or JSON escapes. Keep all turns; never truncate a transcript.
  const chunks = [];
  for (let i = 0; i < body.length; i += 12000) chunks.push(body.slice(i, i + 12000));
  const update = {};
  for (let i = 0; i < chunks.length; i++) update['transcript:data:' + version + ':' + i] = chunks[i];
  update['transcript:head:' + record.noteId] = { version, chunks: chunks.length };
  update['transcript:version:' + version] = { noteId: record.noteId, chunks: chunks.length, lessonDay };
  await storage.put(update);
  return { ok: true };
}

export async function readTranscriptCache(storage, noteId) {
  if (!validNoteId(noteId)) invalid();
  const head = await storage.get('transcript:head:' + noteId);
  if (!head) return null;
  if (!hashPattern.test(head.version) || !Number.isInteger(head.chunks) || head.chunks < 1 || head.chunks > 24) return null;
  const chunks = [];
  for (let i = 0; i < head.chunks; i++) {
    const part = await storage.get('transcript:data:' + head.version + ':' + i);
    if (typeof part !== 'string' || part.length > 12000) return null;
    chunks.push(part);
  }
  const body = chunks.join('');
  if (await transcriptHash(body) !== head.version) return null;
  try { const record = validateTranscriptCache(JSON.parse(body)); return record.noteId === noteId && transcriptLessonDay(record.meeting.start_time) >= transcriptRetentionDay() ? record : null; }
  catch { return null; }
}

export async function pruneTranscriptCache(storage) {
  const cutoff = transcriptRetentionDay(); let end, removed = 0;
  while (true) {
    const page = [...await storage.list({ prefix: 'transcript:version:', reverse: true, limit: 50, ...(end ? { end } : {}) })];
    for (const [key, manifest] of page) {
      if (manifest.lessonDay >= cutoff) continue;
      const version = key.slice('transcript:version:'.length);
      if (!hashPattern.test(version) || !validNoteId(manifest.noteId) || !Number.isInteger(manifest.chunks) || manifest.chunks < 1 || manifest.chunks > 24) throw new Error('invalid_transcript_cache');
      for (let i = 0; i < manifest.chunks; i++) await storage.delete('transcript:data:' + version + ':' + i);
      const headKey = 'transcript:head:' + manifest.noteId;
      if ((await storage.get(headKey))?.version === version) await storage.delete(headKey);
      await storage.delete(key); removed++;
    }
    if (page.length < 50) break;
    end = page.at(-1)[0];
  }
  return { ok: true, removed, cutoff };
}

export function reusableTranscript(record, job, mappingHash, now = Date.now()) {
  if (!record || record.privacyVersion !== TRANSCRIPT_PRIVACY_VERSION || record.noteId !== job.noteId ||
      transcriptLessonDay(record.meeting.start_time) < transcriptRetentionDay(now) ||
      record.meetingId !== job.meetingId || record.mappingHash !== mappingHash || record.modifiedAt !== (job.modifiedAt || null) ||
      record.sourceEventAt !== (job.sourceEventAt || null)) return false;
  // Without a source revision, conservatively refresh after seven days on a
  // pending retry. Completed jobs remain skipped and their archive is retained.
  return Boolean(record.modifiedAt || record.sourceEventAt) || now - Date.parse(record.savedAt) < 7 * 86400000;
}
