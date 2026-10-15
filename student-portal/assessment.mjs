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

function sessionIds(value) {
  const ids = list(value, id => {
    if (typeof id !== 'string' || !SESSION_ID.test(id)) throw new Error('Invalid source session');
    return id;
  }, 100);
  if (new Set(ids).size !== ids.length) throw new Error('Duplicate sources');
  return ids;
}

function validateQuiz(value, patternCount) {
  const sourceSessions = value?.sourceSessions === undefined ? undefined : sessionIds(value.sourceSessions);
  const patternTitles = value?.patternTitles === undefined ? undefined : list(value.patternTitles, title => text(title, 120));
  if (value?.generatedForSession !== undefined && !sourceSessions?.includes(value.generatedForSession)) throw new Error('Invalid quiz session');
  return {
    title: text(value?.title, 120), instructions: text(value?.instructions, 300),
    ...(sourceSessions ? { sourceSessions } : {}),
    ...(patternTitles ? { patternTitles } : {}),
    ...(value?.generatedForSession === undefined ? {} : { generatedForSession: value.generatedForSession }),
    questions: list(value?.questions, question => {
      if (!Number.isInteger(question.patternIndex) || question.patternIndex < 0 || question.patternIndex >= (patternTitles?.length || patternCount)) throw new Error('Invalid quiz source');
      const options = list(question.options, option => ({ text: text(option.text, 250), feedback: text(option.feedback, 400) }), 4);
      if (options.length < 2 || new Set(options.map(option => option.text.toLowerCase())).size !== options.length) throw new Error('Invalid quiz choices');
      if (!Number.isInteger(question.correctIndex) || question.correctIndex < 0 || question.correctIndex >= options.length) throw new Error('Invalid quiz answer');
      return {
        patternIndex: question.patternIndex, prompt: text(question.prompt, 300), options,
        correctIndex: question.correctIndex, model: text(question.model, 300),
      };
    }, 10),
  };
}

// Keep the assessment structured and private, with references to this student's
// existing session records. Content review still enforces the ESL-only scope.
export function validateAssessment(value) {
  if (!value || value.scope !== 'esl') throw new Error('Invalid assessment');
  const sourceSessions = sessionIds(value.sourceSessions);
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
    plan: list(value.plan, p => ({ title: text(p.title, 120), activity: text(p.activity), target: text(p.target),
      ...(p.aiPrompt === undefined ? {} : { aiPrompt: text(p.aiPrompt) }) })),
    nextLesson: text(value.nextLesson),
    ...(value.quiz === undefined ? {} : { quiz: validateQuiz(value.quiz, value.patterns.length) }),
  };
}

export function assessmentReferences(record) {
  return [...record.strengths.flatMap(s => s.evidence), ...record.progress.evidence, ...record.patterns.flatMap(p => p.examples)];
}
