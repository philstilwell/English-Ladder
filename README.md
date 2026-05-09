# English Ladder

English Ladder is a self-updating ESL website that publishes a daily news lesson at three difficulty levels:

- Beginner: CEFR A1-A2
- Intermediate: CEFR B1-B2
- Advanced: CEFR C1-Higher

Each level keeps a rolling 7-day archive. Every daily run uses the same news story, but the lesson difficulty and page theme change for the target learner.

## Site Structure

- `index.html`
  The hub page. Learners choose Beginner, Intermediate, or Advanced from a red, white, and blue level selector.

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
  Runs the daily automation at `10:00 UTC` and supports manual runs with `workflow_dispatch`.

- `update_site.py`
  Fetches the top BBC World News RSS item, sends it to Gemini, generates three CEFR-specific HTML lessons, and updates the three rolling archive pages.

## How the Daily Update Works

1. GitHub Actions starts the workflow.
2. `update_site.py` fetches the latest BBC World News headline and summary.
3. Gemini creates:
   - one beginner lesson
   - one intermediate lesson
   - one advanced lesson
4. The script inserts each lesson at the top of its matching page.
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

## Deployment Notes

- `CNAME`
  Points the site to `englishladder.com`.

The hub page remains the root entry point, and the three lesson pages stay linked from there.
