import bank from './vocabulary-bank.json' with { type: 'json' };
import { createSelfCheckHandler } from './self-check.mjs';
const selfCheck = createSelfCheckHandler('vocabulary', bank, ['finished', 'question', 'review']);
const json = (data, status = 200) => Response.json(data, { status });

export async function handleVocabulary(storage, request) {
  if (request.method !== 'PATCH') return selfCheck(storage, request);
  let input;
  try { input = await request.clone().json(); } catch { return json({ error: 'Please check your work.' }, 400); }
  if (input?.field !== 'batch') return selfCheck(storage, request);
  const expected = bank.items.slice((input.batch - 1) * 10, input.batch * 10);
  if (new URL(request.url).pathname !== '/vocabulary/state' || !Number.isInteger(input.batch) || input.batch < 1 || !expected.length ||
      Object.keys(input).some(k => !['field', 'batch', 'entries'].includes(k)) || !Array.isArray(input.entries) || input.entries.length !== expected.length ||
      input.entries.some((e, i) => !e || e.number !== expected[i].number || !Number.isSafeInteger(e.revision) || e.revision < 0 ||
        typeof e.answer !== 'string' || e.answer.length > 120 || typeof e.sentence !== 'string' || e.sentence.length > 1000 ||
        Object.keys(e).some(k => !['number', 'revision', 'answer', 'sentence'].includes(k)))) return json({ error: 'Please check this batch. Answers may have 120 characters and sentences 1,000 characters.' }, 400);
  return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    const entries = [], changes = {};
    for (const draft of input.entries) {
      const key = 'vocabulary:item:' + draft.number;
      const saved = await txn.get(key) || { number: draft.number, finished: false, question: false, review: false, answer: '', sentence: '', revision: 0, updatedAt: null };
      if ((saved.answer || '') === draft.answer && (saved.sentence || '') === draft.sentence) { entries.push(saved); continue; }
      if (saved.revision !== draft.revision) return json({ error: 'This batch changed on another page. Your draft has not replaced the saved work.' }, 409);
      const updated = { ...saved, answer: draft.answer, sentence: draft.sentence, revision: saved.revision + 1, updatedAt: new Date().toISOString() };
      entries.push(updated); changes[key] = updated;
    }
    if (Object.keys(changes).length) await txn.put(changes);
    return json({ entries });
  });
}
