import { directoryStudents, directoryRequest } from './student-directory.mjs';
import { authorQuiz, readTranscript, sessionId } from './server-quiz-model.mjs';
import { anonymizeTranscript } from './transcript-privacy.mjs';
import { TRANSCRIPT_PRIVACY_VERSION, reusableTranscript } from './transcript-cache.mjs';

const json = (data, status = 200) => Response.json(data, { status });
const encoder = new TextEncoder();
const hex = bytes => [...new Uint8Array(bytes)].map(b => b.toString(16).padStart(2, '0')).join('');
export const hash = async value => hex(await crypto.subtle.digest('SHA-256', encoder.encode(value)));
const noteIdValid = id => typeof id === 'string' && /^[\w-]{10,80}$/.test(id);
const safeError = error => [
  'zoom_reconnect', 'zoom_unavailable', 'transcript_unusable', 'transcript_too_large', 'ambiguous_student',
  'insufficient_evidence', 'invalid_evidence', 'content_review_failed', 'assessment_required', 'unsafe_content',
  'invalid_model_response', 'monthly_limit', 'daily_limit', 'meeting_pending', 'publish_failed', 'meeting_reference_missing', 'discovery_incomplete',
  'transcript_privacy_failed', 'source_changed', 'student_changed',
].includes(error.message) ? error.message : 'generation_failed';

export function studentsFor(env) {
  const students = JSON.parse(env.QUIZ_STUDENTS || '{}');
  for (const [id, student] of Object.entries(students)) {
    if (!/^[a-z0-9-]+$/.test(id) || typeof student.firstName !== 'string' || /\s/.test(student.firstName) ||
        !Array.isArray(student.zoomNames) || !student.zoomNames.length || student.zoomNames.some(n => typeof n !== 'string' || !n) ||
        !Number.isFinite(Date.parse(student.startAfter))) throw new Error('Invalid student configuration');
    new Intl.DateTimeFormat('en', { timeZone: student.timeZone });
  }
  return students;
}
export function configuredAutomation(env) {
  return Boolean(env.ZOOM_CLIENT_ID && env.ZOOM_CLIENT_SECRET && env.AI && Object.keys(studentsFor(env)).length);
}
export async function zoomSignatureValid(secret, request, body, now = Date.now()) {
  const timestamp = request.headers.get('x-zm-request-timestamp'), signature = request.headers.get('x-zm-signature');
  if (!secret || !/^\d{10}$/.test(timestamp || '') || Math.abs(now / 1000 - Number(timestamp)) > 300 ||
      !/^v0=[a-f0-9]{64}$/.test(signature || '')) return false;
  const key = await crypto.subtle.importKey('raw', encoder.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['verify']);
  const bytes = Uint8Array.from(signature.slice(3).match(/../g), h => parseInt(h, 16));
  return crypto.subtle.verify('HMAC', key, bytes, encoder.encode('v0:' + timestamp + ':' + body));
}
async function signedChallenge(secret, plainToken) {
  const key = await crypto.subtle.importKey('raw', encoder.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return hex(await crypto.subtle.sign('HMAC', key, encoder.encode(plainToken)));
}
async function boundedText(response, limit) {
  const reader = response.body?.getReader();
  if (!reader) return '';
  let size = 0; const chunks = [];
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    size += value.byteLength;
    if (size > limit) { await reader.cancel(); throw new Error('transcript_too_large'); }
    chunks.push(value);
  }
  const bytes = new Uint8Array(size); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
  return new TextDecoder().decode(bytes);
}

export function nightlyDate(time) {
  if (!Number.isFinite(time)) return null;
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date(time)).map(p => [p.type, p.value]));
  return parts.hour === '01' && parts.minute === '00' ? `${parts.year}-${parts.month}-${parts.day}` : null;
}

