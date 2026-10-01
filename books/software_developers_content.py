"""Original Software Development English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='software-developers', title='Software Development English',
    cover_label='ENGLISH FOR SOFTWARE ENGINEERS AND DEVELOPMENT TEAMS',
    cover_title='Software\nDevelopment', cover_size=38,
    tagline='Make the behavior clear. Make the limits explicit.',
    audience='For software developers discussing interfaces, debugging, reviews, dependencies, tests, performance, distributed behavior, and releases.',
    map_intro='Eight engineering conversations follow work from an unclear interface contract to a release handoff. Practice requesting evidence, challenging assumptions, explaining tradeoffs, and distinguishing a tested result from an unverified expectation.',
    notes_title='Describe behavior before confidence.',
    notes_intro='A confident engineering statement names its evidence and its boundary. A test double is not the real dependency; a staging deployment is not a production release; a timeout does not establish that a request failed.',
    field_notes=[
        ('Separate contract from convention', 'An omitted field, an empty string, and null can mean different things. State what this interface actually promises rather than relying on how another system behaves. A proposed interpretation needs agreement before it becomes a contract.', '"Omission leaves the nickname unchanged; the meaning of null is not specified."'),
        ('Make disagreement actionable', 'Anchor review comments in a changed line, observable behavior, and a concrete request. Keep naming preferences separate from defects. A focused failure test can make the concern easier to discuss without turning the review into a judgment of its author.', '"Moving this call outside the success branch also sends completion notices after failure."'),
        ('Attach the measurement conditions', 'A median describes the middle of observed results, not the slowest users or production behavior. Compare implementations under the same stated conditions, and include resource budgets. A faster measured response does not settle an overall tradeoff.', '"B lowers the median to twenty-five milliseconds but exceeds the memory budget."'),
        ('Keep release stages distinct', 'Code can be deployed but disabled, tested in staging but not production, or approved for review but not release. Name the environment, flag state, unresolved compatibility check, and actual decision owner in the handoff.', '"R18 is in staging with search disabled; Lee still owns the release decision."'),
    ],
    scope_note='All products, people, measurements, interfaces, and release processes are fictional. These scenarios teach professional English, not production operating instructions. Actual contracts, security requirements, engineering review, test environments, and change authorization take precedence. No exercise authorizes production changes or guarantees correctness, compatibility, reliability, or performance. Code-review and testing terminology is used without requiring a particular language or framework.',
    sources=[
        dict(title='Google Engineering Practices. What to Look for in a Code Review.',
             url='https://google.github.io/eng-practices/review/reviewer/looking-for.html',
             note='Context for reviewing functionality, tests, naming, and changed behavior. All pull requests and conversations here are original.', checked='1 October 2026'),
        dict(title='Amazon Builders Library. Making Retries Safe with Idempotent APIs.',
             url='https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/',
             note='Background on uncertain outcomes and retry contracts. The fictional reservation interface is not an AWS service or implementation guide.', checked='1 October 2026'),
        dict(title='Python Documentation. unittest.mock.',
             url='https://docs.python.org/3/library/unittest.mock.html',
             note='Reference for configured test doubles, return values, and raised exceptions. Exercises distinguish simulated behavior from actual dependency coverage.', checked='1 October 2026'),
        dict(title='Semantic Versioning 2.0.0.',
             url='https://semver.org/',
             note='Terminology for public interfaces, compatibility, and deprecation. The fictional packages are not assumed to follow this versioning convention.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying interface contracts',
    scene='Three nickname states, only two defined meanings',
    skill='Distinguish omission, an empty string, and null while requesting an explicit interface decision before implementation.',
    brief='A fictional profile interface accepts an optional nickname. Its current contract says an omitted nickname leaves the stored value unchanged, while an empty string clears it. A proposed client sends null. The meaning of null has not been specified. Client developer Maya and service developer Arun review the mismatch before either side implements a new interpretation. Optional describes whether the field may be absent; it does not settle what an explicit null means.',
    cast='Maya | Client developer\nArun | Service developer',
    culture=('Ask for the missing rule, not a guess', 'Developers may use the same familiar word for different behaviors. Repeat the exact input and resulting state before agreeing that an interface is clear. An explicit question about null avoids hiding a product decision inside an implementation detail.'),
    a='''What does omitting nickname do under the current contract? | Leaves the stored value unchanged | Clears it | Writes the word null | Rejects every update | The current contract explicitly preserves the value when nickname is omitted.
What does an empty string do? | Clears the nickname | Leaves it unchanged | Sets an unspecified default | Proves null is accepted | The empty string has a defined clearing meaning distinct from omission.
What remains undefined? | The meaning of an explicit null | Whether omission is possible | Whether an empty string clears | Whether nickname is a field | The proposed client sends null, whose meaning the contract has not specified.''',
    vocabulary='''interface contract | Agreed rules for inputs, outputs, and observable behavior. | clarify the interface contract
application programming interface | Defined way software components communicate; abbreviated API. | document the API
request payload | Data carried by a request. | inspect the request payload
optional field | Field that may be absent under the contract. | omit an optional field
nullable field | Field whose allowed values include null under the contract. | declare a nullable field
omitted field | Field not included in the submitted data. | distinguish an omitted field
empty string | Text value containing zero characters. | send an empty string
null value | Explicit marker whose meaning depends on the contract. | define the null value
stored state | Value or condition currently retained by the system. | preserve stored state
partial update | Change affecting only specified parts of a record. | apply a partial update
default value | Value supplied when the governing rules call for one. | document the default value
validation rule | Condition an input must satisfy. | agree on a validation rule
serialization | Conversion of data into a transportable representation. | inspect serialization behavior
deserialization | Conversion from transported data into usable values. | verify deserialization behavior
schema | Formal description of data structure and constraints. | revise the schema
field presence | Whether a particular field exists in the input. | check field presence
sentinel value | Special value used to signal a particular condition. | define a sentinel value
backward compatibility | Ability to preserve supported behavior for earlier consumers. | assess backward compatibility
consumer | Component using another component's interface. | identify the consumer
producer | Component providing data or behavior through an interface. | align producer expectations
wire format | Actual representation transmitted between components. | inspect the wire format
contract test | Test checking agreed interactions across an interface boundary. | add a contract test
undefined behavior | Behavior not specified by the relevant agreement here. | resolve undefined behavior
acceptance criterion | Specific condition used to judge whether work meets requirements. | state an acceptance criterion''',
    precision='Optional and nullable answer different questions. Optional concerns presence; nullable concerns allowed values. The stated contract defines omission and an empty string, but it does not authorize treating null as either one.',
    precision_extra='Use an input-to-effect sentence: If nickname is omitted, the stored value remains unchanged. Keep the proposed null behavior explicitly unresolved until the responsible parties agree, document it, and add the appropriate checks.',
    phrases='''Name the boundary | I want to confirm the profile interface contract.
Describe absence | An omitted nickname leaves the stored value unchanged.
Describe clearing | An empty string clears the nickname.
Identify the proposal | The proposed client sends null.
Expose the gap | The contract does not specify what null means.
Separate terms | Optional does not automatically mean nullable.
Ask for the effect | What should the stored value be after that input?
Avoid borrowing a rule | I would not infer this from another API.
Inspect the actual data | Can we check the request payload?
State a condition | If the field is absent, the current value stays.
Keep a proposal provisional | Treating null as clear would be a new decision.
Request agreement | Can we agree on the intended behavior first?
Request documentation | Please record that rule in the contract.
Request a check | We need a test for each defined input state.
Avoid premature completion | The null case is still unresolved.
Close precisely | We agree on omission and empty string, but not yet on null.''',
    notes='''Does not automatically mean | Rejects an inference without rejecting the other person's whole proposal.
After that input | Connects a request value to observable stored state.
Would be | Marks a proposed consequence rather than an existing rule.
Not yet | Keeps an unresolved decision visible without implying permanent disagreement.
Each defined input state | Prevents a broad test claim based on only one example.
Can we agree | Invites a concrete decision about the missing behavior.''',
    d='''Which comment identifies the real gap? | The null case needs an agreed meaning | Optional proves null clears it | Empty string and omission are identical | Every API interprets null alike | Only null lacks a specified meaning in this particular contract.
Which pair must remain distinct? | Omission and an empty string | Two spellings of the same field name | Two confirmed clearing commands | Null and a documented clearing command | Omission preserves the value, whereas an empty string clears it.
What would justify calling null a clearing command? | An explicit agreed contract change | The developer's preference alone | The word optional alone | An unrelated API example | A new interpretation needs agreement rather than an unsupported inference.
Which test plan matches the discussion? | Check each defined input state and resolve null before asserting its effect | Test omission and assume all other inputs match | Test only the client's display | Treat null as proven compatible | Distinct input states require distinct expectations, with null still unresolved.''',
    dialogue='''Maya | Before I finish the profile client, can we check what happens when someone removes a nickname? My proposed payload sends null, but the contract mentions an empty string.
Arun | We should separate that from an [[omitted field::An omitted field is absent and preserves the stored nickname under the stated contract.]]. If nickname is absent from the request, the stored value stays unchanged. That part is already defined.
Maya | Right. I was reading optional as permission to send no value. I can see that absence and an explicit value are different on the wire.
Arun | Exactly. An [[optional field::Optional field describes allowed absence, not the meaning or acceptability of an explicit null.]] may be absent. It does not tell us whether null is accepted or what effect null should have if it is accepted.
Maya | For the existing clearing behavior, the client should send a string with no characters. That is different from leaving the property out altogether.
Arun | Yes, an [[empty string::An empty string has the specified effect of clearing the nickname, unlike omission.]] clears the nickname. We should preserve that distinction in the examples so nobody silently changes the current behavior while updating the client.
Maya | Then my null proposal has no agreed effect yet. I should not describe it as equivalent to clearing just because another service uses it that way.
Arun | Correct. The [[interface contract::The interface contract is the agreement that must specify the missing null behavior before implementation.]] needs a decision for that input. We could discuss a change, but discussion alone does not make the proposed meaning an existing guarantee.
Maya | Could we inspect what the client actually sends? A serializer might drop a property, and then our conversation about null would not match the transmitted data.
Arun | Let us check the [[request payload::Request payload identifies the actual submitted data, which may differ from an assumed client representation.]] in a controlled example. We need to distinguish the client's internal value from the representation delivered to the service.
Maya | I will keep three examples separate: nickname absent, nickname as an empty string, and nickname explicitly null. The third will have no claimed result until we agree.
Arun | That will make [[field presence::Field presence distinguishes an absent nickname property from a present property carrying a value.]] visible. For the first two, write the resulting stored value beside the input rather than using the vague label no nickname.
Maya | Should the schema be changed now to allow null? I do not want the schema to appear to settle a behavior we have not actually decided.
Arun | Hold that change until the [[validation rule::The validation rule must reflect an agreed input policy rather than preempt the unresolved decision.]] and intended effect are agreed. Allowing a value and defining its effect need to be consistent.
Maya | Once the rule is documented, I can add client examples and ask for checks at the interface boundary, not only checks of the form display.
Arun | A [[contract test::A contract test checks the agreed interaction across the client-service boundary rather than only the visible form.]] can support that. Its expected result must come from the agreement, though; the test must not invent the missing null rule.
Maya | I also want existing clients protected. We should not accidentally change omission from leave unchanged to clear while solving this new input question.
Arun | That is a [[backward compatibility::Backward compatibility concerns preserving supported behavior for existing clients, including the established omission rule.]] concern worth recording. We have not demonstrated compatibility merely by agreeing that the new client looks correct.
Maya | My summary will say omission preserves, empty string clears, and null remains unspecified. I will leave the proposed null implementation pending the interface decision.
Arun | Good. That gives us an explicit [[acceptance criterion::An acceptance criterion must name the agreed input and effect before implementation can be judged complete.]] once the decision is made, instead of treating an ambiguous word as enough to approve the change.''',
    transfer_title='Three inputs, three separate statements',
    transfer_setup='Complete the interface summary using only the stated contract and the unresolved proposal.',
    transfer='''Developer: "An omitted nickname leaves the value ___." | unchanged | Omission explicitly preserves the existing nickname under the current contract.
Reviewer: "An empty string ___ the nickname." | clears | The empty string is the defined clearing input in this interface.
Developer: "The meaning of null remains ___." | unspecified | No agreed effect for null is supplied in the scenario.
Reviewer: "Optional does not automatically mean ___." | nullable | Optional concerns absence, while nullable concerns allowed explicit values.''',
))


BOOK['units'].append(unit(
    title='Debugging from reproducible evidence',
    scene='The empty date is a suspect, not yet the cause',
    skill='Report a reproducible failure, expose a confounded comparison, and request a controlled test without overstating causation.',
    brief='Developer Nia has a three-row import file containing one empty date. It fails, and the stack trace points to date parsing. A two-row file without that row succeeds. Colleague Ellis reviews the evidence. No controlled test has isolated the empty date as the cause: the successful file differs in both row count and content. They need a test in a suitable nonproduction environment that changes one relevant condition while preserving the others.',
    cast='Nia | Developer investigating the import\nEllis | Developer reviewing the evidence',
    culture=('Treat a hypothesis as useful, not embarrassing', 'Naming a likely cause can help investigation, provided its status remains clear. Distinguish I suspect from I have isolated. A colleague can challenge a comparison without dismissing the observation or the person who found it.'),
    a='''Which input fails? | A three-row file containing an empty date | Every three-row file | A two-row file with all dates empty | Every file with any date | Only the stated three-row example is established as failing.
What does the successful comparison change? | Both row count and content | Only the date format | Only the environment | Nothing relevant | Removing the row changes the number of rows and their content.
What does the stack trace establish? | The observed failure path reaches date parsing | The empty field is conclusively the root cause | The database is corrupt | Production is safe to test | The trace locates part of the failure path but does not isolate the cause.''',
    vocabulary='''reproduction | Repeatable demonstration of an observed failure. | obtain a reproduction
reproducible example | Input and conditions that consistently show the behavior. | share a reproducible example
stack trace | Recorded chain of calls associated with an error. | inspect the stack trace
parser | Component interpreting structured input. | inspect the parser
date parsing | Conversion of date text into a usable representation. | investigate date parsing
input fixture | Prepared input used in a test. | preserve the input fixture
hypothesis | Proposed explanation requiring evidence. | test a hypothesis
root cause | Underlying cause established through investigation. | isolate the root cause
confounding variable | Additional changed factor obscuring a comparison. | remove a confounding variable
controlled comparison | Comparison holding relevant conditions fixed except the tested change. | run a controlled comparison
minimal example | Reduced example retaining the relevant behavior. | reduce to a minimal example
baseline | Reference condition against which changes are compared. | establish a baseline
failure signature | Identifying pattern of an observed failure. | compare the failure signature
exception | Signal that interrupts normal execution under specified conditions. | capture the exception
log context | Surrounding recorded information explaining an event. | preserve log context
row count | Number of records or lines in the input table. | hold row count constant
empty field | Present field containing no supplied value. | isolate the empty field
malformed input | Data not conforming to the required structure or rules. | identify malformed input
deterministic behavior | Behavior producing the same result under the same relevant conditions. | check deterministic behavior
environment parity | Relevant similarity between execution environments. | establish environment parity
regression | Previously working behavior broken by a later change. | investigate a regression
instrumentation | Added observation mechanisms such as logs or measurements. | improve instrumentation
causal claim | Statement that one condition produces an effect. | qualify a causal claim
nonproduction environment | Environment not serving the live production workload. | use a nonproduction environment''',
    precision='The two-row success is useful evidence, but it changes two things at once. It does not distinguish an empty-date effect from other differences associated with the removed row or the changed row count.',
    precision_extra='A stack trace helps locate where the failure surfaced. It is not automatically a root-cause analysis. Propose a controlled comparison with the same row count and other content while varying the suspect date condition.',
    phrases='''Report the failing input | The three-row file fails during import.
Report the distinguishing detail | One row contains an empty date.
Name the observation | The stack trace reaches date parsing.
Report the comparison | The two-row file succeeds.
Qualify the conclusion | I suspect the empty date, but have not isolated it.
Expose the confound | We changed both row count and content.
Ask for control | Can we hold the other fields constant?
Propose a narrow change | Change only the suspect date condition.
Preserve evidence | Keep the original failing fixture.
Avoid a universal claim | We have not shown that every empty date fails.
Ask for repeatability | Does the same fixture fail consistently?
Compare the outcome | Check whether the failure signature stays the same.
Name the setting | Run the comparison in a suitable nonproduction environment.
Separate location and cause | The trace points to parsing, not yet to a proven cause.
Report a limit | We do not have the controlled result yet.
Close the handoff | Share the fixture, conditions, trace, and next comparison.''',
    notes='''I suspect | Gives a working explanation an explicitly provisional status.
Have not isolated | Identifies the missing causal evidence.
Both ... and | Makes the two changing factors visible.
Hold constant | Requests an unchanged comparison condition.
Not yet | Limits the conclusion without discarding the evidence.
Whether | Introduces a check whose result is genuinely unresolved.''',
    d='''Which conclusion is supported? | The observed failing path reaches date parsing | All empty dates always fail | Row count has no effect | The root cause is proven | The trace supports a location statement, not the broader causal claims.
Which proposed comparison is strongest? | Keep three rows and other content fixed while varying the suspect date | Delete two more rows and change the environment | Compare unrelated files | Change date, encoding, and parser version together | Holding other factors fixed better isolates the condition being tested.
Which phrase avoids overstating evidence? | The empty date is a working hypothesis | The empty date is conclusively responsible | The trace proves every input rule | The successful file eliminates all other causes | A working hypothesis accurately labels the explanation as still requiring evidence.
What should the handoff preserve? | The failing fixture, conditions, and trace | Only the developer's confidence | A rewritten file without its original data | A production change without authorization | Reproducible evidence needs the original input and execution context.''',
    dialogue='''Nia | I can reproduce the import failure with this three-row file. One row has an empty date, and the trace ends in the date-parsing path.
Ellis | That gives us a useful [[reproducible example::A reproducible example provides the input and conditions needed to observe the reported failure again.]]. What did you change in the file that succeeds, and did you keep the other conditions the same?
Nia | I removed the row with the empty date. The remaining two rows import successfully. I was about to report that the empty date causes the failure.
Ellis | I would call that a [[hypothesis::Hypothesis labels the empty-date explanation as plausible but not yet isolated by a controlled test.]] for now. Removing the row changed its content and the total number of rows, so the comparison does not isolate the date.
Nia | Fair point. The successful file tells us the smaller input works, but it cannot show which part of the removed row matters.
Ellis | Exactly. The changed row count is a possible [[confounding variable::A confounding variable is another changed factor that prevents this comparison from isolating the date condition.]]. We should avoid ruling it out before making a comparison that keeps the relevant conditions fixed.
Nia | Would keeping all three rows and changing only that date give us a clearer test? I would preserve the other fields and use the same environment.
Ellis | That is a [[controlled comparison::Controlled comparison holds the other relevant conditions fixed while varying the suspected date condition.]] worth preparing. We still need to run it and record the outcome; a proposed test is not evidence of its result.
Nia | I will keep the original file untouched as a reference. The comparison file can be separate, with the specific change recorded beside it.
Ellis | Good. Preserve the failing [[input fixture::Input fixture names the prepared test data, which must remain available to reproduce the original failure.]] so another developer can reproduce your starting point. Otherwise we may accidentally lose the very example that made the problem observable.
Nia | How should I describe the trace in the issue? I do not want to make it sound irrelevant just because it does not settle causation.
Ellis | Say the [[stack trace::The stack trace records the observed call path around the error but does not alone establish its root cause.]] points to date parsing. That is useful location evidence. Keep it separate from the stronger claim that a particular input condition caused the failure.
Nia | I should also record the exact error pattern. If the modified file fails differently, saying both failed could hide an important distinction.
Ellis | Yes, compare the [[failure signature::Failure signature distinguishes the original error pattern from a different failure in the comparison run.]], not just the final status. A different exception or call path may mean you are looking at another problem rather than reproducing the same one.
Nia | I have not checked repeated runs yet. The example failed when I tried it, but I should confirm how consistently it behaves under those conditions.
Ellis | That helps establish [[deterministic behavior::Deterministic behavior concerns consistent results under the same relevant conditions, which repeated checks can investigate.]]. Record what you actually observe rather than assuming repeatability from one successful reproduction.
Nia | This should stay outside production. We can prepare the comparison in an appropriate test setting without asking live users to trigger the error.
Ellis | Agreed. Use a suitable [[nonproduction environment::A nonproduction environment supports the investigation without treating this dialogue as permission to test on live workloads.]] and record its relevant conditions. A result there still needs its environment boundary stated when you pass it on.
Nia | I will update the issue to say the empty date is suspected, the two-row comparison is inconclusive, and the controlled three-row test is pending.
Ellis | That is a well-qualified [[causal claim::A causal claim needs stronger evidence than the current confounded comparison, so the proposed cause remains qualified.]]. Include the fixture and trace, and we will assess the controlled result before calling anything the root cause.''',
    transfer_title='Report the evidence without upgrading the conclusion',
    transfer_setup='Complete the debugging handoff. The controlled test has not yet produced a result.',
    transfer='''Developer: "The failing file contains ___ rows." | three | The supplied failing fixture has three rows, including one empty date.
Reviewer: "The successful file contains ___ rows." | two | Removing the suspect row leaves the stated successful two-row file.
Developer: "The empty date remains a ___." | hypothesis | The current comparison has not isolated the date as the cause.
Reviewer: "Keep the other conditions ___ in the next comparison." | constant | Holding other conditions constant helps isolate the suspected date effect.''',
))

BOOK['units'].append(unit(
    title='Giving actionable code-review feedback',
    scene='A rename that changed the failure path',
    skill='Anchor a review comment in a changed call location, its observable effect, and a specific correction and test.',
    brief='A pull request is titled Rename export helper. The diff also moves the completion-notification call outside the success branch. Failed exports therefore notify users as though export completed. Reviewer Priya accepts the naming change but raises the behavior change with author Tomas. The review should request restoration of success-only notification and a failure-path test. The acceptable rename does not justify approving the unintended notification behavior.',
    cast='Priya | Code reviewer\nTomas | Pull-request author',
    culture=('Critique the change, not the author', 'A useful review points to behavior and asks for a verifiable change. Acknowledge acceptable parts without letting praise obscure a defect. Separating naming from functionality lets the author respond to a concrete concern instead of defending personal competence.'),
    a='''What is the pull request titled? | Rename export helper | Rewrite notification policy | Remove all export tests | Release the importer | The stated title describes a helper rename, not a notification-policy change.
What additional change appears in the diff? | Notification moves outside the success branch | The export always succeeds | The failure branch is proven unreachable | Notifications are removed entirely | The changed call location permits notification after an unsuccessful export.
What part does Priya accept? | The naming change | The false success message | Missing failure coverage | Automatic production release | Priya accepts the rename while objecting to the changed notification behavior.''',
    vocabulary='''pull request | Proposed code change submitted for review; abbreviated PR. | review the pull request
diff | Display of changes between versions. | inspect the diff
review comment | Feedback attached to a proposed change. | write a review comment
success branch | Execution path entered when the relevant operation succeeds. | keep the call in the success branch
failure path | Execution path taken when an operation fails. | cover the failure path
call site | Location where a function or operation is invoked. | identify the call site
control flow | Order and conditions under which code executes. | trace the control flow
side effect | Observable effect beyond a function's returned value. | examine the side effect
completion notification | Message indicating an operation has finished successfully here. | gate the completion notification
behavior change | Alteration in what the system observably does. | flag the behavior change
refactor | Internal restructuring intended to preserve observable behavior. | separate a refactor from a behavior change
rename | Change to an identifier's name. | approve the rename
regression test | Test guarding against recurrence of a known defect. | add a regression test
assertion | Test statement checking an expected condition. | strengthen the assertion
blocking concern | Issue that must be resolved before approval under the review process. | explain the blocking concern
nonblocking suggestion | Improvement that does not prevent approval under the process. | label a nonblocking suggestion
review scope | Set of changes and concerns covered by a review. | clarify review scope
intent | Purpose the author means a change to achieve. | confirm the intent
observable behavior | Effect visible to a user or another component. | preserve observable behavior
false success | Indication of success when the operation did not succeed. | prevent false success
guard condition | Condition controlling whether an action may occur. | restore the guard condition
patch revision | Updated version of a proposed change. | request a patch revision
approval | Explicit acceptance at the relevant review stage. | withhold approval pending correction
verification evidence | Results supporting a claim that a change behaves as intended. | provide verification evidence''',
    precision='A rename can be acceptable while the same diff contains a blocking defect. Moving the notification outside the success branch changes observable behavior, so it is not merely a naming preference or a behavior-preserving refactor.',
    precision_extra='Make the request testable: restore success-only notification, then add a check that a failed export does not produce a completion notice. Do not substitute a general request to improve code quality for the specific observed issue.',
    phrases='''Acknowledge the acceptable part | The helper name is clear.
Locate the concern | This notification call has moved outside the success branch.
Describe the consequence | A failed export can now send a completion notice.
Separate preference and defect | My concern is behavior, not the naming choice.
Ask about intent | Was this control-flow change intentional?
State the expected boundary | The completion notice belongs on the success path.
Make a concrete request | Please restore the success-only condition.
Request evidence | Add a test for a failed export.
Specify the assertion | The failure case should not send a completion notification.
Avoid personal criticism | This change introduces a false-success path.
Clarify review status | I cannot approve this behavior yet.
Limit the objection | I am not asking you to undo the rename.
Distinguish scope | The diff does more than the title suggests.
Request a revision | Please update the patch and its description.
Keep verification separate | I will review the revised behavior and test.
Close constructively | The rename can stay once the notification issue is resolved.''',
    notes='''This call | Anchors the concern to a particular location in the change.
Can now | Identifies a newly possible behavior rather than a style preference.
Was ... intentional | Asks about purpose without assuming carelessness.
Not ... but | Separates the accepted naming issue from the behavioral objection.
Should not | States the negative assertion needed in the failure test.
Once | Makes approval conditional on a specific unresolved correction.''',
    d='''Which comment is actionable? | Restore the success-only notification and test that failure sends no completion notice | Your code is careless | Make this nicer | The name is fine, so everything is approved | The correct comment names the behavior, requested change, and verification.
Why is this not only a refactor? | Observable notification behavior changes | The helper has a new name | Review comments are present | The title is short | A behavior-preserving refactor would not add completion notices after failure.
What should the failure test assert? | No completion notice is sent | A completion notice always appears | Only the helper spelling is correct | Production release is approved | The defect concerns a false success message after export failure.
Which statement preserves Priya's position? | The rename is acceptable; the notification behavior needs correction | Every line must be reverted | The author cannot write software | The test can be omitted because the rename is small | Priya distinguishes an acceptable naming change from an unresolved behavioral defect.''',
    dialogue='''Priya | The new helper name makes sense to me. I have one blocking concern in the same diff: the completion-notification call has moved outside the success branch.
Tomas | I intended this as a [[rename::Rename identifies the accepted identifier change, which does not explain or justify the additional behavioral change.]], so I was not expecting a behavior objection. Can you point me to the consequence you are seeing rather than the name itself?
Priya | When export fails, execution can still reach that notification call. Users then receive a completion message even though the export did not complete successfully.
Tomas | I see the changed [[control flow::Control flow determines whether a failed export can reach the notification call after it moves outside the branch.]] now. The call used to depend on success, and the new position removes that condition. That was not my intended change.
Priya | Thanks. I am not asking you to undo the clearer name. I am asking for the notification to remain conditional on a successful export.
Tomas | So the concern is the [[side effect::Side effect refers to the externally visible notification rather than the helper's new name.]], not the naming style. I can keep the rename and restore the original success-only placement.
Priya | Yes. Please also add a test where export fails and verify that no completion notification is sent. The success case alone will not cover this problem.
Tomas | That gives the [[failure path::The failure path must be exercised to check that unsuccessful exports do not trigger a completion notice.]] an explicit expectation. I will not just assert that the helper was called; I need to check the notification does not happen.
Priya | Exactly. The review comment will identify the moved call, explain the false completion message, and request the condition and test. That should make the revision clear.
Tomas | I appreciate the specific [[review comment::A review comment is actionable when it identifies the changed location, effect, and requested correction.]]. A general request to improve the code would not tell me which behavior you need preserved.
Priya | The title also understates the current diff. Once you revise it, please make sure the description accurately reflects what remains and why the test was added.
Tomas | I will update the [[review scope::Review scope should reflect the actual remaining changes rather than rely solely on the original rename title.]] rather than assume the title proves this is harmless. Reviewers still need to examine the changed lines.
Priya | Calling the whole change a refactor would be misleading in its present form. A behavior-preserving change should not turn failed exports into apparent successes.
Tomas | Agreed. The [[false success::False success is the completion indication produced even though the export operation failed.]] is the defect here. It is separate from whether the new name is clearer or the patch is small.
Priya | After your revision, I will check the call placement and the failure assertion. Please include the test result, but do not describe my current feedback as approval.
Tomas | Understood. I will submit a [[patch revision::A patch revision is an updated proposed change, which still needs review rather than automatic approval.]] with the rename intact, the notification guarded by success, and evidence from the added test.
Priya | The test should be specific enough to fail if someone moves the call out again. Otherwise it could pass while the same user-visible problem returns.
Tomas | That makes it a useful [[regression test::A regression test should detect recurrence of the known false-notification defect rather than merely execute the helper.]]. I will check the negative notification expectation, not only that the test reaches the export code.
Priya | Good. My final comment will say the naming change is acceptable and the notification issue blocks approval until corrected and verified. That keeps the two points distinct.
Tomas | Then the next step is [[verification evidence::Verification evidence supports the revised behavior and is needed before the reviewer can resolve the blocking concern.]], not a debate about naming. I will revise the patch and return it for review with the relevant result.''',
    transfer_title='Turn a vague objection into a review request',
    transfer_setup='Complete the review summary while preserving the accepted rename and unresolved behavior issue.',
    transfer='''Reviewer: "The helper ___ is acceptable." | name | Priya explicitly accepts the naming change in the pull request.
Author: "The notification must remain on the ___ path." | success | Completion notification is intended only for a successful export here.
Reviewer: "Add a test for the ___ path." | failure | The regression occurs when export fails yet a completion notice appears.
Author: "The current feedback is not yet ___." | approval | The blocking behavior issue still requires correction and verification.''',
))


BOOK['units'].append(unit(
    title='Requesting dependency evidence',
    scene='A direct upgrade with an indirect change',
    skill='Request the resolved dependency version, affected call sites, and migration evidence before claiming upgrade compatibility.',
    brief='A fictional application uses ParcelKit directly. ParcelKit in turn uses TextCore. The proposed ParcelKit upgrade changes the resolved TextCore version. A change note marks a parsing entry point as deprecated. Developers Leila and Ben have not established whether the application or its dependencies use that entry point, whether it has been removed, or whether the replacement is compatible. The packages are not assumed to follow any particular versioning convention.',
    cast='Leila | Developer proposing the upgrade\nBen | Developer checking dependency impact',
    culture=('Ask what changed below the headline', 'An upgrade can affect more than the package named in the request. Asking for the resolved dependency tree and affected calls is a practical evidence request, not resistance to maintenance. Avoid translating deprecated into removed or compatible without checking the actual contract.'),
    a='''Which dependency does the application use directly? | ParcelKit | TextCore only | Both are proven direct | Neither | The application uses ParcelKit directly, while TextCore is introduced through ParcelKit.
What changes indirectly? | The resolved TextCore version | The application name | Every public interface | A confirmed production failure | The proposed ParcelKit upgrade changes the TextCore version selected in the dependency resolution.
What does the note establish? | A parsing entry point is deprecated | The replacement is fully compatible | The application definitely uses it | The entry point has definitely been removed | Deprecation is stated, but usage, removal, and replacement compatibility remain unverified.''',
    vocabulary='''direct dependency | Package explicitly used or declared by the application here. | upgrade a direct dependency
transitive dependency | Package brought in through another dependency. | inspect a transitive dependency
dependency tree | Structure showing how packages depend on one another. | inspect the dependency tree
resolved version | Specific version selected after dependency resolution. | record the resolved version
lockfile | File recording resolved dependency selections for reproducibility. | inspect the lockfile
version constraint | Rule limiting which dependency versions may be selected. | check a version constraint
release note | Published description of changes in a release. | read the release note
deprecation | Notice that an interface is discouraged or scheduled for replacement. | investigate a deprecation
removal | Elimination of a previously available interface or behavior. | verify removal separately
migration guide | Instructions describing transition to a changed interface. | consult the migration guide
entry point | Named interface through which functionality is invoked. | locate the parsing entry point
call site | Location that invokes a particular interface. | search for affected call sites
public interface | Supported surface exposed for other components to use. | compare the public interface
breaking change | Change that can invalidate previously supported use. | identify a breaking change
compatibility | Ability to work with the relevant existing consumers and behavior. | verify compatibility
semantic versioning | Version convention relating version numbers to public-interface changes. | confirm semantic versioning policy
major version | Leading version component under a stated convention. | interpret the major version
minor version | Version component whose meaning depends on the adopted convention. | check minor-version guarantees
patch version | Version component commonly used for fixes under a stated convention. | verify patch-version policy
pin | Fixed dependency selection restricting version movement. | review the version pin
changelog | Maintained record of notable changes between versions. | compare the changelog
replacement interface | Interface intended to supersede another. | assess the replacement interface
resolution | Process selecting concrete dependency versions. | reproduce dependency resolution
upgrade evidence | Records and checks supporting an upgrade assessment. | assemble upgrade evidence''',
    precision='Direct describes the application-to-ParcelKit relationship. Transitive describes the application-to-TextCore relationship through ParcelKit. The dependency actually selected matters, not just the version written in the top-level upgrade request.',
    precision_extra='Deprecated does not itself mean removed, unused, or compatible with a replacement. Version numbers provide guarantees only under the package policy that actually applies. Request usage and migration evidence before declaring the upgrade safe.',
    phrases='''Identify the direct dependency | The application uses ParcelKit directly.
Identify the indirect dependency | TextCore comes through ParcelKit.
Name the additional change | The resolved TextCore version also changes.
Request the actual selection | Which version does the lockfile record?
Ask for the relationship | Can you show the dependency tree?
Quote the narrow finding | The note marks the parsing entry point as deprecated.
Avoid an unsupported upgrade | Deprecated does not by itself mean removed.
Ask about usage | Do we have any affected call sites?
Include indirect callers | Check whether ParcelKit invokes it as well.
Request migration detail | What does the migration guide say about the replacement?
Separate availability and behavior | An available replacement is not automatically compatible.
Qualify the version inference | We need the package's actual versioning policy.
Request verification | Which checks exercise the affected parsing behavior?
Keep the decision open | We do not have enough evidence to claim compatibility.
State the pending work | Usage and replacement behavior still need review.
Close the request | Please attach the resolved versions and the relevant findings.''',
    notes='''Comes through | Expresses an indirect dependency relationship in ordinary speech.
Also changes | Exposes a second effect hidden by the top-level upgrade description.
By itself | Limits what the deprecation label establishes.
Whether | Leaves actual usage unresolved.
Not automatically | Challenges a shortcut inference without claiming the opposite.
Actual | Directs attention to the selected versions and applicable policy.''',
    d='''Which statement is accurate? | TextCore is transitive through ParcelKit | TextCore cannot affect the application | ParcelKit is only transitive | All transitive dependencies are unused | TextCore is brought into the application through its direct dependency ParcelKit.
What should be checked first about the selected version? | The resolved dependency record | Only the pull-request title | An unrelated package's policy | The latest version mentioned in a blog | The resolved record establishes the concrete TextCore version selected by this upgrade.
What does deprecated not establish? | That the entry point has been removed | That a transition may need review | That a note exists | That the interface deserves attention | Deprecation and removal are different statuses, and removal has not been established.
Which compatibility claim is justified now? | Compatibility remains unverified | The replacement is guaranteed identical | Every minor upgrade is safe | No call-site review is needed | Usage and replacement behavior have not yet been checked.''',
    dialogue='''Leila | I have proposed the ParcelKit upgrade. The headline change looks small, but the resolved dependency list also shows a different TextCore version.
Ben | Then we need to review the [[transitive dependency::TextCore is a transitive dependency because the application receives it through ParcelKit rather than using it directly here.]] change as well. The application uses ParcelKit directly, but that does not make TextCore irrelevant to its behavior.
Leila | I can attach the resolved versions before and after. Would the package declaration alone be enough, or do you want the selection recorded by the build?
Ben | Please include the [[lockfile::The lockfile records resolved dependency selections and is more specific than a top-level version constraint alone.]] and the relevant dependency relationship. A constraint can allow several versions, while the resolved record tells us which one this change actually selects.
Leila | There is also a note about a deprecated parsing entry point. I have not found whether we call it or whether ParcelKit calls it internally.
Ben | Keep that as a [[deprecation::Deprecation marks an interface for discouragement or transition but does not alone establish removal or current usage.]] finding, not a removal finding. The note deserves investigation, but its label alone does not tell us whether this application is affected.
Leila | So I should not write that the upgrade removes a parser we use. Both removal and our usage are still unverified.
Ben | Correct. Start by locating any relevant [[call site::A call site shows where the affected parsing interface is invoked, which must be checked rather than assumed.]], including indirect calls through ParcelKit. An absence of direct application calls would not automatically rule out an indirect dependency on that behavior.
Leila | If there is a replacement entry point, could I simply switch to it? The name suggests it does the same kind of parsing.
Ben | Consult the [[migration guide::The migration guide provides transition details that a similar replacement name cannot establish.]] first. Similar names do not establish identical inputs, outputs, error behavior, or handling of edge cases. We need the relevant documented differences.
Leila | I was also tempted to rely on the version number. The upgrade request does not tell us what versioning policy these packages follow.
Ben | Then do not assume [[semantic versioning::Semantic versioning provides specific conventions only when the relevant project actually adopts and follows that policy.]] guarantees. We can check the actual policy, but a familiar number pattern is not evidence that its promised compatibility rules apply.
Leila | I will separate the questions: selected versions, affected usage, the old interface status, and the replacement's behavior. That should keep the review focused.
Ben | Good. The [[dependency tree::The dependency tree makes the ParcelKit-to-TextCore relationship visible so indirect impact is included in the review.]] will help explain why TextCore belongs in the discussion even though the request is named after ParcelKit.
Leila | What should the test evidence cover once we identify the affected calls? Running the existing suite is useful, but I do not know whether it reaches them.
Ben | Ask which checks exercise the relevant [[public interface::The public interface is the exposed parsing surface whose supported behavior and affected callers need verification.]]. A passing suite cannot establish coverage of a path it never executes.
Leila | That makes sense. I can list any coverage gap explicitly instead of using all tests passed as a blanket compatibility claim.
Ben | Exactly. We need [[upgrade evidence::Upgrade evidence combines actual versions, affected usage, documentation, and relevant checks rather than a broad assertion of safety.]] tied to this change. It should show what was checked and what remains unknown, not just that an upgrade command succeeded.
Leila | My revised summary will say ParcelKit changes the resolved TextCore version, the parsing entry point is deprecated, and usage and replacement behavior still need review.
Ben | That is accurate. Keep [[compatibility::Compatibility remains unverified until the relevant consumers and behavior have been checked against the proposed versions.]] unverified for now. Once those findings are available, we can discuss the upgrade on evidence rather than infer its impact from the headline.''',
    transfer_title='Keep the dependency chain and uncertainty intact',
    transfer_setup='Complete the upgrade handoff without turning deprecation into confirmed removal or compatibility.',
    transfer='''Developer: "ParcelKit is the ___ dependency." | direct | The application uses ParcelKit directly under the stated dependency relationship.
Reviewer: "TextCore is the ___ dependency." | transitive | TextCore is introduced through ParcelKit rather than directly here.
Developer: "The parsing entry point is marked ___." | deprecated | The change note establishes deprecation, not removal or usage.
Reviewer: "Replacement compatibility remains ___." | unverified | The relevant behavior and affected callers have not yet been checked.''',
))

BOOK['units'].append(unit(
    title='Explaining what a test actually exercises',
    scene='A green test that never sees rejection',
    skill='Explain the limits of a success-only test double and distinguish a failure-path unit test from real-adapter integration coverage.',
    brief='A save-operation unit test uses a storage double that always succeeds and checks the success message. A previous bug showed success after storage rejected the save. The current test never produces rejection, and the real storage adapter is untested. Developers Owen and Farah need to configure a rejection case, assert that false success does not appear, and keep real-adapter integration coverage as a separate unresolved concern.',
    cast='Owen | Developer maintaining the test\nFarah | Developer reviewing coverage',
    culture=('A passing result needs a scope statement', 'Green is a useful status, but it is not a complete explanation. Name the behavior the test actually exercises and the dependencies it replaces. This allows a colleague to request missing coverage without denying the value of existing tests.'),
    a='''What does the storage double currently do? | Always succeeds | Rejects every request | Uses the real adapter | Alternates unpredictably | The supplied test double is configured only for successful storage.
What did the previous bug show? | Success after storage rejected the save | Failure after a confirmed save | A missing helper name | A proven adapter timeout | The prior defect was a false success indication after rejection.
What remains separately untested? | The real storage adapter | Whether the test shows a success message | The existence of the double | Every application feature | The scenario explicitly states that the real adapter has not been tested.''',
    vocabulary='''unit test | Focused test of a small behavior or component. | extend the unit test
test double | Substitute for a real dependency during testing. | configure the test double
stub | Test substitute supplying predetermined responses. | use a success stub
mock | Test substitute that can record or check interactions. | inspect mock interactions
fixture | Prepared state or data used by a test. | arrange the fixture
success response | Result indicating an operation succeeded. | return a success response
rejection | Failed outcome reported by the storage operation here. | simulate a rejection
exception | Error signal raised during execution under the relevant model. | configure an exception
assertion | Explicit check of an expected test condition. | add a negative assertion
negative assertion | Check that an unwanted event or state does not occur. | verify a negative assertion
test isolation | Separation of a tested unit from unrelated dependencies. | preserve test isolation
integration test | Test of interaction between connected components. | add an integration test
adapter | Component translating between an application and an external interface. | test the storage adapter
branch coverage | Measure of which decision outcomes a test set executes. | examine branch coverage
happy path | Expected successful execution path. | cover the happy path
error path | Execution path handling an unsuccessful operation. | exercise the error path
false negative | Test result that misses a defect which is present. | avoid a false negative
test oracle | Rule or reference used to judge the expected result. | define the test oracle
arrange | Prepare the conditions for a test. | arrange a rejection case
act | Execute the behavior being tested. | act on the save request
assert | Check the observed result against the expectation. | assert no false success
interaction verification | Check of how a component called its dependencies. | separate interaction verification
behavioral verification | Check of the externally observable result. | perform behavioral verification
coverage gap | Relevant behavior not exercised by the current tests. | report the coverage gap''',
    precision='A double that always succeeds can support a success-path assertion, but it cannot exercise rejection handling. Configure a failing response and check the user-visible consequence relevant to the known bug.',
    precision_extra='The rejection unit test can verify application behavior against a simulated storage outcome. It does not establish that the real adapter produces that outcome correctly or that the actual integration behaves the same way.',
    phrases='''Describe the current setup | The storage double always succeeds.
Name the tested path | This test exercises the happy path.
Recall the defect | The bug showed success after a rejected save.
Identify the gap | The current test never triggers rejection.
Request a configured outcome | Make the double reject in a separate case.
Specify the check | Assert that no success message appears after rejection.
Preserve existing coverage | Keep the successful-save case too.
Separate call and result | A storage call alone does not prove the right user message.
Name the substitute | This is a double, not the real adapter.
Limit the conclusion | The result applies to the simulated rejection case.
Request another test level | The real adapter needs separate integration coverage.
Avoid a blanket claim | Green tests do not establish all storage behavior.
State the open question | We have not verified the real adapter.
Ask about expectations | What observable result should this case check?
Request evidence | Please include the configured outcome and assertion.
Close accurately | The new unit case can close one gap, not every storage risk.''',
    notes='''Always | Exposes a fixture that cannot produce the missing failure condition.
After rejection | Connects the assertion to the relevant event sequence.
Separate case | Preserves success coverage while adding failure coverage.
Alone | Limits what a dependency-call assertion can demonstrate.
Simulated | Marks the boundary between a double and real integration.
One gap | Avoids overstating the scope of the proposed improvement.''',
    d='''Why does the current test miss the prior bug? | Its double never rejects | Its name contains save | Every unit test uses production storage | Success messages cannot be tested | The failing condition required to expose the bug is absent from the fixture.
Which addition targets the defect? | Configure rejection and assert no success message | Rename the success test only | Check only that storage is called | Remove all assertions | The new case must trigger rejection and verify the missing user-visible boundary.
What does the rejection unit test not establish? | Correct behavior of the real storage adapter | Behavior under the configured double response | Whether the assertion passes in that case | Whether the fixture rejects | The test still substitutes for the real adapter rather than exercising it.
Which report is precise? | Success-path coverage exists; rejection and real-adapter coverage need work | All storage behavior is verified | A green test proves no bugs remain | Rejection cannot be simulated | The report separates existing coverage from two distinct unresolved areas.''',
    dialogue='''Owen | The save test is green, but I am not sure it would catch the old bug. It checks the success message after the storage double returns success.
Farah | Then it exercises the [[happy path::The happy path is the successful execution route supplied by the always-successful storage double.]]. What happens in the test when storage rejects the save, which was the condition behind the earlier false success message?
Owen | Nothing produces rejection in the current fixture. The double always succeeds, so that condition is never reached. I should not claim the old defect is covered.
Farah | Right. The [[test double::The test double replaces real storage and must be configured to produce the rejection needed by this test.]] is useful, but its configured behavior limits the test. We need a separate case that makes storage report the relevant unsuccessful outcome.
Owen | I can add that case while preserving the successful-save test. Then the new check should concern the displayed result, not just whether storage was called.
Farah | Add a [[negative assertion::A negative assertion checks that the unwanted success message does not appear after the simulated rejection.]] that no success message appears after rejection. Calling storage is compatible with both correct handling and the old bug.
Owen | That distinction helps. A call-count check could pass even if the application ignored the rejected result and displayed completion anyway.
Farah | Exactly. [[Interaction verification::Interaction verification checks dependency calls but does not alone establish the correct user-visible result.]] is not the same as verifying the resulting message. The assertion needs to match the defect we are trying to prevent.
Owen | Should I describe the new case as an integration test? It crosses from the save operation to the storage interface, but the real adapter is still replaced.
Farah | No. The relevant [[integration test::An integration test would exercise the relevant connected components, whereas this case still replaces the real storage adapter.]] would need to exercise the actual components whose interaction you are claiming to verify. This proposed case still uses a substitute.
Owen | Then I will state that it checks application behavior under a simulated rejection. It does not establish how the real adapter responds.
Farah | That keeps the [[coverage gap::The coverage gap for the real adapter remains open even if the simulated rejection unit case passes.]] visible. We know the real adapter is untested, and changing the double does not make that separate fact disappear.
Owen | For the new case, I will prepare the rejection response, execute the save, and inspect the resulting user message. That gives the test a clear sequence.
Farah | Yes: [[arrange::Arrange is the preparation stage that configures the rejection condition before the save behavior is executed.]] the condition, act on the save request, and assert the expected result. Keep the failure setup explicit so reviewers can see what the test really exercises.
Owen | The success-only test was not worthless, then. Its result was simply being described too broadly as proof of the whole storage workflow.
Farah | Correct. It provides evidence for its [[success response::Success response is the outcome configured in the existing test, so its evidence is limited to that path.]] case. The problem is the wider claim, not the existence of a focused test for a successful save.
Owen | When I report the new result, I will name the double's configured outcome and the no-success assertion. I will list actual adapter behavior separately as unverified.
Farah | Good. That is [[behavioral verification::Behavioral verification checks the observed application result, while retaining the boundary imposed by the substituted dependency.]] within a clear boundary. Avoid saying storage is fully tested when the evidence concerns only these simulated responses.
Owen | The handoff will retain the happy-path test, add the rejection case, and call out the missing real-adapter check. Approval still depends on reviewing the actual revision.
Farah | Exactly. A targeted [[unit test::A unit test can cover the application's rejection handling without proving the behavior of the real storage integration.]] closes a specific omission. We should welcome that improvement while remaining precise about what it does and does not demonstrate.''',
    transfer_title='Name the test boundary',
    transfer_setup='Complete the review note about the current test and the proposed rejection case.',
    transfer='''Developer: "The existing double always ___." | succeeds | The current fixture supplies only successful storage outcomes to the save operation.
Reviewer: "The new case must trigger ___." | rejection | Rejection is the missing condition that exposed the previous false-success bug.
Developer: "The assertion should prevent a false ___ message." | success | The known defect incorrectly displayed success after storage rejected the save.
Reviewer: "The real adapter remains ___." | untested | Simulated rejection coverage does not exercise the real storage adapter.''',
))


BOOK['units'].append(unit(
    title='Comparing performance tradeoffs fairly',
    scene='Fifteen milliseconds faster, forty megabytes over budget',
    skill='Compare measured latency and memory under matched conditions while separating median improvement from budget compliance and production claims.',
    brief='In a controlled benchmark using the same input and machine, implementation A has median latency of 40 milliseconds and memory use of 80 megabytes. B has median latency of 25 milliseconds and memory use of 160 megabytes. The memory budget is 120 megabytes. Developers Sora and Malik discuss the tradeoff. Tail latency and production behavior have not been measured. B reduces the measured median by 15 milliseconds, or 37.5 percent relative to A, but exceeds the memory budget by 40 megabytes.',
    cast='Sora | Developer presenting the benchmark\nMalik | Developer reviewing the tradeoff',
    culture=('Do not hide a constraint inside a headline', 'Faster is incomplete when a resource budget matters. State the metric, conditions, comparison baseline, and constraint together. A colleague can acknowledge a genuine latency improvement while rejecting the claim that it settles the overall implementation decision.'),
    a='''Which conditions are matched? | Input and machine | Production traffic and every user | All future workloads | Tail-latency percentiles | The benchmark explicitly uses the same input and machine for both implementations.
How far is B over the memory budget? | 40 megabytes | 15 megabytes | 80 megabytes | It is under budget | B uses 160 megabytes against a budget of 120, exceeding it by forty.
What is unmeasured? | Tail latency and production behavior | The stated median values | The stated memory values | The budget difference | Only the benchmark median and memory figures are supplied, not tail or production results.''',
    vocabulary='''benchmark | Structured measurement under specified conditions. | run a benchmark
latency | Time taken for a request or operation. | measure latency
median | Middle value of an ordered set of measurements. | report median latency
tail latency | Slower-end behavior in a latency distribution. | measure tail latency
percentile | Value below which a stated percentage of observations falls. | report a latency percentile
p95 | Ninety-fifth percentile of a measured distribution. | distinguish p95 from the median
throughput | Amount of work completed per unit of time. | measure throughput separately
memory footprint | Amount of memory used under the stated conditions. | compare the memory footprint
resource budget | Allowed limit for a specified resource. | respect the resource budget
headroom | Remaining capacity below a stated limit. | calculate memory headroom
overrun | Amount by which usage exceeds a limit. | quantify the budget overrun
baseline | Reference implementation or measurement for comparison. | use A as the baseline
relative reduction | Decrease expressed as a fraction of the original value. | calculate the relative reduction
absolute difference | Direct numerical subtraction between comparable measurements. | report the absolute difference
tradeoff | Gain in one property accompanied by a cost in another. | explain the tradeoff
workload | Type and amount of work applied to a system. | describe the workload
sample | Set of observations used in an analysis. | document the sample
distribution | Pattern of observed values across a range. | inspect the latency distribution
outlier | Observation unusually distant from most other values. | investigate an outlier
measurement noise | Variation not attributable to the intended comparison alone. | account for measurement noise
controlled conditions | Specified conditions held consistent during comparison. | preserve controlled conditions
production behavior | Behavior under actual live operating conditions. | avoid assuming production behavior
bottleneck | Constraint limiting overall system performance. | identify the bottleneck
budget compliance | Whether measured usage satisfies the stated limit. | check budget compliance''',
    precision="B reduces the median from 40 to 25 milliseconds: a 15-millisecond difference and a 37.5 percent reduction relative to A. It uses twice A's measured memory, but doubling memory is not the same as doubling speed.",
    precision_extra='A uses 80 megabytes, leaving 40 below the 120-megabyte budget. B uses 160, exceeding it by 40. Neither median describes the unmeasured tail, and neither controlled result establishes production behavior.',
    phrases='''Name the conditions | Both runs use the same input and machine.
State A | A has a forty-millisecond median and uses eighty megabytes.
State B | B has a twenty-five-millisecond median and uses one hundred sixty megabytes.
Report the absolute gain | B lowers the median by fifteen milliseconds.
Name the baseline | That is a thirty-seven-point-five percent reduction relative to A.
Report the cost | B uses twice A's measured memory.
State the constraint | The memory budget is one hundred twenty megabytes.
Calculate the overrun | B exceeds that budget by forty megabytes.
Calculate the headroom | A remains forty megabytes below the limit.
Avoid a vague verdict | B is faster on this median measure, not automatically better overall.
Limit the metric | The median does not tell us the tail latency.
Name the missing evidence | We have not measured production behavior.
Separate throughput | These figures do not establish throughput.
Request a balanced summary | Put the latency gain and memory cost together.
Keep the decision bounded | The measured gain does not remove the budget constraint.
Close without overclaiming | We have a documented tradeoff, not a production guarantee.''',
    notes='''Relative to A | Names the denominator for the percentage comparison.
By versus to | By gives the change; to gives the resulting value.
Twice | Compares B's memory with A's, not with the budget.
On this measure | Limits a faster claim to the reported metric.
Does not tell us | Prevents inference from median to unmeasured tail behavior.
Not automatically | Preserves the benefit while resisting an overall conclusion.''',
    d='''What is B's median reduction relative to A? | 37.5 percent | 60 percent | 15 percent | 100 percent | Fifteen divided by the forty-millisecond baseline equals 0.375, or 37.5 percent.
Which budget statement is correct? | A is 40 below and B is 40 above | Both are within budget | B is 80 below budget | A is 40 above budget | The 120-megabyte limit lies forty above A and forty below B.
Which claim exceeds the evidence? | B improves every production request | B has a lower measured median | B uses more measured memory | The benchmark used the same machine | Production behavior and every-request outcomes have not been measured.
Which summary is balanced? | B lowers median latency but exceeds the memory budget; tail and production remain unmeasured | B is universally superior | A is faster in the supplied test | Memory no longer matters because latency improved | The summary combines the measured benefit, resource constraint, and remaining evidence limits.''',
    dialogue='''Sora | The benchmark gives B a lower median: twenty-five milliseconds against A's forty. Both used the same input and machine, so the comparison conditions are matched.
Malik | That is useful [[benchmark::Benchmark identifies the controlled measurement, whose conditions limit the scope of the comparison.]] evidence. Put the memory figures beside it before we call B the better option. The resource budget is part of this decision.
Sora | A uses eighty megabytes and B uses one hundred sixty. The budget is one hundred twenty, so B does not fit the stated limit.
Malik | Right. Its [[memory footprint::Memory footprint is the measured memory usage, which is 160 megabytes for B against a 120-megabyte budget.]] is twice A's and forty megabytes over budget. The latency improvement does not cancel that constraint.
Sora | I want the percentage wording right. The median drops by fifteen milliseconds from a forty-millisecond baseline, which is a thirty-seven-point-five percent reduction.
Malik | Yes, that is the [[relative reduction::Relative reduction divides the fifteen-millisecond decrease by A's forty-millisecond baseline, yielding 37.5 percent.]] relative to A. Keep the baseline explicit so nobody divides by twenty-five and reports a different quantity under the same label.
Sora | Could I say B is thirty-seven-point-five percent faster? That sounds more compact, but I can see it might blur latency with another speed measure.
Malik | Prefer the precise [[absolute difference::Absolute difference is the direct fifteen-millisecond reduction, which can be reported alongside the relative latency reduction.]] and percentage latency reduction. Those statements tell readers exactly which measurement changed without suggesting an unmeasured throughput result.
Sora | We also have no tail-latency data. The median does not tell us whether the slowest requests improved or became worse.
Malik | Correct. [[Tail latency::Tail latency concerns slower-end observations and cannot be inferred from the supplied median alone.]] remains unmeasured. Do not turn a better middle value into a claim about every request or a specific percentile we did not record.
Sora | For A, the memory calculation goes the other way: eighty against a limit of one hundred twenty leaves forty megabytes available.
Malik | That is forty megabytes of [[headroom::Headroom is the forty-megabyte difference between A's eighty-megabyte usage and the 120-megabyte limit.]] under the stated budget. It is a different claim from saying A has more memory available under all possible workloads.
Sora | Should the summary mention production explicitly? These measurements come from the controlled comparison, and we have not collected live-environment results.
Malik | Yes. [[Production behavior::Production behavior remains unmeasured, so the controlled benchmark cannot establish live-system outcomes.]] is not established by these figures. Name that limit instead of relying on readers to infer it from the word benchmark.
Sora | Then the headline should combine the gain and cost: lower measured median, higher memory, and a budget violation for B.
Malik | That presents the [[tradeoff::Tradeoff connects B's lower median latency with its higher memory use and failure to meet the stated budget.]] fairly. It acknowledges a real improvement without treating one favorable number as a complete engineering decision.
Sora | I will not ask for the budget to disappear from the table. If someone proposes a different limit, that would be another decision, not a property of this measurement.
Malik | Exactly. Current [[budget compliance::Budget compliance is evaluated against the stated 120-megabyte limit, which B exceeds regardless of its latency gain.]] is clear: A is below the limit and B is above it. A hypothetical future budget should not rewrite today's comparison.
Sora | My final summary will report both values, the fifteen-millisecond decrease, the memory difference, and the missing tail and production measurements.
Malik | Good. Keep the [[controlled conditions::Controlled conditions specify the matched input and machine and prevent the result being generalized without further evidence.]] visible alongside that summary. We can make a reasoned next decision without pretending the benchmark answers questions it never measured.''',
    transfer_title='Report both sides of the comparison',
    transfer_setup='Use the supplied numbers to complete the benchmark summary. Units are printed in each sentence.',
    transfer='''Developer: "B's median is ___ milliseconds." | 25 | The measured median for implementation B is twenty-five milliseconds.
Reviewer: "The median decreases by ___ milliseconds relative to A." | 15 | Forty minus twenty-five gives a fifteen-millisecond absolute decrease.
Developer: "B uses ___ megabytes of memory." | 160 | The supplied memory measurement for implementation B is 160 megabytes.
Reviewer: "B exceeds the budget by ___ megabytes." | 40 | One hundred sixty minus the 120-megabyte budget leaves forty over.''',
))

BOOK['units'].append(unit(
    title='Discussing retries and shared state',
    scene='The timeout did not answer the business question',
    skill='Explain an uncertain request outcome and request a retry contract before risking a second reservation.',
    brief="A fictional reservation client times out before receiving a reply. The service may already have created the reservation. A proposed automatic retry would submit a new reservation request, and the service's duplicate-handling behavior is unspecified. Developers Imani and Leo discuss the risk. No production change is authorized. They need to clarify outcome reconciliation and retry semantics, then test agreed behavior in a suitable controlled environment.",
    cast='Imani | Client developer\nLeo | Service developer',
    culture=('Distinguish not knowing from knowing failure', 'Timeout language can silently collapse uncertainty into failure. Say what the client observed and what the service may have done. This makes a request for an explicit retry contract sound like necessary coordination rather than unnecessary caution.'),
    a='''What did the client observe? | No reply before its timeout | Confirmed rejection before processing | Confirmed creation twice | A verified cancellation | A timeout establishes lack of a timely reply, not the service's final action.
What might the service have done? | Created the reservation already | Definitely done nothing | Guaranteed cancellation | Automatically merged duplicates | The scenario explicitly leaves prior creation possible and unresolved.
What is unspecified? | Duplicate-handling behavior for the proposed retry | Whether the client timed out | Whether the retry is proposed as new | Whether production authorization exists | The service's treatment of duplicate requests is not defined in the supplied contract.''',
    vocabulary='''timeout | End of a waiting period without the required response. | observe a timeout
retry | Repeated attempt after an earlier uncertain or unsuccessful attempt. | define retry behavior
request identity | Identifier or meaning used to distinguish one operation from another. | preserve request identity
idempotency | Property allowing repeated equivalent requests without additional intended effects. | specify idempotency semantics
idempotency key | Identifier used under an agreed contract to recognize repeated intent. | define an idempotency key
duplicate request | Repeated request that may represent the same intended operation. | detect a duplicate request
duplicate side effect | Additional effect caused by repeating an operation. | prevent a duplicate side effect
shared state | Data or condition used by multiple participants or operations. | reconcile shared state
uncertain outcome | Situation where the operation's final result is not known. | report an uncertain outcome
acknowledgment | Response indicating receipt or completion as defined by the protocol. | distinguish an acknowledgment
reconciliation | Checking records to establish and align the actual outcome. | request outcome reconciliation
at-least-once delivery | Delivery model allowing one or more deliveries of a message. | discuss at-least-once delivery
at-most-once delivery | Delivery model allowing no more than one delivery, with possible loss. | distinguish at-most-once delivery
deduplication | Recognition and handling of repeated requests or records. | define deduplication behavior
race condition | Behavior depending on timing among concurrent operations. | investigate a race condition
concurrency | Overlapping progress of multiple operations. | account for concurrency
atomic operation | Operation treated as an indivisible state change under its model. | define the atomic operation
transaction boundary | Scope within which specified changes are coordinated. | clarify the transaction boundary
backoff | Delay strategy between repeated attempts. | configure retry backoff
retry budget | Limit on permitted repeated attempts under a policy. | set a retry budget
correlation identifier | Identifier linking related events across components. | retain the correlation identifier
status lookup | Query intended to retrieve an operation's recorded state. | define a status lookup
sandbox | Controlled environment separated from live operations. | test in a sandbox
authorization | Permission for a specified action or change. | obtain production authorization''',
    precision="A timeout describes the client's wait, not proof that the service did nothing. Submitting a new reservation could create another business effect if the first request already succeeded and duplicate handling is not defined.",
    precision_extra='An idempotency key is not a magic guarantee. Its scope, reuse rules, retention, responses, and service behavior need a contract. Backoff changes timing; it does not by itself resolve an uncertain outcome or prevent duplication.',
    phrases='''State the observation | The client timed out before receiving a reply.
Preserve uncertainty | The service may already have created the reservation.
Avoid a false conclusion | No reply does not prove no reservation.
Identify the proposal | The retry would submit a new reservation request.
Name the risk | That could create a duplicate business effect.
Ask for the contract | How does the service recognize repeated intent?
Avoid assuming support | Duplicate handling is not specified.
Clarify identity | Would this carry the same request identity or a new one?
Request reconciliation | Can we establish the outcome of the first request?
Separate timing and semantics | Backoff does not itself prevent duplicates.
Qualify the key | An idempotency key needs agreed service behavior.
State the permission boundary | No production change is authorized.
Request a controlled check | Test the agreed behavior in a suitable sandbox.
Name the missing evidence | We do not know whether the first reservation exists.
Keep the design provisional | Automatic retry remains a proposal.
Close with the dependency | Define the contract before claiming retry safety.''',
    notes='''May already have | Expresses a possible completed action whose result is not yet known.
Does not prove | Blocks an invalid inference from silence to failure.
Could create | Names a risk without falsely asserting duplication already occurred.
Same ... or new | Exposes request identity as a design decision.
By itself | Limits what backoff or a key can guarantee alone.
Before claiming | Makes a confidence statement dependent on missing contract evidence.''',
    d='''Which statement follows from the timeout? | The client did not receive a timely reply | No reservation exists | Two reservations definitely exist | The service canceled the request | A client timeout leaves the service-side result uncertain.
Why is a new reservation request risky? | The first may already have created a reservation | Every retry always duplicates | The client has confirmed cancellation | Backoff guarantees a second failure | A repeated new operation may add another effect while the first outcome remains unknown.
What does an idempotency key require? | Agreed service semantics | Only a convenient label | No server participation | Automatic universal guarantees | A key is useful only when the service contract defines how repeated intent is handled.
Which next step is appropriate? | Clarify reconciliation and retry behavior, then test it outside production | Enable the retry in production immediately | Assume timeout means rejection | Promise exactly one reservation without evidence | The contract and controlled evidence are missing, and production changes are not authorized.''',
    dialogue='''Imani | The reservation client timed out before it received a reply. I have a proposal to retry automatically, but it currently submits the second attempt as a new reservation.
Leo | We need to preserve the [[uncertain outcome::Uncertain outcome means the first reservation may exist even though the client did not receive a timely response.]] of the first attempt. The service may already have created it, so the timeout is not proof that nothing happened.
Imani | That is the gap in my current explanation. I described the request as failed, when what I actually know is that the client stopped waiting.
Leo | Exactly. A [[timeout::Timeout describes expiration of the client's wait, not a confirmed service-side rejection or absence of a reservation.]] is an observation at the client. We need separate evidence about the service state before turning that into a business conclusion.
Imani | If the first reservation exists, the new request might create another. We do not have documented behavior saying the service will recognize it as the same intent.
Leo | Then [[deduplication::Deduplication behavior is unspecified, so repeated intent cannot be assumed to produce only one reservation.]] must remain unspecified in the proposal. We cannot promise the second request will be merged or ignored just because the input looks similar.
Imani | Would adding a request key solve it? I have heard teams describe keys as making retries safe, but I do not know this service's rules.
Leo | An [[idempotency key::An idempotency key needs a defined service contract for repeated intent rather than merely being added to a request.]] needs agreed semantics on the service side. A new field alone does not tell us its scope, reuse rules, or what response a repeat receives.
Imani | We should also be clear whether the retry represents the original operation or a genuinely new booking. Giving it a new identity could contradict our intended behavior.
Leo | Yes. Define the [[request identity::Request identity distinguishes a repeated attempt at the original operation from a new reservation with another intended effect.]] and how the service interprets it. That distinction belongs in the contract, not in an assumption hidden inside the client's retry loop.
Imani | Before another attempt, could we establish the first result through a supported status check? I do not want to invent an endpoint that this service may not have.
Leo | Request an agreed [[status lookup::Status lookup is a possible reconciliation mechanism that must actually be supported and defined rather than invented.]] or another supported reconciliation process. Its availability and meaning need confirmation; we have not established either in this discussion.
Imani | Someone suggested adding a delay between attempts. That could reduce repeated traffic, but it would not tell us whether the first reservation already exists.
Leo | Correct. [[Backoff::Backoff changes timing between attempts but does not itself establish the earlier outcome or prevent duplicate business effects.]] is a timing policy, not a substitute for outcome and duplicate-handling semantics. A slower duplicate is still a possible duplicate.
Imani | I will revise the proposal around those unresolved questions. There is no permission to enable the automatic retry in production while we investigate.
Leo | Keep that [[authorization::Authorization is explicitly absent for production changes, so investigation must not be described as permission to enable the retry.]] boundary visible. Once the contract is defined, we can plan a controlled check without changing live reservation behavior.
Imani | The test should cover a reply arriving too late after the service may have completed the operation, not only an immediate rejection before any work.
Leo | That will address the relevant [[shared state::Shared state is the reservation state whose service-side result may differ from what the timed-out client knows.]] uncertainty. Use a suitable sandbox and define the expected outcome before interpreting the test as evidence.
Imani | My summary is no timely reply, first outcome unknown, proposed retry currently new, duplicate handling unspecified, and no production change approved.
Leo | Good. We need [[reconciliation::Reconciliation establishes the actual first-request outcome and supports a defined retry decision rather than assuming failure from silence.]] and an explicit retry contract before claiming safety. That is the concrete next discussion, not a guarantee that an extra attempt will be harmless.''',
    transfer_title='Do not turn silence into failure',
    transfer_setup='Complete the retry discussion using the stated uncertainty and permission boundary.',
    transfer='''Developer: "The client observed a ___." | timeout | The client stopped waiting before it received the service reply.
Reviewer: "The first reservation may already ___." | exist | The service may have completed creation before the client timed out.
Developer: "Duplicate handling remains ___." | unspecified | The service contract supplies no duplicate-handling behavior for this proposal.
Reviewer: "No production change is ___." | authorized | The scenario explicitly withholds permission to enable a live change.''',
))

BOOK['units'].append(unit(
    title='Handing over a release with explicit limits',
    scene='R18 is deployed, but the release decision is not made',
    skill='Hand over environment, flag state, migration limits, and decision ownership without conflating deployment with production readiness.',
    brief='Release R18 is deployed in staging. Its new search feature is disabled by a feature flag. A migration adds an optional field, but compatibility with the previous application version has not been tested. Developer Chen hands the status to release reviewer Lee. The production decision remains with Lee and has not been made. Neither the optional field nor the staging deployment establishes that an older application will safely work with the migrated data.',
    cast='Chen | Developer handing over R18\nLee | Release reviewer',
    culture=('Say done with an object attached', 'Deployed, enabled, tested, and approved describe different milestones. Attach each status to an environment, feature, or specific check. This reduces pressure on the next person to infer readiness from a single broad word such as ready or complete.'),
    a='''Where is R18 deployed? | Staging | Production | Every customer environment | Nowhere | The scenario establishes a staging deployment only, not production deployment.
What is the new search feature's state? | Disabled by a feature flag | Enabled for all users | Deleted from the release | Proven compatible with every client | The search feature is present but disabled by its flag.
Which check is unresolved? | Compatibility with the previous application version | Whether the staging deployment occurred | Whether the field is optional | Who owns the production review | Compatibility with the prior application has not been tested.''',
    vocabulary='''release candidate | Version proposed for release pending the relevant checks. | review the release candidate
deployment | Placement of software into a specified environment. | report the deployment
staging | Preproduction environment used for relevant checks. | deploy to staging
production | Live environment serving actual operational users or workloads. | authorize production release
feature flag | Control that enables or disables specified behavior. | verify the feature flag
disabled state | Condition in which a feature is not enabled. | preserve the disabled state
rollout | Process of making a change available to intended users. | plan the rollout
migration | Change to stored data or its structure. | review the migration
optional field | Field that may be absent under the applicable rules. | add an optional field
schema compatibility | Ability of components to work with the relevant data structure. | verify schema compatibility
previous version | Earlier application version relevant to the comparison. | test the previous version
rollback | Return to an earlier application or system state under a defined plan. | assess rollback readiness
forward compatibility | Ability to work with relevant newer data or interfaces. | check forward compatibility
backward compatibility | Ability to preserve supported use by earlier consumers. | verify backward compatibility
release gate | Required condition before advancing a release. | satisfy the release gate
sign-off | Explicit approval at a stated decision point. | obtain release sign-off
go/no-go decision | Decision whether to proceed under the relevant release process. | record the go/no-go decision
handoff | Transfer of relevant status, evidence, and responsibility. | prepare the release handoff
known limitation | Identified restriction or unresolved boundary. | list known limitations
verification matrix | Organized record of combinations and checks to be verified. | update the verification matrix
environment boundary | Limit separating claims about different execution settings. | preserve the environment boundary
data compatibility | Ability to interpret and use the relevant stored data correctly. | test data compatibility
release owner | Person responsible for the specified release decision. | name the release owner
readiness claim | Statement that required conditions for proceeding are met. | qualify the readiness claim''',
    precision="R18 is deployed in staging, and search is disabled. Those are two separate facts. They do not imply production deployment, enabled search, completed compatibility testing, or Lee's approval to proceed.",
    precision_extra='An optional new field may look low risk, but its optional status does not prove an older application can handle the changed data or schema. Rollback readiness requires evidence about the earlier version and the actual post-migration state.',
    phrases='''Identify the release | This handoff concerns R18.
Name the environment | R18 is deployed in staging.
Name the feature state | New search remains disabled by its flag.
Separate deployment and use | Deployed does not mean enabled.
Describe the data change | The migration adds an optional field.
State the missing check | Compatibility with the previous application version is untested.
Avoid a shortcut | Optional does not prove compatibility.
Name the decision owner | Lee owns the production review.
Keep the decision open | The production decision has not been made.
Limit the readiness claim | This is a staging status, not production sign-off.
Request the exact evidence | Check the previous application against the migrated state.
Separate rollback assumptions | An older build alone does not establish rollback readiness.
Identify the pending item | The compatibility check remains open.
Ask for a traceable decision | Record the review outcome explicitly.
Preserve the boundary | Do not describe search as live.
Close with status | Staging deployed, search disabled, compatibility pending, decision with Lee.''',
    notes='''Remains disabled | Preserves feature state despite completed deployment.
Against | Connects the previous application to the data state it must handle.
Not production sign-off | Prevents a handoff from being mistaken for permission.
Has not been made | Makes the unresolved decision explicit.
Alone | Limits what an available earlier build establishes.
With Lee | Assigns decision ownership without predicting approval.''',
    d='''Which status is accurate? | R18 is in staging with search disabled | Search is live in production | R18 has full production sign-off | The old application is verified compatible | Only the staging deployment and disabled search state are established.
Why does optional not settle compatibility? | The previous application's behavior with migrated data is untested | Optional fields are always incompatible | The migration never ran anywhere | Lee has already rejected release | Optional describes a field rule, not evidence of the older application's behavior.
Which rollback claim is justified? | Readiness remains unverified without the relevant compatibility evidence | An older build guarantees safe rollback | Staging deployment proves data reversibility | A disabled flag automatically undoes the migration | The earlier application's compatibility with the changed state has not been tested.
Who owns the unresolved production decision? | Lee | Every staging user | The feature flag itself | The migration tool | Lee is explicitly identified as the reviewer responsible for the production decision.''',
    dialogue='''Chen | I am handing over R18 for your release review. It is deployed in staging, and the new search feature remains disabled by its flag.
Lee | Keep that [[environment boundary::Environment boundary limits the deployment claim to staging rather than implying a live production release.]] explicit in the summary. I do not want deployed shortened into live when someone forwards this message.
Chen | Agreed. The deployment is complete in staging, but the feature is not enabled there. I will report those as separate statuses.
Lee | Good. The [[feature flag::The feature flag controls whether new search is enabled, which is separate from the code being deployed.]] state matters independently of where the code is installed. Neither fact is a production decision.
Chen | The migration adds an optional field. I initially wrote backward compatible in the handoff, but we have not tested the previous application version against the changed state.
Lee | Then replace that with [[known limitation::Known limitation identifies the untested previous-version compatibility rather than presenting optionality as proof.]]. Optional describes the field, not the older application's demonstrated behavior. We need to preserve the missing check.
Chen | I will say compatibility with the previous application version remains untested. That is more accurate than predicting it from the small size of the change.
Lee | Yes. [[Schema compatibility::Schema compatibility requires relevant evidence about components working with the changed structure, which is not supplied here.]] is a claim about interaction with the changed structure. A field being optional does not automatically establish every consumer's handling.
Chen | Someone may ask whether we can simply return to the previous build if production review uncovers a problem. We have not verified that path either.
Lee | Do not claim [[rollback::Rollback is a return to an earlier state whose readiness depends on compatibility with the actual migrated data and system state.]] readiness from the existence of an older build alone. Its behavior against the post-migration state is part of the unresolved question.
Chen | Should I list that as a request to check the prior application with the migrated data, rather than as a request merely to locate the old build?
Lee | Exactly. The relevant [[data compatibility::Data compatibility concerns whether the earlier application can correctly use the actual migrated state, not whether an old executable exists.]] evidence needs the real combination under review. Availability of a file is not the same as verified operation.
Chen | I will keep the review outcome separate from the handoff. Sending you this status does not mean I have permission to enable search or proceed to production.
Lee | Correct. I own the [[go/no-go decision::The go/no-go decision is Lee's unresolved production decision, not an automatic consequence of receiving the handoff.]] for production, and it has not been made. Please do not phrase my pending review as expected approval.
Chen | The summary can list R18, staging, search disabled, optional-field migration, untested prior-version compatibility, and your decision ownership. That should be enough to avoid an ambiguous ready label.
Lee | That is a useful [[handoff::Handoff transfers specific state, evidence gaps, and responsibility so the reviewer does not have to infer readiness.]]. It gives the next person concrete facts and an open item instead of a broad status that means different things to different readers.
Chen | Once the missing check is performed, its actual result should be added. Until then, I will not mark compatibility complete because the staging deployment succeeded.
Lee | Right. Keep the [[release gate::A release gate is a condition for advancing the release and cannot be treated as satisfied by an unrelated completed deployment.]] distinct from a completed deployment step. The relevant review still needs its evidence and an explicit decision.
Chen | My final line will be staging deployed, search disabled, compatibility pending, production decision with Lee. There will be no claim that search is live.
Lee | That supports an accurate [[readiness claim::A readiness claim must stay within the completed checks and unresolved decision rather than equating staging deployment with approval.]]. We can review what is actually known without confusing a status update with authorization to release.''',
    transfer_title='Four facts for the release handoff',
    transfer_setup='Complete the R18 handoff. Do not upgrade any pending check or decision to completed status.',
    transfer='''Developer: "R18 is deployed in ___." | staging | The only established deployment environment in the scenario is staging.
Reviewer: "New search remains ___." | disabled | The feature flag keeps search disabled despite the completed deployment.
Developer: "Prior-version compatibility is ___." | untested | No test of the previous application against the migrated state is established.
Reviewer: "The production decision remains with ___." | Lee | Lee owns the production review and has not made that decision.''',
))
