(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const sections = ['overview', 'assessments', 'sessions', 'feedback', 'quiz', 'quiz-results', 'account', 'activities', 'resources'];
  const assessmentSections = ['summary', 'strengths', 'patterns', 'next'];
  const validId = /^\d{4}-\d{2}-\d{2}-\d{4}$/;
  let authenticated = false, checking = false, identityRevision = 0, pageRevision = 0;
  let sessions = [], nextCursor = null, indexReady = false, indexLoading = false, currentPage = '';
  let assessment = null, assessmentLoading = false;
  let quizState = null, quizRevision = 0;
  let teacherMode = false, resultRows = [], resultCursor = null, resultsLoading = false, resultsRevision = 0;
  let assessmentScrollFrame = 0;
  let settings = null, settingsLoading = false, settingsSaving = false, settingsRevision = 0, profileRevision = 0;
  const sectionMenu = document.querySelector('.section-nav');
  const stickyHeader = document.querySelector('.masthead-band');
  let activityChoices = null, activitiesLoading = false, activitiesRevision = 0, activitiesError = false;
  let resourceChoices = null, resourcesLoading = false, resourcesRevision = 0, resourcesError = false;
  const roadPractice = window.EnglishRoadPractice?.create({ root: $('road-practice'), api, expired }) || {
    clear() { $('road-practice').replaceChildren(); $('road-practice').hidden = true; },
    open() { $('road-practice').hidden = false; $('road-practice').textContent = 'Practice could not load. Reload this page to try again.'; },
  };
  const grammarPractice = window.GrammarPractice?.create({ root: $('grammar-practice'), api, expired }) || {
    clear() { $('grammar-practice').replaceChildren(); $('grammar-practice').hidden = true; },
    open() { $('grammar-practice').hidden = false; $('grammar-practice').textContent = 'Practice could not load. Reload this page to try again.'; },
  };
  const vocabularyPractice = window.VocabularyPractice?.create({ root: $('vocabulary-practice'), api, expired }) || { clear() { $('vocabulary-practice').replaceChildren(); $('vocabulary-practice').hidden = true; }, open() { $('vocabulary-practice').hidden = false; $('vocabulary-practice').textContent = 'Reload this page to open Vocabulary practice.'; } };
  const businessTerms = window.BusinessTerms?.create({ root: $('business-terms'), api, expired }) || {
    clear() { $('business-terms').replaceChildren(); $('business-terms').hidden = true; },
    open() { $('business-terms').hidden = false; $('business-terms').textContent = 'Practice could not load. Reload this page to try again.'; },
  };
  const studyPractice = window.StudyPractice.create({ api, expired });
  const dropdowns = ['overview', 'activities'].map(id => ({
    group: $(id + '-menu'), toggle: $(id + '-toggle'), list: $(id + '-submenu'),
    label: id === 'overview' ? 'Overview links' : 'Activities links',
  }));
  const [overviewDropdown, activitiesDropdown] = dropdowns;
  const overviewMenu = overviewDropdown.group;
  function positionDropdown(menu) {
    const left = menu.group.getBoundingClientRect().left;
    const width = menu.list.getBoundingClientRect().width;
    menu.list.style.left = Math.max(24, Math.min(left, document.documentElement.clientWidth - 24 - width)) - left + 'px';
  }
  function showDropdown(menu, open) {
    if (open) for (const other of dropdowns) if (other !== menu) showDropdown(other, false);
    menu.list.hidden = !open;
    menu.toggle.setAttribute('aria-expanded', String(open));
    menu.toggle.setAttribute('aria-label', (open ? 'Hide ' : 'Show ') + menu.label);
    if (open) {
      positionDropdown(menu);
      if (menu === activitiesDropdown && authenticated) void loadActivities();
    }
  }
  function closeDropdowns() { for (const menu of dropdowns) showDropdown(menu, false); }
  for (const menu of dropdowns) {
    menu.group.addEventListener('pointerenter', event => {
      if (event.pointerType === 'mouse' || event.pointerType === 'pen') showDropdown(menu, true);
    });
    menu.group.addEventListener('pointerleave', event => {
      if ((event.pointerType === 'mouse' || event.pointerType === 'pen') && !menu.list.contains(document.activeElement)) showDropdown(menu, false);
    });
    menu.toggle.addEventListener('click', () => showDropdown(menu, menu.list.hidden));
    menu.group.addEventListener('keydown', event => {
      if (event.key === 'ArrowDown' && !menu.list.contains(event.target)) {
        event.preventDefault(); showDropdown(menu, true);
        menu.list.querySelector('a:not([hidden]), button:not([disabled])')?.focus();
      }
    });
  }
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    for (const menu of dropdowns) if (!menu.list.hidden) {
      event.preventDefault(); showDropdown(menu, false);
      if (menu.group.contains(document.activeElement)) menu.toggle.focus();
    }
  });
  for (const type of ['pointerdown', 'focusin']) document.addEventListener(type, event => {
    for (const menu of dropdowns) if (!menu.group.contains(event.target)) showDropdown(menu, false);
  });
  sectionMenu.addEventListener('click', event => {
    if (!event.target.closest('a')) return;
    for (const menu of dropdowns) if (menu.list.contains(document.activeElement)) menu.toggle.focus({ preventScroll:true });
    closeDropdowns();
  });
  function updateHeaderHeight() {
    const height = stickyHeader.getBoundingClientRect().height;
    if (height) document.documentElement.style.setProperty('--student-header-height', height + 'px');
    scheduleAssessmentHighlight();
    for (const menu of dropdowns) if (!menu.list.hidden) positionDropdown(menu);
  }
  const headerResizeObserver = typeof ResizeObserver === 'undefined' ? null : new ResizeObserver(updateHeaderHeight);
  headerResizeObserver?.observe(stickyHeader);
  const assessmentResizeObserver = typeof ResizeObserver === 'undefined' ? null : new ResizeObserver(scheduleAssessmentHighlight);

  async function api(path, options = {}) {
    const response = await fetch(path, { credentials: 'same-origin', cache: 'no-store', ...options });
    let data;
    try { data = await response.json(); } catch { throw new Error('The page could not connect. Please try again.'); }
    if (!response.ok) {
      const error = new Error(data.error || 'Something went wrong. Please try again.');
      error.status = response.status;
      throw error;
    }
    return data;
  }
  function node(tag, text, className) {
    const el = document.createElement(tag);
    if (text) el.textContent = text;
    if (className) el.className = className;
    return el;
  }
  function date(s, zone = s.timeZone, time = false) {
    return new Intl.DateTimeFormat('en-US', { timeZone: zone, month: 'short', day: 'numeric', year: 'numeric', ...(time ? { hour: 'numeric', minute: '2-digit' } : {}) }).format(new Date(s.startedAt));
  }
  function link(s, className) {
    const el = node('a', '', className);
    el.href = '#feedback/' + s.id;
    el.append(node('span', date(s), 'session-date'), node('span', s.title, 'session-topic'));
    return el;
  }
  function show(view) {
    for (const id of ['loading', 'login-view', 'dashboard-view', 'unavailable-view']) $(id).hidden = id !== view;
    $('logout').hidden = view !== 'dashboard-view';
    sectionMenu.hidden = view !== 'dashboard-view';
    updateHeaderHeight();
  }
  function clearIdentity() {
    identityRevision++; pageRevision++;
    studyPractice.clear();
    roadPractice.clear();
    grammarPractice.clear();
    businessTerms.clear();
    vocabularyPractice.clear();
    closeDropdowns();
    clearSettings();
    clearResources();
    activityChoices = null; activitiesLoading = false; activitiesError = false; activitiesRevision++;
    activitiesDropdown.list.replaceChildren(); $('activity-title').textContent = 'Activities'; $('activity-message').textContent = '';
    clearActivityCatalog();
    authenticated = false; sessions = []; nextCursor = null; indexReady = false; indexLoading = false; currentPage = '';
    assessment = null; assessmentLoading = false;
    quizState = null; quizRevision++;
    teacherMode = false; resultRows = []; resultCursor = null; resultsLoading = false; resultsRevision++;
    $('quiz-nav').hidden = true;
    $('quiz-history').replaceChildren();
    $('quiz-results-status').textContent = ''; $('more-quiz-results').hidden = true;
    $('quiz-automation').replaceChildren(); $('quiz-automation').hidden = true;
    assessmentResizeObserver?.disconnect();
    if (assessmentScrollFrame) cancelAnimationFrame(assessmentScrollFrame);
    assessmentScrollFrame = 0;
    markAssessmentSection(null);
    for (const id of ['student-name', 'teacher-student-name', 'avatar', 'account-address', 'profile-nickname', 'account-status']) $(id).textContent = '';
    for (const id of ['session-list', 'session-select', 'session-summaries', 'feedback-page', 'assessment-content', 'assessment-source-count', 'quiz-content']) $(id).replaceChildren();
    $('assessment-sidebar').hidden = true;
    $('assessment-count').textContent = 'Loading assessment…';
    $('latest-title').textContent = 'Your learning notebook.';
    $('latest-summary').textContent = 'Open your session feedback to revisit useful language and find a short practice activity.';
    $('latest-link').href = '#feedback';
    $('session-count').textContent = 'Loading sessions…';
    $('feedback-count').textContent = 'Loading feedback…';
    $('session-list-status').textContent = 'Loading sessions…';
    $('more-sessions').hidden = true; $('retry-feedback').hidden = true;
    $('dashboard-title').textContent = 'Welcome back.';
    $('teacher-banner').hidden = true;
    document.title = 'Your student space · English Ladder';
  }
  function showLogin(message = '') {
    clearIdentity();
    $('login-notice').textContent = ''; $('login-notice').hidden = true;
    $('password').value = ''; $('password').type = 'password';
    $('show-password').textContent = 'Show';
    $('show-password').setAttribute('aria-label', 'Show password');
    $('show-password').setAttribute('aria-pressed', 'false');
    $('login-error').textContent = message; $('login-error').hidden = !message;
    show('login-view');
  }
  function expired(error) {
    if (error.status !== 401) return false;
    showLogin('Your session has ended. Please sign in again.');
    return true;
  }
  function messagePage(message, retry) {
    const content = node('div', '', 'feedback-message');
    content.append(node('p', message));
    if (retry) {
      const button = node('button', 'Try again', 'secondary-button');
      button.addEventListener('click', retry); content.append(button);
    }
    $('feedback-page').replaceChildren(content);
    $('feedback-page').setAttribute('aria-busy', 'false');
  }
  function markCurrent(id) {
    for (const el of $('session-list').querySelectorAll('a')) {
      if (el.hash === '#feedback/' + id) el.setAttribute('aria-current', 'page');
      else el.removeAttribute('aria-current');
    }
    $('session-select').value = id || '';
  }
  function clearResources() {
    resourcesRevision++; resourceChoices = null; resourcesLoading = false; resourcesError = false;
    $('resource-catalog').hidden = true; $('resource-status').textContent = ''; $('retry-resources').hidden = true;
    $('resource-count').textContent = '';
    for (const card of document.querySelectorAll('[data-resource-id]')) card.hidden = true;
  }
  function renderResources(requested = location.hash.slice(1).split('/').length === 2 ? location.hash.slice(1).split('/')[1] : '', focus = false) {
    const groups = [...document.querySelectorAll('[data-resource-group]')];
    for (const card of document.querySelectorAll('[data-resource-id]')) card.hidden = !resourceChoices?.includes(card.dataset.resourceId);
    const available = groups.filter(group => group.querySelector('.resource-card:not([hidden])'));
    const selected = available.some(group => group.dataset.resourceGroup === requested) ? requested : '';
    let count = 0;
    for (const group of groups) {
      group.hidden = !available.includes(group) || Boolean(selected && group.dataset.resourceGroup !== selected);
      if (!group.hidden) count += group.querySelectorAll('.resource-card:not([hidden])').length;
    }
    for (const link of document.querySelectorAll('.resource-filters a')) {
      const category = link.hash.split('/')[1];
      link.hidden = Boolean(category && !available.some(group => group.dataset.resourceGroup === category));
      if (link.hash === '#resources' + (selected ? '/' + selected : '')) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    }
    $('resource-catalog').hidden = !available.length;
    $('resource-count').textContent = count + (count === 1 ? ' resource' : ' resources');
    $('resource-status').textContent = resourceChoices
      ? available.length ? '' : 'Your teacher has not selected any resources yet.'
      : resourcesError ? 'Your resources could not be loaded. Please try again.' : 'Loading your resources…';
    $('retry-resources').hidden = !resourcesError;
    document.title = 'English resources · English Ladder';
    if (focus) $('resources-title').focus();
  }
  async function loadResources(force = false) {
    if (!authenticated || location.hash.slice(1).split('/')[0] !== 'resources' || resourcesLoading || resourceChoices && !force) return;
    const identity = identityRevision, revision = ++resourcesRevision;
    resourcesLoading = true; resourcesError = false; resourceChoices = null; renderResources();
    try {
      const data = await api('/api/account');
      if (identity !== identityRevision || revision !== resourcesRevision) return;
      if (!Number.isInteger(data.revision) || !Array.isArray(data.visibleResources) ||
          new Set(data.visibleResources).size !== data.visibleResources.length ||
          data.visibleResources.some(id => typeof id !== 'string' || !/^[a-z0-9-]{1,60}$/.test(id)))
        throw new Error('Resources unavailable');
      resourceChoices = data.visibleResources;
      renderResources();
    } catch (error) {
      if (identity !== identityRevision || revision !== resourcesRevision || expired(error)) return;
      resourcesError = true; renderResources();
    } finally { if (identity === identityRevision && revision === resourcesRevision) resourcesLoading = false; }
  }
  function navigate(focus = false) {
    if (!authenticated) return;
    const [part, requested, extra] = location.hash.slice(1).split('/');
    const selected = part === 'quiz-results' && !teacherMode ? 'quiz' : sections.includes(part) ? part : 'feedback';
    if (selected !== 'activities' || requested !== 'english-road' || extra !== undefined) roadPractice.clear();
    if (selected !== 'activities' || requested !== 'grammar-practice' || extra !== undefined) grammarPractice.clear();
    if (selected !== 'activities' || requested !== 'business-terms' || extra !== undefined) businessTerms.clear();
    if (selected !== 'activities' || requested !== 'vocabulary-practice' || extra !== undefined) vocabularyPractice.clear(true);
    if (selected !== 'account') clearSettings();
    if (selected !== 'activities') clearActivityCatalog();
    if (selected !== 'resources') clearResources();
    if (selected !== 'assessments') studyPractice.clear();
    else if ($('study-topics') && !$('study-topics').children.length && assessment) studyPractice.open($('study-topics'), assessment.plan, teacherMode);
    for (const id of sections) $(id).hidden = selected !== id;
    for (const el of document.querySelectorAll('.section-nav a')) {
      if (el.hash === '#' + selected || selected === 'activities' && el.hash === '#activities/' + requested) el.setAttribute('aria-current', 'page');
      else el.removeAttribute('aria-current');
    }
    activitiesDropdown.group.classList.toggle('is-current', selected === 'activities');
    overviewMenu.classList.toggle('is-current', ['overview', 'assessments', 'quiz', 'sessions', 'feedback'].includes(selected));
    if (selected !== 'feedback') {
      pageRevision++; currentPage = '';
      document.title = selected === 'assessments' ? 'My English assessment · English Ladder' : 'My learning space · English Ladder';
      if (selected === 'assessments') focusAssessment(requested, focus);
      if (selected === 'quiz') {
        document.title = 'My English quiz · English Ladder';
        if (focus) $('quiz-question-title')?.focus();
      }
      if (selected === 'quiz-results') {
        document.title = 'Quiz results · English Ladder';
        loadQuizResults();
        if (focus) $('quiz-results-title').focus();
      }
      if (selected === 'activities') { renderActivityPage(); void loadActivities(); if (focus) $('activity-title').focus(); }
      if (selected === 'resources') { renderResources(extra === undefined ? requested : '', focus); void loadResources(); }
      if (selected === 'account') {
        document.title = 'My account · English Ladder';
        loadSettings();
        if (focus) $('account-title').focus();
      }
      return;
    }
    if (extra !== undefined || (requested && !validId.test(requested))) {
      pageRevision++; currentPage = ''; markCurrent('');
      messagePage('This session link is not valid. Choose a session from your notebook.'); return;
    }
    const id = requested || sessions[0]?.id;
    if (id) { markCurrent(id); if (currentPage !== id) loadPage(id, focus); }
    else if (indexReady) messagePage('Your session feedback will appear here after your teacher adds it.');
    else if (indexLoading) messagePage('Opening your session notebook…');
  }
  function renderIndex() {
    for (const id of ['session-list', 'session-select', 'session-summaries']) $(id).replaceChildren();
    for (const s of sessions) {
      $('session-list').append(link(s, 'session-link'));
      const option = node('option', date(s) + ' · ' + s.title);
      option.value = s.id; $('session-select').append(option);
      const card = node('div', '', 'session-summary');
      card.append(link(s), node('p', s.summary)); $('session-summaries').append(card);
    }
    const count = sessions.length + (nextCursor ? '+' : '');
    $('session-list-status').textContent = sessions.length ? count + ' sessions · English language feedback' : 'No sessions yet';
    $('session-count').textContent = count + ' sessions';
    $('feedback-count').textContent = count + ' feedback pages';
    $('more-sessions').hidden = !nextCursor;
    if (sessions.length) {
      $('latest-title').textContent = sessions[0].title;
      $('latest-summary').textContent = sessions[0].summary;
      $('latest-link').href = '#feedback/' + sessions[0].id;
    } else $('session-summaries').append(node('p', 'No session summaries have been added yet.'));
  }
  async function loadIndex(more = false) {
    if (indexLoading || !authenticated) return;
    indexLoading = true;
    const revision = identityRevision;
    $('retry-feedback').hidden = true; $('more-sessions').disabled = true;
    try {
      const data = await api('/api/feedback' + (more && nextCursor ? '?before=' + encodeURIComponent(nextCursor) : ''));
      if (revision !== identityRevision) return;
      sessions = more ? [...sessions, ...data.sessions] : data.sessions;
      nextCursor = data.nextCursor; indexReady = true;
      renderIndex(); navigate();
    } catch (error) {
      if (revision !== identityRevision || expired(error)) return;
      $('session-list-status').textContent = error.message;
      $('session-count').textContent = 'Sessions unavailable'; $('feedback-count').textContent = 'Feedback unavailable';
      $('retry-feedback').hidden = false;
      if (!currentPage) messagePage('Your feedback could not be loaded.', () => loadIndex());
    } finally {
      if (revision === identityRevision) { indexLoading = false; $('more-sessions').disabled = false; }
    }
  }
  function section(title, className) {
    const el = node('section', '', className); el.append(node('h3', title)); return el;
  }
  function renderPage(record, focus) {
    const fragment = document.createDocumentFragment();
    const header = node('header', '', 'feedback-header');
    header.append(node('p', 'SESSION FEEDBACK / ENGLISH ONLY', 'eyebrow'));
    const title = node('h2', record.title); title.id = 'feedback-title'; title.tabIndex = -1;
    const dates = node('div', '', 'feedback-dates');
    dates.append(node('strong', date(record)), node('span', 'New York: ' + date(record, 'America/New_York', true)), node('span', 'Japan: ' + date(record, 'Asia/Tokyo', true)));
    header.append(title, dates, node('p', record.summary, 'session-reflection')); fragment.append(header);
    const strengths = section('What worked well', 'feedback-strengths');
    for (const item of record.strengths) {
      const card = node('div', '', 'strength');
      card.append(node('h4', item.title), node('p', item.detail)); strengths.append(card);
    }
    fragment.append(strengths);
    const points = section('Things to practice', 'feedback-focus');
    record.focus.forEach((item, i) => {
      const card = node('section', '', 'focus-card'), heading = node('div', '', 'focus-heading');
      heading.append(node('span', String(i + 1).padStart(2, '0'), 'focus-number'), node('h4', item.title));
      card.append(heading, node('p', item.kind === 'teacher-feedback' ? 'From this lesson' : 'Extra practice', 'evidence-label'), node('p', item.observed, 'observed'));
      const model = node('div', '', 'model-sentence');
      model.append(node('span', 'TRY SAYING THIS'), node('p', item.model));
      const ai = window.PracticePrompt.create({
        label: ' for practice topic ' + (i + 1),
        prompt: window.PracticePrompt.text(
          'English practice topic: ' + item.title + '\nModel sentence: “' + item.model + '”\nExplanation: ' + item.explanation,
          'Explain the language pattern and how the model sentence uses it. Focus only on the English, not on the learner.'
        ),
      });
      const promptControls = node('div', '', 'practice-prompt-controls'); promptControls.append(ai.controls, ai.status);
      card.append(model, node('p', item.explanation), promptControls); points.append(card);
    });
    fragment.append(points);
    const words = section('Useful language', 'feedback-vocabulary');
    words.append(node('p', 'These are new sentences for you to practice.', 'section-intro'));
    for (const item of record.vocabulary) {
      const row = node('div', '', 'vocabulary-row');
      const ai = window.PracticePrompt.create({
        label: ' for “' + item.term + '”',
        prompt: window.PracticePrompt.text(
          'English word or phrase: “' + item.term + '”\nMeaning: ' + item.meaning + '\nExample sentence: “' + item.example + '”',
          'Explain the meaning and how to use this word or phrase. Explain its use in the example sentence and common mistakes to avoid.'
        ),
      });
      const promptControls = node('div', '', 'practice-prompt-controls'); promptControls.append(ai.controls, ai.status);
      row.append(node('h4', item.term, 'vocabulary-term'), node('p', item.meaning), node('p', item.example, 'vocabulary-example'), promptControls); words.append(row);
    }
    fragment.append(words);
    const practice = section('A few minutes of practice', 'feedback-practice');
    record.practice.forEach((item, i) => {
      const row = node('div', '', 'practice-item'), answer = node('details');
      row.append(node('p', (i + 1) + '. ' + item.prompt));
      answer.append(node('summary', 'Show an example answer'), node('p', item.answer));
      const ai = window.PracticePrompt.create({
        label: ' for practice item ' + (i + 1),
        prompt: window.PracticePrompt.text(
          'English practice exercise:\n' + item.prompt + '\n\nExample answer: “' + item.answer + '”',
          'Explain how to do this exercise and why the example answer works. It is one possible answer; other answers may also work. Focus only on the English in this exercise.'
        ),
      });
      const promptControls = node('div', '', 'practice-prompt-controls'); promptControls.append(ai.controls, ai.status);
      row.append(answer, promptControls); practice.append(row);
    });
    fragment.append(practice);
    const next = section('Your next step', 'feedback-next-step'); next.append(node('p', record.nextStep)); fragment.append(next);
    const sources = node('details', '', 'feedback-source');
    sources.append(node('summary', 'How we made this feedback'));
    sources.append(node('p', 'AI helped write this page. We used all the available text from this lesson.'));
    sources.append(node('p', 'This page is only about your English. The lesson text was made by a computer, so some words may be wrong. We show what you practiced with Phil and label extra practice. The example sentences are for practice; they may be new. We cannot check how you say words from text alone.'));
    fragment.append(sources);
    const position = sessions.findIndex(s => s.id === record.id), navigation = node('nav', '', 'feedback-pager');
    navigation.setAttribute('aria-label', 'Other feedback pages');
    if (position >= 0) {
      for (const [s, label] of [[sessions[position + 1], '← Earlier session'], [sessions[position - 1], 'Later session →']]) {
        if (!s) continue;
        const el = link(s, 'pager-link'); el.prepend(node('strong', label)); navigation.append(el);
      }
    }
    fragment.append(navigation);
    $('feedback-page').replaceChildren(fragment); $('feedback-page').setAttribute('aria-busy', 'false');
    document.title = date(record) + ' · Session feedback · English Ladder';
    if (focus) title.focus();
  }
  async function loadPage(id, focus = false) {
    const revision = ++pageRevision, identity = identityRevision;
    currentPage = id; messagePage('Opening this session’s feedback…'); $('feedback-page').setAttribute('aria-busy', 'true');
    try {
      const record = await api('/api/feedback/' + encodeURIComponent(id));
      if (revision !== pageRevision || identity !== identityRevision) return;
      renderPage(record, focus);
    } catch (error) {
      if (revision !== pageRevision || identity !== identityRevision || expired(error)) return;
      currentPage = ''; messagePage(error.message, error.status === 404 ? null : () => loadPage(id, true));
    }
  }
  function assessmentDate(day) {
    return new Intl.DateTimeFormat('en-US', { timeZone: 'UTC', month: 'short', day: 'numeric', year: 'numeric' }).format(new Date(day + 'T12:00:00Z'));
  }
  function evidenceLink(ref) {
    const el = node('a', assessmentDate(ref.sessionId.slice(0, 10)), 'assessment-evidence');
    el.href = '#feedback/' + ref.sessionId;
    el.setAttribute('aria-label', 'Open lesson feedback for ' + assessmentDate(ref.sessionId.slice(0, 10)));
    return el;
  }
  function evidenceList(refs) {
    const details = node('details', '', 'assessment-references');
    const sessions = [...new Map(refs.map(ref => [ref.sessionId, ref])).values()];
    details.append(node('summary', 'From your ' + (sessions.length === 1 ? 'lesson' : 'lessons')));
    const list = node('div');
    for (const ref of sessions) list.append(evidenceLink(ref));
    details.append(list); return details;
  }
  function markAssessmentSection(key) {
    for (const el of document.querySelectorAll('.assessment-outline a')) {
      if (el.hash === '#assessments/' + key) el.setAttribute('aria-current', 'location');
      else el.removeAttribute('aria-current');
    }
  }
  function scheduleAssessmentHighlight() {
    if (assessmentScrollFrame || !authenticated || !assessment || $('assessments').hidden) return;
    assessmentScrollFrame = requestAnimationFrame(() => {
      assessmentScrollFrame = 0;
      if (!authenticated || !assessment || $('assessments').hidden) return;
      // Follow the section at the reading line, including long sections whose
      // headings have already scrolled off screen. Do not move focus or history.
      // Section jumps leave 16px of scroll padding and 24px of heading margin.
      const readingLine = Math.max(stickyHeader.getBoundingClientRect().height + 48, Math.min(160, window.innerHeight * 0.2));
      let current = assessmentSections[0];
      for (const key of assessmentSections) {
        if ($('assessment-' + key).getBoundingClientRect().top <= readingLine) current = key;
      }
      // A short final section may never reach the reading line.
      if (window.scrollY > 0 && window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) current = assessmentSections.at(-1);
      markAssessmentSection(current);
    });
  }
  function focusAssessment(requested, focus) {
    if (!assessment) return;
    const key = assessmentSections.includes(requested) ? requested : 'summary';
    markAssessmentSection(key);
    const heading = $('assessment-' + key);
    if (focus) heading.focus({ preventScroll: true });
    if (requested) heading.scrollIntoView?.({ block: 'start' });
    scheduleAssessmentHighlight();
  }
  function assessmentSection(title, key, className) {
    const el = section(title, className), heading = el.querySelector('h3');
    heading.id = 'assessment-' + key; heading.tabIndex = -1;
    return el;
  }
  function assessmentMessage(message, retry) {
    const content = node('div', '', 'feedback-message');
    content.append(node('h2', 'Your English assessment'), node('p', message));
    if (retry) {
      const button = node('button', 'Try again', 'secondary-button');
      button.addEventListener('click', loadAssessment); content.append(button);
    }
    $('assessment-content').replaceChildren(content);
    $('assessment-content').setAttribute('aria-busy', String(assessmentLoading));
  }
  function renderAssessment(record) {
    const fragment = document.createDocumentFragment(), header = node('header', '', 'feedback-header');
    header.append(node('p', 'OVERALL ASSESSMENT / ENGLISH ONLY', 'eyebrow'));
    const title = node('h2', record.title); title.id = 'assessment-title';
    const dates = node('div', '', 'feedback-dates');
    dates.append(node('strong', 'Assessed ' + assessmentDate(record.assessedOn)), node('span', record.sourceSessions.length + ' sessions · ' + assessmentDate(record.sourceSessions[0].slice(0, 10)) + ' – ' + assessmentDate(record.sourceSessions.at(-1).slice(0, 10))));
    header.append(title, dates);
    const summary = assessmentSection('Your English now', 'summary', 'assessment-overview');
    summary.append(node('p', record.summary, 'session-reflection'));
    const priority = node('div', '', 'assessment-priority');
    priority.append(node('span', 'START HERE'), node('p', record.mainPriority)); summary.append(priority);
    if (record.quiz) {
      const quizLink = node('a', 'Try the ' + record.quiz.questions.length + '-question quiz →', 'secondary-button assessment-quiz-link');
      quizLink.href = '#quiz'; summary.append(quizLink);
    }
    fragment.append(header, summary);
    const strengths = assessmentSection('What you do well', 'strengths', 'feedback-strengths');
    for (const item of record.strengths) {
      const card = node('div', '', 'strength');
      card.append(node('h4', item.title), node('p', item.detail), evidenceList(item.evidence)); strengths.append(card);
    }
    fragment.append(strengths);
    const progress = section('Your progress', 'assessment-progress');
    progress.append(node('p', record.progress.detail), evidenceList(record.progress.evidence)); fragment.append(progress);
    const patterns = assessmentSection('Things to practice', 'patterns', 'feedback-focus');
    patterns.append(node('p', 'These are things you practiced with Phil. The sentences under “Try saying this” are for practice; some are new.', 'section-intro'));
    record.patterns.forEach((item, index) => {
      const card = node('section', '', 'focus-card'), heading = node('div', '', 'focus-heading');
      heading.append(node('span', String(index + 1).padStart(2, '0'), 'focus-number'), node('h4', item.title));
      card.append(heading, node('p', item.detail));
      for (const example of item.examples) {
        const row = node('div', '', 'assessment-example');
        row.append(evidenceLink(example), node('p', example.observed, 'observed'));
        const model = node('div', '', 'model-sentence');
        model.append(node('span', 'TRY SAYING THIS'), node('p', example.model)); row.append(model); card.append(row);
      }
      const practice = node('p', '', 'assessment-practice');
      practice.append(node('strong', 'Practice: '), document.createTextNode(item.practice));
      const ai = window.PracticePrompt.create({
        label: ' for assessment practice topic ' + (index + 1),
        prompt: window.PracticePrompt.text(
          'English practice topic: ' + item.title + '\nModel sentences:\n' +
          item.examples.map(example => '• “' + example.model + '”').join('\n') + '\n\nPractice suggestion: ' + item.practice,
          'Explain the language pattern and how the model sentences use it. Show how to follow the practice suggestion. Focus only on the English, not on assessing the learner.'
        ),
      });
      const promptControls = node('div', '', 'practice-prompt-controls'); promptControls.append(ai.controls, ai.status);
      card.append(practice, promptControls); patterns.append(card);
    });
    fragment.append(patterns);
    const plan = assessmentSection('Study on your own', 'next', 'assessment-plan');
    plan.append(node('p', 'Your lessons showed which parts of your English need more practice. We chose these topics to help you improve. Choose a topic. Copy its AI prompt and paste it into an AI chat.', 'section-intro'));
    const studyRoot = node('div'); studyRoot.id = 'study-topics'; plan.append(studyRoot);
    fragment.append(plan);
    const source = node('details', '', 'feedback-source');
    source.append(node('summary', 'How we made this assessment'), node('p', 'AI helped write this page. We used all the available text from each lesson below. Dates link to your lesson feedback.'));
    const list = node('div', '', 'assessment-source-links');
    for (const id of record.sourceSessions) { const el = node('a', assessmentDate(id.slice(0, 10))); el.href = '#feedback/' + id; list.append(el); }
    source.append(list, node('p', 'This page is only about your English. The lesson text was made by a computer, so some words may be wrong. We checked what you practiced with Phil and what you did well. This is not a test score or an official English level. We cannot check your pronunciation or speaking speed from text alone.'));
    fragment.append(source);
    $('assessment-content').replaceChildren(fragment);
    studyPractice.open(studyRoot, record.plan, teacherMode);
    $('assessment-content').setAttribute('aria-busy', 'false');
    $('assessment-sidebar').hidden = false;
    $('assessment-source-count').textContent = 'Based on ' + record.sourceSessions.length + ' lessons';
    assessmentResizeObserver?.observe($('assessment-content'));
  }
  async function loadAssessment() {
    if (assessmentLoading || !authenticated) return;
    assessmentLoading = true;
    const revision = identityRevision;
    assessmentMessage('Opening your assessment…');
    quizMessage('Opening your quiz…');
    $('quiz-content').setAttribute('aria-busy', 'true');
    try {
      const data = await api('/api/assessment');
      if (revision !== identityRevision) return;
      assessment = data.assessment;
      resetQuiz();
      $('assessment-count').textContent = assessment ? 'Overall assessment · ' + assessmentDate(assessment.assessedOn) : 'No assessments yet';
      if (assessment) {
        renderAssessment(assessment);
        if (location.hash.split('/')[0] === '#assessments') focusAssessment(location.hash.split('/')[1], false);
      } else assessmentMessage('Your teacher’s assessment of your English and areas to focus on will appear here.');
    } catch (error) {
      if (revision !== identityRevision || expired(error)) return;
      $('assessment-count').textContent = 'Assessment unavailable';
      assessmentMessage('Your assessment could not be loaded. ' + error.message, true);
      quizMessage('Your quiz could not be loaded. Please try again.', true);
    } finally {
      if (revision === identityRevision) {
        assessmentLoading = false;
        $('assessment-content').setAttribute('aria-busy', 'false');
        $('quiz-content').setAttribute('aria-busy', 'false');
      }
    }
  }
  function quizMessage(message, retry = false) {
    const heading = node('h2', 'Your English quiz'); heading.id = 'quiz-question-title'; heading.tabIndex = -1;
    $('quiz-content').replaceChildren(heading, node('p', message, 'section-intro'));
    if (retry) {
      const button = node('button', 'Try again', 'secondary-button');
      button.addEventListener('click', () => loadAssessment()); $('quiz-content').append(button);
    }
  }
  function resetQuiz(focus = false) {
    if (!teacherMode) { loadSavedQuiz(false, focus); return; }
    quizRevision++;
    quizState = assessment?.quiz ? { quiz: assessment.quiz, patternTitles: assessment.quiz.patternTitles || assessment.patterns.map(p => p.title), sourceSessions: assessment.quiz.sourceSessions || assessment.sourceSessions, index: 0, answers: assessment.quiz.questions.map(() => []), finished: false } : null;
    $('quiz-nav').hidden = !quizState;
    if (quizState) renderQuiz(focus);
    else quizMessage('Your teacher can add a quiz here.');
  }
  function useSavedQuiz(data, focus = false) {
    const attempt = data.attempt, quiz = data.quiz;
    $('quiz-nav').hidden = !quiz;
    if (!quiz) { quizState = null; quizMessage('Your teacher can add a quiz here.'); return; }
    const answers = attempt?.answers || quiz.questions.map(() => []);
    const pending = answers.findIndex((a, i) => !a.includes(quiz.questions[i].correctIndex));
    quizState = {
      quiz, patternTitles: data.patternTitles, sourceSessions: data.sourceSessions, version: data.version, id: attempt?.id || crypto.randomUUID(),
      answers, index: pending < 0 ? quiz.questions.length - 1 : pending, finished: Boolean(attempt?.completedAt),
      pending: null, saving: false, saveError: null, saved: Boolean(attempt),
    };
    renderQuiz(focus);
  }
  async function loadSavedQuiz(fresh = false, focus = false) {
    const run = ++quizRevision, identity = identityRevision;
    quizState = null; $('quiz-nav').hidden = true; quizMessage('Opening your saved quiz…');
    try {
      const data = await api('/api/quiz/state' + (fresh ? '?new=1' : ''));
      if (!authenticated || run !== quizRevision || identity !== identityRevision) return;
      useSavedQuiz(data, focus);
    } catch (error) {
      if (run !== quizRevision || identity !== identityRevision || expired(error)) return;
      quizMessage('Your quiz could not be loaded. Please try again.', true);
    }
  }
  function quizSources(sourceSessions) {
    const sources = node('div', '', 'quiz-sources');
    const dates = [...new Set((sourceSessions || []).map(id => id.slice(0, 10)))].sort();
    sources.append(node('p', 'Based on your ' + (sourceSessions?.length === 1 ? 'lesson' : 'lessons') + ': ' + dates.map(assessmentDate).join(' · ')));
    return sources;
  }
  function renderQuiz(focus = false) {
    if (!authenticated || !quizState) return;
    const quiz = quizState.quiz, run = quizRevision, identity = identityRevision, index = quizState.index;
    const currentRun = () => authenticated && run === quizRevision && identity === identityRevision;
    const fragment = document.createDocumentFragment();
    const header = node('header', '', 'quiz-header');
    header.append(node('p', 'NEW PRACTICE', 'eyebrow'), node('h2', quiz.title));
    header.append(quizSources(quizState.sourceSessions));
    fragment.append(header);
    if (quizState.finished) {
      const complete = node('section', '', 'quiz-complete');
      const heading = node('h3', 'You finished!'); heading.id = 'quiz-question-title'; heading.tabIndex = -1;
      const correct = quizState.answers.filter((answers, i) => answers[0] === quiz.questions[i].correctIndex).length;
      complete.append(heading, node('p', correct + ' of ' + quiz.questions.length, 'quiz-score'), node('p', 'You got ' + correct + ' out of ' + quiz.questions.length + ' right on your first try.'));
      complete.append(node('p', 'You practiced every question. You can try the quiz again.', 'section-intro'));
      if (!teacherMode) complete.append(node('p', 'Saved. Phil can see your results.', 'quiz-save-note'));
      const review = [...new Set(quiz.questions.filter((q, i) => quizState.answers[i][0] !== q.correctIndex).map(q => q.patternIndex))];
      if (review.length) {
        complete.append(node('h4', 'Practice these again'));
        const list = node('ul');
        for (const patternIndex of review) list.append(node('li', quizState.patternTitles[patternIndex]));
        complete.append(list);
      }
      const restart = node('button', 'Try the quiz again', 'primary-button');
      restart.addEventListener('click', () => { if (currentRun()) teacherMode ? resetQuiz(true) : loadSavedQuiz(true, true); });
      complete.append(restart); fragment.append(complete);
      $('quiz-content').replaceChildren(fragment);
      if (focus) heading.focus();
      return;
    }
    const question = quiz.questions[index], tried = quizState.answers[index];
    const complete = tried.includes(question.correctIndex);
    const counter = node('p', 'Question ' + (index + 1) + ' of ' + quiz.questions.length, 'quiz-counter');
    const progress = node('progress'); progress.max = quiz.questions.length; progress.value = index + 1;
    progress.setAttribute('aria-label', counter.textContent);
    const heading = node('h3', question.prompt, 'quiz-prompt'); heading.id = 'quiz-question-title'; heading.tabIndex = -1;
    const choices = node('div', '', 'quiz-choices'); choices.setAttribute('role', 'group'); choices.setAttribute('aria-labelledby', heading.id);
    const result = node('div', '', 'quiz-result'); result.id = 'quiz-result'; result.setAttribute('role', 'status'); result.setAttribute('aria-live', 'polite'); result.setAttribute('aria-atomic', 'true');
    const answer = question.options[question.correctIndex];
    const ai = window.PracticePrompt.create({
      label: ' for question ' + (index + 1),
      prompt: window.PracticePrompt.text(
        'English quiz exercise:\n' + question.prompt + '\n\nChoices:\n' +
        question.options.map((option, i) => String.fromCharCode(65 + i) + '. “' + option.text + '”').join('\n') +
        '\n\nAnswer key: “' + answer.text + '”\nExplanation: ' + answer.feedback + '\nModel sentence: “' + question.model + '”',
        'Explain why the answer fits and why the other choices do not. Explain the model sentence. Focus only on the English in this exercise.'
      ),
    });
    const promptControls = node('div', '', 'practice-prompt-controls'); promptControls.append(ai.controls, ai.status);
    const next = node('button', index === quiz.questions.length - 1 ? 'See my results' : 'Next question →', 'primary-button quiz-next');
    const saveStatus = node('p', '', 'quiz-save-status'); saveStatus.setAttribute('role', 'status');
    const retrySave = node('button', 'Save my answer again', 'secondary-button'); retrySave.hidden = true;
    retrySave.addEventListener('click', () => {
      if (!currentRun() || quizState.saving) return;
      if (quizState.saveError?.status === 409) loadSavedQuiz(false, true);
      else saveAnswer();
    });
    next.hidden = !complete;
    const buttons = question.options.map((option, choice) => {
      const button = node('button', '', 'quiz-option'); button.type = 'button';
      const letter = node('span', String.fromCharCode(65 + choice), 'quiz-letter'); letter.setAttribute('aria-hidden', 'true');
      button.append(letter, node('em', option.text), node('span', '', 'quiz-option-status'));
      button.addEventListener('click', () => {
        if (!currentRun() || quizState.finished || quizState.pending || quizState.index !== index || tried.includes(choice) || tried.includes(question.correctIndex)) return;
        tried.push(choice);
        if (!teacherMode) {
          quizState.pending = { attemptId: quizState.id, version: quizState.version, questionIndex: index, choiceIndex: choice };
          saveAnswer();
        } else updateAnswer();
        (tried.includes(question.correctIndex) ? next : result).scrollIntoView?.({ block: 'nearest' });
      });
      choices.append(button); return button;
    });
    async function saveAnswer() {
      if (!currentRun() || !quizState.pending || quizState.saving) return;
      quizState.saving = true; quizState.saveError = null; updateAnswer();
      try {
        const data = await api('/api/quiz/answer', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(quizState.pending) });
        if (!currentRun()) return;
        quizState.saving = false; quizState.pending = null; quizState.saved = true;
        if (JSON.stringify(data.attempt.answers) !== JSON.stringify(quizState.answers)) {
          useSavedQuiz({ ...data.attempt, attempt: data.attempt }, true); return;
        }
        updateAnswer();
        (tried.includes(question.correctIndex) ? next : buttons.find(b => !b.disabled))?.focus({ preventScroll: true });
      } catch (error) {
        if (!currentRun() || expired(error)) return;
        quizState.saving = false; quizState.saveError = error; updateAnswer();
        retrySave.focus({ preventScroll: true }); retrySave.scrollIntoView?.({ block: 'nearest' });
      }
    }
    function updateAnswer() {
      const solved = tried.includes(question.correctIndex), choice = tried.at(-1);
      const hadChoiceFocus = buttons.includes(document.activeElement);
      buttons.forEach((button, i) => {
        const chosen = tried.includes(i), right = chosen && i === question.correctIndex;
        button.disabled = solved || chosen || Boolean(quizState.pending);
        button.classList.toggle('is-correct', right); button.classList.toggle('is-wrong', chosen && !right);
        button.querySelector('.quiz-option-status').textContent = chosen ? (right ? 'Correct' : 'Try again') : '';
      });
      next.hidden = !solved;
      next.disabled = Boolean(quizState.pending);
      saveStatus.textContent = teacherMode ? '' : quizState.saving ? 'Saving your answer…' : quizState.saveError ? (quizState.saveError.status === 409 ? 'Your quiz changed in another tab. Load your saved quiz to continue.' : 'Your answer may not be saved yet. Keep this page open and try saving again.') : quizState.saved ? 'Saved.' : '';
      retrySave.hidden = !quizState.saveError;
      retrySave.textContent = quizState.saveError?.status === 409 ? 'Load my saved quiz' : 'Save my answer again';
      if (choice === undefined) return;
      result.className = 'quiz-result ' + (solved ? 'is-correct' : 'is-wrong');
      result.replaceChildren(node('strong', solved ? 'That’s right!' : 'Not yet. Try again.'), node('p', question.options[choice].feedback));
      if (solved) result.append(node('p', question.model, 'quiz-model'));
      // Keep keyboard users in the quiz after their answer button is disabled.
      if (hadChoiceFocus) {
        if (solved) next.focus({ preventScroll: true });
        else buttons.find(button => !button.disabled)?.focus({ preventScroll: true });
      }
    }
    next.addEventListener('click', () => {
      if (!currentRun() || quizState.finished || quizState.pending || quizState.index !== index || !tried.includes(question.correctIndex)) return;
      if (index === quiz.questions.length - 1) quizState.finished = true;
      else quizState.index++;
      renderQuiz(true);
    });
    fragment.append(counter, progress, heading, node('p', quiz.instructions, 'quiz-hint'), choices, result, saveStatus, retrySave, promptControls, next);
    $('quiz-content').replaceChildren(fragment); updateAnswer();
    if (focus) heading.focus();
  }
  function quizDate(value) {
    return new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', second: '2-digit' }).format(new Date(value));
  }
  async function loadAutomationStatus() {
    const identity = identityRevision;
    try {
      const data = await api('/api/automation/status');
      if (!authenticated || !teacherMode || identity !== identityRevision) return;
      const panel = $('quiz-automation'); panel.hidden = false;
      const message = !data.configured ? 'The server setup is waiting for its Zoom app connection.'
        : data.connectionError === 'zoom_reconnect' ? 'Zoom needs attention. Please connect it again.'
        : data.connectionError ? 'The last Zoom check could not finish. It will try again tomorrow.'
        : !data.connected ? 'Connect Zoom for nightly lesson updates. Your computer can be off.'
        : !data.enabled ? 'Zoom is connected. Nightly updates are waiting to be switched on.'
        : 'Nightly updates are on. Your computer can be off.';
      panel.replaceChildren(node('h3', 'Nightly lesson updates'), node('p', message));
      panel.append(node('p', 'Every night at 1 a.m. Eastern time. The time adjusts for daylight saving.'));
      if (data.lastCheck) panel.append(node('p', 'Last check: ' + quizDate(data.lastCheck), 'section-intro'));
      if (data.costLimitReached) panel.append(node('p', 'The spending limit has been reached. More updates are waiting.'));
      if (data.needsAttention) panel.append(node('p', 'Some lessons need a check before their pages can be updated.'));
      if (data.latestPublication) panel.append(node('p', 'Latest update: ' + quizDate(data.latestPublication), 'section-intro'));
      if (data.configured && (!data.connected || data.connectionError === 'zoom_reconnect')) {
        const connect = node('button', 'Connect Zoom', 'secondary-button'); panel.append(connect);
        connect.addEventListener('click', async () => {
          connect.disabled = true;
          try {
            const result = await api('/api/automation/connect', { method: 'POST', body: '{}' });
            if (!authenticated || !teacherMode || identity !== identityRevision) return;
            const destination = new URL(result.url);
            if (destination.origin !== 'https://zoom.us' || destination.pathname !== '/oauth/authorize') throw new Error('Invalid Zoom link');
            location.assign(destination.href);
          } catch (error) {
            if (identity !== identityRevision || expired(error)) return;
            connect.disabled = false; panel.append(node('p', 'Zoom could not be opened. Please try again.'));
          }
        });
      }
    } catch (error) {
      if (identity !== identityRevision || expired(error)) return;
      $('quiz-automation').hidden = true;
    }
  }
  async function loadQuizResults(append = false) {
    if (!authenticated || !teacherMode || resultsLoading) return;
    if (!append) loadAutomationStatus();
    resultsLoading = true;
    const revision = ++resultsRevision, identity = identityRevision;
    $('quiz-results-status').textContent = 'Loading saved results…';
    $('refresh-quiz-results').disabled = true; $('more-quiz-results').disabled = true;
    try {
      const data = await api('/api/quiz/results' + (append && resultCursor ? '?before=' + encodeURIComponent(resultCursor) : ''));
      if (!teacherMode || identity !== identityRevision || revision !== resultsRevision) return;
      resultRows = append ? [...resultRows, ...data.attempts] : data.attempts;
      resultCursor = data.nextCursor;
      renderQuizResults();
      $('quiz-results-status').textContent = resultRows.length ? resultRows.length + ' saved attempts shown.' : 'No saved attempts yet. Results will appear after the student answers a question. Earlier quizzes were not saved.';
    } catch (error) {
      if (identity !== identityRevision || revision !== resultsRevision || expired(error)) return;
      $('quiz-results-status').textContent = 'Results could not be loaded. Use “Refresh results” to try again.';
    } finally {
      if (identity === identityRevision && revision === resultsRevision) {
        resultsLoading = false; $('refresh-quiz-results').disabled = false; $('more-quiz-results').disabled = false;
        $('more-quiz-results').hidden = !resultCursor;
      }
    }
  }
  function renderQuizResults() {
    const fragment = document.createDocumentFragment(), groups = new Map();
    for (const row of [...resultRows].reverse()) {
      if (!groups.has(row.version)) groups.set(row.version, []);
      groups.get(row.version).push(row);
    }
    if (resultRows.some(row => row.completedAt)) {
      const trends = node('section', '', 'quiz-trends');
      trends.append(node('h3', 'Progress over time'), node('p', 'First-try scores for completed attempts shown below. Each set uses the same questions. Repeating a quiz is practice, not a measure of overall English level.', 'section-intro'));
      let set = 0;
      for (const rows of groups.values()) {
        set++;
        const completed = rows.filter(row => row.completedAt);
        if (!completed.length) continue;
        trends.append(node('h4', 'Set ' + set + ' · ' + rows[0].title));
        const list = node('ol', '', 'quiz-trend-list');
        for (const row of completed) {
          const item = node('li'), label = quizDate(row.startedAt), score = row.firstTryCorrect + ' / ' + row.total;
          const progress = node('progress'); progress.max = row.total; progress.value = row.firstTryCorrect; progress.setAttribute('aria-label', label + ': ' + score + ' on the first try');
          item.append(node('span', label), progress, node('strong', score)); list.append(item);
        }
        trends.append(list);
      }
      fragment.append(trends);
    }
    const heading = node('h3', 'Attempts · newest first'); if (resultRows.length) fragment.append(heading);
    for (const row of resultRows) {
      const card = node('article', '', 'quiz-attempt-card');
      card.append(node('h4', quizDate(row.startedAt)), node('p', row.title, 'section-intro'));
      card.append(node('p', row.completedAt ? 'Finished · ' + row.firstTryCorrect + ' of ' + row.total + ' right on the first try' : 'In progress · ' + row.answered + ' of ' + row.total + ' questions tried · ' + row.firstTryCorrect + ' right on the first try', 'quiz-attempt-score'));
      card.append(node('p', row.missedQuestions.length ? 'Wrong on the first try: ' + row.missedQuestions.map(n => 'Q' + n).join(', ') : row.answered ? 'No first-try mistakes so far.' : 'No answers yet.'));
      const details = node('details'), content = node('div', '', 'quiz-answer-history');
      details.append(node('summary', 'See each answer'), content); card.append(details);
      let loaded = false, loading = false;
      const revision = resultsRevision, identity = identityRevision;
      const current = () => teacherMode && authenticated && identity === identityRevision && revision === resultsRevision;
      const load = async () => {
        if (!current() || loaded || loading || !details.open) return;
        loading = true; content.replaceChildren(node('p', 'Loading answers…'));
        try {
          const data = await api('/api/quiz/results/' + row.id);
          if (!current()) return;
          const attempt = data.attempt; content.replaceChildren();
          content.append(quizSources(attempt.sourceSessions));
          content.append(node('p', 'Started ' + quizDate(attempt.startedAt) + (attempt.completedAt ? ' · Finished ' + quizDate(attempt.completedAt) : ' · Last saved ' + quizDate(attempt.updatedAt)), 'section-intro'));
          attempt.quiz.questions.forEach((question, i) => {
            const answers = attempt.answers[i], first = answers[0], wrong = first !== undefined && first !== question.correctIndex;
            const item = node('section', '', 'quiz-history-question' + (wrong ? ' first-try-wrong' : ''));
            item.append(node('h5', 'Question ' + (i + 1) + ' · ' + (first === undefined ? 'Not answered yet' : wrong ? 'Wrong on first try' : 'Right on first try')));
            item.append(node('p', question.prompt), node('p', attempt.patternTitles[question.patternIndex], 'section-intro'));
            if (first !== undefined) {
              const firstLine = node('p', 'First answer: '); firstLine.append(node('em', question.options[first].text)); item.append(firstLine);
              const correct = node('p', 'Correct answer: '); correct.append(node('em', question.options[question.correctIndex].text)); item.append(correct);
              if (answers.length > 1) {
                const retries = node('p', 'Later choices: ');
                answers.slice(1).forEach((choice, n) => { if (n) retries.append(document.createTextNode(' → ')); retries.append(node('em', question.options[choice].text)); }); item.append(retries);
              }
            }
            content.append(item);
          });
          loaded = true;
        } catch (error) {
          if (!current() || expired(error)) return;
          const retry = node('button', 'Try loading answers again', 'secondary-button'); retry.addEventListener('click', load);
          content.replaceChildren(node('p', 'Answers could not be loaded.'), retry);
        } finally { loading = false; }
      };
      details.addEventListener('toggle', load); fragment.append(card);
    }
    $('quiz-history').replaceChildren(fragment);
  }
  function applyActivityChoices(data) {
    if (!Number.isInteger(data.revision) || !Array.isArray(data.activities) || !Array.isArray(data.visibleActivities) ||
        data.activities.some(a => !a || !/^[a-z0-9-]{1,60}$/.test(a.id) || typeof a.name !== 'string' || typeof a.description !== 'string'))
      throw new Error('Your activities could not be loaded. Please try again.');
    // An earlier read can finish after a save. Never restore the older choices.
    if (activityChoices && data.revision < activityChoices.revision) return;
    activityChoices = { revision: data.revision, activities: data.activities.map(({ id, name, description, benefit, steps }) => ({
      id, name, description, benefit: typeof benefit === 'string' ? benefit : '',
      steps: Array.isArray(steps) && steps.every(step => typeof step === 'string') ? steps : [],
    })),
      visibleActivities: data.visibleActivities.filter(id => data.activities.some(a => a.id === id)) };
    activitiesError = false; renderActivities();
  }
  function renderActivities() {
    const list = activitiesDropdown.list;
    const selected = activityChoices?.activities.filter(a => activityChoices.visibleActivities.includes(a.id));
    list.replaceChildren();
    if (selected?.length) {
      for (const activity of selected) {
        const item = node('li'), link = node('a', activity.name);
        link.href = '#activities/' + activity.id;
        if (link.hash === location.hash) link.setAttribute('aria-current', 'page');
        item.append(link); list.append(item);
      }
    } else {
      const item = node('li', '', 'submenu-message');
      item.append(node('p', selected ? 'No activities yet. Please ask your teacher.' : activitiesError ? 'Your activities could not be loaded.' : 'Loading your activities…'));
      if (!selected && activitiesError) {
        const retry = node('button', 'Try again'); retry.type = 'button'; retry.addEventListener('click', loadActivities); item.append(retry);
      }
      list.append(item);
    }
    if (!list.hidden) positionDropdown(activitiesDropdown);
    renderActivityPage();
  }
  function clearActivityCatalog() {
    $('activity-catalog').replaceChildren(); $('activity-catalog').hidden = true;
    $('retry-activities').hidden = true;
    $('activity-title').parentElement.classList.remove('is-overview');
  }
  $('retry-activities').addEventListener('click', loadActivities);
  function renderActivityPage() {
    const [part, id, extra] = location.hash.slice(1).split('/');
    if (!authenticated || part !== 'activities') return;
    clearActivityCatalog();
    const activity = extra === undefined && activityChoices?.visibleActivities.includes(id) && activityChoices.activities.find(a => a.id === id);
    if (activity?.id === 'english-road') roadPractice.open(teacherMode); else roadPractice.clear();
    if (activity?.id === 'grammar-practice') grammarPractice.open(teacherMode); else grammarPractice.clear();
    if (activity?.id === 'business-terms') businessTerms.open(teacherMode); else businessTerms.clear();
    if (activity?.id === 'vocabulary-practice') vocabularyPractice.open(teacherMode); else vocabularyPractice.clear(true);
    $('activity-title').textContent = activity ? activity.name : 'Activities';
    $('activity-message').textContent = activity ? activity.description : !activityChoices
      ? (activitiesError ? 'Your activities could not be loaded. Please try again.' : 'Loading your activities…')
      : id ? 'Your teacher has not selected this activity for your menu.'
      : activityChoices.visibleActivities.length ? 'Choose an activity. Read what it helps you practice, then open it to begin.' : 'No activities yet. Please ask your teacher.';
    $('retry-activities').hidden = !activitiesError;
    if (!id && extra === undefined && activityChoices) {
      const catalog = $('activity-catalog');
      for (const tool of activityChoices.activities.filter(a => activityChoices.visibleActivities.includes(a.id))) {
        const card = node('article', '', 'activity-guide'), heading = node('h3', tool.name);
        heading.id = 'activity-guide-' + tool.id; card.setAttribute('aria-labelledby', heading.id);
        const why = node('p', '', 'activity-guide-label'); why.append(node('strong', 'Why try it?'));
        const how = node('p', '', 'activity-guide-label'); how.append(node('strong', 'How it works'));
        const steps = node('ol');
        for (const step of tool.steps.length ? tool.steps : [tool.description]) steps.append(node('li', step));
        const link = node('a', 'Open activity →', 'secondary-button');
        link.href = '#activities/' + tool.id; link.setAttribute('aria-label', 'Open ' + tool.name);
        card.append(heading, why, node('p', tool.benefit || tool.description), how, steps, link); catalog.append(card);
      }
      catalog.hidden = !catalog.children.length;
      $('activity-title').parentElement.classList.add('is-overview');
    }
    document.title = (activity ? activity.name : 'My activities') + ' · English Ladder';
  }
  async function loadActivities() {
    if (!authenticated || activitiesLoading) return;
    const identity = identityRevision, revision = ++activitiesRevision;
    activitiesLoading = true; activitiesError = false;
    if (!activityChoices) renderActivities();
    try {
      const data = await api('/api/account');
      if (identity !== identityRevision || revision !== activitiesRevision) return;
      applyActivityChoices(data);
    } catch (error) {
      if (identity !== identityRevision || revision !== activitiesRevision || expired(error)) return;
      activitiesError = true; renderActivities();
    } finally {
      if (identity === identityRevision && revision === activitiesRevision) activitiesLoading = false;
    }
  }
  function clearSettings() {
    settingsRevision++; settings = null; settingsLoading = false; settingsSaving = false;
    $('settings-form').reset(); $('password-form').reset();
    for (const id of ['settings-status', 'settings-message', 'password-message']) $(id).textContent = '';
    $('reload-settings').hidden = true; $('settings-teacher-note').hidden = true;
    $('settings-fields').disabled = true; $('password-fields').disabled = true;
  }
  function lockSettings(busy) {
    $('settings-fields').disabled = busy || teacherMode || !settings;
    $('password-fields').disabled = busy || teacherMode || !settings;
  }
  async function loadSettings(force = false) {
    if (!authenticated || settingsLoading || settingsSaving || settings && !force) return;
    settingsLoading = true; lockSettings(true);
    const identity = identityRevision, revision = ++settingsRevision;
    $('settings-message').textContent = ''; $('password-message').textContent = '';
    if (force) $('password-form').reset();
    $('settings-status').textContent = 'Loading your account…'; $('reload-settings').hidden = true;
    $('password-form').hidden = teacherMode; $('settings-teacher-note').hidden = !teacherMode;
    try {
      const data = await api('/api/account');
      if (identity !== identityRevision || revision !== settingsRevision) return;
      applyActivityChoices(data);
      settings = data; $('nickname').value = data.nickname;
      $('settings-status').textContent = '';
    } catch (error) {
      if (identity !== identityRevision || revision !== settingsRevision || expired(error)) return;
      settings = null; $('settings-status').textContent = error.message; $('reload-settings').hidden = false;
    } finally {
      if (identity === identityRevision && revision === settingsRevision) { settingsLoading = false; lockSettings(false); }
    }
  }
  async function saveSettings(event, passwordChange) {
    event.preventDefault();
    if (!authenticated || teacherMode || !settings || settingsLoading || settingsSaving) return;
    const identity = identityRevision, revision = settingsRevision;
    const message = $(passwordChange ? 'password-message' : 'settings-message');
    const body = { revision: settings.revision, ...(passwordChange ? {
      currentPassword: $('current-password').value, newPassword: $('new-password').value, confirmPassword: $('confirm-password').value,
    } : { nickname: $('nickname').value }) };
    settingsSaving = true; lockSettings(true); message.textContent = 'Saving…'; message.classList.remove('error-message');
    try {
      const data = await api('/api/account' + (passwordChange ? '/password' : ''), {
        method: passwordChange ? 'POST' : 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
      });
      if (identity !== identityRevision) return;
      if (passwordChange) {
        showLogin(); $('login-notice').textContent = 'Your password has changed. Sign in with your new password.';
        $('login-notice').hidden = false; $('password').focus(); return;
      }
      applyActivityChoices(data);
      profileRevision++;
      $('student-name').textContent = data.nickname; $('profile-nickname').textContent = data.nickname;
      if (revision !== settingsRevision) return;
      settings = data; $('nickname').value = data.nickname; message.textContent = 'Your nickname is saved.';
    } catch (error) {
      if (identity !== identityRevision || revision !== settingsRevision || expired(error)) return;
      message.textContent = error.message; message.classList.add('error-message');
      if (error.status === 409) { settings = null; $('reload-settings').hidden = false; }
    } finally {
      if (identity === identityRevision && revision === settingsRevision) { settingsSaving = false; lockSettings(false); }
    }
  }
  $('settings-form').addEventListener('submit', event => saveSettings(event, false));
  $('password-form').addEventListener('submit', event => saveSettings(event, true));
  $('reload-settings').addEventListener('click', () => loadSettings(true));
  window.addEventListener('pagehide', () => { studyPractice.clear(); clearSettings(); clearResources(); clearActivityCatalog(); roadPractice.clear(); grammarPractice.clear(); businessTerms.clear(); vocabularyPractice.clear(); closeDropdowns(); });

  function showDashboard(data, focus = false) {
    if (authenticated && teacherMode !== (data.role === 'teacher')) clearIdentity();
    const initial = !authenticated; authenticated = true;
    const { name, nickname, id } = data.student, teacher = data.role === 'teacher';
    teacherMode = teacher;
    $('student-name').textContent = nickname; $('profile-nickname').textContent = nickname;
    $('teacher-student-name').textContent = name; $('avatar').textContent = name[0].toUpperCase();
    $('account-address').textContent = id + '.englishladder.com';
    $('dashboard-title').textContent = teacher ? name + '’s learning space' : 'Welcome back, ' + name + '.';
    $('teacher-banner').hidden = !teacher; $('account-status').textContent = ''; $('password').value = '';
    show('dashboard-view');
    if (initial) { loadActivities(); loadIndex(); loadAssessment(); navigate(); }
    if (focus) $('dashboard-title').focus();
  }
  async function start() {
    show('loading');
    try {
      const context = await api('/api/context'); $('student-id').value = context.id;
      try { showDashboard(await api('/api/session')); }
      catch (error) { if (error.status === 401) showLogin(); else throw error; }
    } catch (error) {
      clearIdentity(); $('unavailable-message').textContent = error.message; show('unavailable-view');
    }
  }
  $('password').addEventListener('input', () => {
    const field = $('password'), start = field.selectionStart, end = field.selectionEnd;
    field.value = field.value.toLowerCase(); field.setSelectionRange(start, end);
    field.removeAttribute('aria-invalid'); $('login-error').hidden = true;
  });
  $('show-password').addEventListener('click', () => {
    const visible = $('password').type === 'password'; $('password').type = visible ? 'text' : 'password';
    $('show-password').textContent = visible ? 'Hide' : 'Show';
    $('show-password').setAttribute('aria-label', visible ? 'Hide password' : 'Show password');
    $('show-password').setAttribute('aria-pressed', String(visible));
  });
  $('login-form').addEventListener('submit', async event => {
    event.preventDefault(); if ($('login-submit').disabled) return;
    $('login-submit').disabled = true; $('login-submit').textContent = 'Opening your space…'; $('login-error').hidden = true;
    try {
      const data = await api('/api/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ password: $('password').value.toLowerCase() }) });
      showDashboard(data, true);
    } catch (error) {
      $('login-error').textContent = error.message; $('login-error').hidden = false;
      $('password').setAttribute('aria-invalid', 'true'); $('password').focus();
    } finally { $('login-submit').disabled = false; $('login-submit').textContent = 'Open my space →'; }
  });
  $('logout').addEventListener('click', async () => {
    clearSettings();
    $('logout').disabled = true;
    try {
      await api('/api/logout', { method: 'POST' }); history.replaceState(null, '', location.pathname);
      showLogin(); $('password').focus();
    } catch (error) { $('account-status').textContent = 'Could not sign out. ' + error.message; }
    finally { $('logout').disabled = false; }
  });
  async function checkSession() {
    if (!authenticated || checking || document.hidden) return;
    checking = true; const revision = identityRevision, profile = profileRevision;
    try {
      const data = await api('/api/session'); if (revision === identityRevision && profile === profileRevision) { showDashboard(data); loadActivities(); void loadResources(true); }
    } catch (error) {
      if (revision !== identityRevision) return;
      if (!expired(error)) { clearIdentity(); $('unavailable-message').textContent = error.message; show('unavailable-view'); }
    } finally { checking = false; }
  }
  window.addEventListener('pageshow', event => { if (event.persisted) { clearIdentity(); start(); } });
  document.addEventListener('visibilitychange', checkSession);
  window.addEventListener('hashchange', () => { closeDropdowns(); navigate(true); });
  $('retry-resources').addEventListener('click', () => loadResources(true));
  $('resources-nav').addEventListener('click', () => { if (location.hash === '#resources') void loadResources(true); });
  window.addEventListener('scroll', scheduleAssessmentHighlight, { passive: true });
  window.addEventListener('resize', updateHeaderHeight);
  document.querySelector('.assessment-outline').addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    // Clicking the original anchor again after manually scrolling does not fire
    // hashchange, so handle that case without adding a duplicate history entry.
    if (link.hash === location.hash) { event.preventDefault(); focusAssessment(link.hash.split('/')[1], true); }
  });
  $('session-select').addEventListener('change', event => { location.hash = 'feedback/' + event.target.value; });
  $('more-sessions').addEventListener('click', () => loadIndex(true));
  $('retry-feedback').addEventListener('click', () => loadIndex(Boolean(sessions.length)));
  $('refresh-quiz-results').addEventListener('click', () => loadQuizResults());
  $('more-quiz-results').addEventListener('click', () => loadQuizResults(true));
  $('retry').addEventListener('click', start);
  setInterval(checkSession, 60_000); start();
})();
