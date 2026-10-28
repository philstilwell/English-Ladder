# Independent daily monitor

For the existing producer's registration, time-zone requirements, and a fresh
effective next-run receipt, see [producer registration](daily-registration.md).
An old inspection report does not establish the current registration state.

The local scheduled Codex task is the only automatic producer. It requests starts
at 22:30, 23:30, and 00:30 America/New_York every day. The first start targets
the following local date, and the two recovery starts remain pinned to that
edition across midnight. Each attempt follows
`.agents/skills/english-ladder-daily-producer/SKILL.md`, resumes missing stages,
and exits without model work when the complete edition is already live. It uses
the supported local checkout mode, resumes recognized current-date producer
artifacts, and stops on unrelated checkout changes or low disk space. The Mac
must be on, awake, connected, and signed in to ChatGPT through the Codex app.

A separate macOS timer runs `daily_recovery.py` every 15 minutes and at login.
It is a read-only monitor, not a second producer. From 22:30 through 00:59 New
York time it records that the production window is still open. From 01:00 until
the next 22:30 cycle it checks:

- today's date-specific archive on GitHub;
- all three reviewed levels and their minimum reading, vocabulary, and quiz data;
- every reviewed seven-language vocabulary record and the matching image bytes;
- the identical public archive and current feed;
- Discover, the archive listing, the three level feeds, and the three dated pages;
- whether the local producer lock or an offline GitHub publication check is still active; and
- a 30-minute grace period for a saved commit to reach hosting.

Missing, partial, unreadable, or stale state is reported as `needs_attention`.
An edition still being produced or in its bounded publication handoff is reported
as `producer_running`, not a false failure. A handoff older than two hours no
longer suppresses `needs_attention`. The producer keeps its advisory process lock
and also exposes short-lived timestamped activity metadata; the background timer
uses only file metadata so macOS does not need to grant it access to open producer
artifacts in Documents.
The monitor never dispatches a workflow, starts generation, repeats a model call,
changes a schedule, or mutates GitHub. Network uncertainty is reported rather
than treated as proof that an edition is missing.

The installed files are:

- `~/Library/Application Support/EnglishLadderDailyRecovery/daily_recovery.py`
- `~/Library/LaunchAgents/com.philstilwell.englishladder.daily-recovery.plist`
- `~/Library/Application Support/EnglishLadderDailyRecovery/state/last-check.json`
- `~/Library/Application Support/EnglishLadderDailyRecovery/state/recovery.log`

`--apply` means “persist this read-only health result and its rotating log.” It
does not authorize recovery or a remote write:

```sh
python3 daily_recovery.py --json
python3 daily_recovery.py --apply --json
```

When a stage needs recovery, run the repository skill or
`.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD`. The runner preserves complete
artifacts and uses fresh, ChatGPT-authenticated Codex sessions only for missing
work. A hosting failure after a saved commit is verified and retried as a
publishing problem; it is never a reason to regenerate the lesson.
