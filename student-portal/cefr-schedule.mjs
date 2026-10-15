import { readTranscriptCache, transcriptHash, transcriptLessonDay } from './transcript-cache.mjs';
import { sessionId, nextCalendarMonth } from './lesson-time.mjs';

// Reads only the latest reviewed version of each distinct retained meeting.
// No source download, old assessment, or previous CEFR quote fills a missing lesson.
export async function cefrReviewContext(storage, timeZone = 'America/New_York') {
  const records = []; let end;
  while (true) {
    const page = [...await storage.list({ prefix: 'transcript:head:', reverse: true, limit: 50, ...(end ? { end } : {}) })];
    for (const [key] of page) {
      const record = await readTranscriptCache(storage, key.slice('transcript:head:'.length));
      if (record && Date.parse(record.meeting.end_time) <= Date.now() - 900000) records.push(record);
    }
    if (page.length < 50) break;
    end = page.at(-1)[0];
  }
  records.sort((a, b) => Date.parse(b.meeting.start_time) - Date.parse(a.meeting.start_time) || Date.parse(b.savedAt) - Date.parse(a.savedAt));
  const seenMeetings = new Set(), seenContent = new Set(), seenSessions = new Set(), available = [];
  for (const record of records) {
    const id = sessionId(record.meeting.start_time, timeZone);
    if (seenMeetings.has(record.meetingId) || seenContent.has(record.sourceHash) || seenSessions.has(id)) continue;
    seenMeetings.add(record.meetingId); seenContent.add(record.sourceHash); seenSessions.add(id);
    available.push({ sessionId: id, noteId: record.noteId, sourceHash: record.sourceHash, segments: record.segments });
    if (available.length === 4) break;
  }
  const current = await storage.get('cefr:current') || null, review = await storage.get('cefr:review') || null;
  const initial = current?.state !== 'estimated' || current.sourceSessions.length < 2;
  const sessions = available.slice(0, initial ? 2 : 4).reverse();
  const references = sessions.map(({ sessionId, noteId, sourceHash }) => ({ sessionId, noteId, sourceHash }));
  const windowHash = await transcriptHash(JSON.stringify({ timeZone, references, segments: sessions.map(s => s.segments) }));
  const today = transcriptLessonDay(Date.now());
  const nextReviewOn = !initial ? nextCalendarMonth(review?.completedOn || current.assessedOn) : null;
  const unchanged = review?.windowHash === windowHash || (review?.references && references.every(ref => review.references.some(old => old.sessionId === ref.sessionId && old.sourceHash === ref.sourceHash)));
  const due = sessions.length >= 2 && (!nextReviewOn || today >= nextReviewOn) && !unchanged;
  return { current, review, sessions, references, windowHash, today, due, initial, nextReviewOn, availableSessions: available.length };
}

export function cefrScheduleSummary(context) {
  return { initialAfter: 2, monthlySessionLimit: 4, availableSessions: context.availableSessions, nextReviewOn: context.nextReviewOn,
    lastReviewOn: context.review?.completedOn || null, lastReviewState: context.review?.state || null };
}
