---
name: english-ladder-student-updates
description: Run English Ladder's nightly Zoom lesson updates, with an immediate stop when the day's transcripts are unavailable, followed by reviewed publication, Teacher view checks and due monthly English-level reviews on eligible nights. Use for student lesson automation, not the daily news edition.
---

# English Ladder student updates

Work in `/Users/philstilwell/.codex/english-ladder-cefr`. Read [student feedback rules](../../AGENTS.md) and [the nightly procedure](../../CODEX_UPDATES.md). Use the existing `verify-takako-s-feedback-recovery` automation at **23:35 America/New_York**, with one publisher and the existing Codex allowance. No separately billed AI, Cloudflare AI, subscriptions or new credentials.

## First decision: is a transcript available for this run's day?

Owner instruction, November 13, 2026: **end the entire scheduled run immediately when no Zoom lesson transcripts are available for the day.** This replaces the earlier requirement to wait 15 minutes even on an empty day.

1. If the scheduler woke early, wait until the scheduled time as documented, then perform the initial `nightly-discover`. Use its `discovery.runDate` as the New York lesson day. A catch-up after midnight retains the preceding scheduled day; do not switch to the new UTC date. A day's boundaries are consecutive New York midnights, including daylight-saving changes.
2. Quickly establish transcript availability from successful Zoom discovery and, when necessary, the connected Zoom search and note tools. Use actual meeting dates, not a note's modification date or guessed title. Inspect all result pages needed to establish absence. The queue omits completed jobs, so an empty unpublished queue alone is not proof of no transcripts. Old queued jobs are not today's transcripts. A successful complete meeting/note search with no matching sessions can establish an empty day. For any matching note, request `zoom_my_notes_get_note_content` with `include: transcript` before concluding that its transcript is missing or empty. Keep returned source text transient; never save full transcripts. A nonempty transcript is availability evidence, not permission to publish without the normal full-source and matching checks. Completed lesson sources can establish availability but must not be republished. Skip ignored, paused and deleted work.
3. If no transcript is available for that day, save only a minimal private outcome (day, check time, evidence of the empty result and `no_day_transcripts`) and **end now**. Do not wait for `discovery.recheckAt`, run the follow-up discovery or any readiness recheck, process older queued lessons, start CEFR reviews, retry Teacher view checks, or refresh the queue again. Preserve all pending work and reservations for a later eligible run or explicit manual request. Stay quiet unless a new meaningful failure or approval warning was already found. A meeting that occurred but has no available transcript is also an immediate-stop result.
4. A failed, incomplete or unauthorized Zoom lookup means availability is unknown, not zero. Report the meaningful failure and follow only the existing bounded lookup-recovery rules; never label that failure an empty day, reset reservations or create extra searches.

## When a transcript is available

Continue [CODEX_UPDATES.md](../../CODEX_UPDATES.md), retaining the single follow-up discovery and single delayed-source recheck limits. Process only verified eligible work. Preserve assessments, original quiz attempts, ignored work and exact-lesson catch-up authorization. Apply trusted speaker roles and fixed known-name/contact removal, read every full source transiently, and obtain a separate Codex lesson editor's approval of the exact draft before publishing.

After each successful publication, verify the saved results and follow [Teacher view verification](../../TEACHER_VIEW_VERIFICATION.md), including the exact feedback, seven-question quiz and unchanged student progress. Use the already saved Keychain credential privately; keep pending/failed checks for a later eligible run.

After ordinary work on a night that passed the availability check, follow [monthly CEFR reviews](../../CODEX_CEFR.md), even if that night's available transcripts were already published and no new lesson was produced. Preserve due dates, evidence windows, durable attempt limits and independent review. An empty day does not consume a CEFR attempt or change a review date.

Explicit owner requests to process or verify a named older lesson or level estimate are manual work and are not blocked by this scheduled-run stop rule. They retain all existing source, approval, retry and publication safeguards.
