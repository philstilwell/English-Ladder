# Recovery guidance

Read only the section relevant to the current failure. Work on the date
printed by the schedule gate, with the same checkout and producer lock.

## Lesson review

Look at `.daily-agent/DATE/issues-LEVEL.json` and the last corresponding
`review-result-LEVEL-*.json`. Save a concise diagnosis and the runner log for
the next attempt. Capacity or connection failures are not editorial failures;
resume the saved draft at review when possible. Never substitute a model or
increase the three-attempt bound. After the final scheduled attempt the
separate Mac monitor can record `needs_attention`; it does not generate.

- **Quiz only:** The runner can replace just the quiz when the reviewer names
  only `quiz`, the saved draft and feedback hashes both match, and no other
  validation or level check calls for a broader change. The reading and other
  sections stay locked. The existing isolated mechanical and grammar-only
  repairs still apply. Every repair gets full validation and a fresh independent
  whole-lesson review.
- **Reading and dependent quiz:** Use the runner's complete revision by default.
  If the user requests a manual retry and the reviewer supplies a precise,
  source-supported correction to a still-unapproved draft, it can be safer to
  apply that correction directly before resuming. Preserve anything outside the
  explicit issue. For example, retain “whatever the court decided” when the
  source makes that qualification; update a quiz item that repeats the sentence.
  A reading quiz must be answerable from the lesson, and its explanations must
  not introduce details available only in the source excerpt.
- **Ambiguous or conflicting feedback:** Do not hand-edit based on guesswork.
  Use the bounded producer with the retained evidence and feedback, or report
  the specific issue if it cannot be resolved.

For the narrow manual path, acquire `plan_daily_runner.producer_lock` on
`.daily-agent/DATE/producer.lock` without waiting. If held, stop. Under the lock,
require no publication handoff, staged archive for that date, or approval for
the level. Verify that `repair-scope-LEVEL.json` matches the exact draft and
issues (use `plan_daily.draft_digest`), and that the saved review agrees with
the scope. Back up the draft, review and feedback in the ignored state
directory. Run `validate_plan_lesson` and `validate_evidence` on the candidate
before writing it with `plan_daily.atomic_json`. Use `plan_daily.prepare_review`
to recheck the draft and remove resolved feedback, so the runner resumes at
independent review. Restore the backup on an error. Release the lock and run
the normal producer once; it reacquires the lock and honors any competing
owner. Never write an approval or patch an archived or published lesson.

## Usage or capacity

Use the account's current usage view to distinguish unavailable included
allowance, usable existing credits, and a provider capacity error. Exhausted
included allowance alone is not a blocker. If credits are needed, estimate
from retained sessions and the [current standard credit rates](https://learn.chatgpt.com/docs/pricing#token-rates).
Distinguish producer sessions from this supervising chat. If token type or
image usage is unavailable, say what the estimate excludes (typically one
built-in image, any revisions, or orchestration). A before/after credit balance
is account-wide and can include concurrent activity. Existing credits consumed
and new purchases are different; report them separately.

## Hosting after push

The site can serve stale lesson data or a 404 for several minutes after a
successful push. Check the deployment status, then repeat the public verifier
at short intervals within a bounded wait. A deployment failure or timeout is a
publication blocker: report the pushed commit, deployment link and failing
public check. Keep the handoff so a later verified owner can resume. GitHub's
offline workflow status is useful context; the public site and interactive
checks decide whether the handoff can be cleared.
