# Nightly server updates

The authorized schedule is **1 a.m. America/New_York every night**, adjusting for daylight saving time. Cloudflare runs the job; the teacher's computer and Codex may be off. The former hourly Codex heartbeat must be paused when this server workflow is enabled. Do not run both publishers.

## Schedule and connection

`worker.mjs` receives UTC cron triggers at 05:00 and 06:00, checks the Eastern local hour, and dispatches only at 01:00. `QuizAutomation` stores the local date before work so the repeated autumn hour cannot publish twice. There is no browser timer or local scheduler. Connection status and last successful check appear in the teacher's Quiz results page.

The private Zoom General App uses user OAuth (authorization and rotating refresh tokens). Register the exact `/api/automation/callback` URL on the student host and enable strict redirects. Only an authenticated teacher can begin connection. The single-use state is bound to the initiating host and expires after ten minutes. Tokens stay in the private coordinator database; app credentials stay in Worker secrets. Authorizing a different Zoom owner cannot silently replace an existing owner.

Required scopes:
- `user:read:user`
- `canvas:write:file_search` (Zoom names it “write,” but this operation only searches notes)
- `meeting:read:list_meetings`, `meeting:read:list_past_instances`, `meeting:read:past_meeting`
- `my_notes:read:note`, `my_notes:read:content`

Optional signed My Notes notifications (`my_notes:read:notes_transcript`) may supply note/meeting references for instant meetings outside the personal room. These only queue work; they never generate pages outside the nightly run. Configure `/api/automation/webhook` with `ZOOM_WEBHOOK_SECRET` if enabled.

Worker secrets: `ZOOM_CLIENT_ID`, `ZOOM_CLIENT_SECRET`, `QUIZ_STUDENTS`, and optionally `ZOOM_WEBHOOK_SECRET`. Keep all existing login secrets. `QUIZ_STUDENTS` is an object keyed by an already registered student account, with `firstName`, exact `zoomNames`, `timeZone`, and `startAfter`. Never commit actual student mappings or credential inputs. `AUTOMATION_ENABLED` is an explicit server switch.

## Discover and match

Search all pages of the owner's My Notes by modification time. Advance the checkpoint only after successful discovery, overlapping two days to catch indexing lag. Persist discovered note IDs before processing. Resolve dates through ended instances of the personal meeting room and scheduled meetings; recheck eligible instances for delayed notes. Signed notifications can provide additional meeting references.

Require the full My Notes transcript with every returned segment, a confirmed completed meeting, and a match to exactly one configured student's Zoom speaker name. Never identify a student from the room title alone. Never guess a meeting date from a note name. A matched note whose meeting reference cannot be resolved is flagged for the teacher instead of published. Unknown students are flagged for the teacher; adding a student still requires provisioning their private account and initial reviewed assessment. Historical baseline sessions before `startAfter` are not backfilled.

Missing/empty/growing transcripts, very recent meetings, uncertain identity, oversized transcripts, or unclear language evidence do not produce invented records. Retry transient failures on later nights; flag persistent problems in the teacher view. Full transcript responses exceeding the safe model input size are rejected, never silently truncated. Zoom summaries are never substitutes.

## Create the student pages

Read the student's current assessment and **all** saved quiz attempts, including unfinished ones. Use the original first choice in `answers[i][0]`; unanswered questions are not errors and later retries never erase a first mistake. Rank review by repeated quizzes, recency, and frequency. If no misses exist, use relevant assessment patterns without claiming quiz errors.

The server model reads the entire new transcript, earlier reviewed assessment, and actual first-try mistakes. Create a short ESL session summary and feedback, update the assessment with new timestamped evidence, and author 4–6 new practice questions mixing this lesson and useful review. Apply AGENTS.md: A1–A2 reading register, respectful adult tone, first name only, quoted target English, simple feedback for each answer, ESL only, no unrelated personal details or external note links. Do not call text-based practice scores proficiency levels or infer pronunciation quality.

Validate structure, exact new timestamp references, earlier assessment references, source ownership, answer indexes, and question evidence. A second model pass checks the full transcript against all proposed content before publication. This reduces errors but is not a guarantee of perfect pedagogy. Reject failed checks and retain existing content.

## Save safely

Publish feedback, session-list summary, current assessment, and quiz in one private database transaction. Check that the current assessment still matches the version used for authoring; if a teacher edited it meanwhile, retry from the latest version. Save the prior assessment and the authored quiz/evidence privately. Never alter student attempts. Duplicate note events and retries cannot create another update for an already published session. Delayed older sessions are archived without replacing a newer current quiz.

The latest quiz shows its source lesson links. Unfinished attempts keep their original questions. Completed attempts retain original first answers and dated progress. Accounts without any reviewed quiz omit the Quiz menu. Failed generation never removes a useful existing quiz.

## Cost and operation

The model is Cloudflare Workers AI `@cf/openai/gpt-oss-120b`, using two calls per eligible update. The initial estimate for Koji is under $1/month in AI usage before free allowances. No paid plan is enabled automatically. Initial safeguards reserve at most two generations per UTC day and twelve per month for each configured student; failed attempts count toward the cap. Reaching the cap keeps jobs pending and shows a teacher message. Adjust limits and estimate costs before expanding the student roster.

Tests use fictional records and mocked model/Zoom calls. Run `npm run test:students`, then `npm run deploy:students`. Verify live teacher-only connection status and student isolation. Once OAuth is connected, verify a real read-only discovery pass before enabling publishing. Do not run paid inference just to test setup or regenerate the baseline five quizzes. Keep checkpoints, secrets, and student records private. Remove temporary credential files and preview state, and close temporary browser tabs/dialogs.

## Sources

- [Zoom My Notes API](https://developers.zoom.us/docs/api/my-notes/)
- [Zoom Canvas search](https://developers.zoom.us/docs/api/canvas/)
- [Zoom meeting API](https://developers.zoom.us/docs/api/meetings/)
- [Cloudflare cron triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/)
- [Cloudflare model pricing](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/)


### Administrator-managed students

The private StudentDirectory now supplies the active roster at runtime. Manage it at phil.englishladder.com with the existing teacher credential. STUDENT_ACCOUNTS and QUIZ_STUDENTS seed the initial directory only; new accounts and Zoom-name edits require no deployment. Draft or paused students are excluded. Activation sets the transcript cutoff; exact names are unique across the directory. Old unmatched jobs are reconsidered after a mapping change, and mappings are rechecked immediately before publication. Empty new accounts can receive a first assessment from their first usable full transcript, with single-lesson practice targets clearly distinguished from recurring patterns. Keep full names, emails, staff details, course hours, and private notes out of AI authoring inputs and every student response.
