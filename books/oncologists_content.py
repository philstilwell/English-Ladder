"""Original English for oncology consultations, multidisciplinary review, and supportive care."""
from books.medical_support import medical_unit as unit, source, SCOPE

BOOK = dict(slug='oncologists', title='Oncology English', cover_label='ENGLISH FOR ONCOLOGISTS',
    cover_title='Oncology', cover_size=42, tagline='Explain precisely. Leave room to respond.',
    audience='For oncologists, oncology fellows, and physicians coordinating cancer care.',
    roles='oncologists, medical oncologists, radiation oncologists, surgical oncologists, oncology fellows',
    summary='Specialist English for diagnosis discussions, staging, biomarkers, treatment intent, toxicity reports, scan reviews, research consent, and supportive care.',
    map_intro='Eight oncology encounters practice difficult news, staging language, biomarker uncertainty, treatment choices, symptom escalation, response assessment, trial discussions, and care goals.',
    notes_title='Precision without emotional distance.',
    notes_intro='Oncology conversations often carry unfamiliar terminology and strong emotion at the same time. These original cases practice small information steps, explicit uncertainty, and a clear next conversation.',
    field_notes=[
        ('Ask how much information is wanted', 'Check the patient\'s understanding and information preference. Pause after difficult news instead of covering silence with more terminology.', '"Would you like the main finding first, then time for questions?"'),
        ('Separate related technical terms', 'Stage, grade, response, remission, and cure answer different questions. State what the available evidence supports and what remains unresolved.', '"The pathology establishes the diagnosis; staging is still incomplete."'),
        ('Make the treatment aim explicit', 'A discussion of benefit needs a stated goal and uncertainty. Avoid describing control, symptom relief, and cure as interchangeable outcomes.', '"The aim of this option is disease control; it is not a guarantee."'),
        ('Connect support with active care', 'Pain, distress, practical needs, and family communication belong in cancer care. A supportive-care referral does not by itself mean anticancer treatment is ending.', '"We can address symptoms alongside the cancer treatment discussion."'),
    ], scope_note=SCOPE,
    sources=[
        source('National Cancer Institute. Cancer Staging.', 'https://www.cancer.gov/about-cancer/diagnosis-staging/staging', 'Terminology context for extent of disease and staging; no fictional case supplies a staging algorithm.'),
        source('National Cancer Institute. Biomarker Testing for Cancer Treatment.', 'https://www.cancer.gov/about-cancer/treatment/types/biomarker-testing-cancer-treatment', 'Background on biomarker findings, treatment relevance, and the limits of a possible match.'),
        source('National Cancer Institute. Palliative Care in Cancer.', 'https://www.cancer.gov/about-cancer/advanced-cancer/care-choices/palliative-care-fact-sheet', 'Context for supportive care alongside treatment and the distinction from hospice care.'),
        source('National Cancer Institute. Taking Part in Cancer Treatment Research Studies.', 'https://www.cancer.gov/publications/patient-education/crs.pdf', 'Background for voluntary research participation and informed-consent discussions.')], units=[])

BOOK['units'].append(unit(
    title='Explaining a new cancer diagnosis', scene='The first clear sentence',
    skill='Deliver an established finding in small steps while responding to emotion and information preferences.',
    brief='Dr Imani meets Maya after a pathology report confirms a malignant tumor. Staging is incomplete, and no treatment recommendation or prognosis estimate has been established. Maya wants the main finding first and then a pause. Maya has not yet decided whether a relative should join. The clinician must give the finding plainly, acknowledge the response, and separate the diagnosis from unanswered questions.',
    cast='Dr Imani | Oncologist\nMaya | Patient',
    culture=('A pause is part of the conversation', 'Silence after difficult news need not be filled with statistics. Check what the person wants next and who they want involved, without assuming either preference.'),
    a='''What is established? | A malignant tumor on pathology | A completed stage | A guaranteed treatment outcome | A survival estimate | The pathology confirms malignancy; staging and individual outcomes remain unresolved.
What does Maya request? | The main finding followed by a pause | Every statistic immediately | Disclosure to all relatives automatically | No explanation ever | Maya's stated preference is a clear main finding and time to respond.
What family decision is unfinished? | Whether a relative should join | Whether all relatives consented | Whether the relative is the decision-maker | Whether privacy no longer applies | Maya has not yet chosen whether to include a relative.''',
    vocabulary='''pathology report | Laboratory interpretation of examined tissue or cells. | review the pathology report
biopsy | Removal of tissue or cells for examination. | explain the biopsy finding
malignancy | Cancerous disease characterized by malignant cells or tissue. | explain a confirmed malignancy
histology | Microscopic study of tissue structure and features. | review the histology
primary tumor | Tumor at the site where the cancer began. | identify the primary tumor
diagnostic disclosure | Communication of an established diagnosis to the patient. | prepare for diagnostic disclosure
warning statement | Brief introduction preparing a listener for difficult information. | use a clear warning statement
information preference | How much detail a person wants and how they want it presented. | check the information preference
emotional acknowledgment | Recognition of the listener's expressed feelings or response. | offer emotional acknowledgment
prognostic uncertainty | Incomplete ability to predict an individual's future disease course. | explain prognostic uncertainty
staging workup | Investigations used to establish the extent of cancer. | complete the staging workup
multidisciplinary team | Professionals from different specialties contributing to a care discussion. | consult the multidisciplinary team
second opinion | Assessment or advice from another qualified clinician. | arrange a second opinion
care navigator | Professional helping a person move through services and appointments. | contact the care navigator
support person | Individual the patient wants involved for assistance. | invite a chosen support person
diagnostic certainty | Degree to which the diagnosis is established by evidence. | distinguish diagnostic certainty
information overload | More information than a listener can usefully process at one time. | avoid information overload
follow-up consultation | Later meeting to review findings, options, or unresolved questions. | arrange a follow-up consultation''',
    precision='The diagnosis is established in this case, but stage, treatment, and prognosis are not. Do not soften a confirmed finding into vagueness or turn it into an unsupported prediction.',
    precision_extra='Ask permission before involving a relative. A support person is not automatically a substitute decision-maker.',
    phrases='''Prepare for the finding | I am afraid the result is not what we hoped for.
Name the diagnosis | The tissue examination confirms a malignant tumor.
Allow a pause | We can stop here for a moment.
Acknowledge emotion | I can see that this is a great deal to take in.
Separate questions | We know the diagnosis; we do not yet know the full extent.
Ask about support | Would you like someone you choose to join us?
Limit a prediction | I cannot give an individual outlook from this finding alone.
Offer continuity | We will arrange another conversation when the remaining results are available.''',
    notes='''Confirms | Appropriate here because the fictional pathology finding is established, unlike the incomplete stage.
Not yet | Keeps an unanswered question visible without treating uncertainty as a negative result.
Would you like | Invites a preference rather than assuming how much information or family involvement is wanted.''',
    d='''Which opening is clearest? | The tissue examination confirms a malignant tumor. | Something might be a little unusual, but who knows. | Everything is definitely curable. | The stage is already complete. | Naming the confirmed tumor states the established finding without obscuring it or inventing later conclusions.
Which response respects Maya's preference? | Pause after the main finding. | Continue through every statistic immediately. | Invite relatives without asking. | Demand an immediate treatment decision. | Maya explicitly requests time to respond before receiving more detail.
Which conclusion exceeds the facts? | The diagnosis alone establishes Maya's individual prognosis. | Staging remains incomplete. | The pathology confirms malignancy. | A later discussion is needed. | A confirmed diagnosis does not supply the missing stage or an individual outlook.
What should precede family involvement? | Clarifying Maya's wishes and the appropriate permissions | Assuming every relative may receive details | Treating attendance as legal authority | Posting the result publicly | Family involvement must reflect the patient's wishes and the applicable information-sharing rules.''',
    dialogue='''Dr Imani | Before we discuss the report, how much detail would you like in this first conversation?
Maya | The main finding first, please. My [[information preference::Information preference describes Maya's requested amount and sequence of detail for this difficult conversation.]] may change once I have heard it.
Dr Imani | I am afraid the result is not what we hoped for. The tissue examination confirms a [[malignant tumor::A malignant tumor is the cancerous finding established by the pathology in this fictional case.]].
Maya | Please give me a moment. I knew the [[biopsy::A biopsy provides tissue or cells for examination; here its report has established a malignant finding.]] might find something, but hearing that is different.
Dr Imani | Of course. We can pause. I can see this is a great deal to take in.
Maya | When I am ready, could you explain what the [[pathology report::The pathology report contains the interpretation of the examined tissue and supports the established diagnosis.]] tells you and what it does not?
Dr Imani | It establishes the cancer diagnosis. It does not yet give us every answer about the extent or treatment.
Maya | So the [[staging workup::The staging workup establishes the extent of disease and is still incomplete in this case.]] is a separate part of understanding what happens next?
Dr Imani | Yes. We need those remaining details before completing the treatment discussion or estimating your individual outlook.
Maya | I was about to ask how long I have. I hear that there is still [[prognostic uncertainty::Prognostic uncertainty means the individual future course cannot be established from the available finding alone.]].
Dr Imani | I will answer as honestly as I can, including what we do not know. I will not invent a number.
Maya | Thank you. I might want my brother here, but I have not chosen a [[support person::A support person is someone Maya chooses to involve; a relative is not automatically entitled to the information.]] for this conversation yet.
Dr Imani | You can decide. We will discuss what you want shared rather than assume that every family member is involved.
Maya | Could someone help me understand the appointments? I am finding even ordinary arrangements difficult to absorb.
Dr Imani | Our [[care navigator::A care navigator helps coordinate access and appointments without replacing the clinician's diagnostic or treatment responsibilities.]] can help with those arrangements while we keep the clinical questions with the appropriate team.
Maya | I do not want a large pack of unexplained information to be my only connection with the team.
Dr Imani | That would risk [[information overload::Information overload occurs when the volume of detail exceeds what a person can usefully process at the time.]]. We will give manageable information and a clear contact route.
Maya | I may also want another clinician to review the findings once I understand the next steps.
Dr Imani | We can discuss a [[second opinion::A second opinion is another qualified assessment and can be discussed without treating the request as disloyalty.]] and arrange a follow-up conversation. You do not need every decision settled in this first exchange.
Maya | For now, I understand the diagnosis is confirmed and the full extent is not. Please let us stop there briefly.''',
    rehearsal=['Read the corrected disclosure slowly. Pause after the finding and after Maya\'s request for time.', 'Swap roles. Repeat the distinction between a confirmed diagnosis and an incomplete stage without adding a prognosis.'],
    transfer_title='Check who should join', transfer_setup='Alex wants partner Ren to attend the next results conversation but has not authorized disclosure to other relatives. The next meeting will review outstanding findings; no outcome is supplied.',
    transfer='''Alex: "I would like ___ to join." | Ren | Ren is the chosen partner for the next conversation in this scenario.
Clinician: "The permission does not automatically include other ___." | relatives | The specified preference does not authorize broader family disclosure by itself.
Alex: "Some findings remain ___." | outstanding | The next meeting is intended to review findings that are still outstanding.
Clinician: "No outcome has been ___." | supplied | The case provides an arrangement for discussion, not a new clinical result.'''))

