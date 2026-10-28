# Existing producer registration and receipts

The sole daily-news producer is the desktop automation **English Ladder Daily
Plan**, ID `english-ladder-daily-plan`, in the local **English Ladder Daily**
project on Phil's current Mac. Its stable checkout is
`/Users/philstilwell/.local/share/EnglishLadder/English-Ladder`.
Manage this existing ID with the app's `automation_update` tool or Scheduled
screen. Do not create another task, LaunchAgent, or generation workflow.

The requested local starts remain **22:30, 23:30, and 00:30 America/New_York**.
The desktop scheduler uses a small dispatch offset; its saved effective dispatch
and nominal start are different fields. The producer's
`daily_schedule.py --wait-for-start` guard holds an early arrival until the
nominal start before selecting the edition. The 22:30 and 23:30 opportunities
select tomorrow's edition; the following 00:30 selects that same edition.

## Verified local-time format

Use the recurrence in `ops/english-ladder-daily.automation.toml`, without a
`DTSTART` line. The Mac's system time zone must remain `America/New_York`.
This follows New York daylight-saving changes; it is not a fixed UTC schedule.
If the Mac's time zone changes, this registration needs rechecking.

On October 28, 2026, the supported app update tool accepted an explicit
`DTSTART;TZID=America/New_York` recurrence but saved an incorrect **19:30 New
York** nominal next run. It was immediately reverted through the same tool,
restoring **22:30**. Acceptance of a schedule string alone is therefore not
proof of the effective schedule. The repository template now matches the
working local registration. No app files or scheduler database records were
edited directly.

## Refresh the evidence

From the stable checkout, run this diagnostic command:

```sh
.venv/bin/python daily_registration.py
```

It prints a timestamped receipt containing the existing registration, recognized
active daily-producer IDs, Mac time zone, effective next dispatch, and nominal
next start. It checks both saved configuration and scheduler records. It omits
credentials and the full prompt. It uses read-only database access, makes no
network or model calls, and does not register, run, repair, or publish anything.
Its additional service cost is $0.

The database is supplemental local diagnostic evidence, not a supported editing
interface. If a future app version changes its schema, the command reports
`needs_attention`; use the app's Scheduled screen to establish the current
registration and next run. Never repair it by writing the database.

Use the existing independent publication check separately:

```sh
.venv/bin/python daily_recovery.py --json
```

Registration does not prove successful generation or publication. A receipt is
only valid at its `observed_at` timestamp; after its next dispatch is due, get a
fresh receipt. A stale report must not be restated as a current failure.

## October 28 reconciliation

The earlier report at repository revision `6b773369` saying registration was
incomplete is superseded by local scheduled runs on October 26–28, the active
registration, and the [dated receipt](../ops/receipts/daily-registration-2026-10-28.json).
The current Mac is `Mac.lan`; its system zone was verified as `America/New_York`.
Only one active daily-news producer was found in both local configuration and
scheduler records. The `com.philstilwell.englishladder.daily-recovery`
LaunchAgent remains the independent, read-only monitor.

The October 28 edition passed fresh public completeness and monitor checks.
The known early-dispatch failure was fixed in commit `e3fb2e8`: the 22:26
arrival had previously selected yesterday's edition. The next real first
nightly attempt after that fix is still required to confirm automatic operation;
passing tests and a registration receipt do not establish that future outcome.
