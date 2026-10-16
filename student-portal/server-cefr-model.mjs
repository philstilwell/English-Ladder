import { CEFR_RULES, groundCefrWindow } from './cefr.mjs';
import { modelJson } from './server-ai-json.mjs';

export function cefrModelInput(context) {
  const input = { sessions: context.sessions.map(({ sessionId, segments }) => ({ sessionId, segments })) };
  // Keep every turn of every selected lesson. An oversized window is deferred,
  // never silently shortened to a sample or replaced by old assessment prose.
  if (new TextEncoder().encode(JSON.stringify(input)).length > 300000) throw new Error('cefr_window_too_large');
  return input;
}

async function generate(ai, rules, input, maxTokens) {
  return modelJson(ai, rules, input, maxTokens);
}

export async function authorCefr(ai, context) {
  const input = cefrModelInput(context);
  const draft = await generate(ai, CEFR_RULES, input, 5000);
  let cefr;
  try { cefr = groundCefrWindow(draft.cefr, context.sessions, context.today); }
  catch { throw new Error('invalid_cefr_evidence'); }
  const review = await generate(ai, CEFR_RULES + '\nAct as an independent editor. Verify the proposed estimate against ALL supplied transcripts, including exact learner attribution, privacy, every session, level/range, confidence, and the limited scope. Return {"approved":true} only if it meets every rule; otherwise return {"approved":false}. An honest insufficient state is valid when the language is insufficient.', { ...input, proposed: cefr }, 4000);
  if (review.approved !== true) throw new Error('cefr_review_failed');
  return cefr;
}