BOOK['units'].append(unit(
    title='Separating stage, grade, and prognosis', scene='Two terms on one report',
    skill='Explain closely related oncology terms without converting one into another.',
    brief='Theo has a pathology report that includes a tumor grade. Imaging needed for staging is still pending. Dr Malik must explain that grade concerns microscopic features while stage describes extent using the applicable cancer-specific system. No grade value, stage, or individual survival estimate is supplied. Theo has mistaken the grade for a completed stage.',
    cast='Theo | Patient\nDr Malik | Oncologist',
    culture=('Correct the interpretation, not the person', 'Technical terms can appear together on reports while answering different questions. Use a clear contrast and a brief check-back rather than telling the patient they read it incorrectly.'),
    a='''Which item is available? | A pathology report containing grade | A completed staging conclusion | A supplied survival estimate | All pending imaging | The pathology grade is available while the staging workup is unfinished.
What is pending? | Imaging needed for staging | Whether Theo attended | The word grade on the report | A confirmed cure | The brief explicitly identifies staging imaging as still pending.
What has Theo confused? | Grade with stage | A treatment cycle with a payment | A medicine with an appointment | Two confirmed diagnoses | Theo has interpreted the grade as though it were the completed stage.''',
    vocabulary='''tumor grade | Classification of microscopic tumor features under the relevant grading system. | explain tumor grade
cancer stage | Description of cancer extent under the applicable staging system. | establish the cancer stage
differentiation | Degree to which tumor cells resemble normal cells of their origin. | describe cellular differentiation
local extent | Spread of a tumor within its original area. | assess local extent
regional lymph node | Lymph node in the region draining or associated with the tumor site. | assess regional lymph nodes
distant metastasis | Cancer spread to a site distant from the primary tumor. | evaluate distant metastasis
clinical stage | Stage based on clinical evaluation before definitive pathological staging when applicable. | record the clinical stage
pathological stage | Stage incorporating surgical and pathological findings where applicable. | distinguish pathological stage
TNM classification | Cancer-specific classification describing tumor, regional nodes, and distant metastasis. | explain the TNM classification
stage group | Overall stage category combining applicable staging information. | confirm the stage group
staging investigation | Test used to help determine cancer extent. | arrange a staging investigation
imaging finding | Observation reported from a diagnostic image. | review an imaging finding
indeterminate finding | Finding whose nature or significance is not yet established. | explain an indeterminate finding
nodal involvement | Presence of cancer in lymph nodes. | assess nodal involvement
localized disease | Cancer confined to a defined local site in the relevant context. | describe localized disease
metastatic disease | Cancer that has spread to distant body sites. | discuss metastatic disease
prognostic factor | Feature associated with a disease's expected course or outcome. | interpret a prognostic factor
staging completion | Point at which the necessary staging information has been assembled. | confirm staging completion''',
    precision='Grade and stage are not synonyms. Staging systems differ by cancer type; do not assign a TNM category or stage from a vocabulary definition.',
    precision_extra='An indeterminate imaging finding is not automatically metastatic disease. Preserve the report\'s uncertainty and the need for clinical interpretation.',
    phrases='''Introduce the contrast | These two terms answer different questions.
Explain grade | Grade describes microscopic features of the tumor.
Explain stage | Stage describes the extent using the system for this cancer.
Name the missing evidence | The required imaging is still pending.
Avoid a shortcut | We cannot convert the grade into a stage.
Preserve uncertainty | Indeterminate does not mean confirmed spread.
Limit prognosis | A stage label is not an exact prediction for one person.
Check the contrast | Which term describes extent, and which describes the tissue features?''',
    notes='''Describes versus predicts | A classification describes evidence; it does not predict an individual's exact outcome.
Still pending | States that an investigation is unfinished rather than negative.
Not automatically | Blocks an invalid inference while leaving room for appropriate assessment.''',
    d='''Which contrast is correct? | Grade concerns microscopic features; stage concerns extent. | Grade and stage are interchangeable. | Stage always means cure. | Grade alone proves distant spread. | The two classifications address different properties and cannot replace each other.
What does pending imaging mean? | The required result is not yet available. | Spread has been excluded. | Spread has been confirmed. | Imaging has been canceled permanently. | Pending describes availability and does not establish the result's clinical meaning.
Which wording preserves an indeterminate finding? | Its significance is not yet established. | It is definitely metastatic. | It is definitely harmless. | It must be deleted. | Indeterminate means uncertainty remains and should not be converted into certainty.
Which claim is unsupported? | The grade supplies Theo's exact survival time. | The report contains grade. | Staging remains incomplete. | The terms need explaining. | Neither the grade nor the supplied facts establish an individual survival prediction.''',
    dialogue='''Theo | My report gives a grade. I thought that meant you already knew the stage of the cancer.
Dr Malik | [[Tumor grade::Tumor grade describes microscopic features under the relevant system and is distinct from the cancer's extent.]] describes microscopic features. Stage answers a different question about the extent of disease.
Theo | Then I may have combined two separate pieces of information when I explained the report at home.
Dr Malik | That is understandable. The [[cancer stage::Cancer stage describes extent under the applicable system and remains incomplete while necessary evidence is pending.]] is not complete while we are waiting for the required imaging.
Theo | I also saw a word about how much the cells resemble ordinary tissue. Where does that fit?
Dr Malik | [[Differentiation::Differentiation concerns how closely tumor cells resemble normal cells and can contribute to grading in the relevant system.]] concerns that resemblance. It can inform grading, but it does not by itself tell us where disease is present.
Theo | What does the staging investigation need to establish beyond what the microscope has shown?
Dr Malik | Depending on the cancer, it examines features such as [[local extent::Local extent describes disease in the original area and is one component rather than the entirety of staging.]], nearby nodes, and possible disease elsewhere.
Theo | So a nearby lymph node and a finding in a distant organ would not be described identically?
Dr Malik | Correct. A [[regional lymph node::A regional lymph node belongs to the relevant nearby drainage region and differs from a distant disease site.]] and a distant site have different roles in the applicable staging system.
Theo | I have heard people use the word metastatic for any unusual spot. Is that too definite?
Dr Malik | Yes. An [[indeterminate finding::An indeterminate finding has unresolved nature or significance and is not the same as confirmed cancer spread.]] has not yet been characterized. We must not relabel uncertainty as confirmed spread.
Theo | That distinction helps. I would rather the report's uncertainty stay visible than be translated into the worst possibility.
Dr Malik | Exactly. [[Distant metastasis::Distant metastasis means established cancer spread to a distant site, which an uncertain spot does not prove.]] is a specific conclusion, not a synonym for every finding that needs further review.
Theo | Will every cancer use the same letters and numbers once those investigations are complete?
Dr Malik | No. [[TNM classification::TNM classifies tumor, regional nodes, and metastasis in cancer-specific ways and is not a universal staging shortcut.]] applies in cancer-specific ways, and some cancers use other systems.
Theo | And even when the stage is known, it will not tell you exactly what happens to me personally?
Dr Malik | Correct. A [[prognostic factor::A prognostic factor is associated with the expected course but does not determine one person's exact future.]] informs a discussion; it is not an exact individual timetable.
Theo | Then I can say the grade is reported, but the stage still needs the remaining investigation results.
Dr Malik | Yes. We will confirm [[staging completion::Staging completion means the necessary information has been assembled and interpreted rather than assumed from grade alone.]] and explain the conclusion when the evidence is available.''',
    rehearsal=['Read the corrected terminology discussion. Contrast grade, stage, and an indeterminate finding.', 'Swap roles. Repeat the final summary without supplying a stage or prognosis that the case does not contain.'],
    transfer_title='Keep an uncertain scan finding uncertain', transfer_setup='A report calls a lung finding indeterminate. The oncology team is reviewing it. No metastatic diagnosis or stage change has been established.',
    transfer='''Patient: "The report calls the finding ___." | indeterminate | The supplied report explicitly preserves uncertainty about the finding's nature.
Clinician: "The team is still ___ it." | reviewing | Review is the current action, not a completed metastatic diagnosis.
Patient: "Spread has not been ___." | established | The case provides no conclusion that the finding represents cancer spread.
Clinician: "No stage change is ___." | confirmed | A stage change cannot be inferred from the uncertain finding alone.'''))

