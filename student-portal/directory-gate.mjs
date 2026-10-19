// A private, short-lived existence hint rejects guessed hostnames without one
// Durable Object request per guess. It never authorizes a student or caches a
// password, profile, session, or active/paused decision.
const hints = new WeakMap();
const TTL_MS = 60_000;
const RETRY_MS = 5_000;

export function clearDirectoryHint(binding) {
  if (binding) hints.delete(binding);
}

export async function directoryMayContainAccount(binding, id, now = Date.now) {
  let hint = hints.get(binding);
  if (!hint) {
    hint = { ids: null, expires: 0, pending: null, retryAt: 0, error: null };
    hints.set(binding, hint);
  }
  if (hint.ids && now() < hint.expires) return hint.ids.has(id);
  if (now() < hint.retryAt) throw hint.error;
  if (!hint.pending) {
    hint.pending = Promise.resolve().then(async () => {
      try {
        const response = await binding.get(binding.idFromName('students')).fetch(new Request('https://directory.internal/account-ids'));
        if (!response.ok) throw new Error('Directory unavailable');
        const data = await response.json();
        if (!Array.isArray(data.studentIds) || data.studentIds.some(value => typeof value !== 'string')) throw new Error('Directory unavailable');
        hint.ids = new Set(data.studentIds);
        hint.expires = now() + TTL_MS;
        hint.error = null;
        hint.retryAt = 0;
      } catch (error) {
        hint.error = error;
        hint.retryAt = now() + RETRY_MS;
        throw error;
      } finally {
        hint.pending = null;
      }
    });
  }
  await hint.pending;
  return hint.ids.has(id);
}
