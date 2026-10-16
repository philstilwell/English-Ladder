(() => {
  'use strict';
  const element = (tag, text = '', cls = '') => { const el = document.createElement(tag); el.textContent = text; el.className = cls; return el; };
  const topicKey = item => JSON.stringify([item.title, item.activity, item.target, item.aiPrompt ?? null]);
  const validTopic = item => item && ['title', 'activity', 'target'].every(key => typeof item[key] === 'string') && (item.aiPrompt === undefined || typeof item.aiPrompt === 'string');
  const validProgress = entry => entry && /^[a-f0-9]{64}$/.test(entry.id) && typeof entry.finished === 'boolean' && typeof entry.question === 'boolean' && Number.isSafeInteger(entry.revision) && entry.revision >= 0;
  const validItems = items => Array.isArray(items) && items.every(item => validTopic(item) && validProgress(item.progress) && item.id === item.progress.id);
  function card(item) {
    const row = element('section', '', 'assessment-plan-card');
    row.append(element('h4', item.title), element('p', item.activity));
    const target = element('p', '', 'assessment-target'); target.append(element('strong', 'Try this: '), document.createTextNode(item.target));
    const box = element('div', '', 'study-prompt');
    const prompt = item.aiPrompt || 'Help me study this English topic: “' + item.title + '”. Use short, simple English. First, explain the topic and give three easy examples. Then give me five practice questions, one at a time. Wait for my answer. Explain any mistake and let me try again.';
    const ai = window.PracticePrompt.create({ prompt, label: ': ' + item.title });
    ai.controls.classList.add('study-prompt-actions'); ai.status.classList.add('study-prompt-status');
    const actions = element('div', '', 'study-actions'); actions.append(ai.controls);
    box.append(actions, ai.status); row.append(target, box);
    return { row, actions };
  }
  function choiceControls(view, item, save) {
    const finished = element('button', 'Finish', 'secondary-button study-finish');
    const question = element('button', 'Questions', 'secondary-button question-button');
    finished.type = question.type = 'button';
    view.actions.prepend(finished, question);
    function update(entry, disabled) {
      view.row.classList.toggle('is-finished', Boolean(entry?.finished));
      finished.textContent = entry?.finished ? 'Finished' : 'Finish';
      question.textContent = entry?.question ? 'Saved to Questions' : 'Questions';
      for (const [button, field] of [[finished, 'finished'], [question, 'question']]) {
        button.disabled = disabled || !entry;
        button.setAttribute('aria-pressed', String(Boolean(entry?.[field])));
        button.setAttribute('aria-label', button.textContent + ': ' + item.title);
      }
    }
    finished.addEventListener('click', () => save('finished'));
    question.addEventListener('click', () => save('question'));
    update(item.progress, true);
    return { update };
  }
  window.StudyPractice = {
    card, validItems,
    review(item) {
      const view = card(item);
      choiceControls(view, item, () => {}).update(item.progress, true);
      if (!item.current) view.row.prepend(element('p', 'From an earlier assessment', 'field-hint'));
      return view.row;
    },
    create({ api, expired }) {
      let generation = 0, root = null, plan = [], teacher = false, ready = false, busy = false;
      let rows = [], saved = new Map(), topics = [], questions = [], cursor = null, pages = [null];
      let status, retry, list, listContent, listSummary, listStatus, listRequest = 0;
      function clear() {
        generation++; listRequest++; root?.replaceChildren(); root = null; plan = []; rows = []; saved.clear(); topics = []; questions = []; pages = [null]; cursor = null; ready = false; busy = false;
      }
      function update() {
        for (const row of rows) row.controls.update(saved.get(row.id), teacher || busy || !ready);
      }
      function addCard(item, parent, id = null) {
        const view = card(item);
        const row = { ...view, id, item };
        row.controls = choiceControls(view, item, field => save(row, field));
        rows.push(row); parent.append(view.row);
        return row;
      }
      function renderQuestions() {
        rows = rows.filter(row => !row.fromList); listContent.replaceChildren();
        listSummary.textContent = 'Questions list';
        if (!questions.length) listContent.append(element('p', 'No questions on this page. Use “Questions” on a topic to add it here.', 'field-hint'));
        for (const item of questions) {
          saved.set(item.id, item.progress);
          const row = addCard(item, listContent, item.id); row.fromList = true;
          if (!item.current) row.row.prepend(element('p', 'From an earlier assessment', 'field-hint'));
        }
        const paging = element('div', '', 'terms-controls');
        const back = element('button', 'Previous questions', 'secondary-button'), more = element('button', 'More questions', 'secondary-button');
        back.type = more.type = 'button'; back.disabled = pages.length < 2; more.disabled = !cursor;
        back.addEventListener('click', () => loadQuestions(pages.slice(0, -1)));
        more.addEventListener('click', () => loadQuestions([...pages, cursor]));
        if (pages.length > 1 || cursor) { paging.append(back, more); listContent.append(paging); }
        update();
      }
      async function loadQuestions(nextPages = [null]) {
        const current = generation, request = ++listRequest;
        listStatus.textContent = 'Loading questions…';
        try {
          const data = await api('/api/study/questions' + (nextPages.at(-1) ? '?after=' + nextPages.at(-1) : ''));
          if (current !== generation || request !== listRequest) return;
          if (!validItems(data.questions) || data.nextCursor !== null && !/^[a-f0-9]{64}$/.test(data.nextCursor)) throw new Error('Invalid questions');
          questions = data.questions; cursor = data.nextCursor; pages = nextPages; renderQuestions(); listStatus.textContent = '';
        } catch (error) {
          if (current !== generation || request !== listRequest || expired(error)) return;
          listStatus.textContent = 'Questions could not load. Use “Refresh questions list” to try again.';
        }
      }
      async function load() {
        const current = generation;
        ready = false; update(); retry.hidden = true; status.textContent = 'Loading saved choices…';
        try {
          const data = await api('/api/study/state');
          if (current !== generation) return;
          if (!validItems(data.topics)) throw new Error('Invalid saved choices');
          topics = data.topics; saved = new Map(topics.map(item => [item.id, item.progress]));
          for (const row of rows.filter(row => !row.fromList)) row.id = topics.find(topic => topicKey(topic) === topicKey(row.item))?.id;
          ready = true; update();
          status.textContent = rows.some(row => !row.fromList && !row.id) ? 'Some topics changed. Reload the page to see the latest topics.' : '';
          await loadQuestions();
        } catch (error) {
          if (current !== generation || expired(error)) return;
          status.textContent = 'Saved choices could not load. Please try again.'; retry.hidden = false;
        }
      }
      async function save(row, field) {
        if (teacher || busy || !ready || !saved.has(row.id)) return;
        const current = generation, entry = saved.get(row.id), value = !entry[field];
        busy = true; update(); status.textContent = 'Saving your choice…';
        try {
          const data = await api('/api/study/state', { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id: row.id, field, value, revision: entry.revision }) });
          if (current !== generation) return;
          if (!validProgress(data.entry) || data.entry.id !== row.id) throw new Error('Invalid saved choice');
          saved.set(row.id, data.entry); update(); status.textContent = 'Your choice is saved.';
          await loadQuestions();
        } catch (error) {
          if (current !== generation || expired(error)) return;
          if (error.status === 409) {
            await load();
            if (current === generation && ready) status.textContent = 'Your choices changed on another page. Saved choices are shown. Please try again. If a topic changed, reload this page.';
          } else status.textContent = 'Your choice could not be saved. Please try again.';
        } finally { if (current === generation) { busy = false; update(); } }
      }
      function open(target, items, isTeacher) {
        clear(); root = target; plan = items; teacher = isTeacher;
        root.append(element('p', teacher ? 'Teacher view: you can see saved choices. Only the student can change them.' : 'Choose “Finish” when you are done. Choose “Questions” to ask your teacher about a topic. Click again to undo. Your choices are saved.', 'field-hint'));
        status = element('p', '', 'study-save-status'); status.setAttribute('role', 'status');
        retry = element('button', 'Try again', 'secondary-button'); retry.type = 'button'; retry.hidden = true; retry.addEventListener('click', load);
        list = element('details', '', 'study-questions'); listSummary = element('summary', 'Questions list');
        listContent = element('div', '', 'study-question-items'); listStatus = element('p', '', 'field-hint'); listStatus.setAttribute('role', 'status');
        const refresh = element('button', 'Refresh questions list', 'secondary-button'); refresh.type = 'button'; refresh.addEventListener('click', () => loadQuestions());
        list.append(listSummary, element('p', 'These topics are saved for you and your teacher. Questions stay here after an assessment changes. Click “Saved to Questions” to remove a topic.', 'field-hint'), refresh, listStatus, listContent);
        const cards = element('div', '', 'study-current');
        for (const item of plan) addCard(item, cards);
        root.append(status, retry, list, cards); void load();
      }
      return { open, clear };
    },
  };
})();
