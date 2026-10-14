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

Publish a reviewed assessment JSON object with `node student-portal/publish-feedback.mjs <student-origin> <private-file> --assessment`, supplying the teacher password privately on standard input as above. Publish its source session records first. Use the full transcripts to identify repeated patterns, include successful uses and evidence of progress, and distinguish future practice targets from measured performance. Do not infer a formal proficiency level or pronunciation score from transcript text.
