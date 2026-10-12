"""Twenty-four contextual conversations for localization testers and developers."""
from books.localization_qa_content import BOOK
from books.specialist_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], '''
The screenshot does not show the trigger | A tester adds missing context to a bug report. | Engineer | Tester
I can see the wrong label in your screenshot, but I cannot reach that screen from a new account.
The account needs the tutorial completed and the shield equipped before the action prompt appears.
That prerequisite should be in the report, or I may spend time testing a different state.
I will add the account state, exact steps, build, and locale without including any personal account data.
Please also identify whether the problem occurs every time or only after changing equipment.
It occurred on all three attempts after equipping the shield; I have not tested every equipment combination.
That gives me a repeatable starting point without claiming broader coverage.
I will keep the observed result separate from my suspicion about the shared resource.
Good. We can investigate the implementation once we reproduce the actual finding.
The updated report will make clear what I observed and what still needs investigation.

Open is a command in one place and a state in another | A reviewer explains ambiguous source text. | Tester | Developer
The source word Open is used on a button and in a status column, but the target language needs different forms.
The button asks the user to open something, while the column describes something already open.
Exactly. The identical English spelling hides a grammatical and functional difference.
We should not force one translation to cover both contexts merely because the source word matches.
Please give each resource a context note identifying command or state.
I can separate the resources and preserve their links to the relevant controls.
The language reviewer can then choose the correct form for each use.
Will the report include both screenshots so the distinction remains visible?
Yes, along with the resource identifiers and the action associated with the button.
That will make the change understandable to engineers who do not read the target language.

Cannot reproduce on a different locale is not a rejection | Two colleagues compare test environments. | Developer | Tester
I tested the issue in fr-FR and could not reproduce it, so I was about to close the fr-CA ticket.
Those are different locale configurations. The affected package uses a distinct resource for fr-CA.
Then my result does not contradict your report; it describes another environment.
Correct. We need the same build, locale, and product state before comparing results.
I will rerun the steps with the locale tag you supplied.
Please record the actual resource loaded as well, because fallback behavior may conceal the difference.
If the affected locale still fails, we can preserve the passing result as a comparison.
Yes, but label the scope so nobody treats it as a fix verification.
I will change the ticket comment from not reproducible to not reproduced in the different configuration tested.
That accurately describes the evidence and gives the next tester a useful starting point.
''')
LESSONS['module-2'] = short_lesson(BOOK['units'][1], '''
Save and sync name different operations | A tester reviews terminology with a product owner. | Tester | Product owner
The target translation uses the same term for Save and Sync, but the product treats them as different operations.
Save stores the local change, while Sync exchanges updates with the connected account under this design.
Then the terminology needs to preserve that distinction instead of making the two buttons sound interchangeable.
Our glossary currently lists both under a single source entry without explaining the behavior.
Can we add separate concept definitions and approved terms for the actual functions?
Yes. We should review the affected screens rather than replace words blindly throughout the product.
A global substitution could alter unrelated uses where the existing term is correct.
I will ask the terminology owner to approve the distinction and record the relevant resource identifiers.
The language team can then check consistency against that approved concept, not just matching spelling.
Good. The glossary should help users predict what each operation does.

A tag was translated as visible text | A tester diagnoses a resource-processing problem. | Engineer | Tester
The target label now displays a formatting tag on screen instead of applying the expected emphasis.
Was the tag changed during export, translation, or reimport?
The exported resource looks correct, but the imported version contains an altered closing token.
Then the report should identify the first stage where the syntax changes.
I will compare the files and the actual rendered result rather than blame the translator from the screenshot alone.
Good. The protected markup and localizable wording need different validation checks.
The wording can be fluent while the resource syntax is still invalid.
Exactly. Preserve the intended emphasis, but use the actual format's supported syntax.
After the processing fix, we should run the same resource through the complete pipeline.
And verify the built label, because an editor preview does not establish the packaged result.

The sample name hides the real problem | A tester requests realistic runtime values. | Tester | Developer
The notification passes with the sample name Jo, but a longer display name overlaps the action link.
The message pattern is valid, so this looks like a layout issue triggered by the inserted value.
Yes. The variable resolves correctly; the resulting sentence still needs enough usable space.
We should not shorten the user's name in storage to make this one preview fit.
Agreed. Test the supported display behavior with realistic names and multiword item labels.
I will also check whether the link remains separately identifiable and usable after wrapping.
Please preserve the complete meaning and follow the actual product rules for any visual shortening.
We can record the exact values and viewport without using real personal information.
That gives us a reproducible test rather than a general complaint about long languages.
I will attach the updated package for a combined language and layout check.
''')
LESSONS['module-3'] = short_lesson(BOOK['units'][2], '''
Zero is a product message as well as a number | A tester separates grammar from copy choices. | Designer | Tester
We want the empty state to say No messages instead of displaying the numeric count zero.
That can be a deliberate product message, but it is separate from assuming every language has a category named zero.
So the wording decision and the locale's grammatical category rules are not the same thing.
Correct. The implementation needs to distinguish the exact empty-state requirement from general plural selection.
We should specify what appears at zero and what happens when the first message arrives.
Yes, and test the transition rather than inspect only a static empty screenshot.
The approved wording should also remain consistent with whether the count refers to all messages or unread messages.
That context matters. No messages and no unread messages do not make the same claim.
I will clarify the product condition before the resource goes to translation.
Then the language reviewer can assess the intended state instead of guessing what zero measures.

Second is not the plural of two | An engineer checks a reused formatting rule. | Engineer | Tester
I reused the quantity formatter for the ranking label because both screens display a number.
The ranking describes position, while the quantity screen describes how many items exist.
So second item and two items require different kinds of formatting.
Exactly. Cardinal and ordinal rules are not interchangeable merely because the input is numeric.
We need separate expectations for the actual locales supported by the ranking component.
Yes. A passing item-count test does not establish correct position labels.
I will document which formatter each screen uses and add the relevant ranking examples.
The target-language reviewer can then check the full phrase, not just a suffix in isolation.
That should also catch cases where the label changes with the surrounding noun.
Good. Keep the test evidence tied to the complete message and actual product context.

An integer pass does not cover decimal formatting | A tester reviews a coverage claim. | Lead | Tester
The plural tests passed at one, two, five, eleven, twenty-one, and twenty-two. Can we mark all numeric forms complete?
Those are the listed integer cases. We have not tested the decimal representations used elsewhere.
The runtime may preserve visible fraction digits, so the actual representation can affect the rule selection.
Yes. We need the product's real inputs and formatting behavior, not a guess based on the displayed integer examples.
I will add a separate matrix for the supported decimal cases.
Please record the formatter and locale-data versions so results from different environments remain comparable.
The current report can still say the six integer cases passed.
Exactly. That is useful evidence when its scope is stated accurately.
We should avoid replacing a precise result with an all-plurals label.
Agreed. Coverage should show what we exercised and what remains in the test plan.
''')
LESSONS['module-4'] = short_lesson(BOOK['units'][3], '''
The missing line is a height problem | A tester distinguishes vertical clipping from word choice. | Tester | Engineer
The translated paragraph wraps correctly, but the bottom of the second line is cut off.
Then widening the text area may not address the actual vertical constraint.
The screenshot shows the line box is too short for the rendered characters in this font.
I will inspect line height and container height in the same target configuration.
Please do not remove the second sentence merely to make the screenshot look clean.
Agreed. The complete approved content needs to remain visible within the supported design.
We should also check the actual font fallback because its metrics may differ from the primary font.
I will compare the rendered result rather than assume the configured font is the one being used.
Record the viewport and text-size setting so the retest reproduces the same condition.
Then we can verify that the lower line remains complete without colliding with the next element.

An ellipsis hides the decisive word | A language reviewer explains why visual shortening fails. | Designer | Tester
The label now ends with an ellipsis, so it no longer overflows the control.
The omitted word distinguishes deleting locally from deleting everywhere in the account.
Then the layout looks cleaner, but the user has lost the information needed to choose safely.
Exactly. This is not an acceptable shortening just because the component stays within its boundary.
We need a design that preserves the distinction under the actual supported conditions.
The approved wording should remain available and legible without relying on an undiscoverable hint.
I will review wrapping and control width with the design owner.
Please include the neighboring control so the fix does not create a new overlap.
The retest should check meaning, visibility, and the actual action together.
That will show whether the user can understand the choice, not merely whether the box is tidy.

The pseudo build leaves one word unchanged | A tester investigates a hard-coded string. | Tester | Developer
Most labels show the pseudo transformation, but this error message remains ordinary English.
That may mean the message is not coming from the localizable resource path.
It is evidence to investigate, not proof that the final target translation is missing.
I will trace the source and check whether the error is generated by a separate component.
Please include the exact error trigger, because the normal screen uses the correct resource.
If this string is hard-coded, we need to expose it through the supported localization pipeline.
Then rerun the pseudo test to check that it participates in the transformation.
And later inspect the real target-language error message in the actual product.
Correct. Pseudo coverage and linguistic correctness are different verification steps.
I will keep both in the ticket so an extraction fix is not mistaken for completed language review.
''')
LESSONS['module-5'] = short_lesson(BOOK['units'][4], '''
Right alignment did not fix the sentence | A tester clarifies text-direction properties. | Engineer | Tester
I moved the Arabic label to the right edge, but the embedded identifier still interacts strangely with punctuation.
Right alignment positions the block; it does not by itself establish the correct directional behavior.
We need to inspect the base direction and how the inserted identifier is handled.
Yes. Preserve the identifier's logical content while testing the surrounding mixed-direction sentence.
I will attach the stored value and the rendered screenshot to the same report.
That helps distinguish a data problem from a presentation problem.
The proposed fix should also be checked when another number follows the identifier.
Correct. A short isolated example may hide the boundary interaction that occurs in the real message.
We can keep the underlying order code unchanged throughout the test.
Exactly. A visual correction should not silently rewrite the user's data.

The play symbol is not a word | A designer reviews indiscriminate mirroring. | Designer | Tester
We mirrored the entire screen image for the right-to-left version, including every symbol and brand asset.
That needs a more specific review. Text direction does not imply that every visual element should reverse.
Some navigation relationships may change, while other symbols retain their intended meaning.
Yes. Follow the actual component and asset guidance instead of treating the page as one reversible picture.
The current result also reverses the letters inside a logo, which is plainly not the intended localized asset.
We should preserve the approved logo and review directional controls individually.
I will separate text layout, navigation behavior, and image substitution in the design checklist.
Good. That makes each expected result testable instead of relying on a blanket mirror flag.
The language reviewer can check the complete scene after the appropriate changes are implemented.
And the interaction test should verify that the controls still perform the actions their appearance suggests.

The copied identifier differs from the visible one | A tester documents a data-order failure. | Tester | Engineer
The order code looks plausible on screen, but copying it into the support form produces a reversed sequence.
Then the display workaround may have changed the stored or copied text rather than solving directional presentation.
The expected value is still AB-123, and the support team needs exactly that identifier.
We should reject a fix that only passes a screenshot comparison.
Please test copy, selection, and the actual value delivered to the receiving field.
I will inspect the transformation path and preserve the original data.
The report should show both the visual result and the copied sequence.
That will make clear why the apparently successful display is still a functional defect.
After the correction, we can repeat the same interaction with surrounding Arabic text.
Yes. The final result must preserve both readable presentation and the identifier's intended content.
''')
LESSONS['module-6'] = short_lesson(BOOK['units'][5], '''
An idiom preserves energy but loses the instruction | A reviewer discusses a tutorial line. | Writer | Tester
The localized tutorial uses an energetic idiom, but reviewers say it no longer tells players to hold the button.
The source is playful, yet the action instruction still needs to remain explicit.
Exactly. Preserving tone does not mean we can lose the mechanic the player must perform.
We should compare the line against both the character voice and the required action.
The reviewer can suggest wording that keeps the energy while naming the hold action.
I will supply the actual interaction and timing context rather than only the isolated English sentence.
That will help distinguish holding from tapping or repeatedly pressing.
The implementation team should also check that the subtitle and controller prompt remain consistent.
Yes. A charming line can still fail if it teaches the wrong interaction.
We will review the revised line in the scene before treating the adaptation as complete.

A familiar joke is not familiar to every audience | A tester scopes cultural feedback. | Tester | Narrative lead
Several reviewers did not recognize the reference behind this joke, so the character's response seemed unrelated.
Does the joke need that specific reference for the plot, or is its purpose simply to show friendly teasing?
The brief says friendly teasing; the reference itself does not drive a later event.
Then an adaptation may preserve the relationship better than a literal explanation.
We should still review the target line with the scene and the character's established voice.
Agreed. We do not want a new joke that changes the relationship into ridicule.
The report will describe the observed confusion without claiming that nobody in the market knows the reference.
Good. Keep the sample and context visible so the decision is grounded in evidence.
After approval, the new line needs the usual language and in-game checks.
Yes. Cultural adaptation remains a product change with a defined purpose and review process.

The rating label needs the right reviewer | A tester avoids making an unsupported compliance claim. | Producer | Tester
The target text seems more explicit than the source. Can you confirm that it violates the market's rating rules?
I can describe the wording and the increased explicitness, but I cannot make that compliance determination.
Then the ticket should separate the linguistic finding from the rating question.
Yes. Include the source, target meaning, scene, and the qualified review needed under our process.
We should not publish a claim that the content is prohibited without the relevant determination.
Nor should we dismiss the language difference simply because that determination is still pending.
I will route the case to the responsible content and compliance reviewers.
The language team can explain the alternatives and their effects on character voice.
The final decision should identify the approved wording and any related asset changes.
Then QA can verify the implemented scene against that actual decision.
''')
LESSONS['module-7'] = short_lesson(BOOK['units'][6], '''
The subtitle names someone outside the scene | A tester checks branch-specific speaker mapping. | Implementer | Tester
The subtitle label is correct on the first attempt, but your report shows another character after the learner retries.
The retry branch appears to use a different speaker mapping even though Mara delivers both lines.
We need the exact branch trigger and asset identifier to compare the two paths.
I will attach those details and a recording of the label at the point it changes.
The timing correction alone will not resolve a wrong identity.
Correct. Speaker attribution should have its own expected result in the retest.
I will check the mapping in the retry path rather than replace every speaker label globally.
Please preserve the first path's correct behavior while fixing the second.
The updated package can then be tested on both paths with the same locale.
That will give us branch-specific evidence instead of a general subtitles-fixed claim.

The panel moves with the head but covers the task | A VR tester reports a placement problem. | Tester | Designer
The subtitle remains visible when I turn, but it overlaps the object the learner needs to manipulate.
So visibility alone is not enough; the panel is obstructing the actual task.
Exactly. We need to review its placement under the supported interaction and headset conditions.
Is it currently anchored to the viewer or to the virtual environment?
It follows the viewer's head in this implementation, which is why it continues covering the object during the turn.
I will review that behavior against the actual product requirements rather than assume one anchoring approach is always best.
Please keep the complete text legible while checking whether the learner can see the required object.
We should test the scene in the headset, not decide from a cropped desktop preview.
I will record the viewing direction and the task state for the comparison.
Good. The report will then connect the placement defect to an observable interaction problem.

Captions need more than translated speech | A tester checks an accessibility specification. | Tester | Producer
The speech is translated, but the required caption for the alarm sound is missing from this scene.
Then this is not just a subtitle wording issue; the specification includes relevant non-speech information.
Correct. We need to verify the caption requirements actually defined for this product.
The report should identify the sound event, its trigger, and the expected text or approved representation.
I will also distinguish the missing sound cue from the separate wrong speaker label.
Good. One corrected dialogue line does not establish complete caption coverage.
The updated package should be checked with the actual caption setting enabled.
And we should preserve the evidence for the supported locale and branch.
Yes. I will not claim every accessibility requirement passed from this single scene.
That keeps the result useful and avoids turning a narrow fix into an unsupported global sign-off.
''')
LESSONS['module-8'] = short_lesson(BOOK['units'][7], '''
The change landed on the wrong branch | A tester checks why the package still fails. | Developer | Tester
The resource change is merged, but I now see it landed on the development branch rather than the release branch.
That explains why the current release candidate still displays the old wording.
We need to follow the approved change process for the intended release branch.
Yes. Do not mark the ticket verified until the actual candidate includes the correction and passes the check.
I will identify the change and the target branch explicitly in the update.
Please also provide the new build identifier so the retest does not accidentally use the old package.
The source history can show the change path without being treated as final test evidence.
Exactly. Merge status and package verification answer different questions.
I will attach the candidate when it is available and keep the current status accurate.
Then QA can test the affected locale and confirmation flow against the release criteria.

A reopened defect is not a personal accusation | A lead discusses a failed retest. | Engineer | Tester
You reopened my ticket even though I fixed the resource. Did you think I had not made the change?
I am reporting that the same defect is still present in the tested release candidate, not questioning your effort.
The resource may be correct in source while the package still includes an earlier version.
Exactly. Let us compare the build and package contents before guessing at the cause.
I will check the manifest and the branch used for that candidate.
I will preserve the steps and observed result so the failed retest is reproducible.
If the package was stale, we can say that clearly rather than relabel the language finding.
Yes. The ticket status should follow the product evidence, not a judgment about the person.
I will send a new candidate after the packaging issue is resolved.
Then I will repeat the same check and record the actual result.

An exception does not erase the known issue | A producer records a release decision. | Producer | QA lead
The authorized release owner accepted the documented punctuation issue for this release. Should we mark it fixed?
No. The decision permits the exception under its stated scope; the wording has not changed.
We should keep the issue open or use the approved deferred status with the decision linked.
Exactly. The record needs the impact, affected scope, owner, and follow-up required by the actual process.
That also prevents the next team from assuming the resource was corrected.
Yes. Risk acceptance and verified correction are different histories.
We should not extend this exception to the destructive-action label or other locales.
Correct. An exception applies only to the specific scope actually authorized.
I will update the release record and keep the separate serious finding visible.
Then the release notes and future test plan can reflect what was delivered rather than what we hoped to fix.
''')
