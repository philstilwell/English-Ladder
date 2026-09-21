# Publishing recovery

## Why this exists

On September 21, 2026, lesson generation and repository checks succeeded in GitHub run `35641320571`, but Cloudflare build `f477f88c-43c1-4b0e-8c61-9713b2a208d3` failed while running `npx wrangler deploy`. The last detailed line showed an automatic installation of Wrangler 4.136.0; the log did not establish the cause. Retrying the same commit as build `63103a12-3e69-4553-9f5a-65428b2bc03f` succeeded without source changes. The recovery was verified by deployment-only GitHub run `35644346600`.

The changes here address repeatability, bounded upload recovery, and useful diagnostics. They do not claim that the Wrangler version itself caused the incident.

## Cloudflare configuration

For the existing `englishladder` Worker, production branch `main`, set **Settings → Builds → Build configuration → Deploy command** to:

```sh
npm run deploy:cloudflare
```

The separate Cloudflare build command can be empty: the deploy wrapper runs the complete preflight itself. Keep dependency installation enabled so Cloudflare installs from `package-lock.json`. Wrangler is pinned to **4.136.0**, the version that successfully deployed the recovered commit. Upgrade it deliberately with the lockfile and validate a deployment after changing it. Do not replace the deploy command with an unversioned `npx` installation.

`build:cloudflare` runs JavaScript syntax checks, site and search audits, and packages the allowlisted public files. It does not generate lessons, translations, or images. The deployment wrapper verifies the installed Wrangler version and prepared source revision before uploading. It runs preflight once (60-second limit), then attempts to deploy the same prepared files up to three times, with 10- and 30-second delays and a 120-second limit per attempt. A timed-out child process is stopped before another attempt. Preflight failure prevents all uploads. Detailed Wrangler output and numbered attempts stay in the Cloudflare build log.

The retry budget is under eight minutes once the wrapper starts. It does not include Cloudflare queueing or dependency installation. Failure before the wrapper starts, permanent authentication/configuration errors, or a longer outage can still require manual recovery.

## GitHub verification

The daily workflow first generates/checks/saves lessons, then passes the exact saved commit to the separate **Verify saved lesson publishing** job. Selecting **Re-run failed jobs** after a publishing-only failure reruns that check without running lesson, translation, image, or page generation. Re-running all jobs is unnecessary for a hosting failure.

The verifier waits up to 12 minutes for the complete public-file hash map. A matching revision alone is never enough; all file hashes must match. Conversely, a code-only commit with identical public files may pass, while the report still records the actual served revision. Existing current-lesson checks continue to verify the ordinary URLs, all three levels and feeds, archive, homepage, JSON hashes, and private-path 404 responses. A public-domain 403 from GitHub's runner retains the existing warning behavior; the Workers hostname remains a blocking check.

Each run retains a `publishing-RUN-ATTEMPT` artifact for 14 days. It contains the expected deployment manifest, a JSON comparison report, and available verification logs. The report records expected/live revisions, file counts, sample missing/changed/unexpected files, and whether the expected revision was ever observed. Shell pipeline failures propagate even when output is copied into a log.

## Recovering a persistent failure

1. Open the publishing artifact and note the expected revision. Check whether Cloudflare is serving an older commit, changed files, or no readable manifest.
2. Open the English Ladder Cloudflare build for that commit. If its deployment attempts failed, inspect their output and retry that existing build after addressing any persistent error. Keep the generated lessons saved in GitHub; do not regenerate them merely to retry hosting.
3. After Cloudflare succeeds, choose **Re-run failed jobs** in the matching GitHub run. Confirm that only **Verify saved lesson publishing** reruns.
4. Alternatively, run **Daily ESL Lesson Generator** with `deploy_only=true` to rebuild existing pages and verify them without paid generation. This is a verification/rebuild route: if no repository files change, it does **not** trigger or retry a Cloudflare build by itself.
5. Confirm the current lesson date and public site. If a newer lesson was intentionally published meanwhile, verify that newer revision using a fresh deployment-only run rather than rolling the site back to satisfy an old check.

Local read-only verification after installing the existing project dependencies:

```sh
npm run build:cloudflare
python3 cloudflare/verify-publishing.py https://englishladder.philstilwell.workers.dev --report /tmp/english-ladder-publishing.json
node cloudflare/verify-current-lesson.cjs https://englishladder.philstilwell.workers.dev
node cloudflare/verify-current-lesson.cjs https://englishladder.com
```

Offline failure tests cover eventual success, exhausted retries, preflight rejection, tool-version mismatches, interruption/timeouts and child-process cleanup, stale/partial/malformed manifests, matching files across revisions, and bounded verification waits. No provider generation API is called by these tests.

Cloudflare references: [build configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/) and [Wrangler deploy command](https://developers.cloudflare.com/workers/wrangler/commands/workers/).
