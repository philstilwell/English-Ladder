# Vocabulary definition translations

Generated and separately edited definitions in Japanese (`ja`), Korean (`ko`),
Simplified Chinese (`zh-Hans`), Spanish (`es`), and Brazilian Portuguese (`pt-BR`).
`vocabulary_translations.py` stores one reviewed record per lesson context hash.
The hash includes vocabulary, reading, level and translation policy. Changing any
of them invalidates the old translations; missing or invalid records use English.
Page builds read these records without contacting an AI service.

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
