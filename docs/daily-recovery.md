# Independent daily monitor

The local scheduled Codex task is the only automatic producer. It requests starts
at 06:15, 07:15, and 08:15 UTC every day. Each attempt follows
`.agents/skills/english-ladder-daily-producer/SKILL.md`, resumes missing stages,
and exits without model work when the complete edition is already live. It uses
the supported local checkout mode, resumes recognized current-date producer
artifacts, and stops on unrelated checkout changes or low disk space. The Mac
must be on, awake, connected, and signed in to ChatGPT through the Codex app.

A separate macOS timer runs `daily_recovery.py` every 15 minutes and at login.
It is a read-only monitor, not a second producer. Before 08:45 UTC it records that
the production window is still open. After that time it checks:

- today's date-specific archive on GitHub;
- all three reviewed levels and their minimum reading, vocabulary, and quiz data;
- the identical public archive and current feed;
- Discover, the archive listing, the three level feeds, and the three dated pages;
- whether an offline GitHub publication check is still active; and
- a 30-minute grace period for a saved commit to reach hosting.

Missing, partial, unreadable, or stale state is reported as `needs_attention`.
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
