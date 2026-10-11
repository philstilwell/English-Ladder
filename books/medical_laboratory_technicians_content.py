"""Original Medical Laboratory Technician English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='medical-laboratory-technicians', title='Medical Laboratory Technician English',
    cover_label='ENGLISH FOR MEDICAL LABORATORY AND SPECIMEN-SUPPORT TEAMS',
    cover_title='Medical Laboratory\nTechnicians', cover_size=31,
    tagline='Clear records. Confirmed messages.',
    audience='For medical laboratory technicians and support staff communicating about identifiers, specimens, quality status, equipment, reports, and handovers.',
    map_intro='Eight laboratory conversations practice exact identifiers, recollection requests, release status, service coordination, realistic timing, report versions, critical notifications, and referral follow-up.',
    notes_title='Preserve the distinction that matters.',
    notes_intro='Laboratory language links records, people, and decisions. Similar accession numbers are not a verified match. An instrument finishing is not permission to release results. A delivered parcel is not proof that a referral laboratory accepted the individual specimen.',
    field_notes=[
        ('Verify before linking records', 'Read the reference precisely and follow the laboratory verification process before connecting a caller to case information. Do not correct an identifier by guessing which similar number was intended. Keep an unresolved mismatch explicit.', '"I need to verify the requested case before discussing its status."'),
        ('State operational status without diagnosis', 'Insufficient quantity concerns the specimen available for testing, not a low patient result. Quality review pending describes release status, not a clinical conclusion. Use the documented message and refer missing technical or clinical questions to the authorized role.', '"The lead documented insufficient quantity for Q6 and requested recollection through the clinic."'),
        ('Correct and confirm the whole message', 'When a spoken number is repeated incorrectly, interrupt the error clearly, restate the correct value with its unit, request the complete read-back, and confirm accuracy. Receipt and understanding must not be inferred from silence or a vague acknowledgment.', '"Correction: six point four millimoles per liter, not six point one. Please read back the complete result."'),
        ('Hand over ownership, not just a note', 'A pending referral enquiry needs a named recipient, the exact unresolved question, and the agreed update time. Distinguish parcel delivery from accession acceptance and an update commitment from a result promise.', '"Eli has accepted the X8 enquiry and the fifteen-hundred clinic update; no result date is confirmed."'),
    ],
    scope_note='All cases and local procedures are fictional. This is English practice, not medical advice or laboratory operating instruction. Follow applicable privacy rules, validated procedures, professional scope, and authorized escalation. No exercise authorizes specimen collection, testing, instrument operation, result release, diagnosis, or treatment. The critical designation in Unit 7 belongs only to fictional Lumen; it is not a universal threshold. Patient identity and recipient authority must be verified through actual local arrangements.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Clinical Laboratory Technologists and Technicians.',
             url='https://www.bls.gov/ooh/healthcare/clinical-laboratory-technologists-and-technicians.htm',
             note='Occupational context for specimen work, equipment, records, and communication. No salary forecasts or qualification advice are reproduced.', checked='10 October 2026'),
        dict(title='World Health Organization. Laboratory Quality Management System: Handbook, publication overview.',
             url='https://www.who.int/publications/i/item/9789241548274',
             note='Overview of laboratory quality-management scope. Fictional procedures and examples are original, not reproductions of the handbook or current accreditation rules.', checked='10 October 2026'),
        dict(title='Agency for Healthcare Research and Quality. Check-Back or Repeat-Back.',
             url='https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/checkback.html',
             note='Communication reference for recipient repetition and sender confirmation. The critical-result scenario supplies its own fictional value and local designation.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Accessioning and unambiguous identifiers',
    scene='A314 in the log, A341 in the request',
    skill='Resolve an accession-reference mismatch through the approved verification route without guessing identity or disclosing an unverified case.',
    brief="The receiving log lists accession A314. Clinic caller Mira asks technician Noor about A341. No identity match between the request and the logged case has been established. Noor can check the accession log, but Mira must identify the requested case through the laboratory's privacy and verification arrangements. Similar digits do not establish a transcription error or authorize disclosure. The discussion ends with verification still required, not with a claimed case match.",
    cast='Noor | Laboratory technician\nMira | Clinic caller',
    culture=('Slow down the identifier, not the standard', 'A caller may expect a quick answer because a reference looks nearly right. Be helpful by naming the verification step and repeating the supplied reference precisely. Do not offer another case as a likely match or let conversational confidence replace privacy checks.'),
    a='''Which accession appears in the receiving log? | A314 | A341 | Q6 | X8 | The briefing identifies A314 as the accession in the receiving log.
Which reference does the caller request? | A341 | A314 | H2 | T5 | Mira asks about A341, which differs from the logged A314.
What has been established about identity? | No match has been established | Both references definitely identify one patient | The clinic made a confirmed typo | Disclosure is automatically authorized | Similar digits do not establish a match, an error, or permission to disclose.''',
    vocabulary='''accession | Laboratory registration of a specimen or request under its identifier. | check the accession
accession number | Reference assigned to a registered laboratory case or specimen. | read the accession number
accession log | Record of registered laboratory items. | consult the accession log
receiving log | Record of items received by the laboratory. | check the receiving log
requisition | Request document specifying laboratory testing information. | review the requisition
patient identifier | Detail used under the approved process to identify a patient. | verify patient identifiers
specimen identifier | Reference linking a specimen to its record. | confirm the specimen identifier
case match | Established link between a request and the correct case. | establish the case match
identifier mismatch | Difference between references that should be reconciled. | report an identifier mismatch
transposed digits | Digits whose positions have been exchanged. | avoid assuming transposed digits
transcription error | Mistake made while copying information. | investigate a transcription error
verification | Check establishing required information under the applicable process. | complete verification
caller identity | Identity of the person making an enquiry. | verify caller identity
receiving authority | Permission for a person to receive particular information. | verify receiving authority
confidentiality | Protection of information from unauthorized disclosure. | maintain confidentiality
disclosure | Sharing information with a recipient. | authorize disclosure
minimum necessary information | Information limited to what the applicable purpose and rules require. | limit information sharing
secure channel | Approved communication route with relevant protection. | use a secure channel
laboratory information system | System managing laboratory records; abbreviated LIS. | consult the LIS
audit trail | Record showing actions and changes over time. | preserve the audit trail
source record | Original or authoritative record for the fact being checked. | consult the source record
unverified reference | Identifier not yet matched through the required checks. | retain the unverified reference
clarification request | Question seeking missing or inconsistent information. | raise a clarification request
identity resolution | Process of reconciling identifiers to the correct case. | complete identity resolution''',
    precision='A314 and A341 contain the same digits in a different order, but that resemblance does not prove they represent the same case. The log entry and caller request must remain distinct until the required verification establishes a match.',
    precision_extra='Do not disclose another accession as a suggested answer to an unverified caller. Repeat the reference the caller supplied, explain that verification is needed, and use the approved route for the necessary identifiers and authority checks.',
    phrases='''Repeat the request | You are asking about A341.
Read it clearly | That is A, three, four, one.
State the limit | I have not established a verified case match.
Avoid guessing | I cannot assume a digit transposition.
Name the next step | We need to follow the laboratory's verification process.
Protect other records | I cannot discuss another case as a possible match.
Request the approved route | Please use the required verification channel.
Separate checks | Caller identity and receiving authority both need the applicable checks.
Consult the record | I can check the accession log.
Avoid automatic correction | I will not change the reference to make it fit.
Keep the enquiry traceable | I will retain the reference exactly as supplied.
Explain the purpose | This helps ensure we discuss the correct case.
Avoid a result claim | No case-specific status has been confirmed in this exchange.
Request clarification | Please confirm the requested case through the approved arrangements.
Preserve uncertainty | The reference remains unverified.
Close precisely | Verification is still required before case details can be discussed.''',
    notes='''As supplied | Preserves the caller's actual reference rather than a guessed correction.
Have not established | States the missing verification without disclosing another case.
Cannot assume | Rejects a shortcut while leaving investigation possible.
Both | Separates identity from authority to receive information.
Before | Makes disclosure dependent on the required verification.
Still required | Prevents the conversation from being mistaken for a completed match.''',
    d='''Which response is appropriate before verification? | You asked about A341; please complete the required case verification | I found A314, so I will give you its details | The digits look similar, so this is the same patient | I will change the log to A341 | The appropriate response repeats the supplied reference and preserves the verification requirement.
What does the digit resemblance establish? | A possible mismatch requiring checking, not identity | A confirmed typo by the clinic | Automatic disclosure permission | A final result for A341 | Similar digits do not establish identity, responsibility for an error, or report status.
Which action preserves traceability? | Keep the supplied reference and document the unresolved enquiry | Replace the caller's number silently | Delete the enquiry because it is inconvenient | Combine both cases without review | Retaining the actual request prevents a guessed correction from obscuring the enquiry.
Which final status is accurate? | Identity verification remains required | The case match is complete | The other accession has been disclosed appropriately | A341 is confirmed absent from every system | The scenario ends without an established case match or broader search conclusion.''',
    dialogue='''Mira | I have A341 on our request. Could you check the case status? I'm calling from the clinic.
Noor | You are asking about A, three, four, one. I need to complete the required [[verification::Verification must establish the correct case and permitted recipient before Noor discusses case-specific information.]] before discussing case details, and I have not established a match yet.
Mira | I may have transposed two digits. Could you tell me which other reference looks closest?
Noor | That is helpful. A possible [[transcription error::Transcription error is only a possibility, not an established explanation for the difference between references.]] should be checked against the appropriate source rather than assumed. I will retain the number you actually supplied.
Mira | If you can search the log, why can't we just use the closest number and confirm it afterward?
Noor | I can consult the [[accession log::Accession log is the laboratory record Noor can check, without treating a similar entry as an authorized case match.]]. That does not replace the case and recipient checks required by our process, and I cannot offer another case as a likely answer.
Mira | Understood. I'll keep our request separate until the required checks link it to the right case.
Noor | Exactly. The [[case match::Case match is the verified link between the clinic's enquiry and the correct laboratory record, which remains unestablished.]] remains unresolved. Similar digits are not enough to link records or authorize a case-specific status update.
Mira | I can use the usual protected verification route. Should I send the details through that process rather than this enquiry?
Noor | Yes, use the approved [[secure channel::Secure channel is the approved protected route for the required verification information rather than unrestricted disclosure in the enquiry.]] and provide the information that process requires. We should not improvise a different identity check during this call.
Mira | I'll check the original requisition. A number I remember from another call may not be reliable.
Noor | The [[source record::Source record provides the authoritative reference to check rather than relying on a remembered or guessed number.]] is the right place to confirm what was requested. Please keep any correction traceable through the established arrangements.
Mira | Our clinic name is on the request. Does that also establish my authority to receive this particular information?
Noor | Correct. [[Receiving authority::Receiving authority concerns permission to receive the specific information and is separate from merely claiming a clinic affiliation.]] needs the applicable check as well. We should keep the correct case and the permitted recipient clear before sharing its status.
Mira | I'll note that I asked about A341 and that verification is still required. I won't write case confirmed.
Noor | That preserves the [[unverified reference::Unverified reference accurately describes A341 while the enquiry has not been linked to the correct case through the required checks.]]. It also avoids turning a search or clarification conversation into evidence of a completed identity resolution.
Mira | If our source shows a correction, I'll send it through the established route. I won't silently replace the number in the enquiry.
Noor | Thank you. That supports the [[audit trail::Audit trail preserves the supplied reference, subsequent correction, and verification actions instead of silently replacing the original request.]] without changing records simply to make two numbers agree.
Mira | I'll complete those checks next. For now, I have no case-specific result or status from you.
Noor | Agreed. [[Confidentiality::Confidentiality requires protecting case information while the correct identity and recipient authority remain unresolved.]] remains important throughout that process. I can assist with the enquiry once the required checks establish the correct case and authorized recipient.''',
    rehearsal=["Check the completed dialogue, then read A341 as A, three, four, one. Do not offer the other logged accession as a possible patient match.","Switch roles. Repeat the lines that require case verification and receiving authority before disclosure; retain the supplied request unchanged.","Complete the four-line exchange. Confirm that A314 belongs to the receiving log and A341 to the caller's request, with the match still unverified."],
    transfer_title='Read the reference without guessing',
    transfer_setup='Complete the internal training summary. These record references are not authorization to disclose a real case.',
    transfer='''Technician: "The receiving log lists ___." | A314 | A314 is the reference explicitly supplied for the receiving log.
Caller: "The requested reference is ___." | A341 | Mira supplied A341, which differs from the logged accession.
Technician: "The case match remains ___." | unverified | No required verification has established that the two references identify the same case.
Caller: "I will follow the approved verification ___." | process | The requested case must be identified through the laboratory's applicable arrangements.''',
))

BOOK['units'].append(unit(
    title='Specimen suitability and recollection language',
    scene='Insufficient quantity is not a low patient result',
    skill='Explain a documented specimen-quantity problem and relay a recollection request without inventing a collection method or clinical interpretation.',
    brief='The laboratory lead has documented insufficient quantity for test request Q6 and requested recollection through the clinic. No cause, collection method, or urgency is supplied. Clinic coordinator Alex thinks insufficient quantity means the patient has a low test result. Technician Noor corrects that misunderstanding and relays only the documented operational message. Further collection or urgency questions need the appropriate authorized guidance, not a guessed instruction.',
    cast='Noor | Laboratory technician\nAlex | Clinic coordinator',
    culture=('Correct the meaning before adding detail', 'A familiar word such as low can move a conversation from specimen status into an unsupported patient conclusion. State what the term refers to, repeat the documented action, and keep missing clinical or collection details separate.'),
    a='''What does the lead document for Q6? | Insufficient specimen quantity | A low patient test result | A confirmed diagnosis | A documented collection error | The documented finding concerns the amount available for the requested test.
What action has the lead requested? | Recollection through the clinic | Immediate treatment | A specific unsupplied collection method | Release of a numerical result | The scenario explicitly supplies a recollection request through the clinic.
Which detail is not supplied? | Collection method | Test-request reference Q6 | The quantity issue | The lead's recollection request | No collection method, urgency, or cause is included in the stated facts.''',
    vocabulary='''specimen | Material submitted for laboratory examination. | identify the specimen
specimen suitability | Whether the submitted material meets the relevant test requirements. | assess specimen suitability
insufficient quantity | Available amount below what the requested test requires here. | document insufficient quantity
quantity not sufficient | Common laboratory expression for insufficient material; abbreviated QNS. | clarify a QNS message
recollection | Obtaining another specimen under the applicable instructions. | request recollection
test request | Order identifying the examination being requested. | quote the test request
specimen volume | Amount of submitted material. | distinguish specimen volume
analyte | Substance or property being measured by a test. | name the analyte
measured concentration | Reported amount of an analyte relative to a unit quantity. | distinguish measured concentration
patient result | Reported finding from the patient's test. | avoid inventing a patient result
collection method | Approved way the required specimen is obtained. | confirm the collection method
collection container | Receptacle specified for a specimen under the relevant procedure. | verify the collection container
specimen requirement | Condition the submitted material must meet for a test. | consult specimen requirements
rejection reason | Documented reason a specimen cannot be accepted for the requested work. | relay the rejection reason
preanalytical phase | Work before the analytical measurement, including specimen handling. | discuss a preanalytical issue
aliquot | Portion separated from a specimen for a defined purpose. | identify an aliquot
hemolysis | Breakdown of red blood cells that can affect specimen assessment. | report documented hemolysis
clotted specimen | Specimen containing clotting where relevant to suitability. | describe a documented clotted specimen
contamination | Unwanted material introduced into a specimen. | investigate documented contamination
stability | Ability of a specimen or analyte to remain suitable under defined conditions. | check stability requirements
transport condition | Required condition during specimen movement. | confirm transport conditions
recollection request | Documented request for another specimen. | relay the recollection request
clinical interpretation | Explanation of a result's meaning for patient care. | refer clinical interpretation
authorized guidance | Instructions from the role or procedure permitted to provide them. | obtain authorized guidance''',
    precision="Insufficient quantity refers to specimen amount for Q6. It is not a numerical test result and does not mean the patient's measured concentration is low. Do not substitute a clinical conclusion for an operational suitability message.",
    precision_extra='The lead requested recollection through the clinic. That request supplies no method, cause, or urgency. Relay the stated action and seek the appropriate authorized guidance for missing details rather than inventing instructions.',
    phrases='''Identify the request | This message concerns test request Q6.
Attribute the finding | The laboratory lead documented insufficient quantity.
Explain the term | It refers to the amount of specimen available for testing.
Correct the misunderstanding | It does not mean the patient has a low result.
Avoid inventing a value | No patient result is supplied in this message.
Relay the action | The lead requested recollection through the clinic.
Keep cause separate | The cause is not documented here.
Avoid blame | I cannot attribute this to a collection error.
Name missing instructions | No collection method is included in this message.
Seek the right guidance | Please obtain the applicable authorized collection instructions.
Keep urgency separate | No urgency classification is supplied here.
Avoid a timing promise | I cannot confirm a new report time from this message.
Preserve the wording | Please retain insufficient quantity in the record.
Check understanding | Are we clear that this is a specimen-amount issue?
Limit the handoff | I am relaying the documented request, not giving a diagnosis.
Close accurately | Q6 needs recollection through the clinic under the appropriate guidance.''',
    notes='''Refers to | Defines the subject of the quantity statement.
Does not mean | Corrects the specific clinical misunderstanding.
Documented | Attributes the finding to the supplied record.
Not included | Marks missing instructions without guessing them.
Through the clinic | Preserves the stated route for the recollection request.
Not giving | Separates operational communication from clinical interpretation.''',
    d='''Which explanation is accurate? | There is insufficient specimen quantity for Q6, not a low patient result | The patient has a low concentration | The clinic definitely collected incorrectly | The test confirms a diagnosis | The message concerns suitability of the available specimen amount only.
Which action is documented? | Recollection through the clinic | A specific unsupplied collection technique | Emergency treatment | Release of an invented value | Only recollection through the clinic is stated as the lead's requested action.
Which statement wrongly adds a cause? | The collector definitely used the wrong container | No cause is supplied | The lead documented insufficient quantity | Collection details need authorized guidance | The scenario supplies no cause, so blaming a container or collector is unsupported.
How should urgency be described? | Not supplied in this message; follow the applicable escalation arrangements | Automatically routine | Automatically critical | Already assessed by the caller | No urgency classification is given, so neither routine nor critical may be invented.''',
    dialogue='''Alex | I'm updating the clinic's Q6 note. It says insufficient quantity. Should I tell the clinician the patient's result is low?
Noor | No. It refers to [[specimen volume::Specimen volume is the amount available for testing, not the patient's measured test result.]], not the patient's concentration. The lead documented too little material for the requested test and asked for recollection through the clinic.
Alex | I'll remove low result. Which reference should stay with the message so the team links it to the right order?
Noor | Keep [[test request::Test request Q6 identifies the work associated with the documented quantity issue and recollection request.]] Q6 in the note. The quantity message and the requested follow-up both belong to that request.
Alex | The result field is blank. Should I enter zero until the replacement specimen arrives?
Noor | No. No [[patient result::Patient result has not been supplied, so Noor must not invent a value or a low-result interpretation.]] is supplied. A blank result field does not mean the measured value is zero.
Alex | Understood. The action is to obtain another specimen. Can you confirm that is actually what the lead requested?
Noor | Yes, the documented request is [[recollection::Recollection is the lead's requested next action through the clinic, without a supplied method or urgency classification.]] through the clinic. That is the action supplied, not an instruction to use a particular collection method.
Alex | Someone has suggested the collector used the wrong container. Is that documented anywhere in this message?
Noor | No. The stated [[rejection reason::Rejection reason here is insufficient quantity for Q6, which does not establish who caused it or how it happened.]] is insufficient quantity. It does not establish a container error or identify who caused the shortage.
Alex | So I can report a suitability issue without recording collector error. Is this a problem before the analytical measurement rather than a low concentration?
Noor | Yes. This is a [[preanalytical phase::Preanalytical phase concerns work before measurement, and this specimen issue must not be recast as an analytical patient finding.]] issue about the submitted material. It is not a patient finding from an analytical result.
Alex | The clinic will ask whether recollection is routine or urgent. Neither label appears in the message I have.
Noor | Obtain the applicable [[authorized guidance::Authorized guidance is needed for missing urgency or collection details rather than inventing a classification from the quantity message.]] through the actual escalation arrangements. Don't assign a clinical urgency from the quantity wording alone.
Alex | I also need the collection instructions. I should not choose a container or amount simply to complete the note.
Noor | Correct. Check the relevant [[specimen requirement::Specimen requirement must be established from the relevant test instructions, not inferred into a collection or reporting promise.]] through the authorized procedure. This message does not provide those instructions or a new report time.
Alex | I'll relay Q6, insufficient specimen quantity, and the lead's request to recollect through the clinic. Missing instructions go to the appropriate contact.
Noor | That preserves the [[recollection request::Recollection request is the documented action to obtain another specimen through the clinic without additional invented details.]]. It also removes the unsupported low-result statement without replacing it with a guessed cause.
Alex | The clinician may still ask what this means for the patient. I'll distinguish that question from the specimen-status message.
Noor | Yes. Refer [[clinical interpretation::Clinical interpretation concerns patient meaning and is not provided by this specimen-quantity communication.]] to the appropriately qualified professional with the actual clinical context. Our note should preserve the documented limitation and requested follow-up.''',
    rehearsal=["Check the answers, then contrast specimen volume with patient result in turns 1-6. Do not read a blank result field as zero.","Switch roles and read the recollection message for Q6. Keep collection method, cause and urgency unspecified, as supplied.","Complete the four-line exchange. Say insufficient specimen quantity and recollection through the clinic without adding a diagnosis."],
    transfer_title='Correct the meaning and retain the request',
    transfer_setup='Complete the clinic exchange without adding a collection method or patient finding.',
    transfer='''Technician: "The request reference is ___." | Q6 | The documented insufficient-quantity message concerns test request Q6.
Clinic: "The issue is insufficient specimen ___." | quantity | The finding concerns the amount available for testing, not a patient concentration.
Technician: "The lead requested ___ through the clinic." | recollection | Recollection through the clinic is the only supplied next action.
Clinic: "This is not a low patient ___." | result | No patient result or low measured concentration is supplied in this message.''',
))


BOOK['units'].append(unit(
    title='Quality-control status and reportable results',
    scene='The run is complete; release is not authorized',
    skill='Explain the difference between completed analysis, unresolved quality review, and authorized reporting without supplying unsanctioned results.',
    brief='An analytical run has finished, but its quality-control review remains unresolved. The laboratory lead has not authorized result release. Clinic contact Dana asks technician Noor to describe the results as final because the instrument has completed its work. No patient values, quality findings, or troubleshooting instructions are supplied. Noor must report the actual status and refer the unresolved review to the laboratory lead without relabeling or releasing results.',
    cast='Noor | Laboratory technician\nDana | Clinic contact',
    culture=('A completed stage is not a completed process', 'Under time pressure, a caller may use finished to mean ready to report. Repeat the completed stage, then name the outstanding review and authority. This acknowledges progress without allowing the caller to infer a final report that does not exist.'),
    a='''Which stage is complete? | The analytical run | The quality-control review | Authorized result release | A final clinic report | The instrument has finished the analytical run, but review and release remain unresolved.
What is the quality-control status? | Review unresolved | Passed and approved | Confirmed failed under supplied criteria | Irrelevant because the instrument stopped | No resolved quality-control finding is supplied, so neither pass nor failure may be assumed.
Which release claim is supported? | The lead has not authorized release | Instrument completion itself authorizes release | A clinic request replaces lead authorization | Review pending means approval with a warning | The run is complete, but only the stated laboratory process can authorize release; no such permission is supplied.''',
    vocabulary='''analytical run | Defined set of measurements performed in one testing sequence. | complete the analytical run
quality control | Checks used to monitor analytical performance; abbreviated QC. | review quality control
control material | Material with defined characteristics used to assess analytical performance. | identify control material
control result | Measurement obtained from a quality-control material. | review a control result
acceptance limit | Defined boundary used to assess an applicable control condition. | apply the approved acceptance limit
quality review | Authorized assessment of relevant quality evidence. | await quality review
release authorization | Permission to issue results under the applicable process. | obtain release authorization
reportable result | Result meeting the applicable requirements for reporting. | distinguish a reportable result
standard deviation | Measure of spread around the mean; abbreviated SD. | express a difference in SD units
pending review | Status indicating an assessment is not yet resolved. | retain pending review
z-score | Difference from a specified mean divided by the specified SD. | calculate the control z-score
report status | Current stage of a report in its lifecycle. | state report status
precision | Closeness among repeated measurements under specified conditions. | discuss analytical precision
accuracy | Closeness of a measurement to an accepted reference value. | distinguish accuracy from precision
bias | Systematic difference from an appropriate reference. | investigate documented bias
random variation | Unpredictable spread in measurements under relevant conditions. | assess random variation
trend | Directional pattern across observations over time. | identify a control trend
shift | Sustained change in the level of observed measurements. | investigate a control shift
out-of-control condition | Quality state outside the applicable accepted criteria. | report a documented out-of-control condition
coefficient of variation | SD divided by the mean, usually expressed as a percentage; CV. | report the CV with its basis
withheld result | Result not released pending the applicable process. | preserve withheld-result status
review outcome | Documented conclusion of an assessment. | request the review outcome
authorized reviewer | Person permitted to assess and approve the relevant evidence. | consult the authorized reviewer
status update | Message reporting the current process stage. | give a status update''',
    precision='Run complete is an instrument-workflow status. It does not establish resolved quality control or release authorization. Because review is unresolved, do not describe the quality outcome as passed, failed, or irrelevant.',
    precision_extra='The clinic may need an update, but its request does not supply the missing authorization. Give the current stage and route the review question to the laboratory lead. No values or technical corrective actions are part of this exchange.',
    phrases='''Acknowledge completion | The analytical run has finished.
Name the unresolved stage | Quality-control review remains unresolved.
State the authority limit | The lead has not authorized result release.
Correct the inference | Instrument completion does not make the report final.
Avoid an invented QC outcome | I cannot describe the review as passed or failed.
Offer the actual status | I can provide a process-status update.
Keep values protected | I am not releasing patient values in this exchange.
Refer the review | The laboratory lead needs to resolve the review.
Avoid a deadline promise | No release time is confirmed.
Separate stages | Analysis, review, and release are different steps.
Preserve the wording | Please retain pending review in the update.
Resist relabeling | I cannot relabel unreleased results as final.
Attribute the next decision | Release depends on the authorized process.
Avoid technical improvisation | I am not supplying troubleshooting instructions.
Check the handoff | Please confirm that final reporting has not been authorized.
Close accurately | Run complete, review unresolved, release not authorized.''',
    notes='''Remains | Shows that completion of one stage did not resolve another.
Does not make | Blocks the shortcut from instrument status to final report.
Passed or failed | Names two unsupported conclusions, not two available choices.
Depends on | Preserves the required authorization relationship.
Not confirmed | Avoids turning a requested deadline into a promise.
Relabel | Identifies a wording change that would misrepresent actual status.''',
    d='''Which update is accurate? | The run is complete, QC review is unresolved, and release is not authorized | The report is final because the instrument finished | QC is confirmed failed | The clinic's request authorizes release | The correct update preserves all three distinct process and authorization states.
What does unresolved QC review establish? | No completed review outcome is supplied | Every result is wrong | Every result is final | The review can be ignored | An unresolved review supports neither a pass nor a failure conclusion.
Who should address the review question? | The laboratory lead under the authorized process | The caller by renaming the report | An unrelated delivery driver | The learner by inventing a control limit | The stated release and review authority belongs to the laboratory process and lead.
Which action misrepresents status? | Calling the results final without authorization | Reporting that the run finished | Saying review remains unresolved | Declining to invent a release time | Final status cannot be created merely by changing the wording of an unreleased result.''',
    dialogue='''Dana | The instrument has finished. Can I tell the clinic these are final results? They're waiting for an answer.
Noor | The [[analytical run::Analytical run completion confirms that the measurement sequence finished, not that review or release has been authorized.]] is complete, but quality review remains unresolved. The laboratory lead has not authorized release.
Dana | I'll remove final from the update. What wording should I use for the stage that is still outstanding?
Noor | Use [[pending review::Pending review accurately states the unresolved quality assessment without suggesting it has passed or failed.]]. That describes the unresolved assessment without suggesting the controls passed or failed.
Dana | I was about to call it a QC failure because nothing is being released. Is that too strong?
Noor | Yes. No [[review outcome::Review outcome is not supplied, so an unresolved assessment cannot be reported as a confirmed pass or failure.]] is supplied. An unresolved assessment is not the same as a documented failure.
Dana | The clinic still needs a message. Can we give them the process status without including patient values?
Noor | Yes. A [[status update::Status update communicates the current workflow stage without inventing patient findings or an analytical conclusion.]] can say analysis completed, review unresolved, release not authorized. It must not imply a final report exists.
Dana | Would the clinic's request to treat it as final count as permission? They say they accept that review is pending.
Noor | No. [[release authorization::Release authorization must come through the applicable laboratory process, not from the clinic's request for final wording.]] must come through the laboratory's applicable process. The request does not replace the lead's decision.
Dana | Then the next question is who can resolve the review, rather than whether I can change the label.
Noor | Correct. The [[authorized reviewer::Authorized reviewer is the role that must resolve the quality assessment under the laboratory process before a release claim is made.]] needs to assess the relevant evidence. I can pass the enquiry to the laboratory lead without inventing a technical conclusion.
Dana | If I leave final off but say available, could that still suggest the results are ready to use?
Noor | It could. Keep the [[report status::Report status remains unreleased and not final, even though the instrument's analytical stage is complete.]] explicit: not released, not final. A softer label should not hide the outstanding requirement.
Dana | Understood. The completed measurement stage alone does not establish that the result meets the reporting requirements.
Noor | Exactly. A [[reportable result::Reportable result must meet the relevant reporting requirements, which are not established by instrument completion alone.]] requires those requirements to be met; instrument completion alone is not enough.
Dana | Is there any supplied indication that the review can be skipped because the clinic is under time pressure?
Noor | No. The unresolved [[quality control::Quality control is the analytical-performance review area still unresolved, not an optional step erased by the completed run.]] remains part of the process. We have no authorization to bypass it or provide troubleshooting instructions.
Dana | I'll send the process update, remove the final claim, and direct the release-status enquiry to the lead.
Noor | Good. Keep any [[withheld result::Withheld result describes information not released pending the applicable review and authorization rather than a final report.]] unreleased until the applicable review and authorization are resolved. A clear update can acknowledge the delay without supplying unsanctioned findings.''',
    rehearsal=["After checking the dialogue, read the three statuses aloud: analysis complete, quality review unresolved, release not authorized.","Switch roles. Correct final to not released in the printed exchange; keep unresolved distinct from both QC passed and QC failed.","Complete the four-line exchange. Retain the lead's authorization requirement and do not substitute the clinic's request for permission."],
    transfer_title='Three stages, three separate facts',
    transfer_setup='Complete the clinic update using the actual run, review, and release status.',
    transfer='''Technician: "The analytical run is ___." | complete | The instrument has finished the stated analytical sequence.
Clinic: "Quality-control review remains ___." | unresolved | No completed quality-control review outcome is supplied in this scenario.
Technician: "Result release is not ___." | authorized | The laboratory lead has not given permission to release results.
Clinic: "We must not call the report ___." | final | Final reporting is not established by the instrument's completed run.''',
))

BOOK['units'].append(unit(
    title='Reagents, instruments, and service coordination',
    scene='The service visit ended; H2 is still unavailable',
    skill='Request a documented instrument-status decision and distinguish service attendance from authorized return to use.',
    brief='Analyzer H2 is marked unavailable. A service visit ended at 11:00, but the laboratory lead has not confirmed return to service. Technician Noor asks lead Elena for the status needed before updating the clinic. No repair steps, instrument settings, reagent findings, patient results, or confirmed restart time are supplied. The end of the service visit is a known event, not evidence that the analyzer is available.',
    cast='Noor | Laboratory technician\nElena | Laboratory lead',
    culture=('Name the status, not the hopeful implication', 'A completed visit can sound like a completed repair and approved restart. Keep those events separate. Ask the lead for the documented operating status rather than interpreting a service departure time as permission to use equipment.'),
    a='''What is H2's current recorded status? | Unavailable | Returned to service | Approved for all testing | Confirmed beyond repair | H2 is explicitly marked unavailable, with no confirmed return to service.
What happened at 11:00? | The service visit ended | H2 was authorized for use | All patient results were released | A restart was guaranteed | Eleven o'clock is only the recorded end of the service visit.
What does Noor need before the clinic update? | The lead's confirmed status | A guessed restart time | Unprovided repair instructions | An invented reagent diagnosis | Noor needs the laboratory lead's documented status rather than an inference from the visit.''',
    vocabulary='''analyzer | Instrument used to perform laboratory measurements. | identify the analyzer
instrument status | Recorded condition or availability of equipment. | confirm instrument status
unavailable | Not available for the stated operational use. | retain unavailable status
service visit | Attendance by personnel providing equipment support. | record the service visit
return to service | Authorized restoration of equipment to operational use. | confirm return to service
service report | Record describing work or findings from a service event. | review the service report
maintenance log | Record of equipment upkeep and related actions. | consult the maintenance log
equipment identifier | Reference distinguishing one instrument from another. | quote the equipment identifier
downtime | Period when equipment is not available for its intended use. | report downtime
restart authorization | Permission to resume operation under the relevant process. | obtain restart authorization
reagent | Substance used in a laboratory reaction or analytical process. | identify the reagent
reagent lot | Identified production batch of a reagent. | record the reagent lot
lot number | Reference identifying a particular production batch. | verify the lot number
expiry date | Date limiting use under applicable product instructions. | check the expiry date
inventory status | Recorded availability of supplies. | check inventory status
calibration | Establishing the relation between instrument response and reference values. | document calibration
verification check | Check confirming a specified requirement is met. | record a verification check
preventive maintenance | Planned upkeep intended to reduce equipment problems. | schedule preventive maintenance
corrective maintenance | Work addressing an identified equipment problem. | document corrective maintenance
service provider | Organization or person supplying equipment support. | contact the service provider
operational readiness | State meeting the requirements for intended operation. | confirm operational readiness
status confirmation | Explicit verification of the current equipment condition. | request status confirmation
outstanding review | Assessment not yet completed or resolved. | identify outstanding review
dilution factor | Ratio of final diluted volume to the original sample volume. | verify whether the factor was applied''',
    precision='The service visit ended at 11:00, but H2 remains marked unavailable. A departure time is not return-to-service authorization, proof of a completed repair, or a guaranteed restart time.',
    precision_extra="Request the lead's confirmed status and report only the authorized message. Do not add repair steps, settings, calibration results, reagent causes, or patient findings that are not supplied in the record.",
    phrases='''Identify the instrument | I am checking the status of analyzer H2.
State the current record | H2 is marked unavailable.
Name the known event | The service visit ended at eleven.
Separate the implication | That does not confirm return to service.
Ask for authority | Has the lead confirmed operational availability?
Request the record | What status is documented for the clinic update?
Avoid a restart promise | I have no confirmed restart time.
Keep repair findings separate | The visit end does not tell me what repair was completed.
Avoid inventing a reagent issue | No reagent finding is supplied here.
Avoid technical improvisation | I am not changing settings based on this conversation.
Preserve the equipment reference | Please keep H2 in the status message.
Name the pending step | Return-to-service confirmation is still outstanding.
Limit the clinic message | I will report the current documented availability.
Separate service and testing | A service visit is not permission to resume analysis.
Request explicit notification | Please notify me when the authorized status changes.
Close precisely | Visit ended at eleven; H2 remains unavailable pending confirmation.''',
    notes='''Marked | Attributes status to the record rather than a personal impression.
Ended at | Gives an event time without implying operational approval.
Does not confirm | Separates evidence of attendance from evidence of readiness.
Has ... confirmed | Requests a completed authorized decision.
No ... supplied | Keeps technical findings outside the stated evidence.
When ... changes | Makes a later update conditional on an actual status change.''',
    d='''Which clinic update is supported? | H2 remains unavailable; the service visit ended at 11:00 but return is unconfirmed | H2 is ready because the engineer left | All results will be final at 11:00 | The reagent lot caused the outage | The supplied facts distinguish completed service attendance from unresolved operational status.
What would establish a status change here? | The laboratory lead's confirmed return-to-service status | The visit end alone | A caller's assumption | The learner choosing a setting | The lead has not yet confirmed return, so that explicit status is needed.
Which detail must not be invented? | A restart time | The identifier H2 | The visit's 11:00 end | The unavailable label | No restart time is supplied by the known service event.
What does the service visit prove? | Support personnel attended and the visit ended | Every repair was successful | Calibration passed | Patient results are authorized | Attendance and its end are the only service facts established in the scenario.''',
    dialogue='''Noor | The clinic saw that service on H2 ended at eleven. They're asking if we can use the analyzer again. Its status still says unavailable.
Elena | Keep the [[instrument status::Instrument status remains unavailable until the lead confirms a documented change, regardless of the service visit ending.]] separate from the visit time. I have not confirmed return to service, so unavailable remains the status you can report.
Noor | Does the completed visit establish anything about availability, or only that the service attendance has finished?
Elena | Correct. A [[service visit::Service visit records support attendance and its completion, not automatic approval that the instrument is operational.]] can end without establishing operational readiness. We need the relevant documented outcome and authorized decision, not an inference from departure.
Noor | I'll remove eleven as the restart time. Can you confirm that return to use is still outstanding?
Elena | Exactly. [[Return to service::Return to service is the authorized restoration of operational use and has not been confirmed for H2.]] has not been confirmed. Please do not turn a known event time into a commitment we have not made.
Noor | Which document should the authorized reviewer check for the work completed? I don't have the service findings.
Elena | The [[service report::Service report can document service work or findings, but its contents and resulting authorization must be reviewed rather than assumed.]] is relevant to the authorized review, but do not invent its contents. No repair steps or completed verification findings are supplied in this exchange.
Noor | The clinic is asking if this was a reagent problem. I don't see a reagent batch or fault finding in the supplied information.
Elena | Good. A [[reagent lot::Reagent lot identifies a production batch and is not a documented cause of H2's unavailability in this scenario.]] reference would be a specific technical claim. We have no such finding here, and it should not be added to make the explanation sound complete.
Noor | Someone has also described calibration as passed. We don't have that result from the completed visit, do we?
Elena | Correct. [[Calibration::Calibration is a technical measurement-related process whose successful completion is not established by the service visit ending.]] status and settings belong to the applicable technical process. This conversation is about accurate coordination, not an instruction to perform or bypass that work.
Noor | Then my update is H2 unavailable, service visit ended at eleven, and no confirmed restart time. I won't give a duration for the remaining outage.
Elena | That describes the [[downtime::Downtime is the period of unavailability, which remains ongoing in the supplied status despite the completed visit.]] without inventing its cause or duration. We can acknowledge the completed visit while preserving the unresolved operating status.
Noor | If the next message just says service done, I'll still need to ask whether the operational status changed.
Elena | Yes. Ask for [[status confirmation::Status confirmation explicitly establishes the operating state needed for a clinic update rather than relying on a vague service-complete message.]] tied to H2. The wording should tell you whether availability changed, not merely that a person completed a task.
Noor | I'll retain H2 in the subject and message. An update about another instrument would not resolve this enquiry.
Elena | The [[equipment identifier::Equipment identifier H2 keeps the status attached to the correct analyzer and prevents confusion with another instrument.]] should remain visible. That is especially important when multiple service enquiries are being handled at once.
Noor | Please send the documented status change through the proper route when available. Until then, I'll keep the clinic's message at unavailable.
Elena | That is accurate. [[Operational readiness::Operational readiness requires the relevant confirmed requirements for use and has not been established for H2.]] remains unconfirmed. I will communicate a documented status change through the proper route when one is available.''',
    rehearsal=["Check the dialogue and read H2 unavailable beside service visit ended at eleven. Stress which statement describes the instrument.","Switch roles. Read the lines rejecting an unsupported restart time, reagent fault and passed calibration; retain the missing findings.","Complete the four-line exchange. End with return to service unconfirmed, not operational readiness established."],
    transfer_title='Do not turn a visit time into a restart time',
    transfer_setup='Complete the status exchange using the known event and unresolved availability.',
    transfer='''Technician: "The analyzer identifier is ___." | H2 | H2 is the equipment reference supplied for this service enquiry.
Lead: "Its recorded status remains ___." | unavailable | No confirmed return-to-service decision has changed the unavailable status.
Technician: "The service visit ended at ___." | 11:00 | Eleven o'clock is the documented end of the service visit only.
Lead: "Return to service is not yet ___." | confirmed | The laboratory lead has not confirmed operational return for H2.''',
))


BOOK['units'].append(unit(
    title='Turnaround times and realistic updates',
    scene='The two-hour clock starts at receipt',
    skill='Clarify a turnaround-time starting point and distinguish a quoted interval from a confirmed reporting promise during a backlog.',
    brief='The service quotes a two-hour turnaround measured from laboratory receipt to reporting. Specimen T5 was collected at 08:00 and received by the laboratory at 09:00. A backlog affects estimates, and no report time is confirmed. Clinic coordinator Eva assumes the two hours began at collection and expects a report at 10:00. Technician Noor explains the receipt-based interval without replacing the mistaken 10:00 promise with an unsupported 11:00 guarantee.',
    cast='Noor | Laboratory technician\nEva | Clinic coordinator',
    culture=('Correct the clock and the certainty level', 'A timing misunderstanding may involve both the starting event and the strength of a promise. Explain each separately. A calculation from a quoted interval is not the same as a confirmed delivery time, especially when a stated backlog affects estimates.'),
    a='''When does the quoted turnaround begin? | Laboratory receipt | Specimen collection | The clinic's phone call | The patient's appointment booking | The service explicitly measures the quoted interval from laboratory receipt to reporting.
When was T5 received? | 09:00 | 08:00 | 10:00 | 11:00 | The specimen was collected at eight but received by the laboratory at nine.
What report time is confirmed? | None | 10:00 | 11:00 | Exactly two hours after this call | The backlog affects estimates and the scenario supplies no confirmed report time.''',
    vocabulary='''turnaround time | Interval between defined starting and ending events; abbreviated TAT. | clarify turnaround time
collection time | Recorded time the specimen was obtained. | distinguish collection time
receipt time | Recorded time the laboratory received the specimen. | confirm receipt time
reporting time | Time a report is issued under the relevant process. | confirm reporting time
start point | Event from which an interval is measured. | name the start point
end point | Event at which a measured interval ends. | define the end point
quoted interval | Stated expected duration under the service description. | explain the quoted interval
estimate | Approximate expectation subject to relevant uncertainty. | qualify the estimate
confirmed deadline | Explicitly established time commitment. | distinguish a confirmed deadline
backlog | Accumulated work awaiting completion. | explain the backlog
work queue | Ordered or managed set of pending tasks. | check the work queue
elapsed time | Time that has passed since a specified event. | calculate elapsed time
transport interval | Time between the relevant dispatch and receipt events. | distinguish the transport interval
receipt-to-report interval | Duration measured from laboratory receipt to reporting. | explain the receipt-to-report interval
service standard | Defined service expectation under its stated conditions. | clarify the service standard
estimated completion | Predicted finish time rather than a confirmed outcome. | qualify estimated completion
delay notice | Communication explaining a later-than-expected process. | issue a delay notice
update commitment | Promise to communicate status at a stated time. | separate an update commitment
result commitment | Promise that a result will be available at a stated time. | avoid an unsupported result commitment
queue status | Current position or condition of pending work. | report queue status
time reference | Stated event and clock time used in a message. | preserve the time reference
expectation reset | Correction of an earlier timing assumption. | make an expectation reset
escalation route | Authorized path for raising a concern requiring further attention. | use the escalation route
confirmed information | Details established by the relevant record or authority. | relay confirmed information''',
    precision='Collection at 08:00 and receipt at 09:00 are different events. Applying the quoted two-hour interval to receipt gives 11:00 as the arithmetic reference, not 10:00. It still does not confirm a report time.',
    precision_extra='The backlog affects estimates, so do not promise 11:00 merely because the starting point is now correct. Keep any status-update commitment separate from a result promise, and use the actual escalation route for clinical urgency concerns.',
    phrases='''Identify the specimen | This timing enquiry concerns T5.
State collection | Collection was recorded at eight.
State receipt | Laboratory receipt was recorded at nine.
Define the service interval | The quoted two hours run from receipt to reporting.
Correct the starting point | Collection does not start this service's quoted clock.
Explain the arithmetic | Nine plus two hours gives eleven as the reference calculation.
Limit the calculation | That is not a confirmed reporting promise.
Name the delay factor | A backlog is affecting estimates.
Preserve uncertainty | No report time is confirmed.
Avoid replacing one promise | I cannot change an unsupported ten-o'clock promise into an eleven-o'clock guarantee.
Separate an update | A status update is not a promise that results will be ready.
Ask for the right information | We need the current authorized estimate, if available.
Keep the clinical boundary | Urgency concerns need the applicable clinical escalation route.
Avoid reassurance without evidence | I cannot promise the delay is clinically unimportant.
Correct the clinic message | Please state receipt-based turnaround and the current uncertainty.
Close with the facts | Collected at eight, received at nine, reporting time unconfirmed.''',
    notes='''From ... to | Defines both ends of the measured interval.
Reference calculation | Separates arithmetic from an actual service commitment.
Affecting estimates | Explains why the quoted duration does not settle the current case.
If available | Avoids implying a current estimate already exists.
Not a promise | Limits the meaning of a status update.
Current uncertainty | Keeps the unresolved reporting time explicit after correcting the starting point.''',
    d='''Why is the assumed 10:00 time unsupported? | It starts the two-hour interval at collection rather than receipt | T5 was received at ten | The service quotes three hours | Collection and receipt are always simultaneous | The clinic uses the wrong starting event for the stated receipt-to-report interval.
What does 09:00 plus two hours establish? | An 11:00 reference calculation, not a confirmed report time | Guaranteed final results at eleven | A new clinical urgency classification | Proof that no backlog exists | Arithmetic applies the quoted interval correctly but does not remove the stated uncertainty.
Which update is accurate? | T5 arrived at nine; backlog affects estimates; no report time is confirmed | T5 is guaranteed final at ten | T5 is guaranteed final at eleven | The delay has no possible clinical importance | The correct update uses the receipt time and preserves the unresolved estimate.
What is distinct from a result commitment? | An agreed time to provide a status update | An explicit promise results will be ready | A guaranteed final report deadline | A confirmed reporting time | An update can communicate progress or continued delay without promising completed results.''',
    dialogue='''Eva | I told the clinic T5 would be reported at ten: collected at eight plus the quoted two hours. Have I used the right starting point?
Noor | The quoted [[turnaround time::Turnaround time for this service is measured from laboratory receipt to reporting, not from specimen collection.]] starts at laboratory receipt, not collection. T5 was received at nine, and a backlog is currently affecting estimates.
Eva | Then the nine-o'clock laboratory entry matters for that interval. I'll keep the eight-o'clock collection event in the record as a separate fact.
Noor | Correct. The [[receipt time::Receipt time is 09:00 for T5 and is the starting event specified in this service's quoted interval.]] is the relevant starting point here. It is important to keep both events in the record rather than replacing one with the other.
Eva | Nine plus two gives eleven. Is eleven an actual reporting commitment, or only what the quoted interval would calculate?
Noor | No. That is a [[reference calculation::Reference calculation applies the quoted interval to receipt but does not establish a confirmed report time during the backlog.]], not a confirmed reporting promise. No report time is confirmed, and the backlog means the estimate cannot be treated as guaranteed.
Eva | I need to withdraw the guarantee as well as correct the arithmetic. Simply replacing ten with eleven would keep the certainty error.
Noor | Exactly. The [[quoted interval::Quoted interval is the service's stated receipt-to-report duration, which is distinct from a guaranteed time for this specimen.]] explains how timing is described, but it does not by itself establish when this particular report will be issued under the current conditions.
Eva | I'll tell the clinic I used collection instead of receipt and gave a promise the available status didn't support.
Noor | That is a clear [[expectation reset::Expectation reset corrects both the collection-based assumption and the unsupported reporting guarantee in the earlier message.]]. It preserves the known collection and receipt facts while withdrawing the unsupported ten-o'clock commitment.
Eva | Can I attribute the uncertainty to a confirmed backlog, or would that be another assumption?
Noor | The [[backlog::Backlog is explicitly supplied as affecting estimates, while the exact report time remains unconfirmed.]] is a stated factor affecting estimates. We should not add an exact queue position, duration, or cause beyond the information actually available.
Eva | If we later agree an update time, I'll say update rather than report ready. No replacement update time has been agreed here.
Noor | Yes. An [[update commitment::Update commitment promises communication of status, which may still be pending, rather than guaranteeing that a report is ready.]] is different from a result commitment. No new update time is supplied in this discussion, so we should not invent one either.
Eva | If the clinic raises clinical urgency, whom should that concern go through? I can't assess it from these timestamps.
Noor | Use the applicable [[escalation route::Escalation route directs clinical urgency concerns to the authorized process rather than inferring their significance from turnaround arithmetic.]]. We must not dismiss urgency or give clinical reassurance merely because the quoted interval was misunderstood.
Eva | My correction will retain collection at eight, receipt at nine, and the quoted two-hour receipt-to-report interval, with no report time confirmed.
Noor | That keeps the [[time reference::Time reference links each clock time to its actual event so collection and receipt are not confused again.]] explicit. Anyone reading the note can see which event starts the quoted interval and which timing remains unknown.
Eva | I'll withdraw ten o'clock and avoid promising eleven. Any actual reporting commitment needs its own confirmation.
Noor | Agreed. A [[confirmed deadline::Confirmed deadline would require an explicit established reporting commitment, which this scenario does not provide.]] is not supplied here. Keep the calculation, estimate, and any later authorized commitment distinct in subsequent messages.''',
    rehearsal=["Check the answers. Read collection at eight and receipt at nine as separate events, then calculate nine plus two as eleven.","Switch roles. Read the correction withdrawing the ten-o'clock promise; do not replace it with an eleven-o'clock guarantee.","Complete the four-line exchange. Keep a status update separate from a report-ready commitment, and retain the unconfirmed reporting time."],
    transfer_title='Correct the clock without inventing a promise',
    transfer_setup='Complete the T5 timing summary. Clock values identify known events or arithmetic only.',
    transfer='''Clinic: "T5 was collected at ___." | 08:00 | Eight o'clock is the specimen collection time, not the service's starting event.
Technician: "Laboratory receipt was at ___." | 09:00 | Nine o'clock is the recorded receipt time used by the quoted service interval.
Clinic: "Adding the quoted two hours gives ___ as a reference calculation." | 11:00 | Nine plus two hours is eleven, but this arithmetic is not a guarantee.
Technician: "The actual report time remains ___." | unconfirmed | The backlog affects estimates and no reporting commitment is supplied.''',
))

BOOK['units'].append(unit(
    title='Preliminary, final, and amended reports',
    scene="Correcting the ten-o'clock report label",
    skill='Withdraw an inaccurate report-status statement and identify the superseding final version without inventing changed findings or an amendment.',
    brief='The clinic received a preliminary report at 10:00 and a final report at 14:00 for the same request. Technician Noor mistakenly called the earlier version final. Clinic contact Priya asks which report status is correct. The 14:00 final report supersedes the 10:00 preliminary version for this request. No findings, clinical conclusions, or subsequent amended report are supplied. Noor needs to correct the earlier communication clearly and retain a traceable record.',
    cast='Noor | Laboratory technician\nPriya | Clinic contact',
    culture=('Name the correction directly', 'A vague later update may leave the original mistaken statement in circulation. Identify the earlier label, withdraw it explicitly, and state the correct version and time. Correcting communication is not the same as claiming the laboratory issued an amended clinical report.'),
    a='''What was received at 10:00? | A preliminary report | The final report | An amended report | A confirmed diagnosis only | The earlier report is explicitly preliminary, despite Noor's mistaken description.
Which version supersedes it? | The 14:00 final report | An unspecified future report | The incorrect phone label | Neither version | The supplied final report at fourteen hundred supersedes the preliminary version for this request.
What has not been supplied? | Findings or a later amended report | The two issue times | The preliminary status at ten | The final status at fourteen | The scenario provides report stages and times but no findings or later amendment.''',
    vocabulary='''preliminary report | Report issued before the relevant final reporting stage. | identify the preliminary report
final report | Report issued with final status under the applicable process. | confirm the final report
amended report | Formally revised report issued through the applicable correction process. | distinguish an amended report
supersede | Replace an earlier version as the applicable later record. | supersede the preliminary version
report version | Identified edition or stage of a report. | check the report version
issue time | Recorded time a report was issued. | quote the issue time
status label | Wording identifying a report's current stage. | correct the status label
communication correction | Explicit repair of an inaccurate spoken or written message. | make a communication correction
detection limit | Lowest amount reliably detectable under the stated method conditions. | distinguish detection from quantification
version control | Management of identifiable document revisions and their relationships. | preserve version control
current report | Report currently applicable under the stated reporting process. | identify the current report
superseded version | Earlier record replaced by an applicable later version. | retain the superseded version appropriately
correction trail | Record linking an error to its documented correction. | preserve the correction trail
recipient acknowledgment | Confirmation that the intended recipient received the message. | obtain recipient acknowledgment
report discrepancy | Difference in report information or status requiring clarification. | clarify the report discrepancy
finding | Recorded result or observation in a report. | avoid inventing a finding
interpretation | Explanation of the meaning of a finding. | refer interpretation appropriately
addendum | Additional report information issued under the applicable process. | distinguish an addendum
revision reason | Documented explanation for a report change. | state the revision reason
reissue | Issuance of a report again under the applicable procedure. | verify the reissue status
distribution record | Record of where a report or update was sent. | check the distribution record
document history | Record of earlier versions and changes. | preserve document history
explicit correction | Statement directly identifying and fixing the prior error. | provide an explicit correction
quantification limit | Lowest amount quantified with suitable precision and accuracy. | retain the below-quantification qualifier''',
    precision='The 10:00 report was preliminary; calling it final was a communication error. The 14:00 final report supersedes that version. This sequence does not establish what any findings say or whether their content changed.',
    precision_extra="An amended report is a formally revised report under the relevant process. Correcting Noor's inaccurate label does not prove such a report exists. Preserve the report history and follow the actual record-correction arrangements rather than deleting the earlier version.",
    phrases='''Open the correction | I need to correct my earlier description.
Name the error | I called the ten-o'clock report final.
Withdraw the label | That label was incorrect.
State the correct status | The ten-o'clock report was preliminary.
Identify the later version | The fourteen-hundred report is final.
Explain the relationship | The final report supersedes the preliminary version for this request.
Avoid a content claim | I am not saying the findings changed.
Avoid inventing an amendment | No later amended report is supplied here.
Separate processes | This is a correction to my communication.
Request acknowledgment | Please confirm you have the corrected status.
Preserve time references | Keep ten and fourteen attached to their respective versions.
Maintain history | Retain the earlier version according to the record policy.
Identify the current reference | Please use the final version's status in this enquiry.
Avoid clinical interpretation | No clinical conclusion is part of this correction.
Make follow-up traceable | Link the correction to the earlier message.
Close precisely | Ten was preliminary; fourteen is final and supersedes it.''',
    notes='''I called | Takes responsibility for the inaccurate description.
Was incorrect | Withdraws the earlier label without ambiguity.
Supersedes | Explains the relationship between versions, not the meaning of findings.
Not saying | Prevents a status correction from becoming a content claim.
No later ... supplied | Limits the known report sequence.
Respective | Keeps each time paired with its own version.''',
    d='''Which correction is clear? | I incorrectly called the 10:00 report final; it was preliminary; the 14:00 report is final | There was some confusion, but all versions are final | Ignore the times | The patient findings definitely changed | The correct message identifies the error and gives both accurate version statuses.
What does supersedes mean here? | The later final version replaces the preliminary version for this request | Both reports become preliminary | Every previous record must be destroyed | A diagnosis has been reversed | Superseding describes which version is applicable, not deletion or a clinical conclusion.
Which claim is unsupported? | An amended report was issued after 14:00 | The 10:00 report was preliminary | The 14:00 report is final | Noor's earlier label was wrong | No later amendment appears in the supplied report sequence.
What should be preserved? | A traceable correction and report history under policy | Only the incorrect phone message | An invented new issue time | A claim that no error occurred | A documented correction should repair the message without concealing the relevant history.''',
    dialogue='''Noor | Priya, I need to correct my earlier message. I called the ten-o'clock report final. It was preliminary; the fourteen-hundred report is final.
Priya | Thank you for the [[explicit correction::Explicit correction directly identifies the earlier inaccurate final label instead of leaving the recipient to infer what changed.]]. I'll correct my note before passing the earlier label on.
Noor | Please keep both issue times. The ten-o'clock document wasn't final at issue, even though a final version now exists.
Priya | I'll change the earlier [[status label::Status label for the earlier report must be preliminary, correcting Noor's mistaken description without inventing clinical content.]] to preliminary and identify fourteen hundred as the final version. I won't relabel the original document itself.
Noor | Right. I'm correcting what I said about its status, not announcing a new laboratory finding.
Priya | So this is a [[communication correction::Communication correction repairs Noor's inaccurate message and does not itself establish an amended clinical report.]]. It repairs your message but does not, by itself, tell me that any clinical content changed.
Noor | Exactly. Nor should we call the fourteen-hundred final report amended merely because I used the wrong word earlier.
Priya | An [[amended report::Amended report would be a formally revised report under the applicable process, which the stated preliminary-to-final sequence does not establish.]] would need its own formal status and record. The supplied sequence is preliminary followed by final.
Noor | Can you repeat the two versions back? I want to make sure the earlier mistake is not carried forward.
Priya | Ten hundred: preliminary. Fourteen hundred: final. I'll retain each [[issue time::Issue time distinguishes the 10:00 preliminary report from the 14:00 final report in the correction and handoff.]] beside the corresponding status.
Noor | That's correct. We haven't been given the clinical content of either version, so I can't describe a change in the patient's result.
Priya | I won't infer a changed [[finding::Finding refers to report content, which has not been supplied and must not be inferred from a change in report status.]] from the status change. The supplied evidence concerns the report versions and your earlier wording.
Noor | Please link this correction to the inaccurate message rather than silently replacing it. The next reader should know what was corrected.
Priya | I'll preserve the [[correction trail::Correction trail links the inaccurate message to its explicit replacement so the earlier error remains traceable.]] through the applicable record process. That keeps the original error and its correction traceable.
Noor | The earlier report also belongs in the retained version record under policy. Superseded does not mean erase the history.
Priya | Understood. The [[document history::Document history retains the version sequence and correction record according to policy instead of hiding the earlier report or error.]] stays intact while the fourteen-hundred final version is identified as current for this request.
Noor | Can you confirm that you've received the corrected version information, rather than only seen that I sent a follow-up?
Priya | I confirm [[receipt::Receipt establishes that Priya received the corrected version information rather than leaving communication assumed.]]: ten hundred preliminary, fourteen hundred final, and your earlier final label for ten hundred is withdrawn.
Noor | Thank you. No later amendment is established here. I'll use the same version wording in any onward communication.
Priya | I'll refer to the fourteen-hundred final version as the [[current report::Current report is the supplied 14:00 final version applicable to this request, with no later amendment established.]], without inventing findings or hiding the earlier correction.''',
    rehearsal=["After checking the answers, read the explicit correction: ten hundred preliminary, fourteen hundred final.","Switch roles and repeat both versions and times. Say communication correction without converting the sequence into an amended-report claim.","Complete the four-line exchange. Keep the earlier mistake traceable and identify the current final version without inventing clinical findings."],
    transfer_title='Correct the version, not the patient finding',
    transfer_setup='Complete the report-status correction using only the supplied times and relationship.',
    transfer='''Technician: "The 10:00 report was ___." | preliminary | The earlier report's correct status is preliminary despite the mistaken phone label.
Clinic: "The ___ report is final." | 14:00 | Fourteen hundred is the stated time of the later final report.
Technician: "The final report ___ the earlier version." | supersedes | The later final version replaces the preliminary version for this request.
Clinic: "No later ___ report is supplied." | amended | The scenario establishes no subsequent formally amended report.''',
))


BOOK['units'].append(unit(
    title='Critical notifications and acknowledged handoffs',
    scene='Six point four, not six point one',
    skill='Deliver and correct a critical-result message with an exact value, unit, complete read-back, and confirmed receipt.',
    brief="Fictional Lumen laboratory designates C7's potassium result of 6.4 mmol/L as critical under its own criteria. The unit mmol/L means millimoles per liter. Case identity and Dr Shah's receiving authority are already verified. The report was issued at 14:10, and the call occurs at 14:12. Dr Shah is at extension 214 and initially repeats 6.1. Technician Noor must correct the value, obtain a complete read-back, and confirm receipt. No diagnosis, treatment, or universal critical threshold is supplied.",
    cast='Noor | Laboratory technician\nDr Shah | Verified authorized recipient',
    culture=('Interrupt an inaccurate repeat clearly', 'Politeness should not obscure a wrong number. Say correction, give the exact value and unit, and ask for the complete message again. This scenario begins after identity and receiving authority have been verified; the abbreviated case label does not replace real patient-identification requirements.'),
    a='''What potassium value must be communicated? | 6.4 mmol/L | 6.1 mmol/L | 14.10 mmol/L | 214 mmol/L | Lumen's supplied report value is 6.4 millimoles per liter, not the initial mistaken repeat.
What is already verified? | Case identity and Dr Shah's receiving authority | A treatment plan | A universal critical threshold | A diagnosis | The briefing explicitly establishes identity and recipient authority before the call.
Which time is the call time? | 14:12 | 14:10 | 02:14 | 06:40 | The report was issued at 14:10, while the notification call occurs at 14:12.''',
    vocabulary='''critical result | Result requiring urgent notification under the laboratory's defined criteria. | communicate a critical result
critical notification | Communication of a locally designated critical result. | document the critical notification
potassium | Chemical element measured as an analyte in this fictional report. | state the potassium result
millimoles per liter | Concentration unit written mmol/L. | say millimoles per liter
numerical value | Number reported with the relevant analyte and unit. | correct the numerical value
unit of measurement | Scale or quantity expression accompanying a value. | retain the unit of measurement
decimal point | Mark separating the whole and fractional parts of a number. | pronounce the decimal point
read-back | Recipient's spoken repetition of the received message. | obtain a complete read-back
closed-loop communication | Exchange in which the recipient repeats and sender confirms the message. | complete closed-loop communication
acknowledgment | Explicit confirmation that a message was received. | obtain acknowledgment
authorized recipient | Person verified as permitted to receive the information. | identify the authorized recipient
verified identity | Identity established through the required checks. | preserve verified identity
report issue time | Time at which the report was issued. | state the report issue time
notification time | Time at which the communication occurs. | record the notification time
contact extension | Internal telephone number for the recipient. | confirm the contact extension
discrepant repeat | Read-back differing from the intended message. | correct a discrepant repeat
verbal correction | Spoken statement replacing inaccurate information. | make a verbal correction
complete message | Required case reference, analyte, value, unit, and relevant status details. | repeat the complete message
local critical criteria | Laboratory-specific rules defining critical designation. | apply local critical criteria
notification record | Documentation of the communication and its receipt. | complete the notification record
sender confirmation | Speaker's check that the repeated message is accurate. | give sender confirmation
recipient role | Function or authority of the person receiving information. | record the recipient role
clinical action | Patient-care decision made by an appropriately authorized professional. | separate clinical action
communication discrepancy | Difference between intended and received information. | resolve the communication discrepancy''',
    precision='The correct value is 6.4 mmol/L, spoken six point four millimoles per liter. The incorrect 6.1 read-back must be corrected immediately and followed by a complete accurate repetition, not a vague yes or okay.',
    precision_extra='Lumen alone supplies the critical designation for this fictional case. Report issue time is 14:10; notification time is 14:12; extension 214 is a contact number. None is a treatment instruction, diagnosis, or universal laboratory threshold.',
    phrases='''Identify the notification | This is Lumen laboratory with a critical-result notification for verified case C7.
State the analyte | The analyte is potassium.
State the value and unit | The result is six point four millimoles per liter.
Attribute the designation | Lumen designates this result critical under its own criteria.
Give the report time | The report was issued at fourteen ten.
Request repetition | Please read back the case, analyte, value, and unit.
Interrupt the error | Correction: six point four, not six point one.
Repeat the whole value | Potassium, six point four millimoles per liter.
Request a complete second read-back | Please repeat the complete message again.
Confirm accuracy | That read-back is correct.
Confirm the recipient | You are Dr Shah at extension two one four.
Confirm receipt | Please confirm receipt of this critical-result notification.
Distinguish times | The report time is fourteen ten; this call is at fourteen twelve.
Keep the record exact | I will document the recipient, times, correction, and confirmed read-back.
Separate clinical decisions | This notification does not supply a diagnosis or treatment instruction.
Close the communication loop | The corrected value and unit have been read back accurately and receipt confirmed.''',
    notes='''Correction | Clearly interrupts an inaccurate number rather than politely allowing it to stand.
Not six point one | Identifies the exact mistaken value being replaced.
Complete | Requests analyte and unit as well as the number.
That ... is correct | Supplies the sender's confirmation after the recipient repeats.
Under its own criteria | Prevents the fictional critical designation becoming a universal threshold.
Report time versus call time | Keeps two distinct events from being combined in the record.''',
    d='''Which correction is precise? | Correction: potassium 6.4 mmol/L, not 6.1; please read back the complete result | Yes, close enough | Change it to whatever you heard | It is probably six something | The correct response replaces the wrong value and requests complete confirmation.
Which read-back is complete for the result? | C7, potassium, 6.4 millimoles per liter | Six point four only | Potassium, six point one | Extension 214 is critical | The complete result repeat includes the verified case reference, analyte, exact value, and unit.
What does 214 identify? | Dr Shah's contact extension | The potassium value | The report time | A critical threshold | Extension 214 is the supplied recipient contact number, not a laboratory measurement.
Which conclusion is not authorized by the scenario? | A specific diagnosis or treatment plan | Lumen's local critical designation | The exact value and unit | A corrected and confirmed read-back | The scenario explicitly provides no diagnosis, treatment instruction, or universal threshold.''',
    dialogue='''Noor | Dr Shah, this is Noor at Lumen laboratory. For verified case C7, potassium is six point four millimoles per liter, designated critical by Lumen. The report was issued at fourteen ten. Please read it back.
Dr Shah | My [[read-back::Read-back is the recipient's repetition, which initially contains the incorrect 6.1 value and must be corrected.]] is C7, potassium, six point one millimoles per liter, report issued at fourteen ten. Have I received that correctly?
Noor | Correction: six point four, not six point one. For C7, potassium is six point four millimoles per liter, critical under Lumen's criteria, report issued at fourteen ten. Please repeat the complete message.
Dr Shah | C7, potassium, six point four [[millimoles per liter::Millimoles per liter is the required concentration unit accompanying the corrected potassium value of 6.4.]], critical under Lumen's criteria, report issued at fourteen ten.
Noor | That read-back is correct. Please confirm receipt of the critical notification. Our case-identity and receiving-authority checks were completed before this exchange.
Dr Shah | I confirm [[receipt::Receipt confirms that the verified authorized recipient has received the corrected critical-result message.]] of the critical notification for C7: potassium six point four millimoles per liter, with the report issued at fourteen ten.
Noor | Thank you. This call is at fourteen twelve; the report issue time is fourteen ten. I'll keep those events separate.
Dr Shah | Agreed. Fourteen twelve is the [[notification time::Notification time is 14:12 for this call and must remain distinct from the report's 14:10 issue time.]], not a revised issue time.
Noor | Please confirm extension two-one-four for the communication record. The receiving identity and authority checks are already complete.
Dr Shah | Two-one-four is my [[contact extension::Contact extension 214 identifies Dr Shah's telephone contact and is not a result value or timestamp.]]. It isn't part of the concentration or the report time.
Noor | I'll record that the initial six-point-one repeat was corrected and the complete six-point-four message confirmed.
Dr Shah | Yes, retain that [[communication discrepancy::Communication discrepancy is the initial 6.1 repeat that was explicitly corrected to 6.4 and confirmed.]]. The error was in my initial repetition, not a newly amended laboratory value.
Noor | Correct. I haven't changed the result. The report remains potassium six point four millimoles per liter.
Dr Shah | That is the confirmed [[numerical value::Numerical value is 6.4, while the correction concerns the misheard repeat rather than a changed laboratory report.]]. Keep the unit with it, not just the digits.
Noor | The laboratory notification is now acknowledged. No treatment instruction has been supplied in this call.
Dr Shah | Any [[clinical action::Clinical action belongs to the appropriate authorized patient-care process and is not supplied by this language-practice notification.]] will go through the appropriate patient-care process. Please retain the notification record while I attend to that responsibility.
Noor | I will retain C7, potassium, six point four, millimoles per liter, Lumen's critical designation, and fourteen-ten report time.
Dr Shah | That preserves the [[complete message::Complete message retains the case reference, potassium, corrected 6.4 value, unit, critical designation, and report time.]] I received, along with the separate call time and corrected read-back.
Noor | Your accurate repeat and acknowledgment are recorded. I won't substitute message sent for confirmed receipt.
Dr Shah | Thank you. That completes the [[closed-loop communication::Closed-loop communication is completed through the corrected recipient repetition, sender confirmation, and explicit acknowledgment of receipt.]] for the notification; the subsequent care decisions remain separate.''',
    rehearsal=["Check the answers, then read turns 1-6 in order. Correct six point one immediately to six point four millimoles per liter and confirm the complete repeat.","Switch roles. Read the record details: report fourteen ten, notification fourteen twelve, extension two-one-four. Keep each number attached to its purpose.","Complete the four-line exchange with C7, potassium, the correct value and unit. Use only the fictional case; no treatment instruction is supplied."],
    transfer_title='Correct, repeat, confirm',
    transfer_setup='Complete the result exchange. Identity and authority are already verified; the critical designation is specific to fictional Lumen.',
    transfer='''Technician: "Correction: potassium ___ mmol/L, not 6.1." | 6.4 | The supplied potassium value is 6.4, correcting the inaccurate initial repeat.
Recipient: "The unit means ___." | millimoles per liter | The abbreviation mmol/L expands to millimoles per liter.
Technician: "The report was issued at ___." | 14:10 | Fourteen ten is the report issue time, distinct from the later call.
Recipient: "This notification call occurs at ___." | 14:12 | Fourteen twelve is the supplied time of the critical-result notification call.''',
))

BOOK['units'].append(unit(
    title='Referral laboratories and outstanding work',
    scene='Delivered parcel, unconfirmed accession, accepted handover',
    skill='Distinguish courier delivery from referral acceptance and transfer a pending enquiry with explicit ownership and an update commitment.',
    brief="Send-out X8 appears on Monday's manifest. The courier confirms parcel delivery on Tuesday, but the referral laboratory has not confirmed accession acceptance for X8. Noor's shift is ending. Incoming technician Eli accepts responsibility for the enquiry and the agreed 15:00 clinic update. No result date is confirmed. The handover must preserve the difference between parcel delivery, individual accession acceptance, and the promise to provide an update rather than a result.",
    cast='Noor | Outgoing laboratory technician\nEli | Incoming laboratory technician',
    culture=('A message left is not a responsibility accepted', 'A useful handover ends with the incoming colleague naming the work they accept. Keep the exact unresolved question and the promised update time visible. Evidence of transport progress should not be upgraded to specimen acceptance or a confirmed result date.'),
    a='''What does the courier confirm? | Parcel delivery on Tuesday | X8's accession acceptance | A completed patient result | A Friday reporting promise | The courier confirms transport delivery, not the referral laboratory's individual accession decision.
What remains unconfirmed? | X8's accession acceptance | Its appearance on Monday's manifest | Parcel delivery on Tuesday | Eli's acceptance of the enquiry | The referral laboratory has not confirmed accession acceptance for X8.
What does Eli accept? | The enquiry and the 15:00 clinic update | A guaranteed result by 15:00 | Permission to invent a referral number | Responsibility for an already final result | Eli explicitly accepts follow-up ownership and the agreed update, not a result deadline.''',
    vocabulary='''referral laboratory | External laboratory receiving work referred for testing. | contact the referral laboratory
send-out | Specimen or request sent to another laboratory for work. | track the send-out
manifest | Record listing items included in a shipment. | check the manifest
courier | Service transporting the parcel. | contact the courier
parcel delivery | Arrival of a transport package at its destination. | confirm parcel delivery
accession acceptance | Referral laboratory's recorded acceptance of the individual request or specimen. | confirm accession acceptance
delivery confirmation | Evidence that the transport package arrived. | retain delivery confirmation
referral reference | Identifier used for the externally referred work. | request the referral reference
tracking number | Transport identifier used to follow a shipment. | verify the tracking number
chain of custody | Documented sequence of possession and transfer where required. | preserve chain of custody
dispatch record | Record of sending an item onward. | consult the dispatch record
outstanding enquiry | Follow-up question not yet resolved. | transfer the outstanding enquiry
handover | Transfer of status, responsibility, and next actions. | complete the handover
incoming technician | Staff member taking over work at a shift transition. | identify the incoming technician
outgoing technician | Staff member transferring work before leaving. | support the outgoing technician
action owner | Person explicitly responsible for the next task. | name the action owner
acceptance acknowledgment | Explicit statement accepting a responsibility or received item. | obtain acceptance acknowledgment
update time | Agreed time to communicate current status. | preserve the update time
result date | Confirmed or proposed date for an issued finding. | avoid inventing a result date
pending accession | Status where registration or acceptance remains unresolved. | report pending accession
transport milestone | Recorded event in the movement of a parcel. | distinguish a transport milestone
laboratory milestone | Recorded event in laboratory processing or acceptance. | confirm the laboratory milestone
follow-up ownership | Assigned responsibility for continuing an enquiry. | transfer follow-up ownership
continuity | Preservation of work and communication across a transition. | maintain continuity''',
    precision="Monday's manifest records X8 in the outgoing shipment, and Tuesday's courier confirmation establishes parcel delivery. Neither document by itself establishes the referral laboratory's accession acceptance of X8.",
    precision_extra='Eli accepts both the unresolved enquiry and the agreed 15:00 clinic update. That creates an explicit owner for follow-up, not a confirmed result date. The update may need to say acceptance is still unconfirmed if that remains the actual status.',
    phrases='''Identify the send-out | This handover concerns X8.
State the dispatch evidence | X8 appears on Monday's manifest.
State the transport evidence | The courier confirms parcel delivery on Tuesday.
Name the missing milestone | Referral accession acceptance is not confirmed.
Avoid upgrading evidence | Delivered does not mean individually accepted.
Name the enquiry | We need confirmation of X8's accession acceptance.
Transfer responsibility | Can you accept this outstanding enquiry?
Accept explicitly | I accept responsibility for following up X8.
Preserve the clinic commitment | The agreed clinic update is at fifteen hundred.
Separate result timing | No result date is confirmed.
Avoid inventing a reference | Do not create a referral accession number.
Keep the source visible | Attribute delivery to the courier and acceptance to the referral laboratory.
Request an accurate update | Report the actual status even if acceptance remains unresolved.
Preserve the record | Keep the manifest and delivery confirmation linked to X8.
Close the shift handover | Eli has accepted the enquiry and the clinic update.
Maintain the boundary | Follow-up accepted does not mean testing completed.''',
    notes='''Appears on | Attributes X8's dispatch listing to the manifest.
Confirms delivery | Limits the courier's evidence to transport.
Individually accepted | Distinguishes the specimen's laboratory status from its parcel.
I accept responsibility | Makes task ownership explicit.
Even if | Preserves the update obligation when the enquiry is still unresolved.
Does not mean | Prevents one completed milestone from implying another.''',
    d='''Which summary is accurate? | X8 is on Monday's manifest; its parcel arrived Tuesday; accession acceptance is unconfirmed | X8 is accepted because the parcel arrived | X8 has a final result | The manifest confirms a reporting date | The accurate summary keeps dispatch, delivery, and accession acceptance separate.
What is the precise follow-up question? | Has the referral laboratory accepted X8's accession? | Did the courier diagnose the patient? | Can we invent a result date? | Was every parcel in the country delivered? | The outstanding laboratory milestone is X8's individual accession acceptance.
What should happen at 15:00 under the agreed handover? | Eli gives the clinic the actual status | A final result is guaranteed | The enquiry disappears automatically | Noor is assumed to remain on shift | The commitment concerns a clinic update, not guaranteed testing completion.
Which statement confirms ownership? | I accept the X8 enquiry and the 15:00 clinic update | Someone probably saw the note | Delivered means everything is finished | No reply means accepted | Eli's explicit acceptance transfers both the enquiry and the stated communication responsibility.''',
    dialogue='''Noor | Can you take over X8 before I leave? Monday's manifest lists it, and the parcel was delivered Tuesday, but one laboratory status is still missing.
Eli | What is the outstanding [[laboratory milestone::Laboratory milestone is X8's individual accession acceptance, which is distinct from the confirmed transport delivery.]]? I want to separate what the courier has confirmed from what the referral laboratory has actually acknowledged.
Noor | It's the individual accession acceptance. The referral laboratory hasn't confirmed accepting X8, even though the courier delivered the parcel.
Eli | Then the [[outstanding enquiry::Outstanding enquiry asks whether the referral laboratory has accepted X8, rather than whether its parcel reached the destination.]] is specifically about X8's accession acceptance. I will not treat parcel arrival as evidence that this particular item was accepted for work.
Noor | I'll leave you both records. The manifest supports dispatch; the courier record supports arrival. Neither is an issued-result notice.
Eli | I will preserve the [[dispatch record::Dispatch record is the Monday manifest listing X8, which supports shipment history but not later acceptance or reporting.]] and the courier evidence. I will not replace those source details with a single vague status such as received and complete.
Noor | The clinic is expecting a status update at fifteen hundred. That commitment remains even if the acceptance enquiry is unresolved.
Eli | I accept the [[update time::Update time is the agreed 15:00 clinic communication commitment, not a confirmed result deadline.]] of fifteen hundred as part of the handover. If accession acceptance remains unresolved, the update must state that accurately.
Noor | Can you explicitly take the enquiry as well as the call? I need to know who will continue it after this shift.
Eli | Yes. I accept [[follow-up ownership::Follow-up ownership makes Eli responsible for continuing the X8 accession enquiry rather than merely receiving a note.]] for X8's accession enquiry and the clinic update. I will carry both tasks forward under the laboratory's actual process.
Noor | The referral's accession field is blank in the information I have. X8 is our send-out reference, not a newly confirmed external accession.
Eli | Understood. A [[referral reference::Referral reference must come from the relevant confirmed record and must not be invented to make the handover appear complete.]] needs the appropriate source. I will preserve X8 as the send-out reference while seeking the missing acceptance information.
Noor | If someone says received, please ask whether they mean the whole parcel or acceptance of the individual specimen.
Eli | I will call it [[delivery confirmation::Delivery confirmation establishes the parcel's arrival on Tuesday but not the referral laboratory's acceptance of every individual item.]], not accession confirmation. The referral laboratory must establish the individual laboratory status we are asking about.
Noor | We also have no result date. Please don't turn the fifteen-hundred update into a promise that the report will be ready.
Eli | No [[result date::Result date remains unconfirmed and cannot be inferred from dispatch, parcel arrival, or acceptance of follow-up responsibility.]] is confirmed. I will not turn the fifteen-hundred update into a reporting promise or infer a date from the transport timeline.
Noor | I'll read back the handover: X8 dispatched Monday, parcel delivered Tuesday, accession acceptance outstanding; you own that enquiry and the fifteen-hundred update.
Eli | That is my [[acceptance acknowledgment::Acceptance acknowledgment explicitly confirms Eli's responsibility for both the unresolved enquiry and the agreed clinic update.]] of the handover. I accept those two responsibilities, with the accession status and result timing still unresolved as stated.
Noor | Thanks. I'll record your acceptance before leaving. The unresolved enquiry now has an owner, but the laboratory status itself has not changed.
Eli | That maintains [[continuity::Continuity preserves the unresolved work, evidence, and communication commitment across Noor's shift ending and Eli taking over.]]. I will follow up the acceptance question and give the clinic the actual status at fifteen hundred, without claiming a result that has not been confirmed.''',
    rehearsal=["Check the dialogue, then read the timeline: Monday dispatch, Tuesday parcel delivery, individual accession acceptance unconfirmed.","Switch roles. Have Eli explicitly accept both the X8 enquiry and the fifteen-hundred clinic update, not just receipt of a note.","Complete the four-line exchange. Preserve the absent result date and do not turn the update time into a reporting promise."],
    transfer_title='Transfer the question and the commitment',
    transfer_setup='Complete the shift handover without upgrading parcel delivery to laboratory acceptance.',
    transfer='''Outgoing: "The send-out reference is ___." | X8 | X8 identifies the outstanding referral enquiry in the supplied handover.
Incoming: "The courier confirms delivery on ___." | Tuesday | Tuesday is the confirmed parcel-delivery day, not an accession-acceptance confirmation.
Outgoing: "Accession acceptance remains ___." | unconfirmed | The referral laboratory has not confirmed acceptance for the individual send-out.
Incoming: "I accept the enquiry and the ___ clinic update." | 15:00 | Eli accepts responsibility for the agreed fifteen-hundred status update, not a result deadline.''',
))
