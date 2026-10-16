import vocabularyBank from './vocabulary-bank.json' with { type: 'json' };
import grammarBank from './grammar-bank.json' with { type: 'json' };
import termsBank from './business-terms-bank.json' with { type: 'json' };

// Read existing work only. Opening this overview never creates activity records.
async function* records(storage, prefix) {
  let cursor;
  do {
    const page = await storage.list({ prefix, limit: 500, ...(cursor ? { startAfter: cursor } : {}) });
    for (const value of page.values()) yield value;
    if (page.size < 500) return;
    cursor = [...page.keys()].at(-1);
  } while (cursor);
}
const latest = (...values) => values.filter(value => typeof value === 'string' && Number.isFinite(Date.parse(value)))
  .sort((a, b) => Date.parse(b) - Date.parse(a))[0] || null;
const banks = [
  { id: 'grammar-practice', prefix: 'grammar', numbers: new Set(grammarBank.items.map(item => item.number)) },
  { id: 'business-terms', prefix: 'terms', numbers: new Set(termsBank.items.map(item => item.number)) },
  { id: 'vocabulary-practice', prefix: 'vocabulary', numbers: new Set(vocabularyBank.items.map(item => item.number)) },
];

export async function activitySummary(storage) {
  const road = { id: 'english-road', setsStarted: 0, setsCompleted: 0, answered: 0, correct: 0, latestSet: null, lastActivityAt: null };
  for await (const row of records(storage, 'road:index:')) {
    road.setsStarted++;
    if (row.completedAt) road.setsCompleted++;
    road.answered += row.answered;
    road.correct += row.correct;
    const at = latest(row.updatedAt, row.completedAt, row.endedAt, row.startedAt);
    if (!road.latestSet || at && (!road.lastActivityAt || Date.parse(at) >= Date.parse(road.lastActivityAt))) {
      road.latestSet = { band: row.band, topic: row.topic, answered: row.answered, total: row.total,
        state: row.completedAt ? 'completed' : row.endedAt ? 'ended' : 'in_progress' };
    }
    road.lastActivityAt = latest(road.lastActivityAt, at);
  }
  const activities = [road];
  for (const bank of banks) {
    const summary = { id: bank.id, total: bank.numbers.size, finished: 0, questions: 0, savedPlace: null, lastActivityAt: null };
    for await (const row of records(storage, bank.prefix + ':item:')) {
      if (!bank.numbers.has(row.number)) continue;
      if (row.finished) summary.finished++;
      if (row.question) summary.questions++;
      summary.lastActivityAt = latest(summary.lastActivityAt, row.updatedAt);
    }
    const position = await storage.get(bank.prefix + ':position');
    const preferences = await storage.get(bank.prefix + ':preferences');
    if (bank.numbers.has(position?.number)) {
      summary.savedPlace = position.number;
      summary.lastActivityAt = latest(summary.lastActivityAt, position.updatedAt);
    }
    summary.lastActivityAt = latest(summary.lastActivityAt, preferences?.updatedAt);
    activities.push(summary);
  }
  return { activities };
}

// Student pages receive counts for their own account, without administrator
// dates, saved positions, answer content, or transcript information.
export async function studentActivityProgress(storage) {
  const { activities } = await activitySummary(storage);
  return { activities: activities.map(row => row.id === 'english-road'
    ? { id: row.id, setsStarted: row.setsStarted, setsCompleted: row.setsCompleted, answered: row.answered,
      currentSet: row.latestSet?.state === 'in_progress' ? { answered: row.latestSet.answered, total: row.latestSet.total } : null }
    : { id: row.id, total: row.total, finished: row.finished, questions: row.questions }) };
}
