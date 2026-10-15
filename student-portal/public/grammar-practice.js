(() => {
  'use strict';
  const PAGE_SIZE = 10;
  function answerSentence({ prompt, answer }) {
    // Braces hold source instructions, not part of the sentence. Multi-gap
    // answers use slash-separated words in the same order as the blanks.
    const sentence = prompt.replace(/\{[^}]*\}/g, '').trim();
    const gaps = sentence.match(/_+/g) || [];
    if (gaps.length) {
      const parts = gaps.length > 1 ? answer.split(/\s*\/\s*/) : [answer];
      let index = 0;
      return sentence.replace(/_+/g, () => parts[index++]).replace(/\s+([.,!?;:])/g, '$1');
    }
    const completed = sentence ? sentence + ' ' + answer : answer;
    return /[.!?]$/.test(completed) ? completed : completed + '.';
  }
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  function validItems(items) {
    return Array.isArray(items) && items.length > 0 && items.length <= 1000 && items.every((item, index) =>
      Number.isInteger(item?.number) && item.number > 0 && (!index || item.number > items[index - 1].number) &&
      typeof item.prompt === 'string' && item.prompt.trim() && typeof item.answer === 'string' && item.answer.trim() &&
      Array.isArray(item.options) && item.options.length === 4 && item.options.every(option => typeof option === 'string' && option.trim()) &&
      item.options.includes(item.answer) && ((item.prompt.match(/_+/g) || []).length <= 1 || item.answer.split(/\s*\/\s*/).length === item.prompt.match(/_+/g).length));
  }
  function exercise(item, tag = 'li') {
    const row = element(tag, '', 'grammar-item');
    row.id = 'grammar-item-' + item.number; row.tabIndex = -1; row.setAttribute('aria-label', 'Item ' + item.number);
    const prompt = element('p', '', 'grammar-prompt'); prompt.setAttribute('aria-live', 'polite');
    const sentence = element('q', item.prompt); sentence.id = 'grammar-sentence-' + item.number; prompt.append(sentence);
    const options = element('ul', '', 'grammar-options'); options.setAttribute('aria-label', 'Choices for item ' + item.number);
    for (const text of item.options) { const option = element('li'); option.append(element('q', text)); options.append(option); }
    const reveal = element('label', '', 'grammar-reveal');
    const checkbox = element('input'); checkbox.type = 'checkbox'; checkbox.autocomplete = 'off';
    checkbox.setAttribute('aria-label', 'Show answer for item ' + item.number);
    checkbox.setAttribute('aria-controls', sentence.id);
    checkbox.addEventListener('change', () => {
      sentence.textContent = checkbox.checked ? answerSentence(item) : item.prompt;
      prompt.classList.toggle('is-revealed', checkbox.checked);
    });
    reveal.append(checkbox, element('span', 'Show answer'));
    row.append(prompt, options, reveal);
    return row;
  }
  window.GrammarPractice = {
    exercise, validItems,
    create({ root, api, expired }) {
      let revision = 0, active = false, items = [], page = 0, progress = new Map(), teacher = false, saving = false;
      let listOpen = false, listPage = 0, hideFinished = false;
      function clear() {
        revision++; active = false; items = []; page = 0; progress.clear(); saving = false; listOpen = false; listPage = 0; hideFinished = false;
        root.replaceChildren(); root.hidden = true; root.removeAttribute('aria-busy');
      }
      function readProgress(data) {
        if (!Array.isArray(data.entries) || data.entries.length > 1000 || data.entries.some(entry =>
          !Number.isInteger(entry.number) || typeof entry.finished !== 'boolean' || typeof entry.question !== 'boolean' ||
          !Number.isSafeInteger(entry.revision) || entry.revision < 0)) throw new Error('Invalid saved choices');
        progress = new Map(data.entries.map(entry => [entry.number, entry]));
      }
      const visibleItems = () => hideFinished ? items.filter(item => !progress.get(item.number)?.finished) : items;
      function render(focus = false, focusNumber = null, message = '') {
        const visible = visibleItems();
        page = Math.max(0, Math.min(page, Math.ceil(visible.length / PAGE_SIZE) - 1));
        const start = page * PAGE_SIZE, end = Math.min(start + PAGE_SIZE, visible.length);
        const range = index => `${visible[index * PAGE_SIZE].number}–${visible[Math.min((index + 1) * PAGE_SIZE, visible.length) - 1].number}`;
        const filter = element('label', '', 'practice-filter');
        const checkbox = element('input'); checkbox.type = 'checkbox'; checkbox.id = 'grammar-hide-finished'; checkbox.checked = hideFinished; checkbox.autocomplete = 'off';
        checkbox.addEventListener('change', () => { hideFinished = checkbox.checked; page = 0; render(); root.querySelector('#grammar-hide-finished').focus(); });
        filter.append(checkbox, element('span', 'Hide finished items'));
        const filterStatus = element('p', message, 'field-hint'); filterStatus.setAttribute('role', 'status');
        const intro = element('p', `${items.length} items. Later questions are harder. Choose any group.`, 'field-hint');
        const help = element('p', teacher ? 'Teacher view: you can see saved choices. Only the student can change them.' : 'Choose “Finish” when you are done. Choose “Questions” to ask your teacher about an item. Click a button again to undo it. These choices are saved.', 'field-hint');
        const questions = element('details', '', 'grammar-questions'); questions.open = listOpen;
        questions.addEventListener('toggle', () => { listOpen = questions.open; });
        const summary = element('summary'), questionList = element('div'); questions.append(summary, questionList);
        function updateList() {
          const selected = items.filter(item => progress.get(item.number)?.question);
          summary.textContent = 'Questions list (' + selected.length + ')'; questionList.replaceChildren();
          if (!selected.length) { questionList.append(element('p', 'No questions yet. Use “Questions” on an item to add it here.', 'field-hint')); return; }
          listPage = Math.min(listPage, Math.floor((selected.length - 1) / 20));
          questionList.append(element('p', 'Open an item to talk about it with your teacher. After you talk, click “Saved to Questions” to remove it.', 'field-hint'));
          const links = element('ul', '', 'grammar-question-links');
          for (const item of selected.slice(listPage * 20, (listPage + 1) * 20)) {
            const row = element('li'), button = element('button', `Item ${item.number} · “${item.prompt}”` + (progress.get(item.number)?.finished ? ' · Finished' : ''), 'secondary-button');
            button.type = 'button'; button.disabled = saving;
            button.addEventListener('click', () => {
              const showAll = hideFinished && progress.get(item.number)?.finished;
              if (showAll) hideFinished = false;
              page = Math.floor(visibleItems().findIndex(entry => entry.number === item.number) / PAGE_SIZE); listOpen = false;
              render(true, item.number, showAll ? 'Showing all items so you can view this question.' : '');
            });
            row.append(button); links.append(row);
          }
          questionList.append(links);
          if (selected.length > 20) {
            const paging = element('div', '', 'grammar-controls');
            const back = element('button', 'Previous questions', 'secondary-button'), forward = element('button', 'More questions', 'secondary-button');
            back.type = forward.type = 'button'; back.disabled = saving || listPage === 0; forward.disabled = saving || (listPage + 1) * 20 >= selected.length;
            back.addEventListener('click', () => { listPage--; updateList(); }); forward.addEventListener('click', () => { listPage++; updateList(); });
            paging.append(back, element('span', `Page ${listPage + 1} of ${Math.ceil(selected.length / 20)}`), forward); questionList.append(paging);
          }
        }
        if (!visible.length) {
          updateList();
          const empty = element('p', 'All items are finished. Uncheck “Hide finished items” to see them again.', 'practice-empty'); empty.tabIndex = -1;
          root.replaceChildren(intro, help, filter, filterStatus, questions, empty);
          if (focus) empty.focus();
          return;
        }
        const picker = element('div', '', 'grammar-picker');
        const label = element('label', 'Choose items'); label.htmlFor = 'grammar-group';
        const select = element('select'); select.id = 'grammar-group';
        for (let index = 0; index < Math.ceil(visible.length / PAGE_SIZE); index++) {
          const option = element('option', range(index)); option.value = String(index); select.append(option);
        }
        select.value = String(page);
        select.addEventListener('change', () => { page = Number(select.value); render(true); });
        picker.append(label, select);
        const heading = element('h4', `Items ${range(page)}`, 'grammar-heading'); heading.tabIndex = -1;
        const list = element('ol', '', 'grammar-items'); list.start = visible[start].number;
        const rows = new Map();
        function updateRows() {
          for (const [number, {row, finished, question, status}] of rows) {
            const entry = progress.get(number);
            row.classList.toggle('is-finished', Boolean(entry?.finished));
            finished.textContent = entry?.finished ? 'Finished' : 'Finish';
            question.textContent = entry?.question ? 'Saved to Questions' : 'Questions';
            finished.setAttribute('aria-label', finished.textContent + ' for item ' + number);
            question.setAttribute('aria-label', question.textContent + ' for item ' + number);
            finished.setAttribute('aria-pressed', String(Boolean(entry?.finished))); question.setAttribute('aria-pressed', String(Boolean(entry?.question)));
            finished.disabled = question.disabled = teacher || saving;
            status.textContent = [entry?.finished ? 'Marked as finished.' : '', entry?.question ? 'In your Questions list.' : ''].filter(Boolean).join(' ');
          }
          updateList();
        }
        async function save(number, field) {
          if (saving || teacher) return;
          const current = revision, entry = progress.get(number), {status} = rows.get(number);
          const body = { number, field, value: !entry?.[field], revision: entry?.revision || 0 };
          let refreshFiltered = false, filterMessage = '';
          saving = true;
          const controls = [...root.querySelectorAll('button, select, #grammar-hide-finished')].map(el => [el, el.disabled]);
          for (const [el] of controls) el.disabled = true;
          status.textContent = 'Saving…';
          try {
            const data = await api('/api/grammar-practice/state', {method:'PATCH', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)});
            if (current !== revision) return;
            progress.set(number, data.entry); updateRows();
            refreshFiltered = field === 'finished'; filterMessage = 'Item ' + number + ' is finished.';
          } catch (error) {
            if (current !== revision || expired(error)) return;
            if (error.status === 409) {
              try {
                const data = await api('/api/grammar-practice/state');
                if (current !== revision) return;
                readProgress(data); updateRows(); refreshFiltered = true; filterMessage = 'Your saved choices have changed. The list is now up to date.';
              } catch (reloadError) {
                if (current !== revision || expired(reloadError)) return;
                status.textContent = 'Your choices could not reload. Leave this activity and open it again.'; return;
              }
            }
            status.textContent = error.status === 409 ? error.message : 'Your change could not be saved. Please try again.';
          } finally {
            if (current === revision) {
              saving = false;
              for (const [el, disabled] of controls) el.disabled = disabled;
              updateList();
              if (hideFinished && refreshFiltered) render(true, null, filterMessage);
            }
          }
        }
        for (const item of visible.slice(start, end)) {
          const row = exercise(item), actions = element('div', '', 'grammar-actions'); row.value = item.number;
          const finished = element('button', 'Finish', 'secondary-button'), question = element('button', 'Questions', 'secondary-button question-button');
          finished.type = question.type = 'button';
          const status = element('p', '', 'grammar-save-status field-hint'); status.setAttribute('role', 'status');
          finished.addEventListener('click', () => save(item.number, 'finished')); question.addEventListener('click', () => save(item.number, 'question'));
          actions.append(finished, question); row.append(actions, status); list.append(row);
          rows.set(item.number, {row, finished, question, status});
        }
        updateRows();
        const controls = element('div', '', 'grammar-controls');
        const previous = element('button', 'Previous 10', 'secondary-button'); previous.type = 'button'; previous.disabled = page === 0;
        const next = element('button', 'Next 10', 'secondary-button'); next.type = 'button'; next.disabled = end === visible.length;
        previous.addEventListener('click', () => { if (page > 0) { page--; render(true); } });
        next.addEventListener('click', () => { if (end < visible.length) { page++; render(true); } });
        controls.append(previous, next);
        root.replaceChildren(intro, help, filter, filterStatus, questions, picker, heading, list, controls);
        if (focus) { const target = focusNumber ? rows.get(focusNumber).row : heading; target.focus(); target.scrollIntoView?.({ block: 'start' }); }
      }
      async function open(teacherView = false) {
        if (active) return;
        active = true; teacher = teacherView; const current = ++revision;
        root.hidden = false; root.setAttribute('aria-busy', 'true');
        const loading = element('p', 'Loading grammar practice…'); loading.setAttribute('role', 'status'); root.replaceChildren(loading);
        try {
          const [data, state] = await Promise.all([api('/api/grammar-practice'), api('/api/grammar-practice/state')]);
          if (current !== revision) return;
          if (!validItems(data.items) || data.items.some((item, index) => item.number !== index + 1)) throw new Error('Invalid practice items');
          readProgress(state); items = data.items; page = 0; root.removeAttribute('aria-busy'); render();
        } catch (error) {
          if (current !== revision || expired(error)) return;
          root.removeAttribute('aria-busy');
          const message = element('p', 'Grammar practice could not load. Please try again.'); message.setAttribute('role', 'alert');
          const retry = element('button', 'Try again', 'secondary-button'); retry.type = 'button';
          retry.addEventListener('click', () => { active = false; open(teacher); });
          root.replaceChildren(message, retry);
        }
      }
      return { open, clear };
    },
  };
})();
