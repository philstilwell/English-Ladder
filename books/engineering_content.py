"""Original engineering conversations and evidence-based language practice."""
from books.authoring import unit

BOOK = dict(
    slug='engineering', title='Engineering English',
    cover_label='Requirements / evidence / interfaces / decisions',
    cover_title='Engineering', cover_size=34,
    tagline='Challenge the assumption. Explain the evidence.',
    audience='For design, systems, test, reliability, manufacturing, and field engineers.',
    map_intro='Eight technical conversations that connect requirements, engineering evidence, trade-offs, and decisions.',
    notes_title='Precision makes disagreement productive.',
    notes_intro='Engineering conversations move between customer needs, models, drawings, measurements, and decisions. A familiar word such as verified, robust, or compatible can mean different things to different teams. These cases develop the language for naming the exact claim, testing its basis, and explaining what remains unresolved without making the discussion personal.',
    field_notes=[
        ('Name the reference', 'A result needs a requirement, revision, condition, or comparison point. Identify the reference before saying the design passes, improves, or remains compatible.', '"The result applies to revision B under the recorded test conditions."'),
        ('Separate observation from explanation', 'A failed response is an observation. A suspected mechanism is an explanation to investigate. Preserve the distinction even when the hypothesis sounds convincing.', '"The output dropped during the test; connector damage is not yet confirmed."'),
        ('Make the trade-off explicit', 'Lower material cost can accompany higher assembly cost. A stronger part may add mass. State the comparison basis and the constraints instead of presenting one favorable number as the whole decision.', '"Option B costs less at the stated volume after tooling is included."'),
        ('Close with evidence and ownership', 'A meeting can identify a gap without closing it. Name who will supply the missing evidence, who reviews it, and what decision remains pending.', '"Please attach the interface analysis before the release owner reviews closure."')],
    scope_note='Original fictional English practice, not engineering design guidance, safety certification, professional approval, or instructions for operating equipment. Numbers and technical cases are invented. Actual design, testing, field action, and compliance decisions require qualified personnel, applicable requirements, approved procedures, and the relevant authority.',
    sources=[
        dict(title='NASA. Systems Engineering Handbook, Appendix C: How to Write a Good Requirement.', url='https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/', note='Background on clear, verifiable requirements. The enclosure requirements and customer discussion are original fictional examples.', checked='10 October 2026'),
        dict(title='NASA. Systems Engineering Handbook, Section 6: Crosscutting Technical Management.', url='https://www.nasa.gov/reference/6-0-crosscutting-technical-management/', note='Background on interface and configuration management. The book does not prescribe NASA procedures for other organizations.', checked='10 October 2026'),
        dict(title='ASQ. What Is Failure Mode and Effects Analysis?', url='https://asq.org/quality-resources/fmea', note='Background on distinguishing failure modes, effects, and possible causes. No scoring scale or acceptance rule is asserted as universal.', checked='10 October 2026'),
        dict(title='NIST/SEMATECH. Engineering Statistics Handbook, Section 8.1.3.2: Lack of Failures.', url='https://www.itl.nist.gov/div898/handbook/apr/section1/apr132.htm', note='Background on the limits of reliability information when few failures are observed. The prototype case is language practice, not a statistical qualification plan.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Requirements and Constraints',
    scene='Lightweight compared with what?',
    skill='Convert an ambiguous customer request into a measurable proposal while keeping unresolved conditions and approval visible.',
    brief='Customer representative Julia asks engineer Wei for a lightweight, durable enclosure. Their meeting proposes a maximum mass of 1.2 kg for the empty enclosure including its cover and fasteners. Electronics are excluded. The proposed service life is five years, but operating temperature, humidity, handling conditions, and the verification method are unresolved. Nothing is approved. Wei must record the proposed mass limit accurately and avoid turning the life target into a demonstrated durability claim.',
    cast='Julia | Customer representative\nWei | Design engineer',
    culture=('Ask for the boundary behind the adjective', 'A request for a robust or lightweight product communicates a preference, not a complete acceptance basis. Ask what is included, under which conditions, and how success will be checked. Keep the discussion focused on the product rather than criticizing the customer for imprecise language.'),
    a='''What is included in the proposed mass limit? | The empty enclosure, cover, and fasteners | All installed electronics | Only the removable cover | Shipping packaging and spare parts | The briefing explicitly includes the enclosure, cover, and fasteners while excluding electronics.
What is the status of five years? | A proposed service-life target | A demonstrated test result | An approved warranty promise | A measured failure-free period | Five years is proposed while conditions and the verification method remain unresolved.
Which condition is still open? | Operating temperature | The proposed 1.2 kg mass value | The inclusion of fasteners | The exclusion of electronics | Operating temperature is listed among the unresolved conditions needed to define the proposal.''',
    vocabulary='''stakeholder need | The capability or outcome a stakeholder wants. | capture the stakeholder need
design requirement | A specified condition the design must satisfy. | define a design requirement
design constraint | A limit on available design choices. | work within a design constraint
mass budget | The planned allocation of allowable mass. | allocate the mass budget
maximum mass | The greatest permitted mass under a stated boundary. | specify maximum mass
system boundary | The line defining what is included in the system. | define the system boundary
operating envelope | The range of conditions for intended operation. | define the operating envelope
service life | The intended period of use under specified conditions. | state the service life
duty cycle | The pattern of operation and rest over time. | specify the duty cycle
environmental condition | A surrounding condition affecting operation or storage. | document environmental conditions
acceptance criterion | A condition used to judge whether a result is acceptable. | agree an acceptance criterion
verification method | The means used to check a stated requirement. | select a verification method
testability | The extent to which a claim can be checked by testing. | improve testability
requirement allocation | Assignment of a requirement to a system element. | review requirement allocation
derived requirement | A requirement developed from higher-level needs or analysis. | justify a derived requirement
design margin | Allowance between a predicted value and a defined limit. | preserve design margin
threshold | A stated boundary for an acceptable result. | specify the threshold
objective value | A desired value beyond a minimum acceptable level. | distinguish threshold and objective
assumption register | A record of unverified premises used in planning or design. | update the assumption register
traceability | Recorded connections between needs, requirements, and evidence. | maintain traceability
baseline | An approved reference placed under change control. | establish a baseline
ambiguity | Wording that permits more than one interpretation. | resolve ambiguity
rationale | The reason supporting a requirement or decision. | record the rationale
requirement owner | The role responsible for maintaining a requirement. | identify the requirement owner''',
    precision='Mass is not the same as the mass of the fully populated product. The proposal includes the enclosure, cover, and fasteners but excludes electronics. A five-year target needs defined use conditions and a suitable evidence plan before it can support a durability claim.',
    precision_extra='A proposed value is not an approved baseline. Separate what the meeting clarified from what remains open. Terms such as shall, should, and target also need the meaning assigned by the governing specification, not an assumed universal interpretation.',
    phrases='''Clarify the adjective | What maximum mass would count as lightweight?
Set the boundary | Does that value include the cover and fasteners?
Exclude explicitly | Electronics are outside this mass boundary.
State the proposal | We propose a maximum mass of 1.2 kg.
Qualify the status | This is a proposal, not an approved requirement.
Ask about conditions | What operating temperature range must the enclosure withstand?
Clarify the life claim | Five years under which use and maintenance conditions?
Identify a missing input | The handling conditions have not been specified.
Separate target from evidence | The service-life target is not a demonstrated result.
Ask how to check | Which verification method will support acceptance?
Keep the requirement singular | Separate the mass limit from the service-life requirement.
Protect the boundary | A packaging change should not silently alter the measured assembly.
Connect the need | Which customer task makes this limit necessary?
Record a premise | Put the unconfirmed condition in the assumption register.
Request ownership | Who will confirm the environmental requirements?
Close accurately | We have clarified the proposal, but approval is still pending.''',
    notes='''Lightweight | Needs a value, boundary, and comparison context.
Durable | Needs relevant conditions and a defined life or performance basis.
Maximum | A limit, not the same as a preferred nominal value.
Including | Identifies items counted in the stated boundary.
Proposed | Keeps a discussion value separate from approval.
Demonstrated | Requires evidence appropriate to the exact claim.''',
    d='''Which statement accurately records the mass proposal? | Maximum 1.2 kg for the empty enclosure including cover and fasteners, excluding electronics | Approximately 1.2 kg for any version of the complete product | A guaranteed 1.2 kg for packaging and all components | An approved mass limit for electronics alone | The complete boundary prevents different teams from weighing different assemblies against the same number.
Which sentence avoids overstating durability? | Five years is the proposed service life; operating conditions and verification remain open. | The enclosure has already survived five years. | The proposal proves performance in every environment. | A mass limit establishes service life automatically. | The proposed duration is not evidence of achieved life under unspecified conditions.
What should happen to unresolved environmental assumptions? | Record them with owners for confirmation. | Remove them to make the requirement look finished. | Convert each into a favorable test result. | Let every supplier choose a different interpretation without recording it. | Recording ownership preserves uncertainty and provides a route to resolve the missing inputs.
A prototype meets the proposed mass boundary at 1.15 kg. What does that establish about the five-year target? | Nothing by itself; a mass result does not demonstrate service life under undefined conditions. | Five-year life is verified because 1.15 is below 1.2. | The operating envelope is automatically approved. | The electronics must be included because the measured mass is below the limit. | Mass and durability are different properties with separate boundaries and evidence needs. The mass comparison does not resolve life, conditions, or approval.''',
    dialogue='''Julia | We need the new enclosure to be lightweight and durable. The previous proposal felt too heavy, but our brief does not yet give a numerical limit.
Wei | Let us define the [[maximum mass::Maximum mass states the upper limit, unlike an undefined preference for a lightweight product.]]. Would 1.2 kilograms be the proposed upper limit, and what exactly should be included when we measure it?
Julia | Use that value for discussion. I mean the empty enclosure with its cover and fasteners, not the electronics that our team will install later.
Wei | Then the [[system boundary::The system boundary identifies which physical items count toward the proposed mass limit.]] includes those three items and excludes electronics. I will put that beside the number so nobody compares it with a populated assembly.
Julia | For durability, our commercial team has suggested five years. They have not told us the expected operating temperature or how often the unit will be handled.
Wei | Five years is a proposed [[service life::Service life is the intended period of use under specified conditions, which are still incomplete here.]], not yet a demonstrated result. We need the use conditions before selecting evidence that could support the requirement.
Julia | Could we leave the conditions to the design team? I do not want to slow the project by asking the customer for every detail immediately.
Wei | We can propose an [[operating envelope::The operating envelope defines the conditions under which the design is expected to operate.]], but the customer needs to confirm it. Otherwise we might optimize for conditions that do not match the actual installation.
Julia | I will ask about temperature, humidity, and handling. Some units may move between workstations, so we should not assume they all stay fixed in one installation.
Wei | Record each unresolved premise in the [[assumption register::An assumption register preserves unconfirmed premises and their ownership until they are resolved.]]. Give it an owner and a confirmation point rather than hiding it inside a confident statement about durability.
Julia | Once the conditions are clear, I assume we will need a way to show that the proposal has been met, not just a convincing description.
Wei | Yes. The [[verification method::The verification method specifies how evidence will be obtained to check the requirement.]] must suit the requirement. We should agree what is checked, on which configuration, and what evidence the acceptance decision will use.
Julia | I also want the specification to preserve why we chose the limit. A later reviewer may otherwise change it without understanding the installation problem behind it.
Wei | Keep the [[rationale::The rationale records why the requirement exists and supports later review of changes.]] with the requirement. That helps reviewers assess whether a proposed change still serves the customer need instead of debating the number in isolation.
Julia | Let us send the precise mass proposal now and mark the environmental questions as open. I do not want the clear mass limit to make the whole specification look settled.
Wei | Correct. Clear [[traceability::Traceability links the customer need, requirement, and later evidence without pretending unfinished items are complete.]] will connect the need, the agreed wording, and the eventual evidence. It also makes the unresolved links visible during review.
Julia | I will send the customer the proposed boundary and the missing questions. Please do not label the specification approved until their review is complete.
Wei | We will establish the [[baseline::A baseline is an approved reference, not merely the latest proposal discussed at a meeting.]] only through the agreed approval process. Today's useful result is a precise proposal and an explicit list of remaining decisions.
Julia | Good. I can explain that progress without claiming the enclosure has already met the five-year target. Who should keep the environmental questions moving?
Wei | Name a [[requirement owner::The requirement owner is responsible for maintaining the requirement and coordinating resolution of its open details.]] for that follow-up. The record should say who confirms the conditions and when, so the open questions do not disappear between teams.''',
    transfer_title='A boundary changes the meaning',
    transfer_setup='A proposal limits an empty housing with lid and screws to 0.8 kg. Batteries are excluded. The operating humidity and acceptance test are not yet agreed. Approval remains pending.',
    transfer='''Engineer: "The lid and screws are ___." | included | The supplied boundary explicitly counts the housing, lid, and screws.
Customer: "The batteries are ___." | excluded | Batteries are explicitly outside the proposed mass boundary in this case.
Engineer: "Humidity remains ___." | unresolved | The briefing states that operating humidity has not yet been agreed.
Customer: "This is a proposal, not an approved ___." | baseline | Approval is pending, so the proposal is not an approved reference.''',
    rehearsal=["Read the requirements dialogue. Stress the enclosure, cover, and fasteners included in 1.2 kg, with electronics excluded.","Switch roles. Keep five years as proposed service life while operating conditions, verification, and approval remain open.","Complete and check the transfer. State the 0.8 kg boundary without adding batteries or an approved humidity condition."]))


BOOK['units'].append(unit(
    title='Design Reviews and Technical Pushback',
    scene='The drawing fits; the evidence is missing',
    skill='Challenge a release recommendation by identifying a specific evidence gap and proposing a bounded closure action.',
    brief='At a design review, mechanical lead Ahmed and reviewer Clara examine an enclosure interface. The CAD model shows 2 mm nominal clearance. Requirement R-14 specifies at least 1 mm clearance across the approved dimensional tolerances. The tolerance stack-up has not been documented, and the supplier drawing revision used in the model is unconfirmed. The chair is preparing to recommend release. Clara must distinguish nominal fit from verified minimum clearance and record a specific closure action without claiming the design has already failed.',
    cast='Ahmed | Mechanical lead\nClara | Design reviewer',
    culture=('Push back on the claim, not the person', 'A direct technical challenge can be cooperative when it identifies the requirement, the missing evidence, and the decision affected. State what would resolve the concern. Avoid either approving from politeness or treating an incomplete analysis as proof that a colleague designed a defective product.'),
    a='''What does the CAD model currently show? | 2 mm nominal clearance | A verified 1 mm minimum across all tolerances | The approved supplier revision | A completed tolerance analysis | The model supplies nominal geometry but not the missing tolerance evidence.
What does R-14 require? | At least 1 mm across approved dimensional tolerances | Exactly 2 mm in every assembly | A nominal value greater than zero only | An undocumented supplier agreement | The stated requirement applies across tolerances, not only at nominal dimensions.
What is not established? | Whether the minimum clearance meets R-14 | Whether the CAD view shows a nominal gap | Whether R-14 contains a numerical limit | Whether a release recommendation is being prepared | Without the stack-up and confirmed revision, compliance with the minimum remains unverified.''',
    vocabulary='''design review | A structured examination of a design and its supporting evidence. | conduct a design review
review package | The drawings, analyses, and records provided for review. | complete the review package
nominal dimension | The stated reference dimension before permitted variation. | check the nominal dimension
clearance | The space between adjacent parts. | verify minimum clearance
interference | Unwanted overlap or contact between parts. | identify potential interference
dimensional tolerance | The permitted variation in a specified dimension. | apply dimensional tolerances
tolerance stack-up | The combined dimensional variation affecting an assembly condition. | calculate the tolerance stack-up
worst-case analysis | An assessment using the most adverse allowed combination. | document a worst-case analysis
datum | A reference used to establish dimensional relationships. | identify the datum
mating surface | A surface that joins or interfaces with another part. | inspect the mating surface
CAD model | A computer-aided design representation of geometry. | update the CAD model
drawing revision | The identified version of an engineering drawing. | confirm the drawing revision
assumption log | A record of premises used in an analysis. | review the assumption log
open item | An unresolved matter recorded for follow-up. | assign an open item
closure evidence | Information demonstrating that an open item is resolved. | attach closure evidence
review action | A task assigned as a result of a review. | record a review action
technical objection | A reasoned challenge to a technical claim or decision. | state a technical objection
dissent | A recorded difference of professional judgment. | document unresolved dissent
release recommendation | Advice that a design proceed to a release decision. | qualify a release recommendation
release authority | The role authorized to approve the relevant release. | identify the release authority
conditional approval | Approval explicitly subject to specified conditions, where allowed. | document conditional approval
concurrence | Agreement with a stated position or disposition. | obtain reviewer concurrence
design freeze | A defined point after which design changes require controls. | prepare for design freeze
action closure | Formal resolution of an assigned review task. | verify action closure''',
    precision='A nominal 2 mm gap does not establish the minimum gap across permitted variation. Missing evidence also does not prove physical interference. The supported finding is that R-14 is not yet verified on a confirmed configuration.',
    precision_extra='Conditional approval is meaningful only if the local process permits it and records its conditions, restrictions, and authority. An informal promise to finish the analysis later must not be written as unconditional release approval.',
    phrases='''Locate the concern | My concern is the evidence for R-14.
Acknowledge the work | The nominal geometry is clear in the model.
Distinguish the claim | Nominal clearance is not minimum clearance across tolerances.
Ask for the analysis | Where is the documented tolerance stack-up?
Check the reference | Which supplier drawing revision does the model use?
Avoid alleging failure | I am not saying interference has been demonstrated.
State the gap | We cannot yet verify the required minimum.
Bound the action | Confirm the revision and attach the stack-up for this interface.
Define closure | Closure needs a reviewed result against R-14.
Name responsibility | Ahmed will prepare the analysis for review.
Keep the decision visible | The release recommendation remains unresolved.
Separate meeting roles | Reviewer concurrence is not automatically release authority.
Clarify conditions | What restrictions would apply to conditional approval?
Preserve disagreement | Record the technical objection with its evidence basis.
Prevent silent closure | Do not close the item because the meeting has ended.
Invite resolution | What evidence would let us resolve this concern today?''',
    notes='''Fits | May describe nominal geometry without addressing variation.
Minimum | Must be evaluated against the stated range of conditions.
Unverified | Does not mean demonstrated failure.
No objection | Should not conceal an unresolved technical concern.
Conditional | Needs explicit conditions and an authorized process.
Closed | Requires the specified evidence, not merely an assigned task.''',
    d='''Which review comment is best supported? | R-14 remains unverified pending the stack-up and revision confirmation. | The design definitely interferes because no stack-up is attached. | The nominal gap alone verifies every allowed assembly. | The supplier revision cannot affect interface review. | This comment identifies the evidence gap without converting uncertainty into failure or compliance.
Which closure action addresses both missing inputs for R-14? | Confirm the supplier drawing revision and review the interface tolerance stack-up against the 1 mm minimum. | Measure the nominal CAD gap again and mark the minimum verified. | Confirm the drawing filename without checking the tolerances used. | Obtain meeting attendance signatures and treat them as clearance evidence. | The open item concerns combined allowed variation on an identified configuration. Repeating nominal geometry, checking a filename alone, or recording attendance does not resolve it.
What may the minutes record now? | An open verification item and its assigned follow-up | Unconditional release approval inferred from meeting attendance | A measured clearance failure without measurement or analysis | Supplier concurrence that has not been received | The current record supports a pending item, not an invented approval, failure, or agreement.
What would justify closing the item? | Reviewed evidence for the confirmed configuration against R-14 | Repeating the 2 mm nominal value more confidently | A later meeting date without new evidence | A statement that similar designs usually fit | Closure must resolve the specific requirement and configuration gap identified in the review.''',
    dialogue='''Ahmed | The model shows a two-millimeter gap, and the chair wants to recommend release today. Do you have a specific concern, or can we close the review?
Clara | My concern is the [[tolerance stack-up::The tolerance stack-up evaluates combined dimensional variation rather than relying on the nominal CAD gap.]]. R-14 applies across the permitted dimensional variation, and the supporting calculation is not in the review package.
Ahmed | The nominal geometry is comfortably above one millimeter. I agree that it does not show every combination, but I do not want the team to hear that the design has failed.
Clara | Nor do I. [[Nominal clearance::Nominal clearance describes the reference geometry; it does not establish the smallest gap across allowed variation.]] is two millimeters. The minimum remains unverified, which is different from saying that interference has been observed or established.
Ahmed | That is a fair distinction. The model also came from the supplier file, but I cannot confirm which drawing issue was used without checking our records.
Clara | Confirm the [[drawing revision::The drawing revision identifies the supplier geometry and tolerances that the analysis must actually evaluate.]] before completing the calculation. An analysis of an obsolete interface could look convincing while answering the wrong configuration question.
Ahmed | Please replace check fit with the actual task: confirm the supplier revision and assess minimum clearance against R-14. I can own that analysis.
Clara | Exactly. Make it a [[review action::A review action assigns a specific task arising from the meeting, rather than leaving an unowned concern.]] with an owner and a review point. The task is narrow enough to complete without reopening unrelated parts of the design.
Ahmed | I can own the analysis. I will identify the confirmed supplier revision, state the tolerance assumptions, and present the resulting minimum against R-14.
Clara | That provides the intended [[closure evidence::Closure evidence must show that the specific requirement gap has been resolved on the confirmed configuration.]]. The reviewer still needs to assess the result; attaching a file is not itself the same as resolving the concern.
Ahmed | Could the chair record conditional approval and allow the release team to continue? I want to avoid delaying work that does not depend on this interface.
Clara | [[Conditional approval::Conditional approval must follow the applicable process and state its limits; it cannot silently mean unrestricted release.]] is only available if our process permits it. The record would need clear restrictions and the appropriate decision maker, not a casual promise to finish later.
Ahmed | I will ask the chair to separate any permitted preparatory work from release. We should not imply that every downstream activity has the same dependency.
Clara | Agreed. Identify the [[release authority::The release authority is the role permitted to make the release decision, distinct from individual reviewers.]] and let that role decide on the recorded basis. My review comment should not be mistaken for unilateral approval or rejection.
Ahmed | That is a concern I can answer. Keep the comment tied to the missing stack-up and revision, so the team knows exactly what needs closing.
Clara | A [[technical objection::A technical objection challenges a defined claim with reasons and a route to resolution, not a colleague's competence.]] should be answerable. Here the requirement, missing analysis, and configuration question make the concern concrete enough for us to resolve.
Ahmed | I will revise the minutes to keep the interface item open. The release recommendation will remain unresolved until the evidence and required review are available.
Clara | Keep that [[open item::An open item records the unresolved matter until the stated closure conditions are satisfied.]] visible in the action list. A meeting ending or an owner accepting the task must not make its status appear complete.
Ahmed | Once the reviewed analysis is available, we can record the result and route the recommendation to the authorized decision maker with any remaining conditions.
Clara | Yes. [[Action closure::Action closure requires verified resolution of the assigned task, not simply an intention to provide evidence later.]] should identify the evidence and reviewer. That gives the release decision a traceable basis while preserving what the team actually established.''',
    transfer_title='A nominal fit is not a verified minimum',
    transfer_setup='A model shows 3 mm nominal clearance. The requirement specifies at least 1 mm across tolerances. The stack-up is missing, and the supplier revision is not confirmed.',
    transfer='''Reviewer: "Three millimeters is the ___ clearance." | nominal | The value comes from reference geometry, not a completed variation analysis.
Engineer: "The supplier revision needs ___." | confirmation | The briefing explicitly says the supplier revision has not been confirmed.
Reviewer: "The minimum remains ___." | unverified | A missing stack-up prevents verification of the required minimum across tolerances.
Engineer: "The item closes with reviewed ___." | evidence | Closure needs evidence addressing the requirement, not merely a repeated nominal value.''',
    rehearsal=["Read the design review. Contrast the 2 mm nominal gap with R-14's minimum of 1 mm across tolerances.","Switch roles. Request the confirmed supplier revision and reviewed stack-up without announcing interference or release approval.","Complete and check the transfer. Keep the 3 mm nominal value distinct from the unverified minimum and evidence needed for closure."]))


BOOK['units'].append(unit(
    title='Failure Modes and Reliability',
    scene='One interruption, several possible explanations',
    skill='Report a failure observation precisely, distinguish mechanism from cause, and propose evidence-led investigation language.',
    brief='During a planned 60-minute bench run, sample S7 stops producing an output at minute 46. Test engineer Grace and reliability engineer Pavel review the event. The failure has not been reproduced. The test setup has not been checked, and connector damage is only a hypothesis. The team has not established a population failure rate or a corrective action. Grace must preserve the result and test records while preventing a draft report from naming connector damage as the confirmed root cause.',
    cast='Grace | Test engineer\nPavel | Reliability engineer',
    culture=('A plausible explanation is still a hypothesis', 'Technical teams often converge quickly on a familiar failure mechanism. Use language that invites testing of the explanation without dismissing experience. Keep the observed event, possible causes, immediate controls, and eventual corrective action in separate statements so confidence does not outrun evidence.'),
    a='''What was directly observed? | S7 stopped producing an output at minute 46. | Connector damage was confirmed by inspection. | Every sample failed before an hour. | The test setup passed all checks. | The briefing gives an output interruption on one identified sample, not a confirmed explanation.
Which statement accurately describes the cause? | Connector damage is an unconfirmed hypothesis. | Connector damage is the established root cause. | The test fixture has been ruled out. | The component population is known to be defective. | Neither reproduction nor setup checks have established the cause of the event.
What cannot be calculated from the supplied facts alone? | A representative population failure rate | The time of the observed interruption | The planned run duration | Whether the sample reached the full planned duration | A single reported event without an adequate exposure and sampling basis does not establish population reliability.''',
    vocabulary='''failure mode | The way an item fails to perform its required function. | describe the failure mode
failure effect | The consequence of a failure at a stated level. | assess the failure effect
failure mechanism | The physical or other process producing a failure. | investigate the failure mechanism
root cause | An underlying cause supported by an appropriate investigation. | establish the root cause
hypothesis | A proposed explanation that requires testing. | test a hypothesis
anomaly | An observed departure from expected behavior. | record an anomaly
intermittent fault | A fault that appears and disappears under some conditions. | investigate an intermittent fault
reproducibility | Measurement precision under specified changed conditions, such as different laboratories or operators. | assess reproducibility
repeatability | Agreement of repeated measurements under the same stated conditions. | check repeatability
test setup | The equipment and arrangement used for a test. | verify the test setup
test fixture | Equipment that holds or connects the item during testing. | inspect the test fixture
failure analysis | Investigation of evidence about a failure and its causes. | commission failure analysis
fault isolation | Narrowing a fault to a component, location, or cause. | support fault isolation
diagnostic evidence | Information used to distinguish possible explanations. | preserve diagnostic evidence
event log | A time-ordered record of system or test events. | export the event log
specimen | An identified item submitted for examination or testing. | preserve the specimen
containment | An immediate measure to limit exposure while investigation continues. | define containment
corrective action | An action addressing an established cause to prevent recurrence. | evaluate corrective action
recurrence | Reappearance of a previously observed problem. | monitor recurrence
FMEA | Failure mode and effects analysis, a structured review of possible failures and consequences. | update the FMEA
severity | The seriousness of a stated consequence. | assess severity
occurrence | The likelihood or frequency of a failure cause or event on a defined basis. | estimate occurrence
detectability | The ability of controls to identify a condition before its consequence. | assess detectability
residual uncertainty | What remains unknown after available evidence is considered. | state residual uncertainty''',
    precision='The observed mode is loss of output, not connector damage. A connector problem might explain the event, but it remains a hypothesis. Checking the setup is necessary to interpret the result; it does not justify deleting an inconvenient observation.',
    precision_extra='Failure mode, effect, and cause answer different questions: what failed, what happened as a consequence, and why. FMEA ratings depend on the chosen method and evidence. Do not invent a universal score or infer a population failure rate from this case.',
    phrases='''State the observation | S7 stopped producing an output at minute 46.
Preserve the duration | The planned run was 60 minutes.
Separate cause from symptom | Loss of output is the observed mode, not the confirmed cause.
Qualify the explanation | Connector damage is one hypothesis under investigation.
Name missing checks | The test setup has not yet been checked.
Avoid premature exclusion | We have not ruled out a fixture-related explanation.
Protect the record | Preserve the sample identification and event log.
Request discriminating evidence | Which observation would distinguish the competing explanations?
Keep the result | An unresolved cause does not erase the observed interruption.
Limit the inference | This case does not establish a population failure rate.
Separate action types | Containment can precede a confirmed corrective action.
Avoid a false fix | A replacement alone would not prove the cause was removed.
Clarify recurrence | Has the same mode reappeared under documented conditions?
Use FMEA carefully | Link the mode to its possible effects and causes.
State the uncertainty | The mechanism remains unresolved.
Close the update | Report the event, current hypotheses, next checks, and review point.''',
    notes='''Failed | Needs a required function, condition, and identified item.
Because | Signals a causal claim and needs supporting evidence.
Suspected | Marks an explanation as provisional.
Could not reproduce | Does not establish that the original event was imaginary.
Contained | Does not mean the underlying cause has been removed.
Fixed | Should be supported by cause-based action and appropriate verification.''',
    d='''Which draft sentence should replace "connector damage caused the failure"? | S7 lost output at minute 46; connector damage remains a hypothesis. | S7 probably worked normally because the setup is unchecked. | All connectors in the product are defective. | The failure rate is one per 46 minutes for every unit. | The replacement preserves the observation while accurately qualifying the unconfirmed cause.
Why preserve the event log and sample identity? | They connect the investigation to the actual event and configuration. | They automatically prove which component caused the interruption. | They replace all further diagnostic work. | They establish that every later sample will behave identically. | Traceable records let investigators evaluate the event without inventing a causal conclusion.
A later repeat run shows no interruption. What should happen to the original S7 result? | Retain the minute-46 event and investigate why the observations differ; one repeat does not identify the cause. | Delete it because the latest run replaces every earlier observation. | Confirm connector damage because the event is intermittent. | Declare the test setup fault-free because the repeat ran normally. | A non-recurrence in a later run does not erase the original observation or distinguish the connector, fixture, setup, and other possible explanations.
Which wording distinguishes containment from corrective action? | Exposure controls may begin while the cause-based action remains undecided. | Containment proves that recurrence is impossible. | A suspected cause is enough to declare permanent correction. | Every temporary control removes the underlying mechanism. | Immediate exposure management and action against an established cause have different purposes.''',
    dialogue='''Grace | S7 stopped producing an output at minute forty-six of the planned hour. The draft report says connector damage caused the failure, but we have not examined that explanation yet.
Pavel | Start with the [[failure mode::The failure mode is loss of output, the observed way the sample stopped meeting its intended function.]]. Loss of output is what we observed. Connector damage is a proposed explanation, and the wording needs to preserve that distinction.
Grace | The team has seen similar symptoms before, which is why the explanation sounds persuasive. I do not want to ignore their experience, but this event has not been reproduced.
Pavel | Treat it as a [[hypothesis::A hypothesis is a plausible explanation to investigate, not an established finding based on this event.]]. Prior experience can guide the investigation without allowing us to write the conclusion before examining this sample and its records.
Grace | The setup checks are still open too. Can we examine the fixture and connection without treating either as the explanation before we have the evidence?
Pavel | Review the [[test setup::The test setup includes the fixture and connections whose condition may affect interpretation of the sample result.]] under the approved process. That is part of interpreting the event, not a reason to dismiss the sample interruption as inconvenient.
Grace | I have S7's identifier, the event time, and the configuration details. What other original records should I attach before the team starts the investigation?
Pavel | Preserve the [[event log::The event log retains time-ordered evidence connecting the observed interruption to the test and sample.]] as well. We need the original sequence, including anything recorded before the output stopped, rather than a summary written from memory.
Grace | The manager asked whether one failure means the whole population is unreliable. I can report this event, but we do not have the information for that broader conclusion.
Pavel | State the [[residual uncertainty::Residual uncertainty includes the unresolved cause and the limits on any population-level reliability claim.]] plainly. This record does not establish a representative population failure rate, and neither a reassuring nor an alarming estimate should be invented.
Grace | We should also be clear about what happened beyond the sample. Loss of output is the mode, while the consequence depends on the function it serves.
Pavel | Correct. Describe the [[failure effect::The failure effect is the consequence of the mode at a stated level, distinct from the mechanism causing it.]] at the relevant level. Do not let the consequence, the observed mode, and the suspected cause become interchangeable labels.
Grace | Would it be useful to record the possible mode and causes in the structured review now, even while the evidence remains incomplete?
Pavel | Yes, update the [[FMEA::FMEA connects possible failure modes, their effects, causes, and controls without converting hypotheses into proven causes.]] where appropriate, with the uncertainty visible. Its entries should support investigation and control decisions, not give an unsupported explanation the appearance of formal proof.
Grace | We may need an immediate restriction while the investigation continues. I want to avoid calling that restriction a permanent fix in the status update.
Pavel | Call it [[containment::Containment limits immediate exposure while the underlying cause and permanent response may still be unresolved.]] if that is its actual purpose. The responsible team must define the measure and its limits; the name does not establish that recurrence is prevented.
Grace | Once evidence supports a cause, we can assess a response against it. Simply replacing something and observing a short successful run would not settle every question.
Pavel | A [[corrective action::Corrective action addresses an established cause and requires appropriate evidence that the intended correction works.]] needs a cause-based rationale and appropriate verification. Keep the action proposal separate from evidence that it has removed the problem.
Grace | I will revise the report to state the interruption, the unconfirmed connector explanation, the unchecked setup, and the next investigation review. The original result will stay in the record.
Pavel | That supports [[failure analysis::Failure analysis systematically evaluates the preserved evidence and possible explanations rather than endorsing the first plausible story.]]. We can communicate progress honestly without choosing a cause early or allowing uncertainty to make the observed event disappear.''',
    transfer_title='Observed does not mean explained',
    transfer_setup='Sample K4 loses its signal during a run. A damaged cable is suspected, but neither the cable nor the fixture has been checked. The original log is available.',
    transfer='''Tester: "Loss of signal is the observed failure ___." | mode | The mode describes how the required function failed, not why it failed.
Engineer: "Cable damage is still a ___." | hypothesis | The suspected explanation has not been confirmed by the stated checks.
Tester: "We will preserve the original ___." | log | The available original log is relevant evidence for the recorded event.
Engineer: "The root cause remains ___." | unresolved | Neither the cable nor the fixture has been checked, so the cause is not established.''',
    rehearsal=["Read the failure discussion. State S7, minute 46, and the planned 60-minute run before naming the connector hypothesis.","Switch roles. Separate the observed mode, possible cause, setup checks, containment, and cause-based corrective action.","Complete and check the transfer. Preserve K4's original log and keep cable damage unconfirmed."]))

BOOK['units'].append(unit(
    title='Testing, Validation, and Data Interpretation',
    scene='Three passes do not mean every condition',
    skill='Report prototype results with their sample, conditions, criterion, and limits while distinguishing verification from broader validation.',
    brief='Test lead Ben reviews a presentation with design engineer Amina. Three revision-B prototypes completed a two-hour bench test at 20 degrees Celsius. Their recorded maximum response times were 150, 160, and 175 milliseconds; the test criterion was no more than 200 milliseconds. All three met that criterion. The intended operating range extends from 10 to 40 degrees Celsius, but those other temperatures were not tested. The presentation currently claims that the design is proven for every operating condition.',
    cast='Ben | Test lead\nAmina | Design engineer',
    culture=('Lead with the result and its boundary', 'A qualified result can still be useful and positive. State what passed before explaining what was not tested. This avoids both overclaiming and burying genuine progress under vague caution. List the exact evidence gap that limits the wider claim.'),
    a='''Which result is supported? | All three prototypes met the stated bench criterion at 20 degrees Celsius. | The complete operating range was tested. | Every future unit will meet the criterion. | The design has a proven lifetime reliability of 100%. | Each recorded maximum is below 200 milliseconds, but the conditions and sample are limited.
Which value was the largest recorded maximum? | 175 milliseconds | 200 milliseconds | 160 milliseconds | 150 milliseconds | The three recorded maxima are 150, 160, and 175 milliseconds.
What remains untested in this case? | Performance at the other temperatures in the intended range | All three revision-B prototypes | The stated two-hour duration at 20 degrees Celsius | The recorded response-time criterion at 20 degrees Celsius | Only 20 degrees Celsius was tested; the remaining intended temperatures were not covered.''',
    vocabulary='''test protocol | The documented plan and procedure for a test. | approve the test protocol
test condition | A specified circumstance under which a test is conducted. | record test conditions
test article | The identified item subjected to testing. | identify the test article
sample size | The number of items or observations in a stated sample. | report the sample size
acceptance limit | The boundary used to judge a measured result. | compare with the acceptance limit
response time | The time between a defined input and response. | measure response time
observed maximum | The largest value recorded in the stated observations. | report the observed maximum
measurement uncertainty | A quantified expression of doubt about a measured value. | evaluate measurement uncertainty
instrument calibration | Establishing the relation between instrument indications and reference values. | check instrument calibration
resolution | The smallest distinguishable change in a measurement or indication. | specify instrument resolution
test coverage | The requirements or conditions addressed by the performed tests. | identify gaps in test coverage
boundary condition | A limiting input or operating condition used in analysis or testing. | examine boundary conditions
verification | Checking that specified requirements have been met. | complete requirement verification
validation | Assessing whether a product meets intended-use needs. | plan intended-use validation
representativeness | How well a sample or condition reflects the target use or population. | assess representativeness
extrapolation | Extending a conclusion beyond the observed range. | avoid unsupported extrapolation
confidence interval | A statistical interval constructed by a method with stated coverage properties. | report a confidence interval
pass fraction | The proportion of tested items meeting a stated criterion. | calculate the observed pass fraction
population | The full set of items about which an inference is intended. | define the target population
censored observation | A lifetime observation ending before the event of interest occurs. | account for censored observations
test duration | The length of time a test runs. | state the test duration
reliability claim | A statement about performance without failure under stated conditions over time. | qualify a reliability claim
test deviation | A recorded departure from the approved test procedure. | assess a test deviation
evidence boundary | The limit of what the available evidence establishes. | state the evidence boundary''',
    precision='Three out of three is a 100% observed pass fraction for this test. It is not proof of perfect reliability in the population or across the operating range. The largest recorded maximum, 175 ms, is 25 ms below the stated 200 ms criterion.',
    precision_extra='Verification checks specified requirements; validation addresses intended-use needs. Passing one bench criterion does not settle both. No uncertainty budget, statistical sampling plan, or lifetime model is supplied here, so do not invent a confidence level or a life prediction.',
    phrases='''Lead with the result | All three prototypes met the stated criterion.
Name the configuration | These results apply to revision B.
Give the conditions | The test ran for two hours at 20 degrees Celsius.
State the criterion | The response-time limit was 200 milliseconds.
Report the largest value | The largest recorded maximum was 175 milliseconds.
Preserve the unit | These values are in milliseconds, not seconds.
Bound the percentage | The observed pass fraction was three out of three.
Avoid population overclaim | That is not proof that every production unit will pass.
Identify missing coverage | The other intended temperatures were not tested.
Separate purposes | This bench check is not complete intended-use validation.
Qualify the headline | Replace proven everywhere with the result actually demonstrated.
Ask about uncertainty | Where is the measurement-uncertainty assessment?
Keep records connected | Link the result to its test article and protocol.
Avoid invented confidence | The supplied data do not provide a stated confidence level.
Preserve positive progress | The test supports this criterion under these conditions.
Close the report | State the result, conditions, limitation, and next evidence need.''',
    notes='''Passed | Always attach the criterion and tested configuration.
Proven | Usually overbroad without a clearly bounded claim.
100% | Can describe a sample proportion without proving population certainty.
Maximum | Specify whether observed, allowed, or predicted.
Representative | Requires a reason why the sample reflects intended use.
Validation | Do not use it as a synonym for any successful bench test.''',
    d='''Which presentation headline is most accurate? | Three revision-B prototypes met the response-time criterion in the stated bench test. | Revision B is proven across all operating conditions. | Every manufactured unit will respond within 175 milliseconds. | Two hours establish the complete service life. | The headline reports the demonstrated sample result without extending it to untested conditions or units.
What does the observed 100% pass fraction mean? | All three tested items met this criterion in this test. | The true population failure probability is known to be zero. | The entire 10-to-40-degree range has been covered. | No additional evidence could change the assessment. | A sample pass fraction describes these observations and does not establish universal reliability.
The largest recorded maximum is 175 ms against a 200 ms limit. Which statement is precise? | The observed gap to the limit is 25 ms; no supplied uncertainty budget establishes a guaranteed margin for all units. | The product is guaranteed to remain 25 ms below the limit at every temperature. | The limit should be revised to 175 ms because that is the largest observed value. | The gap is 25 seconds, proving the five-year service target. | Subtraction gives 25 milliseconds for the reported result. That arithmetic does not extend the sample, cover other temperatures, or supply a measurement-uncertainty assessment.
Which limitation is specific and useful? | Performance at the other intended temperatures was not tested. | Nothing at all can be learned from the test. | The design necessarily fails at every untested temperature. | All intended-use requirements are automatically satisfied. | This identifies the missing coverage without denying the observed passes or inventing failures.''',
    dialogue='''Amina | The presentation says the design is proven for every operating condition. All three prototypes passed, so I thought that was a concise way to report the positive result.
Ben | We can report the [[pass fraction::The pass fraction is three passing prototypes out of three tested, limited to this criterion and test.]], but the headline goes further. Three out of three describes the tested sample, not every unit or every condition in the operating range.
Amina | Let us put the actual conditions beside the result. These were revision-B prototypes, tested for two hours at twenty degrees Celsius under the bench procedure.
Ben | Those [[test conditions::Test conditions specify the temperature, duration, and procedure under which the observations were obtained.]] are essential. Readers should not have to search an appendix to discover that the rest of the intended temperature range was not tested.
Amina | The recorded maximum response times were one hundred fifty, one hundred sixty, and one hundred seventy-five milliseconds. The criterion allowed up to two hundred milliseconds.
Ben | Then the largest [[observed maximum::The observed maximum is the largest recorded value, not a guaranteed limit for every future unit or condition.]] was one hundred seventy-five. That is twenty-five milliseconds below the criterion, but it is not a universal product limit.
Amina | I will write three out of three met the criterion. That is clearer than a large one-hundred-percent headline with the sample size hidden below it.
Ben | Exactly. Keep the [[sample size::Sample size identifies the three prototypes behind the percentage and prevents an impression of broader evidence.]] visible. A percentage can sound much more comprehensive than the underlying evidence when the number of tested items is omitted.
Amina | The intended operating range is ten to forty degrees. Since we tested only twenty, the other temperatures remain a gap rather than a demonstrated pass.
Ben | That is a [[test coverage::Test coverage describes which requirements and conditions were actually addressed, exposing the untested temperature range.]] limitation. State it directly; do not imply the untested temperatures failed, but do not label them verified either.
Amina | Would it help to distinguish checking this performance criterion from confirming that the product works adequately for its intended users and operating tasks?
Ben | Yes. This supports [[verification::Verification checks a specified requirement; this bench result does not by itself establish complete intended-use suitability.]] of the stated criterion under the recorded conditions. Broader intended-use questions need their own evidence and cannot be settled by relabeling this test.
Amina | The slide also calls the product fully validated. We have not supplied evidence for the complete use context, so that phrase creates a second overclaim.
Ben | Remove the unsupported [[validation::Validation addresses intended-use needs, which are broader than the single bench criterion described here.]] claim. We can explain what has been demonstrated and which intended-use evidence remains outstanding without making the result sound like a failure.
Amina | What should I say if someone asks about ten and forty degrees? We have no supporting model or test at those temperatures in this package.
Ben | Then that would be unsupported [[extrapolation::Extrapolation extends conclusions beyond the observed temperature; no supporting model or additional evidence is supplied here.]]. Do not substitute a plausible expectation for evidence, especially when the presentation may guide a release or customer commitment.
Amina | I will also avoid adding a confidence percentage. The supplied records do not include a statistical sampling plan, uncertainty budget, or lifetime analysis.
Ben | Correct. A [[reliability claim::A reliability claim requires a defined performance, time, conditions, and supporting basis beyond a small unqualified pass count.]] needs its own defined basis. The fact that no failure occurred in these runs does not establish a zero population failure probability.
Amina | The revised headline will say three revision-B prototypes met the response-time criterion during a two-hour bench test at twenty degrees. The next sentence will identify the untested temperatures.
Ben | That states the [[evidence boundary::The evidence boundary separates the supported bench result from broader claims about other conditions, units, or lifetime.]] clearly. We retain the positive result and give the review team enough context to decide what additional evidence is needed.''',
    transfer_title='Four passes, one tested temperature',
    transfer_setup='Four prototypes pass a three-hour bench test at 25 degrees Celsius. The intended range also includes lower and higher temperatures, which were not tested. No population reliability estimate is supplied.',
    transfer='''Engineer: "The tested sample size was ___." | four | The briefing identifies four prototypes in this particular bench test.
Reviewer: "The duration was three ___." | hours | The supplied test duration is three hours, not a service-life result.
Engineer: "The other temperatures remain ___." | untested | The briefing explicitly excludes testing at the other intended temperatures.
Reviewer: "The result does not establish population ___." | reliability | No population reliability estimate or adequate supporting basis is supplied.''',
    rehearsal=["Read the test-results dialogue. Say three prototypes, revision B, two hours, 20 degrees Celsius, and the 200 ms criterion.","Switch roles. Bound the 175 ms observed maximum and 100% sample pass fraction without extending them across 10-40 degrees Celsius.","Complete and check the transfer. Keep four passes at 25 degrees Celsius separate from untested temperatures and population reliability."]))


BOOK['units'].append(unit(
    title='Manufacturability and Cost Engineering',
    scene='Cheaper material, more expensive assembly',
    skill='Compare design costs on the same volume and cost basis while keeping manufacturability and approval separate from arithmetic.',
    brief='Design engineer Tessa and manufacturing engineer Arun compare two proposed housings for 3,000 acceptable units. Option A has material cost of $8 and assembly cost of $6 per unit, plus $1,000 one-time tooling. Option B has material cost of $10 and assembly cost of $2 per unit, plus $5,000 tooling. These are the only cost elements in the comparison, with no scrap assumed. Technical suitability, supplier capacity, and approval are unresolved. A slide nevertheless recommends A solely because its material is cheaper.',
    cast='Tessa | Design engineer\nArun | Manufacturing engineer',
    culture=('Compare like with like', 'An engineer can challenge a cost recommendation without challenging the cost-saving objective. Put both alternatives on the same quantity, cost categories, and assumptions. Then distinguish the numerical result from the separate evidence needed to select and release a design.'),
    a='''What is the recurring material-plus-assembly cost of A? | $14 per unit | $8 per unit | $6 per unit | $12 per unit | Adding A's stated material cost of eight dollars and assembly cost of six gives fourteen.
What is the total stated cost of B for 3,000 units? | $41,000 | $36,000 | $35,000 | $47,000 | Three thousand units at twelve dollars cost thirty-six thousand, plus five thousand in tooling.
What remains unresolved after the calculation? | Technical suitability, capacity, and approval | The supplied tooling amount for A | The supplied material cost for B | The stated comparison quantity | The briefing explicitly leaves technical and supply decisions open despite the available cost figures.''',
    vocabulary='''manufacturability | How readily a design can be produced by the intended process. | assess manufacturability
design for assembly | Design choices that simplify or improve assembly, abbreviated DFA. | apply design for assembly
design for manufacture | Design choices suited to the intended manufacturing process, abbreviated DFM. | review design for manufacture
bill of materials | The structured list of parts and materials in a product, abbreviated BOM. | compare the bill of materials
material cost | The stated cost of materials used in a unit. | estimate material cost
assembly cost | The cost assigned to assembling a unit. | reduce assembly cost
recurring cost | A cost incurred repeatedly as units are produced. | compare recurring cost
nonrecurring cost | A cost incurred once for the defined program or setup. | identify nonrecurring cost
tooling investment | Expenditure on equipment or tools needed for production. | justify tooling investment
unit cost | Cost per unit on a stated inclusion and volume basis. | calculate unit cost
cost model | A structured calculation connecting cost assumptions and totals. | review the cost model
cost driver | A factor that materially changes cost. | identify the cost driver
production volume | The number of units made in a stated period or program. | state production volume
break-even volume | The quantity at which compared total costs are equal. | calculate break-even volume
incremental cost | The change in cost between specified alternatives. | compare incremental cost
cost trade-off | An exchange between cost categories or other design outcomes. | explain the cost trade-off
process capability | The ability of a stable process to meet specified limits. | assess process capability
cycle time | Time taken for one defined production cycle. | measure cycle time
takt time | Available production time divided by required customer demand. | compare cycle time with takt time
scrap allowance | A stated cost or quantity provision for unusable production. | include a scrap allowance
yield assumption | The assumed proportion of production meeting a defined criterion. | challenge the yield assumption
tolerance relaxation | Widening a dimensional limit subject to design requirements. | assess tolerance relaxation
part consolidation | Combining functions to reduce the number of separate parts. | evaluate part consolidation
make-or-buy decision | Choosing between internal production and external supply. | support a make-or-buy decision''',
    precision='A costs $43,000 and B costs $41,000 for 3,000 units on the stated basis. B saves $2 per unit in recurring cost but requires $4,000 more tooling. Their totals are equal at 2,000 units. These arithmetic results do not establish technical suitability.',
    precision_extra='Unit cost can include different categories. Name the categories before comparing figures. This case excludes other cost elements and assumes no scrap; those simplifying assumptions must not be presented as a complete real-world business case.',
    phrases='''Set the comparison | Use the same 3,000-unit quantity for both options.
Name the categories | Include material, assembly, and one-time tooling.
Challenge the narrow claim | Lower material cost does not necessarily mean lower total cost.
Add recurring costs | A has $14 of material and assembly cost per unit.
State the alternative | B has $12 of recurring cost per unit.
Keep tooling separate | B requires $4,000 more upfront tooling.
Give the total | The stated totals are $43,000 for A and $41,000 for B.
Explain the difference | B is $2,000 lower at this volume.
Identify the crossover | The total costs are equal at 2,000 units.
Qualify the model | The comparison includes only the listed cost elements.
Expose the assumption | No scrap is assumed in these figures.
Protect technical criteria | A cost advantage does not establish manufacturability.
Ask about capacity | Can the proposed process deliver the required volume?
Avoid premature selection | B leads on this cost basis, pending the other reviews.
Check the denominator | Which production quantity supports that unit-cost figure?
Close the recommendation | Separate the cost result from the design approval decision.''',
    notes='''Cheaper | Needs a cost boundary and quantity.
Per unit | Can mean recurring cost or a total allocated over volume.
Upfront | Describes timing, not automatically recoverability.
Break-even | Here means equal option totals, not business profitability.
No scrap | A model assumption, not proof of perfect production yield.
Preferred | State the criterion on which the preference is based.''',
    d='''Which recommendation is supported at 3,000 units? | B has the lower stated cost, subject to unresolved technical and capacity reviews. | A must be chosen because its material costs less. | B is technically approved because its calculated total is lower. | A and B have equal totals at every quantity. | B's total is two thousand dollars lower, but cost arithmetic does not resolve the other reviews.
At which volume are the stated totals equal? | 2,000 units | 500 units | 3,000 units | 4,000 units | B's additional four-thousand-dollar tooling cost is offset by two dollars per unit at two thousand units.
B saves $2 per unit for 3,000 units. Why is the stated total saving $2,000 rather than $6,000? | The $6,000 recurring saving is offset by B's $4,000 additional tooling. | B's $5,000 tooling should be deducted twice. | A's tooling is recurring and must be multiplied by 3,000. | The two-dollar difference applies only to the first 1,000 units. | Recurring savings are 3,000 times $2. Tooling differs by $5,000 minus $1,000, so the net difference is $6,000 minus $4,000 = $2,000.
Why should the model state no scrap? | Different production yields could change the cost comparison. | The assumption proves every real unit will be acceptable. | Tooling cost disappears when scrap is excluded. | Scrap can never affect unit cost. | A stated simplification is needed because actual losses may alter the cost of acceptable output.''',
    dialogue='''Tessa | The slide recommends A because its material costs eight dollars per unit instead of ten. I have not included assembly or tooling in that recommendation yet.
Arun | Then we need the full stated [[cost model::The cost model combines the same cost categories and quantity for both alternatives rather than comparing material alone.]] before recommending an option. Use material, assembly, and one-time tooling for three thousand acceptable units, with no scrap.
Tessa | A is eight plus six, so fourteen per unit. B is ten plus two, so twelve. The cheaper material does not give A the cheaper repeated work.
Arun | Correct. B saves two dollars in [[recurring cost::Recurring cost is the material-plus-assembly amount incurred for each unit, excluding the one-time tooling.]] per unit. That comparison includes assembly but not either option's one-time production equipment expense.
Tessa | Two dollars times three thousand gives six thousand saved. Should I put six thousand as the overall saving on the slide?
Arun | Not yet. B's [[tooling investment::Tooling investment is the one-time amount added to the recurring production total for each option.]] is five thousand against A's one thousand. Subtract that additional four thousand from the recurring saving; the overall difference is two thousand.
Tessa | Let me check the totals: A is forty-two thousand plus one thousand, and B is thirty-six thousand plus five thousand. Forty-three versus forty-one thousand.
Arun | Yes, at the stated [[production volume::Production volume is the three-thousand-unit basis that determines how recurring savings compare with fixed tooling differences.]] of three thousand. Attach the quantity to the conclusion; a smaller order may not recover B's extra upfront expense.
Tessa | The extra tooling is four thousand and the recurring difference is two per unit. Dividing gives two thousand units. Is that where the costs are equal?
Arun | That is the [[break-even volume::Break-even volume is two thousand units because the two-dollar saving offsets four thousand dollars of additional tooling.]]. At two thousand units, A is twenty-eight thousand plus one thousand; B is twenty-four thousand plus five thousand. Both total twenty-nine thousand.
Tessa | At only one thousand units, A becomes fifteen thousand and B seventeen thousand. So saying B is always cheaper would also be wrong.
Arun | Exactly. State the [[cost trade-off::The cost trade-off exchanges higher upfront tooling for lower recurring assembly-inclusive cost.]]: higher tooling buys lower recurring expense. The comparison changes with quantity even before we examine any unlisted costs.
Tessa | Can we recommend buying B now that it wins this calculation? Its assembly estimate is attractive, but technical suitability has not been reviewed.
Arun | No. Its [[manufacturability::Manufacturability concerns producing the design by the intended process; a lower calculated price does not establish it.]] is still unresolved. The cost sheet does not show that the proposed process can produce a housing meeting the design requirements.
Tessa | I also need the supplier's capacity confirmation. Having enough machines available would answer volume, but not necessarily whether the parts meet dimensional limits.
Arun | Right. Assess [[process capability::Process capability concerns meeting specified limits in a stable process and is distinct from a quoted cost or available capacity.]] separately from capacity. Consistent conformance under a stable process and available production quantity are different questions.
Tessa | We assumed every produced unit is acceptable. I will state that clearly, rather than present the model as though we measured the supplier's losses.
Arun | Keep that [[yield assumption::The yield assumption is the no-scrap premise used here; different actual yields could change acceptable-unit cost.]] beside the totals. Scrap or rework could change acceptable-unit cost; the present comparison includes only the three listed cost categories.
Tessa | I will revise the slide: B is two thousand lower at three thousand units on the stated basis, pending suitability, capacity, and approval. No purchase is authorized.
Arun | Also label each [[unit cost::Unit cost must identify included categories and volume; otherwise recurring-only and tooling-inclusive figures can be confused.]] figure as recurring-only or tooling-inclusive. That will stop the next reader comparing twelve dollars with a total-cost figure from another volume.''',
    transfer_title='When the quantity changes the answer',
    transfer_setup='Option C costs $9 per unit plus $2,000 tooling. Option D costs $7 per unit plus $6,000 tooling. Only these costs apply, with no scrap. Compare 1,000 units.',
    transfer='''Engineer: "C totals ___ dollars." | 11000 | Nine dollars times one thousand units plus two thousand tooling equals eleven thousand.
Reviewer: "D totals ___ dollars." | 13000 | Seven dollars times one thousand units plus six thousand tooling equals thirteen thousand.
Engineer: "At this quantity, the lower-cost option is ___." | C | C costs eleven thousand, which is two thousand less than D.
Reviewer: "Equal totals occur at ___ units." | 2000 | D's four-thousand-dollar additional tooling is offset by two dollars per unit at two thousand.''',
    rehearsal=["Read turns 1-10. Correct the $6,000 recurring saving to $2,000 overall after the extra tooling, then check the 2,000-unit crossover.","Switch roles for turns 11-20. Separate cost, capacity, process capability, and design approval.","Complete and check the transfer. Calculate C at $11,000 and D at $13,000 for 1,000 units, then state the 2,000-unit crossover."]))

BOOK['units'].append(unit(
    title='Safety Factors and Compliance',
    scene='A ratio is not a compliance decision',
    skill='Question a compliance claim by identifying the applicable requirement, analysis basis, evidence scope, and decision authority.',
    brief='Engineer Rosa and assurance lead Malik review a fictional design note labeled compliant. A preliminary static model reports a safety factor of 2.0 using its stated capacity-to-demand convention. The applicable requirement, acceptance threshold, and reviewer are not identified. Fatigue and dynamic loading are outside the model. No release approval or formal conformity assessment is recorded. Rosa must correct the note without claiming the design is either safe or unsafe from the ratio alone.',
    cast='Rosa | Design engineer\nMalik | Assurance lead',
    culture=('Ask what compliant refers to', 'Compliance is a relationship to specific applicable requirements, not a general compliment about design quality. Ask for the requirement, version, evidence, limitations, and authorized decision. A numerical margin may be useful evidence, but its meaning depends on the model and the failure modes considered.'),
    a='''What does 2.0 describe in the note? | A preliminary static-model ratio under its stated convention | Complete product conformity | A demonstrated fatigue life | An authorized release decision | The ratio belongs to the preliminary static model and does not establish the broader claims.
Which behavior is outside the model's assessment? | Fatigue and dynamic-loading effects | Every possible static input | The model's stated capacity-to-demand convention | The numerical result of 2.0 | The briefing explicitly places fatigue and dynamic loading outside the model.
What is missing from the compliance claim? | The applicable requirement and acceptance threshold | A preliminary ratio of 2.0 | A statement that the model is static | A statement that release approval is absent | A compliance conclusion needs an identified basis, which the note currently does not provide.''',
    vocabulary='''factor of safety | A defined ratio comparing capacity and demand on a stated basis. | state the factor of safety
allowable | A permitted value established by the applicable design basis. | identify the allowable
design load | A load case specified for design assessment. | define the design load
load case | A defined combination of actions considered in an analysis. | assess the load case
static analysis | Analysis of conditions treated without significant time-dependent dynamics. | review static analysis
dynamic loading | Loading whose time variation requires dynamic effects to be considered. | assess dynamic loading
fatigue | Progressive damage associated with repeated loading. | evaluate fatigue
ultimate capacity | Capacity associated with a defined ultimate failure limit. | state ultimate capacity
yield limit | A boundary associated with the onset of specified permanent deformation. | identify the yield limit
buckling | Instability involving a change in structural form under loading. | assess buckling
failure criterion | The condition used to define failure in an analysis. | specify the failure criterion
load combination | A defined set of loads considered together. | document the load combination
model validity | The degree to which a model is suitable for its intended assessment. | assess model validity
analysis limitation | A condition or behavior not adequately addressed by an analysis. | state analysis limitations
applicable requirement | A requirement that governs the specific product or situation. | identify applicable requirements
compliance matrix | A record linking requirements to evidence and status. | maintain a compliance matrix
conformity assessment | Evaluation of whether specified requirements are fulfilled. | identify the conformity assessment route
normative reference | A referenced document needed to apply a specification's requirements. | check normative references
standard edition | The identified version of a published standard. | confirm the standard edition
evidence package | The records supporting a technical or compliance conclusion. | assemble the evidence package
independent review | Review by a suitably separate qualified reviewer. | arrange independent review
authorized sign-off | Recorded approval by a person with the relevant authority. | obtain authorized sign-off
deviation approval | Authorized acceptance of a defined departure where permitted. | record deviation approval
release restriction | A stated limit on what may proceed under a decision. | communicate release restrictions''',
    precision='A factor of safety is meaningful only with its stated convention, failure criterion, inputs, and load cases. A value of 2.0 in one preliminary static model is not a universal safety threshold and cannot establish fatigue performance or complete conformity.',
    precision_extra='Requirements may come from law, contracts, standards, and internal specifications, with different authority and scope. Identify what actually applies. Neither a missing compliance record nor a favorable ratio alone justifies declaring the product categorically safe or unsafe.',
    phrases='''Ask for the basis | Compliant with which applicable requirement?
Identify the version | Which standard edition does the assessment use?
Name the convention | The reported factor uses the stated capacity-to-demand ratio.
Limit the result | This is a preliminary static-model result.
Ask for the criterion | Which failure criterion and acceptance threshold apply?
Expose excluded behavior | Fatigue and dynamic loading are outside this model.
Avoid a universal rule | A factor of 2.0 is not a universal acceptance threshold.
Separate analysis from approval | A calculated result is not authorized sign-off.
Request traceability | Link each requirement to its supporting evidence.
Check model scope | Does the model represent the load cases being claimed?
Keep status precise | The compliance conclusion is not yet established.
Avoid unsupported alarm | The missing record does not itself prove physical failure.
Ask about review | Who is qualified and authorized to review this assessment?
Clarify a departure | Any permitted deviation needs the required approval.
Preserve restrictions | State what cannot proceed while the item remains open.
Close the note | Report the result, limits, missing basis, and pending decision.''',
    notes='''Safe | A broad claim that cannot rest on one unexplained ratio.
Compliant | Requires an identified applicable requirement and evidence.
Factor | Specify the ratio convention and relevant failure criterion.
Preliminary | Signals a maturity limit, not a release authorization.
Outside scope | Makes excluded behavior visible to the reader.
Signed | Verify the signer's authority and the exact decision covered.''',
    d='''Which replacement note is justified? | The preliminary static model reports 2.0; applicable acceptance requirements and review remain unresolved. | The product is fully compliant because 2.0 exceeds one. | The product is proven unsafe because no reviewer is listed. | Fatigue is acceptable because the static result is favorable. | The replacement preserves the numerical result and clearly identifies the missing decision basis.
Why is the applicable requirement necessary? | It establishes what must be assessed and the acceptance basis. | It changes every preliminary result into automatic approval. | It removes the need to identify model limitations. | It guarantees that all standards use the same factor convention. | Without the governing requirement, the ratio cannot be judged against the correct acceptance conditions.
The static factor is 2.0 and fatigue is outside the model. Which conclusion is justified? | Fatigue performance is not established by this model; it needs an appropriate assessment basis. | Fatigue life is doubled because the factor is two. | Fatigue has failed because the report omits it. | Fatigue can be ignored once the static factor exceeds one. | A static capacity-to-demand ratio is not a fatigue-life result. An excluded behavior is unassessed here, not automatically passed, failed, or irrelevant.
What should a compliance matrix connect? | Applicable requirements, evidence, and assessment status | Only the project team's preferred conclusion | Every possible standard regardless of relevance | A release signature with no stated scope | The matrix supports traceability between the actual requirements, supporting records, and current conclusions.''',
    dialogue='''Rosa | The note says compliant, and the preliminary analysis reports a factor of two. Before I circulate it, I want to check whether that label is justified.
Malik | Start with the [[applicable requirement::The applicable requirement defines the governing obligation and acceptance basis missing from the current note.]]. Compliant with what, and on which acceptance basis? A favorable number does not identify the requirement or the scope of the conclusion.
Rosa | The model uses its stated capacity-to-demand convention. It is a static assessment, but the note does not identify the required threshold or who reviewed the result.
Malik | Then describe the [[factor of safety::The factor of safety is a defined ratio in this model, not a universal measure proving complete product safety.]] on that limited basis. Two is the reported preliminary value, not a universal rule that establishes compliance for every design.
Rosa | I will name the failure condition beside the ratio. Which inputs and assumptions must the reviewer see to understand what this particular calculation covers?
Malik | Exactly. Name the [[failure criterion::The failure criterion defines the condition against which capacity and demand are assessed.]] and the relevant inputs. A ratio without that context can sound precise while leaving its actual technical meaning unclear.
Rosa | Fatigue and dynamic loading were excluded. I will state that directly instead of allowing the static result to stand in for those separate questions.
Malik | Those are important [[analysis limitations::Analysis limitations identify excluded behaviors, including fatigue and dynamic loading, that the reported model cannot establish.]]. The reader needs them beside the result, especially if the note might be used to support a broader design or release decision.
Rosa | Could I say the static result is encouraging, provided I avoid saying it proves the product safe? I do not want to hide useful work either.
Malik | Report the result, but keep [[model validity::Model validity concerns whether the model is appropriate for the claimed assessment, beyond simply producing a numerical output.]] and review status explicit. The model must be suitable for the claim, and the acceptance basis still needs to be identified.
Rosa | I will check the contract requirements too. Can we identify the applicable documents and versions before the note lists standards that may not govern this product?
Malik | Yes, including the relevant [[standard edition::The standard edition identifies the specific version whose requirements are being applied, rather than assuming all versions are interchangeable.]] where a standard applies. Do not list an impressive collection of references without establishing their relevance and authority.
Rosa | I can organize the record so each applicable requirement points to the analysis or test evidence and shows whether assessment is complete, open, or awaiting review.
Malik | That is the purpose of a [[compliance matrix::A compliance matrix connects each applicable requirement with evidence and its assessment status.]]. It should expose the missing links rather than turn a single favorable calculation into a blanket green status.
Rosa | We also have no formal conformity assessment recorded. I should not write as though assembling the internal note has completed whatever external or internal route applies.
Malik | Correct. The [[conformity assessment::Conformity assessment evaluates specified requirements through the applicable route; writing an internal note does not establish its completion.]] route needs confirmation for this product and jurisdiction. This discussion cannot replace the responsible specialists or the required process.
Rosa | Then the revised note can preserve the factor of two, identify the model exclusions, and say that the compliance conclusion remains unestablished pending the required review.
Malik | Also distinguish that from [[authorized sign-off::Authorized sign-off is an actual approval by the relevant authority, which is not supplied by the preliminary calculation.]]. No release approval is recorded, and a technical result must not silently become permission to proceed.
Rosa | I will keep the current restrictions visible and identify who will confirm the requirements and review the evidence. I will not call the design either safe or unsafe from this ratio alone.
Malik | Good. The [[evidence package::The evidence package must support the exact claim through identified requirements, suitable analyses, limitations, and review records.]] should let a qualified decision maker see what is supported and what is missing. That is more useful than an unsupported compliance label.''',
    transfer_title='Keep the model inside its scope',
    transfer_setup='A preliminary static report gives a factor of 1.8 under its stated convention. It excludes fatigue, has no identified acceptance threshold, and has not received release approval.',
    transfer='''Engineer: "The reported value belongs to the ___ model." | static | The briefing identifies the report as a preliminary static assessment.
Reviewer: "The model excludes ___." | fatigue | Fatigue is explicitly outside the scope of the supplied model.
Engineer: "The acceptance threshold remains ___." | unidentified | No applicable acceptance threshold is supplied in the briefing.
Reviewer: "Release approval has not been ___." | granted | The briefing states that the report has not received release approval.''',
    rehearsal=["Read the assurance discussion. Keep the reported 2.0 factor within its preliminary static-model basis.","Switch roles. Name the unidentified requirement and excluded fatigue and dynamic effects without declaring universal safety or failure.","Complete and check the transfer. Read the 1.8 factor, missing threshold, and absent release approval as separate facts."]))


BOOK['units'].append(unit(
    title='Field Issues and Customer Communication',
    scene='Correct the cause without losing the customer',
    skill='Correct an unsupported causal statement, acknowledge customer impact, and give a useful next update without promising an unconfirmed resolution.',
    brief='A customer reports two output interruptions from field unit L18. Service engineer Marco previously emailed that humidity caused the interruptions, although humidity remains only a hypothesis and no root cause is confirmed. Customer engineer Nia requests a correction and a resolution date. The investigation is open; records are being gathered, no repair or operating change is authorized, and Marco can commit only to an update by 10 a.m. on October 2. The cases are fictional and supply no instruction to continue operating the unit.',
    cast='Nia | Customer engineer\nMarco | Service engineer',
    culture=('Correct the record explicitly', 'A quiet change of wording may leave the customer relying on the earlier claim. Identify what was overstated, give the corrected status, and acknowledge the practical effect of uncertainty. A promised update is valuable when it specifies what will be reported, even if resolution timing remains unknown.'),
    a='''What needs correction? | Humidity was stated as a confirmed cause without confirmation. | The customer reported only one interruption. | A repair was authorized but not recorded. | The investigation was completed before the email. | The earlier email converted an unconfirmed humidity hypothesis into a causal finding.
What can Marco commit to? | An update by 10 a.m. on October 2 | A completed repair by 10 a.m. on October 2 | A confirmed cause before any record review | Unrestricted continued operation | The only supplied commitment is the next update, not resolution or operating authorization.
Which statement preserves the customer's report? | Unit L18 has two reported output interruptions. | Every unit has a humidity defect. | L18 is known to be unaffected. | The interruptions did not occur because the cause is unknown. | The two reported events remain relevant even though their cause is unresolved.''',
    vocabulary='''field report | Information about product behavior in actual use. | assess a field report
customer impact | The effect of an issue on the customer's work or results. | acknowledge customer impact
reported symptom | Behavior described by a user but not necessarily independently verified. | record the reported symptom
confirmed finding | A conclusion supported by the completed relevant checks. | separate confirmed findings
working hypothesis | A provisional explanation guiding investigation. | qualify the working hypothesis
causal statement | Wording that says one condition produced another. | correct a causal statement
correction notice | A message explicitly amending earlier information. | issue a correction notice
case reference | An identifier connecting records for the same issue. | use the case reference
unit serial number | A unique identifier for an individual product unit. | confirm the unit serial number
installed configuration | The hardware, software, and settings present in the field. | document the installed configuration
operating history | Records of how and when a unit has been used. | request operating history
evidence request | A specific request for information needed in an investigation. | make an evidence request
traceable record | A record connected to its source, time, and relevant item. | retain a traceable record
return authorization | Permission and arrangements for returning an item. | confirm return authorization
chain of custody | A record of possession and transfer of evidence or an item. | maintain chain of custody
service instruction | An authorized direction for servicing or handling a product. | follow the service instruction
field action | A coordinated response affecting products in use. | assess a field action
impact statement | A bounded description of an issue's effects. | prepare an impact statement
interim update | A progress report before the final outcome is available. | provide an interim update
resolution commitment | A promise about when or how an issue will be resolved. | avoid an unsupported resolution commitment
update cadence | The agreed frequency or timing of progress communication. | agree an update cadence
escalation contact | The named route for raising concerns requiring further attention. | identify the escalation contact
case owner | The person responsible for coordinating a case. | name the case owner
closure confirmation | A recorded check that the case's closure conditions are met. | obtain closure confirmation''',
    precision='Reported interruptions are not erased by uncertainty about cause. The error is the email saying humidity caused them. The correction should explicitly withdraw that unsupported conclusion while preserving humidity as a hypothesis and the customer report as relevant evidence.',
    precision_extra='An update commitment is not a repair deadline. State what the update will contain, even if the investigation remains open. Do not improvise operating or repair instructions; any such direction must come through the authorized process for the actual product and risk.',
    phrases='''Acknowledge the correction | Our earlier email overstated the cause.
Withdraw the unsupported claim | Humidity has not been confirmed as the cause.
Preserve the hypothesis | It remains one explanation under investigation.
Recognize the report | We have recorded two interruptions on unit L18.
Acknowledge the impact | I understand that the uncertainty affects your planning.
Ask for specific records | Please connect each event to its time and installed configuration.
Avoid false reassurance | We do not yet have evidence to rule out recurrence.
Separate the commitments | I can commit to an update, not a resolution date.
State the next contact | I will update you by 10 a.m. on October 2.
Define update contents | The update will distinguish findings, open questions, and next steps.
Keep authority clear | No repair or operating change is authorized by this message.
Route service decisions | Product-specific instructions must come through the authorized service process.
Connect the correction | Attach this correction to the same case record.
Name ownership | I remain the case owner for communication.
Avoid premature closure | Sending the correction does not close the investigation.
Close the loop | Please confirm that the corrected status reached the relevant team.''',
    notes='''Reported | Attributes a statement without dismissing it.
Caused | Requires stronger evidence than a plausible association.
Correction | Explicitly identifies the earlier information that changed.
Update | A communication milestone, not necessarily a technical resolution.
No evidence yet | Does not mean proof of absence.
Closed | Needs the case's actual closure conditions to be satisfied.''',
    d='''Which opening best corrects the earlier message? | Our email overstated the cause; humidity remains unconfirmed. | As previously confirmed, humidity is probably responsible. | We have slightly refined our wording but the conclusion is unchanged. | The customer report is withdrawn because we lack a cause. | The opening explicitly corrects the unsupported certainty without discarding the reported events.
Which deadline statement is supported? | I will send an investigation update by 10 a.m. on October 2. | The unit will be repaired by 10 a.m. on October 2. | We guarantee no further interruptions before October 2. | The investigation must be closed before the next message. | Only the communication deadline is authorized by the supplied facts.
Which request could help distinguish causes without presuming humidity is responsible? | Provide event times, installed configuration, and available environmental records linked to L18. | Confirm that each interruption was humidity-related before sending the original logs. | Remove events that occurred during apparently normal humidity. | Supply only a summary supporting the first email's conclusion. | Traceable observations let investigators test competing explanations. Filtering or labeling the evidence to fit the prior claim would prejudge the investigation.
What should the correction not imply? | Permission to change operation or perform an unapproved repair | That the earlier causal claim was too strong | That the cause remains unresolved | That the investigation is still open | The briefing gives no authorized operating or repair change, so the message must not create one.''',
    dialogue='''Nia | Your email said humidity caused the two interruptions on L18. Our team now understands that the cause has not been confirmed, so we need the record corrected.
Marco | You are right. The earlier [[causal statement::The causal statement claimed humidity produced the interruptions, which the available investigation has not established.]] was too strong. Humidity is unconfirmed, and I will explicitly correct the message rather than quietly change the wording in our next update.
Nia | Please keep the two interruptions in the record. Uncertainty about the explanation does not change what our operators reported or the disruption they experienced.
Marco | We will preserve the [[field report::The field report records the customer's two interruptions and remains relevant while the cause is unresolved.]]. The correction concerns our explanation, not whether your team raised the events. Both reports remain part of the investigation for this unit.
Nia | Should our internal summary remove humidity entirely? I want it to be accurate without hiding an explanation that your engineers are still examining.
Marco | Describe it as a [[working hypothesis::A working hypothesis remains under investigation without being presented as a supported causal finding.]]. It is one explanation being investigated, not a confirmed finding and not something we have ruled out through completed checks.
Nia | Please identify the earlier email in the correction. People are still forwarding it, so they need an explicit statement that the cause has not been confirmed.
Marco | I will issue a [[correction notice::A correction notice explicitly amends the earlier claim so recipients do not continue relying on its unsupported certainty.]] on the same case. It will say that our previous message overstated the cause and that the investigation remains open.
Nia | We can supply the event times and the installed version information. Tell us how to connect those records so the engineers can distinguish the two occurrences.
Marco | Each [[traceable record::A traceable record connects evidence to its source, event time, unit, and configuration rather than leaving context ambiguous.]] should identify L18, the event time, and the installed configuration. We will coordinate the evidence request through the case rather than ask you to guess which material matters.
Nia | Planning needs a date. What can you commit to now, and what is still preventing a resolution estimate?
Marco | I cannot give a [[resolution commitment::A resolution commitment promises an outcome or timing that remains unsupported while the cause and repair are unresolved.]] yet. I can commit to an update by ten a.m. on October second, and I understand that uncertainty creates a planning burden for you.
Nia | What will that update contain if the cause is still open? Saying we are working on it would give us little new information.
Marco | The [[interim update::An interim update reports progress before final resolution and should distinguish findings, uncertainties, and next steps.]] will separate confirmed findings, open hypotheses, outstanding evidence, and the next review point. It will not turn the communication deadline into a promised repair date.
Nia | One colleague asked whether the correction means we should change how the unit is used or attempt a repair. We have not received an authorized instruction.
Marco | This message is not a [[service instruction::A service instruction must come through the authorized product-specific process; the correction does not authorize operating or repair changes.]]. Any operating or repair direction must come through the authorized product-specific process. I will route that question to the responsible team rather than improvise an answer.
Nia | Please clarify ownership. We have heard from several people, and we need to know who will collect the questions and respond.
Marco | I will remain the [[case owner::The case owner coordinates the investigation communication and follow-up so the customer has a clear responsible contact.]] for communication. Your questions will stay linked to the same record, and I will identify the appropriate escalation contact if additional attention is needed.
Nia | That gives us a usable correction and a clear next contact. I will circulate the amended status, but I will not mark the technical issue resolved.
Marco | Correct. [[Closure confirmation::Closure confirmation requires the actual case conditions to be satisfied; correcting an email alone does not resolve the underlying issue.]] comes only when the relevant conditions are met. Today's correction restores an accurate record while the investigation and technical decisions continue.''',
    transfer_title='An update is not a repair promise',
    transfer_setup='A supplier wrongly called contamination the confirmed cause. It is still a hypothesis. The investigation is open. The supplier promises a progress report Friday at noon, not a repair.',
    transfer='''Supplier: "Our earlier claim needs a ___." | correction | The earlier message presented an unconfirmed explanation as an established cause.
Customer: "Contamination remains a ___." | hypothesis | The briefing explicitly says contamination has not been confirmed as the cause.
Supplier: "Friday noon is the next ___." | update | The promised milestone is a progress report rather than a completed repair.
Customer: "The investigation remains ___." | open | Neither the cause nor the resolution has been established in the supplied facts.''',
    rehearsal=["Read the customer exchange. Explicitly correct the earlier humidity claim while retaining the two reported L18 interruptions.","Switch roles. Promise the October 2, 10 a.m. update without creating a repair deadline or operating instruction.","Complete and check the transfer. Withdraw confirmed contamination and retain a hypothesis, Friday-noon update, and open investigation."]))

BOOK['units'].append(unit(
    title='Systems Integration and Interface Control',
    scene='The same number, a different unit',
    skill='Explain an interface mismatch using configuration, units, and affected evidence while coordinating a controlled integration decision.',
    brief='Hardware lead Isabel and software lead Noah integrate a fictional measurement display with no control output. Approved interface document revision 1 defines each transmitted count as 1 mm. Hardware test build H2 instead sends hundredths of a millimeter: 100 counts means 1 mm. Existing software S1 still interprets 100 counts as 100 mm. Earlier tests used H1, S1, and revision 1. A revision-2 interface proposal is not approved, and the impact review and retest plan are incomplete. No production release is authorized.',
    cast='Isabel | Hardware lead\nNoah | Software lead',
    culture=('Compatibility includes meaning', 'Teams may use the same connector, packet length, and field name while interpreting a value differently. State the units and scaling explicitly. When an interface changes, connect the proposed contract, actual builds, affected tests, and approval route instead of assuming a successful connection proves compatibility.'),
    a='''What does 100 counts mean for H2? | 1 mm | 100 mm | 0.01 mm | 10,000 mm | H2 sends hundredths of a millimeter, so one hundred counts represent one millimeter.
What does S1 currently display for those 100 counts? | 100 mm | 1 mm | 0.01 mm | An explicitly supplied error code | S1 still applies revision 1's interpretation of one millimeter for each transmitted count.
Which configuration has the earlier test evidence? | H1 with S1 under revision 1 | H2 with an approved revision 2 | Every possible hardware and software pairing | H2 with a completed retest plan | The briefing identifies the earlier tests as H1, S1, and the approved revision-1 interface.''',
    vocabulary='''interface control document | A controlled definition of an interface, abbreviated ICD. | update the interface control document
interface contract | The agreed expectations for interaction between components. | define the interface contract
configuration baseline | The approved set of identified versions used as a reference. | establish the configuration baseline
hardware build | An identified version or assembly of hardware. | identify the hardware build
software version | An identified release or build of software. | record the software version
integration test | A test of components working together. | run an integration test
regression test | A check that changes have not broken previously working behavior. | define regression tests
unit scaling | The conversion between encoded values and physical units. | document unit scaling
payload | The data carried inside a message or transmission. | inspect the payload
data type | The defined representation and permitted operations for a value. | specify the data type
field width | The size allocated to a data field. | confirm the field width
byte order | The sequence used to store or transmit a multi-byte value. | specify byte order
message schema | The defined structure and meaning of a message. | version the message schema
backward compatibility | Ability to work with an earlier version under stated conditions. | assess backward compatibility
version negotiation | A process for identifying or agreeing compatible interface versions. | define version negotiation
configuration mismatch | A combination of versions that does not share the expected contract. | identify a configuration mismatch
change impact analysis | Assessment of the consequences of a proposed or actual change. | complete change impact analysis
affected test | A test whose relevance or expected result changes with the modification. | identify affected tests
test evidence reuse | Using earlier results where their continued applicability is justified. | justify test evidence reuse
conversion factor | A multiplier used to express a value on another unit basis. | apply the conversion factor
interface owner | The role responsible for maintaining the interface definition. | identify the interface owner
change approval | Authorization to make a defined controlled change. | obtain change approval
configuration record | A record identifying the versions and settings used. | preserve the configuration record
integration readiness | The state of having the agreed inputs and evidence needed to integrate. | assess integration readiness''',
    precision='The mismatch is semantic: the number has a different unit scale. For H2, 100 counts times 0.01 mm per count equals 1 mm. S1 applies 1 mm per count and displays 100 mm. A successful message transfer would not establish correct interpretation.',
    precision_extra='Earlier test evidence still describes H1 with S1 under revision 1. It does not automatically validate H2, but not every unrelated result must automatically be discarded. Reuse needs an impact-based justification and a recorded configuration.',
    phrases='''Identify the pairing | Which hardware build and software version are under test?
Name the contract | The approved interface is still revision 1.
State the change | H2 sends hundredths of a millimeter.
Show the consequence | One hundred counts means 1 mm for H2 but 100 mm for S1.
Separate connection from meaning | A received message can still be interpreted incorrectly.
Check the scale | What conversion factor does this version apply?
Preserve the old result | The earlier evidence applies to H1 with S1.
Avoid blanket reuse | That result does not automatically cover the new pairing.
Avoid blanket deletion | Unaffected evidence may be reusable with justification.
Identify the proposal | Revision 2 is not yet approved.
Bound the review | Assess decoding, display, records, and affected tests.
Name interface ownership | Who owns the shared interface definition?
Require a controlled decision | Route the proposed change through the approval process.
Plan the retest | Link each affected requirement to the appropriate test.
Record the exact configuration | Store the hardware, software, and interface versions with the result.
Close without overclaim | Integration and production release remain pending.''',
    notes='''Compatible | Includes shared meaning, not only physical connection.
Count | Has no useful physical meaning without the scaling definition.
Latest | An ambiguous version description in a technical record.
Passed before | Needs the exact configuration and test scope.
Reuse | Requires continued applicability, not convenience alone.
Approved change | Distinct from a test build or draft document already existing.''',
    d='''Which diagnosis matches the facts? | H2 and S1 use different scaling for the same transmitted count. | The customer has approved revision 2. | The interface is compatible because a number can be transmitted. | The earlier test proves S1 handles every scaling convention. | H2 encodes hundredths of a millimeter while S1 interprets whole millimeters.
For H2's 100-count message, which correction addresses the unit meaning? | Multiply 100 by 0.01 mm per count to obtain 1 mm; changing only the display label is insufficient. | Divide 100 by 0.01 to obtain 10,000 mm. | Keep the displayed value 100 and relabel it mm, because the packet arrived. | Multiply 100 by 100 to compensate for the smaller encoded unit. | Each count represents one hundredth of a millimeter. Multiplication by the encoded unit scale gives the intended physical value; a label change does not correct the number.
How should earlier evidence be treated? | Preserve it and assess which results remain applicable to the changed configuration. | Relabel all earlier results as H2 tests. | Delete all results without an impact review. | Declare the new interface approved because earlier tests passed. | Prior results remain valid records of the old configuration; reuse for the change needs justification.
What is needed before claiming integration readiness? | A resolved interface definition, controlled configuration, and appropriate reviewed test evidence | Only a message received without a connection error | Only the existence of a draft revision 2 | A statement that both teams prefer the new units | Readiness depends on a shared approved basis and evidence, not merely connectivity or preference.''',
    dialogue='''Noah | The message arrives without an error, but S1 displays one hundred millimeters. You expected one millimeter. Can we compare the transmitted count and its meaning?
Isabel | H2 sends one hundred, but its [[unit scaling::Unit scaling converts the encoded count into a physical quantity; H2 now uses hundredths of a millimeter.]] is now hundredths of a millimeter. The approved revision-one interface still defines whole millimeters per count.
Noah | Then S1 is applying its documented multiplier of one. The number was received, but this pairing interprets it one hundred times too large.
Isabel | Yes, we have a [[configuration mismatch::The configuration mismatch pairs hardware using the new scale with software expecting the old scale.]]. A successful packet transfer does not demonstrate agreement about physical units.
Noah | Our earlier test passed. Before anybody uses that result to clear H2, which actual builds and interface revision did the test cover?
Isabel | The [[configuration record::The configuration record identifies the exact H1, S1, and revision-one combination behind the earlier evidence.]] says H1, S1, revision one. Preserve that result as evidence for that combination; it was not a test of H2.
Noah | I found the revision-two proposal in the folder. Its presence does not mean the new scale is approved, even though the hardware test build already uses it.
Isabel | Correct. The [[interface control document::The interface control document is the controlled shared definition; a draft revision does not replace the approved one automatically.]] still needs controlled review and approval. A new test build cannot silently replace the shared definition for the software team.
Noah | For the proposed scale, should I divide one hundred by zero point zero one? That would produce ten thousand millimeters, which makes the mismatch worse.
Isabel | Multiply by the [[conversion factor::The conversion factor is 0.01 millimeters per count, converting H2's value of 100 into 1 millimeter.]] instead: zero point zero one millimeters per count. One hundred counts then gives one millimeter. Include that worked example in the proposal.
Noah | Could we just change the label beside the displayed number? The field name and packet size are unchanged, so the patch could look quite small.
Isabel | A label alone would leave the value wrong. The [[change impact analysis::Change impact analysis identifies which functions, records, requirements, and tests are affected by the scaling change.]] must follow decoding, display, stored records, and any other uses of the physical quantity.
Noah | Should I discard every earlier test, or can some results remain useful? I want to avoid both unsupported reuse and rerunning unrelated checks without a reason.
Isabel | Assess [[test evidence reuse::Test evidence reuse requires justified continued applicability; previous success cannot simply be transferred to the changed pairing.]] against the change. Keep applicable results with their original configuration references, and identify where changed behavior needs new evidence.
Noah | I will list affected requirements and expected values for the proposed pairing. The tests should catch both a wrong factor and a correct-looking number from the wrong configuration.
Isabel | Include [[regression tests::Regression tests check that the change has not broken previously working behavior in the defined affected scope.]] for previously working behavior within the assessed scope. A direct scaling check alone does not establish that the rest of the affected behavior is unchanged.
Noah | Who will maintain the shared definition? Separate hardware and software notes could leave us with this disagreement again at the next test.
Isabel | We need a named [[interface owner::The interface owner maintains the shared definition and coordinates controlled changes across the participating teams.]] and a confirmed approval route. I will bring the hardware-build details; please attach the software interpretation and affected-test list.
Noah | I will. Today's outcome is an understood scaling mismatch and assigned evidence preparation, not an approved new interface or production release.
Isabel | Agreed. Establishing [[integration readiness::Integration readiness requires the agreed configuration and supporting evidence, not merely understanding the source of a mismatch.]] still needs the controlled definition, compatible configuration, and reviewed evidence. We will not relabel the earlier pass as proof for H2.''',
    transfer_title='A count needs its conversion',
    transfer_setup='A proposed interface uses 0.1 mm per count. A test message contains 50 counts, so its intended distance is 5 mm. Old software uses 1 mm per count and displays 50 mm. The proposal is unapproved.',
    transfer='''Engineer: "The proposed distance is ___ mm." | 5 | Fifty counts multiplied by 0.1 millimeters per count equals five millimeters.
Reviewer: "The old software displays ___ mm." | 50 | The old interpretation uses one millimeter per count, producing fifty millimeters.
Engineer: "The difference comes from unit ___." | scaling | The same count is converted using two different physical-unit multipliers.
Reviewer: "The proposed change still needs ___." | approval | The briefing explicitly states that the new interface proposal is unapproved.''',
    rehearsal=["Read turns 1-10. Contrast H2's 100 counts as 1 mm with S1's 100 mm display; correct division to multiplication by 0.01.","Switch roles for turns 11-20. Keep evidence for H1/S1/revision 1 separate from the unapproved H2 proposal.","Complete and check the transfer. Contrast 5 mm intended with 50 mm displayed, then state that approval remains outstanding."]))
