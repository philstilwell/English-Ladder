import { studyTopics } from './study-progress.mjs';
import vocabularyBank from './vocabulary-bank.json' with { type: 'json' };
import grammarBank from './grammar-bank.json' with { type: 'json' };
import termsBank from './business-terms-bank.json' with { type: 'json' };

const sources = [
  { id: 'vocabulary-practice', label: 'Vocabulary practice', prefix: 'vocabulary:item:', bank: vocabularyBank },
  { id: 'grammar-practice', label: 'Grammar practice', prefix: 'grammar:item:', bank: grammarBank },
  { id: 'business-terms', label: 'Business terms', prefix: 'terms:item:', bank: termsBank },
  { id: 'study-practice', label: 'Study on your own', prefix: 'study:question:' },
];
for (const source of sources) if (source.bank) source.items = new Map(source.bank.items.map(item => [item.number, item]));

async function* records(storage, prefix) {
  let cursor;
  do {
    const page = await storage.list({ prefix, limit: 500, ...(cursor ? { startAfter: cursor } : {}) });
    for (const entry of page.values()) yield entry;
    if (page.size < 500) return;
    cursor = [...page.keys()].at(-1);
  } while (cursor);
}

// Derive the combined list from existing choices. Reading it never writes or
// changes completion, questions, or assessment history.
export async function questionsOverview(storage, { after = null, statusOnly = false } = {}) {
  if (after !== null && !/^(grammar-practice|business-terms|study-practice|vocabulary-practice):(?:\d{8}|[a-f0-9]{64})$/.test(after)) {
    return Response.json({ error: 'Please check the page.' }, { status: 400 });
  }
  const counts = {}, selected = [];
  const currentTopics = statusOnly ? new Set() : new Set((await studyTopics(await storage.get('assessment:current'))).map(t => t.id));
  let count = 0;
  for (const source of sources) {
    counts[source.id] = 0;
    for await (const entry of records(storage, source.prefix)) {
      if (!entry.question) continue;
      const item = source.items ? source.items.get(entry.number) : entry.topic;
      if (!item) continue;
      counts[source.id]++; count++;
      if (statusOnly) continue;
      const id = source.id + ':' + (source.items ? String(entry.number).padStart(8, '0') : entry.id);
      if (after && id <= after) continue;
      const progress = { ...(source.id === 'study-practice' ? { id: entry.id, revision: entry.revision } : {}), finished: Boolean(entry.finished), question: true, updatedAt: entry.updatedAt || null };
      selected.push({ id, source: source.id, label: source.label, item: { ...item, progress, ...(source.id === 'study-practice' ? { current: currentTopics.has(entry.id) } : {}), ...(source.id === 'vocabulary-practice' ? { studentAnswer: entry.answer || '', studentSentence: entry.sentence || '' } : {}) } });
      // Keep only the next page and one sentinel while scanning bounded pages.
      selected.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
      if (selected.length > 21) selected.pop();
    }
  }
  return Response.json(statusOnly ? { state: 'ready', count } : {
    count, counts, questions: selected.slice(0, 20), nextCursor: selected.length > 20 ? selected[19].id : null,
  });
}
