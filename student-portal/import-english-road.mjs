// Import a reviewed snapshot from the owner's English Road checkout. No AI calls.
// Usage: node student-portal/import-english-road.mjs /path/to/EnglishRoad
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';

const root = resolve(process.argv[2] || ''), levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
assert(process.argv[2], 'Supply the existing English Road checkout path.');
execFileSync(process.execPath, [join(root, 'scripts/compile-editorial-bank.cjs'), '--check'], { cwd: root, stdio: 'inherit' });
const groups = readdirSync(join(root, 'editorial/items')).filter(f => f.endsWith('.json')).sort()
  .map(f => JSON.parse(readFileSync(join(root, 'editorial/items', f), 'utf8')));
const questions = groups.flatMap(group => group.items.map(q => {
  assert.equal(q.audit?.status, 'reviewed');
  assert(levels.includes(q.level));
  assert.equal(q.options.length, 4);
  assert.equal(new Set(q.options).size, 4);
  assert(q.options.includes(q.answer));
  for (const text of [q.setupText, q.taskText, q.explanation, ...q.options, ...q.options.map(o => q.rationales[o])]) assert(typeof text === 'string' && text.trim());
  return { id: q.id, band: q.level, topic: group.topic, category: group.category,
    setup: q.setupText, prompt: q.taskText, options: q.options, correctIndex: q.options.indexOf(q.answer),
    explanation: q.explanation, feedback: q.options.map(o => q.rationales[o]) };
}));
assert.equal(questions.length, 4200); assert.equal(new Set(questions.map(q => q.id)).size, 4200);
assert.equal(groups.length, 35);
for (const group of groups) for (const level of levels) assert.equal(questions.filter(q => q.topic === group.topic && q.band === level).length, 20);
const bank = { source: 'https://englishroad.com/practice.html',
  sourceCommit: execFileSync('git', ['rev-parse', 'HEAD'], { cwd: root, encoding: 'utf8' }).trim(),
  version: createHash('sha256').update(JSON.stringify(questions)).digest('hex'),
  levels, topics: groups.map(g => g.topic).sort(), questions };
writeFileSync(new URL('./english-road-bank.json', import.meta.url), JSON.stringify(bank) + '\n');
console.log(`Imported ${questions.length} reviewed questions across ${groups.length} topics. Version ${bank.version}.`);
