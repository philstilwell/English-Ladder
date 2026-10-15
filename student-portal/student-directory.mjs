// This database is reachable only through the Worker binding. Public routes never
// expose it; the administrator API uses a host-bound teacher session.
import { makeStudentPassword, matchesStudentPassword, encryptStudentPassword, decryptStudentPassword } from './student-password.mjs';
const json = (value, status = 200) => Response.json(value, { status });
const adminRecord = ({ passwordCredential, passwordCopy, ...record }) => ({ ...record, hasCustomPassword: Boolean(passwordCredential) });
export const STUDENT_ID = /^[a-z]{2,8}\d{2}(?:-[a-z0-9]{1,12})?$/;
const RESERVED = new Set(['phil', 'www', 'admin', 'students', 'mail', 'api']);
const norm = value => String(value || '').trim().toLowerCase();
const fail = message => { throw new Error(message); };
const text = (value, limit = 200) => {
  if (value == null) return '';
  if (typeof value !== 'string' || value.length > limit || /[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(value)) fail('Please shorten or check the text you entered.');
  return value.trim();
};
const date = value => {
  const v = text(value, 10);
  if (v && (!/^\d{4}-\d{2}-\d{2}$/.test(v) || new Date(v + 'T12:00:00Z').toISOString().slice(0, 10) !== v)) fail('Please enter a valid date.');
  return v;
};
const hours = value => {
  if (value === '' || value == null) return null;
  const number = Number(value);
  if (!Number.isFinite(number) || Math.abs(number) > 100000) fail('Please enter a valid number of hours.');
  return number;
};
export function validateStudent(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) fail('Please check the student details.');
  const firstName = text(input.firstName, 80), lastName = text(input.lastName, 120);
  if (!firstName) fail('Enter the student’s first name.');
  const status = input.status || 'draft';
  if (!['draft', 'active', 'paused'].includes(status)) fail('Choose a valid account status.');
  const studentId = text(input.studentId, 30).toLowerCase();
  if (studentId && (!STUDENT_ID.test(studentId) || RESERVED.has(studentId))) fail('Use initials and a two-digit year, such as “ab26”. Add a suffix if needed, such as “ab26-2”.');
  if (!Array.isArray(input.zoomNames) || input.zoomNames.length > 10) fail('Enter up to ten Zoom names.');
  const zoomNames = input.zoomNames.map(v => text(v, 100)).filter(Boolean);
  if (new Set(zoomNames.map(norm)).size !== zoomNames.length) fail('Remove the repeated Zoom name.');
  const timeZone = text(input.timeZone || 'America/New_York', 80);
  try { new Intl.DateTimeFormat('en', { timeZone }); } catch { fail('Choose a valid time zone.'); }
  if (status === 'active' && (!lastName || !studentId || !zoomNames.length)) fail('To activate the site, enter both names, a student address, and at least one exact Zoom name.');
  return { firstName, lastName, studentId, status, zoomNames, timeZone,
    nickname: text(input.nickname, 100), course: text(input.course), fileNumber: text(input.fileNumber, 60),
    staff: text(input.staff, 100), email: text(input.email, 254), otherEmail: text(input.otherEmail, 254),
    endsOn: date(input.endsOn), contactedOn: date(input.contactedOn),
    hoursAuthorized: hours(input.hoursAuthorized), hoursUsed: hours(input.hoursUsed),
    hoursPending: hours(input.hoursPending), hoursRemaining: hours(input.hoursRemaining), notes: text(input.notes, 4000) };
}

