---
name: english-ladder-daily-producer
description: Produce, recover, publish, and verify the daily English Ladder news edition through the sole ChatGPT-authenticated Codex producer. Use for scheduled editions and manual recovery of their lessons, reviews, translations, illustration, or publication.
---

# English Ladder daily producer

Work on Mac.lan in `/Users/philstilwell/.local/share/EnglishLadder/English-Ladder`
using the existing checkout and installed environment. The static archive is
too large for a second checkout. GitHub Actions runs offline checks only.

Use the ChatGPT-authenticated Codex CLI with `gpt-6.1-sol`, high reasoning, and
ChatGPT's built-in image generation. Use included allowance first; authorized
existing credits may cover any shortfall, including the image.
[Estimate credit use](references/recovery.md#usage-or-capacity) before it begins. Stop if neither can
support the work. No API keys, Gemini, fallback publisher, purchases, resets,
top-ups, subscription, billing, credential, security, hosting, schedule, or
audio changes. The runner alone handles generation and rebuilds.

## Preflight and run

1. Run this gate **before resolving the edition or checking publication**:

   ```bash
   .venv/bin/python daily_schedule.py --wait-for-start
   ```

   Wait through any early dispatch and use only the printed date as `DATE`.
   The 22:30 and 23:30 New York starts target the next local date; 00:30
   recovers that same edition. Keep local wall-clock times across daylight saving.

2. Confirm the required checkout, installed dependencies, ChatGPT sign-in and
   `CODEX_THREAD_ID`. Inspect status and fetch `origin/main`. Fast-forward a
   clean checkout as needed. Preserve only recognized artifacts for this date
   backed by `.daily-agent/DATE/`; stop on unrelated changes, a checkout you
   cannot safely synchronize, or an unavailable prerequisite.

3. Check for a completed edition:

   ```bash
   .venv/bin/python daily_publication.py --date "$DATE" --require-published
   ```

   If already live with no handoff, exit. If already live with a handoff, go
   to ownership and live verification below. Otherwise run:

   ```bash
   .venv/bin/python plan_daily_runner.py --date "$DATE"
   ```

   Preserve saved source, approved levels, reviewed translations and matching
   illustration. A valid draft can resume at review. The runner caps lesson
   attempts at three per level per run. After a failure, retain state and logs.
   See [recovery guidance](references/recovery.md) for manual repairs, capacity
   errors, and credit estimates.

4. Follow the runner's final status:

   - `already_running`: exit immediately.
   - `ready_to_publish`: this chat owns the durable publication handoff.
   - `publication_pending`: recover only the saved publication, as follows.

   For pending publication, use the reported owner (or the saved owner in
   `publication-pending.json` on the already-live path). Read only that chat
   with the supported Codex app `read_thread` tool, one recent turn and bounded
   output. Leave active, waiting, unavailable, ambiguous and unknown owners
   alone. A marker's age or absent producer process proves nothing. If the app
   confirms the chat failed or ended and its last commands/tools also stopped,
   transfer ownership under the lock:

   ```bash
   .venv/bin/python plan_daily_runner.py --date "$DATE" --resume-publication-from STOPPED_THREAD_ID
   ```

   Continue only on `ready_to_publish`. This checks the expected owner,
   saved completeness and archive checksum. Do not guess a missing owner,
   delete a marker, regenerate or rebuild. If resuming the current chat's own
   handoff after an explicit retry, confirm its prior commands ended before
   continuing; no ownership transfer is needed.

## Validate, push, and verify

1. For an unpushed edition, inspect the changed files, illustration and
   provenance, and run `git diff --check`. Stage only expected generated
   publication files; keep state, usage logs, secrets and audio out of Git.
   Once the runner has returned `ready_to_publish` and writes have stopped,
   run all three checks (they may run in parallel):

   ```bash
   .venv/bin/python audit_site.py
   .venv/bin/python -m unittest discover -s tests
   /Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node --test tests/*.test.cjs
   ```

   Fetch `origin/main` again before pushing. Use a normal rebase if safe, then
   recheck saved completeness and repeat checks invalidated by changes. Stop
   on conflicts you cannot resolve without altering unrelated work. Commit
   with `Auto-update daily lessons [skip-daily-workflow]` and push to `main`.
   If the matching complete commit is already on `origin/main`, skip commit
   and push; proceed to live verification.

2. Wait for hosting and verify on `https://englishladder.com`:

   ```bash
   /Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node cloudflare/check-daily-publication.cjs "$DATE"
   ```

   This checks the dated pages, live data and matching image bytes. In a
   temporary browser tab, also verify the Discover feature and its three level
   links. On each dated Beginner, Intermediate and Advanced page, select all
   seven definition languages, check the displayed definitions against the
   reviewed values, and verify English reset. Restore the original preferences
   and close the tab. Stale data or a 404 during rollout calls for bounded
   read-only rechecks, not regeneration.

3. Only after the live verifier **and** browser checks pass, clear the handoff:

   ```bash
   .venv/bin/python plan_daily_runner.py --date "$DATE" --finish-publication
   ```

   Report the edition, commit and offline workflow link, or the failing stage
   and next action. If publication cannot be verified, retain the handoff.
