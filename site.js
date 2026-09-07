/* Lesson interactions. Practice answers and notes stay on the current page. */
(() => {
  'use strict';
  const masthead = document.querySelector('.site-masthead');
  if (masthead) {
    const measureMenu = () => document.documentElement.style.setProperty(
      '--masthead-height', `${Math.ceil(masthead.getBoundingClientRect().height)}px`);
    measureMenu();
    if ('ResizeObserver' in window) new ResizeObserver(measureMenu).observe(masthead);
    window.addEventListener('resize', measureMenu, {passive: true});
    window.addEventListener('load', () => {
      measureMenu();
      if (/^#lesson-[a-z0-9-]+$/.test(location.hash)) {
        document.getElementById(location.hash.slice(1))?.scrollIntoView({block: 'start', behavior: 'instant'});
      }
    }, {once: true});
  }
  const levels = ['beginner', 'intermediate', 'advanced'];
  const LEVEL_KEY = 'english-ladder-level';
  const read = key => { try { return localStorage.getItem(key); } catch (_) { return null; } };
  const write = (key, value) => { try { localStorage.setItem(key, value); return true; } catch (_) { return false; } };
  const currentLevel = location.pathname.match(/\/(beginner|intermediate|advanced)\.html$/)?.[1];
  let level = currentLevel || read(LEVEL_KEY) || 'beginner';
  if (!levels.includes(level)) level = 'beginner';
  function applyLevel(value) {
    level = value;
    document.querySelectorAll('[data-level-link], .explore-story').forEach(a => {
      const url = new URL(a.href, location.href);
      url.pathname = url.pathname.replace(/\/(beginner|intermediate|advanced)\.html$/, `/${level}.html`);
      a.href = url.href;
    });
    const input = document.querySelector(`input[name="feature-level"][value="${level}"]`);
    if (input) {
      input.checked = true;
      const start = document.querySelector('#feature-start');
      if (start && /^(?:stories\/[a-z-]+\/)?(?:beginner|intermediate|advanced)\.html(?:#lesson-\d{4}-\d{2}-\d{2})?$/.test(input.dataset.lessonHref || "")) start.href = input.dataset.lessonHref;
    }
  }
  applyLevel(level);
  if (currentLevel) write(LEVEL_KEY, currentLevel);
  document.querySelectorAll('input[name="feature-level"]').forEach(input => input.addEventListener('change', () => {
    if (levels.includes(input.value)) { write(LEVEL_KEY, input.value); applyLevel(input.value); }
  }));
  function preserveDate() {
    document.querySelectorAll('[data-level-choice]').forEach(a => {
      const url = new URL(a.href, location.href);
      if (/^#lesson-\d{4}-\d{2}-\d{2}$/.test(location.hash)) url.hash = location.hash;
      a.href = url.href;
    });
  }
  document.querySelectorAll('[data-level-choice]').forEach(a => a.addEventListener('click', () => {
    if (levels.includes(a.dataset.levelChoice)) write(LEVEL_KEY, a.dataset.levelChoice);
  }));
  preserveDate(); window.addEventListener('hashchange', preserveDate);
  document.querySelectorAll('.daily-lesson').forEach(lesson => lesson.addEventListener('toggle', () => {
    if (window.history && lesson.open && /^lesson-\d{4}-\d{2}-\d{2}$/.test(lesson.id)) {
      window.history.replaceState(null, '', '#'+lesson.id); preserveDate();
    }
  }));

  document.querySelectorAll('[data-library]').forEach(library => {
    const search = library.querySelector('[data-library-search]');
    const category = library.querySelector('[data-library-category]');
    const levelFilter = library.querySelector('[data-library-level]');
    const cards = [...library.querySelectorAll('[data-library-item]')];
    const filter = () => {
      const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
      let count=0;
      cards.forEach(card => {
        const match = terms.every(t => card.dataset.search.toLocaleLowerCase().includes(t)) && (!category?.value || card.dataset.category===category.value) && (!levelFilter?.value || card.dataset.level?.includes(levelFilter.value));
        card.hidden=!match; if(match) count++;
      });
      library.querySelector('[data-library-count]').textContent=`${count} of ${cards.length} available`;
      library.querySelector('[data-library-empty]').hidden=count!==0;
    };
    search.addEventListener('input',filter);category?.addEventListener('change',filter);levelFilter?.addEventListener('change',filter);filter();
  });

  const grammarQuestions=[...document.querySelectorAll('[data-choice-question]')];
  function updateGrammarProgress(){
    if(!grammarQuestions.length)return;
    const selected=grammarQuestions.map(q=>q.querySelector('input[type="radio"]:checked')).filter(Boolean);
    const correct=selected.filter(input=>input.dataset.choiceCorrect==='true').length;
    const total=grammarQuestions.length;
    document.querySelector('[data-choice-progress]').textContent=`${correct} of ${total} correct · ${selected.length} answered`;
    const complete=document.querySelector('[data-complete-study]');complete.disabled=correct!==total;
    complete.textContent='Mark this lesson practiced';
    document.querySelector('[data-study-status]').textContent=correct===total?'All answers are correct. You can mark this lesson practiced.':`Answer all ${total} questions correctly to complete this activity.`;
  }
  function showChoice(question,option){
    const correct=option.dataset.choiceCorrect==='true';
    const feedback=question.querySelector('.choice-feedback');
    feedback.textContent=(correct?'Correct. ':'Not quite. ')+option.dataset.choiceFeedback+(correct?'':' Choose another answer and try again.');
    feedback.dataset.result=correct?'correct':'incorrect';feedback.hidden=false;
    question.querySelectorAll('input[type="radio"]').forEach(input=>{
      input.closest('label').dataset.choiceResult=input===option?(correct?'correct':'incorrect'):'';
      if(input===option)input.setAttribute('aria-describedby',feedback.id);else input.removeAttribute('aria-describedby');
    });
    updateGrammarProgress();
  }
  grammarQuestions.forEach(question=>{
    question.querySelectorAll('input[type="radio"]').forEach(option=>option.addEventListener('change',()=>{
      if(option.checked)showChoice(question,option);
    }));
  });
  updateGrammarProgress();
  document.querySelector('[data-complete-study]')?.addEventListener('click',event=>{
    event.target.textContent='Practiced ✓';
    document.querySelector('[data-study-status]').textContent='Practiced on this page. Try using the pattern again tomorrow.';
  });
})();
