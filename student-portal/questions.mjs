import { roadQuestionItem } from './road-questions.mjs';
import { COMMUNICATION_ACTIVITIES, communicationPrefix } from './communication-practice.mjs';
import { studyTopics } from './study-progress.mjs';
import vocabularyBank from './vocabulary-bank.json' with { type: 'json' };
import grammarBank from './grammar-bank.json' with { type: 'json' };
import termsBank from './business-terms-bank.json' with { type: 'json' };

const sources = [
  { id: 'english-road', label: 'English Road Practice', prefix: 'road:question:' },
  ...COMMUNICATION_ACTIVITIES.map(bank => ({ id: bank.id, label: bank.name, prefix: communicationPrefix(bank) + ':item:', bank, communication: true })),
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
  if (after !== null && (typeof after !== 'string' || !sources.some(source => after.startsWith(source.id + ':')) || !/^(?:[a-z-]+:(?:\d{8}|[a-f0-9]{64})|english-road:[0-9a-f-]{36}_\d{2})$/.test(after))) {
    return Response.json({ error: 'Please check the page.' }, { status: 400 });
  }
  const counts = {}, selected = [];
  const currentTopics = statusOnly ? new Set() : new Set((await studyTopics(await storage.get('assessment:current'))).map(t => t.id));
  let count = 0;
  for (const source of sources) {
    counts[source.id] = 0;
    for await (const entry of records(storage, source.prefix)) {
      if (!entry.question) continue;
      const item = source.items ? source.items.get(entry.number) : source.id === 'english-road' ? entry.exercise : entry.topic;
      if (!item) continue;
      counts[source.id]++; count++;
      if (statusOnly) continue;
      const id = source.id + ':' + (source.items ? String(entry.number).padStart(8, '0') : entry.id);
      if (after && id <= after) continue;
      const progress = { ...(source.communication ? { choice: entry.choice, correct: entry.correct, firstChoice: entry.firstChoice, firstCorrect: entry.firstCorrect } : {}), ...(source.id === 'study-practice' ? { id: entry.id, revision: entry.revision } : {}), finished: Boolean(entry.finished), question: true, updatedAt: entry.updatedAt || null };
      selected.push({ id, revision: entry.revision, source: source.id, label: source.label, item: source.id === 'english-road' ? entry : { ...item, progress, ...(source.id === 'study-practice' ? { current: currentTopics.has(entry.id) } : {}), ...(source.id === 'vocabulary-practice' ? { studentAnswer: entry.answer || '', studentSentence: entry.sentence || '' } : {}) } });
      // Keep only the next page and one sentinel while scanning bounded pages.
      selected.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
      if (selected.length > 21) selected.pop();
    }
  }
  return Response.json(statusOnly ? { state: 'ready', count } : {
    count, counts, questions: await Promise.all(selected.slice(0, 20).map(async row => row.source === 'english-road' ? { ...row, item: await roadQuestionItem(storage, row.item) } : row)), nextCursor: selected.length > 20 ? selected[19].id : null,
  });
}

// Called only inside the account's deletion-checked transaction. The teacher
// clears the same flag the student reads; no learning record is deleted.
export async function resolveQuestion(storage, input, undo = false) {
  const invalid = () => Response.json({ error: 'Please refresh the Questions list and try again.' }, { status: 400 });
  if (!input || typeof input.id !== 'string' || !Number.isSafeInteger(input.revision) || input.revision < 1 ||
      Object.keys(input).some(key => !['id', 'revision'].includes(key))) return invalid();
  const [sourceId, itemId, extra] = input.id.split(':'), source = sources.find(s => s.id === sourceId);
  if (!source || extra !== undefined) return invalid();
  if (source.items ? !/^\d{8}$/.test(itemId) || !source.items.has(Number(itemId)) :
      !(sourceId === 'english-road' ? /^[0-9a-f-]{36}_\d{2}$/ : /^[a-f0-9]{64}$/).test(itemId)) return invalid();
  const key = source.prefix.replace(':question:', ':item:') + (source.items ? Number(itemId) : itemId);
  const entry = await storage.get(key);
  if (!entry) return Response.json({ error: 'This saved question is no longer available. Refresh the list.' }, { status: 404 });
  const receiptKey = 'questions:resolved:' + input.id, receipt = await storage.get(receiptKey);
  if (undo) {
    const conflict = () => Response.json({ error: 'This item changed after it was resolved. Undo was not applied; the newer choices were kept.' }, { status: 409 });
    // An undo refers to one specific administrator resolution, not any later
    // student removal or a newer resolution. Receipts contain no exercise text.
    if (!receipt || receipt.revision !== input.revision) return conflict();
    if (entry.question) return Response.json({ restored: true, id: input.id, revision: entry.revision });
    if (receipt.restoredRevision || entry.revision !== input.revision) return conflict();
    const restored = { ...entry, question: true, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
    await storage.put({ [key]: restored, [receiptKey]: { ...receipt, restoredRevision: restored.revision },
      ...(!source.items ? { [source.prefix + itemId]: restored } : {}) });
    return Response.json({ restored: true, id: input.id, revision: restored.revision });
  }
  // Repeating a successful request after a lost response is harmless. A newer
  // re-added question still requires its current revision before resolving.
  if (!entry.question) return Response.json({ resolved: true, id: input.id, revision: entry.revision,
    undoable: Boolean(receipt && receipt.revision === entry.revision && !receipt.restoredRevision) });
  if (entry.revision !== input.revision) return Response.json({ error: 'This item changed since you opened it. Refresh the Questions list before marking it resolved.' }, { status: 409 });
  const updated = { ...entry, question: false, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
  await storage.put({ [key]: updated, [receiptKey]: { revision: updated.revision } });
  if (!source.items) await storage.delete(source.prefix + itemId);
  return Response.json({ resolved: true, id: input.id, revision: updated.revision, undoable: true });
}
