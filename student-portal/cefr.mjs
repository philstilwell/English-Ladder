// A teaching estimate of transcript-observable conversation, never an exam result.
// Stored separately from student-facing assessments and returned only to the admin.
export const CEFR_LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
export const CEFR_AREAS = ['range', 'accuracy', 'coherence', 'interaction'];
export const CEFR_SOURCE = 'https://www.coe.int/en/web/common-european-framework-reference-languages/table-3-cefr-3.3-common-reference-levels-qualitative-aspects-of-spoken-language-use';
const session = value => typeof value === 'string' && /^\d{4}-\d{2}-\d{2}-\d{4}$/.test(value) &&
  Number.isFinite(Date.parse(value.slice(0, 10))) && new Date(value.slice(0, 10)).toISOString().slice(0, 10) === value.slice(0, 10);
const invalid = () => { throw new Error('Invalid CEFR estimate'); };
const text = (value, max) => {
  if (typeof value !== 'string' || !value.trim() || value.length > max || /https?:\/\/|<\/?[a-z]/i.test(value)) invalid();
  return value.trim();
};

export function insufficientCefr(latestSessionId, assessedOn, reason = 'There is not enough reliable evidence for a level estimate from this update.') {
  return { state: 'insufficient', latestSessionId, assessedOn, rationale: reason };
}

export function validateCefr(value) {
  if (!value || !['estimated', 'insufficient'].includes(value.state) || !session(value.latestSessionId) ||
      !session(value.assessedOn + '-0000') || value.latestSessionId.slice(0, 10) > value.assessedOn) invalid();
  const common = { state: value.state, latestSessionId: value.latestSessionId, assessedOn: value.assessedOn, rationale: text(value.rationale, 1000) };
  if (value.state === 'insufficient') return common;
  const low = CEFR_LEVELS.indexOf(value.lower), high = CEFR_LEVELS.indexOf(value.upper);
  if (low < 0 || high < low || high - low > 1 || !['low', 'moderate'].includes(value.confidence)) invalid();
  if (!Array.isArray(value.evidence) || value.evidence.length < 2 || value.evidence.length > 12) invalid();
  const evidence = value.evidence.map(ref => {
    if (!session(ref.sessionId) || ref.sessionId > value.latestSessionId || !/^\d{2}:[0-5]\d:[0-5]\d$/.test(ref.at)) invalid();
    return { sessionId: ref.sessionId, at: ref.at, quote: text(ref.quote, 300), note: text(ref.note, 500) };
  });
  if (new Set(evidence.map(ref => ref.sessionId + ':' + ref.at)).size !== evidence.length ||
      !evidence.some(ref => ref.sessionId === value.latestSessionId)) invalid();
  const sourceSessions = [...new Set(evidence.map(ref => ref.sessionId))].sort();
  if (!Array.isArray(value.aspects) || value.aspects.length !== CEFR_AREAS.length ||
      new Set(value.aspects.map(item => item.area)).size !== CEFR_AREAS.length) invalid();
  const aspects = value.aspects.map(item => {
    if (!CEFR_AREAS.includes(item.area)) invalid();
    return { area: item.area, detail: text(item.detail, 600) };
  });
  return { ...common, lower: value.lower, upper: value.upper,
    // Three evidenced sessions are a minimum for moderate confidence, not proof of it.
    confidence: sourceSessions.length < 3 ? 'low' : value.confidence, sourceSessions, evidence, aspects };
}

export function cefrOverview(record) {
  if (!record) return { state: 'pending' };
  const { state, latestSessionId, assessedOn, lower, upper, confidence, sourceSessions } = record;
  return { state, latestSessionId, assessedOn, ...(state === 'estimated' ? { lower, upper, confidence, sessionCount: sourceSessions.length } : {}) };
}

// Match brief quotations to actual learner turns, not teacher models or quiz scores.
export function groundCefr(value, latestSessionId, assessedOn, segments, learner, prior) {
  const record = validateCefr({ ...value, latestSessionId, assessedOn });
  if (record.state !== 'estimated') return record;
  const normalize = value => value.normalize('NFKC').replace(/\s+/g, ' ').trim();
  for (const ref of record.evidence) {
    if (ref.sessionId === latestSessionId) {
      if (!segments.some(s => s.speaker === learner && s.at === ref.at && normalize(s.text).includes(normalize(ref.quote)))) invalid();
    } else if (!prior?.evidence?.some(old => old.sessionId === ref.sessionId && old.at === ref.at && old.quote === ref.quote)) invalid();
  }
  return record;
}

export const CEFR_RULES = `Also return a separate cefr object for the administrator only. Never put CEFR levels in student-facing feedback, assessment, or quiz.
Estimate conversational English observable in the transcript against CEFR (Common European Framework of Reference for Languages) spoken-language descriptors.
Use this concise guide: A1: basic words and memorised patterns, simple exchanges with substantial help. A2: basic everyday sentences, frequent basic errors, simple linked responses. B1: connected accounts on familiar subjects, workable vocabulary, reasonably controlled common patterns. B2: clear descriptions and viewpoints, some complex forms, good grammatical control and sustained discussion. C1: broad flexible expression, consistently accurate complex language and well-organised contributions. C2: precise shades of meaning, highly flexible expression and consistently controlled complex discourse.
Assess range (words and structures), accuracy, coherence (connecting ideas), and interaction visible in exchanges. State when an area is not observable. This is not a comprehensive or certified CEFR level. Do not infer pronunciation, pace, spoken fluency, reading, writing, or an independent listening score from text.
Judge independent learner language, distinguishing teacher help, repeated models, rehearsed answers, and automatic transcription errors. Do not use quiz scores, lesson difficulty, first-try mistakes, or the A1-A2 reading style of our pages as evidence of a CEFR level.
Use the FULL new transcript plus only previously verified evidence in priorCefr. Old assessment summaries alone cannot establish a baseline level. Include successful language and limitations, and prefer a conservative adjacent range when uncertain. Do not upgrade or downgrade on one isolated error or advanced word. Do not claim a measured trend.
cefr: {state:"estimated",lower:"B1",upper:"B2",confidence:"low",rationale:"...",aspects:[{area:"range",detail:"..."},{area:"accuracy",detail:"..."},{area:"coherence",detail:"..."},{area:"interaction",detail:"..."}],evidence:[{sessionId,at,quote,note}]}.
The labels in this schema are examples, not a default level. lower and upper must be A1,A2,B1,B2,C1,C2, identical or adjacent and in that order. Confidence is low or moderate, never high; at least three evidenced sessions are needed for moderate.
Use 2-12 distinct timestamped brief exact learner quotations (max 300 characters each), including the new session; keep sufficient surrounding context in mind. Use newSessionId and actual learner timestamps. Older quotes must match priorCefr evidence exactly. Explain each quote's relevance; never include unrelated personal details or full names. Keep the latest lesson represented. Do not invent source counts or dates.
If independent language is too sparse, ambiguous, largely repeated, or too personal to quote safely, return cefr:{state:"insufficient",rationale:"..."} without a level. This does not prevent useful lesson feedback.`;
