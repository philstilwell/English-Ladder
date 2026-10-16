(() => {
  'use strict';
  const node = (tag, text, className) => {
    const el = document.createElement(tag); if (text != null) el.textContent = text;
    if (className) el.className = className; return el;
  };
  function exercise(row) {
    const item = row.item;
    if (row.source === 'grammar-practice') return window.GrammarPractice.exercise(item, 'article');
    if (row.source === 'business-terms') return window.BusinessTerms.exercise(item).card;
    if (row.source === 'study-practice') return window.StudyPractice.review(item);
    if (row.source === 'vocabulary-practice') return window.VocabularyPractice.review(item, false);
    if (row.source === 'english-road') return window.RoadQuestions.review(item);
    if (window.CommunicationPractice.ids.includes(row.source)) return window.CommunicationPractice.review(item, false);
    throw new Error('This question could not load. Please reload the page.');
  }
  window.AllQuestions = { create({ root, api, expired }) {
    let generation = 0, active = false, pages = [null], busy = false;
    function clear() {
      generation++; active = false; busy = false; pages = [null]; root.replaceChildren(); root.hidden = true;
    }
    async function load(nextPages = [null], focus = false) {
      if (!active || busy) return;
      const current = ++generation; busy = true; root.replaceChildren();
      const back = node('a', 'Back to Activities', 'activity-questions-link'); back.href = '#activities';
      const toolbar = node('div', null, 'activity-progress-toolbar');
      const refresh = node('button', 'Refresh Questions', 'secondary-button'); refresh.type = 'button'; refresh.disabled = true;
      refresh.addEventListener('click', () => load([null], true));
      const status = node('p', 'Loading your questions…'); status.setAttribute('role', 'status'); status.tabIndex = -1;
      const content = node('div', null, 'all-questions-content'); toolbar.append(refresh, status); root.append(back, toolbar, content);
      const valid = () => active && current === generation;
      try {
        const data = await api('/api/activities/questions' + (nextPages.at(-1) ? '?after=' + encodeURIComponent(nextPages.at(-1)) : ''));
        if (!valid()) return;
        if (!Number.isSafeInteger(data.count) || data.count < 0 || !Array.isArray(data.questions) || data.questions.length > 20 ||
            data.nextCursor !== null && typeof data.nextCursor !== 'string') throw new Error('Your questions could not load. Please try again.');
        const fragment = document.createDocumentFragment();
        for (const row of data.questions) {
          const card = node('article', null, 'all-question-card');
          const itemLabel = Number.isInteger(row.item?.number) ? ' · Item ' + row.item.number : '';
          card.append(node('h3', row.label + itemLabel), exercise(row));
          if (row.item.progress?.finished) card.append(node('p', 'Marked as finished', 'field-note'));
          fragment.append(card);
        }
        pages = nextPages; content.append(fragment);
        status.textContent = data.count ? data.count + ' saved questions · Page ' + pages.length : 'No saved questions yet. Choose “Questions” on an activity item to add it here.';
        if (data.count && !data.questions.length) content.append(node('p', 'No questions on this page. Choose “Refresh Questions” to see the latest list.'));
        if (pages.length > 1 || data.nextCursor) {
          const controls = node('div', null, 'terms-controls');
          const previous = node('button', 'Previous questions', 'secondary-button'), more = node('button', 'More questions', 'secondary-button');
          previous.type = more.type = 'button'; previous.disabled = pages.length < 2; more.disabled = !data.nextCursor;
          previous.addEventListener('click', () => load(pages.slice(0, -1), true)); more.addEventListener('click', () => load([...pages, data.nextCursor], true));
          controls.append(previous, more); content.append(controls);
        }
        if (focus) status.focus();
      } catch (error) {
        if (!valid() || expired(error)) return;
        content.replaceChildren(); status.textContent = error.message; refresh.textContent = 'Try loading Questions again';
      } finally { if (valid()) { busy = false; refresh.disabled = false; } }
    }
    return { clear, open() { if (active) return; active = true; root.hidden = false; void load(); } };
  } };
})();
