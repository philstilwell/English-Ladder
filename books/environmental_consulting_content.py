"""Original learner-book content for environmental consulting."""
from books.authoring import unit

BOOK = dict(
    slug='environmental-consulting', title='Environmental Consulting English',
    cover_label='ENGLISH FOR ENVIRONMENTAL PROFESSIONALS',
    cover_title='Environmental\nConsulting', cover_size=32,
    tagline='Define the boundary. Trace the evidence. Explain the finding.',
    audience='For environmental consultants, field coordinators, project managers, and sustainability teams.',
    map_intro='Eight consulting conversations: qualify a site assessment, investigate a custody gap, clarify an agency request, compare remediation proposals, report audit progress, correct an emissions claim, address residents, and negotiate a scope change.',
    notes_title='Make the limits as clear as the findings',
    notes_intro='An environmental result belongs to a location, period, method, and question. These conversations practice preserving those boundaries while explaining evidence to clients, agencies, colleagues, and the public.',
    field_notes=[
        ('Separate absence from evidence', 'A missing record does not establish either a clean site or a release. Explain what is missing, who will assess its significance, and what conclusion remains unsupported.', '"The tank-closure record is missing; its significance still requires review."'),
        ('Keep the evidence traceable', 'Report a documentation gap without inventing the missing event or silently repairing the original. Distinguish a quality review from a final decision about whether data can support a particular use.', '"The receiving signature is blank; the data-usability review remains open."'),
        ('Name the comparison basis', 'Implementation duration is not the whole remediation period, and selected electricity emissions are not an organization-wide footprint. State included activities and excluded costs or sources.', '"These totals include the stated monitoring costs, but technical suitability is still unresolved."'),
        ('Translate uncertainty respectfully', 'Residents may hear a narrow technical statement as a broad reassurance. Acknowledge the practical question and explain exactly which places, substances, and conditions were assessed.', '"These results cover three locations on one morning; they do not characterize the entire area."')],
    scope_note='All sites, people, projects, figures, and local procedures are fictional. This book teaches professional English, not environmental, engineering, legal, health, or investment advice. Actual assessment, sampling, remediation, regulatory, and safety decisions require qualified professionals using applicable requirements. No exercise certifies a site, establishes safe exposure, or authorizes field work.',
    sources=[
        dict(title='U.S. Environmental Protection Agency. Brownfields All Appropriate Inquiries.', url='https://www.epa.gov/brownfields/brownfields-all-appropriate-inquiries', note='Background on environmental site inquiries, professional review, and assessment context. The fictional site is not an AAI determination or an opinion about liability protection.', checked='1 October 2026'),
        dict(title='U.S. Environmental Protection Agency, Region 4. Sample and Evidence Management.', url='https://www.epa.gov/sites/default/files/2015-06/documents/Sample-and-Evidence-Management.pdf', note='Background on traceable sample custody and documentation. This regional procedure is not a universal rule; the fictional missing signature concerns a field-team-to-laboratory handoff required by the stated project plan, not a common-carrier signature.', checked='1 October 2026'),
        dict(title='U.S. Environmental Protection Agency. Regional Screening Levels: User Guide.', url='https://www.epa.gov/risk/regional-screening-levels-rsls-users-guide', note='Background on screening, site-specific evaluation, and exposure context. No actual screening value or cleanup criterion is supplied or prescribed.', checked='1 October 2026'),
        dict(title='Greenhouse Gas Protocol. Corporate Accounting and Reporting Standard.', url='https://ghgprotocol.org/sites/default/files/ghgp/standards/ghg-protocol-revised.pdf', note='Background vocabulary for organizational boundaries and emissions scopes. The book does not certify an inventory, establish carbon neutrality, or treat standards under revision as adopted requirements.', checked='1 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Phase I and Phase II Site Assessments',
    scene='A missing record is not a clean-site conclusion',
    skill='Qualify an assessment summary and explain the significance review without guessing its outcome.',
    brief='A buyer is reviewing the former Bell workshop site. Consultant Maya has completed the scheduled site visit, interviews, and available historical-record review. The tank-closure record requested from the archive has not arrived. Environmental professional Eric has not yet assessed the significance of that gap. A draft executive summary says no further questions remain. No sampling is included in the current Phase I scope, and no Phase II investigation has been authorized. Maya will contact the archive and give Eric a status update on Tuesday at 14:00; receipt of the record by then is not guaranteed.',
    cast='Maya | Project consultant\nEric | Environmental professional',
    culture=('A qualification is useful information', 'A client may interpret a cautious phrase as indecision. Tie the qualification to a specific missing source and a named review step. Do not use broad reassurance to make an incomplete evidential position sound more commercially convenient.'),
    a='''Which information is missing? | The tank-closure record | Every historical source | The completed site-visit notes | All interview records | The brief identifies one outstanding tank-closure record, not an absence of all assessment work.
What is authorized now? | The current Phase I scope, without sampling | An unrestricted Phase II investigation | Excavation of every tank | A clean-site certificate | The stated scope excludes sampling, and no Phase II investigation has been authorized.
What is promised for Tuesday at 14:00? | A status update | Guaranteed record receipt | A final clean-site conclusion | Completed soil sampling | Maya commits to reporting status, not to controlling the archive or completing additional investigation.''',
    vocabulary='''Phase I environmental site assessment | An inquiry into a property's environmental conditions using specified assessment methods. | conduct a Phase I assessment
Phase II investigation | A further investigation that may include sampling to address identified questions. | scope a Phase II investigation
historical land use | Past uses of a property or surrounding land. | investigate historical land use
records review | Examination of documents relevant to an assessment question. | complete the records review
site reconnaissance | Observational examination of a site as part of an assessment. | document site reconnaissance
tank-closure record | Documentation concerning the closure of a storage tank. | request the tank-closure record
all appropriate inquiries (AAI) | A U.S. environmental inquiry framework relevant to specified property transactions. | evaluate AAI requirements
environmental professional | A professional meeting the applicable qualifications for the assessment role. | refer to the environmental professional
data gap | Missing or unavailable information relevant to an assessment. | identify a data gap
release | An escape or discharge of a substance into the environment. | investigate a reported release
source limitation | A restriction affecting what a source can establish. | disclose a source limitation
scope of inquiry | The defined questions and work included in an assessment. | confirm the scope of inquiry
recognized environmental condition (REC) | A defined assessment classification concerning specified hazardous-substance or petroleum conditions. | evaluate a potential REC
historical aerial photograph | An overhead image documenting past site appearance. | compare historical aerial photographs
fire insurance map | A historical map that may describe buildings and past uses. | review a fire insurance map
regulatory database | Organized agency information about regulated sites or activities. | search a regulatory database
adjoining property | A property directly next to the subject site. | review adjoining property uses
subject property | The property being assessed. | define the subject property
significant data gap | A gap that affects the professional's ability to identify relevant environmental conditions. | assess a significant data gap
interview record | Documentation of information obtained from an interview. | retain the interview record
professional opinion | A qualified interpretation based on evidence and applicable practice. | support a professional opinion
follow-up request | A further request for information or action. | issue a follow-up request
executive summary | A concise account of major findings and qualifications. | qualify the executive summary
authorization | Permission to undertake specified work. | obtain investigation authorization''',
    precision='A data gap is not automatically a significant data gap, and neither label alone proves a release. The environmental professional evaluates its significance using the assessment context and applicable requirements.',
    precision_extra='Phase I and Phase II are not synonyms for safe and unsafe. A further investigation addresses defined questions; its need, scope, and authorization must be established rather than inferred from a missing document.',
    phrases='''Identify the outstanding source | The tank-closure record has not arrived.
Name completed work | The scheduled visit, interviews, and available records review are complete.
Limit the conclusion | We cannot say that no further questions remain.
Separate absence from proof | A missing record does not prove either a release or its absence.
Request professional review | Please assess the significance of this gap.
Preserve a classification | We have not classified the gap as significant.
State the existing scope | Sampling is outside the current Phase I scope.
Avoid an automatic next step | No Phase II investigation has been authorized.
Give a traceable request | I will follow up with the archive.
Distinguish a commitment | Tuesday at 14:00 is our status-update time.
Avoid a receipt promise | The archive has not guaranteed delivery by then.
Qualify the summary | The conclusion remains subject to review of the outstanding information.
Keep the source visible | Cite the missing record beside the qualification.
Explain the purpose | Further investigation would address a defined unresolved question.
Clarify authority | A proposed investigation is not permission to start.
Close the handoff | I will report the archive response and any continuing limitation.''',
    notes='''Has not arrived | Describes a missing source without speculating about its contents.
No further questions | A broad conclusion unsupported by the outstanding review.
Significance | Refers to the gap's effect on interpretation, not simply its existence.
Subject to review | Makes an unresolved condition explicit.
Outside scope | Identifies work not included in the current agreement.
By versus at | Delivery by a time differs from an update at that time.''',
    d='''Which summary is supported? | The tank-closure record remains outstanding, and its significance requires review. | Missing paperwork proves contamination. | The completed visit proves the site is clean. | Phase II work starts automatically tomorrow. | The accurate summary names the missing source and preserves the unresolved professional assessment.
Who assesses the gap's significance? | Eric in the environmental-professional role | The buyer solely because of the purchase deadline | The archive delivery driver | Any reader who prefers a definite answer | Eric holds the stated professional-review role; commercial pressure does not replace that assessment.
Which statement improperly broadens the scope? | Sampling is already authorized under this Phase I assignment. | The archive request remains open. | A follow-up investigation may need a defined scope. | The summary needs a qualification. | The brief excludes sampling from the current scope and provides no further investigation authorization.
What should Maya report if the record is still missing on Tuesday? | The outstanding status and the continuing review limitation | That delivery occurred because the update was promised | A guessed tank-closure date | A final absence-of-release finding | The update commitment remains valid even if the requested source is still unavailable.''',
    dialogue='''Maya | The draft says no further questions remain. We have finished the visit and interviews, but the tank-closure record is still missing. Can that sentence stay?
Eric | No. The outstanding record creates a [[data gap::Data gap identifies missing relevant information without deciding its significance or proving an environmental condition.]]. We need to describe it before I assess how it affects the conclusions. Completed work does not erase that unresolved source.
Maya | The buyer wants a short answer today. Would it be fair to say that the missing document means the property has an environmental problem?
Eric | That also goes too far. A missing document is not evidence of a [[release::A release concerns a substance escaping into the environment, not merely an absent administrative record.]]. We must distinguish the absence of information from a finding about what happened at the property.
Maya | The archive might send it tomorrow, although it has given no commitment. I can follow up and identify the request number in our project record.
Eric | Good. Retain that [[follow-up request::The follow-up request traces the effort to obtain missing information without treating the request as successful receipt.]] and any response. Do not imply that the source is unavailable forever simply because it has not arrived for this draft.
Maya | Should I label the gap significant now so that nobody overlooks it? That would certainly draw attention to the outstanding record in the summary.
Eric | Do not preempt the [[professional opinion::The professional opinion evaluates the evidence and the gap's significance; emphasis alone cannot supply that assessment.]]. We can make the issue prominent without deciding its significance before the relevant assessment. The distinction matters to the client.
Maya | Another colleague suggested scheduling samples immediately. Sampling is not in our present assignment, and the client has not approved any additional investigation.
Eric | Then keep the [[scope of inquiry::The scope of inquiry defines the existing assessment work; it does not automatically expand when a question remains unresolved.]] explicit. A further investigation would need a defined question, appropriate professional input, and the necessary authorization. This conversation does not supply those things.
Maya | I will avoid saying that Phase II work has started. Can the summary list the work completed while clearly leaving the record question open?
Eric | Yes. Revise the [[executive summary::The executive summary should communicate both major findings and material qualifications instead of replacing them with blanket reassurance.]] to name the outstanding tank-closure record and the pending significance review. Do not bury the qualification where a reader is unlikely to see it.
Maya | Could the buyer interpret pending review as proof that every other source is unreliable? We have useful interviews and historical records already.
Eric | Describe the specific [[source limitation::The source limitation concerns the outstanding record; it does not automatically invalidate every other source or completed assessment step.]], not a wholesale failure. The other material remains part of the evidence, with its own context. Precision avoids both false reassurance and unnecessary alarm.
Maya | I will contact the archive and update you Tuesday at fourteen hundred, whether or not the record arrives. That gives us a clear next contact.
Eric | Correct. The update is not [[authorization::Authorization permits specified work; a communication deadline neither authorizes sampling nor determines the investigation outcome.]] for sampling or a promise of a final conclusion. Keep the two commitments separate when explaining the next step to the buyer.
Maya | The revised wording will say the outstanding information requires your review. It will not say the site is clean or that contamination has been established.
Eric | That preserves the [[records review::Records review examines documentary evidence; an incomplete source set must be described accurately rather than treated as a definitive site finding.]] position. We can explain exactly what is complete, what remains missing, and who will evaluate the consequence without guessing the answer.
Maya | I will circulate that revision with the archive request reference and the Tuesday update time. No additional field work will be represented as approved.
Eric | Agreed. Keep the [[subject property::Subject property identifies the actual site under assessment, so qualifications are not silently expanded into claims about other properties.]] and assessment boundaries clear throughout. The client needs a useful, limited statement grounded in this site's evidence, not a slogan about every possible environmental condition.''',
    transfer_title='Repair a second assessment update',
    transfer_setup='For the Park site, an old solvent-storage record is missing. Nora will assess its significance. The current assignment excludes sampling. An archive status update is due Friday at 11:00.',
    transfer='''Consultant: "The outstanding source is the ___ record." | solvent-storage | The supplied case identifies the solvent-storage record, not a tank document.
Reviewer: "The person assessing significance is ___." | Nora | Nora is explicitly assigned the significance review in this separate case.
Consultant: "The present assignment excludes ___." | sampling | Sampling is outside the stated scope and cannot be presented as authorized.
Reviewer: "The archive status update is due ___." | Friday at 11:00 | The stated time concerns a status update rather than guaranteed source receipt.'''))


BOOK['units'].append(unit(
    title='Sampling Plans and Data Quality',
    scene='Trace a missing custody signature without inventing it',
    skill='Describe a documentation deviation and distinguish review status from data acceptance.',
    brief='Project plan P6 requires a receiving signature for the direct handoff from the field team to the laboratory custodian. For sample GW03, the sender signed, the receiving-signature box is blank, and the laboratory receipt log records arrival at 16:25. The bottle identifier matches the submission sheet. An analytical result is available, but quality reviewer Jonas has not decided its usability for the project question. Field coordinator Elena must report the discrepancy, preserve the original record, and seek a traceable clarification. These are stated project requirements, not universal rules about carrier signatures.',
    cast='Elena | Field coordinator\nJonas | Quality reviewer',
    culture=('Investigate the gap without accusing a colleague', 'A missing signature can trigger blame before the event has been established. Describe the exact field and supporting records. Request a documented clarification rather than asking someone to fill a blank as though the original record had always been complete.'),
    a='''What is missing? | The laboratory custodian's receiving signature | The sample identifier on every bottle | The analytical result | The sender's signature | The receiving-signature box is blank, while the other named information is available.
What does the receipt log establish in this case? | Recorded laboratory arrival at 16:25 | A complete custody record | Guaranteed analytical accuracy | A final usability decision | The log provides a recorded arrival time but does not replace the missing signature or quality review.
What is the correct current data status? | Usability remains under review. | The result is automatically invalid. | The result is approved for every purpose. | The signature has already been reconstructed. | Jonas has not decided usability, so neither automatic rejection nor unrestricted acceptance is supported.''',
    vocabulary='''sampling plan | A document defining the intended collection and analysis of samples. | follow the sampling plan
data quality objective (DQO) | A statement of the data needed to support a specified decision. | define a data quality objective
quality assurance project plan (QAPP) | A plan describing quality requirements and activities for a project. | review the QAPP
chain of custody (COC) | The documented possession and transfer history of a sample or evidence. | maintain chain of custody
custodian | A person responsible for possession or care of a sample. | identify the receiving custodian
sample identifier | The unique label linking a sample to its records. | verify the sample identifier
receipt log | A record of received items and associated information. | check the receipt log
transfer signature | A signature documenting a specified custody handoff. | obtain the required transfer signature
deviation | A departure from a stated procedure or requirement. | document a deviation
traceable amendment | A recorded correction that preserves the original and identifies the change. | make a traceable amendment
holding time | The specified period allowed before a sample-related preparation or analysis step. | review the holding time
preservation | Measures specified to maintain a sample's relevant condition. | document sample preservation
field blank | A control sample used to evaluate potential contamination associated with field handling. | assess a field blank
trip blank | A control accompanying samples to assess specified transport-related contamination. | review a trip blank
equipment blank | A control used to evaluate contamination associated with sampling equipment. | examine an equipment blank
field duplicate | An additional field sample used to assess aspects of sampling and analytical variability. | compare a field duplicate
laboratory control sample | A known control used to assess laboratory analytical performance. | review a laboratory control sample
method blank | A control assessing contamination from laboratory preparation or analytical processes. | evaluate a method blank
reporting limit | A stated concentration or level below which results are not reported quantitatively under the method. | state the reporting limit
detection limit | A method-related level associated with detecting an analyte under stated conditions. | identify the detection limit
qualifier | A notation communicating a limitation or condition attached to a result. | interpret a data qualifier
data validation | A systematic evaluation of data against specified requirements. | conduct data validation
data usability | Suitability of data for a defined question or decision. | assess data usability
corrective record | Documentation of a correction or follow-up action. | retain the corrective record''',
    precision='A receipt log and matching identifier provide relevant evidence, but they do not supply a missing signature. Conversely, the missing signature does not itself prove tampering, contamination, or that every result is unusable.',
    precision_extra='Apply the stated project requirement to this direct field-to-laboratory handoff. Do not generalize it to every common-carrier transfer. Any amendment must preserve the original and accurately identify its timing, basis, and author.',
    phrases='''Locate the gap | The receiving-signature box for GW03 is blank.
Identify the requirement | Project plan P6 requires that signature for this handoff.
Preserve the evidence | Keep the original record unchanged.
State corroborating information | The receipt log records arrival at 16:25.
Check identity | The bottle identifier matches the submission sheet.
Avoid an accusation | We have not established why the signature is missing.
Separate result and acceptance | An analytical result is available; usability is still under review.
Request a clarification | Please provide a traceable account of the handoff.
Avoid fabrication | Do not sign as though the original entry had been completed.
Name the reviewer | Jonas will evaluate the documentation and data context.
Limit the conclusion | The gap alone does not prove that the sample was contaminated.
Avoid automatic acceptance | Matching labels do not resolve every quality question.
State the intended use | Assess suitability for the stated project question.
Keep qualifications attached | Carry relevant qualifiers into the report.
Document a correction | Identify the amendment's author, date, and evidential basis.
Close the issue accurately | The deviation remains open pending the quality review.''',
    notes='''Available versus usable | A reported result may still await suitability review.
Blank box | An observation about a specific record, not an accusation.
For this handoff | Restricts the requirement to the supplied project context.
As though | Signals a misleading reconstruction of an earlier record.
For the stated purpose | Limits a usability conclusion to its actual decision context.
Pending review | Does not mean either accepted or rejected.''',
    d='''Which action preserves traceability? | Retain the original and request a dated, attributed clarification. | Replace the original with an undated clean copy. | Ask someone to imitate the missing signature. | Delete the receipt log to make the records consistent. | A traceable clarification preserves the original and identifies the later explanation rather than concealing the gap.
Which statement is supported? | The log records receipt at 16:25, but the receiving signature remains missing. | The log proves every custody requirement was met. | A matching bottle proves the method had no error. | Every unsigned transfer universally invalidates every result. | The accurate statement combines the available record with its unresolved documentation limitation.
What question should guide usability review? | Can these data support the defined project question, given the quality evidence? | Can we make the report look complete? | Can the signature be added without anyone noticing? | Can all quality records be omitted? | Data usability concerns a defined purpose and the relevant evidence, not cosmetic completeness.
Which claim is an unsupported accusation? | Someone tampered with GW03. | A signature is missing. | The identifier matches the submission sheet. | The receipt log records 16:25. | No supplied evidence establishes tampering; the missing signature requires investigation rather than accusation.''',
    dialogue='''Elena | GW03 has an analytical result, but its receiving-signature box is blank. The sender signed. How should I describe this?
Jonas | Call it a documented [[deviation::Deviation names the departure from this project's signature requirement without inventing why it happened.]] from project plan P6. That plan requires the laboratory custodian's signature for this direct handoff. Keep the description limited to the observed gap.
Elena | The laboratory log records arrival at sixteen twenty-five. The bottle identifier also matches the submission sheet sent with the sample.
Jonas | Include the [[receipt log::The receipt log supplies recorded arrival evidence but does not recreate the missing receiving signature.]] as supporting evidence. Those records matter, but neither the arrival entry nor matching label fills the empty signature box or ends the review.
Elena | A colleague suggested asking the custodian to sign the original without a note, so that the document looks complete.
Jonas | We need a [[traceable amendment::A traceable amendment preserves the original and identifies the later correction, author, timing, and basis.]], not a reconstruction presented as an original entry. Preserve the record and request an attributed account of the handoff through the applicable quality process.
Elena | Should I tell the client that the result is invalid until we receive that account? The report deadline is approaching.
Jonas | Say [[data usability::Data usability concerns whether evidence can support the defined project question; its review is not automatic rejection.]] remains under review. We have not reached a rejection or acceptance decision. A documentation gap needs evaluation in context, not a conclusion chosen to sound decisive.
Elena | The client may ask whether the missing signature proves that someone changed the bottle or contaminated its contents.
Jonas | It does not establish either allegation. Describe the [[chain of custody::Chain of custody documents sample possession and transfers; a gap prompts review without itself proving tampering.]] gap accurately and refer the question to the review. Avoid turning missing documentation into an accusation about a person's conduct.
Elena | Could I at least say that matching labels establish that the analytical value is correct? That seems reassuring but perhaps too broad.
Jonas | The matching [[sample identifier::The sample identifier links the bottle to its records; it does not establish analytical accuracy by itself.]] supports identity checks. Analytical quality involves other evidence. We should not use one matching field to certify every aspect of collection, handling, preparation, and analysis.
Elena | I will attach the original form, receipt log, submission sheet, and any later clarification. Is the intended project decision also relevant?
Jonas | Yes. The [[data quality objective::The data quality objective specifies what evidence the project decision needs, giving the usability review its purpose.]] helps define what the data must support. Review suitability for that question rather than treating usable as an unrestricted label for every possible application.
Elena | The report writer wants to remove qualification symbols because they make the table harder to read. What should I tell her?
Jonas | Keep each relevant [[qualifier::A qualifier communicates a result's limitation or condition and must not disappear merely for a cleaner presentation.]] attached and explain it clearly. Readability is important, but a cleaner table must not silently strip away limitations that affect interpretation of the results.
Elena | I will leave the issue open, send the evidence package, and ask for your review status before the report is finalized.
Jonas | Good. [[Data validation::Data validation evaluates evidence against requirements; it is distinct from simply receiving an analytical result.]] and the usability decision need their own status. The presence of a number in a laboratory report does not show that these review steps are complete.
Elena | My update will identify the blank receiving signature, the corroborating records, and the pending decision. It will not blame the custodian.
Jonas | That works. Retain the eventual [[corrective record::The corrective record documents the follow-up without erasing the original gap or pretending the review was always complete.]] alongside the original evidence. Once a decision is made, state its basis and any limits, rather than merely replacing pending with an unexplained approved label.''',
    transfer_title='Report another custody discrepancy',
    transfer_setup='For sample SW08, the project-required receiving signature is blank. The receipt log states 10:40. Mina owns the usability review, which is still pending.',
    transfer='''Coordinator: "The affected sample is ___." | SW08 | SW08 is the identifier supplied for this separate documentation case.
Reviewer: "The receipt log records ___." | 10:40 | Ten forty is the recorded receipt time, not a fabricated signature time.
Coordinator: "The review owner is ___." | Mina | Mina is explicitly responsible for the usability review in the supplied facts.
Reviewer: "The usability decision remains ___." | pending | The case gives no completed decision, so pending preserves its status.'''))

BOOK['units'].append(unit(
    title='Permitting and Agency Coordination',
    scene='Clarify the requested modeling scenario',
    skill='Ask a bounded agency question without presenting an assumption as a requirement.',
    brief='Agency comment C7 asks the Delta project team to add wet-weather modeling. The submission already includes a dry-weather baseline. Comment C7 does not state the storm duration, intensity, or return period to use. Consultant Arun thinks the agency may mean a 100-year event, but that interpretation is unconfirmed. Agency coordinator Becca will seek written clarification using the existing comment reference and a concise list of missing parameters. A response package is scheduled internally for Friday; the agency has not promised a clarification date. No revised scenario or permit approval has been issued.',
    cast='Arun | Modeling consultant\nBecca | Agency coordinator',
    culture=('A precise question can save an entire revision', 'Teams sometimes avoid clarification because they fear appearing inexperienced. State what is understood, isolate the missing parameters, and ask for confirmation. A bounded question demonstrates control of the submission without pretending that an ambiguous comment is complete.'),
    a='''What does C7 explicitly request? | Additional wet-weather modeling | A confirmed 100-year event | Immediate permit approval | Deletion of every existing model | The comment requests wet-weather modeling but leaves the event parameters unspecified.
What is Arun's 100-year interpretation? | An unconfirmed assumption | A written agency instruction | An approved permit condition | A completed simulation | Arun proposes an interpretation that the agency has not confirmed.
What does Friday represent? | An internal response-package target | An agency-guaranteed reply date | The permit issue date | Automatic approval of the dry-weather model | The team has an internal target, but the agency has made no clarification-date commitment.''',
    vocabulary='''permit application | A request for authorization under an applicable permitting process. | submit a permit application
agency comment | A reviewing authority's documented question or requested change. | respond to an agency comment
comment-response matrix | A table linking each comment to a response and supporting material. | update the comment-response matrix
modeling scenario | A defined set of conditions evaluated in a model. | specify a modeling scenario
baseline condition | The reference condition against which alternatives are evaluated. | define the baseline condition
wet-weather event | A rainfall-related condition relevant to the assessment. | characterize a wet-weather event
dry-weather flow | Flow under the specified conditions without the modeled rainfall contribution. | estimate dry-weather flow
storm duration | The period over which a storm event is represented. | confirm the storm duration
rainfall intensity | The rate of rainfall over a specified interval. | state rainfall intensity
return period | A statistical expression of event frequency under specified assumptions. | specify the return period
annual exceedance probability | The estimated chance an event magnitude is exceeded in a given year. | explain annual exceedance probability
boundary condition | A specified condition imposed at the edge or interface of a model. | document a boundary condition
model domain | The spatial or conceptual extent represented in a model. | define the model domain
input parameter | A value supplied to a model. | confirm an input parameter
calibration | Adjustment of model parameters against relevant observations. | document model calibration
sensitivity analysis | Evaluation of how outputs change when inputs or assumptions change. | conduct sensitivity analysis
submission package | The documents and data formally provided for review. | revise the submission package
review cycle | A round of submission, assessment, and response. | plan the review cycle
written clarification | A documented explanation resolving an ambiguity. | obtain written clarification
assumption register | A record of assumptions and their confirmation status. | maintain an assumption register
permit condition | A requirement attached to an issued authorization. | interpret a permit condition
technical memorandum | A focused document explaining a technical issue or analysis. | prepare a technical memorandum
response deadline | The required or agreed time for a response, as applicable. | verify the response deadline
version identifier | A label distinguishing one document or model issue from another. | retain the version identifier''',
    precision='A 100-year return period does not mean an event occurs exactly once every century. It expresses frequency statistically under stated assumptions. Here, no return period has been specified by the agency.',
    precision_extra='An internal Friday target is not an agency response deadline or an approval date. Record the missing parameters and the clarification request without representing a proposed model run as an agreed requirement.',
    phrases='''Cite the comment | We are responding to comment C7.
State what is clear | The comment requests wet-weather modeling.
Name the existing case | The submission includes a dry-weather baseline.
Identify missing inputs | The duration, intensity, and return period are unspecified.
Label the interpretation | The 100-year event is our unconfirmed interpretation.
Ask a bounded question | Please confirm the event parameters intended for C7.
Avoid assumed agreement | We have not received written clarification.
Keep the record organized | Link the reply to the comment-response matrix.
Separate target and promise | Friday is our internal package target.
Protect accuracy | Do not call a proposed scenario an agency requirement.
Clarify the model boundary | Confirm whether the existing model domain remains applicable.
Preserve versions | Identify which model issue the response addresses.
Report the dependency | The revised scenario depends on clarification of these inputs.
Request a usable response | A written parameter set will let us scope the revision.
Avoid approval language | No permit approval has been issued.
Close the coordination | I will report the clarification status against C7.''',
    notes='''Requests versus specifies | A request can establish the task while leaving parameters unresolved.
We understand | Introduces an interpretation that should remain open to confirmation.
Intended | Asks what the authority meant rather than asserting it.
Internal target | A planning date controlled by the team, not an agency promise.
Depends on | Names an unresolved input needed for the next step.
Issued | Refers to an actual authorization, not a predicted outcome.''',
    d='''Which agency question is most useful? | For C7, please confirm the storm duration, intensity, and return period. | Can you approve everything now? | Why was your comment so vague? | We used a 100-year storm because you required it. | The useful question references the comment and asks for the specific missing parameters without blame or invention.
Which statement overstates the agency's instruction? | C7 requires a 100-year event. | C7 requests wet-weather modeling. | The duration is unspecified. | We need written clarification. | The supplied comment does not state a return period, so the asserted requirement is unsupported.
What should the response matrix show before clarification arrives? | The open parameter question and clarification-request status | A fabricated approval date | A closed comment with no response | A claim that no additional modeling was requested | An accurate matrix preserves the unresolved question and the actual status of the team's request.
What does a 100-year return period not mean? | Exactly one occurrence every hundred years | A statistical frequency expression under stated assumptions | A parameter requiring appropriate interpretation | A concept distinct from storm duration | Return period is statistical and does not schedule one event at fixed century intervals.''',
    dialogue='''Arun | C7 asks for wet-weather modeling. I think they mean a hundred-year event, but the comment does not actually say that.
Becca | Then put that interpretation in the [[assumption register::The assumption register records an unconfirmed interpretation without converting it into an agency instruction.]]. Mark it unconfirmed. We should ask what the reviewer intends before describing a particular storm as a requirement.
Arun | The submitted model covers a dry-weather baseline. It does not include the additional rainfall case, so the request itself is understandable.
Becca | Agreed. Distinguish the requested [[modeling scenario::The modeling scenario requires defined conditions; the broad request does not supply every necessary event parameter.]] from its missing inputs. We can acknowledge the wet-weather request while asking for the duration, intensity, and return period.
Arun | Would a general question asking what they want be enough? I worry that a long message will slow the response.
Becca | Use a concise [[written clarification::Written clarification creates a traceable interpretation of the agency's request instead of relying on an undocumented guess.]] request tied to C7. List only the unresolved parameters and state which baseline is already included. That makes the question easier to answer.
Arun | I will not call the hundred-year event an agency instruction. Should I explain that return period is different from storm duration?
Becca | Yes, where needed. The [[return period::Return period expresses event frequency statistically; it is neither storm duration nor a guarantee of once-per-century occurrence.]] describes statistical frequency under stated assumptions, not how long a storm lasts or a fixed interval between occurrences. Keep those terms separate.
Arun | Our manager wants the response package on Friday. The agency has not told us when it will provide the missing parameters.
Becca | Report Friday as an internal [[response deadline::Here the response deadline is the team's internal target; it must not be represented as an agency commitment.]] for our package, not a promised agency reply. If clarification remains outstanding, identify the dependency and the actual status rather than pretending it arrived.
Arun | The project team also asked whether receiving a clarification would mean the permit is effectively approved. That seems like another leap.
Becca | It would not establish a [[permit condition::A permit condition belongs to an issued authorization; clarification of a modeling request is not permit issuance.]] or permit approval by itself. A clarification can define the requested analysis without deciding whether the eventual submission satisfies the permitting process.
Arun | I will track the request and response under C7. We need readers to find the same question across the correspondence and revised package.
Becca | Use the [[comment-response matrix::The comment-response matrix links the original comment, response, and supporting evidence while keeping unresolved items visible.]] for that connection. Leave the item open until its actual response status supports a change. Do not close it merely because we sent an email.
Arun | There may also be a question about whether the current model boundary remains appropriate. Can we include that without introducing an entirely new assignment?
Becca | Ask whether the existing [[model domain::The model domain defines the represented extent; confirming its applicability is more precise than silently changing that extent.]] remains applicable to the requested scenario. Keep it a clarification question, not an assertion that the agency has ordered additional geographic coverage.
Arun | When the reply arrives, the modeler will need to know which existing issue it refers to. We have two internal versions.
Becca | Include the [[version identifier::The version identifier ties the clarification to the correct model issue and prevents mismatched assumptions across revisions.]] in the technical record. Otherwise, a correct parameter can still be applied to the wrong model issue, creating another avoidable review problem.
Arun | The message will identify C7, the existing baseline, the missing parameters, and our internal target. It will ask for confirmation without promising an outcome.
Becca | Good. Keep the [[submission package::The submission package should contain the actual agreed analysis and traceable responses, not unsupported claims of agency approval.]] consistent with that exchange. When we know the intended scenario, we can plan the revision and describe what remains to be reviewed.''',
    transfer_title='Clarify a second agency comment',
    transfer_setup='Comment C12 requests noise modeling but leaves the operating hours and receptor locations unspecified. Dev owns the clarification request. Monday is the internal package target.',
    transfer='''Consultant: "The unresolved comment reference is ___." | C12 | C12 is the specific agency reference supplied for this separate case.
Coordinator: "One missing input is the operating ___." | hours | Operating hours are explicitly unspecified and must not be guessed.
Consultant: "The clarification owner is ___." | Dev | Dev is assigned the clarification request in the given facts.
Coordinator: "The internal package target is ___." | Monday | Monday is the team's target, not an agency-guaranteed reply or approval.'''))


BOOK['units'].append(unit(
    title='Remediation Options and Risk',
    scene='Faster implementation is not necessarily a shorter project',
    skill='Compare alternatives on a stated basis without choosing a technical solution from incomplete evidence.',
    brief='Client representative Omar asks consultant Tess which of two preliminary remediation options is best. Option A estimates four weeks of implementation at $120,000, followed by 12 months of monitoring at $5,000 per month. Option B estimates two weeks of implementation at $90,000, followed by 24 months of monitoring at the same monthly amount. All amounts are undiscounted planning estimates with no escalation or other costs included. Technical suitability, regulatory acceptability, and actual completion criteria remain unassessed. Neither option is authorized. Tess must compare the stated time and cost components without recommending a remedy from these figures alone.',
    cast='Omar | Client representative\nTess | Environmental consultant',
    culture=('Replace best with a defined comparison', 'A client may ask for one clear winner when the evidence supports several limited comparisons. Answer the specific cost and time questions directly, then identify the unresolved technical and acceptance criteria that prevent a complete recommendation.'),
    a='''Which option has the lower implementation estimate? | B at $90,000 | A at $120,000 | Both at $90,000 | Neither has a cost estimate | B's stated implementation estimate is lower, but that component excludes its longer monitoring period.
What is A's stated monitoring cost? | $60,000 | $5,000 | $120,000 | $180,000 | Twelve months multiplied by five thousand dollars gives sixty thousand dollars for A's monitoring component.
What remains unresolved? | Technical suitability and regulatory acceptability | Every implementation estimate | The monthly monitoring amount | Whether the options have different monitoring periods | The brief explicitly leaves technical suitability, regulatory acceptability, and completion criteria unassessed.''',
    vocabulary='''remediation | Work intended to address environmental contamination under defined objectives. | evaluate remediation options
remedial objective | A defined outcome that a remediation approach aims to achieve. | establish a remedial objective
conceptual site model | A representation of sources, pathways, receptors, and relevant site conditions. | refine the conceptual site model
source area | The location from which contamination originates or is concentrated. | characterize the source area
exposure pathway | A route linking a contaminant source to a potential receptor. | evaluate an exposure pathway
receptor | A person or ecological entity potentially exposed to a contaminant. | identify a potential receptor
contaminant of concern | A substance selected for further evaluation in the site context. | identify a contaminant of concern
feasibility | Practical suitability of an approach under the relevant conditions. | assess technical feasibility
treatability study | An investigation of how a treatment may perform for particular material or conditions. | scope a treatability study
in situ treatment | Treatment performed in place rather than after removing the affected material. | evaluate in situ treatment
ex situ treatment | Treatment of affected material after removal from its original location. | compare ex situ treatment
containment | Measures intended to limit contaminant movement or exposure. | assess a containment approach
monitored natural attenuation | A monitored strategy relying on natural processes under appropriate evaluated conditions. | evaluate monitored natural attenuation
institutional control | A non-engineered restriction or mechanism intended to limit exposure or use. | document an institutional control
engineering control | A physical measure intended to reduce exposure or contaminant movement. | maintain an engineering control
implementation period | Time allocated to carrying out the specified installation or active work. | estimate the implementation period
monitoring period | Time during which specified conditions or performance are checked. | define the monitoring period
performance criterion | A measure used to evaluate whether an approach meets its objective. | specify a performance criterion
residual risk | Risk remaining after specified controls or actions. | evaluate residual risk
life-cycle cost | Cost across the defined stages and period of an option. | compare life-cycle costs
undiscounted estimate | An estimate that does not adjust future amounts to present value. | present an undiscounted estimate
contingency allowance | An amount reserved for specified uncertainty in a cost estimate. | define the contingency allowance
regulatory acceptability | Whether an approach meets the relevant authority's applicable expectations or requirements. | assess regulatory acceptability
completion criterion | A defined condition required to establish completion. | confirm the completion criterion''',
    precision='A totals $180,000 and B totals $210,000 on the stated implementation-plus-monitoring basis. These are undiscounted estimates, not complete life-cycle costs or proof that A is technically preferable.',
    precision_extra='B has a shorter estimated implementation period but a longer monitoring period. Neither the two-week nor four-week figure establishes when the whole remediation obligation ends; completion criteria remain unresolved.',
    phrases='''Define the question | Best depends on the criteria we are comparing.
Compare the initial component | B has the lower implementation estimate.
Add the monitoring component | A includes 12 months of monitoring at $5,000 per month.
State the limited total | A totals $180,000 on this stated basis.
Contrast the second total | B totals $210,000 on the same stated basis.
Name the calculation | These are undiscounted planning estimates.
Preserve exclusions | No escalation or other costs are included.
Separate duration measures | Implementation time is not the full monitoring period.
Avoid a completion promise | Two weeks does not establish project completion.
Name the unresolved evidence | Technical suitability remains unassessed.
Keep approval separate | Neither option has been authorized.
Request the decision criteria | We need the relevant performance and acceptance criteria.
Avoid a false winner | The lower stated total is not a complete recommendation.
Explain the trade-off | B starts with a lower implementation cost but more monitoring months.
Limit the claim | This comparison addresses only the supplied components.
Close the discussion | Record the cost comparison and the questions requiring technical review.''',
    notes='''On this basis | Restricts a conclusion to included components and assumptions.
Implementation versus completion | Active work can end before monitoring or other obligations end.
Lower versus best | A numerical ranking is not a full technical recommendation.
Undiscounted | Future amounts are added without present-value adjustment.
Remains unassessed | States that suitability has not yet been determined.
Authorized | Requires actual permission, not preference for a preliminary estimate.''',
    d='''What is B's stated combined total? | $210,000 | $90,000 | $120,000 | $180,000 | Ninety thousand plus twenty-four times five thousand equals two hundred ten thousand dollars.
Which comparison is accurate? | B has shorter implementation but longer monitoring. | B completes every obligation in two weeks. | A has no monitoring cost. | Both have identical monitoring periods. | The supplied periods are two versus four implementation weeks and twenty-four versus twelve monitoring months.
Which recommendation exceeds the evidence? | Select A because its lower stated total proves technical suitability. | A's limited total is $30,000 lower. | Both options need further technical assessment. | The estimates exclude other costs. | The cost difference does not establish whether either remedy is technically suitable or acceptable.
What should appear beside the totals? | Included components, undiscounted basis, exclusions, and unresolved criteria | A guarantee that costs cannot change | An assertion of regulator approval | A claim that monitoring is unnecessary | The comparison depends on its stated components and assumptions, while technical and acceptance questions remain unresolved.''',
    dialogue='''Omar | B looks best: ninety thousand dollars and two weeks. Why would we choose the option costing more and taking longer?
Tess | Those are the [[implementation period::Implementation period covers the stated active work, not the later monitoring or all completion obligations.]] and its associated cost. B also has twenty-four months of monitoring. We need to compare the same components before drawing a broader conclusion.
Omar | A has twelve monitoring months, and both use five thousand dollars per month. What does that make the monitoring totals?
Tess | A's [[monitoring period::Monitoring period determines the number of monthly costs in this limited comparison: twelve for A and twenty-four for B.]] adds sixty thousand dollars; B's adds one hundred twenty thousand. Those amounts belong beside the implementation figures, not outside the comparison merely because they occur later.
Omar | So A is one hundred eighty thousand overall, and B is two hundred ten thousand, assuming only these stated components.
Tess | Correct. Each is an [[undiscounted estimate::An undiscounted estimate adds the stated future amounts without present-value adjustment and does not remove uncertainty or exclusions.]]. We have not adjusted future amounts to present value or added escalation and other costs. Do not present either number as a fixed complete price.
Omar | That reverses the initial ranking. Could I now tell management that A is definitely the recommended solution because it costs less?
Tess | Not yet. [[Feasibility::Feasibility concerns practical suitability under site conditions; the limited cost calculation does not establish it.]] remains unassessed. A lower total on this basis does not prove that A will work at the site or satisfy the relevant performance and acceptance requirements.
Omar | Does B's shorter implementation mean the whole project finishes earlier?
Tess | No. We do not have the [[completion criterion::The completion criterion defines when obligations are fulfilled; implementation duration alone cannot establish that endpoint.]] needed to make that claim. Installation duration and overall completion are different. The longer monitoring requirement also matters when describing what follows implementation.
Omar | I see. We need to distinguish the physical work from the subsequent checks, and avoid making the short schedule sound like final closure.
Tess | Exactly. A [[performance criterion::A performance criterion states how success will be evaluated; a short schedule does not demonstrate that outcome.]] tells us what an approach must achieve. Until those requirements and the technical evidence are assessed, neither schedule is a guarantee of a successful remedy.
Omar | The client team also wants to know whether the regulator will accept either proposal. Do these preliminary estimates tell us that?
Tess | They do not establish [[regulatory acceptability::Regulatory acceptability requires relevant review against applicable expectations; a commercial estimate does not supply that decision.]]. We should name that as unresolved rather than imply acceptance. Technical suitability, authority requirements, cost, and timing are related questions, but they are not interchangeable answers.
Omar | How should we label the comparison table so that management still gets a useful result without mistaking it for a complete recommendation?
Tess | Call it the stated implementation-plus-monitoring comparison. Avoid claiming a complete [[life-cycle cost::Life-cycle cost spans defined stages and costs; this limited table excludes other costs and is not a complete analysis.]] assessment. Put the amounts, periods, exclusions, and unresolved criteria together where the reader can see the limits immediately.
Omar | Could unforeseen work change either total? We have not included a reserve or any amount for uncertain additional work in these figures.
Tess | Yes. No [[contingency allowance::A contingency allowance addresses specified cost uncertainty; none is included in the supplied figures, so it cannot be assumed.]] is included here. That does not mean uncertainty is absent. It means this comparison has not assigned an additional amount to it.
Omar | I will report A's lower stated total and B's shorter implementation, then list technical suitability, acceptance, and completion criteria as unresolved.
Tess | That is balanced. Keep the [[remedial objective::The remedial objective defines the environmental outcome sought; choosing a price or schedule does not establish that the outcome is achievable.]] central when the qualified team develops its recommendation. Neither preliminary option is authorized simply because we have clarified the arithmetic or expressed a preference.''',
    transfer_title='Compare a smaller proposal',
    transfer_setup='Option C estimates $40,000 implementation plus six monitoring months at $2,000 monthly. Option D estimates $35,000 plus twelve months at $2,000. Other costs are excluded; suitability remains unassessed.',
    transfer='''Consultant: "C's monitoring component is ___ dollars." | 12,000 | Six monitoring months at two thousand dollars total twelve thousand dollars.
Client: "C's stated combined estimate is ___ dollars." | 52,000 | Forty thousand plus twelve thousand equals fifty-two thousand on the limited basis.
Consultant: "D's stated combined estimate is ___ dollars." | 59,000 | Thirty-five thousand plus twenty-four thousand equals fifty-nine thousand on the same basis.
Client: "Technical suitability remains ___." | unassessed | The brief explicitly leaves suitability unresolved despite the completed arithmetic.'''))

BOOK['units'].append(unit(
    title='Regulatory Compliance and Audits',
    scene='A documented action is not automatically a closed finding',
    skill='Report audit status using explicit evidence, ownership, and closure categories.',
    brief='A fictional facility review has six findings, F1-F6. Four have documented corrective-action plans and assigned owners. Of those four, F1 and F2 also have verified effectiveness evidence and are closed under the local review process. F3 and F4 remain open because their effectiveness checks are pending. F5 and F6 have neither a documented action plan nor an assigned owner. Coordinator Ruby and review lead Ian must correct a dashboard that calls all four planned findings closed. Ian will secure ownership for F5 and F6; the next status review is Thursday at 15:00, not a promise that all findings will be resolved.',
    cast='Ruby | Compliance coordinator\nIan | Review lead',
    culture=('Report progress without changing the definition', 'Teams want visible progress, and a completed plan can feel like a completed problem. Recognize the planning milestone while keeping closure tied to the stated evidence. Consistent categories make the report useful rather than pessimistic.'),
    a='''How many findings are verified closed? | Two | Four | Six | None | F1 and F2 have the required effectiveness evidence and are closed under the stated local process.
How many findings remain open? | Four | Two | Six | Three | F3-F6 remain open: two await effectiveness checks and two lack plans and owners.
What is missing for F5 and F6? | Both a documented action plan and an assigned owner | Only the original finding identifier | Only a dashboard color | A verified closure date despite completed evidence | The brief explicitly states that F5 and F6 have neither plans nor owners.''',
    vocabulary='''compliance obligation | An applicable requirement that an organization must meet. | identify a compliance obligation
audit scope | The defined coverage and boundaries of an audit or review. | agree the audit scope
audit criterion | A requirement or benchmark used to evaluate evidence. | identify the audit criterion
objective evidence | Verifiable information supporting a finding or conclusion. | examine objective evidence
finding | A documented result of comparing evidence with review criteria. | record a finding
nonconformity | A failure to meet a specified requirement. | document a nonconformity
observation | A noted condition whose classification depends on the review process. | record an observation
corrective-action plan | A documented proposal to address an identified problem and its cause. | approve a corrective-action plan
correction | Action addressing a detected problem or instance. | document the immediate correction
corrective action | Action aimed at removing a cause to prevent recurrence. | verify corrective action
root cause | An underlying cause relevant to preventing recurrence. | investigate the root cause
action owner | The person accountable for a specified follow-up action. | assign an action owner
target date | A planned completion or review date. | agree a target date
effectiveness check | Evaluation of whether an action achieved its intended result. | complete an effectiveness check
closure evidence | Information supporting closure under the applicable process. | retain closure evidence
open finding | A finding not yet meeting the stated closure requirements. | track an open finding
overdue action | An action not completed by its applicable due date. | escalate an overdue action
recurring finding | A finding involving a problem identified again. | investigate a recurring finding
audit trail | Records allowing actions and decisions to be traced. | preserve the audit trail
evidence register | An organized record linking evidence to review items. | update the evidence register
closure rate | The proportion of defined findings meeting the stated closure condition. | calculate the closure rate
management review | A structured leadership review of relevant performance and issues. | prepare for management review
escalation route | The defined path for raising an unresolved matter. | use the escalation route
verification status | The recorded stage of checking a claim or action. | report verification status''',
    precision='Two of six findings are closed, approximately 33.3%. Four of six have plans, approximately 66.7%. These percentages measure different states. Neither percentage alone establishes facility-wide compliance.',
    precision_extra='A correction fixes an instance; corrective action addresses a cause to prevent recurrence. A plan for either is not proof of implementation or effectiveness. Use the local closure definition supplied in this case.',
    phrases='''Correct the headline | Four findings have plans, but only two are closed.
State the denominator | The review contains six findings in total.
Name the closed items | F1 and F2 have verified effectiveness evidence.
Describe the pending checks | F3 and F4 remain open pending effectiveness checks.
Identify the ownership gap | F5 and F6 have no assigned owner.
Separate milestones | A documented plan is not verified closure.
Calculate consistently | The verified closure rate is two out of six.
Limit the percentage | That is approximately 33.3% of this review's findings.
Preserve the remaining work | Four findings remain open.
Assign the next coordination | Ian will secure ownership for F5 and F6.
Avoid a false deadline | Thursday at 15:00 is the status review.
Ask for evidence | Link each closure to its supporting record.
Distinguish action types | An immediate correction does not automatically address recurrence.
Use the agreed criterion | Apply the local effectiveness-based closure process.
Prevent silent relabeling | Do not change the closure definition to improve the dashboard.
Close the handoff | Bring the owner updates and pending evidence to Thursday's review.''',
    notes='''Have plans | Describes documentation status, not completed implementation.
Verified closed | Adds the evidence requirement supplied by this case.
Two out of six | Makes the denominator visible before giving a percentage.
Remain open | Includes both pending checks and unassigned work.
Secure ownership | Commits to coordination, not instant resolution of the finding.
This review | Limits the conclusion to the defined scope.''',
    d='''Which dashboard headline is accurate? | Two closed, two awaiting effectiveness checks, two without plans or owners. | Four closed because four plans exist. | All six compliant because a review occurred. | No progress because four findings remain open. | The accurate headline preserves all three distinct states supplied in the brief.
What is the verified closure rate? | Approximately 33.3% | Approximately 66.7% | 100% | 50% | Two verified closures divided by six total findings gives approximately thirty-three point three percent.
What must not be inferred from Thursday's review time? | All findings will be resolved by then. | Ian will report ownership progress. | Pending evidence will be discussed. | The team will update the status. | A status-review appointment is not a commitment that every corrective action will be complete.
Which record best supports closure in this case? | Verified effectiveness evidence linked to the finding | A plan title alone | A more positive dashboard color | An unassigned reminder | The local process explicitly requires effectiveness evidence rather than the mere existence of a plan.''',
    dialogue='''Ruby | The dashboard shows four of six findings closed. I traced the count to the four corrective-action plans, but that seems wrong.
Ian | It is. A [[corrective-action plan::A corrective-action plan documents intended work; its existence alone does not establish implementation or verified effectiveness.]] records what is intended. Only F1 and F2 have the verified effectiveness evidence required for closure under our local process. Correct the headline.
Ruby | F3 and F4 have owners and plans, but their effectiveness checks are pending. They should not disappear from the open list.
Ian | Keep each as an [[open finding::An open finding has not met the stated closure requirements, even if a plan and owner already exist.]]. We can acknowledge the planning progress while retaining the unresolved verification. Progress and closure are different categories, and both deserve an accurate place on the dashboard.
Ruby | F5 and F6 are a different problem. Neither has an owner or a documented plan, so their next steps are unclear.
Ian | I will secure an [[action owner::The action owner is accountable for follow-up; assigning that person is necessary coordination, not evidence that the finding is resolved.]] for each. Until that is confirmed, do not put my name in the owner field as though the action responsibility has already been settled.
Ruby | You are coordinating the assignment, not necessarily taking responsibility for both corrective actions. I will show that distinction in the status note.
Ian | Exactly. Use the [[escalation route::The escalation route raises unresolved responsibility through the agreed process rather than hiding the ownership gap in the report.]] if the ownership decision remains unresolved. An empty field needs visible follow-up, but an invented owner would only make the report appear more complete.
Ruby | For the summary percentage, two divided by six gives approximately thirty-three point three percent. Four plans would be approximately sixty-six point seven percent.
Ian | Label the first [[closure rate::Closure rate uses findings meeting the closure condition as its numerator; here that is two of six, not four planned actions.]]. Label the other as plan coverage if we include it. Do not use the larger percentage with the closure label, even if the calculation itself is correct.
Ruby | Could a reader interpret the closure percentage as saying the whole facility is thirty-three percent compliant? That would not be our intended meaning.
Ian | Tie it to the [[audit scope::Audit scope limits what the review covers; a finding-closure percentage cannot establish a percentage of overall facility compliance.]]. It describes these six findings under this review, not the proportion of all facility obligations being met. The denominator needs a plain-language explanation.
Ruby | I will link F1 and F2 to the verification records. A dashboard reader should be able to locate the basis for closure.
Ian | Put those references in the [[evidence register::The evidence register links each claimed closure to its supporting information, making the status reviewable rather than merely asserted.]]. A closed label without the supporting record is harder to check and easier to misinterpret when the next reviewer takes over.
Ruby | For F3 and F4, I will show the checks as pending. I will not claim that the actions failed simply because verification is incomplete.
Ian | Correct. An [[effectiveness check::An effectiveness check evaluates the action's result; pending means that evaluation is incomplete, not necessarily that the action failed.]] still pending is not evidence of failure or success. Preserve that distinction when discussing progress with the teams responsible for the actions.
Ruby | Thursday at fifteen hundred is the next status review. Should the slide call that the deadline for closing all remaining findings?
Ian | No. That [[target date::The target date here is for a status review, not a promised completion date for every corrective action.]] concerns our review meeting. Bring the ownership updates and verification status. Do not turn a coordination appointment into a resolution promise that the action teams have not made.
Ruby | The corrected dashboard will show two closed, two awaiting effectiveness checks, and two lacking plans and owners. It will keep the six-finding denominator.
Ian | Good. Preserve the [[audit trail::The audit trail records how evidence and decisions support status changes, including the correction of a misleading dashboard count.]] for this correction too. We want the next reader to understand why the number changed, rather than assume the underlying findings suddenly became worse.''',
    transfer_title='Fix another closure report',
    transfer_setup='A separate review has eight findings: three verified closed, two with plans awaiting effectiveness checks, and three with neither plans nor owners. The next status review is Monday.',
    transfer='''Coordinator: "The number verified closed is ___." | three | Three findings explicitly meet the verified-closure condition in the supplied case.
Reviewer: "The number still open is ___." | five | Eight total findings minus three verified closures leaves five open findings.
Coordinator: "The verified closure rate is ___." | 37.5% | Three divided by eight equals thirty-seven point five percent of this review's findings.
Reviewer: "The next status review is ___." | Monday | Monday is the review appointment, not a guaranteed resolution date.'''))


BOOK['units'].append(unit(
    title='Sustainability and ESG Reporting',
    scene='A partial electricity estimate cannot support a company-wide claim',
    skill='Define emissions-reporting boundaries and replace an unsupported headline with a precise statement.',
    brief='Sustainability analyst Ana has estimated 40 metric tonnes of carbon dioxide equivalent from purchased electricity used at two offices during 2025. The calculation excludes the factory, company vehicles, purchased heat, and value-chain emissions. It has not undergone independent assurance. Communications manager Leo has drafted the headline "Our company is carbon neutral." No company-wide inventory or substantiation for that claim is available. Ana and Leo must replace the headline, name the included offices, period, and electricity source, and list the exclusions. They must not imply that omitted sources have zero emissions or that an estimate has been independently verified.',
    cast='Ana | Sustainability analyst\nLeo | Communications manager',
    culture=('A narrower claim can be more credible', 'Communications teams value simple messages, while technical teams need boundaries and qualifications. Collaborate on a clear positive description of what was actually measured. Do not treat a shorter headline as permission to remove the scope that makes the statement true.'),
    a='''What does the 40-tonne estimate cover? | Purchased electricity at two offices during 2025 | The entire company and value chain | All factory emissions | Only emissions from company vehicles | The calculation explicitly covers purchased electricity for two offices in the stated year.
Which headline is unsupported? | Our company is carbon neutral. | We estimated electricity-related emissions for two offices. | The calculation excludes the factory. | Independent assurance has not been completed. | A partial electricity estimate does not substantiate a company-wide carbon-neutrality claim.
What must not be inferred from excluded sources? | Their emissions are zero. | They are outside this calculation. | The inventory is incomplete for a company-wide claim. | More work is needed to assess the broader footprint. | Exclusion means a source was not included, not that it produced no emissions.''',
    vocabulary='''greenhouse gas (GHG) | A gas that contributes to the atmosphere's heat-trapping effect. | quantify greenhouse gas emissions
carbon dioxide equivalent (CO2e) | A common unit expressing different gases using a specified warming-potential basis. | report tonnes of CO2e
emissions inventory | An accounting of emissions within defined boundaries and a period. | compile an emissions inventory
organizational boundary | The operations included under the chosen organizational accounting approach. | define the organizational boundary
operational boundary | The categories of emissions included in an inventory. | describe the operational boundary
Scope 1 | Direct emissions from sources owned or controlled within the inventory boundary. | report Scope 1 emissions
Scope 2 | Indirect emissions from generation of purchased or acquired energy consumed by the organization. | calculate Scope 2 emissions
Scope 3 | Other indirect value-chain emissions within the applicable accounting framework. | assess Scope 3 categories
purchased electricity | Electricity obtained from an external supplier for consumption. | quantify purchased electricity use
purchased heat | Heat acquired from an external source for use. | account for purchased heat
value chain | Activities upstream and downstream associated with an organization's products or operations. | map the value chain
activity data | Measured or estimated activity used in calculating emissions. | collect activity data
emission factor | A coefficient relating an activity to an emissions quantity. | document the emission factor
global warming potential (GWP) | A measure comparing a gas's warming effect over a specified time horizon. | state the GWP basis
reporting year | The period assigned to an emissions or sustainability report. | specify the reporting year
base year | A reference year used for a defined comparison or target. | establish a base year
location-based method | A Scope 2 method reflecting average emissions associated with the relevant grids. | describe the location-based method
market-based method | A Scope 2 method using applicable contractual instruments under relevant criteria. | document the market-based method
assurance | An independent evaluation of reported information under an agreed engagement. | obtain independent assurance
reporting boundary | The defined extent of what a report includes. | disclose the reporting boundary
carbon-neutrality claim | An assertion about balancing or neutralizing emissions under a specified substantiated basis. | substantiate a carbon-neutrality claim
avoided emissions | Estimated emissions not occurring relative to a specified counterfactual. | distinguish avoided emissions
carbon credit | A unit representing a specified quantified emissions reduction or removal under a program. | examine carbon credit documentation
retirement | The recorded use of a credit that removes it from further use under its registry rules. | verify credit retirement''',
    precision='Scope 2 is not limited to electricity: it can include purchased or acquired steam, heat, and cooling. This case includes only electricity at two offices, not the entire company or all Scope 2 sources.',
    precision_extra='CO2e aggregates gases using a specified warming-potential basis. It is not the same as electricity consumption. An inventory figure, an avoided-emissions estimate, and a carbon credit are different quantities that cannot simply replace one another.',
    phrases='''Name the measured activity | The estimate covers purchased electricity at two offices.
State the reporting period | The reporting year is 2025.
Give the correct unit | The estimate is 40 metric tonnes of CO2e.
Limit the boundary | This is not a company-wide emissions inventory.
Correct the headline | The evidence does not support a carbon-neutrality claim.
Preserve exclusions | The factory, vehicles, purchased heat, and value chain are excluded.
Avoid a zero assumption | Excluded does not mean zero emissions.
State assurance status | Independent assurance has not been completed.
Explain Scope 2 carefully | Purchased energy categories extend beyond electricity.
Keep methods visible | Document the calculation method and emission factors.
Separate the quantities | Electricity use and CO2e are different measures.
Avoid unsupported comparisons | We have not established a comparable base year.
Protect the claim | Keep the boundary beside the reported figure.
Avoid substitution | A credit purchase is not a complete emissions inventory.
Ask for substantiation | What evidence supports the proposed public claim?
Close accurately | Publish the limited estimate with its period, boundary, and qualifications.''',
    notes='''Estimated | Signals a calculated result without implying independent verification.
At two offices | Restricts the organizational coverage of this calculation.
Company-wide | A broader boundary that this evidence does not support.
Excluded | Describes omission, not the amount emitted.
Assured versus prepared | Independent evaluation is different from producing the calculation.
CO2e versus kWh | Emissions units and electricity-consumption units answer different questions.''',
    d='''Which replacement headline is supported? | Estimated 2025 purchased-electricity emissions for two offices: 40 tonnes CO2e. | Company-wide emissions eliminated. | All Scope 2 sources independently verified. | Factory and fleet emissions confirmed as zero. | The accurate headline preserves the activity, two-office boundary, year, estimate status, and unit.
Which statement about Scope 2 is accurate? | It can include purchased heat, steam, and cooling as well as electricity. | It always means only office electricity. | It means every value-chain emission. | It excludes all acquired energy. | Scope 2 covers relevant purchased or acquired energy categories, not only the electricity subset in this case.
What does lack of independent assurance mean here? | The estimate must not be described as independently assured. | The number is automatically proven false. | All emissions are therefore zero. | The company is automatically carbon neutral. | No assurance engagement has established independent assurance, but its absence does not itself prove the estimate false.
Which question addresses the headline's main defect? | Does the evidence cover and substantiate the company-wide claim? | Can the number be printed in a larger font? | Can excluded sources be called zero without calculation? | Can the year be removed to shorten the sentence? | The main defect is the mismatch between a narrow calculation and a broad unsubstantiated claim.''',
    dialogue='''Leo | The headline says our company is carbon neutral. I assumed the forty-tonne estimate covered the whole footprint.
Ana | It is a limited [[emissions inventory::An emissions inventory has defined boundaries; this calculation covers only the stated electricity sources rather than the whole company.]] calculation for purchased electricity at two offices in 2025. It excludes the factory, vehicles, purchased heat, and value chain. That headline is unsupported.
Leo | The number is not necessarily wrong. My wording assigns it a broader meaning than the calculation supports.
Ana | Exactly. Keep the [[reporting boundary::The reporting boundary states what is included, preventing a partial office estimate from becoming a company-wide assertion.]] beside the number. We can communicate the estimate clearly without claiming that every operation or every relevant emissions source has been included.
Leo | I will name the two offices and year. The unit is tonnes of carbon dioxide equivalent, not kilowatt-hours of electricity consumed.
Ana | Correct. [[CO2e::CO2e expresses emissions on a common warming-potential basis; it is not a unit of electricity consumption.]] is the emissions unit. Electricity consumption is activity data used in the calculation, alongside the applicable factors and method. Keep those quantities distinct in the table and headline.
Leo | Can I say we have completed Scope 2 reporting? I thought Scope 2 was simply purchased electricity, which is what this file calculates.
Ana | [[Scope 2::Scope 2 includes relevant purchased or acquired energy, so selected office electricity is only a subset of its potential coverage.]] can include purchased steam, heat, and cooling as well as electricity. This file covers only two offices and excludes purchased heat. Do not describe it as complete company-wide Scope 2 reporting.
Leo | The excluded factory and company vehicles must remain visible. Otherwise a reader could assume they were checked and contributed no emissions.
Ana | Yes. Relevant direct sources may fall within [[Scope 1::Scope 1 concerns direct emissions from owned or controlled sources under the chosen boundary; omitted sources cannot be presumed zero.]], depending on the organizational boundary. Excluding a source from this calculation says nothing by itself about whether that source emits zero, forty, or any other amount.
Leo | What about suppliers and customer use? Those are not included either, so our statement should not imply that we measured them.
Ana | Keep the relevant [[Scope 3::Scope 3 addresses other indirect value-chain emissions under the framework, which are outside this limited calculation.]] boundary explicit. The applicable categories require their own assessment. A two-office electricity figure cannot stand in for upstream and downstream emissions simply because it is the number currently available.
Leo | The team prepared the estimate internally. I have no independent assurance report. Should I describe the figure as verified to make the wording confident?
Ana | No. [[Assurance::Assurance is an independent evaluation under an agreed engagement; internal preparation alone does not establish that status.]] has not been completed. Say estimated and give the calculation boundary. Accurate confidence comes from describing what we have, not borrowing a status the evidence does not support.
Leo | Someone suggested purchasing forty credits and retaining the carbon-neutral headline. We have no company-wide inventory or substantiation package for that claim.
Ana | A [[carbon credit::A carbon credit is a separate quantified unit under a program; purchasing it does not supply a complete inventory or substantiate every claim.]] purchase would not repair the missing boundary or establish the whole claim. Its quality, use, and relevant claim requirements would need their own evidence and review.
Leo | Could we compare this estimate with last year instead? I do not have a matching calculation for the same two offices and methodology.
Ana | Then do not invent a [[base year::A base year provides a defined comparison reference; no comparable prior-year calculation is supplied in this case.]] comparison. A reduction claim needs a comparable basis and supporting data. We can report the current limited estimate without claiming a trend that has not been established.
Leo | The revised headline will state estimated 2025 purchased-electricity emissions for two offices: forty metric tonnes of CO2e. The exclusions will appear immediately below.
Ana | Good. Keep the [[emission factor::The emission factor links activity data to the calculated emissions and should be documented with the method and boundary.]] and method documentation traceable in the supporting material. That gives readers a precise statement and reviewers a basis to examine, without implying company-wide neutrality or independent assurance.''',
    transfer_title='Narrow another emissions headline',
    transfer_setup='A calculation estimates 12 tonnes CO2e from purchased electricity at one warehouse in 2024. Fuel use and transport are excluded. Independent assurance has not been completed.',
    transfer='''Analyst: "The estimated emissions are ___ tonnes CO2e." | 12 | Twelve is the emissions quantity supplied for this separate limited calculation.
Editor: "The included location is one ___." | warehouse | The calculation covers one warehouse, not every company operation.
Analyst: "The reporting year is ___." | 2024 | The supplied reporting period is 2024 and must remain attached to the figure.
Editor: "Independent assurance has ___ been completed." | not | The brief explicitly states that independent assurance has not been completed.'''))

BOOK['units'].append(unit(
    title='Community and Stakeholder Meetings',
    scene='Answer a safety question without extending the evidence',
    skill='Acknowledge residents and explain preliminary results in plain language with precise boundaries.',
    brief='Consultant Suki and community representative Daniel are preparing a public meeting about a fictional environmental study. Preliminary laboratory results cover water samples from locations S1, S2, and S3 collected on one June morning and tested for the listed analytes. For analyte X, each result is below the laboratory reporting limit. Other locations, other dates, and unlisted substances are outside these results. The study has not established area-wide safety or a drinking-water determination. Suki will explain these limits, record questions, and direct requests for current health or water-use advice to the responsible public authority without inventing advice.',
    cast='Daniel | Community representative\nSuki | Environmental consultant',
    culture=('Answer the human question as well as the technical one', 'Residents are asking about daily decisions, not merely laboratory vocabulary. Acknowledge that practical concern before explaining the evidence. Avoid using uncertainty as a reason to withdraw from the conversation or using reassurance as a substitute for a qualified answer.'),
    a='''What does the sampling cover? | Three locations on one June morning | Every location in every season | Every substance in the area | All drinking-water decisions | The brief limits the results to three locations, one collection period, and the listed analytes.
What does below the reporting limit establish? | The laboratory did not report a quantitative value at or above that limit for X. | The entire area is safe. | Every substance is absent. | X is proven to be exactly zero everywhere. | A below-limit result is tied to the laboratory reporting basis and does not prove universal absence or safety.
Where should requests for current health or water-use advice go? | The responsible public authority | An invented rule from the consultant | A guess based on one chart | A guarantee from the meeting audience | The consultant must refer these advice questions to the responsible authority rather than inventing a determination.''',
    vocabulary='''stakeholder | A person or group affected by or interested in a project. | engage a stakeholder
community liaison | A contact connecting a project team with affected community members. | appoint a community liaison
public meeting | A gathering for sharing information and receiving public questions. | prepare a public meeting
sampling location | The place where a sample was collected. | identify the sampling location
sampling event | A defined occasion or period of sample collection. | describe the sampling event
analyte | A substance or property targeted by an analysis. | list the target analytes
preliminary result | A result not yet at the final review or reporting stage. | qualify a preliminary result
non-detect | A result indicating an analyte was not detected at the stated analytical threshold. | explain a non-detect
quantitation | Determination of an amount or concentration under the method's conditions. | describe the quantitation limit
screening level | A comparison value used to identify matters needing further evaluation. | interpret a screening level
cleanup level | An applicable concentration or criterion used in a defined cleanup context. | identify the applicable cleanup level
exposure assessment | Evaluation of how, how much, and under what conditions exposure may occur. | conduct an exposure assessment
spatial coverage | The geographic extent represented by the data. | explain spatial coverage
temporal coverage | The period or times represented by the data. | explain temporal coverage
representativeness | The extent to which data reflect the conditions relevant to a question. | evaluate representativeness
uncertainty | A limitation in knowledge or confidence about a result or inference. | communicate uncertainty
risk communication | Exchange of information about risks, evidence, and relevant uncertainties. | improve risk communication
plain-language summary | An account using accessible words while preserving the meaning. | prepare a plain-language summary
question log | A record of questions and their follow-up status. | maintain a question log
responsible authority | The body with the relevant responsibility for the matter. | contact the responsible authority
public advisory | An official notice giving relevant information or guidance to the public. | check the current public advisory
meeting record | Documentation of discussion, questions, and commitments. | circulate the meeting record
follow-up contact | A named person or channel for subsequent communication. | provide a follow-up contact
area-wide claim | A statement applied to an entire geographic area. | qualify an area-wide claim''',
    precision='Below the reporting limit does not mean zero. It also does not describe untested substances, places, or dates. Distinguish the laboratory statement from a conclusion about health or allowable water use.',
    precision_extra='A screening level identifies a need for further evaluation in context; it is not automatically a cleanup standard or a universal safe/unsafe boundary. This fictional case supplies no threshold for a health determination.',
    phrases='''Acknowledge the concern | I understand that you need information for everyday decisions.
State the sampling coverage | These results cover S1, S2, and S3 on one June morning.
Name the tested substance | This statement concerns analyte X.
Explain the result | X was below the laboratory reporting limit in these samples.
Avoid an absence claim | Below the limit does not mean proven zero.
Preserve the stage | These results are preliminary.
Limit the geography | We cannot extend them to every location in the area.
Limit the time | One sampling event does not represent every season.
Keep untested substances separate | The report does not characterize substances that were not analyzed.
Avoid a health guarantee | This study has not established an area-wide safety determination.
Answer respectfully | That is a reasonable question, but these results do not answer it fully.
Refer the advice question | Please consult the responsible public authority for current water-use advice.
Avoid inventing guidance | I will not create a drinking-water instruction from this chart.
Record the question | We will include that request in the question log.
Provide continuity | The meeting record will identify the follow-up contact.
Close with the evidence | We will distinguish the measured findings from the questions still open.''',
    notes='''These samples | Keeps a statement attached to its actual evidence.
Below the limit | Does not mean absent, harmless, or unmeasurable by every method.
Preliminary | Names the reporting stage without declaring the result false.
Everywhere and always | Expand spatial and temporal coverage beyond this study.
Current advice | Requires the responsible authority's actual guidance, not a guessed instruction.
Does not answer fully | Acknowledges a relevant question without manufacturing certainty.''',
    d='''Which public statement is accurate? | X was below the reporting limit in these three preliminary samples. | X is absent from the entire area. | Every water source is safe to drink. | No further question is possible anywhere. | The supported statement preserves the analyte, sample count, analytical limit, and preliminary status.
Which phrase improperly expands time coverage? | The area is safe in every season. | The samples were collected on one June morning. | This is one sampling event. | Other dates are outside these results. | Every season claims evidence beyond the single collection period supplied in the case.
How should Suki respond to a drinking-water question? | Acknowledge the concern and refer current advice to the responsible authority. | Invent a rule from the below-limit result. | Guarantee safety because three samples exist. | Refuse to record the question because it is inconvenient. | The study does not establish drinking-water advice, so Suki should acknowledge the question and use the appropriate referral.
Which comparison is correct? | Screening levels and cleanup levels serve different purposes. | Every screening value is automatically a cleanup standard. | A screening exceedance proves a specific health outcome. | A below-limit result replaces an exposure assessment. | Screening values support further evaluation and are not automatically the applicable cleanup criteria or a health determination.''',
    dialogue='''Daniel | Residents will ask whether the results prove the whole area is safe. They need to know what this means for their families.
Suki | I understand that concern. Start with the actual [[spatial coverage::Spatial coverage identifies represented places; three sampling locations do not characterize the whole area.]]: locations S1, S2, and S3. We should not imply that these three points represent every location or every possible exposure in the area.
Daniel | The chart shows X below the reporting limit at all three locations. Some readers will interpret that as no X anywhere.
Suki | Explain the [[analyte::Analyte names the tested substance; the result concerns X rather than every possible substance.]] and the limit together. The laboratory did not report a quantitative value at or above its reporting limit for X in these samples. That is not proof of zero.
Daniel | Would calling it a clean result be simpler? A string of qualifications could sound evasive.
Suki | Use a [[plain-language summary::A plain-language summary simplifies wording without replacing the result's limits with a misleading label.]], but avoid clean as a blanket label. Say what was tested, where, and when. Then explain that the result does not establish conditions at untested locations or for unlisted substances.
Daniel | We should name the June collection date. Otherwise the chart could appear to describe the whole year.
Suki | Exactly. The [[temporal coverage::Temporal coverage identifies represented times; one morning does not establish conditions throughout the year.]] is limited. One sampling event does not show seasonal variation or every later condition. A clear date helps readers understand what the study actually observed.
Daniel | If someone asks whether they can drink water from a particular source, can we answer from these results alone?
Suki | No. We need to identify the [[responsible authority::The responsible authority provides current advice; the consultant must not invent guidance from these limited results.]] for current health or water-use advice. These preliminary study results have not established a drinking-water determination. We must not improvise one during the meeting.
Daniel | I want that referral to sound helpful rather than like passing the question away. Residents deserve a clear route to an answer.
Suki | Provide the appropriate [[follow-up contact::A follow-up contact offers further communication without implying that the study answers the water-use question.]] and record the question. Explain why the study does not answer it, and distinguish that limitation from unwillingness to listen or help them locate the relevant guidance.
Daniel | Someone may bring a screening-level table from another report. Should we tell them any number below that table is automatically safe?
Suki | No. A [[screening level::A screening level supports further evaluation, not an automatic cleanup criterion or universal safety determination.]] has a defined purpose and assumptions. It is not automatically a cleanup standard or a universal dividing line between safe and unsafe for every place, substance, and exposure.
Daniel | The meeting materials should also make clear that the results are preliminary. Does that mean we should avoid discussing them at all?
Suki | We can discuss each [[preliminary result::A preliminary result can be explained with its stage and limits; preliminary does not mean false.]] accurately. State the stage and limitations, and avoid final claims it cannot support. Withholding every explanation would leave readers to supply their own, possibly broader interpretation.
Daniel | I will organize the questions by topic and identify which ones the study can answer and which need a separate response.
Suki | Maintain a [[question log::The question log keeps community concerns and their follow-up status visible, including unresolved questions.]] with the follow-up status. Do not mark a question answered merely because someone spoke about a related issue. The record should show the actual response or remaining need.
Daniel | Our closing message will give the three locations, one June morning, listed analytes, below-limit result for X, and the limits on wider conclusions.
Suki | Good. Keep [[risk communication::Risk communication combines accurate evidence and uncertainty with respectful attention to affected people's practical concerns.]] both precise and respectful. We can acknowledge the practical concern, explain the evidence, and provide a route for further advice without claiming that this limited dataset establishes area-wide safety.''',
    transfer_title='Limit another public summary',
    transfer_setup='A preliminary soil report covers locations P1 and P2 sampled on 8 May. It reports analyte Y only. The report does not characterize other locations, dates, or substances.',
    transfer='''Consultant: "The report covers ___ locations." | two | P1 and P2 are the two locations explicitly included in the report.
Resident: "The collection date was ___." | 8 May | Eight May is the supplied sampling date, not a claim about other periods.
Consultant: "The reported analyte is ___." | Y | Y is the only analyte included in this separate report.
Resident: "The results are still ___." | preliminary | The supplied report is preliminary and must not be presented as a final determination.'''))


BOOK['units'].append(unit(
    title='Proposal, Scope, and Client Expectations',
    scene='Price the additional work before promising its delivery',
    skill='Clarify a change request, distinguish locations from samples, and negotiate a documented next step.',
    brief='The signed assignment covers six sampling locations during one site visit, followed by the agreed laboratory work and report. Client manager Grace requests four additional locations and a second visit. Project manager Malik has not assessed the additional methods, sample quantities, laboratory work, access requirements, cost, or schedule. Under this fictional agreement, additional field work requires a written approved change before it starts. Malik will provide a change-estimate status on Wednesday at 12:00; that is not a field-visit or report-delivery commitment. The existing six-location scope remains unchanged unless the parties approve a change.',
    cast='Grace | Client manager\nMalik | Project manager',
    culture=('Cooperation does not require an instant promise', 'A client may hear a scope boundary as resistance. Acknowledge the request, identify the concrete information needed to price it, and give a useful next contact. Keep willingness to assess the change separate from authorization or a delivery guarantee.'),
    a='''What does the existing agreement cover? | Six locations during one visit, with agreed laboratory work and report | Ten locations across two approved visits | Unlimited sampling whenever requested | Only a proposal with no defined locations | The signed assignment specifies six locations and one visit; the requested additions are not yet approved.
What is requested as additional work? | Four more locations and a second visit | Four fewer locations | Elimination of laboratory analysis | Immediate acceptance of a final report | Grace requests four additional locations and another visit beyond the existing agreement.
What does Wednesday at 12:00 represent? | A change-estimate status update | A confirmed field start | Guaranteed final report delivery | Automatic change approval | Malik promises an estimate-status update, not delivery, field access, or approval of additional work.''',
    vocabulary='''scope of work | The agreed tasks, boundaries, and deliverables of an assignment. | define the scope of work
deliverable | A specified output supplied under an agreement. | confirm the deliverable
assumption | A condition used in planning that needs appropriate confirmation. | document a pricing assumption
exclusion | Work or cost explicitly outside an agreed scope or estimate. | state the exclusion
change request | A proposed modification to agreed work. | assess a change request
change authorization | Approval permitting a defined modification under the applicable agreement. | obtain change authorization
additional service | Work beyond the existing agreed services. | price an additional service
fee estimate | A projected charge based on stated work and assumptions. | prepare a fee estimate
cost breakdown | An allocation of a total estimate into named components. | provide a cost breakdown
mobilization | Preparing and moving resources to begin field activity. | estimate mobilization costs
demobilization | Removing resources and closing out field presence after activity. | account for demobilization
site access | Permission and practical arrangements for entering a location. | confirm site access
sample count | The number of samples specified for collection or analysis. | verify the sample count
analytical suite | The set of tests or analytes included in an analytical assignment. | define the analytical suite
laboratory turnaround | The specified or estimated time for laboratory completion under stated conditions. | confirm laboratory turnaround
reporting allowance | Planned time or resources for preparing and reviewing the report. | include a reporting allowance
dependency | An input or event needed before another step can proceed. | identify a schedule dependency
lead time | The period needed before a resource, service, or activity is available. | check the lead time
schedule impact | The effect of a proposed change on planned timing. | assess the schedule impact
not-to-exceed amount | A stated spending limit subject to the agreement's terms and scope. | confirm the not-to-exceed amount
acceptance condition | A requirement used to determine whether a deliverable is accepted. | define the acceptance condition
work order | A document authorizing or specifying work under the relevant arrangement. | issue a work order
commercial review | Evaluation of proposed scope, price, and contractual terms. | complete commercial review
client sign-off | Documented client approval under the applicable process. | obtain client sign-off''',
    precision='Six existing locations plus four requested locations would make ten locations if approved. That does not automatically mean ten samples: the sampling design, controls, depths, and analytical requirements determine the sample count.',
    precision_extra='Laboratory turnaround is only one schedule component. Access, mobilization, collection, review, and reporting may also matter. Wednesday at 12:00 is a status-update commitment, not a promise that those dependencies will be resolved.',
    phrases='''Acknowledge the request | You are requesting four additional locations and a second visit.
Restate the agreement | The current scope covers six locations during one visit.
Separate willingness and approval | We can assess the request; it is not yet authorized.
Clarify quantities | Ten locations would not automatically mean ten samples.
Identify the needed detail | We need the methods, sample quantities, and analytical requirements.
Keep access visible | The second visit also depends on site-access arrangements.
Name the commercial step | We will assess the additional cost and schedule.
Avoid a free-work assumption | Additional work is not included merely because it is discussed.
State the local condition | This agreement requires an approved written change before extra field work.
Give the next commitment | I will provide an estimate-status update Wednesday at 12:00.
Limit that commitment | That is not a field-start or report-delivery date.
Separate timing components | Laboratory turnaround is not the complete project schedule.
Preserve the current scope | The existing six-location assignment remains unchanged.
Request an explicit decision | The change proposal will need client sign-off.
Record the basis | The estimate will state its assumptions and exclusions.
Close constructively | I will bring the cost, timing, and open dependencies together for review.''',
    notes='''Would if approved | Describes a conditional expanded scope, not an existing commitment.
Locations versus samples | Different units that must not be counted interchangeably.
Can assess | Expresses willingness to evaluate, not authorization to perform.
Before extra work | States the supplied agreement's condition, not a universal contract rule.
Status update | A communication commitment rather than a delivery promise.
Remains unchanged | Protects the original agreement while a proposal is considered.''',
    d='''If the request is approved, how many locations would be included? | Ten locations, with sample count still to be determined | Exactly ten samples in every case | Four locations in total | Twelve automatically approved locations | Six plus four gives ten locations, but the brief does not establish the number of samples.
Which reply is cooperative and accurate? | We can assess the extra work and provide estimate status Wednesday at noon. | We will start the extra visit tomorrow at no charge. | The change is already approved because you asked. | Laboratory turnaround guarantees the final report date. | The accurate reply offers a concrete assessment step without inventing authorization, cost, or delivery commitments.
What is required before extra field work under this agreement? | An approved written change | A casual mention in a meeting | An assumed approval from silence | A preferred date in a draft estimate | The fictional agreement expressly requires approved written authorization for the additional field work.
Which schedule statement is unsupported? | The laboratory turnaround equals the full report-delivery period. | Site access is an unresolved dependency. | The added visit needs schedule assessment. | The estimate update is due Wednesday at noon. | Laboratory work is only one component; collection, review, access, and reporting also affect the schedule.''',
    dialogue='''Grace | We need four more locations and a second visit. Can your team add those to the assignment and keep the existing report date?
Malik | We can assess that [[change request::The change request proposes extra work; it does not itself amend the agreement or authorize performance.]]. The signed scope currently covers six locations in one visit. We have not yet assessed the added work, cost, access, or schedule impact.
Grace | I thought four extra locations would simply mean four extra samples. Would that make ten samples altogether once we add them?
Malik | It would make ten locations if approved, but the [[sample count::Sample count depends on the sampling design and quality requirements, not simply the number of locations.]] remains to be determined. Methods, depths, quality controls, and analytical needs can affect the number. We should not price an unsupported quantity.
Grace | I can explain the request and provide the access contact. What else does the estimate need?
Malik | We need the proposed [[analytical suite::The analytical suite defines the testing included; changing locations does not by itself specify the laboratory work required.]] and relevant methods, along with the sample quantities and field arrangements. The estimate should state those assumptions so you can see exactly what it covers.
Grace | The site contact has not confirmed entry for the second visit. I would prefer not to hold up the entire discussion while that is checked.
Malik | We can develop the proposal while recording [[site access::Site access is an unresolved practical dependency; drafting a proposal does not establish permission or a confirmed visit.]] as an unresolved dependency. We cannot turn a preferred visit date into a confirmed field commitment before the necessary arrangements and authorization are in place.
Grace | Can you update me Wednesday at noon? I have a budget discussion that afternoon.
Malik | I can provide the [[fee estimate::The fee estimate projects charges on a defined basis; the promised status update does not guarantee every pricing input will be resolved.]] status then. If inputs remain outstanding, I will identify them clearly. That is a communication commitment, not a guarantee that the added visit or final report happens that day.
Grace | That distinction is fine. Please show the extra field work and laboratory costs separately, so the budget reviewer understands what changes.
Malik | I will provide a [[cost breakdown::The cost breakdown separates estimate components so the client can review what the proposed change adds and excludes.]] with the assumptions and exclusions. A single unexplained total would make it harder to identify whether the proposed work matches your request or whether anything important remains omitted.
Grace | If the laboratory offers a five-day turnaround, can we tell our internal team that the final report will arrive five days after approval?
Malik | No. [[Laboratory turnaround::Laboratory turnaround covers the stated laboratory service period, not all access, collection, review, and reporting steps.]] is only one component. We also need to consider access, mobilization, collection, review, and report preparation. Its starting point and conditions must be confirmed rather than assumed.
Grace | I do not want the team to lose a possible field date while paperwork circulates. Does today's discussion authorize them to reserve and perform the visit?
Malik | It does not provide [[change authorization::Change authorization requires the approved written change specified by this agreement; discussion or interest alone does not permit extra field work.]]. Under this agreement, extra field work requires an approved written change before it starts. We can discuss availability without representing the work itself as authorized.
Grace | Please keep the existing assignment clear. The original six locations have not been cancelled.
Malik | The current [[scope of work::The scope of work remains the agreed six-location assignment until the parties approve a change; a request does not silently replace it.]] remains unchanged. We will identify the proposed additions separately and assess their interaction with the existing schedule. Nothing in this request automatically cancels the original assignment.
Grace | Then Wednesday's update will cover estimate status, open inputs, and timing questions. Once the written proposal is ready, I will arrange the approval review.
Malik | Agreed. Obtain the required [[client sign-off::Client sign-off documents approval under the agreement; arranging a review is not the same as receiving that approval.]] through the stated process before additional work proceeds. We can be responsive while keeping the quantities, costs, dependencies, and authorization status visible to both teams.''',
    transfer_title='Confirm a smaller scope change',
    transfer_setup='A current agreement covers five locations in one visit. The client requests three additional locations and a second visit. Sample count is unresolved, and an approved written change is required before extra field work.',
    transfer='''Manager: "The proposed expanded scope would cover ___ locations." | eight | Five existing plus three requested locations equals eight if the change is approved.
Client: "The requested visit would be the ___ visit." | second | The client requests a second visit beyond the one already agreed.
Manager: "The sample count is still ___." | unresolved | Location arithmetic does not determine the sample count, which the brief leaves unresolved.
Client: "Before extra field work, we need an approved written ___." | change | The supplied agreement explicitly requires an approved written change before additional field work.'''))
