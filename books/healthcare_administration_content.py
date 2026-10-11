"""Original healthcare-administration communication cases."""
from books.authoring import unit

BOOK = dict(
    slug='healthcare-administration', title='Healthcare Administration English',
    cover_label='Access / operations / privacy / patient communication',
    cover_title='Healthcare\nAdministration', cover_size=30,
    tagline='Clarify the status. Coordinate the next step. Keep the patient informed.',
    audience='For patient-access, operations, revenue-cycle, quality, coordination, and administrative leadership teams.',
    map_intro='Practice eight administrative conversations in which precise status language, ownership, and follow-through matter.',
    notes_title='A clear handoff includes an owner.',
    notes_intro='Healthcare administration connects people, records, schedules, and decisions. A referral received is not an appointment booked; a discharge planned is not a bed available; a message sent is not a handoff accepted. These fictional cases practice the language needed to preserve those distinctions while remaining considerate and useful.',
    field_notes=[
        ('Tell the patient what is known', 'Acknowledge the request, explain the missing administrative step in ordinary language, and name the next update. Avoid making patients decode internal queue names or promises that depend on an unconfirmed clinical decision.', '"We received the referral. I am checking the missing information and will update you by three."'),
        ('Separate current status from expected status', 'Forecasts help teams plan, but they must remain visibly conditional. Confirm what has actually happened before reporting capacity, payment, transport, or approval as available.', '"Two discharges are planned; neither bed is confirmed available now."'),
        ('Match access to the actual task', 'A colleague\'s job title alone does not settle the scope of a data request. Confirm purpose, role, applicable permissions, and the appropriate sharing route through organizational policy.', '"Which fields are needed for this task, and has the requested access been confirmed?"'),
        ('Close the communication loop', 'A named owner, a next action, an update time, and acknowledgment make a handoff usable. Administrative follow-up does not replace clinical judgment or the appropriate route for urgent concerns.', '"I will confirm receipt and record who owns the unresolved transport request."')],
    scope_note='Original fictional language practice, not medical, legal, billing, coding, or compliance advice. US terminology appears where identified. Follow applicable law, payer rules, privacy safeguards, current organizational procedures, and qualified clinical judgment. No real patient information is used.',
    sources=[
        dict(title='US Department of Health and Human Services. Minimum Necessary Requirement.', url='https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html', note='Background for the US privacy example, including the standard\'s exceptions. The exercise is not a universal rule for every disclosure.', checked='10 October 2026'),
        dict(title='Centers for Medicare & Medicaid Services. Health Care Payment and Remittance Advice.', url='https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice', note='Background on remittance information and adjustment explanations. Fictional claim counts do not prescribe payer-specific correction or appeal steps.', checked='10 October 2026'),
        dict(title='Agency for Healthcare Research and Quality. What Is Patient Experience?', url='https://www.ahrq.gov/cahps/about-cahps/patient-experience/index.html', note='Background on patient interactions, timely information, and communication. The scheduling and service-recovery dialogues are original.', checked='10 October 2026'),
        dict(title='AHRQ Patient Safety Network. Communication During Transitions of Care.', url='https://psnet.ahrq.gov/perspective/communication-during-transitions-care', note='Background on clear handoffs and coordination. The administrative cases do not replace clinical transition protocols.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Patient Access, Scheduling, and Referrals',
    scene='The referral arrived, but the booking is not ready',
    skill='Request missing referral information and give a patient a reliable update without inventing clinical details.',
    brief='Scheduler Elena receives a referral with patient identifiers and contact details but no requested specialty or reason for the appointment. The patient expects a booking confirmation today. No appointment has been reserved and no clinical priority has been assigned. Referral-office colleague Marcus can seek clarification from the referring team. Elena can promise a status update by 3 p.m., not a confirmed appointment. Clinical urgency questions must follow the clinical review process rather than a scheduler\'s guess.',
    cast='Elena | Scheduler\nMarcus | Referral-office colleague',
    culture=('Make the next step concrete', 'Patients may hear received as ready to book. Explain the difference without blaming the referring office or listing internal obstacles. Promise an update you can control, identify who is seeking the missing information, and keep clinical prioritization with the appropriately qualified team.'),
    a='''What information is missing? | The requested specialty and reason for the appointment | Every patient identifier and contact detail | A confirmed appointment that already exists | A documented clinical priority marked urgent | The referral contains identifiers and contact details but lacks the specialty and appointment reason.
What can Elena reliably promise on the supplied facts? | A status update by 3 p.m. | A confirmed appointment by 3 p.m. | A particular specialist's clinical assessment | A same-day consultation regardless of availability | Elena controls the update, while booking depends on missing information and unconfirmed availability.
Who should determine clinical urgency? | The appropriately qualified clinical team through its review process | The scheduler from an assumption about the referral | The patient-access dashboard from receipt time alone | The newest staff member to open the file | The brief reserves clinical prioritization for the clinical review process, not administrative guesswork.''',
    vocabulary='''patient access | Administrative processes helping patients reach appropriate services. | coordinate patient access
referral | A request directing a patient to another service or professional. | process a referral
referring clinician | The clinician requesting another service or consultation. | contact the referring clinician
receiving service | The team or department expected to act on a referral. | identify the receiving service
specialty | A defined branch of clinical practice. | confirm the requested specialty
reason for referral | The stated clinical purpose of the requested consultation. | clarify the reason for referral
referral completeness | Whether the required referral information has been supplied. | check referral completeness
clinical triage | Qualified assessment of clinical priority and appropriate next care steps. | route for clinical triage
appointment slot | A defined time available for a scheduled visit. | confirm an appointment slot
scheduling template | The configured pattern of appointment types and times. | review the scheduling template
booking confirmation | A message establishing that an appointment has been arranged. | issue a booking confirmation
provisional hold | A temporary reservation subject to stated conditions. | distinguish a provisional hold from a booking
waitlist | A managed list of patients awaiting an available appointment. | maintain the waitlist
cancellation list | A list used to offer newly available appointments. | check the cancellation list
intake queue | The worklist holding incoming requests for initial processing. | monitor the intake queue
demographic verification | Checking patient identity and contact details for accuracy. | complete demographic verification
eligibility verification | Checking current insurance or service eligibility information. | request eligibility verification
network status | Whether a provider participates in the relevant insurance network. | confirm network status
authorization requirement | A condition requiring the relevant approval before a specified service or coverage. | check authorization requirements
interpreter request | A request for appropriate language assistance. | arrange an interpreter request
accessibility need | A requirement affecting a person's ability to use a service. | record an accessibility need
callback commitment | An explicit promise to contact someone again by a stated time. | honor a callback commitment
closed-loop referral | A referral process with tracked receipt, action, and feedback to the relevant parties. | support closed-loop referrals
escalation pathway | The designated route for unresolved or urgent issues. | follow the escalation pathway''',
    precision='Received means the referral arrived; complete means the required information is present; booked means an appointment is arranged. None of these statuses automatically establishes clinical urgency, insurance coverage, or authorization. State each confirmed fact separately.',
    precision_extra='A callback commitment promises communication, not a clinical decision or available appointment. Record the owner and time. If clinical urgency arises, follow the appropriate clinical escalation process; an administrative update deadline must not become a reason to delay necessary clinical attention.',
    phrases='''Acknowledge receipt | We received your referral and are checking the information needed to book.
Name the missing detail | The requested specialty and appointment reason are not shown.
Request clarification | Please confirm the intended receiving service with the referring team.
Avoid an invented reason | I cannot supply a clinical reason from the contact details alone.
Set an update | I will contact you by 3 p.m. with the current status.
Separate the promise | That is an update time, not a confirmed appointment time.
Mark booking status | No appointment has been reserved yet.
Route urgency | Clinical priority needs review by the qualified clinical team.
Take ownership | I will track the clarification request rather than ask you to restart it.
Confirm the contact | What is the appropriate contact route recorded for this request?
Support access | Let us confirm any interpreter or accessibility arrangements through the usual process.
Keep the patient informed | We are waiting for specific information, and I will update you even if it is still pending.
Check receipt | Please confirm that the referring team received the clarification request.
Preserve the distinction | A provisional hold would still need its conditions explained.
Avoid a guarantee | I cannot promise an available slot before the receiving service is confirmed.
Close the loop | Record the response, next action, owner, and patient update.''',
    notes='''Received versus accepted | Receipt alone may not establish that the receiving service can act.
By three | Specify whether this means an update or a completed booking.
Urgent | Do not infer a clinical category from impatience, a missing field, or an administrative deadline.
Clarify rather than diagnose | Ask for the clinical reason; do not invent it.
Ownership | A transfer to another queue should not erase responsibility for the promised update.
Coverage | Verification and authorization have distinct meanings and do not automatically guarantee payment.''',
    d='''Which message matches the referral's actual status? | We received the referral and need its specialty and reason; I will update you by 3 p.m. | Your referral is accepted, with the appointment awaiting only a convenient time. | Your booking is provisional because the patient identifiers have been checked. | The referral is routine, and three o'clock is the consultation window. | Receipt and identifiers do not establish acceptance, a held slot, or clinical priority. The supported commitment is a status update while the two missing details are clarified.
Which clarification should Marcus request? | The intended specialty and clinical reason from the referring team | A specialty selected to match today's first free slot | A clinical reason reconstructed from the patient's address | Permission to call the referral complete without further information | The missing fields require reliable clarification from the referring team rather than administrative invention.
What does the absence of an assigned priority mean? | Clinical priority is unconfirmed. | The patient is definitely low priority. | The patient automatically requires the highest priority. | Receipt time alone establishes the clinical category. | Missing priority information is not evidence of either low or high urgency.
At 3 p.m., clarification is still pending. What honors the commitment? | Contact the patient with the current status and a clear next update. | Wait silently until an appointment can be guaranteed. | Report a booking that has not been made. | Close the request because the deadline passed. | The promised action is a status update, so it should occur even when the underlying question remains unresolved.''',
    dialogue='''Elena | The referral arrived this morning, but the specialty and appointment reason are blank. The patient expects a booking confirmation today. I need to explain what happens next.
Marcus | Start with [[referral completeness::Referral completeness concerns the information required to process the request, and two essential details are missing here.]]. We have identifiers and contact details, but not enough information to identify the requested service. Receipt and readiness to book are different statuses.
Elena | The patient may think we lost the referral if I say we cannot confirm a visit yet. I want to acknowledge that it is here.
Marcus | Say it is in the [[intake queue::The intake queue holds the received request for processing; its presence there does not mean an appointment is arranged.]] and explain the missing details in ordinary language. Avoid giving the patient an internal queue name as though that answers the practical question.
Elena | Could you ask the referring office to confirm the specialty? I should not choose whichever service happens to have an opening this afternoon.
Marcus | I will contact the [[referring clinician::The referring clinician or team can clarify the intended clinical purpose and destination rather than leaving the scheduler to invent them.]] through the appropriate office route. The request will identify both missing fields so we do not resolve one and overlook the other.
Elena | We also have no clinical priority recorded. I cannot assume that the missing reason means the request is routine or unimportant.
Marcus | Correct. Any urgency question belongs in [[clinical triage::Clinical triage is the qualified assessment of priority; missing administrative information does not establish a clinical category.]]. Follow the established clinical review pathway instead of assigning a category from incomplete administrative information.
Elena | No appointment is reserved. I can update the patient by three, but I cannot promise that the missing information or a suitable slot will be available then.
Marcus | Make that a [[callback commitment::The callback commitment promises a status update by a stated time, not a completed appointment booking.]]. State the time and your responsibility clearly. The patient should hear a reliable next contact, not an implied promise of a consultation.
Elena | I will say we received the referral and are checking two details before booking. I can avoid blaming the other office or making the patient repeat everything.
Marcus | That distinguishes the update from a [[booking confirmation::A booking confirmation establishes an arranged appointment; none has been made in this case.]]. If the information is still pending at three, contact the patient anyway and explain the next step rather than letting the promise expire silently.
Elena | Once the specialty is confirmed, we still need the receiving team to identify the appropriate appointment type. A general opening may not fit the requested service.
Marcus | Yes. The [[scheduling template::The scheduling template defines appointment types and times; an available opening is not automatically suitable for every referral.]] needs to match the confirmed request. We should not turn an available time into an unsuitable booking simply to make the status look complete.
Elena | If the patient needs language assistance or an access arrangement, that should be recorded through our usual process before the visit is finalized.
Marcus | Include an [[interpreter request::An interpreter request identifies a language-access need that should be arranged through the appropriate service process.]] where appropriate, and check other relevant access needs. The booking should be usable for the patient, not merely occupy a line on the calendar.
Elena | I will update the patient by three. Please confirm when the referring office receives your request, and tell me if you need help reaching them.
Marcus | That gives us a [[closed-loop referral::A closed-loop referral tracks receipt, action, and feedback so the request does not disappear between teams.]] process rather than two disconnected messages. We need a visible response and next action, not just evidence that someone pressed send.
Elena | If the usual contact cannot resolve it, who takes the next step? I want a clear route while I keep the patient updated.
Marcus | Follow the [[escalation pathway::The escalation pathway identifies how unresolved issues reach the appropriate owner without inventing clinical decisions or promises.]] and preserve the distinction between administrative follow-up and clinical judgment. The immediate commitment remains a clear update by three, with no invented appointment or priority.''',
    transfer_title='A callback is not a consultation',
    transfer_setup='A scheduler promises a status call by 2 p.m. The specialist has not reviewed the referral, and no appointment is reserved. At 2 p.m., review is still pending.',
    transfer='''Scheduler: "I promised a status ___." | call | The commitment concerns communication at a stated time, not a clinical consultation.
Colleague: "The specialist review remains ___." | pending | The supplied facts say review has not been completed.
Scheduler: "No appointment is ___." | reserved | The briefing expressly states that no appointment has been held or booked.
Colleague: "Make the promised update without implying a booking ___." | confirmation | A status update must not be presented as confirmation of an appointment that does not exist.''', rehearsal=["Check the cloze key, then read the referral exchange. Keep identifiers received separate from the missing specialty and appointment reason.","Switch roles for the scheduling discussion. Stress update by three, no reserved slot, and clinical priority unconfirmed; do not choose a specialty for convenience.","Complete and check the two-o'clock callback exchange. Make the promised status call while review remains pending, without calling it a consultation."]))

BOOK['units'].append(unit(
    title='Revenue Cycle, Coding, and Denials',
    scene='One exception total hides two kinds of follow-up',
    skill='Distinguish submission rejections from adjudicated denials and assign follow-up using the actual response record.',
    brief='A dashboard lists 20 exceptions among 100 submitted claims. The underlying records show 12 rejected before adjudication because required member identifiers were missing or invalid, and eight denied after payer review. The other 80 claims have not been analyzed in this meeting and must not be called paid. Revenue-cycle manager Leo and billing analyst Tessa need separate worklists, reasons, owners, and applicable deadlines. They must verify payer-specific correction or appeal routes, not change clinical codes merely to obtain payment.',
    cast='Leo | Revenue-cycle manager\nTessa | Billing analyst',
    culture=('Name the stage before naming the solution', 'A rejected submission and a denied claim may require different follow-up. Start with the actual acknowledgment or remittance record, not a dashboard label. Explain the stage, reason, and next responsible team without promising payment or treating every unpaid item as a patient balance.'),
    a='''How many exceptions were rejected before adjudication? | Twelve | Eight | Twenty | Eighty | The underlying records identify twelve submission rejections and eight post-review denials.
What is known about the other 80 claims? | They were not analyzed in this meeting. | All were paid in full. | All were denied for missing identifiers. | They are all patient balances. | The briefing expressly leaves their status unanalyzed, so payment and responsibility cannot be inferred.
What must guide the correction or appeal route? | The actual response and applicable payer rules | The assumption that every exception uses the same appeal | A change to whichever diagnosis code pays more | The color of the dashboard category | The stage, reason, and payer-specific process determine follow-up; an exception total alone does not.''',
    vocabulary='''revenue cycle | The sequence of administrative and financial processes from patient access through payment follow-up. | manage revenue-cycle performance
claim submission | Sending a request for payment to a payer. | track claim submissions
clearinghouse | An intermediary processing and transmitting electronic health-care transactions. | review clearinghouse responses
acknowledgment | A response indicating receipt or initial processing status. | inspect the claim acknowledgment
front-end rejection | A submission failure before the relevant adjudication stage in the stated workflow. | correct a front-end rejection
adjudication | Payer review determining how a claim is processed for benefits and payment. | confirm adjudication status
claim denial | A payer decision not to allow payment as requested after review in this case. | analyze claim denials
remittance advice | Information explaining payment and adjustments for processed claims. | review the remittance advice
claim adjustment reason code | A standardized code explaining why a claim payment differs from the billed amount. | interpret the claim adjustment reason code
remittance advice remark code | A code supplying additional explanation related to an adjustment or processing result. | review remittance advice remark codes
member identifier | The information identifying the person within the relevant health plan. | verify the member identifier
payer identifier | The identifier used to direct a transaction to the intended payer. | validate the payer identifier
clean claim | A claim meeting the applicable completeness and processing requirements. | define the clean-claim measure
corrected claim | A submission changing information through the payer's applicable correction process. | submit a corrected claim
resubmission | Sending a claim again through the appropriate process. | track the resubmission
appeal | A request to reconsider an adverse determination under the applicable rules. | evaluate appeal options
timely-filing limit | The applicable deadline for submitting a claim. | verify the timely-filing limit
appeal deadline | The applicable time limit for requesting review of a decision. | track the appeal deadline
denial reason | The stated basis for a payer's denial. | categorize denial reasons
workqueue | A managed list of items awaiting assigned action. | assign the billing workqueue
accounts receivable | Amounts recorded as due to the organization. | review accounts receivable
aging bucket | A grouping of outstanding balances by elapsed time. | monitor aging buckets
patient responsibility | The amount properly assigned to the patient under applicable coverage and billing rules. | verify patient responsibility
coding integrity | Accurate coding supported by the clinical record and applicable rules. | preserve coding integrity''',
    precision='For this case, rejected means not accepted into adjudication; denied means reviewed and not allowed as requested. Real systems may use labels differently. Verify the acknowledgment and remittance details rather than relying on one word in a dashboard.',
    precision_extra='ERA means electronic remittance advice; CARC, claim adjustment reason code; RARC, remittance advice remark code; and A/R, accounts receivable. These records help explain status and adjustments. An unpaid amount is not automatically patient responsibility, and a correction does not guarantee payment.',
    phrases='''Separate the stages | Twelve submissions were rejected before adjudication; eight claims were denied after review.
Avoid an inflated conclusion | The other eighty claims have not been analyzed here.
Request the source | Show the acknowledgment or remittance record behind this category.
Name the rejection issue | The member identifier is missing or invalid on these submissions.
Verify before correcting | Check the identifier against the appropriate source record.
Route by reason | Assign follow-up according to the actual response and payer process.
Check the deadline | Confirm the applicable filing or appeal deadline for each item.
Preserve coding accuracy | Do not change a clinical code solely to obtain payment.
Distinguish next steps | A correction and an appeal are not interchangeable in every workflow.
Clarify the denominator | The twenty exceptions are out of one hundred submitted claims.
Avoid a payment promise | Resubmission does not establish that the payer will pay.
Track completion | Record the action, owner, date, and resulting status.
Keep responsibility open | Do not transfer an unresolved amount to the patient without the required review.
Explain the adjustment | Read the reason code together with any relevant remark.
Prevent double-counting | Count a claim consistently as it moves through the workqueues.
Close with visibility | Show separate rejection and denial totals alongside unresolved follow-up.''',
    notes='''Rejected versus denied | Use the actual transaction stage, since local labels may be inconsistent.
Submitted versus paid | Submission counts do not establish collection results.
Reason plus remark | One code may not contain the full explanation needed for action.
Corrected versus original | Follow the payer's actual process instead of creating uncontrolled duplicate submissions.
Deadline | Do not assume one universal filing or appeal period.
Patient balance | Confirm the applicable basis before describing an amount as owed by the patient.''',
    d='''What percentage of the 20 exceptions are pre-adjudication rejections? | 60% | 12% | 40% | 80% | Twelve divided by twenty equals 60%; 12% would use all one hundred submissions as the denominator.
Which dashboard breakdown preserves both stage and denominator? | Twelve pre-adjudication rejections and eight reviewed denials out of 100 submissions | Twenty reviewed denials and eighty paid claims out of 100 submissions | Twelve rejected claims, eight appeals won, and eighty claims awaiting payment | Twenty rejected submissions out of eighty successfully paid claims | The records identify twelve rejections before adjudication and eight denials after review. They establish neither appeal outcomes nor the payment status of the other eighty.
A rejection cites an invalid member identifier. What should happen first? | Verify the identifier and applicable correction process against reliable records. | Replace the diagnosis with a higher-paying code. | Send a generic appeal without checking the stage. | Charge the patient immediately because the submission failed. | The stated rejection concerns identifier data, so the first action is accurate verification and route selection.
Which summary preserves the financial uncertainty? | Correction or appeal may resolve the issue, but payment and patient responsibility remain subject to review. | Every corrected claim must be paid at its full billed amount. | Every denial automatically creates a patient debt. | A submitted appeal is equivalent to an overturned denial. | Taking a follow-up action does not establish its outcome or the correct assignment of financial responsibility.''',
    dialogue='''Leo | Twenty exceptions out of one hundred submissions. Can I call that a twenty-percent denial rate in the management update?
Tessa | Not from this breakdown. Twelve are [[front-end rejections::Front-end rejections occurred before adjudication in this case, unlike the eight claims denied after review.]] for missing or invalid member identifiers. Only eight reached payer review and were denied.
Leo | Then my appeals-backlog label is wrong too. Where do we check which stage each submission actually reached?
Tessa | Start with its [[acknowledgment::The acknowledgment records the submission's receipt or processing status and helps establish where it stopped.]] and payer response. The dashboard groups work for convenience; it does not establish the correct next action.
Leo | For the twelve identifier errors, could we copy the number from an older paid claim? That would clear them quickly.
Tessa | Verify the current [[member identifier::The member identifier identifies the person within the plan; missing or invalid values are the stated rejection cause.]] against the appropriate source first. An old claim can be a lead, but it is not permission to guess or reuse unchecked information.
Leo | And for the eight denials, I need more than denied on a list. Can we see why payment was not allowed?
Tessa | Yes. Review the [[remittance advice::The remittance advice explains processed-claim payment and adjustments, helping identify the denial reason and relevant follow-up.]] and supporting details. A documentation issue and a coverage determination may require different payer-specific follow-up.
Leo | The summary has a broad adjustment reason. Is there another code that explains the missing detail?
Tessa | Check for a [[remittance advice remark code::A remittance advice remark code adds detail that may be needed to interpret the adjustment or processing result.]] alongside the adjustment reason and group code. Read them together before assigning correction, reconsideration, or appeal work.
Leo | Prioritize by deadline as well as category. I do not want older items expiring while we fix the easier ones.
Tessa | We will check each [[timely-filing limit::The timely-filing limit governs submission timing and must be verified for the relevant payer and claim context.]] and any separate appeal deadline. Sending something again does not necessarily restart the applicable clock.
Leo | A colleague suggested a different diagnosis code on one denial because it might pay. I want that handled properly.
Tessa | That needs qualified review for [[coding integrity::Coding integrity requires support from the clinical record and applicable rules, not changes selected solely to obtain payment.]], based on the clinical record. Payment preference cannot supply evidence for changing a diagnosis.
Leo | What can I say about the other eighty? The dashboard leaves them outside the exception group, but we have not reviewed them here.
Tessa | Their payment status is unresolved in this meeting. We cannot label them paid or assign [[patient responsibility::Patient responsibility must be established under applicable rules; unresolved or unanalyzed claims do not automatically become patient balances.]] merely because this view shows no exception.
Leo | Create two lists, then: twelve rejections and eight denials. I need an owner, reason, deadline, and latest status against each claim.
Tessa | I will structure the [[workqueue::The workqueue organizes follow-up with owners and status, rather than leaving a combined exception total without actions.]] that way and retain claim identity across resubmissions. Several messages about one claim must not become several claims.
Leo | The twelve are sixty percent of exceptions, but twelve percent of all submissions. I will put the denominator next to each percentage.
Tessa | Good. Keep the [[denial analysis::Denial analysis should use the reviewed-denial group and its actual reasons, not combine every submission exception into one category.]] focused on the eight adjudicated denials. We can describe the follow-up clearly without promising its payment outcome.''',
    transfer_title='The denominator changes the percentage',
    transfer_setup='A separate batch contains 200 submitted claims and 30 exceptions. Of the exceptions, 18 were rejected before adjudication and 12 denied after review. No payment status is supplied for the remainder.',
    transfer='''Analyst: "Rejections are ___ of all submissions." | 9% | Eighteen divided by two hundred equals 9%, using all submissions as the denominator.
Manager: "Rejections are ___ of the exceptions." | 60% | Eighteen divided by thirty equals 60%, using only the exception group.
Analyst: "Reviewed denials total ___." | twelve | The briefing identifies twelve claims denied after review, distinct from eighteen rejections.
Manager: "Payment status for the remainder is ___." | unspecified | The exercise gives no payment information for the remaining claims, so paid status cannot be inferred.''', rehearsal=["After checking the answers, read the claims discussion. Distinguish twelve front-end rejections from eight post-review denials, with 100 submissions as the total.","Switch roles for turns 11-20. Say sixty percent of exceptions and twelve percent of submissions distinctly; do not label the other eighty paid.","Complete the separate-batch exchange and check the key. Read eighteen out of 200 as 9%, and eighteen out of thirty as 60%."]))


BOOK['units'].append(unit(
    title='Patient Flow, Capacity, and Staffing',
    scene='Planned discharges are not available beds',
    skill='Report usable capacity with a time reference and distinguish physical space from staffed, ready capacity.',
    brief='A unit has 28 physical beds, of which 24 are staffed and operational today. All 24 operational beds are occupied at the 10 a.m. census. Two discharges are planned, but neither timing nor completion is confirmed. The other four beds are not staffed for use. Flow coordinator Hana and unit manager Paul must correct a message saying two beds are available now. Any new placement depends on confirmed departure, room readiness, appropriate staffing, and the relevant clinical allocation process.',
    cast='Hana | Flow coordinator\nPaul | Unit manager',
    culture=('Attach time and conditions to capacity', 'Capacity figures become misleading when yesterday\'s position, a forecast, and the current state share the same label. Say available now only when the relevant readiness conditions are confirmed. Explain the next check and owner so a conditional forecast remains useful without becoming an instruction to place a patient.'),
    a='''How many staffed operational beds are unoccupied at 10 a.m.? | Zero | Two | Four | Six | All twenty-four staffed operational beds are occupied; planned departures and unstaffed spaces do not create current availability.
What is the occupancy rate using staffed operational beds? | 100% | About 86% | About 92% | 50% | Twenty-four occupied beds divided by twenty-four staffed operational beds equals 100%; using all physical beds changes the denominator.
What remains unconfirmed? | The timing and completion of the two planned discharges | Whether twenty-four beds are occupied at the census | Whether four physical beds are unstaffed | Whether the census has a stated time | The case supplies the current counts but expressly leaves discharge timing and completion unconfirmed.''',
    vocabulary='''patient flow | Movement of patients through stages and locations of care. | coordinate patient flow
bed census | A count of occupied beds at a defined time. | report the bed census
physical bed capacity | The number of bed spaces physically present. | distinguish physical bed capacity
staffed capacity | Capacity supported by the required available staffing. | confirm staffed capacity
operational bed | A bed available for use when applicable operational conditions are met. | verify operational-bed status
occupancy rate | Occupied capacity divided by a specified capacity denominator. | state the occupancy-rate denominator
anticipated discharge | An expected departure that has not necessarily occurred. | track anticipated discharges
confirmed discharge | A departure or discharge status verified under the relevant process. | distinguish confirmed discharges
discharge barrier | An unresolved condition delaying a planned departure. | identify discharge barriers
bed turnaround | The process and time needed to prepare a vacated bed for reuse. | monitor bed turnaround
environmental services | The function providing cleaning and related environmental support. | coordinate with environmental services
room readiness | Confirmation that a room meets the conditions for its next use. | verify room readiness
bed allocation | Assignment of a suitable bed through the appropriate process. | confirm bed allocation
acuity | The level of a patient's clinical complexity or care needs. | account for patient acuity
skill mix | The combination of staff capabilities available for a workload. | review the skill mix
staffing coverage | The personnel available to support defined work over a period. | verify staffing coverage
surge capacity | Additional capacity that can be mobilized under defined conditions. | assess surge capacity
contingency staffing | Alternative staffing arrangements used under an approved plan. | confirm contingency staffing
admission demand | The number and nature of patients requiring admission. | review admission demand
transfer request | A request to move a patient between care locations. | track transfer requests
boarding | Waiting in a location for an appropriate inpatient placement or next care setting. | monitor boarding
throughput | The rate at which patients move through a defined process. | evaluate patient throughput
flow huddle | A brief coordination meeting about current flow and constraints. | conduct a flow huddle
capacity forecast | An estimate of future usable capacity with stated assumptions. | qualify the capacity forecast''',
    precision='Occupancy is 100% on the staffed operational basis: 24 divided by 24. Dividing by 28 gives about 86% physical-bed occupancy, a different measure. Neither calculation makes the four unstaffed beds or two anticipated discharges available now.',
    precision_extra='A forecast can inform planning without authorizing placement. A departure may still be followed by cleaning, readiness checks, staffing confirmation, and clinical allocation. Keep each status explicit; no universal staffing ratio or clinical placement rule is supplied by this exercise.',
    phrases='''Time-stamp the count | At 10 a.m., all twenty-four staffed operational beds are occupied.
Correct the availability | The two discharges are planned, not completed.
State the denominator | Occupancy is 100% of staffed operational capacity.
Separate physical space | Four additional physical beds are not staffed for use today.
Keep the forecast conditional | Two beds may become available after the required conditions are met.
Name the dependency | Departure, room readiness, staffing, and allocation still need confirmation.
Avoid an implied placement | This forecast does not authorize a patient transfer.
Request a fresh status | Please confirm the position before the next flow huddle.
Identify the owner | Who will update the bed status after readiness is verified?
Expose the barrier | Which unresolved issue affects the expected discharge time?
Protect the distinction | Vacated does not automatically mean ready for the next patient.
Check suitability | Clinical placement must follow the appropriate assessment process.
Avoid a false promise | I cannot report capacity that is not yet confirmed.
Coordinate the handoff | Notify the receiving team when the actual status changes.
Label the estimate | This is a capacity forecast, not an available-bed count.
Close the correction | Replace available now with anticipated, timing unconfirmed.''',
    notes='''Now versus later | A time reference is essential when capacity changes quickly.
Physical versus staffed | An empty physical space may not be usable capacity.
Discharged versus ready | Departure and readiness are separate operational states.
Two planned | This describes a forecast, not a completed event.
Occupancy denominator | Always identify whether the measure uses physical, staffed, or another defined capacity.
Placement | An administrative capacity statement does not replace clinical allocation decisions.''',
    d='''Which message accurately corrects the original update? | At 10 a.m., no staffed operational beds are free; two discharges are anticipated with timing unconfirmed. | Two beds are available because two discharges appear in the plan. | Four beds are available because physical capacity exceeds occupied beds. | Occupancy is low enough to accept any transfer immediately. | The corrected message preserves the current census and keeps planned departures conditional.
What does 24 divided by 28 measure here, and what does it omit? | Physical-bed occupancy; it includes four beds not staffed for use. | Staffed-bed occupancy; it includes two completed discharges. | Available operational capacity; it excludes the four unstaffed spaces. | Post-discharge occupancy; it assumes the two rooms are cleaned. | The denominator 28 counts physical beds, whereas today's staffed operational denominator is 24. The ratio is about 86%, but all 24 operational beds are occupied and neither discharge is confirmed.
What must follow a confirmed departure before availability is reported? | Verify the relevant readiness, staffing, and allocation conditions. | Automatically mark every adjacent bed ready. | Assume the forecast has supplied clinical approval. | Treat the discharge plan as proof that cleaning already occurred. | A departed patient does not by itself establish all conditions needed for the next placement.
Which update best supports planning without promising capacity? | Two discharges are anticipated; the unit will confirm timing and readiness at the next agreed check. | Two beds are definitely available now, subject to later confirmation. | Physical space alone is sufficient for every placement. | No update should be given until every future admission is known. | The useful forecast states its uncertainty and next confirmation step without contradicting the current count.''',
    dialogue='''Hana | The transfer desk has been told that two beds are available. Your ten o'clock count shows twenty-four occupied beds. What changed after the count?
Paul | Nothing has been confirmed. The [[bed census::The bed census is the count at a stated time; at 10 a.m. all operational beds were occupied.]] still shows all twenty-four staffed operational beds occupied. Two departures are planned, but neither has a confirmed completion time.
Hana | Then the message has converted an expectation into present capacity. I will correct it before the receiving team treats it as permission to send someone.
Paul | Please call them [[anticipated discharges::Anticipated discharges are expected departures, not confirmation that beds are empty or ready.]], not available beds. That keeps the information useful for planning while making clear that the patients have not yet left.
Hana | The building has twenty-eight beds. Someone may divide twenty-four by twenty-eight and conclude that four spaces are free for admissions.
Paul | That confuses physical space with [[staffed capacity::Staffed capacity excludes the four physical beds not staffed for use today.]]. The other four beds are not staffed for use today. They are not an immediately usable reserve merely because they appear on the floor plan.
Hana | For today's operational position, twenty-four occupied out of twenty-four staffed beds means full occupancy. We should name the denominator in the update.
Paul | Yes. The [[occupancy rate::The occupancy rate is 100% on the stated staffed operational basis: 24 occupied out of 24.]] is one hundred percent on that basis. A physical-bed percentage answers a different question and should not be substituted without explanation.
Hana | Do we know what is holding up the two expected departures? A forecast would be more useful if we understood which conditions remain unresolved.
Paul | We need a current [[discharge-barrier::A discharge-barrier check identifies unresolved conditions affecting departure without assuming that the discharge has occurred.]] check through the responsible team. I will request the status without inventing a departure time or making the clinical decision myself.
Hana | Even after a patient leaves, the room may not be ready for immediate reuse. The next team needs more than a departure notification.
Paul | Correct. [[Bed turnaround::Bed turnaround includes preparing a vacated bed for reuse; departure does not automatically establish readiness.]] must be tracked through the relevant process. Environmental services and the responsible staff need to confirm their parts before the status becomes ready.
Hana | Once a room is ready, who confirms it is suitable for the incoming patient? I do not want a room-status change treated as placement approval.
Paul | The [[bed allocation::Bed allocation assigns a suitable bed through the appropriate process, including relevant clinical and operational requirements.]] process handles that. Capacity language should support the decision, not bypass the appropriate assessment of patient needs, staffing, and the setting.
Hana | I will label the two possible openings as conditional. The transfer desk can plan around the possibility without treating it as a completed availability check.
Paul | That is a [[capacity forecast::A capacity forecast estimates future availability under conditions and is distinct from the current available-bed count.]]. Include the dependencies and the next update time. A forecast without those limits can quickly become a promise as it moves between teams.
Hana | Who will update the desk when the status changes? I do not want the corrected message to sit unchanged after the room actually becomes ready.
Paul | I will own the unit update and confirm it at the next [[flow huddle::The flow huddle is the coordination point for sharing current status, constraints, and responsible follow-up.]]. If the position changes sooner, I will notify the desk through the usual channel rather than wait for the meeting.
Hana | I will correct the desk now: no operational bed is free at ten, and the two possible openings depend on discharge and readiness confirmation.
Paul | That matches the facts. We still need [[room readiness::Room readiness confirms the relevant conditions for reuse; it has not yet been established for the anticipated discharges.]] and the other applicable conditions before reporting availability. Keep the current count and the future possibility on separate lines.''',
    transfer_title='An empty room still has conditions',
    transfer_setup='One patient has left. The room is awaiting cleaning, and staffing for the next placement has not been confirmed. The status system distinguishes vacated from ready.',
    transfer='''Coordinator: "The room is ___." | vacated | Departure establishes that the patient has left, not that the room meets all readiness conditions.
Colleague: "Cleaning remains ___." | pending | The briefing says the room is awaiting cleaning.
Coordinator: "Staffing still needs ___." | confirmation | Staffing for the next placement has not been verified.
Colleague: "Do not mark the room ___ yet." | ready | Cleaning and staffing are unresolved, so the supplied readiness conditions have not been met.''', rehearsal=["Check the cloze key and read the flow huddle. State the ten-o'clock census as twenty-four occupied staffed beds out of twenty-four.","Switch roles for the forecast. Keep two anticipated discharges separate from available beds, and retain the four unstaffed physical spaces.","Complete and check the vacated-room exchange. Distinguish departure, pending cleaning, unconfirmed staffing, and actual readiness before placement."]))

BOOK['units'].append(unit(
    title='Quality, Safety, and Accreditation',
    scene='Caught in time, but not yet explained',
    skill='Describe a near miss factually and distinguish a corrective action from evidence that recurrence risk has been reduced.',
    brief='A patient was assigned to the wrong specialty clinic. A second check caught the error before the appointment, and no clinical harm is reported. The referral record and booking history are available, but the cause has not been established. Quality coordinator Asha and operations lead Ben are preparing a learning review and evidence for an upcoming accreditation discussion. The event must follow the organization\'s reporting process. A proposed refresher session is not yet supported by a finding that lack of training caused the error.',
    cast='Asha | Quality coordinator\nBen | Operations lead',
    culture=('Investigate the process without inventing blame', 'A factual account separates what happened, how it was detected, the known impact, and what remains uncertain. Thank the person who detected the problem while examining why the earlier steps allowed it. An action plan should address supported contributing factors rather than assume that another reminder will solve everything.'),
    a='''What is established about the event? | The wrong-specialty booking was caught before the appointment, with no clinical harm reported. | A training failure has been proved. | The system is guaranteed to prevent recurrence. | The accreditation review has already approved every process. | The brief establishes the booking error and interception, while cause and recurrence protection remain unresolved.
Why is a refresher session not yet a complete response? | The review has not established a training gap or how the action would address the cause. | Training can never be part of a quality response. | Near misses must be excluded from learning reviews. | A proposed meeting automatically demonstrates effectiveness. | The response should follow evidence about contributing factors rather than assume a cause before investigation.
What should the review use? | The referral record, booking history, and other relevant verified evidence | Only the first explanation offered in conversation | Only the absence of reported clinical harm | A rewritten record removing the error | The available records can help reconstruct the sequence; absence of harm alone does not explain the event.''',
    vocabulary='''near miss | A potentially harmful event intercepted or otherwise not resulting in harm. | report a near miss
safety event | An occurrence relevant to patient safety under the applicable reporting system. | document a safety event
incident report | A structured record of an event requiring review or follow-up. | submit an incident report
event chronology | The verified sequence of events and actions. | reconstruct the event chronology
contributing factor | A condition that helped an event occur or affected its outcome. | identify contributing factors
root cause analysis | A structured investigation of underlying factors behind an event. | scope the root cause analysis
systems approach | Examination of how processes and conditions shape performance. | use a systems approach
human factors | Study of how people interact with tools, tasks, and environments. | assess human-factors issues
just culture | An approach combining learning, fair accountability, and attention to system conditions. | support a just culture
psychological safety | A climate in which people can raise concerns without interpersonal fear. | strengthen psychological safety
detection control | A process intended to identify an error before further consequences. | evaluate the detection control
preventive control | A process intended to reduce the chance that an error occurs. | strengthen preventive controls
process map | A representation of the steps and handoffs in a workflow. | build a process map
failure mode | A way in which a process or component can fail. | identify a failure mode
risk register | A record of identified risks, responses, and ownership. | update the risk register
corrective action plan | A documented set of actions addressing an identified problem. | agree the corrective action plan
action owner | The person accountable for completing a specified action. | name the action owner
implementation evidence | Records showing that a planned action was carried out. | collect implementation evidence
effectiveness measure | A defined measure used to judge whether an action worked. | specify the effectiveness measure
process measure | A measure of whether a defined activity or step occurs as intended. | track a process measure
outcome measure | A measure of the result the process is intended to influence. | review the outcome measure
balancing measure | A measure monitoring unintended effects of a change. | include a balancing measure
accreditation evidence | Material supporting assessment against relevant accreditation requirements. | organize accreditation evidence
tracer review | Examination following a process or experience across relevant steps and records. | prepare for a tracer review''',
    precision='No clinical harm reported is a statement about known impact, not proof that the process is reliable. A successful second check is evidence of detection in this event. The review still needs to understand the earlier failure and whether the control works consistently.',
    precision_extra='Root cause analysis is often shortened to RCA. A completed action and an effective action are different claims. Attendance at a refresher session shows participation; a defined follow-up measure is needed to evaluate whether the relevant process actually improved.',
    phrases='''State the event | The patient was booked into the wrong specialty clinic.
Report the interception | A second check caught the error before the appointment.
Limit the impact claim | No clinical harm has been reported in the available information.
Keep cause open | The cause has not yet been established.
Request the sequence | Let us reconstruct the booking steps from the records.
Avoid premature blame | We should not label this a training failure without evidence.
Value the detection | The second check worked in this event; we still need to examine the earlier steps.
Connect the action | Which verified contributing factor does this proposed action address?
Assign accountability | Each action needs an owner and completion date.
Define effectiveness | What measure would show that the relevant error risk has decreased?
Separate completion | A completed session does not itself demonstrate improved performance.
Preserve the record | Keep the original booking history and the documented correction.
Prepare the evidence | Show the event, response, implementation, and follow-up findings.
Monitor side effects | Check whether the change introduces delays or new workarounds.
Avoid a guarantee | One intercepted event does not prove that recurrence is impossible.
Close the review | Record supported findings and unresolved questions separately.''',
    notes='''No harm reported | This preserves the information boundary without minimizing the event.
Cause versus factor | Several interacting conditions may contribute; avoid forcing an unsupported single explanation.
Detected versus prevented | Catching an error after it occurs differs from preventing the initial error.
Complete versus effective | Task completion needs separate evidence from improved outcomes.
Accreditation | An upcoming review does not justify overstating what the evidence shows.
Learning and accountability | A systems approach does not mean that responsibilities disappear.''',
    d='''Which review opening is most precise? | The wrong-specialty booking was intercepted; we will reconstruct the sequence and assess contributing factors. | The scheduler needs training because all booking errors have that cause. | No review is needed because no harm was reported. | The second check guarantees that this process is safe in every case. | The opening states known facts and a defensible investigation purpose without assuming cause or perfect protection.
What does refresher attendance demonstrate? | That the recorded participants attended, not necessarily that the process improved | That recurrence risk is now zero | That the original event was definitely caused by poor training | That every accreditation requirement has been satisfied | Attendance is implementation evidence; effectiveness requires a relevant measure of the intended improvement.
Which measure most directly tests whether wrong-specialty booking accuracy improved? | Verified wrong-specialty bookings divided by comparable reviewed bookings over the planned period | Staff attending the refresher divided by staff scheduled for it | Completed action-plan tasks divided by tasks assigned | Refresher slides approved divided by slides submitted for review | A consistently defined booking-error rate measures the intended process result. Attendance and task completion provide implementation evidence, not evidence that the booking process became more accurate.
Why include a balancing measure? | To detect unintended effects such as added delays or workarounds | To replace the main effectiveness question | To ensure every result can be described as successful | To avoid recording the original error | A change can improve one aspect while harming another, so monitoring side effects supports a fuller assessment.''',
    dialogue='''Ben | The patient was booked into the wrong specialty, but the second check caught it before the appointment. Can we close the issue as a harmless administrative mistake?
Asha | We should report the [[near miss::The near miss was intercepted before reported clinical harm, but still warrants the applicable reporting and learning process.]] through our process. No clinical harm is reported, but that does not explain the error or establish that the same process will always catch it.
Ben | The referral record and booking history are available. We can identify the sequence without relying only on what people remember after the correction.
Asha | Build the [[event chronology::The event chronology reconstructs the verified sequence rather than substituting an assumed explanation.]] from those records and relevant accounts. Keep confirmed facts distinct from assumptions, especially where the timing or handoff is unclear.
Ben | The immediate suggestion is a refresher session for schedulers. That may help, but we have not established that missing knowledge caused this event.
Asha | Identify the [[contributing factors::Contributing factors are supported conditions that helped the event occur; lack of training has not yet been established.]] first. The interface, referral wording, workflow, or other conditions may need examination. We should not select a cause merely because the proposed action is easy to organize.
Ben | We can thank the person who noticed the mismatch. At the same time, the review should not stop with the fact that the second check worked.
Asha | Exactly. It was a [[detection control::The detection control identified an error already made; it is different from preventing the initial wrong booking.]] in this event. We need to examine the earlier steps and whether the check operates reliably, rather than assuming one successful catch proves universal protection.
Ben | A simple diagram of the referral-to-booking route may help the teams see where information changed or responsibility became unclear.
Asha | Use a [[process map::The process map shows workflow steps and handoffs, helping locate where the error could enter or escape.]] grounded in actual practice. Include the handoffs and workarounds people really use, not just the ideal sequence written in the procedure.
Ben | Staff are worried this meeting will start by naming someone to blame. How do we get an honest account of the workarounds without losing accountability?
Asha | A [[just culture::A just culture combines learning about system conditions with fair accountability rather than automatic blame or absence of responsibility.]] supports both learning and fair accountability. Ask what happened and why the process allowed it, while preserving the responsibilities appropriate to each role.
Ben | Once the findings are supported, the action plan should show who will do what. A general instruction to improve accuracy will not be easy to follow up.
Asha | Name an [[action owner::The action owner is accountable for a defined task; a general aspiration does not assign responsibility.]] and a date for each specific task. Connect each action to the relevant finding so the plan is more than a list of familiar training activities.
Ben | For the accreditation discussion, we can show that an action was completed. But completion alone will not tell us whether it reduced the error risk.
Asha | Separate [[implementation evidence::Implementation evidence shows an action occurred, while effectiveness requires evidence about its result.]] from effectiveness evidence. A revised form or attendance record proves an activity occurred; it does not automatically prove that bookings became more accurate.
Ben | We could review a consistently defined sample of bookings afterward. The measure and review period should be agreed before we decide whether the change worked.
Asha | That provides an [[effectiveness measure::The effectiveness measure tests the intended improvement using a defined, relevant comparison rather than task completion alone.]]. Also monitor unintended consequences, such as delays or new workarounds, so an apparent improvement in one measure does not hide another problem.
Ben | I will prepare the timeline and mark the open questions. We can show what caught the error without claiming that we have already established its cause.
Asha | Good. The [[accreditation evidence::Accreditation evidence should accurately show the event, investigation, actions, and follow-up, without overstating completion or effectiveness.]] should reflect the actual state of the work. A clear account of an open investigation is more accurate than a completed-looking story unsupported by the records.''',
    transfer_title='Attendance is not effectiveness',
    transfer_setup='A refresher session has been delivered to all ten scheduled staff. No post-session booking review has yet occurred. The action plan calls for a four-week review of booking accuracy.',
    transfer='''Lead: "The session has been ___." | delivered | The briefing confirms completion of the session for the scheduled staff.
Reviewer: "Attendance supplies implementation ___." | evidence | Attendance demonstrates that the activity occurred, not that its intended effect has been achieved.
Lead: "Effectiveness remains ___." | untested | No post-session accuracy review has occurred, so the result has not been evaluated.
Reviewer: "Complete the planned four-week ___." | review | The action plan specifies a follow-up review of booking accuracy as the next evidence-gathering step.''', rehearsal=["Check the answers and read the booking-error review. State the intercepted wrong-specialty booking without claiming a proven cause or absence of all risk.","Switch roles for the action discussion. Contrast refresher attendance with a defined measure of booking accuracy; preserve the original event record.","Complete and check the ten-person training exchange. Read the session as delivered and effectiveness as untested until the planned four-week review."]))


BOOK['units'].append(unit(
    title='HIPAA, Privacy, and Information Governance',
    scene='A full patient list for a counting task',
    skill='Clarify a data request and apply the appropriate privacy review without turning a limited task into unnecessary disclosure.',
    brief='An operations colleague wants to count last month\'s missed appointments by clinic. The request asks for every patient\'s name, date of birth, diagnosis, and full visit notes. A clinic-level count may meet the stated purpose, but neither the appropriate data scope nor the requester\'s export permission has been confirmed. This is an administrative reporting task, not a provider-to-provider treatment request. Analyst Omar and privacy colleague Nina must confirm the purpose, access, output, and approved sharing route before any extract is sent.',
    cast='Omar | Reporting analyst\nNina | Privacy colleague',
    culture=('Clarify the purpose before choosing the fields', 'A privacy question need not sound obstructive. Explain that the requested output should match the task and ask which decision the data must support. Avoid treating internal status, removal of names, or technical access as sufficient evidence that an extract is appropriate. Use the designated privacy process for uncertainty.'),
    a='''What is the stated purpose? | Count missed appointments by clinic for last month | Review individual treatment decisions between providers | Publish full clinical notes for public use | Change every patient's clinical priority | The brief describes a limited administrative count, not treatment review or publication of identifiable records.
What remains unconfirmed? | Appropriate data scope and export permission | Whether a full patient list has been requested | Whether the reporting period is last month | Whether the task concerns missed appointments | The purpose and requested fields are supplied, but scope and export authority still require confirmation.
Which output may meet the stated purpose? | A suitably reviewed clinic-level count | Full visit notes for every patient by default | A diagnosis list with names removed and no further review | Any extract the analyst can technically download | A clinic-level count may answer the reporting question, subject to the applicable privacy and disclosure review.''',
    vocabulary='''HIPAA | US Health Insurance Portability and Accountability Act; includes relevant privacy and security provisions. | follow applicable HIPAA requirements
protected health information | Identifiable health information covered by the applicable HIPAA definitions. | safeguard protected health information
electronic PHI | Protected health information maintained or transmitted electronically. | protect electronic PHI
covered entity | A health plan, clearinghouse, or qualifying provider covered by HIPAA. | identify the covered entity
business associate | A party handling PHI for specified functions on a covered entity's behalf. | assess business-associate responsibilities
business associate agreement | A contract setting relevant duties for a business associate handling PHI. | verify the business associate agreement
minimum necessary | Reasonable limitation of information to the purpose where the applicable standard applies. | apply the minimum-necessary standard
permitted use | A use allowed under the applicable legal and organizational basis. | verify the permitted use
disclosure | Release or access to information outside the entity holding it in the relevant privacy context. | assess the proposed disclosure
authorization | A specific permission meeting applicable requirements for a defined use or disclosure. | verify the authorization
role-based access | Access assigned according to work responsibilities. | enforce role-based access
access entitlement | The permission assigned to a user for defined information or functions. | review access entitlements
export permission | Authority to extract information from a system under the relevant controls. | confirm export permission
purpose limitation | Restricting information handling to a specified appropriate purpose. | document the purpose limitation
data minimization | Limiting collected or shared data to what is appropriate for the task. | practice data minimization
aggregate report | A report combining individual records into group-level results. | review an aggregate report
de-identification | A process meeting applicable criteria for removing or reducing identification risk. | verify de-identification
re-identification risk | The possibility that information can be linked back to a person. | assess re-identification risk
small-cell disclosure | Identification risk arising from very small groups in reported data. | assess small-cell disclosure risk
secure transfer | Sharing through an approved protected method. | use an approved secure transfer
recipient verification | Confirmation of the intended recipient's identity and authority. | complete recipient verification
retention schedule | Rules specifying how long records are kept and when they are disposed of. | follow the retention schedule
audit log | A record of system access or activity used for review. | review the audit log
privacy incident | An event involving possible inappropriate handling of protected information. | report a suspected privacy incident''',
    precision='The US minimum-necessary standard has exceptions, including disclosures to or requests by health-care providers for treatment. This case concerns administrative reporting, not that treatment exception. Confirm the applicable basis and organizational policy rather than applying one slogan to every information request.',
    precision_extra='PHI means protected health information; ePHI is its electronic form; BAA means business associate agreement. Removing names alone does not establish de-identification. Aggregate outputs can also create identification risk through small groups or linked information, so review the proposed output appropriately.',
    phrases='''Clarify the purpose | Which decision requires this information, and what output is needed?
Match the scope | A clinic-level count may answer the stated question.
Challenge excess fields | Why would this counting task require full clinical notes?
Confirm the role | Please verify the requester's relevant access and export permissions.
Separate capability | Being able to download a file does not establish permission to share it.
Identify the context | This is administrative reporting, not a treatment disclosure request.
Apply the right rule | Check the applicable privacy basis and any relevant exceptions.
Avoid a false shortcut | Removing names alone does not make the extract de-identified.
Review group risk | Small counts may still reveal information about individuals.
Verify the recipient | Confirm identity, authority, and the intended destination.
Use the approved route | Share only through the authorized protected channel.
Keep a record | Document the purpose, approved scope, and handling decision.
Consult the owner | Route unresolved privacy questions to the designated reviewer.
Limit onward use | The output should not be repurposed beyond its authorized context.
Do not send yet | Scope and permission are unconfirmed, so the extract remains unsent.
Close the request | Confirm the approved output and record that the recipient received it appropriately.''',
    notes='''Internal | Internal employment does not automatically justify access to every patient record.
Can versus may | Technical capability and authorized use are different.
Minimum necessary | State where the standard applies; do not erase its exceptions.
Anonymous | Do not use this label merely because a name column was deleted.
Aggregate | Group-level data still need review for identification risk.
Consent versus authorization | Use the precise applicable term rather than assuming all forms of permission are interchangeable.''',
    d='''Which proposed output best matches the stated reporting purpose, subject to privacy review? | Clinic-level monthly missed-appointment counts with appropriate small-group checks | Patient names and diagnoses with visit notes omitted but no purpose review | Full notes with names removed and the result labeled anonymous | Every field visible to the analyst because the requester is an employee | The purpose is counting missed appointments by clinic, not reviewing individuals' diagnoses. Aggregation may meet it, but output scope, permissions, and identification risk still need review.
What does technical download access establish? | That the system permits the action technically, not that the proposed sharing is authorized | That every external destination is approved | That the requester needs all available fields | That privacy review is unnecessary for all exports | System capability does not settle purpose, permission, recipient, or sharing conditions.
Which statement about the treatment exception is accurate? | Provider treatment disclosures and requests have an exception to minimum necessary; this case is administrative reporting. | Every task performed in a hospital is automatically a treatment disclosure. | The exception means all workforce members may export every record. | The standard has no exceptions under HIPAA. | The exception is context-specific and does not convert this limited administrative task into a treatment request.
Why review an aggregate report? | Small groups or combined information may still allow identification. | All aggregate reports are automatically prohibited. | Counts always contain full medical notes. | Removing names guarantees that no identification is possible. | Aggregation can reduce exposure but does not automatically eliminate identification risk in every output.''',
    dialogue='''Omar | Operations wants last month's missed appointments by clinic. The request asks for names, dates of birth, diagnoses, and full visit notes. That seems broader than the question.
Nina | Clarify the [[permitted use::The permitted use must match an appropriate purpose and basis; the limited counting task does not itself justify every requested field.]] and the intended output first. We should understand the decision they need to make before choosing fields from the patient record.
Omar | A count for each clinic may answer the question. I do not see why the report would need individual clinical notes.
Nina | Propose an [[aggregate report::An aggregate report combines records into clinic-level counts that may satisfy the stated purpose with less individual information.]] for review. It may meet the purpose without individual details, but we should still assess the output and its disclosure risks.
Omar | The colleague works in operations and can view some records in the system. That does not tell me whether they can receive a broad export.
Nina | Check [[role-based access::Role-based access ties permissions to work responsibilities; internal employment does not establish unrestricted access.]] and the specific permissions. A legitimate role can require some information without authorizing every field or every way of transferring it.
Omar | My reporting account can technically download the full table. I should not treat the availability of an export button as approval for this request.
Nina | Exactly. Confirm [[export permission::Export permission is authority to extract information under the applicable controls, distinct from technical download capability.]] and the proposed recipient. Technical capability does not settle the purpose, scope, or appropriate destination of the information.
Omar | This is an administrative reporting task. It is not a request between providers to support treatment of an individual patient.
Nina | That distinction matters for [[minimum necessary::Minimum necessary limits information where the standard applies; the provider-treatment exception does not describe this administrative task.]]. The US standard has exceptions, including provider treatment disclosures and requests. We should apply the actual rule and policy to this context, not an oversimplified slogan.
Omar | Would removing the name column be enough? The export would still contain dates of birth, diagnoses, and free-text visit notes.
Nina | That is not established [[de-identification::De-identification requires meeting applicable criteria; deleting names while retaining identifying details is not enough.]]. Removing one identifier does not prove the extract meets the relevant criteria or eliminates the possibility of linking information back to an individual.
Omar | Even clinic counts could be revealing if a group is very small or the recipient can combine the report with other information.
Nina | Review [[re-identification risk::Re-identification risk includes linking small groups or combined information to individuals, even in an aggregate report.]] before release. Appropriate aggregation or other controls may be needed, depending on the purpose, context, and applicable review process.
Omar | Once the output is approved, I will verify the recipient and use our designated channel. I will not attach it to an unapproved personal message.
Nina | Use an approved [[secure transfer::Secure transfer uses the authorized protected channel, but does not replace the need for an appropriate purpose and recipient.]] method and confirm the destination. Security of the channel matters, but it does not make an excessive or unauthorized disclosure acceptable.
Omar | I will document the purpose, approved fields or counts, and the decision. That will help prevent a later request from silently expanding the same report.
Nina | Preserve the relevant [[audit log::The audit log records access or activity and supports review of how information was handled.]] and request records under the retention process. The output should remain connected to its authorized purpose rather than becoming an unrestricted reusable patient list.
Omar | I will hold the extract and ask whether clinic-level counts answer the question. Please review the scope and recipient before we send anything.
Nina | Good. Complete [[recipient verification::Recipient verification confirms identity and authority before information is shared through the approved route.]] and scope review before sharing. We can support the operational question without assuming that more personal information produces a better report.''',
    transfer_title='An export button is not permission',
    transfer_setup='An analyst can download a patient table. The requester needs monthly clinic counts, but the requested export includes diagnoses. Recipient authority and output scope are not yet verified.',
    transfer='''Analyst: "The button shows technical ___." | capability | The system allows an action technically, but that alone does not establish authorization.
Reviewer: "The report's approved scope is ___." | unconfirmed | The briefing says output scope has not yet been verified.
Analyst: "Clinic-level counts may meet the stated ___." | purpose | The operational request concerns monthly counts, which may not require individual diagnoses.
Reviewer: "Complete recipient and scope checks before ___." | sharing | Authority and scope remain unresolved, so the information should not yet be sent.''', rehearsal=["Check the cloze key, then read the data-request discussion. Keep the purpose limited to last month's missed appointments by clinic.","Switch roles for the proposed output. Distinguish a reviewed aggregate count, export permission, and a protected sharing route; do not call name removal de-identification.","Complete and check the export-button exchange. Keep technical capability separate from authority, with scope and recipient checks unfinished."]))

BOOK['units'].append(unit(
    title='Patient Experience and Service Recovery',
    scene='Two calls, still no clear answer',
    skill='Acknowledge a communication failure, offer an accountable next step, and avoid making a clinical promise.',
    brief='Patient Leah has called twice to ask when a clinician will discuss a test result. The required identity checks for this call are complete. The call record confirms both messages, but no clinician callback time is confirmed. Leah says this call concerns the missing response, not a current urgent symptom. Administrator Arun can trace the messages, contact the clinical team, and promise his own status update by 3 p.m. He cannot interpret the result, assure Leah that it is normal, or promise a clinical callback at a time the team has not agreed.',
    cast='Leah | Patient\nArun | Administrator',
    culture=('Acknowledge the experience before explaining the process', 'A patient who has already called twice needs recognition and a dependable next step, not another unexplained transfer. State what you can personally do and when you will update them. Keep empathy separate from unsupported reassurance about a result or a clinical decision outside your role.'),
    a='''What can Arun verify? | Both earlier messages appear in the call record. | The result is normal. | A clinician will definitely call at 3 p.m. | Leah has received a clinical explanation. | The call record confirms the messages, but no clinical interpretation or clinician callback time is supplied.
What can Arun promise? | His own status update by 3 p.m. | A diagnosis during this administrative call | A clinician callback at an unagreed time | That no further clinical follow-up is needed | Arun controls his administrative update, not the clinical team's timing or judgment.
What does Leah say about the present call? | It concerns the missing response, not a current urgent symptom. | She is reporting a confirmed medical emergency. | She wants the administrator to prescribe treatment. | She has already spoken with the clinician about the result. | The brief explicitly defines this as a communication-delay call and does not provide a current urgent symptom.''',
    vocabulary='''patient experience | The interactions a patient has with the health-care system. | improve patient experience
service recovery | Actions addressing a service failure and its effects on the person affected. | initiate service recovery
acknowledgment | Recognition of a person's concern or the facts of a situation. | offer a specific acknowledgment
empathy statement | Language recognizing another person's experience or difficulty. | use an appropriate empathy statement
communication delay | A gap between needed or expected communication and its occurrence. | investigate a communication delay
call history | The recorded sequence of telephone contacts and messages. | review the call history
contact attempt | An effort to reach a person through a communication channel. | document each contact attempt
callback window | An agreed period during which a return call is expected. | confirm the callback window
status update | Information about the current state of an unresolved matter. | provide a status update
resolution commitment | A promise to deliver a specified outcome. | distinguish an update from a resolution commitment
clinical interpretation | Qualified explanation of medical findings and their meaning. | route for clinical interpretation
scope of role | The responsibilities and limits of a person's position. | stay within the scope of role
warm transfer | A handoff connecting the person with the next team while conveying relevant context. | arrange a warm transfer
named owner | An identified person accountable for a follow-up action. | assign a named owner
handoff acceptance | Confirmation that the receiving person or team accepts responsibility for the specified task. | verify handoff acceptance
contact preference | A person's preferred appropriate method or timing of communication. | confirm the contact preference
identity verification | Checking that the person is who they claim to be under the relevant process. | complete identity verification
plain language | Wording intended to be readily understood by the audience. | use plain language
complaint | An expression of dissatisfaction requiring the applicable response. | document a complaint
grievance pathway | The designated process for formally reviewing specified patient concerns. | explain the grievance pathway
de-escalation | Communication intended to reduce tension and support a constructive exchange. | use respectful de-escalation
expectation setting | Clarifying what will happen, what is uncertain, and who is responsible. | improve expectation setting
follow-through | Completion of the action or update that was promised. | demonstrate follow-through
closure confirmation | Checking that the relevant follow-up or resolution has actually occurred. | seek closure confirmation''',
    precision='An apology for a communication delay does not require interpreting the test result. A status update promises information about progress, not a clinical conclusion. Explain the difference in ordinary language, particularly when the patient has already waited through earlier unsuccessful contacts.',
    precision_extra='Administrative staff should use the appropriate clinical route when a clinical concern arises. This case states that Leah is calling about delayed communication, not a current urgent symptom. A promised administrative update must not become a reason to delay appropriate urgent attention in a different situation.',
    phrases='''Acknowledge the history | I can see both earlier messages in the record.
Recognize the impact | I understand why having to call again is frustrating.
Apologize specifically | I am sorry you have not received a clear update.
State your action | I will trace the messages and contact the clinical team.
Set a controlled promise | I will update you myself by 3 p.m.
Separate the timing | That is my update time, not yet a confirmed clinician callback time.
Respect the role | I cannot interpret the result, but I can help get your question to the clinical team.
Avoid unsupported reassurance | I do not have a basis to tell you the result is normal.
Keep ownership | You should not have to restart the same explanation at each transfer.
Confirm the channel | Let us check the appropriate contact method on your record.
Explain a handoff | I will pass along the earlier call history and confirm that the team received it.
Use plain language | I am checking who will respond and when, rather than simply moving your message.
Offer the process | I can explain the patient-concern process if you want the delay formally reviewed.
Update even when pending | I will contact you at the agreed time even if the clinical response is still unconfirmed.
Read back the plan | I will contact the team now and update you by three.
Confirm closure | We will check that the promised follow-up actually occurred.''',
    notes='''I understand | Connect empathy to the actual difficulty rather than using a stock phrase alone.
I will versus they will | Promise your own action; verify another team's commitment before promising theirs.
Normal | Do not infer a clinical result from silence, timing, or administrative status.
Transferred | A transfer is not complete merely because a message was forwarded.
Complaint versus grievance | Follow the organization's applicable definitions and process rather than assigning labels casually.
Update versus resolution | Make clear which outcome is promised and which remains dependent on further action.''',
    d='''Which opening best addresses Leah's experience? | I can see both messages, and I am sorry you have had to call again without a clear update. | The system has a queue, so there is nothing to discuss. | No call probably means the result is normal. | You should assume the clinician will call today. | The opening acknowledges the documented history and frustration without unsupported clinical or timing reassurance.
Which promise can Arun make without committing another team? | I will update you by three, even if the clinician's callback time is still unconfirmed. | The clinical team will explain the result by three because I have forwarded the request. | I will close the complaint by three as soon as the clinical team acknowledges receipt. | The result will be ready for explanation by three if no further messages arrive. | Arun controls his own status call. Forwarding, receipt, and silence do not establish a clinician's agreed time, completed result review, or resolution of the complaint.
Leah asks whether silence means the result is normal. What should Arun say? | I cannot infer that or interpret the result; I will route the question to the clinical team. | Yes, silence reliably means normal. | The length of the delay determines the diagnosis. | A booking administrator can confirm normality from the call log. | Administrative silence and call records do not establish a clinical interpretation.
What closes the administrative handoff? | Confirm that a clinical team member accepts the follow-up and keep the promised patient update. | Mark the task complete immediately after forwarding a message. | Remove the earlier contacts so only the latest call remains. | Promise a new clinician time without checking it. | Explicit acceptance assigns the clinical follow-up, while Arun retains his promised patient update. Merely forwarding or receiving a message does not establish responsibility.''',
    dialogue='''Leah | This is my third call about the result. I have answered the identity questions again, but I still do not know who will call me.
Arun | I can see both earlier messages in the [[call history::The call history confirms Leah's earlier contacts, so Arun can acknowledge them without asking her to prove she called.]]. I am sorry you have had to call again. I will trace where those messages went.
Leah | This is about the missing response, not a new urgent symptom. Last time I was told the message had been passed on.
Arun | That [[communication delay::The communication delay is the unresolved response gap; acknowledging it does not require interpreting the medical result.]] needs follow-up, not another unexplained transfer. I will contact the clinical team and check who is taking responsibility for your question.
Leah | Does no call mean the result is normal? I keep trying to work out whether the silence tells me anything.
Arun | I cannot give that [[clinical interpretation::Clinical interpretation requires qualified medical judgment; silence and call records do not establish that a result is normal.]]. A missing callback does not tell me what the result means. The qualified clinical team needs to explain it.
Leah | What can you actually promise? I cannot keep waiting beside my phone without knowing whether anyone is dealing with this.
Arun | I will give you a [[status update::The status update is Arun's controlled commitment to report progress, not a promise of a completed clinical discussion.]] myself by three today. I will tell you what the team has confirmed and what is still outstanding.
Leah | So should I keep three o'clock free for the clinician? I do not want to miss the explanation if that is the time.
Arun | We do not have a clinician's [[callback window::A callback window must be agreed by the responding team; Arun's update time is not an established clinician appointment.]] yet. Three is my update time; I will not describe it as a medical appointment that has not been agreed.
Leah | Please do not make me explain the first two calls to another person. They are already in the record.
Arun | I will include that history and seek [[handoff acceptance::Handoff acceptance confirms that the receiving person or team accepts responsibility for the follow-up; sending or receiving a message alone does not establish that.]], so a responsible team member accepts the follow-up. Forwarding your message alone is not enough.
Leah | Use the contact method already on my record. I do not want details sent to a different number during another handover.
Arun | I will confirm that [[contact preference::The contact preference identifies the agreed communication method and should be checked under the usual verification process.]] through our usual checks. We will use the agreed route rather than assume a new destination is acceptable.
Leah | I also want the delay reviewed. Will raising a complaint distract from getting the result explained?
Arun | Those can proceed separately. I can explain the [[grievance pathway::The grievance pathway provides the appropriate formal route for the concern, separate from clinical interpretation of the result.]] for the communication concern while continuing to seek the clinical response.
Leah | And if you have not got a clinician's time by three? That is usually when the promised update disappears.
Arun | I will still call. That [[follow-through::Follow-through means honoring the promised update even when the underlying clinical response remains unresolved.]] is my responsibility. You will hear the actual status and next action, even if the clinical timing remains unresolved.
Leah | All right. Include the earlier messages, find out who is handling it, and contact me by three whether or not the time is confirmed.
Arun | I will remain the [[named owner::The named owner is the identified person accountable for this administrative follow-up, not a substitute for the clinician's medical role.]] for this administrative follow-up. The clinical team explains the result; I will keep the communication commitment we have agreed.''',
    transfer_title='Keep the promised update',
    transfer_setup='At 3 p.m., the clinical team has acknowledged the request but has not confirmed a callback time. The administrator promised a status update at 3 p.m.',
    transfer='''Administrator: "The clinical team has ___ the request." | acknowledged | Receipt has been confirmed, so that limited status can be reported accurately.
Patient: "Is the callback time confirmed?" Administrator: "It is still ___." | unconfirmed | The briefing explicitly says no clinical callback time has been agreed.
Administrator: "This call honors my promised ___." | update | The administrator promised a status update at three, not a completed medical discussion.
Patient: "Does receipt establish a result?" Administrator: "No clinical ___ follows from receipt alone." | interpretation | Acknowledging a message does not establish what the test result means.''', rehearsal=["Check the answers and read Leah's call with patient frustration and a calm, specific acknowledgment. Do not interpret the test result from the delay.","Switch roles for turns 9-20. Distinguish Arun's three-o'clock update from an unconfirmed clinician callback and seek explicit acceptance of clinical follow-up.","Complete and check the three-o'clock exchange. Report acknowledgment accurately while preserving the unconfirmed callback time and lack of clinical interpretation."]))


BOOK['units'].append(unit(
    title='Population Health and Care Coordination',
    scene='Transport pending, but whose next action?',
    skill='Hand over unresolved care-transition tasks with verified status, ownership, and a clear escalation condition.',
    brief='Outgoing coordinator Rachel hands over a discharge coordination case to Imran. The note says transport pending. The transport service has acknowledged the request but has not assigned a vehicle or pickup time. A home-health referral has been received, but its first visit is unconfirmed. Rachel will finish her shift at noon. Imran is to confirm responsibility for both follow-ups and give the care team a status update at 2 p.m. Clinical discharge readiness remains for the qualified team to decide; the administrative handoff does not authorize departure.',
    cast='Rachel | Outgoing coordinator\nImran | Incoming coordinator',
    culture=('Pending needs a noun, an owner, and a next check', 'A short note is useful only when the next person can act on it. Explain what is awaiting confirmation, who holds the next action, and when a response is needed. Repeat the agreed responsibilities so that a shift change does not turn an active request into an unowned task.'),
    a='''What has the transport service confirmed? | Receipt of the request only | A vehicle and pickup time | Completion of the journey | Clinical discharge readiness | Acknowledgment confirms receipt, while vehicle assignment and pickup time remain unconfirmed.
What is the home-health status? | The referral was received; the first visit is unconfirmed. | A first visit is booked at noon. | The service has already visited the patient. | The transport provider has accepted clinical responsibility. | The briefing separates receipt of the referral from confirmation of a first visit.
What does the 2 p.m. commitment mean? | Imran will give the care team a status update. | The patient is authorized to depart at two. | A vehicle is guaranteed to arrive at two. | The home-health visit is confirmed for two. | The stated commitment is communication at a set time, not transport, a visit, or a clinical discharge decision.''',
    vocabulary='''population health | Work addressing health outcomes and needs across a defined group. | define the population-health cohort
care coordination | Organization of activities and information across people involved in a person's care. | strengthen care coordination
transition of care | Movement between care settings, providers, or stages. | support a transition of care
discharge coordination | Organization of practical arrangements related to leaving a care setting. | document discharge coordination
care plan | The agreed account of needs, goals, and responsibilities for care. | communicate the care plan
care gap | A difference between needed or planned care and care received. | identify a care gap
patient panel | A defined group of patients associated with a team or service. | review the patient panel
risk stratification | Grouping by assessed risk to support appropriate planning. | review risk-stratification criteria
social needs | Practical social circumstances affecting a person's ability to access or manage care. | assess reported social needs
transport barrier | A transport-related obstacle to reaching or leaving care. | resolve a transport barrier
non-emergency medical transport | Transport for medical access when emergency transport is not required, under applicable arrangements. | coordinate non-emergency medical transport
dispatch confirmation | Verification that the transport provider has made specified dispatch arrangements. | request dispatch confirmation
pickup window | The period during which a pickup is expected. | verify the pickup window
receiving provider | The professional or organization expected to take the next care role. | contact the receiving provider
home-health referral | A request for an appropriate service delivered in the home setting. | track a home-health referral
service acceptance | Confirmation that a receiving service will take the specified referral or task. | distinguish receipt from service acceptance
first-visit confirmation | Verification of the initial service visit's agreed arrangements. | obtain first-visit confirmation
medication reconciliation | Qualified comparison and clarification of medication information across care transitions. | route medication-reconciliation questions
follow-up appointment | A subsequent visit arranged for continued review or care. | verify the follow-up appointment
community resource | A local service supporting practical or health-related needs. | verify community-resource availability
handoff checklist | A structured aid for communicating required transition information. | complete the handoff checklist
closed-loop communication | An exchange including acknowledgment and confirmation of understanding. | use closed-loop communication
contingency plan | An agreed response if the expected arrangement cannot occur. | confirm the contingency plan
care-team update | A status communication to the relevant people coordinating care. | provide a care-team update''',
    precision='Request received, service accepted, vehicle assigned, and pickup confirmed describe different steps. Use the provider\'s actual response. A transport arrangement also does not establish clinical readiness for discharge; that decision remains with the qualified team under the relevant process.',
    precision_extra='A handoff should identify current status, open actions, ownership, and timing. SBAR means situation, background, assessment, and recommendation or request. Administrative use of a structured handoff does not authorize an administrator to make a clinical assessment outside their role.',
    phrases='''Clarify pending | Is transport awaiting acceptance, vehicle assignment, or a pickup time?
State the confirmed step | The provider acknowledged the request but has not assigned a vehicle.
Name the next owner | I will take responsibility for the transport follow-up after noon.
Separate the service | Home health received the referral; the first visit is not yet confirmed.
Set the check | I will update the care team at 2 p.m.
Avoid a departure promise | That update time is not authorization for the patient to leave.
Verify suitability | The relevant qualified team must confirm the required transport arrangements.
Check the next visit | Please confirm the receiving service's first-visit plan.
Preserve the distinction | Received does not necessarily mean accepted for service.
Escalate a barrier | If arrangements remain unresolved, use the agreed escalation route.
Record the response | Document the provider's exact status and the time of contact.
Confirm the fallback | What is the approved contingency if transport cannot be arranged?
Read back ownership | You are handing over both follow-ups, and I am accepting them.
Keep the patient informed | Share the confirmed practical arrangements through the appropriate care-team process.
Avoid duplicate work | Check the existing request before creating another transport booking.
Close the handoff | Record acknowledgment, next actions, and the next update time.''',
    notes='''Pending what | Name the exact step awaiting confirmation.
Received versus accepted | The receiving service may acknowledge a request before agreeing to provide care.
Pickup versus discharge | A transport time and clinical discharge authorization are different facts.
Owner after handoff | Responsibility must be explicitly accepted, not inferred from a copied email.
First visit | A referral alone does not establish when service begins.
Contingency | Use the approved alternative process rather than improvising a care arrangement.''',
    d='''Which handoff statement is most actionable? | Transport acknowledged the request; no vehicle or time is assigned; Imran owns follow-up and a 2 p.m. update. | Transport pending; someone should check later. | Transport is booked because the provider replied. | The patient can leave at two because an update is due. | The actionable statement contains confirmed status, unresolved steps, ownership, and timing.
Which next check goes beyond a home-health referral receipt? | Whether the service accepts responsibility and what first-visit arrangements are confirmed | Whether the sender saved a copy of the original referral email | Whether the referral title contains the expected service name | Whether transport has acknowledged its separate request | A received referral is not yet service acceptance or a confirmed first visit. The sending record and transport acknowledgment cannot establish the receiving service's commitment.
Which statement preserves the clinical boundary? | The qualified team determines discharge readiness; administrative coordination supports that decision. | A completed handoff authorizes departure in every case. | A vehicle assignment replaces the clinical discharge process. | An administrator can resolve all medication questions from a transport note. | Coordination communicates arrangements but does not transfer clinical decision authority to administrative staff.
What closes the ownership transfer? | Imran acknowledges the tasks and the agreed next actions are documented. | Rachel copies Imran on an email without confirming receipt. | The note is shortened to pending. | Both coordinators assume the other will call. | Explicit acceptance and documented next actions prevent responsibility from disappearing during the shift change.''',
    dialogue='''Rachel | Before I finish at noon, I need to hand over this discharge coordination case. The note says transport pending, but that wording leaves too much unclear.
Imran | Let us identify the [[transport barrier::The transport barrier is the unresolved practical arrangement, which must be specified rather than hidden under pending.]]. Has the provider received the request, accepted it, assigned a vehicle, or confirmed a pickup time? Those are different stages.
Rachel | The provider acknowledged receipt. No vehicle or pickup time has been assigned, so we should not describe the journey as booked.
Imran | I will request [[dispatch confirmation::Dispatch confirmation verifies actual transport arrangements; acknowledgment of a request alone does not provide it.]] through the existing request. I will check what remains unresolved instead of creating another booking and risking two competing requests.
Rachel | The home-health referral has also been received, but we do not have a confirmed first visit. It belongs on the handoff as a separate open item.
Imran | I will verify [[service acceptance::Service acceptance means the receiving service agrees to take the task; simple receipt does not establish that commitment.]] and the first-visit plan. The fact that a referral arrived does not tell the care team when the next service will begin.
Rachel | Good. Those arrangements support discharge planning, but neither of us should turn the administrative status into a decision about clinical readiness.
Imran | Agreed. The [[transition of care::A transition of care involves movement between care settings or stages and requires the appropriate clinical and practical coordination.]] remains coordinated with the qualified team. We will communicate the practical facts without substituting our judgment for the clinical discharge process.
Rachel | I will give you the request references and the last contact times. You should not have to reconstruct everything from a note that simply says pending.
Imran | I will use the [[handoff checklist::The handoff checklist helps preserve required status, references, open actions, and responsibilities during the transfer.]] to capture the open actions. Let us record the provider responses exactly and separate verified information from expected next steps.
Rachel | You will own both follow-ups after noon. I had planned a care-team update at two, even if the providers had not confirmed the arrangements by then.
Imran | I accept that responsibility and will give the [[care-team update::The care-team update is a promised status communication at 2 p.m., not a guaranteed pickup or clinical discharge time.]] at two. I will state what is confirmed, what remains open, and any escalation underway rather than wait silently for a complete answer.
Rachel | If transport is still unresolved, the team needs to know early enough to use the appropriate escalation route. We should not imply that two is a pickup time.
Imran | Correct. Any [[pickup window::A pickup window must come from confirmed transport arrangements; the administrative update time does not establish it.]] must come from the provider's actual arrangements. The update deadline is our communication commitment, not a transport guarantee.
Rachel | If this transport cannot be arranged, check the approved alternative with the team. Please do not book a different type before suitability and authority are confirmed.
Imran | I will confirm the [[contingency plan::The contingency plan is the approved response to an unresolved arrangement, not an improvised substitute for assessed transport needs.]] with the relevant team. Suitability and authorization must be established through the proper route before an alternative is reported as available.
Rachel | For home health, please distinguish a general acknowledgment from an actual start date. The receiving team and patient need an accurate expectation.
Imran | I will ask for [[first-visit confirmation::First-visit confirmation establishes the agreed initial service arrangement, which is not yet supplied by the referral receipt.]] and document the answer. If it is still unknown, I will retain that status and identify who is following up.
Rachel | Before I leave, read back the two follow-ups and the update time. I want to make sure neither task remains assigned to someone whose shift has ended.
Imran | I own transport and home-health follow-up after noon, with a two o'clock status update. That [[closed-loop communication::Closed-loop communication includes acknowledgment and confirmation of understanding, making responsibility explicit rather than assumed.]] confirms the tasks, not clinical readiness or departure. I will record the agreed actions and keep the care team informed.''',
    transfer_title='Acknowledged, not assigned',
    transfer_setup='A transport provider confirms receipt of a request but says no vehicle is assigned. The coordinator will check again at 1 p.m.; this is not a pickup promise.',
    transfer='''Coordinator: "The request was ___." | acknowledged | The provider confirmed receipt, which is the only completed transport step supplied.
Colleague: "A vehicle remains ___." | unassigned | The provider explicitly says no vehicle has been assigned.
Coordinator: "One o'clock is the next ___." | check | The coordinator promised another status check at one, not transport arrival.
Colleague: "Do not present it as a confirmed ___." | pickup | The briefing excludes a pickup promise and supplies no assigned vehicle.''', rehearsal=["Check the cloze key and read the shift handover. Separate acknowledged transport, no assigned vehicle, and the unconfirmed home-health visit.","Switch roles for turns 11-20. Make Imran's acceptance of both follow-ups explicit, with the two-o'clock care-team update unchanged.","Complete and check the transport exchange. Read one o'clock as the next check, not pickup, and do not let administrative arrangements authorize discharge."]))

BOOK['units'].append(unit(
    title='Executive Dashboards and Board Updates',
    scene='A shorter wait, or a different reporting window?',
    skill='Explain a performance change with comparable definitions and turn a dashboard into a bounded decision request.',
    brief='A board chart compares last month\'s median waiting time of 40 minutes across 200 visits with this week\'s median of 30 minutes across 50 visits. The clinic mix and measurement consistency have not been checked. The headline claims a proven 25% improvement caused by a staffing change. Analyst Jo and executive sponsor Malik must distinguish arithmetic from evidence of sustained improvement or causation. The proposed board request is approval of a four-week validation review, not a claim that staffing changes are already proven effective.',
    cast='Jo | Performance analyst\nMalik | Executive sponsor',
    culture=('Explain the comparison before celebrating the result', 'A numerical reduction can be real in the reported values while the operational conclusion remains uncertain. Name the periods, populations, and definitions. Then give decision-makers a specific next step, rather than using caveats either to conceal a weak claim or to avoid making any useful request.'),
    a='''What changed between the compared data sets? | The reporting period and visit count, with clinic mix still unchecked | Only the font used in the chart | Nothing; both use the same monthly population | The outcome from waiting time to revenue | One figure is monthly across 200 visits and the other weekly across 50, so comparability needs assessment.
What does 40 to 30 minutes establish arithmetically? | A ten-minute, 25% reduction between the reported medians | Proof that every patient's wait fell by ten minutes | Proof that the staffing change caused the reduction | A confirmed sustained improvement across comparable months | The arithmetic is correct, but it does not establish individual change, causation, or sustained comparable performance.
What decision is proposed? | Approve a four-week validation review | Declare the staffing change conclusively effective | Approve unlimited additional staffing | Eliminate measurement checks because the chart improved | The supplied request is a bounded review to validate the comparison, not an implementation or causal conclusion.''',
    vocabulary='''executive dashboard | A concise display of measures supporting leadership oversight and decisions. | review the executive dashboard
key performance indicator | A selected measure of important performance. | define the key performance indicator
metric definition | The specified calculation, population, and interpretation of a measure. | document the metric definition
reporting period | The time interval covered by a reported result. | align reporting periods
measurement window | The interval over which observations are collected for a measure. | keep the measurement window consistent
numerator | The quantity counted above the line in a defined ratio. | verify the numerator
denominator | The reference quantity used below the line in a defined ratio. | state the denominator
median | The middle ordered observation, or mean of the two middle observations for an even count. | report median waiting time
mean | The total of observed values divided by their number. | distinguish the mean from the median
percentile | A value indicating a specified position in an ordered distribution. | examine the ninetieth percentile
case mix | The composition of patients or cases with characteristics relevant to comparison. | assess case-mix differences
stratification | Separating data into defined groups for analysis. | use clinic-level stratification
data lineage | The traceable path from source data to a reported result. | verify data lineage
refresh date | The time a data display was last updated. | show the refresh date
completeness check | Assessment of whether expected records or fields are present. | perform a completeness check
like-for-like comparison | A comparison using sufficiently consistent populations, definitions, and periods. | build a like-for-like comparison
run chart | A time-ordered display of a measure used to examine patterns. | review the run chart
common-cause variation | Variation inherent in the current process under the relevant statistical model. | assess common-cause variation
special-cause variation | Variation associated with an identifiable change outside usual process behavior in context. | investigate potential special-cause variation
causal attribution | A conclusion that a specified factor produced an observed effect. | qualify causal attribution
relative change | A difference expressed as a proportion of the reference value. | calculate relative change
absolute change | The numerical difference in the original measurement units. | report absolute change
data-quality caveat | A stated limitation affecting confidence in a reported result. | retain a data-quality caveat
decision request | The specific action a decision-making body is asked to authorize. | state the decision request''',
    precision='The reported median fell by ten minutes, or 25% relative to forty. That arithmetic does not show that each patient waited ten minutes less. Nor does it establish a like-for-like trend or prove that a staffing change caused the difference.',
    precision_extra='KPI means key performance indicator. Median, mean, and percentile measures answer different questions. Keep the definition and time basis visible. A run chart can reveal patterns, but a chart alone does not establish causation or remove the need to check data quality.',
    phrases='''Describe the figures | The reported medians are forty minutes last month and thirty this week.
State the arithmetic | That is ten minutes lower, or 25% relative to forty.
Limit the conclusion | The comparison does not yet establish sustained improvement.
Name the changed basis | The periods and visit counts differ, and clinic mix is unchecked.
Check the definition | Are arrival and service-start times measured consistently?
Preserve the statistic | Both figures are medians; do not describe them as every patient's wait.
Request comparable data | Rebuild the comparison on aligned periods and definitions.
Separate association | The timing of the staffing change does not prove it caused the result.
Show the limitation | Place the comparability caveat beside the headline.
Verify the source | Trace the measure to its underlying records and calculation.
Look beyond one point | Review the time pattern rather than declaring a trend from two unmatched values.
State the ask | Approve a four-week review to validate the comparison.
Bound the authority | This request does not authorize unlimited staffing changes.
Name the owner | The performance team will own the validation and report-back.
Keep the finding useful | Report the observed values while marking the conclusion provisional.
Close with evidence | Return with comparable results, limitations, and the next decision needed.''',
    notes='''Twenty-five percent | This is relative to the forty-minute reference, not twenty-five percentage points.
Median | A change in a group median does not describe every individual's change.
After versus because of | Sequence in time is not sufficient causal evidence.
Comparable | Check definitions, periods, and population composition.
Provisional | Use the qualifier with the conclusion it limits, not only in an appendix.
Approve what | A board update should specify whether it seeks a decision or merely reports information.''',
    d='''Which headline accurately describes the observed 40-to-30-minute comparison? | Reported median is ten minutes lower; period, mix, and causal comparability remain under review. | Waiting times fell ten percentage points after the staffing change. | The typical patient is proven to wait 25% less because the newer sample is smaller. | Staffing delivered a sustained 25% improvement, with data validation to follow. | Ten minutes divided by forty is a 25% relative difference between medians, not percentage points. Different periods and unchecked clinic mix prevent the headline from establishing a sustained or staffing-caused improvement.
What is the relative reduction between the reported values? | 25% | 10% | 33.3% | 75% | Subtract thirty from forty and divide the ten-minute difference by the forty-minute reference value.
Which validation task is most relevant? | Align time periods, definitions, and clinic composition, then review the underlying data. | Replace the median with the smallest wait to strengthen the headline. | Remove the earlier month because it looks worse. | Assume fifty visits always represent the same mix as two hundred. | The proposed checks address the actual comparability gaps instead of selecting a more favorable number.
Which board request matches the brief? | Approve the four-week validation review and require a report-back on comparable results. | End the review because the arithmetic is correct. | Approve any future staffing plan without further evidence. | Treat the chart as a completed causal evaluation. | A bounded validation request addresses uncertainty without claiming proof or expanding the requested authority.''',
    dialogue='''Malik | The board chart says waiting time improved by twenty-five percent because of the staffing change. Before I use that headline, are the two figures comparable?
Jo | The [[reporting periods::The reporting periods differ: one result covers a month and the other a week.]] differ. Forty minutes is last month's median across two hundred visits; thirty is this week's median across fifty. We have not checked the clinic mix.
Malik | The arithmetic is still a ten-minute reduction, relative to forty. I want to preserve that fact without suggesting it answers every other question.
Jo | Yes. The [[relative change::The relative change is ten divided by forty, or 25%, without proving comparability or causation.]] is twenty-five percent between the reported values. That does not establish a sustained operational improvement or explain why the difference occurred.
Malik | We should also be careful with the word average. Both values are medians, and people may hear that every patient's wait fell by ten minutes.
Jo | Retain [[median::The median summarizes the middle of a group's ordered values; its change does not describe every individual's change.]] in the label. It is a group summary, not a statement about each person's experience. A different summary statistic could tell a different part of the story.
Malik | One clinic may have contributed a larger share of visits this week. If clinics have different waiting patterns, that could affect the combined result.
Jo | Check the [[case mix::Case mix describes the composition of visits; changes in clinic contribution may affect the overall comparison.]] and use appropriate clinic-level comparisons. We should not assume the smaller weekly sample has the same composition as the previous month's visits.
Malik | Do both extracts start the clock at the same event? Arrival and completed registration would give us different waiting intervals.
Jo | Exactly. Confirm the [[metric definition::The metric definition specifies what interval is measured and must remain consistent across the compared results.]] and trace the calculation. A familiar dashboard label does not prove that the underlying start and end events are identical.
Malik | Can the team reconstruct the data from source records? I want a repeatable calculation rather than a number copied between presentations.
Jo | We will verify [[data lineage::Data lineage traces the reported measure back to its sources and calculation so the result can be checked.]], completeness, and the refresh date. That should show what is included, what is missing, and whether the displayed figures reflect the intended periods.
Malik | The staffing change happened before this week's result, but other factors may have changed too. We should not equate timing with proof.
Jo | Correct. [[Causal attribution::Causal attribution claims that staffing produced the change; temporal sequence and two unmatched summaries do not establish that.]] needs more than these two values. We can describe the timing without presenting the staffing explanation as established.
Malik | A series over comparable periods would be more informative than selecting one month and one week. We should look at the broader pattern.
Jo | A [[run chart::A run chart displays a measure over time and can support pattern review, while not establishing causation by itself.]] on a consistent basis can help. It should support investigation of the pattern, not serve as a visual shortcut around checking definitions and context.
Malik | For the board, the immediate request is a four-week validation review. It is not a proposal for unlimited staffing changes or a declaration that the intervention succeeded.
Jo | Put that [[decision request::The decision request is approval of the bounded validation review, not a claim of proven staffing effectiveness.]] up front, with an owner and report-back. The directors should know what they are being asked to authorize before interpreting the chart.
Malik | I will remove the proven-improvement claim and ask for the four-week review. Put the comparability caveat beside the figures, where the board will see it.
Jo | Keep the [[data-quality caveat::The data-quality caveat makes the comparison limitations visible beside the reported finding rather than hiding them in supporting material.]] beside the finding. We can report the observed values honestly and still offer a practical next step that will make the next decision better informed.''',
    transfer_title='Minutes and percentages are different',
    transfer_setup="On an otherwise comparable basis in a separate exercise, median waiting time changes from 50 to 40 minutes. The figures alone do not identify the cause or every patient's experience.",
    transfer='''Analyst: "The absolute reduction is ___ minutes." | ten | Fifty minus forty equals ten minutes, expressed in the original units.
Reviewer: "Relative to fifty, the reduction is ___." | 20% | Divide the ten-minute reduction by the fifty-minute reference to obtain 20%.
Analyst: "These are group ___." | medians | The briefing specifies median waiting times, not each individual's change.
Reviewer: "The cause remains ___ from these figures alone." | unestablished | Even a comparable difference does not by itself identify the factor that caused it.''', rehearsal=["Check the answers, then read the board-chart review. Distinguish last month's 200 visits from this week's fifty before comparing their medians.","Switch roles for the conclusion. State ten minutes or 25% lower, with clinic mix, measurement consistency, and causation still unresolved.","Complete and check the separate 50-to-40-minute exchange. Read ten minutes and 20% as different expressions of the change, not individual patient outcomes."]))
