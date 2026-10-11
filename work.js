/* All lessons and explanations remain readable without JavaScript. */
(() => {
  'use strict';
  // Retire course drafts and completion records without touching other site preferences.
  try {
    const storage = window.localStorage;
    for (let index = storage.length - 1; index >= 0; index -= 1) {
      const key = storage.key(index);
      if (key?.startsWith('english-ladder-work-v2:')) storage.removeItem(key);
    }
  } catch (_) { /* Lessons remain usable when browser storage is blocked. */ }
  const searchText = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLocaleLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
  const directory = document.querySelector('[data-work-directory]');
  if (directory) {
    const search = directory.querySelector('[data-course-search]');
    const category = directory.querySelector('[data-course-category]');
    const reset = directory.querySelector('[data-course-reset]');
    const cards = [...directory.querySelectorAll('[data-work-course-link]')];
    const searchable = cards.map(card => searchText(`${card.dataset.search} ${card.dataset.category}`));
    const filter = () => {
      const terms = searchText(search.value).split(/\s+/).filter(Boolean);
      let shown = 0;
      cards.forEach((card, index) => {
        const match = (!category.value || card.dataset.category === category.value) && terms.every(term => searchable[index].includes(term));
        card.hidden = !match;
        if (match) shown += 1;
      });
      directory.querySelector('[data-course-count]').textContent = `${shown} of ${cards.length} courses`;
      directory.querySelector('[data-course-empty]').hidden = shown !== 0;
      reset.hidden = !search.value && !category.value;
    };
    search.addEventListener('input', filter);
    category.addEventListener('change', filter);
    reset.addEventListener('click', () => {
      search.value = '';
      category.value = '';
      filter();
      search.focus();
    });
    directory.querySelector('.work-directory-filters').hidden = false;
    window.addEventListener('pageshow', filter);
    filter();
  }
  const course = document.querySelector('[data-work-course]');
  if (!course) return;
  const modules = [...course.querySelectorAll('.work-module')];
  function setupLessonNavigation() {
    const toolbar = course.querySelector('.work-lesson-tools');
    const navigation = toolbar?.querySelector('.work-jump');
    if (!navigation) return;
    const masthead = document.querySelector('.site-masthead');
    const promptsLink = navigation.querySelector('.work-prompts-link');
    const promptSections = [...course.querySelectorAll('#finished-dialogue-prompts, #ai-practice')];
    const steps = [
      ['.work-case', 'Read the situation'],
      ['.work-words, .work-module-body > .work-two-column > section:nth-child(2)', 'Find the words'],
      ['.work-language', 'Notice the language'],
      ['.work-checks', 'Check your understanding'],
      ['.work-conversations', 'Conversations'],
      ['.work-speaking', 'Say it'],
    ];
    const entries = modules.map(module => {
      const link = navigation.querySelector(`a[href="#${module.id}"]`);
      if (!link) return null;
      link.setAttribute('aria-controls', module.id);
      const sections = steps.map(([selector], index) => {
        const section = module.querySelector(selector);
        if (section) section.dataset.workStep = String(index + 1);
        return section;
      });
      if (sections.some(section => !section)) return null;
      const markers = document.createElement('span');
      markers.className = 'work-section-dots';
      markers.setAttribute('aria-hidden', 'true');
      const dots = steps.map(([, label], index) => {
        const dot = document.createElement('span');
        dot.className = 'work-section-dot';
        dot.title = `${String.fromCharCode(65 + index)}. ${label}`;
        markers.append(dot);
        return dot;
      });
      const status = document.createElement('span');
      status.className = 'sr-only';
      status.dataset.workScrollStatus = '';
      status.textContent = '. 0 of 6 subsections reached.';
      link.append(markers, status);
      return {module, link, sections, dots, status, reached: 0};
    }).filter(Boolean);
    const frame = window.requestAnimationFrame?.bind(window) || (callback => setTimeout(callback, 0));
    let pending = false;
    const update = () => {
      pending = false;
      const height = Math.ceil(toolbar.getBoundingClientRect().height);
      course.style.setProperty('--work-navigation-height', `${height}px`);
      const readingLine = (masthead?.getBoundingClientRect().bottom || 0) + height + 24;
      entries.forEach(entry => {
        entry.link.classList.toggle('is-open', entry.module.open);
        entry.link.setAttribute('aria-expanded', String(entry.module.open));
        const bounds = entry.module.getBoundingClientRect();
        const active = entry.module.open && bounds.height > 0 && bounds.top <= readingLine && bounds.bottom > readingLine;
        if (active) entry.link.setAttribute('aria-current', 'location');
        else entry.link.removeAttribute('aria-current');
        // Closed lessons have no visible subsections. Preserve their last position
        // without marking skipped lessons as read when scrolling past their titles.
        if (!entry.module.open || bounds.height === 0) return;
        const reached = entry.sections.filter(section => {
          const rect = section.getBoundingClientRect();
          return rect.height > 0 && rect.top <= readingLine;
        }).length;
        if (reached === entry.reached) return;
        entry.reached = reached;
        entry.dots.forEach((dot, index) => dot.classList.toggle('is-reached', index < reached));
        entry.status.textContent = `. ${reached} of 6 subsections reached.`;
      });
      const inPrompts = promptSections.some(section => {
        const bounds = section.getBoundingClientRect();
        return bounds.height > 0 && bounds.top <= readingLine && bounds.bottom > readingLine;
      });
      if (inPrompts) promptsLink?.setAttribute('aria-current', 'location');
      else promptsLink?.removeAttribute('aria-current');
    };
    const schedule = () => {
      if (!pending) { pending = true; frame(update); }
    };
    navigation.addEventListener('click', event => {
      if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const entry = entries.find(item => item.link === event.target.closest('a'));
      if (!entry) return;
      entry.module.open = true;
      if (location.hash === `#${entry.module.id}`) {
        event.preventDefault();
        frame(() => entry.module.scrollIntoView({block: 'start'}));
      }
      schedule();
    });
    window.addEventListener('scroll', schedule, {passive: true});
    window.addEventListener('resize', schedule, {passive: true});
    window.addEventListener('pageshow', schedule);
    window.addEventListener('load', schedule, {once: true});
    course.addEventListener('toggle', schedule, true);
    if ('ResizeObserver' in window) {
      const observer = new ResizeObserver(schedule);
      observer.observe(toolbar);
      observer.observe(course);
      if (masthead) observer.observe(masthead);
    }
    update();
  }
  setupLessonNavigation();
  course.querySelectorAll('[data-work-quiz]').forEach(quiz => {
    const check = quiz.querySelector('[data-check-answer]');
    const feedback = quiz.querySelector('[data-quiz-feedback]');
    check.hidden = false;
    check.addEventListener('click', () => {
      const selected = quiz.querySelector('input:checked');
      if (!selected) { feedback.textContent = 'Choose an answer first.'; delete feedback.dataset.result; return; }
      const correct = selected.value === quiz.dataset.correct;
      const reason = quiz.querySelectorAll('.work-answer-reasons li')[Number(selected.value)];
      const explanation = quiz.dataset.explanation || [...reason.childNodes].filter(n => n.nodeType === Node.TEXT_NODE).map(n => n.textContent).join('').trim();
      feedback.textContent = `${correct ? 'Correct.' : 'Try again.'} ${explanation}`;
      feedback.dataset.result = correct ? 'correct' : 'retry';
    });
    quiz.querySelectorAll('input').forEach(input => input.addEventListener('change', () => { feedback.textContent = ''; delete feedback.dataset.result; }));
  });
  course.querySelectorAll('[data-work-cloze]').forEach(activity => {
    const answers = JSON.parse(activity.querySelector('[data-cloze-answers]').textContent);
    const gaps = [...activity.querySelectorAll('[data-cloze-gap]')];
    const status = activity.querySelector('[data-cloze-status]');
    const feedback = [...activity.querySelectorAll('[data-cloze-feedback]')];
    activity.querySelector('.work-cloze-actions').hidden = false;
    const clear = () => {
      status.textContent = '';
      delete status.dataset.result;
      feedback.forEach(item => { item.hidden = true; item.textContent = ''; });
      gaps.forEach(gap => { delete gap.dataset.result; gap.removeAttribute('aria-invalid'); });
    };
    gaps.forEach(gap => gap.addEventListener('change', clear));
    activity.querySelector('[data-check-cloze]').addEventListener('click', () => {
      let correct = 0;
      let missing = 0;
      gaps.forEach((gap, index) => {
        const explanation = feedback[index];
        if (!gap.value) {
          missing += 1;
          explanation.textContent = `${index + 1}. Choose a word or phrase.`;
          gap.dataset.result = 'missing';
          gap.setAttribute('aria-invalid', 'true');
        } else {
          const matches = gap.value === answers[index].answer;
          if (matches) correct += 1;
          gap.dataset.result = matches ? 'correct' : 'retry';
          gap.setAttribute('aria-invalid', String(!matches));
          explanation.textContent = `${index + 1}. ${matches ? 'Correct' : 'Review'}: ${answers[index].answer}. ${answers[index].reason}`;
        }
        explanation.hidden = false;
      });
      status.textContent = `${correct} of ${gaps.length} correct.${missing ? ` ${missing} unanswered.` : ''} ${correct === gaps.length ? 'Read the complete exchange aloud.' : 'Use the explanations to correct the remaining gaps.'}`;
      status.dataset.result = correct === gaps.length ? 'correct' : 'retry';
    });
    activity.querySelector('[data-reset-cloze]').addEventListener('click', () => {
      gaps.forEach(gap => { gap.value = ''; });
      clear();
      activity.querySelectorAll('details').forEach(details => { details.open = false; });
      gaps[0]?.focus();
    });
  });
  const openHash = () => {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (!target || !course.contains(target)) return;
    let disclosure = target.closest('details');
    while (disclosure && course.contains(disclosure)) {
      disclosure.open = true;
      disclosure = disclosure.parentElement.closest('details');
    }
    // Reveal the content before positioning it below both sticky menus.
    const frame = window.requestAnimationFrame?.bind(window) || (callback => setTimeout(callback, 0));
    frame(() => target.scrollIntoView?.({block: 'start'}));
  };
  addEventListener('hashchange', openHash);
  openHash();
  const expand = course.querySelector('[data-expand-lessons]');
  const updateExpand = () => { expand.textContent = modules.every(m => m.open) ? 'Close all lessons' : 'Open all lessons'; };
  expand.hidden = false;
  expand.addEventListener('click', () => { const open = !modules.every(m => m.open); modules.forEach(m => { m.open = open; }); updateExpand(); });
  modules.forEach(m => m.addEventListener('toggle', updateExpand));
  updateExpand();
  const vocabSearch = course.querySelector('[data-vocabulary-search]');
  const terms = [...course.querySelectorAll('[data-work-term]')];
  const filterVocabulary = () => {
    const query = searchText(vocabSearch.value).split(/\s+/).filter(Boolean);
    terms.forEach(term => { term.hidden = !query.every(word => searchText(term.textContent).includes(word)); });
    const count = terms.filter(term => !term.hidden).length;
    course.querySelector('[data-vocabulary-count]').textContent = count ? `${count} of ${terms.length} vocabulary entries` : 'No terms match. Try a shorter word.';
  };
  course.querySelector('[data-vocabulary-filter]').hidden = false;
  vocabSearch.addEventListener('input', filterVocabulary);
  window.addEventListener('pageshow', filterVocabulary);
  filterVocabulary();
})();
