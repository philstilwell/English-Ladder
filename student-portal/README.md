# English Ladder student portal

The student portal is a separate Cloudflare Worker, `englishladder-students`, in the existing Cloudflare account. It serves the student subdomains without changing the public lesson site's Worker or publishing schedule. The first registered address is `kh26.englishladder.com`.

The portal provides login, private dated session feedback, an overall ESL assessment, session summaries, a session sidebar, and a mobile session picker. Each session has a bookmarkable `#feedback/YYYY-MM-DD-HHMM` address; the time suffix allows multiple sessions on one day. The newest feedback opens after login. The `#assessments` page shows strengths, recurring patterns, and next priorities with links to the relevant session feedback. Accounts without an assessment show an empty state. Teacher access is clearly labeled.

## Account addresses

Use the student's initials followed by the last two digits of the year the account is created, for example `ab26`. Keep that address permanently; do not recalculate it in January. If an address is already assigned, explicitly choose a distinct suffix before registering another account. Never overwrite an existing student to resolve a collision.

Each configured subdomain points to the same Worker. For this pilot, domains are registered explicitly in `wrangler.jsonc`. Adding an account requires both its secret record and a corresponding custom-domain route. The universal teacher credential works on every configured account; a teacher signs in separately on each subdomain. No public student directory is exposed.

## Runtime secrets

Provision these through Cloudflare's encrypted Worker secrets. Do not commit actual names, passwords, signing keys, `.dev.vars`, or provisioning inputs:

- `STUDENT_ACCOUNTS`: JSON object keyed by student ID, each with first-name-only `name`, optional chosen `nickname`, and `password` string properties. The API also reduces legacy full-name records to their first word before responding.
- `TEACHER_PASSWORD`: the universal teacher password.
- `SESSION_SECRET`: at least 32 characters of cryptographically random signing material.

Passwords are lowercased in the browser and again on the server, including teacher passwords. Spaces are significant. Passwords are read only on the server and never embedded in the public bundle. They are stored as encrypted Cloudflare secrets; verification uses a keyed, constant-time HMAC comparison. This pilot follows the requested shared/static password model rather than providing password recovery or individual teacher identities.

Sessions use an eight-hour, signed, host-only `HttpOnly; Secure; SameSite=Strict` cookie. The session is bound to both the student ID and exact host. Changing an account password invalidates that account's student sessions; changing the teacher password invalidates teacher sessions; rotating `SESSION_SECRET` invalidates every session. Sign-out removes this browser's cookie. There is no server-side session registry, so sign-out does not revoke a previously copied token; it expires or is invalidated by credential rotation.

Login permits five attempts per student/IP per minute and twenty per student per minute using Cloudflare rate-limit bindings. These limits are local to each Cloudflare location and are not a globally exact lockout. Unknown accounts and unconfigured Workers fail closed. Requests that change sign-in state require an exact same-origin header. No student information is returned before login. All responses disable caching and indexing, and the portal loads no analytics or third-party scripts.

## Development and checks

Use the repository's locked dependencies (`npm ci`). Set test-only credentials in an ignored `student-portal/.dev.vars` file and include `LOCAL_STUDENT_ID` for the account to preview. The local override is accepted only for `localhost` and `127.0.0.1`.

```sh
npm run test:students
npm run dev:students
```

Tests cover credentials, account isolation, tampering, expiry, rotation, cross-origin rejection, rate limits, private storage, teacher-only publishing, transcript validation, pagination, deep links, stale responses, sign-out cleanup, and safe text rendering. Use only fictional credentials and records in automated tests.

## Publishing

The portal is deployed explicitly, independently of the main lesson site:

```sh
npm run deploy:students
```

For the initial deployment, the Worker returns 503 until all secrets are configured. Supply secret values to `wrangler secret bulk --config student-portal/wrangler.jsonc` through standard input, without putting them in shell arguments, logs, or tracked files. Verify both student and teacher login after provisioning. Subsequent deployments retain existing secrets.

## Private session storage

`FEEDBACK_STORE` binds the `FeedbackStore` Durable Object class, using a private SQLite database for each student. The Worker selects the database from the registered account hostname after checking the signed session. The database has no public URL. The `feedback-v1` migration creates the SQLite-backed namespace. Never remove or rename this migration or class to reset a deployment; that can affect stored records.

`GET /api/feedback` returns up to 100 newest session entries with a `nextCursor`; pass `?before=<cursor>` for older entries. `GET /api/feedback/<id>` returns a session. Both require login. `PUT /api/feedback/<id>` requires the teacher role and exact same origin, validates a maximum 64 KiB JSON body, and atomically updates the record and its index. Repeating a PUT replaces that session, without duplicates. There is no deletion endpoint. Both student and teacher responses omit Zoom note identifiers, and neither view links to Zoom meeting notes. All responses prohibit caching. The browser stores no records persistently and clears private content on sign-out, expiry, and restoration from the browser's page cache.

`GET /api/assessment` returns `{ assessment: <record or null> }` for the authenticated account. `PUT /api/assessment` has the same teacher, origin, size, and privacy restrictions as feedback publishing. It replaces the current assessment at the private key `assessment:current`. Each assessment source must already exist in this student's feedback storage with a reviewed full transcript; every timestamp must fall inside that transcript's recorded coverage. Assessment evidence links lead only to internal feedback pages. No raw transcript or source-note link is exposed.

