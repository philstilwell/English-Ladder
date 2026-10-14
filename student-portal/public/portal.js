(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const sections = ['overview', 'assessments', 'sessions', 'feedback'];
  let authenticated = false;
  let checking = false;
  let identityRevision = 0;

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

  function show(view) {
    for (const id of ['loading', 'login-view', 'dashboard-view', 'unavailable-view']) $(id).hidden = id !== view;
    $('logout').hidden = view !== 'dashboard-view';
  }

  function clearIdentity() {
    identityRevision += 1;
    authenticated = false;
    for (const id of ['student-name', 'teacher-student-name', 'avatar', 'account-address']) $(id).textContent = '';
    $('dashboard-title').textContent = 'Welcome back.';
    $('teacher-banner').hidden = true;
    document.title = 'Your student space · English Ladder';
  }

  function showLogin(message = '') {
    clearIdentity();
    $('password').value = '';
    $('password').type = 'password';
    $('show-password').textContent = 'Show';
    $('show-password').setAttribute('aria-label', 'Show password');
    $('show-password').setAttribute('aria-pressed', 'false');
    $('login-error').textContent = message;
    $('login-error').hidden = !message;
    show('login-view');
  }

  function navigate() {
    const selected = sections.includes(location.hash.slice(1)) ? location.hash.slice(1) : 'overview';
    for (const id of sections) $(id).hidden = selected !== id;
    for (const link of document.querySelectorAll('.section-nav a')) {
      if (link.hash === `#${selected}`) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    }
  }

  function showDashboard(data, focus = false) {
    authenticated = true;
    const { name, id } = data.student;
    const teacher = data.role === 'teacher';
    $('student-name').textContent = name;
    $('teacher-student-name').textContent = name;
    $('avatar').textContent = name.split(/\s+/).map(part => part[0]).slice(0, 2).join('').toUpperCase();
    $('account-address').textContent = `${id}.englishladder.com`;
    $('dashboard-title').textContent = teacher ? `${name}’s space` : `Welcome back, ${name.split(/\s+/)[0]}.`;
    $('teacher-banner').hidden = !teacher;
    $('account-status').textContent = teacher ? 'Teacher access is active. Assessments, session notes, and feedback will be added in the next stage.' : '';
    $('password').value = '';
    document.title = 'My learning space · English Ladder';
    navigate();
    show('dashboard-view');
    if (focus) $('dashboard-title').focus();
  }

  async function start() {
    show('loading');
    try {
      const context = await api('/api/context');
      $('student-id').value = context.id;
      try { showDashboard(await api('/api/session')); }
      catch (error) { if (error.status === 401) showLogin(); else throw error; }
    } catch (error) {
      clearIdentity();
      $('unavailable-message').textContent = error.message;
      show('unavailable-view');
    }
  }

  $('password').addEventListener('input', () => {
    const field = $('password');
    const start = field.selectionStart;
    const end = field.selectionEnd;
    field.value = field.value.toLowerCase();
    field.setSelectionRange(start, end);
    field.removeAttribute('aria-invalid');
    $('login-error').hidden = true;
  });

  $('show-password').addEventListener('click', () => {
    const visible = $('password').type === 'password';
    $('password').type = visible ? 'text' : 'password';
    $('show-password').textContent = visible ? 'Hide' : 'Show';
    $('show-password').setAttribute('aria-label', visible ? 'Hide password' : 'Show password');
    $('show-password').setAttribute('aria-pressed', String(visible));
  });

  $('login-form').addEventListener('submit', async event => {
    event.preventDefault();
    if ($('login-submit').disabled) return;
    $('login-submit').disabled = true;
    $('login-submit').textContent = 'Opening your space…';
    $('login-error').hidden = true;
    try {
      const data = await api('/api/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ password: $('password').value.toLowerCase() }) });
      showDashboard(data, true);
    } catch (error) {
      $('login-error').textContent = error.message;
      $('login-error').hidden = false;
      $('password').setAttribute('aria-invalid', 'true');
      $('password').focus();
    } finally {
      $('login-submit').disabled = false;
      $('login-submit').textContent = 'Open my space →';
    }
  });

  $('logout').addEventListener('click', async () => {
    $('logout').disabled = true;
    try {
      await api('/api/logout', { method: 'POST' });
      history.replaceState(null, '', location.pathname);
      showLogin();
      $('password').focus();
    } catch (error) { $('account-status').textContent = `Could not sign out. ${error.message}`; }
    finally { $('logout').disabled = false; }
  });

  async function checkSession() {
    if (!authenticated || checking || document.hidden) return;
    checking = true;
    const revision = identityRevision;
    try {
      const data = await api('/api/session');
      if (revision === identityRevision) showDashboard(data);
    }
    catch (error) {
      if (revision !== identityRevision) return;
      if (error.status === 401) showLogin('Your session has ended. Please sign in again.');
      else { clearIdentity(); $('unavailable-message').textContent = error.message; show('unavailable-view'); }
    } finally { checking = false; }
  }

  // Clear restored personal content before trusting the browser's back/forward cache.
  window.addEventListener('pageshow', event => { if (event.persisted) { clearIdentity(); start(); } });
  document.addEventListener('visibilitychange', checkSession);
  window.addEventListener('hashchange', navigate);
  $('retry').addEventListener('click', start);
  setInterval(checkSession, 60_000);
  start();
})();
