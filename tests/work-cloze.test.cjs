const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'efsp-ai-development.html'), 'utf8');
const script = fs.readFileSync(path.join(root, 'work.js'), 'utf8');

test('extended conversation checks missing, wrong, and correct answers without saving them', () => {
  const dom = new JSDOM(html, {url:'https://englishladder.com/efsp-ai-development.html', runScripts:'outside-only'});
  const w = dom.window;
  try {
    w.Storage.prototype.setItem = () => assert.fail('No learner state may be saved.');
    w.eval(script);
    const activity = w.document.querySelector('[data-work-cloze]');
    const gaps = [...activity.querySelectorAll('[data-cloze-gap]')];
    const answers = JSON.parse(activity.querySelector('[data-cloze-answers]').textContent);
    const check = activity.querySelector('[data-check-cloze]');
    const status = activity.querySelector('[data-cloze-status]');
    check.click();
    assert.match(status.textContent, /0 of 10 correct. 10 unanswered/);
    assert.equal(gaps[0].getAttribute('aria-invalid'), 'true');
    gaps.forEach((gap, i) => { gap.value = answers[(i + 1) % answers.length].answer; });
    check.click();
    assert.match(status.textContent, /0 of 10 correct/);
    assert.equal(activity.querySelector('[data-cloze-feedback]').hidden, false);
    assert.match(activity.querySelector('[data-cloze-feedback]').textContent, /Review:/);
    gaps.forEach((gap, i) => { gap.value = answers[i].answer; gap.dispatchEvent(new w.Event('change')); });
    assert.equal(status.textContent, '');
    check.click();
    assert.match(status.textContent, /10 of 10 correct/);
    assert.equal(status.dataset.result, 'correct');
    assert.ok(gaps.every(gap => gap.getAttribute('aria-invalid') === 'false'));
    activity.querySelector('.work-answer').open = true;
    activity.querySelector('[data-reset-cloze]').click();
    assert.ok(gaps.every(gap => gap.value === '' && !gap.hasAttribute('aria-invalid')));
    assert.equal(status.textContent, '');
    assert.equal(activity.querySelector('.work-answer').open, false);
    assert.equal(w.document.activeElement, gaps[0]);
    assert.equal(w.localStorage.length, 0);
    assert.equal(w.sessionStorage.length, 0);
  } finally { w.close(); }
});

test('all cloze keys and completed dialogues remain available without JavaScript', () => {
  const dom = new JSDOM(html);
  try {
    const activities = [...dom.window.document.querySelectorAll('[data-work-cloze]')];
    assert.equal(activities.length, 11);
    for (const activity of activities) {
      assert.equal(activity.querySelector('.work-cloze-actions').hidden, true);
      assert.ok(activity.querySelector('.work-word-bank').textContent.length > 30);
      assert.equal(activity.querySelectorAll('.work-completed-script li').length, 20);
      const answers = JSON.parse(activity.querySelector('[data-cloze-answers]').textContent);
      assert.equal(activity.querySelectorAll('.work-answer li').length, answers.length);
      assert.equal(activity.querySelector('.work-answer').open, false);
    }
  } finally { dom.window.close(); }
});
