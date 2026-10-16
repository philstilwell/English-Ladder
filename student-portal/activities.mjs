import { COMMUNICATION_ACTIVITIES } from './communication-practice.mjs';
// These tools are selected by default for new students. Administrator choices
// control menu visibility only; they never grant access or change learning data.
export const ACTIVITY_TOOLS = Object.freeze([
  { id: 'english-road', name: 'English Road Practice', description: 'Practice grammar and words. Choose a topic and a practice band. Your answers are saved in your account.',
    benefit: 'Build your grammar and word skills. Find out why an answer is right and learn from mistakes.',
    steps: ['Choose a topic and a practice band, such as A2 or B1. The band sets the difficulty.',
      'Choose an answer for each question. Read the explanation after you answer.',
      'Review your answers. Your work is saved, so you can stop and come back later.',
      'Choose “Questions” to save an exercise to discuss with your teacher. Open “Saved Questions” to see your list.'] },
  { id: 'grammar-practice', name: 'Grammar practice', description: 'Read each item. Think of an answer. Check “Show answer” to see the full sentence in blue. Uncheck it to try again. Save finished items and questions to discuss with your teacher.',
    benefit: 'Learn how words fit together in a sentence. Check your own ideas and notice useful grammar patterns.',
    steps: ['Work through a group of ten items. Think of an answer before you check it.',
      'Choose “Show answer” to see the full sentence in blue. Uncheck it to try again.',
      'Choose “Finish” when you are ready. Choose “Questions” to save an item to discuss with your teacher.'] },
  { id: 'business-terms', name: 'Business terms', description: 'Use the six choices to complete the three sentences. Check “Show answers” to fill the blanks. The answers appear in blue. Save finished items and questions to discuss with your teacher.',
    benefit: 'Learn words and phrases for work. See how they are used in complete sentences.',
    steps: ['Read the three sentences. Use the six choices to fill the numbered blanks.',
      'Choose “Show answers” to check all six answers in blue. Uncheck it to try again. Later items are harder.',
      'Choose “Finish” when you are ready, or “Questions” to save an item to discuss with your teacher.'] },
  { id: 'vocabulary-practice', name: 'Vocabulary practice', description: 'Work on ten words. Save your answers. Copy the batch prompt and paste it into an AI chat to check your work.',
    benefit: 'Learn new words and use them in your own sentences. Get feedback on your answers from an AI chat.',
    steps: ['Choose one batch of ten words. Read each meaning and example. There are 50 words to start with.',
      'Answer the short exercise for each word. Write your own sentence, then choose “Save batch”.',
      'Choose “Copy AI prompt”. It includes the ten words and your answers. Open an AI chat, paste the prompt, and send it to check your work.',
      'Read the feedback. Use “Practice again” for words to review, or “Questions” for help from your teacher.'] },
  ...COMMUNICATION_ACTIVITIES.map(({id,name,description})=>({id,name,description,
    benefit: description,
    steps: ['Choose a topic set. Read the situation and the question.',
      'Choose an answer. Read the explanation. You can try again.',
      'Choose “Finish” when you are ready. Choose “Questions” to save an item to discuss with your teacher.'],
  })),
]);
export const visibleActivities = record => Array.isArray(record.visibleActivities)
  ? ACTIVITY_TOOLS.filter(tool => record.visibleActivities.includes(tool.id)).map(tool => tool.id)
  : ['english-road', 'grammar-practice', 'business-terms'];

export function validateActivities(value) {
  if (!Array.isArray(value) || value.length > ACTIVITY_TOOLS.length || new Set(value).size !== value.length ||
      value.some(id => !ACTIVITY_TOOLS.some(tool => tool.id === id))) throw new Error('Please choose from the activities shown.');
  return ACTIVITY_TOOLS.filter(tool => value.includes(tool.id)).map(tool => tool.id);
}
