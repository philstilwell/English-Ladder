"""Original biotechnology research and partnering communication cases."""
from books.authoring import unit

BOOK = dict(
    slug='biotechnology', title='Biotechnology English',
    cover_label='Platforms / assays / translation / partnering',
    cover_title='Biotechnology', cover_size=34,
    tagline='Explain the signal. Define the claim. Connect evidence to decisions.',
    audience='For biotechnology research, translational science, development, operations, and partnering teams.',
    map_intro='Eight conversations connecting laboratory evidence, development decisions, and collaboration terms.',
    notes_title='A promising signal needs a precise claim.',
    notes_intro='Biotechnology teams must explain specialized results to colleagues who make different kinds of decisions. A scientist asks whether the assay supports the mechanism; a development lead asks what remains untested; a partner asks what rights and evidence are actually available. The conversations here keep the scientific detail while making those decision boundaries explicit.',
    field_notes=[
        ('Name the experimental system', 'State which model, material, readout, and comparison support the finding. A result in one setting can justify further investigation without proving a platform works across every proposed use.', '"We observed the signal in one cell line; the broader application remains a hypothesis."'),
        ('Expand the word validated', 'Say what was evaluated, for which intended use, against which criteria, and with what remaining limits. Analytical performance and a useful clinical decision are different claims.', '"The assay measures the analyte in the assessed range; clinical prediction has not been established."'),
        ('Make the next decision visible', 'A list of completed experiments is not a decision-ready update. Connect each result to the milestone criterion, the unresolved question, and the proposed next allocation of time or resources.', '"The binding work is complete; the functional criterion remains open."'),
        ('Define rights before promising access', 'Materials, confidential information, patents, know-how, and resulting data are different things. Identify the proposed use and unresolved terms before assuming that one agreement grants every permission.', '"The confidentiality agreement does not settle the material-use or publication terms."')],
    scope_note='Original fictional language practice, not experimental instructions or medical, regulatory, legal, or investment advice. All organizations, candidates, numerical examples, and negotiations are invented. Apply current scientific standards, local procedures, appropriate professional review, and the actual governing agreements.',
    sources=[
        dict(title='Assay Guidance Manual. Basic Guidelines for Reporting Non-Clinical Data.', url='https://www.ncbi.nlm.nih.gov/sites/books/NBK550206/', note='Background on reporting experimental conditions, types of replicates, and variation. The datasets and research conversations are original.', checked='10 October 2026'),
        dict(title='FDA-NIH Biomarker Working Group. BEST Resource: Validation.', url='https://www.ncbi.nlm.nih.gov/books/NBK464453/', note='Background on distinguishing analytical performance from clinical validation for an intended use.', checked='10 October 2026'),
        dict(title='US Food and Drug Administration. ICH Q5E: Comparability.', url='https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q5e-comparability-biotechnologicalbiological-products-subject-changes-their-manufacturing-process', note='Background on quality-focused comparability after manufacturing changes. No example constitutes a regulatory determination.', checked='10 October 2026'),
        dict(title='World Intellectual Property Organization. Technology Transfer Agreements.', url='https://www.wipo.int/en/web/technology-transfer/agreements', note='Background on confidentiality, material transfer, licensing, and collaboration arrangements. Fictional terms are discussion examples, not model legal clauses.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Platform Technology and Scientific Thesis',
    scene='One cell line, three proposed diseases',
    skill='Distinguish a measured platform signal from a proposed mechanism and a broader development hypothesis.',
    brief='Research lead Nia reviews a fictional platform presentation with venture lead Leo. Three independent preparations of one cell line show an average reporter-signal reduction of 40% against the stated control. No orthogonal functional result or data from other disease systems are available. The slide claims proven activity across three diseases. The immediate request is funding for a bounded follow-up study, not approval for clinical use. Nia and Leo must retain the promising observation while correcting the unsupported breadth.',
    cast='Nia | Research lead\nLeo | Venture lead',
    culture=('Precision can strengthen a pitch', 'A confident scientific presentation distinguishes observation, interpretation, and the next test. Qualifying a claim does not require burying the result. Put the system and limitation beside the headline so a listener can understand both the promise and the reason for the next study.'),
    a='''Which evidence is supplied? | A 40% average reporter-signal reduction in three independent preparations of one cell line | Confirmed benefit in three diseases | A completed human efficacy study | Functional confirmation from an orthogonal assay | The brief supplies a reporter result in one cell line, not cross-disease or clinical evidence.
Which claim exceeds that evidence? | Proven activity across three diseases | A signal observed in the stated cell line | Three independent preparations tested | A follow-up study proposed | The additional disease systems have not been tested in the supplied case.
What is the immediate decision request? | Funding a bounded follow-up study | Authorizing clinical use | Declaring every platform application validated | Licensing all disease rights without review | The stated request concerns a limited next research study, not a clinical or rights decision.''',
    vocabulary='''platform technology | A reusable technological approach intended to support multiple applications. | develop a platform technology
scientific thesis | The evidence-based argument and hypotheses underlying a research program. | articulate the scientific thesis
modality | A type of therapeutic or technological approach. | compare therapeutic modalities
target | The biological entity a program aims to affect. | define the target
target engagement | Evidence that an intervention interacts with its intended biological target. | assess target engagement
mechanism of action | The biological process through which an intervention produces an effect. | investigate the mechanism of action
reporter signal | A measurable output used as an indicator in an experimental system. | quantify a reporter signal
cell line | A maintained population of cells used for research. | characterize the cell line
biological replicate | An independently prepared biological sample or experimental unit. | include biological replicates
technical replicate | A repeated measurement of the same biological material or preparation. | distinguish technical replicates
control condition | A comparison used to interpret an experimental result. | specify the control condition
orthogonal assay | A different measurement approach used to examine the same underlying question. | run an orthogonal assay
functional readout | A measurement of a relevant biological activity or outcome. | confirm a functional readout
assay interference | An effect on the measurement system that can distort the apparent result. | investigate assay interference
counter-screen | A separate screen used to identify unwanted or misleading effects. | include a counter-screen
selectivity | Preference for the intended target or effect relative to alternatives. | assess selectivity
off-target effect | An effect involving an unintended biological target or pathway. | evaluate off-target effects
proof of concept | Evidence supporting feasibility within a specified scope. | define the proof-of-concept scope
proof of mechanism | Evidence supporting the proposed causal biological mechanism. | seek proof of mechanism
generalizability | The extent to which a finding applies beyond the tested setting. | assess generalizability
disease model | An experimental system representing selected aspects of a disease. | qualify the disease model
translational hypothesis | A proposed link between experimental findings and a later development setting. | test a translational hypothesis
evidence gap | A missing piece of information relevant to a claim or decision. | identify an evidence gap
decision gate | A defined point at which evidence is reviewed against criteria. | set a decision gate''',
    precision='Three independent preparations provide information about variation within the tested biological system. They are not three diseases or three clinical trials. A reporter signal can support a research direction without establishing the full mechanism or proving human benefit.',
    precision_extra='An orthogonal assay uses a different measurement approach to examine the underlying question; a technical repeat of the same readout is not automatically orthogonal. Define the relevant follow-up and decision criteria without assuming its result in advance.',
    phrases='''Lead with the observation | We observed a 40% average reduction in the reporter signal.
Name the system | The data come from three independent preparations of one cell line.
Limit the breadth | Other disease systems have not yet been tested.
Separate signal from function | The reporter result does not yet establish the functional effect.
Keep the hypothesis | The broader platform application remains a testable hypothesis.
Request another method | We need a different readout to examine the underlying question.
Check interference | Could the signal reflect an effect on the assay rather than the intended biology?
Describe the control | The percentage is relative to the control specified in this experiment.
Avoid a mechanism claim | We have not established the full mechanism from this result alone.
State the opportunity | The signal is promising enough to justify a focused next study.
Identify the gap | The missing evidence is functional confirmation in a relevant additional system.
Define the decision | The next study should answer whether this application merits further development.
Keep replication precise | These are independent preparations, not repeated reads presented as independent samples.
Correct the slide | Replace proven across three diseases with the result actually measured.
Bound the ask | We are requesting the next research step, not clinical authorization.
Close with criteria | Agree what evidence would support or stop the next stage.''',
    notes='''Promising | Signals potential without claiming an established development outcome.
Proven | Requires the claim's scope to match the supporting evidence.
Platform | A reusable ambition does not itself demonstrate every application.
Replicate | Specify whether the repeat is technical, biological, or across runs.
Reduction | Name the readout and comparison; do not let a percentage imply patient benefit.
Orthogonal | Different measurement logic matters more than a new label on the same assay.''',
    d='''Which slide headline is best supported? | Reporter signal reduced by an average 40% in the tested cell line; broader applications remain untested. | Platform efficacy proven across three diseases. | Human benefit confirmed by three preparations. | All off-target effects excluded. | The supported headline retains the observed result and its actual experimental boundary.
One preparation is read three times with the same method. How should those reads be described? | Three technical measurements of one biological preparation | Three biological replicates from three separate preparations | Three orthogonal assays confirming the mechanism | Three disease models demonstrating broader applicability | Repeated reads of the same material are technical replication. They do not create independently prepared biological units, change the measurement approach, or establish new disease applications.
Why request an orthogonal functional readout? | To examine the biological question through a different measurement approach | To relabel the same reporter result as clinical evidence | To guarantee a favorable outcome | To avoid describing the original control | A different approach can test whether the original signal reflects the intended biology.
Which funding request matches the brief? | Support a bounded follow-up addressing functional confirmation and broader relevance. | Authorize clinical use because the signal is promising. | Assume all diseases will respond and skip further evidence. | Treat three preparations as completed trials in three indications. | The brief asks for a next research study that addresses the stated evidence gaps.''',
    dialogue='''Leo | The headline says our platform has proven activity across three diseases. It sounds strong, but I want to know whether each part of that claim is supported.
Nia | We have a [[reporter signal::The reporter signal is the measured experimental output, not a direct demonstration of clinical benefit.]] reduction averaging forty percent against the specified control. The work used three independent preparations of one cell line, not three disease systems.
Leo | Can we still call it a platform result? The investors need to see why this is more than a single isolated observation with no development direction.
Nia | Yes, as evidence relevant to the [[scientific thesis::The scientific thesis connects the observation to a research argument without treating every hypothesis as established.]]. We should explain the proposed applications while separating what we observed from what we expect to test next.
Leo | The slide currently turns the three preparations into a visual with three disease labels. I can see how that could imply that each disease has been tested.
Nia | Keep the [[biological replicate::A biological replicate is an independent preparation within the tested system, not a different disease application.]] description explicit. Three independent preparations tell us something about that system; they do not create evidence for three separate indications.
Leo | What would you say about the mechanism? The lower signal looks consistent with the proposed pathway, but the headline makes the connection sound settled.
Nia | We do not yet have [[proof of mechanism::Proof of mechanism requires evidence for the proposed biological explanation beyond the supplied reporter observation.]]. The reporter finding supports investigation, but an effect on the measurement system could also influence the apparent result.
Leo | What would the next study tell us that another reporter run would not? The funding request needs a scientific question, not just a larger sample count.
Nia | It should include an [[orthogonal assay::An orthogonal assay uses a different measurement approach to examine the underlying biological question.]] addressing the underlying biology. A different measurement approach would help distinguish a relevant biological effect from a feature of this reporter system.
Leo | We should be clear that you are asking to test that distinction, not promising that the second method will confirm the first. Otherwise the milestone is misleading.
Nia | Correct. We also need to assess [[assay interference::Assay interference can alter the measured signal without establishing the intended biological effect.]] and the appropriate controls. A promising decrease is not sufficient to dismiss competing explanations for the measured change.
Leo | How do we describe the proposed disease expansion without making it sound like a result? I want an ambitious but defensible sentence in the investor discussion.
Nia | Call it a [[translational hypothesis::A translational hypothesis proposes a link to another development setting that remains to be tested.]] and name the additional systems we propose to evaluate. The audience can understand the opportunity without being told that unperformed work has succeeded.
Leo | I will keep the forty-percent observation in the main line and put the tested system beside it. The expansion will be a proposed application, not a proven one.
Nia | That makes the [[evidence gap::The evidence gap is the missing functional and broader-system support needed for the larger claim.]] visible. We still lack functional confirmation and data in other disease systems, so those limits should travel with the headline.
Leo | For the decision itself, we want a bounded research budget, not a commitment to take every suggested indication into development. The proposal needs a stopping point.
Nia | Set a [[decision gate::A decision gate defines when the follow-up evidence will be reviewed against agreed continuation criteria.]] with agreed evidence criteria. We should know what question the work will answer and how that answer affects the next development choice.
Leo | I will remove the three-disease claim and request the bounded follow-up. Keep the forty-percent result beside the actual cell system so the claim cannot drift again.
Nia | Good. That preserves the platform ambition while keeping [[generalizability::Generalizability concerns application beyond the tested setting, which the supplied evidence has not yet established.]] open to investigation. We can be confident about the observation without claiming that every future application already works.''',
    transfer_title='One model is not every model',
    transfer_setup='A screening result is observed in one cell model. Two other proposed models have not been tested. The team requests a study of those additional systems.',
    transfer='''Scientist: "The signal was observed in one ___." | model | The supplied result belongs to one tested cell model only.
Partner: "The other two are still ___." | untested | The briefing states that no testing has occurred in those additional systems.
Scientist: "Broader application remains a ___." | hypothesis | The proposed extension is a testable idea rather than an established result.
Partner: "The next study should address that evidence ___." | gap | The missing data concern whether the finding extends beyond the tested setting.''',
    rehearsal=["Read the slide-review exchange. State 40% average reporter reduction, three independent preparations, and one cell line together.","Swap roles. Contrast a technical repeat with an orthogonal method; retain the untested broader applications.","Read the corrected one-model transfer. Keep two proposed models untested and the wider claim a hypothesis."]))

BOOK['units'].append(unit(
    title='Assay Development and Reproducibility',
    scene='Tight wells, shifting days',
    skill='Explain within-run precision separately from between-day variation and request a traceable investigation.',
    brief='Assay scientist Imani and project lead Chen review a fictional control sample measured over three days. Each day has a within-run coefficient of variation of 5%, but the day means are 80, 100, and 125 signal units. The same nominal control level was intended each day. The summary says fully reproducible. Reagent-lot, calibration, and operator records still need comparison. No acceptance limits or confirmed cause are supplied; the team must describe the variation without inventing a validation decision.',
    cast='Imani | Assay scientist\nChen | Project lead',
    culture=('Ask which kind of consistency', 'A colleague may use reproducible as a broad compliment while an assay specialist means a defined set of conditions. Clarify the tested source of variation rather than argue about the word alone. Numbers become useful when the comparison, units, and experimental structure are visible.'),
    a='''What is consistent within each run? | The stated coefficient of variation is 5%. | Every day mean is 100. | Every reagent lot has been verified identical. | A common acceptance limit has been met. | The briefing gives a five-percent within-run coefficient of variation on each day.
What changes across days? | The mean signal: 80, 100, and 125 units | The supplied acceptance limit | The number of confirmed disease indications | The definition of an independent clinical trial | The day means differ even though the within-run variation is stated as the same.
What cannot yet be concluded? | A confirmed cause or full validation status | That day three has a mean of 125 | That the within-run CV is supplied | That records need comparison | Neither a cause nor acceptance criteria sufficient for a validation decision are provided.''',
    vocabulary='''assay development | Designing and refining a measurement method for a specified purpose. | plan assay development
repeatability | Precision under closely matched conditions over a short interval. | assess repeatability
intermediate precision | Precision with relevant changes within one laboratory, such as day or operator. | evaluate intermediate precision
reproducibility | Precision under specified changed conditions, commonly across laboratories. | define reproducibility conditions
within-run variation | Differences among measurements within a single analytical run. | quantify within-run variation
between-day variation | Differences associated with measurements on different days. | investigate between-day variation
coefficient of variation | Standard deviation divided by the mean, often expressed as a percentage. | report the coefficient of variation
standard deviation | A measure of how observations are spread around their mean. | calculate the standard deviation
mean signal | The average measured output for a defined group. | compare mean signals
precision | Closeness among repeated measurements under stated conditions. | assess analytical precision
accuracy | Closeness of a measurement to the relevant reference or accepted value. | evaluate analytical accuracy
bias | A systematic difference from the relevant reference value. | investigate measurement bias
calibration | Establishing the relationship between measurement response and reference values. | verify calibration records
reference standard | A characterized material used to support measurement comparisons. | qualify a reference standard
quality-control sample | A sample used to monitor analytical performance. | review quality-control samples
reagent lot | An identified production batch of a reagent. | compare reagent lots
lot-to-lot variation | Differences associated with separate batches of a material. | evaluate lot-to-lot variation
plate effect | Variation associated with a measurement plate or its positions. | assess a plate effect
edge effect | A position-related difference at the outer wells of a plate. | check for an edge effect
assay drift | A change in measurement performance over time. | monitor assay drift
normalization | Adjusting results to a defined comparison or reference basis. | document normalization
acceptance criterion | A predefined requirement for judging a result or process. | specify acceptance criteria
root-cause investigation | A structured effort to identify supported underlying explanations. | conduct a root-cause investigation
run metadata | Information describing the conditions and history of an analytical run. | preserve run metadata''',
    precision='A 5% within-run coefficient of variation describes relative spread inside that run. It does not establish matching means across days or accuracy against a reference. Without supplied acceptance criteria, the exercise cannot declare the assay validated or failed.',
    precision_extra='Intermediate precision examines relevant changes within a laboratory; reproducibility often refers to broader changed conditions. Specify the intended meaning. Normalization must have a justified, documented basis, not be invented after the fact solely to make disagreeing runs appear aligned.',
    phrases='''Separate the levels | The within-run precision is consistent, but the day means differ.
Give the values | The means are eighty, one hundred, and one hundred twenty-five signal units.
Define the statistic | The CV describes relative spread within each run.
Limit the conclusion | That does not establish agreement across days.
Ask for the criteria | Which predefined acceptance criteria apply to this intended use?
Check the comparison | Was the same nominal control level used in each run?
Preserve the raw result | Keep the original measurements and their run records.
Investigate conditions | Compare reagent lots, calibration, operator, and relevant run conditions.
Avoid premature blame | We have not established which factor explains the shift.
Explain precision | Tight measurements can still differ systematically from a reference.
Name the percentage base | Twenty-five above one hundred is a 25% increase relative to one hundred.
Challenge the label | Fully reproducible is broader than these data support.
Keep normalization justified | State the reference and method used for any adjustment.
Request traceability | Link the plotted mean to its raw data and metadata.
Report the status | Between-day variation is under investigation.
Close with the question | The next review must explain the shift and evaluate it against the agreed criteria.''',
    notes='''Precise versus accurate | Close repeated values may still be systematically offset from a reference.
CV | Expand coefficient of variation before using the abbreviation in a mixed-audience meeting.
Same mean | Equal spread does not require equal averages.
Drift | A descriptive possibility, not a confirmed mechanism for these three values.
Reproducible | Specify what was repeated and which conditions changed.
Failed | A formal judgment requires the applicable criteria, not only an unfavorable-looking chart.''',
    d='''Which statement fits the data? | Each run has 5% CV, while day means differ from 80 to 125 units. | A 5% CV proves the same mean every day. | The assay is clinically validated because the means are positive. | The operator caused the shift, as already established. | The correct statement keeps within-run spread separate from the observed between-day differences.
Relative to day two's mean of 100, how much higher is day three's mean of 125? | 25% | 5% | 20% | 125% | The increase is twenty-five divided by the reference value one hundred, giving twenty-five percent.
Which follow-up best supports investigation? | Compare traceable run conditions and raw data before assigning a cause. | Delete the two means that differ from 100. | Declare every run acceptable without criteria. | Rename the axis to conceal the shift. | Comparing records and raw data can test explanations without prematurely choosing one.
A colleague rescales each day to a mean of 100 and calls the assay reproducible. What remains unresolved? | Whether the adjustment has a justified basis and the original between-day variation is understood | Whether the rescaled means are numerically equal to each other | Whether the three original runs occurred on different days | Whether the adjusted chart now uses the same vertical scale | Equalizing the plotted means is the adjustment's result, not independent evidence of performance. The original shift and the scientific basis for normalization still require examination.''',
    dialogue='''Chen | Every run has a five-percent CV, so I kept fully reproducible in the summary. What am I missing before we show this to the project team?
Imani | The [[within-run variation::Within-run variation describes spread inside each run, not whether the averages match across different days.]] is similar, but the means are eighty, one hundred, and one hundred twenty-five. The runs do not sit at the same level.
Chen | So the points can be tightly grouped each day while the groups move? I treated the repeated percentage as evidence of an unchanged result.
Imani | The [[coefficient of variation::The coefficient of variation expresses relative spread as standard deviation divided by the mean.]] is standard deviation divided by mean. Five percent describes relative spread; it does not tell us that the means match.
Chen | We intended the same nominal control level. Could the newest operator explain the shift? That was the first suggestion in yesterday's meeting.
Imani | Let us compare the [[run metadata::Run metadata identifies conditions such as operator, reagent lot, and calibration that can support investigation.]] first: operator, reagent lot, calibration and relevant conditions. We do not yet know which changes coincide.
Chen | Right. If the operator and reagent lot changed together, the pattern would not isolate either one. I should not report an attribution we cannot defend.
Imani | Keep both as questions in the [[root-cause investigation::A root-cause investigation tests supported explanations rather than assigning responsibility from an incomplete pattern.]]. The point is to test explanations against the records, not settle on the most convenient person to blame.
Chen | All three runs were in this laboratory. Is between-day reproducibility the clearest heading, or would another term make the conditions more precise?
Imani | We are examining [[intermediate precision::Intermediate precision covers relevant variation within one laboratory, including between-day conditions.]] within this laboratory. State the days and conditions examined so the reader does not infer an interlaboratory study.
Chen | I also wrote that day three rose twenty percent from day two. I divided twenty-five by the final value of one hundred twenty-five.
Imani | Use day two as the base. The [[mean signal::Mean signal is the average measured output being compared between day two and day three.]] increased twenty-five percent: twenty-five divided by one hundred. Twenty percent describes the reverse decrease.
Chen | Thanks. Is the shift enough to call the assay failed? I cannot find the intended-use limits in this review pack.
Imani | We need the applicable [[acceptance criterion::An acceptance criterion supplies the predefined requirement needed for a formal performance judgment.]]. Do not invent a pass or failure threshold from this chart; report the between-day difference as under investigation.
Chen | Someone offered to rescale every day's mean to one hundred. It would remove the visible shift, but would it resolve the performance question?
Imani | Not by itself. Any [[normalization::Normalization requires a defined and justified reference basis rather than an adjustment chosen only to conceal disagreement.]] needs a justified reference and documented method. An adjustment chosen only to align these means can hide what needs investigation.
Chen | Then retain the original readings and show how any adjusted result was derived. The unadjusted plot should not disappear from the package.
Imani | Agreed. Include the [[calibration::Calibration records describe the relationship to reference values and may help explain measurement differences.]] records too, so we can trace the measurement basis rather than infer it from the graph alone.
Chen | I will show the three means beside their CVs, correct the percentage, and list the missing criteria and records. No validation conclusion yet.
Imani | That gives [[precision::Precision concerns agreement among repeated measurements under specified conditions and must be qualified by those conditions.]] its proper scope. We retain the useful within-run result while making the unresolved between-day performance visible.''',
    transfer_title='A percentage needs its reference',
    transfer_setup='Two comparable fictional runs have means of 120 and 150 units. Their within-run CVs are both 4%. No acceptance criteria are supplied.',
    transfer='''Analyst: "The mean rose by ___ units." | thirty | Subtracting one hundred twenty from one hundred fifty gives thirty units.
Reviewer: "Relative to 120, that is a ___ increase." | 25% | Thirty divided by the reference value one hundred twenty equals twenty-five percent.
Analyst: "The four-percent CV describes within-run ___." | spread | The coefficient of variation concerns relative spread, not the change between means.
Reviewer: "A formal acceptance decision still needs the applicable ___." | criteria | The briefing supplies no acceptance criteria against which to make that decision.''',
    rehearsal=["Read the assay review. State the 5% within-run CV alongside daily means of 80, 100, and 125.","Swap roles. Correct the denominator: 100 to 125 is a 25% increase; 125 to 100 is a 20% decrease.","Read the corrected transfer. Preserve the 120 reference, 30-unit change, 25% increase, and missing acceptance criteria."]))

BOOK['units'].append(unit(
    title='Biomarkers and Translational Strategy',
    scene='Validated for which use?',
    skill='Specify the scope of biomarker validation and distinguish measurement performance from response prediction.',
    brief='Translational lead Sara and assay lead Noah review a fictional plasma-protein test. The analytical study met its predefined measurement criteria over 2 to 20 research units in the tested plasma conditions. No study has established that the protein predicts response to candidate B17. A slide calls it a validated predictive biomarker and proposes selecting trial participants by its value. The team must correct that claim and identify the intended-use evidence still needed. No patient-selection rule is authorized by the exercise.',
    cast='Sara | Translational lead\nNoah | Assay lead',
    culture=('A qualifier should identify the claim', 'Validated is persuasive because it sounds complete. Ask what was validated, in which material and range, and for which intended use. These questions help colleagues align scientific and clinical claims without treating the person who raised the issue as an obstacle to progress.'),
    a='''Which claim is supported by the supplied study? | The test met predefined analytical criteria over the assessed range and plasma conditions. | The protein predicts B17 response. | A patient-selection threshold has clinical support. | Regulatory qualification has been granted. | The supplied study concerns measurement performance in a defined analytical setting.
What evidence is absent? | A study establishing prediction of response to B17 | The fact that plasma was tested | The stated analytical range | The existence of predefined measurement criteria | The briefing expressly says response prediction has not been established.
Which proposed use requires additional support? | Selecting participants on an asserted predictive role | Describing the measured analyte | Stating the tested range | Reporting the analytical study's actual scope | Patient selection based on response prediction goes beyond the supplied analytical evidence.''',
    vocabulary='''biomarker | A measured characteristic indicating a biological process or response. | evaluate a biomarker
analyte | The substance or component a test measures. | identify the analyte
context of use | The defined purpose and setting in which a biomarker is to be used. | specify the context of use
analytical validation | Establishing that a test adequately measures its intended analyte for the stated use. | complete analytical validation
clinical validation | Establishing the relationship to the relevant clinical concept for the proposed use. | plan clinical validation
clinical utility | The usefulness of applying a test in a particular care decision. | assess clinical utility
biomarker qualification | Formal acceptance for a specified use through an applicable qualification process. | define the qualification scope
fit for purpose | Adequate for a specifically defined intended use. | demonstrate fit-for-purpose performance
reportable range | The interval over which results can be appropriately reported under the method. | specify the reportable range
limit of detection | The lowest level distinguishable from absence under defined conditions. | establish a limit of detection
limit of quantification | The lowest level measurable with specified quantitative performance. | establish a limit of quantification
matrix effect | An influence of other sample components on the measurement. | assess matrix effects
diagnostic sensitivity | The proportion of people with the target condition correctly identified as positive. | estimate diagnostic sensitivity
diagnostic specificity | The proportion without the target condition correctly identified as negative. | estimate diagnostic specificity
positive predictive value | The proportion of positive test results that correspond to the target condition. | interpret positive predictive value
negative predictive value | The proportion of negative results that correspond to absence of the target condition. | interpret negative predictive value
prevalence | The proportion of the relevant population with a condition at a stated time. | account for prevalence
decision threshold | A specified cutoff used in making a defined classification or decision. | justify a decision threshold
prognostic biomarker | A marker associated with likelihood of a clinical event or disease progression. | distinguish a prognostic biomarker
predictive biomarker | A marker identifying differing likelihood of an effect from a particular intervention. | evaluate a predictive biomarker
pharmacodynamic biomarker | A marker indicating biological response after exposure to an intervention. | measure a pharmacodynamic biomarker
patient stratification | Grouping patients by defined characteristics for analysis or an intended use. | justify patient stratification
prospective validation | Testing performance in a study planned before the relevant outcomes are observed. | design prospective validation
external validation | Evaluation in an independent setting or data source. | obtain external validation''',
    precision='Analytical validation concerns the measurement; clinical validation concerns the proposed clinical relationship. Clinical utility asks a further question about using the result in a decision. None of these labels should be inferred solely from another label or from an attractive plot.',
    precision_extra='Predictive refers here to differing effects of a particular intervention; prognostic concerns clinical course. Diagnostic sensitivity is not the same as an assay\'s detection limit. Always define the population, sample conditions, range, and intended decision before interpreting performance claims.',
    phrases='''Ask for the scope | Validated for which measurement and intended use?
State the analyte | The test measures the specified protein in plasma.
Name the range | The assessed measurement range is two to twenty research units.
Preserve the conditions | That evidence applies to the tested plasma conditions.
Separate the claims | Analytical performance does not establish prediction of treatment response.
Define the purpose | The proposed use is participant selection for the B17 program.
Avoid premature selection | We do not yet have evidence supporting that predictive selection rule.
Use the correct label | Describe an analytically evaluated test, not a clinically validated predictive biomarker.
Clarify qualification | A study result is not automatically formal biomarker qualification.
Ask about the cohort | Which population and outcomes would establish the claimed relationship?
Separate prognosis | Association with disease course is not necessarily prediction of treatment effect.
Check the cutoff | What supports the proposed decision threshold?
Preserve uncertainty | The relationship to B17 response remains unestablished.
Compare samples carefully | Performance in plasma does not automatically transfer to another sample matrix.
Identify the next evidence | The next study must address the intended clinical relationship.
Close the slide review | Keep the measurement result and the proposed clinical use in separate statements.''',
    notes='''Validated | Name the object and use rather than presenting validation as unlimited.
Predictive | In this context, prediction concerns effects of a particular intervention.
Qualified | A formal process and its defined scope cannot be inferred from an internal label.
Sensitive | Specify analytical detection or diagnostic classification.
Research units | Do not present an invented study scale as a clinical reference range.
Clinical utility | A relationship may be real without yet showing that using the test improves a decision.''',
    d='''Which description matches the supplied evidence? | The test met analytical criteria from 2 to 20 research units; prediction of B17 response is unestablished. | The test selects all B17 responders reliably. | The protein is qualified for every clinical use. | A result above ten guarantees benefit. | The correct description separates the completed analytical evaluation from the unestablished clinical relationship.
Why is a predictive label premature? | No study has established differing B17 response associated with the marker. | The analyte is measured in plasma. | A measurement range was defined. | The analytical criteria were predefined. | A predictive claim requires evidence about the intervention-related response, which the brief says is absent.
A colleague chooses 11 as an eligibility cutoff because it is the midpoint of 2 to 20. What evidence is missing? | Evidence supporting classification by that cutoff for the proposed B17 use | Evidence that 11 lies inside the assessed measurement range | Evidence that the midpoint of 2 and 20 equals 11 | Evidence that the analytical study used plasma samples | An in-range midpoint is an arithmetic property, not validation of a selection rule. The missing evidence concerns the intended response-related clinical use.
What would changing the sample from plasma require in the claim? | Appropriate evaluation of the changed matrix rather than automatic transfer of performance | Assuming identical performance because the analyte has the same name | Calling the new matrix clinically validated without data | Removing all information about sample conditions | Sample components can affect measurement, so the original conditions cannot be generalized automatically.''',
    dialogue='''Sara | The slide says validated predictive biomarker and then proposes selecting participants by the protein value. Can you tell me which part of that statement our study establishes?
Noah | It establishes the assessed [[analytical validation::Analytical validation concerns the test's measurement performance under its specified conditions and intended analytical use.]] scope: the test met predefined measurement criteria from two to twenty research units in the plasma conditions we evaluated.
Sara | That is useful, but it does not tell us whether a participant with a particular value is more likely to respond to B17 than another participant.
Noah | Correct. We have not established [[clinical validation::Clinical validation would establish the relationship to the proposed clinical concept, here B17 response prediction.]] for that proposed relationship. The measurement study did not test whether the marker identifies differences in response to this candidate.
Sara | We should state the planned decision explicitly, then. The proposed use is selecting participants for the B17 program, not simply reporting protein concentration in a research sample.
Noah | That is the [[context of use::Context of use specifies the purpose and setting of the proposed biomarker application.]] that needs supporting evidence. A reliable measurement can be necessary without being sufficient for the clinical decision being proposed.
Sara | What should replace validated predictive biomarker in the current deck? I do not want to lose the analytical achievement while correcting the clinical overstatement.
Noah | Name the [[analyte::The analyte is the substance measured, allowing a precise analytical claim without an unsupported predictive label.]], tested matrix, and range, then state that response prediction remains unestablished. We can report the achievement accurately without borrowing a broader label.
Sara | Why did the team choose ten units as the cutoff? Being inside the measurement range does not tell us who is likely to respond to B17.
Noah | A [[decision threshold::A decision threshold needs support for its classification purpose and is not supplied by the midpoint of an analytical range.]] needs a justified relationship to the intended decision. The assay's ability to measure a value does not tell us what that value means for response.
Sara | Suppose another study later associates the protein with faster disease progression. Would that automatically make it predictive for B17?
Noah | No. A [[prognostic biomarker::A prognostic biomarker concerns clinical course and does not automatically identify differential effects of a treatment.]] concerns the likely clinical course. That association would not by itself establish that the marker identifies a differing effect of this intervention.
Sara | The distinction needs to appear in our terminology sheet. People use predict in everyday English for almost any association with a later event.
Noah | In this development claim, a [[predictive biomarker::A predictive biomarker identifies different likelihoods of effects from a particular intervention, requiring the relevant evidence.]] relates to the effect of a particular intervention. We should define the intended scientific meaning rather than assume the everyday word settles it.
Sara | Another team wants to transfer the assay to a different sample type. They believe the protein name being unchanged means the measurement evidence transfers automatically.
Noah | We need to evaluate possible [[matrix effect::Matrix effect describes how other sample components can influence measurement, limiting automatic transfer between sample types.]] and the changed conditions. The same analyte in another sample environment is not automatically covered by the plasma performance study.
Sara | And an internal study meeting its criteria is not the same as receiving formal acceptance for every possible regulatory use. We should remove qualified from that sentence too.
Noah | Yes. [[Biomarker qualification::Biomarker qualification is a formal, scoped acceptance process, not a synonym for an internal analytical result.]] has an applicable process and defined scope. We should not imply that such a determination exists when the evidence described here does not establish one.
Sara | I will remove validated predictive biomarker and the implied selection rule. Please give me wording that preserves the analytical result and names the clinical question still open.
Noah | Then later we can also assess [[clinical utility::Clinical utility asks whether applying the test is useful in the specific care decision, beyond measurement alone.]] for the relevant decision. For now, accurate measurement is a defined achievement, and the clinical application remains a separate evidence question.''',
    transfer_title='Measurement is not selection',
    transfer_setup='A test measures a protein adequately from 5 to 50 study units. No relationship to treatment response has been studied. A colleague proposes using 25 as an eligibility cutoff.',
    transfer='''Scientist: "Five to fifty is the assessed measurement ___." | range | The supplied interval describes where measurement performance was evaluated.
Colleague: "Twenty-five is a proposed decision ___." | threshold | The proposed cutoff concerns an eligibility decision, not merely measurement capability.
Scientist: "Its relationship to response is ___." | unstudied | The briefing explicitly says no response relationship has been studied.
Colleague: "The analytical result does not authorize participant ___." | selection | Measurement performance alone does not support the proposed clinical selection rule.''',
    rehearsal=["Read the biomarker discussion. Keep the 2-to-20 range and tested plasma conditions with the analytical result.","Swap roles. Distinguish measuring the protein from predicting B17 response; do not create an eligibility rule.","Read the corrected threshold transfer. Separate the 5-to-50 measurement range from the proposed cutoff of 25."]))

BOOK['units'].append(unit(
    title='Preclinical Data Packages',
    scene='A model effect is not proof of human benefit',
    skill='Summarize a nonclinical finding with its design and limitations, then identify missing information for the next review.',
    brief='A fictional animal-model report compares 12 treated animals with 12 controls and reports a 20% lower mean model-endpoint value at one tested exposure. Groups were randomized; assessor blinding is not documented in the supplied summary. No uncertainty interval, exposure-response series, or human outcome data are provided. Scientist Amir and development lead Zoe review a slide calling the result proof of human benefit. They need a precise nonclinical summary and the missing study details, not an invented clinical conclusion.',
    cast='Amir | Scientist\nZoe | Development lead',
    culture=('Report what the study can carry', 'Development discussions reward concise conclusions, but a short sentence should still name the model, comparison, and limits. Separate a positive result from a claim about people. Asking for missing design information strengthens the review without implying that the study was necessarily conducted badly.'),
    a='''What is the reported comparison? | A 20% lower mean model-endpoint value in 12 treated animals versus 12 controls at one exposure | A 20% improvement in human survival | Identical results across every tested exposure | A completed clinical trial in 24 patients | The brief describes an animal-model mean endpoint comparison, not a human outcome.
What is known about blinding? | It is not documented in the supplied summary. | The assessors were definitely blinded. | The assessors were definitely unblinded. | Randomization automatically establishes blinding. | The summary's omission leaves blinding status unestablished rather than proving either condition.
Which conclusion is unsupported? | Human benefit has been proved. | The groups were randomized. | One exposure was tested. | Further study details are needed. | No human outcome data are supplied, so the animal result cannot establish human benefit.''',
    vocabulary='''preclinical package | The body of nonclinical evidence supporting a development review. | assemble a preclinical package
model relevance | How an experimental system relates to the biological question of interest. | assess model relevance
sex as a biological variable | Consideration of sex-related differences in design, analysis, and reporting. | address sex as a biological variable
randomization | Allocation by a chance-based process to reduce systematic selection differences. | document randomization
blinding | Keeping relevant group or treatment information hidden from specified people. | verify assessor blinding
sample size | The number of experimental units in a defined analysis. | justify the sample size
experimental unit | The independently assigned unit underlying an experimental comparison. | identify the experimental unit
pharmacokinetics | The time course of a substance's absorption, distribution, metabolism, and elimination. | characterize pharmacokinetics
pharmacodynamics | The biological effects of an intervention and their relationship to exposure. | evaluate pharmacodynamics
exposure | The amount or concentration reaching a biological system over time. | characterize exposure
exposure-response relationship | The relationship between measured exposure and an observed effect. | examine the exposure-response relationship
bioavailability | Rate and extent of systemic availability of an active substance. | assess bioavailability
biodistribution | The pattern of a substance's presence across tissues or body compartments. | characterize biodistribution
efficacy endpoint | A defined measurement used to assess the intended effect in a study. | specify the efficacy endpoint
tolerability | How adverse effects affect the ability to tolerate an intervention. | report tolerability findings
toxicology | Study of harmful effects of substances under specified conditions. | review toxicology data
NOAEL | No-observed-adverse-effect level under the conditions of a defined study. | interpret the NOAEL in context
safety margin | A comparison of relevant exposure or dose levels used in safety assessment. | justify the safety-margin comparison
good laboratory practice | A formal quality system for applicable nonclinical safety studies. | verify good laboratory practice status
dose-response relationship | The relationship between administered dose and a measured effect. | distinguish dose-response from exposure-response
translational uncertainty | Uncertainty in applying findings from one biological setting to another. | communicate translational uncertainty
study report | The documented methods, results, and interpretation of a study. | review the full study report
data provenance | The origin and processing history of data used in a result. | preserve data provenance
uncertainty interval | A stated range expressing uncertainty under a defined analytical method. | report the uncertainty interval''',
    precision='A 20% lower model-endpoint mean is not automatically a 20% clinical benefit or a statistically established effect. State the comparison and missing uncertainty information. Randomization and blinding are distinct design features; one does not establish the other.',
    precision_extra='Dose is what is administered; exposure concerns what reaches the biological system over time. PK means pharmacokinetics and PD means pharmacodynamics. A result at one exposure does not describe an exposure-response relationship or establish a human safety margin.',
    phrases='''Name the model result | The treated group had a 20% lower mean model-endpoint value than controls.
State the groups | There were twelve treated animals and twelve controls.
Identify the tested condition | The result comes from one tested exposure.
Keep the species boundary | Human benefit has not been established by these data.
Separate design features | Randomization is documented; assessor blinding is not stated in this summary.
Request the source | Please provide the full report and the relevant analysis details.
Ask about uncertainty | Which interval or analysis describes uncertainty around the reported difference?
Avoid a significance claim | The supplied percentage alone does not establish statistical significance.
Name the missing relationship | We do not yet have an exposure-response series.
Keep safety separate | An efficacy-endpoint result does not establish the complete safety profile.
Clarify PK and PD | Distinguish the exposure measurements from the biological response.
Check study status | Do not infer formal GLP compliance from the word preclinical.
Preserve unit definitions | Identify the experimental units behind the reported sample size.
Limit the translation | This supports further investigation within a defined development question.
Avoid an invented margin | We cannot calculate a human safety margin from these facts alone.
Close the package review | Summarize the finding, its limits, and the specific evidence still required.''',
    notes='''Twenty-percent lower | Specify which endpoint, comparison, and mean; do not translate it into a patient claim.
Significant | Distinguish statistical evidence from an everyday judgment of importance.
Not documented | Does not automatically mean not performed.
PK/PD | Expand the terms for mixed audiences before using shorthand.
GLP | A defined quality framework, not a general compliment about laboratory work.
Safe | Specify the evidence and setting; one positive endpoint does not establish an unrestricted safety claim.''',
    d='''Which sentence best represents the result? | At one exposure, the treated animal group had a 20% lower mean model endpoint than controls; human benefit is unestablished. | Humans improve by 20% with this intervention. | The treatment is proven safe at every exposure. | Blinded human efficacy was confirmed. | The supported sentence preserves the model, comparison, exposure limit, and absence of human evidence.
What does the missing blinding information mean? | The review needs clarification from the study record. | Randomization proves the assessors were blinded. | The study definitely had no blinding. | The endpoint can be described as independently replicated in humans. | An omitted design detail needs verification rather than an assumption about how the study was conducted.
Which addition would directly clarify uncertainty around the reported 20% model-endpoint difference? | The underlying group results and a justified uncertainty analysis | Confirmation that both groups contained twelve animals, without their results | The reported randomization method alone, without variability or analysis | The proposed human population, without additional model-study results | Group sizes and randomization matter but do not alone quantify uncertainty in the observed difference. The results and appropriate analysis address that question; a target population does not replace them.
Which distinction is accurate? | Administered dose and measured exposure are related but not identical concepts. | One tested exposure establishes every dose-response relationship. | An efficacy endpoint is the complete toxicology package. | Formal GLP status follows automatically from using animals. | Dose describes administration, while exposure describes the substance reaching the system over time.''',
    dialogue='''Zoe | The development slide says this is proof of human benefit. The reported model effect is encouraging, but I need a sentence that will survive a detailed package review.
Amir | The [[efficacy endpoint::The efficacy endpoint is the defined model measurement, not a directly measured human clinical outcome.]] mean was twenty percent lower in twelve treated animals than in twelve controls. That is the comparison the study summary actually reports.
Zoe | We should say it was an animal model in the headline, not leave the audience to find that in a footnote after hearing a clinical claim.
Amir | Agreed. The [[model relevance::Model relevance concerns how the experimental system relates to the development question without equating it with people.]] needs explanation, but relevance does not make the model identical to human disease. No human outcome data are included in this package.
Zoe | I see randomized allocation, but nothing about assessor blinding. Can you obtain that record before anyone adds blinded to the summary?
Amir | [[Randomization::Randomization concerns chance-based allocation and does not establish whether assessors knew group assignments.]] and assessor blinding are separate design features. The first is documented here; the second is not stated, so we need clarification rather than an assumption.
Zoe | I will request that detail from the study team. An omission in this summary does not prove the assessors knew the assignments, but it leaves the status unclear.
Amir | Ask for the relevant [[study report::The full study report provides methods and results needed to verify details omitted from a short summary.]] section and any supporting record. We should correct the summary from verified information, not fill the gap with the most favorable wording.
Zoe | The twenty-percent difference also appears without an interval. I cannot tell how much uncertainty surrounds the estimate from the headline alone.
Amir | We need the appropriate [[uncertainty interval::An uncertainty interval expresses the estimate's uncertainty under the relevant analytical method.]] or other specified analysis and the underlying results. A percentage by itself does not establish statistical significance or the reliability of the estimate.
Zoe | The team tested one exposure. That can establish a result under that condition, but it cannot show the whole pattern across lower and higher exposures.
Amir | Correct. We do not yet have an [[exposure-response relationship::An exposure-response relationship requires evidence about how effects vary with exposure, not one tested condition alone.]]. Keep that limitation beside the result so the development discussion does not assume a series that was never performed.
Zoe | We also need to separate an administered dose from what reaches the relevant biological system. Those terms are being used interchangeably in the notes.
Amir | The [[pharmacokinetics::Pharmacokinetics concerns the substance's disposition over time and helps distinguish dose from resulting exposure.]] information addresses the disposition and exposure over time. The biological effect belongs to the pharmacodynamic question; neither can be replaced by a vague statement that the dose worked.
Zoe | What about the sentence saying the favorable endpoint establishes safety? I assume the full safety question requires different information and appropriate professional review.
Amir | Yes. Review the relevant [[toxicology::Toxicology concerns harmful effects and cannot be replaced by a favorable efficacy-endpoint result.]] and other safety evidence separately. We should not infer a complete safety profile from an endpoint designed to assess the intended effect.
Zoe | Nor should we invent a human safety margin from this one model result. We do not have the necessary comparison or its scientific justification.
Amir | Exactly. Any [[safety margin::A safety margin needs a justified comparison of relevant levels, which the supplied facts do not provide.]] must state the compared quantities and supporting basis. A reassuring label cannot supply the missing exposure information or translation rationale.
Zoe | I will keep the result explicitly nonclinical and request the missing uncertainty and exposure information. Please also confirm the blinding status from the study records.
Amir | That communicates [[translational uncertainty::Translational uncertainty limits the extension from the tested model to another biological or clinical setting.]] without discarding the finding. The result can justify further investigation while remaining distinct from proof that people will benefit.''',
    transfer_title='An omission is not a finding',
    transfer_setup='A study summary documents random allocation but does not describe assessor blinding. A colleague proposes writing either fully blinded or definitely unblinded without checking the report.',
    transfer='''Scientist: "Random ___ is documented." | allocation | The supplied summary explicitly describes random assignment to groups.
Reviewer: "Assessor blinding remains ___." | unstated | The summary gives no information establishing the assessors' blinding status.
Scientist: "We need the relevant study ___." | record | The underlying study documentation can clarify the omitted design detail.
Reviewer: "Neither proposed label is supported without ___." | verification | Both fully blinded and definitely unblinded exceed the currently supplied evidence.''',
    rehearsal=["Read the preclinical review. Preserve twelve treated animals, twelve controls, one exposure, and the 20% model-endpoint difference.","Swap roles. State blinding not documented rather than blinded or unblinded; request the relevant study record.","Read the corrected omission transfer. Keep random allocation distinct from unverified assessor blinding."]))

BOOK['units'].append(unit(
    title='CMC and Scale-Up in Biotech',
    scene='Two small runs do not prove the large process',
    skill='Distinguish titer, recovered quantity, product quality, and scale-up evidence in a process-transfer discussion.',
    brief='Process scientist Hana and manufacturing lead Ben review two fictional 1-liter runs after a process transfer. Both achieved a harvest titer of 0.8 grams per liter. A 200-liter run has not been performed. The slide promises 160 grams of finished acceptable product by multiplying titer by volume. Downstream recovery and relevant quality results at the larger scale are unestablished. The team must retain the small-run result while correcting the forecast and defining the missing scale-up evidence.',
    cast='Hana | Process scientist\nBen | Manufacturing lead',
    culture=('A calculation can be correct and the promise wrong', 'Operational audiences need quantities and delivery expectations, but an arithmetic projection must keep its assumptions visible. Clarify the process stage, recovery basis, and quality status. A useful estimate is conditional; it should not quietly become a commitment to release finished material.'),
    a='''What was demonstrated? | Harvest titer of 0.8 g/L in two 1-liter runs | Release of 160 grams of finished product | A successful 200-liter run | Complete quality comparability at all scales | The evidence is limited to harvest titer in the two specified small runs.
What does 0.8 g/L multiplied by 200 liters give under the stated assumption? | A hypothetical 160 grams at harvest before downstream losses | A guaranteed 160 grams of released finished product | A 160% recovery rate | A validated clinical dose | The arithmetic estimates harvest quantity if the same titer holds; recovery and quality are separate.
Which evidence remains missing? | Larger-scale performance, downstream recovery, and relevant quality results | Whether two small runs occurred | The small-run titer value | The proposed large-run volume | The briefing expressly leaves those larger-scale and finished-product conditions unestablished.''',
    vocabulary='''CMC | Chemistry, manufacturing, and controls: the product and process quality package. | review the CMC package
technology transfer | Movement of process knowledge and capability between teams or sites. | execute technology transfer
upstream processing | The production stages that generate the biological material. | characterize upstream processing
downstream processing | Stages that recover and purify material after production. | evaluate downstream processing
titer | Product concentration at a specified process stage. | report harvest titer
yield | Output relative to a stated input or theoretical basis, with context required. | define the yield basis
recovery | The proportion of material retained through a specified process step. | calculate downstream recovery
purity | The proportion or profile of intended material relative to impurities. | assess product purity
potency | A measure of biological activity relevant to the product's function. | evaluate product potency
aggregation | Association of molecules into larger assemblies. | monitor product aggregation
critical quality attribute | A property needing control within appropriate limits to ensure desired quality. | identify critical quality attributes
critical process parameter | A process variable whose variability can affect a critical quality attribute. | assess critical process parameters
process parameter | A measurable or controlled operating variable in a process. | document process parameters
process characterization | Study of how process conditions affect performance and quality. | plan process characterization
scale-up | Increasing the size or production capacity of a process. | evaluate scale-up risks
scale-down model | A smaller model intended to represent relevant larger-process behavior. | qualify a scale-down model
mass transfer | Movement of a substance between regions or phases of a system. | assess mass-transfer behavior
mixing | Distribution of material within a process vessel or system. | characterize mixing
hold time | The time material remains at a specified stage or condition. | justify hold times
bioburden | The level of viable microorganisms associated with a material or process. | monitor bioburden
comparability | Assessment that a change does not adversely affect relevant product quality, safety, or efficacy. | establish a comparability strategy
change control | Formal review and management of a proposed change. | follow change control
process validation | Documented evidence that a process can consistently deliver the intended quality. | plan process validation
batch record | The record of materials, steps, observations, and events for a batch. | review the batch record''',
    precision='At the same assumed titer, 0.8 grams per liter times 200 liters gives 160 grams at harvest. It does not establish downstream recovery, final purity, potency, or release. Titer is a concentration; always define the basis when using yield.',
    precision_extra='CMC means chemistry, manufacturing, and controls; CQA means critical quality attribute; CPP means critical process parameter. Matching one output does not establish complete product comparability. Assess relevant quality properties and process changes through the applicable development and quality framework.',
    phrases='''State the observed scale | Both results came from one-liter runs.
Name the stage | The measured value is harvest titer, not released final quantity.
Show the arithmetic | At the same titer, two hundred liters would contain one hundred sixty grams at harvest.
Expose the assumption | The larger process has not yet demonstrated that titer.
Separate recovery | Downstream losses are not included in that calculation.
Keep quality visible | Quantity alone does not establish purity or potency.
Clarify the acronym | CMC covers chemistry, manufacturing, and controls.
Ask about attributes | Which quality attributes need comparison after this change?
Avoid premature validation | Two small runs do not establish the complete larger-scale process.
Check process behavior | Mixing and mass transfer may differ with scale.
Identify the evidence | We need relevant larger-scale performance and quality data.
Respect change review | Route the process change through the appropriate quality review.
Define the model | Which aspects of the large process does the small model represent?
Qualify the forecast | Present this as a conditional harvest estimate.
Separate release | A projected quantity is not a release decision.
Close the transfer | Document the observed performance, open risks, and next agreed evaluation.''',
    notes='''Grams per liter | Concentration, not total quantity.
Harvest versus finished | Material at harvest has not necessarily passed through purification and release.
Recovery | Specify the process stage and input basis.
Same titer | Does not establish the same impurity profile or biological activity.
Scale-up | A larger vessel does not guarantee proportionally identical performance.
Validated | State the process, scope, and supporting evidence rather than use it as a general success label.''',
    d='''Which forecast is appropriately qualified? | If 0.8 g/L holds at 200 liters, harvest quantity would be 160 grams before recovery and quality evaluation. | Two small runs guarantee 160 grams of released product. | Titer alone proves complete comparability. | The larger process is validated without being run. | The qualified forecast states its titer assumption, process stage, and unresolved finished-product conditions.
If a separate hypothetical process retains 70% of 160 grams, how much remains after that step? | 112 grams | 230 grams | 70 grams | 160 grams | Multiplying one hundred sixty by zero point seven gives one hundred twelve grams.
Which item is a quality question rather than simply a quantity calculation? | Whether relevant potency and impurity attributes remain appropriate | Whether 0.8 times 200 equals 160 | Whether the proposed volume is 200 liters | Whether two one-liter runs were reported | Potency and impurity attributes concern product quality, not only arithmetic output.
Both one-liter runs have the same titer. Which proposed summary overstates the demonstrated scope? | Matching titer establishes larger-scale quality comparability. | Matching titer is one result from the small-run process. | Larger-scale recovery and quality evidence remain outstanding. | The 160-gram figure assumes the titer holds at 200 liters. | Equal small-run concentration is not evidence for all relevant larger-scale quality attributes. The other statements retain the observed scale or explicitly identify the open assumptions.''',
    dialogue='''Ben | I have a production slide promising 160 grams of acceptable finished product at 200 liters. That comes from the two one-liter runs. Can we support it?
Hana | The measured [[titer::Titer is concentration at the specified harvest stage, not a quantity of finished released material.]] was 0.8 grams per liter at harvest. We have not run 200 liters, and finished material is a different stage.
Ben | Then 160 is a correct multiplication with an unproven scale assumption. I also mislabeled where in the process that quantity would exist.
Hana | Yes. The [[scale-up::Scale-up changes process size and requires relevant performance evidence rather than automatic extrapolation from small runs.]] still needs evidence. Write conditional harvest estimate, not finished-product commitment, so the receiving team can see both limits.
Ben | What would change the amount after harvest? The table currently carries all 160 grams straight through purification without showing any loss.
Hana | It omits downstream [[recovery::Recovery describes the proportion retained through specified downstream stages and affects the final quantity.]]. We need the retained fraction for the relevant stages, not an implicit assumption that all harvested material reaches the end.
Ben | If a later run did match the concentration, could I at least use quality confirmed? The slide needs a short status for the review.
Hana | Matching concentration does not verify every [[critical quality attribute::Critical quality attributes concern properties necessary for intended quality, beyond the amount produced.]]. A short status still has to preserve the relevant purity, activity, and other quality questions.
Ben | So an equal number of grams does not necessarily mean an equal biological effect. That distinction needs to survive when this becomes a commercial forecast.
Hana | Correct. [[Potency::Potency measures relevant biological activity and is not established solely by product concentration.]] addresses relevant biological activity. The concentration alone does not establish it, just as it does not describe the full impurity profile.
Ben | We are also changing vessel size. I do not want the scale discussion reduced to multiplying every small-run setting by two hundred.
Hana | The review needs relevant [[mass transfer::Mass transfer concerns movement within the system and may behave differently when the process scale changes.]] and mixing behavior. Larger volume can change process conditions; proportional arithmetic does not demonstrate equivalent performance.
Ben | Can we still use the small system to investigate risks? I do not want to discard two useful runs because they answer a narrower question.
Hana | We can establish what a [[scale-down model::A scale-down model can represent selected larger-process behavior when its relevance is appropriately established.]] represents. Its value depends on the relevant behavior demonstrated, not merely on using a smaller vessel.
Ben | I will attach the process versions and batch records to the transfer pack. Which route keeps the proposed changes and their review traceable?
Hana | Use [[change control::Change control provides the formal review and traceability needed when process changes are proposed or implemented.]] and the applicable transfer process. The receiving team needs the actual settings, changes, and supporting records, not just the headline.
Ben | One last wording point: two matching titers do not support saying comparability demonstrated. We still lack the relevant larger-scale quality results.
Hana | Exactly. Establishing [[comparability::Comparability requires assessment of relevant product consequences of a change, not agreement in a single output alone.]] requires examining the consequences for the product. A single matching output is not the whole assessment.
Ben | The revised slide will say two one-liter runs at 0.8 grams per liter; 160 grams is hypothetical harvest output before recovery and quality evaluation.
Hana | That is a usable [[CMC::CMC is the chemistry, manufacturing, and controls package connecting process performance with product quality.]] update. Keep finished acceptable output unconfirmed and name the remaining evidence needed before making that commitment.''',
    transfer_title='Concentration is not the final quantity',
    transfer_setup='A hypothetical harvest contains 0.5 grams per liter in 100 liters. A stated downstream step retains 80% of the harvest material. No release decision is supplied.',
    transfer='''Scientist: "The harvest contains ___ grams." | fifty | One hundred liters multiplied by zero point five grams per liter equals fifty grams.
Reviewer: "At eighty-percent recovery, ___ grams remain." | forty | Eighty percent of fifty grams equals forty grams after the specified step.
Scientist: "That is a quantity calculation, not a ___ decision." | release | The briefing gives no quality review or authorization releasing the material.
Reviewer: "Keep the relevant product-quality evidence ___." | separate | The amount retained does not by itself establish the relevant quality attributes.''',
    rehearsal=["Read the scale-up exchange. Distinguish observed one-liter titer from assumed 200-liter performance and harvest from finished output.","Swap roles. State 0.8 times 200 equals 160 grams before downstream recovery; do not claim release.","Read the corrected transfer. Say fifty grams at harvest and forty after the stated step, with quality assessment separate."]))

BOOK['units'].append(unit(
    title='IP, Freedom to Operate, and Collaboration',
    scene='A confidentiality agreement is not a material license',
    skill='Identify unresolved material-use and publication terms while keeping ownership, permission, and freedom to operate distinct.',
    brief='Two fictional research partners plan to exchange a nonclinical reference protein for three named bench assessments. A confidentiality agreement is signed, but the material-transfer terms remain a draft. Permitted use, onward transfer, publication review, and rights in new findings are unresolved. Scientist Julia asks counsel Ravi whether shipment can proceed and whether owning a related patent settles third-party rights. Their discussion identifies questions for the authorized review; it does not interpret a real agreement or approve a transfer.',
    cast='Julia | Scientist\nRavi | Counsel',
    culture=('A shared scientific aim does not settle the agreement', 'Researchers may use collaborate to mean anything from a limited evaluation to joint development. Define the intended work and the relevant rights before relying on that word. Asking about publication or ownership early can protect the relationship by exposing different expectations before materials move.'),
    a='''Which agreement is signed? | The confidentiality agreement | The final material-transfer agreement | A worldwide exclusive development license | A completed assignment of every future invention | The brief states that confidentiality is agreed while the material-transfer terms remain a draft.
Which issue remains unresolved? | Permitted use and publication review, among other material-transfer terms | Whether a reference protein is proposed | Whether three bench assessments are contemplated | Whether counsel has been asked for review | The briefing explicitly identifies the listed terms as unresolved.
What does ownership of a related patent establish about third-party rights here? | It does not by itself establish freedom to operate. | It automatically removes every third-party right. | It authorizes every recipient use worldwide. | It replaces the material-transfer review. | A party's own patent does not automatically resolve rights held by others.''',
    vocabulary='''intellectual property | Legally recognized rights in inventions, works, marks, or other protected subject matter. | identify relevant intellectual property
background IP | Intellectual property brought into a collaboration, as defined by the agreement. | define background IP
foreground IP | New intellectual property arising from the collaboration under its agreed definitions. | address foreground IP
inventorship | Legal identification of the people who contributed to a claimed invention. | assess inventorship
ownership | The legal holding of a right or asset. | clarify ownership
assignment | Transfer of ownership of specified rights. | distinguish an assignment from a license
license | Permission to exercise specified rights under stated terms. | negotiate a license
field of use | The defined application area within which permission applies. | limit the field of use
territory | The geographic scope of a right or permission. | specify the territory
exclusive license | Permission with defined exclusivity within its agreed scope. | define exclusive-license scope
nonexclusive license | Permission that does not generally prevent granting similar rights to others. | discuss a nonexclusive license
confidentiality obligation | A duty concerning protection and permitted disclosure of information. | comply with confidentiality obligations
nondisclosure agreement | An agreement governing specified confidential information. | review a nondisclosure agreement
material transfer agreement | An agreement governing the transfer and use of tangible research material. | finalize a material transfer agreement
permitted use | The activities authorized for the material or rights under the agreement. | define permitted use
onward transfer | Passing material or rights to another recipient. | address onward transfer
publication review | An agreed process for reviewing proposed public disclosure. | specify publication review
publication embargo | A stated restriction or delay on publication under applicable terms. | define a publication embargo
patent claim | The legal wording defining the scope of protection sought or granted. | review relevant patent claims
patentability | Whether an invention meets the applicable criteria for patent protection. | assess patentability
freedom to operate | Whether proposed acts can proceed without infringing relevant third-party rights. | obtain a scoped freedom-to-operate review
know-how | Practical technical information or expertise, sometimes protected as confidential information. | identify transferred know-how
third-party rights | Rights held by someone outside the parties to the proposed arrangement. | assess third-party rights
governing agreement | The contract whose applicable terms control the relevant relationship or activity. | identify the governing agreement''',
    precision='NDA means nondisclosure agreement; MTA means material transfer agreement; FTO means freedom to operate. Confidentiality, material permission, ownership, and third-party rights are different questions. The effect of any document depends on its actual language, scope, law, and circumstances.',
    precision_extra='A patent generally provides a right to exclude specified acts by others, not an automatic right to practice every related activity. Patentability and freedom to operate therefore ask different questions. Obtain appropriately scoped professional review rather than infer clearance from ownership.',
    phrases='''Identify the signed document | The confidentiality agreement is signed; the material-transfer terms are not final.
Define the activity | The proposed use is three named nonclinical bench assessments.
Separate permissions | Permission to receive information does not necessarily authorize use of the material.
Check onward transfer | May the recipient send the material to another laboratory?
Clarify new findings | How will rights in results and new inventions be addressed?
Separate inventorship | Inventorship and ownership should not be treated as interchangeable labels.
Protect publication | What review process and time limits apply before public disclosure?
Avoid an unlimited delay | Publication review needs defined terms, not an unstated permanent veto.
Name existing rights | Identify the background IP each party brings.
Define the new work | Distinguish collaboration results from pre-existing know-how.
Ask about third parties | Which relevant rights are held outside these two parties?
Scope FTO | The review needs the proposed acts, territories, and relevant time.
Avoid a patent shortcut | Owning our patent does not automatically establish freedom to operate.
Reserve authorization | Shipment needs the appropriate completed review and authorization.
Record the open terms | Keep permitted use and publication questions visible in the draft.
Close accurately | Scientific interest is aligned; the transfer terms remain unresolved.''',
    notes='''Own versus use | Holding one right and having permission for a proposed activity are different questions.
NDA versus MTA | The labels indicate different purposes; read the actual terms rather than assume either is comprehensive.
Research only | Define the permitted research and any restrictions instead of relying on a broad phrase.
Publication review | Specify purpose, timing, and consequences through the actual agreement.
Inventor versus owner | The legal concepts differ and may involve different people or entities.
Cleared | State the reviewed activity and scope; do not present a limited review as universal permission.''',
    d='''Which response best fits the shipment question? | The MTA terms remain unresolved, so seek the required review and authorization before treating shipment as approved. | The signed NDA automatically approves every material use. | A common scientific goal replaces contract review. | Shipment proves the terms were accepted in advance. | The brief establishes only a signed confidentiality agreement and unfinished transfer terms.
Which review question concerns permitted use rather than a different transfer term? | Which named bench assessments may the recipient perform with the protein? | May the recipient send the protein to a third laboratory? | How long may the provider review a proposed manuscript? | Who owns an invention arising from the collaboration? | Permitted use defines the recipient's authorized activities. The other questions concern onward transfer, publication review, and ownership; each is important but distinct.
Why does a related owned patent not settle FTO? | Other parties may hold relevant rights affecting the proposed acts. | Patent ownership always means the patent is invalid. | Every research material is automatically unprotected. | An MTA can never contain use terms. | Rights held by others can remain relevant despite ownership of a separate patent.
Which statement preserves the publication issue? | The publication-review process and timing remain to be agreed. | Every result may be published immediately because an NDA exists. | Publication is forbidden forever regardless of the draft. | A planned manuscript proves ownership of all inventions. | The supplied draft has unresolved publication terms, so neither unrestricted release nor permanent prohibition is established.''',
    dialogue='''Julia | The partners agree on the science, and the confidentiality agreement is signed. Can I arrange shipment of the reference protein for the three bench assessments now?
Ravi | The [[material transfer agreement::The material transfer agreement governs the proposed tangible-material transfer and remains unfinished in this case.]] is still a draft. We need the relevant terms reviewed and authorized before treating the transfer as approved.
Julia | I had assumed the signed confidentiality document covered the exchange. It lets us discuss the work, but that may be different from permission to use the material.
Ravi | Exactly. A [[nondisclosure agreement::A nondisclosure agreement addresses specified confidential information and does not automatically settle material-use permission.]] does not automatically answer every material-use question. We must examine the actual documents rather than assume the title grants whatever the project needs.
Julia | The intended work is limited to three named assessments. The recipient also mentioned asking a separate laboratory to help, which is not addressed in the draft.
Ravi | Define the [[permitted use::Permitted use identifies which activities the recipient is authorized to perform under the agreement.]] precisely and address any onward transfer. The scientific plan should match the scope being reviewed, including which organizations would actually handle the material.
Julia | We also need to clarify what happens to discoveries made during the evaluation. Each team is bringing existing methods and information to the work.
Ravi | Identify the [[background IP::Background IP identifies pre-existing intellectual property brought into the collaboration under the agreed definitions.]] separately from new results. The definitions should let both parties distinguish their existing rights from what the collaboration may generate.
Julia | If a new invention results, naming the people who contributed is not necessarily the same as deciding which organization will own the resulting rights.
Ravi | Correct. [[Inventorship::Inventorship identifies qualifying contributors to a claimed invention and is distinct from ownership of the rights.]] and ownership are different legal questions. We should not resolve either casually in an email saying that every new idea belongs to the team.
Julia | The recipient wants to publish. Can the draft specify how review would work, including timing, without implying either immediate unrestricted publication or an unlimited veto?
Ravi | Agree a defined [[publication review::Publication review is the agreed process for examining proposed disclosure, with its purpose and timing specified.]] process with the relevant purpose, timing, and consequences. Do not assume immediate unrestricted publication or an unlimited veto when neither term has been settled.
Julia | They also asked whether access to the material means they can use our practical methods in a later unrelated project. That sounds broader than this evaluation.
Ravi | Clarify any [[know-how::Know-how concerns practical technical information whose permitted use may differ from possession of a material.]] being supplied and the authorized uses. Physical possession of a reference protein does not automatically settle rights in every method discussed alongside it.
Julia | Our team owns a related patent. Some colleagues think that means we can tell the partner there are no intellectual-property obstacles to any proposed use.
Ravi | Ownership does not itself establish [[freedom to operate::Freedom to operate concerns the proposed acts and relevant rights of others, not merely ownership of one's own patent.]]. Other rights may matter, and the review needs the actual activity, territory, and relevant circumstances before anyone makes a clearance statement.
Julia | Then our own patentability work and a third-party-rights review should not be presented as the same assessment. They answer different questions for the collaboration.
Ravi | Yes. Examine relevant [[third-party rights::Third-party rights are held outside these two partners and can remain relevant to the proposed activities.]] through appropriately scoped professional review. A right we hold is not a universal permission to practice every related technology or distribute every associated material.
Julia | I will hold shipment and send the exact assessment list and laboratory names for review. The teams agree on the science; the transfer terms still need resolution.
Ravi | That gives us a clear [[governing agreement::The governing agreement supplies the actual applicable terms for the authorized collaboration rather than an informal assumption.]] to finalize through the proper process. Once the terms and authorization are established, the team can act within that defined scope rather than rely on assumptions.''',
    transfer_title='Access to a file is not every right',
    transfer_setup='A partner may receive a confidential method summary for evaluation. No permission for commercial use or onward disclosure has been agreed in the supplied facts.',
    transfer='''Scientist: "The stated purpose is ___." | evaluation | The supplied permission concerns evaluating the confidential method summary.
Partner: "Commercial use is not established as ___." | permitted | The brief expressly says commercial-use permission has not been agreed.
Scientist: "Onward disclosure also remains ___." | unresolved | No onward-disclosure permission is supplied, so it cannot be assumed.
Partner: "We need the actual governing ___." | terms | The relevant permissions depend on the applicable agreement rather than access alone.''',
    rehearsal=["Read the transfer review. Distinguish the signed confidentiality agreement from the unfinished material-transfer terms.","Swap roles. Separate permitted use, onward transfer, publication review, and ownership; retain the unapproved shipment status.","Read the corrected file-access transfer. Keep evaluation permission distinct from commercial use and onward disclosure."]))

BOOK['units'].append(unit(
    title='Investor and Board Updates',
    scene='Six experiments, one unfinished milestone',
    skill='Connect completed work to a scientific funding criterion and explain a conditional cash-runway calculation.',
    brief='Program lead Daria and finance lead Miles prepare a fictional board update. Four binding experiments and two functional runs are complete. The agreed next funding criterion requires three consistent independent functional runs; the third is pending. Unrestricted cash is $12 million and the base-case net cash burn is $1.2 million per month. A proposed $0.3 million follow-up budget is not yet approved or included in that base case. The board needs milestone status and a bounded decision request, not a count presented as proof.',
    cast='Daria | Program lead\nMiles | Finance lead',
    culture=('A board update should connect evidence and choice', 'Senior audiences often ask whether a program is de-risked. Identify which uncertainty has been reduced and which criterion remains open. A clear request names the proposed work and resources without presenting a favorable experimental outcome or future funding as guaranteed.'),
    a='''Why is the funding criterion not yet met? | Only two of the required three independent functional runs are complete. | No experiments of any kind have been completed. | Four binding experiments automatically count as functional runs. | Cash balance alone determines the scientific result. | The agreed criterion requires three consistent functional runs, and the third remains pending.
What is the simple base-case runway at unchanged net burn? | Ten months | Twelve months | One month | One hundred months | Twelve million divided by one point two million per month equals ten months.
How should the $0.3 million proposal be described? | Additional proposed funding, not yet approved or included in the base case | Cash already spent and reflected in the base case | A guaranteed investment return | Proof that the functional criterion is met | The brief explicitly leaves the proposed budget unapproved and outside the current base case.''',
    vocabulary='''milestone criterion | The evidence or condition required to reach a defined project milestone. | specify the milestone criterion
readout | The reporting of results from a study or experiment. | schedule a data readout
evidence package | The organized results and supporting records used for a decision. | assemble the evidence package
go/no-go decision | A defined decision to continue, stop, or redirect a program. | support a go/no-go decision
scientific risk | Uncertainty about whether the underlying biological or technical premise will hold. | reduce scientific risk
execution risk | Uncertainty about delivering the planned work as intended. | manage execution risk
critical path | The sequence of dependent tasks determining the earliest completion point. | identify the critical path
dependency | An input or task that another activity relies on. | make dependencies explicit
board ask | The specific decision or support requested from the board. | state the board ask
resource allocation | Assignment of money, people, or capacity to defined work. | justify resource allocation
unrestricted cash | Cash available for use without the specified restrictions of restricted funds. | report unrestricted cash
net cash burn | Net cash outflow over a stated period. | calculate monthly net cash burn
gross cash burn | Total cash outflow before offsetting inflows over a stated period. | distinguish gross cash burn
cash runway | The estimated period before available cash is exhausted under stated assumptions. | estimate cash runway
run rate | A current rate projected over another period under stated assumptions. | qualify the run-rate estimate
base case | The central planning scenario used for comparison. | update the base case
downside case | A planning scenario with less favorable specified assumptions. | test the downside case
budget variance | The difference between planned and actual spending on the same basis. | explain a budget variance
contingent funding | Funding dependent on specified future conditions. | identify contingent funding
financing round | A defined transaction or process to raise capital. | prepare for a financing round
dilution | Reduction in an existing owner's proportional interest following additional equity issuance. | explain potential dilution
inflection point | A development event expected to materially change a program's position or perceived value. | define the proposed inflection point
milestone payment | A payment triggered by a specified achievement under an agreement. | verify milestone-payment conditions
decision record | A record of the decision, basis, conditions, and responsible parties. | maintain a decision record''',
    precision='Six completed experiments do not satisfy a criterion requiring three consistent independent functional runs when only two are complete. The category and quality of evidence matter. A milestone is not met merely because the activity count looks substantial.',
    precision_extra='The simple runway is $12 million divided by $1.2 million per month: ten months at unchanged net burn. This is a conditional illustration, not a forecast guarantee. New spending, timing, inflows, or restrictions require an updated cash model.',
    phrases='''Lead with the decision | We are asking for a bounded follow-up budget, not declaring the milestone complete.
Report the work | Four binding experiments and two functional runs are complete.
Name the criterion | The gate requires three consistent independent functional runs.
State the gap | The third functional run is pending.
Separate evidence types | Binding data support the program but do not replace the functional criterion.
Avoid total de-risking | One uncertainty may be reduced while other risks remain.
Connect the spend | The proposed budget supports the next defined evidence question.
State approval status | The additional $0.3 million has not yet been approved.
Show the runway basis | At unchanged net burn, twelve divided by one point two gives ten months.
Keep the model current | The new proposal is outside the current base case.
Separate cash and science | Available cash does not establish a successful scientific result.
Name the dependency | The funding decision depends on the evidence criterion, not only the calendar.
Use a downside case | Show what changes if the result or timing is less favorable.
Avoid a funding promise | A planned financing round is not cash already received.
Record the conditions | Capture the board's actual decision and any conditions.
Close with the next readout | Return with the third-run result and the updated cash implications.''',
    notes='''Completed | Name the work completed rather than imply every milestone is complete.
De-risked | Specify the risk reduced; do not imply that uncertainty disappeared.
Runway | State cash, burn basis, and assumptions.
Funded | Distinguish a proposal, approval, contractual commitment, and cash received.
Milestone | Use the agreed criterion, not a convenient substitute created for the update.
Base case | An unapproved new cost is not automatically already included.''',
    d='''Which opening is most decision-ready? | Two functional runs are complete; the third required by the funding criterion is pending, and we request $0.3 million for the defined follow-up. | Six experiments prove the milestone is met. | The program is completely de-risked because the slide is finished. | The cash balance guarantees a positive third result. | The opening connects actual evidence, the unmet criterion, and the specific proposed decision.
What makes the ten-month runway conditional? | It assumes unchanged net burn and the stated available cash basis. | It proves future funding will arrive. | It includes every unapproved future cost automatically. | It depends only on the number of experiments completed. | The arithmetic holds only under the cash and burn assumptions stated in the brief.
The board packet counts six completed experiments against the three-run gate. What is the reporting error? | It combines different evidence categories although the criterion specifies functional runs. | It understates the completed activity because six is fewer than three. | It treats the two functional runs as pending even though they are complete. | It excludes a third completed functional run that is already in the record. | Four binding experiments plus two functional runs is six activities, but only two match the specified category. The third functional run is still pending; a total count does not satisfy the gate.
What should happen if the new budget is approved? | Update the cash model for the actual spending assumptions and record the decision. | Keep calling it excluded from every forecast permanently. | Treat approval as proof of scientific success. | Add the budget amount to cash as though it were revenue. | An approved additional spend changes planning inputs without establishing the experimental outcome.''',
    dialogue='''Daria | The update opens with six experiments completed. That is accurate as an activity count, but I am concerned it makes the next funding milestone sound finished.
Miles | State the [[milestone criterion::The milestone criterion specifies three consistent independent functional runs rather than a total activity count.]] before the count. The agreed requirement is three consistent independent functional runs, and we currently have two with the third still pending.
Daria | Four of the six completed experiments are binding work. They support the program, but they do not replace the particular functional evidence required at this gate.
Miles | Exactly. The [[evidence package::The evidence package organizes the relevant results for the decision without treating unlike experiments as interchangeable.]] should separate those categories. The board needs to see which result addresses which criterion, not infer progress from a single large total.
Daria | We also need to revise the phrase fully de-risked. The completed work may reduce some uncertainty, but the pending functional result could still affect the direction.
Miles | Name the remaining [[scientific risk::Scientific risk concerns whether the biological or technical premise will hold, which completed activity alone cannot eliminate.]]. Do not turn progress into a claim that every uncertainty has disappeared, particularly when the agreed evidence condition remains open.
Daria | My request is the additional three-hundred-thousand-dollar budget for the defined follow-up. I am not asking for an unlimited commitment to every later development stage.
Miles | Make that the [[board ask::The board ask is the specific bounded funding decision being requested, distinct from reporting completed work.]]. State the work it supports and its approval status. At present the amount is proposed, not approved or already incorporated into the base case.
Daria | The finance panel shows twelve million dollars of unrestricted cash and net burn of one point two million a month. That gives ten months under unchanged assumptions.
Miles | Yes, as a simple [[cash runway::Cash runway estimates the duration of available cash under the stated net-burn assumptions.]] illustration. Put the assumptions next to the number so it is not heard as a guarantee that every future spending plan is already covered.
Daria | Show the proposed three hundred thousand separately. What happens to the forecast if the board approves it, given that the base case excludes it?
Miles | Update the [[base case::The base case is the current central planning scenario, which excludes the unapproved additional proposal here.]] if the board approves new spending, using the actual timing assumptions. Approval changes the plan; it does not make the original calculation timeless.
Daria | There is also a proposed financing round later. We should keep that distinct from cash already available rather than use it to make the runway look longer today.
Miles | Correct. Treat any [[contingent funding::Contingent funding depends on future conditions and is not equivalent to cash already received.]] according to its actual status. A plan to raise money is not a receipt, and an unmet scientific condition should remain visible.
Daria | For the schedule, the third functional run is the key unresolved item. The board should understand how its outcome connects to the next program decision.
Miles | Identify that [[dependency::A dependency identifies the evidence or task on which the next decision relies.]] explicitly. The calendar alone does not satisfy an evidence gate, and a completed run still needs its result evaluated against the criterion.
Daria | We can also show what happens if the result does not support continuation or if the timing moves. That makes the spending choice more concrete.
Miles | Use a stated [[downside case::A downside case shows the consequences of specified less-favorable assumptions without treating them as established outcomes.]] without presenting it as a prediction. The purpose is to show which assumptions change the resource choice and when the board would revisit it.
Daria | I will put the third functional run and the budget request on the decision slide. Please add when the board will see the result and updated cash position.
Miles | Capture the actual approval or deferral in the [[decision record::The decision record preserves what the board actually decided and any conditions attached to it.]]. Keep funding authorization, experiment completion, and a successful scientific result distinct, even on the same slide.''',
    transfer_title='New spending changes the assumptions',
    transfer_setup='A fictional program has $9 million of available cash and a steady net burn of $1.5 million per month. A new project cost is proposed but excluded from that base case.',
    transfer='''Finance lead: "The simple base-case runway is ___ months." | six | Nine million divided by one point five million per month equals six months.
Program lead: "That assumes an unchanged net ___." | burn | The calculation holds only at the stated net cash-outflow rate.
Finance lead: "The new project cost is currently ___." | excluded | The briefing states that the proposed cost is outside the base case.
Program lead: "Approval would require an updated cash ___." | model | Adding approved spending requires the planning assumptions and resulting cash estimate to be updated.''',
    rehearsal=["Read the board update. Report four binding experiments and two functional runs, with the third functional run pending.","Swap roles. State ten months at the base-case burn and the unapproved $0.3 million outside that model.","Read the corrected cash transfer. Use nine divided by one point five: six months before any new project cost."]))

BOOK['units'].append(unit(
    title='Partnering and Business Development',
    scene='Define the collaboration before granting exclusivity',
    skill='Clarify the scope and conditions of a proposed partnership without confusing a discussion, an option, and a granted license.',
    brief='Biotech partnering lead Nina meets prospective partner Tomas. The proposed first stage is a six-month nonclinical evaluation of two fictional targets, T2 and T5. Tomas requests worldwide exclusive rights across all platform applications before the collaboration scope is defined. No license, option, budget, or governance terms are approved. Nina is authorized to discuss a narrower proposal, not grant rights. They must identify the scope, evidence, decision process, and unresolved commercial terms for a reviewed term sheet.',
    cast='Nina | Biotech partnering lead\nTomas | Prospective partner',
    culture=('Explore interests before accepting the broad wording', 'A request for exclusivity may reflect a concern about investing resources while a competitor receives the same opportunity. Acknowledge that concern, then clarify the protected activity and duration. A narrower proposal can keep negotiation moving without implying that rights have already been granted.'),
    a='''What is the proposed first-stage work? | A six-month nonclinical evaluation of T2 and T5 | Worldwide commercial development of every application | An approved clinical trial across all diseases | Permanent assignment of the whole platform | The stated initial proposal is limited to two targets and a six-month nonclinical evaluation.
What authority does Nina have? | Discuss a narrower proposal, not grant rights | Execute every exclusive license immediately | Approve all governance and budget terms | Assign unrelated third-party patents | The brief expressly limits Nina to discussion rather than granting rights.
What remains unapproved? | License, option, budget, and governance terms | The fact that Tomas requested exclusivity | The identity of the two proposed targets | The proposed six-month evaluation duration | The briefing identifies those substantive agreement terms as not approved.''',
    vocabulary='''partnering thesis | The argument for why a collaboration could create value for both parties. | articulate the partnering thesis
strategic fit | Alignment between the collaboration and the parties' capabilities or goals. | assess strategic fit
evaluation license | Permission limited to a defined assessment purpose under agreed terms. | scope an evaluation license
option agreement | An agreement giving a defined opportunity to obtain specified rights on stated conditions. | negotiate an option agreement
option exercise | The act of using an option according to its agreed conditions. | define option-exercise requirements
license grant | The clause or act conveying specified permission under a license. | delimit the license grant
exclusivity scope | The defined activities, rights, territory, and period covered by exclusivity. | narrow the exclusivity scope
field restriction | A limitation to specified applications or uses. | define a field restriction
territorial restriction | A geographic limit on the relevant rights or activities. | clarify territorial restrictions
reserved rights | Rights explicitly retained rather than granted to the other party. | identify reserved rights
sublicensing | Granting another party rights under authority provided by a license. | address sublicensing permission
diligence obligation | An agreed requirement to make specified efforts or progress. | negotiate diligence obligations
development milestone | A defined development achievement linked to review or agreed consequences. | specify development milestones
upfront payment | Consideration due at an initial agreed point in a transaction. | distinguish an upfront payment
royalty | A payment calculated on an agreed basis for use of licensed rights. | define the royalty basis
milestone consideration | Payment or value contingent on a specified contractual achievement. | clarify milestone consideration
cost sharing | Allocation of specified expenses between collaborating parties. | agree cost sharing
joint steering committee | A joint body with defined oversight or coordination responsibilities. | establish a joint steering committee
governance | The agreed structures and rules for overseeing a collaboration. | define collaboration governance
decision right | Authority to make a specified decision. | allocate decision rights
termination right | A contractual ability to end an arrangement under defined conditions. | review termination rights
rights reversion | Return or cessation of specified granted rights under agreed conditions. | define rights reversion
data room | An organized controlled-access collection of information for review. | maintain the data room
term sheet | A document summarizing proposed principal deal terms, with legal effect depending on its wording. | prepare a reviewed term sheet''',
    precision='A proposal to discuss exclusivity does not grant it. A term sheet is not automatically entirely nonbinding; its effect depends on the actual wording and law. An option to obtain rights is also distinct from an exercised option or an existing license grant.',
    precision_extra='Scope includes more than the word exclusive: identify the rights, field, territory, duration, conditions, and retained uses. Governance also needs actual decision authority. A committee name alone does not establish who may approve a budget, change the program, or license an asset.',
    phrases='''Acknowledge the interest | I understand that you want protection for the resources you would commit.
Define the first stage | The proposed evaluation covers T2 and T5 for six months.
Challenge the breadth | All platform applications is broader than the work currently proposed.
Separate discussion from grant | I can discuss scope, but I cannot grant rights in this meeting.
Ask about the field | Which specific applications need exclusivity for the evaluation?
Clarify duration | What period would the proposed restriction cover?
Protect retained uses | We need to identify the rights and activities each party retains.
Distinguish the option | A future licensing option is not the same as a present commercial license.
Define the trigger | Which evidence and conditions would permit an option to be exercised?
Connect commitment | Any exclusivity proposal needs appropriately defined obligations and review.
Clarify funding | Which costs would each party bear during the evaluation?
Ask about governance | Who would have authority over scope, budget, and continuation decisions?
Avoid assumed agreement | Those terms are still open and subject to the required review.
Limit the information | Provide data-room access within the agreed confidentiality and use conditions.
Check the document | Identify which term-sheet provisions, if any, are intended to bind the parties.
Close the meeting | We will prepare a narrower proposal without representing that rights are already granted.''',
    notes='''Exclusive | Incomplete without the rights, activity, place, time, and conditions.
Option versus license | The ability to obtain rights later is not the same as already holding them.
Partner | A commercial relationship label does not define decision authority.
Worldwide | Geographic breadth does not specify the field of use.
Milestone payment | The trigger comes from actual agreed terms, not any favorable laboratory result.
Agreed to discuss | A process commitment should not be recorded as a completed rights grant.''',
    d='''Which counterproposal fits Nina's authority? | Prepare a reviewed proposal limited to the two-target, six-month evaluation and explicitly unresolved terms. | Grant worldwide exclusive rights to all platform applications immediately. | Assign every future invention without review. | Treat the request as an executed license. | Nina may discuss and prepare a narrower proposal but is not authorized to grant rights.
Why distinguish an option from a license? | An option concerns a defined opportunity to obtain rights, while a license grants specified permission. | Every option already grants all commercial rights. | A license is always merely a meeting invitation. | An option removes the need to define any conditions. | The two arrangements confer different positions, and the actual terms determine their scope and exercise.
A draft names a joint steering committee but gives it no powers. Which question addresses that gap? | Who may approve scope changes, budgets, and continuation decisions? | Which targets are included in the six-month evaluation? | Which territories would the proposed exclusive rights cover? | Which material will be placed in the controlled data room? | Governance requires actual decision authority and rules. Targets, territory, and data access are separate scope questions and do not establish what the committee may decide.
What should the meeting record say? | The parties will prepare a narrower proposal; no rights grant is approved. | Worldwide exclusivity is effective because Tomas requested it. | Every term-sheet provision is automatically nonbinding. | The unapproved budget has already been paid. | The record must preserve discussion status and the absence of an authorized grant.''',
    dialogue='''Tomas | Before we commit resources, we would like worldwide exclusive rights across the platform. We do not want to fund the work while a competitor receives the same opportunity.
Nina | I understand the concern, but the [[exclusivity scope::Exclusivity scope defines what is protected and cannot be inferred from the broad word exclusive alone.]] you describe is wider than the proposed six-month evaluation of T2 and T5. Let us identify the activity you need protected.
Tomas | Our immediate interest is those two targets. We also see possible applications beyond them, and we would prefer not to renegotiate every time the opportunity develops.
Nina | A defined [[field restriction::A field restriction limits the proposed rights to specified applications rather than every possible platform use.]] could keep the first stage aligned with the actual work. Broader applications require their own review; I cannot grant platform-wide rights in this meeting.
Tomas | Could we start with evaluation rights and secure a route to a later commercial license if the results meet agreed criteria?
Nina | We can discuss an [[option agreement::An option agreement could provide a defined opportunity to obtain rights later under specified conditions.]] as a proposal. It would need clear scope, conditions, and approval; a possible future option is not already a commercial license.
Tomas | We would need to know what evidence qualifies and when we must decide. Otherwise the option could be too uncertain to support a meaningful investment.
Nina | Define the [[option exercise::Option exercise is the use of the option in accordance with its specified timing and conditions.]] requirements alongside the evidence criteria. We should also distinguish scientific success from the separate commercial and legal conditions for obtaining rights.
Tomas | What happens to your own research during the evaluation? We do not necessarily need to stop unrelated platform work, but we need to understand competing activity.
Nina | Identify the [[reserved rights::Reserved rights are the uses or permissions retained rather than included in the proposed grant.]] and proposed restrictions explicitly. Neither side should infer a platform-wide freeze from a limited evaluation, nor assume an exception that the terms do not state.
Tomas | We can bring specialist capability and funding for the evaluation, but the division of costs has not been discussed. That needs to be part of the same proposal.
Nina | Yes, specify [[cost sharing::Cost sharing allocates the defined evaluation expenses and cannot be assumed from general interest in partnering.]] for the actual work. A broad expression of interest should not conceal who is paying for which activities or approving additional spending.
Tomas | If we seek some exclusivity, you will want assurance that the work moves forward. We should discuss what commitments would accompany that protection.
Nina | Appropriate [[diligence obligation::A diligence obligation defines the agreed efforts or progress expected rather than leaving exclusivity without operational commitments.]] terms can address that, subject to review. The proposal should state the expected progress and consequences rather than rely on a general promise to try.
Tomas | Could a joint committee handle routine technical decisions? I do not want a small adjustment to require another executive negotiation every time.
Nina | A [[joint steering committee::A joint steering committee can coordinate the collaboration, but its authority must be specified in the agreement.]] can help if its authority is defined. We still need to assign decisions about scope, budget, continuation, and matters reserved for authorized signatories.
Tomas | We should also describe what happens if the evaluation ends without a later license. Materials, data access, and any temporary restrictions need a clear position.
Nina | Address [[rights reversion::Rights reversion concerns the return or cessation of specified rights under agreed end conditions.]] and the relevant end-of-project obligations in the reviewed proposal. Do not assume that a temporary arrangement continues indefinitely because nobody discussed its end.
Tomas | I will tell our team we are preparing a two-target proposal, not announcing worldwide exclusivity. Send me the open points so we can assign reviewers on our side.
Nina | Exactly. We will prepare a [[term sheet::A term sheet summarizes proposed principal terms whose binding effect must be explicitly reviewed.]] covering the two-target evaluation and open issues, with its intended legal effect reviewed. No license, option, or exclusivity grant is approved by this discussion alone.''',
    transfer_title='An option is not an exercised grant',
    transfer_setup='Two partners discuss a possible option to negotiate a future license after a defined evaluation. No option is signed and no license is granted. A meeting note says commercial rights acquired.',
    transfer='''Partner: "The possible option is still under ___." | discussion | The briefing states that the option is being discussed and is not signed.
Lead: "No option has been ___." | signed | The supplied facts explicitly deny a signed option agreement.
Partner: "No commercial license has been ___." | granted | The briefing states that no license grant has occurred.
Lead: "The meeting note must preserve that ___." | status | The note should reflect discussion rather than falsely report acquired commercial rights.''',
    rehearsal=["Read the partnering exchange. Preserve two targets, six months, and Nina's authority to discuss but not grant rights.","Swap roles. Separate a possible option, its future exercise, and a current license; keep the terms unapproved.","Read the corrected meeting-note transfer. No option signed and no commercial license granted are the supplied statuses."]))
