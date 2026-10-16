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

## Private transcript cache and retention

Cache eligible new transcripts in the existing private per-student server store, after anonymization and independent privacy review. Match the student from configured Zoom names before removing identities. Trusted instructor names default to `Phil` and `Phil Stilwell`; the optional private `ZOOM_INSTRUCTOR_NAMES` JSON array can override these. Preserve `Student`, `Instructor`, and separate `Speaker N` roles, every turn, and elapsed timestamps. Unknown speakers must not be guessed to be the instructor. Conflicting speaker identities prevent processing.

Known speaker names and direct contact patterns are removed before the first privacy model call. That call selects exact spans containing remaining proper names, identifying details, or sensitive personal information. Code replaces those spans with neutral placeholders without rewriting or correcting other language. A second model pass reviews the entire result. Only reviewed text may be saved or used for language assessment. Raw Zoom responses and name mappings are transient in server memory; they are not saved, logged, exposed in browser APIs, or committed. The privacy service uses the existing Cloudflare AI model; this is automated redaction, not a guarantee that all contextual identifying details are detected. A failed privacy review is flagged for attention and no transcript is cached or used for publishing.

The cache contains anonymous segments, meeting times, internal source references, revision metadata, and hashes. Size-bounded chunks and a content hash preserve the complete text and detect incomplete reads. Public Worker routes never expose cache reads or writes, even to a logged-in teacher. Ordinary assessment/context exports omit the full cache. A deleted account's permanent write barrier covers cache writes too.

Completed lessons remain skipped. Pending retries reuse a matching reviewed copy, avoiding both the transcript download and the two privacy calls. New source notifications, newer modification times, speaker-mapping changes, or a privacy-version change invalidate reuse. Without a source revision, pending copies are refreshed after seven days. Discovery still checks Zoom metadata for new or changed notes. Matching source hashes can reuse the reviewed text after a refresh. No historical cache backfill is triggered by deployment.

Nightly cleanup removes every cached version whose Eastern lesson date is earlier than the date three calendar months ago; a month-end boundary is clamped to the last day of the target month. The cutoff day is retained until the following night. Expired copies are also refused on read/save. Cleanup covers paused accounts and runs even when publishing is disabled, no students are active, or Zoom is disconnected. It makes no AI call. Failures appear in the administrator's nightly status and retry on the next night. This deletes the portal's cached transcripts only; feedback, assessment/CEFR history, quizzes, first choices, and original Zoom records remain.

## Create the student pages

Read the student's current assessment and **all** saved quiz attempts, including unfinished ones. Use the original first choice in `answers[i][0]`; unanswered questions are not errors and later retries never erase a first mistake. Rank review by repeated quizzes, recency, and frequency. If no misses exist, use relevant assessment patterns without claiming quiz errors.

The server model reads the entire new transcript, earlier reviewed assessment, and actual first-try mistakes. Create a short ESL session summary and feedback, update the assessment with new timestamped evidence, and author exactly seven new practice questions mixing this lesson and useful review. Apply AGENTS.md: A1–A2 reading register, respectful adult tone, first name only, quoted target English, simple feedback for each answer, ESL only, no unrelated personal details or external note links. Write assessment plans as independent-study suggestions, with a specific copyable AI prompt for each topic. Introduce the topic, give simple examples, and offer guided practice one question at a time. Never promise future lesson content or assign tasks to Phil. Student pages show dates without elapsed transcript times; keep timestamped evidence privately for review. Do not call text-based practice scores proficiency levels or infer pronunciation quality.

Validate structure, exact new timestamp references, earlier assessment references, source ownership, answer indexes, and question evidence. A second model pass checks the full transcript against all proposed content before publication. This reduces errors but is not a guarantee of perfect pedagogy. Reject failed checks and retain existing content.

## Save safely

Feedback practice must use fresh situations to apply the lesson's language. Neither tasks nor example answers may copy the focus models or vocabulary examples, turn them into gaps, or make only a trivial word swap. Both the author and independent editor check this. Publishing also rejects normalized duplicate examples, including complete sentences embedded in a longer answer. This check does not replace the editor's review of meaning and usefulness.

Publish feedback, session-list summary, current assessment, and quiz in one private database transaction. Check that the current assessment still matches the version used for authoring; if a teacher edited it meanwhile, retry from the latest version. Save the prior assessment and the authored quiz/evidence privately. Never alter student attempts. Duplicate note events and retries cannot create another update for an already published session. Delayed older sessions are archived without replacing a newer current quiz.

The latest quiz introduction shows only plain source lesson dates, without links. Short instructions appear beside the questions. Unfinished attempts keep their original questions. Completed attempts retain original first answers and dated progress. Accounts without any reviewed quiz omit the Quiz menu. Failed generation never removes a useful existing quiz.

## Cost and operation

The model is Cloudflare Workers AI `@cf/openai/gpt-oss-120b`, using two author/editor calls per eligible update, plus two privacy calls when a new sanitized transcript is needed. The initial estimate for Koji was under $1/month in AI usage before free allowances; privacy processing adds an estimated $0.01–$0.05 per newly cached transcript, depending on length and redactions. Private storage is expected to fit the existing allowance (5 GB included, then $0.20/GB-month at the October 15, 2026 published SQLite-backed Durable Object rates). No new service or paid plan is enabled. Reserve at most two generation attempts per UTC day and twelve per month for each configured student before any privacy or authoring call; failed attempts count toward the cap. These are attempt limits, not a dollar-enforced ceiling. Reaching the cap keeps jobs pending and shows a teacher message. Adjust limits and estimate costs before expanding the student roster.