BOOK['units'].append(unit(
    title='Discussing biomarker results', scene='A possible match is not a promise',
    skill='Explain the difference between a molecular finding, a relevant option, and treatment eligibility.',
    brief='A tumor biomarker report identifies a potentially relevant molecular alteration for Quinn. Dr Sato has not established that a particular treatment is appropriate or available. Clinical context, the strength of evidence, and access need review. The report is tumor testing; no inherited finding has been established. Quinn hopes the result guarantees an effective targeted treatment.',
    cast='Dr Sato | Oncologist\nQuinn | Patient',
    culture=('Hope does not require a guarantee', 'Acknowledge why a possible treatment match matters. Explain the remaining checks without presenting them as bureaucratic obstacles or erasing the potential relevance.'),
    a='''What does the report identify? | A potentially relevant tumor alteration | Guaranteed treatment benefit | Confirmed inherited risk | An approved appointment date | The molecular finding may be relevant, but further interpretation is still required.
What is not established? | Suitability or availability of a particular treatment | That a report exists | That Quinn has questions | That clinical review is needed | The case leaves appropriateness and access unresolved rather than promising a treatment.
What kind of testing is described? | Tumor testing | Confirmed germline testing | Testing every relative | A completed trial enrollment | The report concerns the tumor and does not establish an inherited finding.''',
    vocabulary='''biomarker | Measurable feature providing information about a biological process or disease. | interpret a tumor biomarker
molecular alteration | Change in a molecular feature such as DNA sequence or gene activity. | characterize a molecular alteration
targeted therapy | Treatment directed at a relevant molecular target involved in disease. | evaluate a targeted therapy
somatic variant | Genetic change acquired in body cells rather than inherited through germ cells. | explain a somatic variant
germline variant | Genetic change in the inherited genetic material that may be passed to offspring. | assess a germline variant
variant of uncertain significance | Genetic change whose clinical meaning is not established. | report a variant of uncertain significance
actionability | Degree to which a finding can usefully inform a clinical action. | assess clinical actionability
evidence level | Strength or category of support for a clinical claim or action. | review the evidence level
companion diagnostic | Test providing information essential for appropriate use of a corresponding treatment. | verify a companion diagnostic
tumor profiling | Characterization of molecular features of a tumor. | review tumor profiling
sequencing panel | Test examining a selected set of genetic targets. | interpret a sequencing panel
specimen adequacy | Whether a sample meets the requirements for a reliable analysis. | confirm specimen adequacy
tumor heterogeneity | Differences among cells or regions within or between tumors. | discuss tumor heterogeneity
acquired resistance | Reduced treatment sensitivity developing during or after exposure. | investigate acquired resistance
predictive biomarker | Feature associated with likelihood of response to a particular treatment. | interpret a predictive biomarker
genetic counseling | Professional support in understanding genetic findings and their implications. | arrange genetic counseling
testing limitation | Restriction on what a test can detect or establish. | explain a testing limitation
treatment access | Practical ability to obtain an appropriate treatment. | clarify treatment access''',
    precision='A molecular alteration does not guarantee a useful treatment match or response. A tumor finding is not automatically an inherited finding.',
    precision_extra='Uncertain significance means the clinical meaning remains unresolved. Do not call a variant actionable solely because it appears in a detailed report.',
    phrases='''Acknowledge hope | I understand why a possible match feels important.
State the finding | The report identifies a tumor alteration that may be relevant.
Separate two steps | Finding a target and choosing a treatment are different steps.
Limit a promise | This does not guarantee that a treatment will work.
Explain review | We need to assess the evidence and your clinical circumstances.
Separate inheritance | Tumor testing does not automatically establish an inherited change.
Name access | We also need to establish whether an appropriate option is available.
Protect uncertainty | Uncertain significance is not the same as proven actionability.''',
    notes='''Potentially relevant | States possible significance without claiming a confirmed treatment indication.
Does not automatically | Prevents a tumor result from being treated as proof of inherited risk.
Need to establish | Marks a necessary unresolved check rather than a promised outcome.''',
    d='''Which statement preserves the result accurately? | The alteration may be relevant; suitability still needs review. | A targeted treatment is guaranteed to work. | Every reported variant is actionable. | Testing proves every relative is affected. | May be relevant preserves the finding without treating unresolved suitability as an established treatment choice.
Which distinction matters for relatives? | Tumor findings are not automatically inherited findings. | Every somatic variant is inherited. | All tumor tests test the entire family. | Germline and somatic mean identical things. | The type of testing and further assessment determine whether inherited implications are established.
What does uncertain significance mean? | Clinical meaning is not established. | A treatment must be started immediately. | The report is always wrong. | The condition is certainly inherited. | The phrase preserves uncertainty rather than supporting a specific action by itself.
Which additional issue belongs in the discussion? | Evidence, clinical context, and treatment access | Only the color of the report | A guaranteed response date | Automatic trial enrollment | Those unresolved factors affect whether a possible match becomes a useful clinical option.''',
    dialogue='''Dr Sato | The tumor report is available. What have you understood from it so far, and what would you like clarified?
Quinn | It lists a [[molecular alteration::A molecular alteration is a change in a molecular feature and does not alone establish an effective treatment.]]. I hoped that meant there was a medicine certain to work.
Dr Sato | I understand that hope. The finding may be relevant, but it is the start of another clinical discussion.
Quinn | Is this the difference between a finding and its [[actionability::Actionability concerns whether a finding can usefully inform a clinical action in the actual context.]], rather than just a complicated way to say the same thing?
Dr Sato | Yes. We need to review the supporting evidence and whether the finding fits an appropriate option for you.
Quinn | I would like you to explain the [[evidence level::Evidence level describes the strength of support for a proposed clinical use, which can vary between findings.]]. A long report can look more certain than the information really is.
Dr Sato | That is a fair request. A possible target does not guarantee a response to the associated treatment.
Quinn | Then [[targeted therapy::Targeted therapy acts on a relevant molecular target but is not a guarantee of effectiveness for every patient.]] describes how an option works, not a promise of benefit for me.
Dr Sato | Correct. The clinical setting and other factors matter, and we also need to establish availability.
Quinn | Please include [[treatment access::Treatment access concerns whether an appropriate option can actually be obtained, separate from a report's potential match.]] in that discussion. I cannot assume something listed in a report is obtainable here.
Dr Sato | We will. You also asked whether this result means your children have the same genetic change.
Quinn | Yes. I was unsure whether a [[somatic variant::A somatic variant is acquired in body cells and is distinct from a change established as inherited.]] was the same as something inherited through the family.
Dr Sato | It is not the same category. This is tumor testing; it does not automatically establish an inherited finding.
Quinn | So a [[germline variant::A germline variant concerns inherited genetic material, which has not been established by this tumor report alone.]] would require the appropriate separate interpretation and, where indicated, further assessment.
Dr Sato | Exactly. We can discuss a genetics referral if appropriate, without declaring an inherited result that we do not have.
Quinn | I also noticed a different entry marked [[variant of uncertain significance::A variant of uncertain significance has an unresolved clinical meaning and should not be presented as a proven treatment target.]]. I should not treat that as another proven treatment target.
Dr Sato | Correct. We will explain the limits of the test as well as the findings it reports.
Quinn | A [[testing limitation::A testing limitation restricts what the analysis can detect or establish and belongs in a balanced interpretation.]] is important to me because I do not want a negative entry interpreted as an answer to every question.
Dr Sato | We will review those limits, the possible options, and the next steps together before making recommendations.
Quinn | And [[genetic counseling::Genetic counseling provides qualified support for understanding genetic findings and implications without assuming inherited risk has already been proved.]] can help if the inherited-risk question needs specialist discussion, rather than me guessing from the report.''',
    rehearsal=['Read the corrected biomarker discussion. Contrast a finding, a possible option, and a guaranteed response.', 'Swap roles. Repeat the somatic and germline distinction without declaring an inherited result.'],
    transfer_title='A result with insufficient sample', transfer_setup='A profiling report says the sample was insufficient for one analysis. The result for that target is unavailable, not negative. A clinician will discuss whether further testing is appropriate.',
    transfer='''Patient: "The sample was ___ for that analysis." | insufficient | The report describes a sample limitation, not an absent molecular target.
Clinician: "The target result is ___." | unavailable | The analysis did not produce an interpretable result for that target.
Patient: "That is not the same as a ___ result." | negative | Failure to obtain a result cannot be converted into a negative finding.
Clinician: "Further testing needs clinical ___." | review | The next testing decision requires assessment rather than automatic repetition.'''))

