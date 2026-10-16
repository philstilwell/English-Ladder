const json = (data, status = 200) => Response.json(data, { status });
const ID = /^[a-f0-9]{64}$/;
const PAGE_SIZE = 20;
// Identity follows the complete authored exercise, not its list position or date.
// Publishing a rewritten topic cannot inherit completion from an older exercise.
export async function studyTopics(assessment) {
  return Promise.all((assessment?.plan || []).map(async item => {
    const topic = { title: item.title, activity: item.activity, target: item.target, ...(item.aiPrompt === undefined ? {} : { aiPrompt: item.aiPrompt }) };
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(JSON.stringify(topic)));
    return { ...topic, id: Array.from(new Uint8Array(digest), byte => byte.toString(16).padStart(2, '0')).join('') };
  }));
}
const empty = id => ({ id, finished: false, question: false, revision: 0, updatedAt: null });
const progress = entry => ({ id: entry.id, finished: entry.finished, question: entry.question, revision: entry.revision, updatedAt: entry.updatedAt });

export async function handleStudyProgress(storage, request) {
  const url = new URL(request.url), route = url.pathname;
  if (!['/study/state', '/study/questions'].includes(route)) return json({ error: 'Page not found.' }, 404);
  if (request.method === 'GET') {
    const after = url.searchParams.get('after');
    if (after !== null && !ID.test(after)) return json({ error: 'Please check the page.' }, 400);
    return storage.transaction(async txn => {
      if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
      const topics = await studyTopics(await txn.get('assessment:current'));
      if (route === '/study/state') {
        return json({ topics: await Promise.all(topics.map(async topic => ({ ...topic, progress: progress(await txn.get('study:item:' + topic.id) || empty(topic.id)) }))) });
      }
      const saved = [...(await txn.list({ prefix: 'study:question:', limit: PAGE_SIZE + 1, ...(after ? { startAfter: 'study:question:' + after } : {}) })).values()];
      const current = new Set(topics.map(topic => topic.id));
      return json({ questions: saved.slice(0, PAGE_SIZE).map(entry => ({ ...entry.topic, progress: progress(entry), current: current.has(entry.id) })), nextCursor: saved.length > PAGE_SIZE ? saved[PAGE_SIZE - 1].id : null });
    });
  }
  if (route !== '/study/state' || request.method !== 'PATCH') return json({ error: 'Method not allowed.' }, 405);
  let input;
  try { input = await request.json(); } catch { return json({ error: 'Please check your choice.' }, 400); }
  if (!input || typeof input.id !== 'string' || !ID.test(input.id) || !['finished', 'question'].includes(input.field) || typeof input.value !== 'boolean' ||
      !Number.isSafeInteger(input.revision) || input.revision < 0 || Object.keys(input).some(key => !['id', 'field', 'value', 'revision'].includes(key))) return json({ error: 'Please check your choice.' }, 400);
  return storage.transaction(async txn => {
    if (await txn.get('account:deleted')) return json({ error: 'This account was deleted.' }, 410);
    const key = 'study:item:' + input.id, saved = await txn.get(key);
    const topic = (await studyTopics(await txn.get('assessment:current'))).find(topic => topic.id === input.id) || saved?.topic;
    if (!topic) return json({ error: 'This topic changed. Reopen Assessments to see the latest topics.' }, 409);
    const entry = saved || { ...empty(input.id), topic };
    // Safe to retry after losing a response; never toggle blindly or overwrite
    // a different field from another tab. Only the server supplies topic content.
    if (entry[input.field] === input.value) return json({ entry: progress(entry) });
    if (entry.revision !== input.revision) return json({ error: 'This topic changed on another page. Your saved choices have been reloaded. Please try again.' }, 409);
    const updated = { ...entry, [input.field]: input.value, revision: entry.revision + 1, updatedAt: new Date().toISOString() };
    await txn.put({ [key]: updated });
    if (updated.question) await txn.put({ ['study:question:' + input.id]: updated });
    else await txn.delete('study:question:' + input.id);
    return json({ entry: progress(updated) });
  });
}
