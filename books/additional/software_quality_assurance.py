"""Original QA decision-rule, mutation-report, and accessibility conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Three conditions, not three separate promises",
        skill="Challenge incomplete test combinations using an explicit eligibility rule.",
        setup="Fictional promotion: give a $10 discount only when membership is active, basket subtotal before discount is at least $100, and the offer has not already been redeemed. Otherwise discount is zero. These three yes/no conditions have eight feasible combinations. Existing cases cover active/$120/not redeemed and inactive/$80/already redeemed. Both passed. No other combinations or threshold values have been tested.",
        cast="Zara|Test analyst\nEvan|Developer",
        dialogue="""Zara|Both promotion tests passed. One qualifies on every condition; the other fails all three. Do those results show that each restriction works independently?
Evan|Not yet. We need the [[condition combinations::The rule depends on combinations of three conditions; testing one all-qualifying and one all-disqualifying case leaves six feasible combinations unchecked.]]. The second case could reject for just one reason while the other restrictions are broken.
Zara|So if the implementation accidentally ignored membership, our inactive eighty-dollar redeemed basket would still reject because of the other conditions.
Evan|Exactly. That is [[masking::Other disqualifying conditions can hide a missing membership check; an inactive basket below the threshold and already redeemed would reject even if membership were ignored.]] in this example. Use an inactive member with one hundred twenty dollars and no redemption to expose that omission.
Zara|That isolated negative case should get zero discount. We also need active membership with ninety-nine dollars ninety-nine, and active membership with an already redeemed offer.
Evan|Those add useful [[negative cases::Each proposed negative case makes one required condition fail while the other two qualify, allowing the relevant restriction to affect the expected outcome.]]. Keep the other conditions qualifying so the restriction you're targeting can determine the outcome.
Zara|There are three yes-or-no conditions, so two times two times two gives eight combinations. Only one combination earns the ten-dollar discount.
Evan|Right. The full [[decision table::The full table records all eight feasible combinations of the three binary conditions and their expected discounts; only active, threshold-met, not-redeemed qualifies.]] makes that explicit. Two executed combinations cover two of its eight columns, not all eight.
Zara|At exactly one hundred dollars, active and not redeemed should qualify. The threshold is before discount, so the resulting ninety doesn't disqualify it afterward.
Evan|Yes. That's an [[inclusive threshold::At least one hundred includes exactly one hundred; eligibility is assessed on the pre-discount subtotal and is not recalculated from the discounted total.]]. Test that equality separately from a qualifying hundred-twenty-dollar example.
Zara|The two existing cases give twenty-five percent of the full table's combinations. That doesn't mean twenty-five percent of the software is correct.
Evan|Keep the [[coverage denominator::The denominator here is eight feasible columns of the stated full decision table; two executed columns give twenty-five percent, not a general measure of software correctness.]] visible. A percentage without its coverage items invites a much broader interpretation.
Zara|Could we minimize the table by grouping cases where a disqualifying condition already determines the outcome?
Evan|A reduced table can be useful, but then describe its rules and denominator. Don't report full eight-column execution coverage from a smaller unexecuted plan.
Zara|And adding six planned combinations doesn't mean those combinations have passed. We'll need the actual outputs against their expectations.
Evan|Correct. Keep design coverage and execution evidence separate. A complete plan can still reveal failures when run.
Zara|I'll attach the eight combinations, mark only the two executed ones passed, and add focused checks at ninety-nine ninety-nine and one hundred.
Evan|Good. Include the ten-dollar amount too; eligibility alone wouldn't catch the implementation applying the wrong discount to a qualifying basket.
Zara|The summary will say two of eight combinations exercised, equality untested, and the new combinations and threshold checks proposed.
Evan|That accurately describes the gap. We can explain why the extra cases matter without pretending the initial two passes established every part of the rule.""",
        transfer_title="Qualify before applying the discount",
        transfer_setup="Same promotion rule. All amounts are pre-discount subtotals. A: active, $100, not redeemed. B: inactive, $140, not redeemed. C: active, $100, already redeemed. D: active, $99.99, not redeemed. Expectations only; these cases have not run.",
        transfer="""Analyst: The only qualifying case is ___ .|A|A meets all three requirements; exactly one hundred satisfies the inclusive threshold.