export class QuizAutomation {
  constructor(state, env) {
    this.storage = state.storage; this.env = env; this.authWork = null;
  }
  async students() {
    return this.env.STUDENT_DIRECTORY ? (await directoryStudents(this.env)).students : studentsFor(this.env);
  }
  async isConfigured() {
    return Boolean(this.env.ZOOM_CLIENT_ID && this.env.ZOOM_CLIENT_SECRET && this.env.AI && Object.keys(await this.students()).length);
  }
  async refreshDirectory() {
    if (!this.env.STUDENT_DIRECTORY) return;
    const directory = await directoryStudents(this.env);
    if (await this.storage.get('directory-revision') === directory.revision) return;
    for (const [key, job] of await this.storage.list({ prefix: 'job:' })) {
      if (job.status === 'needs_attention' && ['student_not_matched', 'ambiguous_student'].includes(job.lastError)) {
        await this.storage.put({ [key]: { ...job, status: 'pending', tries: 0, nextAt: 0 } });
      }
    }
    const dates = Object.values(directory.students).map(s => Date.parse(s.startAfter));
    if (dates.length) await this.storage.put({ 'discovery-since': new Date(Math.min(...dates)).toISOString() });
    await this.storage.put({ 'directory-revision': directory.revision });
  }
  async tokenRequest(params) {
    const response = await fetch('https://zoom.us/oauth/token', {
      method: 'POST', redirect: 'manual', signal: AbortSignal.timeout(30000),
      headers: { Authorization: 'Basic ' + btoa(this.env.ZOOM_CLIENT_ID + ':' + this.env.ZOOM_CLIENT_SECRET),
        'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(params),
    });
    if (!response.ok) {
      let code; try { code = JSON.parse(await boundedText(response, 16384)).error; } catch {}
      throw Object.assign(new Error('zoom_reconnect'), { httpStatus: response.status, apiCode: /^[a-z_]{1,40}$/.test(code || '') ? code : 'token_error' });
    }
    const tokens = JSON.parse(await boundedText(response, 16384));
    if (!tokens.access_token || !tokens.refresh_token || !Number.isFinite(tokens.expires_in)) throw new Error('zoom_reconnect');
    return { access: tokens.access_token, refresh: tokens.refresh_token, expiresAt: Date.now() + tokens.expires_in * 1000 };
  }
  async accessToken() {
    if (this.authWork) return this.authWork;
    this.authWork = (async () => {
      const saved = await this.storage.get('oauth');
      if (!saved) throw new Error('zoom_reconnect');
      if (saved.expiresAt > Date.now() + 60000) return saved.access;
      const next = await this.tokenRequest({ grant_type: 'refresh_token', refresh_token: saved.refresh });
      await this.storage.put({ oauth: { ...saved, ...next } });
      return next.access;
    })();
    try { return await this.authWork; } finally { this.authWork = null; }
  }
  async zoom(path, token, body) {
    const response = await fetch('https://api.zoom.us/v2' + path, {
      headers: { Authorization: 'Bearer ' + (token || await this.accessToken()), ...(body ? { 'Content-Type': 'application/json' } : {}) },
      ...(body ? { method: 'POST', body: JSON.stringify(body) } : {}),
      signal: AbortSignal.timeout(30000), redirect: 'manual',
    });
    if (!response.ok) {
      let code; try { code = JSON.parse(await boundedText(response, 16384)).code; } catch {}
      throw Object.assign(new Error(response.status === 401 || response.status === 403 ? 'zoom_reconnect' : 'zoom_unavailable'), { httpStatus: response.status, apiCode: Number.isInteger(code) ? code : 'api_error' });
    }
    return JSON.parse(await boundedText(response, 2000000));
  }
  async connect(origin, studentId) {
    if (!await this.isConfigured() || !(await this.students())[studentId]) return json({ error: 'The Zoom app still needs to be set up.' }, 503);
    const state = crypto.randomUUID() + crypto.randomUUID();
    await this.storage.put({ ['state:' + await hash(state)]: { origin, studentId, expiresAt: Date.now() + 600000 } });
    const url = new URL('https://zoom.us/oauth/authorize');
    url.search = new URLSearchParams({ response_type: 'code', client_id: this.env.ZOOM_CLIENT_ID,
      redirect_uri: origin + '/api/automation/callback', state }).toString();
    return json({ url: url.href });
  }
  async callback(url) {
    const state = url.searchParams.get('state'), code = url.searchParams.get('code');
    if (!state || state.length > 100 || !code || code.length > 2000) return json({ error: 'Start the Zoom connection again from Quiz results.' }, 400);
    const key = 'state:' + await hash(state);
    const pending = await this.storage.transaction(async txn => {
      const item = await txn.get(key);
      if (!item || item.expiresAt < Date.now() || item.origin !== url.origin) return null;
      await txn.delete(key); return item;
    });
    if (!pending) return json({ error: 'This Zoom connection link has expired or was already used.' }, 400);
    let stage = 'token_exchange';
    try {
      const tokens = await this.tokenRequest({ grant_type: 'authorization_code', code, redirect_uri: pending.origin + '/api/automation/callback' });
      stage = 'user_profile';
      const owner = await this.zoom('/users/me', tokens.access), prior = await this.storage.get('oauth');
      stage = 'owner_check';
      if (!owner.id || !owner.account_id || prior && prior.userId !== owner.id) throw new Error('zoom_reconnect');
      await this.storage.put({ oauth: { ...tokens, userId: owner.id, accountId: owner.account_id, pmi: owner.pmi }, 'connection-error': null, 'connection-detail': null });
      return new Response(null, { status: 303, headers: { Location: pending.origin + '/#quiz-results' } });
    } catch (error) {
      await this.storage.put({ 'connection-error': safeError(error), 'connection-detail': { stage, httpStatus: error.httpStatus || null, apiCode: error.apiCode || null, errorType: ['TypeError','SyntaxError','ReferenceError','Error'].includes(error.name) ? error.name : 'Other', hints: ['AbortSignal', 'timeout', 'redirect', 'fetch', 'JSON', 'Invalid character', 'not defined', 'not a function', 'network', 'canceled', 'refused'].filter(word => String(error.message).includes(word)) } });
      return json({ error: 'Zoom could not be connected. Check the app permissions and try again from Quiz results.' }, 400);
    }
  }
  async webhook(request) {
    let body;
    try { body = await boundedText(request, 32768); } catch { return json({ error: 'Invalid event.' }, 413); }
    if (!await zoomSignatureValid(this.env.ZOOM_WEBHOOK_SECRET, request, body)) return json({ error: 'Invalid signature.' }, 401);
    let event; try { event = JSON.parse(body); } catch { return json({ error: 'Invalid event.' }, 400); }
    if (event.event === 'endpoint.url_validation') {
      const plainToken = event.payload?.plainToken;
      if (typeof plainToken !== 'string' || plainToken.length > 1024) return json({ error: 'Invalid challenge.' }, 400);
      return json({ plainToken, encryptedToken: await signedChallenge(this.env.ZOOM_WEBHOOK_SECRET, plainToken) });
    }
    if (!['my_notes.transcript_generated', 'my_notes.note_completed'].includes(event.event)) return new Response(null, { status: 204 });
    const owner = await this.storage.get('oauth'), payload = event.payload, object = payload?.object;
    if (!owner || payload.account_id !== owner.accountId || payload.operator_id !== owner.userId) return json({ error: 'Wrong note owner.' }, 403);
    if (!noteIdValid(object?.note_id) || typeof object.meeting_id !== 'string' || !object.meeting_id || object.meeting_id.length > 128) return json({ error: 'A Zoom meeting reference is required.' }, 400);
    const key = 'job:' + await hash(object.note_id);
    await this.storage.transaction(async txn => {
      const existing = await txn.get(key);
      if (existing) {
        existing.meetingId = object.meeting_id;
        existing.sourceEventAt = Math.max(existing.sourceEventAt || 0, Number(request.headers.get('x-zm-request-timestamp')) * 1000);
        if (event.event === 'my_notes.transcript_generated' && existing.status === 'needs_attention' &&
            ['transcript_unusable', 'meeting_pending', 'meeting_reference_missing', 'zoom_unavailable'].includes(existing.lastError)) {
          existing.status = 'pending'; existing.tries = 0; existing.nextAt = 0;
        }
        await txn.put({ [key]: existing });
        return;
      }
      await txn.put({ [key]: { noteId: object.note_id, meetingId: object.meeting_id, receivedAt: Date.now(),
        sourceEventAt: Number(request.headers.get('x-zm-request-timestamp')) * 1000,
        nextAt: Date.now() + 60000, status: 'pending', tries: 0 } });
    });
    return json({ accepted: true });
  }
  async discover() {
    const owner = await this.storage.get('oauth');
    const cutoff = new Date(Math.min(...Object.values(await this.students()).map(s => Date.parse(s.startAfter)))).toISOString();
    const since = await this.storage.get('discovery-since') || cutoff;
    const until = new Date().toISOString();
    // Search notes by modification time: this catches transcripts that arrive late.
    let cursor; const seen = new Set();
    do {
      const result = await this.zoom('/docs/file_search', undefined, { file_types: ['note'], owner_id: owner.userId,
        modified_time_from: since, modified_time_to: until, page_size: 50, ...(cursor ? { next_page_token: cursor } : {}) });
      if (!Array.isArray(result.files)) throw new Error('discovery_incomplete');
      for (const file of result.files) {
        if (!noteIdValid(file.file_id)) throw new Error('discovery_incomplete');
        const key = 'job:' + await hash(file.file_id);
        const prior = await this.storage.get(key);
        if (!prior) await this.storage.put({ [key]: { noteId: file.file_id, receivedAt: Date.now(), nextAt: 0, status: 'pending', tries: 0 } });
        else if (prior.status === 'needs_attention' && ['transcript_unusable', 'meeting_pending', 'meeting_reference_missing'].includes(prior.lastError)) {
          await this.storage.put({ [key]: { ...prior, status: 'pending', tries: 0, nextAt: 0 } });
        }
      }
      cursor = result.next_page_token;
      if (cursor && seen.has(cursor)) throw new Error('discovery_incomplete');
      seen.add(cursor);
    } while (cursor);

    // Search does not include meeting dates. Resolve them from completed instances
    // of the host's personal room and scheduled meetings, never a guessed note title.
    const rooms = new Set(owner.pmi ? [String(owner.pmi)] : []);
    let page; const pages = new Set();
    do {
      const result = await this.zoom('/users/me/meetings?' + new URLSearchParams({ type: 'previous_meetings', page_size: '100', ...(page ? { next_page_token: page } : {}) }));
      if (!Array.isArray(result.meetings)) throw new Error('discovery_incomplete');
      result.meetings.forEach(m => rooms.add(String(m.pmi || m.id)));
      page = result.next_page_token;
      if (page && pages.has(page)) throw new Error('discovery_incomplete');
      pages.add(page);
    } while (page);
    for (const room of rooms) {
      if (!/^\d{9,11}$/.test(room)) throw new Error('discovery_incomplete');
      const result = await this.zoom('/past_meetings/' + room + '/instances');
      if (!Array.isArray(result.meetings)) throw new Error('discovery_incomplete');
      for (const instance of result.meetings) {
        if (!instance.uuid || !Number.isFinite(Date.parse(instance.start_time)) || Date.parse(instance.start_time) < Date.parse(cutoff)) continue;
        const notes = await this.zoom('/my_notes/notes?' + new URLSearchParams({ meeting_id: instance.uuid }));
        if (!Array.isArray(notes.notes)) throw new Error('discovery_incomplete');
        for (const note of notes.notes) {
          if (!noteIdValid(note.note_id)) throw new Error('discovery_incomplete');
          const key = 'job:' + await hash(note.note_id), prior = await this.storage.get(key);
          const modifiedAt = Number.isFinite(Date.parse(note.modified_time)) && (!prior?.modifiedAt || Date.parse(note.modified_time) > Date.parse(prior.modifiedAt)) ? note.modified_time : prior?.modifiedAt;
          await this.storage.put({ [key]: { receivedAt: Date.now(), nextAt: 0, status: 'pending', tries: 0, ...prior,
            noteId: note.note_id, meetingId: instance.uuid, startedAt: instance.start_time, modifiedAt } });
        }
      }
    }
    // Advance only after ALL pages succeed. A two-day overlap handles indexing lag.
    await this.storage.put({ 'discovery-since': new Date(Math.max(Date.parse(cutoff), Date.parse(until) - 172800000)).toISOString() });
  }
  async portal(studentId, path, body) {
    const object = this.env.FEEDBACK_STORE.get(this.env.FEEDBACK_STORE.idFromName(studentId));
    const response = await object.fetch(new Request('https://feedback.internal' + path, body ? { method: 'POST', body: JSON.stringify(body) } : {}));
    if (!response.ok) throw new Error('publish_failed');
    return response.json();
  }
  async reserveGeneration(studentId) {
    await this.storage.transaction(async txn => {
      const day = new Date().toISOString().slice(0, 10), month = day.slice(0, 7);
      const key = 'usage:' + studentId;
      const usage = await txn.get(key) || {};
      const daily = usage.day === day ? usage.daily : 0, monthly = usage.month === month ? usage.monthly : 0;
      if (monthly >= 12) throw new Error('monthly_limit');
      if (daily >= 2) throw new Error('daily_limit');
      // Reserve before AI calls; a crash cannot bypass the limit.
      await txn.put({ [key]: { day, month, daily: daily + 1, monthly: monthly + 1 } });
    });
  }
  async process(key, job) {
    const students = await this.students();
    if (job.studentId && !students[job.studentId]) throw new Error('other_student');
    const instructorNames = JSON.parse(this.env.ZOOM_INSTRUCTOR_NAMES || '["Phil","Phil Stilwell"]');
    if (!Array.isArray(instructorNames) || instructorNames.length > 20 || instructorNames.some(n => typeof n !== 'string' || !n.trim() || n.length > 200)) throw new Error('Invalid instructor names');
    const mappingHash = await hash(JSON.stringify({ students, instructorNames }));
    let context = job.studentId ? await this.portal(job.studentId, '/automation/context') : null;
    const alreadyPublished = () => {
      const known = context?.sourceNotes?.find(source => source.noteId === job.noteId);
      const id = known?.id || job.sessionId;
      if (id && (context?.publishedSessions.includes(id) || context?.assessment?.quiz?.generatedForSession === id)) {
        job.status = 'published'; job.sessionId = id; return true;
      }
      return false;
    };
    // Completed jobs and retries whose publication already committed need no
    // transcript or meeting download, including after a coordinator restart.
    if (alreadyPublished()) return;
    const cached = job.studentId ? (await this.portal(job.studentId, '/automation/transcript/' + job.noteId)).transcript : null;
    let note, transcript, meeting, sourceHash;
    const reusable = reusableTranscript(cached, job, mappingHash);
    if (reusable) {
      transcript = { studentId: job.studentId, student: students[job.studentId], learnerLabel: 'Student', segments: cached.segments };
      meeting = cached.meeting; sourceHash = cached.sourceHash;
    } else {
      note = await this.zoom('/my_notes/notes/' + encodeURIComponent(job.noteId) + '/content?include=transcript');
      transcript = readTranscript(note, students);
      if (job.studentId && job.studentId !== transcript.studentId) throw new Error('ambiguous_student');
      job.studentId = transcript.studentId;
      context ||= await this.portal(job.studentId, '/automation/context');
      if (alreadyPublished()) return;
      const known = context.sourceNotes?.find(source => source.noteId === job.noteId);
      if (known && Date.parse(known.startedAt) < Date.parse(transcript.student.startAfter)) { job.status = 'skipped'; return; }
      if (!job.meetingId) throw new Error('meeting_reference_missing');
      const uuid = job.meetingId.startsWith('/') || job.meetingId.includes('//') ? encodeURIComponent(encodeURIComponent(job.meetingId)) : encodeURIComponent(job.meetingId);
      meeting = await this.zoom('/past_meetings/' + uuid);
      sourceHash = await hash(JSON.stringify(note.transcript));
    }
    if (!meeting.start_time || !meeting.end_time || Date.parse(meeting.end_time) > Date.now() - 900000 ||
        !Number.isFinite(Date.parse(meeting.start_time)) || !Number.isFinite(Date.parse(meeting.end_time))) throw new Error('meeting_pending');
    if (job.modifiedAt && Date.parse(job.modifiedAt) > Date.now() - 900000) throw new Error('meeting_pending');
    if (job.sourceEventAt && job.sourceEventAt > Date.now() - 900000) throw new Error('meeting_pending');
    if (Date.parse(meeting.start_time) < Date.parse(transcript.student.startAfter)) {
      job.status = 'skipped'; return;
    }
    const id = sessionId(meeting.start_time, transcript.student.timeZone);
    if (context.publishedSessions.includes(id) || context.assessment?.quiz?.generatedForSession === id) {
      job.status = 'published'; job.sessionId = id; return;
    }
    await this.reserveGeneration(job.studentId);
    if (!reusable) {
      const sameContent = cached?.privacyVersion === TRANSCRIPT_PRIVACY_VERSION && cached.mappingHash === mappingHash && cached.sourceHash === sourceHash;
      const segments = sameContent ? cached.segments : await anonymizeTranscript(this.env.AI, note, transcript, instructorNames);
      if (JSON.stringify(await this.students()) !== JSON.stringify(students)) throw new Error('student_changed');
      await this.checkSource(key, job);
      await this.portal(job.studentId, '/automation/transcript/' + job.noteId, {
        privacyVersion: TRANSCRIPT_PRIVACY_VERSION, privacyReviewed: true, noteId: job.noteId, meetingId: job.meetingId,
        mappingHash, sourceHash, savedAt: new Date().toISOString(), modifiedAt: job.modifiedAt || null,
        sourceEventAt: job.sourceEventAt || null, meeting, segments,
      });
      // Retain only the pointer in the coordinator, even if authoring later fails.
      await this.saveJob(key, job);
      transcript = { ...transcript, learnerLabel: 'Student', segments };
      note = null;
    }
    const output = await authorQuiz(this.env.AI, transcript, meeting, job.noteId, context);
    // Recheck the mapping after generation: a pause or name edit must take effect
    // before any content reaches the student's account.
    const currentStudent = (await this.students())[job.studentId];
    if (JSON.stringify(currentStudent) !== JSON.stringify(transcript.student)) throw new Error('student_changed');
    await this.checkSource(key, job);
    const saved = await this.portal(job.studentId, '/automation/publish', { ...output, fingerprint: sourceHash });
    if (!saved.ok) throw new Error('publish_failed');
    job.status = 'published'; job.sessionId = id; job.publishedAt = new Date().toISOString(); job.lastError = null;
  }
  sourceChanged(current, job) {
    return current && ((current.sourceEventAt || 0) > (job.sourceEventAt || 0) ||
      Date.parse(current.modifiedAt) > (Date.parse(job.modifiedAt) || 0) || current.meetingId && current.meetingId !== job.meetingId);
  }
  async checkSource(key, job) {
    if (this.sourceChanged(await this.storage.get(key), job)) throw new Error('source_changed');
  }
  async saveJob(key, job) {
    await this.storage.transaction(async txn => {
      const current = await txn.get(key);
      const next = this.sourceChanged(current, job) ? { ...job, modifiedAt: current.modifiedAt || job.modifiedAt,
        sourceEventAt: current.sourceEventAt || job.sourceEventAt, meetingId: current.meetingId || job.meetingId,
        ...(job.status === 'published' ? {} : { status: 'pending', nextAt: 0, tries: 0 }) } : job;
      await txn.put({ [key]: next });
    });
  }
  async pruneTranscripts() {
    let studentIds;
    if (this.env.STUDENT_DIRECTORY) {
      const response = await directoryRequest(this.env, '/retention-accounts');
      if (!response.ok) throw new Error('transcript_retention_failed');
      studentIds = (await response.json()).studentIds;
    } else studentIds = [...new Set([...Object.keys(JSON.parse(this.env.STUDENT_ACCOUNTS || '{}')), ...Object.keys(studentsFor(this.env))])];
    if (!this.env.FEEDBACK_STORE) return;
    const failed = [];
    for (const id of studentIds) {
      try {
        const response = await this.env.FEEDBACK_STORE.get(this.env.FEEDBACK_STORE.idFromName(id)).fetch(new Request('https://feedback.internal/automation/prune-transcripts', { method: 'POST' }));
        if (!response.ok && response.status !== 410) throw new Error('cleanup_failed');
      } catch { failed.push(id); }
    }
    if (failed.length) throw new Error('transcript_retention_failed');
    await this.storage.put({ 'last-retention': new Date().toISOString() });
  }
  async run(scheduledTime) {
    const lease = crypto.randomUUID(), deadline = Date.now() + 480000;
    const acquired = await this.storage.transaction(async txn => {
      const lock = await txn.get('run-lock');
      if (lock?.until > Date.now()) return false;
      if (scheduledTime !== undefined) {
        const day = nightlyDate(scheduledTime);
        if (!day || await txn.get('nightly-date') === day) return false;
        await txn.put({ 'nightly-date': day });
      }
      await txn.put({ 'run-lock': { lease, until: Date.now() + 900000 } }); return true;
    });
    if (!acquired) return;
    try {
      // Privacy retention runs even when publishing is disabled, all accounts
      // are paused, or Zoom is disconnected. It never needs an AI call.
      try { await this.pruneTranscripts(); await this.storage.put({ 'retention-error': null }); }
      catch { await this.storage.put({ 'retention-error': 'transcript_retention_failed' }); }
      if (this.env.AUTOMATION_ENABLED !== 'true' || !await this.isConfigured()) return;
      await this.accessToken(); // Keep the rotating refresh token alive even between lessons.
      await this.refreshDirectory();
      await this.discover();
      const jobs = [...await this.storage.list({ prefix: 'job:' })];
      const pending = jobs.filter(([, j]) => j.status === 'pending' && j.nextAt <= Date.now()).sort((a, b) => (a[1].startedAt || '').localeCompare(b[1].startedAt || '') || a[1].receivedAt - b[1].receivedAt);
      for (const [key, job] of pending) {
        if (Date.now() > deadline) break;
        try { await this.process(key, job); }
        catch (error) {
          if (error.message === 'other_student') { job.status = 'needs_attention'; job.lastError = 'student_not_matched'; }
          else {
            job.lastError = safeError(error); job.tries++;
            job.status = job.tries >= 6 || ['transcript_too_large', 'ambiguous_student', 'meeting_reference_missing', 'transcript_privacy_failed'].includes(job.lastError) ? 'needs_attention' : 'pending';
            job.nextAt = Date.now() + 3600000;
            if (['daily_limit', 'monthly_limit'].includes(job.lastError)) { job.status = 'pending'; job.tries--; }
          }
        }
        await this.saveJob(key, job);
      }
      await this.storage.put({ 'last-check': new Date().toISOString(), 'connection-error': null });
    } catch (error) { await this.storage.put({ 'connection-error': safeError(error) }); }
    finally {
      await this.storage.transaction(async txn => {
        if ((await txn.get('run-lock'))?.lease === lease) await txn.delete('run-lock');
      });
    }
  }
  async fetch(request) {
    const url = new URL(request.url), path = url.pathname;
    if (path === '/webhook' && request.method === 'POST') return this.webhook(request);
    if (path === '/callback' && request.method === 'GET') return this.callback(new URL(request.headers.get('X-Callback-URL')));
    if (path === '/run' && request.method === 'POST') { const input = await request.json(); await this.run(input.scheduledTime); return json({ ok: true }); }
    const studentId = request.headers.get('X-Student-ID'), origin = request.headers.get('X-Student-Origin');
    if (path === '/admin-status' && request.method === 'GET') {
      const jobs = [...await this.storage.list({ prefix: 'job:' })].map(([, j]) => j);
      return json({ enabled: this.env.AUTOMATION_ENABLED === 'true', connected: Boolean(await this.storage.get('oauth')),
        lastRetention: await this.storage.get('last-retention') || null, retentionError: await this.storage.get('retention-error') || null,
        lastCheck: await this.storage.get('last-check') || null, connectionError: await this.storage.get('connection-error') || null,
        pending: jobs.filter(j => j.status === 'pending').length,
        needsAttention: jobs.filter(j => j.status === 'needs_attention').length,
        students: Object.fromEntries(Object.keys(await this.students()).map(id => [id, {
          latestPublication: jobs.filter(j => j.studentId === id && j.publishedAt).map(j => j.publishedAt).sort().at(-1) || null,
          pending: jobs.filter(j => j.studentId === id && j.status === 'pending').length,
          needsAttention: jobs.filter(j => j.studentId === id && j.status === 'needs_attention').length,
        }])) });
    }
    if (!(await this.students())[studentId]) return json({ configured: false, connected: false, enabled: false });
    if (path === '/connect' && request.method === 'POST') return this.connect(origin, studentId);
    if (path === '/verify' && request.method === 'POST') {
      try {
        await this.accessToken(); await this.discover();
        const probes = [...await this.storage.list({ prefix: 'job:' })].slice(0, 5);
        for (const [, job] of probes) await this.zoom('/my_notes/notes/' + encodeURIComponent(job.noteId) + '/content?include=transcript');
        await this.storage.put({ 'last-check': new Date().toISOString(), 'connection-error': null });
        return json({ ok: true });
      } catch (error) { return json({ error: safeError(error), httpStatus: error.httpStatus || null, apiCode: error.apiCode || null }, 502); }
    }
    if (path === '/status' && request.method === 'GET') {
      const jobs = [...await this.storage.list({ prefix: 'job:' })].map(([, j]) => j).filter(j => !j.studentId || j.studentId === studentId);
      return json({ configured: await this.isConfigured(), connected: Boolean(await this.storage.get('oauth')),
        enabled: this.env.AUTOMATION_ENABLED === 'true', lastCheck: await this.storage.get('last-check') || null,
        connectionError: await this.storage.get('connection-error') || null,
        connectionDetail: await this.storage.get('connection-detail') || null,
        costLimitReached: jobs.some(j => ['daily_limit', 'monthly_limit'].includes(j.lastError)),
        pending: jobs.filter(j => j.status === 'pending').length,
        needsAttention: jobs.filter(j => j.status === 'needs_attention').length,
        latestPublication: jobs.filter(j => j.publishedAt).map(j => j.publishedAt).sort().at(-1) || null });
    }
    return json({ error: 'Not found.' }, 404);
  }
}
