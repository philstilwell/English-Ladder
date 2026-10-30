# Recovering interrupted daily publication

The October 30, 2026 edition exposed a gap between successful generation and
publication. The first scheduled chat completed all lessons, independent reviews,
seven-language definitions, the illustration, and offline checks. The desktop
app then reported `Selected model is at capacity` for that chat before it could
commit. Its persistent publication marker remained. Both later scheduled chats
obeyed the former unconditional `publication_pending` exit instruction, so
neither finished the already validated edition.

The marker must survive an interruption, but its existence does not establish
that its original owner is still working. New markers therefore record the
owning `CODEX_THREAD_ID`. The producer reports that identity when publication is
pending. The existing scheduled skill uses the supported app `read_thread` tool
to distinguish an active owner from a stopped one. It does not use marker age or
the absence of a short-lived runner process as evidence of abandonment.

If the app confirms the owner has failed or ended its turn and is idle, and its
last commands/tools have also ended, the next existing opportunity uses:

```sh
.venv/bin/python plan_daily_runner.py --date YYYY-MM-DD --resume-publication-from STOPPED_THREAD_ID
```

The command takes the normal producer lock, compares the expected owner with
the marker, checks the edition date and archive checksum, and validates saved
completeness. It atomically transfers ownership to the current chat and records
the transfer history. It returns `ready_to_publish` without generation or page
rebuilding. If two recovery chats race, only the first matching claim succeeds;
the other sees a changed owner and must stop.

The caller then follows the normal inspection, validation, commit, push, and
public-domain verification steps. Already committed output needs publication
verification rather than another content commit. The marker is removed only by
`--finish-publication` after its independent live check succeeds.

Active or waiting owners are left alone. Unavailable or ambiguous app status,
missing owner identity, a changed checksum, incomplete content, or a held process
lock prevents takeover. A legacy marker without identity requires explicit
manual recovery; the October 30 legacy marker was recovered under the user's
direct instruction. The command deliberately relies on the scheduled skill to
obtain the app's stopped-owner evidence; it cannot determine chat status from
local process metadata.

This repairs the permanent publication blockage after an interrupted chat. It
does not prevent service-capacity failures. The sole producer, three local
schedule opportunities, model, approval reviews, audio, and live verification
requirements remain unchanged.