BOOK['units'].append(unit(
    title='Making treatment intent explicit', scene='What is this option trying to achieve?',
    skill='Explain treatment goals and tradeoffs without promising a response or presenting consent as a formality.',
    brief='Dr Bell discusses a proposed treatment option with Jordan. In this fictional case its stated aim is disease control, not a promised cure. The benefits, burdens, alternatives, and practical effects still need an individual discussion. Jordan prioritizes being able to care for a partner. No regimen, dose, response probability, or final decision is supplied.',
    cast='Jordan | Patient\nDr Bell | Oncologist',
    culture=('Ask what the goal means in daily life', 'A treatment goal has both a clinical meaning and a personal significance. A patient may value time at home, symptom relief, or a particular activity differently from the clinician\'s initial assumption.'),
    a='''What is the proposed aim? | Disease control | A guaranteed cure | A completed response | A fixed survival extension | The case names disease control and explicitly excludes a promised cure.
What matters particularly to Jordan? | Caring for a partner | A decision already made | A specific dose supplied here | Avoiding every future discussion | Jordan's caregiving role is the stated personal priority to explore.
What remains undecided? | The final treatment choice | Whether Jordan has a partner | Whether a discussion is taking place | Whether the option has an aim | The discussion is ongoing and no final treatment decision is supplied.''',
    vocabulary='''treatment intent | Goal a treatment is intended to pursue. | clarify treatment intent
curative intent | Treatment aim of eliminating the cancer. | explain curative intent
disease control | Limiting cancer growth or spread as a treatment goal. | discuss disease control
neoadjuvant treatment | Treatment given before the main local treatment in an applicable plan. | explain neoadjuvant treatment
adjuvant treatment | Additional treatment after a primary treatment to reduce recurrence risk when appropriate. | discuss adjuvant treatment
systemic therapy | Treatment acting throughout the body rather than only at one local site. | explain systemic therapy
local treatment | Treatment directed at a particular body area. | discuss local treatment
treatment regimen | Planned combination and schedule of treatment components. | review the treatment regimen
treatment cycle | Repeated unit of a planned treatment schedule. | explain a treatment cycle
performance status | Clinical description of a person's activity and functional ability. | assess performance status
quality of life | Person's experienced well-being across relevant areas of life. | discuss quality of life
treatment burden | Physical, practical, and emotional demands associated with treatment. | assess treatment burden
benefit-risk balance | Weighing expected benefits against possible harms. | explain the benefit-risk balance
alternative option | Another reasonable approach available for discussion. | compare alternative options
supportive treatment | Intervention addressing symptoms or treatment-related difficulties. | coordinate supportive treatment
informed consent | Voluntary agreement after an appropriate explanation and opportunity for questions. | support informed consent
decision capacity | Ability to make the relevant decision under the applicable assessment. | assess decision capacity
caregiving responsibility | Duties involved in helping another person with care. | discuss caregiving responsibilities''',
    precision='Curative intent states an aim, not a guarantee. Disease control and symptom relief are also meaningful but different goals.',
    precision_extra='A signature does not replace a discussion of the proposed intervention, alternatives, benefits, risks, and the person\'s questions. This exercise supplies no treatment selection rule.',
    phrases='''State the aim | The aim of this option is to control the disease.
Avoid a guarantee | An intended benefit is not a promised outcome.
Ask about daily life | How would the treatment demands affect caring for your partner?
Explain the burden | We should discuss visits, symptoms, and practical demands together.
Invite alternatives | Let us compare the reasonable alternatives for your circumstances.
Keep choice open | You have not made a final decision in this discussion.
Check the goal | What do you understand this option is trying to achieve?
Respect questions | Questions are part of the consent discussion, not an obstacle to it.''',
    notes='''The aim is | States intended purpose without claiming an achieved result.
Would affect | Explores a possible practical consequence before a final decision.
Not a guarantee | Prevents treatment-intent language from becoming a promised outcome.''',
    d='''Which statement accurately names the goal? | This option aims at disease control. | This option guarantees cure. | A response has already occurred. | The outcome is certain. | Disease control is the stated aim; no response or cure is promised.
Which question elicits a relevant priority? | How would the treatment demands affect caring for your partner? | Why does your partner matter? | Can we ignore your home responsibilities? | You agree that practical issues are irrelevant? | Asking about the effect on caregiving links treatment demands with Jordan's stated priority.
Which account of consent is incomplete? | A signature alone proves understanding. | Questions need attention. | Alternatives need discussion. | The decision must be voluntary. | Signing a form cannot replace adequate explanation and attention to understanding and choice.
Which distinction is correct? | Curative intent is an aim, not a guarantee. | Disease control means certain cure. | Treatment burden means only cost. | Quality of life means only a scan result. | Intent describes the goal pursued and does not establish that it will be achieved.''',
    dialogue='''Jordan | Before we go through appointments, I need to understand what you hope this treatment will do.
Dr Bell | The [[treatment intent::Treatment intent identifies the goal pursued by an option rather than an outcome that has already occurred.]] here is disease control. I am not describing it as a guaranteed cure.
Jordan | That is clearer than saying it will help. Does control mean stopping everything permanently?
Dr Bell | [[Disease control::Disease control means limiting growth or spread and does not mean a guaranteed permanent elimination of cancer.]] means trying to limit growth or spread; the possible benefit and uncertainty need an individual discussion.
Jordan | I care for my partner. Repeated hospital visits could affect both of us, not only me.
Dr Bell | Your [[caregiving responsibility::Caregiving responsibility is a real practical priority that should inform the discussion of treatment demands.]] belongs in this conversation. Let us examine those demands alongside the clinical aims.
Jordan | I do not want practical difficulties to sound as though I am refusing treatment without listening.
Dr Bell | They do not. [[Treatment burden::Treatment burden includes physical, practical, and emotional demands and is relevant to an informed treatment choice.]] includes visits and disruption as well as physical effects.
Jordan | Could you explain the proposed schedule, then distinguish what is definite from what may change?
Dr Bell | We would review the [[treatment regimen::A treatment regimen is the planned combination and schedule, which must be explained for the actual option rather than invented here.]] and the circumstances in which it might need review.
Jordan | I have heard cycle used as though everyone knows what it means. Please explain that too.
Dr Bell | A [[treatment cycle::A treatment cycle is a repeating unit of a planned schedule, not a guarantee of response or a universal length.]] is a repeated unit of the schedule. Its details depend on the actual plan.
Jordan | I would also like to understand the other reasonable options, not just the one named first.
Dr Bell | We should compare each [[alternative option::An alternative option is another reasonable approach that belongs in the individualized discussion before a voluntary decision.]], including the expected benefits, limitations, and demands relevant to you.
Jordan | Being able to function at home matters to me. A scan is not the only thing I will judge by.
Dr Bell | Your [[quality of life::Quality of life concerns experienced well-being and functioning, not merely a radiological measure.]] is important. We need to understand the outcomes that matter to you.
Jordan | I am not ready to sign anything just because an appointment slot might be available.
Dr Bell | [[Informed consent::Informed consent requires a voluntary decision after appropriate explanation and questions, not merely a convenient appointment or signature.]] is a discussion and a voluntary decision, not simply obtaining a signature.
Jordan | Then let us compare the possible benefit with the burdens before calling this a settled plan.
Dr Bell | Yes. We will review the [[benefit-risk balance::The benefit-risk balance weighs potential benefit against possible harm without treating either as certain.]] and your priorities; no final choice has been made in this conversation.''',
    rehearsal=['Read the corrected options conversation. Contrast intended benefit with promised outcome.', 'Swap roles. Repeat the caregiving-priority question and the consent explanation without choosing a treatment for Jordan.'],
    transfer_title='A goal before a schedule', transfer_setup='Reese asks about a proposed option whose stated aim is symptom relief. The schedule has not been agreed. Reese wants its practical demands explained before deciding.',
    transfer='''Clinician: "The stated aim is symptom ___." | relief | Symptom relief is the goal supplied for this fictional option.
Reese: "The schedule is not yet ___." | agreed | The case explicitly leaves the treatment schedule unsettled.
Clinician: "We need to explain the practical ___." | demands | Reese requests information about the option's practical effect before deciding.
Reese: "My decision remains ___." | open | No final choice is supplied in this ongoing discussion.'''))

