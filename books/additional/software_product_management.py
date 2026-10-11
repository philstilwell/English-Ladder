"""Original pricing, accessibility, and research-moderation conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='What exactly counts as a paid seat?',
        skill='Resolve conflicting plan descriptions before a customer sees a price.',
        setup='A proposed monthly plan costs $120 including eight editor seats. Each additional editor seat costs $12 for a full month; viewers are free. Taxes and partial-month changes are outside this example. A draft incorrectly calls every member a paid user. The plan is not launched.',
        cast='Mina|Product manager\nTheo|Billing analyst',
        dialogue='''Theo|Your plan page says twenty members, but the billing specification counts editors. Which number am I supposed to show in the preview?
Mina|The paid [[seat type::Seat type distinguishes editors, who count toward this proposed price, from viewers, who do not.]] is editor. Viewers can belong to the workspace without adding a charge. The page needs to make that distinction explicit.
Theo|Then a workspace with eleven editors and nine viewers has twenty members but only eleven seats counted for this price. Correct?
Mina|Yes. The [[included allowance::The included allowance covers eight editor seats within the base price; only the additional three incur the stated extra charge.]] is eight editor seats. Eleven editors means three additional seats, not eleven additional charges.
Theo|At twelve dollars each, those three add thirty-six dollars. With the base charge, the full-month subtotal is one hundred fifty-six dollars.
Mina|That matches the proposal. Show the base, included seats, additional quantity, and unit price separately so customers can reproduce the total.
Theo|What if someone promotes a viewer halfway through the month? The full-month example does not tell me what to charge then.
Mina|The [[proration::Proration concerns adjusting a charge for part of a billing period; the full-month example supplies no approved partial-month rule.]] rule is still unresolved. Please mark that case as a decision needed, rather than assume a daily rate or a full-month charge.
Theo|We also need the event that changes the billable quantity. An invitation is not necessarily an accepted membership or an editor assignment.
Mina|Agreed. Bring those states to the billing review. The product and billing records must agree about which event starts or ends a charge.
Theo|The feature table has another issue. It says unlimited exports, while the proposed plan permits five scheduled exports a month.
Mina|That is an [[entitlement::An entitlement is a capability or allowance provided by the plan, distinct from the number of seats used to calculate its price.]] mismatch. Correct the capability table as well as the price; a consistent subtotal does not fix an inaccurate feature promise.
Theo|Does the five-export limit include manual downloads? The current wording could be read either way.
Mina|The proposal only specifies scheduled exports. We need the owner to confirm manual-download behavior before we publish a broader statement.
Theo|Some existing customers have a different plan. Should the new page imply their terms change on launch day?
Mina|No. [[Grandfathering::Grandfathering means retaining specified existing terms for an eligible group; whether it applies here remains a separate unapproved policy decision.]] is a separate policy question. Neither continued old terms nor automatic migration has been approved for those customers.
Theo|I will keep the existing-customer decision separate and prepare a clearly labeled example for the proposed new plan.
Mina|Use an [[invoice preview::An invoice preview shows the proposed charge breakdown before final billing; it is not evidence that an unlaunched plan or unresolved policy is approved.]] with the eleven editors and nine viewers. Label it as a full-month subtotal before tax, not an actual invoice.
Theo|I will also list partial-month changes, invitation states, manual downloads, and existing-customer treatment as open decisions.
Mina|Good. We can review the example now, but the page and billing rules need the same approved definitions before launch.''',
        transfer_title='Members are mistaken for extra seats',
        transfer_setup='Use the proposed full-month plan above. A workspace has ten editors and six viewers. No partial-month rule has been approved.',
        transfer='''Billing: Ten editors use eight included seats and ___ additional seats.|two|Ten minus the eight included editor seats leaves two separately charged seats.
Product: That adds ___ dollars to the base charge.|twenty-four|Two additional editor seats multiplied by twelve dollars gives twenty-four dollars.
Billing: The subtotal before tax is ___ dollars.|one hundred forty-four|The one-hundred-twenty-dollar base plus twenty-four dollars gives the stated subtotal.
Product: Do not apply this full-month example to an unresolved ___ rule.|proration|The example contains no approved method for charging part of a month.'''),
    scenario(
        title='The button works, but keyboard users cannot see it',
        skill='Describe an accessibility defect precisely and negotiate a testable correction.',
        setup='A new sticky promotion banner completely covers the Save button when that button receives keyboard focus. The issue is reproduced at a documented browser size and zoom setting. A mouse-only test passed. The team must define the defect and a retest, not certify the entire product.',
        cast='Ravi|Product owner\nEllis|Accessibility specialist',
        dialogue='''Ravi|The Save button passed the click test yesterday. Is this a separate defect, or the same one reported twice?
Ellis|It is a [[keyboard navigation::Keyboard navigation uses keys to move between and operate controls; a successful mouse click does not establish that this route is usable.]] problem. Tab reaches Save, but the promotion banner covers the entire button, so the user cannot see which control is active.
Ravi|Does the focus actually move to the button, or does it get trapped somewhere earlier in the page?
Ellis|Focus reaches it. The [[focus indicator::The focus indicator is the visible cue identifying the active control; here both it and the button are hidden behind the banner.]] is hidden along with the button. I can reproduce it using the recorded browser size and zoom.
Ravi|Then calling the button disabled would be inaccurate. It is active, but covered. Can you attach the sequence rather than only a screenshot?
Ellis|Yes. I will record the starting position, keys pressed, viewport, zoom, and expected result. The screenshot will show where the obstruction occurs.
Ravi|The designer asks whether making the button a brighter color would solve it. That would be a small change.
Ellis|Not while the [[sticky banner::The sticky banner remains positioned over the focused control; changing the color of a completely covered button would not remove that obstruction.]] covers it completely. We need the layout or scrolling behavior to expose the focused control, not just recolor what is behind it.
Ravi|Could we remove the banner from this version while the permanent change is designed? The promotional content is not essential to saving.
Ellis|That is an option to evaluate. Removing it still needs testing so we do not assume the replacement layout has no other problem.
Ravi|How should we describe the relevant accessibility requirement without claiming that one check proves the whole application conforms?
Ellis|Keep the [[acceptance criterion::The acceptance criterion defines the specific observable result required for this correction; passing it does not establish complete accessibility conformance.]] specific: the focused Save control must not be entirely hidden by our content on the documented route. We should aim for it to be fully visible.
Ravi|And test more than that one screenshot size? The banner changes height when its text wraps.
Ellis|Yes. Agree relevant layouts and settings for the retest. The original reproduction is the starting point, not the entire coverage plan.
Ravi|We already have an automated report with no failures. Can that close this ticket?
Ellis|No. These [[reproduction steps::Reproduction steps describe how to observe the actual defect; a clean automated report does not disprove a manually reproducible keyboard problem.]] still produce the problem. Automated checks are useful, but they do not replace the interaction check that exposed it.
Ravi|I will keep the ticket open, attach the evidence, and ask Design and Engineering to assess removing or repositioning the banner.
Ellis|Once the change is ready, include a [[regression test::A regression test checks that a previously identified problem stays corrected and that the change has not reintroduced the relevant failure.]] for this keyboard route. Also check that Save remains operable, not merely visible.
Ravi|The release note can say this particular obstruction was corrected after verification, not that every accessibility issue is fixed.
Ellis|Exactly. Report the tested behavior and scope. That is more useful than a broad assurance unsupported by the work.''',
        transfer_title='A clean scan is offered instead of a keyboard retest',
        transfer_setup='After a banner change, the automated scan is clear. Nobody has repeated the keyboard route that originally hid Save.',
        transfer='''Product: The scan does not replace the keyboard ___.|retest|The original interaction must be checked again; an automated result alone does not establish the correction.
Specialist: Repeat the recorded steps at the stated size and ___.|zoom|The reproduction includes the zoom setting, which can change the layout and obstruction.
Product: Confirm that Save is visible and remains ___.|operable|A visible control must still work; appearance alone does not establish usable interaction.
Specialist: Report this correction without claiming complete ___.|conformance|One corrected defect does not prove that the entire product meets all accessibility requirements.''',
        reference=('W3C: Focus Not Obscured (Minimum)', 'https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html')),
    scenario(
        title='A research task that accidentally gives away the answer',
        skill='Revise leading research language and agree a neutral, respectful session.',
        setup='A team will observe invoice approvers using a prototype. Its draft task names the button participants are meant to discover. Recruiting has selected daily administrators, although the target role approves invoices only monthly. All invoice data will be fictional.',
        cast='June|Product manager\nOmar|User researcher',
        dialogue='''June|The task says, "Click the Approvals tab and approve the invoice." Is that clear enough for tomorrow's sessions?
Omar|It gives away the route. For a [[usability task::A usability task sets a goal for the participant without supplying the interface actions whose discoverability the research is intended to examine.]], describe the goal: an invoice needs your approval before payment. Let the participant find how to do it.
June|So we should remove the tab name. We want to observe whether they find it, not whether they can follow our instructions.
Omar|Exactly. That wording is a [[leading instruction::A leading instruction directs the participant toward a particular action and can obscure whether the interface itself supports the task.]]. A successful click after we name the control would not answer the original discoverability question.
June|The recruiting list is all administrators. They process invoices every day. Are they close enough to the monthly approvers we described?
Omar|Not for that question. Familiar administrators may know paths that occasional approvers have to rediscover. We need people with the relevant role and frequency of use.
June|Could we still interview the administrators about setup, then keep those findings separate from the approval task?
Omar|Possibly, but revise the [[recruitment screener::The recruitment screener checks participant characteristics against the research question; role and frequency matter more here than general familiarity with the product.]] for the approval sessions. Do not silently relabel the recruited group as representative of monthly approvers.
June|I will make the role and frequency explicit. What happens if a participant gets stuck and asks which tab to use?
Omar|Give them time and use a neutral prompt such as, "What would you do next?" If we provide help, record when and what we supplied.
June|The observer sheet has only pass or fail. That would hide the fact that someone finished after we told them the route.
Omar|Add [[moderator assistance::Moderator assistance is help supplied during the session; documenting it distinguishes independent task completion from completion after prompting or guidance.]] to the observation record. Completion after a hint is different from completion without help.
June|Sales wants to sit in and explain why we designed the screen that way. I suspect that could change what we observe.
Omar|Ask observers to hold comments. We are examining the interface, not testing the participant, and defending the design can discourage candid reactions.
June|Can we record the sessions for the team? I have not put recording in the participant information yet.
Omar|Arrange [[informed consent::Informed consent requires participants to understand and agree to the proposed research and recording arrangements; attendance alone does not establish agreement to recording.]] before recording, under our research process. Explain the purpose, access, retention, and choices clearly; do not assume attendance authorizes a recording.
June|We will use the fictional invoices and the prototype account. There is no need for participants to show their real invoices or passwords.
Omar|Good. The [[discussion guide::The discussion guide provides the planned tasks and neutral prompts, helping sessions address the same questions without prescribing participants' actions.]] should also say what to do if real information appears, so the session stays within our agreed safeguards.
June|I will update the task, recruitment request, observer instructions, and recording information before confirming the sessions.
Omar|Then we can learn how the intended users approach the task, while keeping assistance and the limits of the sample visible in the findings.''',
        transfer_title='A prompted completion is reported as independent',
        transfer_setup='A participant finds Approvals only after the moderator names the tab. The observer records an unassisted success.',
        transfer='''Researcher: The participant finished after a ___.|prompt|Naming the tab supplied guidance before completion, so the recorded outcome was not independent.
Product: Change the result to assisted completion and retain the ___.|observation|The record should preserve what happened rather than erase the session or pretend it was unassisted.
Researcher: The next task should describe the goal without naming the ___.|tab|Naming the interface location gives away the route the task is meant to investigate.
Product: Do not use this outcome as proof of independent ___.|discoverability|Completion after supplied navigation does not establish that users can find the control themselves.''',
        reference=('GOV.UK: Using Moderated Usability Testing', 'https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing')),
]
