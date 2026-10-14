(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const sections = ['overview', 'assessments', 'sessions', 'feedback'];
  const assessmentSections = ['summary', 'strengths', 'patterns', 'next'];
  const validId = /^\d{4}-\d{2}-\d{2}-\d{4}$/;
  let authenticated = false, checking = false, identityRevision = 0, pageRevision = 0;
  let sessions = [], nextCursor = null, indexReady = false, indexLoading = false, currentPage = '';
  let assessment = null, assessmentLoading = false;
  let assessmentScrollFrame = 0;
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
  }
  function clearIdentity() {
    identityRevision++; pageRevision++;
    authenticated = false; sessions = []; nextCursor = null; indexReady = false; indexLoading = false; currentPage = '';
    assessment = null; assessmentLoading = false;
    assessmentResizeObserver?.disconnect();
    if (assessmentScrollFrame) cancelAnimationFrame(assessmentScrollFrame);
    assessmentScrollFrame = 0;
    markAssessmentSection(null);
    for (const id of ['student-name', 'teacher-student-name', 'avatar', 'account-address', 'profile-nickname', 'account-status']) $(id).textContent = '';
    for (const id of ['session-list', 'session-select', 'session-summaries', 'feedback-page', 'assessment-content', 'assessment-source-count']) $(id).replaceChildren();
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
  function navigate(focus = false) {
    if (!authenticated) return;
    const [part, requested, extra] = location.hash.slice(1).split('/');
    const selected = sections.includes(part) ? part : 'feedback';
    for (const id of sections) $(id).hidden = selected !== id;
    for (const el of document.querySelectorAll('.section-nav a')) {
      if (el.hash === '#' + selected) el.setAttribute('aria-current', 'page');
      else el.removeAttribute('aria-current');
    }
    if (selected !== 'feedback') {
      pageRevision++; currentPage = '';
      document.title = selected === 'assessments' ? 'My English assessment · English Ladder' : 'My learning space · English Ladder';
      if (selected === 'assessments') focusAssessment(requested, focus);
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
  function reference(at) { return node('span', 'Lesson time: ' + at, 'evidence-time'); }
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
      card.append(node('h4', item.title), node('p', item.detail), reference(item.at)); strengths.append(card);
    }
    fragment.append(strengths);
    const points = section('Things to practice', 'feedback-focus');
    record.focus.forEach((item, i) => {
      const card = node('section', '', 'focus-card'), heading = node('div', '', 'focus-heading');
      heading.append(node('span', String(i + 1).padStart(2, '0'), 'focus-number'), node('h4', item.title));
      card.append(heading, node('p', item.kind === 'teacher-feedback' ? 'From this lesson' : 'Extra practice', 'evidence-label'), node('p', item.observed, 'observed'), reference(item.at));
      const model = node('div', '', 'model-sentence');
      model.append(node('span', 'TRY SAYING THIS'), node('p', item.model));
      card.append(model, node('p', item.explanation)); points.append(card);
    });
    fragment.append(points);
    const words = section('Useful language', 'feedback-vocabulary');
    words.append(node('p', 'These are new sentences for you to practice.', 'section-intro'));
    for (const item of record.vocabulary) {
      const row = node('div', '', 'vocabulary-row');
      row.append(node('h4', item.term, 'vocabulary-term'), node('p', item.meaning), node('p', item.example, 'vocabulary-example'), reference(item.at)); words.append(row);
    }
    fragment.append(words);
    const practice = section('A few minutes of practice', 'feedback-practice');
    record.practice.forEach((item, i) => {
      const row = node('div', '', 'practice-item'), answer = node('details');
      row.append(node('p', (i + 1) + '. ' + item.prompt));
      answer.append(node('summary', 'Show an example answer'), node('p', item.answer));
      row.append(answer); practice.append(row);
    });
    fragment.append(practice);
    const next = section('Your next step', 'feedback-next-step'); next.append(node('p', record.nextStep)); fragment.append(next);
    const sources = node('details', '', 'feedback-source');
    sources.append(node('summary', 'How we made this feedback'));
    sources.append(node('p', 'AI helped write this page. We used all the available lesson text (' + record.source.segmentCount.toLocaleString() + ' parts). The text covers ' + record.source.coverageStart + '–' + record.source.coverageEnd + '. Each time shows a point in the lesson, counted from the start.'));
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
    const el = node('a', assessmentDate(ref.sessionId.slice(0, 10)) + ' · ' + ref.at, 'assessment-evidence');
    el.href = '#feedback/' + ref.sessionId;
    el.setAttribute('aria-label', 'Open lesson feedback for ' + assessmentDate(ref.sessionId.slice(0, 10)) + ', lesson time ' + ref.at);
    return el;
  }
  function evidenceList(refs) {
    const details = node('details', '', 'assessment-references');
    details.append(node('summary', 'Examples from your lessons (' + refs.length + ')'));
    const list = node('div');
    for (const ref of refs) list.append(evidenceLink(ref));
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
      const readingLine = Math.min(160, window.innerHeight * 0.2);
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
    const title = node('h2', record.title); title.id = 'assessment-summary'; title.tabIndex = -1;
    const dates = node('div', '', 'feedback-dates');
    dates.append(node('strong', 'Assessed ' + assessmentDate(record.assessedOn)), node('span', record.sourceSessions.length + ' sessions · ' + assessmentDate(record.sourceSessions[0].slice(0, 10)) + ' – ' + assessmentDate(record.sourceSessions.at(-1).slice(0, 10))));
    header.append(title, dates, node('p', record.summary, 'session-reflection'));
    const priority = node('div', '', 'assessment-priority');
    priority.append(node('span', 'START HERE'), node('p', record.mainPriority)); header.append(priority); fragment.append(header);
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
      practice.append(node('strong', 'Practice: '), document.createTextNode(item.practice)); card.append(practice); patterns.append(card);
    });
    fragment.append(patterns);
    const plan = assessmentSection('Your next steps', 'next', 'assessment-plan');
    plan.append(node('p', 'Here is a plan for your next three lessons. These are goals to work toward, not scores you have now.', 'section-intro'));
    for (const item of record.plan) {
      const card = node('section', '', 'assessment-plan-card');
      card.append(node('h4', item.title), node('p', item.activity));
      const target = node('div', '', 'assessment-target'); target.append(node('strong', 'Your goal'), node('p', item.target)); card.append(target); plan.append(card);
    }
    fragment.append(plan);
    const next = section('Our next lesson', 'feedback-next-step');
    next.append(node('p', record.nextLesson)); fragment.append(next);
    const source = node('details', '', 'feedback-source');
    source.append(node('summary', 'How we made this assessment'), node('p', 'AI helped write this page. We used all the available text from each lesson below. Each time shows a point in the lesson, counted from the start. Links open your lesson feedback. Dates use New York time.'));
    const list = node('div', '', 'assessment-source-links');
    for (const id of record.sourceSessions) { const el = node('a', assessmentDate(id.slice(0, 10))); el.href = '#feedback/' + id; list.append(el); }
    source.append(list, node('p', 'This page is only about your English. The lesson text was made by a computer, so some words may be wrong. We checked what you practiced with Phil and what you did well. This is not a test score or an official English level. We cannot check your pronunciation or speaking speed from text alone.'));
    fragment.append(source);
    $('assessment-content').replaceChildren(fragment);
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
    try {
      const data = await api('/api/assessment');
      if (revision !== identityRevision) return;
      assessment = data.assessment;
      $('assessment-count').textContent = assessment ? 'Overall assessment · ' + assessmentDate(assessment.assessedOn) : 'No assessments yet';
      if (assessment) {
        renderAssessment(assessment);
        if (location.hash.split('/')[0] === '#assessments') focusAssessment(location.hash.split('/')[1], false);
      } else assessmentMessage('Your teacher’s assessment of your English and areas to focus on will appear here.');
    } catch (error) {
      if (revision !== identityRevision || expired(error)) return;
      $('assessment-count').textContent = 'Assessment unavailable';
      assessmentMessage('Your assessment could not be loaded. ' + error.message, true);
    } finally {
      if (revision === identityRevision) {
        assessmentLoading = false;
        $('assessment-content').setAttribute('aria-busy', 'false');
      }
    }
  }
  function showDashboard(data, focus = false) {
    const initial = !authenticated; authenticated = true;
    const { name, nickname, id } = data.student, teacher = data.role === 'teacher';
    $('student-name').textContent = nickname; $('profile-nickname').textContent = nickname;
    $('teacher-student-name').textContent = name; $('avatar').textContent = name[0].toUpperCase();
    $('account-address').textContent = id + '.englishladder.com';
    $('dashboard-title').textContent = teacher ? name + '’s learning space' : 'Welcome back, ' + name + '.';
    $('teacher-banner').hidden = !teacher; $('account-status').textContent = ''; $('password').value = '';
    show('dashboard-view');
    if (initial) { loadIndex(); loadAssessment(); navigate(); }
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
    $('logout').disabled = true;
    try {
      await api('/api/logout', { method: 'POST' }); history.replaceState(null, '', location.pathname);
      showLogin(); $('password').focus();
    } catch (error) { $('account-status').textContent = 'Could not sign out. ' + error.message; }
    finally { $('logout').disabled = false; }
  });
  async function checkSession() {
    if (!authenticated || checking || document.hidden) return;
    checking = true; const revision = identityRevision;
    try {
      const data = await api('/api/session'); if (revision === identityRevision) showDashboard(data);
    } catch (error) {
      if (revision !== identityRevision) return;
      if (!expired(error)) { clearIdentity(); $('unavailable-message').textContent = error.message; show('unavailable-view'); }
    } finally { checking = false; }
  }
  window.addEventListener('pageshow', event => { if (event.persisted) { clearIdentity(); start(); } });
  document.addEventListener('visibilitychange', checkSession);
  window.addEventListener('hashchange', () => navigate(true));
  window.addEventListener('scroll', scheduleAssessmentHighlight, { passive: true });
  window.addEventListener('resize', scheduleAssessmentHighlight);
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
  $('retry').addEventListener('click', start);
  setInterval(checkSession, 60_000); start();
})();