BOOK['units'].append(unit(
    title='Escalating a treatment-related symptom report', scene='The call cannot become a routine message',
    skill='Give a concise urgent handoff that distinguishes a reported symptom from an established treatment complication.',
    brief='Oncology nurse Ana calls Dr Ford about Lee, who reports fever and shaking after recent systemic treatment. The urgent oncology assessment pathway has already been activated according to the service protocol. The cause and laboratory results are unknown. The clinicians must exchange the relevant history and confirm responsibility; this case provides no triage threshold, diagnosis, or dosing instruction.',
    cast='Ana | Oncology nurse\nDr Ford | Oncologist',
    culture=('Urgency and uncertainty can coexist', 'A clinician can request urgent assessment without claiming a confirmed cause. Lead with the concern and action already taken, then identify the information still needed.'),
    a='''What is reported? | Fever and shaking after recent treatment | A confirmed laboratory diagnosis | A completed response assessment | No symptoms | Lee reports symptoms; the cause has not been established.
What action is already taken? | The urgent assessment pathway is activated | A routine message is awaiting next week | A dose has been selected here | All results are normal | The brief says the service's urgent pathway has already been activated.
What remains unknown? | Cause and laboratory results | Who called Dr Ford | Whether symptoms were reported | Whether treatment was recent | The handoff must preserve these unknowns rather than manufacture findings.''',
    vocabulary='''treatment-related toxicity | Harmful effect attributed to treatment after appropriate assessment. | assess suspected treatment-related toxicity
febrile episode | Period during which fever occurs. | report a febrile episode
neutropenia | Abnormally low neutrophil count. | assess for neutropenia
neutrophil count | Measurement of the number of neutrophils in blood. | review the neutrophil count
immunosuppression | Reduced activity or effectiveness of immune defenses. | consider immunosuppression
infection concern | Suspicion that infection may be relevant to a clinical presentation. | escalate an infection concern
infusion reaction | Adverse response occurring in association with an infusion. | report a suspected infusion reaction
extravasation | Escape of an infused substance from a vessel into surrounding tissue. | escalate suspected extravasation
mucositis | Inflammation affecting mucous membranes. | describe mucositis symptoms
dehydration | Deficit of body water requiring clinical assessment in context. | assess suspected dehydration
adverse event | Unfavorable occurrence during care, not necessarily caused by treatment. | report an adverse event
causality assessment | Evaluation of whether one event caused another. | preserve uncertainty in causality assessment
symptom onset time | Time when the reported symptom began. | confirm symptom onset time
last treatment date | Most recent date on which treatment was administered. | verify the last treatment date
urgent assessment | Prompt clinical evaluation through the appropriate service pathway. | arrange urgent assessment
receiving clinician | Professional taking responsibility for the next clinical assessment. | identify the receiving clinician
read-back | Repetition of important information to verify its accuracy. | use read-back for key details
escalation acknowledgment | Confirmation that an urgent request has been received and accepted. | obtain escalation acknowledgment''',
    precision='Fever after treatment raises a concern requiring the actual clinical pathway; it does not establish neutropenia, infection, or treatment causality by itself.',
    precision_extra='Do not delay an urgent response to finish a language exercise or obtain a perfect history. This scenario begins after the real service pathway has been activated.',
    phrases='''Lead with urgency | I am calling about an urgent symptom report after recent treatment.
State the action | The urgent assessment pathway is already activated.
Attribute the report | Lee reports fever and shaking.
Preserve an unknown | We do not yet have the laboratory results.
Avoid premature diagnosis | I am reporting the concern, not a confirmed cause.
Confirm responsibility | Who is accepting the next assessment?
Read back | I will repeat the key details to check accuracy.
Separate processes | This must not be left as a routine administrative message.''',
    notes='''Reports versus has confirmed | Separates the patient's symptom account from an established clinical diagnosis.
Already activated | Marks an action completed before this handoff begins.
Accepting | Makes the transfer of responsibility explicit rather than implying that a message sent itself completes a handoff.''',
    d='''Which opening best supports the handoff? | Urgent symptom report after recent treatment; the pathway is activated. | There is a small administrative question for next week. | All causes are already established. | Lee must be fine because the call is clear. | Naming the urgent report and activated pathway communicates the concern and action without inventing a diagnosis.
Which diagnosis cannot be asserted from this brief? | Confirmed neutropenia | Reported fever | Reported shaking | Recent treatment | A low neutrophil count has not been established because laboratory results are unknown.
What must the handoff confirm? | The receiving clinician and responsibility | Only that an email was sent | An invented medicine dose | A guaranteed cause | A handoff requires an accepted next step rather than relying on a message's existence.
Which statement preserves causality correctly? | Symptoms occurred after treatment; the cause is not established. | Treatment definitely caused every symptom. | Timing proves infection. | No assessment is needed until causality is certain. | Temporal sequence does not prove causality and does not remove the need for urgent assessment.''',
    dialogue='''Ana | I am calling about Lee, who reports fever and shaking after recent systemic treatment. The urgent pathway is activated.
Dr Ford | Thank you. Keep this with [[urgent assessment::Urgent assessment is the activated clinical pathway in this case, not a routine message to be reviewed later.]], not a routine message. Tell me the verified details and what remains unknown.
Ana | The symptoms are patient-reported. I am confirming their timing, and we do not yet have laboratory results.
Dr Ford | Please preserve the [[symptom onset time::Symptom onset time identifies when the symptoms began and must be confirmed rather than guessed during the handoff.]] as reported, including any uncertainty in the account.
Ana | I will also verify the most recent treatment information from the actual record rather than rely on memory.
Dr Ford | Yes. The [[last treatment date::The last treatment date provides relevant clinical context and should be verified from the appropriate source.]] matters, but do not delay the active response while completing every detail.
Ana | Shall I describe this as confirmed treatment toxicity in the handoff heading, or keep the cause open?
Dr Ford | Keep the [[causality assessment::Causality assessment determines whether treatment caused an event; that conclusion is not supplied by timing alone.]] open. The symptoms followed treatment, but we have not established their cause.
Ana | I have not labeled Lee neutropenic. There is no count available to support that description yet.
Dr Ford | Correct. A [[neutrophil count::A neutrophil count is a laboratory measurement that has not yet been supplied in this scenario.]] is not available; do not fill that gap with an assumed result.
Ana | The clinical concern remains urgent even while we avoid assigning a diagnosis that has not been established.
Dr Ford | Exactly. We can escalate an [[infection concern::An infection concern is a clinical suspicion requiring assessment, not a confirmed infection diagnosis.]] without declaring that infection is confirmed.
Ana | I need a clear receiving contact so that the report does not move between teams without an owner.
Dr Ford | The [[receiving clinician::The receiving clinician is the professional accepting the next clinical assessment and responsibility in the handoff.]] must be identified through our pathway. I am accepting this clinical discussion now.
Ana | I will repeat the patient's reported symptoms and the actions already taken, then confirm the next communication.
Dr Ford | Use [[read-back::Read-back repeats important details to confirm accuracy rather than assuming the message was understood correctly.]] for the important details and correct anything that differs from the record.
Ana | I will document that the concern was received and who accepted it, not simply that a call was attempted.
Dr Ford | That [[escalation acknowledgment::Escalation acknowledgment records that the urgent request was received and accepted, beyond merely attempting contact.]] makes the handoff clear. Keep any new information with the active clinical team.
Ana | Understood. The urgent pathway remains active, the cause is unresolved, and we are not inventing missing results.
Dr Ford | Correct. Record the [[adverse event::An adverse event is an unfavorable occurrence during care and does not by itself prove treatment causation.]] factually and follow the actual clinical and reporting procedures.''',
    rehearsal=['Read the corrected urgent handoff. Lead with the concern and the pathway already activated.', 'Swap roles. Repeat the unknown-results statement and the acknowledgment without inventing a diagnosis or a dose.'],
    transfer_title='Confirm a received escalation', transfer_setup='The urgent pathway is active for a new symptom report. Dr Lane accepts the handoff. Laboratory results remain pending; the cause is not established.',
    transfer='''Nurse: "The urgent pathway is ___." | active | The scenario begins with the actual urgent response already in progress.
Dr Lane: "I ___ the handoff." | accept | Dr Lane explicitly accepts responsibility for receiving the clinical handoff.
Nurse: "The laboratory results remain ___." | pending | The results have not yet become available in the supplied facts.
Dr Lane: "The cause is not ___." | established | Neither the symptom report nor the handoff establishes a cause by itself.'''))

