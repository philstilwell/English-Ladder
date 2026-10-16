// These tools are selected by default for new students. Administrator choices
// control menu visibility only; they never grant access or change learning data.
export const ACTIVITY_TOOLS = Object.freeze([
  { id: 'english-road', name: 'English Road Practice', description: 'Practice grammar and words. Choose a topic and a practice band. Your answers are saved in your account.' },
  { id: 'grammar-practice', name: 'Grammar practice', description: 'Read each item. Think of an answer. Check “Show answer” to see the full sentence in blue. Uncheck it to try again. Save finished items and questions to discuss with your teacher.' },
  { id: 'business-terms', name: 'Business terms', description: 'Use the six choices to complete the three sentences. Check “Show answers” to fill the blanks. The answers appear in blue. Save finished items and questions to discuss with your teacher.' },
  { id: 'vocabulary-practice', name: 'Vocabulary practice', description: 'Work on ten words. Save your answers. Copy the batch prompt and paste it into an AI chat to check your work.' },
]);
export const visibleActivities = record => Array.isArray(record.visibleActivities)
  ? ACTIVITY_TOOLS.filter(tool => record.visibleActivities.includes(tool.id)).map(tool => tool.id)
  : ['english-road', 'grammar-practice', 'business-terms'];

export function validateActivities(value) {
  if (!Array.isArray(value) || value.length > ACTIVITY_TOOLS.length || new Set(value).size !== value.length ||
      value.some(id => !ACTIVITY_TOOLS.some(tool => tool.id === id))) throw new Error('Please choose from the activities shown.');
  return ACTIVITY_TOOLS.filter(tool => value.includes(tool.id)).map(tool => tool.id);
}
