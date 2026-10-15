import bank from './business-terms-bank.json' with { type: 'json' };

const items = new Map(bank.items.map(item => [item.number, item]));
const json = (data, status = 200) => Response.json(data, { status });
const empty = number => ({ number, finished: false, question: false, revision: 0, updatedAt: null });

export async function handleBusinessTerms(storage, request) {
  const route = new URL(request.url).pathname;
  if (request.method === 'GET' && ['/terms/state', '/terms/questions'].includes(route)) {
    return storage.transaction(async txn => {
      if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
      const entries = [...(await txn.list({ prefix: 'terms:item:' })).values()]
        .filter(entry => items.has(entry.number)).sort((a, b) => a.number - b.number);
      return json(route === '/terms/state' ? { entries } : {
        questions: entries.filter(entry => entry.question).map(entry => ({ ...items.get(entry.number), progress: entry })),
      });
    });
  }
  if (route !== '/terms/state' || request.method !== 'PATCH') return json({ error: 'Page not found.' }, 404);
  let input;
  try { input = await request.json(); } catch { return json({ error: 'Please check your choice.' }, 400); }
  if (!input || !items.has(input.number) || !['finished', 'question'].includes(input.field) ||
      typeof input.value !== 'boolean' || !Number.isSafeInteger(input.revision) || input.revision < 0 ||
      Object.keys(input).some(key => !['number', 'field', 'value', 'revision'].includes(key))) {
    return json({ error: 'Please check your choice.' }, 400);
  }
  return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    const key = 'terms:item:' + input.number;
    const entry = await txn.get(key) || empty(input.number);
    // Explicit values make a repeated save harmless after a lost response.
    if (entry[input.field] === input.value) return json({ entry });
    if (entry.revision !== input.revision) return json({ error: 'This item changed on another page. Your saved choices have been reloaded. Please try again.' }, 409);
    const updated = { ...entry, [input.field]: input.value, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
    await txn.put({ [key]: updated });
    return json({ entry: updated });
  });
}
