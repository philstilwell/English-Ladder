const SESSION_ID = /^\d{4}-\d{2}-\d{2}-\d{4}$/;
function text(value, max = 1800) {
  if (typeof value !== 'string' || !value.trim() || value.length > max) throw new Error('Invalid text');
  return value.trim();
}
function list(value, convert, max = 12) {
  if (!Array.isArray(value) || !value.length || value.length > max) throw new Error('Invalid list');
  return value.map(convert);
}
function date(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value) || !Number.isFinite(Date.parse(value)) || new Date(value).toISOString().slice(0, 10) !== value) throw new Error('Invalid date');
  return value;
}

// Keep the assessment structured and private, with references to this student's
// existing session records. Content review still enforces the ESL-only scope.
export function validateAssessment(value) {
  if (!value || value.scope !== 'esl') throw new Error('Invalid assessment');
  const sourceSessions = list(value.sourceSessions, id => {
    if (typeof id !== 'string' || !SESSION_ID.test(id)) throw new Error('Invalid source session');
    return id;
  }, 100);
  if (new Set(sourceSessions).size !== sourceSessions.length) throw new Error('Duplicate sources');
  const reference = item => {
    if (!sourceSessions.includes(item.sessionId) || typeof item.at !== 'string' || !/^\d{2}:[0-5]\d:[0-5]\d$/.test(item.at)) throw new Error('Invalid evidence');
    return { sessionId: item.sessionId, at: item.at };
  };
  const assessedOn = date(value.assessedOn);
  if (sourceSessions.some(id => id.slice(0, 10) > assessedOn)) throw new Error('Source is later than assessment');
  return {
    scope: 'esl', assessedOn, sourceSessions,
    title: text(value.title, 120), summary: text(value.summary), mainPriority: text(value.mainPriority, 300),
    strengths: list(value.strengths, s => ({ title: text(s.title, 120), detail: text(s.detail), evidence: list(s.evidence, reference) })),
    progress: { detail: text(value.progress?.detail), evidence: list(value.progress?.evidence, reference) },
    patterns: list(value.patterns, p => ({
      title: text(p.title, 120), detail: text(p.detail), practice: text(p.practice),
      examples: list(p.examples, e => ({ ...reference(e), observed: text(e.observed), model: text(e.model) })),
    })),
    plan: list(value.plan, p => ({ title: text(p.title, 120), activity: text(p.activity), target: text(p.target) })),
    nextLesson: text(value.nextLesson),
  };
}

export function assessmentReferences(record) {
  return [...record.strengths.flatMap(s => s.evidence), ...record.progress.evidence, ...record.patterns.flatMap(p => p.examples)];
}
