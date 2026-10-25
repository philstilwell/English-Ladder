# Vocabulary definition translations

Generated and separately edited definitions in Japanese (`ja`), Korean (`ko`),
Simplified Chinese (`zh-Hans`), Spanish (`es`), Brazilian Portuguese (`pt-BR`),
French (`fr`), and German (`de`).
`vocabulary_translations.py` stores one reviewed record per lesson context hash.
The hash includes vocabulary, reading, level and translation policy. Changing any
of them invalidates the old translations; missing or invalid records use English.
Page builds read these records without contacting an AI service. The reviewed
definitions are embedded in the lesson HTML; this entire working directory is
excluded from the public asset package. Student browsers never request these
records separately.

Historical hidden draft and usage files record earlier provider attempts. They
remain excluded from the public deployment and are not used by the plan-based
daily producer. No credentials or student data are stored.

Offline coverage: `python3 vocabulary_translations.py --all --check`. The daily
producer uses `python3 plan_daily_runner.py --date YYYY-MM-DD`; it fills missing
definitions for the latest three editions with a ChatGPT-plan translation session
and a separate editing session. No paid-API fallback is permitted. The automated
language review is not a claim of professional human certification.

When a language is added, existing reviewed definitions and their review history
are preserved. Only missing languages are translated and separately reviewed.
Available reviewed languages remain usable while an addition is incomplete;
the coverage check requires every supported language.

For a language addition or archive repair, extend the plan producer's requested
language set, run separate translation and review sessions, then rebuild and audit
the pages before publishing. The separate Everyday English workflow does not fill
daily-news vocabulary records.
