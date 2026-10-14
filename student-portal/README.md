# English Ladder student portal

The student portal is a separate Cloudflare Worker, `englishladder-students`, in the existing Cloudflare account. It serves the student subdomains without changing the public lesson site's Worker or publishing schedule. The first registered address is `kh26.englishladder.com`.

This first stage implements login and the responsive frontend. Assessments, session summaries, and feedback have honest empty states. It does not yet store or edit learning records. Teacher access is clearly labeled and uses the same student dashboard.

## Account addresses

Use the student's initials followed by the last two digits of the year the account is created, for example `ab26`. Keep that address permanently; do not recalculate it in January. If an address is already assigned, explicitly choose a distinct suffix before registering another account. Never overwrite an existing student to resolve a collision.

Each configured subdomain points to the same Worker. For this pilot, domains are registered explicitly in `wrangler.jsonc`. Adding an account requires both its secret record and a corresponding custom-domain route. The universal teacher credential works on every configured account; a teacher signs in separately on each subdomain. No public student directory is exposed.

## Runtime secrets

Provision these through Cloudflare's encrypted Worker secrets. Do not commit actual names, passwords, signing keys, `.dev.vars`, or provisioning inputs:

- `STUDENT_ACCOUNTS`: JSON object keyed by student ID, each with `name` and `password` string properties.
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

Tests cover student and teacher credentials, mixed case, cross-account isolation, tampering, expiry, credential rotation, cross-origin rejection, rate limits, missing secrets, source-file isolation, and public-bundle privacy. Use only fictional credentials in automated tests.

## Publishing

The portal is deployed explicitly, independently of the main lesson site:

```sh
npm run deploy:students
```

For the initial deployment, the Worker returns 503 until all secrets are configured. Supply secret values to `wrangler secret bulk --config student-portal/wrangler.jsonc` through standard input, without putting them in shell arguments, logs, or tracked files. Verify both student and teacher login after provisioning. Subsequent deployments retain existing secrets.

Do not place future student records in `public/`, the public lesson repository assets, or browser storage. The next stage needs authenticated server storage with account checks on every read and write. The public site's existing local completion markers are separate from this portal and do not transfer automatically.
