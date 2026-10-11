"""Original Software Quality Assurance and Testing English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='software-quality-assurance', title='Software Quality Assurance and Testing English',
    cover_label='ENGLISH FOR QUALITY ASSURANCE AND SOFTWARE TESTING',
    cover_title='Software Quality\n& Testing', cover_size=33,
    tagline='Clear findings. Useful next checks.',
    audience='For software testers, quality analysts, automation engineers, and test leads discussing requirements, defects, coverage, and release evidence.',
    map_intro='Eight testing conversations build precise reporting and productive challenge: expected results, reproduction, boundary cases, change risk, inconsistent automation, triage, exploratory findings, and release handovers.',
    notes_title='A result is only as clear as its boundary.',
    notes_intro='A passing test does not cover an untested path. A blocked check is not a pass. An unexpected behavior may expose a missing requirement rather than a confirmed violation. Good testing English keeps those distinctions visible.',
    field_notes=[
        ('Agree what correct means', 'Conflicting examples cannot both define the same expected result. Name the exact equality case and ask the requirement owner to resolve it. Do not allow a test script to silently become the product rule.', '"One example accepts exactly twenty-four hours and another rejects it. Which result is intended?"'),
        ('Report the conditions with the result', 'Include the build, saved input, action, actual output, and observed frequency. A successful attempt using different input does not refute a failure under the reported conditions. Keep the scope of the evidence explicit.', '"On Q12, this three-item selection omitted the last item in both attempts."'),
        ('Keep impact and timing separate', 'A visible error may deserve urgent attention before a demonstration, while a less frequent data defect has a different functional impact. Explain both dimensions without inventing a severity rating, priority decision, or release approval.', '"The typo affects every account page; the export defect loses a row in the monthly workflow."'),
        ('Distinguish untested from successful', 'A release summary should show passes, failures, blocked checks, unresolved criteria, and decision ownership. Percentages can conceal an unexecuted critical path. A report supports the release decision; it does not replace the authorized decision maker.', '"Seven passed, one failed, and two are blocked; one blocked check is critical."'),
    ],
    scope_note='All products, builds, requirements, observations, and decisions are fictional. This book teaches workplace English, not certification content or a complete testing method. Actual requirements, test policies, evidence standards, privacy safeguards, and release authority take precedence. The exercises authorize no live-system changes. A proposed check has no result until executed, and an observed result applies only to its stated conditions.',
    sources=[
        dict(title='International Software Testing Qualifications Board. Foundation Level Syllabus v4.0.1.',
             url='https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf',
             note='Terminology reference for boundaries, exploratory sessions, and reporting. Copyright in the syllabus belongs to its authors and ISTQB; these cases are original.', checked='10 October 2026'),
        dict(title='pytest Documentation. Flaky Tests.',
             url='https://docs.pytest.org/en/stable/explanation/flaky.html',
             note='Background on shared state and order-dependent results. The fictional cleanup and search scenario does not prescribe a particular framework.', checked='10 October 2026'),
        dict(title='MDN Web Docs. When and How to File Bugs with Browsers.',
             url='https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/File_browser_bugs',
             note='Context for reproducible examples, versions, and expected versus actual results. No source code examples are reproduced.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Agreeing the expected result',
    scene='Exactly twenty-four hours: accept or reject?',
    skill='Expose contradictory examples and obtain a clear equality rule without inventing a missing requirement.',
    brief='A fictional booking requirement says cancellation is allowed within 24 hours. One example permits cancellation exactly 24 hours before the event; another rejects it. Tester Maya and requirement owner Dev review the conflict. The equality case has not been settled. Time-zone handling is outside this discussion. Maya needs an agreed expected result before using a test to declare this exact boundary behavior correct or defective.',
    cast='Maya | Tester\nDev | Requirement owner',
    culture=('A precise question is not obstruction', 'When a phrase supports different readings, identify the exact case rather than asking whether the entire requirement is clear. Two contradictory examples provide a concrete reason to seek a decision. Keep your own preferred interpretation separate from the agreed rule.'),
    a='''Which case is contradictory? | Cancellation exactly 24 hours before the event | Every cancellation more than a week ahead | Only time-zone conversion | Every completed booking | The two supplied examples disagree specifically at exactly twenty-four hours.
Who can clarify the intended rule? | The requirement owner | The test result alone | An unrelated customer | The test framework | The scenario gives the requirement owner authority to clarify the equality case.
What is outside this discussion? | Time-zone handling | The equality case | The contradictory examples | The expected cancellation result | Time-zone handling is explicitly excluded from this exercise's scope.''',
    vocabulary='''requirement | Statement of behavior or capability the product should provide. | clarify the requirement
expected result | Outcome a test should produce under the agreed rule. | agree the expected result
actual result | Outcome observed when the test is executed. | record the actual result
acceptance criterion | Condition used to judge whether a requirement is met. | refine the acceptance criterion
ambiguity | Wording that permits more than one interpretation. | resolve an ambiguity
contradiction | Two statements that cannot both hold for the same case. | identify a contradiction
boundary | Point where an applicable rule or outcome changes. | test the boundary
equality case | Input exactly equal to the specified threshold. | clarify the equality case
inclusive limit | Limit that includes the endpoint itself. | specify an inclusive limit
exclusive limit | Limit that excludes the endpoint itself. | distinguish an exclusive limit
threshold | Value at which a rule changes or applies. | name the threshold
test oracle | Reference used to decide the expected outcome. | establish the test oracle
test basis | Information from which tests and expectations are derived. | review the test basis
Boolean condition | Condition with a true or false value. | combine Boolean conditions
business rule | Product behavior specified for a business purpose. | confirm the business rule
requirement owner | Person responsible for clarifying the relevant requirement. | consult the requirement owner
decision record | Traceable statement of an agreed decision. | preserve the decision record
assumption | Belief used without current confirmation. | label an assumption
precondition | State required before a test action is performed. | state the precondition
postcondition | State expected after the relevant action. | define the postcondition
traceability | Ability to link a test or result to its supporting requirement. | maintain traceability
scope boundary | Limit on topics or behavior covered by the work. | respect the scope boundary
pass/fail judgment | Conclusion comparing observed behavior with an agreed expectation. | defer the pass/fail judgment
clarification request | Specific question seeking missing or inconsistent information. | raise a clarification request''',
    precision='The exact twenty-four-hour case has two conflicting expected outcomes. Neither the word within nor the current implementation resolves that conflict by itself. Request an explicit accept-or-reject decision for equality.',
    precision_extra='Do not confuse a requirement decision with an observed result. The owner defines intended behavior; testing then compares behavior with that rule. Leave time-zone handling outside this focused discussion rather than inventing a policy.',
    phrases='''Locate the ambiguity | The two examples disagree at exactly twenty-four hours.
Name the first outcome | One example allows the cancellation.
Name the second outcome | The other rejects the same case.
Ask the precise question | Should equality be accepted or rejected?
Separate preference | My interpretation is not yet an agreed rule.
Request authority | Can the requirement owner clarify this point?
Avoid an implementation shortcut | Current behavior does not settle intended behavior.
Request a usable expectation | We need one expected result for this input.
Name the boundary | I am asking about the endpoint itself.
Keep scope focused | Time-zone handling is outside this discussion.
Request alignment | Please update the conflicting example after the decision.
Preserve traceability | Link the test to the clarified requirement.
Defer judgment | I cannot make a justified pass/fail judgment on this case yet.
Avoid premature agreement | The equality rule remains unresolved.
Confirm the decision status | This is a clarification request, not a chosen outcome.
Close with the next step | Record the intended result before finalizing the test expectation.''',
    notes='''Exactly | Focuses the question on equality rather than a nearby value.
The same case | Makes the contradiction explicit.
Should ... or | Requests a choice without choosing on the owner's behalf.
Not yet | Preserves the unresolved status of an interpretation.
By itself | Limits what an ambiguous phrase or implementation can establish.
After the decision | Keeps the sequence of clarification and test update clear.''',
    d='''Which question isolates the unresolved rule? | At exactly 24 hours before the event, should cancellation be accepted or rejected? | Did cancellation work at 23 hours? | Does the current build reject at 24 hours? | Which time zone does the event use? | Only the equality question asks for the intended outcome at the conflicting endpoint; observed behavior and excluded time zones do not settle it.
What should serve as the test expectation? | The explicitly clarified requirement | The tester's unrecorded preference | Whatever the code currently does | A different product's behavior | A justified expectation must follow the agreed rule rather than an unsupported assumption.
Which status is accurate now? | Equality remains unresolved | Equality is confirmed accepted | Equality is confirmed rejected | Time zones have been fully tested | No owner decision has resolved the contradictory equality examples yet.
What should follow clarification? | Align the examples and link the test to the decision | Keep contradictory examples as equal authorities | Erase all requirement history | Claim every cancellation case passed | Updating conflicting examples and preserving the decision supports consistent test expectations.''',
    dialogue='''Maya | Before I finalize the cancellation test, can we resolve the two examples for exactly twenty-four hours before the event? One accepts it; one rejects it.
Dev | Show me the [[equality case::Equality case is the input exactly twenty-four hours before the event, where the examples disagree.]] you are comparing. I want to separate that exact endpoint from any other timing question before we decide what the rule should mean.
Maya | They describe the same endpoint, not nearby times. I can't give the test two incompatible expected outcomes for the same condition.
Dev | That is a real [[contradiction::Contradiction identifies the incompatible accept and reject outcomes assigned to the same input.]], not merely a difference in wording. We need to resolve the intended outcome rather than ask you to choose whichever example matches the implementation.
Maya | My first reading included the endpoint, but I haven't treated that as an approved product rule. I need the owner's decision.
Dev | Good. Label it an [[assumption::Assumption marks Maya's preferred interpretation as unconfirmed rather than an agreed cancellation rule.]] until the requirement decision is explicit. Your reading may be reasonable, but it is not enough to declare the product correct or defective.
Maya | The precise question is accept or reject at exactly twenty-four hours. I want to leave time-zone conversion outside this particular clarification.
Dev | That keeps the [[scope boundary::Scope boundary excludes time-zone handling and keeps the discussion focused on the conflicting endpoint rule.]] clear. We should not introduce a separate timing policy into this discussion and then mistake that for resolving the original conflict.
Maya | Could I copy what the application currently does into the expected result? It would finish the script, but wouldn't show whether the behavior is intended.
Dev | That would not establish the [[test oracle::Test oracle is the reference for correct behavior and cannot be established merely by copying the current implementation.]]. We need the intended rule first, otherwise the test can repeat an existing mistake and still appear to pass.
Maya | Once the outcome is agreed, I'll record it and correct the conflicting example. A note saying clarified without the actual rule won't be enough.
Dev | Yes. The [[decision record::Decision record preserves the owner's clarified outcome so examples and tests can consistently refer to it.]] should state the endpoint behavior explicitly. A vague note saying clarified would leave the same interpretation problem for the next tester.
Maya | I'll hold off calling the boundary inclusive. That describes one possible decision, and the other example currently says the opposite.
Dev | Exactly. An [[inclusive limit::Inclusive limit would include the endpoint, but that interpretation has not yet been selected for this requirement.]] is one possible decision, not a fact we have already agreed. Keep the options separate from the final rule.
Maya | I can attach the two examples and the one equality question. That should give the owner a focused decision instead of a vague requirement complaint.
Dev | That is a useful [[clarification request::Clarification request asks for the missing authoritative outcome while retaining the evidence of the conflicting examples.]]. It gives the requirement owner a concrete choice and shows why testing cannot make a justified judgment yet.
Maya | I'll link the updated expectation to that decision. Silently changing an example would hide why we chose the new outcome.
Dev | Preserve that [[traceability::Traceability links the updated test and examples to the requirement decision that justifies their expectation.]]. Anyone reviewing the result should be able to see which rule was applied and why it replaced the conflicting interpretation.
Maya | For now: equality unresolved, expected result pending, time zones outside this discussion. I haven't selected accept or reject.
Dev | That is accurate. Defer the [[pass/fail judgment::Pass/fail judgment requires an agreed expected outcome, which the unresolved equality case does not yet provide.]] for this case until the intended outcome is recorded. The next step is a requirement decision, not an invented test result.''',
    rehearsal=["Read the two conflicting examples and the single equality question aloud. Do not choose an outcome that the case leaves unresolved.","Swap roles for turns 9-16, stressing intended rule rather than current application behavior.","Repeat the closing status and compare it with the brief: equality unresolved and time zones outside this discussion."],
    transfer_title='Ask one answerable requirement question',
    transfer_setup='Complete the clarification exchange without choosing the unresolved cancellation outcome.',
    transfer='''Tester: "The examples conflict at exactly ___ hours." | 24 | Both examples concern the exact twenty-four-hour boundary before the event.
Owner: "The equality case remains ___." | unresolved | No decision has selected acceptance or rejection for that exact case.
Tester: "The test needs an agreed expected ___." | result | A test judgment requires an authoritative expected result for the input.
Owner: "Time-zone handling is outside this ___." | discussion | The scenario explicitly excludes time-zone handling from this focused clarification.''',
))


BOOK['units'].append(unit(
    title='Making a failure reproducible',
    scene='Three selected, two exported, twice',
    skill='Give a reproducible defect report and explain why a successful attempt with different input does not disprove it.',
    brief='On fictional build Q12, tester Hana exports a saved selection of three items. The output omits the last selected item. She observes the omission in two attempts out of two. Developer Joel exports one item successfully. No other build or selection size has been checked. They compare conditions and prepare a handoff using the saved three-item selection, the export action, and the observed output without claiming every export fails.',
    cast='Hana | Tester reporting the omission\nJoel | Developer investigating the report',
    culture=('Different results may come from different conditions', 'Cannot reproduce can sound like dismissal if the input is not compared. State the successful attempt accurately, then ask for the reported fixture. A bounded reproduction frequency is more useful than always or sometimes without a denominator.'),
    a='''Which build did Hana test? | Q12 | Q20 | Every release | An unspecified previous build | The reported omission was observed specifically on build Q12.
What did Joel successfully export? | One item | The same saved three-item selection | Every selection size | The omitted item in every build | Joel's successful attempt used one item rather than Hana's three-item selection.
What frequency is established? | Two omissions in two attempts with the saved selection | Every export always fails | One failure in ten attempts | No repeatable omission | Hana observed the same omission in both of her two stated attempts.''',
    vocabulary='''defect report | Record describing a suspected or confirmed product problem. | submit a defect report
build identifier | Label identifying the software version under test. | include the build identifier
reproduction steps | Ordered actions used to observe a reported problem. | follow the reproduction steps
saved selection | Retained set of items used as input. | reuse the saved selection
test fixture | Prepared data or state for a test. | share the test fixture
actual output | Data or behavior produced by the executed operation. | attach the actual output
expected output | Data or behavior required for the test to pass. | state the expected output
omission | Absence of something that should be included. | report the final-item omission
selection size | Number of items included in the chosen input. | compare selection size
reproduction frequency | Observed failures relative to stated attempts and conditions. | report reproduction frequency
denominator | Total count against which a proportion is measured. | state the denominator
environment detail | Relevant setting or configuration for an observation. | preserve environment details
mutation testing | Checking test sensitivity using deliberately modified program variants. | interpret mutation testing results
evidence bundle | Group of supporting records for an investigation. | prepare an evidence bundle
equivalent mutant | Modified variant with the same observable behavior for the relevant domain. | investigate an equivalent mutant
log excerpt | Relevant portion of recorded system events. | include a log excerpt
minimal reproduction | Smallest useful example retaining the observed problem. | seek a minimal reproduction
counterexample | Example contradicting a universal claim under its relevant terms. | assess a counterexample
scope of evidence | Range of conditions actually supported by observations. | limit the scope of evidence
unverified condition | Condition whose behavior has not been checked. | identify an unverified condition
reproduction run | Repeat intended to check the reported behavior. | perform a reproduction run
input parity | Use of matching input in a comparison. | establish input parity
cannot reproduce | Status indicating failure to observe the report under stated attempts. | qualify cannot reproduce
handoff note | Concise record transferring evidence and next steps. | prepare the handoff note''',
    precision="Two out of two describes Hana's observed attempts with the saved three-item selection on Q12. It is not a universal failure rate for every input, every session, or every build.",
    precision_extra="Joel's one-item success is compatible with Hana's report because the input differs. Reuse the saved selection before deciding whether the original failure can be reproduced. Do not invent results for untested selection sizes.",
    phrases='''Identify the build | I observed this on Q12.
Identify the input | I used the saved selection of three items.
State the action | I exported that selection.
State the omission | The last selected item is missing from the output.
Report frequency | It occurred in two attempts out of two.
Limit the claim | I have not tested other builds.
Acknowledge the comparison | Your one-item attempt succeeded.
Explain the difference | That uses a different selection size.
Request matching input | Please use the same saved selection.
Avoid dismissal | The one-item result does not disprove this report.
Request evidence | I will attach the selection and actual output.
Keep steps repeatable | Follow the recorded action sequence.
Name an unknown | Other selection sizes remain unchecked.
Avoid overgeneralizing | I am not claiming that every export fails.
Request confirmation | Report the result with the same input and build.
Close the handoff | The report includes the conditions, omission, and observed frequency.''',
    notes='''Out of | Supplies the denominator for the observed frequency.
On Q12 | Restricts the observation to the named build.
The same | Requests matched input rather than a vaguely similar attempt.
Does not disprove | Explains why a different successful case can coexist with the report.
Have not tested | Keeps an evidence gap explicit.
Not claiming every | Corrects an overgeneralization without weakening the actual observation.''',
    d='''Which title best preserves the evidence? | Q12 export omits last item from saved three-item selection, observed twice | All exports always lose data | Export fails on every build | One-item exports are broken | The title includes the build, input, behavior, and bounded observed frequency.
Why does Joel's result not refute Hana's? | The selection size differs | Successful tests never matter | Q12 cannot export anything | Hana tested every possible input | A one-item input does not reproduce the reported three-item conditions.
Which next attempt is most directly relevant? | Use Q12 and the same saved three-item selection | Use an unrelated build and ten new items | Change all settings at once | Repeat only the one-item test | Matching the reported build and input directly checks the existing reproduction.
Which claim is unsupported? | Every selection size is affected | The last item was omitted twice | Joel's one-item attempt succeeded | Other builds are unchecked | No selection sizes beyond the stated one-item and three-item cases have been checked.''',
    dialogue='''Hana | Q12 exported only two of my three selected items. The last selected item is missing, and I got the same omission in both attempts.
Joel | My one-item export worked, so I marked it [[cannot reproduce::Cannot reproduce must be qualified by Joel's different one-item attempt rather than treated as refutation of Hana's conditions.]]. I should qualify that: I didn't use your three-item selection.
Hana | Exactly. I'm reporting this saved selection on Q12, not claiming that every export fails. Other builds and sizes haven't been checked.
Joel | Let's establish [[input parity::Input parity requires using the same saved three-item selection instead of comparing it with a different one-item input.]]. Send the saved selection so I can repeat your input, not just pick three different items.
Hana | I'll attach the output alongside it. The export isn't empty; comparing selected and exported items shows which one disappeared.
Joel | That distinguishes the [[actual output::Actual output is the produced export, which demonstrates the specific missing final item rather than a total export failure.]] from a total failure. We need the precise omission, not just export broken.
Hana | For frequency, I'm writing two out of two attempts. Always would make it sound as though I'd tested a much larger set.
Joel | Include the [[denominator::Denominator is the two total attempts supporting the observed two-out-of-two frequency, not an unlimited set of exports.]] with the conditions. Two repeats support your report, but not a failure rate across every possible export.
Hana | The second attempt used the same build and selection and lost the same final item. I haven't changed any code or checked a fix.
Joel | Call that a [[reproduction run::Reproduction run describes the repeated attempt under the reported conditions, while leaving broader behavior untested.]] of the failure. It is not confirmation testing of a repaired version, because no repair has been tested.
Hana | I suspect a loop boundary, but I don't have internal evidence. Should I leave that theory out of the title?
Joel | Yes. A useful [[defect report::Defect report can document reproducible behavior and conditions without inventing an internal explanation for the omission.]] doesn't require guessing the cause. Keep the observed behavior in the title and any hypothesis explicitly provisional.
Hana | I'll put Q12 first, then the saved input, export action, and item comparison. That should make the starting conditions clear.
Joel | Good. The [[build identifier::Build identifier Q12 ties the observation to the tested software version and prevents assumptions about untested builds.]] matters. A result from another version belongs in the record with that difference, not as an identical repeat.
Hana | Your one-item pass should stay too. It doesn't erase my failure, but neither should we erase a genuine successful case.
Joel | Agreed. Keep the [[scope of evidence::Scope of evidence includes the separate one-item success and three-item failures without generalizing to untested conditions.]] bounded: one-item success, this three-item failure, other sizes unknown. Those facts can coexist.
Hana | If you reduce the input and the same omission remains, record that smaller case. We don't yet know the smallest failing selection.
Joel | That would establish a [[minimal reproduction::Minimal reproduction is a smaller retained failure example, which has not yet been established by the current observations.]]. I'll start with the known saved selection before trying to remove anything from it.
Hana | My handoff will include both observations and the exact reproducer, with two attempts out of two and untested conditions listed.
Joel | That's the [[evidence bundle::Evidence bundle combines the saved input, actual output, build, action, and frequency needed for a focused investigation.]] I need. I'll return the result under those conditions, not another unqualified cannot-reproduce label.''',
    rehearsal=["Read the failure report using the actual build, saved selection, missing item, and two-out-of-two frequency.","Swap roles for turns 3-10. Keep different input separate from a reproduction of the reported failure.","Check the final handoff against turns 17-20. Include the saved evidence and untested conditions without guessing the cause."],
    transfer_title='Report a bounded reproduction',
    transfer_setup='Complete the report using only the observed build, input, output, and frequency.',
    transfer='''Tester: "The tested build is ___." | Q12 | Hana's reported omission is tied specifically to build Q12.
Developer: "The saved selection contains ___ items." | three | The reproducible input is the saved selection of three items.
Tester: "The ___ selected item is omitted." | last | The reported defect removes the final selected item from the export.
Developer: "The omission occurred in ___ attempts out of two." | two | Hana observed the omission in both of the two reported attempts.''',
))

BOOK['units'].append(unit(
    title='Choosing cases at boundaries and across rules',
    scene='Five, ten, and fifteen never touch the limits',
    skill='Explain missing boundary and rejection coverage while keeping unspecified decimal behavior separate from the whole-number rule.',
    brief='A fictional quantity form accepts whole numbers from 1 through 20 inclusive and rejects whole-number values outside that range. The proposed tests use only 5, 10, and 15. Tester Rosa and developer Amir review the gap. They propose boundary-focused values 0, 1, 2, 19, 20, and 21. Decimal handling is unspecified and outside the stated whole-number rule. The new tests are proposed, not executed results.',
    cast='Rosa | Tester reviewing case selection\nAmir | Developer discussing the rule',
    culture=('Explain why a case matters', 'Adding more inputs is less persuasive than connecting each input to a rule. Name the accepted endpoint, its nearby accepted neighbor, and the adjacent rejected value. Keep a missing decimal rule visible without silently expanding the product specification.'),
    a='''Which whole-number values are accepted by the rule? | 1 through 20 inclusive | 0 through 20 inclusive | 1 through 19 only | Every positive number | The stated acceptance range includes both one and twenty.
What is missing from 5, 10, and 15? | Endpoint and outside-range checks | All accepted values | The existence of a quantity field | A confirmed decimal policy | All three proposed inputs lie inside the accepted range rather than at or beyond its limits.
What is known about decimals? | Handling is unspecified | They are all accepted | They are all rejected under an explicit rule | They are rounded automatically | The supplied whole-number rule does not specify decimal handling.''',
    vocabulary='''boundary value | Input at an edge where a rule changes. | select a boundary value
boundary value analysis | Test design concentrating on rule edges and nearby values. | apply boundary value analysis
equivalence partition | Group of inputs expected to follow the same relevant rule. | identify an equivalence partition
valid partition | Input group accepted under the specified rule. | sample the valid partition
invalid partition | Input group rejected under the specified rule. | cover an invalid partition
lower bound | Smallest value within a defined range. | check the lower bound
upper bound | Largest value within a defined range. | check the upper bound
inclusive range | Range containing both stated endpoints. | specify an inclusive range
whole number | Number without a fractional part in the stated quantity context. | enter a whole number
adjacent value | Nearest relevant value beside a boundary. | test the adjacent value
interior value | Input strictly between the relevant endpoints. | distinguish an interior value
off-by-one error | Mistake that shifts a count or boundary by one unit. | detect an off-by-one error
acceptance region | Set of inputs the stated rule accepts. | define the acceptance region
rejection region | Set of inputs the stated rule rejects. | cover the rejection region
input domain | Set of inputs relevant to the defined problem. | state the input domain
decimal input | Input containing a fractional numeric value. | clarify decimal input
validation message | User-facing message explaining an input condition. | check the validation message
test case | Defined input, action, and expected outcome for a check. | specify the test case
case selection | Choice of checks to cover relevant behavior. | explain case selection
coverage item | Rule, value, or condition counted in a coverage assessment. | identify the coverage item
decision rule | Condition-to-outcome relationship. | map the decision rule
decision table | Organized mapping of condition combinations to outcomes. | build a decision table
out-of-range value | Input below or above the accepted range. | reject an out-of-range value
unspecified behavior | Behavior for which no governing rule is supplied. | flag unspecified behavior''',
    precision='One and twenty are accepted endpoints. Zero and twenty-one are adjacent rejected whole-number values. Two and nineteen check just inside the range. The existing five, ten, and fifteen do not test these edges.',
    precision_extra='Keep rule-based expectations separate from execution results: the proposed cases should accept or reject as stated, but no new test has yet been run. Decimal handling needs its own requirement clarification rather than an invented rounding or rejection rule.',
    phrases='''State the domain | The rule concerns whole-number quantities.
State the range | One through twenty are accepted, including both endpoints.
Describe existing cases | Five, ten, and fifteen are interior values.
Name the lower endpoint | One should be accepted.
Name the value below | Zero should be rejected.
Name the upper endpoint | Twenty should be accepted.
Name the value above | Twenty-one should be rejected.
Add inside neighbors | Two and nineteen check just inside the limits.
Explain the gap | The current set never reaches either boundary.
Connect case and rule | Each added value tests a specific edge condition.
Avoid a result claim | These are expected outcomes, not completed test results.
Separate decimals | Decimal handling is not specified.
Avoid inventing rounding | We have no agreed rounding rule.
Request clarification | Ask for the decimal policy separately.
Keep coverage honest | Boundary cases improve coverage but do not prove the form defect-free.
Close the proposal | Add the six boundary-focused cases and retain their expected outcomes.''',
    notes='''Through ... inclusive | Includes both endpoints in the accepted range.
Should be | States a rule-derived expectation rather than an observed result.
Just inside | Identifies the accepted neighbor near a boundary.
Below versus above | Separates the two rejected regions.
Not specified | Marks missing requirements without choosing a behavior.
Improve ... but | Recognizes a benefit while limiting the coverage claim.''',
    d='''Which six-value set checks both endpoints and their immediate neighbors? | 0, 1, 2, 19, 20, 21 | 5, 6, 10, 11, 14, 15 | 1, 5, 10, 15, 18, 19 | 2, 3, 4, 5, 6, 7 | The correct set includes each endpoint and the nearest whole number on either side.
Which expected result is correct? | Accept 20 and reject 21 | Reject 20 and accept 21 | Accept both 0 and 21 | Reject every interior value | Twenty is included in the stated range, while twenty-one lies above it.
Which decimal statement is justified? | The rule requires clarification for decimals | All decimals round down | Every decimal is explicitly rejected | Decimals are already tested | The scenario provides no decimal policy or completed decimal checks.
Which coverage claim is appropriate? | The proposed set addresses the missing edges but has not been executed | All possible defects are eliminated | Three interior checks prove both bounds | The new cases have already passed | Case design identifies intended coverage, but execution evidence is still absent.''',
    dialogue='''Rosa | The quantity tests use five, ten, and fifteen. All sit inside the accepted range, so none reaches the point where the rule changes.
Amir | You mean the [[boundary value::Boundary value identifies an endpoint where the quantity rule changes between acceptance and rejection.]] cases at one and twenty. The requirement says both endpoints are included, so those exact values should be accepted.
Rosa | The nearest rejected whole-number values are zero and twenty-one. They check both sides of the accepted one-through-twenty range.
Amir | That gives us an [[invalid partition::An invalid partition contains whole-number inputs outside the accepted one-through-twenty range that the rule says to reject.]] on either side. The existing tests only sample the accepted middle and tell us nothing about either rejection region.
Rosa | I propose zero, one, two, nineteen, twenty, and twenty-one. That includes each endpoint and the nearest relevant value on either side.
Amir | The [[adjacent value::Adjacent value refers to the nearest whole-number neighbor beside an endpoint, such as zero or two beside one.]] matters because a comparison can be wrong by one. Checking only five would not expose an error that rejects one but accepts the rest.
Rosa | Two and nineteen are accepted, but they test just inside the edges. I'll explain that role rather than describe the extra values as more coverage without details.
Amir | That is a clear use of [[boundary value analysis::Boundary value analysis concentrates case selection on endpoints and nearby inputs rather than only central accepted values.]]. Connect each proposed input to its expected result and the edge condition it helps examine.
Rosa | At the lower edge, zero should reject and one and two should accept. Those are expectations; the new cases haven't run.
Amir | Keep that [[expected result::Expected result states the outcome required by the rule, which is distinct from an actual result of an executed test.]] language. Saying should be accepted follows the requirement; saying passed would falsely imply an observation we do not have.
Rosa | At the upper edge, nineteen and twenty should accept, twenty-one should reject. Inclusive means we must not reject twenty itself.
Amir | Exactly. An [[inclusive range::Inclusive range includes both stated endpoints, so one and twenty belong to the accepted set.]] includes the endpoints themselves. We should not quietly turn twenty into the first rejected value.
Rosa | What about one point five? The stated rule covers whole-number quantities, and we haven't been given a fractional-input policy.
Amir | Then [[decimal input::Decimal input falls outside the supplied whole-number rule and needs its own clarified handling policy.]] needs a separate clarification. We should not invent rounding, truncation, acceptance, or rejection and present it as an existing requirement.
Rosa | I'll map below one, one through twenty, and above twenty to their outcomes, with decimal handling visibly unresolved rather than silently added to reject.
Amir | Yes. A [[decision table::A decision table maps the stated quantity regions to their required outcomes without inventing a decimal rule.]] can organize those outcomes. Mark decimal behavior as unspecified rather than folding it into a rejection rule that was never agreed.
Rosa | We can retain useful interior cases, but their count won't establish edge coverage. Three central examples still miss both endpoints.
Amir | Correct. [[Case selection::Case selection concerns which meaningful conditions are checked, not merely how many tests exist.]] is about the conditions exercised, not simply having several numbers in a list. The current values all occupy the interior.
Rosa | I'll submit the six cases and expected outcomes as a proposal, not a pass report. The separate decimal question remains open.
Amir | That is accurate [[coverage::Coverage describes the conditions addressed by the proposed cases, not proof that every defect is absent or every test has passed.]] language. It improves the design while keeping both execution status and the missing decimal rule visible to the team.''',
    rehearsal=["Read the six proposed boundary values in order, with their expected accept or reject results.","Swap roles for turns 9-16. Stress should accept rather than passed, and keep decimal handling unresolved.","Compare the final proposal with the brief: both endpoints and immediate neighbors, with no invented execution result."],
    transfer_title='Read the limits literally',
    transfer_setup='Complete the expected-result exchange. These expectations come from the stated rule, not from completed test runs.',
    transfer='''Tester: "The accepted lower endpoint is ___." | 1 | One is explicitly included as the lower endpoint of the range.
Developer: "The accepted upper endpoint is ___." | 20 | Twenty is explicitly included as the upper endpoint of the range.
Tester: "The whole number immediately above the range is ___." | 21 | Twenty-one is the nearest whole number above the accepted upper endpoint.
Developer: "Decimal handling remains ___." | unspecified | The stated rule provides no handling policy for decimal input.''',
))


BOOK['units'].append(unit(
    title='Explaining coverage and change risk',
    scene='The account page opens; the changed paths are unchecked',
    skill='Explain limited smoke-test evidence and justify focused follow-up on both consumers of a changed formatter.',
    brief='A fictional account update passes a smoke test that signs in and opens the account page. The update changes a formatter used by account-save and by the existing export path. Neither of those paths has been tested. Tester Elena and team lead Sam have one hour for further checking. They need to prioritize evidence around the shared change without claiming full coverage or assuming the existing export path is unaffected.',
    cast='Elena | Tester\nSam | Team lead',
    culture=('Replace tested with named paths', 'A short status such as smoke passed can be useful if everyone knows its limits. Name what ran, then connect the changed component to its consumers. A time limit calls for explicit priorities and residual risk, not a larger claim about the same narrow evidence.'),
    a='''What did the smoke test cover? | Sign-in and opening the account page | Account-save and export | Every formatter consumer | All regression checks | The supplied smoke test covers only sign-in and opening the account page.
Which paths use the changed formatter? | Account-save and existing export | Sign-in only | Export only | No existing behavior | The formatter is shared by account-save and the existing export path.
How much time remains? | One hour | A full week | No time limit | Two completed test cycles | The scenario allows one hour for additional checking, not unlimited coverage.''',
    vocabulary='''smoke test | Small check set used to detect major basic failures. | pass the smoke test
regression testing | Checking existing behavior for problems introduced by change. | prioritize regression testing
change impact | Potential effect of a modification on related behavior. | assess change impact
shared component | Component used by more than one path or feature. | identify the shared component
formatter | Component converting values into a required representation. | trace formatter usage
consumer path | Execution route using a shared component. | test the consumer path
account-save path | Route that persists an account update. | exercise the account-save path
export path | Route producing output for external use. | check the export path
coverage gap | Relevant behavior not yet checked. | report the coverage gap
risk-based testing | Selection of tests according to relevant likelihood and impact concerns. | propose risk-based testing
test priority | Relative order or urgency assigned to checks. | set test priority
timebox | Fixed amount of time allocated to work. | use a one-hour timebox
residual risk | Risk remaining after the checks or controls performed. | disclose residual risk
test scope | Behavior and conditions included in the checking effort. | state the test scope
execution evidence | Record of checks actually run and their results. | distinguish execution evidence
untested path | Execution route with no relevant test result yet. | identify an untested path
dependency mapping | Identification of relationships between components and consumers. | use dependency mapping
functional impact | Effect on what users or systems can do. | assess functional impact
test objective | Purpose a particular check is meant to serve. | define the test objective
selection rationale | Reason for choosing particular checks. | explain the selection rationale
coverage claim | Statement about what the tests have exercised. | limit the coverage claim
test summary | Concise account of scope, results, and limits. | write the test summary
branch coverage | Proportion of defined control-flow branches exercised by tests. | report branch coverage
release recommendation | Evidence-based advice about proceeding with a release. | qualify a release recommendation''',
    precision='Opening the account page does not establish correct account-save formatting, and it does not exercise export. Both use the changed formatter. Existing behavior can need regression checking even when the visible update is described as an account change.',
    precision_extra='One hour limits the work, not the meaning of full coverage. Propose focused checks of the changed formatter through both consumer paths, then report what actually ran and any remaining gaps without implying all risks were removed.',
    phrases='''State the narrow success | Sign-in and opening the account page passed.
Name the change | The shared formatter changed.
Identify both consumers | Account-save and export use that formatter.
Expose the gap | Neither consumer path has been tested.
Challenge the label | An account update can still affect export.
Explain the priority | I would focus the next checks on the changed component's consumers.
Name the time limit | We have one hour for further checking.
Keep a proposal provisional | Those checks are planned, not completed.
Request a clear objective | Check the formatted result in each consumer path.
Avoid claiming total coverage | A smoke pass is not full regression coverage.
Preserve the unknown | Export behavior after this change remains unverified.
Report actual execution | List which checks ran and their results.
Report unfinished work | Keep any untested path visible.
Separate evidence and advice | The summary can support a recommendation without proving every risk absent.
Name remaining exposure | There will still be residual risk.
Close with a bounded plan | Prioritize both affected paths and report the limits of the hour's work.''',
    notes='''Neither | Makes clear that both relevant consumer paths lack results.
Still affect | Challenges an assumption that an existing path is outside the change.
Would focus | Offers a reasoned proposal without fabricating a completed plan.
After this change | Ties the needed evidence to the modified version.
Not full | Limits the coverage meaning of a smoke pass.
Which ... and their | Requires named checks paired with actual outcomes.''',
    d='''Which summary is accurate? | Smoke passed for sign-in and page opening; save and export remain untested | All account behavior passed | Export is unaffected because it is old | The formatter is fully verified | The summary preserves the exact checked scope and both missing consumer paths.
Why include export in follow-up? | It uses the changed formatter | Every old feature must be rewritten | The smoke test already failed export | Export is the only account feature | Shared-component usage creates a relevant change-impact question for the existing export path.
What does one hour justify? | Prioritized checks with disclosed gaps | A full-coverage claim without execution | Automatic release approval | Ignoring all shared consumers | The timebox limits testing and requires explicit reporting of remaining uncertainty.
Which statement confuses plan and evidence? | Both paths passed because we intend to check them | Both paths need checking | The current smoke scope is narrow | One hour remains for further work | Intending to run checks provides no evidence that either path has passed.''',
    dialogue='''Elena | Sign-in and opening the account page passed. I don't want that smoke result reported as account-save or export tested; neither path ran.
Sam | Agreed. What changed that makes those the next checks? The [[smoke test::Smoke test describes the small basic check set, not evidence that every changed behavior has been exercised.]] itself tells us only about those basic actions.
Elena | The update changes a formatter used by both save and export. The account label on the change doesn't remove export from its impact.
Sam | Then the [[shared component::Shared component identifies the formatter used by both account-save and export, linking both paths to the modification.]] gives us a concrete reason to include both. Existing export behavior can regress when its dependency changes.
Elena | Opening the page doesn't compare the formatted saved value. It also doesn't generate an export whose contents we can check.
Sam | That's the [[coverage gap::Coverage gap names the untested account-save and export behavior that the narrow smoke test did not exercise.]]. We have basic access evidence, not results for the two consumers of the changed formatter.
Elena | We have one hour. I'd focus on each consumer's output, with an explicit expected representation, before spending time on unrelated screens.
Sam | That is a defensible [[selection rationale::Selection rationale explains why the changed formatter's consumers deserve attention within the limited testing time.]]. Explain which changed behavior the checks target rather than just promising more test cases.
Elena | I can't promise full regression coverage in that hour. I'll keep the uncompleted checks visible if the time runs out.
Sam | Right. The [[timebox::Timebox is the one-hour limit on additional work, which does not expand the meaning of the evidence collected.]] constrains the work; it doesn't redefine a short check set as full coverage.
Elena | For export, the rationale is the shared formatter, not evidence that it already fails. I don't have a failure probability to attach.
Sam | State the [[change impact::Change impact concerns the plausible effect of the modified formatter on both consumers without asserting an unmeasured failure probability.]] relationship without inventing one. A relevant dependency is enough to justify investigating that path.
Elena | Both proposed checks are still planned. I'll update their statuses only after execution gives us actual results.
Sam | Keep [[execution evidence::Execution evidence consists of actual performed checks and results, not a planned check list.]] separate from intention. A planned check doesn't become passed because we expect it to be straightforward.
Elena | If only one consumer finishes, I'll identify which one and its result. I won't combine it with the other under formatter verified.
Sam | That preserves the [[residual risk::Residual risk is the uncertainty or exposure remaining after the checks actually completed, including unfinished planned work.]]. Readers need to know what remains unchecked as well as what the completed case showed.
Elena | I'll also check the content, not merely that Save or Export can be clicked. Otherwise we'd repeat the smoke-test limitation.
Sam | Exactly. The [[test objective::Test objective specifies the formatted behavior to verify in each consumer path rather than only opening a screen.]] is the changed formatting behavior in each path. Make the assertion answer that question.
Elena | Current update: narrow smoke pass, save and export untested, shared formatter changed, one hour available, focused follow-up proposed.
Sam | That's an accurate [[test summary::Test summary combines checked scope, actual results, proposed follow-up, and limits without claiming complete coverage or release approval.]]. The subsequent evidence can inform a recommendation without implying that every risk or release question is settled.''',
    rehearsal=["Read the narrow smoke result and identify both consumers of the changed formatter.","Swap roles for turns 7-14. Keep the one-hour plan separate from completed execution evidence.","Repeat the closing update, retaining both untested paths and the limit on coverage."],
    transfer_title='Keep scope, change, and time together',
    transfer_setup='Complete the testing update before the proposed follow-up checks have run.',
    transfer='''Tester: "The ___ test covered sign-in and opening the page." | smoke | The initial smoke test was limited to those two basic actions.
Lead: "Both paths use the changed ___." | formatter | The formatter is shared by account-save and the existing export path.
Tester: "Neither account-save nor export has been ___." | tested | The scenario provides no execution result for either consumer path.
Lead: "We have one ___ for further checking." | hour | One hour is the stated time available for additional testing.''',
))

BOOK['units'].append(unit(
    title='Investigating inconsistent automated results',
    scene='Cleanup deletes what search expects',
    skill='Describe an order-dependent automated failure and request isolated test data instead of treating reruns as a fix.',
    brief='On fictional build T8, an automated search check fails when it follows a cleanup check but passes when run alone. The cleanup removes a shared sample record that search expects. No code change occurs between these observations. Automation engineer Noah and tester Aisha compare the starting state and execution order. They need to remove the shared-data interference and verify the revised arrangement rather than simply rerun until the suite appears green.',
    cast='Noah | Automation engineer\nAisha | Tester',
    culture=('Inconsistent does not mean meaningless', 'Different outcomes can become understandable when hidden conditions are named. Record order and data state before calling a test random. A passing rerun can be evidence about changed conditions, but it does not erase the earlier failure or repair isolation.'),
    a='''When does the search check fail? | After the cleanup check | Whenever run alone | Only after a code change | On every build | The reported failure occurs when cleanup runs before search on T8.
What does cleanup remove? | The shared sample record search expects | All test source code | The T8 build | A confirmed unrelated log only | Cleanup deletes the same sample record required by the search check.
What changes between the observations? | Order and relevant starting state, not code | The code is confirmed rewritten | The search requirement disappears | Every environment setting | No code change occurs; the supplied difference concerns test order and shared data.''',
    vocabulary='''flaky test | Test showing inconsistent outcomes under apparently similar conditions. | investigate a flaky test
order dependency | Dependence of a result on the sequence of test execution. | expose an order dependency
shared fixture | Prepared data or state used by multiple checks. | isolate a shared fixture
setup | Preparation establishing a test's starting conditions. | verify setup
teardown | Work restoring or removing state after a test. | review teardown
cleanup | Removal of data or resources no longer needed by a check. | limit cleanup scope
test isolation | Independence of a test from other tests' state changes. | restore test isolation
state leakage | Unintended influence of one test's state on another. | detect state leakage
sample record | Prepared data item used for testing. | preserve the sample record
precondition | Required state before a check starts. | establish the precondition
execution order | Sequence in which checks run. | record execution order
standalone run | Execution of a check without the surrounding suite. | compare a standalone run
suite run | Execution of a group of related checks. | inspect the suite run
rerun | Another execution of an existing check. | qualify a rerun result
false alarm | Failure signal not caused by the claimed product defect. | investigate a false alarm
failure evidence | Records supporting an observed unsuccessful result. | retain failure evidence
test data ownership | Responsibility for creating and removing test records. | define test data ownership
unique test data | Data assigned specifically to one test or execution. | use unique test data
deterministic setup | Preparation that establishes predictable required conditions. | create deterministic setup
environment state | Relevant current conditions in the test setting. | compare environment state
interference | Effect of one check on another's operation. | remove test interference
quarantine | Temporary separation of an unreliable check under a defined policy. | review quarantine status
continuous integration | Frequent integration with automated checking; abbreviated CI. | investigate the CI result
verification run | Execution used to check whether a proposed correction works. | perform a verification run''',
    precision='The search result differs with test order because cleanup removes its expected sample record. No code change is needed for this interference to matter. Compare the starting state, not just the build identifier.',
    precision_extra="A passing standalone rerun is not a repair of the suite. Define data ownership and setup so each check has its required state without deleting another check's data, then verify both the relevant sequence and isolated behavior.",
    phrases='''Identify the build | Both observations are on T8.
Report the failing order | Search fails after cleanup.
Report the comparison | Search passes when run alone.
Preserve the code fact | No code changed between those observations.
Name the shared dependency | Both checks depend on the sample record's state.
Explain cleanup's effect | Cleanup removes the record search expects.
Avoid calling it random | The observed pattern is order-dependent.
Request the starting state | Was the required record present when search began?
Separate rerun and repair | A passing rerun does not fix isolation.
Request ownership | Which check creates and removes this record?
Propose isolation | Give the checks independent data or a defined setup.
Preserve the evidence | Keep the failed sequence and logs.
Avoid suppressing the symptom | Do not remove the assertion merely to get green.
Request verification | Check the revised arrangement in the relevant sequence.
Limit the conclusion | The standalone pass does not prove the suite is reliable.
Close with the cause of interference | Resolve shared-data ownership and verify the resulting behavior.''',
    notes='''After | Makes sequence part of the reported condition.
When run alone | Identifies the comparison as a different execution context.
No code changed | Removes one explanation without claiming all conditions were identical.
Required record | Names a specific precondition rather than vague environment trouble.
Does not fix | Distinguishes another observation from an actual correction.
Relevant sequence | Requests verification where the interference was originally observed.''',
    d='''Which explanation matches the evidence? | Cleanup removes data needed by the later search check | The code changes between every run | Search never passes | Every failure is random | The supplied shared-record relationship explains the observed order-dependent interference.
What comparison most directly tests the reported interference? | Record presence before search alone and after cleanup on T8 | Only search duration in two unrelated runs | Q12 export output versus T8 search output | Pass percentages with execution order omitted | The difference is the shared record removed by cleanup; matching the build while observing record presence targets that interference.
Which action is not a demonstrated fix? | Rerun alone until the check passes | Define independent test data | Review cleanup scope | Verify required setup | A standalone pass leaves the original suite interference unresolved.
What should verification include? | The relevant sequence after the data arrangement is corrected | Only deleting the failing assertion | A claim that no tests need data | An unchanged summary saying always passes | Verification must address the sequence and starting-state problem that produced the failure.''',
    dialogue='''Noah | Search fails after cleanup on T8 but passes alone. I was about to enable reruns, though no code changed between these results.
Aisha | Before doing that, compare the [[execution order::Execution order is the relevant sequence in which cleanup precedes the failing search check on the same build.]]. What does cleanup remove that the isolated search run still has?
Noah | The shared sample record. Search expects it, and cleanup deletes it. The build matches, but the data at the start doesn't.
Aisha | That explains an [[order dependency::Order dependency means the search result depends on cleanup having run first and removed its required record.]]. An identical build doesn't make the starting conditions identical.
Noah | A standalone rerun could turn the report green without fixing the sequence that lost the record. It would hide what we need to investigate.
Aisha | Exactly. A [[rerun::Rerun is another execution, whose success does not repair the original interference between cleanup and search.]] is another observation, not a repair. Keep its changed context visible instead of replacing the failure with it.
Noah | We need to decide who creates and removes the sample. Right now cleanup assumes ownership of something search treats as available.
Aisha | Make [[test data ownership::Test data ownership assigns responsibility for creating and removing records so one check does not invalidate another's preconditions.]] explicit. Otherwise a different execution order can expose the same problem again.
Noah | We could give each check its own records, or establish the required state explicitly without depending on another check's leftovers.
Aisha | Those address [[test isolation::Test isolation prevents another check's state changes from determining whether search has its required starting data.]]. Choose and review the arrangement, then verify it; proposing separation isn't evidence that the suite is repaired.
Noah | I'll retain the failing order and logs. The successful isolated run belongs beside them as a comparison, not as a replacement.
Aisha | Good. That [[failure evidence::Failure evidence preserves the observed failing sequence and its conditions even when a different standalone attempt passes.]] shows why the shared state matters. Deleting it would remove the most useful reproduction conditions.
Noah | The record's presence is required before the search assertion can mean anything. We shouldn't leave that hidden in the environment.
Aisha | Establish the [[precondition::Precondition is the required sample-record state that must be established before the search check starts.]] in setup. A missing fixture and an application search defect are different problems to report.
Noah | Cleanup also needs narrower ownership checks. A broad delete based on a shared label could still remove another test's record.
Aisha | That's the [[interference::Interference is cleanup's unintended effect on the later search check through removal of its required record.]] to remove. Keep the useful search assertion rather than weakening it until the suite looks green.
Noah | After the revision, I'll run cleanup then search, as well as search alone, and capture the starting data and actual results.
Aisha | The [[verification run::Verification run checks the revised data arrangement under the relevant sequence instead of assuming the proposed fix succeeded.]] needs that original sequence. A standalone pass alone would leave the reported interaction unverified.
Noah | My handoff will show T8, unchanged code, deletion of the expected record, and the two observed outcomes. The revised arrangement is not yet verified.
Aisha | That names the [[environment state::Environment state includes the sample-record presence that changes between suite and standalone execution despite an unchanged build.]] precisely. We can investigate the actual dependency instead of calling the result random and moving on.''',
    rehearsal=["Read the two T8 outcomes with their execution order and starting data state.","Swap roles for turns 7-16. Stress ownership of the sample record and preserving the search assertion.","Compare the final report with the brief. The data arrangement is proposed, not yet verified."],
    transfer_title='Name the hidden difference',
    transfer_setup='Complete the automation report using the observed order and shared-record facts.',
    transfer='''Engineer: "Both observations use build ___." | T8 | The scenario names T8 for both the suite and standalone observations.
Tester: "Search fails after ___." | cleanup | Cleanup runs first and removes the record required by search.
Engineer: "The shared sample ___ is removed." | record | The missing sample record is the relevant starting-state difference.
Tester: "A standalone pass does not prove test ___." | isolation | The original shared-data interference remains despite a successful standalone execution.''',
))


BOOK['units'].append(unit(
    title='Separating impact from scheduling in triage',
    scene="The missing export row and tomorrow's visible typo",
    skill='Compare functional impact, reach, and timing without equating demonstration urgency with defect severity or release approval.',
    brief="An export defect omits the final row in one monthly workflow. A heading typo appears on every account page. Tomorrow's customer demonstration uses the account page, with no export planned. Tester Lina and product lead Marcus discuss triage. The export has a data-completeness impact; the typo has broad visibility and immediate demonstration relevance. No severity scale, final repair order, or approval to release either issue is supplied.",
    cast='Lina | Tester\nMarcus | Product lead',
    culture=('Keep two dimensions on the table', 'Teams can disagree because one person is discussing harm and another is discussing timing. Name each dimension before comparing issues. A visible typo may be urgent for an event without making lost export data harmless, and discussing either issue does not authorize release.'),
    a='''What does the export defect do? | Omits the final row in one monthly workflow | Misspells every account heading | Prevents all sign-ins | Deletes every database record | The reported functional effect is a missing final export row in the monthly workflow.
What will tomorrow's demonstration use? | The account page, with no export planned | Only the monthly export | Every workflow | Neither affected area | The demonstration uses the account page, while export is not planned.
What decision has already been made? | No final repair order or release approval is supplied | The typo must always be first | The export is approved for release | Both defects are waived | The scenario provides discussion facts but no final scheduling or release decision.''',
    vocabulary='''triage | Structured review to classify issues and decide next handling. | bring a defect to triage
severity | Degree of impact caused by a defect under the relevant scale. | assess severity
priority | Relative urgency or order assigned to work. | set priority
functional impact | Effect on the ability to perform the intended task. | explain functional impact
visibility | Extent to which users encounter or notice an issue. | describe visibility
reach | Range of users or surfaces affected. | distinguish reach from harm
frequency | How often the relevant event or workflow occurs. | state workflow frequency
data completeness | Presence of all required data items. | verify data completeness
cosmetic defect | Presentation issue without an established functional failure here. | classify a cosmetic defect carefully
customer demonstration | Planned presentation of product behavior to a customer. | prepare for the customer demonstration
business timing | Importance arising from an event or deadline. | explain business timing
repair order | Sequence in which issues are scheduled for correction. | agree the repair order
release blocker | Issue preventing release under the applicable criteria. | identify a release blocker
waiver | Explicit authorized acceptance of an exception. | record a waiver
risk acceptance | Authorized decision to proceed with identified exposure. | distinguish risk acceptance
workaround | Alternative way to complete a task despite a defect. | verify a workaround
affected workflow | Process in which the reported issue occurs. | name the affected workflow
stakeholder impact | Consequence for people who rely on the product. | assess stakeholder impact
defect classification | Assignment of an issue to a defined category. | explain defect classification
scheduling constraint | Limit affecting when work can be performed. | state the scheduling constraint
decision owner | Person responsible for a specified decision. | identify the decision owner
evidence-based comparison | Comparison grounded in observed effects and stated context. | make an evidence-based comparison
defer | Postpone work without claiming the issue is resolved. | document a decision to defer
disposition | Recorded decision about how an issue will be handled. | record the disposition''',
    precision="Monthly describes when the export workflow occurs; it does not make a missing row trivial. Every account page describes the typo's reach; it does not make its functional impact identical to missing export data.",
    precision_extra="Tomorrow's demonstration creates a timing reason to discuss the typo urgently. It does not automatically set a universal severity ranking, decide the repair order, or approve release with either defect. Those decisions require the actual process and authority.",
    phrases='''Name the export effect | The export omits its final row.
Limit the affected workflow | The observed issue affects the monthly workflow.
Name the typo's reach | The heading typo appears on every account page.
State tomorrow's scope | The demonstration uses the account page.
Preserve the exclusion | No export is planned for the demonstration.
Separate dimensions | Impact and scheduling urgency are different questions.
Avoid minimizing | Monthly use does not make missing data harmless.
Avoid inflating | Broad visibility does not automatically mean greater functional harm.
Explain timing | The demonstration makes the typo immediately relevant.
Request the scale | Which severity definitions apply here?
Keep the decision open | We have not agreed the repair order.
Avoid implying permission | Triage discussion is not release approval.
Request a recorded decision | Please record the disposition for each issue.
Avoid inventing a workaround | We have not established an alternative export method.
Preserve both concerns | Keep data completeness and presentation visibility in the comparison.
Close with the distinction | Discuss impact, timing, and authorization separately.''',
    notes='''Affects | Names the observed consequence without inventing additional damage.
Does not make | Rejects an invalid inference from frequency or reach.
Immediately relevant | Expresses timing without assigning a severity category.
Which definitions | Requests the actual scale instead of assuming a universal one.
Have not agreed | Keeps scheduling unresolved.
For each issue | Prevents one broad statement from concealing different dispositions.''',
    d='''Which comparison is accurate? | Export loses a row; the typo is widely visible and relevant to tomorrow's demo | The monthly defect is harmless | The typo destroys all account data | Neither issue has any user effect | The correct comparison preserves functional impact, reach, and event timing separately.
What does the demonstration establish? | A timing reason to discuss the typo urgently | Automatic permission to release both defects | A universal severity ranking | Proof export is correct | The planned account-page demonstration affects scheduling relevance, not defect correctness or release authority.
Which claim needs more evidence? | A workaround exists for the export | The export omits its final row | The typo appears on every account page | No export is planned for the demo | No alternative export method or verified workaround is supplied.
Which statement avoids a false decision? | The repair order and release disposition still need agreement | The typo is automatically first under every policy | The export has been waived | Both issues are approved for release | The scenario gives no final scheduling or authorization decision.''',
    dialogue='''Lina | Before we rank these issues, can we separate missing export data from the heading typo? Tomorrow's demonstration affects urgency, but not the underlying consequences.
Marcus | Start with the [[functional impact::Functional impact identifies what the export defect prevents or corrupts, here completeness of the exported rows.]] of the export. A missing row affects the completeness of that workflow's output, even though the workflow runs monthly.
Lina | Monthly is the workflow frequency, not proof that the missing row is harmless. We should retain the actual completeness problem in the description.
Marcus | Agreed. [[Frequency::Frequency describes how often the monthly workflow occurs and does not determine the seriousness of a missing row by itself.]] is one part of the context, not a substitute for describing the effect. What is established about the typo?
Lina | The typo appears on every account page, including the one used in tomorrow's demonstration. No export is planned for that event.
Marcus | That gives the typo immediate [[business timing::Business timing captures the upcoming demonstration's relevance to scheduling without equating it with greater functional harm.]]. We should discuss it urgently for that reason, while keeping its presentation effect distinct from the export's missing data.
Lina | So its visibility is broad, while the export has a different functional consequence. I don't want account-wide to become a substitute for an impact analysis.
Marcus | Yes. [[Reach::Reach describes the affected surfaces, such as every account page, rather than the degree of functional damage.]] and severity are not synonyms. A widespread heading error and an incomplete export have different consequences that need separate descriptions.
Lina | We haven't been supplied a severity scale. I'll describe the observed consequences before assigning labels such as critical or minor.
Marcus | Use the applicable [[defect classification::Defect classification should follow the actual agreed categories rather than invented labels based only on frequency or visibility.]] process when those labels are assigned. For this discussion, the concrete effects and timing are enough to explain the competing concerns.
Lina | Does discussing the typo urgently imply the export is cleared to ship? I'd like the meeting note to avoid linking those decisions.
Marcus | No. [[Priority::Priority concerns urgency or work order and does not itself authorize release with an unresolved defect.]] concerns what receives attention and when. It is not permission to ship a known issue, and we have not finalized the repair order either.
Lina | Then each issue needs a recorded outcome once decided: corrected, deferred, or still pending. Handled wouldn't tell the next person which one applies.
Marcus | Exactly. Record the [[disposition::Disposition is the specific handling decision for each issue, which must not be replaced by a vague handled status.]] once the authorized decision is made. Do not write deferred as though it meant corrected.
Lina | We also don't have a verified alternative export method. I won't soften the risk statement by inventing a workaround.
Marcus | Correct. A [[workaround::Workaround is an alternative way to complete the task, and none has been established for the incomplete export.]] is another factual claim requiring evidence. It cannot be added just to make the risk summary sound more reassuring.
Lina | My comparison will show the missing row, the typo's reach, and the demonstration's actual scope. It won't invent consequences we haven't observed.
Marcus | That is an [[evidence-based comparison::Evidence-based comparison uses the stated effects and demonstration scope without inventing severity ratings, workarounds, or approvals.]]. It gives the team a clear basis for scheduling discussion without pretending a decision has already been reached.
Lina | I'll leave the repair order and release disposition pending. Strongly arguing for urgency doesn't mean I can announce an authorization.
Marcus | Good. Keep any [[risk acceptance::Risk acceptance is an explicit authorized decision about identified exposure, not an inference from urgency or a triage conversation.]] separate and explicit. We can discuss urgency strongly without silently approving either defect for release.''',
    rehearsal=["Read the triage comparison once for functional impact, then again for demonstration timing.","Swap roles for turns 9-16. Keep classification, work order, and permission to release separate.","Repeat the closing status without adding an invented workaround, severity scale, or approved repair order."],
    transfer_title="Impact is not the same as tomorrow's priority",
    transfer_setup='Complete the triage summary without assigning an unsupported rating or release decision.',
    transfer='''Tester: "The export omits the final ___." | row | The supplied export defect concerns the final row of the monthly output.
Lead: "The typo appears on every account ___." | page | The heading typo has stated visibility across every account page.
Tester: "The demonstration is ___." | tomorrow | Tomorrow is the event timing that makes the account-page typo immediately relevant.
Lead: "The final repair order is still ___." | undecided | No final repair sequence is supplied by the scenario's discussion facts.''',
))

BOOK['units'].append(unit(
    title='Reporting exploratory findings',
    scene='Saved edits persist; unsaved edits disappear silently',
    skill='Report a timeboxed exploratory observation while separating behavior, an unresolved warning requirement, and untested mobile scope.',
    brief='Tester Isha completes a twenty-minute exploratory session with the charter Investigate interrupted profile edits. Navigating away after a saved edit preserves the value. Navigating away during an unsaved edit loses it without warning. Whether a warning is required is unspecified. Mobile behavior was not explored. Isha debriefs with product analyst Owen, who needs a factual record and a clarification request rather than a claim that every profile edit is broken.',
    cast='Isha | Exploratory tester\nOwen | Product analyst',
    culture=('An observation can be important before classification', 'Describe the exact sequence and what happened, then ask whether the intended behavior requires a warning. This preserves a potentially important user experience without inventing a requirement. Naming untested scope helps colleagues use the finding appropriately.'),
    a='''What was the session's charter? | Investigate interrupted profile edits | Verify every mobile workflow | Approve the release | Measure all search latency | The stated exploratory goal concerns interruption during profile editing.
What happens after a saved edit? | Navigating away preserves the value | Every value is lost | A warning always appears | The application crashes | The saved-edit observation shows persistence after navigating away.
What is unresolved? | Whether a warning is required for unsaved edits | Whether mobile was fully tested | Whether the session lasted twenty minutes | Whether the saved value persisted | Warning requirements are unspecified even though the no-warning behavior was observed.''',
    vocabulary='''exploratory testing | Investigation that adapts checks as the tester learns. | conduct exploratory testing
test charter | Statement guiding the purpose of an exploratory session. | define the test charter
focus containment | Keeping keyboard tab navigation within an open modal dialog. | verify focus containment
timebox | Fixed time allocated to an investigation. | respect the timebox
debrief | Discussion reviewing observations, limits, and follow-up. | hold a debrief
session notes | Record of actions, observations, and questions from testing. | preserve session notes
observation | Behavior directly seen during the investigation. | separate observation from interpretation
finding | Recorded result or question arising from investigation. | report a finding
saved state | Data retained after a completed save under the observed behavior. | verify saved state
unsaved change | Edit not yet committed by the relevant save action. | identify an unsaved change
navigation away | Leaving the current view or page. | describe navigation away
persistence | Continued retention of data across the relevant transition. | check persistence
warning prompt | Message alerting a user before a consequential action. | clarify the warning prompt
state transition | Change from one defined condition to another. | record the state transition
user journey | Sequence of actions a user takes toward an objective. | describe the user journey
focus restoration | Returning keyboard focus to the required target after an interface closes. | check focus restoration
requirement gap | Missing specification needed to judge intended behavior. | raise the requirement gap
usability concern | Potential difficulty in understanding or using the product. | record a usability concern
confirmed defect | Established departure from an applicable expectation. | distinguish a confirmed defect
follow-up question | Specific unresolved point for further investigation or clarification. | record a follow-up question
scope exclusion | Area explicitly not covered by the investigation. | list a scope exclusion
mobile coverage | Evidence from checking behavior on mobile devices or conditions. | avoid assuming mobile coverage
evidence trail | Records linking a finding to actions and observations. | retain the evidence trail
session outcome | Bounded summary of findings and remaining questions. | summarize the session outcome''',
    precision='The saved and unsaved paths have different observations. Saved edits persist after navigation; unsaved edits are lost without warning. Do not merge them into all edits are lost or assume that loss of an unsaved change violates an unstated rule.',
    precision_extra='Record the no-warning behavior and request a decision on whether a warning is required. Mobile was not explored, and twenty minutes is the session duration, not evidence of complete profile-edit coverage.',
    phrases='''Name the charter | The session investigated interrupted profile edits.
State the timebox | I explored for twenty minutes.
Separate the saved path | After saving, navigation preserved the value.
Separate the unsaved path | Navigating away during an unsaved edit lost the change.
Describe the interface | No warning appeared in that sequence.
Avoid a broad defect claim | I did not observe all profile edits failing.
Expose the requirement gap | The warning requirement is unspecified.
Request the intended behavior | Should leaving an unsaved edit trigger a warning?
Keep the observation | The no-warning behavior remains a useful finding.
Avoid inventing policy | I have not assumed that every unsaved edit must persist.
State the excluded scope | I did not explore mobile behavior.
Request traceable follow-up | Link the warning decision to the session notes.
Separate classification | The observation is not yet a confirmed requirement violation.
Preserve the sequence | Record whether save occurred before navigation.
Limit the conclusion | These findings apply to the paths explored.
Close the debrief | Saved value persists; unsaved change is lost without warning; requirement and mobile questions remain.''',
    notes='''After versus during | Distinguishes navigation following save from navigation during an unsaved edit.
No warning appeared | Reports an observation without asserting an unstated requirement.
Should ... trigger | Requests the intended behavior as an explicit decision.
Not yet confirmed | Preserves a finding while qualifying its classification.
Did not explore | Names an evidence gap without predicting the result.
Whether save occurred | Identifies the state distinction needed to reproduce the observation.''',
    d='''Which report matches the observations? | Saved edits persist; unsaved edits are lost without warning | Every saved edit is lost | Unsaved edits always persist | Mobile behavior is confirmed identical | The two stated navigation sequences have different outcomes that must remain separate.
What should be requested? | Clarification of whether an unsaved-edit warning is required | Automatic release approval | A declaration that all edits are broken | Removal of the saved-path observation | The missing rule concerns the intended warning behavior for unsaved navigation.
Which claim exceeds the evidence? | Mobile shows the same result | No warning appeared in the explored unsaved path | The session lasted twenty minutes | Saved value persisted in the explored saved path | Mobile was explicitly not explored, so its behavior is unknown.
Why avoid calling this a confirmed warning defect now? | The applicable warning requirement is unspecified | Observations never matter | Unsaved changes cannot affect users | Twenty minutes invalidates every finding | A confirmed requirement violation needs an applicable expectation, which is missing for the warning.''',
    dialogue='''Isha | My twenty-minute session found different results before and after saving a profile edit. I'd like to report those separately and ask about the warning rule.
Owen | Start with the [[test charter::Test charter names the session's purpose, investigating interrupted profile edits, rather than a claim of complete feature coverage.]]. That will help me understand which paths you explored and what the session was not intended to settle.
Isha | The charter was interrupted profile edits. In the saved path, I saved first and then navigated away; the value remained.
Owen | So the [[saved state::Saved state refers to the value retained after the completed save, which persisted through the observed navigation.]] persisted in that sequence. Keep it separate from what happened when navigation occurred before the edit was saved.
Isha | When I left during an unsaved edit, the change disappeared without a warning. I didn't observe saved values disappearing in that sequence.
Owen | That is a specific [[observation::Observation reports the actual loss of the unsaved change without warning, without inventing an intended-behavior rule.]]. We can record both the lost change and the absence of a warning without yet deciding whether either violates a requirement.
Isha | The requirement doesn't say whether a warning is required. I can raise that question without choosing the policy myself.
Owen | Raise that [[requirement gap::Requirement gap identifies the missing warning rule needed to classify the observed behavior against intended expectations.]] explicitly. Ask whether leaving an unsaved edit should trigger a warning, rather than treating your preferred behavior as already agreed.
Isha | I'll record edit, no save, navigate away, change absent, no warning. Saying profile loses data would omit the condition that makes this finding meaningful.
Owen | The [[evidence trail::Evidence trail connects the question to the recorded action sequence and outcome so another person can investigate it.]] matters. A note saying profile loses data would omit the saved-versus-unsaved distinction and could misrepresent the finding.
Isha | The lack of warning may confuse users, but I haven't established that it violates an agreed rule. Both points can stay in the report.
Owen | Correct. A [[usability concern::Usability concern can flag a potentially confusing user experience before an unspecified warning policy is resolved.]] can be worth discussing while its status remains clear. We do not need to exaggerate the evidence to make the question relevant.
Isha | Mobile wasn't explored. That needs to remain visible if someone forwards the report to another platform team.
Owen | List the [[scope exclusion::Scope exclusion records that mobile behavior was not explored and prevents the observed result being generalized to it.]]. Untested mobile behavior is unknown, not assumed identical and not assumed different.
Isha | The twenty-minute duration tells you how long I explored, not that I covered every possible interruption. I'll name the paths actually checked.
Owen | Exactly. The [[timebox::Timebox is the twenty-minute duration of the investigation, not a measure proving complete coverage of interruptions.]] explains the session boundary. Report the actual paths and questions rather than using elapsed time as a proxy for exhaustive checking.
Isha | After the owner decides the warning rule, we can test against it. Until then the original observation stays attached to the clarification request.
Owen | That keeps [[confirmed defect::Confirmed defect requires evidence of a departure from an applicable expectation, which the missing warning rule does not yet provide.]] separate from an unresolved finding. The eventual decision may change the classification without changing what you actually observed.
Isha | My summary will retain saved-value persistence, unsaved loss without warning, the missing warning rule, and no mobile coverage.
Owen | Good. That is a bounded [[session outcome::Session outcome summarizes the explored behaviors and remaining questions without claiming all profile edits or mobile behavior were tested.]]. It gives the next reviewer concrete evidence and one answerable follow-up question, rather than a broad label they have to reconstruct.''',
    rehearsal=["Read the saved and unsaved navigation sequences separately, with the observed result after each.","Swap roles for turns 7-14. Keep the warning requirement unresolved and mobile behavior untested.","Check the final debrief against the supplied observations, not a broad claim that all profile edits fail."],
    transfer_title='Separate the two paths and the missing rule',
    transfer_setup='Complete the exploratory report without converting an observation into an unsupported requirement judgment.',
    transfer='''Tester: "The session lasted twenty ___." | minutes | Twenty minutes is the stated duration of the exploratory session.
Analyst: "The ___ edit persisted after navigation." | saved | The value remained when navigation followed a completed save.
Tester: "The unsaved edit was lost without a ___." | warning | No warning appeared in the observed unsaved-navigation sequence.
Analyst: "___ behavior was not explored." | Mobile | Mobile is explicitly outside the behavior explored in this session.''',
))

BOOK['units'].append(unit(
    title='Giving a release-evidence handover',
    scene='Seven passed is not ten completed',
    skill='Report pass, failure, and blocked counts while identifying the unmet critical-path criterion and preserving release ownership.',
    brief='Fictional candidate Q20 has ten planned checks. Seven passed, one failed, and two are blocked by unavailable sample data. One blocked check is critical. The agreed exit criterion requires every critical-path check to be executed and reviewed. Tester Ben hands the evidence to release owner Mara. The critical blocked check means this criterion is not met. Mara has not made the release decision; the test summary is not approval.',
    cast='Ben | Tester preparing the handover\nMara | Release decision owner',
    culture=('Do not let a percentage hide a blocker', 'A headline pass count can sound reassuring while omitting an unexecuted critical path. Give the complete breakdown, explain the relevant criterion, and name the missing evidence. Keep your report of readiness conditions separate from the authorized release decision.'),
    a='''How are the ten checks divided? | Seven passed, one failed, two blocked | Seven passed and three passed by assumption | Eight passed and two failed | Ten executed and reviewed | The stated totals are seven passes, one failure, and two blocked checks.
Why is the critical-path criterion unmet? | One critical check is blocked and unexecuted | All seven passes are invalid | Every blocked check has failed | No criterion exists | The criterion requires execution and review of every critical-path check, including the blocked one.
Who owns the release decision? | Mara | The pass percentage | Every user | The unavailable sample data | Mara is explicitly named as the owner of the unresolved release decision.''',
    vocabulary='''release candidate | Version proposed for release pending the relevant decision. | identify the release candidate
planned check | Test included in the intended checking scope. | count planned checks
passed check | Executed check meeting its expected result. | report passed checks
failed check | Executed check not meeting its expected result. | report the failed check
blocked check | Check unable to proceed because a prerequisite is unavailable. | identify blocked checks
sample data | Prepared input needed to execute a test. | obtain sample data
critical path | Essential workflow or route under the agreed release criteria here. | identify the critical path
exit criterion | Condition required before leaving a testing stage. | assess the exit criterion
execution status | Whether and how a test has been run. | distinguish execution status
review status | Whether relevant evidence has received the required review. | report review status
test completion | End-of-stage accounting of performed work and unresolved items. | assess test completion
pass rate | Proportion of passes under a stated denominator. | qualify the pass rate
denominator | Total used to calculate a fraction or percentage. | specify the denominator
blocked dependency | Missing prerequisite preventing a check from proceeding. | resolve the blocked dependency
open defect | Unresolved product issue recorded for follow-up. | retain the open defect
readiness evidence | Results and records relevant to whether criteria are satisfied. | present readiness evidence
release authority | Permission or role empowered to decide release. | respect release authority
decision pending | Status showing that a decision has not been made. | keep decision pending
status breakdown | Separate counts or categories explaining the overall position. | give the status breakdown
evidence handover | Transfer of results, limits, and unresolved dependencies. | prepare the evidence handover
criterion exception | Explicit authorized departure from an agreed criterion. | document a criterion exception
risk register | Record of identified risks and their handling. | update the risk register
unexecuted check | Planned check that has not actually run. | disclose the unexecuted check
release disposition | Recorded decision on whether and how to proceed. | record the release disposition''',
    precision='Seven plus one plus two accounts for all ten planned checks. Eight have executed; two have not. Seven out of ten planned is 70 percent, while seven out of eight executed is 87.5 percent. Neither percentage makes the critical blocked check disappear.',
    precision_extra='The agreed criterion is unmet because a critical check has not executed and therefore cannot have its result reviewed. A summary must say this directly. No exception or release approval has been granted, and Mara retains the pending decision.',
    phrases='''Identify the candidate | This handover concerns Q20.
State the total | Ten checks were planned.
Give passes | Seven checks passed.
Give failures | One check failed.
Give blockers | Two checks are blocked by unavailable sample data.
Identify the critical gap | One blocked check is critical.
State the criterion | All critical-path checks must be executed and reviewed.
State the consequence | That criterion is not currently met.
Separate blocked and failed | Blocked does not mean executed and failed.
Separate blocked and passed | Missing data cannot count as a pass.
Qualify the percentage | Name whether the denominator is planned or executed checks.
Preserve the failure | Keep the failed check visible alongside the blockers.
Request the dependency | The blocked checks need their sample data.
Name authority | Mara owns the release decision.
Avoid implying approval | The decision remains pending.
Close the handover | Report the full breakdown, unmet criterion, and next evidence needed.''',
    notes='''Planned versus executed | Distinguishes ten intended checks from the eight that actually ran.
Currently | States the present criterion status without predicting the final decision.
By unavailable data | Names the dependency causing the blocked status.
Must be ... and | Preserves both execution and review requirements.
Alongside | Keeps failures visible rather than reporting only blockers.
Remains pending | Makes clear that a report is not an authorization.''',
    d='''How many checks have executed? | Eight | Ten | Seven | Two | Seven passed checks plus one failed check equals eight executed checks.
Which pair states pass proportions with matching denominators? | 70% of planned; 87.5% of executed | 87.5% of planned; 70% of executed | 70% of both planned and executed | 87.5% of both planned and executed | Seven divided by ten planned is 70%; seven divided by eight executed is 87.5%. Neither rate satisfies the missing critical-path criterion.
Which criterion statement is justified? | It is unmet because a critical check remains unexecuted | It is met because most checks passed | It does not apply to blocked checks | It is automatically waived by missing data | Every critical-path check must execute and be reviewed, and one remains blocked.
Which handover is complete? | Q20: seven passed, one failed, two blocked including one critical; criterion unmet; Mara's decision pending | Q20 passed because seven is a majority | Q20 has only two minor gaps | Q20 approved automatically | The complete handover includes all statuses, the critical gap, criterion consequence, and decision ownership.''',
    dialogue='''Ben | Q20 has ten planned checks: seven passed, one failed, two blocked by unavailable sample data. One of the blocked checks is critical.
Mara | Keep that [[status breakdown::Status breakdown accounts separately for all ten planned checks instead of hiding failure and blockers behind the pass count.]] in the headline. A pass percentage alone won't tell me whether our critical-path condition has been met.
Ben | It hasn't. Every critical-path check must execute and have its evidence reviewed, and the blocked one has no result to review.
Mara | Then state the [[exit criterion::Exit criterion requires execution and review of every critical-path check, which the blocked critical check prevents us from satisfying.]] is unmet. A majority of passes doesn't substitute for that missing critical evidence.
Ben | I'll keep blocked separate from failed. Those two never executed, so there's no result showing either success or an expectation mismatch.
Mara | Correct. A [[blocked check::Blocked check means execution is prevented by a missing prerequisite, not that the expected result was met or violated.]] isn't a pass by default, and it isn't an executed failure. Name why it couldn't proceed.
Ben | Eight ran: seven passes plus one failure. Ten is the planned total, not the number completed.
Mara | That makes [[execution status::Execution status separates the eight checks that ran from the two that could not run due to missing data.]] unambiguous. The remaining two still need their prerequisites before they can run.
Ben | Seven over ten planned is seventy percent. Seven over eight executed is eighty-seven-point-five. Both leave the critical blocker unresolved.
Mara | Exactly. Every rate needs its [[denominator::Denominator determines whether the reported pass proportion uses ten planned checks or eight executed checks.]]. A higher-looking percentage doesn't change what actually happened.
Ben | I'll retain the failed result alongside the blockers. Otherwise the missing-data discussion could overshadow a defect we actually observed.
Mara | Yes. The [[failed check::Failed check records an executed expectation mismatch and must remain visible separately from the unavailable-data blockers.]] needs its own follow-up. It shouldn't vanish when the report focuses on enabling the unexecuted checks.
Ben | The data request is still pending. I won't write data received or assume the tests will pass once somebody supplies it.
Mara | Keep that [[blocked dependency::Blocked dependency is the unavailable sample data that must be resolved before the affected checks can execute.]] explicit. Requesting a prerequisite, receiving it, and executing a check are separate stages.
Ben | And even after execution, the criterion still requires review. I'll show that separately instead of copying completed into every column.
Mara | Good. [[Review status::Review status is a separate requirement from execution under the stated criterion, so running a check alone is not sufficient.]] can't be inferred from a test run. Account for both parts of the requirement.
Ben | The report will say criterion unmet, no granted exception, and your production decision pending. This handoff isn't a sign-off.
Mara | That respects [[release authority::Release authority remains with Mara, and the evidence report does not itself grant approval or an exception.]]. I own the decision, but I haven't made it or authorized an exception.
Ben | Final status: Q20, seven passed, one failed, two blocked including one critical, missing data, required review, and decision pending.
Mara | That's usable [[readiness evidence::Readiness evidence presents actual results and unmet conditions for the decision maker without claiming release approval.]]. It supports an explicit decision without concealing the failed check or implying the blocked critical path has passed.''',
    rehearsal=["Read the Q20 status counts aloud and verify that seven plus one plus two accounts for ten planned checks.","Swap roles for turns 7-16. Say the denominator with each percentage and keep execution separate from review.","Repeat the closing handoff. Retain the unmet critical-path criterion and Mara's pending decision."],
    transfer_title='Account for every planned check',
    transfer_setup='Complete the Q20 handover. The release decision has not been made.',
    transfer='''Tester: "___ checks passed." | Seven | The scenario establishes seven passed checks out of the ten planned.
Owner: "___ check failed." | One | One executed check failed and must remain distinct from blocked checks.
Tester: "___ checks are blocked by missing sample data." | Two | Two checks could not execute because their required sample data was unavailable.
Owner: "The release decision remains ___." | pending | Mara has not made the release decision, and the report is not approval.''',
))
