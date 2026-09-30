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

Hidden draft files preserve a successful paid draft awaiting review. Hidden usage
files retain per-request spending estimates, including conservative reservations
for requests with unknown usage. They are committed for reliable retries and
excluded from the public deployment. No credentials or student data are stored.

Offline coverage: `python3 vocabulary_translations.py --all --check`.
Paid initial fill: `python3 vocabulary_translations.py --all --budget 10 --budget-key initial-backfill`.
The initial budget is cumulative across retries with that key. Scheduled runs use
a cumulative $0.30 daily cap and check the latest three editions for missing work.
The separate editing call checks every translation and can correct it. It is an
automated language review, not a claim of professional human certification.

When a language is added, existing reviewed definitions and their review history
are preserved. Only missing languages are translated and separately reviewed.
Available reviewed languages remain usable while an addition is incomplete;
the coverage check requires every supported language.

For a language addition, the manual **Translate Everyday English explanations**
workflow can also fill this entire archive with `include_vocabulary=true` under
a $5 cap. Choose a descriptive `budget_key` and reuse it for every retry. It saves
progress to the branch on which it was started; rebuild and check the pages before
publishing the completed addition. Its separate Everyday English cap is $2, so
the combined maximum is $7 for that key. These are cumulative cost estimates,
including conservative reservations when provider usage is unknown.