Developer: Its expected discount is ___ dollars.|10|The rule supplies a ten-dollar discount for a qualifying basket, not ten percent.
Analyst: B fails the ___ condition.|membership|B meets the subtotal and redemption conditions but is inactive, so membership alone prevents eligibility.
Developer: The execution status of these cases is ___ .|unexecuted|The setup explicitly supplies expected outcomes without completed test runs.""",
        reference=("ISTQB Foundation Level syllabus: decision-table terminology; original promotion example", "https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf"),
    ),
    scenario(
        title="Which mutation score are we reporting?",
        skill="Read mutation-test categories and state a score with its actual numerator and denominator.",
        setup="Fictional completed Stryker-style report: 12 mutants total; 6 killed, 2 timeout, 2 survived, 1 no coverage, 1 compile error. Use these report definitions: detected = killed + timeout; valid = detected + survived + no coverage; covered = detected + survived. Overall score = detected/valid; covered-code score = detected/covered. Round percentages to one decimal place. These are deliberately modified program variants, not observed production defects.",
        cast="Nikhil|Automation engineer\nPaula|Test lead",
        dialogue="""Nikhil|The report has twelve variants and six killed. I started to write fifty percent, but the dashboard shows a different score.
Paula|Check what each [[mutant::A mutant is a deliberately modified program variant used to assess test sensitivity; the twelve variants are not twelve discovered production defects.]] status means before dividing. This report counts timeout as detected and excludes compile error from valid variants.
Nikhil|The six killed variants each caused at least one test to fail. That is the desired detection, not six failures in our original program.
Paula|Exactly. [[Killed::Killed means a test detected an active modified variant by failing; it is not the count of production defects or of failing original-program tests.]] describes the modified run. Keep it distinct from the baseline suite's result.
Nikhil|There are two timeouts. I was going to move them to survived because no assertion failure is listed.
Paula|Don't relabel them. A [[timeout::Under the supplied Stryker-style definitions, a timeout counts as detected and remains a separate status; it is not silently classified as survived or compile error.]] counts as detected under these definitions. Six plus two gives eight detected variants.
Nikhil|The one no-coverage variant is different from the two survived variants that ran without a failing test. Does it still enter the overall denominator?
Paula|Yes. [[No coverage::The no-coverage variant is undetected and included in valid variants for the overall score, but it is excluded from the covered-code denominator in this report.]] is undetected here. Excluding it would change which score you're reporting.
Nikhil|Then valid is eight detected plus two survived plus one no coverage: eleven. The compile error is outside that denominator.
Paula|Correct. Eight divided by eleven [[valid mutants::The supplied definitions give eleven valid mutants after excluding the one compile error; eight detected divided by eleven is 72.7 percent when rounded to one decimal place.]] gives seventy-two-point-seven percent. Don't divide by twelve generated variants.
Nikhil|For covered, we use eight detected plus two survived, so ten. Eight over ten is eighty percent.
Paula|That's the [[covered-code score::The covered-code score uses ten covered variants and gives eighty percent; it excludes the no-coverage variant and must not replace the overall 72.7 percent score without its label.]], not the overall score. The labels explain why both figures can be correct.
Nikhil|A colleague read eighty percent as eighty percent of the product's defects prevented. We don't have evidence for that.
Paula|No. These ratios describe this mutation set and these test runs. They aren't estimates of all real defects or a release guarantee.
Nikhil|For the survivors, should I immediately add assertions until every one is killed? Some modifications might not change observable behavior for the supported inputs.
Paula|Review them first. An equivalent variant and an inadequately tested behavior require different explanations; survival alone doesn't establish which one it is.
Nikhil|I'll also retain the timeout and compile-error details. Counting timeout as detected doesn't mean the underlying run conditions need no attention.
Paula|Right. Preserve the tool's categories and investigate the evidence as needed. Don't change a status merely to make a headline score improve.
Nikhil|My handoff will show twelve total, eleven valid, eight detected, seventy-two-point-seven overall, eighty covered, and the remaining categories.
Paula|Include the definitions with the report. That lets someone reproduce the arithmetic and understand the limits instead of comparing unlike percentages.""",
        transfer_title="Keep uncovered variants in the overall score",
        transfer_setup="New completed report using the same definitions: 10 total; 4 killed, 1 timeout, 2 survived, 2 no coverage, 1 compile error. Round percentages to one decimal place.",
        transfer="""Engineer: The detected count is ___ .|5|Four killed plus one timeout equals five detected under the supplied report definitions.