const SHEET_ZONES = {
  'Eastern Time (US & Canada)': 'America/New_York', 'Central Time (US & Canada)': 'America/Chicago',
  'Mountain Time (US & Canada)': 'America/Denver', 'Pacific Time (US & Canada)': 'America/Los_Angeles',
  'Osaka, Sapporo, Tokyo': 'Asia/Tokyo', 'Chennai, Kolkata, Mumbai, New Delhi': 'Asia/Kolkata',
  'Dublin, Edinburgh, Lisbon, London': 'Europe/London',
  'Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna': 'Europe/Berlin',
};
function sheetDate(value) {
  if (!value) return '';
  const parsed = Date.parse(String(value));
  if (!Number.isFinite(parsed)) fail('One spreadsheet date could not be read. Check the date cells before importing.');
  return new Date(parsed).toISOString().slice(0, 10);
}
export function inspectStudentRows(rows, now = Date.now()) {
  if (!Array.isArray(rows) || rows.length < 2 || rows.length > 201 || rows.some(r => !Array.isArray(r) || r.length > 40)) fail('Paste a header row and up to 200 students.');
  const index = rows.findIndex(r => r.includes('Learner/Group Name') && r.includes('Course Name'));
  if (index < 0) fail('Include the “New-Students” column headings when copying the cells.');
  const header = rows[index], get = (row, title) => row[header.indexOf(title)] ?? '';
  if (!header.includes('Ends On')) fail('Include the “Ends On” column so expired courses can be excluded.');
  const checkboxColumn = header.indexOf('Course Name') - 1;
  if (checkboxColumn < 0) fail('Include the checkbox column immediately before “Course Name” (column C) when copying the spreadsheet.');
  const today = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(now));
  const excluded = [];
  const students = rows.slice(index + 1).filter(r => get(r, 'Name') || get(r, 'Learner/Group Name')).map(row => {
    const sourceName = text(get(row, 'Name') || get(row, 'Learner/Group Name'));
    const checkbox = norm(row[checkboxColumn]);
    if (!['true', 'false', ''].includes(checkbox)) fail('The checkbox column must contain TRUE or FALSE. Include column C and the headings.');
    const endsOn = sheetDate(get(row, 'Ends On'));
    const sourceKey = norm(get(row, 'File No.')) + ':' + norm(sourceName);
    if (checkbox === 'true' || endsOn && endsOn < today) {
      excluded.push({ key: sourceKey, reason: checkbox === 'true' ? 'checked' : 'expired' });
      return null;
    }
    const words = sourceName.replace(/\s*\([^)]*\)\s*/g, ' ').trim().split(/\s+/);
    const zone = text(get(row, 'Learner Time Zone'));
    const record = validateStudent({ firstName: words.shift(), lastName: words.join(' '), status: 'draft', zoomNames: [],
      timeZone: SHEET_ZONES[zone] || 'America/New_York', course: get(row, 'Course Name'), fileNumber: String(get(row, 'File No.')),
      staff: get(row, 'Staff'), email: get(row, 'Gmail'), otherEmail: get(row, 'Other EM'),
      endsOn, contactedOn: sheetDate(get(row, 'Contacted')),
      hoursAuthorized: get(row, 'Hours Authorized'), hoursUsed: get(row, 'Hours Used'),
      hoursPending: get(row, 'Hours Upcoming/Pending'), hoursRemaining: get(row, 'Unscheduled Hours'),
      notes: zone && !SHEET_ZONES[zone] ? 'Check time zone from spreadsheet: ' + zone : '',
    });
    return { ...record, source: { tab: 'New-Students', name: sourceName, timeZone: zone,
      key: sourceKey, importedAt: new Date().toISOString() } };
  }).filter(Boolean);
  return { students, excluded };
}
export const parseStudentRows = (rows, now) => inspectStudentRows(rows, now).students;

