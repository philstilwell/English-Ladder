"""Original pharmaceutical communication cases for advanced English learners."""
from books.authoring import unit

BOOK = dict(
    slug='pharmaceutical', title='Pharmaceutical English',
    cover_label='Evidence / development / quality / communication',
    cover_title='Pharmaceutical', cover_size=29,
    tagline='State the evidence. Qualify the claim. Close the communication gap.',
    audience='For pharmaceutical development, clinical, regulatory, safety, quality, medical, and access teams.',
    map_intro='Follow eight cross-functional conversations from early evidence to development decisions, safety, quality, and access.',
    notes_title='Precision protects the meaning.',
    notes_intro='Pharmaceutical conversations often connect specialists who use similar words for different purposes. A result, a hypothesis, a submission, and an approval are not interchangeable. These fictional cases practice concise clarification, careful evidence language, and explicit handoffs without turning English exercises into technical operating instructions.',
    field_notes=[
        ('Name the evidence level', 'Say whether a finding comes from a laboratory model, a clinical trial, or routine-care data. Keep the population, comparator, outcome, and limitations attached to the claim.', '"The laboratory finding supports a hypothesis; it does not establish patient benefit."'),
        ('Verify the controlling document', 'A familiar attachment may be outdated or not applicable to a particular site. Ask for the document identifier, version, approval status, and effective status before treating conflicting wording as settled.', '"Please confirm the version authorized for this site and the exact section that governs the visit."'),
        ('Report uncertainty without losing urgency', 'Incomplete information is not the same as evidence that nothing happened. Follow the applicable safety or quality process and preserve what was reported, what is missing, and who owns follow-up.', '"The report is incomplete; I am routing the available information through the required channel now."'),
        ('Keep review and approval distinct', 'Receiving a submission, reviewing a draft, and authorizing use are different events. State the actual status and next decision instead of using reassuring language that implies more than the record supports.', '"Comments are resolved, but final approval for this version is still pending."')],
    scope_note='Original fictional language practice, not medical advice, clinical training, regulatory guidance, or authorization to perform regulated work. US terminology is used where identified; requirements vary by jurisdiction, product, and context. Follow current approved procedures, qualified professional judgment, and applicable requirements.',
    sources=[
        dict(title='US Food and Drug Administration. The Drug Development Process.', url='https://www.fda.gov/patients/learn-about-drug-and-device-approvals/drug-development-process', note='Background on development stages and post-market monitoring. All products, figures, and conversations in this book are invented.', checked='30 September 2026'),
        dict(title='FDA / ICH. E9(R1): Estimands and Sensitivity Analysis in Clinical Trials.', url='https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical', note='Background for precise treatment-effect questions and interpretation. The fictional statistical exercise is not a trial-analysis specification.', checked='30 September 2026'),
        dict(title='FDA. Questions and Answers on CGMP Requirements: Records and Reports.', url='https://www.fda.gov/drugs/guidances-drugs/questions-and-answers-current-good-manufacturing-practice-requirements-records-and-reports', note='Background for quality documentation terminology. The batch dialogue does not prescribe release decisions or replace site procedures.', checked='30 September 2026'),
        dict(title='FDA. The Office of Prescription Drug Promotion.', url='https://www.fda.gov/about-fda/cder-offices-and-divisions/office-prescription-drug-promotion-opdp', note='Background for truthful, non-misleading promotion and review boundaries. Examples are invented, not approved product claims.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Drug Development Strategy, Unmet Need, TPP, and Evidence Logic',
    scene='A laboratory signal becomes a patient-benefit claim',
    skill='Replace an overstated development claim with a precise finding and a testable next question.',
    brief='An internal slide for fictional candidate PX-17 says it improves patient mobility. The available experiment used a cell-based assay, not patients. Across three experimental runs, the team observed a change in a disease-related marker at one tested concentration. Human exposure, tolerability, and clinical benefit have not been established. Scientist Leila and development lead Owen are preparing a portfolio discussion. The proposed target product profile describes a desired future benefit, not an achieved product characteristic. No clinical study is authorized by this discussion.',
    cast='Leila | Translational scientist\nOwen | Development lead',
    culture=('A narrower claim can be more useful', 'Do not soften an unsupported assertion merely by adding promising. State what was measured, where it was measured, and what remains unknown. Then connect the result to the next question. This lets a colleague support further investigation without endorsing a conclusion the evidence cannot carry.'),
    a='''Where was the observed result obtained? | In a cell-based assay across three experimental runs | In a completed patient mobility trial | In routine treatment at multiple hospitals | In an approved product label | The supplied evidence is laboratory evidence, with no patient study or approved label in the case.
What does the target product profile represent here? | Desired future characteristics to guide development | Proof that patient mobility has improved | Authorization to begin a clinical study | A final regulatory approval | The proposed profile sets aspirations; it does not establish that those characteristics have been demonstrated.
Which claim exceeds the evidence? | PX-17 improves patient mobility. | A disease-related marker changed in the assay. | Human tolerability remains unestablished. | Further evidence is required. | No patients were studied, so the laboratory result cannot establish a patient mobility benefit.''',
    vocabulary='''unmet medical need | A health-related need not adequately addressed by available options. | characterize the unmet medical need
target product profile | A planning description of desired future product characteristics. | refine the target product profile
development candidate | A selected investigational substance being evaluated for further development. | nominate a development candidate
mechanism of action | The biological process through which an intervention produces an effect. | investigate the mechanism of action
target engagement | Evidence that an intervention interacts with its intended biological target. | assess target engagement
proof of concept | Evidence supporting the feasibility of a defined scientific or clinical idea. | specify the proof-of-concept question
cell-based assay | A laboratory test using cells to assess a specified response. | qualify the cell-based assay
biomarker | A measured characteristic indicating a biological process or response. | evaluate a candidate biomarker
surrogate endpoint | A substitute outcome used to predict a clinical outcome, with context-dependent support. | justify a surrogate endpoint
clinical benefit | A meaningful favorable effect on how patients feel, function, or survive. | establish clinical benefit
translational evidence | Information connecting findings across experimental and human contexts. | strengthen translational evidence
biological plausibility | A reasoned basis for believing a biological explanation could be credible. | assess biological plausibility
dose-response relationship | How a measured effect varies with administered dose. | characterize the dose-response relationship
exposure-response relationship | How an effect varies with drug exposure in the body. | examine exposure-response relationships
pharmacokinetics | Study of the time course of drug exposure through absorption, distribution, metabolism, and elimination. | characterize pharmacokinetics
pharmacodynamics | Study of a drug's biological effects and their relation to exposure. | measure pharmacodynamic effects
nonclinical study | Research conducted outside human clinical studies. | interpret nonclinical findings
tolerability | The extent to which unwanted effects can be endured in a defined context. | evaluate tolerability
therapeutic window | The exposure range associated with desired effects and acceptable toxicity in context. | investigate the therapeutic window
reproducibility | The ability to obtain consistent findings under specified repeat conditions. | test reproducibility
assay limitation | A restriction affecting what a test can establish. | disclose assay limitations
go/no-go criterion | A defined condition informing whether development proceeds or stops. | set go/no-go criteria
evidence gap | Missing information needed to support a proposed conclusion. | prioritize evidence gaps
development milestone | A defined point of progress or review in a development program. | plan the next development milestone''',
    precision='A biomarker change is not automatically clinical benefit. Its meaning depends on the marker, context, and supporting evidence. Here, one concentration and three laboratory runs do not establish human exposure, tolerability, dose response, or improved mobility.',
    precision_extra='Target product profile is often shortened to TPP; mechanism of action to MOA; pharmacokinetics to PK; and pharmacodynamics to PD. Expand the terms when needed, and distinguish a planned characteristic from an observed result. A development goal must not silently become an evidence claim.',
    phrases='''Locate the evidence | The observation comes from a cell-based assay, not a patient study.
Narrow the claim | We observed a marker change under the tested conditions.
Protect the distinction | Clinical benefit has not been established.
Clarify the aspiration | The target product profile describes what we aim to demonstrate.
Ask for the bridge | What evidence connects this marker to the intended patient outcome?
Qualify repetition | Three runs support repeatability within these conditions, not general clinical effectiveness.
Name the limitation | We tested one concentration, so this does not characterize a dose-response relationship.
State the next question | We need to test whether the finding persists under relevant follow-up conditions.
Avoid implied safety | The current experiment does not establish human tolerability.
Check the population | Which patients would the proposed product eventually be intended to serve?
Separate stages | An early signal supports investigation, not a treatment recommendation.
Request a criterion | What result would support the next development decision?
Clarify the measure | Are we discussing target engagement, a biomarker, or a patient outcome?
Keep the goal conditional | The desired benefit remains a hypothesis to be evaluated.
Mark authority | This portfolio discussion does not authorize a clinical study.
Close accurately | Retain the finding, its conditions, and the unresolved evidence gap.''',
    notes='''Observed | Use for the measured result, not for an extrapolated patient benefit.
Suggests | State exactly what the result suggests and why.
Proof of concept | Specify the concept; laboratory and clinical proof are different claims.
TPP | This is a planning tool, not automatically an approved label.
At one concentration | This qualifier limits what can be said about response across concentrations.
In patients | Do not add this phrase when the evidence comes only from laboratory work.''',
    d='''Which replacement is best supported? | PX-17 changed the marker in the tested cell assay; patient benefit remains unestablished. | PX-17 restores mobility in patients because the marker changed. | PX-17 is safe at every human dose. | PX-17 has an approved mobility indication. | The replacement preserves the observed laboratory finding while explicitly limiting the clinical inference.
What does testing one concentration fail to characterize? | How the effect changes across different concentrations | Whether the tested assay recorded any response | Whether the experiment used cells | The number of experimental runs stated in the brief | A response across concentrations requires additional concentration conditions; the supplied experiment used only one.
Which question best tests the evidence bridge? | How well does this marker predict the intended patient outcome in this context? | Which adjective makes the slide sound most certain? | Can we delete the laboratory setting to simplify the claim? | Does a planning goal count as an observed clinical result? | The question asks for the missing connection between the measured marker and the claimed patient benefit.
What can the portfolio discussion decide on the supplied authority? | A proposed next investigation for appropriate review, not automatic clinical-study authorization | Immediate patient treatment with the candidate | Final marketing authorization | A universal human dosing recommendation | The brief excludes clinical-study authorization and supplies no basis for treatment or marketing claims.''',
    dialogue='''Owen | The portfolio slide says PX-17 improves patient mobility. I thought the latest package contained laboratory work only. Have I missed a clinical result?
Leila | No. The result comes from a [[cell-based assay::A cell-based assay is laboratory evidence, not a study establishing outcomes in patients.]]. We saw the marker change across three runs at one tested concentration. Nobody measured mobility in patients.
Owen | Then the headline has moved beyond the evidence. The team wanted a clear link to the disease, but the wording makes that link sound demonstrated.
Leila | We can describe the [[biomarker::The biomarker is the measured biological characteristic; its change does not itself establish improved patient function.]] response precisely and explain why it interests us. We still need evidence connecting that response to the outcome we hope to influence.
Owen | The commercial planning page also lists improved mobility. That is in the target profile, so perhaps someone copied it into the result summary.
Leila | The [[target product profile::The target product profile sets desired future characteristics rather than recording benefits already demonstrated.]] is aspirational at this stage. We should label the desired outcome separately from the finding so readers do not confuse the development goal with achieved performance.
Owen | Can we call this proof of concept? The phrase is familiar, but different colleagues may hear very different claims when they read it.
Leila | Specify the concept and setting. It is not evidence of [[clinical benefit::Clinical benefit concerns meaningful patient outcomes; this experiment did not measure any patient outcome.]]. A broad proof-of-concept label could conceal exactly the distinction we are trying to restore.
Owen | We also tested only one concentration. The slide's rising arrow looks like an established relationship between dose and effect, even though we have no such series.
Leila | Remove that implication. A [[dose-response relationship::Dose-response describes effects across doses; the single tested concentration cannot establish that relationship.]] has not been characterized here. The visual should not make a stronger statement than the accompanying words or the experiment itself.
Owen | What can we say about the three runs? I do not want to discard useful repetition merely because the result is still early.
Leila | Describe the observed consistency and the conditions. It informs [[reproducibility::Reproducibility concerns consistent findings under specified repeat conditions, not automatic generalization to humans.]] within this setup, while leaving broader confirmation open. We should also report any relevant variation rather than showing only the most favorable run.
Owen | Someone has added well tolerated to the summary. There were no human participants, so I cannot see what that statement is based on.
Leila | Human [[tolerability::Tolerability concerns enduring unwanted effects in a defined context; this laboratory experiment did not establish human tolerability.]] is unestablished. We can report the actual observations, but we should not translate the absence of a particular laboratory finding into a general human safety claim.
Owen | Let us make the next decision concrete. What missing information matters most before the program can support a stronger development proposal?
Leila | Start with the [[evidence gap::The evidence gap is missing information connecting the assay finding to a more meaningful development conclusion.]] between the assay response and the intended outcome. The scientific team should define the follow-up question and its limits through the appropriate development process.
Owen | The committee will ask what would count as enough progress to continue. A broad instruction to produce more data will not help them compare programs.
Leila | Propose a defined [[go/no-go criterion::A go/no-go criterion identifies evidence needed for a development decision rather than treating all additional data as progress.]] for qualified review. It should match the next decision, without pretending that an early laboratory threshold alone establishes a product suitable for patients.
Owen | I will separate the observation, the hypothesis, and the requested next step. We can keep the result interesting without making the conclusion premature.
Leila | Good. The next [[development milestone::A development milestone is a defined progress or review point, not automatic authorization for human studies.]] remains subject to the required review. This discussion does not authorize a clinical study, and the final slide should say no more than the evidence supports.''',
    transfer_title='A goal is not a result',
    transfer_setup='A planning profile targets once-daily use. The candidate has no human dosing data. A laboratory test measured target engagement but did not measure patient symptoms.',
    transfer='''Scientist: "Once-daily use is currently a ___." | goal | The planning profile states an intended characteristic, while no human dosing evidence is supplied.
Reviewer: "The measured laboratory finding concerns ___." | target engagement | The test measured interaction with the intended target, not patient symptoms.
Scientist: "Human dosing remains ___." | unestablished | The brief explicitly says there are no human dosing data.
Reviewer: "We cannot claim symptom ___." | improvement | Patient symptoms were not measured, so an improvement claim would exceed the evidence.'''))

BOOK['units'].append(unit(
    title='Regulatory Pathways, IND Readiness, NDA/BLA Strategy, and Agency Interaction',
    scene='A meeting question that asks for blanket agreement',
    skill='Frame a focused regulatory question and accurately record the scope of the response.',
    brief='A US development team is preparing an agency meeting package for fictional investigational product RV-8. Its draft asks whether the entire development plan is acceptable. The immediate unresolved question concerns the proposed patient population and the rationale for a planned study endpoint. Supporting summaries exist, but two supporting reports are unfinished. Regulatory lead Priya and clinical lead Evan must distinguish the sponsor proposal, available evidence, and specific advice requested. No agency response has been received, and meeting preparation does not constitute authorization to begin the study.',
    cast='Priya | Regulatory lead\nEvan | Clinical lead',
    culture=('Make the question answerable', 'A focused question gives reviewers a proposal, supporting rationale, and a specific point on which advice is sought. Avoid treating a useful discussion as blanket agreement with every part of a program. Meeting records should preserve conditions, unresolved issues, and any distinction between advice and formal authorization.'),
    a='''What is wrong with the current question? | It asks broadly about the entire plan instead of the specific unresolved proposal. | It contains a confirmed agency decision. | It identifies too narrow a product name. | It asks for information already supplied as final approval. | The real issue concerns population and endpoint rationale, while the draft requests undifferentiated agreement with the entire plan.
What is the status of two supporting reports? | Unfinished | Approved by the agency | Replaced by a marketing authorization | Irrelevant because the meeting is scheduled | The brief explicitly says two supporting reports remain unfinished.
Which statement is accurate now? | No agency response has been received. | The study is authorized because a package is being prepared. | The entire program has formal agreement. | An NDA has been approved for RV-8. | Preparation is ongoing, and the case supplies no response or study authorization.''',
    vocabulary='''regulatory strategy | A plan for addressing applicable regulatory requirements and interactions. | align the regulatory strategy
regulatory pathway | The applicable route for development, review, or authorization. | confirm the regulatory pathway
investigational new drug application | A US submission supporting proposed clinical investigation of a drug. | prepare an IND submission
new drug application | A US application seeking approval to market a new drug. | plan the NDA content
biologics license application | A US application seeking licensure of a biological product. | prepare the BLA strategy
agency interaction | A formal or informal exchange with a regulatory authority. | document the agency interaction
meeting package | Materials submitted to support a scheduled regulatory discussion. | assemble the meeting package
briefing document | A structured account of background, evidence, proposals, and questions. | finalize the briefing document
sponsor position | The development sponsor's proposed approach and rationale. | state the sponsor position
focused question | A question limited to a defined issue that can receive a useful answer. | formulate a focused question
supporting rationale | The reasoning and evidence behind a proposal. | substantiate the supporting rationale
information gap | Missing material relevant to assessing a proposal. | disclose an information gap
submission readiness | The state of being sufficiently prepared for an intended submission. | assess submission readiness
dossier | An organized collection of documents supporting regulatory review. | maintain a coherent dossier
cross-reference | A pointer connecting a statement to supporting material. | verify the cross-reference
version control | Management of document revisions and their status. | maintain version control
regulatory commitment | An undertaking made in the relevant regulatory context. | track regulatory commitments
meeting minutes | The documented account of a meeting's discussion and outcomes. | reconcile meeting minutes
written response | A documented reply to a submitted question or issue. | review the written response
conditional advice | Advice whose applicability depends on stated circumstances. | preserve conditional advice
clinical hold | A regulatory order delaying or suspending a clinical investigation in the US context. | address a clinical hold
approval status | The actual state of a specified authorization decision. | verify approval status
indication | The disease, condition, or use for which a product is intended or authorized in context. | define the proposed indication
regulatory affairs | The function coordinating regulatory strategy, submissions, and interactions. | consult regulatory affairs''',
    precision='IND means investigational new drug application; NDA means new drug application; BLA means biologics license application in US usage. These terms name different regulatory submissions. An IND is not a marketing approval, and preparing a meeting package does not authorize a study.',
    precision_extra='Agency advice may address a specific question under stated assumptions. Preserve those limits in the meeting record. Do not report advice on a population or endpoint as approval of the complete program, final labeling, or a marketing application.',
    phrases='''Focus the question | We seek advice on the proposed population and endpoint rationale.
State the sponsor view | Our proposed approach is set out in section three.
Supply the reason | The rationale rests on the following evidence and assumptions.
Disclose incompleteness | Two supporting reports are not yet final.
Avoid blanket agreement | This question does not ask for approval of the entire program.
Check the reference | Please verify that the cited section supports this statement.
Distinguish status | The package is in preparation; no agency response has been received.
Preserve a condition | Record the qualification alongside the advice, not in a separate summary.
Confirm the pathway | Regulatory affairs should confirm the applicable route for this product.
Separate submissions | An IND and a marketing application serve different purposes.
Resolve a discrepancy | The summary and supporting report currently describe different populations.
Control the version | Use the agreed document version for the submitted package.
Track an undertaking | Identify the owner and due date for each recorded commitment.
Limit the conclusion | Advice on this question does not settle every development issue.
Mark study authority | Meeting preparation is not permission to begin the study.
Close the record | Distinguish answered questions, conditions, and issues still open.''',
    notes='''Acceptable in what respect | Ask which specific proposal and evidence the question concerns.
Sponsor position | This is the company's proposal, not the authority's conclusion.
Final versus available | A draft can be available without being final or approved.
Advice versus authorization | Keep the applicable legal and procedural status explicit.
No objection | Do not paraphrase a limited response as unrestricted approval.
As proposed | This phrase ties the response to the details actually presented.''',
    d='''Which revised question is most useful? | Does the agency agree with the proposed population and endpoint rationale described in section three? | Is everything about the company acceptable forever? | Will every future application be approved? | Can we call unfinished reports final to simplify review? | The focused question identifies the proposal and its supporting section without seeking blanket approval.
Which package statement is accurate? | Two reports remain unfinished and their status is identified. | All supporting reports are final because the meeting is planned. | No evidence needs to support a sponsor position. | A scheduled meeting constitutes marketing authorization. | The statement preserves the actual document status and allows reviewers to understand the information gap.
Which distinction is correct in US terminology? | An IND supports clinical investigation; an NDA seeks marketing approval for a new drug. | An IND is a guarantee that an NDA will be approved. | A meeting package replaces every required application. | A BLA is merely a meeting calendar invitation. | These submissions serve different purposes, and permission or advice at one stage does not guarantee later approval.
How should limited advice be summarized? | Preserve its subject, assumptions, conditions, and unresolved issues. | Expand it into approval of every proposed study. | Delete qualifications to make the update easier to read. | Treat the sponsor's preferred wording as the agency's conclusion. | An accurate record retains the boundaries of the actual response instead of changing its meaning.''',
    dialogue='''Evan | Our lead question asks whether the whole development plan is acceptable. It is concise, but I suspect it will not give us the advice we need.
Priya | We need a [[focused question::A focused question identifies the specific unresolved issue, here population and endpoint rationale.]]. The immediate issue is the proposed patient population and endpoint rationale, not every aspect of the program from development through launch.
Evan | The team has a preferred approach. Should we present alternatives equally, or make clear which approach we are proposing and why we favor it?
Priya | State the [[sponsor position::The sponsor position is the company's proposed approach, which must not be confused with agency agreement.]] clearly, then give the rationale and relevant alternatives. Reviewers should not have to infer our proposal from a collection of background slides.
Evan | The supporting summaries are available, although two underlying reports are unfinished. I do not want the package to imply that those reports are final.
Priya | Identify that [[information gap::The information gap is the unfinished supporting material, whose status must remain visible in the package.]] and explain its relevance. We should not conceal unfinished work or claim that a summary has the status of a completed report.
Evan | Section three explains the population. Another section uses a broader description, which could make our question seem different depending on where the reviewer starts.
Priya | Reconcile the wording in the [[briefing document::The briefing document should present a coherent proposal, evidence, and questions rather than conflicting population descriptions.]]. A precise question is not enough if the supporting text describes a different proposal or leaves the study population ambiguous.
Evan | I will also check the references. One footnote points to an earlier table, and the current table no longer contains the information cited.
Priya | Verify each [[cross-reference::A cross-reference must lead to material that actually supports the statement, including after document revisions.]] after the content is settled. A broken evidence trail forces reviewers to guess which material we intended and can weaken an otherwise useful discussion.
Evan | Some colleagues are calling the meeting package our IND approval package. That seems to mix the meeting purpose with the status of a regulatory submission.
Priya | Use the terms carefully. An [[investigational new drug application::An investigational new drug application concerns clinical investigation in the US; a meeting package is not itself that authorization.]] concerns proposed clinical investigation in the US context. Preparing this meeting package does not authorize the study or establish a marketing approval.
Evan | The long-range plan also mentions an NDA or BLA. We should explain the applicable route without suggesting that either application is already ready.
Priya | Exactly. The [[regulatory pathway::The regulatory pathway is the applicable route for this product, which qualified regulatory colleagues must confirm.]] depends on the product and context. Regulatory affairs should confirm the route, while the current discussion remains focused on the specific development question.
Evan | After the meeting, the executive team will want a short update. How do we keep it concise without losing qualifications that affect the advice?
Priya | Preserve any [[conditional advice::Conditional advice applies within stated circumstances; removing those conditions changes the meaning of the response.]] in the main summary. If a response depends on the proposed population or additional evidence, that condition belongs beside the conclusion, not buried elsewhere.
Evan | We should compare our notes with the official record through the applicable process. A colleague's enthusiastic recollection should not become the only account.
Priya | Yes, reconcile the [[meeting minutes::Meeting minutes record the discussion and outcomes; discrepancies should be resolved through the applicable process.]] and track unresolved differences. Assign owners to follow-up items and commitments rather than treating a successful conversation as completion of all required work.
Evan | I will revise the package to separate the proposal, evidence, questions, and missing reports. Our internal update will say that no response has yet been received.
Priya | And keep [[approval status::Approval status must reflect the actual authorization record, not expectations created by meeting preparation or positive discussion.]] explicit. Advice on one issue is not blanket program approval, and preparation for a meeting is not permission to start the study.''',
    transfer_title='The response answers one question',
    transfer_setup='An invented meeting note supports an endpoint approach only for the population described in the package. It requests further justification of follow-up duration. It grants no marketing authorization.',
    transfer='''Regulatory lead: "The endpoint advice is ___." | conditional | The note limits support to the population actually described, so it is not unconditional agreement.
Clinical lead: "Follow-up duration remains ___." | unresolved | Further justification is requested, so the note does not settle that issue.
Regulatory lead: "Preserve the stated ___." | population | The population defines the scope within which the endpoint advice applies.
Clinical lead: "This is not marketing ___." | authorization | The briefing explicitly excludes marketing authorization, regardless of the favorable endpoint comment.'''))


BOOK['units'].append(unit(
    title='Clinical Trial Design, Protocols, GCP, and Operations',
    scene='Two visit windows and no confirmed controlling version',
    skill='Resolve conflicting trial instructions through an explicit, documented clarification rather than choosing a convenient version.',
    brief='Coordinator Maya is scheduling next week. A protocol attachment gives a plus-or-minus-three-day visit window; a site quick-reference sheet gives seven. The controlling version and site implementation status are unconfirmed. No participant awaits an urgent care decision. Clinical research associate Ben must obtain clarification through the investigator and sponsor process. Neither may invent a window, silently change records, or assume the newest attachment governs the site.',
    cast='Maya | Site coordinator\nBen | Clinical research associate',
    culture=('Read back the conflict exactly', 'A useful escalation states both wordings, identifies their sources, and asks a specific question about the applicable version. Avoid describing the issue merely as confusion at the site. Precise language helps colleagues resolve the document problem without assigning blame or improvising clinical instructions.'),
    a='''What is the documented conflict? | Three-day versus seven-day visit windows in two sources | Two confirmed identical protocol versions | A participant refusing all care | A completed decision approving a new window | The brief supplies conflicting window descriptions and no confirmed controlling version.
What has not been confirmed? | The controlling version and its implementation status at the site | Whether appointments are being prepared for next week | Whether a quick-reference sheet exists | Whether the two wordings differ | Both document authority and site applicability remain unresolved in the supplied facts.
Which response avoids an unauthorized assumption? | Escalate the exact discrepancy for documented clarification through the applicable process. | Select seven days because it is more convenient. | Treat the newest email attachment as automatically controlling. | Rewrite historical visit records to match the preferred version. | The case requires authorized clarification, not a convenient choice, inferred authority, or silent alteration of records.''',
    vocabulary='''protocol | The document specifying a clinical study's objectives, design, and procedures. | follow the applicable protocol
protocol amendment | A documented change to a study protocol. | implement an authorized protocol amendment
visit window | The allowed timing range for a specified study visit or assessment. | confirm the visit window
schedule of assessments | The planned timing of study procedures and measurements. | reconcile the schedule of assessments
controlling version | The authorized document version applicable to the work in question. | identify the controlling version
effective date | The date from which a document or change applies in context. | verify the effective date
site activation | Confirmation that a site meets the applicable conditions to begin specified study activity. | confirm site activation status
principal investigator | The investigator responsible for leading the study at a site. | consult the principal investigator
clinical research associate | A professional supporting study oversight and monitoring within assigned responsibilities. | contact the clinical research associate
study coordinator | A site professional coordinating assigned trial activities. | brief the study coordinator
good clinical practice | Principles and standards for ethical, reliable clinical trial conduct. | apply good clinical practice
informed consent | The voluntary agreement process based on adequate study information and understanding. | document the informed-consent process
institutional review board | A body reviewing research involving human participants in the US context. | confirm institutional review board review
eligibility criterion | A condition determining whether someone may enter a study. | verify eligibility criteria
randomization | Allocation to study groups using a chance-based method. | protect the randomization process
blinding | Concealment of treatment allocation from specified parties. | maintain blinding
source record | The original record or certified copy containing relevant study observations. | preserve the source record
electronic case report form | An electronic tool for collecting protocol-required participant data. | complete the electronic case report form
data query | A documented request to clarify or resolve a data issue. | resolve a data query
protocol deviation | A departure from the study protocol. | assess a potential protocol deviation
monitoring finding | An issue identified during study monitoring. | document a monitoring finding
audit trail | A traceable record of changes and associated information. | preserve the audit trail
training record | Documentation of completed instruction or qualification. | verify the training record
essential record | A record supporting evaluation of trial conduct and result reliability. | maintain essential records''',
    precision='A later file date does not establish that a document is approved and effective for a particular site. Confirm identity, version, authorization, and applicability. A quick-reference sheet should not silently replace the controlling protocol or become an unofficial amendment.',
    precision_extra='GCP means good clinical practice; CRA, clinical research associate; PI, principal investigator; IRB, institutional review board; and eCRF, electronic case report form. Roles and approval processes vary. These exercises practice clarification, not instructions to alter care, consent, or study procedures.',
    phrases='''State the discrepancy | The protocol attachment says three days; the quick-reference sheet says seven.
Request the authority | Which approved version is effective for this site?
Identify the source | I will include the document identifiers and exact sections.
Avoid a guess | I cannot confirm the visit window from these conflicting files.
Escalate precisely | Please resolve the timing discrepancy through the investigator and sponsor process.
Protect the record | We must preserve the original entry and any documented correction history.
Separate status | Received by email does not necessarily mean approved for implementation.
Check training | Has the relevant site team completed the required update?
Limit the response | I am confirming the governing instruction, not proposing a new window.
Close the loop | Please acknowledge the clarification and identify any affected appointments.
Assess impact | After confirmation, determine whether any completed visits require review.
Avoid blame | The two sources conflict; let us establish the applicable instruction.
Keep care distinct | Administrative clarification must not replace appropriate clinical judgment.
Document the outcome | Record the confirmed version, effective status, and source of clarification.
Control obsolete copies | Handle superseded quick-reference material through the document process.
Confirm understanding | Please read back the confirmed window and the document it comes from.''',
    notes='''Applicable | A document can be approved but not yet applicable to a given site or activity.
Clarification versus amendment | Explaining an existing requirement differs from changing it.
Received versus implemented | Receipt of a file does not prove authorized implementation or training.
Source versus eCRF | These records have related but distinct roles; discrepancies need traceable resolution.
Potential deviation | Do not classify the event definitively before the governing facts are established.
Read-back | Repeat the key instruction and source to expose misunderstanding before action.''',
    d='''Which clarification request is strongest? | Please confirm the approved site-effective version and section governing the visit window. | Which window will make our calendar easiest? | May we ignore both documents and choose five days? | Can the newest attachment replace approval evidence? | The request asks for authority and applicability rather than convenience or an invented compromise.
What does a newer file date prove by itself? | Only that the file carries a later date, not that it governs the site | That every site has implemented the document | That all required training is complete | That older source records may be overwritten | File recency alone does not establish approval, effective status, training, or authority to change records.
How should a necessary record correction be handled? | Through the applicable traceable correction process, preserving the original history | By silently replacing the original value | By deleting the discrepancy from the record | By changing all records before checking the protocol | Traceable correction preserves what was recorded and why it changed, instead of concealing the original entry.
What should follow an authorized clarification? | Confirm understanding and assess affected appointments or records through the appropriate process. | Assume no further communication is needed. | Declare every prior visit compliant without review. | Treat clarification as permission to change any unrelated procedure. | The clarified instruction must reach the relevant people, and any impact needs assessment rather than an unsupported conclusion.''',
    dialogue='''Maya | I am scheduling next week's visits and have two different windows. The protocol attachment says plus or minus three days; the quick-reference sheet says seven.
Ben | Please send the identifiers and exact sections for both. We need the [[controlling version::The controlling version is the authorized document applicable to this site, not whichever file is easier to use.]] before confirming the schedule. I cannot choose a window from the filenames alone.
Maya | The seven-day sheet arrived in a newer email. The coordinator who forwarded it assumed that made it the current instruction for every site.
Ben | A later email does not establish the [[effective date::The effective date establishes when a document applies; a later email alone does not establish implementation status.]] or implementation status. We should confirm which approved document applies here through the investigator and sponsor process.
Maya | I will quote both wordings in the request. Calling it a scheduling question without the numbers would make the reviewer reconstruct the discrepancy.
Ben | Include the relevant [[schedule of assessments::The schedule of assessments supplies timing details that must be reconciled with the governing protocol.]] references as well. The team needs enough context to identify whether the quick-reference material reflects an authorized change or an error.
Maya | Nobody is waiting for an urgent care decision. This concerns next week's appointments, but I want to resolve it before we send instructions to participants.
Ben | Ask the [[principal investigator::The principal investigator leads the study at the site and is part of the appropriate clarification route.]] to handle the site issue through the appropriate route. We should not invent clinical instructions or let an administrative document question substitute for medical judgment.
Maya | If the seven-day wording came from an amendment, we need more than a copy of the amended page. We need to know its status here.
Ben | Correct. A [[protocol amendment::A protocol amendment changes the study document and requires applicable authorization and implementation, not merely receipt by email.]] has an applicable approval and implementation process. Confirm those facts rather than treating circulation of the file as evidence that every required step occurred.
Maya | The quick-reference sheet is useful at the desk, but it cannot create a separate set of rules. We should reconcile it after the answer is confirmed.
Ben | And verify the relevant [[training record::The training record helps establish whether the site team received the required instruction for an implemented change.]]. Even a correct document may not resolve the operational problem if the people using it have not received the required update.
Maya | What about earlier visits? We should not declare them compliant or noncompliant until we know which instruction actually applied at the time.
Ben | Exactly. Assess any potential [[protocol deviation::A protocol deviation is a departure from the protocol; classification requires knowing which requirement actually applied.]] through the appropriate process after establishing the facts. Do not assume that today's clarification automatically governs every historical visit.
Maya | One colleague suggested changing the old dates in the tracker to remove the apparent conflict. That would conceal what happened rather than resolve it.
Ben | Preserve the [[audit trail::The audit trail preserves the history of recorded changes; silently altering dates would conceal rather than resolve the discrepancy.]]. Any necessary correction must follow the applicable process and retain traceability. We must not rewrite the history to make the schedule appear consistent.
Maya | Once we receive the response, I will send a short site update with the confirmed version and the appointments that need attention.
Ben | Use a [[read-back::A read-back repeats the key instruction and source, allowing misunderstanding to be detected before the team acts.]] for the critical timing instruction. Ask the relevant colleague to repeat the window and its source so we can detect a misunderstanding before acting on it.
Maya | I will keep the clarification with the study records and route any affected data questions separately. We should not leave the answer only in someone's inbox.
Ben | Good. The [[essential records::Essential records support reconstruction and evaluation of trial conduct, including the documented clarification relevant to this discrepancy.]] should show the discrepancy, the authorized resolution, and the follow-up. That closes the communication loop without turning a convenient reference sheet into an unofficial protocol.''',
    transfer_title='Receipt does not establish applicability',
    transfer_setup='A coordinator receives version 5 by email. The site record still identifies version 4 as effective. No implementation confirmation for version 5 has been supplied.',
    transfer='''Coordinator: "Version 5 has been ___." | received | Email receipt is established, but the briefing supplies no confirmation of authorized implementation.
Monitor: "Its site applicability remains ___." | unconfirmed | The available record still names version 4, so applicability must be clarified.
Coordinator: "I will request implementation ___." | confirmation | The missing information concerns whether and when the newer version applies at the site.
Monitor: "Do not infer authority from file ___." | recency | A newer file alone does not establish the approval and effective status required to govern the work.'''))

BOOK['units'].append(unit(
    title='Endpoints, Estimands, Statistics, Data Readouts, and Clinical Meaning',
    scene='A favorable secondary result takes over the headline',
    skill='Explain a trial readout without replacing the prespecified question or overstating statistical certainty.',
    brief='A fictional trial measures week-12 symptoms; lower scores are better. The primary treatment-minus-control estimate is -2 points (95% confidence interval: -5 to +1; p=0.19). The prespecified two-sided threshold is 0.05. A secondary endpoint has nominal p=0.01, but the testing plan requires primary success before a confirmatory secondary claim. Statistician Anika and medical lead Luis must correct the headline: the trial proved efficacy.',
    cast='Anika | Statistician\nLuis | Medical lead',
    culture=('Do not repair a result by changing the question', 'Lead with the prespecified primary result and explain uncertainty before highlighting other findings. A disappointing primary test does not make every observation worthless, but a favorable secondary result does not erase the testing plan. Keep statistical evidence and clinical importance separate in the discussion.'),
    a='''Did the primary analysis meet the specified significance threshold? | No; p=0.19 is above 0.05. | Yes; every negative point estimate is significant. | Yes; the secondary p-value replaces it. | No; because the confidence interval contains only negative values. | The supplied p-value exceeds the prespecified threshold, and the interval actually includes both negative and positive values.
What is the secondary endpoint's status under this plan? | A nominal result that cannot support the stated confirmatory claim after primary failure | Automatic proof that the primary endpoint succeeded | A replacement primary endpoint chosen after the readout | A guarantee of clinical benefit in every patient | The specified testing sequence requires primary success before a confirmatory secondary claim.
What does the negative point estimate indicate? | The estimated difference favors treatment on this lower-is-better scale. | The trial has proved no possible benefit. | The treatment is worse because negative numbers are always unfavorable. | The confidence interval excludes no difference. | Treatment minus control is negative on a scale where lower is better, but uncertainty and the test result still matter.''',
    vocabulary='''primary endpoint | The outcome designated to address the study's principal objective. | report the primary endpoint
secondary endpoint | An additional prespecified outcome supporting other study objectives. | interpret secondary endpoints
exploratory endpoint | An outcome analyzed to investigate questions without the same confirmatory status. | label exploratory endpoints
estimand | The precise treatment-effect target defined for a clinical question. | specify the estimand
intercurrent event | An event after treatment starts that affects interpretation or existence of relevant measurements. | address intercurrent events
treatment-policy strategy | An estimand approach targeting outcomes regardless of specified intercurrent events. | define a treatment-policy strategy
hypothetical strategy | An estimand approach targeting a scenario in which specified intercurrent events would not occur. | justify a hypothetical strategy
analysis population | The defined group included in an analysis. | specify the analysis population
statistical analysis plan | The detailed prespecified methods for study analyses. | follow the statistical analysis plan
point estimate | A single numerical estimate of a population quantity. | present the point estimate
confidence interval | An interval from a procedure designed to cover the target parameter at a stated long-run rate. | report the confidence interval
p-value | The probability, under the null model, of a result at least as incompatible with it as observed. | interpret the p-value
significance threshold | The prespecified criterion used for a statistical test decision. | apply the significance threshold
multiplicity | The issue of repeated testing increasing opportunities for false positive conclusions. | control multiplicity
testing hierarchy | A prespecified order and conditions for confirmatory tests. | respect the testing hierarchy
nominal p-value | A p-value reported without the relevant multiple-testing adjustment or confirmatory protection. | label a nominal p-value
effect size | The magnitude of a difference or relationship on a stated scale. | interpret the effect size
clinical importance | The relevance of an effect to patients or clinical decisions. | assess clinical importance
missing data | Required or relevant observations not available for analysis. | assess missing data
sensitivity analysis | An analysis examining robustness to assumptions for the same target question. | perform sensitivity analysis
subgroup analysis | Examination of results within defined subsets of participants. | qualify a subgroup analysis
post hoc analysis | An analysis developed after the relevant data were examined. | label a post hoc analysis
data cutoff | The date or point defining the data included in a readout. | state the data cutoff
topline readout | An initial summary of key study results. | prepare a balanced topline readout''',
    precision='The estimate favors treatment, but the interval includes zero and the primary p-value exceeds 0.05. This is not proof of no effect. It is also not a successful primary test. The secondary finding retains its actual status under the prespecified plan.',
    precision_extra='An estimand defines treatments, population, outcome, intercurrent-event handling, and summary measure. An analysis method estimates that target. Changing how discontinuation is handled can change the question, not merely the numerical answer.',
    phrases='''Lead with the primary | The primary analysis did not meet the prespecified significance threshold.
State the direction | The point estimate favors treatment on this lower-is-better scale.
Preserve uncertainty | The confidence interval includes no difference.
Qualify the secondary | The secondary p-value is nominal under this testing plan.
Respect the plan | Primary success was required before a confirmatory secondary claim.
Avoid a false negative claim | Failure to meet the threshold does not prove there is no effect.
Separate importance | Statistical significance and clinical importance are different questions.
Define the target | Which treatment effect does the estimand specify?
Check the population | Confirm which participants are included in this analysis.
Handle events explicitly | State how treatment discontinuation affects the target question.
Ask about missingness | What assumptions support the handling of missing outcomes?
Label later work | This post hoc analysis was not the prespecified primary analysis.
Clarify the scale | The difference is treatment minus control, measured in score points.
Keep dates visible | Identify the data cutoff for this readout.
Avoid a rescue headline | A favorable secondary result does not replace the primary outcome.
Close with the full result | Present the estimate, uncertainty, testing status, and clinical context together.''',
    notes='''Nominal | Do not omit this qualifier when multiplicity protection does not support the claim.
Not significant | This does not mean the effect is known to be exactly zero.
Minus two points | Name the comparison direction and whether lower values are favorable.
Confidence interval | Do not describe this frequentist interval as a 95% probability that this fixed parameter lies inside it.
Estimand versus estimator | The estimand is the target; the estimator is the method used to estimate it.
Post hoc | Later exploration can be useful, but it must retain its actual evidential status.''',
    d='''Which headline is most accurate? | Primary threshold not met; secondary finding is nominal under the prespecified plan. | Trial proved efficacy because one p-value was 0.01. | Treatment has exactly zero effect in every patient. | The secondary endpoint is now the primary endpoint. | The accurate headline preserves both the primary outcome and the limited status of the secondary result.
What does the interval from -5 to +1 show? | It includes values favoring treatment, zero, and values favoring control on this scale. | It excludes every possibility of no difference. | It contains only unfavorable treatment differences. | It proves that 95% of patients improved by two points. | The interval crosses zero and spans both directions of the treatment-minus-control difference.
Why does clinical importance need separate discussion? | The practical meaning of a score difference is not established by a p-value alone. | Any p-value below one guarantees patient benefit. | A negative sign always proves a meaningful improvement. | Clinical importance is identical to the number of endpoints. | Statistical evidence alone does not determine whether an effect matters to patients in the relevant clinical context.
Which statement about later subgroup work is appropriate? | Label it according to its actual prespecification and multiplicity status. | Present it as the original primary analysis regardless of timing. | Hide the overall trial result whenever a subgroup looks favorable. | Assume smaller groups cannot produce chance findings. | Transparency about timing and testing status prevents exploratory work from being misrepresented as confirmatory evidence.''',
    dialogue='''Luis | The draft headline says the trial proved efficacy. The supporting slide leads with the secondary endpoint's p-value of point zero one and moves the primary result below it.
Anika | We need to lead with the [[primary endpoint::The primary endpoint addresses the principal prespecified objective and cannot be replaced by a favorable secondary finding.]]. Its p-value is point one nine, above the prespecified threshold of point zero five. The primary test did not succeed.
Luis | The estimated difference is minus two points. Since lower symptom scores are better, that direction favors treatment, even though the test did not meet the threshold.
Anika | Correct. Keep the [[point estimate::The point estimate is the estimated two-point difference favoring treatment; it must be reported with uncertainty.]] and its uncertainty together. We should not erase the observed direction, but neither should we turn a favorable estimate into a definitive efficacy conclusion.
Luis | The interval runs from minus five to plus one. That includes no difference and some values in the opposite direction, not just improvements.
Anika | State the [[confidence interval::The confidence interval crosses zero and includes differences in both directions, showing uncertainty around the estimate.]] plainly. It is not evidence that every patient improved by two points, and it does not establish that the true effect must be exactly zero.
Luis | Can the secondary result support the headline independently? The plan says it can be confirmatory only after primary success, which did not occur.
Anika | Then the [[testing hierarchy::The testing hierarchy conditions the confirmatory secondary claim on primary success, which the supplied result did not achieve.]] prevents that interpretation. We cannot change the sequence after seeing the readout simply because another result is more attractive.
Luis | We can still report the secondary observation, provided we describe its status. Hiding it would not make the primary explanation more complete.
Anika | Yes, report its [[nominal p-value::The nominal p-value can be reported with its limitation, but lacks the confirmatory status required by this testing plan.]] with the relevant qualification. The problem is not mentioning the result; it is implying a level of confirmatory support the plan does not provide.
Luis | The medical team will also ask whether a two-point change matters clinically. The statistical slide alone does not answer that question.
Anika | Exactly. [[Clinical importance::Clinical importance concerns the meaning of the effect for patients, which a p-value alone cannot establish.]] depends on the scale, context, and supporting evidence. A significance label is not a substitute for explaining what the measured difference could mean to patients.
Luis | Before finalizing the interpretation, I want to confirm the treatment-effect question. Colleagues have used different language about participants who stopped the assigned treatment.
Anika | Return to the [[estimand::The estimand defines the treatment effect of interest, including how relevant intercurrent events are handled.]]. We need the defined population, outcome, treatments, event-handling strategy, and summary measure, not an informal description that changes from one slide to another.
Luis | So discontinuation is not merely a nuisance to remove from the dataset. Its treatment may change which question the analysis answers.
Anika | It can be an [[intercurrent event::An intercurrent event occurs after treatment starts and affects the interpretation or existence of relevant measurements.]]. Distinguish the target question from missing observations and explain the planned approach; do not assume every discontinuation should be handled in the same way.
Luis | Additional analyses may help us understand how dependent the result is on assumptions. We should avoid choosing only the most favorable alternative.
Anika | Use the planned [[sensitivity analyses::Sensitivity analyses examine robustness to assumptions for the target question, rather than searching only for a favorable result.]] and label other work accurately. A later subgroup finding does not become the primary result, and a different question should not be presented as the same analysis.
Luis | I will replace the headline and show the primary estimate, interval, and test status first. The secondary finding will retain its qualification.
Anika | That will make the [[topline readout::The topline readout should summarize the key results with their uncertainty and actual testing status.]] balanced and intelligible. We can discuss further investigation without either claiming proven efficacy or pretending that an unsuccessful significance test proves the absence of every possible effect.''',
    transfer_title='Relative and absolute reductions',
    transfer_setup='In a separate fictional comparison, events occur in 200 of 1,000 control participants and 150 of 1,000 treatment participants. Use only these counts; no significance result is supplied.',
    transfer='''Analyst: "The control event rate is ___." | 20% | Dividing 200 events by 1,000 participants gives 0.20, or 20%.
Reviewer: "The treatment event rate is ___." | 15% | Dividing 150 events by 1,000 participants gives 0.15, or 15%.
Analyst: "The absolute reduction is ___." | five percentage points | Subtract 15% from 20%; the difference between the rates is five percentage points.
Reviewer: "Relative to control, the reduction is ___." | 25% | The five-percentage-point reduction divided by the 20% control rate equals 25%; this does not establish statistical significance.'''))


BOOK['units'].append(unit(
    title='Pharmacovigilance, Safety Signals, Risk-Benefit, and Label Updates',
    scene='An incomplete safety report',
    skill='Preserve reported facts, avoid premature causality judgments, and route a safety report without waiting for perfect information.',
    brief='Medical-information associate Nora receives a message from a clinician reporting dizziness after a patient used fictional product LM-4. The clinician calls the dizziness severe, but the message does not state whether hospitalization, a life-threatening condition, or another seriousness criterion applies. Dates, dose, outcome, and other medicines are missing. The company procedure requires prompt internal routing of available safety information and documented follow-up. Safety colleague Rafael must distinguish reported severity, unconfirmed seriousness, and unassessed causality. This conversation is an internal handoff, not advice to the patient.',
    cast='Nora | Medical-information associate\nRafael | Safety colleague',
    culture=('Keep the report and the judgment separate', 'Use reported for the clinician\'s words and unconfirmed for missing facts. Do not delay the required internal handoff while trying to prove that a product caused the event. Equally, do not dismiss the report because causality is uncertain. Qualified safety assessment and clinical care have their own appropriate routes.'),
    a='''What has the clinician actually reported? | Dizziness described as severe after product use | Confirmed product-caused hospitalization | A completed causality assessment | A verified outcome and dosing history | The message reports dizziness and its described intensity, while key assessment details remain missing.
Can severe automatically be treated as serious in the regulatory sense? | No; intensity and seriousness criteria are different concepts. | Yes; the words are always interchangeable. | Yes; any adjective establishes hospitalization. | No; severe events must never be routed. | Severe describes intensity, whereas seriousness depends on applicable outcome or medical criteria that are not confirmed here.
What does the stated company procedure require? | Prompt internal routing of available information with documented follow-up | Waiting until causality is proved before any handoff | Deleting reports with missing dates | Giving the patient a dosing recommendation during the handoff | The procedure requires routing despite incompleteness and does not authorize diagnosis or treatment advice.''',
    vocabulary='''pharmacovigilance | Activities concerned with detecting, assessing, understanding, and preventing medicine-related problems. | support pharmacovigilance
adverse event | An unfavorable medical occurrence reported during product use, without necessarily established causation. | capture an adverse event
adverse reaction | An undesirable response for which a causal relationship is at least reasonably suspected in context. | assess a suspected adverse reaction
seriousness | Classification based on applicable outcomes or medical criteria, not intensity alone. | assess seriousness
severity | The intensity of an event or symptom. | record reported severity
causality assessment | Evaluation of whether and how a product may be related to an event. | document causality assessment
expectedness | Whether the nature or severity of an event is consistent with the applicable reference safety information. | evaluate expectedness
reference safety information | The designated information used for defined safety assessments in context. | identify reference safety information
safety signal | Information suggesting a possible new or changed risk that warrants further evaluation. | evaluate a safety signal
case intake | Initial receipt and recording of a safety report. | complete case intake
individual case safety report | A structured account of an individual suspected safety case. | prepare an individual case safety report
reporter | The person or source providing event information. | preserve reporter details
verbatim term | The exact wording used by the original reporter. | retain the verbatim term
event onset | The time an event began. | confirm event onset
temporal association | A relationship in timing without necessarily proving causation. | distinguish temporal association from causation
concomitant medication | Another medicine used during the relevant period. | document concomitant medications
dechallenge | What happens after a suspected product is withdrawn or reduced, when this occurs clinically. | record available dechallenge information
rechallenge | What happens after re-exposure to a product, when this has occurred clinically. | record reported rechallenge information
follow-up request | A request for additional information about an existing case. | issue a focused follow-up request
case reconciliation | Checking that related records are consistent and accounted for across sources. | perform case reconciliation
duplicate report | Another report concerning a case already recorded. | investigate a possible duplicate report
MedDRA | Medical Dictionary for Regulatory Activities, a standardized terminology used for regulatory medical information. | apply appropriate MedDRA coding
benefit-risk assessment | Evaluation of favorable and unfavorable effects in the relevant context. | update the benefit-risk assessment
aggregate safety review | Evaluation of safety information across cases or datasets. | conduct an aggregate safety review''',
    precision='Severe describes intensity. Serious uses applicable criteria, including death, life-threatening events, hospitalization, disability, congenital anomalies, and other medically important conditions. Clarify missing facts; do not infer seriousness from intensity alone.',
    precision_extra='Dechallenge and rechallenge describe actual clinical events, not instructions to change treatment. Preserve reported facts, follow the safety process, and route clinical questions to qualified treating professionals.',
    phrases='''Open the handoff | I have an incomplete report that needs safety intake.
Preserve the wording | The clinician described the dizziness as severe.
Separate the classification | Seriousness has not yet been confirmed.
Avoid causality overreach | The event followed use; causality has not been assessed.
Name the gaps | Dates, dose, outcome, and concomitant medicines are missing.
Route promptly | I will send the available information through the required internal channel now.
Keep follow-up focused | Please clarify whether any applicable seriousness criterion was met.
Protect the original | Retain the reporter's exact words alongside any coded term.
Clarify timing | When did the event begin relative to product use?
Mark an unknown | The outcome is unknown, not recovered.
Assign ownership | Who will make the follow-up request and track the response?
Confirm receipt | Please acknowledge intake so we know the handoff reached the safety team.
Avoid dismissal | Missing information does not justify discarding the report.
Distinguish a signal | One report does not by itself establish a confirmed causal risk.
Separate care | Clinical treatment questions belong with the qualified treating professional.
Close accurately | Record what was reported, what remains unknown, and the next responsible owner.''',
    notes='''Reported versus confirmed | Attribute unverified facts to their source.
Unknown versus no | Missing hospitalization information is not evidence that hospitalization did not occur.
After versus because of | Timing alone does not establish product causation.
Serious versus severe | Preserve the original wording while clarifying the applicable classification.
Duplicate | Check the connection; do not discard similar reports merely because their wording resembles an earlier case.
Prompt internal routing | Follow the actual procedure and applicable timelines, not a deadline invented for this language exercise.''',
    d='''Which handoff is most precise? | Severe dizziness was reported after LM-4 use; seriousness and causality remain unassessed. | LM-4 definitely caused a serious reaction. | No serious event occurred because hospitalization was not mentioned. | The patient recovered because no outcome was supplied. | The precise handoff preserves the reported symptom while distinguishing unknown classifications and outcomes.
What should happen while missing details are sought? | Route available information promptly under the stated procedure and document follow-up. | Keep the report outside the safety process until every field is complete. | Delete the original wording after choosing a code. | Give a medication-change instruction to improve the report. | The stated process requires timely internal routing and follow-up, not waiting for complete information or providing treatment advice.
Which follow-up asks for a missing fact without leading the reporter? | Was the patient hospitalized, and what was the outcome? | Please confirm the product was definitely responsible. | Can you change severe to mild so the case is simpler? | Since the patient recovered, can we close the case? | The neutral question seeks hospitalization and outcome facts that are absent without suggesting the desired answer.
What does a temporal association establish? | That the event and product use have a stated timing relationship, not necessarily causation | That the product caused the event in every similar patient | That a label update is automatically required | That further assessment is unnecessary | Temporal association concerns timing; causal conclusions and labeling decisions require the relevant assessment.''',
    dialogue='''Nora | I received a clinician's message about dizziness after LM-4 use. The clinician called it severe, but several details are missing. I want to route it correctly.
Rafael | Send the available information through [[case intake::Case intake records the available report so assessment and follow-up can proceed under the required process.]] now, as our procedure requires. We can document what is unknown and arrange follow-up without waiting for you to complete a safety assessment yourself.
Nora | I have kept the clinician's wording. There is no statement about hospitalization, a life-threatening condition, or another criterion that would establish seriousness.
Rafael | Keep [[severity::Severity describes the reported intensity, while seriousness depends on separate applicable criteria.]] separate from seriousness. Severe describes intensity; it does not settle the regulatory classification. We need to clarify the relevant facts rather than translate one word directly into the other.
Nora | The event occurred after product use, but the message gives no exact dates. I cannot tell how close the timing was or whether other explanations were considered.
Rafael | Describe a reported [[temporal association::Temporal association concerns timing and does not by itself prove that the product caused the event.]], not proven causation. The safety assessment will consider the available evidence. Do not add a causal conclusion that the source did not establish.
Nora | We are missing dose, outcome, and other medicines. I will list those gaps so they remain visible in the structured record.
Rafael | Include [[concomitant medications::Concomitant medications are other medicines used in the relevant period and are missing from this report.]] in the follow-up request. Record unknown fields as unknown; absence of information must not become an assertion that no other medicine was used.
Nora | The clinician's exact phrase is severe dizziness. Should I replace it with a preferred term before sending the message, so the record looks consistent?
Rafael | Preserve the [[verbatim term::The verbatim term preserves the original reporter's wording, even when standardized coding is added later.]]. Appropriate coding can be added through the process, but the original wording remains important. Standardization should not erase what the reporter actually said.
Nora | I can ask when the dizziness started, whether it resolved, and whether hospitalization occurred. I should avoid asking the clinician to confirm a conclusion we prefer.
Rafael | Make the [[follow-up request::A follow-up request seeks missing facts neutrally rather than suggesting the answer or demanding proof of causation.]] neutral and specific. Ask for the facts needed to assess the case, and document the request and response through the required channel.
Nora | Who owns that contact? I do not want both teams to approach the reporter independently and create two incomplete versions of the same conversation.
Rafael | We will assign an owner and use [[case reconciliation::Case reconciliation checks related records and handoffs so the same case is consistently accounted for across teams.]] to keep the records aligned. If another report arrives, assess whether it is connected rather than assuming similar wording means a duplicate.
Nora | The commercial team may ask whether this is a new safety signal. I do not think this handoff alone answers that broader question.
Rafael | Correct. A [[safety signal::A safety signal suggests a possible new or changed risk requiring evaluation, not a confirmed causal conclusion from this handoff.]] requires evaluation in context. This individual report contributes information, but we should not announce a confirmed new risk or dismiss it without assessment.
Nora | I also want the internal update to avoid implying that a label change has been decided. We are much earlier in the information process.
Rafael | Any [[benefit-risk assessment::Benefit-risk assessment considers favorable and unfavorable effects in context; this incomplete report does not determine a labeling decision.]] or labeling action belongs in the qualified review process. Our immediate task is accurate capture, appropriate routing, and follow-up, not deciding the product's overall profile.
Nora | I will route the original message, identify every missing field, and note the agreed follow-up owner. Clinical treatment questions will stay with the qualified treating professional.
Rafael | Please request [[receipt confirmation::Receipt confirmation closes the handoff by establishing that the safety team received the information.]] as well. That gives us a closed handoff rather than an assumption that sending a message means the information reached the right team.''',
    transfer_title='Unknown is not negative',
    transfer_setup='A report says a rash occurred after product use. It does not state hospitalization, outcome, or a causal assessment. The applicable internal process requires routing available information now.',
    transfer='''Associate: "Hospitalization status is ___." | unknown | The report contains no hospitalization information, so neither occurrence nor absence can be asserted.
Reviewer: "The timing does not establish ___." | causation | Occurrence after use supplies a temporal relationship, not proof that the product caused the rash.
Associate: "I will route the available report ___." | now | The stated process requires routing the information now rather than waiting for every missing detail.
Reviewer: "Record the missing details for ___." | follow-up | Additional information is needed, and the reporting process must preserve the outstanding questions.'''))

BOOK['units'].append(unit(
    title='CMC, CGMP, Quality Events, Manufacturing, and Supply',
    scene='A gap in the batch record',
    skill='Report a quality-documentation gap precisely and separate investigation status from batch disposition.',
    brief='Batch Q-214 lacks a verification entry; whether the check occurred is unknown. The batch remains under quality review, not released. Production lead Diego asks quality specialist Helen whether available laboratory results justify saying fully reviewed. Site procedure requires documented investigation and authorized disposition. Neither may backdate an entry, assume the check occurred, or promise release to meet a shipment date.',
    cast='Diego | Production lead\nHelen | Quality specialist',
    culture=('Describe the gap without deciding the cause', 'Missing documentation is a fact; assuming the activity happened or did not happen adds a conclusion. State the observed gap, current batch status, investigation owner, and next update. This is more useful to supply colleagues than either premature reassurance or an unsupported declaration that the product failed.'),
    a='''What is established about batch Q-214? | A verification entry is missing and quality review remains open. | The batch has been released. | The verification definitely occurred. | The product definitely failed every laboratory test. | The brief establishes a documentation gap and open review, not completion, release, or a confirmed manufacturing failure.
Why is fully reviewed inaccurate? | The required investigation and authorized disposition are not complete. | Available laboratory results make all records irrelevant. | A shipment date automatically closes review. | A production request supplies quality authorization. | Laboratory results do not resolve the missing verification or complete the specified quality process.
Which action is excluded by the case? | Backdating an entry to make the record appear complete | Preserving the record | Investigating the gap | Giving supply an accurate status update | The brief expressly prohibits backdating and requires a documented investigation rather than retrospective fabrication.''',
    vocabulary='''chemistry, manufacturing, and controls | Product and process information addressing composition, manufacture, and quality control. | assess CMC readiness
current good manufacturing practice | Applicable requirements and practices supporting consistent pharmaceutical quality. | maintain CGMP compliance
batch record | Documentation of the production and control activities for a specific batch. | review the batch record
master production instruction | The authorized instruction defining how a product is to be manufactured. | follow master production instructions
verification entry | A record showing a required check and its associated information. | complete the verification entry
documentation gap | Missing or incomplete recorded information. | investigate a documentation gap
data integrity | The completeness, consistency, and accuracy of data through its lifecycle. | protect data integrity
contemporaneous record | A record made when the relevant activity occurs. | maintain contemporaneous records
traceability | The ability to follow an activity, material, or result through its records. | preserve traceability
deviation investigation | A structured examination of a departure from an applicable requirement or procedure. | conduct a deviation investigation
root cause | The underlying cause supported by investigation. | establish the root cause
corrective action | Action addressing a detected problem and its cause in the relevant system. | implement corrective action
preventive action | Action intended to prevent a potential problem from occurring. | define preventive action
CAPA | Corrective and preventive action, the system for addressing actual and potential quality problems. | verify CAPA effectiveness
effectiveness check | A review of whether an action achieved its intended result. | plan an effectiveness check
out-of-specification result | A test result outside established acceptance specifications. | investigate an out-of-specification result
out-of-trend result | A result inconsistent with an expected pattern, even when it may meet specifications. | evaluate an out-of-trend result
specification | Defined tests, procedures, and acceptance criteria for a material or product. | confirm the applicable specification
certificate of analysis | A document reporting specified test results for a material or batch. | verify the certificate of analysis
batch disposition | The authorized decision on how a batch may be used or handled. | document batch disposition
release authorization | Formal permission for a batch to proceed to the defined use or distribution. | verify release authorization
change control | The managed evaluation and authorization of proposed changes. | route a change through change control
stability program | Planned assessment of product quality over time under specified conditions. | maintain the stability program
supply constraint | A limit affecting availability or delivery. | communicate the supply constraint''',
    precision='Available test results are not the same as a completed batch review or release. The missing entry needs investigation under the applicable process. A signature added later must not falsely represent when an activity occurred; any permitted correction needs an accurate, traceable basis.',
    precision_extra='CMC means chemistry, manufacturing, and controls; CGMP means current good manufacturing practice; CAPA means corrective and preventive action. OOS means out of specification and OOT means out of trend. A documentation gap is not automatically an OOS test result or a proven product defect.',
    phrases='''State the observed gap | The verification entry is missing from the batch record.
Avoid an assumed cause | We have not established whether the check occurred.
Report the status | The batch remains under quality review and is not released.
Separate evidence | Available laboratory results do not complete the documentation review.
Protect integrity | Do not backdate or reconstruct an entry as though it were contemporaneous.
Request the investigation | Please identify the evidence needed to resolve this discrepancy.
Name the owner | Quality will coordinate the documented investigation under the site process.
Limit the supply update | Release timing is unconfirmed pending authorized disposition.
Preserve traceability | Any permitted correction must retain its source and history.
Distinguish results | This documentation issue is not itself an out-of-specification test result.
Check effectiveness | An action is not complete merely because a training session was scheduled.
Escalate pressure | The shipment deadline does not change the evidence or release authority.
Avoid blanket blame | Establish the cause before assigning an unsupported explanation.
Keep actions separate | Correction of the record and prevention of recurrence are distinct tasks.
Confirm authorization | Who has authority to make the batch-disposition decision?
Close with an update | We will provide the next status update without promising a release date.''',
    notes='''Fully reviewed | Use only when the applicable review is actually complete.
Performed versus documented | The absence of an entry leaves a question; it does not settle what happened.
Backdate | Do not make a later entry appear to have been made earlier.
OOS versus OOT | A specification failure and an unusual trend are different findings.
Investigation versus disposition | Finding the cause and authorizing batch use are related but separate steps.
Estimated versus authorized | A hoped-for shipment date is not release authorization.''',
    d='''Which supply update is supported? | Q-214 remains under quality review; release timing is unconfirmed. | Q-214 is fully reviewed because laboratory results are available. | Q-214 is released because a customer needs it tomorrow. | Q-214 definitely failed manufacturing because a field is blank. | The update states the actual open status without assuming either release or a confirmed product defect.
What does the missing entry prove by itself? | That required recorded information is absent | That the check definitely occurred | That the check definitely did not occur | That every test result is invalid | A missing entry establishes a documentation gap; the underlying event requires investigation.
Which action preserves data integrity? | Use the authorized correction process with an accurate, traceable account. | Add yesterday's date to make today's entry look timely. | Copy another batch's verification to fill the space. | Remove the blank page so the review looks complete. | An authorized, traceable correction preserves the true record rather than inventing evidence or concealing the gap.
What should a preventive response address? | The supported cause and a way to check whether recurrence risk is reduced | A convenient explanation chosen before investigation | Only the visual appearance of the record | A promise that no future quality issue is possible | A meaningful action follows evidence about the cause and includes a check of its intended effect.''',
    dialogue='''Diego | Supply wants a Q-214 update. Laboratory results are available, but the verification entry is missing. Can I say fully reviewed?
Helen | No. The [[batch record::The batch record contains a missing verification entry, so the required review is not complete.]] remains incomplete for review purposes, and the investigation is open. Available laboratory results do not resolve the missing verification or authorize release.
Diego | We do not know whether the check was undocumented or missed. I will not choose an explanation before we have evidence.
Helen | Call it a [[documentation gap::The documentation gap is the established missing information; its underlying cause has not yet been determined.]]. That states the observed fact without deciding the cause. The investigation should establish what evidence exists and what conclusions it can actually support.
Diego | A colleague suggested adding the signature with yesterday's date. They see it as tidying the record because production is under pressure.
Helen | That would misrepresent a [[contemporaneous record::A contemporaneous record is made when the activity occurs; a later entry must not falsely appear to have been made earlier.]]. We must not backdate or fabricate evidence. Any permitted later correction needs the appropriate process and an accurate account of its timing and basis.
Diego | I will preserve the original and supporting records. We need to understand the sequence without losing evidence of the discrepancy.
Helen | Exactly. Protect [[traceability::Traceability preserves the links between activities, evidence, and changes so the discrepancy can be reconstructed.]] throughout the investigation. A cleaner-looking page is not an improvement if it hides what was recorded, what changed, or why the change was made.
Diego | Is this an out-of-specification result? Supply uses that phrase broadly, but we have a missing entry rather than a test value.
Helen | An [[out-of-specification result::An out-of-specification result is a test result outside acceptance specifications, not merely missing documentation.]] is a different finding. Use the precise term so colleagues understand the problem we actually have instead of assuming a laboratory failure that has not been established.
Diego | We need an owner for the investigation and a realistic next update. I can make records and production personnel available through the site process.
Helen | Quality will coordinate the [[deviation investigation::The deviation investigation examines the discrepancy through the applicable documented process and identifies supported conclusions.]]. We should identify the evidence needed and document the findings before choosing a cause or claiming that the issue is resolved.
Diego | If the investigation finds a process weakness, simply asking everyone to be more careful may not address it. We need an action connected to the actual cause.
Helen | Yes. Establish the [[root cause::The root cause must be supported by investigation rather than selected because it is a convenient explanation.]] before prescribing the response. Training may be relevant in some circumstances, but we should not use it as a default explanation for every documentation problem.
Diego | The action plan should also show how we will know it worked. Finishing a task is not necessarily the same as preventing the same gap again.
Helen | Include an [[effectiveness check::An effectiveness check evaluates whether the action achieved its intended result, rather than merely confirming task completion.]] suited to the issue. The review should examine the intended result, not just confirm that a meeting occurred or a new form was issued.
Diego | Supply asks whether release tomorrow is likely. I can report the status, but cannot promise a decision quality has not made.
Helen | The [[batch disposition::Batch disposition is the authorized decision on batch use or handling, which remains pending here.]] remains pending under the authorized process. A shipment deadline does not change the evidence standard or transfer release authority to the production update.
Diego | Then I will say the batch is under review, the investigation is open, and the release date is unconfirmed. I will provide the next agreed status update.
Helen | That is accurate. Keep [[release authorization::Release authorization is formal permission to proceed; it cannot be inferred from available tests or a desired shipment date.]] separate from expectations about timing. We can communicate the supply constraint clearly without calling an unfinished review complete or declaring a defect that the facts have not established.''',
    transfer_title='A test report is not a release decision',
    transfer_setup='A certificate of analysis is available, but the batch-disposition record is pending. The current status says not released. A customer has requested shipment tomorrow.',
    transfer='''Planner: "The certificate reports test ___." | results | A certificate of analysis reports specified testing information, not every aspect of the release decision.
Quality: "Batch disposition is still ___." | pending | The briefing states that the authorized disposition record has not been completed.
Planner: "The current status is not ___." | released | The supplied status expressly says not released, despite the available certificate.
Quality: "The customer request does not supply release ___." | authorization | A delivery request cannot replace the applicable authorized decision on whether the batch may ship.'''))


BOOK['units'].append(unit(
    title='Labeling, Medical Affairs, Promotion Review, and Compliance Boundaries',
    scene='Stronger wording changes the claim',
    skill='Identify an unsupported promotional implication and return a precisely scoped claim through the required review route.',
    brief='A fictional approved source supplied for an internal exercise describes a lower mean symptom score versus placebo at week 12 in a defined adult study population. A promotional draft instead says immediate relief for every patient and places risk information in an unreadable footnote. No evidence supports immediate onset or benefit in every patient. The complete revised item requires medical, legal, and regulatory review before external use. Medical reviewer Sofia and brand colleague Adam must restore the supported scope without treating familiar wording or an approaching deadline as final approval.',
    cast='Sofia | Medical reviewer\nAdam | Brand colleague',
    culture=('Explain what changed in the meaning', 'A review comment is more useful when it identifies the unsupported implication and the evidence boundary, rather than merely saying noncompliant. Offer wording tied to the supplied source, keep risk information appropriately visible, and identify the decision still required before the material can be used.'),
    a='''Which part of the draft is unsupported by the supplied source? | Immediate relief for every patient | A comparison with placebo | Assessment at week 12 | A defined adult study population | The supplied claim concerns a mean score at week 12, not immediate onset or a benefit for every individual.
What remains necessary before external use? | Review and approval of the complete revised item through the stated process | Only a check that the headline uses familiar words | Only the brand colleague's confirmation of the deadline | Reuse of approval from any earlier version | The case requires review of the complete revised item, not just a phrase or an earlier version.
Why is the risk footnote a concern? | Its unreadable presentation undermines meaningful communication of risk. | Any footnote is automatically prohibited in every context. | Risks cease to matter when the benefit is a mean difference. | Risk information belongs only in internal records. | The problem is the unreadable presentation, not a universal prohibition on footnotes or the existence of a benefit claim.''',
    vocabulary='''approved labeling | The regulator-authorized product information in the relevant jurisdiction. | check approved labeling
prescribing information | The professional product information describing authorized use and relevant details. | consult the prescribing information
promotional claim | A statement or implication used to communicate a product benefit or attribute in promotion. | substantiate a promotional claim
claim substantiation | Evidence supporting the precise meaning of a claim. | verify claim substantiation
fair balance | Appropriate presentation of benefit and risk information in the relevant promotional context. | assess fair balance
risk disclosure | Communication of relevant risks and limitations. | improve risk disclosure
material limitation | A qualification important to understanding a claim accurately. | retain material limitations
intended audience | The people a communication is designed to reach. | identify the intended audience
indication boundary | The limits of the use or population described by the relevant authorization. | preserve the indication boundary
onset claim | A claim about when a treatment effect begins. | substantiate an onset claim
comparative claim | A claim comparing products, treatments, or outcomes. | review comparative claims
absolute claim | An unqualified assertion suggesting no exceptions. | challenge an absolute claim
net impression | The overall meaning conveyed by words, visuals, and presentation together. | evaluate the net impression
qualifier | Language restricting the scope of a statement. | keep the qualifier visible
medical affairs | The function supporting scientific and medical exchange within its responsibilities. | consult medical affairs
medical information | The function providing appropriate responses to product-related medical inquiries. | route a medical-information inquiry
unsolicited request | An inquiry not prompted or solicited through the relevant promotional activity. | document an unsolicited request
off-label use | Use outside the authorized labeling in the relevant jurisdiction. | distinguish an off-label question
scientific exchange | Communication of scientific information in an appropriate context. | define the scientific-exchange context
medical-legal-regulatory review | Cross-functional review of materials under the applicable company process. | complete MLR review
reference pack | The supporting evidence linked to a communication's claims. | update the reference pack
redline | A version showing proposed text changes. | review the redline
approval expiry | The end of a material's permitted use period under the applicable process. | check approval expiry
final-form approval | Authorization of the complete version in its intended presentation. | obtain final-form approval''',
    precision='A group mean difference does not mean every patient benefits. A week-12 assessment does not establish immediate onset. Qualifiers about population, comparator, timing, and measure carry substantive meaning; removing them can create a different claim even when individual words remain familiar.',
    precision_extra='MLR means medical-legal-regulatory review; USPI means US prescribing information. Review must consider context, audience, channel, visuals, and risks. These examples are not approved copy; follow applicable requirements and the actual review process.',
    phrases='''Identify the overreach | Immediate relief is not supported by the week-12 assessment.
Preserve the population | The supplied evidence concerns the defined adult study population.
Keep the measure | The finding is a difference in mean symptom score, not universal relief.
Name the comparator | Retain versus placebo where it is part of the supported statement.
Challenge an absolute | Every patient implies a guarantee the source does not establish.
Review the whole item | The headline, visual, and footnote must be assessed together.
Make risk readable | Risk information must not be reduced to unreadable text.
Tie the comment to evidence | Please align this sentence with the cited source and its limitations.
Route the inquiry | The off-label question should follow the appropriate medical-information process.
Separate contexts | A scientific response is not automatic permission to reuse a claim in promotion.
Check the version | Approval of an earlier item does not establish approval of this revision.
Request final review | Return the complete final-form item through the required review route.
Preserve the caveat | This qualifier belongs next to the claim it limits.
Avoid deadline pressure | The publication date does not replace approval.
Close the action | I will identify the unsupported implication and the supported alternative.
State current status | The item remains pending review and is not ready for external use.''',
    notes='''Mean versus every | A group average does not describe every individual's response.
At week 12 versus immediately | These are different timing claims.
Overall presentation | A technically accurate sentence can still sit within a misleading visual message.
Tiny qualification | A qualification that cannot be read does not reliably correct the headline's impression.
Off-label inquiry | Route through the appropriate process; do not improvise a promotional response.
Final form | Review the version that will actually be used, including layout and linked content.''',
    d='''Which revision best preserves the supplied scope? | Lower mean symptom score versus placebo at week 12 in the defined adult study population | Relief in adults, with timing omitted because the study lasted twelve weeks | Immediate improvement in the average patient | Proven symptom relief for all adults who receive treatment | Only the first wording retains the measured outcome, comparator, timepoint, and defined population without adding a universal or onset claim.
What is the best review comment on the headline? | It adds an onset claim and an individual guarantee absent from the supplied evidence. | It is acceptable once a source number is added. | It is only a stylistic change because relief and score are related. | It is acceptable if the universal claim is placed in a visual instead of text. | The draft changes the substantive meaning; a citation or change of presentation does not establish the missing evidence.
Which action addresses the footnote problem? | Revise the risk presentation so it is readable and assess the complete item's balance. | Keep the text unchanged because it is technically present. | Remove the risk information to reduce visual clutter. | Assume the source document's risks need not appear in a reviewed communication. | Meaningful risk communication requires attention to presentation and context, not merely the physical presence of tiny text.
A colleague asks about an unapproved use. What is the appropriate response here? | Route the inquiry through the relevant medical-information process without repurposing it as promotion. | Add the use to the promotional slide while review is pending. | Treat an internal discussion as a new approved indication. | Answer with the strongest benefit sentence from the draft. | The communication context and approved scope matter; the inquiry does not authorize an expanded promotional claim.''',
    dialogue='''Adam | The creative team shortened the headline to immediate relief for every patient. They say it carries the same idea as the approved source, but more clearly.
Sofia | It changes the [[promotional claim::The promotional claim now adds immediate onset and universal benefit, neither of which the supplied evidence supports.]]. The source describes a lower mean symptom score versus placebo at week twelve in a defined adult population. Those qualifications are part of the meaning.
Adam | I see that every patient is stronger than an average difference. The study result does not tell us that all participants responded in the same way.
Sofia | Correct. That [[absolute claim::An absolute claim suggests no exceptions; a group mean result does not establish benefit for every patient.]] is unsupported. We should not turn a group result into an individual guarantee, even if the wording sounds accessible and avoids technical language.
Adam | Immediate is also new. The source identifies a week-twelve assessment, but it does not say when any effect began.
Sofia | Then remove the [[onset claim::An onset claim concerns when an effect begins; a week-12 assessment does not establish immediate relief.]] unless appropriate supporting evidence and review establish it. A timepoint of measurement cannot silently become a claim about the first moment of benefit.
Adam | Could we retain a shorter line and put all the conditions in the footnote? The current layout has very little space below the image.
Sofia | A [[material limitation::A material limitation affects the accurate interpretation of the claim and should not disappear into unreadable text.]] must remain meaningfully available in context. Moving essential conditions into unreadable text does not reliably repair the stronger message in the headline.
Adam | The risk information has the same problem. It is technically on the page, but at the current size it is difficult to read.
Sofia | Review the [[fair balance::Fair balance concerns appropriate benefit-risk presentation; merely including unreadable risk text does not resolve the issue.]] of the complete item. We need to assess how benefit and risk are communicated, not just tick a box saying that a block of risk text exists.
Adam | The image shows a person returning immediately to normal activity. Even with a revised sentence, that could keep suggesting a rapid and universal benefit.
Sofia | Exactly. Assess the [[net impression::Net impression is the combined meaning of wording, imagery, and layout, not just the literal accuracy of one sentence.]] created by words and visuals together. Correcting one sentence is insufficient if the overall presentation still makes the unsupported implication.
Adam | I will send the revised wording with the evidence references. That should make it easier to see which source supports each part of the claim.
Sofia | Update the [[reference pack::The reference pack links claims to their supporting evidence and allows reviewers to check the precise scope.]] and check the exact scope. A source citation is useful only when it supports the statement actually made, including population, comparator, timing, and outcome.
Adam | A field colleague has also asked whether this could be used for a different, unapproved condition. That question should not go into this promotional revision.
Sofia | Route it through [[medical information::Medical information provides the appropriate route for the inquiry; the question does not authorize an expanded promotional claim.]] under the applicable process. The existence of a scientific question does not expand the approved indication or authorize a new promotional use.
Adam | Once the edits are complete, can the brand team publish because the original item was approved? The deadline is close, and most of the layout is unchanged.
Sofia | The revised item still needs [[final-form approval::Final-form approval applies to the complete version intended for use; approval of an earlier item does not cover every revision.]]. Earlier approval does not automatically cover changed claims or presentation. The deadline does not replace the required decision.
Adam | I will keep it pending, attach the redline, and return the full item through review. The revised wording will match the supplied evidence.
Sofia | Good. The [[medical-legal-regulatory review::Medical-legal-regulatory review assesses the revised communication through the required cross-functional process before external use.]] should see the actual version intended for use. We can make the message readable without deleting the limits that make it accurate.''',
    transfer_title='Earlier approval, changed meaning',
    transfer_setup='An approved internal example says benefit was measured at week 12 in adults. A revision says rapid benefit in all ages. The revised item has not completed review.',
    transfer='''Reviewer: "Rapid adds an unsupported ___ claim." | onset | The source supplies a week-12 measurement, not evidence about how quickly benefit begins.
Author: "All ages expands the stated ___." | population | The original example concerns adults, while the revision extends the claim beyond that group.
Reviewer: "Earlier approval does not cover this changed ___." | version | A substantive revision must be assessed under the applicable process rather than inheriting approval automatically.
Author: "External use remains ___." | pending | The revised item has not completed review, so the briefing supplies no authorization for external use.'''))

BOOK['units'].append(unit(
    title='Market Access, RWE, Launch Readiness, Biosimilars, and Lifecycle Management',
    scene='Two sources, different questions',
    skill='Explain differences between study designs and keep evidence, economic assumptions, and access decisions distinct.',
    brief='An access deck combines a 12-week randomized placebo-controlled trial in 400 adults with a six-month observational analysis of routine-care claims from 5,000 adults. The trial measures symptom score; the claims analysis measures hospitalization. Baseline differences and treatment-selection factors remain incompletely assessed in the claims analysis. The draft calls the combined material one randomized proof of reduced hospitalizations and guaranteed coverage. Access lead Mina and evidence specialist Jules must separate the evidence streams and qualify both causal and payer claims. No payer decision has been received.',
    cast='Mina | Market-access lead\nJules | Evidence specialist',
    culture=('Different evidence can complement without merging', 'Explain what each source answers before placing results side by side. A larger routine-care dataset may broaden context without becoming randomized evidence. Likewise, clinical results, economic models, and coverage decisions address different questions. A useful access conversation makes these boundaries visible without dismissing a source simply because it has limitations.'),
    a='''Which source measures hospitalization? | The six-month observational claims analysis | The 12-week trial's stated symptom-score endpoint | Both sources using an identical protocol | A completed payer coverage decision | The brief assigns hospitalization to the claims analysis and symptom score to the trial.
Why is one randomized proof inaccurate? | The claims analysis is observational and uses a different outcome and follow-up period. | Routine-care data can never contribute evidence. | A 5,000-person analysis automatically has fewer participants than a 400-person trial. | Placebo-controlled studies cannot measure symptoms. | The sources differ in design, endpoint, and duration; combining slides does not make the observational analysis randomized.
What is the status of coverage? | No payer decision has been received. | Guaranteed by the observational sample size | Approved by the trial's completion | Identical to the investigator's efficacy assessment | The briefing explicitly says no payer decision exists, so coverage cannot be reported as guaranteed.''',
    vocabulary='''market access | Work addressing whether and how patients can obtain a product within a health system. | develop the market-access plan
payer | An organization or body funding or reimbursing health care. | address payer evidence needs
coverage decision | A decision defining whether and under what conditions a payer funds a service or product. | track the coverage decision
formulary | A payer or system's list of medicines and associated access conditions. | review formulary status
prior authorization | A requirement for advance approval before specified coverage applies. | clarify prior-authorization criteria
health technology assessment | Structured evaluation of a health technology's effects and implications in context. | prepare for health technology assessment
value dossier | A structured presentation of clinical, economic, and other evidence for an access audience. | tailor the value dossier
real-world data | Routinely collected information about health or health-care delivery. | assess real-world data quality
real-world evidence | Clinical evidence generated by analyzing real-world data using an appropriate study design. | evaluate real-world evidence
claims data | Records created for billing or reimbursement of health-care services. | assess claims-data limitations
observational study | A study in which the investigator does not assign the treatment under study. | describe the observational study
confounding | Distortion of an exposure-outcome comparison by other relevant factors. | address confounding
confounding by indication | Differences in treatment choice related to prognosis or clinical need that affect comparison. | assess confounding by indication
selection bias | Distortion related to how participants or observations enter the analysis. | examine selection bias
residual confounding | Confounding remaining after the applied adjustment. | acknowledge residual confounding
external validity | How well findings apply beyond the studied setting or population. | assess external validity
comparative effectiveness | Comparison of health outcomes from different care options in relevant settings. | evaluate comparative effectiveness
budget impact | The expected change in spending for a specified budget holder over a defined period. | model budget impact
cost-effectiveness | Assessment of costs relative to health outcomes for compared options. | examine cost-effectiveness assumptions
uptake assumption | An estimate of how many eligible people will use a product over time. | test the uptake assumption
launch readiness | Preparedness of the relevant functions for a planned market introduction. | verify launch readiness
biosimilar | A biological product shown to be highly similar to a reference product without clinically meaningful safety or effectiveness differences. | evaluate a biosimilar evidence package
reference product | The authorized biological product used as the comparator for biosimilar development. | identify the reference product
lifecycle management | Planned development and stewardship of a product across its commercial and regulatory life. | align lifecycle management''',
    precision='Real-world describes data context, not guaranteed quality or one study design. Randomized studies can use routine data. This claims comparison, however, is observational, with treatment-selection issues still incompletely assessed.',
    precision_extra='RWD means real-world data; RWE, real-world evidence; HTA, health technology assessment. Budget impact estimates spending; cost-effectiveness relates costs to health outcomes. Neither analysis, nor regulatory approval alone, establishes payer coverage.',
    phrases='''Separate the sources | The trial and claims analysis answer different questions.
State the design | The claims comparison is observational, not randomized.
Keep the outcome clear | The trial measures symptom score; the claims analysis measures hospitalization.
Preserve follow-up | The studies use different observation periods.
Qualify causality | Treatment-selection differences may affect the observed association.
Ask about adjustment | Which confounders were measured, and what uncertainty remains?
Avoid sample-size overreach | A larger dataset does not remove systematic bias by itself.
Retain useful context | Routine-care evidence may add context without replacing the trial's design.
Separate economic questions | Budget impact and cost-effectiveness are not interchangeable.
Expose model inputs | Uptake and eligible-population assumptions should remain visible.
Limit the coverage claim | No payer decision has been received.
Check the audience | Which evidence question is this payer asking us to address?
Distinguish similarity | Biosimilarity is a specific evidence and regulatory concept, not a loose claim of being similar.
Avoid automatic substitution claims | Substitution implications require the relevant product status and applicable rules.
Track launch dependencies | Clinical evidence does not complete every access and supply dependency.
Close the deck | Label each evidence stream, its limitations, and the decision it can inform.''',
    notes='''Association versus causation | An observed difference needs a defensible causal design and assumptions before a causal interpretation.
Large versus unbiased | More records can increase precision without removing confounding.
Trial versus routine care | State the actual design instead of ranking evidence by a label alone.
Coverage versus approval | Regulatory authorization and payer funding are different decisions.
Biosimilar versus interchangeable | These are not identical terms; implications depend on jurisdiction and product status.
Forecast versus commitment | A modeled uptake rate is not a payer commitment or confirmed patient count.''',
    d='''Which summary is best supported? | The trial assesses symptoms; the observational claims study examines hospitalizations with unresolved confounding questions. | Both studies independently prove the same hospitalization effect. | The claims analysis is randomized because the trial is randomized. | The larger sample makes treatment-selection assessment unnecessary. | The accurate summary preserves each source's design, outcome, and unresolved limitation.
What should be checked before interpreting the claims difference causally? | Treatment selection, measured confounders, remaining bias, and the analysis design | Only whether the sample exceeds the trial's sample | Only whether the result supports the launch message | Whether the trial used an unrelated symptom scale | Causal interpretation depends on the design and assumptions, not merely sample size or a favorable result.
Which statement about economic evidence is accurate? | Budget impact estimates spending for a defined budget holder; cost-effectiveness relates costs to health outcomes. | Budget impact proves that a product is clinically superior. | Cost-effectiveness guarantees that every payer will provide coverage. | An uptake assumption is the same as an executed coverage decision. | These economic analyses address different questions and do not themselves determine clinical superiority or coverage.
Which launch update preserves the actual status? | The access evidence package is being revised; payer decisions remain pending. | Coverage is guaranteed because the evidence sources were combined. | Every launch dependency is complete once a trial ends. | The claims dataset authorizes unrestricted substitution of all biological products. | The brief states that no payer decision has been received and the deck still needs correction.''',
    dialogue='''Mina | The access deck combines the trial and claims results under one headline: randomized proof of fewer hospitalizations and guaranteed coverage. That seems to merge several different claims.
Jules | Start by separating the [[evidence streams::The evidence streams differ in study design, outcome, and follow-up, so their findings cannot be presented as one randomized result.]]. The trial assessed symptom score over twelve weeks. The claims analysis assessed hospitalization over six months in a different, routine-care population.
Mina | The trial randomized four hundred adults, while the claims dataset contains five thousand. The larger number is attracting more attention in the discussion.
Jules | Size does not change the [[observational design::The observational design did not assign treatment randomly; a larger sample does not change that fact.]]. Treatment was not assigned by the claims study. We need to examine how people entered each treatment group and which differences might affect their outcomes.
Mina | Patients receiving one treatment could have had different clinical needs before follow-up began. Those needs might also affect their chances of hospitalization.
Jules | That raises [[confounding by indication::Confounding by indication arises when treatment choice relates to clinical need or prognosis that also affects outcomes.]]. We should ask which relevant factors were measured and addressed, while acknowledging that the current assessment is incomplete.
Mina | The team adjusted for some recorded characteristics. That is useful, but the slide now says adjustment removed every possible source of bias.
Jules | It cannot establish that from the supplied information. [[Residual confounding::Residual confounding is distortion remaining after adjustment, which cannot be ruled out merely by listing adjusted variables.]] may remain, particularly for factors not adequately captured. Explain the approach and limitations rather than describe adjustment as a universal cure.
Mina | We should still show what the routine-care analysis adds. It may help an access audience understand patterns outside the trial's narrower setting.
Jules | Yes. Discuss [[external validity::External validity concerns applicability beyond the studied setting; routine-care context may help but does not automatically guarantee generalizability.]] without assuming that all routine-care records represent every intended patient. Data relevance and quality need examination alongside the study design.
Mina | The phrase real-world evidence is being used as though it automatically means observational. That is too broad, even though this particular study is observational.
Jules | Correct. [[Real-world data::Real-world data describes routinely collected health information; the study design using those data must be specified separately.]] describes the data context. Different designs can use those data. In this case, we should state the actual observational design rather than let the label do the explaining.
Mina | The financial slide also combines budget impact with cost-effectiveness. One estimates payer spending, while the other relates costs to health outcomes.
Jules | Keep the [[budget impact::Budget impact estimates spending consequences for a specified budget holder over a defined period, not value per health outcome.]] model separate and state its horizon, eligible population, and uptake assumptions. A useful economic result depends on a clearly defined question and inputs.
Mina | The uptake assumption is twenty percent of an estimated eligible population. It is a planning input, not a confirmed number of people who will receive coverage.
Jules | Then label the [[uptake assumption::The uptake assumption is a model input about use, not a confirmed patient count or payer commitment.]] prominently. The model should not transform an estimate into a commitment simply because it appears in a launch forecast.
Mina | We have no payer decision yet. The headline's guaranteed coverage wording could create expectations that neither the evidence team nor the access team can support.
Jules | A [[coverage decision::A coverage decision is the payer's funding determination, which has not been received in this case.]] is distinct from the clinical findings and economic models. State the current status and any unresolved evidence requests instead of promising an outcome.
Mina | I will revise the deck into separate trial, routine-care, economic, and access sections. Each result will retain its design, population, period, and limitations.
Jules | That supports a realistic [[launch-readiness::Launch-readiness assessment checks multiple dependencies; evidence preparation alone does not establish coverage, supply, or complete operational readiness.]] discussion. We can explain what is ready, what remains under review, and who owns each dependency without presenting a collection of evidence as a completed launch decision.''',
    transfer_title='An assumption is not a covered population',
    transfer_setup='A fictional spending model assumes 10,000 eligible adults, 20% uptake, and $300 incremental annual spending per user. No offsets or other costs are included. No payer decision is available.',
    transfer='''Analyst: "The model assumes ___ users." | 2,000 | Twenty percent of 10,000 eligible adults equals 2,000 modeled users, not a confirmed covered population.
Reviewer: "The modeled annual spending increase is ___." | $600,000 | Multiply 2,000 modeled users by $300 each, with no other costs or offsets included.
Analyst: "The 20% figure is an uptake ___." | assumption | The briefing identifies the figure as a planning input rather than an observed or guaranteed use rate.
Reviewer: "Coverage remains ___." | undecided | No payer decision has been supplied, so the model cannot establish that coverage has been granted.'''))
