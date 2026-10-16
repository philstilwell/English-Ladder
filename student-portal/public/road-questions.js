// Private saved questions. This controller never submits practice answers.
(() => {
  'use strict';
  const node = (tag, text, className) => {
    const el = document.createElement(tag); if (text != null) el.textContent = text;
    if (className) el.className = className; return el;
  };
  function review(item) {
    const box = node('article', null, 'road-review'), q = item.exercise;
    box.append(node('h3', item.band + ' · ' + item.topic + ' · Question ' + (item.questionIndex + 1)),
      node('p', 'Practice set: ' + new Date(item.startedAt).toLocaleString(), 'field-note'),
      node('p', q.setup), node('p', '“' + q.prompt + '”', 'road-prompt'));
    const choices = node('ul'); q.options.forEach(option => choices.append(node('li', '“' + option + '”'))); box.append(choices);
    if (item.answer && Number.isInteger(q.correctIndex)) {
      box.append(node('p', 'Saved answer: “' + q.options[item.answer.choiceIndex] + '”'));
      const details = node('details'); details.append(node('summary', 'Show answer and explanation'),
        node('p', 'Correct answer: “' + q.options[q.correctIndex] + '”'), node('p', q.explanation)); box.append(details);
    } else box.append(node('p', 'No answer saved for this question.', 'field-note'));
    let exercise = 'English practice exercise:\n' + q.setup + '\n“' + q.prompt + '”\nChoices:\n' + q.options.map(option => '• “' + option + '”').join('\n');
    if (Number.isInteger(q.correctIndex)) exercise += '\nAnswer key: “' + q.options[q.correctIndex] + '”\nExercise explanation: ' + q.explanation;
    const ai = window.PracticePrompt.create({ prompt: window.PracticePrompt.text(exercise, 'Explain the grammar or vocabulary step by step.') });
    box.append(ai.controls, ai.status); return box;
  }
  window.RoadQuestions = { review, create({ api, expired }) {
    let epoch = 0, choices = new Map(), views = new Set();
    function clear() { epoch++; choices.clear(); views.clear(); }
    function remember(progress) {
      if (!choices.has(progress.id) || choices.get(progress.id).revision <= progress.revision) choices.set(progress.id, progress);
    }
    function toggle(item) {
      remember(item.progress);
      const version = epoch, box = node('div', null, 'grammar-actions'), button = node('button', '', 'secondary-button question-button'), status = node('span', '', 'save-message');
      button.type = 'button'; status.setAttribute('role', 'status');
      let saving = false, pending = null, needsReload = false;
      const valid = () => version === epoch;
      function paint() {
        const progress = choices.get(item.progress.id); if (!progress) return;
        button.textContent = progress.question ? 'Saved to Questions' : 'Questions';
        button.setAttribute('aria-pressed', String(progress.question)); button.classList.toggle('is-selected', progress.question); button.disabled = saving;
      }
      const view = { box, paint }; views.add(view);
      function refreshButtons() { for (const entry of views) { if (entry.box.isConnected) entry.paint(); else views.delete(entry); } }
      async function save() {
        if (saving || !valid()) return;
        saving = true; status.textContent = needsReload ? 'Loading saved choice…' : 'Saving…'; paint();
        try {
          if (needsReload) {
            const data = await api('/api/road/questions?id=' + encodeURIComponent(item.progress.id));
            if (!valid()) return; remember(data.entry); needsReload = false;
            status.textContent = 'Saved choice loaded. Check it, then choose again.';
          } else {
            const progress = choices.get(item.progress.id);
            pending ||= { attemptId: item.attemptId, questionIndex: item.questionIndex, value: !progress.question, revision: progress.revision };
            const data = await api('/api/road/questions', { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(pending) });
            if (!valid()) return; remember(data.entry); pending = null;
            status.textContent = data.entry.question ? 'Saved.' : 'Removed from Questions.';
          }
        } catch (error) {
          if (!valid() || expired(error)) return;
          if (error.status === 409) { pending = null; needsReload = true; }
          status.textContent = error.message + (needsReload ? ' Select the button to load the saved choice.' : ' Select the button to try saving again.');
        } finally { if (valid()) { saving = false; paint(); refreshButtons(); } }
      }
      button.addEventListener('click', save); box.append(button, status); paint(); return box;
    }
    function list(root, teacher) {
      const version = epoch; let request = 0;
      const valid = n => version === epoch && request === n && root.isConnected;
      async function load(pages = [null]) {
        const n = ++request; root.replaceChildren(node('p', 'Loading saved Questions…'));
        try {
          const data = await api('/api/road/questions' + (pages.at(-1) ? '?after=' + encodeURIComponent(pages.at(-1)) : ''));
          if (!valid(n)) return;
          root.replaceChildren(node('h3', 'Saved Questions'));
          root.append(node('p', 'Keep questions here to discuss with your teacher. Removing one keeps your saved answer.', 'field-note'));
          if (!data.questions.length) root.append(node('p', 'No saved questions on this page.'));
          for (const item of data.questions) {
            const card = review(item); if (!teacher) card.append(toggle(item)); root.append(card);
          }
          const controls = node('div', null, 'terms-controls');
          function control(text, action) { const b = node('button', text, 'secondary-button'); b.type = 'button'; b.addEventListener('click', action); controls.append(b); }
          control('Refresh Questions', () => load());
          if (pages.length > 1) control('Previous questions', () => load(pages.slice(0, -1)));
          if (data.nextCursor) control('More questions', () => load([...pages, data.nextCursor]));
          root.append(controls);
        } catch (error) {
          if (!valid(n) || expired(error)) return;
          const retry = node('button', 'Try loading Questions again', 'secondary-button'); retry.type = 'button'; retry.addEventListener('click', () => load(pages));
          root.replaceChildren(node('p', error.message, 'error-message'), retry);
        }
      }
      void load();
    }
    return { clear, toggle, list };
  } };
})();