BOOK['units'].append(unit(
    title='Discussing a response-assessment scan', scene='Smaller is useful, but not the whole conclusion',
    skill='Explain a scan comparison while distinguishing measurement, interpretation, and an agreed treatment decision.',
    brief='Pat\'s report describes a measured lesion as smaller than on the comparison scan. The complete response assessment is still under oncology review, and no formal response category or treatment change has been agreed. Dr Ng must acknowledge the encouraging observation without declaring cure, complete response, or a settled next regimen.',
    cast='Pat | Patient\nDr Ng | Oncologist',
    culture=('Share the useful finding without expanding its meaning', 'Patients deserve to hear favorable observations clearly. Precision does not require withholding them; it requires separating the observation from conclusions still under review.'),
    a='''What does the report describe? | A measured lesion is smaller | Every lesion has disappeared | A confirmed cure | A new regimen already started | Only the specific size comparison is supplied, not a complete response conclusion.
What is still under review? | The complete response assessment | Whether Pat has a report | Whether a comparison scan exists | Whether a clinician is involved | The complete assessment has not yet been finalized by oncology.
What has not been agreed? | A treatment change | That the report is available | That the lesion was measured | That Pat wants an explanation | The brief supplies no agreed change to the treatment plan.''',
    vocabulary='''response assessment | Evaluation of how disease has changed during or after treatment. | complete a response assessment
comparison scan | Earlier imaging study used as a reference. | review the comparison scan
measurable lesion | Abnormality that can be measured under the relevant assessment criteria. | identify a measurable lesion
target lesion | Selected lesion followed for measurement under a response-assessment system. | measure a target lesion
non-target lesion | Disease finding assessed outside the selected target-lesion measurements. | assess non-target lesions
partial response | Reduction meeting the relevant criteria without a complete response. | explain a partial response
complete response | Disappearance of detectable disease findings under the applicable response criteria. | qualify a complete response
stable disease | Disease not meeting the relevant response or progression thresholds. | discuss stable disease
progressive disease | Worsening that meets applicable progression criteria. | evaluate progressive disease
new lesion | Newly identified abnormality requiring interpretation in context. | investigate a new lesion
radiological response | Change in disease appearance assessed using imaging. | describe radiological response
clinical response | Change assessed through clinical symptoms, signs, or functioning. | compare clinical response
remission | Reduction or disappearance of signs of disease, described as partial or complete when appropriate. | explain remission
recurrence | Return of cancer after a period of improvement or remission. | discuss recurrence
measurement variability | Differences arising from how measurements are obtained or interpreted. | account for measurement variability
scan interval | Time between imaging examinations. | confirm the scan interval
restaging | Reassessment of disease extent after treatment or a change. | explain restaging
assessment criteria | Defined rules used to classify findings or changes. | apply the relevant assessment criteria''',
    precision='A smaller lesion is an observation, not automatically a formal partial response. Complete response and cure are not interchangeable claims.',
    precision_extra='Use the applicable cancer-specific assessment criteria and full clinical context. The exercise supplies no measurement thresholds and cannot classify a real scan.',
    phrases='''State the observation | This measured lesion is smaller than on the comparison scan.
Recognize its value | That is a useful finding to discuss.
Separate the review | The complete response assessment is still under review.
Avoid overstatement | Smaller does not by itself mean cured.
Include other evidence | The team will interpret the scan with the other relevant findings.
Keep status accurate | No treatment change has been agreed yet.
Explain a category | A response category uses defined criteria, not one adjective.
Check the summary | What would you tell someone about what is known and what is still pending?''',
    notes='''Smaller than | Makes a comparative observation and identifies the reference image.
By itself | Limits the conclusion supported by one finding.
Has been agreed | Distinguishes an agreed decision from a possible change under discussion.''',
    d='''Which update is supported? | One measured lesion is smaller; the full assessment remains under review. | Pat is cured. | Complete response is confirmed. | Every finding has resolved. | The supported statement keeps the favorable measurement separate from the unfinished overall interpretation.
Which claim confuses observation and classification? | Smaller automatically means formal partial response. | A comparison scan is used. | A lesion was measured. | The review is incomplete. | Formal response categories require their applicable criteria and the full relevant assessment.
Which treatment statement is accurate? | No change has been agreed. | A new regimen is already authorized. | Treatment has ended permanently. | The next dose is supplied here. | The case explicitly leaves any treatment change undecided.
Why avoid equating complete response with cure? | They describe different claims about disease and future outcome. | The words have identical meanings. | Cure is merely a measurement unit. | Complete response means no review is needed. | A response category does not automatically establish a permanent individual outcome.''',
    dialogue='''Pat | The report says the spot is smaller. I have been waiting to hear whether I can call that good news.
Dr Ng | The [[comparison scan::A comparison scan provides the earlier imaging reference for the reported change in the measured lesion.]] shows the reference point. This measured lesion is smaller, and that is useful information.
Pat | I would like to understand the finding without saying more than the report can actually support.
Dr Ng | That is sensible. The full [[response assessment::Response assessment considers the relevant evidence and criteria rather than assigning a category from one descriptive word.]] is still under review; one measurement is not the entire conclusion.
Pat | Does smaller automatically mean the treatment has produced what the team calls a partial response?
Dr Ng | A [[partial response::A partial response must meet the applicable assessment criteria and cannot be inferred from the word smaller alone.]] has defined criteria. I need the full assessment before using that label for your results.
Pat | I noticed the report described other findings as well. Are they part of the same review?
Dr Ng | Yes. A [[target lesion::A target lesion is selected for measurement under an assessment system and does not represent every relevant disease finding.]] is selected for measurement, but other findings can matter to the overall interpretation.
Pat | Then I should not assume that measuring one selected area means every other area has been ignored.
Dr Ng | Correct. [[Non-target lesions::Non-target lesions are relevant disease findings assessed outside the selected target measurements and may affect interpretation.]] and any new findings may need assessment under the appropriate system.
Pat | My symptoms have also changed. Should I describe those even if the scan appears encouraging?
Dr Ng | Absolutely. [[Clinical response::Clinical response concerns changes in symptoms, signs, or functioning and adds information distinct from imaging measurements.]] and imaging findings offer different information; we need the clinical context too.
Pat | I want to tell my family there is an encouraging change, but not that everything has disappeared.
Dr Ng | That is accurate. A [[complete response::Complete response refers to disappearance of detectable findings under applicable criteria and has not been established here.]] has not been established by the facts we are discussing.
Pat | And even that term would need explaining rather than being used as a simple synonym for cure?
Dr Ng | Yes. [[Remission::Remission describes reduction or disappearance of disease signs and should not be used as an automatic guarantee of permanent cure.]] and cure are not interchangeable promises about an individual's future.
Pat | Does the smaller measurement mean you have already decided to change the treatment schedule?
Dr Ng | No. We must finish the review using the relevant [[assessment criteria::Assessment criteria are the defined rules used to classify changes and support interpretation rather than an automatic schedule change.]] and clinical context before discussing any recommendation.
Pat | Then my summary is that one lesion is smaller, the full review is pending, and the plan has not changed yet.
Dr Ng | Exactly. We will explain the [[radiological response::Radiological response is change assessed on imaging and will be discussed with the full clinical picture when the review is complete.]] and its implications when the complete assessment is available.''',
    rehearsal=['Read the corrected scan discussion. Keep the encouraging observation separate from a formal response category.', 'Swap roles. Repeat Pat\'s final summary without declaring cure or changing treatment.'],
    transfer_title='A new finding awaiting interpretation', transfer_setup='A scan mentions a new finding. The oncology review is incomplete. No progression category or treatment change has been agreed.',
    transfer='''Patient: "The report describes a ___ finding." | new | New describes the observation supplied, not its established significance.
Clinician: "The review remains ___." | incomplete | The oncology interpretation has not yet been completed in this scenario.
Patient: "Progression is not yet ___." | classified | The case does not supply a formal progression category.
Clinician: "No treatment change is ___." | agreed | A new observation does not by itself establish an agreed treatment change.'''))

