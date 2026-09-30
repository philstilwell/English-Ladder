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
  const directory = document.querySelector('[data-work-directory]');
  if (directory) {
    const search = directory.querySelector('[data-course-search]');
    const category = directory.querySelector('[data-course-category]');
    const cards = [...directory.querySelectorAll('[data-work-course-link]')];
    const filter = () => {
      const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
      let shown = 0;
      cards.forEach(card => {
        const match = (!category.value || card.dataset.category === category.value) && terms.every(term => card.dataset.search.toLocaleLowerCase().includes(term));
        card.hidden = !match;
        if (match) shown += 1;
      });
      directory.querySelector('[data-course-count]').textContent = `${shown} of ${cards.length} courses`;
      directory.querySelector('[data-course-empty]').hidden = shown !== 0;
    };
    search.addEventListener('input', filter);
    category.addEventListener('change', filter);
  }
  const course = document.querySelector('[data-work-course]');
  if (!course) return;
  const modules = [...course.querySelectorAll('.work-module')];
  function setupLessonNavigation() {
    const toolbar = course.querySelector('.work-lesson-tools');
    const navigation = toolbar?.querySelector('.work-jump');
    if (!navigation) return;
    const masthead = document.querySelector('.site-masthead');
    const steps = [
      ['.work-case', 'Read the situation'],
      ['.work-module-body > .work-two-column > section:nth-child(2)', 'Find the words'],
      ['.work-language', 'Notice the language'],
      ['.work-checks', 'Check your understanding'],
      ['.work-conversations', 'Conversations'],
      ['.work-speaking', 'Say it'],
    ];
    const entries = modules.map(module => {
      const link = navigation.querySelector(`a[href="#${module.id}"]`);
      if (!link) return null;
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
        dot.title = `${index + 1}. ${label}`;
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
      const explanation = [...reason.childNodes].filter(n => n.nodeType === Node.TEXT_NODE).map(n => n.textContent).join('').trim();
      feedback.textContent = `${correct ? 'Correct.' : 'Try again.'} ${explanation}`;
      feedback.dataset.result = correct ? 'correct' : 'retry';
    });
    quiz.querySelectorAll('input').forEach(input => input.addEventListener('change', () => { feedback.textContent = ''; delete feedback.dataset.result; }));
  });
  const openHash = () => { const target = modules.find(m => m.id === location.hash.slice(1)); if (target) target.open = true; };
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
  vocabSearch.addEventListener('input', () => {
    const query = vocabSearch.value.toLocaleLowerCase().trim();
    terms.forEach(term => { term.hidden = !term.textContent.toLocaleLowerCase().includes(query); });
    const count = terms.filter(term => !term.hidden).length;
    course.querySelector('[data-vocabulary-count]').textContent = count ? `${count} of ${terms.length} terms` : 'No terms match. Try a shorter word.';
  });
})();