Follow [AGENTS.md](AGENTS.md) for every student's feedback. The `scope: "esl"` value and transcript metadata are required, but they do not replace a human/agent content review. Read full available transcripts, separate teacher feedback from extra practice, use first names, and omit unrelated personal conversation. New exercises are clearly labeled. Show both New York and Japan dates to avoid confusion across midnight.

Write student-facing content at an A1–A2 reading register: short sentences, common words, and simple examples. This does not assign a proficiency level to the student. Put words and phrases being discussed in quotation marks or italics. Vocabulary headings and practice models are italicized by the page; authors must mark target words in prose and distinguish lesson quotations from new examples. These preferences are saved in the portal's AGENTS.md for future pages.

Keep authoring inputs under ignored `student-portal/private/`, with directory permission 700 and file permission 600. Actual records, transcripts, and credentials must never enter Git, public assets, or browser storage. `tests/fixture.mjs` shows the schema with fictional data. Source transcript offsets and segment counts document the available coverage; raw transcripts are not stored on the portal.

Publish a reviewed JSON array using `node student-portal/publish-feedback.mjs <student-origin> <private-file>`. Supply the existing teacher password on standard input through a private pipe or a terminal with echo disabled, never as a command argument. The publisher validates all records before connecting, verifies teacher access, uploads each record, compares every saved record with its input, and signs out. It supports HTTPS student subdomains and HTTP localhost for development. The SQLite-backed service is available on Cloudflare's free plan; this small text library is expected to remain within included quotas. See [Cloudflare pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/).

The public lesson site's existing local completion markers are separate from this portal and do not transfer automatically.

An assessment may include an optional private `quiz` with a title, simple instructions, and up to ten multiple-choice questions. Each question references one assessment pattern by `patternIndex`, provides two to four distinct options with individual feedback, identifies `correctIndex`, and includes a correct model sentence. The same teacher-only assessment publisher validates and saves it. Older assessments without a quiz continue to work.

The `#quiz` page shows one question at a time with immediate feedback, retries, and a first-try result. It names the quiz’s source lesson dates and links to their private feedback pages. These are new practice questions based on the assessment, not transcript quotations. The Quiz menu entry stays hidden until a quiz is available. If lesson evidence is insufficient, leave the optional quiz absent; no arbitrary session-count threshold is imposed. After-session quizzes can be enabled through a Codex thread heartbeat; see [QUIZ_AUTOMATION.md](QUIZ_AUTOMATION.md). It reads full Zoom transcripts and private first-try history. A quiz may have its own `sourceSessions`, `patternTitles`, and `generatedForSession`, allowing a later lesson without changing the earlier assessment. Quiz sources must exist in the same private account with reviewed transcripts. Legacy quizzes inherit assessment sources and pattern titles. The workflow helper exports complete history and merges a new quiz into the live assessment.

Student answers save after each choice in the same private per-student database. The first choice is append-only; later choices do not change the first-try score. A completed attempt is marked when the last question is answered correctly. Reloading or signing back in resumes the saved attempt, and starting again creates a new attempt only on its first answer. One unfinished attempt is shared across tabs/devices. Teacher practice is labeled and never writes student results. Earlier in-memory quizzes cannot be recovered.

`GET /api/quiz/state` resumes an unfinished attempt; after completion, it offers a newer published quiz automatically. Without a newer quiz, it returns the completed result. `?new=1` offers a fresh quiz only after the previous attempt is complete. `POST /api/quiz/answer` accepts only an attempt UUID, quiz version, question index, and choice index (maximum 1 KiB). It requires a student session and exact same origin. A transaction validates question order and appends the choice, using server timestamps and server-calculated summary scores. Identical retries are idempotent, so a lost response cannot duplicate an attempt or change its first answer. Conflicting tabs reload the saved state. Failed saves block further answers until retried or reloaded and are never labeled as saved. There are no update/delete endpoints for history.

The teacher-only `#quiz-results` page shows dated attempts, first-try mistakes, original answer choices, later retries, and progress bars grouped by matching question sets. `GET /api/quiz/results` returns 20 newest summaries with a `nextCursor`; pass `?before=<cursor>` for earlier attempts. `GET /api/quiz/results/<uuid>` returns the full saved attempt. Each attempt snapshots the quiz, pattern titles, and source lesson references, so changing an assessment cannot reinterpret earlier results. Unfinished attempts remain visible and are excluded from completed-score trends. Dates use New York time.

No answers are stored in browser persistent storage. Private page state clears on sign-out or expiry, while saved server records remain available. This is learning practice, not a secure exam or proficiency score: authenticated students can see answer keys, and repeated exposure affects scores. Tests cover private access, roles, account isolation, ordering, invalid answers, concurrent tabs, duplicate requests, version snapshots, pagination, save failure, resuming, teacher preview, source links, and logout cleanup.

Publish a reviewed assessment JSON object with `node student-portal/publish-feedback.mjs <student-origin> <private-file> --assessment`, supplying the teacher password privately on standard input as above. Publish its source session records first. Use the full transcripts to identify repeated patterns, include successful uses and evidence of progress, and distinguish future practice targets from measured performance. Do not infer a formal proficiency level or pronunciation score from transcript text.