BOOK['units'].append(unit(
    title='Explaining a clinical trial invitation', scene='An option to discuss, not an obligation',
    skill='Explain research participation while separating eligibility, consent, and proven benefit.',
    brief='Dr Ortiz discusses a possible treatment trial with Val. Eligibility screening is not complete, and Val has not consented or enrolled. The trial compares approaches using random assignment. No investigational product, benefit probability, or payment terms are supplied. Val worries that declining would harm the relationship with the care team.',
    cast='Val | Patient\nDr Ortiz | Oncologist',
    culture=('Keep research and care roles clear', 'An invitation can feel like a recommendation the patient must obey. Explain the research purpose, uncertainty, and voluntary decision without presenting an experimental option as proven superior.'),
    a='''What is the participation status? | Eligibility review incomplete; no consent or enrollment | Already enrolled | Assigned to a study group | Benefit already demonstrated for Val | The scenario keeps eligibility, consent, and enrollment as unfinished and distinct stages.
How does the trial assign approaches? | Random assignment | Val choosing any group after enrollment | A guaranteed best-treatment allocation | A payment determining the group | The brief explicitly states random assignment without describing a guaranteed superior group.
What worries Val? | Declining might harm the care relationship | A dose already selected here | A result already received | A completed treatment switch | Val's concern is pressure on the relationship rather than a supplied clinical result.''',
    vocabulary='''clinical trial | Research study evaluating a health intervention in people. | discuss a clinical trial
eligibility criteria | Requirements determining whether a person may enter a study. | review eligibility criteria
screening visit | Assessment checking whether trial-entry requirements are met. | arrange a screening visit
enrollment | Formal entry into a study after required processes. | distinguish enrollment from screening
randomization | Assignment to study groups through a chance-based process. | explain randomization
study arm | Group receiving a specified intervention or approach in a trial. | describe a study arm
control group | Comparison group used to evaluate an intervention. | explain the control group
investigational treatment | Treatment being studied for the relevant use. | discuss an investigational treatment
standard of care | Accepted clinical approach for the relevant setting and circumstances. | compare with standard of care
research protocol | Approved plan specifying how a study is conducted. | explain the research protocol
primary endpoint | Main outcome used to evaluate the study question. | identify the primary endpoint
overall survival | Time from a defined starting point until death from any cause. | interpret overall survival
progression-free survival | Time from a defined point without disease progression or death under study definitions. | explain progression-free survival
voluntary participation | Taking part by choice without improper pressure. | protect voluntary participation
withdrawal | Ending participation through the applicable study process. | explain withdrawal options
consent discussion | Conversation supporting an informed decision about participation. | allow time for the consent discussion
research coordinator | Professional organizing study visits and participation processes. | contact the research coordinator
therapeutic misconception | Mistaken belief that research is designed solely to provide individualized treatment benefit. | address therapeutic misconception''',
    precision='Trial eligibility is not enrollment, and consent does not guarantee benefit. Randomization is not a clinician choosing the group believed best for one participant.',
    precision_extra='Explain withdrawal and remaining care using the actual protocol and applicable duties. Do not invent payment, access, or administrative guarantees.',
    phrases='''Introduce research | This is an option to discuss, not an obligation.
State uncertainty | The study is asking a question that is not already settled.
Explain assignment | Random assignment determines the study group.
Separate stages | Eligibility review is not the same as enrollment.
Protect the relationship | Declining research does not remove your right to appropriate care.
Invite review | Take the opportunity to ask about visits, risks, and alternatives.
Avoid a guarantee | An investigational treatment is not proven better simply because it is new.
Clarify withdrawal | We will explain the actual withdrawal process and remaining care arrangements.''',
    notes='''May be eligible | Describes a possibility before the entry criteria have been checked.
Investigational | Identifies a research status, not a promise of superior treatment.
Not an obligation | Removes an implied demand while leaving the option available for discussion.''',
    d='''Which statement separates the stages correctly? | Eligibility is under review; Val is not enrolled. | Discussing a trial automatically enrolls Val. | Screening proves benefit. | A consent form guarantees entry. | The case gives neither completed eligibility nor consent nor enrollment.
Which claim creates therapeutic misconception? | The research exists solely to give Val the best individual treatment. | The study has a research question. | Participation is voluntary. | Random assignment determines a group. | Research evaluates a question and cannot be presented as a guarantee of individualized benefit.
What does randomization mean? | Chance-based assignment under the study process | The doctor selecting a guaranteed best arm | The patient purchasing a preferred arm | A completed response assessment | Randomization assigns groups through chance rather than individualized selection of a supposedly superior group.
Which response to Val's concern is appropriate? | Declining research does not remove the right to appropriate care. | The team will stop listening if you decline. | You owe the study your participation. | Signing now is the only way to ask questions. | Voluntary participation requires avoiding coercion and clarifying continuing care.''',
    dialogue='''Val | You mentioned a trial. I worry that saying no would make you think I am not cooperating with care.
Dr Ortiz | This [[clinical trial::A clinical trial is research evaluating an intervention, and an invitation to discuss it is not an obligation to join.]] is an option to discuss. Declining research does not remove your right to appropriate care.
Val | Am I already accepted because you brought it up, or is there another process before that?
Dr Ortiz | We still need to review the [[eligibility criteria::Eligibility criteria are entry requirements that remain under review and do not establish enrollment by themselves.]]. Discussing the study does not establish that you can enter it.
Val | I would like to understand what the study is trying to find out before considering any forms.
Dr Ortiz | The [[research protocol::The research protocol sets out the study's purpose and procedures and should guide an accurate explanation of participation.]] describes its question, procedures, and participant requirements. We will review the relevant details with you.
Val | Would you choose whichever treatment group you think is best for me after I join?
Dr Ortiz | This study uses [[randomization::Randomization assigns study groups through a chance-based process rather than the clinician selecting an individually preferred arm.]]. Assignment follows a chance-based process rather than my choosing an arm for you.
Val | That matters to my decision. I do not want to assume that the new option is already known to be better.
Dr Ortiz | An [[investigational treatment::An investigational treatment is being studied for the relevant use and is not proven superior merely because it is new.]] is being studied; its possible advantages and disadvantages are not a promised result for you.
Val | Please compare participation with the ordinary care options I could discuss outside the study.
Dr Ortiz | We should explain the relevant [[standard of care::Standard of care describes accepted clinical approaches in context and belongs in the discussion of alternatives to research participation.]] and other reasonable alternatives, not present research as the only possible conversation.
Val | The visits and tests may affect my work. Can I ask about those before deciding whether to proceed?
Dr Ortiz | Certainly. The [[research coordinator::A research coordinator can clarify study arrangements and visits while clinical and consent questions remain with the appropriate professionals.]] can help explain practical arrangements, alongside our discussion of the clinical questions.
Val | If I first agree and later want to stop, I need to understand what happens to my care.
Dr Ortiz | We will explain [[withdrawal::Withdrawal is ending participation through the applicable process, with its details and continuing care discussed accurately.]] using the actual study process and clarify the remaining care arrangements.
Val | I would like time to read the information and return with questions rather than sign because I feel rushed.
Dr Ortiz | That is part of a proper [[consent discussion::A consent discussion supports understanding and a voluntary decision rather than treating a signature as the whole process.]]. Questions and time to understand are important to a voluntary decision.
Val | Then eligibility is still being checked, and I have not consented or joined by having this conversation.
Dr Ortiz | Correct. [[Enrollment::Enrollment is formal entry after the required study processes and has not occurred in this scenario.]] has not happened. We can continue discussing the option without treating today as a commitment.''',
    rehearsal=['Read the corrected research discussion. Contrast invitation, eligibility, consent, and enrollment.', 'Swap roles. Repeat the randomization explanation and the response to perceived pressure.'],
    transfer_title='A screening visit is not enrollment', transfer_setup='Jo has agreed to a trial-screening visit. Eligibility remains unknown. Jo has not enrolled and wants the withdrawal information explained before making a participation decision.',
    transfer='''Jo: "I agreed to a ___ visit." | screening | Jo agreed to an eligibility-related visit, not completed study enrollment.
Clinician: "Your eligibility remains ___." | unknown | The entry requirements have not yet been established as met.
Jo: "I have not ___ in the study." | enrolled | The case explicitly states that formal study entry has not occurred.
Clinician: "We will explain the ___ process." | withdrawal | Jo asks about ending participation before deciding whether to participate.'''))

