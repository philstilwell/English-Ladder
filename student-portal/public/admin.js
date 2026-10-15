'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const adminMenu = document.querySelector('.admin-nav');
  function updateMenuHeight() {
    const height = adminMenu.getBoundingClientRect().height;
    if (height) document.documentElement.style.setProperty('--admin-menu-height', height + 'px');
  }
  const menuResizeObserver = typeof ResizeObserver === 'undefined' ? null : new ResizeObserver(updateMenuHeight);
  menuResizeObserver?.observe(adminMenu);
  let signedIn = false, epoch = 0, students = [], current = null, importRows = null, addressEdited = false;
  let activityTools = [];
  let quizRequest = 0, quizStatuses = {};
  let cefrRequest = 0, cefrStatuses = {}, cefrDetailRequest = 0;
  let loginRequest = 0, loginDetails = null;
  let roadEpoch = 0, roadRows = [], roadCursor = null, roadLoading = false;
  let activityOverviewRequest = 0;
  let deleting = null, deleteBusy = false, saving = false;
  const fields = ['firstName','lastName','nickname','studentId','status','timeZone','course','fileNumber','email','otherEmail','staff','contactedOn','endsOn','hoursAuthorized','hoursUsed','hoursPending','hoursRemaining','notes'];
  const displayDate = value => value ? new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeZone: 'UTC' }).format(new Date(value)) : '';
  const displayTime = value => value ? new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeStyle: 'short', timeZone: 'America/New_York' }).format(new Date(value)) + ' Eastern' : '';
  const element = (tag, text, className) => { const node = document.createElement(tag); if (text != null) node.textContent = text; if (className) node.className = className; return node; };
  function message(text, error = false) { $('message').textContent = text; $('message').hidden = !text; $('message').classList.toggle('error', error); }
  const cefrLabel = record => record?.state === 'estimated' ? (record.lower === record.upper ? record.lower : record.lower + '–' + record.upper) :
    { pending: 'Not assessed yet', insufficient: 'More evidence needed', unavailable: 'Unable to check', loading: 'Checking…' }[record?.state] || 'Not assessed yet';
  function clearCefr() { cefrDetailRequest++; $('cefr-panel').hidden = true; $('cefr-content').replaceChildren(); }
  function createQuestionsPanel(id, activity, renderer, label) {
    let requestRevision = 0, questions = [], page = 0;
    function clear() {
      requestRevision++; questions = []; page = 0;
      $(id + '-questions-panel').hidden = true; $(id + '-questions-content').replaceChildren(); $(id + '-questions-status').textContent = '';
      $('load-' + id + '-questions').disabled = false; $('load-' + id + '-questions').textContent = 'Load questions list';
    }
    function render() {
      const content = $(id + '-questions-content'); content.replaceChildren();
      for (const item of questions.slice(page * 20, (page + 1) * 20)) {
        const details = element('details', null, 'terms-questions'), summary = element('summary', label(item) + (item.progress.finished ? ' · Finished' : ''));
        const { card } = renderer().exercise(item); card.classList.toggle('is-finished', item.progress.finished);
        details.append(summary, card); content.append(details);
      }
      if (questions.length > 20) {
        const controls = element('div', null, 'terms-controls');
        const back = element('button', 'Previous questions', 'secondary-button'), next = element('button', 'More questions', 'secondary-button');
        back.type = next.type = 'button'; back.disabled = page === 0; next.disabled = (page + 1) * 20 >= questions.length;
        back.addEventListener('click', () => { page--; render(); }); next.addEventListener('click', () => { page++; render(); });
        controls.append(back, element('span', `Page ${page + 1} of ${Math.ceil(questions.length / 20)}`), next); content.append(controls);
      }
    }
    async function load() {
      if (!signedIn || !current?.activated || current.deletionPending) return;
      const student = current, version = epoch, request = ++requestRevision;
      const valid = () => signedIn && epoch === version && request === requestRevision && current?.key === student.key;
      $('load-' + id + '-questions').disabled = true; $(id + '-questions-content').replaceChildren(); questions = []; page = 0;
      $(id + '-questions-status').textContent = 'Loading questions…';
      try {
        const data = await api('/api/admin/students/' + student.key + '/' + activity);
        if (!valid()) return;
        if (!Array.isArray(data.questions) || data.questions.length && !renderer().validItems(data.questions)) throw new Error('Questions could not load. Please try again.');
        questions = data.questions; render();
        $(id + '-questions-status').textContent = questions.length ? questions.length + (questions.length === 1 ? ' item' : ' items') + ' to discuss. Refresh the list to see new choices.' : 'No items in this student’s Questions list.';
        $('load-' + id + '-questions').textContent = 'Refresh questions list';
      } catch (error) { if (valid()) $(id + '-questions-status').textContent = error.message; }
      finally { if (valid()) $('load-' + id + '-questions').disabled = false; }
    }
    $('load-' + id + '-questions').addEventListener('click', load);
    return { clear, load, show(student) { clear(); $(id + '-questions-panel').hidden = !student?.activated || Boolean(student?.deletionPending); } };
  }
  const termsPanel = createQuestionsPanel('terms', 'business-terms', () => window.BusinessTerms, item => `Item ${item.number} · “${item.term}”`);
  const grammarPanel = createQuestionsPanel('grammar', 'grammar-practice', () => ({
    validItems: window.GrammarPractice.validItems,
    exercise: item => ({ card: window.GrammarPractice.exercise(item, 'article') }),
  }), item => `Item ${item.number} · “${item.prompt}”`);
  function clearQuestions() { termsPanel.clear(); grammarPanel.clear(); }
  function clearActivityOverview() {
    activityOverviewRequest++;
    $('activity-overview-panel').hidden = true;
    $('activity-overview-content').replaceChildren(); $('activity-overview-status').textContent = '';
    $('refresh-activity-overview').disabled = false;
  }
  async function loadActivityOverview() {
    if (!signedIn || !current?.activated || current.deletionPending) return;
    const student = current, version = epoch, request = ++activityOverviewRequest;
    const valid = () => signedIn && version === epoch && request === activityOverviewRequest && current?.key === student.key;
    $('activity-overview-panel').hidden = false; $('activity-overview-content').replaceChildren();
    $('activity-overview-status').textContent = 'Loading saved activity…'; $('refresh-activity-overview').disabled = true;
    try {
      const data = await api('/api/admin/students/' + student.key + '/activity-summary');
      if (!valid()) return;
      const ids = ['english-road', 'grammar-practice', 'business-terms'];
      const count = value => Number.isSafeInteger(value) && value >= 0;
      if (!Array.isArray(data.activities) || data.activities.length !== ids.length || data.activities.some((item, index) =>
        !item || item.id !== ids[index] || item.lastActivityAt !== null && !Number.isFinite(Date.parse(item.lastActivityAt)) ||
        !(index ? ['total', 'finished', 'questions'] : ['setsStarted', 'setsCompleted', 'answered', 'correct']).every(key => count(item[key]))))
        throw new Error('Activity records could not load. Please try again.');
      for (const item of data.activities) {
        const tool = activityTools.find(tool => tool.id === item.id), card = element('article', null, 'activity-overview-card');
        card.append(element('h3', tool?.name || item.id));
        if (!student.visibleActivities.includes(item.id)) card.append(element('p', 'Hidden from student menu', 'field-note'));
        if (item.id === 'english-road') {
          card.append(element('p', item.setsCompleted + ' of ' + item.setsStarted + ' sets completed'),
            element('p', item.correct + ' correct / ' + item.answered + ' answers saved'));
          if (item.latestSet) card.append(element('p', 'Latest set: ' + ({ completed: 'Completed', ended: 'Ended early', in_progress: 'In progress' }[item.latestSet.state] || 'Saved') + ' · ' + item.latestSet.answered + '/' + item.latestSet.total + ' answered', 'field-note'));
        } else {
          card.append(element('p', item.finished + ' of ' + item.total + ' items marked finished'),
            element('p', item.questions + (item.questions === 1 ? ' question' : ' questions') + ' to discuss'));
          if (item.savedPlace !== null) card.append(element('p', 'Saved place: item ' + item.savedPlace, 'field-note'));
        }
        card.append(element('p', item.lastActivityAt ? 'Last saved activity: ' + displayTime(item.lastActivityAt) : 'No saved activity yet.', 'field-note'));
        const review = element('button', item.id === 'english-road' ? 'View practice results' : 'View questions', 'secondary-button');
        review.type = 'button'; review.addEventListener('click', () => {
          if (!valid()) return;
          const id = item.id === 'english-road' ? 'road-results-panel' : item.id === 'grammar-practice' ? 'grammar-questions-panel' : 'terms-questions-panel';
          if (item.id === 'english-road') void loadRoad(); else void (item.id === 'grammar-practice' ? grammarPanel : termsPanel).load();
          $(id).scrollIntoView?.({ behavior: 'smooth', block: 'start' });
          const heading = $(id).querySelector('h2'); heading.tabIndex = -1; heading.focus({ preventScroll: true });
        });
        card.append(review); $('activity-overview-content').append(card);
      }
      $('activity-overview-status').textContent = '';
    } catch (error) { if (valid()) $('activity-overview-status').textContent = error.message; }
    finally { if (valid()) $('refresh-activity-overview').disabled = false; }
  }
  $('refresh-activity-overview').addEventListener('click', loadActivityOverview);
  function clearRoad() {
    roadEpoch++; roadRows = []; roadCursor = null; roadLoading = false;
    $('road-results-panel').hidden = true; $('road-results').replaceChildren(); $('road-results-status').textContent = '';
    $('more-road-results').hidden = true; $('more-road-results').disabled = false;
    $('load-road-results').disabled = false; $('load-road-results').textContent = 'Load practice results';
  }
  async function loadRoad(append = false) {
    if (!signedIn || !current?.activated || current.deletionPending || roadLoading) return;
    if (!append) { roadEpoch++; roadRows = []; roadCursor = null; $('road-results').replaceChildren(); $('more-road-results').hidden = true; }
    const student = current, version = epoch, request = roadEpoch;
    const valid = () => signedIn && version === epoch && request === roadEpoch && current?.key === student.key;
    roadLoading = true; $('load-road-results').disabled = true; $('more-road-results').disabled = true;
    $('road-results-status').textContent = 'Loading saved practice…';
    try {
      const data = await api('/api/admin/students/' + student.key + '/road' + (append && roadCursor ? '?before=' + encodeURIComponent(roadCursor) : ''));
      if (!valid()) return;
      roadRows.push(...data.attempts); roadCursor = data.nextCursor;
      $('road-results-status').textContent = roadRows.length ? 'Open a set to see each original answer. Dates use New York time.' : 'No English Road practice has been started yet.';
      $('load-road-results').textContent = 'Refresh practice results';
      for (const row of data.attempts) {
        const details = element('details', null, 'road-result-set'), summary = element('summary');
        const state = row.completedAt ? 'Completed' : row.endedAt ? 'Ended early' : 'In progress';
        summary.append(element('strong', row.band + ' · ' + (row.topic || 'All topics')),
          element('span', state + ' · ' + row.correct + ' correct out of ' + row.answered + ' answered · ' + row.answered + '/' + row.total + ' questions', 'detail'),
          element('span', 'Started ' + displayTime(row.startedAt), 'detail'));
        if (row.completedAt || row.endedAt) summary.append(element('span', 'Finished ' + displayTime(row.completedAt || row.endedAt), 'detail'));
        const content = element('div'); details.append(summary, content); $('road-results').append(details);
        let loaded = false, loading = false;
        async function loadDetail() {
          if (loaded || loading || !valid() || !details.isConnected) return;
          loading = true; content.replaceChildren(element('p', 'Loading answers…'));
          try {
            const data = await api('/api/admin/students/' + student.key + '/road/' + row.id);
            if (!valid() || !details.isConnected) return;
            loaded = true; content.replaceChildren();
            const attempt = data.attempt;
            if (!attempt.answers.length) content.append(element('p', 'No answers submitted.'));
            attempt.answers.forEach((answer, i) => {
              const q = attempt.questions[i], box = element('article', null, 'road-review');
              box.append(element('h3', 'Question ' + (i + 1) + ' · ' + q.topic), element('p', q.setup), element('p', '“' + q.prompt + '”', 'road-prompt'));
              const options = element('ol'); q.options.forEach(option => options.append(element('li', option))); box.append(options);
              box.append(element('p', 'Original answer: “' + q.options[answer.choiceIndex] + '”'),
                element('strong', answer.choiceIndex === q.correctIndex ? 'Correct' : 'Incorrect'),
                element('p', 'Correct answer: “' + q.options[q.correctIndex] + '”'), element('p', q.feedback[answer.choiceIndex]), element('p', q.explanation),
                element('p', 'Answered ' + displayTime(answer.answeredAt), 'field-note')); content.append(box);
            });
          } catch (error) {
            if (!valid() || !details.isConnected) return;
            const retry = element('button', 'Try again', 'secondary-button'); retry.type = 'button'; retry.addEventListener('click', loadDetail);
            content.replaceChildren(element('p', error.message), retry);
          } finally { loading = false; }
        }
        details.addEventListener('toggle', () => { if (details.open) loadDetail(); });
      }
      $('more-road-results').hidden = !roadCursor;
    } catch (error) { if (valid()) $('road-results-status').textContent = error.message; }
    finally { if (valid()) { roadLoading = false; $('load-road-results').disabled = false; $('more-road-results').disabled = false; } }
  }
  $('load-road-results').addEventListener('click', () => loadRoad());
  $('more-road-results').addEventListener('click', () => loadRoad(true));
  async function loadCefr(student) {
    clearCefr();
    if (!student || student.deletionPending) return;
    $('cefr-panel').hidden = false;
    $('cefr-content').append(element('p', 'Loading the estimate…', 'field-note'));
    const request = cefrDetailRequest, version = epoch;
    const stillCurrent = () => signedIn && version === epoch && request === cefrDetailRequest && current?.key === student.key && location.hash === '#students/' + student.key;
    try {
      const { cefr, schedule } = await api('/api/admin/students/' + student.key + '/cefr');
      if (!stillCurrent()) return;
      const content = $('cefr-content'); content.replaceChildren();
      content.append(element('strong', cefrLabel(cefr), 'cefr-level'));
      content.append(element('p', 'First estimate after two recorded sessions. Monthly reviews use the latest four available transcripts, with at least two required.', 'field-note'));
      if (schedule?.nextReviewOn) content.append(element('p', 'Next review from ' + displayDate(schedule.nextReviewOn) + ', when new session evidence is available.', 'field-note'));
      if (schedule?.lastReviewState === 'insufficient' && cefr?.state === 'estimated') content.append(element('p', 'The latest review had too little reliable evidence. The earlier estimate is retained.', 'field-note'));
      if (!cefr) { content.append(element('p', 'An estimate can be added during the next eligible nightly check after two usable redacted transcripts are saved. Existing lessons have not been reprocessed.', 'field-note')); return; }
      content.append(element('p', 'Reviewed ' + displayDate(cefr.assessedOn) + ' · Latest lesson ' + displayDate(cefr.latestSessionId.slice(0, 10)), 'field-note'));
      content.append(element('p', cefr.rationale));
      if (cefr.state !== 'estimated') return;
      content.append(element('p', (cefr.confidence === 'moderate' ? 'Moderate' : 'Low') + ' confidence · Evidence from ' + cefr.sourceSessions.length + (cefr.sourceSessions.length === 1 ? ' lesson' : ' lessons'), 'field-note'));
      const aspects = element('dl', null, 'cefr-aspects');
      const labels = { range: 'Vocabulary and sentence range', accuracy: 'Grammar control', coherence: 'Connecting ideas', interaction: 'Conversation skills' };
      for (const aspect of cefr.aspects) { const item = element('div'); item.append(element('dt', labels[aspect.area]), element('dd', aspect.detail)); aspects.append(item); }
      content.append(aspects);
      const evidence = element('details', null, 'cefr-evidence'); evidence.append(element('summary', 'Supporting learner examples'));
      for (const ref of cefr.evidence) {
        const item = element('div', null, 'cefr-example');
        item.append(element('p', displayDate(ref.sessionId.slice(0, 10)) + ' · Transcript ' + ref.at, 'field-note'), element('blockquote', '“' + ref.quote + '”'), element('p', ref.note));
        evidence.append(item);
      }
      content.append(evidence);
    } catch (error) {
      if (!stillCurrent()) return;
      const retry = element('button', 'Try again', 'secondary-button'); retry.type = 'button'; retry.addEventListener('click', () => loadCefr(student));
      $('cefr-content').replaceChildren(element('p', error.message), retry);
    }
  }
  function clearLoginDetails() {
    loginRequest++; loginDetails = null;
    $('login-details-panel').hidden = true;
    $('login-url').value = ''; $('current-password').value = ''; $('current-password').type = 'password';
    $('reveal-password').textContent = 'Show password'; $('reveal-password').setAttribute('aria-pressed', 'false');
    $('reveal-password').disabled = true; $('copy-login-details').disabled = true;
    $('login-details-status').textContent = ''; $('copy-login-text').value = ''; $('copy-fallback').hidden = true;
  }
  async function loadLoginDetails(student) {
    clearLoginDetails();
    if (!student || student.deletionPending) return null;
    $('login-details-panel').hidden = false; $('login-details-status').textContent = 'Loading saved login details…';
    const request = loginRequest, version = epoch;
    const stillCurrent = () => signedIn && epoch === version && request === loginRequest && current?.key === student.key && location.hash === '#students/' + student.key;
    try {
      const data = await api('/api/admin/students/' + student.key + '/login-details');
      if (!stillCurrent()) return null;
      loginDetails = data;
      $('login-url').value = data.url || '';
      $('current-password').value = data.password || '';
      $('reveal-password').disabled = !data.password;
      $('copy-login-details').disabled = !data.password || !data.url || !data.active;
      $('login-details-status').textContent = data.message || (data.active ? 'Ready to copy. Capital letters also work when the student signs in.' : 'This site is not active. You can view its password here; copying login details is available when the site is active.');
      return data;
    } catch (error) {
      if (stillCurrent()) $('login-details-status').textContent = error.message;
      return null;
    }
  }
  function clearPrivate() {
    epoch++; signedIn = false; students = []; current = null; importRows = null; activityTools = [];
    $('student-activities').replaceChildren();
    clearRoad(); clearQuestions(); clearActivityOverview();
    clearLoginDetails();
    clearCefr(); cefrRequest++; cefrStatuses = {};
    closeDelete();
    quizRequest++; quizStatuses = {};
    $('admin-view').hidden = true; $('login-view').hidden = false; $('sign-out').hidden = true;
    $('student-rows').replaceChildren(); $('import-names').replaceChildren(); $('student-form').reset();
    $('paused-student-rows').replaceChildren(); $('paused-students').open = false; $('paused-students').hidden = true; $('paused-count').textContent = '0';
    $('delete-account-panel').hidden = true;
    $('sheet-paste').value = ''; $('password').value = ''; $('search').value = ''; $('filter').value = 'all';
    $('edit-title').textContent = ''; $('source-note').textContent = ''; $('open-site').removeAttribute('href'); $('open-quiz-results').removeAttribute('href'); $('open-quiz-results').hidden = true;
    $('activation-note').textContent = ''; $('save-state').textContent = ''; $('import-preview').hidden = true;
    $('password-status').textContent = '';
    $('active-count').textContent = '0'; $('draft-count').textContent = '0'; $('list-count').textContent = '';
    $('last-check').textContent = ''; $('schedule-state').textContent = ''; message('');
    document.title = 'Phil’s students · English Ladder';
  }
  async function api(path, options = {}) {
    const version = epoch;
    const response = await fetch(path, { credentials: 'same-origin', cache: 'no-store', ...options,
      headers: { ...(options.body ? { 'Content-Type': 'application/json' } : {}), ...options.headers } });
    if (version !== epoch) throw new Error('Session changed.');
    const data = await response.json();
    if (version !== epoch) throw new Error('Session changed.');
    if (response.status === 401 && path !== '/api/login') { const expired = signedIn; clearPrivate(); $('login-message').textContent = expired ? 'Please sign in again.' : ''; }
    if (!response.ok) throw Object.assign(new Error(data.error || 'The request could not be saved. Please try again.'), { deletionPending: data.deletionPending });
    return data;
  }
  function showList() {
    const query = $('search').value.trim().toLowerCase(), filter = $('filter').value;
    const shown = students.filter(s => (filter === 'all' || s.status === filter) && [s.firstName,s.lastName,s.studentId,...s.zoomNames].join(' ').toLowerCase().includes(query));
    $('student-rows').replaceChildren();
    $('paused-student-rows').replaceChildren();
    const paused = shown.filter(s => s.status === 'paused');
    $('paused-count').textContent = paused.length;
    $('paused-students').hidden = !paused.length;
    $('main-student-table').hidden = shown.length === paused.length;
    $('active-count').textContent = students.filter(s => s.status === 'active').length;
    $('draft-count').textContent = students.filter(s => s.status === 'draft').length;
    $('list-count').textContent = shown.length + ' of ' + students.length + ' students';
    $('empty-list').hidden = shown.length > 0;
    for (const student of shown) {
      const row = element('tr'), name = element('td'), site = element('td'), course = element('td'), status = element('td'), latestQuiz = element('td', null, 'latest-quiz'), cefrCell = element('td', null, 'cefr-cell'), action = element('td');
      const link = element('a', [student.firstName,student.lastName].filter(Boolean).join(' '), 'student-name'); link.href = '#students/' + student.key; name.append(link);
      if (student.nickname) name.append(element('span', student.nickname, 'detail'));
      site.append(element('span', student.studentId ? student.studentId + '.englishladder.com' : 'Site not activated'));
      site.append(element('span', student.zoomNames.length ? 'Zoom: ' + student.zoomNames.join(' · ') : 'Add a Zoom name to connect lessons', 'detail'));
      course.append(element('span', student.hoursRemaining != null ? student.hoursRemaining + ' hours remaining' : student.course || 'Course details not added'));
      if (student.endsOn) course.append(element('span', 'Ends ' + displayDate(student.endsOn), 'detail'));
      status.append(element('span', student.deletionPending ? 'Deletion pending' : {active:'Active',draft:'Draft',paused:'Paused'}[student.status], 'status-pill ' + student.status));
      const quiz = quizStatuses[student.key] || { state: 'loading' };
      latestQuiz.append(element('span', 'Latest quiz: ', 'quiz-mobile-label'));
      latestQuiz.append(element('span', {completed:'Done',in_progress:'In progress',not_started:'Not started',no_quiz:'No quiz yet',unavailable:'Unable to check',loading:'Checking…'}[quiz.state] || 'Unable to check', 'quiz-pill ' + quiz.state));
      if (quiz.state === 'completed') latestQuiz.append(element('span', 'Finished ' + displayTime(quiz.completedAt), 'detail'));
      if (quiz.state === 'in_progress') latestQuiz.append(element('span', quiz.answered + ' of ' + quiz.total + ' questions answered', 'detail'));
      const cefr = cefrStatuses[student.key] || { state: 'loading' };
      const cefrLink = element('a', cefrLabel(cefr), 'cefr-badge ' + cefr.state); cefrLink.href = link.href;
      cefrLink.setAttribute('aria-label', 'CEFR estimate for ' + student.firstName + ': ' + cefrLabel(cefr));
      cefrCell.append(element('span', 'CEFR estimate: ', 'quiz-mobile-label'), cefrLink);
      if (cefr.state === 'estimated') cefrCell.append(element('span', (cefr.confidence === 'moderate' ? 'Moderate' : 'Low') + ' confidence', 'detail'));
      if (cefr.latestSessionId) cefrCell.append(element('span', 'Lesson ' + displayDate(cefr.latestSessionId.slice(0, 10)), 'detail'));
      const edit = element('a', 'Edit account →', 'edit-link'); edit.href = link.href; edit.setAttribute('aria-label', 'Edit account for ' + student.firstName + ' ' + student.lastName); action.append(edit);
      row.append(name,site,course,status,latestQuiz,cefrCell,action); $(student.status === 'paused' ? 'paused-student-rows' : 'student-rows').append(row);
    }
  }
  async function refresh() {
    quizRequest++;
    cefrRequest++;
    const version = epoch;
    const data = await api('/api/admin/students');
    if (!signedIn || version !== epoch) return;
    if (!Array.isArray(data.activities) || !data.activities.length || data.activities.some(a => !a || typeof a.id !== 'string' || typeof a.name !== 'string' || typeof a.description !== 'string')) throw new Error('The activity list could not load. Please refresh before editing a student.');
    activityTools = data.activities;
    students = data.students; quizStatuses = {}; cefrStatuses = {}; showList(); route();
    void refreshQuizStatuses();
    void refreshCefrStatuses();
    try {
      const status = await api('/api/admin/automation');
      if (!signedIn || version !== epoch) return;
      $('schedule-state').textContent = status.retentionError ? 'Transcript cleanup needs attention. Older cached copies could not be removed.' : status.cefrNeedsAttention ? 'CEFR review needs attention. Existing estimates have been kept.' : status.connectionError ? 'Zoom needs attention. Open a student’s Quiz results to check the connection.' : status.connected && status.enabled ? 'On the server · adjusts for daylight saving' : 'Automatic updates are not connected yet.';
      $('last-check').textContent = status.lastCheck ? 'Last check: ' + displayTime(status.lastCheck) + (status.needsAttention ? ' · ' + status.needsAttention + ' sessions need attention' : '') : 'The first nightly check is still ahead.';
    } catch (error) { if (signedIn && version === epoch) $('schedule-state').textContent = 'Server status is temporarily unavailable.'; }
  }
  async function refreshQuizStatuses() {
    const version = epoch, request = ++quizRequest;
    let cursor;
    try {
      do {
        const data = await api('/api/admin/quiz-status' + (cursor ? '?after=' + encodeURIComponent(cursor) : ''));
        if (!signedIn || version !== epoch || request !== quizRequest) return;
        Object.assign(quizStatuses, data.statuses); showList();
        cursor = data.nextCursor;
      } while (cursor);
    } catch {
      if (!signedIn || version !== epoch || request !== quizRequest) return;
      for (const student of students) if (!quizStatuses[student.key]) quizStatuses[student.key] = { state: 'unavailable' };
      showList();
    }
  }
  async function refreshCefrStatuses() {
    const version = epoch, request = ++cefrRequest;
    let cursor;
    try {
      do {
        const data = await api('/api/admin/cefr-status' + (cursor ? '?after=' + encodeURIComponent(cursor) : ''));
        if (!signedIn || version !== epoch || request !== cefrRequest) return;
        if (!data.statuses) throw new Error('Unavailable');
        Object.assign(cefrStatuses, data.statuses); showList(); cursor = data.nextCursor;
      } while (cursor);
    } catch {
      if (!signedIn || version !== epoch || request !== cefrRequest) return;
      for (const student of students) if (!cefrStatuses[student.key]) cefrStatuses[student.key] = { state: 'unavailable' };
      showList();
    }
  }
  function suggestedAddress() {
    const first = $('firstName').value.trim().normalize('NFKD').replace(/[^a-z]/gi, ''), last = $('lastName').value.trim().split(/\s+/).at(-1)?.normalize('NFKD').replace(/[^a-z]/gi, '');
    if (first && last && !addressEdited && !current?.activated) $('studentId').value = (first[0] + last[0]).toLowerCase() + new Intl.DateTimeFormat('en', { timeZone: 'America/New_York', year: '2-digit' }).format(new Date());
  }
  function editStudent(student) {
    current = student; addressEdited = Boolean(student?.studentId);
    $('student-form').reset(); $('save-state').textContent = '';
    $('student-activities').replaceChildren();
    const selected = student?.visibleActivities ?? activityTools.map(activity => activity.id);
    for (const activity of activityTools) {
      const label = element('label', null, 'activity-choice'), input = element('input');
      input.type = 'checkbox'; input.name = 'visibleActivities'; input.value = activity.id; input.checked = selected.includes(activity.id);
      label.append(input, element('span', activity.name)); $('student-activities').append(label);
    }

    for (const fieldset of $('student-form').querySelectorAll('fieldset')) fieldset.disabled = Boolean(student?.deletionPending);
    $('save-student').disabled = Boolean(student?.deletionPending) || saving;
    $('delete-account-panel').hidden = !student;
    $('open-delete').disabled = saving;
    $('delete-account-note').textContent = student?.deletionPending ? 'The site is closed. Deletion is not finished. Use Delete student account again to finish removing the saved records.' : 'Permanently remove this account and its saved learning records. To keep the records and stop access, choose “Paused” above instead.';
    $('password-status').textContent = student?.hasCustomPassword ? 'This student has a personal password. You can view and copy it in Student login details above.' : 'This account uses the existing default student password until you assign a personal one.';
    for (const field of fields) $(field).value = student?.[field] ?? (field === 'status' ? 'active' : field === 'timeZone' ? 'America/New_York' : '');
    $('zoomNames').value = student?.zoomNames.join('\n') || '';
    $('studentId').readOnly = Boolean(student?.activated);
    $('status').querySelector('option[value="draft"]').disabled = Boolean(student?.activated);
    $('edit-title').textContent = student ? student.firstName + ' ' + student.lastName : 'Register new student';
    $('edit-kicker').textContent = student ? 'EDIT STUDENT ACCOUNT' : 'A NEW LEARNING SPACE';
    $('edit-description').textContent = student ? 'Update the account details. Changes take effect when you save.' : 'Add the student’s details and exact Zoom display name.';
    $('source-note').hidden = !student?.source;
    $('source-note').textContent = student?.source ? 'Imported from “New-Students” on ' + displayDate(student.source.importedAt) + ' as “' + student.source.name + '”. Check the first and last names before activation. Changes here do not change the spreadsheet.' : '';
    $('activation-note').textContent = student?.activated ? 'Includes sessions held after ' + displayTime(student.startAfter) + '. Pausing stops access and updates; saved learning records stay in place.' : 'Activation includes sessions held after you activate this account. Updates arrive after the nightly check.';
    $('open-site').hidden = student?.status !== 'active';
    if (student?.status === 'active') $('open-site').href = 'https://' + student.studentId + '.englishladder.com/'; else $('open-site').removeAttribute('href');
    $('open-quiz-results').hidden = student?.status !== 'active';
    if (student?.status === 'active') $('open-quiz-results').href = 'https://' + student.studentId + '.englishladder.com/#quiz-results'; else $('open-quiz-results').removeAttribute('href');
    if (student && !student.studentId) suggestedAddress();
    updateSaveLabel();
    void loadLoginDetails(student);
    void loadCefr(student);
    clearRoad(); $('road-results-panel').hidden = !student?.activated || Boolean(student?.deletionPending);
    termsPanel.show(student); grammarPanel.show(student);
    clearActivityOverview(); void loadActivityOverview();
  }
  function updateSaveLabel() { $('save-student').textContent = $('status').value === 'active' && !current?.activated ? 'Save and activate site' : 'Save changes'; }
  function route() {
    if (!signedIn) return;
    clearRoad(); clearQuestions(); clearActivityOverview();
    closeDelete();
    clearLoginDetails(); current = null;
    $('student-activities').replaceChildren();
    clearCefr();
    $('newPassword').value = ''; $('confirmPassword').value = '';
    const hash = location.hash || '#students';
    for (const id of ['list-view','edit-view','import-view','technical-view']) $(id).hidden = true;
    for (const id of ['list-nav','register-nav','import-nav','technical-nav']) $(id).removeAttribute('aria-current');
    if (hash === '#register') { $('edit-view').hidden = false; $('register-nav').setAttribute('aria-current','page'); editStudent(null); }
    else if (hash.startsWith('#students/')) {
      const student = students.find(s => s.key === hash.slice(10));
      if (!student) { message('This student could not be found.', true); $('list-view').hidden = false; }
      else { $('edit-view').hidden = false; editStudent(student); }
      $('list-nav').setAttribute('aria-current','page');
    } else if (hash === '#import') { $('import-view').hidden = false; $('import-nav').setAttribute('aria-current','page'); }
    else if (hash === '#technical-notes') { $('technical-view').hidden = false; $('technical-nav').setAttribute('aria-current','page'); }
    else { $('list-view').hidden = false; $('list-nav').setAttribute('aria-current','page'); $('paused-students').open = $('filter').value === 'paused' || Boolean($('search').value.trim()); showList(); }
  }
  function closeDelete() {
    deleting = null; deleteBusy = false;
    if ($('delete-dialog').open) $('delete-dialog').close();
    $('delete-confirmation').value = ''; $('delete-confirmation').disabled = false;
    $('delete-student-name').textContent = ''; $('delete-confirmation-label').textContent = ''; $('delete-error').textContent = '';
    $('confirm-delete').disabled = true; $('confirm-delete').textContent = 'Delete account permanently'; $('cancel-delete').disabled = false;
  }
  function matchesDeletion() { return deleting && $('delete-confirmation').value.trim().toLowerCase() === deleting.confirmation.toLowerCase(); }
  $('open-delete').addEventListener('click', () => {
    if (!signedIn || !current || saving) return;
    clearLoginDetails();
    deleting = { ...current, confirmation: current.studentId || [current.firstName,current.lastName].filter(Boolean).join(' ') };
    $('delete-student-name').textContent = [current.firstName,current.lastName].filter(Boolean).join(' ');
    $('delete-confirmation-label').textContent = deleting.confirmation;
    $('delete-dialog').showModal();
  });
  const cancelDelete = () => { closeDelete(); if (signedIn) void loadLoginDetails(current); };
  $('cancel-delete').addEventListener('click', cancelDelete);
  $('delete-dialog').addEventListener('cancel', event => { event.preventDefault(); if (!deleteBusy) cancelDelete(); });
  $('delete-confirmation').addEventListener('input', () => { $('confirm-delete').disabled = deleteBusy || !matchesDeletion(); });
  $('delete-form').addEventListener('submit', async event => {
    event.preventDefault();
    if (!signedIn || deleteBusy || !matchesDeletion()) return;
    const target = deleting, version = epoch;
    deleteBusy = true; $('confirm-delete').disabled = true; $('cancel-delete').disabled = true; $('delete-confirmation').disabled = true;
    $('confirm-delete').textContent = 'Deleting…'; $('delete-error').textContent = '';
    const stillCurrent = () => signedIn && epoch === version && deleting === target;
    try {
      await api('/api/admin/students/' + target.key, { method: 'DELETE', body: JSON.stringify({ revision: target.revision, confirmation: $('delete-confirmation').value }) });
      if (!signedIn || epoch !== version) return;
      students = students.filter(student => student.key !== target.key); quizRequest++; delete quizStatuses[target.key]; showList();
      cefrRequest++; delete cefrStatuses[target.key]; clearCefr();
      if (!stillCurrent()) return;
      closeDelete(); current = null; $('student-form').reset();
      history.replaceState(null, '', '#students'); route(); message('Student account and saved learning records deleted.');
    } catch (error) {
      if (!stillCurrent()) return;
      if (error.deletionPending) {
        const student = students.find(s => s.key === target.key);
        if (student) { student.deletionPending = true; student.status = 'paused'; editStudent(student); showList(); }
      }
      $('delete-error').textContent = error.message;
    } finally {
      if (stillCurrent()) { deleteBusy = false; $('confirm-delete').disabled = !matchesDeletion(); $('cancel-delete').disabled = false; $('delete-confirmation').disabled = false; $('confirm-delete').textContent = 'Delete account permanently'; }
    }
  });
  async function enter() { signedIn = true; $('login-view').hidden = true; $('admin-view').hidden = false; $('sign-out').hidden = false; $('password').value = ''; updateMenuHeight(); await refresh(); }
  $('login-form').addEventListener('submit', async event => {
    event.preventDefault(); const button = event.submitter; button.disabled = true; $('login-message').textContent = '';
    try { await api('/api/login', { method:'POST', body:JSON.stringify({password:$('password').value.toLowerCase()}) }); await enter(); }
    catch (error) { $('login-message').textContent = error.message; }
    finally { button.disabled = false; }
  });
  $('password').addEventListener('input', () => { $('password').value = $('password').value.toLowerCase(); });
  $('sign-out').addEventListener('click', async () => {
    // Clear every private DOM node immediately, before the network response.
    clearPrivate(); location.hash = '#students';
    try { await api('/api/logout', {method:'POST'}); $('login-message').textContent = 'You are signed out.'; }
    catch { $('login-message').textContent = 'The page is cleared. Sign-out could not reach the server; close this browser window to finish.'; }
  });
  $('refresh').addEventListener('click', async () => { try { await refresh(); message('Student list refreshed.'); } catch (error) { if (signedIn) message(error.message,true); } });
  const filterList = () => { $('paused-students').open = $('filter').value === 'paused' || Boolean($('search').value.trim()); showList(); };
  $('search').addEventListener('input',filterList); $('filter').addEventListener('change',filterList);
  $('firstName').addEventListener('input',suggestedAddress); $('lastName').addEventListener('input',suggestedAddress);
  $('studentId').addEventListener('input', () => { addressEdited = true; $('studentId').value = $('studentId').value.toLowerCase(); });
  $('status').addEventListener('change',updateSaveLabel);
  $('reveal-password').addEventListener('click', () => {
    if (!signedIn || !loginDetails?.password) return;
    const show = $('current-password').type === 'password';
    $('current-password').type = show ? 'text' : 'password';
    $('reveal-password').textContent = show ? 'Hide password' : 'Show password';
    $('reveal-password').setAttribute('aria-pressed', String(show));
  });
  $('refresh-login-details').addEventListener('click', () => { if (signedIn) void loadLoginDetails(current); });
  $('copy-login-details').addEventListener('click', async () => {
    if (!signedIn || !current) return;
    // Read again so a password changed in another window is not copied stale.
    const data = await loadLoginDetails(current), request = loginRequest;
    if (!data?.password || !data.url || !data.active) return;
    const text = 'English Ladder — ' + data.firstName + '\nSign in: ' + data.url + '\nStudent ID: ' + data.studentId + '\nPassword: ' + data.password;
    try {
      await navigator.clipboard.writeText(text);
      if (signedIn && request === loginRequest) $('login-details-status').textContent = 'Login details copied. You can paste them into your message to the student.';
    } catch {
      if (!signedIn || request !== loginRequest) return;
      $('copy-login-text').value = text; $('copy-fallback').hidden = false;
      $('copy-login-text').focus(); $('copy-login-text').select();
      $('login-details-status').textContent = 'Automatic copy is unavailable. Copy the selected details below.';
    }
  });
  for (const id of ['newPassword','confirmPassword']) $(id).addEventListener('input', () => { $(id).value = $(id).value.toLowerCase(); });
  $('student-form').addEventListener('submit', async event => {
    event.preventDefault(); const version = epoch, editing = current;
    if (!signedIn || !activityTools.length || saving || deleting || editing?.deletionPending) return;
    const input = Object.fromEntries(fields.map(field => [field,$(field).value]));
    input.visibleActivities = [...$('student-activities').querySelectorAll('input:checked')].map(box => box.value);
    input.zoomNames = $('zoomNames').value.split(/\r?\n/).map(v=>v.trim()).filter(Boolean);
    if ($('newPassword').value || $('confirmPassword').value) {
      if ($('newPassword').value.toLowerCase() !== $('confirmPassword').value.toLowerCase()) { message('The two student passwords do not match.', true); return; }
      input.newPassword = $('newPassword').value.toLowerCase(); input.confirmPassword = $('confirmPassword').value.toLowerCase();
    }
    if (editing) input.revision = editing.revision;
    saving = true; $('open-delete').disabled = true; $('save-student').disabled = true; $('save-state').textContent = 'Saving…'; message('');
    try {
      const data = await api('/api/admin/students' + (editing ? '/' + editing.key : ''), {method:editing?'PUT':'POST',body:JSON.stringify(input)});
      if (!signedIn || version !== epoch) return;
      students = students.filter(s=>s.key!==data.student.key).concat(data.student).sort((a,b)=>(a.firstName+a.lastName).localeCompare(b.firstName+b.lastName));
      history.replaceState(null, '', '#students/' + data.student.key); route();
      message(data.student.status === 'active' ? 'Saved. This student’s site is active and linked to the nightly updates.' : 'Saved. This account is ' + data.student.status + '.');
      $('save-state').textContent = 'Saved';
      void refreshQuizStatuses();
    } catch(error) { if(signedIn && version===epoch){message(error.message,true);$('save-state').textContent='Not saved';} }
    finally { saving = false; $('save-student').disabled = Boolean(current?.deletionPending); $('open-delete').disabled = false; }
  });
  $('sheet-paste').addEventListener('input',()=>{importRows=null;$('import-preview').hidden=true;$('import-names').replaceChildren();});
  $('preview-import').addEventListener('click',async()=>{
    const version=epoch; $('preview-import').disabled=true; message('');
    try {
      const rows=$('sheet-paste').value.trim().split(/\r?\n/).map(row=>row.split('\t'));
      const data=await api('/api/admin/import/preview',{method:'POST',body:JSON.stringify({rows})});
      if(!signedIn||version!==epoch)return;
      importRows=rows;$('import-names').replaceChildren();
      data.students.forEach(s=>$('import-names').append(element('li',s.source.name)));
      $('import-count').textContent=data.students.length+' students ready to review · '+data.excluded+' checked or expired rows excluded';$('import-preview').hidden=false;
    }catch(error){if(signedIn&&version===epoch)message(error.message,true);}finally{$('preview-import').disabled=false;}
  });
  $('confirm-import').addEventListener('click',async()=>{
    if(!importRows)return; const version=epoch; $('confirm-import').disabled=true;
    try {
      const result=await api('/api/admin/import',{method:'POST',body:JSON.stringify({rows:importRows})});
      if(!signedIn||version!==epoch)return;
      importRows=null;$('sheet-paste').value='';$('import-names').replaceChildren();$('import-preview').hidden=true;
      await refresh();history.replaceState(null,'','#students');route();message('Imported '+result.imported+' private drafts. '+result.skipped+' existing records were left unchanged. '+result.excluded+' checked or expired rows were excluded.');
    }catch(error){if(signedIn&&version===epoch)message(error.message,true);}finally{$('confirm-import').disabled=false;}
  });
  window.addEventListener('hashchange',()=>{message('');route();});
  window.addEventListener('resize',updateMenuHeight);
  window.addEventListener('pagehide',clearPrivate);
  window.addEventListener('pageshow',event=>{if(event.persisted)restore();});
  const common = {'America/New_York':'Eastern time — New York','America/Chicago':'Central time — Chicago','America/Denver':'Mountain time — Denver','America/Los_Angeles':'Pacific time — Los Angeles','Asia/Tokyo':'Japan — Tokyo','Europe/Berlin':'Central Europe — Berlin','Europe/London':'United Kingdom — London','Asia/Kolkata':'India — Kolkata'};
  const zones=[...Object.keys(common),...(Intl.supportedValuesOf?.('timeZone')||[]).filter(z=>!common[z])];
  for(const zone of zones){const option=element('option',common[zone]||zone.replaceAll('_',' '));option.value=zone;$('timeZone').append(option);}
  async function restore(){try{const session=await api('/api/session');if(session.administrator)await enter();}catch(error){if(signedIn)message(error.message,true);}}
  restore();
})();