Lead: The valid count is ___ .|9|Five detected plus two survived plus two no coverage equals nine; exclude the one compile error.
Engineer: The overall score is ___ percent.|55.6|Five divided by nine times one hundred is 55.555..., rounded to 55.6 percent.
Lead: The covered-code score is ___ percent.|71.4|Covered equals five detected plus two survived, or seven; five divided by seven rounds to 71.4 percent.""",
        reference=("Stryker: mutant states and metrics, including timeout and coverage denominators", "https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/"),
    ),
    scenario(
        title="The modal is labeled, but focus is outside",
        skill="Report keyboard behavior separately from an automated accessibility scan.",
        setup="Fictional Edit Address modal. Acceptance criteria: opening moves focus inside; Tab and Shift+Tab cycle within the modal; Escape closes it; closing returns focus to the still-present Edit Address button. Tested desktop build A6: labels pass the automated scan, but opening leaves keyboard focus on the background page, Tab reaches a background link, and Escape closes without restoring focus. Screen-reader behavior has not been tested.",
        cast="Leah|Accessibility tester\nOmar|Frontend developer",
        dialogue="""Leah|The label scan passes, but I can't complete the keyboard acceptance check. Opening Edit Address leaves focus on the page behind the modal.
Omar|Then the [[initial focus::The supplied opening criterion requires focus to move inside the modal; leaving it on the background page fails that behavior even when labels pass a scan.]] behavior is wrong for our criterion. A visible overlay doesn't tell us where keyboard input goes.
Leah|When I press Tab, a background link receives focus. The modal is still on screen, so the visual state and keyboard path disagree.
Omar|That breaks the required [[focus containment::The case requires forward and reverse tab navigation to stay within the open modal; moving focus to a background link violates that containment.]]. We need to test the forward and reverse cycle inside, not just whether the first button can be clicked.
Leah|I haven't completed a reverse-cycle check yet. I'll record that as pending rather than infer its result from the forward failure.
Omar|Good. Keep the [[keyboard sequence::The recorded keyboard sequence identifies the exact actions and focus targets observed; unperformed Shift+Tab checks must remain pending rather than inherit a result.]] and actual focus targets in the report. That gives me a reproducible behavior to inspect.
Leah|Escape closes the overlay, but focus doesn't return to the Edit Address button. The button is still present and our criterion names it.
Omar|Then [[focus restoration::For this case, the invoking Edit Address button still exists and is the explicitly required return target; closing the overlay without returning focus does not satisfy that criterion.]] also needs correction. Closing visually is only one part of that interaction.
Leah|Someone suggested adding aria-modal true. Does the attribute itself trap keyboard focus or choose the return target?
Omar|No. The [[modal semantics::Modal semantics describe the intended interface meaning; an accessibility attribute alone does not implement keyboard containment, initial focus, or focus restoration.]] must match implemented behavior. An attribute doesn't do all the focus management for us.
Leah|I'll retain the passing label result, but not mark the whole dialog accessible. We haven't tested it with a screen reader.
Omar|Exactly. The [[automated scan::The automated scan supplies the stated label result only; it does not replace the observed keyboard checks or establish untested screen-reader behavior.]] and manual results belong together with their boundaries, not as competing claims that one erases the other.
Leah|For the defect steps, I'll identify build A6, open from the button using the keyboard, then record where focus lands and where Tab takes it.
Omar|Include the browser and operating-system versions you actually used when attaching the run record. Don't fill those fields with guesses.
Leah|After a fix, I'll check both directions across the first and last tabbable controls, then Escape and the return target.
Omar|Yes. That's the proposed verification sequence. We shouldn't say it passed until those actions have actually been checked on the revised build.
Leah|And the starting control inside the dialog should follow our design decision. The general pattern doesn't require every dialog to focus the same type of element.
Omar|Correct. Content and workflow can affect the appropriate initial target. Here, our supplied criterion requires an inside target, not a guessed universal first field.
Leah|The handoff is labels passed; opening, forward containment, and restoration failed; reverse cycling pending; screen-reader checks not performed.
Omar|That is actionable. It preserves what works, what failed, and what still needs evidence without turning one automated result into a blanket approval.""",
        transfer_title="A visible close is only part of the check",
        transfer_setup="New fictional modal: opening moves focus inside; forward Tab cycles inside; Shift+Tab has not been checked. Escape closes it, but focus remains on the page body instead of the still-present invoking button required by its criterion. Labels passed an automated scan. Screen-reader behavior is untested.",
        transfer="""Tester: Forward containment has ___ .|passed|The supplied forward Tab observation meets the stated inside-cycle requirement.
Developer: Reverse cycling remains ___ .|unchecked|No Shift+Tab result is supplied, so forward success cannot establish reverse behavior.
Tester: Focus restoration has ___ .|failed|The criterion requires return to the invoking button, but the observed target is the page body.
Developer: Screen-reader behavior is ___ .|untested|The setup explicitly says no screen-reader check was performed; the label scan is not that evidence.""",
        reference=("W3C ARIA Authoring Practices: modal dialog keyboard interaction and focus", "https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"),
    ),
]