BOOK['units'].append(unit(
    title='Discussing palliative care and priorities', scene='Support alongside treatment',
    skill='Explain a supportive-care referral and elicit goals without equating it with abandonment or an automatic change in treatment.',
    brief='Dr Ahmed offers Rowan a palliative-care consultation for symptoms and distress while an anticancer-treatment discussion continues. Rowan hears the referral as a decision to stop treatment. No decision to stop treatment, enter hospice, or set a resuscitation status is supplied. Rowan wants more comfortable time with family and clearer help with symptoms.',
    cast='Rowan | Patient\nDr Ahmed | Oncologist',
    culture=('Explore the meaning the patient heard', 'Terms associated with serious illness can carry meanings beyond their clinical definition. Ask what the referral sounded like before correcting the misunderstanding.'),
    a='''Why is the consultation offered? | Symptoms and distress | A supplied decision to stop all treatment | An automatic hospice admission | A completed resuscitation decision | The referral addresses symptoms and distress while the treatment discussion continues.
What does Rowan fear? | That treatment is being stopped | That the report contains a new grade | That a scan is already normal | That a trial has enrolled them | Rowan interprets palliative care as a decision to end anticancer treatment.
Which preference is stated? | More comfortable time with family | A particular resuscitation status | A guaranteed survival period | An instruction to refuse all services | Rowan names comfort and family time, not a completed decision about other care.''',
    vocabulary='''palliative care | Care addressing symptoms, distress, and quality of life in serious illness. | introduce palliative care
hospice care | Care focused on comfort near the end of life under applicable service criteria. | distinguish hospice care
symptom management | Assessment and treatment of distressing symptoms. | coordinate symptom management
goals-of-care discussion | Conversation about priorities and how care should respond to them. | open a goals-of-care discussion
serious-illness conversation | Discussion of understanding, concerns, values, and care in serious illness. | structure a serious-illness conversation
advance care planning | Process of discussing and recording preferences for future care. | offer advance care planning
advance directive | Document expressing future-care wishes or decision arrangements under applicable law. | review an advance directive
surrogate decision-maker | Person authorized to decide when the patient cannot under applicable rules. | clarify the surrogate decision-maker
resuscitation status | Documented decision or order about resuscitation in the relevant setting. | clarify resuscitation status
comfort-focused care | Care organized primarily around comfort and relief of distress. | explain comfort-focused care
concurrent care | Care approaches provided alongside one another. | discuss concurrent care
care preference | Person's expressed wishes about aspects of care. | elicit a care preference
family meeting | Planned discussion involving the patient and appropriate family or support people. | arrange a family meeting
caregiver strain | Physical or emotional burden experienced by someone providing care. | acknowledge caregiver strain
spiritual concern | Concern about meaning, belief, connection, or existential distress. | invite a spiritual concern
symptom burden | Combined effect of symptoms on the person's life. | assess symptom burden
interdisciplinary support | Help provided by professionals with complementary care roles. | coordinate interdisciplinary support
values clarification | Exploration of what matters to a person in a care decision. | support values clarification''',
    precision='Palliative care can accompany anticancer treatment. A referral does not automatically mean hospice enrollment, treatment cessation, or a resuscitation decision.',
    precision_extra='A family member\'s presence does not automatically establish decision-making authority. Discuss preferences and legal arrangements accurately for the setting.',
    phrases='''Ask what was heard | What did the phrase palliative care suggest to you?
Correct the inference | This referral is not a decision to stop treatment.
Explain the purpose | The team can help with symptoms and distress alongside other care.
Elicit a priority | What would make the coming weeks more manageable for you?
Separate decisions | Hospice and resuscitation decisions require their own discussions.
Invite support | We can discuss who you want involved in a family meeting.
Avoid abandonment | We will continue to address your care needs.
Make goals concrete | More comfortable time with family is a priority we should keep visible.''',
    notes='''Alongside | Describes concurrent care rather than replacement or abandonment.
Not a decision to | Corrects an inference about an action that has not been agreed.
What would make | Invites a concrete priority rather than assuming the clinician knows it already.''',
    d='''Which statement explains the referral correctly? | Palliative care can support symptoms alongside treatment. | The referral automatically stops anticancer treatment. | The referral determines resuscitation status. | The referral guarantees hospice admission. | Palliative support can accompany other treatment and does not settle separate care decisions.
Which question explores the misunderstanding? | What did the phrase suggest to you? | Why did you misunderstand an obvious term? | You agree it means giving up? | Can we avoid your concern? | Asking what the phrase suggested invites Rowan's interpretation without blame or a leading conclusion.
What priority should remain visible? | Comfortable time with family | A resuscitation choice invented here | A guaranteed prognosis | A decision attributed to an absent relative | Comfortable family time is Rowan's explicit priority in this fictional conversation.
Which assumption is unsafe? | Every relative present has automatic decision-making authority. | Preferences need discussion. | Symptoms need attention. | Different care decisions should be separated. | Presence or relationship alone does not establish authority under the relevant legal arrangements.''',
    dialogue='''Rowan | When you mentioned palliative care, I heard that you were giving up on the cancer treatment.
Dr Ahmed | What did [[palliative care::Palliative care addresses symptoms and quality of life in serious illness and can accompany anticancer treatment.]] suggest to you? I want to understand that concern before explaining the referral.
Rowan | I thought it meant every other treatment would stop, and that I would no longer see this team.
Dr Ahmed | This is an offer of [[concurrent care::Concurrent care means approaches can be provided alongside one another, rather than assuming one automatically replaces another.]]. It is not a decision to stop treatment or to stop addressing your care needs.
Rowan | Then please tell me what the additional team would actually help with in everyday life.
Dr Ahmed | They can help with [[symptom management::Symptom management addresses distressing symptoms and is one reason for this consultation while other treatment discussions continue.]], distress, and the effects of serious illness on you and those supporting you.
Rowan | I want more comfortable time with my family. At present the symptoms take over the entire day.
Dr Ahmed | That [[symptom burden::Symptom burden is the combined effect of symptoms on daily life and helps make Rowan's stated priority concrete.]] matters. We should keep comfortable family time visible when we discuss care options.
Rowan | Does agreeing to this consultation mean I have agreed to hospice without realizing it?
Dr Ahmed | No. [[Hospice care::Hospice care has a distinct comfort-focused purpose and applicable service criteria; it is not automatically established by this referral.]] is a separate discussion with its own circumstances and service criteria.
Rowan | I also do not want one referral to become a decision about resuscitation without anyone asking me.
Dr Ahmed | It does not establish your [[resuscitation status::Resuscitation status is a separate documented care decision and is not determined by accepting a palliative-care consultation.]]. Those decisions require their own appropriate discussion and documentation.
Rowan | My daughter helps a great deal, but I do not want everyone to assume she makes all decisions for me.
Dr Ahmed | We should clarify that. A [[surrogate decision-maker::A surrogate decision-maker acts under applicable authority when required, which is not established merely by being a helpful relative.]] has a specific role under the applicable arrangements, not simply because a relative attends.
Rowan | Could we have a conversation together where she can hear what I want without taking over the discussion?
Dr Ahmed | We can discuss a [[family meeting::A family meeting is a planned conversation with the appropriate people, guided by the patient's wishes and information-sharing arrangements.]] and who you want involved, keeping your priorities and permissions clear.
Rowan | I also want someone to notice how exhausted she is. She keeps saying she is fine.
Dr Ahmed | [[Caregiver strain::Caregiver strain describes the burden on someone providing care and can be addressed without replacing the patient's own voice.]] is worth discussing, with her involvement and the appropriate support.
Rowan | I understand better now. The referral adds symptom support; it does not silently settle every future decision.
Dr Ahmed | Exactly. A [[goals-of-care discussion::A goals-of-care discussion explores priorities and appropriate care rather than automatically ending treatment or assigning a resuscitation status.]] keeps those priorities explicit while we continue the other necessary clinical conversations.''',
    rehearsal=['Read the corrected supportive-care conversation. Stress alongside and separate discussion.', 'Swap roles. Repeat the response to Rowan\'s fear without promising an outcome or assigning a resuscitation status.'],
    transfer_title='Name a concrete care priority', transfer_setup='Taylor wants symptom support while treatment options are reviewed. Taylor would like friend Jo at a meeting but has not named Jo as a legally authorized decision-maker.',
    transfer='''Taylor: "I want help with my ___." | symptoms | Symptom support is the care need Taylor explicitly identifies.
Clinician: "Treatment options remain under ___." | review | The options are still being reviewed and no treatment decision is supplied.
Taylor: "I would like ___ at the meeting." | Jo | Jo is the friend Taylor wishes to include in the discussion.
Clinician: "Attendance does not establish decision-making ___." | authority | Being invited to a meeting does not automatically create legal decision-making authority.'''))
