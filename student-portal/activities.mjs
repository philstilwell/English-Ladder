// Keep dummy entries until the owner supplies their replacements. Settings
// control menu visibility only; they never grant access or change learning data.
export const ACTIVITY_TOOLS = Object.freeze([
  { id: 'english-road', name: 'English Road Practice', description: 'Practice grammar and words. Choose a topic and a practice band. Your answers are saved in your account.' },
  { id: 'grammar-practice', name: 'Grammar practice', description: 'Read each item. Think of an answer. Check “Show answer” to see the full sentence in blue. Uncheck it to try again. Your practice is not saved.' },
  { id: 'placeholder-1', name: 'Activity 1', description: 'A sample activity. The real activity will be added later.' },
  { id: 'placeholder-2', name: 'Activity 2', description: 'A sample activity. The real activity will be added later.' },
  { id: 'placeholder-3', name: 'Activity 3', description: 'A sample activity. The real activity will be added later.' },
]);
export const visibleActivities = record => Array.isArray(record.visibleActivities)
  ? ACTIVITY_TOOLS.filter(tool => record.visibleActivities.includes(tool.id)).map(tool => tool.id)
  : ACTIVITY_TOOLS.map(tool => tool.id);

export function validateActivities(value) {
  if (!Array.isArray(value) || value.length > ACTIVITY_TOOLS.length || new Set(value).size !== value.length ||
      value.some(id => !ACTIVITY_TOOLS.some(tool => tool.id === id))) throw new Error('Please choose from the activities shown.');
  return ACTIVITY_TOOLS.filter(tool => value.includes(tool.id)).map(tool => tool.id);
}
