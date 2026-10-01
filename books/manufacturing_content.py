"""Original production, improvement, quality, and shift-handoff conversations."""
from books.authoring import unit

BOOK = dict(
    slug='manufacturing', title='Manufacturing English',
    cover_label='Production / improvement / reliability / handoffs',
    cover_title='Manufacturing', cover_size=34,
    tagline='Describe the loss. Test the explanation. Make the handoff clear.',
    audience='For production, quality, maintenance, supplier, and continuous-improvement teams.',
    map_intro='Eight shop-floor and management conversations connecting production facts to clear, accountable next steps.',
    notes_title='Keep the number attached to its meaning.',
    notes_intro='Manufacturing discussions move quickly between quantities, causes, schedules, and decisions. A missed target may be real even when its cause is unknown. A held lot may contain uninspected material. A named action may still be unfinished. These cases develop the language for keeping those distinctions visible under the everyday pressure to restore output and meet commitments.',
    field_notes=[
        ('State the measure and its basis', 'Give the unit, time period, numerator, and comparison. Output attainment, availability, and first-pass yield are different measures; a familiar percentage should not be relabeled without the required data.', '"We achieved 84% of the output target; that is not an OEE result."'),
        ('Observe before assigning a cause', 'A timeline or repeated symptom can guide investigation without proving a root cause. State what changed, what was observed, and which competing explanations remain open.', '"The defect followed the supplier change, but the process settings changed too."'),
        ('Separate material states', 'Scrapped, awaiting rework, on hold, accepted, and released have different consequences. Use quantities for each state and avoid counting expected recovery as finished good output.', '"Sixty units await rework; they are not yet accepted units."'),
        ('Make the handoff closed-loop', 'A sent message does not prove it was understood. Identify the open item, evidence, responsible person, and next checkpoint, then confirm receipt and understanding without implying completion.', '"Two checks remain open; please confirm their identifiers and the next update."')],
    scope_note='Original fictional language practice, not equipment-operation, maintenance, engineering, or safety instructions. Figures, organizations, and workplace cases are invented. Actual work must follow applicable law, approved site procedures, trained personnel, and authorized decisions. Classroom safety discussions do not authorize isolation, servicing, or restart.',
    sources=[
        dict(title='National Institute of Standards and Technology. Value Stream Mapping.', url='https://www.nist.gov/mep/value-stream-mapping', note='Background on mapping material and information flow to identify improvement opportunities. The observations, pilot proposals, and datasets here are original.', checked='30 September 2026'),
        dict(title='American Society for Quality. Root Cause Analysis.', url='https://asq.org/quality-resources/root-cause-analysis', note='Background on investigating causes rather than equating a symptom or timeline with a proven explanation.', checked='30 September 2026'),
        dict(title='American Society for Quality. Quality Glossary.', url='https://asq.org/quality-resources/quality-glossary', note='Terminology reference. Definitions and practice cases in this book are independently written for language learning, not certification or a quality-system standard.', checked='30 September 2026'),
        dict(title='US Occupational Safety and Health Administration. Control of Hazardous Energy.', url='https://www.osha.gov/control-hazardous-energy/', note='Background on the need for an appropriate energy-control program, procedures, and training. The book deliberately supplies no machine-specific isolation sequence.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Production Flow and Daily Management',
    scene='Eight hundred forty is not the whole story',
    skill='Report an output shortfall precisely while separating observed downtime, unconfirmed causes, and different performance measures.',
    brief='Production lead Mei and operations manager Daniel review yesterday\'s line output: 840 completed units against a 1,000-unit target. The log records 40 minutes of downtime, but the cause and its contribution to the shortfall are still being checked. The briefing supplies no planned production time, ideal cycle time, or quality breakdown. A dashboard labels 84% as overall equipment effectiveness. Mei and Daniel must correct the metric and give a useful update without claiming the downtime explains every missing unit.',
    cast='Mei | Production lead\nDaniel | Operations manager',
    culture=('A precise update can still be brief', 'Start with the result, then the confirmed loss information and the open cause. This lets a busy manager distinguish the size of the gap from the explanation. Avoid filling a short status slot with a confident causal claim simply because the investigation is unfinished.'),
    a='''What was the output shortfall? | 160 units | 40 units | 840 units | 1,840 units | Subtracting 840 completed units from the 1,000-unit target gives a 160-unit shortfall.
What does 84% represent here? | Output as a share of the stated target | A supplied OEE calculation | A verified availability percentage | A first-pass yield result | The available calculation is 840 divided by 1,000, which measures output target attainment.
What is known about the downtime? | Forty minutes were logged; its cause and contribution remain under review. | It definitely explains all 160 missing units. | It was caused by operator error. | It proves the line had no quality losses. | The briefing gives a duration but not the cause or a complete loss attribution.''',
    vocabulary='''production target | The planned output quantity for a defined period. | set a production target
actual output | The quantity actually produced in the stated period. | report actual output
target attainment | Actual output expressed relative to the stated target. | calculate target attainment
shortfall | The amount by which a result falls below its target. | quantify the shortfall
throughput | The quantity passing through a process per unit of time. | measure throughput
cycle time | The elapsed time required for a defined process cycle. | measure cycle time
takt time | The production pace required to meet demand using available time. | calculate takt time
lead time | The elapsed time from a defined request or start to completion. | reduce lead time
work in process | Material that has entered production but is not yet finished. | control work in process
bottleneck | The step that limits the output of the overall process. | identify the bottleneck
constraint | A limiting factor on the system's performance. | manage the constraint
line balance | Distribution of work across production steps. | improve line balance
downtime | Time during which equipment or a process is not producing as defined. | log downtime
planned stop | A scheduled interruption included in the operating plan. | distinguish planned stops
unplanned stop | An interruption not included in the intended operating schedule. | investigate unplanned stops
availability | The share of planned production time in which equipment is running. | assess equipment availability
performance loss | Output-speed loss relative to the defined ideal running rate. | analyze performance losses
quality loss | Output that does not meet the defined good-product criteria. | quantify quality losses
overall equipment effectiveness | A combined availability, performance, and quality measure, abbreviated OEE. | calculate overall equipment effectiveness
daily management | Routine review of performance, problems, and follow-up actions. | support daily management
tier meeting | A short escalation meeting at a defined organizational level. | escalate through a tier meeting
visual board | A shared display of current measures, status, and actions. | update the visual board
loss attribution | Assignment of a measured loss to supported contributing factors. | verify loss attribution
recovery plan | A defined proposal for addressing a performance or schedule gap. | review the recovery plan''',
    precision='840 divided by 1,000 is 84% target attainment. The shortfall is 160 units, or 16% of target. Neither result supplies OEE, availability, or first-pass yield. Those measures require their own defined inputs and calculation bases.',
    precision_extra='A recorded 40-minute stop does not automatically explain the entire output gap. The expected running rate, other losses, and the time basis matter. Describe the log as evidence under review rather than a completed causal analysis.',
    phrases='''Lead with the result | We completed 840 units against a target of 1,000.
Quantify the gap | The shortfall is 160 units, or 16% of target.
Name the measure | Eighty-four percent is output target attainment.
Correct the label | The supplied figures do not support an OEE calculation.
State the logged loss | The log records 40 minutes of downtime.
Keep cause open | The reason for that downtime is still being checked.
Limit attribution | We have not established how much of the shortfall the stop explains.
Ask for the time basis | What planned production time was used in this calculation?
Distinguish rate from quantity | Throughput needs a quantity and a time period.
Check the constraint | We have not yet confirmed which step limited total output.
Request the breakdown | Separate speed, availability, and quality information.
Avoid blame | The current log does not establish an operator cause.
Make the update useful | Report the known gap and the next evidence check separately.
Bound the recovery claim | A recovery proposal is not a guarantee that the missing output will be recovered.
Assign the follow-up | Mei will reconcile the log and report the supported loss breakdown.
Close the board update | Keep the metric definition beside the percentage.''',
    notes='''Against | Introduces the comparison target, not necessarily customer demand.
Down by | State the amount and comparison period to avoid ambiguity.
Percent of | Identifies a ratio; it is not the same as a percentage-point change.
Explains | Makes a causal or accounting claim that needs support.
Logged | Means recorded, not necessarily investigated or verified.
Recover | Specify output, schedule, or service; one recovery may not imply another.''',
    d='''Which board entry is accurate? | 840 units completed; 84% of target; 160-unit shortfall. | OEE 84%, with all losses explained. | Availability 84% and first-pass yield 100%. | Forty missing units because downtime was 40 minutes. | The entry uses only the supplied output and target and keeps units distinct from time.
Why is OEE not established? | Planned time, ideal cycle time, and quality information are not supplied. | OEE is always identical to target attainment. | A target of 1,000 automatically defines ideal cycle time. | Downtime alone supplies every OEE input. | OEE combines distinct factors whose required inputs are missing from the brief.
Which sentence best describes the 40-minute stop? | It is recorded downtime whose cause and contribution to the output gap remain under review. | It proves the entire 160-unit loss came from one cause. | It demonstrates an operator was at fault. | It proves all running units met quality criteria. | A duration alone does not establish a cause, a full loss attribution, or quality performance.
If a second shift produces 900 against a target of 1,000, what is its attainment? | 90%, six percentage points above 84% | 90%, exactly six percent above 84% | 10%, because 100 units are missing | 900%, because 900 units were produced | 900 divided by 1,000 is 90%; the difference between 90% and 84% is six percentage points.''',
    dialogue='''Daniel | Yesterday's board shows eight hundred forty units against a thousand. It labels eighty-four percent as OEE, but I cannot see the inputs behind that label.
Mei | The figure is [[target attainment::The calculation compares actual output with the target, not the separate inputs needed for OEE.]]. We divided completed output by the stated target; we did not calculate the availability, performance, and quality factors.
Daniel | Then the output gap should be stated directly. A manager reading the board should not have to infer whether the percentage means output, running time, or good units.
Mei | The [[shortfall::The shortfall is the target minus actual output: 1,000 minus 840 equals 160 units.]] is one hundred sixty units, or sixteen percent of target. That is a quantity gap, not a duration and not an explanation of the cause.
Daniel | The stop log records forty minutes. Does the team believe that interruption accounts for all the missing units, or is the analysis still open?
Mei | The [[downtime::Downtime is the recorded nonproducing duration, whose cause and contribution remain unconfirmed here.]] is logged, but its cause and contribution remain under review. We should not convert forty minutes into one hundred sixty lost units without the relevant basis.
Daniel | We would need to know the expected production rate and whether other losses occurred. The board currently makes a single interruption look like a complete explanation.
Mei | Exactly. [[Loss attribution::Loss attribution assigns losses to supported contributors; the log alone does not complete that analysis.]] needs supporting data. I will reconcile the timing, output, and other relevant records rather than attach the entire gap to the most visible event.
Daniel | What should we request for the equipment measure? I want the corrected board to explain the missing information without turning the morning meeting into a statistics lecture.
Mei | Start with the basis for [[availability::Availability relates running time to planned production time, which is not supplied in this brief.]]. We need the planned production time and the relevant running time, not merely the output target and one stop duration.
Daniel | The speed side also needs a clear reference. Actual output can fall short even while the equipment is running, so time and quantity should not be merged.
Mei | Yes. The [[performance loss::Performance loss concerns running below the defined ideal rate, requiring speed-related information beyond downtime.]] assessment needs the defined ideal rate and actual running performance. The supplied briefing does not provide that basis, so the board cannot claim a completed result.
Daniel | And the completed-unit count does not tell us how many met the quality definition. We should not silently assume that every produced unit was good.
Mei | Correct. [[Quality loss::Quality loss concerns units not meeting the defined good-product criteria, information absent from the supplied count.]] needs the appropriate output breakdown. A production count by itself cannot establish that no defects or other quality losses occurred.
Daniel | Someone has suggested the packing station is the limiting step. That may be worth checking, but I have not seen evidence showing it constrained the whole line.
Mei | Keep [[bottleneck::A bottleneck is the system-limiting step, which must be identified from evidence rather than a local impression.]] as an investigation question. A busy station or visible queue does not automatically identify the system's actual limiting step.
Daniel | For today's meeting, I need a concise update: result, known interruption, open questions, and responsibility for the next check. We can discuss recovery after that evidence is clearer.
Mei | I will update the [[visual board::The visual board should distinguish the confirmed measures, unresolved causes, and assigned next actions.]] accordingly. It will show the output gap and logged stop separately, with me responsible for reconciling the records and reporting the supported breakdown.
Daniel | Good. We can acknowledge the missed target without guessing why it happened. Any proposal to recover output should make its assumptions and constraints clear.
Mei | Agreed. The [[recovery plan::A recovery plan is a proposal for addressing the gap, not proof that the missing output will be recovered.]] will remain a proposal until assessed and authorized. First, the board must use the right measure and keep the unfinished investigation visible.''',
    transfer_title='Compare the right percentages',
    transfer_setup='A line produces 450 units against a target of 500. It logs 20 minutes of downtime. No cause or OEE inputs are supplied.',
    transfer='''Lead: "Target attainment is ___ percent." | ninety | Dividing 450 by 500 gives 0.90, or ninety percent.
Planner: "The output shortfall is ___ units." | fifty | The target of 500 minus actual output of 450 leaves fifty units.
Lead: "Twenty minutes describes recorded ___." | downtime | The supplied duration is nonproducing time, not a quantity of missing units.
Planner: "The cause remains ___." | unconfirmed | The briefing provides no established explanation for the recorded stop.'''))

BOOK['units'].append(unit(
    title='Lean, Waste, and Continuous Improvement',
    scene='The queue is for a shared tool',
    skill='Describe observed waiting, challenge unsupported blame, and define a bounded improvement trial without claiming savings in advance.',
    brief='Improvement facilitator Ana and supervisor Marcus observe a one-hour assembly session. Eight waiting episodes for a shared tool total 24 operator-minutes; some episodes overlap, so this is not 24 minutes of line downtime. The supervisor calls the operators slow. The team proposes a one-bench point-of-use tool trial, but no trial result exists. Ana and Marcus must distinguish waiting from working pace, explain the time basis, and keep safety and quality checks unchanged in the proposal.',
    cast='Ana | Improvement facilitator\nMarcus | Assembly supervisor',
    culture=('Invite the people who do the work', 'A respectful observation describes the delay and asks how the process creates it. Operators can explain practical constraints that a meeting-room proposal misses. Their involvement is not permission to bypass controls; it helps the team design a realistic, reviewable improvement trial.'),
    a='''What was observed? | Eight tool-waiting episodes totaling 24 operator-minutes | Twenty-four minutes of confirmed line downtime | A proven slow working pace for every operator | A successful completed tool trial | The observation concerns waiting episodes and accumulated operator time, not a completed improvement or individual performance diagnosis.
Why is 24 not necessarily line downtime? | Some waiting episodes overlap, and the measure is operator-minutes. | Operator-minutes never include waiting. | Eight episodes always equal eight hours. | The line was proved to run without any delay. | Overlapping individual waits cannot simply be added and labeled elapsed whole-line downtime.
What is the proposed change? | A one-bench point-of-use tool trial with safety and quality checks unchanged | Immediate removal of all inspection steps | A completed factory-wide rollout | A guaranteed saving already verified | The scenario supplies a bounded trial proposal, not a result or permission to remove controls.''',
    vocabulary='''lean manufacturing | An approach to improving customer value by reducing waste in the process. | apply lean manufacturing
waste | Resource use that does not add the defined value or support a necessary requirement. | identify process waste
waiting | Time when work cannot proceed because a needed input is unavailable. | reduce waiting time
motion | Movement of people within a task or process. | analyze unnecessary motion
transportation | Movement of material between locations or steps. | reduce unnecessary transportation
overproduction | Producing earlier or in greater quantity than needed. | prevent overproduction
overprocessing | Performing more work than the relevant requirement needs. | identify overprocessing
excess inventory | Material held beyond the justified operating need. | reduce excess inventory
kaizen | Focused, ongoing improvement of work processes. | run a kaizen event
gemba | The actual place where the work occurs. | observe at the gemba
value stream | The connected activities and information involved in delivering a product. | map the value stream
current-state map | A representation of how the process currently works. | create a current-state map
future-state map | A proposed representation of an improved process. | develop a future-state map
point-of-use storage | Keeping needed items near where they are used. | trial point-of-use storage
5S | A workplace-organization method covering order, cleanliness, standards, and sustainment. | sustain 5S practices
standard work | The agreed method and conditions for performing a process. | update standard work
pull system | Replenishment or production triggered by downstream need. | design a pull system
kanban | A signal authorizing defined replenishment or production in a pull system. | use a kanban signal
work-cell layout | The arrangement of people, equipment, and material in a production cell. | assess the work-cell layout
operator-minute | One minute of one operator's time, accumulated across people if specified. | report operator-minutes
baseline observation | A measurement of the current process before a proposed change. | record a baseline observation
pilot trial | A limited test of a proposed change before broader adoption. | define a pilot trial
countermeasure | An action intended to address an identified problem. | test a countermeasure
sustainment | Maintaining an improvement over time through defined follow-up. | plan sustainment''',
    precision='Twenty-four operator-minutes across eight episodes averages three operator-minutes per episode. Overlapping waits mean that total is not automatically elapsed line downtime. State the observation period and time basis when reporting the result.',
    precision_extra='Point-of-use storage is a proposed countermeasure, not proven savings. A bounded trial should define what is compared while retaining required safety and quality controls. A successful local trial would still need review before broader adoption.',
    phrases='''Describe the delay | Operators waited for the shared tool during eight observed episodes.
Name the time basis | The total is 24 operator-minutes, not 24 minutes of line downtime.
Separate pace from access | Waiting for a tool does not by itself show slow working pace.
Challenge the attribution | The observation does not establish that operator speed caused the delay.
Invite practical detail | Ask the operators where the tool is needed and what constrains access.
Define the current state | Record the present locations, demand, and waiting pattern.
State the proposal | Trial point-of-use storage at one bench.
Bound the claim | No improvement result is available yet.
Preserve controls | Required safety and quality checks remain unchanged.
Compare consistently | Use the same time basis and comparable task conditions.
Check for displaced problems | Confirm that the change does not create a shortage at another bench.
Separate a trial from rollout | A one-bench test is not a factory-wide implementation.
Avoid prebooked savings | Do not report proposed time savings as already achieved.
Make the review specific | Review the waiting observations and any new difficulties after the trial.
Retain operator input | Include the people who use the tool in the practical review.
Plan the follow-through | Agree how an accepted improvement would be maintained.''',
    notes='''Waste | A process concept, not a label for an employee.
Slow | Can confuse working pace with delay caused by missing inputs.
Operator-minutes | Adds individual time; it may exceed elapsed clock time when waits overlap.
Trial | Tests a proposal without claiming the result beforehand.
Unchanged | Specify the controls that remain in force during the trial.
Sustained | Means an improvement persists, not merely that one test looked favorable.''',
    d='''Which observation is defensible? | Eight tool-waiting episodes totaled 24 operator-minutes during the hour. | Operators were lazy for exactly 40% of the shift. | The entire line stopped for 24 minutes. | The proposed trial saved 24 minutes already. | The statement preserves the actual event count, observation period, and accumulated time measure.
What is the average time per recorded episode? | Three operator-minutes | Eight operator-minutes | Twenty-four hours | Forty percent of every operator's shift | Dividing 24 operator-minutes by eight episodes gives three operator-minutes per episode.
Which proposal has suitable boundaries? | Trial tool placement at one bench, keep required controls, and compare waiting under comparable conditions. | Remove checks to guarantee a faster result. | Roll out everywhere before reviewing the local effect. | Declare all waits eliminated before the trial. | The proposal defines a limited comparison without changing required controls or assuming the outcome.
What would a reduction at one bench fail to prove by itself? | That waiting fell across the whole factory without new problems elsewhere | That the local observation can be recorded | That the proposal was tested at that bench | That the trial has a defined location | A local improvement does not automatically establish factory-wide benefit or exclude displaced delays.''',
    dialogue='''Marcus | We watched the bench for an hour and recorded eight delays. The team says the operators are slow, but each delay seemed to involve waiting for the shared tool.
Ana | Then name the observed [[waiting::Waiting describes work delayed by unavailable input, not evidence of a slow working pace.]]. The tool was unavailable at those moments; that does not establish that the operators worked slowly when they had what they needed.
Marcus | The sheet adds up to twenty-four minutes. I was going to call that twenty-four minutes of line downtime, although two operators sometimes waited at the same time.
Ana | The measure is [[operator-minute::An operator-minute measures one person's time; overlapping waits cannot be relabeled as elapsed whole-line downtime.]]. The total accumulates individual waiting time, so overlapping episodes must not be presented as the same amount of elapsed whole-line downtime.
Marcus | We should keep the hour-long observation period visible too. Otherwise someone might use the figure as a whole-shift loss or compare it with a different time basis.
Ana | Exactly. This is our [[baseline observation::The baseline records the current process before a change and needs a clear time and task basis.]]. Record the task conditions and tool demand so the later comparison is meaningful rather than just another isolated total.
Marcus | The operators suggested a tool location beside the bench. It sounds practical, but we need to understand whether other stations depend on that same shared tool.
Ana | Create the [[current-state map::A current-state map represents the existing locations, activities, and information flow before proposing a changed arrangement.]] with their input. Show the tool's movements and users, not just the bench we observed.
Marcus | That would also help us separate people walking to retrieve the tool from material being moved between work areas. Both happen, but they are different kinds of movement.
Ana | Yes. Unnecessary [[motion::Motion concerns people's movements within work, distinct from moving material between locations.]] concerns the people performing the task. We should describe the actual movement rather than use a broad waste label that hides what needs to change.
Marcus | For the trial, the suggestion is to keep an appropriate tool at this one bench. We have not decided that every work area needs a new tool arrangement.
Ana | That is a proposal for [[point-of-use storage::Point-of-use storage places needed items near their use, here as a proposal rather than a verified result.]]. Check the practical requirements and shared demand before assuming that moving the tool solves the problem for the whole process.
Marcus | We can start with one bench and compare the waiting pattern. Required inspection and safety checks should stay in place, so the trial does not gain time by removing controls.
Ana | Make that explicit in the [[pilot trial::A pilot trial is a bounded test whose conditions and retained controls must be clear before interpreting results.]] description. Use comparable task conditions and the same measure, and record any new difficulties rather than reporting only the favorable observations.
Marcus | The improvement slide already lists twenty-four minutes saved. That is not right: twenty-four is the observed waiting total, and no trial result exists yet.
Ana | Correct it to proposed [[countermeasure::A countermeasure is an action intended to address a problem; it does not establish achieved savings before testing.]]. We can explain what the change is intended to address without booking the hoped-for benefit as an achieved result.
Marcus | After the trial, we should ask whether a reduction here created a tool shortage elsewhere. A faster bench would not necessarily mean a better overall flow.
Ana | Review the broader [[value stream::The value stream includes connected activities, so a local change must be assessed for effects elsewhere.]]. Local gains matter, but a change that simply transfers waiting to another step may not improve delivery to the customer.
Marcus | If the trial supports the change, the team still needs an approved method and follow-up. Otherwise the tool could gradually return to the old shared location.
Ana | That is [[sustainment::Sustainment concerns maintaining an accepted improvement through the agreed method and follow-up rather than a one-time result.]]. Update the agreed method through the proper process, clarify ownership, and monitor whether the improvement persists without weakening the required controls.''',
    transfer_title='Add people-time, not clock-time',
    transfer_setup='Four overlapping waiting episodes total 12 operator-minutes in a 30-minute observation. A new tool location is proposed, but no trial has run.',
    transfer='''Facilitator: "The accumulated waiting measure is ___." | operator-minutes | The case adds individuals' waiting time, including overlapping episodes.
Supervisor: "Average waiting per episode is ___ minutes." | three | Twelve operator-minutes divided by four episodes gives three per episode.
Facilitator: "The proposed tool location still needs a ___." | trial | No evaluation of the proposed location has yet been performed.
Supervisor: "We cannot report achieved ___ yet." | savings | A proposal has no measured improvement result before it is tested.'''))


BOOK['units'].append(unit(
    title='Defects, Scrap, and Rework',
    scene='One thousand units, three different states',
    skill='Reconcile output categories and explain yield, pending recovery, and scrap without double-counting or assuming a rework outcome.',
    brief='Quality analyst Priya and production manager Ellis review 1,000 inspected units from one batch. Exactly 900 passed on the first inspection, 60 are awaiting authorized rework, and 40 have an approved scrap disposition. These categories are mutually exclusive and account for all 1,000 units. No reworked units have yet been accepted. A summary labels all 100 non-first-pass units as scrap and forecasts 960 good units as though they already exist. Priya must correct both the loss and recovery statements.',
    cast='Priya | Quality analyst\nEllis | Production manager',
    culture=('Make the categories reconcile', 'A clear quantity discussion starts with the population and the mutually exclusive states. Separate completed results from expected recovery. This prevents a commercially attractive forecast from entering the good-unit count and avoids exaggerating waste by labeling all unfinished work as irreversible loss.'),
    a='''What is the first-pass yield? | 90% | 96% | 94% | 10% | Nine hundred first-pass accepted units divided by 1,000 inspected units gives ninety percent.
How many units have approved scrap disposition? | 40 | 100 | 60 | 900 | Only forty units are in the supplied scrap category; sixty await rework.
How many reworked units are already accepted? | None | 60 | 100 | 960 | The scenario explicitly states that no reworked units have yet been accepted.''',
    vocabulary='''defect | A product characteristic that fails an applicable quality requirement. | classify a defect
defective unit | A unit containing one or more defects under the stated definition. | count defective units
nonconforming unit | A unit that does not meet a specified requirement. | identify nonconforming units
scrap | Product designated not to be used for its original intended purpose. | record approved scrap
rework | Action intended to bring nonconforming product into conformity. | perform authorized rework
repair | Action making product acceptable for intended use without necessarily meeting every original requirement. | distinguish repair from rework
first-pass yield | The share of units meeting requirements on their first pass. | calculate first-pass yield
final yield | The share meeting the stated acceptance criteria after the defined processing stages. | state the final-yield basis
rework queue | Units waiting for the approved rework process. | monitor the rework queue
scrap rate | The scrapped quantity divided by the stated reference quantity. | report the scrap rate
disposition | An authorized decision about how identified material will be handled. | approve a disposition
acceptance status | Whether the required acceptance decision has been completed. | verify acceptance status
reinspection | Inspection after a corrective operation or under a defined repeat process. | complete reinspection
material reconciliation | Accounting for all material quantities across defined states. | perform material reconciliation
mutually exclusive categories | Groups defined so that an item belongs to only one of them. | use mutually exclusive categories
double-counting | Including the same item more than once in a total. | prevent double-counting
defect count | The number of individual defects, potentially more than one per unit. | distinguish defect count
unit count | The number of separate items in the measured population. | verify the unit count
cost of poor quality | Costs arising because products or processes fail to meet requirements. | assess cost of poor quality
scrap cost | The defined cost assigned to scrapped product or material. | calculate scrap cost
rework labor | Labor used to bring product into conformity through rework. | record rework labor
recovery assumption | A premise about the quantity expected to become acceptable. | qualify the recovery assumption
hold status | A controlled state preventing use pending the required decision. | maintain hold status
quality escape | Nonconforming product that passes beyond its intended detection point. | investigate a quality escape''',
    precision='900 first-pass units plus 60 awaiting rework plus 40 scrap equals 1,000 inspected units. First-pass yield is 90%; approved scrap is 4% of this population. The remaining 6% is pending rework, not already recovered output.',
    precision_extra='A unit may contain several defects, so defect counts and defective-unit counts are not interchangeable. Likewise, forecast recovery and accepted reworked quantity are different. If all 60 later pass, 960 accepted units would be a conditional future result, not the present count.',
    phrases='''Define the population | The report covers 1,000 inspected units from this batch.
State the first-pass result | Nine hundred met requirements on the first inspection.
Separate the pending quantity | Sixty units await authorized rework.
State irreversible disposition | Forty units have approved scrap disposition.
Reconcile the categories | These three exclusive states account for the full batch.
Correct the scrap total | The 100 non-first-pass units are not all scrap.
Keep recovery conditional | If all 60 pass after rework, the accepted total would be 960.
Report the current state | No reworked units have been accepted yet.
Name the yield basis | First-pass yield is 90% of the inspected population.
Name the scrap basis | The approved scrap quantity is 4% of these 1,000 units.
Distinguish defects and units | Two defects on one item are not two defective units.
Avoid double-counting | Move accepted reworked units between states rather than add them twice.
Separate costs | Scrap cost and rework labor are different cost categories.
Keep authorization visible | A rework plan does not remove the need for the required acceptance decision.
Correct the forecast label | Mark 960 as conditional recovery, not actual good output.
Close the report | Show current accepted, pending, and scrap quantities separately.''',
    notes='''Awaiting | Indicates a future action, not completed recovery.
Accepted | Requires the defined decision, not merely a planned repair.
Would | Signals a conditional result when the necessary event has not occurred.
First-pass | Excludes later recovery from the initial success measure.
Unit | One item; it may contain more than one defect.
Scrapped | A disposition state, not a synonym for every quality problem.''',
    d='''Which report reconciles the batch correctly? | 900 first-pass accepted, 60 awaiting rework, and 40 scrap | 960 accepted now and 100 scrap | 900 accepted and 100 confirmed scrap | 1,000 accepted because rework is planned | The three supplied mutually exclusive states total 1,000 without counting pending recovery as accepted.
If all 60 later pass the required acceptance process, what would the accepted total be? | 960, while first-pass yield remains 90% | 960, making the original first-pass yield 96% | 1,060 because the rework count is added twice | 900 because reworked units can never be accepted | Later acceptance can increase final accepted quantity without changing how many passed on their first attempt.
An inspected unit has three separate defects. Which statement is accurate? | It contributes one defective unit and three defects under those definitions. | It contributes three defective units. | It must be counted as three scrapped units. | Its defects prove every other unit is defective. | Unit count and defect count describe different measures and must not be substituted for one another.
Which financial statement is supported without further data? | Scrap quantity and pending rework are known; their complete costs are not supplied. | Total poor-quality cost is exactly 100 dollars. | Planned rework has no labor cost. | Every non-first-pass unit has the same financial consequence. | The case supplies quantities but no complete costing basis for scrap or rework.''',
    dialogue='''Ellis | The summary says one hundred units were scrapped, but the detailed report shows forty scrap and sixty awaiting rework. Which quantity should management use for the loss?
Priya | Use the approved [[scrap::Scrap is the forty-unit disposition category, not all one hundred units that failed to pass initially.]] quantity of forty. The other sixty are pending a different process, so combining them would misstate the current material states and their consequences.
Ellis | We should begin with the whole batch: one thousand inspected, nine hundred passed immediately, sixty waiting, and forty scrapped. That accounts for every unit once.
Priya | Those are [[mutually exclusive categories::Exclusive categories place each unit in one state, allowing the total to reconcile without overlap.]]. Keeping each unit in one current state makes the report reconcilable and prevents pending units from appearing simultaneously as accepted output and a loss.
Ellis | The dashboard uses ninety-six percent yield because it assumes all sixty can be recovered. That sounds optimistic before the work and acceptance checks are complete.
Priya | The [[first-pass yield::First-pass yield is 900 divided by 1,000, excluding any later rework recovery.]] is ninety percent. Nine hundred passed initially; a future recovery cannot change what happened on the first inspection.
Ellis | We can still show the possible recovery as a forecast, provided it is clearly conditional. The current accepted quantity is nine hundred, not nine hundred sixty.
Priya | Exactly. The sixty remain in the [[rework queue::The rework queue contains units awaiting the process, not units already recovered and accepted.]]. They have not yet completed the authorized work and required acceptance process, so they are not current good output.
Ellis | If all sixty eventually meet requirements, the accepted total would reach nine hundred sixty. The word would matters because the necessary outcome has not happened yet.
Priya | That is a [[recovery assumption::A recovery assumption describes a possible future accepted quantity and must not be reported as an achieved result.]]. Label it separately from actual results, and keep the condition that every reworked unit must meet the required acceptance criteria.
Ellis | Operations sometimes calls any corrective work repair. Should this report retain the authorized process name instead?
Priya | Keep [[rework::Rework aims to restore conformity to requirements, whereas repair can have a different acceptance basis.]] because the process is intended to bring the units into conformity. Repair can have a different meaning and acceptance basis, so casual substitution can confuse the decision.
Ellis | After the work, the report needs to reflect the actual checks and decisions. It should not move all sixty to good output just because a technician finished the operation.
Priya | Correct. The required [[reinspection::Reinspection provides the specified post-work inspection evidence and is not replaced by completion of the operation alone.]] and acceptance decision still matter. Completion of work is not by itself proof that the resulting units satisfy the relevant requirements.
Ellis | There is another reporting issue: one unit can have several defects. If the defect table lists three problems on one unit, the unit total must still count one.
Priya | Yes. The [[defect count::Defect count can exceed defective-unit count because one unit may contain several distinct defects.]] is not the defective-unit count. Define both measures if the report uses them, rather than letting the same number move between incompatible labels.
Ellis | When units change state after acceptance, we should update the pending balance. Otherwise the total could grow even though no new physical units were added.
Priya | That would be [[double-counting::Double-counting would include recovered units in both the pending and accepted states instead of transferring their status.]]. Move the accepted quantity out of the pending state when the decision is recorded, preserving the batch reconciliation throughout the update.
Ellis | I will correct the scrap figure and separate current accepted units from potential recovery. Finance can then use the right quantities without assuming scrap and rework cost the same.
Priya | Good. Complete the [[material reconciliation::Material reconciliation accounts for the batch across its actual states before quantities are used in cost or production summaries.]] before presenting costs. We know the quantities here, but not the full cost basis, so the report should not invent a monetary loss from these counts alone.''',
    transfer_title='Keep future recovery conditional',
    transfer_setup='A batch of 200 has 170 first-pass accepted units, 20 awaiting rework, and 10 approved scrap. No rework outcome is available.',
    transfer='''Analyst: "First-pass yield is ___ percent." | eighty-five | 170 divided by 200 is 0.85, or eighty-five percent.
Manager: "The pending rework quantity is ___." | twenty | Twenty units await rework and are not yet accepted recovered output.
Analyst: "Approved scrap is ___ units." | ten | The scrap category contains ten units, separate from pending rework.
Manager: "A total of 190 accepted units remains ___." | conditional | Reaching 190 requires all twenty pending units to pass the required acceptance process.'''))

BOOK['units'].append(unit(
    title='Root Cause and Corrective Action',
    scene='The supplier changed, but so did the process',
    skill='Challenge a premature root-cause statement, preserve competing hypotheses, and distinguish containment from verified corrective action.',
    brief='Process engineer Jun and quality lead Rosa investigate a fictional surface defect. It first appears in the records after a supplier switch, but two process settings also changed during the same period. Comparable lot and setting records have not yet been reconciled. A draft names the supplier as the confirmed root cause and calls temporary sorting a completed corrective action. Jun and Rosa must organize the evidence, keep the cause open, and distinguish immediate screening from work that prevents recurrence.',
    cast='Jun | Process engineer\nRosa | Quality lead',
    culture=('A hypothesis is not an accusation', 'Use conditional language to keep plausible explanations available for testing. This is not a refusal to decide; it identifies what evidence a decision requires. A supplier discussion can be direct about the observed defect without presenting timing alone as proof of responsibility.'),
    a='''What changed in the relevant period? | The supplier and two process settings | Only the supplier | Only the inspection report's color | No identified process input | Multiple changes occurred, so the timeline does not isolate the supplier as the cause.
What evidence is still unreconciled? | Comparable lot and process-setting records | A completed proof that every setting was constant | A final supplier admission | An approved effectiveness result | The brief says the relevant lot and setting records have not yet been reconciled.
What is the status of temporary sorting? | An immediate screening measure, not proof of recurrence prevention | A demonstrated permanent cause elimination | Evidence that the supplier definitely caused the defect | A completed effectiveness check for every future lot | Sorting can identify affected output while leaving the underlying cause unresolved.''',
    vocabulary='''root cause | An underlying cause whose removal addresses the problem's recurrence. | establish the root cause
symptom | An observable sign of a problem rather than its underlying explanation. | distinguish a symptom from a cause
hypothesis | A proposed explanation that can be examined against evidence. | test a hypothesis
correlation | An observed association that does not by itself establish causation. | distinguish correlation from causation
confounding factor | Another changing variable that can affect an apparent relationship. | identify confounding factors
change history | A record of relevant modifications over time. | reconstruct the change history
process parameter | A controllable or measured variable describing process operation. | review process parameters
lot traceability | The ability to link material and records to particular lots. | maintain lot traceability
comparative evidence | Information allowing relevant conditions or groups to be compared. | obtain comparative evidence
stratification | Separating data into meaningful groups for analysis. | stratify by supplier and setting
cause-and-effect diagram | A structured display of possible contributors to a problem. | build a cause-and-effect diagram
five whys | A questioning method used to explore successive levels of explanation. | use five whys carefully
8D | An eight-discipline structured approach to team problem solving. | prepare an 8D report
containment action | An immediate measure intended to limit the impact of a problem. | implement a containment action
sorting | Separating items using defined inspection or classification criteria. | document temporary sorting
escape point | The point at which a problem should have been detected but was not. | identify the escape point
occurrence cause | A cause explaining why the defect was produced. | verify the occurrence cause
detection failure | A reason an existing check did not identify the problem. | investigate a detection failure
corrective action | Action addressing a cause to prevent recurrence. | implement corrective action
effectiveness check | Evaluation of whether an action achieved its intended result. | define an effectiveness check
recurrence | The same or a related problem appearing again. | monitor recurrence
verification evidence | Recorded support that a specified condition or action has been achieved. | retain verification evidence
controlled comparison | A planned comparison that accounts for relevant differing conditions. | authorize a controlled comparison
closure criteria | Defined conditions for accepting an issue as resolved. | agree closure criteria''',
    precision='After the supplier switch describes timing, not a proven causal relationship. Two settings also changed, so those variables can confound the apparent supplier effect. Reconcile comparable records before treating one explanation as established.',
    precision_extra='Temporary sorting can limit escape of affected output without preventing the defect from being produced. A completed corrective action needs an identified cause, appropriate action, and the required effectiveness evidence. An analysis diagram organizes possibilities; it does not prove them.',
    phrases='''State the timing | The defect first appears after the supplier switch in the available records.
Identify competing changes | Two process settings changed during the same period.
Qualify the explanation | The supplier is one hypothesis, not a confirmed root cause.
Request comparable records | Link the defect data to the actual supplier lots and settings.
Separate association | The timing suggests a question; it does not establish causation.
Describe containment | Temporary sorting screens output while the investigation continues.
Distinguish prevention | Sorting does not by itself prevent the defect from being produced.
Keep the evidence organized | Stratify the observations by the relevant conditions.
Avoid an unsupported accusation | Ask for supplier records without stating a cause we have not established.
Check detection separately | Why did the existing check fail to identify the issue earlier?
Bound further work | Any comparison or trial must follow the authorized process.
Do not promote a diagram | A listed possible cause is not a verified finding.
Define effectiveness | Specify what evidence would show the action prevents recurrence.
Keep closure open | The issue remains open until the agreed criteria are met.
Assign the next review | Jun will reconcile the change and lot records for the next review.
Close with status | Containment is active; cause and corrective-action effectiveness remain unconfirmed.''',
    notes='''After | Indicates sequence, not automatically cause.
Because | Commits to an explanation that needs evidence.
Suspected | Keeps a plausible explanation open without declaring it confirmed.
Contained | Means impact is being limited, not necessarily that the cause is removed.
Verified | Must identify which proposition or action was checked.
Closed | Requires the agreed criteria, not merely a completed meeting or form.''',
    d='''Which root-cause statement fits the evidence? | The supplier change and two setting changes remain competing explanations pending comparison. | The supplier is proven responsible because its change came first. | The settings are proven responsible because there are two of them. | No investigation is possible when several things change. | Multiple simultaneous changes leave the cause unresolved but identify evidence that can help examine the alternatives.
What does sorting establish by itself? | A screening activity is being used; recurrence prevention is not demonstrated. | The occurrence cause is eliminated. | Every future lot will be defect-free. | The supplier admitted responsibility. | Sorting addresses detection or containment and does not by itself change the process producing the defect.
Which evidence request is most useful? | Reconcile defects with supplier-lot identities and actual settings under comparable conditions. | Ask only for opinions about the least popular supplier. | Delete records that conflict with the favored explanation. | Use the number of ideas on a diagram as proof. | The requested records connect outcomes to competing factors so the explanations can be examined.
What distinguishes an occurrence cause from a detection failure? | One explains production of the defect; the other explains why a check missed it. | Both always mean the supplier changed. | A missed check proves why the defect was created. | Eliminating a detection failure automatically eliminates occurrence. | Producing a defect and failing to detect it are distinct questions that may require different actions.''',
    dialogue='''Rosa | The draft says the new supplier is the root cause because the defect first appeared after the switch. I want to check whether the evidence really isolates that change.
Jun | It does not yet. The supplier is a [[hypothesis::The supplier is a possible explanation awaiting evidence, not a confirmed cause established by sequence.]]. Two process settings changed in the same period, and the comparable lot records have not been reconciled.
Rosa | Then we should retain the timeline but remove the causal conclusion. The fact that one event followed another is useful information without being sufficient proof.
Jun | Exactly. The observed [[correlation::Correlation describes association and does not isolate causation when other relevant variables also changed.]] does not establish which change produced the defect. We need to examine the competing explanations rather than select the easiest one to describe.
Rosa | The process settings could affect the result directly or interact with the supplied material. The current summary treats them as background details instead of relevant changes.
Jun | Each is a possible [[confounding factor::A confounding factor can influence the apparent relationship between the supplier switch and the defect.]]. If conditions changed together, we cannot attribute the outcome to the supplier alone without further supporting comparison.
Rosa | What should the evidence package contain? The identifiers in our defect, receiving, and machine records do not yet line up.
Jun | Reconstruct the [[change history::The change history establishes which modifications occurred and when, allowing records to be compared accurately.]] and link it to actual production. Dates in a meeting summary are not enough if the material or settings took effect at different times.
Rosa | We also need to know which supplier lot was used for each relevant run. Otherwise a supplier label at month level could hide the actual material sequence.
Jun | That is where [[lot traceability::Lot traceability connects specific material lots with production and defect records instead of relying on broad period labels.]] matters. Match the actual lots, settings, and observations before assuming that every unit made after the announcement used the new material.
Rosa | The sorting team has been screening output while we investigate. The draft calls that corrective action complete, which sounds stronger than the work establishes.
Jun | Call it a [[containment action::Containment limits impact while the cause is investigated; sorting alone does not demonstrate recurrence prevention.]]. Sorting may limit the movement of affected output, but it does not by itself stop the process from producing the defect.
Rosa | We should still evaluate the sorting method through the appropriate procedure. A temporary measure should not be treated as perfect simply because it is currently in place.
Jun | Agreed. And keep the [[occurrence cause::The occurrence cause explains why the defect was produced, a question separate from whether sorting detects it.]] separate from the screening question. One concerns why the defect is created; the other concerns whether the existing controls find it.
Rosa | That leaves a second investigation line: why the previous check did not flag the issue. Solving that could improve detection even before the production explanation is settled.
Jun | Yes, examine the [[detection failure::A detection failure explains why a check missed the problem and may require an action different from the production cause.]] on its own evidence. Do not assume that identifying a missed check also identifies the mechanism that created the defect.
Rosa | Once the evidence supports an action, we need a defined way to judge whether it worked. A completed supplier response form will not be enough.
Jun | Set an [[effectiveness check::An effectiveness check evaluates whether the action achieved the intended prevention result rather than merely being documented.]] with the appropriate criteria and review period. Any trial or process change must follow the authorized procedure rather than become an improvised production experiment.
Rosa | I will revise the status: containment active, supplier and setting hypotheses open, and record reconciliation assigned to you. We will not announce a cause before the evidence supports it.
Jun | Good. Keep the [[closure criteria::Closure criteria specify the evidence required before the issue can be accepted as resolved.]] visible so the team knows what remains. A clear open status is more useful than a closed label built on an untested explanation.''',
    transfer_title='Three changes, no isolated cause',
    transfer_setup='A defect appears after a material change and a temperature-setting change. No comparative analysis is complete. Temporary sorting is active.',
    transfer='''Engineer: "The material explanation is still a ___." | hypothesis | Multiple changes occurred, so the material has not been established as the cause.
Reviewer: "The setting change is a potential confounding ___." | factor | The other changing variable can affect the apparent material-defect relationship.
Engineer: "Temporary sorting is a containment ___." | action | Screening limits impact while the cause remains under investigation.
Reviewer: "Recurrence prevention still needs effectiveness ___." | evidence | Active containment does not establish that a corrective action prevents the defect from recurring.'''))


BOOK['units'].append(unit(
    title='Maintenance, Reliability, and Changeover',
    scene='A rush order meets the maintenance window',
    skill='Explain schedule conflicts, distinguish work types, and present conditional options without assuming authority to defer maintenance or restart equipment.',
    brief='Maintenance planner Leila and production scheduler Ben face a conflict. A planned two-hour maintenance window runs from 13:00 to 15:00, while a new rush order would need the same line through 14:00 under the current schedule. No technical assessment or authorization to defer maintenance is supplied. An alternative line might be available, but its suitability is unconfirmed. Leila and Ben must prepare options for the responsible decision maker without describing a possible workaround as an approved plan.',
    cast='Leila | Maintenance planner\nBen | Production scheduler',
    culture=('Acknowledge urgency without borrowing authority', 'A useful maintenance discussion separates customer pressure from the technical assessment and the authorized decision. State the conflict precisely and present options with their conditions. Avoid a casual we can just move it when the people in the conversation have not established that deferral is acceptable.'),
    a='''When do the two demands overlap? | From 13:00 to 14:00 | From 14:00 to 15:00 only | For the entire day | They do not overlap | Maintenance starts at 13:00 while the current rush-order schedule needs the line until 14:00.
What is known about maintenance deferral? | No supporting technical assessment or authorization is supplied. | It is automatically safe because the order is urgent. | Production has already authorized it. | Maintenance has no effect on reliability or safety. | The brief leaves the assessment and decision open rather than approving a schedule change.
What is the alternative-line status? | Possible but unconfirmed in suitability | Fully qualified and reserved | Proven to need no changeover | Already producing the order | A potential option does not establish the line's technical suitability, readiness, or allocation.''',
    vocabulary='''preventive maintenance | Planned work intended to reduce the likelihood of equipment failure. | schedule preventive maintenance
predictive maintenance | Maintenance informed by indicators of equipment condition or future failure. | use predictive maintenance
corrective maintenance | Work performed to restore function after a fault is identified. | plan corrective maintenance
condition monitoring | Tracking indicators of equipment health over time. | review condition-monitoring data
maintenance window | A reserved period for planned maintenance activity. | protect the maintenance window
work order | A controlled record authorizing and describing a defined maintenance task. | review the work order
backlog | Approved or identified work that remains unfinished. | prioritize the maintenance backlog
critical asset | Equipment whose failure has significant operational or other consequences. | identify critical assets
reliability | The ability to perform the required function over a stated period under stated conditions. | assess equipment reliability
maintainability | The ease and speed with which equipment can be maintained or restored. | improve maintainability
mean time between failures | Average operating time between failures for the defined repairable population. | interpret mean time between failures
mean time to repair | Average repair time under the stated measurement definition. | state the mean-time-to-repair basis
failure mode | The way in which an item fails to perform its function. | identify a failure mode
wear indicator | A measured or observed sign of component deterioration. | monitor wear indicators
spare-part readiness | Availability of the correct parts needed for the planned work. | confirm spare-part readiness
changeover | Transitioning equipment from one product or setup to another. | plan the changeover
setup time | The time required to prepare equipment for a specified job. | measure setup time
SMED | A setup-reduction approach distinguishing internal and external changeover work. | apply SMED principles
internal setup | Setup activity that requires the machine to be stopped. | identify internal setup tasks
external setup | Setup activity that can be completed while the machine is running. | separate external setup tasks
deferral | Postponement of a planned task subject to the required assessment and decision. | assess a maintenance deferral
return to service | The authorized restoration of equipment to operational use. | confirm return to service
capacity contingency | A conditional alternative for meeting production needs. | assess a capacity contingency
schedule dependency | A condition or predecessor affecting the timing of planned work. | identify schedule dependencies''',
    precision='The conflict is one hour, from 13:00 to 14:00, but moving a two-hour maintenance task may have consequences beyond that overlap. Its duration does not establish that it can be shortened, split, or deferred without the required assessment.',
    precision_extra='A changeover prepares for a different job; maintenance addresses equipment condition or function. Setup-reduction methods do not authorize skipping required maintenance or safety controls. An alternative line must be assessed before it becomes a credible production commitment.',
    phrases='''State the overlap | The order needs the line until 14:00, while maintenance starts at 13:00.
Keep duration distinct | A one-hour conflict does not mean a two-hour task can be completed in one hour.
Name the open assessment | We do not yet have a basis for deferring the maintenance.
Respect decision ownership | The responsible decision maker needs the technical assessment before approving a change.
Present a conditional option | An alternative line may be possible if suitability and readiness are confirmed.
Check more than space | An idle line is not automatically qualified for this order.
Separate work types | This is maintenance, not merely a product changeover.
Preserve required scope | Do not remove required work just to fit the schedule.
Request readiness information | Confirm the work scope, required parts, personnel, and dependencies.
Avoid a reliability guarantee | Recent operation does not prove the task can be postponed without consequence.
Qualify the finish time | The plan needs its conditions stated before we promise completion.
Keep return distinct | Finishing the work is not the same as authorized return to service.
Offer commercial alternatives | The decision maker can also assess a revised delivery commitment.
Record the actual decision | Update the schedule only after the authorized choice is documented.
Communicate the effect | Tell affected teams which line and time assumptions changed.
Close with next steps | Present the options and unresolved conditions together.''',
    notes='''Can | May describe physical possibility, capability, or permission; make the meaning clear.
Available | Does not necessarily mean suitable, qualified, or ready.
Deferred | Indicates a changed schedule, not evidence that the underlying need disappeared.
Completed | State whether work, checks, or return-to-service authorization is complete.
Changeover | A job transition, not a substitute word for every maintenance activity.
Contingency | A conditional alternative rather than a confirmed allocation.''',
    d='''Which schedule statement is accurate? | There is a one-hour overlap, but the maintenance scope remains two hours unless properly reassessed. | The maintenance must take only one hour because the overlap is one hour. | The order and maintenance never conflict. | The rush order automatically cancels the maintenance. | The overlap calculation does not shorten the planned work or authorize a schedule change.
Which alternative-line statement is best? | Assess suitability, setup, readiness, and allocation before committing the order. | Any idle line can run any product. | Availability alone proves qualification. | A possible alternative is already an approved schedule. | A credible contingency needs more than the possibility of unused capacity.
Which reply preserves authority? | We can present deferral for assessment, but it is not authorized in the current information. | We can skip it because production has a deadline. | No assessment is needed if the machine is currently running. | A planner's suggestion is sufficient return-to-service approval. | The supplied case contains no technical basis or authorized deferral decision.
What should be distinguished at the end of the work? | Task completion, required checks, and authorized return to service | Task completion and automatic proof of permanent reliability | A signed schedule and every safety decision | An unused spare part and a release decision | Completing maintenance does not automatically demonstrate that all required checks and authorization are complete.''',
    dialogue='''Ben | The rush order needs the line until fourteen hundred. Maintenance is booked from thirteen hundred to fifteen hundred, so the current schedule cannot satisfy both plans.
Leila | The [[maintenance window::The maintenance window is the reserved period from 13:00 to 15:00, which conflicts with the order schedule.]] overlaps the order by one hour. That does not mean the two-hour task can be shortened to one hour.
Ben | Could we move the work later? I need an option for the customer discussion, but I do not have the technical basis to say that postponement is acceptable.
Leila | Treat [[deferral::Deferral is a proposed postponement requiring the relevant assessment and authorization, neither of which is supplied here.]] as an option for assessment, not an approved decision. We need the responsible review before changing the commitment or telling the team to proceed.
Ben | The machine ran yesterday without a reported breakdown. I was tempted to use that as reassurance, although it may not answer the maintenance question.
Leila | It does not establish [[reliability::Reliability concerns performance over defined conditions and time, not a guarantee inferred from one recent operating period.]] for the proposed period. The task's purpose, equipment condition, and consequences need assessment rather than a conclusion based only on yesterday's operation.
Ben | What information should we bring to the decision maker? I can show the order timing and the impact on delivery, but the work scope needs your input.
Leila | We should review the [[work order::The work order identifies the defined maintenance task and its controlled scope for the scheduling assessment.]], required resources, and relevant dependencies. The schedule discussion must not silently delete part of the task to make the overlap disappear.
Ben | There may be another line free this afternoon. I have not checked whether it can run this product or what preparation would be needed.
Leila | Call it a [[capacity contingency::A capacity contingency is a conditional alternative whose suitability and readiness still need confirmation.]]. An unoccupied line is not automatically suitable, ready, or allocated to this order, so we cannot promise that route yet.
Ben | It would need a different product setup. That is separate from the maintenance on the original line, even though both activities take equipment time.
Leila | Correct. A [[changeover::A changeover transitions equipment to another job, while the original task concerns maintenance.]] prepares the alternative line for the job. Its scope and timing need review; it does not replace the original maintenance requirement.
Ben | The improvement team has discussed moving preparation outside stopped-machine time. We should not assume every preparation activity can be moved that way.
Leila | Exactly. [[External setup::External setup consists of eligible preparation while equipment runs; not every task can safely or appropriately be moved there.]] refers to eligible tasks that can occur while equipment runs. Required safety, quality, and operating controls still govern how the work is organized.
Ben | We also need the correct maintenance parts and people available. A calendar reservation alone does not demonstrate that the work can finish as planned.
Leila | Confirm [[spare-part readiness::Spare-part readiness establishes whether the correct needed parts are available for the planned scope.]] and the other resources. Missing items could change the plan, and the decision maker needs those facts alongside the customer timing.
Ben | Our options are therefore conditional: assess the alternative line, assess a permitted schedule change, or discuss a revised delivery commitment. None is confirmed yet.
Leila | Yes. Show each [[schedule dependency::A schedule dependency identifies a condition that must be resolved before the corresponding plan can be relied on.]] and the responsible owner. That makes the trade-off visible without allowing the rush order to become an unsupported technical authorization.
Ben | Once the authorized choice is recorded, I will update the affected teams. I will also avoid describing the equipment as ready merely because the work is reported finished.
Leila | Good. [[Return to service::Return to service is the authorized restoration of operational use after the relevant work and checks, not merely task completion.]] remains a distinct status. The final update should identify the completed work, required checks, and actual authorization before making a production commitment.''',
    transfer_title='An option still has conditions',
    transfer_setup='Maintenance is planned from 10:00 to 12:00. An order needs the same equipment until 11:00. A second line is possible but its suitability is unconfirmed.',
    transfer='''Planner: "The schedules overlap by ___ hour." | one | The shared period is 10:00 to 11:00, a one-hour overlap.
Technician: "Moving maintenance would be a proposed ___." | deferral | Postponement is not approved merely because an order conflicts with the window.
Planner: "The second line is a capacity ___." | contingency | The alternative remains conditional until its suitability and readiness are confirmed.
Technician: "Before using it, confirm its ___." | suitability | The briefing specifically leaves the second line's capability for the job unconfirmed.'''))

BOOK['units'].append(unit(
    title='EHS and Safety Communication',
    scene='Stop at the unclear instruction',
    skill='Raise an ambiguous safety instruction clearly, distinguish shutdown from energy control, and confirm the authorized clarification route.',
    brief='During a classroom safety exercise, operator Hana reads a training card saying switch off, then clean. Trainer Oscar confirms that the card does not identify the equipment, energy sources, or applicable isolation procedure. No actual equipment work is underway. Hana is not being authorized to service a machine. The exercise must stop at the ambiguous instruction and refer to the current approved equipment-specific procedure and qualified personnel. Hana and Oscar must clarify the communication without inventing an isolation sequence.',
    cast='Hana | Operator in a classroom exercise\nOscar | Safety trainer',
    culture=('A short stop message can be respectful', 'Safety clarification works best when the concern is specific and the pause is unambiguous. Say which instruction is unclear and what needs confirmation. Do not bury the concern in an apology or turn uncertainty into a request to guess the missing step.'),
    a='''Where is this exchange taking place? | In a classroom safety exercise with no equipment work underway | During an authorized live servicing operation | At a completed restart inspection | In a confirmed emergency rescue | The brief explicitly describes a classroom exercise and supplies no live-work authorization.
What is missing from the card? | Equipment identity, energy sources, and the applicable isolation procedure | The classroom's lunch menu only | A completed isolation verification result | Proof that the machine has no stored energy | The card lacks essential context and cannot supply a valid equipment-specific work instruction.
What must not be invented? | An isolation sequence for an unidentified machine | A clear statement that the card is ambiguous | A request for the approved procedure | A named clarification route | The task is to stop and clarify communication, not create a machine procedure without the required basis.''',
    vocabulary='''EHS | Environment, health, and safety functions and practices. | raise an EHS concern
hazard | A source or condition with the potential to cause harm. | identify a hazard
hazardous energy | Energy that can injure someone if unexpectedly released or applied. | recognize hazardous energy
energy isolation | Separation from energy sources using the applicable control method. | follow the energy-isolation procedure
lockout | Securing an energy-isolating device in the required safe position under the applicable procedure. | follow the lockout procedure
tagout | Use of a warning tag within an applicable energy-control system. | understand tagout limitations
stored energy | Energy remaining in a system after its normal supply is interrupted. | address stored energy
residual energy | Energy that remains after an initial control or shutdown action. | assess residual energy
shutdown | Stopping normal equipment operation. | distinguish shutdown from isolation
unexpected startup | Unintended equipment operation that can expose people to hazards. | prevent unexpected startup
authorized employee | A person assigned and trained for the relevant hazardous-energy-control work. | identify the authorized employee
affected employee | A person whose operation or work area is affected by energy-control activity. | inform affected employees
equipment-specific procedure | Approved instructions applicable to identified equipment and work. | consult the equipment-specific procedure
verification of isolation | Confirmation of the required isolated state using the approved method. | require verification of isolation
stop-work concern | A safety concern requiring work to pause under the applicable process. | raise a stop-work concern
near miss | An event that could have caused harm but did not in the observed outcome. | report a near miss
job hazard analysis | Review of job steps, associated hazards, and appropriate controls. | complete a job hazard analysis
permit to work | A formal authorization process for defined work where required. | verify permit-to-work requirements
personal protective equipment | Protective items worn to reduce exposure to specified hazards. | select required personal protective equipment
hierarchy of controls | An ordered approach to choosing hazard-control measures. | apply the hierarchy of controls
safety data sheet | A document describing a chemical's hazards and handling information. | consult the safety data sheet
exclusion zone | An area with controlled access because of defined hazards or work. | respect the exclusion zone
read-back | Repeating critical information to check shared understanding. | request a read-back
restart authorization | The required permission to resume equipment operation. | confirm restart authorization''',
    precision='Stopping normal operation is not the same as controlling every hazardous energy source. This classroom card does not identify a machine or an approved method. The correct language response is to pause and seek the applicable procedure, not supply missing operational steps.',
    precision_extra='A tag and a physical lock do not perform identical functions. Training participation does not by itself authorize a person for a particular task. Apply the actual energy-control program and assigned roles; no sentence in this exercise permits servicing or restart.',
    phrases='''State the concern | Stop here: the instruction does not identify the equipment or isolation procedure.
Keep the pause clear | We should not continue from this ambiguous card.
Distinguish the actions | Switching off is not the same as verifying energy isolation.
Identify missing context | Which equipment and approved procedure does this instruction refer to?
Request the controlled source | Use the current equipment-specific procedure.
Respect assigned roles | The relevant authorized personnel must handle the required assessment and work.
Avoid improvisation | I will not infer the missing sequence from a generic instruction.
Keep training separate | This classroom exercise does not authorize actual servicing.
Ask for confirmation | Please confirm the document identity and current revision.
Use read-back | I will repeat the clarified scope and next step to check understanding.
Avoid a false safe claim | We have no evidence here that any equipment is isolated.
Do not substitute protection | Protective equipment does not replace the required energy-control process.
Name the escalation | Oscar will refer the ambiguous card for correction through the training process.
Preserve the issue | Record the unclear wording so it is not reused unchanged.
Separate restart | A clarification does not itself authorize equipment restart.
Close the exercise | We will resume the classroom task only with the appropriate reviewed material.''',
    notes='''Stop | A clear pause instruction; do not dilute it with several uncertain alternatives.
Off | May describe a control state without establishing isolation.
Safe | A broad conclusion that needs a defined basis and scope.
Authorized | Refers to assigned role and required competence, not mere presence.
Verify | Requires the approved method; it is not a guess or visual assumption.
Read back | Confirms shared understanding but does not replace technical verification.''',
    d='''Which response best fits the ambiguous card? | Pause and obtain the current applicable equipment-specific procedure through the authorized route. | Guess a generic isolation sequence from memory. | Continue because the words switch off guarantee isolation. | Ask an unassigned learner to certify the machine safe. | The missing context requires clarification by the proper process, not invented operational instructions.
What does switching off establish by itself? | Normal operation may be stopped; complete energy isolation is not established. | All stored energy is necessarily removed. | Restart is authorized. | Every possible energy source has been verified controlled. | Shutdown and complete hazardous-energy control are distinct, so the broader conclusion is unsupported.
What can read-back confirm? | Shared understanding of the clarified message, not the physical isolated state | That every machine is safe to clean | That the learner is automatically authorized | That no approved procedure is needed | Repeating information checks communication and does not replace technical verification or role requirements.
Which closing statement is accurate? | The ambiguous classroom card is referred for correction; no equipment work or restart is authorized. | The equipment is now isolated because the discussion ended. | Every participant can now perform servicing independently. | The unclear card is acceptable if someone signs it. | The exercise identifies a communication problem without supplying live-work or restart authorization.''',
    dialogue='''Hana | I want to stop at this line. The card says switch off, then clean, but it does not identify the machine or the procedure we should be using.
Oscar | That is a clear [[stop-work concern::The concern calls for a pause at the ambiguous instruction rather than guessing a work sequence.]]. We are in a classroom exercise, and we should not continue as though the missing equipment information were already known.
Hana | The phrase switch off sounds simple, but it could refer only to stopping normal operation. It does not tell me what happens to other energy sources.
Oscar | Correct. [[Shutdown::Shutdown stops normal operation but does not establish that every hazardous energy source has been controlled.]] is not the same as complete energy control. This card gives us no basis for declaring any machine isolated or safe for the proposed work.
Hana | There could also be energy remaining after a normal stop. I should not assume that the absence of movement proves there is nothing left that could cause harm.
Oscar | Exactly. [[Stored energy::Stored energy can remain after normal supply or operation stops, so it cannot be dismissed from a generic off instruction.]] must be addressed through the applicable process. We will not improvise that process for unidentified equipment during a language exercise.
Hana | Then the next step is to identify the equipment and obtain the approved instructions that actually apply. A generic training phrase is not enough.
Oscar | We need the current [[equipment-specific procedure::The equipment-specific procedure supplies the approved instructions for identified equipment rather than a generic classroom shortcut.]] and the relevant qualified personnel. The correct document and assigned roles matter as much as the words on the card.
Hana | I understand the need to ask, but I do not want my question to sound as though I am volunteering to perform the isolation myself.
Oscar | You are not. The [[authorized employee::The authorized employee has the assigned role and required training for the relevant energy-control work.]] has an assigned role and the required training. Participating in this discussion does not give you that authorization.
Hana | Some learners also treat a tag as though it physically prevents the same actions as a lock. We should make the distinction clear without demonstrating an unapproved method.
Oscar | Yes. [[Tagout::Tagout uses warning tags within the applicable system and must not be assumed to provide the same physical restraint as a lock.]] has particular functions and limitations under the applicable system. A warning tag must not be described as providing identical physical restraint to a lock.
Hana | Once the correct information is available, I can repeat the equipment identity and the next communication step. That would help confirm that I heard the clarification correctly.
Oscar | That is [[read-back::Read-back checks shared understanding of critical information but does not establish a physical equipment condition.]]. It checks our shared understanding; it does not replace the required technical process or demonstrate that the equipment has reached a particular state.
Hana | So the class should not write isolated on the worksheet merely because we have discussed the concept. We have not performed or observed any equipment work.
Oscar | Correct. [[Verification of isolation::Verification of isolation requires the approved technical method, which has not occurred in this classroom discussion.]] is a separate technical requirement under the applicable procedure. Our conversation does not establish that it has occurred.
Hana | I will keep the concern specific: missing equipment identity and procedure. The training card needs correction, rather than a handwritten guess about the missing steps.
Oscar | I will refer it through the [[EHS::EHS identifies the environment, health, and safety function involved in addressing the safety-related training issue.]] and training process. We should preserve the unclear wording so the responsible people can review and correct the source.
Hana | Then we pause this part of the exercise until the reviewed material is available. No one should interpret the clarification as permission to start cleaning a machine.
Oscar | Exactly. It also provides no [[restart authorization::Restart authorization is a separate required permission and is not created by completing a classroom clarification.]]. The outcome today is a clear concern, a proper referral, and an explicit boundary between classroom communication and actual equipment work.''',
    transfer_title='Clarification is not authorization',
    transfer_setup='A classroom card omits the machine identity and approved procedure. No live equipment work has occurred. The trainer will obtain reviewed material.',
    transfer='''Learner: "The equipment identity is ___." | missing | The card omits the specific machine, so its identity cannot be assumed.
Trainer: "We must obtain the applicable approved ___." | procedure | A generic card cannot replace the required equipment-specific instructions.
Learner: "This discussion remains a classroom ___." | exercise | The case supplies no actual equipment work or servicing authorization.
Trainer: "It does not authorize a ___." | restart | A training clarification does not provide permission to resume equipment operation.'''))


BOOK['units'].append(unit(
    title='Supplier Quality and Incoming Materials',
    scene='One dimension, two drawing revisions',
    skill='Compare measured results against explicit revision limits and resolve the governing requirement before assigning responsibility or release status.',
    brief='Supplier-quality engineer Farah and supplier contact Colin review a component measured at 12.18 mm. The incoming report omits the drawing revision. The inspector used revision C, specifying 12.00 plus or minus 0.10 mm; the supplier used revision B, specifying 12.20 plus or minus 0.10 mm. Which revision governs the order has not been confirmed. The lot is held pending review. Farah and Colin must state both comparisons accurately, trace the order documents, and avoid declaring either party responsible before resolving the requirement.',
    cast='Farah | Supplier-quality engineer\nColin | Supplier quality contact',
    culture=('Resolve the reference before arguing about compliance', 'Two people can make internally consistent statements while using different documents. Put the requirement identity and revision beside the result, then trace the agreed order. This avoids treating a reference mismatch as dishonesty and keeps the discussion focused on evidence and responsibility.'),
    a='''What is the revision C range? | 11.90 to 12.10 mm | 12.10 to 12.30 mm | Exactly 12.18 mm only | 11.00 to 13.00 mm | A nominal 12.00 mm with a tolerance of 0.10 gives limits of 11.90 and 12.10.
How does 12.18 mm compare with revision B's stated range? | It lies within 12.10 to 12.30 mm. | It exceeds 12.30 mm. | It is below 12.10 mm. | It determines that revision B governs the order. | The measurement is within the stated B limits, but that comparison does not establish the governing revision.
What remains unconfirmed? | Which drawing revision governs this order | The reported measured value | That the inspector used C | That the supplier used B | The brief supplies both references but not the agreed revision applicable to the order.''',
    vocabulary='''engineering drawing | A controlled technical representation of product requirements. | consult the engineering drawing
drawing revision | The identified version of a technical drawing. | confirm the drawing revision
nominal dimension | The stated target or reference size. | identify the nominal dimension
tolerance | The permitted variation from a specified value. | apply the stated tolerance
upper specification limit | The largest value permitted by the stated requirement. | check the upper specification limit
lower specification limit | The smallest value permitted by the stated requirement. | check the lower specification limit
measured value | The result reported by the measurement process. | record the measured value
measurement unit | The scale used to express a measurement, such as millimeters. | state the measurement unit
inspection characteristic | A specified feature selected for inspection. | identify the inspection characteristic
inspection report | A record of examined features, methods, and results. | correct the inspection report
purchase order | The commercial document defining the ordered goods and referenced requirements. | review the purchase order
order acknowledgment | The supplier's confirmation of the order terms it received or accepted. | compare the order acknowledgment
applicable revision | The document version governing the specified work or order. | establish the applicable revision
document discrepancy | A mismatch between relevant records or references. | resolve a document discrepancy
controlled copy | A document copy maintained under the applicable version-control process. | obtain the controlled copy
superseded revision | A version replaced by a later one in the relevant document system. | identify a superseded revision
engineering change notice | A controlled communication describing an approved technical change. | trace the engineering change notice
effectivity | The point or population from which a change applies. | confirm change effectivity
supplier flow-down | Communication of applicable requirements through the supply chain. | verify supplier flow-down
receiving record | Documentation of material received and its identifying details. | trace the receiving record
lot identity | The identifier linking material to a specific batch. | preserve lot identity
acceptance basis | The requirements and evidence used for an acceptance decision. | state the acceptance basis
deviation request | A request for authorized departure from a specified requirement. | review a deviation request
release decision | The authorized determination that material may proceed to use or distribution. | document the release decision''',
    precision='Revision B permits 12.10 to 12.30 mm; revision C permits 11.90 to 12.10 mm. The measured 12.18 mm is within the supplied B limits and 0.08 mm above C\'s upper limit. Neither comparison decides which revision governs the order.',
    precision_extra='Latest in a drawing system and applicable to this order are not necessarily identical. Review the order, acknowledgment, change communication, and effectivity. A numerical pass against one reference does not itself authorize release when the governing requirement remains unresolved.',
    phrases='''State the result fully | The reported dimension is 12.18 millimeters.
Name the missing reference | The inspection report does not identify the drawing revision.
Show both bases | The inspector used C; the supplier used B.
Read the C limits | Revision C permits 11.90 to 12.10 millimeters.
Read the B limits | Revision B permits 12.10 to 12.30 millimeters.
Report the comparison | The result is within B's stated limits and above C's upper limit.
Avoid premature blame | We have not established which revision governs the order.
Trace the agreement | Compare the purchase order with the supplier acknowledgment.
Check the change timing | Confirm when revision C became applicable to this order or lot.
Preserve the original record | Add the corrected reference through the controlled process.
Keep the hold visible | The lot remains held pending the required review.
Separate dimension and release | Meeting one dimensional range is not the complete release decision.
Request the controlled source | Send the referenced drawing and relevant change communication.
Clarify a departure | A deviation request is not already an approved exception.
Record the resolution | Document the applicable revision and the resulting assessment.
Close the supplier exchange | Resolve the requirement basis before assigning responsibility or promising release.''',
    notes='''Within | Names a comparison to defined limits; it does not identify which limits apply.
Latest | Describes version chronology, not necessarily contractual effectivity.
Applicable | Connects a requirement to the particular work, order, or lot.
Plus or minus | Sets symmetric limits around the stated nominal value.
Acknowledged | Records the supplier's response; compare it with the actual order terms.
Released | Requires the relevant authorization, not merely a favorable number.''',
    d='''What is the difference between 12.18 mm and revision C's upper limit? | 0.08 mm above the limit | 0.18 mm above the limit | 0.02 mm below the limit | 0.10 mm below the limit | The upper limit is 12.10 mm, and 12.18 minus 12.10 equals 0.08 mm.
Which supplier statement is most precise? | The result meets the supplied B dimensional range; we still need to confirm whether B governs this order. | The result meets B, so the entire lot is automatically released. | The inspector is dishonest because C has a different limit. | A newer revision can never affect an existing order. | The precise statement separates the numerical comparison from the unresolved applicable requirement.
Which evidence best addresses the mismatch? | Order references, acknowledgment, drawing versions, and change effectivity records | Only the most recent filename in someone's downloads | The supplier's production deadline alone | A verbal claim that both revisions are equivalent | The relevant records connect the agreed requirement and change timing to the particular order and lot.
How should the report be corrected? | Add the missing revision and resolution through the controlled record process while retaining traceability. | Replace the result silently so it appears to meet C. | Delete the original record and release immediately. | Remove units and tolerances to avoid disagreement. | The correction must preserve the measured result and traceable requirement basis rather than obscure the discrepancy.''',
    dialogue='''Colin | Our report shows twelve point one eight millimeters within tolerance, but your incoming record calls it a failure. The two teams may be using different requirements.
Farah | The missing reference is the [[drawing revision::The drawing revision identifies the requirement version needed to interpret the inspection result.]]. Our inspector used revision C, while your team used B, and the incoming report omitted that distinction.
Colin | Revision B specifies twelve point two zero, plus or minus zero point one zero. That gives the range we used when assessing the measured feature.
Farah | Its [[lower specification limit::Subtracting 0.10 from the B nominal 12.20 gives the lower permitted value of 12.10 mm.]] is twelve point one zero, with an upper limit of twelve point three zero. The reported result falls within that stated range.
Colin | Revision C has a lower nominal value. I want to state its limits accurately rather than argue that a favorable result against our copy resolves everything.
Farah | C's [[upper specification limit::Adding 0.10 to the C nominal 12.00 gives the upper permitted value of 12.10 mm.]] is twelve point one zero. The lower limit is eleven point nine zero, so the result is zero point zero eight above C's upper limit.
Colin | Then both comparisons can be stated without contradiction. The disagreement concerns which version applies, not whether twelve point one eight is the reported measurement.
Farah | Correct. The [[measured value::The measured value remains 12.18 mm; differing reference limits change its interpretation, not the recorded number.]] stays unchanged. We must not alter it to fit either drawing or let the missing reference obscure what the inspection actually recorded.
Colin | Our production team says B was attached to the order package. We should provide that package, although we still need to compare it with your purchasing records.
Farah | Please send the [[order acknowledgment::The acknowledgment records the supplier's received or accepted terms and can be compared with the purchase order references.]] and referenced drawing. I will check the purchase order so we can establish the agreed requirement rather than rely on separate recollections.
Colin | There may also have been a change notice after the order was placed. A newer document exists, but I do not yet know when it was intended to apply.
Farah | We need its [[effectivity::Effectivity specifies when or to which population the technical change applies, resolving more than simple revision chronology.]]. Latest in the document system does not automatically tell us whether the change governed this particular order or lot.
Colin | If the updated requirement was meant to apply, we should trace how it was communicated. That will help identify the actual mismatch instead of simply assigning blame.
Farah | Review the [[supplier flow-down::Supplier flow-down concerns how applicable requirements were communicated through the supply chain.]] evidence. The communication record may be important, but we should not state a responsible party before we have reconciled the order and change history.
Colin | In the meantime, can you release the lot because it meets B's dimension? The production team is asking for a delivery update.
Farah | No release is established by that comparison alone. The [[acceptance basis::The acceptance basis remains unresolved while the applicable revision is unknown, so a favorable B comparison cannot settle release.]] is still under review, and the lot retains its hold status until the required decision is made.
Colin | We can discuss a formal exception if needed, but I understand that asking for one would not itself authorize use against a requirement.
Farah | Exactly. A [[deviation request::A deviation request seeks an authorized departure and is not itself approval of that departure.]] would follow the applicable process. It must not be treated as an approved exception simply because someone needs the material urgently.
Colin | I will send the order acknowledgment, drawing copy, and any change communication. The update will state both numerical comparisons without promising that the lot can be used.
Farah | Good. Once the governing requirement and evidence are resolved, document the actual [[release decision::The release decision is the authorized result of the review, not an assumption drawn from one favorable comparison.]]. Correct the report through the controlled process and preserve the original measurement and reference history.''',
    transfer_title='Pass against which revision?',
    transfer_setup='A measurement is 5.08 mm. Revision A allows 4.90-5.10 mm; revision B allows 4.95-5.05 mm. The governing revision is unconfirmed and the lot remains held.',
    transfer='''Engineer: "The result is within revision ___ limits." | A | 5.08 lies between the supplied A limits of 4.90 and 5.10.
Supplier: "It exceeds revision B's upper ___." | limit | 5.08 is above the B upper permitted value of 5.05.
Engineer: "The applicable revision remains ___." | unconfirmed | The case does not establish which reference governs the order.
Supplier: "The lot has not been ___." | released | The material remains held, so neither comparison supplies release authorization.'''))

BOOK['units'].append(unit(
    title='Shift Handoffs and Escalation',
    scene='Six checks complete, two still open',
    skill='Transfer unfinished work with specific identifiers, evidence, ownership, dependencies, and a confirmed next update.',
    brief='Outgoing supervisor Diego hands lot L27 to incoming supervisor Elena. Six of eight required release checks are complete, with records attached. Check 7, label-count reconciliation, remains open; check 8, final quality review, depends on it. Site procedure requires all eight before lot release. Elena is the named incoming supervisor but has not yet confirmed receipt. A draft handoff says 75% ready and should be fine. Diego and Elena must replace that reassurance with a precise status and a closed-loop handoff.',
    cast='Diego | Outgoing supervisor\nElena | Incoming supervisor',
    culture=('Ownership is not completion', 'An incoming supervisor can accept responsibility for follow-up without declaring the work finished. A good read-back identifies the open tasks and restrictions, not just the phrase got it. This matters especially when a friendly handoff risks turning an optimistic expectation into an apparent release decision.'),
    a='''Which checks remain open? | Check 7 label-count reconciliation and check 8 final quality review | All eight checks | None because six are complete | Only an unspecified optional check | The brief identifies two specific required checks and their dependency.
What is required before lot release? | Completion of all eight required checks under the site procedure | A 75% completion percentage alone | A friendly verbal reassurance | Merely naming the incoming supervisor | The supplied site procedure requires every release check, not a partial completion threshold.
What has Elena not yet confirmed at the start? | Receipt of the handoff | That Diego is on the outgoing shift | That the lot is called L27 | That eight checks exist | A named recipient is not proof that the information has been received and understood.''',
    vocabulary='''shift handoff | Transfer of relevant work status and responsibility between shifts. | conduct a shift handoff
outgoing shift | The team ending its scheduled work period. | brief the outgoing shift
incoming shift | The team beginning responsibility for the next period. | inform the incoming shift
open item | A task or issue that has not met its completion criteria. | identify open items
completed check | A required check with its completion evidence recorded. | verify completed checks
release checklist | The defined checks required for a material or product release decision. | review the release checklist
label reconciliation | Accounting for issued, used, unused, and rejected labels as required. | complete label reconciliation
final quality review | The designated review of the required evidence before a release decision. | complete the final quality review
dependency | A task or condition that must be resolved before another can proceed. | identify a task dependency
handoff record | The documented status and responsibilities transferred between teams. | update the handoff record
attachment | A supporting file or record linked to the handoff. | verify the attachment
record reference | An identifier locating the supporting evidence. | provide the record reference
named owner | A specifically identified person responsible for an action. | assign a named owner
acknowledgment | Confirmation that information or responsibility has been received. | obtain acknowledgment
closed-loop communication | An exchange in which receipt and understanding are confirmed. | use closed-loop communication
read-back | Repetition of key information to verify shared understanding. | request a read-back
next checkpoint | The agreed time or event for the next status review. | set the next checkpoint
due time | The time by which a task is expected or required to be complete. | distinguish due time from update time
escalation trigger | A condition requiring referral to the next responsible level. | define an escalation trigger
handover acceptance | Confirmation of responsibility for the transferred follow-up. | record handover acceptance
status qualifier | A word or phrase defining the limits of a reported status. | preserve status qualifiers
pending decision | A required determination that has not yet been made. | flag a pending decision
continuity | Preservation of information and control across changes of personnel. | maintain continuity
audit trail | A traceable history of records, actions, and decisions. | preserve the audit trail''',
    precision='Six of eight checks is 75% by count, but it is not 75% release authorization or a measure of remaining risk. The supplied procedure requires all eight. Name the two open checks and keep the lot-release restriction explicit.',
    precision_extra='An update time is not a guaranteed completion time. Receipt, ownership, task completion, and release are distinct statuses. The final quality review depends on label reconciliation, so assigning both tasks does not remove their sequence.',
    phrases='''Identify the lot | This handoff concerns lot L27.
State completed work | Six required checks are complete, with the records attached.
Name each open item | Check 7 is label reconciliation; check 8 is final quality review.
Describe the dependency | The final review depends on completion of the reconciliation.
Keep release explicit | The lot is not released while the required checks remain open.
Replace vague reassurance | Please remove should be fine from the status.
Name the recipient | Elena is the incoming supervisor responsible for follow-up.
Confirm receipt | Please confirm you can access the attached records.
Request a precise read-back | Repeat the two open checks and the release restriction.
Separate ownership | Accepting the handoff does not mean the checks are complete.
Set an update | Agree the next checkpoint without promising an unverified finish time.
Define escalation | If required evidence is unavailable, follow the site's escalation route.
Preserve references | Keep the record identifiers beside the completed checks.
Avoid a misleading percentage | Seventy-five percent counts checks; it does not authorize release.
Record changes | Update each status when supporting evidence becomes available.
Close the loop | Confirm the handoff, owner, open items, and next communication.''',
    notes='''Ready | Specify ready for what: handoff, review, or release.
Done | Needs an identified task and supporting completion evidence.
Should be fine | Reassurance that does not describe actual status or restrictions.
Accepted | May mean ownership accepted, not product accepted; name the object.
By | Can imply a deadline; do not use it for an update unless that meaning is clear.
Pending | Preserves an unresolved task or decision rather than predicting its outcome.''',
    d='''Which handoff line is most useful? | L27: checks 1-6 complete; 7 reconciliation and 8 final review open; lot not released. | L27 is 75% ready and should be fine. | All checks complete because the incoming supervisor is named. | L27 released subject to two required checks that have not occurred. | The line identifies the actual completed and open work and preserves the stated release restriction.
What does Elena's acknowledgment establish? | Receipt and accepted follow-up responsibility, not completed checks | Automatic completion of label reconciliation | Final quality approval | Permission to ignore the dependency | A handoff acknowledgment confirms communication and ownership, not technical completion or release.
The teams agree an update at 09:00. Which interpretation is safest and most precise? | A status report is due at 09:00; completion is not guaranteed unless separately established. | Both checks must already be complete because an update time exists. | The lot is released at 09:00 regardless of results. | No communication is needed unless everything finishes. | An agreed checkpoint concerns reporting status and should not be turned into an unsupported completion promise.
Which task order matches the brief? | Complete label reconciliation before the dependent final quality review. | Complete final review by assuming reconciliation will pass later. | Mark both complete when the attachments are opened. | Remove check 7 because six others are finished. | The brief explicitly makes final quality review dependent on the completed reconciliation.''',
    dialogue='''Diego | This handoff covers lot L27. Six of the eight required checks are complete, but the draft says seventy-five percent ready and should be fine.
Elena | Please replace that with the actual [[open item::An open item is unfinished work that must be named, rather than hidden behind a readiness percentage.]] list. A percentage by check count does not tell me which work remains or whether the lot can be released.
Diego | Check seven is label-count reconciliation. Check eight is the final quality review, and that review depends on the completed reconciliation.
Elena | I will preserve that [[dependency::The dependency requires label reconciliation to be completed before the final quality review can be completed.]]. Assigning both tasks does not make them independent or allow the final review to assume a result that is still missing.
Diego | The completed-check records are attached, with identifiers next to checks one through six. I have named you as the incoming supervisor, but I still need confirmation.
Elena | First, let me verify each [[attachment::Attachments are the supporting records whose availability must be confirmed, not assumed from a sent message.]] is accessible. A file listed in a message is not useful evidence if the incoming team cannot open it or identify what it supports.
Diego | Thank you. The site procedure requires all eight checks before release, so the two unfinished checks mean L27 has not been released.
Elena | That restriction belongs beside the [[release checklist::The release checklist defines the required checks, all of which remain necessary before the stated release decision.]]. Six completed items do not reduce the requirement to finish the other two, regardless of how reassuring the summary sounds.
Diego | I will remove should be fine. It was meant as encouragement, but it could be read as permission to proceed despite the unfinished work.
Elena | Use a clear [[status qualifier::A status qualifier such as not released states the limits of the current condition rather than offering vague reassurance.]] instead: not released, two checks open. That tells the team what the status means without suggesting a result we do not have.
Diego | Can you confirm the records and the two remaining checks now? I want the handoff to be more than a message sent just before I leave.
Elena | Yes. Here is my [[read-back::Read-back repeats the critical lot status, open checks, and restriction to confirm shared understanding.]]: L27, checks one through six complete; seven reconciliation and eight final review open; final review depends on seven; no release yet.
Diego | That matches. You are taking responsibility for coordinating the follow-up, but the record should not mark either check complete just because you accepted the handoff.
Elena | Correct. Record [[handover acceptance::Handover acceptance confirms responsibility for follow-up and does not establish technical completion of the remaining checks.]] separately from check completion. I accept the follow-up responsibility; the actual check results and authorized decision still need their own evidence.
Diego | Let's agree a status update at nine tomorrow. I cannot promise that the reconciliation and final review will both finish by then.
Elena | Nine will be the [[next checkpoint::The next checkpoint is an agreed status-review time, not a guaranteed completion or release time.]], not a guaranteed finish time. I will report the actual status and any unresolved issue rather than make completion a condition for communicating.
Diego | If a required record is unavailable, we need the team to use the site's escalation process instead of treating silence as permission to move the lot.
Elena | I will state that [[escalation trigger::The trigger identifies the missing evidence condition that requires referral through the site's responsible process.]] in the handoff. The appropriate route remains the site process; I will not invent an alternative approval because a record is delayed.
Diego | The corrected record now names the lot, evidence, two open checks, dependency, release restriction, owner, and update time. That is clearer than a readiness percentage.
Elena | It also preserves the [[audit trail::The audit trail records who knew and accepted what, alongside later evidence and decisions, without rewriting earlier uncertainty.]]. Later updates can show when each check was completed and who made the decision, without changing what was actually open at this handoff.''',
    transfer_title='Acknowledged is not completed',
    transfer_setup='Lot M8 has three of four required checks complete. The last review is open. Noor accepts follow-up responsibility and agrees to provide an update at 16:00, with no completion guarantee.',
    transfer='''Outgoing lead: "The final review remains ___." | open | Three completed checks leave the fourth review unfinished.
Noor: "I accept follow-up ___." | responsibility | Noor accepts ownership of the follow-up rather than declaring the review complete.
Outgoing lead: "Sixteen hundred is the agreed update ___." | time | The checkpoint is a reporting time, not a guaranteed completion time.
Noor: "The handoff does not itself authorize ___." | release | An accepted handoff cannot replace the remaining required review or release decision.'''))
