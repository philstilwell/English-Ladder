# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 7-day archive. Every daily run uses the same news story, but the lesson difficulty and page theme change for the target learner.

## Site Structure

- `index.html`
  The hub page. Learners choose Beginner, Intermediate, or Advanced from the level selector and can jump into the study library.

- `tools.html`
  A static ESL tools page with diagnostics, sentence repair, pronunciation shadowing, news-skill prompts, workplace phrase coaching, and register practice.

- `beginner.html`
  The yellow beginner archive page for A1-A2 learners.

- `intermediate.html`
  The blue intermediate archive page for B1-B2 learners.

- `advanced.html`
  The green advanced archive page for C1-higher learners.

- `styles.css`
  Shared styling for the hub and all lesson pages.

- `app.js`
  Shared quiz interaction for every lesson page.

- `tools.js`
  Client-side behavior for the ESL study tools.

- `archive/lessons/YYYY-MM-DD.json`
  Durable JSON archive files for each generated daily lesson set. Each file stores the source news item, release metadata, model name, and the validated structured lesson data for Beginner, Intermediate, and Advanced.

## Automation

- `.github/workflows/cron.yml`
  Runs the daily automation at `10:00 UTC`, with no-op fallback attempts at `13:00 UTC` and `16:00 UTC` in case GitHub does not assign a hosted runner. It supports manual runs with `workflow_dispatch`, installs pinned dependencies, and runs the test suite before publishing lesson updates.

- `update_site.py`
  Fetches the top BBC World News RSS item over HTTPS, requests structured JSON lesson data from Gemini, renders the HTML locally, sanitizes existing lesson markup, and updates the three rolling archive pages.

- `requirements.txt`
  Pins the runtime dependencies used by GitHub Actions.

- `tests/test_update_site.py`
  Covers lesson validation, summary parsing, duplicate-day replacement, and legacy markup cleanup.

## How the Daily Update Works

1. GitHub Actions starts the workflow.
2. `update_site.py` fetches the latest BBC World News headline and summary.
3. Gemini creates:
   - one beginner lesson
   - one intermediate lesson
   - one advanced lesson
4. The script validates the JSON lesson data, renders safe HTML from fixed templates, and replaces any same-day lesson instead of creating duplicates.
5. The validated structured lesson data for all three levels is written to `archive/lessons/YYYY-MM-DD.json`.
6. Older lessons beyond the newest 7 are removed from the live lesson pages automatically.
7. GitHub Actions commits the updated lesson pages and JSON archive files back to the repository.

Scheduled fallback runs use `--skip-existing`, so if the primary run already created that date's JSON archive, the fallback exits before calling Gemini and only continues through the live Pages verification.

## Local Run

Set your Gemini API key, then run:

```bash
python3 update_site.py
```

This updates:

- `beginner.html`
- `intermediate.html`
- `advanced.html`
- `archive/lessons/YYYY-MM-DD.json`

To normalize existing lesson markup without calling Gemini:

```bash
python3 update_site.py --refresh-pages
```

## Deployment Notes

- `CNAME`
  Points the site to `englishladder.com`.

The hub page remains the root entry point, and the three lesson pages stay linked from there.
