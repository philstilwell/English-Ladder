// Replace this catalog when the owner supplies the real activities. Settings
// control menu visibility only; they never grant access or change learning data.
export const ACTIVITY_TOOLS = Object.freeze([
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
