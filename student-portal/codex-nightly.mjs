// Durable readiness limits, shared by queue reporting and scheduled preparation.
// Only metadata is retained; this module never processes transcript text.
export const RECHECK_DELAY = 15 * 60 * 1000;
export const CATCH_UP_LOOKBACK = 24 * 60 * 60 * 1000;
// A partial discovery can find a note before its completed meeting lookup
// succeeds. These temporary failures share the existing single recheck; they
// must not permanently consume it or reset the reservation when metadata lands.
export const delayedSource = code => ['meeting_pending', 'transcript_unusable', 'meeting_reference_missing', 'zoom_unavailable'].includes(code);
export function runDate(now = Date.now()) {
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date(now)).map(p => [p.type, p.value]));
  const date = `${parts.year}-${parts.month}-${parts.day}`;
  // A run continued after midnight still belongs to the preceding 23:35 wake.
  return Number(parts.hour) * 60 + Number(parts.minute) >= 23 * 60 + 35 ? date : new Date(Date.parse(date + 'T12:00:00Z') - 86400000).toISOString().slice(0, 10);
}
export const sourceVersion = job => JSON.stringify([job.modifiedAt || null, job.sourceEventAt || null, job.meetingId || null]);
export function preparationState(job, now = Date.now()) {
  const check = job.codexCheck;
  if (check?.runDate === runDate(now)) {
    if (check.retryAt && check.checks === 1) return { waiting: Date.parse(check.retryAt) > now, retryAt: check.retryAt };
    return { deferred: true, error: job.lastError || null };
  }
  // A known empty source needs a Zoom revision, not a fresh retry every night.
  if (job.lastError === 'transcript_unusable' && (!check || check.sourceVersion === sourceVersion(job))) return { deferred: true, error: job.lastError };
  if (job.status === 'needs_attention') return { deferred: true, error: job.lastError || null };
  return { waiting: false };
}
export async function catchUpWarnings(c, entries) {
  const students = await c.students();
  return entries.filter(([, j]) => j.status === 'skipped' && j.skipReason === 'catch_up_required' && students[j.studentId] &&
    Date.parse(j.startedAt) < Date.parse(students[j.studentId].startAfter) &&
    Date.parse(j.startedAt) >= Date.parse(students[j.studentId].startAfter) - CATCH_UP_LOOKBACK)
    .map(([key, j]) => ({ id: key.slice(4), studentId: j.studentId, startedAt: j.startedAt }))
    .sort((a, b) => b.startedAt.localeCompare(a.startedAt));
}
