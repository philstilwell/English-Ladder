const json = (data, status = 200) => Response.json(data, { status });
const defaultPreferences = () => ({ hideFinished: false, revision: 0, updatedAt: null });
const defaultPosition = () => ({ number: null, revision: 0, updatedAt: null });
const empty = number => ({ number, finished: false, question: false, revision: 0, updatedAt: null });

export function createSelfCheckHandler(prefix, bank) {
  const items = new Map(bank.items.map(item => [item.number, item]));
  return async function handleSelfCheck(storage, request) {
    const route = new URL(request.url).pathname;
    if (request.method === 'GET' && ['/' + prefix + '/state', '/' + prefix + '/questions'].includes(route)) {
      return storage.transaction(async txn => {
        if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
        const entries = [...(await txn.list({ prefix: prefix + ':item:' })).values()]
          .filter(entry => items.has(entry.number)).sort((a, b) => a.number - b.number);
        return json(route === '/' + prefix + '/state' ? { entries, preferences: await txn.get(prefix + ':preferences') || defaultPreferences(), position: await txn.get(prefix + ':position') || defaultPosition() } : {
          questions: entries.filter(entry => entry.question).map(entry => ({ ...items.get(entry.number), progress: entry })),
        });
      });
    }
    if (route !== '/' + prefix + '/state' || request.method !== 'PATCH') return json({ error: 'Page not found.' }, 404);
    let input;
    try { input = await request.json(); } catch { return json({ error: 'Please check your choice.' }, 400); }
    if (input?.field === 'position') {
      if (!items.has(input.value) || !Number.isSafeInteger(input.revision) || input.revision < 0 ||
          Object.keys(input).some(key => !['field', 'value', 'revision'].includes(key))) return json({ error: 'Please check your place.' }, 400);
      return storage.transaction(async txn => {
        if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
        const key = prefix + ':position', position = await txn.get(key) || defaultPosition();
        if (position.number === input.value) return json({ position });
        if (position.revision !== input.revision) return json({ error: 'Your place changed on another page.' }, 409);
        const updated = { number: input.value, revision: position.revision + 1, updatedAt: new Date().toISOString() };
        await txn.put({ [key]: updated });
        return json({ position: updated });
      });
    }
    if (input?.field === 'hideFinished') {
      if (typeof input.value !== 'boolean' || !Number.isSafeInteger(input.revision) || input.revision < 0 ||
          Object.keys(input).some(key => !['field', 'value', 'revision'].includes(key))) return json({ error: 'Please check your choice.' }, 400);
      return storage.transaction(async txn => {
        if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
        const key = prefix + ':preferences', preferences = await txn.get(key) || defaultPreferences();
        if (preferences.hideFinished === input.value) return json({ preferences });
        if (preferences.revision !== input.revision) return json({ error: 'Your choice changed on another page. Your saved choice is shown. Please try again.' }, 409);
        const updated = { hideFinished: input.value, revision: preferences.revision + 1, updatedAt: new Date().toISOString() };
        await txn.put({ [key]: updated });
        return json({ preferences: updated });
      });
    }
    if (!input || !items.has(input.number) || !['finished', 'question'].includes(input.field) ||
        typeof input.value !== 'boolean' || !Number.isSafeInteger(input.revision) || input.revision < 0 ||
        Object.keys(input).some(key => !['number', 'field', 'value', 'revision'].includes(key))) {
      return json({ error: 'Please check your choice.' }, 400);
    }
    return storage.transaction(async txn => {
      if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
      const key = prefix + ':item:' + input.number;
      const entry = await txn.get(key) || empty(input.number);
      // Explicit values make a repeated save harmless after a lost response.
      if (entry[input.field] === input.value) return json({ entry });
      if (entry.revision !== input.revision) return json({ error: 'This item changed on another page. Your saved choices have been reloaded. Please try again.' }, 409);
      const updated = { ...entry, [input.field]: input.value, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
      await txn.put({ [key]: updated });
      return json({ entry: updated });
    });
  };
}
