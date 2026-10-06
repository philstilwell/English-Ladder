# Independent daily recovery

The daily GitHub schedule is the main trigger. A second timer on Phil's Mac checks
every 15 minutes, starting at 02:45 America/New_York, including weekends. The timer
uses the existing GitHub CLI account and does not depend on Codex or GitHub's cron
scheduler. It also runs at login; missed calendar checks are coalesced when the Mac
wakes. No server subscription or new credential stored with another service is
required. The Mac must be on, awake, signed in, and connected to the internet.

`daily_recovery.py` is installed at
`~/Documents/Codex/English-Ladder-daily-recovery/daily_recovery.py`. macOS runs it
through `~/Library/LaunchAgents/com.philstilwell.englishladder.daily-recovery.plist`.
Its `state/last-check.json` records the latest result; `state/state.json` preserves
today's attempt reservations and `state/recovery.log` retains rotating diagnostics.
These installation and state files are not website assets.

The default command is read-only. `--apply` enables recovery:

```sh
python3 daily_recovery.py --json
python3 daily_recovery.py --apply --json
```

The check reads the date-specific archive from GitHub, confirms three reviewed
levels, and checks the identical public archive, current feed, homepage, archive
listing, level feeds and three dated pages. An HTTP failure or unreadable data
does not count as proof of a missing edition. A partial saved edition needs
attention; it never triggers replacement generation.

If today's archive is missing and no daily job is queued/running, recovery starts
the existing daily workflow with the explicit date. The workflow retains its
source/evidence checks, independent review, saved progress, generation limits,
translation budget and illustration limit. It uses `--skip-existing`, checks out
the current branch after waiting, and serializes daily jobs, so a delayed scheduled
attempt sees an edition saved by recovery and does not replace it. Existing daily
generation charges still apply; the timer itself never calls a generation API.

If the complete archive is already saved but the live site is stale, the timer
allows 30 minutes for normal publishing, then starts the workflow with both
`deploy_only=true` and `retry_publishing=true`. This does not generate lesson text,
translations or images. The latter input commits a private publication request,
which causes the existing Cloudflare GitHub integration to retry even when the
public lesson files have not changed. The workflow refuses `retry_publishing`
without `deploy_only`.

A local lock prevents overlapping checks. Attempt reservations are saved before
dispatch, so an uncertain network response cannot cause another immediate request.
Recovery waits an hour between actions and allows at most three generation
requests and three publication requests per date. Exhaustion stops automatic
retries and is visible in the state/report. The weekday follow-up monitor remains
the separate route for surfacing failures needing human attention.

This prevents a GitHub scheduling delay from leaving an edition unstarted while
the Mac is available. It cannot guarantee publication during outages, a failed
editorial review, or when the Mac is unavailable. A future cloud timer can use the
same decisions, but requires a separate GitHub credential restricted to this
repository and renewed Cloudflare access.
