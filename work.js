/* All lessons and explanations remain readable without JavaScript. */
(() => {
  'use strict';
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
  const notes = [...course.querySelectorAll('[data-work-note]')];
  const complete = [...course.querySelectorAll('[data-work-complete]')];
  const saveToggle = course.querySelector('[data-save-notes]');
  const storageStatus = course.querySelector('[data-storage-status]');
  const storageKey = `english-ladder-work-v2:${course.dataset.workCourse}`;
  let canStore = true;
  const updateProgress = () => {
    course.querySelector('[data-work-progress]').textContent = `${complete.filter(input => input.checked).length} of ${complete.length} practiced`;
  };
  const updateCount = note => {
    const words = note.value.trim() ? note.value.trim().split(/\s+/).length : 0;
    note.parentElement.querySelector('[data-word-count]').textContent = `${words} words · target 70-110`;
  };
  const save = () => {
    if (!saveToggle.checked || !canStore) return;
    try {
      localStorage.setItem(storageKey, JSON.stringify({ notes: Object.fromEntries(notes.map(n => [n.dataset.workNote, n.value])), complete: complete.filter(n => n.checked).map(n => n.dataset.workComplete) }));
      storageStatus.textContent = 'Saved in this browser only. Use fictional details; practice is not submitted or automatically graded.';
    } catch (_) {
      canStore = false;
      storageStatus.textContent = 'This browser could not save your practice. Copy any draft you want to keep.';
    }
  };
  try {
    const raw = localStorage.getItem(storageKey);
    if (raw) {
      const stored = JSON.parse(raw);
      if (stored && typeof stored === 'object' && !Array.isArray(stored)) {
        notes.forEach(note => { const value = stored.notes?.[note.dataset.workNote]; if (typeof value === 'string') note.value = value; });
        complete.forEach(input => { input.checked = Array.isArray(stored.complete) && stored.complete.includes(input.dataset.workComplete); });
        saveToggle.checked = true;
        storageStatus.textContent = 'Restored from this browser. Practice is not submitted or automatically graded.';
      }
    }
  } catch (_) { storageStatus.textContent = 'Saved practice could not be restored. You can still practice and copy your draft.'; }
  course.querySelector('[data-storage-controls]').hidden = false;
  saveToggle.addEventListener('change', () => {
    if (saveToggle.checked) { canStore = true; save(); return; }
    try {
      localStorage.removeItem(storageKey);
      storageStatus.textContent = 'Saving is off and the saved copy was removed. Your current draft remains on this page.';
    } catch (_) { storageStatus.textContent = 'Saving is off, but this browser could not remove the saved copy. Use browser site-data settings to remove it.'; }
  });
  course.querySelector('[data-clear-work]').addEventListener('click', event => {
    const before = {notes: notes.map(n => n.value), complete: complete.map(n => n.checked), enabled: saveToggle.checked};
    course.querySelector('[data-undo-work]')?.remove();
    const undo = document.createElement('button'); undo.type='button'; undo.className='work-button work-button-secondary'; undo.dataset.undoWork=''; undo.textContent='Undo clear';
    undo.addEventListener('click', () => {
      notes.forEach((note,i) => { note.value=before.notes[i]; updateCount(note); });
      complete.forEach((input,i) => { input.checked=before.complete[i]; });
      saveToggle.checked=before.enabled; canStore=true; updateProgress();
      storageStatus.textContent='Drafts and progress restored on this page.'; save(); undo.remove();
    });
    event.target.after(undo);
    notes.forEach(note => { note.value = ''; updateCount(note); });
    complete.forEach(input => { input.checked = false; });
    saveToggle.checked = false;
    try {
      localStorage.removeItem(storageKey);
      storageStatus.textContent = 'Drafts and progress cleared for this course. Saving is off.';
    } catch (_) { storageStatus.textContent = 'The page is cleared, but browser storage could not be cleared. Use browser site-data settings to remove saved data.'; }
    updateProgress();
  });
  notes.forEach(note => { updateCount(note); note.addEventListener('input', () => { updateCount(note); save(); }); });
  complete.forEach(input => input.addEventListener('change', () => { updateProgress(); save(); }));
  updateProgress();
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
