// Administrator-selected public study links. These choices control the student
// page, not access to the independent external websites.
export const RESOURCE_TOOLS = Object.freeze([
  {
    "id": "british-council-listening",
    "name": "British Council: A1 listening",
    "group": "listening",
    "groupName": "Listening"
  },
  {
    "id": "elllo",
    "name": "ELLLO",
    "group": "listening",
    "groupName": "Listening"
  },
  {
    "id": "randall-listening",
    "name": "Randall’s Listening Lab",
    "group": "listening",
    "groupName": "Listening"
  },
  {
    "id": "spotlight",
    "name": "Spotlight English",
    "group": "listening",
    "groupName": "Listening"
  },
  {
    "id": "british-council-speaking",
    "name": "British Council: A1 speaking",
    "group": "speaking",
    "groupName": "Speaking"
  },
  {
    "id": "esl-fast",
    "name": "ESL Fast: Easy Conversations",
    "group": "speaking",
    "groupName": "Speaking"
  },
  {
    "id": "youglish",
    "name": "YouGlish",
    "group": "speaking",
    "groupName": "Speaking"
  },
  {
    "id": "news-in-levels",
    "name": "News in Levels",
    "group": "reading",
    "groupName": "Reading and news"
  },
  {
    "id": "breaking-news-english",
    "name": "Breaking News English",
    "group": "reading",
    "groupName": "Reading and news"
  },
  {
    "id": "british-council-grammar",
    "name": "British Council: A1–A2 grammar",
    "group": "grammar",
    "groupName": "Grammar and words"
  },
  {
    "id": "cambridge-activities",
    "name": "Cambridge English activities",
    "group": "grammar",
    "groupName": "Grammar and words"
  },
  {
    "id": "manythings",
    "name": "ManyThings: Sentences with Audio",
    "group": "grammar",
    "groupName": "Grammar and words"
  },
  {
    "id": "write-and-improve",
    "name": "Cambridge Write & Improve",
    "group": "writing",
    "groupName": "Writing and work"
  },
  {
    "id": "british-council-emails",
    "name": "British Council: English for emails",
    "group": "writing",
    "groupName": "Writing and work"
  },
  {
    "id": "punctuation-guide",
    "name": "The Punctuation Guide",
    "group": "writing",
    "groupName": "Writing and work"
  }
]);

export const visibleResources = record => Array.isArray(record.visibleResources)
  ? RESOURCE_TOOLS.filter(resource => record.visibleResources.includes(resource.id)).map(resource => resource.id)
  : RESOURCE_TOOLS.map(resource => resource.id);

export function validateResources(value) {
  if (!Array.isArray(value) || value.length > RESOURCE_TOOLS.length || new Set(value).size !== value.length ||
      value.some(id => !RESOURCE_TOOLS.some(resource => resource.id === id))) throw new Error('Please choose from the resources shown.');
  return RESOURCE_TOOLS.filter(resource => value.includes(resource.id)).map(resource => resource.id);
}
