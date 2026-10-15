(() => {
  'use strict';
  const blanks = /⎛#([1-6])⎞/g;
  const node = (tag, text, className) => {
    const el = document.createElement(tag);
    if (text) el.textContent = text;
    if (className) el.className = className;
    return el;
  };
  function validItems(items) {
    if (!Array.isArray(items) || !items.length || items.length > 5000) return false;
    return items.every((item, index) => {
      if (!Number.isInteger(item?.number) || item.number < 1 || index && item.number <= items[index - 1].number ||
          typeof item.term !== 'string' || !item.term.trim() ||
          !Array.isArray(item.sentences) || item.sentences.length !== 3 || item.sentences.some(s => typeof s !== 'string' || !s.trim()) ||
          !Array.isArray(item.answers) || item.answers.length !== 6 || item.answers.some(s => typeof s !== 'string' || !s.trim()) ||
          !Array.isArray(item.options) || item.options.length !== 6 || item.options.some(s => typeof s !== 'string' || !s.trim())) return false;
      const ids = item.sentences.flatMap(s => [...s.matchAll(blanks)].map(match => match[1])).sort();
      const compare = values => values.map(s => s.toLowerCase()).sort().join('|');
      return ids.join() === '1,2,3,4,5,6' && compare(item.answers) === compare(item.options);
    });
  }
  function exercise(item) {
    const title = node('h4', `Item ${item.number} · “${item.term}”`, 'terms-heading'); title.tabIndex = -1;
    const wordHeading = node('p', 'Words to use', 'terms-label');
    const words = node('ul', '', 'terms-words'); words.setAttribute('aria-label', 'Six words in alphabetical order');
    for (const word of item.options) { const entry = node('li'); entry.append(node('q', word)); words.append(entry); }
    const hint = node('p', 'Use each word once. If a word is shown twice, use it twice.', 'field-hint');
    const sentences = node('ol', '', 'terms-sentences'); sentences.id = 'terms-sentences-' + item.number; sentences.setAttribute('aria-live', 'polite');
    function showAnswers(revealed) {
      sentences.replaceChildren(); sentences.classList.toggle('is-revealed', revealed);
      for (const sentence of item.sentences) {
        const quote = node('q');
        if (revealed) {
          let offset = 0;
          for (const match of sentence.matchAll(blanks)) {
            quote.append(sentence.slice(offset, match.index), node('span', item.answers[Number(match[1]) - 1], 'terms-answer'));
            offset = match.index + match[0].length;
          }
          quote.append(sentence.slice(offset));
        } else {
          quote.textContent = sentence.replace(blanks, (_, id) => `____ (${id})`);
        }
        const line = node('li'); line.append(quote); sentences.append(line);
      }
    }
    showAnswers(false);
    const reveal = node('label', '', 'terms-reveal');
    const checkbox = node('input'); checkbox.type = 'checkbox'; checkbox.autocomplete = 'off'; checkbox.setAttribute('aria-controls', sentences.id);
    checkbox.addEventListener('change', () => showAnswers(checkbox.checked));
    reveal.append(checkbox, node('span', 'Show answers'));
    const card = node('article', '', 'terms-item');
    card.append(title, wordHeading, words, hint, sentences, reveal);
    return { card, title };
  }
  window.BusinessTerms = {
    exercise, validItems,
    create({ root, api, expired }) {
      let revision = 0, active = false, items = [], position = 0, progress = new Map(), teacher = false, saving = false;
      let listOpen = false, listPage = 0;
      function clear() {
        revision++; active = false; items = []; position = 0; progress.clear(); saving = false; listOpen = false; listPage = 0;
        root.replaceChildren(); root.hidden = true; root.removeAttribute('aria-busy');
      }
      function render(focus = false) {
        const item = items[position];
        const intro = node('p', `${items.length.toLocaleString('en')} exercises. Later questions are harder. Start with an easy item and move on when you are ready.`, 'field-hint');
        const jump = node('form', '', 'terms-jump');
        const label = node('label', 'Go to item'); label.htmlFor = 'terms-number';
        const number = node('input'); number.id = 'terms-number'; number.type = 'number'; number.inputMode = 'numeric';
        number.min = '1'; number.max = String(items.at(-1).number); number.step = '1'; number.required = true;
        number.value = String(item.number); number.autocomplete = 'off'; number.setAttribute('aria-describedby', 'terms-jump-status');
        const go = node('button', 'Go', 'secondary-button'); go.type = 'submit';
        const status = node('p', '', 'field-hint'); status.id = 'terms-jump-status'; status.setAttribute('role', 'status');
        jump.append(label, number, go);
        jump.addEventListener('submit', event => {
          event.preventDefault();
          const next = items.findIndex(entry => entry.number === Number(number.value));
          if (next === -1) { status.textContent = 'This item is not available. Try another number.'; return; }
          position = next; render(true);
        });
        const { card, title } = exercise(item);
        const actions = node('div', '', 'terms-actions');
        const finished = node('button', 'Finished', 'secondary-button'); finished.type = 'button';
        const question = node('button', 'Questions', 'secondary-button'); question.type = 'button';
        const saved = node('p', '', 'field-hint'); saved.setAttribute('role', 'status'); saved.id = 'terms-save-status';
        const help = node('p', teacher ? 'Teacher view: you can see saved choices. Only the student can change them.' : 'Choose “Finished” when you are done. Choose “Questions” to ask your teacher about this item. Click a button again to undo it. These choices are saved.', 'field-hint');
        const questions = node('details', '', 'terms-questions'); questions.open = listOpen;
        questions.addEventListener('toggle', () => { listOpen = questions.open; });
        const summary = node('summary'), list = node('div'); questions.append(summary, list);
        function updateList() {
          const selected = items.filter(entry => progress.get(entry.number)?.question);
          summary.textContent = 'Questions list (' + selected.length + ')'; list.replaceChildren();
          if (!selected.length) { list.append(node('p', 'No questions yet. Use “Questions” on an item to add it here.', 'field-hint')); return; }
          listPage = Math.min(listPage, Math.floor((selected.length - 1) / 20));
          list.append(node('p', 'Open an item to talk about it with your teacher. After you talk, click “Questions” again to remove it.', 'field-hint'));
          const entries = node('ul', '', 'terms-question-links');
          for (const entry of selected.slice(listPage * 20, (listPage + 1) * 20)) {
            const row = node('li'), link = node('button', `Item ${entry.number} · “${entry.term}”` + (progress.get(entry.number)?.finished ? ' · Finished' : ''), 'secondary-button');
            link.type = 'button'; link.disabled = saving;
            link.addEventListener('click', () => { position = items.findIndex(i => i.number === entry.number); listOpen = false; render(true); });
            row.append(link); entries.append(row);
          }
          list.append(entries);
          if (selected.length > 20) {
            const paging = node('div', '', 'terms-controls');
            const back = node('button', 'Previous questions', 'secondary-button'), forward = node('button', 'More questions', 'secondary-button');
            back.type = forward.type = 'button'; back.disabled = saving || listPage === 0; forward.disabled = saving || (listPage + 1) * 20 >= selected.length;
            back.addEventListener('click', () => { listPage--; updateList(); }); forward.addEventListener('click', () => { listPage++; updateList(); });
            paging.append(back, node('span', `Page ${listPage + 1} of ${Math.ceil(selected.length / 20)}`), forward); list.append(paging);
          }
        }
        function updateStatus() {
          const entry = progress.get(item.number);
          card.classList.toggle('is-finished', Boolean(entry?.finished));
          finished.setAttribute('aria-pressed', String(Boolean(entry?.finished)));
          question.setAttribute('aria-pressed', String(Boolean(entry?.question)));
          finished.disabled = question.disabled = teacher || saving;
          saved.textContent = [entry?.finished ? 'Marked as finished.' : '', entry?.question ? 'In your Questions list.' : ''].filter(Boolean).join(' ');
          updateList();
        }
        async function save(field) {
          if (saving || teacher) return;
          const current = revision, entry = progress.get(item.number);
          const body = { number: item.number, field, value: !entry?.[field], revision: entry?.revision || 0 };
          saving = true;
          const controls = [...root.querySelectorAll('button, input[type=number]')].map(el => [el, el.disabled]);
          for (const [el] of controls) el.disabled = true;
          saved.textContent = 'Saving…';
          try {
            const data = await api('/api/business-terms/state', { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
            if (current !== revision) return;
            progress.set(item.number, data.entry); updateStatus();
          } catch (error) {
            if (current !== revision || expired(error)) return;
            if (error.status === 409) {
              try {
                const data = await api('/api/business-terms/state');
                if (current !== revision) return;
                readProgress(data); updateStatus();
              } catch (reloadError) {
                if (current !== revision || expired(reloadError)) return;
                saved.textContent = 'Your choices could not reload. Leave this activity and open it again.';
                return;
              }
            }
            saved.textContent = error.status === 409 ? error.message : 'Your change could not be saved. Please try again.';
          } finally {
            if (current === revision) {
              saving = false;
              for (const [el, disabled] of controls) el.disabled = disabled;
              finished.disabled = question.disabled = teacher;
              updateList();
            }
          }
        }
        finished.addEventListener('click', () => save('finished')); question.addEventListener('click', () => save('question'));
        actions.append(finished, question); card.append(actions, help, saved); updateStatus();
        const controls = node('div', '', 'terms-controls');
        const previous = node('button', 'Previous', 'secondary-button'); previous.type = 'button'; previous.disabled = position === 0;
        const next = node('button', 'Next', 'secondary-button'); next.type = 'button'; next.disabled = position === items.length - 1;
        previous.addEventListener('click', () => { if (position > 0) { position--; render(true); } });
        next.addEventListener('click', () => { if (position < items.length - 1) { position++; render(true); } });
        controls.append(previous, next);
        root.replaceChildren(intro, questions, jump, status, card, controls);
        if (focus) { title.focus(); title.scrollIntoView?.({ block: 'start' }); }
      }
      function readProgress(data) {
        if (!Array.isArray(data.entries) || data.entries.some(entry => !Number.isInteger(entry.number) || typeof entry.finished !== 'boolean' || typeof entry.question !== 'boolean' || !Number.isSafeInteger(entry.revision) || entry.revision < 0)) throw new Error('Invalid saved choices');
        progress = new Map(data.entries.map(entry => [entry.number, entry]));
      }
      async function open(teacherView = false) {
        if (active) return;
        active = true; teacher = teacherView; const current = ++revision;
        root.hidden = false; root.setAttribute('aria-busy', 'true');
        const loading = node('p', 'Loading business terms…'); loading.setAttribute('role', 'status'); root.replaceChildren(loading);
        try {
          const [data, state] = await Promise.all([api('/api/business-terms'), api('/api/business-terms/state')]);
          if (current !== revision) return;
          if (!validItems(data.items)) throw new Error('Incomplete practice content');
          readProgress(state); items = data.items; position = 0; root.removeAttribute('aria-busy'); render();
        } catch (error) {
          if (current !== revision || expired(error)) return;
          root.removeAttribute('aria-busy');
          const message = node('p', 'Business terms could not load. Please try again.'); message.setAttribute('role', 'alert');
          const retry = node('button', 'Try again', 'secondary-button'); retry.type = 'button';
          retry.addEventListener('click', () => { active = false; open(teacher); }); root.replaceChildren(message, retry);
        }
      }
      return { open, clear };
    },
  };
})();
