"""Original learner-book content for higher education and research."""
from books.authoring import unit

BOOK = dict(
    slug='higher-education-research',
    title='Higher Education and Research English',
    cover_label='ENGLISH FOR HIGHER EDUCATION AND RESEARCH',
    cover_title='Higher Education\n& Research',
    cover_size=30,
    tagline='Define the question. Defend the evidence.',
    audience='For researchers, doctoral students, research coordinators, and academic collaborators.',
    map_intro='Eight research conversations: sharpen a study question, bound a grant aim, investigate a lab discrepancy, clarify data reuse, agree credit, respond to review, document a dataset, and answer a conference challenge.',
    notes_title='Strong claims need clear boundaries',
    notes_intro='Academic confidence comes from showing exactly what a study can support. Connect the question to the design, explain the evidence, and distinguish a promising next step from a result already established.',
    field_notes=[
        ('Define what the study measures', 'Population, outcome, comparison, and timing change the meaning of a question. A broad word such as works can conceal several different claims.', '"We measured course completion in this cohort, not the program\'s causal effect on all students."'),
        ('Make disagreement inspectable', 'Point to the protocol, data, criterion, or manuscript passage at issue. A direct challenge can be a request for evidence rather than a personal attack.', '"The exposure time changed between runs; we need to check its contribution to the discrepancy."'),
        ('Keep permission separate from possibility', 'Having data, software access, or a technically feasible plan does not settle whether the proposed use is authorized.', '"We can describe the proposed analysis, but the required reuse determination is still pending."'),
        ('Respond at the right scale', 'Answer the narrow question first, then state the limitation and next test. Avoid turning a pilot, one sample, or a successful rerun into universal proof.', '"This result supports the reported observation in our sample; broader testing is still needed."')],
    scope_note='All cases and figures are fictional. This book teaches research communication, not statistical, clinical, or legal advice or ethics approval. Follow the relevant institution, funder, jurisdiction, and journal requirements; obtain required review before conducting or changing research.',
    sources=[
        dict(title='National Center for Complementary and Integrative Health. Pilot Studies: Common Uses and Misuses.', url='https://www.nccih.nih.gov/grants/pilot-studies-common-uses-and-misuses', note='Background on feasibility pilots and limits on efficacy claims. The learning-study milestones in this book are original fictional criteria, not a funder requirement.', checked='30 September 2026'),
        dict(title='U.S. Office for Human Research Protections. Coded Private Information or Biospecimens Used in Research.', url='https://www.hhs.gov/ohrp/coded-private-information-or-biospecimens-used-research.html', note='U.S. guidance on coded information and authorized determinations for secondary research. The exercises supply a fictional local review requirement and do not determine exemption status.', checked='30 September 2026'),
        dict(title='International Committee of Medical Journal Editors. Defining the Role of Authors and Contributors.', url='https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html', note='Background for the authorship case, which explicitly adopts these criteria. Authorship rules and ordering conventions differ among journals and disciplines.', checked='30 September 2026'),
        dict(title='National Institutes of Health. Writing a Data Management and Sharing Plan.', url='https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/writing-dms-plan', note='Background for data documentation, methods, tools, and appropriate sharing. The environmental dataset and laboratory records are original teaching cases.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Research Questions and Study Design',
    scene='What exactly would it mean for tutoring to work?',
    skill='Specify a research question and distinguish an observed association from a causal effect.',
    brief='Doctoral researcher Imani and supervisor Leon revise a proposal asking whether optional tutoring works. Available records cover first-year students in one introductory biology course for one semester: 32 of 40 tutoring participants completed the course, compared with 36 of 60 nonparticipants. Tutoring was self-selected, not randomly assigned. The groups may differ in prior preparation or motivation, which these records do not measure. The immediate analysis can describe the association with completion in this cohort. A future causal study would need a suitable design; it has not been conducted.',
    cast='Imani | Doctoral researcher\nLeon | Research supervisor',
    culture=('Narrowing a claim strengthens the question', 'A supervisor who challenges the word works may be asking for a testable question, not rejecting the project. Respond with the population, measured outcome, and comparison. Keep the broader ambition visible as a future question instead of presenting it as an answer from the current records.'),
    a='''What is the completion rate among tutoring participants? | 80% | 60% | 32% | 125% | Thirty-two completers divided by forty participants equals eighty percent.
What is the difference between the two completion rates? | Twenty percentage points | Twenty percent relative | Eight percentage points | Forty percentage points | Participant completion is eighty percent and nonparticipant completion is sixty percent, a twenty-point difference.
Why is a causal claim unsupported here? | Tutoring was self-selected and relevant group differences are unmeasured. | Every observational record is useless. | The course has no defined outcome. | Both groups have identical completion rates. | Self-selection and unmeasured differences prevent the observed contrast from isolating tutoring's causal effect.''',
    vocabulary='''research question | A specific question a study is designed to answer. | refine a research question
target population | The group to which a research question refers. | define the target population
study sample | The observed group included in the study. | describe the study sample
cohort | A defined group observed over a specified period. | follow a student cohort
outcome variable | The measured result of interest. | specify the outcome variable
exposure | A condition or experience whose relationship with an outcome is studied. | define the exposure
comparison group | The group used as a reference for a contrast. | identify the comparison group
observational study | A study observing conditions without assigning the exposure. | describe an observational study
self-selection | Entry into a group through participants' own choices. | account for self-selection
random assignment | Allocation to study conditions using a random process. | distinguish random assignment
random sampling | Selection of units from a population by a random process. | distinguish random sampling
association | An observed relationship between variables. | report an association
causal effect | A change attributable to an intervention or exposure. | estimate a causal effect
confounder | A factor that can distort the exposure-outcome relationship. | address potential confounders
baseline difference | A group difference present before the studied exposure or outcome. | examine baseline differences
operational definition | A precise specification of how a concept is measured. | state an operational definition
completion rate | The proportion meeting the defined completion outcome. | calculate the completion rate
denominator | The base count used in a proportion. | state the denominator
percentage-point difference | The arithmetic difference between percentages. | report a percentage-point difference
relative difference | A difference expressed in relation to a reference value. | distinguish a relative difference
internal validity | The credibility of the study's inference within its setting. | assess internal validity
external validity | The extent to which findings apply beyond the studied setting. | discuss external validity
estimand | The precise quantity a study seeks to estimate. | define the estimand
study protocol | A documented plan for the study's conduct and analysis. | revise the study protocol''',
    precision='32/40 is 80%; 36/60 is 60%. The difference is 20 percentage points. Relative to 60%, the difference is approximately 33.3%, not 20%. Neither calculation removes the design limitation created by self-selection.',
    precision_extra='Random assignment concerns allocation to conditions; random sampling concerns selection into the sample. They address different questions. The current case has self-selected tutoring participation, and no broader representativeness or causal design is established.',
    phrases='''Clarify the broad verb | "What outcome would count as working?"
Specify the population | "The records cover first-year students in this course."
Set the period | "The observation window is one semester."
Name the outcome | "We are measuring course completion."
Identify exposure | "Tutoring participation was optional."
State the first rate | "Thirty-two of forty participants completed, or 80%."
State the comparison | "Thirty-six of sixty nonparticipants completed, or 60%."
Express the contrast | "That is a 20-percentage-point difference."
Qualify the inference | "This is an observed association, not an isolated causal effect."
Name selection | "Students chose whether to participate."
Identify missing information | "Prior preparation and motivation are not measured here."
Avoid inventing an explanation | "Those are possible group differences, not confirmed causes."
Bound the population claim | "The current result concerns this course cohort."
Separate future work | "A causal question needs a suitable future design."
Preserve the useful result | "The descriptive contrast remains worth reporting."
Close the revision | "The proposal should match its question to the available evidence."''',
    notes='''Works | Needs a specified outcome, population, comparison, and time.
Completed | Requires a consistent completion definition for both groups.
Higher | Describes direction without establishing cause.
Associated with | Does not mean caused by.
Random | State whether it concerns sampling or assignment.
May differ | Marks a possible explanation, not a finding.''',
    d='''Which headline fits the available evidence? | Tutoring participation was associated with higher completion in this course cohort. | Tutoring caused every participant to complete. | Tutoring improves all university outcomes everywhere. | The two groups had equal completion. | The first headline describes the observed contrast while respecting self-selection and the limited setting.
Which question is still unresolved? | Whether tutoring caused the completion difference | Whether 32 of 40 equals 80% | Whether the course records span one semester | Whether participation was optional | The current observational records do not isolate the causal contribution of tutoring.
Which statement about possible confounding is accurate? | Prior preparation or motivation may differ, but these records do not establish those differences. | Motivation is proved to explain the entire contrast. | Self-selection makes confounding impossible. | A percentage-point calculation adjusts for preparation. | The brief identifies plausible unmeasured factors, not verified explanations or adjusted estimates.
Which design distinction is correct? | Random assignment allocates conditions; random sampling selects sample members. | Random assignment guarantees every population is represented. | Random sampling automatically makes an optional program randomized. | Both terms mean the same operation. | The two random processes concern different stages and do not substitute for one another.''',
    dialogue='''Leon | The proposal asks whether tutoring works. That sounds important, but what outcome would answer the question, and whose experience are we actually observing?
Imani | I need a sharper [[research question::The research question must specify what is being measured and for whom rather than relying on the broad word works.]]. The available records concern first-year students in one introductory biology course during one semester. They record tutoring participation and course completion.
Leon | Then completion, rather than examination performance or long-term retention, is the outcome. We should not let the proposal switch among those meanings without noticing.
Imani | Agreed. The [[outcome variable::The outcome variable is course completion, not every possible academic benefit that tutoring might produce.]] is completion as recorded for that semester. I will use the same definition for participants and nonparticipants, so the comparison does not change meaning between groups.
Leon | Walk me through the counts before we discuss the interpretation. Percentages can conceal different group sizes, especially when the audience sees only a headline.
Imani | The participant [[denominator::The denominator is forty tutoring participants; pairing it with thirty-two completers yields the eighty-percent completion rate.]] is forty, with thirty-two completing. That is eighty percent. Among sixty nonparticipants, thirty-six completed, giving sixty percent for the comparison group.
Leon | So the rates differ by twenty percentage points. Saying a twenty-percent increase would not be the same calculation, because that uses a relative base.
Imani | Correct. The [[percentage-point difference::The percentage-point difference subtracts sixty percent from eighty percent, producing twenty points rather than a twenty-percent relative change.]] is twenty. Relative to sixty percent, the difference is about thirty-three point three percent. Neither phrasing, by itself, explains why the groups differ.
Leon | Were students allocated to tutoring, or did they choose it? That matters more for the causal claim than how confidently we present the percentages.
Imani | Participation involved [[self-selection::Self-selection means students chose tutoring, so the groups may differ in ways other than the tutoring exposure.]]. Students chose whether to attend. The records do not measure prior preparation or motivation, and either could differ between groups. We have not established those differences.
Leon | Then the claim that tutoring caused the higher completion rate is stronger than the design supports. We can still report the observed relationship accurately.
Imani | I will call it an [[association::Association describes the observed relationship without claiming that the current design isolates a causal effect.]] with completion in this cohort. That preserves the finding without treating possible unmeasured group differences as either irrelevant or already proved explanations.
Leon | A colleague proposed solving the problem by randomly sampling more records from the same optional program. Would that make tutoring itself randomly assigned?
Imani | No. [[Random assignment::Random assignment allocates study conditions; selecting additional records randomly would not change the original self-selected tutoring exposure.]] concerns allocation to conditions. Random sampling concerns which people enter the sample. A larger randomly sampled record set would not retroactively randomize the tutoring decision.
Leon | Good. We should also avoid implying that one course at one institution establishes what happens for all students in every subject and setting.
Imani | That is an [[external validity::External validity concerns application beyond the studied course and cohort, which the supplied records do not establish.]] question. The current description stays with this course and semester. Broader applicability needs evidence across the relevant settings, not just a less cautious title.
Leon | We can keep the long-term ambition of studying causation, provided the proposal separates that future work from the analysis we can conduct now.
Imani | The future [[causal effect::A causal effect is the contribution attributable to tutoring, which requires a suitable design beyond the current descriptive comparison.]] question needs a suitable design and explicit assumptions. We should discuss that design as a proposed next step, not imply that it has already been implemented.
Leon | Revise the objective to describe completion by tutoring participation in this cohort. Then make the design limitation visible in the abstract as well.
Imani | I will update the [[study protocol::The study protocol should record the precise question, definitions, and analysis boundaries so later reporting follows the same plan.]] and the proposal wording together. The useful result is a bounded comparison with clear counts, while the causal and broader-population questions remain open.''',
    transfer_title='A rate difference is not a randomized effect',
    transfer_setup='In a self-selected workshop cohort, 18 of 30 attendees and 20 of 40 nonattendees completed a task. Prior experience was not measured. The records cover one course only.',
    transfer='''Researcher: "The attendee completion rate is ___ percent." | 60 | Eighteen completers divided by thirty attendees equals sixty percent.
Supervisor: "The nonattendee rate is ___ percent." | 50 | Twenty completers divided by forty nonattendees equals fifty percent.
Researcher: "The difference is ___ percentage points." | 10 | Sixty percent minus fifty percent is ten percentage points.
Supervisor: "The contrast establishes an association, not a ___." | causal effect | Self-selection and unmeasured differences prevent this comparison from isolating causation.'''))

BOOK['units'].append(unit(
    title='Grant Proposals and Specific Aims',
    scene='A feasibility pilot cannot promise a definitive answer',
    skill='Align a grant aim with pilot scope and interpret predefined feasibility milestones.',
    brief='Research lead Sora and grants adviser Ben revise a proposal for a small learning-study pilot. The draft promises to establish that a new workshop improves academic attainment. The actual pilot tests recruitment and follow-up procedures, not efficacy. A completed preparatory pilot recruited 30 students in four weeks and retained 24 at follow-up. The team had specified two local progression criteria: recruit at least 30 in four weeks and retain at least 85% of those recruited. Both must be met for automatic progression to the next planning stage. Only recruitment passed; a redesign or explicit review is needed.',
    cast='Sora | Research lead\nBen | Grants adviser',
    culture=('Ambition and deliverables are different', 'A proposal can explain a significant long-term problem without promising that a small pilot will solve it. State the pilot deliverable precisely and show how it informs a later study. Credible limits help reviewers understand what their funding would actually produce.'),
    a='''What is the pilot designed to assess? | Recruitment and follow-up feasibility | Definitive improvement in attainment | Universal workshop safety | All future funding decisions | The brief defines the pilot's scope as procedures, not efficacy or universal conclusions.
What was the observed retention rate? | 80% | 85% | 24% | 125% | Twenty-four retained students out of thirty recruited equals eighty percent.
Did both local progression criteria pass? | No; recruitment passed and retention did not. | Yes, because thirty students were recruited. | No; retention passed and recruitment did not. | Yes, because eighty and eighty-five are equivalent. | Recruitment met its threshold, but eighty-percent retention fell below the specified eighty-five percent.''',
    vocabulary='''specific aim | A focused objective a proposed study will address. | refine a specific aim
long-term goal | The broader result a research program ultimately seeks. | state the long-term goal
pilot study | A small-scale study testing procedures for later work. | design a feasibility pilot
feasibility | Whether proposed methods can be carried out practicably. | assess feasibility
efficacy | The effect of an intervention under the relevant controlled conditions. | distinguish efficacy from feasibility
recruitment | Bringing eligible participants into a study. | monitor recruitment
recruitment window | The period allowed for enrolling participants. | define the recruitment window
retention | Continued participation through a defined study point. | calculate follow-up retention
follow-up | A later observation or contact after the initial stage. | complete follow-up
attrition | Loss of participants from later study observation. | report participant attrition
progression criterion | A predefined condition for moving to a next stage. | apply progression criteria
milestone | A specified achievement used to assess progress. | set a measurable milestone
deliverable | A defined output the project will provide. | identify the pilot deliverable
study objective | The particular purpose of a study. | align the study objective
rationale | The reasoning that justifies the proposed work. | strengthen the study rationale
significance | Why the research question or gap matters. | explain research significance
innovation | A meaningful new feature of an approach. | describe the innovation precisely
approach | The planned methods for addressing the aims. | evaluate the proposed approach
scope | The boundaries of the work and claims. | keep the aims within scope
sample size | The number of units or participants included. | justify the sample size
precision | The degree of uncertainty around an estimate. | discuss estimate precision
definitive study | A study designed to provide a robust answer to the main question. | plan a definitive study
contingency | A planned response if assumptions or milestones fail. | specify a contingency
funding decision | A determination about financial support. | distinguish a funding decision''',
    precision='24/30 is 80% retention, below the local 85% criterion. With 30 recruited participants, at least 26 retained would reach or exceed 85%; 25 would be only about 83.3%. Do not round a failed threshold into a pass.',
    precision_extra='The two criteria are conjunctive: both are required for automatic progression. Recruitment success does not cancel the retention shortfall. Failing this local rule calls for redesign or review; it does not prove the workshop has no educational effect.',
    phrases='''Separate ambition from aim | "The long-term goal is broader than this pilot deliverable."
State the pilot purpose | "This study tests recruitment and follow-up procedures."
Remove an overclaim | "It is not designed to establish efficacy."
Name the recruitment target | "The local target was 30 students in four weeks."
Report recruitment | "That target was met."
State the retention base | "Retention is calculated among the 30 recruited students."
Give the result | "Twenty-four were retained, which is 80%."
Apply the threshold | "That is below the predefined 85% criterion."
Keep both conditions | "Automatic progression requires both criteria."
Avoid convenient rounding | "Eighty percent cannot be reported as meeting 85%."
Explain the next step | "The shortfall needs redesign or explicit review."
Preserve uncertainty | "This does not establish that the workshop is ineffective."
Specify the output | "The deliverable is a revised, tested study procedure."
Retain significance | "The larger educational question remains important."
Bound funding language | "Meeting a local milestone would not guarantee an award."
Close the aim | "The proposal should promise what this design can deliver."''',
    notes='''Pilot | State whether it tests feasibility rather than definitive effects.
At least | Includes the threshold and values above it.
Retained | Needs a specified follow-up point and denominator.
Both | One successful criterion is insufficient.
Automatic progression | A local planning rule, not a funding guarantee.
Did not meet | Does not establish that the intervention has no effect.''',
    d='''Which specific aim matches the supplied pilot? | Assess recruitment and follow-up procedures to refine a later study. | Establish improved attainment for all students. | Prove every future trial will succeed. | Guarantee an external funding award. | The first aim matches the procedural feasibility purpose and keeps later efficacy work separate.
How many retained participants would meet at least 85% of thirty? | Twenty-six | Twenty-four | Twenty-five | Twenty | Twenty-six out of thirty exceeds eighty-five percent, whereas twenty-five is below it.
What is the correct progression statement? | Recruitment passed, but retention requires redesign or explicit review before progression. | One passed milestone automatically overrides the other. | Retention should be rounded up to the target. | The target can be changed silently after seeing the result. | Both criteria were required, and the retention shortfall prevents automatic progression under that rule.
What does the retention result say about efficacy? | It does not establish whether the workshop improves attainment. | It proves the workshop never works. | It proves a large effect. | It directly measures examination improvement. | Retention describes follow-up feasibility, not the workshop's effect on academic attainment.''',
    dialogue='''Ben | The draft says this pilot will establish that the workshop improves attainment. Is that really the question the small study was designed to answer?
Sora | No. The [[specific aim::The specific aim must describe the work this study can address, which is procedural feasibility rather than definitive attainment improvement.]] should concern recruitment and follow-up procedures. Improving attainment is our long-term goal, but the pilot does not provide a definitive test of that outcome.
Ben | We can keep the wider educational problem in the significance section. Reviewers still need a concrete account of what this grant would deliver now.
Sora | The [[deliverable::The deliverable is the practical output of the pilot, here a refined and tested procedure for later research.]] is a refined study procedure, informed by recruitment and follow-up evidence. That is useful preparation for a later study, without pretending the larger question has already been answered.
Ben | The preparatory work enrolled thirty students in four weeks. Remind me whether that matches the target set before the results were available.
Sora | It meets the [[recruitment::Recruitment concerns bringing students into the study; thirty within four weeks meets the supplied local recruitment threshold.]] criterion of at least thirty within four weeks. We should report that success, while checking the other criterion separately instead of treating enrollment as the whole feasibility assessment.
Ben | At follow-up, twenty-four of the thirty students remained. The draft calls that good retention, but the adjective hides the numerical comparison with our rule.
Sora | The [[retention::Retention is twenty-four of thirty recruited students, or eighty percent, at the specified follow-up point.]] rate is eighty percent. We had set at least eighty-five percent, so this criterion was not met. The denominator is all thirty recruited students.
Ben | Would twenty-five retained students meet the threshold? We need to translate the percentage into a whole-participant count.
Sora | The [[progression criterion::The progression criterion requires at least eighty-five percent, which with thirty recruited students needs at least twenty-six retained.]] requires at least twenty-six retained out of thirty. Twenty-five would be approximately eighty-three point three percent, still below the threshold. We should apply the stated rule accurately.
Ben | Our planning document requires both milestones for automatic progression. Recruitment passed, but it cannot compensate for the retention shortfall under that rule.
Sora | We need a [[contingency::A contingency addresses the failed milestone through redesign or explicit review rather than ignoring or silently changing the predefined rule.]] such as redesign or explicit review. We should explain what the shortfall means for planning, not silently lower the criterion because we prefer a positive result.
Ben | That does not mean the workshop is educationally ineffective. The missing follow-up information concerns the study procedure, and the pilot was not an efficacy trial.
Sora | Correct. [[Feasibility::Feasibility concerns whether the proposed methods can be carried out, which is distinct from the intervention's effect on attainment.]] and efficacy are different questions. The result tells us the retention procedure missed our local target; it does not establish whether the workshop improves attainment.
Ben | I will also remove the sentence promising a future award once the pilot milestones pass. Our internal progression rule cannot bind a funder's decision.
Sora | A [[funding decision::A funding decision is made by the relevant funder and is not guaranteed by satisfying an internal planning milestone.]] remains separate. Even successful local milestones would inform a proposal, not guarantee financial support. We should state the value of the evidence without predicting an external decision.
Ben | The grant can remain ambitious: a clear problem, a bounded pilot, and a reasoned route toward a definitive study.
Sora | Yes. Keep the [[scope::Scope defines what the pilot will do and claim, preventing the long-term research ambition from becoming an unsupported present promise.]] explicit. We can describe the future question and explain how improving follow-up supports it, while keeping the current work focused on procedures and practical uncertainty.
Ben | I will revise the aims, summary, and milestone table together. They should all say recruitment passed, retention did not, and the next planning step requires review.
Sora | That gives us a consistent [[rationale::The rationale explains why the bounded pilot work remains valuable while acknowledging the evidence and unresolved milestone.]] for the proposed work. We are asking for support to resolve a concrete procedural problem, not claiming that a small pilot has settled the educational effect.''',
    transfer_title='Two conditions, not one',
    transfer_setup='A local pilot rule requires 20 recruits within three weeks and at least 90% retention. Twenty are recruited on time, but only 17 reach follow-up. Both conditions are needed for automatic progression.',
    transfer='''Researcher: "The recruitment condition was ___." | met | Twenty students were recruited within the stated three-week window.
Adviser: "Retention was ___ percent." | 85 | Seventeen divided by twenty equals eighty-five percent, below ninety percent.
Researcher: "At least ___ retained students were required." | 18 | Eighteen out of twenty equals the required ninety-percent retention threshold.
Adviser: "Automatic progression is ___ under the stated rule." | not supported | Only recruitment passed, while the rule requires both conditions to be satisfied.'''))


BOOK['units'].append(unit(
    title='Lab Meetings and Data Challenges',
    scene='The repeated run was not performed the same way',
    skill='Present an experimental discrepancy, disclose a method change, and propose a controlled check without editing the record to fit a preferred result.',
    brief='Research associate Alex and lab lead Priya compare two nonclinical fluorescence measurements of the same reference material. Run A reports 120 arbitrary units and Run B 180. Instrument files reveal exposure times of ten seconds for A and twenty for B. The summary lab notes had omitted this change. The team has not tested whether it explains the entire difference, and signal response may not be proportional to exposure. They must retain both raw records, add a dated correction to the notes, and plan a repeat with documented matched settings. No misconduct finding has been made.',
    cast='Alex | Research associate\nPriya | Lab lead',
    culture=('Disclose a discrepancy without assigning blame', 'A lab meeting should make uncertainty inspectable. Name the observed result, the method difference, and the missing evidence. Correct documentation transparently without accusing a colleague of misconduct or presenting an untested explanation as the established cause.'),
    a='''What changed between the runs? | Exposure time increased from ten to twenty seconds. | The notes document identical exposure times. | Run A used no reference material. | Run B's result was 120 units. | Instrument files establish different exposure times for the two recorded measurements.
What is not yet established? | Whether exposure time explains the entire signal difference | Whether the reported values are 120 and 180 | Whether a method change was omitted | Whether raw records exist | The method difference is known, but its full contribution to the result has not been tested.
How should the documentation be corrected? | Add a dated correction while preserving the original record. | Backdate a replacement note as if nothing changed. | Delete the less convenient raw result. | Announce proven misconduct immediately. | Transparent correction preserves provenance without concealing the original omission or inventing a misconduct finding.''',
    vocabulary='''lab meeting | A discussion of research progress, methods, and results. | present at a lab meeting
experimental run | A recorded execution of a measurement or experiment. | compare experimental runs
reference material | Material used as a stable point of comparison. | measure the reference material
raw data | Original recorded observations before later processing. | preserve raw data
processed result | A value produced after defined analysis or transformation. | trace a processed result
arbitrary unit | A relative measurement unit defined by the measurement system. | report arbitrary units
exposure time | The duration used for signal acquisition in this case. | document exposure time
instrument setting | A parameter controlling measurement behavior. | match instrument settings
protocol version | The identified revision of a study procedure. | record the protocol version
method deviation | A departure from the intended or comparison procedure. | document a method deviation
batch effect | A systematic difference associated with processing groups. | investigate a batch effect
technical replicate | A repeated measurement used to assess measurement variability. | compare technical replicates
biological replicate | An independently derived biological sample or unit. | distinguish biological replicates
signal intensity | The magnitude of the detected measurement signal. | compare signal intensity
linear response | A proportional relationship over a specified range. | verify a linear response
saturation | A measurement ceiling beyond which more input is not represented proportionally. | check for signal saturation
normalization | Adjustment to a defined reference or scale. | justify normalization
measurement variability | Variation arising across repeated measurements. | quantify measurement variability
controlled comparison | A comparison with relevant conditions deliberately held consistent. | plan a controlled comparison
lab notebook | The record of research methods, observations, and changes. | maintain the lab notebook
dated correction | A visible amendment recording when a correction was made. | add a dated correction
provenance | The origin and history of data or records. | preserve data provenance
hypothesis | A proposed explanation or prediction to be tested. | test a methodological hypothesis
reproducibility check | A check that specified materials and methods yield consistent outputs. | document a reproducibility check''',
    precision='Run B is 60 arbitrary units higher, a 50% increase relative to Run A. Exposure doubled, but the signal increased by only half. Do not divide or scale signals as though proportional response had been established.',
    precision_extra='A recorded method difference is a candidate explanation, not proof of the entire cause. Retain both results and document the correction. Repeating measurements of the same material does not create new independent biological samples.',
    phrases='''Open with the result | "Run A gave 120 units; Run B gave 180."
Name the verified change | "The instrument files show different exposure times."
State the durations | "A used ten seconds and B used twenty."
Disclose the omission | "The summary notes did not record that change."
Preserve the records | "Keep both raw files and their original settings."
Correct transparently | "Add a dated correction to the notebook."
Avoid blame | "This is a documentation gap, not a misconduct finding."
Limit the explanation | "The change may contribute, but we have not isolated its effect."
Question a shortcut | "Proportional scaling has not been validated."
Check the response | "We need to examine linearity and possible saturation."
Plan the comparison | "Repeat with documented matched settings."
Keep replication precise | "These are repeated measurements of the same material."
Track processing | "State every transformation applied to the raw values."
Separate observation and cause | "The signal changed; the complete cause is unresolved."
Make the action traceable | "Link the repeat to the protocol version and instrument files."
Close honestly | "We have a testable explanation, not a resolved discrepancy."''',
    notes='''Repeated | Does not guarantee identical conditions.
Raw | Keep the original record separate from later transformations.
May explain | A hypothesis, not a completed causal test.
Twice the exposure | Does not establish twice the signal.
Correction | Must remain distinguishable from the original entry.
Independent sample | Not created by measuring the same material again.''',
    d='''Which sentence accurately reports the signal contrast? | Run B is 60 units, or 50%, higher than Run A. | Run B doubled from 120 to 240. | Run A is 180 units. | The signal difference is exactly zero. | One hundred eighty minus one hundred twenty is sixty, which is half of the original value.
Why is dividing Run B by two not justified as a correction? | Proportional signal response to exposure has not been established. | Division is never used in research. | The exposure times are identical. | Arbitrary units mean the records have no information. | Scaling assumes a relationship that the brief explicitly says has not been verified.
What is the next useful comparison? | A documented repeat with matched settings and preserved raw records | A repeat with undisclosed settings | Deleting Run B | Selecting whichever result supports the preferred theory | Matching and documenting conditions helps examine the discrepancy without concealing existing evidence.
Which conclusion should be avoided? | The omitted note proves research misconduct. | The summary record needs correction. | Exposure differs between runs. | The complete cause remains unresolved. | An omission requires examination and correction but does not by itself establish a misconduct finding.''',
    dialogue='''Priya | The slide calls Run B a repeat, but its signal is one hundred eighty units rather than one hundred twenty. Were the measurement conditions actually matched?
Alex | The [[instrument setting::The instrument setting difference is established by the files: exposure was ten seconds in one run and twenty in the other.]] for exposure changed. The files show ten seconds for Run A and twenty for Run B. That difference was omitted from the summary notes.
Priya | Preserve both files, including the unexpected result, before correcting the notes. We need the original evidence intact.
Alex | I have retained the [[raw data::Raw data preserves the original observations and settings, allowing later checks without losing an inconvenient result.]] and the original metadata. I will not replace either measurement with an adjusted value. Any later processing must remain distinguishable from what the instrument originally recorded.
Priya | The exposure doubled, so somebody suggested halving the second signal and treating that as the comparable result. Have we established a proportional response?
Alex | No. A [[linear response::A linear response would justify proportional scaling only within a verified range; that relationship is not established here.]] has not been verified over these settings. The signal changed from one hundred twenty to one hundred eighty, not to two hundred forty, so simple scaling needs justification.
Priya | Check whether the detector reaches a ceiling or other conditions differed. The exposure change is a lead, not a complete explanation.
Alex | We can check for [[saturation::Saturation could make the signal response nonproportional, but it is only a possibility to investigate in this case.]] and review other recorded conditions. I will describe these as possible contributors, not confirmed causes. We have not isolated the exposure effect or explained the full discrepancy.
Priya | How will the correction show when we discovered the omitted setting, without hiding the original note?
Alex | I will add a [[dated correction::A dated correction records the discovery transparently while preserving the original note and the history of the omission.]] linked to the instrument files. It will state the actual exposure for each run and when the omission was identified, without backdating the new entry.
Priya | Good. That also avoids implying misconduct before anything has been investigated. The immediate issue is an incomplete method record and a result needing explanation.
Alex | Preserving [[provenance::Provenance records the origin and history of the data and corrections, making the discrepancy traceable without prejudging responsibility.]] makes that distinction visible. We can show what was measured, what the notes originally said, and what we subsequently learned, without concealing the gap or assigning unsupported blame.
Priya | For the next measurement, we need documented matched settings and a clear plan. Simply running the instrument again would not address the comparison problem.
Alex | I will propose a [[controlled comparison::A controlled comparison holds relevant settings consistent so the team can investigate the discrepancy more meaningfully.]] using matched settings and retained raw files. We should specify the protocol version and checks in advance, so another undocumented change does not create the same uncertainty.
Priya | These measurements use the same reference material. They are not additional independent biological samples.
Alex | They are [[technical replicates::Technical replicates repeat measurements on the material to examine measurement variability; they do not add independent biological samples.]], not new biological replicates. The distinction matters because repeating a measurement can inform measurement variability without increasing the number of independently sampled biological units.
Priya | The slide should report the observed difference as sixty units, fifty percent relative to Run A. It must not say exposure caused exactly that increase.
Alex | I will separate the observation from the [[hypothesis::The hypothesis proposes that the method change contributes to the discrepancy, but it still requires testing rather than being reported as established.]]. The documented change is a plausible contributor. Its role remains to be tested, and other sources of variation have not been ruled out.
Priya | Bring the corrected record, both raw files, and the matched-settings plan to the next meeting. We can then decide what the evidence supports.
Alex | I will label the planned work a [[reproducibility check::The reproducibility check is planned work to examine consistent results under specified conditions, not a completed resolution of the discrepancy.]], not a resolved discrepancy. The current conclusion is limited: the results differ, the exposure settings differ, and the complete explanation is still open.''',
    transfer_title='Preserve the change history',
    transfer_setup='Two readings of the same reference material used different documented gain settings. The summary omitted the change. No causal check has been completed. Both original files remain available.',
    transfer='''Researcher: "The gain change is a verified method ___." | difference | The instrument records establish a setting difference, not merely a suspected change.
Lead: "Its causal contribution remains ___." | untested | No check has isolated the effect of the setting change.
Researcher: "The notebook needs a ___." | dated correction | A dated correction transparently records the omission without rewriting the past.
Lead: "Both original files should be ___." | preserved | Retaining original records allows later verification and avoids selective removal of evidence.'''))

BOOK['units'].append(unit(
    title='Research Ethics and Human Subjects',
    scene='Possessing the data is not permission for a new use',
    skill='Describe a secondary-use proposal and seek an authorized ethics determination without assuming coded data is anonymous.',
    brief='Researcher Tessa wants to reuse coded interviews from a student-stress study for a new employment-discrimination question. Her research team can access the key linking codes to participants. The original approval and consent materials have not been checked against the new purpose. The fictional institution requires its designated ethics office to determine the permitted route before new analysis or sharing begins. No determination, amendment, waiver, or new consent has been granted. Tessa can prepare the proposal and gather existing documents, but must not begin the proposed reuse or promise collaborators access.',
    cast='Tessa | Researcher\nOmar | Research ethics coordinator',
    culture=('A review boundary is not a scientific rejection', 'An ethics coordinator may support the question while withholding permission for the proposed use. Explain the purpose and access conditions accurately. Do not turn a discussion about a possible route into a claim that approval, exemption, or participant agreement has already been obtained.'),
    a='''Why are the coded interviews not automatically anonymous to this team? | The team can access the code-to-participant key. | All coded data are public. | Interviews never contain private information. | The new topic removes the original identities. | The accessible linking key allows the team to connect codes with participants.
Who determines the permitted route under the supplied local rule? | The designated ethics office | Any collaborator who wants the data | The researcher acting alone | The software vendor | The fictional institutional procedure assigns the determination to its designated ethics office.
What can Tessa do now? | Prepare the proposal and gather the existing approval and consent documents. | Start the new analysis immediately. | Promise unrestricted collaborator access. | Declare a waiver has been granted. | Preparatory documentation is permitted, while the new use and sharing must await the required determination.''',
    vocabulary='''secondary use | Using previously collected material for a further purpose. | propose a secondary use
human-subjects research | Research involving people or qualifying information under applicable rules. | assess human-subjects research status
ethics review | Examination of a research proposal's ethical acceptability and requirements. | request ethics review
institutional review board | A U.S. committee reviewing covered human-subjects research. | consult the institutional review board
research ethics committee | A body reviewing research ethics under its remit. | seek research ethics committee review
informed consent | A process supporting an informed, voluntary participation decision. | review informed-consent materials
consent scope | The activities and uses covered by the relevant consent. | check the consent scope
approval scope | The work permitted by a particular authorization. | verify the approval scope
protocol amendment | A proposed change to an approved research protocol. | submit a protocol amendment
waiver | An authorized exception to a specified requirement. | distinguish a requested waiver
exemption determination | An authorized decision about an applicable exemption category. | obtain an exemption determination
coded data | Data using codes with a separate identity-linking key. | describe coded data accurately
linking key | Information connecting study codes to identities. | restrict access to the linking key
identifiability | The possibility of connecting information with a person. | assess identifiability
de-identification | Removing or reducing identifying information under a specified method. | document de-identification
confidentiality | Protection against unauthorized information disclosure. | maintain confidentiality
data-use agreement | Terms governing permitted access and use. | establish a data-use agreement
authorized determination | A decision made by the designated competent authority. | await an authorized determination
recontact | Contacting a participant again after earlier involvement. | assess a recontact proposal
participant information | Material explaining a study to potential participants. | review participant information
voluntariness | Freedom to choose participation without improper pressure. | protect voluntariness
access restriction | A limit on who may obtain or use information. | apply access restrictions
purpose change | A shift from the original use to a different objective. | describe the purpose change
review status | The current stage or outcome of a review request. | state the review status''',
    precision='Coded does not automatically mean anonymous. Here, the team can access a linking key, so the identity connection matters. The new question and access arrangements must be described accurately to the designated reviewer.',
    precision_extra='A request for an amendment, waiver, or exemption is not a granted determination. The applicable route depends on the study and rules. This scenario supplies a local hold on new analysis and sharing until the ethics office determines that route.',
    phrases='''Describe the new question | "The proposed reuse concerns employment discrimination."
Identify the original purpose | "The interviews were collected for a student-stress study."
State the key access | "Our team can access the code-to-participant key."
Avoid an anonymity claim | "Coding does not make these data anonymous to us."
Check the documents | "We need the original approval and consent materials."
Clarify the scope | "The new purpose has not been assessed against those documents."
Name the authority | "The designated ethics office determines the permitted route."
State the hold | "Do not start the new analysis or sharing yet."
Keep requests conditional | "An amendment may be needed; none has been approved."
Avoid inventing a waiver | "No waiver or new consent has been granted."
Prepare useful material | "We can describe the question, fields, recipients, and safeguards."
Separate preparation from reuse | "Gathering documents is not approval to analyze the interviews."
Limit a collaborator promise | "Access is subject to the authorized determination."
Preserve confidentiality | "Keep the current access restrictions in place."
Report status precisely | "The proposal is awaiting review, not approved."
Close with the next step | "Submit the complete proposal and wait for the required decision."''',
    notes='''Coded | A linking key may still allow identification.
Anonymous | Do not use without a justified assessment of the actual situation.
Existing approval | May not cover a new question or sharing arrangement.
May require | A possibility, not a determination already made.
Requested | Not granted.
Preparing a proposal | Distinct from conducting the proposed new research.''',
    d='''Which description should be sent to the ethics office? | Coded interviews with a linking key accessible to the research team | Anonymous data with no possible identity connection | Public information requiring no consideration | Newly consented data for every conceivable purpose | The first description accurately reports the team's actual ability to link codes with people.
What does the old approval establish about this new purpose? | Nothing conclusive until its scope is checked against the proposal. | Automatic approval for all later questions | A granted waiver of every requirement | Permission to promise external access immediately | The original materials have not been reviewed against the new use, so their coverage cannot be assumed.
Which message to a collaborator is accurate? | "The proposed access awaits the designated ethics determination." | "Approval is guaranteed because we have the files." | "All participants have already agreed to this new question." | "A requested exemption is the same as a granted one." | The first message states the pending status without inventing approval or participant agreement.
Which preparatory step respects the supplied boundary? | Gather documents and describe the proposed use without beginning analysis or sharing. | Run the analysis first and seek retrospective permission. | Remove the key label but keep unrestricted key access. | Email the full interviews to collaborators now. | The local procedure permits proposal preparation while holding the proposed research use and disclosure.''',
    dialogue='''Tessa | We already have the interview files, and the new employment-discrimination question is promising. Can I begin analyzing them while we check the old paperwork?
Omar | The local [[review status::The review status is unresolved: the required determination has not been made, so the new analysis cannot start under the supplied rule.]] does not permit that yet. The designated ethics office must determine the route before new analysis or sharing. You can prepare the proposal and gather the existing documents.
Tessa | The interviews came from our student-stress study. They use participant codes rather than names, so I initially described them as anonymous in the draft.
Omar | Describe the [[coded data::Coded data uses substitute labels but may remain identifiable through a linking key, which this team can access.]] accurately. Does the research team have access to the key connecting the codes with participants? That access changes what the reviewer needs to know about identifiability.
Tessa | Yes, the team can access the key. The draft should state that plainly rather than imply there is no possible connection with the people interviewed.
Omar | Exactly. The [[linking key::The linking key connects the interview codes to participant identities and must be disclosed in the description of access conditions.]] must be included in the access description. Coding alone does not establish anonymity to your team, and changing the label would not change the underlying arrangement.
Tessa | I have the original participant information and consent documents, but I have not checked whether the employment question is within what they describe.
Omar | Review the [[consent scope::Consent scope concerns the uses covered by the relevant participant materials, which have not been checked against the new purpose.]] alongside the original approval. We should not assume that agreement to the student-stress study covers every later question or sharing arrangement.
Tessa | The new topic is related to student experience, but related does not necessarily mean it is covered. I should explain the difference in the proposal.
Omar | Yes, state the [[purpose change::The purpose change distinguishes the proposed employment-discrimination question from the original student-stress research and requires assessment.]] clearly. The reviewer needs the actual new question, intended information, recipients, and safeguards, not a broad assurance that everything is still generally about students.
Tessa | Would this be an amendment, a new submission, or an exemption? Collaborators keep asking me which route applies, and I do not want to guess.
Omar | That requires an [[authorized determination::The authorized determination is made by the designated ethics office, not inferred by collaborators or the researcher from possession of the files.]]. The designated office will assess the proposal under the applicable rules. We cannot announce the route before that assessment has been made.
Tessa | I can say an amendment might be needed, but none is approved. The draft wrongly implies approval is routine.
Omar | Keep any [[protocol amendment::A protocol amendment is a proposed change to approved work and must not be described as already authorized when none has been granted.]] conditional. A plausible route is not a completed decision. Likewise, no waiver or new consent has been granted, so neither should appear as an established fact.
Tessa | One collaborator wants the files now to check what variables are available. Can I promise access after simply replacing the names in the documentation?
Omar | No. The current [[access restriction::The access restriction remains in force while review is pending; changing labels does not authorize collaborator access or disclosure.]] remains. Describe the proposed fields and access needs without sharing the interviews. Do not promise access that depends on a decision outside your authority.
Tessa | I will gather the approval, consent materials, key-access details, and proposed analysis description. That gives the office enough context to assess the new use.
Omar | Include the proposed [[data-use agreement::A data-use agreement can describe intended access and use conditions, but it does not replace the required ethics determination.]] arrangements if collaboration is planned. Such terms may be relevant, but they do not replace the required ethics determination or establish participant consent by themselves.
Tessa | My update will say the proposal is being prepared, no new analysis has begun, and collaborator access remains subject to the designated review.
Omar | That accurately describes the [[secondary use::Secondary use is the proposed reuse for a new research purpose, which remains pending rather than already permitted.]]. Keep preparation separate from conducting the new work. Once the authorized decision is recorded, follow its conditions rather than treating review as unlimited permission.''',
    transfer_title='A pending route is not a permission',
    transfer_setup='A researcher proposes a new use of coded survey data. The team can access the linking key. The institution requires a designated-office determination before new analysis. The request has been sent but no decision issued.',
    transfer='''Researcher: "The files are coded, not automatically ___." | anonymous | The accessible linking key means coding does not establish anonymity to the team.
Coordinator: "The proposed use still awaits an authorized ___." | determination | Sending the request does not complete the required institutional decision.
Researcher: "New analysis must remain ___." | on hold | The supplied local rule prohibits starting before the designated decision.
Coordinator: "We can accurately report that review is ___." | pending | No decision has been issued, so pending is the supported status.'''))


BOOK['units'].append(unit(
    title='Authorship, Collaboration, and Credit',
    scene='Credit follows contributions, not job titles',
    skill='Discuss authorship eligibility, outstanding responsibilities, and author order without granting or denying credit by status.',
    brief='Research fellow Harper and project lead Marta discuss a manuscript whose target journal uses ICMJE authorship criteria: substantive research contribution, intellectual drafting or review, final-version approval, and accountability. All four are required. Harper designed and performed the main analysis but has not yet been invited to review the manuscript or approve the final version. Professor Nolan obtained funding only. The team has not agreed author order or documented contributions. Harper must have a genuine opportunity to complete the remaining responsibilities; funding alone does not establish Nolan\'s authorship. No final author list or order is settled.',
    cast='Harper | Research fellow\nMarta | Project lead',
    culture=('Discuss contribution and responsibility together', 'Academic hierarchy can make credit conversations difficult. Refer to the agreed publication criteria and a factual contribution record. Do not frame authorship as a personal favor, and do not exclude a substantive contributor by withholding the chance to fulfill remaining responsibilities.'),
    a='''What substantive contribution has Harper made? | Designed and performed the main analysis | Obtained funding only | Already approved an unseen final manuscript | Determined author order alone | The brief records Harper's analysis design and execution as the substantive contribution.
Does funding alone establish Nolan's authorship under the stated criteria? | No | Yes, regardless of other work | Yes, if the title is professor | Yes, if no contribution record exists | The adopted criteria require more than obtaining funding alone.
What should happen before the author list is finalized? | Give Harper a genuine opportunity to review, approve, and accept the relevant responsibilities. | Exclude Harper because no invitation was sent. | Guarantee Harper first position immediately. | List everyone who attended a meeting. | A substantive contributor should not be excluded by denying opportunities to fulfill the remaining criteria.''',
    vocabulary='''authorship | Credited responsibility for a published scholarly work. | establish authorship eligibility
contributorship | A description of what each person did. | document contributorship
byline | The author names listed on a publication. | finalize the byline
author order | The sequence in which authors are listed. | discuss author order
substantive contribution | Significant intellectual or research work on the project. | recognize a substantive contribution
conceptualization | Development of the study's ideas or research goals. | describe conceptualization
methodology | Development or design of research methods. | record methodology contributions
formal analysis | Application of analytical methods to study material or data. | credit formal analysis
data curation | Organizing and maintaining data for use. | describe data curation
investigation | Conducting the research or collecting relevant evidence. | record investigation work
funding acquisition | Obtaining financial support for a project. | acknowledge funding acquisition
supervision | Oversight or guidance of research work. | distinguish supervision from authorship
critical review | Intellectual examination of a manuscript's content. | contribute critical review
final approval | Agreement to the version intended for publication. | obtain final approval
accountability | Responsibility for addressing the work's accuracy and integrity. | accept accountability
corresponding author | The author managing the journal communication role. | identify the corresponding author
acknowledgment | Recognition of contributions outside the author byline. | agree an acknowledgment
contribution statement | A record describing each contributor's work. | prepare a contribution statement
authorship criteria | The applicable conditions for being listed as an author. | apply authorship criteria
honorary authorship | Listing someone without the required authorship basis. | avoid honorary authorship
omitted contributor | A contributor whose relevant work is not properly recognized. | address an omitted contributor
collaboration agreement | Recorded expectations for joint work. | revisit the collaboration agreement
dispute resolution | A process for addressing unresolved disagreement. | use the dispute-resolution process
manuscript version | An identified revision of a paper. | circulate the final manuscript version''',
    precision='Authorship eligibility and author order are separate decisions. A substantive analysis contribution matters, but the supplied journal requires all four responsibilities. Give Harper the opportunity to complete them; do not invent a final approval or a guaranteed first position.',
    precision_extra='A contribution statement records work but does not automatically settle authorship. Under this case\'s adopted criteria, funding alone is insufficient. Apply the actual journal and institutional rules, since conventions differ by field.',
    phrases='''Open factually | "Let us document what each collaborator contributed."
Name the analytical work | "Harper designed and performed the main analysis."
Use the agreed standard | "The target journal requires all four authorship criteria."
Identify what remains | "The manuscript review and final approval have not happened yet."
Provide a real opportunity | "Harper needs the manuscript and time to review it."
Avoid exclusion by omission | "Not receiving an invitation should not become a reason to deny credit."
Separate funding | "Funding acquisition alone does not establish authorship here."
Keep titles out of the test | "Job title is not the criterion."
Distinguish ordering | "Eligibility does not settle author order."
Avoid a premature promise | "No final position has been agreed."
Make credit visible | "Record contributions accurately in the statement."
Keep responsibility explicit | "Authorship includes accountability, not only recognition."
Identify the version | "Approval must refer to the final manuscript version."
Coordinate communication | "The corresponding-author role should be agreed."
Handle disagreement | "Use the institutional process if the group cannot resolve the dispute."
Close before submission | "Settle contributions, responsibilities, and the author list before submitting."''',
    notes='''Contributed | Specify the actual work rather than relying on a title.
Eligible | Must be assessed against the applicable criteria.
First author | An ordering decision, not automatic from one criterion.
Corresponding | A communication role, not necessarily the first-listed author.
Approved | Requires a real decision about an identified version.
Acknowledged | Recognition distinct from inclusion in the byline.''',
    d='''Which statement about Harper is supported? | Harper has a substantive analysis contribution and outstanding authorship responsibilities. | Harper has already approved the final version. | Harper did no relevant research work. | Harper must automatically be first author. | The analysis is documented, while review, final approval, and related responsibilities remain to be completed.
Which action would unfairly block completion of the criteria? | Withholding the manuscript and then citing lack of review as a reason for exclusion | Circulating the manuscript for substantive review | Recording the analysis contribution | Discussing accountability explicitly | The contributor cannot fulfill review responsibilities if the group denies the opportunity to do so.
What does Nolan's funding-only role establish? | A contribution to record, but not sufficient authorship under the adopted criteria | Automatic first authorship | Final approval by every collaborator | Proof that Harper's analysis is irrelevant | Funding is a real contribution but does not alone meet the journal's stated authorship requirements.
What remains unresolved after identifying a substantive contribution? | Completion of the remaining responsibilities and agreement on the author list and order | Whether the paper has a funding source | Whether all titles are identical | Whether the analysis ever occurred | Substantive contribution is only part of the process, and the brief leaves final authorship decisions unsettled.''',
    dialogue='''Harper | My name was missing from yesterday's draft author list. I designed and performed the main analysis, but nobody discussed credit with me.
Marta | We should start with a [[contribution statement::A contribution statement records the actual work performed, providing a factual basis for the credit discussion.]]. Your analytical work must be recorded accurately. The list is not final, and an informal draft should not substitute for a proper discussion with the collaborators.
Harper | Nobody sent me the manuscript. I need to check whether the methods and interpretation describe my work correctly.
Marta | You need a genuine opportunity for [[critical review::Critical review is an intellectual examination of the manuscript, which Harper should be able to undertake rather than being excluded for not receiving it.]]. I will circulate the manuscript and arrange time for your response. We should not withhold that opportunity and then cite its absence against you.
Harper | The journal uses ICMJE criteria, so I understand that doing the analysis is not the only responsibility. What still needs to happen before submission?
Marta | Beyond the substantive work and intellectual review, we need [[final approval::Final approval concerns the identified publication version and cannot be assumed before Harper has seen and agreed to it.]] of the publication version and agreement on accountability. Those are real responsibilities, not boxes we can mark on someone's behalf.
Harper | I will review the full paper and discuss the analysis. Please do not claim my approval before that happens.
Marta | Agreed. [[Accountability::Accountability connects authorship with responsibility for addressing accuracy and integrity questions, not merely receiving credit.]] must be understood and accepted. We will record the status honestly and identify outstanding steps, rather than inventing agreement to meet the submission timetable.
Harper | Professor Nolan is listed already, but his contribution so far was funding, without the other responsibilities.
Marta | We should record [[funding acquisition::Funding acquisition is a contribution to recognize, but by itself does not meet the adopted journal's authorship criteria.]] accurately too. Under the adopted criteria, that alone does not establish authorship. His title should neither replace the criteria nor prevent a respectful discussion of his actual contribution.
Harper | If I complete the remaining responsibilities, does the main analysis automatically make me first author? Different collaborators seem to have assumed different ordering conventions.
Marta | We must discuss [[author order::Author order is a separate collective decision and is not automatically determined by identifying one substantive contribution.]] separately. The criteria establish eligibility, not a universal ordering formula. We need a transparent conversation about the project and the journal's conventions, without promising a position prematurely.
Harper | That conversation should include the people who collected and curated the data. I do not want my concern resolved by overlooking somebody else's work.
Marta | Yes. Accurate [[contributorship::Contributorship describes each person's work and helps the group avoid overlooking relevant contributions while assessing the author list.]] requires the whole project's contribution record. We should not decide credit solely through the loudest objection, personal seniority, or who happened to see the draft first.
Harper | Who will communicate with the journal? People sometimes describe that role as though it always means first author.
Marta | The [[corresponding author::The corresponding author handles journal communications, a role distinct from a guaranteed first position in the byline.]] role should be agreed explicitly. It concerns communication and associated submission responsibilities. It does not automatically determine first position, and it cannot resolve an unsettled authorship dispute by itself.
Harper | If the group still cannot agree after reviewing contributions and responsibilities, we need a fair route forward rather than submitting an unresolved list.
Marta | Use the institutional [[dispute resolution::Dispute resolution provides a process for unresolved authorship disagreement rather than treating submission or hierarchy as a substitute for agreement.]] process if necessary. We should document the issue and seek the appropriate assistance. A deadline does not justify bypassing a substantive disagreement about credit.
Harper | For now, please circulate the manuscript, record the analysis contribution, and arrange a group discussion. I will review the content before giving any final approval.
Marta | Then we can finalize the [[byline::The byline is the eventual list of authors, which should reflect resolved eligibility and agreed responsibilities rather than the current informal draft.]] on an accurate basis before submission. No final list or order is settled today; the next step is to complete the review and resolve the outstanding decisions.''',
    transfer_title='An invitation is not an approval',
    transfer_setup='A journal uses the same four criteria. A collaborator made a substantive methods contribution and has just received the manuscript for review. No final approval or accountability agreement is yet recorded, and author order is undecided.',
    transfer='''Lead: "The methods work is a substantive ___." | contribution | The supplied methods work satisfies the stated substantive-contribution element.
Collaborator: "Receiving the manuscript gives me an opportunity for ___." | critical review | Circulation enables review but does not mean that intellectual review has already occurred.
Lead: "Final approval remains ___." | outstanding | The brief states that no final approval has yet been recorded.
Collaborator: "Eligibility alone does not settle ___." | author order | The ordering decision remains separate and explicitly unresolved in this case.'''))

BOOK['units'].append(unit(
    title='Peer Review and Revision Responses',
    scene='Revise the claim, not the observed result',
    skill='Respond to a valid reviewer criticism with a precise revision and traceable manuscript locations.',
    brief='Authors Mei and Luca respond to a reviewer of a fictional study involving 60 volunteer students at one campus. The study measured self-reported confidence after one workshop, with a mean of 7.1 on a ten-point scale. There was no baseline measurement, comparison group, or direct learning test. The manuscript nevertheless says the workshop improves learning for all adults. The authors agree to remove that claim from the abstract and conclusion, report the observed confidence in the studied sample, and explain the design limits. No new data or reanalysis has been performed.',
    cast='Mei | Corresponding author\nLuca | Coauthor',
    culture=('Agreement can be specific and professional', 'A reviewer response need not defend every original sentence. Acknowledge the valid point, say exactly what changed, and identify where it changed. Do not claim a limitation has been solved merely because the revised text now describes it honestly.'),
    a='''What did the study directly measure? | Self-reported confidence after one workshop | Improvement from a baseline learning test | Long-term attainment in all adults | A randomized treatment effect | The measured outcome was post-workshop confidence, not demonstrated learning or change.
Which original claim goes beyond the evidence? | The workshop improves learning for all adults. | Sixty volunteer students participated at one campus. | The mean confidence rating was 7.1 out of ten. | No comparison group was included. | The original claim substitutes learning for confidence and extends beyond the study population and design.
What has been done for this revision? | Wording is being corrected; no new data or reanalysis has occurred. | A randomized trial has been completed. | Every adult population has been sampled. | The reported mean has been replaced by a more impressive number. | The brief permits a reporting correction and explicitly states no new data or reanalysis.''',
    vocabulary='''peer review | Expert evaluation of scholarly work before or after publication. | respond to peer review
reviewer comment | A point raised by a manuscript evaluator. | address a reviewer comment
response letter | The document explaining replies and revisions. | prepare a response letter
point-by-point response | A reply organized against each review issue. | provide a point-by-point response
revision | A change to a manuscript or associated material. | document the revision
tracked changes | Visible marking of edits between document versions. | supply tracked changes
revised manuscript | The updated version submitted for consideration. | check the revised manuscript
abstract | A concise summary of a scholarly work. | revise the abstract
conclusion | The manuscript's final interpretation or takeaway. | narrow the conclusion
claim | An assertion about what the evidence establishes. | qualify a claim
overgeneralization | Extending a conclusion beyond its support. | remove an overgeneralization
sampling frame | The source population from which a sample is selected. | describe the sampling frame
volunteer sample | Participants who chose to take part. | acknowledge the volunteer sample
single-site study | Research conducted at one location. | state the single-site limitation
self-report | Information supplied by participants about themselves. | distinguish self-report from direct measurement
post-only measure | An outcome recorded after an event without a baseline measure. | interpret a post-only measure
baseline measure | An observation collected before the relevant intervention or period. | identify the missing baseline measure
comparison condition | A reference condition for evaluating a contrast. | specify a comparison condition
construct | The concept a measure is intended to represent. | identify the measured construct
learning assessment | A task directly assessing relevant learning. | distinguish a learning assessment
limitation | A feature restricting interpretation or application. | state the study limitation
reanalysis | A new analysis of existing data. | distinguish revision from reanalysis
page-and-line reference | A precise locator for manuscript text. | provide page-and-line references
editorial decision | A journal editor's determination about the manuscript. | await the editorial decision''',
    precision='A post-workshop confidence mean describes a measured state, not improvement from baseline. Confidence and demonstrated learning are also different constructs. Changing the claim can correct reporting without altering the observed 7.1 mean.',
    precision_extra='The volunteer, single-campus sample limits broad application. An honest limitation statement does not repair the design or guarantee acceptance. Cite locations in the actual revised version, not stale page and line numbers from an earlier draft.',
    phrases='''Acknowledge the point | "We agree that the original claim exceeded the design."
Identify the measured construct | "We measured self-reported confidence, not demonstrated learning."
State the population | "The sample comprised 60 volunteers at one campus."
Keep the observation | "The observed mean remains 7.1 out of ten."
Remove an unsupported change | "Without a baseline, we cannot claim improvement."
Remove a causal claim | "There was no comparison group to support that inference."
Bound generalization | "The result should not be stated for all adults."
Describe the revision | "We have narrowed the abstract and conclusion."
Make the location traceable | "The response identifies the revised page and lines."
Avoid inventing work | "No new data collection or reanalysis was performed."
Separate honesty from repair | "The limitation is now explicit, not eliminated."
Answer the comment | "The revised wording reports the observation in the studied sample."
Check consistency | "The same claim boundary appears throughout the manuscript."
Use a clean response | "We state the change and its reason directly."
Respect the decision | "The editor will assess the revised submission."
Close the issue | "The response and manuscript now describe the same evidence."''',
    notes='''Improves | A change or effect claim requiring appropriate evidence.
Confidence | Not interchangeable with measured learning.
Volunteers | A sample feature relevant to interpretation.
Revised | Does not mean new data were collected.
Addressed | Can mean clarified, not that a design limitation disappeared.
Accepted | An editorial status, not guaranteed by agreement with a reviewer.''',
    d='''Which revised claim is supported? | Sixty volunteer students at one campus reported mean post-workshop confidence of 7.1 out of ten. | The workshop raised confidence by 7.1 points. | All adults learned more because of the workshop. | Random assignment proved the effect. | The supported statement reports the measured outcome and sample without inventing a baseline or causal design.
Which response accurately describes the work? | The abstract and conclusion are narrowed; no reanalysis was performed. | New trial results solve the issue. | The original mean is now invalid solely because the wording was too broad. | The reviewer has guaranteed acceptance. | The revision changes interpretation and reporting, not the dataset or analysis.
What does acknowledging the limitation accomplish? | Makes the interpretation more accurate without removing the design constraint | Creates an unmeasured baseline | Converts confidence to learning | Makes a volunteer sample nationally representative | Explicit reporting improves transparency but cannot alter how the completed study was designed.
Which locator should the response use? | Page and line numbers verified against the revised manuscript | Numbers copied without checking from an older version | Only the phrase somewhere in the paper | A fabricated appendix | Accurate locations let the reviewer find the actual correction in the submitted revision.''',
    dialogue='''Mei | The reviewer says our claim about improving learning for all adults exceeds the sample and design. I agree, but the response needs to explain the correction precisely.
Luca | Start with the measured [[construct::The measured construct was self-reported confidence, not demonstrated learning, so the original claim described a different outcome.]]. We asked sixty volunteer students at one campus about confidence after the workshop. We did not directly assess learning, and the distinction belongs in the revised wording.
Mei | The mean was seven point one on a ten-point scale. That observed number can remain, provided we do not call it a seven-point improvement.
Luca | Right. It is a [[post-only measure::A post-only measure records the state after the workshop without a baseline from which to calculate improvement.]]. We have no baseline measurement, so we cannot calculate a before-and-after change. The original sentence implied a comparison we never measured.
Mei | We also had no comparison group. Narrowing the claim should therefore address both the measured outcome and the lack of a design supporting that causal language.
Luca | State the [[limitation::The limitation restricts interpretation; making it explicit does not retroactively add a baseline or comparison group.]] directly. The study reports post-workshop confidence in this sample. It does not isolate the workshop's effect, and revising the wording does not change that design boundary.
Mei | What about all adults? Even if we had measured learning, sixty volunteers at one campus would not establish the same result in every adult population.
Luca | Remove that [[overgeneralization::Overgeneralization extends the conclusion beyond the volunteer, single-campus sample without supporting evidence.]]. The revised statement should name the observed sample. We can discuss broader questions as future research without presenting them as conclusions already established by these participants.
Mei | The abstract and conclusion both contain the overclaim. We need to change both, not just the quoted sentence.
Luca | Check the [[revised manuscript::The revised manuscript must use consistent claim boundaries across sections, rather than correcting only one quoted sentence.]] throughout. The title, summary, results description, and final interpretation should not quietly restore the same unsupported claim after we have corrected it elsewhere.
Mei | Our response should say we agree, explain what changed, and show where the reviewer can find it. A generic thank-you would not demonstrate the revision.
Luca | Use a [[point-by-point response::A point-by-point response links the specific reviewer concern to the corresponding explanation and revision.]]. For this comment, identify the outcome correction, the population boundary, and the design limitation. The reviewer should be able to verify each without guessing what we meant.
Mei | I will add the page and line numbers after the revised file is finalized. The current numbers could shift as we edit the abstract.
Luca | A checked [[page-and-line reference::A page-and-line reference must match the revised version so the reviewer can locate the actual correction.]] matters. Use the submitted revision's locations, not an earlier draft's numbering. We should also keep the response wording consistent with the actual replacement text.
Mei | Someone suggested claiming additional analyses. We have not done them, and an impressive-sounding statement would not solve the problem.
Luca | Do not claim [[reanalysis::Reanalysis means new analysis of existing data, which the brief explicitly says has not occurred.]]. No new data or analysis was added. This revision corrects the interpretation and reporting of the existing observation; it does not create evidence the study never collected.
Mei | The response can say the limitation has been addressed in the text, but I worry that addressed might sound as if the methodological weakness disappeared.
Luca | Say the [[revision::The revision clarifies the interpretation and limitation rather than eliminating the underlying design constraint.]] makes the boundary explicit. That is accurate and useful. We have improved the manuscript's claims, not repaired the completed design or established an effect through wording alone.
Mei | I will keep the mean, remove the improvement and all-adults claims, and verify locations before resubmission.
Luca | Then await the [[editorial decision::The editorial decision remains with the journal; a valid correction does not guarantee acceptance.]]. A clear correction supports evaluation, but it does not guarantee acceptance. Our responsibility is to make the evidence, changes, and remaining limitations straightforward to inspect.''',
    transfer_title='A corrected claim, unchanged observations',
    transfer_setup='A single-campus survey records post-session satisfaction from 45 volunteers, with no baseline or comparison group. Authors remove a claim of improved performance. They change wording only and collect no new data.',
    transfer='''Author: "The measured outcome was ___." | satisfaction | The survey asks about satisfaction, not directly observed performance.
Reviewer: "The study cannot calculate improvement without a ___." | baseline | A post-only observation lacks the starting measure needed for a before-and-after change.
Author: "The work completed here is a wording ___." | revision | The authors changed the claim without collecting data or performing a new analysis.
Reviewer: "The design limitation is explicit, not ___." | eliminated | More accurate wording does not change the completed study's design.'''))


BOOK['units'].append(unit(
    title='Data Management and Reproducibility',
    scene='The missing-value code is not a temperature',
    skill='Make a dataset interpretable through verified units, missing-value rules, dates, and traceable processing.',
    brief='Research data steward Elena helps analyst Ravi prepare a small environmental dataset. The column t contains 20, 22, -999, 24, and 26. The collector confirms that t is air temperature in degrees Celsius and -999 means a failed reading, not a temperature or zero. The date label 04/05/26 is confirmed as May 4, 2026; readings were taken at 09:00 UTC. The raw file must remain unchanged. An analysis copy will mark the failed reading as missing and calculate the mean of the four valid values. The release needs a data dictionary, processing record, and identified software version.',
    cast='Elena | Research data steward\nRavi | Analyst',
    culture=('Make the file usable by someone outside the team', 'A familiar variable name can hide assumptions that a new collaborator cannot recover. Confirm definitions with the collector instead of guessing from plausible values. Document the transformation so a later reader can distinguish an observed value from a missing code and reproduce the analysis.'),
    a='''What does -999 represent in this dataset? | A failed reading coded as missing | A valid Celsius temperature | Exactly zero degrees | A Fahrenheit value requiring conversion | The collector explicitly confirms that minus nine hundred ninety-nine is the failed-reading code.
What is the mean of the four valid temperatures? | 23 degrees Celsius | -181.4 degrees Celsius | 18.4 degrees Celsius | 92 degrees Celsius | The valid values sum to ninety-two, and ninety-two divided by four equals twenty-three.
How should 04/05/26 be represented unambiguously after confirmation? | 2026-05-04 | 2026-04-05 | 2026-05-26 | 2004-05-26 | The collector confirms May fourth, twenty twenty-six, which matches the year-month-day representation.''',
    vocabulary='''data dictionary | Definitions and coding rules for dataset variables. | publish a data dictionary
metadata | Information describing data, collection, or processing. | supply essential metadata
variable name | The label assigned to a data field. | clarify variable names
unit of measurement | The scale used to express a quantity. | specify units of measurement
missing-value code | A designated value representing absent information. | document missing-value codes
sentinel value | A special value used to mark a status rather than an observation. | identify a sentinel value
failed reading | A measurement attempt without a valid recorded result. | mark a failed reading
valid observation | A recorded value meeting the applicable inclusion rules. | count valid observations
raw file | The original dataset before later cleaning or transformation. | preserve the raw file
analysis copy | A derived dataset used for analysis. | create a documented analysis copy
transformation log | A record of changes from source to derived data. | maintain a transformation log
data cleaning | Applying documented rules to correct or prepare data. | document data cleaning
imputation | Replacing missing values using a specified estimation method. | distinguish cleaning from imputation
complete-case calculation | A calculation using records with required observed values. | describe a complete-case calculation
date format | The convention used to represent a calendar date. | standardize the date format
time zone | The reference used to interpret recorded times. | record the time zone
collection timestamp | The recorded date and time of observation. | preserve collection timestamps
version identifier | A label identifying a particular dataset or software revision. | record the version identifier
software environment | The tools and versions used to run an analysis. | document the software environment
dependency | A required library or component for a process. | list analysis dependencies
readme | An introductory file explaining a dataset or project. | include a readme
repository | A managed location for preserving and accessing materials. | select a suitable repository
computational reproducibility | Reobtaining results with the specified data and computation. | check computational reproducibility
data validation | Checks that data meet specified rules or expectations. | perform data validation''',
    precision='The valid values are 20, 22, 24, and 26: their mean is 23 degrees Celsius. Treating -999 as a temperature would produce -181.4. Replacing it with zero would produce 18.4. Neither represents the stated valid-observation calculation.',
    precision_extra='The analysis uses four observed values; it does not estimate the failed reading. Preserve the raw sentinel and document its conversion to missing in the analysis copy. The collector, not a guess about regional date conventions, resolves the date.',
    phrases='''Ask for meaning | "What does the variable t represent?"
Confirm the unit | "The collector confirms degrees Celsius."
Identify the special code | "Minus 999 marks a failed reading."
Reject a false zero | "Missing is not the same as zero."
Keep the original | "The raw file remains unchanged."
Describe the derived copy | "The analysis copy marks that code as missing."
State the calculation base | "The mean uses four valid observations."
Give the result with units | "The valid-observation mean is 23 degrees Celsius."
Avoid invented data | "We have not imputed the failed reading."
Resolve the date | "The collector confirms May 4, 2026."
Use an unambiguous format | "Record the date as 2026-05-04."
Keep time meaningful | "The collection time is 09:00 UTC."
Document the fields | "The data dictionary must include units and missing codes."
Record the transformation | "Log the conversion and the calculation rule."
Identify the environment | "State the software version used for the analysis."
Check the release | "Another analyst should be able to reproduce the reported mean."''',
    notes='''Plausible | Not a substitute for a verified variable definition.
Missing | An absent valid observation, not zero.
Excluded from this mean | Does not mean erased from the raw record.
Imputed | An estimated replacement; none is supplied in this case.
May 4 | Confirmed meaning of the otherwise ambiguous source label.
Reproducible | Computation can repeat; that alone does not prove scientific validity.''',
    d='''Which data-handling description is correct? | Preserve the raw file and convert the sentinel to missing in a documented analysis copy. | Overwrite the raw value without a record. | Replace the failed reading with zero and call it observed. | Treat -999 as a valid air temperature. | The first option preserves provenance and applies the collector's confirmed coding rule.
What does using four valid observations imply? | No value has been imputed for the failed reading. | The missing temperature is proved to be zero. | Five valid temperatures were measured. | The raw file must be deleted. | The calculation uses observed values only and does not estimate the failed measurement.
Why is the collector's date confirmation necessary? | The original numeric label could otherwise be interpreted in different date orders. | All countries use the same numeric date order. | Time zone alone decides the calendar format. | The date should be chosen to improve the mean. | The source label is ambiguous without verified knowledge of its intended date convention.
Which release package best supports reproducibility? | Data, dictionary, processing steps, and the identified software environment | Only a column named t | Only the final mean without units | A screenshot with an unexplained missing code | Interpretable data and traceable computation allow another analyst to understand and rerun the result.''',
    dialogue='''Ravi | The shared file has a column called t and five values. Four look like ordinary temperatures, but the fifth is minus nine hundred ninety-nine.
Elena | Do not guess the [[unit of measurement::The unit of measurement must come from verified collection information; the collector confirms degrees Celsius in this case.]] from the values. The collector confirms air temperature in degrees Celsius. We need that definition in the documentation, because the column name alone does not establish it.
Ravi | The collector confirmed that minus nine hundred ninety-nine codes a failed reading, not a cold observation.
Elena | Record it as a [[missing-value code::The missing-value code represents an absent valid reading, not an observed temperature or a zero measurement.]]. In the analysis copy, mark that entry as missing. Do not substitute zero, because that would invent an observed temperature and change the meaning of the calculation.
Ravi | Including the code gives a mean of minus one hundred eighty-one point four, which is not the supported calculation.
Elena | Use the four [[valid observations::The valid observations are twenty, twenty-two, twenty-four, and twenty-six, excluding the failed-reading code from the stated mean.]] for this mean: twenty, twenty-two, twenty-four, and twenty-six. They sum to ninety-two, so the mean is twenty-three degrees Celsius. State the four-observation base alongside it.
Ravi | Replacing the code with zero would give eighteen point four instead. That is also wrong for this requested mean, even though it looks less obviously unusual.
Elena | Correct. We are not performing [[imputation::Imputation would estimate a replacement value, whereas this case calculates a mean from four observed temperatures without filling the missing reading.]]. We have no estimated replacement for the failed reading. The analysis should say exactly which observed values were used, without turning an absent measurement into a convenient number.
Ravi | Should I replace the code in the original to prevent mistakes? Then only the cleaned version would remain.
Elena | Preserve the [[raw file::The raw file retains the original record, including its sentinel, while documented transformations belong in a separate derived copy.]]. Keep the original code and create a documented analysis copy. Future users need both the source record and the explanation of how the derived data were produced.
Ravi | There is also a date labeled zero-four slash zero-five slash twenty-six. The collector says it means May fourth, twenty twenty-six, not April fifth.
Elena | Use an unambiguous [[date format::The date format should reflect the confirmed May fourth date, written as 2026-05-04 rather than guessed from regional convention.]] such as 2026-05-04 in the documented copy. Record how you resolved the source label. A plausible regional assumption would not be enough without that confirmation.
Ravi | The readings were taken at nine in the morning UTC. I will include that reference, because nine o'clock alone could mean different local times.
Elena | Yes, the [[time zone::The time zone anchors the collection time; 09:00 UTC is more precise than an unspecified nine o'clock.]] belongs with the collection information. Keep the timestamp meaning explicit so another researcher does not align these readings with observations from a different hour.
Ravi | The data dictionary will define t, the Celsius unit, the failed-reading code, and the confirmed date and time conventions. What else belongs in the release?
Elena | Add a [[transformation log::The transformation log records conversion of the sentinel and the calculation rule so the result can be traced to the original data.]] describing the missing-code conversion and mean calculation. It should connect the raw file to the analysis copy and reported result without requiring a colleague to reconstruct undocumented choices.
Ravi | We need the software version and dependencies. The file name alone does not identify the analysis environment.
Elena | Document the [[software environment::The software environment identifies the tools and versions used to produce the result, supporting a repeatable computation.]] with the data and instructions. Even a simple calculation benefits from a traceable version, especially when this small example becomes part of a larger processing workflow.
Ravi | I will ask another analyst to follow the release instructions and reproduce the twenty-three-degree mean from the preserved source and documented rules.
Elena | That checks [[computational reproducibility::Computational reproducibility checks whether the specified data and steps reproduce the result, not whether every scientific assumption is thereby validated.]]. A matching result is useful, but it does not alone prove the study's scientific validity. The release must make both the computation and the meaning of the data clear.''',
    transfer_title='Do not turn missing into zero',
    transfer_setup='A confirmed Celsius column contains 10, 12, -999, and 14. The collector defines -999 as missing. The requested mean uses only observed temperatures, and the original file must be preserved.',
    transfer='''Analyst: "There are ___ valid observations." | three | Ten, twelve, and fourteen are valid; the sentinel marks the missing reading.
Steward: "Their mean is ___ degrees Celsius." | 12 | The three valid values sum to thirty-six, which divided by three equals twelve.
Analyst: "The raw sentinel is retained in the ___." | original file | The source record remains unchanged while a derived copy handles missing values.
Steward: "No missing temperature has been ___." | imputed | The calculation uses observed values rather than estimating a replacement temperature.'''))

BOOK['units'].append(unit(
    title='Academic Presentations and Conferences',
    scene='Answer the challenge without claiming universal proof',
    skill='Give a concise evidence-based conference answer, distinguish task performance from mechanism, and handle an unresolved question.',
    brief='Presenter Noor answers a conference question about a memory-strategy study. All 24 volunteers completed one laboratory task in a fixed before-then-after order. Mean response time was 600 milliseconds before training and 540 afterward, a 60-millisecond or 10% reduction. There was no untrained comparison group, so practice and order effects are not isolated from training. No confidence interval or significance test is supplied for this exercise. An audience member asks whether the study proves a general memory theory. During the follow-up discussion, Noor must answer concisely, stating observations, limits, and the next test without inventing evidence.',
    cast='Audience member | Conference participant\nNoor | Presenter',
    culture=('Answer the strongest reasonable version of the question', 'A challenging question can help clarify the contribution. Give the direct answer first, then the main evidence and limitation. You can reject an overstatement without dismissing your own result or treating the questioner as hostile. Offer a relevant next study rather than an unsupported promise.'),
    a='''What change was observed in mean response time? | A reduction of 60 milliseconds, or 10% | A reduction of 540 milliseconds, or 90% | A 60% increase | No before-and-after difference | Six hundred minus five hundred forty is sixty milliseconds, one tenth of the initial mean.
Which alternative explanations are not isolated? | Practice and order effects | A confirmed change in all adult memory systems | A published confidence interval | Randomized group allocation | The fixed sequence and absent untrained group leave practice and order effects unresolved.
What should Noor say about a confidence interval? | None is supplied here, so no interval should be invented. | It is exactly zero to sixty. | It proves the general theory. | It must be 95% to 100%. | The brief provides no interval calculation, so the response must not fabricate one.''',
    vocabulary='''conference presentation | A spoken account of research for a scholarly audience. | deliver a conference presentation
audience question | A query raised by someone attending a talk. | answer an audience question
central finding | The main observation or result being reported. | state the central finding
take-home message | The concise main point an audience should retain. | clarify the take-home message
response time | The elapsed time to produce a response in a task. | measure response time
millisecond | One thousandth of a second. | report milliseconds
within-participant comparison | A comparison of observations from the same participants. | describe a within-participant comparison
fixed order | The same sequence of conditions for all participants. | acknowledge a fixed order
practice effect | A performance change associated with repeated task exposure. | consider a practice effect
order effect | A change associated with the sequence of conditions. | control for order effects
comparison arm | A study group or condition serving as a reference. | include a comparison arm
counterbalancing | Varying condition order across participants under a design. | plan appropriate counterbalancing
mechanism | The process proposed to explain an observed effect. | test a proposed mechanism
theoretical claim | An assertion about a broader explanatory account. | bound a theoretical claim
generalizability | The extent to which results apply beyond the study context. | assess generalizability
statistical uncertainty | Uncertainty associated with estimation from data. | communicate statistical uncertainty
confidence interval | An interval produced by a method with stated long-run coverage. | report a confidence interval
significance test | A statistical assessment under a specified null model. | interpret a significance test
independent replication | A new study testing a finding with independent evidence. | seek independent replication
boundary condition | A circumstance limiting when a finding or explanation applies. | identify boundary conditions
controlled follow-up | A later study designed to address relevant alternative explanations. | propose a controlled follow-up
clarifying question | A question used to resolve ambiguity in what is being asked. | ask a clarifying question
time allocation | The speaking time available for a response. | respect the time allocation
unresolved question | An issue not answered by the current evidence. | state the unresolved question''',
    precision='The mean fell from 600 to 540 milliseconds: 60/600 equals 10%. Lower response time is faster performance on this task. That observation alone does not identify the mechanism, isolate training from practice, or establish a universal memory theory.',
    precision_extra='A sample size and two means do not supply a confidence interval or significance test by themselves. Do not invent either. State the available evidence and propose a design that addresses the fixed order, absent comparison group, and narrow setting.',
    phrases='''Answer directly | "No, this study does not prove the general theory."
State the observed change | "Mean response time fell from 600 to 540 milliseconds."
Give the relative change | "That is a 10% reduction from the initial mean."
Name the sample | "All 24 volunteers completed the task."
Specify the setting | "This was one laboratory task."
Describe the design | "Everyone completed the same before-then-after sequence."
Name the alternative | "Practice and order effects remain possible explanations."
Avoid a causal shortcut | "We have not isolated training from those effects."
Separate mechanism | "Faster responses do not establish the proposed memory mechanism."
Handle missing statistics | "I do not have a verified interval or test result to report here."
Keep the contribution | "The observation is worth testing under stronger controls."
Propose the next test | "A controlled follow-up should address the alternative explanations."
Bound generalization | "Broader populations and tasks need separate evidence."
Clarify the question | "Are you asking about the observed change or the proposed mechanism?"
Respect the time | "The short answer is that the finding is limited but informative."
Close without overpromising | "The next study would test the explanation, not guarantee confirmation."''',
    notes='''Proves | Often stronger than a single empirical study warrants.
Faster | A task-performance description, not a complete explanation.
Before and after | Does not by itself isolate the intervention.
Could reflect | Marks an alternative explanation rather than a finding.
Not supplied | Do not invent a statistic to fill the conversational gap.
Next test | A proposal, not an already completed replication.''',
    d='''Which opening best answers the audience's question? | "No; the study reports a task-specific change, not proof of the general theory." | "Yes; every theory is proved by one lower mean." | "The question is hostile and cannot be answered." | "The effect is definitely statistically significant." | The first opening directly rejects the overstatement while preserving the actual observed result.
Which causal claim is unsupported? | Training alone caused the entire reduction. | Mean response time was lower afterward. | All participants followed the same sequence. | The study used 24 volunteers. | The missing comparison group and fixed order leave alternatives to a training-only explanation.
Which next step best addresses the limitation? | A controlled follow-up designed to separate training from practice and order effects | Repeating the universal claim more confidently | Hiding the fixed sequence | Calling the same data an independent replication | A stronger comparison design can test competing explanations that the current study does not isolate.
Which statement about the mechanism is accurate? | The observed response-time change does not by itself establish the memory mechanism. | Lower response time identifies every internal memory process. | The mechanism was directly measured because the talk was accepted. | A proposed theory and an observed mean are identical evidence. | Task performance and its explanatory mechanism are different claims requiring appropriate evidence.''',
    dialogue='''Audience member | You showed a faster response after training. Does that prove the general memory theory, or are you making a narrower claim about this task?
Noor | Our [[central finding::The central finding is the observed response-time reduction in the supplied task and sample, not universal proof of the theory.]] is narrower. Mean response time fell from six hundred to five hundred forty milliseconds. This does not prove the general theory.
Audience member | What percentage is that reduction? We need the initial response time to interpret its relative size.
Noor | The [[response time::Response time is the measured task duration; sixty milliseconds is ten percent of the initial six-hundred-millisecond mean.]] reduction is ten percent of the initial mean. All twenty-four volunteers completed the task. That calculation describes the observed change, without explaining its cause or importance beyond this setting.
Audience member | Did different groups perform the before and after conditions, or were these repeated observations from the same people?
Noor | It was a [[within-participant comparison::A within-participant comparison uses observations from the same people, here before and after in a fixed sequence.]]. Everyone completed the before condition and then the after condition in the same order. That controls neither every time-related influence nor the effect of repeating the task.
Audience member | People may be faster through practice. How did you separate that possibility from training?
Noor | We did not isolate the [[practice effect::A practice effect is an alternative explanation arising from repeated task exposure, which the current design does not separate from training.]]. There was no untrained comparison group. Repetition may contribute to the reduction, and the fixed order leaves related explanations open. I cannot attribute the entire change to training alone.
Audience member | Did you measure the memory process itself, or is it a proposed explanation for faster responses?
Noor | It remains a proposed [[mechanism::The mechanism is an explanation for performance, not something established merely by observing lower response times.]]. Faster responses do not identify the underlying process. This observation motivates testing that explanation; it cannot replace such a test.
Audience member | What confidence interval surrounds the reduction? It would help us judge how much uncertainty there is around the estimated change.
Noor | I do not have a verified [[confidence interval::No confidence interval is supplied for this exercise, so the presenter must not invent an interval or claim certainty.]] to report here, and I should not guess. The sample size and two means alone do not provide enough information for a defensible interval calculation.
Audience member | Fair enough. Would a controlled follow-up be aimed at repeating the same observation, or at separating the competing explanations?
Noor | A [[controlled follow-up::A controlled follow-up should address practice and order alternatives rather than merely repeat the original uncontrolled sequence.]] should address those alternatives explicitly. The design needs an appropriate comparison and attention to sequence, with its analysis planned before results are examined. That is proposed work, not a completed validation.
Audience member | Even if that study supports a training effect, would you still need evidence beyond this task and these volunteers before making the broad theory claim?
Noor | Yes. [[Generalizability::Generalizability concerns application beyond the observed volunteers and laboratory task, which requires additional relevant evidence.]] remains a separate issue. Other populations, tasks, and conditions could behave differently. A better-controlled local result would not automatically establish every application of the theory.
Audience member | We have little time left. What is the single sentence you would like the audience to take away without overstating the contribution?
Noor | My [[take-home message::The take-home message summarizes the observation and its limits rather than converting a task-specific result into a universal causal claim.]] is that twenty-four volunteers responded faster after training in this task, while training, practice, and order contributions remain unresolved. It is a useful observation to investigate, not universal proof.
Audience member | Thank you. That distinguishes the observed change from a general explanation. The planned test sounds like the important next step.
Noor | Exactly. The [[unresolved question::The unresolved question is what produced the change and how broadly it applies, not whether the reported means differ arithmetically.]] is what produced the change and how broadly it applies. We will keep those questions explicit rather than promise that the next study must confirm our preferred explanation.''',
    transfer_title='Give the observation and its boundary',
    transfer_setup='A fixed-order task study records mean times of 800 milliseconds before training and 720 afterward in 16 volunteers. There is no untrained comparison group, and no interval or significance result is supplied.',
    transfer='''Presenter: "The mean reduction is ___ milliseconds." | 80 | Eight hundred minus seven hundred twenty equals eighty milliseconds.
Questioner: "Relative to the initial mean, that is ___ percent." | 10 | Eighty divided by eight hundred equals ten percent.
Presenter: "Training has not been isolated from ___." | practice and order effects | The fixed sequence and absent comparison group leave those alternative explanations unresolved.
Questioner: "A significance result must not be ___." | invented | No significance test result is supplied in the case.'''))
