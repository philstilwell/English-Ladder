# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 7-day archive. Every daily run uses the same news story, but the lesson difficulty and page theme change for the target learner.

## Site Structure

- `index.html`
  The hub page. Learners choose Beginner, Intermediate, or Advanced from the level selector.

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

## Automation

- `.github/workflows/cron.yml`
  Runs the daily automation at `10:00 UTC`, supports manual runs with `workflow_dispatch`, installs pinned dependencies, and runs the test suite before publishing lesson updates.

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
5. Older lessons beyond the newest 7 are removed automatically.
6. GitHub Actions commits the updated lesson pages back to the repository.

## Local Run

Set your Gemini API key, then run:

```bash
python3 update_site.py
```

This updates:

- `beginner.html`
- `intermediate.html`
- `advanced.html`

To normalize existing lesson markup without calling Gemini:

```bash
python3 update_site.py --refresh-pages
```

## Deployment Notes

- `CNAME`
  Points the site to `englishladder.com`.

The hub page remains the root entry point, and the three lesson pages stay linked from there.
