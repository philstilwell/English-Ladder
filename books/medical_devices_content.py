"""Original medical-device development, quality, and training conversations."""
from books.authoring import unit

BOOK = dict(
    slug='medical-devices', title='Medical Devices English',
    cover_label='Design / evidence / quality / training',
    cover_title='Medical Devices', cover_size=34,
    tagline='Specify the need. Explain the evidence. Keep the boundary clear.',
    audience='For medical-device design, quality, regulatory, manufacturing, and clinical-training professionals.',
    map_intro='Eight conversations across device development, postmarket information, and responsible product communication.',
    notes_title='A precise sentence protects the decision.',
    notes_intro='Device teams work across engineering, clinical, commercial, and regulatory perspectives. The same word can mean different things in different meetings: tested is not the same as validated, a complaint is not a confirmed cause, and a proposed pathway is not an authorization. These cases give you the language to make those distinctions without losing the practical next step.',
    field_notes=[
        ('Put the user beside the requirement', 'Name who will use the device, for which task, and in what environment. A broad adjective such as intuitive cannot replace a reviewable requirement or evidence from the relevant users.', '"Which users and conditions does this requirement cover?"'),
        ('Say what the evidence establishes', 'Identify the object, method, criteria, and result of a test. A passed specification check and evidence about intended use answer related but different questions.', '"The output met this specification; the intended-user evaluation remains open."'),
        ('Separate an observation from its explanation', 'Describe the event before naming a cause. Missing information is a follow-up task, not permission to replace uncertainty with a reassuring conclusion.', '"The caller reported an interruption; the cause has not been established."'),
        ('State whose decision it is', 'Routing a question, proposing a change, and authorizing release are different acts. Use a named review route and a visible status instead of implying that discussion has settled an approval.', '"We can propose the change; the designated reviewer must assess it."')],
    scope_note='Original fictional language practice, not device operating instructions or medical, legal, quality-system, or regulatory advice. US regulatory examples are identified as such; other jurisdictions differ. Use the current labeling, applicable requirements, trained personnel, and your organization\'s controlled procedures. No scenario authorizes patient care or product release.',
    sources=[
        dict(title='US FDA. Quality Management System Regulation (QMSR).', url='https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr', note='Current US framework, effective 2 February 2026, incorporating ISO 13485:2016. Legacy quality-system terminology should not be mistaken for the current rule.', checked='10 October 2026'),
        dict(title='US FDA. Applying Human Factors and Usability Engineering to Medical Devices.', url='https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices', note='Background on intended users, environments, interfaces, and use-related risk. All study observations and proposed changes in this book are invented.', checked='10 October 2026'),
        dict(title='US FDA. Medical Device Safety and the 510(k) Clearance Process.', url='https://www.fda.gov/medical-devices/510k-clearances/medical-device-safety-and-510k-clearance-process', note='Background on pathway distinctions and the comparative 510(k) review standard. Fictional cases do not determine a device classification or submission route.', checked='10 October 2026'),
        dict(title='Electronic Code of Federal Regulations. 21 CFR 803.50.', url='https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.50', note='US manufacturer reporting provisions, including reasonably known and missing information. Apply all relevant provisions and specialist review, not a classroom deadline.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='User Needs and Design Inputs',
    scene='What does easy to use mean?',
    skill='Turn an ambiguous design discussion into a scoped request for users, conditions, and measurable criteria.',
    brief='Design engineer Mira and product lead Owen review a fictional monitoring-device brief. It says easy to use and suitable everywhere. The agreed initial audience is trained clinic staff, but an appended slide also mentions home caregivers. No home-use assessment is supplied. A proposed setup-time target of two minutes has not been reviewed or approved. Mira and Owen must distinguish the agreed scope, the proposed expansion, and the missing basis for a measurable design input.',
    cast='Mira | Design engineer\nOwen | Product lead',
    culture=('Clarify without dismissing the need', 'A customer adjective can be a useful starting point. Acknowledge the concern behind it, then request the user, task, conditions, and evaluation basis. This sounds more collaborative than rejecting the adjective as meaningless, while still preventing an unsupported requirement from becoming an accepted fact.'),
    a='''Who is the agreed initial audience? | Trained clinic staff | All home caregivers | Every possible user without training | Children using the device independently | The brief names trained clinic staff and treats home caregivers as an unassessed expansion.
What is the status of the two-minute target? | Proposed, not reviewed or approved | Approved and already verified | Required by a supplied regulation | Demonstrated in a home-use study | The scenario explicitly describes an unreviewed proposal rather than an established criterion.
What additional evidence question follows from adding home caregivers to the brief? | Whether the new users, training, tasks, and home conditions support the proposed use | Whether the existing clinic-user results have already established identical home performance | Whether mentioning home use automatically adds it to the approved baseline | Whether a numeric setup target alone removes the need to assess the new users | A new user group and setting can change how the device is used. Existing clinic scope and a proposed time target do not establish performance for home caregivers.''',
    vocabulary='''user need | A requirement expressed from the perspective of the intended user. | capture a user need
design input | A specified requirement that guides device design and development. | define a design input
design output | A result of design work that can be checked against inputs. | review a design output
intended user | The person or user group the device is designed for. | identify intended users
intended use | The purpose for which a device is intended. | define the intended use
use environment | The physical and social setting in which a device is used. | characterize the use environment
user profile | Relevant characteristics of a defined user group. | develop a user profile
task analysis | Examination of the actions and decisions needed to perform a task. | conduct a task analysis
use scenario | A description of users performing tasks under specified conditions. | map a use scenario
design constraint | A limit that the design must satisfy. | document a design constraint
acceptance criterion | A specified condition used to decide whether a requirement is met. | establish acceptance criteria
measurable requirement | A requirement expressed so its fulfillment can be evaluated. | formulate a measurable requirement
stakeholder | A person or group with a relevant interest in the product. | consult stakeholders
voice of the customer | Collected customer needs and expectations. | analyze the voice of the customer
requirements baseline | The agreed requirement set used as a reference for controlled work. | approve a requirements baseline
traceability | The ability to follow links between related records or requirements. | maintain requirements traceability
use limitation | A boundary on the conditions or purposes of use. | state a use limitation
ergonomics | Design attention to how people physically and cognitively interact with a product. | evaluate ergonomics
interface | The elements through which a user interacts with a device. | assess the user interface
workflow | The ordered activities through which work is completed. | observe the clinical workflow
design assumption | An unconfirmed premise influencing a design decision. | challenge a design assumption
scope expansion | An increase in the users, uses, or conditions covered by a project. | assess a scope expansion
change request | A documented proposal to alter an agreed item. | raise a change request
requirement owner | The person accountable for clarifying and maintaining a requirement. | assign a requirement owner''',
    precision='A proposed two-minute target is not an approved acceptance criterion. The team must identify what setup includes, who performs it, under which conditions, and why the target is appropriate before treating the number as a settled requirement.',
    precision_extra='Intended user, intended use, and use environment answer different questions. Trained clinic staff and home caregivers cannot be treated as interchangeable merely because the interface looks similar. A new audience may change the evidence needed.',
    phrases='''Acknowledge the need | Ease of use matters; we need to define the task behind that phrase.
Name the current audience | The agreed initial users are trained clinic staff.
Separate an expansion | Home caregivers are a proposed additional user group.
Ask about the setting | Which lighting, noise, and workflow conditions are in scope?
Clarify the task | What exactly counts as setup in this requirement?
Mark a proposal | Two minutes is a candidate target, not an approved criterion.
Ask for the basis | What evidence supports that time limit?
Keep needs visible | The requirement should address the user need rather than only our preferred feature.
Request traceability | Link this input to the need and the planned evaluation.
Challenge a broad claim | Suitable everywhere goes beyond the environments we have assessed.
Identify an assumption | We are assuming equivalent training, but that has not been established.
Define ownership | Who will resolve the user-profile question?
Request a review | The scope change needs review before it enters the baseline.
Distinguish output | A new screen layout is an output, not proof that the need is met.
Preserve status | Keep the home-use item marked proposed in the meeting record.
Close the handoff | We will return with the defined task, conditions, and criterion basis.''',
    notes='''Easy | An adjective that needs a defined task and evaluation basis.
Everywhere | A broad claim that can silently expand the intended environment.
Shall | Often marks a requirement; use it only with the document's agreed convention.
Proposed | Signals that a target or change is not yet approved.
Baseline | The controlled reference, not every idea discussed in a meeting.
Trace | Connect the need, requirement, output, and evidence rather than repeat a label.''',
    d='''Which revision preserves the current scope? | Design for trained clinic staff; assess home-caregiver use as a proposed expansion. | Design for all users because the interface is unchanged. | State home use is validated because it appears on a slide. | Delete every reference to users and retain easy to use. | The revision names the agreed audience and does not promote an unassessed expansion into fact.
Which statement accurately describes the time target? | Two minutes is proposed; task boundaries and the criterion basis need review. | Two minutes is approved because it is measurable. | A numeric target needs no justification. | The target proves suitability for home use. | A number can be measurable while still lacking scope, justification, and approval.
What best distinguishes a need from an output? | The need describes the user requirement; the screen layout is a design result. | The need and the layout are identical records. | Any output proves the need is satisfied. | A user need must specify a preferred screen color. | A design result can address a need but does not replace the need or evidence of fulfillment.
Which meeting record is most accurate? | Clinic scope agreed; home-use assessment and setup criterion remain open. | All environments approved and two-minute performance established. | Home use rejected permanently by this discussion. | Setup performance failed a completed validation study. | The supplied discussion leaves two items unresolved and provides neither approval nor a failure result.''',
    dialogue='''Owen | The customer summary says the device should be easy to use. I agree with that direction, but the design team says it cannot work from that sentence alone.
Mira | We can retain it as a [[user need::The user need preserves the concern before the team develops a more specific requirement.]]. We still need the task, the people performing it, and the conditions that make the task difficult.
Owen | The initial audience is trained clinic staff. The latest slide adds home caregivers because sales sees a possible opportunity, although that group has not been assessed.
Mira | Then mark that as a [[scope expansion::Adding an unassessed user group expands the project scope rather than confirming the current design's suitability.]]. It is not simply another way of describing the audience already agreed in the brief.
Owen | Could we write setup within two minutes? It sounds clearer than easy to use, and the number would give engineering something definite to work toward.
Mira | It is a candidate [[acceptance criterion::The time target could become a decision criterion, but its scope and basis require review first.]], not an approved one. We must define what setup includes and why two minutes is appropriate for those users.
Owen | That distinction matters. I do not want the meeting notes to turn a suggested number into a promise that the product has already been shown to meet.
Mira | We should also characterize the [[use environment::The use environment covers conditions such as lighting and noise that may affect the task.]]. Lighting, interruptions, noise, and access to other staff can affect the task even when the screen stays unchanged.
Owen | The sales slide says suitable everywhere. We have not gathered evidence from homes, so I will remove that claim from the current product description.
Mira | Good. The [[user profile::The user profile identifies relevant characteristics rather than assuming different audiences have equivalent capabilities or training.]] should describe relevant training and capabilities. We cannot assume that clinic staff and home caregivers approach the same instruction in the same way.
Owen | Engineering wants a simpler screen. Is that the requirement, or their proposed way to meet it? I want the brief to distinguish the two.
Mira | Treat the screen layout as a [[design output::A screen layout is a result of design work, not the underlying user requirement.]]. The input should express what must be achieved without presenting an untested layout as proof of success.
Owen | Then we need a record that connects the customer concern to a reviewable input and eventually to evidence. Otherwise the same question will return at every review.
Mira | That is [[traceability::Traceability links the need, requirement, design result, and supporting evidence across the development records.]]. Each link should make the reasoning visible, including which assumptions remain open and which version the team has agreed.
Owen | Who should resolve the setup definition? I can bring customer context, but I should not independently decide the engineering criterion or the relevant evaluation conditions.
Mira | Assign a [[requirement owner::The requirement owner coordinates clarification and maintenance of the requirement without replacing specialist review.]] to coordinate those contributions. The owner can bring the proposed wording and its basis back for the appropriate review.
Owen | I will separate the clinic requirement from the home-use proposal. The notes will say that the two-minute target remains unreviewed, with a named follow-up owner.
Mira | Keep both proposals outside the approved [[requirements baseline::The baseline is the agreed reference set, so unreviewed proposals must not silently become approved requirements.]] until the review is complete. Clear status now prevents later teams from treating a meeting idea as an established obligation.
Owen | I will keep easy to use as the customer concern and assign the setup-definition work. The home-use proposal and two-minute target remain open for review.
Mira | Exactly. A well-scoped [[design input::The design input translates a defined need into a specified requirement that can guide and be evaluated in development.]] will identify what the design must achieve. The evidence must then show whether the resulting device actually meets the relevant requirement.''',
    transfer_title='A new setting, an open requirement',
    transfer_setup='A brief covers trained outpatient staff. A slide proposes home use. A ninety-second task target is suggested but has not been approved.',
    transfer='''Lead: "The agreed setting is the outpatient ___." | clinic | The current brief covers outpatient staff rather than the proposed home setting.
Engineer: "Home use is a proposed ___." | expansion | The additional environment broadens the scope and has not been assessed.
Lead: "Ninety seconds is not yet an approved ___." | criterion | The proposed time has not completed the stated approval process.
Engineer: "Keep the proposal separate from the current ___." | baseline | The agreed requirements reference should not silently incorporate an unapproved proposal.''',
    rehearsal=["Read the design-input discussion. Preserve trained clinic staff as the agreed audience and home caregivers as a proposal.","Swap roles. State the two-minute target as unapproved; identify setup boundaries and the basis still needed.","Read the corrected ninety-second transfer. Keep the outpatient baseline distinct from the proposed home expansion."]))

 
BOOK['units'].append(unit(
    title='Risk Management and Hazard Analysis',
    scene='The hot surface is not the injury',
    skill='Separate a hazard, an exposure situation, possible harm, and the evidence for a risk-control claim.',
    brief='Risk engineer Elena and mechanical lead Sam review a fictional enclosure-heating concern. The worksheet labels skin burn as the hazard and says low risk because no complaints have been received. The team has identified a potentially hot accessible surface, possible prolonged contact, and possible skin injury. No likelihood estimate or verified control result is supplied. An insulating cover is only a proposal. Their task is to correct the chain of reasoning without deciding that the device is safe.',
    cast='Elena | Risk engineer\nSam | Mechanical lead',
    culture=('Challenge the chain, not the person', 'Risk meetings become more productive when colleagues identify the exact missing link. Ask whether a phrase names a source, an exposure, an outcome, or a control. A neutral classification question can reveal an important disagreement without turning the review into a personal argument.'),
    a='''Which item is the potential source of harm? | The accessible hot surface | The possible skin burn | The absence of complaints | The unapproved meeting minutes | The surface is the potential source, while the skin injury is a possible resulting harm.
What is the status of the insulating cover? | Proposed, with no verified control result supplied | Implemented and proven effective | Formally accepted as eliminating every risk | A confirmed cause of the original heating | The briefing gives a proposed control but no implementation or effectiveness evidence.
Why is low risk not established? | Neither a likelihood estimate nor a verified control result is supplied. | Every hot surface necessarily causes injury. | Any complaint-free device is automatically safe. | Possible harm and likelihood are identical concepts. | The supplied information does not support a complete risk conclusion or an effective-control claim.''',
    vocabulary='''hazard | A potential source of injury or other harm. | identify a hazard
harm | Injury or damage to health, property, or the environment. | describe possible harm
hazardous situation | Circumstances in which people or other protected things are exposed to a hazard. | identify a hazardous situation
sequence of events | The linked events that can lead to exposure and harm. | map the sequence of events
severity | The degree of possible harm. | assess harm severity
probability of harm | The likelihood that the specified harm will occur. | estimate the probability of harm
risk | The combination of the probability of harm and its severity. | evaluate a risk
risk analysis | Systematic identification of hazards and estimation of associated risks. | document the risk analysis
risk evaluation | Comparing estimated risk with established acceptability criteria. | perform a risk evaluation
risk control | A measure intended to reduce risk. | implement a risk control
residual risk | Risk remaining after risk-control measures have been implemented. | evaluate residual risk
risk acceptability | Whether risk meets the applicable acceptance criteria. | document risk acceptability
protective measure | A safeguard intended to reduce exposure or its consequences. | assess a protective measure
inherent safety | Safety achieved through the design itself. | consider inherently safe design
information for safety | Warnings or instructions intended to support risk reduction. | review information for safety
benefit-risk analysis | Evaluation of relevant benefits against remaining risks. | document a benefit-risk analysis
risk management file | The organized records of risk-management activities and results. | maintain the risk management file
foreseeable misuse | Incorrect use that can reasonably be anticipated. | assess foreseeable misuse
normal condition | Operation without a fault being present. | assess normal conditions
fault condition | A state in which a component or function has failed. | examine fault conditions
control effectiveness | The demonstrated ability of a measure to reduce the identified risk. | verify control effectiveness
newly introduced risk | A risk created or changed by a design or control modification. | assess newly introduced risks
risk estimate | An assessment of harm probability and severity. | justify a risk estimate
objective evidence | Verifiable information supporting a conclusion. | obtain objective evidence''',
    precision='Hazard, hazardous situation, and harm are not interchangeable. In this case, the potentially hot surface is the source; prolonged contact describes exposure; a burn is the possible injury. These distinctions clarify the analysis without supplying a likelihood estimate.',
    precision_extra='No complaints received is not proof that the probability of harm is zero. A proposed cover is not yet an effective control. Assess implementation, effectiveness, and any risks introduced by the change through the applicable process.',
    phrases='''Identify the source | The accessible hot surface is the potential source of harm.
Name the exposure | Prolonged contact is the exposure situation we need to examine.
Describe the outcome | A skin burn is the possible harm, not the source.
Separate two dimensions | Severity and probability answer different questions.
Ask for the basis | What evidence supports this likelihood estimate?
Avoid false reassurance | No complaints received does not establish zero risk.
Mark a proposed control | The cover is a candidate protective measure.
Request evidence | We have not yet verified the control's effectiveness.
Check the chain | Which sequence could lead from this condition to injury?
Preserve uncertainty | The current record does not support the low-risk conclusion.
Assess the change | Could the proposed cover introduce another risk?
Clarify residual risk | We cannot describe post-control risk before assessing the implemented measure.
Name the criterion | Which acceptability criteria are being applied?
Keep the record linked | Connect the analysis, control, verification, and review decision.
Avoid a guarantee | This review does not establish that every risk has been eliminated.
Close with ownership | Assign the missing evidence to an owner before the next review.''',
    notes='''Potential | Identifies a possibility, not proof that an injury occurred.
May lead to | Connects events conditionally without asserting inevitability.
Severity | Describes how serious the harm could be, not how often it occurs.
Residual | Refers to what remains after implemented controls, not a proposed future state.
No evidence | Must not be shortened into evidence of no risk.
Effective | Requires support tied to the specific control and risk.''',
    d='''Which chain is correctly labeled? | Hot surface: hazard; prolonged contact: exposure situation; burn: harm. | Burn: hazard; hot surface: harm; no complaints: control. | Prolonged contact: proof of injury; burn: probability. | Cover proposal: verified control; burn: acceptance criterion. | The chain distinguishes the potential source, the exposure circumstances, and the possible injury.
Which sentence accurately reports the complaint history? | No complaints have been received; this alone does not establish the likelihood of harm. | No complaints prove that contact cannot occur. | No complaints prove that the cover works. | No complaints make severity irrelevant. | Complaint absence alone cannot supply the missing probability or control-effectiveness evidence.
Which review would support a control claim for the proposed insulating cover? | Its implementation, effect on contact risk, and any risk introduced by the change | Its presence in the drawing, with effectiveness inferred from its protective name | Its proposed geometry, with residual risk accepted before implementation | Its supplier description, with complaint absence substituted for control testing | A proposed safeguard needs evidence that it is implemented and effective, plus assessment of consequences elsewhere in the design. A drawing, name, or complaint count alone cannot establish that.
Which conclusion fits the case? | Further evidence is needed before the stated risk conclusion is supported. | The device is proven safe for every use. | A burn certainly occurred in every unit. | The cover has already eliminated the hazard. | The case supplies neither a completed risk evaluation nor a verified control result.''',
    dialogue='''Sam | The worksheet calls the skin burn a hazard and rates the issue low because we have no complaints. Can we close it with the proposed insulating cover?
Elena | Not from this record. The accessible hot surface is the [[hazard::The surface is the potential source of harm, whereas a burn is the resulting injury.]]. A skin burn describes a possible outcome, and the cover has not been evaluated.
Sam | I see the labeling problem. The surface could be accessible during use, and the scenario includes prolonged contact. We should keep those details in separate fields.
Elena | Yes. That contact describes a [[hazardous situation::Prolonged contact describes circumstances of exposure to the hot surface rather than the injury itself.]]. It helps us explain how someone could be exposed instead of jumping directly from a component to an injury.
Sam | Then the burn belongs in the outcome field. We have not established that it happened, so the wording must not imply an observed patient event.
Elena | Correct. It is possible [[harm::Harm identifies the possible injury, not evidence that an injury has actually occurred.]]. State the outcome conditionally and preserve the distinction between this design concern and a documented incident.
Sam | The team chose low because the complaint log is empty. That seems reassuring, but I cannot find any estimate showing how the exposure might occur.
Elena | We still need a justified [[probability of harm::The missing likelihood assessment cannot be replaced by an empty complaint log.]]. An empty log does not establish zero occurrence, especially without understanding exposure, reporting, and the underlying evidence.
Sam | Should we remove the severity entry as well? It seems difficult to judge the risk while the likelihood information remains incomplete in this version.
Elena | Keep [[severity::Severity concerns the degree of possible injury and remains distinct from the probability assessment.]] separate from likelihood. We need to describe the possible injury carefully; uncertainty in one dimension does not make the other dimension disappear.
Sam | The cover remains attractive as an engineering proposal. I want to record it without giving the impression that it has already solved the issue.
Elena | Call it a proposed [[risk control::The cover is a proposed risk-reduction measure, not yet a demonstrated solution.]]. Identify what it is intended to change, the evidence needed, and who will review whether that change is effective.
Sam | Could the cover trap heat somewhere else? I want the review to consider that possibility as well as reducing contact with the hot surface.
Elena | Exactly. Assess any [[newly introduced risk::A design modification can create or change other risks, which must be considered alongside its intended benefit.]]. A measure can address one exposure while affecting another part of the design, so its consequences need a broader review.
Sam | The draft already says residual risk acceptable. That sounds premature when the proposed measure has not been implemented or assessed against the relevant criteria.
Elena | It is premature. [[Residual risk::Residual risk is assessed after implemented controls, not assumed from an untested proposal.]] refers to what remains after controls. We should not describe a future condition as though its implementation and effectiveness were already established.
Sam | I will change the status to evidence incomplete and retain the proposed cover as an action for engineering review. We also need the criterion behind any acceptance decision.
Elena | Yes, document the applicable [[risk acceptability::Acceptability depends on the established criteria and supporting evaluation, not a reassuring adjective.]] criteria. The reviewer needs the reasoning and evidence, not simply a low label attached to an unfinished analysis.
Sam | I will separate the hot surface, prolonged contact, and possible burn in the record. Send me the evidence needed before we can judge the proposed cover.
Elena | That gives the next review useful [[objective evidence::Objective evidence is verifiable support for the eventual decision, which the current record must identify and obtain.]] to request and evaluate. We can make progress on the concern without converting a proposal into a completed safety conclusion.''',
    transfer_title='Proposal is not verification',
    transfer_setup='A fictional handle may have a sharp edge. Hand contact could cause a cut. A rounded redesign is proposed but has not been evaluated.',
    transfer='''Engineer: "The sharp edge is the potential ___." | hazard | The edge is the source that could cause the described injury.
Reviewer: "The cut is the possible ___." | harm | A cut describes the injury rather than the physical source.
Engineer: "The rounded redesign is a proposed ___." | control | The change is intended to reduce risk but has not been assessed.
Reviewer: "Its effectiveness still requires ___." | evidence | A proposed change cannot be treated as effective without supporting evaluation.''',
    rehearsal=["Read the risk review. Name the hot surface, prolonged contact, and possible burn as source, exposure, and harm.","Swap roles. Keep the cover proposed and its effect unverified; do not use complaint absence as a probability estimate.","Read the corrected sharp-edge transfer. Distinguish the redesign proposal from evidence of control effectiveness."]))

BOOK['units'].append(unit(
    title='Verification, Validation, and Design Review',
    scene='Twelve checks passed, one evaluation still open',
    skill='Report completed specification checks without implying that intended-use evaluation or release authorization is complete.',
    brief='Verification lead Arun and development manager Beth review the status of a fictional device. All twelve planned specification checks in the current package passed. The separate intended-user evaluation has not started. The slide nevertheless says validation complete and ready for release. No release authorization is supplied. A review meeting is scheduled tomorrow. Arun and Beth must present the completed evidence, the unperformed work, and the decision still required without treating the meeting itself as approval.',
    cast='Arun | Verification lead\nBeth | Development manager',
    culture=('Use complete with an object', 'A status update can be confident and narrow at the same time. Say which package is complete and which criterion it addresses. Replacing a global green status with separate evidence and decision lines helps colleagues see progress without confusing a finished test with a finished product.'),
    a='''What has passed? | Twelve planned specification checks in the current package | Every intended-user evaluation | The final release authorization | All future product configurations | The briefing limits the passed work to twelve specification checks in one package.
What has not started? | The separate intended-user evaluation | Every specification check | The project itself | The scheduled review meeting yesterday | The intended-user evaluation is explicitly unperformed in the supplied status.
What does tomorrow's meeting establish now? | Only that a review is scheduled | That release is authorized | That intended use has been validated | That all open actions are closed | Scheduling a review does not supply its conclusions or an authorization in advance.''',
    vocabulary='''verification | Confirmation with evidence that specified requirements have been fulfilled. | complete design verification
validation | Confirmation with evidence that requirements for an intended use are fulfilled. | plan design validation
design review | A systematic evaluation of design progress, evidence, and issues. | hold a design review
test protocol | A documented plan describing how a test will be performed and assessed. | approve a test protocol
test report | A record of test execution, results, and conclusions. | review a test report
test article | The item or configuration used in a test. | identify the test article
configuration | The defined arrangement and versions of a product's elements. | control the test configuration
requirement coverage | The extent to which requirements are addressed by specified evidence. | assess requirement coverage
traceability matrix | A structured table linking requirements to related evidence. | update the traceability matrix
test deviation | A departure from the planned test method or conditions. | assess a test deviation
unresolved anomaly | An observed irregularity whose significance or resolution remains open. | review unresolved anomalies
acceptance result | The recorded outcome against a specified acceptance criterion. | document the acceptance result
representativeness | How well an item or setting reflects the intended evaluated population or use. | justify representativeness
simulated use | Evaluation under conditions designed to represent actual use. | define simulated-use conditions
review action | A task assigned as a result of a review. | track review actions
action closure | Documented completion and acceptance of an assigned task. | verify action closure
release authorization | A formal decision permitting a product or version to be released. | obtain release authorization
design transfer | Translation of the design into production specifications and processes. | review design transfer
document control | Management of document versions, approval, and availability. | maintain document control
change impact | The consequences of a proposed or implemented alteration. | assess change impact
regression testing | Rechecking affected behavior after a change. | plan regression testing
evidence package | The organized records supporting a specific conclusion or decision. | assemble the evidence package
review quorum | The required participation for a particular review under its procedure. | confirm the review quorum
decision record | A documented conclusion, rationale, and associated conditions. | maintain a decision record''',
    precision='The twelve checks support the specified requirements they address, in the tested configuration. They do not automatically cover every user need, later version, or intended-use condition. Report completion at the level supported by the actual evidence.',
    precision_extra='A scheduled design review is not a completed decision. A review action is not closed merely because someone accepts ownership. Distinguish the test result, the remaining evaluation, the review conclusion, and the authorized release decision.',
    phrases='''State the completed work | All twelve checks in this specification package passed.
Limit the conclusion | That result applies to the tested configuration and covered requirements.
Name the open evaluation | The intended-user evaluation has not started.
Correct the status | Replace validation complete with specification checks complete.
Request the link | Which requirement does this result address?
Ask about deviations | Were any departures from the protocol assessed and documented?
Separate the decision | A passed test package is not release authorization.
Describe the meeting | The review is scheduled; its conclusion is not yet available.
Keep actions visible | Assign an owner and closure evidence for each open item.
Check the version | Confirm that the report covers the version presented for review.
Request the rationale | What supports the representativeness of this test article?
Assess a change | A later modification needs an impact assessment before relying on these results.
Avoid a global claim | We have not demonstrated every intended-use requirement.
Clarify the handoff | The review package should show completed evidence and unresolved work separately.
Record the conclusion | Capture the actual decision and any conditions after the review.
Close accurately | Ready for review does not mean ready for release.''',
    notes='''Complete | State exactly which task, package, or decision is complete.
Passed | Applies to specified criteria under stated test conditions.
Representative | Needs a basis; visual similarity alone is not enough.
Pending | Identifies unresolved work without implying failure or success.
Authorized | Describes a decision by the responsible authority, not general enthusiasm.
Covered | Means linked evidence exists for the named requirement, not for every possible claim.''',
    d='''Which slide heading is supported? | Twelve specification checks passed; intended-user evaluation not started. | Validation complete and product released. | All user needs proven by twelve engineering checks. | Review completed because tomorrow is booked. | The heading retains the actual passed work and the explicitly unperformed evaluation.
A software revision follows the tests. What wording is best? | Assess the change before assuming the earlier results cover the new version. | Earlier results automatically cover every future revision. | Any change makes all historical evidence false. | A new version number alone proves validation. | The impact of the change determines what previous evidence remains applicable and what further work is needed.
A reviewer accepts ownership of an open test deviation. Which status can be recorded at that point? | Owner assigned; required assessment, completion evidence, and acceptance still outstanding | Deviation accepted as harmless because a reviewer now owns it | Action closed because responsibility is no longer unassigned | Release approved because the deviation has entered the action log | Assignment establishes who will do the work, not its technical conclusion, completion, acceptance, or release effect. Those require their own evidence and decisions.
Which conclusion may Beth report before the review? | The evidence package is ready for the scheduled review, with the remaining work identified. | The review has approved release. | Intended-use validation succeeded without being performed. | No further decision is required. | The available facts support readiness for review but do not supply its outcome or release authorization.''',
    dialogue='''Beth | The dashboard says validation complete because all twelve checks passed. Before tomorrow's review, I want to be sure that headline means what the team thinks it means.
Arun | The completed work is [[verification::The specification checks confirm specified requirements, which is the verification claim supported by the case.]] against the specifications in this package. The separate intended-user evaluation has not started, so the headline combines two different claims.
Beth | The test result is still good progress. We should not hide it, but we should identify what those twelve checks actually cover and what remains unperformed.
Arun | Exactly. We cannot mark [[validation::Validation concerns requirements for intended use, and the separate intended-user evaluation is still unperformed.]] complete from these checks alone. The report should distinguish specification fulfillment from the evidence still needed about the intended use.
Beth | Can we say every requirement passed? That would be shorter, although I suspect the word every would extend the claim beyond this particular set of checks.
Arun | Show the [[requirement coverage::Coverage identifies the requirements actually addressed by the available evidence rather than implying universal completeness.]] instead. Each result needs a clear link to its requirement, and any uncovered requirements must remain visible in the review package.
Beth | I also noticed that the report refers to the earlier software build. The team discussed a revision, but I do not know whether it has been implemented.
Arun | We must confirm the [[configuration::The configuration identifies the versions and arrangement actually tested, limiting the scope of the result.]]. Evidence belongs to the item actually tested; a discussion about a later build cannot silently extend the report to that version.
Beth | If the revision goes ahead, which test conclusions might it affect? Please flag that question now so the release review does not inherit mismatched versions.
Arun | That calls for a [[change impact::A change-impact assessment examines whether a modification affects the relevance of existing evidence or requires more work.]] assessment. We should not assume that every old result becomes invalid, or that every result automatically remains sufficient.
Beth | The dashboard also says ready for release. I intended ready for tomorrow's meeting, but I can see that those are not interchangeable status descriptions.
Arun | Correct. [[Release authorization::Release authorization is a distinct formal decision and is not supplied by a test result or meeting invitation.]] is a separate decision. We have not been given that authorization, and scheduling a review does not establish its future outcome.
Beth | I will change the status to ready for review and put the unperformed intended-user evaluation beside the completed specification package. That should prevent a misleading green summary.
Arun | Include the [[evidence package::The evidence package organizes the actual records supporting the review rather than relying on a dashboard color.]], not just the totals. Reviewers need the reports, relevant versions, criteria, and any departures from the planned method.
Beth | There was one departure noted during execution. I do not want to describe it as a failed requirement if that is not what happened.
Arun | Call it a [[test deviation::A deviation is a departure from the planned test, whose significance must be assessed rather than assumed.]] and reference its assessment. The record should explain its significance and disposition without treating the label itself as a pass or failure.
Beth | Tomorrow, each unresolved item needs an owner. But the minutes should not show those items as closed simply because someone agrees to take responsibility.
Arun | Yes. [[Action closure::Closure requires the agreed completion evidence and acceptance, not merely assignment of responsibility.]] needs the required evidence and acceptance. Ownership makes follow-up possible; it does not demonstrate that the remaining task has already been completed.
Beth | I will separate the twelve passed checks from the unstarted user evaluation. Please confirm the tested build and keep release authorization off the slide until it exists.
Arun | After the meeting, add the actual [[decision record::The decision record captures the review's real conclusion and conditions after the review occurs.]] and its conditions. That keeps completed testing, open evaluation, review conclusions, and release status distinct throughout the handoff.''',
    transfer_title='A review date is not a decision',
    transfer_setup='Six specification checks passed on version B. The intended-use evaluation is pending, and a review is booked for Friday. No release decision has been made.',
    transfer='''Lead: "Six checks passed on version ___." | B | The evidence is explicitly tied to the supplied tested version.
Engineer: "The intended-use evaluation remains ___." | pending | The briefing gives no completed evaluation or successful result.
Lead: "Friday is the scheduled ___." | review | A booked meeting identifies a review date rather than a release decision.
Engineer: "Release has not been ___." | authorized | No release decision has been made in the supplied facts.''',
    rehearsal=["Read the review exchange. State twelve passed specification checks and the intended-user evaluation not started.","Swap roles. Distinguish the tested configuration, tomorrow's review, and the release decision still unmade.","Read the corrected version-B transfer. Friday remains a review date, not evidence that release is authorized."]))


BOOK['units'].append(unit(
    title='Usability and Human Factors',
    scene='Three participants read the label differently',
    skill='Report observed use difficulties neutrally and distinguish exploratory findings from validation or population-level rates.',
    brief='Human-factors specialist Laila and interface designer Victor review a formative study of a fictional device label. Three of eight participants selected the wrong status label during a simulated task. The draft summary calls them careless and concludes that a larger font will solve the problem. No revised label has been tested, and the study does not establish a population error rate. Laila and Victor must preserve the observation, investigate the interface, and describe the proposed revision without declaring success.',
    cast='Laila | Human-factors specialist\nVictor | Interface designer',
    culture=('Describe the interaction before judging it', 'Careless assigns a personal explanation that an observation may not support. Describe what participants saw, did, and said, then examine the task and interface. Neutral language can be more demanding than blame because it requires the team to specify evidence for its explanation.'),
    a='''What was observed? | Three of eight participants selected the wrong status label in the simulated task. | Every user failed in actual clinical use. | A larger font eliminated the difficulty. | A population-wide error rate was established. | The observation is limited to the stated participants, label, and simulated task.
Which wording adds a cause not established by the three wrong selections? | Participants selected incorrectly because they were careless. | Three participants selected the wrong status label in the task. | The proposed larger-font version has not been evaluated. | The reason for the selections remains under investigation. | The study records a behavior, not carelessness as its cause. Wrong selection does not by itself establish misreading, misunderstanding, inattention, or any single explanation.
What is the status of the larger font? | An untested proposed revision | A validated solution | An approved universal corrective action | Proof that no other interface issue exists | The revised label has not been tested, so its effect is not established.''',
    vocabulary='''human factors | Study and application of how people interact with systems and products. | apply human-factors principles
usability engineering | A structured approach to evaluating and improving user interaction. | conduct usability engineering
formative evaluation | An exploratory assessment used to inform design development. | run a formative evaluation
summative evaluation | An assessment of a sufficiently developed design against defined evaluation goals. | plan a summative evaluation
human-factors validation | Evaluation of intended users performing relevant tasks under representative conditions. | plan human-factors validation
critical task | A task whose error or omission could seriously harm a patient or user, including compromised care. | identify critical tasks
use error | An action or omission producing a result different from that intended or expected. | analyze a use error
close call | A situation in which a problem nearly occurs but is avoided. | document a close call
use difficulty | Observed trouble completing or understanding a task. | record a use difficulty
participant | A person taking part in a study. | recruit representative participants
moderator | The person guiding a study session under its protocol. | brief the moderator
prompting | Assistance that may influence a participant's performance. | document moderator prompting
task success | Completion of a defined task under stated evaluation criteria. | define task success
observation note | A factual record of behavior or events during a study. | write an observation note
root-cause analysis | Investigation of underlying contributors to an observed problem. | conduct root-cause analysis
mental model | A user's understanding of how a system works. | explore the user's mental model
affordance | A feature suggesting how an object or control can be used. | assess interface affordances
label comprehension | Understanding the meaning conveyed by a label. | evaluate label comprehension
visual hierarchy | The arrangement that makes some information more prominent than other information. | improve the visual hierarchy
legibility | How readily individual text or symbols can be distinguished. | assess label legibility
cognitive load | The mental effort needed to process information and perform a task. | reduce cognitive load
training decay | Loss of retained training knowledge or skill over time. | consider training decay
representative sample | A participant group suited to the intended study population and question. | justify the representative sample
design iteration | A revised version created through successive development cycles. | evaluate a design iteration''',
    precision='Three of eight is 37.5% of this study group, not an established error rate for the user population. Report the count and study context. A formative finding can identify a design concern without providing a final validation conclusion.',
    precision_extra='Legibility asks whether text can be distinguished; comprehension asks whether its meaning is understood. Increasing font size may affect one without resolving the other. A proposed revision needs evaluation rather than a sentence declaring it successful.',
    phrases='''Report the observation | Three of eight participants selected the wrong status label.
Preserve the context | This occurred in the simulated task used in the formative study.
Remove blame | The notes do not establish that the participants were careless.
Separate behavior from cause | The selection is observed; the reason still needs investigation.
Ask about wording | Did participants distinguish the meanings of the two labels?
Ask about visibility | Was the relevant text readily legible under the study conditions?
Check assistance | Record whether the moderator prompted the participant.
Bound the percentage | That percentage describes this study group, not the user population.
Mark the revision | A larger font is proposed but has not been evaluated.
Avoid a success claim | We cannot yet say the change resolves the problem.
Compare explanations | Font size, wording, and hierarchy are different possible contributors.
Keep evidence intact | Retain the observation notes when revising the summary.
Clarify task risk | Assess the task's safety significance through the appropriate process.
Name the evaluation stage | These formative findings inform development; they are not a completed validation claim.
Request a scoped follow-up | Evaluate the revised label against the specific difficulty observed.
Close the report | State the finding, the open explanation, and the next evaluation separately.''',
    notes='''Observed | Identifies what was recorded rather than why it happened.
Careless | Assigns blame that the evidence may not support.
Formative | Describes work intended to inform design development.
Resolves | Claims an outcome that needs evidence from the revised design.
Legible | Readable at the text or symbol level, not necessarily understood.
Representative | Depends on users, tasks, and conditions, not only participant count.''',
    d='''Which summary is most accurate? | Three of eight participants selected the wrong label in the formative simulated task. | The product has a proven 37.5% population error rate. | Three careless participants invalidate the study. | Larger text has already solved the issue. | The accurate summary preserves the observed count and the study's scope without adding a cause or outcome.
A participant can read both labels aloud but confuses their meanings. Which issue is most directly suggested? | Label comprehension | Inability to distinguish printed characters alone | Confirmed training decay in every user | Proven mechanical failure | Reading the characters while confusing their meaning points to comprehension rather than legibility alone.
How should assistance during a task be reported? | Document the prompting rather than presenting assisted success as unassisted performance. | Remove the assistance from the notes if the task was completed. | Treat any prompted completion as evidence that no difficulty existed. | Assume the moderator could not influence performance. | Prompting can affect the interpretation of performance and must remain visible in the record.
Which next-status sentence fits the facts? | The larger-font revision is proposed; its effect on the observed difficulty remains untested. | The revised label passed validation. | The study proves that only font size matters. | All intended users will now select correctly. | The supplied facts contain a proposal but no evaluation of that revised label.''',
    dialogue='''Victor | Three of the eight participants chose the wrong status label. The draft calls them careless. That is not something I can establish from watching the selection.
Laila | Then keep the [[observation note::An observation note records what participants did without supplying an unsupported explanation for their behavior.]] factual: which label, which task, and what happened. Remove the character judgment without losing the actual difficulty.
Victor | Would thirty-seven point five percent sound more precise in the headline? I worry the count looks small, even though the issue may matter.
Laila | Identify the [[formative evaluation::A formative evaluation informs design development and does not establish a population error rate or completed validation.]] and keep three of eight visible. The percentage describes these participants; it is not an estimated population error rate.
Victor | The team wants a larger font. That is easy to implement, but I cannot yet say that small characters caused all three wrong selections.
Laila | [[Legibility::Legibility concerns distinguishing text or symbols, which font size may affect without resolving meaning.]] is one question. We also need to examine whether the words distinguish the two states clearly in the task context.
Victor | One person read both labels aloud accurately and still selected the wrong status. Larger letters would not necessarily address that person's interpretation.
Laila | That observation concerns [[label comprehension::Reading text correctly while misunderstanding its meaning suggests a comprehension issue rather than only a visibility problem.]]. Keep it separate from a claim that the text could not be read, and do not assume every participant had the same problem.
Victor | Another person finished after the moderator asked a follow-up question. The results table currently says success, with no note about the intervention.
Laila | Record the [[prompting::Moderator prompting can influence performance and must remain visible when interpreting task completion.]]. We need to see how completion was achieved; assisted success should not silently become unassisted task performance.
Victor | What about placing the status higher on the screen? That changes where attention goes, rather than only changing the text size.
Laila | It is a [[visual hierarchy::Visual hierarchy concerns the relative prominence and arrangement of information, beyond the size of individual characters.]] proposal. We can evaluate it alongside wording, but neither idea is a demonstrated solution yet.
Victor | I will stop calling the larger font a fix. The revised label has not been tested, and we may need a different approach.
Laila | Call it a proposed [[design iteration::A design iteration is a revised version to evaluate, not evidence that the underlying problem is resolved.]]. Link it to the observed difficulty and keep the follow-up result open rather than writing success in advance.
Victor | The project lead also asks whether a wrong selection makes this a critical task. Three errors alone do not answer the safety question, do they?
Laila | No. Designating a [[critical task::Critical-task status depends on the potential harm of incorrect or omitted performance and requires the appropriate assessment.]] depends on potential consequences, including compromised care. The relevant risk assessment must address that, not just the number of selections.
Victor | Then I should not describe this as our final usability validation either. We used the session to find weaknesses while the interface was still developing.
Laila | Correct. Completed [[human-factors validation::The supplied exploratory study and untested revision do not establish completed human-factors validation.]] is not established by a formative session and an untested revision. State the evaluation stage and conditions clearly.
Victor | I will retain the three-of-eight count, the reading-versus-meaning observation, and the assisted completion. Proposed changes will sit in a separate section.
Laila | That gives the [[root-cause analysis::Root-cause analysis examines contributors to the observed difficulty rather than accepting an unsupported blame statement.]] useful evidence. We can investigate the difficulty without blaming participants or promising that one easy design change resolves it.''',
    transfer_title='Readable is not necessarily understood',
    transfer_setup='Two of ten participants read a label accurately but misunderstand its meaning in a formative session. Revised wording is proposed and has not been tested.',
    transfer='''Researcher: "Two of ten had difficulty with the label's ___." | meaning | The participants could read the text but misunderstood what it conveyed.
Designer: "This is an observation from a formative ___." | session | The supplied result comes from a developmental evaluation, not a population study.
Researcher: "The new wording remains ___." | untested | No evaluation of the proposed wording has been performed.
Designer: "We cannot yet claim the difficulty is ___." | resolved | A proposed revision does not demonstrate that the observed problem has been corrected.''',
    rehearsal=["Read the formative-study discussion. State three of eight wrong selections and distinguish behavior from an inferred cause.","Swap roles. Contrast readable text with understood meaning and assisted completion with unassisted performance.","Read the corrected two-of-ten transfer. Keep the revised wording untested and the comprehension issue unresolved."]))

BOOK['units'].append(unit(
    title='Regulatory Pathways and Submissions',
    scene='A route under review is not a clearance',
    skill='Distinguish a proposed US submission pathway, supporting evidence, and an actual regulatory decision.',
    brief='Regulatory specialist Inez and commercial director Caleb review a fictional US launch plan. The team is evaluating a possible 510(k) pathway and has identified a candidate predicate, but its suitability is still under review. No submission has been filed and no FDA decision exists. A sales slide says FDA approved and promises an October launch. Inez must correct both the status and the certainty of the timeline while preserving a clear planning discussion.',
    cast='Inez | Regulatory specialist\nCaleb | Commercial director',
    culture=('Correct status without inventing the opposite', 'An unsupported approval claim should be replaced with the actual status, not with a prediction that the device will fail. Separate the pathway assessment, evidence plan, submission, review, and decision. This gives commercial colleagues information they can use without a guarantee the team cannot make.'),
    a='''What is the current pathway status? | A possible 510(k) route is being evaluated. | FDA has granted a PMA approval. | A 510(k) clearance has been issued. | Every regulatory requirement has been waived. | The briefing identifies an ongoing pathway assessment, not a completed submission or decision.
What is known about the predicate? | A candidate has been identified, but suitability remains under review. | Its suitability has been conclusively accepted by FDA. | It automatically covers every proposed use. | No comparison is needed because the devices look similar. | The candidate's identification does not settle whether it supports the proposed pathway.
Why is the October launch promise unsupported? | No filing or regulatory decision exists, and the pathway assessment is incomplete. | All 510(k) reviews are legally guaranteed to fail. | The product has already been prohibited permanently. | October launches are never possible. | The case supplies unresolved dependencies rather than a guaranteed launch authorization or date.''',
    vocabulary='''regulatory pathway | The applicable route for obtaining a required regulatory decision. | assess the regulatory pathway
device classification | A regulatory category reflecting the device type and applicable controls. | confirm device classification
product code | A code used by FDA to identify a device type. | verify the product code
510(k) | A US premarket notification seeking a substantial-equivalence determination. | prepare a 510(k)
predicate device | A legally marketed comparator used in a 510(k) assessment. | assess a candidate predicate
substantial equivalence | The comparative regulatory determination central to a 510(k) decision. | support substantial equivalence
De Novo request | A US request for risk-based classification of a novel eligible device. | assess a De Novo request
premarket approval | The US PMA pathway requiring an independent safety-and-effectiveness demonstration. | prepare a premarket approval application
clearance | A favorable 510(k) determination permitting marketing within its scope. | obtain 510(k) clearance
approval | A formal favorable decision under an applicable approval pathway. | distinguish approval from clearance
indications for use | The specific purposes and population described for a device's use. | define indications for use
technological characteristics | Design and operating features relevant to a regulatory comparison. | compare technological characteristics
general controls | Baseline regulatory controls applicable to medical devices. | comply with general controls
special controls | Additional controls applicable to certain device types. | identify special controls
submission dossier | The organized documents and evidence submitted for regulatory review. | assemble a submission dossier
evidence plan | A plan for generating and organizing support for specified claims. | develop an evidence plan
regulatory strategy | A coordinated approach to regulatory requirements and decisions. | align the regulatory strategy
pre-submission interaction | A planned exchange with FDA before a later submission. | request a pre-submission interaction
review question | A request for clarification or evidence during review. | address a review question
deficiency | A shortcoming identified in the submitted information. | respond to a deficiency
response package | Documents addressing specified reviewer questions or deficiencies. | compile a response package
marketing authorization | The applicable permission to market a device within a defined scope. | confirm marketing authorization
regulatory dependency | An unresolved regulatory matter affecting another planned step. | identify a regulatory dependency
launch assumption | A planning premise underlying the proposed market-entry date. | qualify a launch assumption''',
    precision='For a US 510(k), clearance is the relevant decision term; it should not be casually called PMA approval. A candidate predicate, a pathway assessment, a submitted file, and an agency decision are four different statuses.',
    precision_extra='A proposed pathway does not determine the outcome or guarantee a date. The actual device, claims, classification, and evidence matter. These fictional facts do not establish eligibility for 510(k), De Novo, PMA, or an exemption.',
    phrases='''State the current stage | We are evaluating a possible 510(k) pathway.
Qualify the comparator | The predicate candidate remains under review.
Correct the decision claim | No FDA decision has been issued for this device.
Name the missing filing | The submission has not yet been filed.
Use the right term | A favorable 510(k) determination is clearance, not PMA approval.
Separate similarity from evidence | Similar appearance alone does not establish substantial equivalence.
Clarify the claim | The proposed indications must be consistent across the evidence and materials.
Bound the timeline | October is a planning assumption, not an authorized launch date.
Identify dependencies | The pathway assessment and evidence requirements remain unresolved.
Avoid predicting rejection | An open assessment does not mean the device has been rejected.
Request specialist review | Regulatory needs to assess the proposed use and comparison.
Describe an interaction | A pre-submission discussion is not a marketing authorization.
Align the slide | Replace FDA approved with the actual development status.
Keep decisions traceable | Use the exact decision and scope when an authorization exists.
Name the next deliverable | The next step is the pathway assessment, not a launch announcement.
Close the planning discussion | We can plan around dependencies without promising the agency's decision.''',
    notes='''Candidate | Identifies an option being assessed rather than an accepted comparator.
Filed | Reports submission, not a favorable review outcome.
Cleared | Use for an actual favorable 510(k) determination within its scope.
Approved | Do not use as a generic synonym for every regulatory interaction.
Expected | A forecast needs assumptions and should not sound like a guarantee.
Under review | Specify whether the review is internal or by the agency.''',
    d='''Which sales-slide correction matches the case? | Possible 510(k) pathway under internal assessment; no submission or FDA decision yet. | FDA approved because a predicate was found. | FDA clearance guaranteed by October. | PMA rejected because the team discussed 510(k). | The correction describes the actual internal stage without inventing approval, timing, or rejection.
Which statement about the candidate predicate is accurate? | Identification begins the assessment; suitability and the comparative evidence still need review. | Any similar-looking marketed product guarantees substantial equivalence. | A candidate predicate grants marketing permission. | A product code alone proves every proposed indication is supported. | A named candidate is not itself an accepted comparison or a regulatory decision.
Which October-launch note preserves the current regulatory status? | Internal planning target; pathway and predicate still under assessment, with no filing or decision | Expected FDA clearance date because the commercial team has approved the target | Confirmed market-entry date once the candidate predicate is listed in the slide | Agency review deadline beginning when the internal pathway discussion started | The date is internal and conditional. Neither internal approval, a candidate comparator, nor a pathway discussion starts or settles the required agency decision.
What does a pre-submission interaction establish by itself? | An opportunity for feedback, not marketing authorization | A final 510(k) clearance | A guaranteed review outcome | Permission for every proposed claim | A pre-submission exchange does not itself supply the later marketing decision.''',
    dialogue='''Caleb | The launch slide says FDA approved and shows October as the launch month. I need to understand whether those statements reflect an actual decision or our working plan.
Inez | Neither is an authorization. We are still assessing the [[regulatory pathway::The pathway is the route being evaluated, not an agency decision already obtained.]], including whether a 510(k) route is appropriate for the proposed device and its claims.
Caleb | The team found a marketed device that looks similar. I took that as confirmation that the route was settled, but the comparison may not be that simple.
Inez | It is a candidate [[predicate device::A candidate predicate is a comparator under assessment, not proof that the route or outcome is settled.]]. Its suitability remains under review; visual similarity alone does not establish the regulatory comparison needed for the proposed use.
Caleb | What should the commercial team understand about that comparison? I want the next discussion to focus on the evidence rather than repeat the same assumption.
Inez | The relevant determination is [[substantial equivalence::Substantial equivalence is the comparative regulatory determination sought through a 510(k), not a claim established by appearance.]]. The proposed use and technological characteristics matter, and the evidence must support the actual comparison rather than a convenient headline.
Caleb | Nothing has been filed, correct? Then under review is too vague; sales could read that as an FDA review already underway.
Inez | Exactly. The [[submission dossier::The dossier is the organized submission material, which has not yet been filed in this case.]] is not filed. Say internal pathway assessment, and keep that separate from any future agency review or decision.
Caleb | If the team eventually follows the 510(k) route successfully, should the slide say approved? That term is common in sales conversations, but I want it to be accurate.
Inez | Use [[clearance::Clearance is the appropriate favorable 510(k) decision term, distinct from PMA approval.]] for the actual favorable 510(k) determination. Do not borrow the language of a different pathway or imply a decision before one exists.
Caleb | Could a different route still be needed? I do not want the revised slide to make the 510(k) plan sound irrevocable while the assessment is incomplete.
Inez | Yes, keep the [[regulatory strategy::The strategy coordinates the applicable route and evidence; it remains subject to the unresolved assessment.]] provisional where appropriate. This discussion does not determine eligibility for another route, and we should not guess the outcome from limited facts.
Caleb | The product team also wants broader wording about who can use the device. That seems connected to the pathway work, not just to marketing style.
Inez | It is. The [[indications for use::Indications describe the specific proposed purposes and population, which must align with the regulatory assessment and evidence.]] must be clear and consistent. A broader statement can change the claim being assessed and the evidence needed to support it.
Caleb | Then October should be shown as an internal target with conditions. We cannot treat it as an agency commitment when neither the pathway nor the evidence package is settled.
Inez | Call it a [[launch assumption::The October date is a conditional planning premise rather than an authorized or guaranteed launch date.]] and show the dependencies. That allows planning without making a promise about a regulatory decision that has not occurred.
Caleb | We may seek feedback before filing. I will make sure the team does not describe a discussion with the agency as permission to market the device.
Inez | Correct. A [[pre-submission interaction::A pre-submission interaction can provide feedback but does not itself authorize marketing.]] is not the marketing decision. Any feedback and its scope should be recorded accurately without converting it into blanket approval.
Caleb | I will remove FDA approved and mark October as conditional. Send me the pathway-assessment milestone and its dependencies for the planning slide.
Inez | Good. The communication must distinguish planning from [[marketing authorization::Marketing authorization is the applicable permission to market within a defined scope, which this case does not supply.]]. We can describe the work confidently while leaving the unresolved regulatory decision exactly where it belongs.''',
    transfer_title='A filing is not a favorable decision',
    transfer_setup='A fictional US 510(k) submission has been filed. Review is ongoing, and no decision has been issued. The commercial team has an internal target date.',
    transfer='''Lead: "The submission has been ___." | filed | The facts establish submission but do not establish a favorable decision.
Specialist: "The agency's review remains ___." | ongoing | The case explicitly places the submission in an unfinished review.
Lead: "No 510(k) ___ has been issued." | clearance | Clearance is the relevant favorable 510(k) decision, which is not yet available.
Specialist: "The target date is a planning ___." | assumption | An internal date does not guarantee the timing or outcome of regulatory review.''',
    rehearsal=["Read the launch discussion. Distinguish pathway assessment, candidate predicate, filing, and an actual agency decision.","Swap roles. Use clearance for the 510(k) outcome and describe October as an internal conditional target.","Read the corrected filing transfer. A filed submission with ongoing review is not a granted clearance."]))


BOOK['units'].append(unit(
    title='Complaints, MDRs, and Postmarket Signals',
    scene='Incomplete information still needs a handoff',
    skill='Capture a complaint accurately, route missing information promptly, and distinguish counts from rates and reports from causation.',
    brief='Complaint specialist Nora and service lead Dev review a caller\'s report that a fictional monitor unexpectedly stopped displaying. The event date, device identifier, and patient outcome are not yet known. The call was received today at 14:10. Dev proposes waiting for every field before routing it. A separate dashboard shows eight complaints this quarter versus four last quarter, without use-volume data. Nora must preserve the unknowns, arrange the required internal review, and prevent either dataset from implying an unsupported conclusion.',
    cast='Nora | Complaint specialist\nDev | Service lead',
    culture=('Unknown is a useful status', 'A missing field can be stated clearly without sounding evasive. Say what was reported, what is unknown, who is seeking it, and where the information has been routed. This supports timely review while avoiding a false conclusion that no injury or device problem occurred.'),
    a='''Which time is known? | The call-receipt time, 14:10 today | The exact event time | The time of a confirmed patient injury | The time FDA issued a decision | The supplied time records receipt of the call, not the underlying event.
What is known about patient outcome? | It is not yet known. | No injury occurred. | A serious injury is confirmed. | The device definitely caused harm. | The case supplies no outcome, so neither absence nor presence of injury is established.
What does eight versus four establish? | The complaint count doubled, but no rate can be calculated from the supplied data. | The rate per use doubled. | The product caused twice as many injuries. | Reporting behavior stayed identical. | Counts can be compared directly, but a use-based rate requires a relevant denominator and context.''',
    vocabulary='''complaint | A reported concern about a device's quality, performance, safety, or related service. | capture a complaint
adverse event | An unfavorable occurrence that may require assessment of its relationship to a device. | assess an adverse event
malfunction | A failure to perform as intended or meet relevant performance specifications. | investigate a reported malfunction
Medical Device Reporting | The US system for reporting specified device events under applicable requirements. | assess Medical Device Reporting obligations
reportability | Whether an event meets applicable reporting requirements. | assess reportability
initial reporter | The person or organization first providing event information. | contact the initial reporter
awareness date | The date relevant event information becomes known for the applicable assessment. | document the awareness date
event date | The date on which the reported occurrence took place. | confirm the event date
receipt date | The date the organization received the communication. | record the receipt date
Unique Device Identifier | A device-identification code with defined identification components. | capture the Unique Device Identifier
serial number | An identifier distinguishing an individual unit. | verify the serial number
lot number | An identifier linking items to a production batch. | record the lot number
patient outcome | The reported effect on the patient's condition or health. | clarify the patient outcome
causal relationship | A supported connection between a device and an observed event. | assess the causal relationship
event narrative | A factual account of the reported occurrence and its context. | preserve the event narrative
reasonably known information | Information available or obtainable as defined by the applicable reporting requirement. | provide reasonably known information
follow-up attempt | A documented effort to obtain missing or clarifying information. | record a follow-up attempt
supplemental report | A later report providing required additional information. | submit a supplemental report
postmarket surveillance | Systematic collection and review of information after market introduction. | conduct postmarket surveillance
safety signal | Information suggesting a potential safety issue that needs assessment. | investigate a safety signal
trend analysis | Review of patterns in data over time. | perform trend analysis
exposure denominator | The relevant use or exposure quantity against which events are compared. | identify the exposure denominator
duplicate report | Another record potentially describing an already reported event. | assess duplicate reports
complaint closure | Documented completion of the required complaint-review process. | authorize complaint closure''',
    precision='The receipt time is not the event time. Unknown patient outcome is not the same as no injury. Preserve the reporter\'s account and route the available information through the applicable process while actively seeking missing facts.',
    precision_extra='Eight complaints versus four is a doubled count, not automatically a doubled rate per use or proof of causation. Reporting patterns, duplicates, exposure, and case differences matter. In this chapter, MDR means US Medical Device Reporting, not the EU Medical Device Regulation.',
    phrases='''Capture the account | The caller reported that the display stopped unexpectedly.
Separate dates | The call was received today; the event date is still unknown.
Mark a missing identifier | We have not yet confirmed the device identifier.
Preserve outcome uncertainty | Patient outcome has not been established.
Avoid causal certainty | This report does not by itself establish the cause.
Route available facts | Send the available information for prompt internal assessment.
Continue follow-up | Record the questions asked and the attempts to obtain missing information.
Distinguish the review | Reportability needs assessment under the applicable requirements.
Avoid a blanket rule | Missing fields do not justify withholding the initial internal handoff.
Use the right denominator | We need the relevant exposure data before describing a rate.
State the count | The count increased from four to eight.
Check duplicates | Confirm whether separate records describe the same event.
Avoid dismissal | An incomplete account still needs appropriate review.
Preserve the original | Keep the initial narrative alongside later clarifications.
Name the update route | New required information must follow the applicable reporting process.
Close with status | The case is routed, follow-up is open, and no cause is confirmed.''',
    notes='''Reported | Attributes information without treating every detail as independently verified.
Unknown | A distinct status, not a synonym for no or none.
Received | Describes the communication date, not necessarily when the event occurred.
Reportable | Requires the relevant criteria; not every complaint has the same reporting obligation.
Doubled | State whether a count, rate, or other measure doubled.
Caused | A causal conclusion needs more support than temporal association alone.''',
    d='''Which intake sentence preserves the facts? | Display interruption reported; event date, identifier, and patient outcome unknown; call received today at 14:10. | No injury and no malfunction; event occurred today at 14:10. | Confirmed device-caused injury at an unknown hospital. | Case closed because the serial number is missing. | The accurate sentence distinguishes supplied facts, unknown fields, and receipt time without inventing an outcome.
What is the appropriate internal handoff wording? | Route the available account promptly for assessment and continue documented follow-up. | Hold the case indefinitely until every field is complete. | Reject the report because the caller lacks an identifier. | Declare it nonreportable without the required assessment. | Missing information should trigger follow-up rather than replace the required internal review.
What does the dashboard support? | The count rose from four to eight; the rate per use is not established. | The injury rate doubled exactly. | Device causation doubled exactly. | Eight complaints prove eight unique serious injuries. | The dashboard supplies counts, not exposure, unique-event confirmation, outcomes, or causation.
The caller later reports no injury. Which update preserves the information history and review responsibilities? | Add the attributed clarification and its receipt time; continue the applicable reporting assessment. | Replace the original unknown field as though no injury was established at first receipt. | Close reporting assessment automatically because no injury is now reported. | Remove the original narrative because a later account supersedes every earlier detail. | A later no-injury report resolves an outcome detail, not the initial knowledge state or every reporting criterion. Some malfunction circumstances can require reporting assessment even without an injury.''',
    dialogue='''Dev | The caller said the monitor stopped displaying, but the device identifier and event date are missing. I thought we should wait before sending an incomplete record onward.
Nora | We should route the available [[event narrative::The event narrative preserves the reported occurrence while missing facts are pursued through follow-up.]] for prompt internal assessment and continue follow-up. An incomplete account is not a reason to withhold it from the responsible team.
Dev | I have routed the account now. The call arrived today at fourteen ten; the event date is still unknown.
Nora | I have received it for assessment. Record the [[receipt date::The supplied date and time concern receipt of the communication, not the unconfirmed event date.]] and time separately; do not copy them into the unknown event-date field.
Dev | The caller did not tell us whether anyone was injured. The draft summary says no injury, which is more definite than the information actually supports.
Nora | Change [[patient outcome::Patient outcome is unknown here; lack of supplied information does not establish that no injury occurred.]] to unknown. We should ask for clarification and record the response without treating silence in the first call as a confirmed absence of harm.
Dev | We also need to identify the unit accurately. A model name alone might not let the investigation team distinguish this device from other units at the site.
Nora | Seek the [[Unique Device Identifier::The Unique Device Identifier helps identify the device, while unavailable identification details remain follow-up items.]] and other relevant identification details through the approved process. Record what is available rather than inventing a serial number to complete the form.
Dev | Is this automatically reportable because the display stopped? Service needs to avoid delay without deciding beyond its role.
Nora | The responsible team must assess [[reportability::Reportability depends on applicable criteria and the event assessment, not the intake team's unsupported assumption.]] under the applicable requirements. Preserve the account and route it promptly; do not replace the assessment with an automatic yes or no.
Dev | I will document the missing questions and the calls we make to obtain answers. The case should show what we tried, not simply remain blank.
Nora | Each [[follow-up attempt::A follow-up attempt records efforts to obtain the information needed for the investigation and reporting assessment.]] helps make the information history clear. New facts should be linked to their source, including when they became available and any earlier uncertainty they resolve.
Dev | The summary says device-caused. Where did that conclusion come from? The caller described the display stopping; we do not yet have the cause.
Nora | Then the [[causal relationship::A causal relationship is not established merely because the caller reported an event involving the device.]] remains unconfirmed. Report the observation accurately without either asserting device causation or dismissing the device as unrelated before the evidence supports that conclusion.
Dev | The quarterly dashboard adds another concern: eight complaints this quarter and four last quarter. The presentation says the rate doubled, but there is no use-volume information.
Nora | We lack the [[exposure denominator::A rate relative to use requires the relevant exposure quantity, which the dashboard does not provide.]]. The count doubled; the rate per use is not established. We also need to examine reporting patterns and whether the records are comparable.
Dev | Some records might refer to the same occurrence. We should check that before treating every entry as a separate event or comparing the clinical outcomes.
Nora | Yes, assess each possible [[duplicate report::A duplicate report may describe an already recorded event, so record counts are not automatically unique-event counts.]] while preserving the source information. Deduplication needs a basis; a similar description alone should not make us erase a separate event.
Dev | The account is routed and you have confirmed receipt. I will correct the unknown fields and retain eight versus four complaints without inventing a rate or injury outcome.
Nora | Good. Any required later information must follow the applicable [[supplemental report::A supplemental report provides required later information through the appropriate reporting process rather than silently altering history.]] process. Keep investigation, reporting assessment, and complaint closure distinct so the record never suggests an unfinished task has already been completed.''',
    transfer_title='The report date is known',
    transfer_setup='A caller reports a device issue today. The event date and outcome are unknown. Six complaints were recorded this month, but the number of uses is unavailable.',
    transfer='''Specialist: "Today is the date the report was ___." | received | The case gives the communication date but not the event date.
Colleague: "The patient outcome is still ___." | unknown | No outcome was supplied, so absence of injury cannot be assumed.
Specialist: "Six is the complaint ___." | count | Six describes recorded complaints rather than a rate per use.
Colleague: "A use-based rate needs the exposure ___." | denominator | The relevant number of uses is missing from the supplied data.''',
    rehearsal=["Read the intake exchange. Route the account and confirm receipt before discussing missing details; preserve 14:10 as call receipt.","Swap roles. Say outcome unknown rather than no injury, and doubled count rather than doubled use-based rate.","Read the corrected six-complaint transfer. Keep event date unknown and the exposure denominator unavailable."]))

BOOK['units'].append(unit(
    title='Manufacturing, Suppliers, and Nonconformance',
    scene='Three hundred pieces on hold',
    skill='Separate affected-lot scope, observed failures, containment, cause, and authorized disposition in a supplier discussion.',
    brief='Quality engineer Tomas and supply planner Grace review two incoming component lots containing 120 and 180 pieces. One sampled piece from each lot failed a specified dimensional check. Both lots are on hold under the fictional site procedure. The cause is not established, and no release or rework disposition is authorized. Production needs parts tomorrow. Grace proposes describing all 300 pieces as defective, then releasing the second lot because its supplier certificate says conforming.',
    cast='Tomas | Quality engineer\nGrace | Supply planner',
    culture=('Be firm about status and exact about scope', 'Quality communication should not soften a hold into an informal preference, but it should not overstate the evidence either. Name the held population, the inspected failures, and the authorized next step separately. Production urgency can be acknowledged without becoming an unsupported release rationale.'),
    a='''How many pieces are in the two held lots? | 300 | 2 | 120 | 180 | The held-lot quantities are 120 and 180, which total 300 pieces.
How many sampled pieces are explicitly reported as failing? | Two, one from each lot | All 300 | Every piece in the second lot | None because a certificate exists | The brief reports two observed sampled failures, not inspection results for every piece.
What is the current disposition? | Both lots remain on hold; no release or rework is authorized. | The second lot is released automatically. | Both lots must be reworked using any available method. | All pieces are confirmed scrap. | The case supplies a hold and explicitly states that disposition has not been authorized.''',
    vocabulary='''incoming inspection | Examination of received material against specified requirements. | perform incoming inspection
nonconformance | Failure to fulfill a specified requirement. | document a nonconformance
nonconforming material | Material identified as not meeting a specified requirement. | control nonconforming material
containment | Immediate action to limit the scope or spread of a problem. | implement containment
quarantine | Controlled segregation or status preventing unintended use. | place material in quarantine
disposition | An authorized decision on how identified material will be handled. | approve material disposition
rework | Action intended to bring nonconforming product into conformity. | authorize a rework instruction
scrap | Material designated not to be used for its intended production purpose. | document a scrap decision
concession | An authorized permission to use or release specified nonconforming product under defined conditions. | evaluate a concession request
certificate of conformity | A supplier statement that supplied material meets specified requirements. | review the certificate of conformity
supplier corrective action request | A formal request for a supplier to address a quality problem. | issue a supplier corrective action request
corrective action | Action addressing the cause of a nonconformity to prevent recurrence. | verify corrective action
correction | Action addressing a detected nonconformity itself. | distinguish correction from corrective action
CAPA | Corrective and preventive action within a quality-system process. | assess the need for CAPA
lot genealogy | Records linking material lots through production and distribution. | trace lot genealogy
acceptance sampling | Evaluation of a lot using a defined sample and decision plan. | apply an acceptance-sampling plan
dimensional tolerance | The permitted variation in a specified measurement. | check dimensional tolerance
measurement uncertainty | The quantified uncertainty associated with a measurement result. | evaluate measurement uncertainty
calibration status | Whether a measuring instrument's calibration requirements are satisfied. | verify calibration status
supplier qualification | Evaluation and approval of a supplier for a defined purpose. | maintain supplier qualification
change notification | Communication of a proposed or implemented change affecting supply. | require a change notification
release status | The current authorization state for using or distributing material. | verify release status
Quality Management System Regulation | The current US device quality-system regulation, commonly called QMSR. | follow the Quality Management System Regulation
ISO 13485 | An international standard for medical-device quality management systems. | apply ISO 13485 requirements''',
    precision='The held population is 300 pieces. The supplied observation is two failed sampled pieces, one from each lot. Do not call all 300 individually confirmed defective, or treat uninspected pieces as conforming. The hold and the observed failures describe different scopes.',
    precision_extra='A supplier certificate does not cancel contrary inspection evidence or authorize release. Containment, correction, corrective action, and disposition are different steps. Since February 2026, the US framework is QMSR, incorporating ISO 13485:2016, rather than the former QSR framework.',
    phrases='''State the held population | Both lots are on hold, totaling 300 pieces.
State the observed failures | One sampled piece from each lot failed the dimensional check.
Avoid overstating scope | We have not inspected and confirmed every piece as defective.
Avoid assuming conformity | The uninspected pieces are not thereby proven conforming.
Name the requirement | Reference the specified dimension and applicable tolerance.
Preserve the hold | No release or rework disposition is authorized.
Acknowledge urgency | I understand tomorrow's need; the material status still has to be respected.
Assess contrary evidence | The certificate does not erase the failed inspection result.
Separate containment | The hold limits unintended use while the issue is assessed.
Keep cause open | The supplier cause has not been established.
Request a response | Ask for evidence addressing the specified nonconformance.
Clarify corrective action | Fixing a piece and preventing recurrence are different objectives.
Verify the instrument | Include calibration status and relevant measurement information in the review.
Trace the scope | Use lot records to assess what other material may be affected.
Define authorization | Only the designated process can approve the material disposition.
Close the handoff | Give production the confirmed status and the next review time, not an assumed release.''',
    notes='''Affected | Define whether this means held, inspected, failed, or potentially involved.
Defective | Avoid applying the label to an unexamined population without support.
Held | Describes a controlled status, not a final scrap decision.
Certificate | A supplier statement that remains subject to relevant acceptance evidence.
Rework | Needs the required authorization and controlled instructions.
Cause | An investigation conclusion, not something established by urgency or suspicion.''',
    d='''Which quantity statement is accurate? | Three hundred pieces are held; two sampled pieces are explicitly reported as failing. | All 300 pieces were individually tested and failed. | Only two pieces are held. | The 180-piece lot has no failed result. | The statement distinguishes total held quantity from the two observed sampled failures.
Production proposes using the 180-piece lot because its certificate is conforming. Which response preserves the current evidence and authority? | The failed sample and hold remain; the certificate does not replace an authorized disposition. | The certificate releases the lot, while only its failed sample remains on hold. | The lot is usable because the other 179 pieces have not been reported as failed. | The production deadline supplies temporary release authority pending the investigation. | The hold covers the whole lot. A certificate, missing individual results, and deadline do not supply the missing handling decision or cancel contrary inspection evidence.
Which statement distinguishes correction from corrective action? | Correction addresses the detected problem; corrective action addresses its cause to prevent recurrence. | Both terms mean signing a supplier certificate. | Correction always proves the cause is known. | Corrective action is complete when material is placed on hold. | The distinction concerns fixing the detected nonconformity versus addressing the cause of recurrence.
Which supplier update is best supported? | The cause remains open; provide relevant evidence while both lots retain their current hold status. | Your process definitely caused every piece to fail. | The second lot is released because its certificate is favorable. | Rework is authorized despite the absence of a disposition. | The supplied evidence supports an open investigation and continued stated hold, not a cause or release decision.''',
    dialogue='''Grace | Production needs the parts tomorrow. The lots contain 120 and 180 pieces. I was about to report all 300 as defective, but that overstates our inspection.
Tomas | [[Incoming inspection::Incoming inspection produced two sampled failures; it did not establish individual results for every piece.]] found two failed sampled pieces, one per lot. Both lots are held; those are different quantities and different statements.
Grace | So the report needs three hundred held, two observed failures. We cannot assign an individual result to pieces that were not inspected.
Tomas | Correct. Link each [[nonconformance::The nonconformance is the failure against the specified dimensional requirement, with its observed scope documented.]] to the dimensional requirement and lot. Uninspected does not mean conforming, either; keep the hold status visible.
Grace | The 180-piece lot has a supplier certificate saying conforming. Can that support using it while we investigate the failed sample?
Tomas | The [[certificate of conformity::A certificate is a supplier statement and does not override contrary inspection evidence or the current hold.]] does not override contrary inspection evidence. That lot remains held unless the authorized process establishes a different disposition.
Grace | I will tell production both lots remain unavailable. We have not established whether the two sampled failures have the same cause.
Tomas | Exactly. [[containment::Containment limits unintended use while the scope and cause are investigated; it is not a final causal conclusion.]] can be in place while cause remains open. Controlling the material does not require us to pretend the investigation is complete.
Grace | Could I ask quality about rework tonight? I need to offer production a next step without accidentally authorizing work myself.
Tomas | Request a [[disposition::Disposition is the authorized handling decision, which has not yet been made for these lots.]] review. Do not tell anyone to rework or use material before the required decision, instructions, and evaluation are in place.
Grace | Then tonight is a request for review, not an expected release. I should give production the actual status and the next update we can commit to.
Tomas | Keep [[release status::Release status records whether use is authorized, independently of schedule pressure or a hoped-for resolution.]] separate from the deadline. Schedule pressure can make the review urgent; it cannot provide evidence or approval.
Grace | The supplier offers to replace the two failed samples. That might address those particular pieces, but does not explain the dimensional problem.
Tomas | Replacement could be a [[correction::Correction addresses a detected nonconformity itself and does not necessarily resolve the underlying cause.]] through the approved process. It would not by itself establish the cause or prevent the same issue recurring.
Grace | I will request their manufacturing and inspection records. We should also examine our measurement setup rather than begin by assigning fault to the supplier.
Tomas | Include our instrument's [[calibration status::Calibration status is relevant measurement information to review, not automatic proof that either party caused the problem.]] and the relevant results. A certificate or a suspicion is not a substitute for the evidence from either side.
Grace | Once a cause is supported, I will ask what action addresses it and how effectiveness will be checked. A promise about future lots is not enough.
Tomas | That is the purpose of [[corrective action::Corrective action addresses a cause to prevent recurrence, with evidence needed to support its effectiveness.]]. Distinguish the action against recurrence from replacing a piece or maintaining the current hold.
Grace | For now: three hundred held, two sampled failures, cause open, no release or rework authorized. I will send that exact status to production.
Tomas | Use [[lot genealogy::Lot genealogy links material through production and distribution, supporting assessment of any wider affected scope.]] to check whether other material may be involved. Keep any wider scope qualified until the records support it.''',
    transfer_title='Held does not mean every piece failed',
    transfer_setup='A lot contains 90 pieces. Two sampled pieces failed a check. The whole lot is held, and no rework or release is authorized.',
    transfer='''Planner: "The held quantity is ___." | ninety | The hold covers the whole ninety-piece lot, not just the inspected failures.
Engineer: "The stated number of failed sampled pieces is ___." | two | Only two sampled failures are supplied in the case.
Planner: "The handling decision still needs authorized ___." | disposition | No decision permitting release or rework has been made.
Engineer: "A production deadline does not change the release ___." | status | Schedule urgency does not supply the missing authorization for material use.''',
    rehearsal=["Read the supplier exchange. State 120 plus 180 equals 300 held, with two observed sampled failures.","Swap roles. Keep both lots held, cause open, and release or rework unapproved despite the certificate and deadline.","Read the corrected ninety-piece transfer. Distinguish ninety held from two sampled failures and a disposition still required."]))

BOOK['units'].append(unit(
    title='Clinical Training and Labeling Boundaries',
    scene='A useful question outside this session',
    skill='Acknowledge an out-of-scope product-use request, keep the demonstration within authorized materials, and arrange a precise follow-up.',
    brief='Clinical trainer Sora is delivering a fictional device session using version 4 of internally approved materials for adult outpatient use. Clinician Alex asks for a pediatric home-use demonstration that the session materials do not cover. A version 3 slide remains in Sora\'s folder, but its current status has not been checked. No expanded-use authorization or reviewed response is supplied. Sora must acknowledge the question, avoid improvising the requested demonstration, and route it without implying that the clinician\'s question is improper.',
    cast='Sora | Clinical trainer\nAlex | Clinician attending the session',
    culture=('A boundary can include a next step', 'A useful response names what you can cover now and what needs another route. Do not shame the questioner or pretend the question was answered by a disclaimer. Keep product training, a clinician\'s independent judgment, and the organization\'s approved response process distinct.'),
    a='''What do the current session materials cover? | Adult outpatient use, version 4 | Pediatric home use under every condition | Every possible setting and population | A newly authorized expanded indication | The brief limits the internally approved session materials to adult outpatient use in version four.
What is missing for the requested demonstration? | Reviewed materials covering the requested pediatric home-use context | A willing audience | A question from a clinician | A previous version in the folder | Neither the request nor an unchecked old slide supplies the reviewed scope for the demonstration.
What should Sora avoid implying? | That the question is improper merely because it is outside the session scope | That version 4 is the session's current material | That a follow-up route is needed | That the requested use is not covered by these materials | The scenario calls for a respectful boundary, not a judgment that asking the question is itself improper.''',
    vocabulary='''labeling | Device-related written, printed, or graphic information accompanying or relating to the product. | review current labeling
instructions for use | The device's documented directions and relevant use information. | consult the instructions for use
indication | A specified condition or purpose for which use is described. | confirm the stated indication
contraindication | A circumstance in which the device should not be used. | identify a contraindication
warning | Information highlighting a significant hazard or safety concern. | communicate the relevant warning
precaution | Information about care needed to avoid problems during appropriate use. | explain a precaution
training scope | The users, tasks, settings, and content covered by a session. | define the training scope
approved material | Content authorized through the relevant internal review process. | use current approved materials
version control | Management of revisions so the appropriate version is used. | maintain version control
obsolete copy | A superseded document that is no longer the current controlled version. | remove an obsolete copy
demonstration unit | A device or model designated for showing functions under specified conditions. | identify the demonstration unit
simulation | A representation of a task or setting used for training or evaluation. | conduct a training simulation
in-service training | Instruction delivered to professionals in their work context. | schedule in-service training
competency assessment | Evaluation against defined knowledge or performance criteria. | distinguish attendance from competency assessment
attendance record | A record that a person participated in a session. | maintain an attendance record
scope boundary | The limit of what a session or role is authorized to cover. | state the scope boundary
off-label use | Use outside the product's authorized labeling, where that concept applies. | route an off-label-use question
unsolicited question | A question initiated by the recipient rather than prompted by the presenter. | document an unsolicited question
medical information request | A request routed for an appropriate reviewed scientific or product response. | route a medical information request
promotional claim | A statement used to encourage product selection or use. | review a promotional claim
disclaimer | A statement explaining a limitation or qualification. | avoid relying on a disclaimer alone
escalation route | The designated path for a question beyond the current role or scope. | follow the escalation route
follow-up commitment | A specified promise about the next communication or action. | make a realistic follow-up commitment
teach-back | Asking a learner to restate or demonstrate key information to check understanding. | use teach-back appropriately''',
    precision='Internally approved training material is not the same thing as a new regulatory authorization. A version number in a folder does not establish that the document is current. Confirm status through the controlled source rather than using an unchecked older slide.',
    precision_extra='Outside this session is narrower than clinically forbidden. The trainer should not turn a session boundary into unsupported medical or legal advice. A disclaimer does not make an otherwise unsupported demonstration appropriate; route the specific question through the applicable process.',
    phrases='''Acknowledge the question | That is a specific and useful question about a different population and setting.
State the session scope | Today we are covering adult outpatient use with version 4 materials.
Name the boundary | These materials do not cover pediatric home use.
Decline the demonstration | I cannot improvise that demonstration within this session.
Avoid judging the question | The limitation is the scope of my materials, not your ability to ask.
Offer the next route | I can document the question for the appropriate reviewed response.
Keep the request precise | I will preserve the population and setting you asked about.
Check the source | I need to confirm the current controlled version before using that slide.
Separate approval types | Internal material approval does not create an expanded product authorization.
Avoid a disclaimer shortcut | Adding a disclaimer would not resolve the missing reviewed content.
Respect clinical roles | I am not making a patient-specific treatment recommendation.
Clarify records | Session attendance is not the same as a completed competency assessment.
Bound the promise | I can confirm that the request was routed; I cannot promise a particular answer.
Keep the demonstration aligned | We will continue with the functions covered by the current session materials.
Check understanding | Please restate which use context today's session covers.
Close respectfully | I will follow up through the designated route while we keep this session within scope.''',
    notes='''Approved | Identify whether the approval concerns materials, product marketing, or another decision.
Current | Means the valid controlled version, not merely the latest file someone remembers.
Outside scope | States a boundary without making a universal clinical prohibition.
Cannot demonstrate | A role-and-material limit, not a claim that the question is illegitimate.
Will route | Promises an action, not the outcome of the reviewed response.
Attended | Confirms participation; it does not automatically establish competence.''',
    d='''Which reply is best supported? | These materials cover adult outpatient use; I can route your pediatric home-use question for a reviewed response. | The question is improper and must not be recorded. | Pediatric home use is authorized because a clinician asked about it. | I can demonstrate anything after adding a disclaimer. | The reply respects the question while accurately limiting the current materials and offering a review route.
How should Sora handle the version 3 slide? | Check its status against the controlled source before using it. | Assume it remains current because it is in the folder. | Treat its existence as expanded-use authorization. | Present it and correct any discrepancy after the session. | The folder copy has unverified status and cannot establish that the content is current.
The attendance sheet is complete after the session. What does that establish? | Recorded participation in this session, not performance against competency criteria | Competence for every task mentioned by a participant during questions | Authorization for pediatric home use because the topic was discussed | Completion of a skills assessment for all functions on the demonstration unit | Attendance records presence. Competence needs the defined assessment, while expanded-use authorization is a separate question that a signature or discussion cannot establish.
Which follow-up commitment is appropriate? | I will route the exact question and confirm the next communication through the designated process. | I guarantee approval of the requested use. | I will supply an improvised protocol tonight. | The reviewed response will certainly endorse the request. | The trainer can commit to routing and communication without promising an unsupported substantive outcome.''',
    dialogue='''Alex | Could you demonstrate pediatric home use? Our team has a question about that setting, although today's examples have been outpatient adults.
Sora | I can document the question, but today's [[training scope::The session scope is adult outpatient use and does not include the requested population and setting.]] is adult outpatient use. The version four materials do not cover the pediatric home-use demonstration you are requesting.
Alex | I understand the session limit. I am not asking you to make a decision for an individual patient; I want to know where the product question can be addressed.
Sora | Thank you. I can use the designated [[escalation route::The escalation route directs a question beyond the trainer's materials to the appropriate review process.]] for an appropriate reviewed response. I should preserve your specific population and setting rather than turn the request into a generic product question.
Alex | Would an older slide help? A previous presentation mentioned another setting, though I am unsure whether it covered this device version.
Sora | I have an older file, but its [[version control::Version control requires checking the valid controlled source rather than trusting an older file's presence.]] status has not been checked. A slide in my folder is not enough to establish that it is current or relevant.
Alex | That makes sense. Please do not use an uncertain slide simply to answer immediately. A reviewed response would be more useful than a demonstration built from partial information.
Sora | I will use only the current [[approved material::Approved material means content authorized through the relevant internal process, not an expanded regulatory permission.]] for this session. Internal approval of those materials also should not be confused with an expanded regulatory authorization for the product.
Alex | Could you still show the requested setup with a disclaimer that it is outside today's scope? I want to understand whether that would resolve your concern.
Sora | A [[disclaimer::A disclaimer does not supply the missing reviewed content or make an unsupported demonstration appropriate.]] would not supply the missing reviewed content. I cannot improvise the demonstration and then rely on a sentence saying it is outside the materials.
Alex | Understood. Please do not imply that my question was inappropriate. We need to be able to ask about uses outside a session's scope.
Sora | Absolutely. An [[unsolicited question::The clinician initiated the question; recording it does not imply that asking it was improper.]] can be documented respectfully. The boundary concerns what I can demonstrate here, not your ability to raise a specific scientific or product question.
Alex | Please keep pediatric home use in the request. A general adult outpatient answer would not address the population and setting our team is asking about.
Sora | I will retain that distinction in the [[medical information request::The request preserves the exact population and setting for an appropriate reviewed response.]] and follow the appropriate process. We do not need to add patient-specific details that are unnecessary for this product-level question.
Alex | Thank you. While we stay with today's materials, could you clarify what the attendance certificate represents? Our team should not confuse participation with a broader qualification.
Sora | The [[attendance record::An attendance record documents participation, not proof of competence across uses or clinical authority.]] confirms participation. It does not by itself establish that someone has met every competency criterion or is authorized for every possible clinical use.
Alex | Then competence requires the relevant assessment; a name on the session list does not demonstrate it.
Sora | Correct. A [[competency assessment::A competency assessment evaluates defined knowledge or performance criteria beyond mere attendance.]] has defined criteria. We should describe exactly what was assessed and avoid extending that result to populations or tasks outside the assessment.
Alex | Please route that question and tell me how we will hear back. We can continue with today's adult outpatient material while the separate response is pending.
Sora | I will make that [[follow-up commitment::The commitment concerns routing and communication, not a guaranteed substantive answer or authorization.]] through the designated process. I can confirm the action and next contact, but I cannot promise that the reviewed response will endorse the requested use.''',
    transfer_title='Stay specific when routing a question',
    transfer_setup='A session covers adult clinic use. A participant asks about pediatric home use. No reviewed material for that request is available, and the trainer will route it.',
    transfer='''Trainer: "Today's approved materials cover adult ___ use." | clinic | The session scope is adult clinic use, not the requested home context.
Participant: "My question concerns pediatric use at ___." | home | The requested setting must remain explicit in the handoff.
Trainer: "I will route the exact request for a reviewed ___." | response | Routing seeks an appropriate response without inventing content in the session.
Participant: "That does not mean the requested use is already ___." | authorized | A question or referral does not itself create authorization for the requested use.''',
    rehearsal=["Read the training exchange. Preserve version 4 adult outpatient scope and the specific pediatric home-use question.","Swap roles. Route the request without improvising a demonstration or treating the question as improper.","Read the corrected referral transfer. Routing for a reviewed response does not authorize the requested use."]))
