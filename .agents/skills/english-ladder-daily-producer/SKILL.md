---
name: english-ladder-daily-producer
description: Produce, recover, publish, and verify the daily English Ladder news edition with ChatGPT-plan Codex sessions and no paid API fallback. Use for the scheduled daily run and manual recovery of missing lesson text, review, seven-language vocabulary definitions, or the daily illustration.
---

# English Ladder daily producer

Run this workflow from the English-Ladder repository. It is the only automatic
daily content producer. GitHub Actions performs offline tests and publication
verification only. Requested starts are 22:30, 23:30, and 00:30
`America/New_York`. The 22:30 run produces the following local date; both later
opportunities stay pinned to that edition across midnight. The Codex
desktop task runs in the repository's supported local environment because the
large static archive makes a second worktree unsafe on this Mac's available
disk space; the checkout-status check below remains mandatory.

## Hard boundaries

- Use `gpt-6.1-sol` with high reasoning through the signed-in Codex CLI.
- Never use, reveal, copy, or request an API key. Never call Gemini or an OpenAI
  API endpoint. `plan_daily_runner.py` removes all common model API-key variables.
- Do not run `update_site.py` without `--refresh-pages`; the retired modes fail
  closed. Do not run `vocabulary_translations.py` without `--check`. Do not call
  `daily_images.ensure_daily_image`.
- Do not alter billing, secrets, permissions, the domain, hosting, or the separate
  manual Everyday English audio/TTS workflow.
- Do not overwrite a complete saved edition. Resume missing stages and preserve
  the approved source, lesson text, translations, and illustration.
- Do not publish a partial edition. Lesson text, independent review, all seven
  translation languages, the matching illustration, offline tests, and the site
  audit must all pass.

## Run

1. Inspect the repository status. A clean checkout is required before starting a
   new date. If the only changes are validated, current-date producer artifacts
   that correspond to the retained `.daily-agent/` state, preserve them and
   resume. If unrelated local changes are present, stop and report them instead
   of overwriting them. Fetch `origin/main` and fast-forward or rebase before
   creating new content.
2. Resolve the release date with:

   ```bash
   .venv/bin/python -c 'from daily_schedule import scheduled_release_date; print(scheduled_release_date().isoformat())'
   ```

3. Check whether the complete edition is already live:

   ```bash
   .venv/bin/python daily_publication.py --date YYYY-MM-DD --require-published
   ```

   When this passes, clear any completed publication handoff with
   `.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD --finish-publication`
   and exit. A later scheduled attempt must be a no-op.
4. Run the bounded producer:

   ```bash
   .venv/bin/python plan_daily_runner.py --date YYYY-MM-DD
   ```

   The runner uses fresh ephemeral Codex sessions for drafting, independent
   editorial review, translation, independent multilingual editing, and image
   generation. The exact underlying built-in image model is recorded as not
   exposed unless the tool reports it explicitly. Local validators import the results. It allows at most three full
   lesson attempts per level during one scheduled run and retains resumable state
   under ignored `.daily-agent/`. A per-edition process lock makes overlapping
   22:30/23:30/00:30 New York opportunities exit without duplicating model work.
   Read its final JSON status. If it is `already_running` or
   `publication_pending`, exit this task immediately: do not rebuild, test,
   inspect, commit, push, or verify publication. `ready_to_publish` creates a
   persistent handoff that blocks later attempts throughout the steps below.
5. Inspect `git status`, `git diff --check`, the new illustration, and the
   provenance records. Never stage `.daily-agent/`, usage ledgers, secrets, or
   audio. Expected daily output may include the dated archive, dated image and
   metadata, translation records, level pages, dated pages, Discover page, feeds,
   search metadata, and sitemaps.
6. Re-run `.venv/bin/python audit_site.py`,
   `.venv/bin/python -m unittest discover -s tests`, and
   `/Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node --test tests/*.test.cjs`
   if any file changed after the runner finished. The absolute Node path is the
   supported runtime bundled with the ChatGPT desktop app that owns this task.
7. Fetch `origin/main` again. Rebase the validated commit if main moved, then
   repeat the focused completeness check. Commit with
   `Auto-update daily lessons [skip-daily-workflow]` and push to `main`. The marker
   is retained for history; the new GitHub workflow is offline-only and may still
   check the push.
8. Wait for hosting, then run:

   ```bash
   /Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node cloudflare/check-daily-publication.cjs YYYY-MM-DD
   ```

   Verify the dated Beginner, Intermediate, and Advanced pages, Discover feature,
   matching illustration bytes, and all seven translation controls on
   `https://englishladder.com` itself. Report the
   commit and GitHub workflow link. If publication is still converging, wait and
   retry the read-only verifier; do not regenerate content.
9. Only after the live verifier passes, run
   `.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD --finish-publication`.
   This independently rechecks the complete live edition and clears the handoff.
   If the task stops before this step, retain the marker and report the blocker;
   never delete it merely to let another producer start.

## Failure handling

- A model or validation failure leaves state for the 23:30 or 00:30 New York attempt.
- A push race requires a normal fetch/rebase and repeated local checks, not a
  force push.
- A hosting failure after a saved commit is a publication problem; do not rerun
  model stages.
- After the final attempt, the separate macOS monitor records `needs_attention`.
  It never dispatches a GitHub generation workflow.
