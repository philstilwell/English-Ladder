# Daily lesson recovery

The daily workflow now keeps completed work when a later step fails. The schedule remains **10:00, 13:00 and 16:00 UTC**. The later runs resume an unfinished edition or preserve an already published edition.

## What is saved

Before requesting lesson text, the workflow saves the selected source. After each draft and successful review, it saves the current draft, feedback, attempt count, and approved levels. A reviewer outage leaves the existing draft awaiting review.

`lesson_checkpoint.py` writes these records atomically: an interrupted write does not replace a usable saved file with a partial one. GitHub retains the date's checkpoint as a `lesson-state-RUN-ATTEMPT` artifact for seven days, including after an ordinary generation failure. These records are outside the public site. Review diagnostics remain a separate artifact.

`workflow_checkpoint.py` restores only a compatible checkpoint from this repository's scheduled or manually dispatched daily workflow on the same branch. It supports an earlier attempt of the same GitHub run. It checks the artifact's origin, date, size, integrity and generation-policy fingerprint before copying the date file. Invalid candidates are skipped; an unavailable GitHub service stops the run after bounded retries so it cannot silently trigger duplicate paid generation.

`lesson_run.py` checks each saved approval against the exact lesson, source, level, vocabulary reservations and current policy. It repeats the local content and evidence checks before reuse. Editing the generation or teaching policy invalidates older checkpoints. A bare approval flag is insufficient.

## Recovery and limits

| Situation | Result |
| --- | --- |
| Temporary Gemini network error, timeout, rate limit or selected server error | Retry the same request, up to three total requests with waits of two and four seconds. |
| Temporary GitHub checkpoint service error | Retry the read or download up to three times with the same waits. |
| Authentication, request-schema or other permanent error | Stop immediately; repeated identical calls would not fix it. |
| Reviewer returns empty or malformed data | Review the same draft again, up to two review responses in that invocation. Preserve it for a later run if the reviewer remains unusable. |
| Reviewer identifies a real lesson defect | Keep publication blocked. Revise the failed sections where possible, then check and review the merged lesson again. |
| One level fails after earlier levels passed | Save progress and resume the unfinished level on the next run. |
| The date already has a complete archive | Manual and scheduled workflow runs preserve its text and reuse or recover its illustration through the existing image process. |
| Push or manual `deploy_only` run | Rebuild and verify existing material without paid generation. |

Each level has at most **three draft attempts per invocation and six across compatible recovery runs for that date**. The attempt counter is saved before requesting a draft, including requests interrupted before a usable response. Transport retries sit within each draft attempt. Gemini requests have a three-minute timeout, with the SDK's internal retries disabled so they cannot multiply the explicit request limit. Generation has a 30-minute step limit within the 45-minute job, reserving time to upload saved progress after a slow-provider timeout. These are workload limits, not a guaranteed billing ceiling; provider charging and request outcomes can vary.

The writer now returns each reading sentence together with its numbered source reference. The program creates the reading and evidence lists together and copies a grammar example from the reading by sentence index. This avoids mismatched array lengths and retyped quotations. The independent reviewer must still determine whether the evidence supports the claim and the example supports the grammar explanation.

All publication requirements remain in force: at least **6/8/10 reading sentences, vocabulary items and multiple-choice questions** for Beginner/Intermediate/Advanced; separate vocabulary targets; appropriate language and register; factual support; unambiguous questions; and correct teaching feedback. All three levels must pass before publication.

## Operational limits and verification

A genuine content problem, persistent service outage, runner termination before artifact upload, or unavailable artifact storage can still prevent publication. Recovery reduces repeated work; it does not turn a failed review into an approval. Exhausting the daily draft allowance leaves diagnostics and the last draft for investigation. Do not reset the counter or relax a quality check just to obtain a green run.

Offline tests cover paired evidence, exact grammar references, transient versus permanent failures, approval binding, checkpoint corruption, same-run recovery, interrupted reviews, targeted repairs, and the per-run/per-date attempt limits. They use saved lessons and simulated provider responses without paid generation. They establish recovery behavior, not a guarantee of model accuracy.

Implementation: `generation_retry.py`, `lesson_checkpoint.py`, `lesson_run.py`, `workflow_checkpoint.py`, `lesson_evidence.py`, `update_site.py`, `news_quality.py`, and `.github/workflows/cron.yml`.

Provider details: [Google Gen AI SDK retry and timeout types](https://github.com/googleapis/python-genai/blob/v1.62.0/google/genai/types.py), [GitHub workflow artifacts](https://docs.github.com/en/rest/actions/artifacts).
