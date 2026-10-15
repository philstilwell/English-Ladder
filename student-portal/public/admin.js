'use strict';
(() => {
  const $ = id => document.getElementById(id);
  let signedIn = false, epoch = 0, students = [], current = null, importRows = null, addressEdited = false;
  const fields = ['firstName','lastName','nickname','studentId','status','timeZone','course','fileNumber','email','otherEmail','staff','contactedOn','endsOn','hoursAuthorized','hoursUsed','hoursPending','hoursRemaining','notes'];
  const displayDate = value => value ? new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeZone: 'UTC' }).format(new Date(value)) : '';
  const displayTime = value => value ? new Intl.DateTimeFormat('en-US', { dateStyle: 'medium', timeStyle: 'short', timeZone: 'America/New_York' }).format(new Date(value)) + ' Eastern' : '';
  const element = (tag, text, className) => { const node = document.createElement(tag); if (text != null) node.textContent = text; if (className) node.className = className; return node; };
  function message(text, error = false) { $('message').textContent = text; $('message').hidden = !text; $('message').classList.toggle('error', error); }
  function clearPrivate() {
    epoch++; signedIn = false; students = []; current = null; importRows = null;
    $('admin-view').hidden = true; $('login-view').hidden = false; $('sign-out').hidden = true;
    $('student-rows').replaceChildren(); $('import-names').replaceChildren(); $('student-form').reset();
    $('sheet-paste').value = ''; $('password').value = ''; $('search').value = ''; $('filter').value = 'all';
    $('edit-title').textContent = ''; $('source-note').textContent = ''; $('open-site').removeAttribute('href');
    $('activation-note').textContent = ''; $('save-state').textContent = ''; $('import-preview').hidden = true;
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
    if (!response.ok) throw new Error(data.error || 'The request could not be saved. Please try again.');
    return data;
  }
  function showList() {
    const query = $('search').value.trim().toLowerCase(), filter = $('filter').value;
    const shown = students.filter(s => (filter === 'all' || s.status === filter) && [s.firstName,s.lastName,s.studentId,...s.zoomNames].join(' ').toLowerCase().includes(query));
    $('student-rows').replaceChildren();
    $('active-count').textContent = students.filter(s => s.status === 'active').length;
    $('draft-count').textContent = students.filter(s => s.status === 'draft').length;
    $('list-count').textContent = shown.length + ' of ' + students.length + ' students';
    $('empty-list').hidden = shown.length > 0;
    for (const student of shown) {
      const row = element('tr'), name = element('td'), site = element('td'), course = element('td'), status = element('td'), action = element('td');
      const link = element('a', [student.firstName,student.lastName].filter(Boolean).join(' '), 'student-name'); link.href = '#students/' + student.key; name.append(link);
      if (student.nickname) name.append(element('span', student.nickname, 'detail'));
      site.append(element('span', student.studentId ? student.studentId + '.englishladder.com' : 'Site not activated'));
      site.append(element('span', student.zoomNames.length ? 'Zoom: ' + student.zoomNames.join(' · ') : 'Add a Zoom name to connect lessons', 'detail'));
      course.append(element('span', student.hoursRemaining != null ? student.hoursRemaining + ' hours remaining' : student.course || 'Course details not added'));
      if (student.endsOn) course.append(element('span', 'Ends ' + displayDate(student.endsOn), 'detail'));
      status.append(element('span', {active:'Active',draft:'Draft',paused:'Paused'}[student.status], 'status-pill ' + student.status));
      const edit = element('a', 'Edit account →', 'edit-link'); edit.href = link.href; edit.setAttribute('aria-label', 'Edit account for ' + student.firstName + ' ' + student.lastName); action.append(edit);
      row.append(name,site,course,status,action); $('student-rows').append(row);
    }
  }
  async function refresh() {
    const version = epoch;
    const data = await api('/api/admin/students');
    if (!signedIn || version !== epoch) return;
    students = data.students; showList(); route();
    try {
      const status = await api('/api/admin/automation');
      if (!signedIn || version !== epoch) return;
      $('schedule-state').textContent = status.connectionError ? 'Zoom needs attention. Open a student’s Quiz results to check the connection.' : status.connected && status.enabled ? 'On the server · adjusts for daylight saving' : 'Automatic updates are not connected yet.';
      $('last-check').textContent = status.lastCheck ? 'Last check: ' + displayTime(status.lastCheck) + (status.needsAttention ? ' · ' + status.needsAttention + ' sessions need attention' : '') : 'The first nightly check is still ahead.';
    } catch (error) { if (signedIn && version === epoch) $('schedule-state').textContent = 'Server status is temporarily unavailable.'; }
  }
  function suggestedAddress() {
    const first = $('firstName').value.trim().normalize('NFKD').replace(/[^a-z]/gi, ''), last = $('lastName').value.trim().split(/\s+/).at(-1)?.normalize('NFKD').replace(/[^a-z]/gi, '');
    if (first && last && !addressEdited && !current?.activated) $('studentId').value = (first[0] + last[0]).toLowerCase() + new Intl.DateTimeFormat('en', { timeZone: 'America/New_York', year: '2-digit' }).format(new Date());
  }
  function editStudent(student) {
    current = student; addressEdited = Boolean(student?.studentId);
    $('student-form').reset(); $('save-state').textContent = '';
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
    if (student && !student.studentId) suggestedAddress();
    updateSaveLabel();
  }
  function updateSaveLabel() { $('save-student').textContent = $('status').value === 'active' && !current?.activated ? 'Save and activate site' : 'Save changes'; }
  function route() {
    if (!signedIn) return;
    const hash = location.hash || '#students';
    for (const id of ['list-view','edit-view','import-view']) $(id).hidden = true;
    for (const id of ['list-nav','register-nav','import-nav']) $(id).removeAttribute('aria-current');
    if (hash === '#register') { $('edit-view').hidden = false; $('register-nav').setAttribute('aria-current','page'); editStudent(null); }
    else if (hash.startsWith('#students/')) {
      const student = students.find(s => s.key === hash.slice(10));
      if (!student) { message('This student could not be found.', true); $('list-view').hidden = false; }
      else { $('edit-view').hidden = false; editStudent(student); }
      $('list-nav').setAttribute('aria-current','page');
    } else if (hash === '#import') { $('import-view').hidden = false; $('import-nav').setAttribute('aria-current','page'); }
    else { $('list-view').hidden = false; $('list-nav').setAttribute('aria-current','page'); showList(); }
  }
  async function enter() { signedIn = true; $('login-view').hidden = true; $('admin-view').hidden = false; $('sign-out').hidden = false; $('password').value = ''; await refresh(); }
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
  $('search').addEventListener('input',showList); $('filter').addEventListener('change',showList);
  $('firstName').addEventListener('input',suggestedAddress); $('lastName').addEventListener('input',suggestedAddress);
  $('studentId').addEventListener('input', () => { addressEdited = true; $('studentId').value = $('studentId').value.toLowerCase(); });
  $('status').addEventListener('change',updateSaveLabel);
  $('student-form').addEventListener('submit', async event => {
    event.preventDefault(); const version = epoch, editing = current;
    const input = Object.fromEntries(fields.map(field => [field,$(field).value]));
    input.zoomNames = $('zoomNames').value.split(/\r?\n/).map(v=>v.trim()).filter(Boolean);
    if (editing) input.revision = editing.revision;
    $('save-student').disabled = true; $('save-state').textContent = 'Saving…'; message('');
    try {
      const data = await api('/api/admin/students' + (editing ? '/' + editing.key : ''), {method:editing?'PUT':'POST',body:JSON.stringify(input)});
      if (!signedIn || version !== epoch) return;
      students = students.filter(s=>s.key!==data.student.key).concat(data.student).sort((a,b)=>(a.firstName+a.lastName).localeCompare(b.firstName+b.lastName));
      history.replaceState(null, '', '#students/' + data.student.key); route();
      message(data.student.status === 'active' ? 'Saved. This student’s site is active and linked to the nightly updates.' : 'Saved. This account is ' + data.student.status + '.');
      $('save-state').textContent = 'Saved';
    } catch(error) { if(signedIn && version===epoch){message(error.message,true);$('save-state').textContent='Not saved';} }
    finally { $('save-student').disabled=false; }
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
  window.addEventListener('pagehide',clearPrivate);
  window.addEventListener('pageshow',event=>{if(event.persisted)restore();});
  const common = {'America/New_York':'Eastern time — New York','America/Chicago':'Central time — Chicago','America/Denver':'Mountain time — Denver','America/Los_Angeles':'Pacific time — Los Angeles','Asia/Tokyo':'Japan — Tokyo','Europe/Berlin':'Central Europe — Berlin','Europe/London':'United Kingdom — London','Asia/Kolkata':'India — Kolkata'};
  const zones=[...Object.keys(common),...(Intl.supportedValuesOf?.('timeZone')||[]).filter(z=>!common[z])];
  for(const zone of zones){const option=element('option',common[zone]||zone.replaceAll('_',' '));option.value=zone;$('timeZone').append(option);}
  async function restore(){try{const session=await api('/api/session');if(session.administrator)await enter();}catch(error){if(signedIn)message(error.message,true);}}
  restore();
})();
