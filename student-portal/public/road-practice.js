// Account-backed English Road practice. Never store learner answers in the browser.
(() => {
  'use strict';
  window.EnglishRoadPractice = {
    create({ root, api, expired }) {
      let epoch = 0, mounted = false, teacher = false, busy = false, catalog = null, attempt = null;
      let viewing = null, pending = null, error = '', conflict = false, questionsOnly = false;
      const questions = window.RoadQuestions.create({ api, expired });
      const node = (tag, text, className) => {
        const el = document.createElement(tag); if (text != null) el.textContent = text;
        if (className) el.className = className; return el;
      };
      const button = (text, action, className = 'secondary-button') => {
        const el = node('button', text, className); el.type = 'button'; el.disabled = busy;
        el.addEventListener('click', action); return el;
      };
      function clear() {
        epoch++; questions.clear(); mounted = false; busy = false; catalog = null; attempt = null; viewing = null;
        pending = null; error = ''; conflict = false; root.replaceChildren(); root.hidden = true;
      }
      function focusQuestion() { root.querySelector('#road-question-title, #road-summary-title')?.focus(); }
      async function load() {
        if (busy) return;
        const version = ++epoch; busy = true; pending = null; error = ''; conflict = false; render();
        try {
          const data = await api('/api/road/state');
          if (!mounted || version !== epoch) return;
          catalog = data.catalog; attempt = data.attempt; viewing = null;
        } catch (e) {
          if (!mounted || version !== epoch || expired(e)) return;
          error = e.message;
        } finally { if (mounted && version === epoch) { busy = false; render(); } }
      }
      async function send(path, body) {
        if (busy || !mounted || teacher) return;
        const version = ++epoch; pending = { path, body }; busy = true; error = ''; conflict = false; render();
        try {
          const data = await api('/api/road/' + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
          if (!mounted || version !== epoch) return;
          attempt = data.attempt; pending = null;
          viewing = path === 'answer' ? body.questionIndex : null;
        } catch (e) {
          if (!mounted || version !== epoch || expired(e)) return;
          error = e.message;
          if (e.status === 409) { pending = null; conflict = true; }
        } finally { if (mounted && version === epoch) { busy = false; render(); focusQuestion(); } }
      }
      function questionButton(question, index) {
        return questions.toggle({ attemptId: attempt.id, questionIndex: index, progress: question.progress || { id: attempt.id + '_' + String(index).padStart(2, '0'), question: false, revision: 0 } });
      }
      function reviewQuestion(question, answer, index) {
        const box = node('div', null, 'road-review');
        box.append(node('p', question.setup), node('p', '“' + question.prompt + '”', 'road-prompt'));
        box.append(node('p', 'Your answer: “' + question.options[answer.choiceIndex] + '”'));
        box.append(node('p', (answer.choiceIndex === question.correctIndex ? 'Correct. ' : 'Correct answer: “' + question.options[question.correctIndex] + '”. ') + question.explanation));
        if (answer.choiceIndex !== question.correctIndex) box.append(node('p', question.feedback[answer.choiceIndex]));
        box.append(questionButton(question, index), promptControls(question));
        return box;
      }
      function promptControls(question) {
        // Copy only exercise wording and any answer key already released by the server.
        let exercise = 'English practice exercise:\n' + question.setup + '\n“' + question.prompt + '”\nChoices:\n' +
          question.options.map(option => '• “' + option + '”').join('\n');
        if (Number.isInteger(question.correctIndex)) exercise += '\nAnswer key: “' + question.options[question.correctIndex] + '”\nExercise explanation: ' + question.explanation;
        const ai = window.PracticePrompt.create({ prompt: window.PracticePrompt.text(exercise,
          'Choose the best answer and explain the grammar or vocabulary step by step. Explain why the other choices do not fit, or when they could fit a different sentence.') });
        ai.button.disabled = busy;
        const controls = node('div', null, 'practice-prompt-controls'); controls.append(ai.controls, ai.status); return controls;
      }
      function setup() {
        if (!catalog) return;
        const form = node('form', null, 'road-setup'), fields = node('fieldset');
        fields.disabled = busy || Boolean(pending) || conflict;
        fields.append(node('legend', 'Start a practice set'));
        const bandLabel = node('label', 'Practice band'), band = node('select'); band.id = 'road-band'; bandLabel.htmlFor = band.id;
        for (const value of catalog.levels) { const option = node('option', value); option.value = value; band.append(option); }
        band.value = (pending?.path === 'start' ? pending.body.band : attempt?.band) || 'A2';
        const topicLabel = node('label', 'Topic'), topic = node('select'); topic.id = 'road-topic'; topicLabel.htmlFor = topic.id;
        const all = node('option', 'All topics · 25 questions'); all.value = ''; topic.append(all);
        for (const value of catalog.topics) { const option = node('option', value); option.value = value; topic.append(option); }
        topic.value = (pending?.path === 'start' ? pending.body.topic : attempt?.topic) || '';
        fields.append(bandLabel, band, topicLabel, topic, node('p', 'A topic set has 20 questions. You can stop and come back later.', 'field-note'));
        const start = node('button', 'Start practice', 'primary-button'); start.type = 'submit'; fields.append(start); form.append(fields);
        form.addEventListener('submit', event => {
          event.preventDefault();
          if (!busy && !pending && !conflict) send('start', { attemptId: crypto.randomUUID(), previousAttemptId: attempt?.id || null, band: band.value, topic: topic.value });
        });
        root.append(form);
      }
      function render() {
        root.replaceChildren(); root.hidden = !mounted;
        if (!mounted) return;
        const link = node('a', questionsOnly ? 'Back to practice' : 'Saved Questions', 'activity-questions-link');
        link.href = '#activities/english-road' + (questionsOnly ? '' : '/questions'); root.append(link);
        if (questionsOnly) {
          const list = node('div', null, 'road-questions'); root.append(list); questions.list(list, teacher); return;
        }
        if (teacher) {
          root.append(node('p', 'Teacher view does not save student practice. Open this student’s account on your administrator page to review English Road results.'));
          return;
        }
        root.append(node('p', 'A1–C2 are practice bands. This quiz does not measure your overall English level.', 'field-note'));
        const status = node('p', busy ? 'Saving or loading…' : pending ? 'Not saved yet. Try again before you continue.' : error ? 'Load saved progress to check your answers.' : 'Your submitted answers are saved in your account. Your teacher can review them.', 'save-message');
        status.setAttribute('role', 'status'); root.append(status);
        if (error) {
          const message = node('p', error, 'error-message'); message.setAttribute('role', 'alert'); root.append(message);
          if (pending) root.append(button('Try saving again', () => send(pending.path, pending.body)));
        }
        root.append(button('Load saved progress', load));
        if (!attempt) { setup(); return; }
        const index = viewing ?? attempt.answers.length;
        root.append(node('p', attempt.band + ' · ' + (attempt.topic || 'All topics'), 'eyebrow'));
        if ((attempt.completedAt || attempt.endedAt) && viewing === null) {
          const title = node('h4', attempt.completedAt ? 'Practice complete' : 'Practice ended'); title.id = 'road-summary-title'; title.tabIndex = -1;
          root.append(title, node('p', attempt.correct + ' correct out of ' + attempt.answered + ' answered.'));
          if (attempt.endedAt) root.append(node('p', 'You answered ' + attempt.answered + ' of ' + attempt.total + ' questions.'));
          if (attempt.answers.length) {
            const details = node('details'); details.append(node('summary', 'Review your answers'));
            attempt.answers.forEach((a, i) => details.append(reviewQuestion(attempt.questions[i], a, i))); root.append(details);
          }
          setup(); return;
        }
        const question = attempt.questions[index]; if (!question) return;
        const heading = node('h4', 'Question ' + (index + 1) + ' of ' + attempt.total); heading.id = 'road-question-title'; heading.tabIndex = -1;
        const progress = node('progress'); progress.max = attempt.total; progress.value = attempt.answered; progress.setAttribute('aria-label', 'Questions answered');
        root.append(heading, progress, node('p', question.setup), node('p', '“' + question.prompt + '”', 'road-prompt'));
        const answer = attempt.answers[index];
        if (answer) {
          const feedback = node('div', null, 'road-answer'); feedback.setAttribute('role', 'status');
          feedback.append(node('strong', answer.choiceIndex === question.correctIndex ? 'Correct.' : 'Not this time.'));
          feedback.append(node('p', 'Your answer: “' + question.options[answer.choiceIndex] + '”'));
          if (answer.choiceIndex !== question.correctIndex) feedback.append(node('p', question.feedback[answer.choiceIndex]));
          feedback.append(node('p', 'Correct answer: “' + question.options[question.correctIndex] + '”'), node('p', question.explanation));
          root.append(feedback, button(attempt.completedAt ? 'See results' : 'Next question', () => { viewing = null; render(); focusQuestion(); }, 'primary-button'));
        } else {
          const form = node('form'), fields = node('fieldset'); fields.className = 'road-options';
          fields.disabled = busy || Boolean(pending) || conflict; fields.append(node('legend', 'Choose one answer. Then select Check answer.'));
          const check = node('button', 'Check answer', 'primary-button'); check.type = 'submit'; check.disabled = true;
          question.options.forEach((text, choiceIndex) => {
            const label = node('label'), radio = node('input'); radio.type = 'radio'; radio.name = 'road-choice'; radio.value = String(choiceIndex); radio.required = true;
            radio.checked = pending?.path === 'answer' && pending.body.questionIndex === index && pending.body.choiceIndex === choiceIndex;
            radio.addEventListener('change', () => { check.disabled = false; }); label.append(radio, node('span', text)); fields.append(label);
          });
          fields.append(check); form.append(fields); root.append(form);
          form.addEventListener('submit', event => {
            event.preventDefault(); const choice = form.querySelector('input:checked');
            if (choice && !busy && !pending && !conflict) send('answer', { attemptId: attempt.id, questionIndex: index, choiceIndex: Number(choice.value) });
          });
        }
        root.append(questionButton(question, index), promptControls(question));
        if (!attempt.completedAt && !attempt.endedAt && !pending && !conflict) root.append(button('End this set', () => {
          if (window.confirm('End this set? Your saved answers will stay in your account. You can then start a new set.')) send('end', { attemptId: attempt.id, revision: attempt.revision });
        }));
      }
      return { clear, open(isTeacher, showQuestions = false) { if (mounted && teacher === isTeacher && questionsOnly === showQuestions) return; clear(); mounted = true; teacher = isTeacher; questionsOnly = showQuestions; render(); if (!teacher && !questionsOnly) load(); } };
    },
  };
})();