Tests use fictional records and mocked model/Zoom calls. Run `npm run test:students`, then `npm run deploy:students`. Verify live teacher-only connection status and student isolation. Once OAuth is connected, verify a real read-only discovery pass before enabling publishing. Do not run paid inference just to test setup or regenerate the baseline five quizzes. Keep checkpoints, secrets, and student records private. Remove temporary credential files and preview state, and close temporary browser tabs/dialogs.

## Sources

- [Zoom My Notes API](https://developers.zoom.us/docs/api/my-notes/)
- [Zoom Canvas search](https://developers.zoom.us/docs/api/canvas/)
- [Zoom meeting API](https://developers.zoom.us/docs/api/meetings/)
- [Cloudflare cron triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/)
- [Cloudflare model pricing](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/)
- [Cloudflare private storage pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/)


### Administrator-managed students

The private StudentDirectory now supplies the active roster at runtime. Manage it at phil.englishladder.com with the existing teacher credential. STUDENT_ACCOUNTS and QUIZ_STUDENTS seed the initial directory only; new accounts and Zoom-name edits require no deployment. Draft or paused students are excluded. Activation sets the transcript cutoff; exact names are unique across the directory. Old unmatched jobs are reconsidered after a mapping change, and mappings are rechecked immediately before publication. Empty new accounts can receive a first assessment from their first usable full transcript, with single-lesson practice targets clearly distinguished from recurring patterns. Keep full names, emails, staff details, course hours, and private notes out of AI authoring inputs and every student response.


### Provisional CEFR conversation estimates

CEFR is a separate monthly task after lesson processing. The first estimate requires two distinct usable saved anonymous transcripts and reviews the latest two. Later reviews wait one calendar month from the previous review (Eastern date with month-end clamping), read the latest four retained sessions, and require at least two. Use two or three when fewer than four remain; never restore an expired transcript or substitute old assessment prose. Unchanged evidence does not cause another paid review. Paused accounts do not receive updates.

The monthly task can run from private cache when Zoom is disconnected or no new lesson arrived. It uses two model calls to author and independently review the estimate against every full selected transcript. At least one exact Student quotation from each selected session is required. Teacher models, older CEFR quotes, quiz scores, and old summaries cannot establish a level. The private publisher rechecks the selected window, minimum sessions, monthly eligibility and quote grounding before saving; concurrent source changes or account deletion prevent a stale write. A failed or insufficient monthly review keeps the previous estimate. The administrator sees review timing and failure/insufficient status; student APIs never include CEFR. See README.md and `cefr.mjs` for evidence and scope rules.

The monthly author output ceiling is 5,000 tokens and the editor ceiling is 4,000. Complete input windows over 300,000 UTF-8 bytes are deferred before model use rather than shortened; a provider context-limit failure also preserves the old estimate. Ordinary lesson authoring no longer requests CEFR. The separate monthly allowance is one attempt per UTC day and two per calendar month, including failures, reserved before calls. Existing ordinary-lesson limits remain two per day and twelve per month. Estimated CEFR cost is $0.02–$0.10 per review before free allowances using the published $0.35/million input and $0.75/million output token rates; actual cost varies, and retry/attempt caps are not a dollar-enforced ceiling. No paid inference or historical backfill runs for deployment validation.


### Model replies and recovery (October 16, 2026)

The GPT-OSS binding uses the Responses API: send `input`, `text.format`, and `max_output_tokens`, and read the completed assistant `output_text` message. Ignore reasoning content and reject refusals, incomplete output, malformed JSON, and provider errors. Privacy and content reviews remain independent required approvals. Review calls allow 4,000 output tokens, including reasoning; malformed model replies are reported separately from rejected privacy reviews.

The authenticated administrator student list shows safe failure reasons without source IDs, transcript content, or provider response bodies. Its exact-origin POST retry endpoint accepts one hashed job ID, takes the same global processing lease as the cron job, and rechecks the active account. Retrying retains all validation, deletion barriers, duplicate protection, and existing two-per-day/twelve-per-month reservations. Failed attempts count. Published jobs do not call AI again. A typical four-call recovery is estimated at $0.05–$0.20 before free allowances; actual cost varies with transcript length. Manual retries do not start unrelated jobs or monthly CEFR reviews. The ordinary unattended schedule remains 1 a.m. New York time.

Privacy processing permits at most one repair per reserved lesson attempt: either regenerate an invalid exact-span plan, or apply omissions identified by the independent reviewer and obtain a fresh independent approval. It uses at most three privacy calls, reading all segments each time, with no persistent raw transcript or rejected model content. Invalid removal spans and a rejected final privacy review have separate safe error codes. The initial privacy review allows 8,000 output tokens to identify missing removals; the final approval-only review allows 4,000. Failed checks still prevent caching and publication.

A one-off recovery beyond the ordinary daily cap requires explicit owner approval and an estimate first. Only then may an operator temporarily set `LESSON_RECOVERY_GRANT` to `{jobId,day,attempt}` for one hashed job and the current UTC date. The reservation atomically consumes the grant once, still increments both usage counters, permits only the explicitly approved next numbered attempt (3–5, default 3), and never bypasses the monthly cap or reviews. Remove the temporary setting after that attempt. No grant is configured by default or exposed through student or administrator browser APIs.

The administrator may ignore an unmatched session through an exact-origin, authenticated action. It marks only that job as ignored, preserves its Zoom source and local matching metadata, skips future processing of the same note, and excludes it from attention counts. Duplicate discovery/events preserve this disposition. It cannot ignore matched student jobs or mutate the queue during a running update. This makes no AI calls and does not ignore a person's future distinct sessions.

When a proposed removal identifies a valid turn but does not match its exact words or format, conservatively redact that entire turn as `[PRIVATE_DETAIL]`. Keep its time, index, and speaker role, preserve other turns, and still require independent privacy approval. Invalid or out-of-range turn indexes remain errors. Such removed turns cannot establish a student's language mistake.
