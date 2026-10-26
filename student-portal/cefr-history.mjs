import { validateCefr } from './cefr.mjs';

const PREFIX = 'cefr:history:';
export const CEFR_HISTORY_PAGE_SIZE = 12;
export function validCefrHistoryCursor(value) {
  if (value === null) return true;
  if (!/^\d{4}-\d{2}-\d{2}:[a-f0-9]{64}$/.test(value)) return false;
  const day = value.slice(0, 10), date = new Date(day);
  return Number.isFinite(date.getTime()) && date.toISOString().slice(0, 10) === day;
}

// Reading history never changes an estimate, a review reservation or a lesson.
// Only the authenticated administrator route exposes these saved snapshots.
export async function cefrHistory(storage, before = null) {
  const rows = [...await storage.list({ prefix: PREFIX, reverse: true,
    limit: CEFR_HISTORY_PAGE_SIZE + 1, ...(before ? { end: PREFIX + before } : {}) })];
  const page = rows.slice(0, CEFR_HISTORY_PAGE_SIZE);
  const history = page.map(([, record]) => validateCefr(record));
  // Support an older saved estimate that predates the monthly history writer.
  // Keep its original date and do not create a new review merely by reading it.
  if (!before && !rows.length) {
    const current = await storage.get('cefr:current');
    if (current) history.push(validateCefr(current));
  }
  return { history, nextCursor: rows.length > CEFR_HISTORY_PAGE_SIZE ? page.at(-1)[0].slice(PREFIX.length) : null };
}