export function directoryRequest(env, path, body, method = body ? 'POST' : 'GET') {
  if (!env.STUDENT_DIRECTORY) throw new Error('Directory unavailable');
  return env.STUDENT_DIRECTORY.get(env.STUDENT_DIRECTORY.idFromName('students')).fetch(new Request('https://directory.internal' + path,
    { method, ...(body ? { headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : {}) }));
}
export async function directoryStudents(env) {
  const response = await directoryRequest(env, '/automation');
  if (!response.ok) throw new Error('Directory unavailable');
  return response.json();
}

export class StudentDirectory {
  constructor(state, env) { this.storage = state.storage; this.env = env; this.ready = null; }
  async initialize() {
    if (!this.ready) this.ready = this.storage.transaction(async txn => {
      if (await txn.get('initialized')) return;
      const accounts = JSON.parse(this.env.STUDENT_ACCOUNTS || '{}'), automation = JSON.parse(this.env.QUIZ_STUDENTS || '{}');
      const records = Object.entries(accounts).map(([studentId, account]) => {
        const auto = automation[studentId];
        return { ...validateStudent({ firstName: account.name.trim().split(/\s+/)[0], lastName: '', nickname: account.nickname || '',
          studentId, status: 'draft', zoomNames: auto?.zoomNames || [], timeZone: auto?.timeZone || 'America/New_York' }),
          key: crypto.randomUUID(), status: 'active', activated: true, revision: 1,
          startAfter: auto?.startAfter || new Date().toISOString(), lessonTimeZone: auto?.timeZone || 'America/New_York',
          createdAt: new Date().toISOString(), updatedAt: new Date().toISOString() };
      });
      await txn.put({ initialized: true, revision: 1, ...Object.fromEntries(records.map(r => ['student:' + r.key, r])) });
    }).catch(error => { this.ready = null; throw error; });
    return this.ready;
  }
  async records(storage = this.storage) { return [...(await storage.list({ prefix: 'student:' })).values()]; }
  async save(input, key) {
    return this.storage.transaction(async txn => {
      const records = await this.records(txn), previous = key ? records.find(r => r.key === key) : null;
      if (key && !previous) return json({ error: 'Student not found.' }, 404);
      if (previous && input.revision !== previous.revision) return json({ error: 'This record changed in another window. Reload it before saving.' }, 409);
      const values = validateStudent(input);
      if (previous?.activated && (previous.studentId !== values.studentId || values.status === 'draft')) return json({ error: 'An activated student keeps the same address. Use “Paused” to stop access and updates.' }, 400);
      const others = records.filter(r => r.key !== key);
      if (values.studentId && others.some(r => r.studentId === values.studentId)) return json({ error: 'That address is already assigned. Add a distinct suffix.' }, 409);
      if (values.zoomNames.some(n => others.some(r => r.zoomNames.some(other => norm(other) === norm(n))))) return json({ error: 'That Zoom name belongs to another student. Each Zoom name must identify one student.' }, 409);
      if (!previous && records.length >= 1000) return json({ error: 'The directory is full. Please contact support.' }, 400);
      const recordKey = previous?.key || crypto.randomUUID();
      const newCredential = await makeStudentPassword(this.env, input, recordKey);
      const passwordCredential = newCredential || previous?.passwordCredential;
      const passwordCopy = newCredential ? await encryptStudentPassword(this.env, input.newPassword, recordKey, newCredential) : previous?.passwordCopy;
      if (values.status === 'active' && !passwordCredential && !this.env.STUDENT_PASSWORD && !JSON.parse(this.env.STUDENT_ACCOUNTS || '{}')[values.studentId]) return json({ error: 'Assign a student password before activating this account.' }, 503);
      const now = new Date().toISOString(), activated = previous?.activated || values.status === 'active';
      const record = { ...values, key: recordKey, revision: (previous?.revision || 0) + 1,
        activated, startAfter: previous?.startAfter || (activated ? now : null),
        lessonTimeZone: previous?.lessonTimeZone || 'America/New_York', createdAt: previous?.createdAt || now, updatedAt: now,
        ...(previous?.source ? { source: previous.source } : {}), ...(passwordCredential ? { passwordCredential } : {}), ...(passwordCopy ? { passwordCopy } : {}) };
      await txn.put({ ['student:' + record.key]: record, revision: (await txn.get('revision') || 0) + 1 });
      return json({ student: adminRecord(record) }, previous ? 200 : 201);
    });
  }
  async loginDetails(key) {
    const record = await this.storage.get('student:' + key);
    if (!record) return json({ error:'Student not found.' }, 404);
    let password = null;
    if (record.passwordCredential) {
      if (record.passwordCopy) {
        try { password = await decryptStudentPassword(this.env, record.passwordCopy, key, record.passwordCredential); }
        catch { return json({ error:'The saved password could not be opened. Please try again later.' }, 503); }
      }
    } else {
      password = JSON.parse(this.env.STUDENT_ACCOUNTS || '{}')[record.studentId]?.password || this.env.STUDENT_PASSWORD || null;
      if (password) password = password.toLowerCase();
    }
    // Never disclose the universal credential, even after a configuration error.
    if (password && password === this.env.TEACHER_PASSWORD?.toLowerCase()) return json({ error:'Assign a separate student password before sharing login details.' }, 409);
    return json({ firstName:record.firstName.split(/\s+/)[0], studentId:record.studentId,
      url:record.studentId ? 'https://' + record.studentId + '.englishladder.com/' : null,
      active:record.status === 'active', password,
      message:password ? null : record.passwordCredential ? 'This older password has no saved copy. Assign a new password below to make it available here.' : 'Assign a student password below.' });
  }
  async restorePasswordCopy(key, input) {
    // Restore only a known, verified current password. This does not rotate the
    // verifier or revoke student sessions; concurrent account changes conflict.
    return this.storage.transaction(async txn => {
      const record = await txn.get('student:' + key);
      if (!record) return json({ error:'Student not found.' }, 404);
      if (input.revision !== record.revision) return json({ error:'This record changed. Reload it before saving.' }, 409);
      if (!record.passwordCredential || typeof input.password !== 'string' || input.password.length > 128 || !input.password || !await matchesStudentPassword(this.env, record.passwordCredential, key, input.password)) return json({ error:'The password does not match the current student login.' }, 400);
      if (input.password.toLowerCase() === this.env.TEACHER_PASSWORD?.toLowerCase()) return json({ error:'Use a separate student password.' }, 400);
      const passwordCopy = await encryptStudentPassword(this.env, input.password, key, record.passwordCredential);
      await txn.put({ ['student:' + key]:{ ...record, passwordCopy, revision:record.revision + 1, updatedAt:new Date().toISOString() }, revision:(await txn.get('revision') || 0) + 1 });
      return json({ saved:true });
    });
  }
  async fetch(request) {
    await this.initialize();
    const url = new URL(request.url), path = url.pathname;
    try {
      if (path === '/students' && request.method === 'GET') return json({ students: (await this.records()).map(adminRecord).sort((a,b) => (a.firstName + a.lastName).localeCompare(b.firstName + b.lastName)) });
      const loginDetails = path.match(/^\/students\/([\w-]{36})\/login-details$/);
      if (loginDetails && request.method === 'GET') return await this.loginDetails(loginDetails[1]);
      if (loginDetails && request.method === 'PUT') return await this.restorePasswordCopy(loginDetails[1], await request.json());
      if ((path.startsWith('/account/') || path.startsWith('/integration-account/')) && request.method === 'GET') {
        const integration = path.startsWith('/integration-account/'), id = path.slice(integration ? 21 : 9);
        const record = (await this.records()).find(r => r.studentId === id && (r.status === 'active' || integration && r.activated));
        return record ? json({ id: record.studentId, name: record.firstName.split(/\s+/)[0], nickname: record.nickname || record.firstName.split(/\s+/)[0],
          ...(record.passwordCredential ? { passwordCredential: record.passwordCredential, credentialAccountKey: record.key } : {}) }) : json({ error: 'Unknown account.' }, 404);
      }
      if (path === '/automation' && request.method === 'GET') {
        const records = (await this.records()).filter(r => r.status === 'active' && r.zoomNames.length && r.startAfter);
        return json({ revision: await this.storage.get('revision'), students: Object.fromEntries(records.map(r => [r.studentId,
          { firstName: r.firstName.split(/\s+/)[0], zoomNames: r.zoomNames, timeZone: r.lessonTimeZone, startAfter: r.startAfter }])) });
      }
      if (path === '/students' && request.method === 'POST') return await this.save(await request.json());
      if (/^\/students\/[\w-]{36}$/.test(path) && request.method === 'PUT') return await this.save(await request.json(), path.slice(10));
      if (['/import/preview', '/import'].includes(path) && request.method === 'POST') {
        const { rows, reconcileExcluded } = await request.json(), inspected = inspectStudentRows(rows), parsed = inspected.students;
        if (path === '/import/preview') return json({ students: parsed, excluded: inspected.excluded.length });
        return await this.storage.transaction(async txn => {
          let existing = await this.records(txn), removed = 0;
          if (reconcileExcluded === true) {
            const excludedKeys = new Set(inspected.excluded.map(row => row.key));
            // Reconcile only untouched import drafts. Never remove an activated,
            // manually edited, or unrelated account. Keep a private recovery copy.
            const removable = existing.filter(r => !r.activated && r.status === 'draft' && r.revision === 1 && excludedKeys.has(r.source?.key));
            for (const record of removable) {
              await txn.put({ ['excluded-import:' + record.key]: record });
              await txn.delete('student:' + record.key);
            }
            removed = removable.length;
            existing = existing.filter(r => !removable.some(old => old.key === r.key));
          }
          const keys = new Set(existing.map(r => r.source?.key).filter(Boolean));
          const names = new Set(existing.map(r => norm(r.firstName + ' ' + r.lastName)));
          const additions = parsed.filter(r => { if (keys.has(r.source.key) || names.has(norm(r.firstName + ' ' + r.lastName))) return false; keys.add(r.source.key); names.add(norm(r.firstName + ' ' + r.lastName)); return true; });
          if (existing.length + additions.length > 1000) return json({ error: 'Too many students.' }, 400);
          const records = additions.map(r => ({ ...r, key: crypto.randomUUID(), revision: 1, activated: false, startAfter: null,
            lessonTimeZone: 'America/New_York', createdAt: new Date().toISOString(), updatedAt: new Date().toISOString() }));
          await txn.put({ ...Object.fromEntries(records.map(r => ['student:' + r.key, r])), revision: (await txn.get('revision') || 0) + 1 });
          return json({ imported: records.length, skipped: parsed.length - records.length, excluded: inspected.excluded.length, removed });
        });
      }
      return json({ error: 'Not found.' }, 404);
    } catch (error) { return json({ error: error instanceof SyntaxError ? 'Please check the submitted data.' : error.message }, 400); }
  }
}
