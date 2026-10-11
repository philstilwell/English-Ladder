"""Original workplace-English cases for analytics and business-intelligence teams."""
from books.authoring import unit

BOOK = dict(
    slug='data-analytics-business-intelligence',
    title='Data Analytics and Business Intelligence English',
    cover_label='METRICS / QUALITY / MODELS / DECISIONS',
    cover_title='Data Analytics\n& Business Intelligence', cover_size=28,
    tagline='Define the measure. Make the finding useful.',
    audience='For analysts, analytics engineers, reporting specialists, and business partners discussing evidence and decisions.',
    map_intro='Eight analytics conversations move from conflicting definitions and data-quality checks to trustworthy calculations, careful inference, and actionable recommendations.',
    notes_title='A number needs a definition and a purpose.',
    notes_intro='Analytics work often fails in the conversation after the calculation. Teams may use one label for different events, confuse a refresh time with source coverage, or present a promising estimate as a guaranteed effect. These cases supply the facts and practice the language that keeps a useful conclusion attached to its actual evidence.',
    field_notes=[
        ('Agree what is being counted', 'Name the entity, event, window, and exclusions. A familiar metric label is not a complete definition.', '"We counted distinct users with a completed transaction during September."'),
        ('Put the denominator into speech', 'A percentage needs an eligible total. Say whether a change is relative or in percentage points.', '"That is 480 of 500 cases, or 96%, one point above target."'),
        ('Keep the limitation near the claim', 'Qualify source coverage and uncertainty where the result is reported, not only in an appendix.', '"The dashboard refreshed today; refunds are complete only through Monday."'),
        ('End with a bounded recommendation', 'Connect the finding to an action, owner, and review point without claiming that the cause is already known.', '"Approve a two-day investigation of the documented service issue."')],
    scope_note='Original fictional English practice, not statistical certification, legal advice, a privacy determination, or authorization to use customer data. All datasets, thresholds, local approval rules, and business decisions are invented. Actual analysis must follow the applicable definitions, methods, access controls, and responsible review.',
    sources=[
        dict(title='UK Government. The Government Data Quality Framework.', url='https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework', note='Background for fit-for-purpose data, quality dimensions, and communicating limitations. The dashboard sources and freshness criteria here are fictional.', checked='30 September 2026'),
        dict(title='PostgreSQL Documentation. Table Expressions.', url='https://www.postgresql.org/docs/current/queries-table-expressions.html', note='Background for join and grouping behavior. The order-and-payment examples are original, small teaching datasets rather than production queries.', checked='30 September 2026'),
        dict(title='NIST/SEMATECH e-Handbook. What Are Confidence Intervals?', url='https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm', note='Background for interval estimates and uncertainty language. The supplied experiment interval is fictional and is interpreted, not estimated from raw observations.', checked='30 September 2026'),
        dict(title='Information Commissioner\'s Office. Principle (c): Data Minimisation.', url='https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/data-minimisation/', note='Background for purpose-linked data selection. This UK guidance is under review; the exercises use explicit fictional local rules, not universal legal conclusions.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Metric Definitions and Business Questions',
    scene='Two active-user totals, two different events',
    rehearsal=['Read turns 1-10. Stress qualifying event and denominator as separate choices.', 'Switch roles for turns 11-20. Keep the subset relationship clear when rejecting addition.', 'Check the transfer. Read 40% and 50% with their different population bases.'],
    skill='Reconcile apparently conflicting metrics by stating the event, distinct entity, window, and denominator.',
    brief='Analyst Mei and product lead Rafael compare September figures for the same 2,000 eligible users, using UTC calendar boundaries and excluding internal and test accounts. One report counts 1,200 distinct users with a successful login. Another counts 900 distinct users with a completed transaction. All 900 are within the login group. Both queries match their stated definitions. The business question is how many eligible users completed a transaction, not how many signed in. The team must choose an accurate label and rate.',
    cast='Mei | Data analyst\nRafael | Product lead',
    culture=('Treat a disagreement as a definition check', 'When two teams defend different totals, ask what each number counts before deciding which team made an error. Preserve useful measures with accurate names. A measure can be correctly calculated yet poorly suited to the business question on the table.'),
    a='''Which count answers the supplied business question? | 900 distinct users with a completed transaction | 1,200 distinct users with a login | 2,100 users obtained by adding the groups | 2,000 completed transactions | The question concerns eligible users completing transactions, which the second measure directly counts.
What is the correct eligible-user transaction rate? | 45% | 60% | 75% | 105% | Nine hundred divided by two thousand eligible users equals forty-five percent.
Why can both query results be correct? | They apply different event definitions to the same eligible population. | Every metric must have the same count. | The larger number is always more accurate. | A login and a transaction are identical events. | Distinct event definitions can produce different accurate totals without a calculation error.''',
    vocabulary='''metric | A defined quantitative measure. | define a metric
business question | The decision-relevant question an analysis is meant to answer. | clarify the business question
metric definition | Rules specifying exactly how a measure is calculated. | agree a metric definition
qualifying event | An action meeting the condition for inclusion. | specify the qualifying event
distinct user | A unique user counted once under a defined identity rule. | count distinct users
event count | The number of recorded qualifying occurrences. | distinguish event counts from users
eligible population | The complete group allowed into the measure's base. | define the eligible population
denominator | The total used as the base of a rate. | state the denominator
numerator | The counted outcome placed over the base of a rate. | verify the numerator
reporting window | The time period included in a measure. | align reporting windows
calendar month | A month bounded by the adopted calendar and time zone. | report by calendar month
time zone | The time reference used to assign event dates. | fix the reporting time zone
exclusion rule | A condition removing records from the measure. | document exclusion rules
internal account | An account belonging to the organization's own personnel or systems. | exclude internal accounts
test account | An account used for testing rather than genuine activity. | filter test accounts
deduplication | Removing repeated representations of the same counted entity. | apply user deduplication
identity resolution | Connecting records that refer to the same entity. | review identity resolution
active user | A user meeting a specified activity definition. | define active users explicitly
login-based activity | Activity defined by a qualifying sign-in. | report login-based activity
transaction-based activity | Activity defined by a qualifying transaction. | report transaction-based activity
subset | A group entirely contained within another group. | identify the subset relationship
metric owner | The role accountable for a measure's definition and use. | identify the metric owner
semantic layer | Shared definitions connecting data to business meaning. | maintain a semantic layer
reconciliation | Explaining and resolving differences between reported figures. | reconcile metric totals''',
    precision='900/2,000 is 45% of eligible users. 900/1,200 is 75% of users who logged in. Both calculations are valid for their stated bases, but only the first answers the supplied eligible-user question.',
    precision_extra='The two groups overlap: all 900 transacting users are among the 1,200 login users. Adding them would double-count those 900. Repeated transactions by one person also do not increase a distinct-user total.',
    phrases='''Clarify the question | "Are we measuring sign-in or completed transactions?"
Define the counted entity | "Each user is counted once."
Name the event | "The qualifying event is a completed transaction."
Set the window | "Use the September calendar month in UTC."
Keep exclusions aligned | "Both measures exclude internal and test accounts."
Acknowledge both results | "Both queries match their own definitions."
Explain the difference | "The reports use different activity events."
Choose the relevant count | "Nine hundred users answer the transaction question."
State the base | "The eligible population is 2,000 users."
Give the rate | "That is 45% of eligible users."
Distinguish another rate | "Seventy-five percent uses logged-in users as its base."
Avoid double-counting | "The transaction group is a subset of the login group."
Improve the label | "Call this transaction-active users."
Preserve the other measure | "Keep the login measure under its own label."
Assign definition ownership | "The metric owner should approve the shared definition."
Close the disagreement | "We need consistent meaning, not an artificial match between different events."''',
    notes='''Active | Incomplete unless the qualifying event is stated.
Users | Distinct identities, not the number of actions.
Of eligible users | Fixes the denominator for the rate.
During September | Needs consistent calendar boundaries and time zone.
Correct | Can mean calculated correctly without being decision-relevant.
Reconcile | Explain differences before forcing totals to match.''',
    d='''Which label best fits the 900 count? | September transaction-active users | All September logins | Completed transaction events, including repeats | Total eligible accounts | The count concerns distinct users with a completed transaction in the reporting window.
What does 900/1,200 measure? | The share of logged-in users who completed a transaction | The share of all eligible users who logged in | The number of repeated transactions | A 75% growth rate from last month | The denominator is the login group, and the numerator is its transacting subset.
Why should the two totals not be added? | The 900 transacting users are already included among the 1,200 login users. | All additions of user counts are invalid. | The UTC boundary changes addition rules. | Each report contains exactly the same 1,200 people. | The supplied subset relationship means adding totals double-counts the transacting group.
Which next step addresses the real disagreement? | Record both event definitions and select the transaction measure for this question. | Alter a correct query until both totals match. | Use whichever number looks more impressive. | Remove the denominator from the slide. | The discrepancy is semantic and decision-related, not a demonstrated query failure.''',
    dialogue='''Rafael | The executive slide says twelve hundred active users, but Finance has nine hundred. Both teams insist their query is right. Which number should I remove?
Mei | First agree the [[business question::The business question determines which correctly calculated measure is relevant to the decision.]]. We need the number of eligible users who completed a transaction during September, not merely the number who signed in.
Rafael | The twelve hundred report counts successful logins, once per user. Finance counts completed transactions, also once per user. Both exclude internal and test accounts.
Mei | Then the [[qualifying event::The qualifying event differs between successful login and completed transaction, explaining the distinct totals.]] differs. The queries can both be correct while answering different questions. We should not change a valid calculation simply to make two different meanings agree.
Rafael | The window is the September calendar month in UTC for both, and they use the same two thousand eligible users. That part is aligned.
Mei | Good. A shared [[reporting window::The reporting window fixes the period and prevents a time-boundary difference from being confused with the event-definition difference.]] removes one possible source of disagreement. The distinction here is activity type, not different month boundaries or different treatment of test accounts.
Rafael | For the actual question, I should choose nine hundred and label it as people completing a transaction. Multiple transactions by one user still count once.
Mei | Yes, the entity is a [[distinct user::A distinct user is counted once even when the user performs multiple qualifying actions within the window.]]. That is not the total number of transaction events. The slide should make the counted entity clear enough that the audience cannot silently substitute another.
Rafael | I have seventy-five percent on the slide: nine hundred divided by twelve hundred. Is that answering the eligible-user question, or have I changed the base?
Mei | That uses a different [[denominator::The denominator defines the rate's base; eligible users and logged-in users answer different percentage questions.]]. Nine hundred divided by two thousand eligible users is forty-five percent. Nine hundred divided by twelve hundred logged-in users is seventy-five percent.
Rafael | Both rates tell us something, but forty-five percent is the answer to the eligible-user question. Seventy-five percent describes the logged-in group instead.
Mei | Exactly. Keep the [[numerator::The numerator remains nine hundred transacting users while the stated denominator changes the meaning of the percentage.]] and base together in speech. Saying just the percentage would hide the change in meaning and invite an incorrect comparison later.
Rafael | Someone suggested adding the two reports to show total engagement. But the nine hundred transacting users are already included in the twelve hundred who logged in.
Mei | That [[subset::The subset relationship means every transacting user is already counted within the login group, so addition would duplicate those users.]] relationship makes addition inappropriate for distinct people. It would count the transaction group twice rather than identify twenty-one hundred different active users.
Rafael | I will keep the login figure because it is useful, but give it a different label. The executive headline will use the transaction definition.
Mei | Put both in the [[semantic layer::The semantic layer preserves shared business definitions so later reports use the same labels and rules consistently.]] with the event, identity rule, exclusions, and time zone. Renaming one slide is not enough if other reports keep reusing the ambiguous active-user label.
Rafael | Who signs off if the transaction event changes next month? I do not want the same label to hide a new definition.
Mei | Assign a [[metric owner::The metric owner is accountable for the definition and its controlled evolution rather than leaving each report to invent its own meaning.]] and record the approved version. That gives both teams a place to resolve changes before comparing totals that no longer mean the same thing.
Rafael | My summary will be nine hundred transaction-active users, forty-five percent of two thousand eligible users, September UTC. The login measure remains separately labeled.
Mei | That completes the [[reconciliation::Reconciliation explains the different totals and their uses without forcing distinct measures to produce an artificial match.]]. We have preserved both correct calculations, selected the measure that answers the decision, and removed the ambiguity that created the apparent conflict.''',
    transfer_title='One count, two possible bases',
    transfer_setup='A month has 1,000 eligible users, 800 distinct login users, and 400 distinct transacting users, all within the login group. The question asks for transaction activity among all eligible users.',
    transfer='''Analyst: "The relevant distinct-user count is ___." | 400 | The supplied transaction-active group contains four hundred distinct users.
Manager: "The eligible-user denominator is ___." | 1000 | The requested rate uses all one thousand eligible users as its base.
Analyst: "The requested rate is ___ percent." | 40 | Four hundred divided by one thousand equals forty percent.
Manager: "Using login users instead would give ___ percent." | 50 | Four hundred divided by eight hundred logged-in users equals fifty percent.'''))

BOOK['units'].append(unit(
    title='Data Quality and Trust',
    scene='Refreshed today, complete only through Monday',
    rehearsal=['Read turns 1-10. Contrast the refresh timestamp with each source cutoff.', 'Switch roles for turns 11-20. Stress event time rather than the later load time.', 'Check the transfer. Read the Wednesday-only option without turning Thursday unknowns into zeros.'],
    skill='Explain mixed source freshness and set an appropriate reporting boundary without mislabeling missing data as zero.',
    brief='Reporting analyst Asha reviews a dashboard with operations manager Tomas on Wednesday at 09:00 UTC. The dashboard refresh completed, and the orders source is verified complete through Tuesday 23:59 UTC. The refunds source is verified complete only through Monday 23:59 UTC because its next delivery is delayed. A Monday-Tuesday net-order-value figure subtracts available refunds from orders, so the periods are misaligned. Asha can publish a verified Monday-only comparison; Tuesday refunds are unknown, not confirmed zero. No delivery time for the missing source is confirmed.',
    cast='Asha | Reporting analyst\nTomas | Operations manager',
    culture=('Explain the affected decision, not just the pipeline', 'A completed refresh can sound like an all-clear to a business reader. Name the source that is late, the measure affected, and the period that remains usable. This gives colleagues a practical reporting option while preserving the visible limitation.'),
    a='''Which source is complete only through Monday? | Refunds | Orders | Both sources through Tuesday | Neither source through any date | The briefing explicitly limits refund coverage to Monday while orders extend through Tuesday.
What is known about Tuesday refunds? | They are unknown in the available source. | They are confirmed zero. | They equal Tuesday orders. | They were all processed on Monday. | Missing source coverage does not establish the amount of Tuesday refunds.
Which comparison can Asha publish as verified? | Monday-only, using aligned source coverage | Monday-Tuesday net value without qualification | A Wednesday full-day total | A guaranteed delivery time for the missing source | Both sources are verified complete through Monday, making that shared period usable.''',
    vocabulary='''data quality | Fitness of data for its intended use. | assess data quality
freshness | How recent data is relative to the intended use. | monitor data freshness
timeliness | Availability of data within the required time. | define timeliness requirements
completeness | Presence of the required records or values. | verify source completeness
accuracy | Agreement between data and the facts it represents. | assess data accuracy
validity | Conformance to defined formats or rules. | test data validity
consistency | Agreement across related representations or rules. | check data consistency
uniqueness | Absence of unintended duplicate records. | test record uniqueness
refresh timestamp | The time a report or model was last updated. | display the refresh timestamp
source cutoff | The boundary through which source data is available or complete. | state the source cutoff
event time | When the represented business event occurred. | distinguish event time from load time
load time | When data entered the relevant system. | record load time
upstream source | An earlier system supplying data to a pipeline. | inspect upstream sources
pipeline | A sequence of data movement and transformation steps. | monitor the data pipeline
ingestion delay | A lag in receiving data from a source. | investigate ingestion delay
late-arriving data | Records received after the expected processing point. | handle late-arriving data
backfill | Loading previously missing historical records. | validate a backfill
watermark | A tracked boundary used to process or assess data progress. | inspect the pipeline watermark
coverage window | The period or population represented by available data. | align coverage windows
reconciliation check | A comparison used to verify agreement between records or totals. | run reconciliation checks
null value | A marker for missing or unknown information in a data field. | distinguish null from zero
zero value | A recorded quantity of none, not automatically a missing value. | preserve zero values correctly
data-quality notice | A visible explanation of a known data limitation. | publish a data-quality notice
recovery estimate | A qualified expectation for restoration of a data flow. | qualify the recovery estimate''',
    precision='A refresh timestamp records when processing ran, not how current every input was. Even a latest event timestamp alone would not prove completeness. Here, the brief explicitly verifies different complete-through cutoffs for the two sources.',
    precision_extra='Unknown Tuesday refunds must not be presented as zero refunds. A combined Monday-Tuesday net figure would mix different coverage windows. A verified Monday-only view is a bounded alternative while the missing delivery is unresolved.',
    phrases='''Acknowledge the refresh | "The dashboard refresh completed at 09:00 UTC."
Separate source coverage | "That does not mean every source is current through Tuesday."
Name the lagging source | "Refunds are complete only through Monday."
State the other cutoff | "Orders are verified through Tuesday 23:59 UTC."
Locate the affected measure | "The two-day net figure mixes coverage periods."
Distinguish missing from zero | "Tuesday refunds are unknown, not confirmed zero."
Offer a usable view | "We can publish the verified Monday-only comparison."
Keep the limitation visible | "Place the source-cutoff note beside the figure."
Avoid a false promise | "The missing delivery time is not confirmed."
Ask for the right evidence | "Check source completeness, not only job completion."
Describe the dependency | "The calculation depends on both orders and refunds."
Name the next validation | "Reconcile the backfill before republishing the two-day figure."
Preserve the old status | "Keep the affected view marked incomplete until validation passes."
Clarify timing | "Load time and event time are different."
Bound the current claim | "This view is complete through Monday only."
Close the update | "Publish the aligned period and report the remaining source delay."''',
    notes='''Fresh | Relative to a defined required time, not merely a green icon.
Refreshed | Describes processing, not necessarily complete source coverage.
Through Monday | State the actual cutoff and time zone.
Unknown | Must not silently become zero.
Backfilled | Requires validation before the limitation is removed.
Expected | An estimate needing a basis, not a delivery guarantee.''',
    d='''Which dashboard note is accurate? | Refreshed Wednesday 09:00 UTC; refunds complete through Monday; two-day net value incomplete. | Refreshed Wednesday, so all source events are current. | Tuesday refunds are zero because none arrived. | The refund delay proves every order is inaccurate. | The note separates successful processing from source coverage and identifies the affected measure.
Why is Monday-only reporting usable here? | Both sources are verified complete through that shared period. | Monday is always more accurate than Tuesday. | Removing refunds would make any period complete. | A short period never needs validation. | The relevant fact is aligned verified coverage, not an inherent property of Monday.
Which check is insufficient by itself? | Seeing that the dashboard refresh job completed | Verifying source coverage against expected records | Reconciling the missing source after backfill | Checking the complete-through cutoff for each input | A completed refresh can process stale inputs without repairing their missing coverage.
What should happen after the delayed records arrive? | Validate and reconcile them before removing the limitation. | Immediately claim that every historical figure was already correct. | Keep treating the records as zero. | Change the event dates to Wednesday load time. | Receiving records is followed by verification, and event dates should preserve business timing.''',
    dialogue='''Tomas | The dashboard says refreshed this morning. Can I use the Monday-Tuesday net-order-value number in the operations meeting as our complete two-day result?
Asha | Not yet. The [[refresh timestamp::The refresh timestamp shows when the dashboard processing completed, not the complete-through date of each input.]] is Wednesday at nine UTC, but the inputs have different coverage. Orders are verified through Tuesday; refunds are complete only through Monday.
Tomas | I had assumed that a successful refresh meant every table contained the latest business activity. Which boundary should I read instead for the refund data?
Asha | Read the [[source cutoff::The source cutoff identifies the period through which the refund source is verified complete, here Monday 23:59 UTC.]]. Refunds are complete through Monday at twenty-three fifty-nine UTC. The next delivery is delayed, so Tuesday is not covered by the available records.
Tomas | Then the two-day net figure has Tuesday orders but not the corresponding Tuesday refunds. It could look better simply because that input is incomplete.
Asha | Yes. The [[coverage window::The coverage window differs across orders and refunds, making the combined two-day net measure misaligned.]] is misaligned. We cannot interpret the result as a complete two-day net amount when the subtraction uses refunds from a shorter period.
Tomas | The chart fills the empty Tuesday cell with zero. Should we change that to unknown while the refund delivery is missing?
Asha | Missing is not a [[zero value::A zero value asserts a quantity of none; absent Tuesday refund coverage does not support that assertion.]]. We do not know the amount yet. Showing zero as the business result would turn a source limitation into a false claim about customer activity.
Tomas | I still need a reliable number for the meeting. Could we show Monday by itself, since both sources are verified complete through that day?
Asha | Yes. That respects [[completeness::Completeness concerns the required records for the stated period; the briefing verifies both sources for Monday.]] for the shared period in this case. We can publish the Monday-only comparison and make clear that the two-day figure remains incomplete.
Tomas | The note should be near the result, not somewhere people will miss it. I will explain that Tuesday orders alone do not settle the net figure.
Asha | Add a [[data-quality notice::The data-quality notice makes the source limitation and affected measure visible where readers interpret the result.]] beside the affected view. State which source is delayed, its complete-through time, and which period remains usable rather than labeling the entire dashboard unreliable.
Tomas | Do we know when the missing refund delivery will arrive? I would like to tell the meeting whether the full figure will be available this afternoon.
Asha | There is no confirmed [[recovery estimate::A recovery estimate needs a supported expectation; this case supplies no confirmed time for the missing delivery.]]. I will request an update from the source owner, but I should not invent a delivery time simply because the meeting needs one.
Tomas | Once the rows arrive, we will have business events from Tuesday loaded on a later day. We should not move those refunds into Wednesday totals.
Asha | Correct. Preserve [[event time::Event time records when the business event occurred, which remains distinct from the later ingestion or load time.]] separately from load time. The records belong to the appropriate business period even when the pipeline receives them later than expected.
Tomas | When the delivery arrives, who checks that it is complete? I do not want the warning removed just because the refresh turns green.
Asha | Validate the [[backfill::The backfill loads previously missing records, which need verification before the incomplete-status notice can be removed.]] and document the checks. A green refresh icon should not be our only evidence that the previously incomplete reporting period is now fit for use.
Tomas | I will take the Monday-only view to the meeting, explain the Tuesday refund gap, and avoid promising a two-day net result before it is verified.
Asha | That is the right [[timeliness::Timeliness is availability within the required period; the refund delay should be disclosed while the usable aligned view is preserved.]] message: a useful aligned result now, a specific limitation, and a clear validation step before the fuller figure is released.''',
    transfer_title='A current job can use an old source',
    transfer_setup='A report refreshed Friday. Sales are verified complete through Thursday, but returns only through Wednesday. Thursday returns are unknown. Both sources are complete for Wednesday.',
    transfer='''Analyst: "The refresh ran on ___." | Friday | The briefing explicitly identifies Friday as the processing day.
Manager: "Returns are complete only through ___." | Wednesday | The source cutoff for returns is Wednesday, not the later refresh day.
Analyst: "Thursday returns are ___." | unknown | Missing Thursday coverage does not prove a zero business amount.
Manager: "A Wednesday-only comparison is ___." | aligned | Both sources are verified complete for Wednesday, so their coverage aligns.'''))


BOOK['units'].append(unit(
    title='Dashboards and Executive Reporting',
    scene='Four hundred eighty needs a denominator and a target',
    rehearsal=['Read turns 1-10. Say percentage points and relative percent distinctly.', 'Switch roles for turns 11-20. Keep the twenty late requests in the summary.', 'Check the transfer. Contrast five points above last month with two above target.'],
    skill='Turn an isolated monthly count into a clear performance statement with definition, target, comparison, and units.',
    brief='BI analyst Jonas reviews a card labeled 480 with service director Elena. It counts September requests completed within 24 hours of receipt: 480 of 500 eligible requests. All requests have a complete observation window, and the remaining 20 finished late. The approved target is at least 95%. August had 450 timely completions among 500 eligible requests under the same definition. Jonas must report the current rate, position against target, and change from August without calling a percentage-point change a relative percentage increase.',
    cast='Jonas | Business-intelligence analyst\nElena | Service director',
    culture=('Make the interpretation portable', 'A useful executive card should survive being quoted outside the meeting. Include the measure and comparison in a sentence that can be repeated accurately. Avoid forcing the listener to infer whether a larger number represents improvement, demand growth, or a changed definition.'),
    a='''What is the September timely-completion rate? | 96% | 95% | 90% | 480% | Four hundred eighty timely requests divided by five hundred eligible requests equals ninety-six percent.
How does September compare with the target? | One percentage point above the 95% target | One percent below target | Six percentage points below target | Exactly equal to target | Ninety-six percent minus ninety-five percent is one percentage point.
What was the August rate? | 90% | 45% | 95% | 96% | Four hundred fifty timely requests divided by five hundred eligible requests equals ninety percent.''',
    vocabulary='''KPI | Key performance indicator, a measure tied to an objective. | define a KPI
dashboard card | A compact display of a selected metric. | label the dashboard card
performance target | A specified desired level of a measure. | compare with the performance target
actual result | The observed value of the defined measure. | report the actual result
comparison period | An earlier or alternative interval used as a reference. | state the comparison period
variance | A difference from a specified reference value. | explain the target variance
percentage point | One unit of difference between percentage values. | report percentage-point changes
relative change | Change divided by the original reference value. | calculate relative change
month-on-month | Compared with the immediately preceding month. | describe month-on-month movement
year-on-year | Compared with the corresponding period a year earlier. | report year-on-year change
service-level target | An agreed performance threshold for a service measure. | track the service-level target
timely completion | Completion within the specified permitted duration. | measure timely completion
elapsed time | Duration between defined start and end events. | calculate elapsed time
observation window | The period available to observe the relevant outcome. | complete the observation window
threshold | A boundary used for a rule or decision. | apply the threshold
direction of improvement | Whether higher or lower values are favorable. | state the direction of improvement
trend | A pattern across a sequence of observations. | qualify a trend claim
seasonality | Recurring variation related to calendar patterns. | assess seasonality
run chart | A display of values ordered through time. | review the run chart
annotation | Explanatory text attached to a chart or figure. | add a relevant annotation
drill-down | Moving from a summary to more detailed data. | provide a drill-down
exception queue | Items selected for attention under a defined rule. | review the exception queue
comparability | The extent to which measures use compatible bases. | establish period comparability
executive summary | A concise account of the main evidence and decision relevance. | sharpen the executive summary''',
    precision='September is 96%: 480/500. August is 90%: 450/500. The increase is 6 percentage points, or approximately 6.67% relative to August. September exceeds the 95% target by 1 percentage point.',
    precision_extra='The 480 card alone omits its denominator, timing rule, target, and comparison. Two monthly results establish a month-on-month improvement here, not a sustained long-term trend or an explanation of why performance changed.',
    phrases='''Name the measure | "This is the share completed within 24 hours."
State the start | "The clock starts when the request is received."
Give count and base | "September recorded 480 timely completions out of 500."
State the result | "The timely-completion rate is 96%."
Compare with target | "That is one percentage point above the 95% target."
Give the prior result | "August was 450 of 500, or 90%."
Use the correct change unit | "The rate rose by six percentage points."
Give the relative alternative | "That is about a 6.67% relative increase."
Protect comparability | "Both months use the same definition."
Confirm maturity | "Every request has a complete observation window."
Keep the exceptions visible | "Twenty September requests finished late."
Avoid an invented cause | "These totals do not explain the improvement."
Bound the trend | "This is a two-month comparison, not a sustained-trend claim."
Make the card interpretable | "Add the definition, denominator, target, and comparison."
Offer the next view | "The drill-down can show the late requests."
Close the readout | "September met the target and improved from August on the same basis."''',
    notes='''Above target | State the amount and use the correct unit.
Up six points | Not identical to up six percent.
Within 24 hours | Requires defined start and completion events.
Monthly total | Does not by itself reveal a performance rate.
Trend | Needs more than a confident adjective about two observations.
Favorable | Depends on the measure's direction and target.''',
    d='''Which card text is most complete? | September: 480/500 within 24 hours, 96%; target 95%; August 90%. | 480, excellent. | 96, target unknown. | Up 6%, with no reference period. | The complete text provides the definition, count, denominator, target, and comparable prior rate.
Which change statement is accurate? | Up 6 percentage points from August | Up 6% relative to August exactly | Up 30 percentage points because the count rose by 30 | Up 1 percentage point from August | Ninety-six percent minus ninety percent is six percentage points.
What is the approximate relative increase from 90% to 96%? | 6.67% | 6 percentage points expressed as 60% | 1% | 96% | The six-point difference divided by the ninety-percent reference rate is approximately 6.67%.
What cannot be concluded from the supplied totals? | The specific cause of the improvement | September met the target | Twenty September requests finished late | The two months used the same definition | The briefing supplies outcomes and comparable definitions but no causal investigation evidence.''',
dialogue='''Elena | The card says four hundred eighty with a green arrow. What does it count, and how should I interpret it?
Jonas | The [[KPI::The KPI is the defined performance measure, here the share of eligible requests completed within twenty-four hours.]] is timely completion: requests finished within twenty-four hours of receipt. Four hundred eighty is the timely count, not the rate or the total demand.
Elena | There were five hundred eligible requests in September, and the other twenty finished late. All requests have had enough time for us to observe their outcomes.
Jonas | Then the [[actual result::The actual result is ninety-six percent, calculated from 480 timely completions among 500 eligible requests.]] is ninety-six percent, or four hundred eighty out of five hundred. We should display both the count and the base so the rate is interpretable.
Elena | Our approved target is at least ninety-five percent. That means September passed, but I want the amount above the target described accurately.
Jonas | It is one [[percentage point::A percentage point expresses the difference between percentage values, so 96% exceeds 95% by one point.]] above target. Saying one percent without qualification can suggest a relative calculation, which is a different way of expressing the comparison.
Elena | August had four hundred fifty timely requests out of five hundred. The same definition and exclusions apply, so that earlier rate was ninety percent.
Jonas | August is the [[comparison period::The comparison period is the earlier month, whose ninety-percent rate provides the reference for the reported improvement.]]. September increased by six percentage points on that basis. We should name the month rather than leave the audience guessing what the arrow compares.
Elena | My draft says up six percent. Should I change that to six percentage points? I need wording I can repeat without changing the calculation.
Jonas | Correct it. The [[relative change::Relative change divides the six-point rise by the ninety-percent August rate, giving approximately 6.67%.]] is approximately six point six seven percent. The absolute difference between the percentage values is six points. Both are valid when labeled, but they are not interchangeable.
Elena | I also want to avoid the green arrow hiding the twenty late requests. Meeting the overall threshold does not mean every customer received the target service.
Jonas | We can provide a [[drill-down::A drill-down exposes the individual or grouped exceptions beneath the favorable summary rate.]] for those late cases. The headline can report that the target was met while the detail preserves the exceptions that still need operational attention.
Elena | Can I call it a sustained improvement, or do two months only support the month-on-month comparison? I want to recognize the result accurately.
Jonas | We can report the [[month-on-month::Month-on-month describes the immediate September-versus-August comparison without claiming a longer established pattern.]] improvement. Two months do not establish a sustained trend, and these totals do not identify the cause. Recognition does not require a stronger statistical story.
Elena | Fair. We can acknowledge the result without attributing it to a particular staffing change that has not been evaluated. The definition should stay visible too.
Jonas | Preserve [[comparability::Comparability rests on the shared definition, eligibility, and observation basis that make the two monthly rates meaningful to compare.]] by retaining the same start, completion rule, exclusions, and denominator. A future definition change should be flagged instead of being presented as an unexplained performance movement.
Elena | The clock begins on receipt and stops on completion. We should also state that the data covers fully observed requests, not a partial month of immature outcomes.
Jonas | Yes, the [[observation window::The observation window must allow the outcome to be observed; the briefing confirms all requests have complete windows.]] is complete for every request here. That matters because unresolved timing can otherwise distort a rate even when the arithmetic itself is correct.
Elena | September was ninety-six percent: one point above target, six above August, twenty requests late. The cause is unestablished.
Jonas | That is a useful [[executive summary::The executive summary brings together the result, target, comparison, exceptions, and limits in a concise repeatable account.]]. The card will include the definition and base, and the detail will support the late-case review rather than asking the audience to infer everything from 480.''',
    transfer_title='Above target and above last month are different',
    transfer_setup='A service completes 180 of 200 eligible requests on time this month. Last month was 170 of 200. The target is 88%, and both months use the same fully observed definition.',
    transfer='''Analyst: "This month is ___ percent." | 90 | One hundred eighty divided by two hundred equals ninety percent.
Manager: "Last month was ___ percent." | 85 | One hundred seventy divided by two hundred equals eighty-five percent.
Analyst: "The month-on-month increase is ___ percentage points." | five | Ninety percent minus eighty-five percent is five percentage points.
Manager: "This month exceeds target by ___ percentage points." | two | Ninety percent minus the eighty-eight-percent target equals two percentage points.'''))

BOOK['units'].append(unit(
    title='Causation, Correlation, and Caveats',
    scene='Training attendees renewed more often',
    rehearsal=['Read turns 1-10. Stress observed association and voluntary attendance.', 'Switch roles for turns 11-20. Keep a possible confounder distinct from a proven explanation.', 'Check the transfer. Read both group rates without attributing the gap to training.'],
    skill='Report a meaningful association while separating the observed difference from an unestablished causal effect.',
    brief='Analyst Priya reviews voluntary customer-training results with customer-success lead Marcus. Over the same renewal window, 90 of 100 eligible attendees renewed, compared with 160 of 200 eligible non-attendees. Attendance was not randomized. Baseline motivation and engagement may differ between the groups and were not measured. The records establish a 90% versus 80% renewal association, not the effect of making everyone attend. Priya recommends a reviewed evaluation design before the team uses the difference as a causal benefit claim.',
    cast='Priya | Data analyst\nMarcus | Customer-success lead',
    culture=('Protect the useful observation while correcting the claim', 'A causal caveat should not sound like all the work was pointless. State the real association first, then explain the specific competing explanation. This helps a colleague keep the finding while replacing an overconfident promise with an appropriate next evaluation.'),
    a='''What is the attendee renewal rate? | 90% | 80% | 45% | 10% | Ninety renewals divided by one hundred eligible attendees equals ninety percent.
What is the non-attendee renewal rate? | 80% | 160% | 90% | 20% | One hundred sixty renewals divided by two hundred eligible non-attendees equals eighty percent.
Why is the causal effect not established? | Attendance was voluntary, and unmeasured baseline differences may matter. | The two rates are identical. | No customer renewed. | The renewal window differs by definition. | Voluntary selection and possible unmeasured differences prevent the observed comparison from isolating the training effect.''',
    vocabulary='''association | An observed relationship between variables or groups. | report an association
correlation | A measure or description of co-variation. | distinguish correlation from causation
causal effect | A change attributable to a specified intervention. | estimate a causal effect
confounding | Distortion from factors related to both exposure and outcome. | assess potential confounding
self-selection | Participation determined partly by people's own choices. | account for self-selection
selection bias | Systematic distortion related to how observations enter groups. | evaluate selection bias
baseline characteristic | A feature measured before the exposure or intervention. | compare baseline characteristics
motivation | A person's underlying inclination to act or engage. | assess baseline motivation
engagement | Participation or involvement under a specified definition. | define customer engagement
observational study | Analysis of naturally occurring exposures without assigned treatment. | interpret an observational study
random assignment | Allocation to groups by a defined random process. | use random assignment
treatment group | The group assigned or exposed to the studied intervention. | define the treatment group
comparison group | The group used as a reference for the outcome. | select a comparison group
counterfactual | The outcome that would occur under an alternative exposure. | define the counterfactual question
renewal | Continuation of an eligible customer contract or relationship. | measure customer renewal
renewal window | The period over which renewal outcomes are observed. | align renewal windows
eligible customer | A customer meeting the defined inclusion conditions. | identify eligible customers
absolute difference | A difference expressed in the original measure's units. | state the absolute difference
relative lift | A difference expressed relative to a comparison value. | qualify relative lift
adjustment | Accounting for specified variables in an analysis. | assess the adjustment method
unmeasured factor | A relevant characteristic not recorded in the data. | disclose unmeasured factors
generalizability | Applicability of a result beyond the studied group. | assess generalizability
causal claim | A statement that an intervention produced an outcome. | qualify a causal claim
evaluation design | The planned method for assessing a program or intervention. | review the evaluation design''',
    precision='The observed difference is 10 percentage points: 90%-80%. Relative to the non-attendee rate, it is 12.5%. Neither expression turns the voluntary comparison into an estimated causal benefit for mandatory training.',
    precision_extra='Unmeasured motivation is a possible confounder, not a proven explanation of the full difference. Likewise, failure to establish causation does not prove that training has no effect. The appropriate conclusion is narrower than either claim.',
    phrases='''State the observed rates | "Attendees renewed at 90%; non-attendees at 80%."
Give the counts | "That is 90 of 100 versus 160 of 200."
Name the difference | "The observed gap is ten percentage points."
Label the finding | "This is an association in the supplied data."
Identify selection | "Customers chose whether to attend."
Name the alternative explanation | "Baseline engagement may differ between the groups."
Preserve uncertainty | "Those baseline factors were not measured."
Reject the causal leap | "We cannot attribute the whole difference to training."
Avoid the opposite overclaim | "This does not prove that training has no effect."
Clarify the counterfactual | "We need to know what would have happened to comparable customers without training."
Keep the window aligned | "Both rates use the same renewal window."
Bound the audience | "The result concerns these eligible customer groups."
Qualify adjustment | "Adjusting measured factors would not automatically remove every unmeasured difference."
Recommend evaluation | "Review a design that can better isolate the training effect."
Revise the headline | "Use higher observed renewal among attendees."
Close the discussion | "Keep the association and remove the unsupported promise."''',
    notes='''Because | Introduces a causal claim that needs appropriate support.
Among | Describes a group comparison without asserting cause.
May differ | Identifies a plausible concern, not a proven explanation.
Lift | Specify whether descriptive or causal, relative or absolute.
No proof of effect | Not equivalent to proof of no effect.
Everyone | Extends the claim beyond the observed voluntary groups.''',
    d='''Which headline is supported? | Higher observed renewal among voluntary training attendees | Training caused a ten-point renewal increase for everyone | Training has no possible effect | Mandatory training is proven to prevent all churn | The supported headline describes the observed association without asserting an unestablished causal result.
What is the relative observed difference compared with 80%? | 12.5% | 10% exactly | 90% | 20 percentage points | The ten-point gap divided by the eighty-percent reference rate equals 12.5%.
Which statement about motivation is accurate? | It is an unmeasured possible source of group differences. | It is proven to explain the entire gap. | It was balanced by random assignment. | It was measured and found identical. | The briefing identifies motivation as a possible difference but supplies no measurement or randomization.
What should a revised recommendation do? | Preserve the association and seek a reviewed design for a causal evaluation. | Hide the group sizes and announce a guaranteed benefit. | Treat voluntary attendance as random assignment. | Conclude no evaluation can ever be useful. | A better evaluation can address the causal question while the current association remains honestly reported.''',
dialogue='''Marcus | Training attendees renewed at ninety percent, versus eighty percent for non-attendees. Can we say the sessions improved renewal by ten points?
Priya | We can report the [[association::The association is the observed difference between voluntary attendance groups, not an isolated effect of training.]], but not that causal conclusion from these records. Ninety of one hundred attendees renewed; one hundred sixty of two hundred non-attendees renewed.
Marcus | Both groups had the same renewal window and eligibility rules. That makes the comparison cleaner, even though attendance was voluntary rather than assigned.
Priya | Correct, but [[self-selection::Self-selection means customers chose attendance, which can create relevant differences between the compared groups.]] remains important. Customers who chose training may have been more motivated or engaged already. Those baseline differences were not measured in the supplied data.
Marcus | Then the ten-point difference could reflect training, pre-existing differences, or both. We should not assume the entire gap was created by the sessions.
Priya | Exactly. The [[causal effect::The causal effect concerns what training itself changes, which the voluntary comparison does not isolate.]] asks what the intervention changes compared with what would otherwise have happened. This comparison does not isolate that quantity simply because the rates are clearly different.
Marcus | I do not want the caveat to erase the positive finding. The team has real evidence that attendees renewed more often in this group.
Priya | Keep that observation. [[Confounding::Confounding is a possible distortion from factors related to both attendance and renewal, not proof that the observed association is meaningless.]] is a reason to qualify the causal interpretation, not to deny the counts. We can state the association and the specific limitation together.
Marcus | Sales will ask whether you are saying motivation caused the whole gap. We did not measure it, so that is not our conclusion either, is it?
Priya | Right. It is an [[unmeasured factor::Motivation is an unmeasured factor that could matter, but the case does not establish its size or explanatory contribution.]] that may matter, not a proven explanation of every percentage point. We should avoid replacing one unsupported causal story with another equally unsupported story.
Marcus | For the numerical wording, ninety minus eighty is ten percentage points. Would a twelve-point-five-percent improvement headline simply express the same observed difference another way?
Priya | It expresses [[relative lift::Relative lift divides the ten-point observed difference by the eighty-percent comparison rate, giving 12.5% without establishing causation.]] against the eighty-percent reference rate. But improvement may still imply cause. Say a twelve-point-five-percent higher observed rate, and keep the nonrandom attendance qualification nearby.
Marcus | The business question is whether offering or requiring training would improve renewal for eligible customers. That is different from describing people who already chose to attend.
Priya | Yes. The [[counterfactual::The counterfactual concerns what the relevant customers would have done under a different training exposure, which is not directly observed here.]] question is what comparable customers would do without the intervention. We need a reviewed evaluation approach suited to that decision, not just a more persuasive headline.
Marcus | We may be able to add customer size and tenure. Would adjusting for those settle the concern, or would important differences still be missing?
Priya | A suitable [[adjustment::Adjustment can account for specified measured variables but does not automatically remove all unmeasured differences or prove a causal effect.]] may help with measured differences, but it does not automatically address unmeasured motivation or every source of bias. The method and assumptions need explicit review.
Marcus | And a mandatory program could reach people unlike the voluntary attendees. Even a stronger estimate in this group might not transfer unchanged to everyone.
Priya | That is a [[generalizability::Generalizability asks whether a result applies beyond the studied voluntary groups to the broader proposed audience.]] issue as well as a causal one. The population, intervention, and implementation matter when translating evidence into a wider operational recommendation.
Marcus | I will revise the slide to higher observed renewal among attendees, show both counts and rates, and recommend a better evaluation before claiming a guaranteed benefit.
Priya | Good. A reviewed [[evaluation design::The evaluation design specifies how the next assessment will address the causal question more credibly than the current voluntary comparison.]] can address the decision we actually face. We have kept the useful finding, corrected its interpretation, and made the next evidence step clear.''',
    transfer_title='A difference does not supply its cause',
    transfer_setup='In a voluntary program, 45 of 50 attendees renew and 80 of 100 non-attendees renew. Baseline engagement is unmeasured. Attendance was not randomized.',
    transfer='''Analyst: "Attendee renewal is ___ percent." | 90 | Forty-five divided by fifty equals ninety percent for attendees.
Lead: "Non-attendee renewal is ___ percent." | 80 | Eighty divided by one hundred equals eighty percent for non-attendees.
Analyst: "The observed gap is ___ percentage points." | ten | Ninety percent minus eighty percent equals ten percentage points.
Lead: "The causal effect remains ___." | unestablished | Voluntary attendance and unmeasured baseline differences prevent this comparison from isolating causation.'''))


BOOK['units'].append(unit(
    title='SQL, Models, and Transformation Logic',
    scene='The join adds rows, not order value',
    rehearsal=['Read turns 1-10. Contrast an order identity with its amount.', 'Switch roles for turns 11-20. Stress one row per order and both reconciliation checks.', 'Check the transfer. Read the correct total, inflated sum, and distinct-value sum separately.'],
    skill='Explain row grain and join multiplicity, diagnose a duplicated aggregate, and reject a misleading distinct-value fix.',
    brief='Analytics engineer Lina reviews a report with analyst Owen. The complete teaching dataset has two orders: O1 is $100 and O2 is $100. Payment rows are O1: $60 and $40; O2: $100. Joining orders to payments on order ID creates three rows. Summing the repeated order amount then gives $300, although total order value is $200. SUM(DISTINCT order_amount) gives $100 because the two legitimate orders share an amount. Lina proposes aggregating payments to one row per order before joining, with key and total checks.',
    cast='Lina | Analytics engineer\nOwen | Reporting analyst',
    culture=('Explain the row, then the total', 'When a report suddenly grows after a join, avoid treating the larger figure as business growth or blaming a source team without checking the transformation. A small concrete example lets technical and business colleagues inspect the same logic and agree on a verifiable repair.'),
    a='''How many rows result from the supplied join? | Three | Two | Four | One | O1 matches two payment rows and O2 matches one, producing three joined rows.
What is the actual total order value? | $200 | $300 | $100 | $160 | Two distinct orders worth one hundred dollars each total two hundred dollars.
Why does SUM(DISTINCT order_amount) give $100 here? | Both legitimate orders have the same amount, so distinct values collapse them. | It deduplicates correctly by order ID. | It adds all payment amounts. | It restores the missing third order. | Distinct amounts are not distinct orders when different orders can share the same value.''',
    vocabulary='''SQL | Structured Query Language, used to query relational data. | review SQL logic
row grain | What one row represents in a dataset. | define the row grain
primary key | A non-null column or set of columns uniquely identifying each row. | validate the primary key
foreign key | A column or set of columns constrained to reference a key in a table. | check foreign-key relationships
join key | The field or fields used to match tables. | choose the join key
join cardinality | The relationship in match counts between joined entities. | inspect join cardinality
one-to-many relationship | One entity matching multiple related records. | model a one-to-many relationship
fanout | Multiplication of rows caused by multiple join matches. | detect join fanout
aggregation | Combining records into summary values. | control aggregation grain
pre-aggregation | Summarizing data before another transformation or join. | apply pre-aggregation
GROUP BY | SQL grouping of rows for aggregate calculations. | group by order ID
SUM | An aggregate that adds non-null numeric values. | check the SUM result
DISTINCT | SQL removal of duplicate values or rows in its specified scope. | inspect DISTINCT semantics
COUNT | An aggregate that counts rows or non-null expressions. | distinguish COUNT variants
inner join | A join returning matching combinations from both sides. | inspect inner-join matches
left join | A join retaining left rows even without a right match. | preserve orders with a left join
null handling | Rules for processing missing or unknown values. | define null handling
filter | A condition selecting which records remain. | apply the filter
CTE | Common table expression, a named query expression. | use a CTE
data model | A representation of entities, relationships, and measures. | review the data model
fact table | A table storing business events or measurements at a defined grain. | define the fact-table grain
dimension table | A table holding descriptive attributes for analysis. | maintain dimension keys
reconciliation total | A reference total used to verify transformed output. | compare reconciliation totals
uniqueness test | A check that a defined key has no duplicates. | run a uniqueness test''',
    precision='The joined order amounts are 100, 100, and 100: O1 appears twice because it has two payments. The correct order total is 200. The payment amounts themselves are 60, 40, and 100, also totaling 200 for this dataset.',
    precision_extra='SUM(DISTINCT order_amount) removes duplicate numeric values, not duplicate order identities. It wrongly collapses the two $100 orders to one amount. Restore the intended grain and verify keys, unmatched rows, and totals instead of using a convenient-looking shortcut.',
    phrases='''Ask about grain | "What does one row represent before the join?"
Name the key | "The tables match on order ID."
Describe the relationship | "O1 has two payment rows."
Explain the fanout | "The order row is repeated for each matching payment."
Separate data from growth | "The extra row is not an extra order."
Give the wrong total | "Summing joined order amounts produces $300."
Give the reference | "The order-level total is $200."
Reject the shortcut | "Distinct amounts do not mean distinct orders."
Show the counterexample | "Both legitimate orders have an amount of $100."
Propose the repair | "Aggregate payments to one row per order before joining."
Verify the key | "Check uniqueness of order ID in the summarized payments."
Preserve unmatched orders | "The intended order population must survive the join."
Compare totals | "Reconcile the repaired output to the source order total."
Separate measures | "Order value and payment value are different measures."
Keep null rules explicit | "Define how orders without payments are represented."
Close the review | "Fix the grain and verify the result before republishing."''',
    notes='''Row | Not always the same as a business entity.
Many | Indicates multiple matches, not necessarily bad source data.
Distinct | Ask distinct on which fields or values.
Sum | Depends on the grain of the rows being summed.
Left join | Preserves left-side presence but does not prevent fanout.
Fixed | Requires checks beyond making one displayed total look plausible.''',
    d='''Which operation explains the $300 result? | Summing order amounts after O1 is repeated for two payments | Summing the actual 60, 40, and 100 payment amounts | Adding the two original order amounts once each | Counting distinct order IDs | The joined order measure repeats O1's one-hundred-dollar value and inflates the aggregate.
Why is summing distinct amounts not a valid repair? | It merges different orders that happen to have equal values. | It always preserves every order identity. | It forces payment rows to become unique by ID. | It changes O2 into a zero-value order. | A value-level distinct operation does not deduplicate business entities by their keys.
Which proposed repair fits this report? | Summarize payments by order ID, then join at one row per order and verify totals. | Keep the payment-detail join and sum distinct order amounts. | Group payments by amount before joining to each order amount. | Replace the inner join with a left join and sum the repeated order values. | Pre-aggregation by order ID preserves business identity and aligns the grain. Distinct amounts merge legitimate orders, amount joins use the wrong key, and a left join alone does not prevent multiple matches.
Which statement about a left join is accurate? | It can preserve unmatched orders but still duplicate an order with multiple matches. | It always guarantees one row per order. | It prevents every duplicate amount. | It discards every left-side order without payment. | Left retention and match multiplicity are separate properties of the join.''',
    dialogue='''Owen | The report jumped from two hundred dollars of order value to three hundred after I added payment details. I thought the join would only add columns.
Lina | Check the [[row grain::Row grain describes what each row represents, which changes when an order is matched to multiple payment rows.]]. Before the join, each row represents one order. After matching O1 to two payment records, that order appears in two joined rows.
Owen | O1 is one hundred dollars with payments of sixty and forty. O2 is another one-hundred-dollar order with a single one-hundred-dollar payment.
Lina | That is a [[one-to-many relationship::The one-to-many relationship lets one order match multiple payment records, producing more than one output row for O1.]]. The join produces three rows: two for O1 and one for O2. The third row is not evidence of another business order.
Owen | I summed the order amount after the join. Each resulting row displays one hundred, so the three displayed amounts add to three hundred.
Lina | That is join [[fanout::Fanout multiplies the order row through payment matches, so summing the repeated order measure inflates its total.]]. The payment rows are legitimate, but the order-level measure is repeated. We need to preserve its meaning instead of treating each joined occurrence as new value.
Owen | SUM DISTINCT brought it down to one hundred. That looks worse: we have two separate orders worth one hundred each. Have I removed the wrong duplicate?
Lina | Exactly. [[DISTINCT::DISTINCT on the amount removes equal numeric values, not repeated order identities, so both legitimate hundred-dollar orders collapse.]] applies to the selected value here. Two different orders can both be worth one hundred dollars, so amount equality does not establish duplicate business identity.
Owen | The correct order total is two hundred. The payment amounts also total two hundred in this small dataset, but that does not make the measures identical.
Lina | Keep the [[aggregation::Aggregation combines rows at a chosen grain; the measure and that grain must match to avoid repeated order values.]] tied to the intended entity. An order-value report and a payment-value report answer different questions, even when their totals happen to match in this example.
Owen | For the order report, I can summarize the payment side first so there is one payment-summary row for each order ID.
Lina | Yes, use [[pre-aggregation::Pre-aggregation summarizes payments before the join so each order matches at most one summarized payment row.]]. Then verify that the payment summary has only one row per order. Joining two aligned grains avoids repeating the original order amount for every payment.
Owen | The grouping field should be order ID, not amount. Grouping by amount would combine the two orders again because they both have the same value.
Lina | Correct. The [[join key::The join key is order ID, which identifies the business relationship rather than a coincidentally equal amount.]] must preserve the intended relationship. Test the summary key and check that the matching logic uses the appropriate identifier on both sides.
Owen | This teaching dataset has payments for both orders. In the full report, an order without a payment should still appear if it belongs to the reporting population.
Lina | Then choose and test the appropriate [[left join::A left join can retain orders without a matching payment summary, but its retention behavior does not itself prevent fanout.]]. It can preserve unmatched orders, but it would not by itself solve multiple matches. Population preservation and multiplicity are separate checks.
Owen | I will check both the two-order count and the two-hundred-dollar total. Could those totals look right even if one missing order offsets a duplicate?
Lina | Use the original [[reconciliation total::The reconciliation total is the two-hundred-dollar source order value used to verify that the transformed report preserves the intended measure.]] as a reference and inspect differences. A plausible-looking grand total alone is not enough if missing orders and duplicated orders happen to offset each other.
Owen | My explanation will say the join repeated an order-level amount; it did not create revenue. I will withhold the inflated result while the transformation is corrected.
Lina | Add a [[uniqueness test::The uniqueness test checks one row per order ID in the summarized data so the corrected relationship can be maintained.]] for the summarized order key and document the grain. That makes the repair repeatable rather than relying on someone noticing another surprising total later.''',
    transfer_title='Equal amounts can belong to different orders',
    transfer_setup='Order A is $80 with two $40 payments. Order B is $80 with one $80 payment. An order-to-payment join yields three rows. The report must count each order amount once.',
    transfer='''Engineer: "The correct order total is $___." | 160 | Two distinct eighty-dollar orders total one hundred sixty dollars.
Analyst: "The joined sum of order amounts is $___." | 240 | Three joined rows each repeat an eighty-dollar order amount.
Engineer: "The sum of distinct amount values is $___." | 80 | The equal eighty-dollar values collapse to one distinct numeric amount.
Analyst: "The repair must preserve order ___." | identity | Correct deduplication depends on distinct order identity, not distinct amount values.'''))

BOOK['units'].append(unit(
    title='Experiment Readouts and Statistical Thinking',
    scene='A positive estimate is not the rollout rule',
    rehearsal=['Read turns 1-10. Say minus and plus clearly for both interval endpoints.', 'Switch roles for turns 11-20. Contrast an unmet rollout rule with proof of no effect.', 'Check the transfer. Stress the lower bound rather than the positive point estimate.'],
    skill='Present an experiment estimate with its interval, practical threshold, and pre-agreed decision rule.',
    brief='Experiment analyst Theo reviews a completed randomized test with product director Hana. The validated readout estimates a 1.2-percentage-point increase in completion, with a 95% confidence interval from -0.4 to +2.8 points. The pre-agreed rollout rule requires the interval lower bound to exceed +1.0 point, with guardrails passing. Guardrails passed, but the lower-bound condition did not. The slide currently shows only +1.2. The test has reached its planned endpoint; no unplanned extension or new rollout approval is authorized.',
    cast='Theo | Experiment analyst\nHana | Product director',
    culture=('Distinguish a promising signal from a passed rule', 'A positive estimate can be worth discussing without being a win under the actual decision standard. Show the interval and threshold together. Correcting an overconfident slide should preserve the evidence, not replace optimism with an equally unsupported claim of no effect.'),
    a='''What is the point estimate? | +1.2 percentage points | +2.8 percentage points | -0.4 percentage points | +1.0 percentage point | The supplied central effect estimate is positive one point two percentage points.
Did the lower-bound rule pass? | No; -0.4 does not exceed +1.0. | Yes; the point estimate exceeds +1.0. | Yes; every positive estimate passes. | No; guardrails failed. | The rule concerns the interval lower bound, not the positive point estimate.
What stage has the test reached? | Its planned endpoint | An unplanned first-day peek | An automatically approved extension | A completed rollout | The briefing explicitly says the planned endpoint has been reached without new authorization.''',
    vocabulary='''randomized experiment | A study allocating exposure through a random process. | interpret a randomized experiment
point estimate | A single value estimating an unknown quantity. | report the point estimate
interval estimate | A range estimating an unknown quantity under a method. | report an interval estimate
confidence interval | An interval from a method with specified long-run coverage. | interpret a confidence interval
confidence level | The nominal long-run coverage rate of the interval method. | state the confidence level
lower bound | The smaller endpoint of an interval. | compare the lower bound
upper bound | The larger endpoint of an interval. | report the upper bound
effect size | The magnitude of a difference or relationship. | assess effect size
no-change value | The parameter value representing no effect on the stated scale. | identify the no-change value
practical threshold | The effect boundary relevant to a business decision. | set a practical threshold
decision rule | A predefined condition governing a conclusion or action. | apply the decision rule
guardrail | A measure limiting unacceptable side effects. | check the guardrails
primary outcome | The main measure used to assess the intervention. | specify the primary outcome
planned endpoint | The pre-agreed point for completing the analysis or test. | respect the planned endpoint
statistical significance | A result meeting a specified statistical testing criterion. | qualify statistical significance
practical significance | Importance of an effect for a real decision. | assess practical significance
null hypothesis | A specified claim assessed by a statistical test. | state the null hypothesis
standard error | The standard deviation of an estimator's sampling distribution, usually estimated. | report the standard error
sampling variability | Variation in estimates across possible samples. | account for sampling variability
statistical power | Probability of detecting a specified effect under assumptions. | plan statistical power
minimum detectable effect | An effect size used in the study's power planning. | specify the minimum detectable effect
sequential analysis | A method allowing planned repeated statistical decisions. | use a valid sequential analysis
equivalence | Similarity within a predefined acceptable difference margin. | test equivalence appropriately
inconclusive result | Evidence insufficient for the specified conclusion. | explain an inconclusive result''',
    precision='The point estimate is +1.2 points, but the interval runs from -0.4 to +2.8. It includes zero and values below the practical threshold. Under the supplied rule, a passing guardrail cannot compensate for a failing lower bound.',
    precision_extra='A 95% confidence method has a stated long-run coverage property under its assumptions; it does not make the realized fixed parameter 95% likely to lie in this particular interval. An interval including zero also does not prove equivalence or no effect.',
    phrases='''Report the center | "The estimated effect is plus 1.2 percentage points."
Show the uncertainty | "The 95% interval runs from minus 0.4 to plus 2.8 points."
Name the no-change value | "The interval includes zero."
Keep the scale explicit | "These are percentage points, not relative percentages."
State the actual rule | "The lower bound must exceed plus 1.0 point."
Apply the rule | "The lower-bound condition was not met."
Preserve the guardrail result | "The guardrails passed."
Separate the conditions | "Passing guardrails does not replace the effect requirement."
Avoid declaring a winner | "This readout does not authorize rollout under our rule."
Avoid declaring no effect | "It also does not prove the true effect is zero."
Respect the endpoint | "The planned test has ended."
Reject opportunistic extension | "We cannot keep collecting until the result looks favorable."
Discuss next work honestly | "Any new study needs an explicitly reviewed design."
Keep the interval visible | "Place both bounds beside the estimate."
Distinguish decision from interest | "The signal may merit follow-up without passing this launch rule."
Close the readout | "Report the estimate, interval, guardrails, and unmet decision condition together."''',
    notes='''Positive | Describes the estimate's sign, not guaranteed benefit.
Includes zero | Does not establish an exact zero effect.
95% | Describes the method's confidence level, not every possible uncertainty.
Significant | Distinguish statistical criteria from business importance.
Failed rule | Not the same as proof that an intervention is useless.
More data | Needs a justified design, not a search for a preferred result.''',
    d='''Which slide is most faithful to the readout? | +1.2 points; 95% interval -0.4 to +2.8; guardrails pass; rollout criterion unmet | +1.2 points; 95% interval -0.4 to +2.8; rollout approved because guardrails pass | +1.2% relative lift; 95% interval -0.4 to +2.8 points; criterion unmet | +1.2 points; 95% interval +0.4 to +2.8; guardrails pass; criterion unmet | The correct slide retains percentage-point units, the negative lower bound, and both conditions of the rollout rule. The alternatives change the decision, scale, or sign.
Why does the +1.2 estimate not satisfy the rule? | The rule uses the interval lower bound, which is -0.4. | The rule requires the upper bound to be negative. | Every positive effect must be ignored. | Guardrails always determine effect size. | The pre-agreed rule explicitly concerns the lower endpoint exceeding one point.
What would be an unsupported next step? | Extend the finished test repeatedly until the original method produces a favorable result. | Report that the decision condition was unmet. | Review a properly designed follow-up study. | Keep the interval visible on the slide. | Opportunistic extension changes the analysis behavior without the approved method needed for valid inference.
Which statement about zero is correct? | Its inclusion does not prove either exact zero effect or equivalence. | Inclusion proves the treatment and control are identical. | Inclusion means no further study can be useful. | Inclusion makes the interval a probability distribution over customers. | An interval containing zero permits uncertainty and does not establish an equivalence conclusion.''',
    dialogue='''Hana | The slide says plus one point two, which looks promising. Can we call the test a win and move to rollout now that it has finished?
Theo | Show the [[point estimate::The point estimate is the single plus-1.2-point estimate, which must be interpreted with its uncertainty and the decision rule.]] with the interval. The estimated increase is one point two percentage points, but the ninety-five-percent interval extends from minus zero point four to plus two point eight.
Hana | That range includes a small negative effect and zero as well as useful positive outcomes. The current slide hides those possibilities by showing only the center.
Theo | Correct. The [[confidence interval::The confidence interval communicates uncertainty under its statistical method instead of treating the estimate as a guaranteed effect.]] belongs beside the estimate. It prevents us from presenting a promising central value as if the uncertainty were negligible or entirely favorable.
Hana | Remind me of the actual rollout rule. I remember that we set a one-percentage-point threshold and also required the guardrails to pass.
Theo | The [[lower bound::The lower bound is minus 0.4 points, which fails the requirement that it exceed plus 1.0 point.]] must exceed plus one point zero, with guardrails passing. Our lower endpoint is minus zero point four, so that condition was not met.
Hana | The guardrails did pass, which is good news. But that is a separate condition, not a substitute for the evidence requirement on completion improvement.
Theo | Exactly. Apply the whole [[decision rule::The decision rule requires both the lower-bound condition and passing guardrails, so one passing condition cannot replace the other.]]. We can acknowledge the guardrail result while saying the test did not authorize rollout under the standard agreed before seeing these results.
Hana | Then should the slide say no effect? Zero is inside the interval, but so are positive effects. I do not want to replace one overclaim with another.
Theo | No. The [[no-change value::Zero is the no-change value on the difference scale, but its presence in the interval does not prove the effect is exactly zero.]] is included, but useful positive effects are included too. The readout does not establish exact zero or show that the two experiences are equivalent.
Hana | Then the decision is clearer than the underlying effect. We know the supplied rollout rule failed, while the magnitude and even direction remain uncertain.
Theo | That is an [[inconclusive result::The result is inconclusive for the desired positive-effect conclusion, while the supplied rollout rule has a definite unmet condition.]] for the desired benefit claim, not permission to hide the estimate. We should report what the evidence supports and what decision it does not support.
Hana | Could we extend it until the lower bound clears one point? Or would that change the rule after we have already seen the result?
Theo | We reached the [[planned endpoint::The planned endpoint has already been reached, so an opportunistic extension would change the agreed analysis behavior.]]. Continuing until the result looks favorable changes the statistical behavior. There is no authorized extension or approved repeated-decision method in the supplied plan.
Hana | A new study might still be justified, but it would need a clear design and rationale rather than an attempt to rescue the original headline.
Theo | Yes. An appropriate [[sequential analysis::Sequential analysis is designed for planned repeated decisions; it cannot be assumed to justify an unapproved extension of this completed test.]] can support planned repeated decisions, but that is not what was specified here. Any new evaluation needs its own reviewed assumptions and rules.
Hana | I will also keep the units visible. Plus one point two means percentage points, not a one-point-two-percent relative increase from an unstated baseline.
Theo | Good. The [[practical threshold::The practical threshold is the one-point business-relevant boundary used in the agreed lower-bound decision condition.]] should be displayed on the same scale. Statistical uncertainty and business value are related in the decision, but they are not interchangeable labels.
Hana | My revised readout will show the center, both bounds, passing guardrails, and the unmet rollout condition. No launch approval or no-effect conclusion will be implied.
Theo | That preserves [[practical significance::Practical significance concerns whether an effect matters for the business, which is not established merely by a positive central estimate.]] as a separate question. The signal may merit well-designed follow-up, but this completed test has not passed the agreed rule for rollout.''',
    transfer_title='Read the endpoint named in the rule',
    transfer_setup='An experiment estimates +0.8 points with a 95% interval from -0.2 to +1.8. The rule requires the lower bound to exceed +0.5, and guardrails pass. The planned test has ended.',
    transfer='''Analyst: "The point estimate is plus ___ points." | 0.8 | The supplied central estimate is positive zero point eight percentage points.
Director: "The lower bound is minus ___ points." | 0.2 | The interval begins at negative zero point two percentage points.
Analyst: "The required boundary is plus ___ points." | 0.5 | The stated lower-bound rule uses positive zero point five as its threshold.
Director: "The rollout condition is ___." | unmet | The negative lower bound does not exceed the required positive threshold.'''))


BOOK['units'].append(unit(
    title='Data Governance and Privacy',
    scene='The analysis needs weekly counts, not customer names',
    rehearsal=['Read turns 1-10. Stress the four needed fields and remaining disclosure review.', 'Switch roles for turns 11-20. Keep access expiry distinct from retention.', 'Check the transfer. Read the fourteen-day proposal without implying approval already exists.'],
    skill='Specify a purpose-limited data request, distinguish pseudonymization from anonymity, and preserve approval and retention controls.',
    brief='Analyst Sara asks data steward Malik for a full customer export to compare weekly late-resolution rates by product tier. The supplied analysis can use week, tier, eligible-case count, and late-case count; names, emails, phone numbers, and free-text comments are unnecessary. A team proposal uses a reviewed aggregate table in the approved workspace with 30-day access, subject to owner approval and disclosure review. Approval is pending. Small groups still require review. Replacing names with stable IDs would not automatically make row-level data anonymous or remove controls.',
    cast='Sara | Data analyst\nMalik | Data steward',
    culture=('Tie each field to the question', 'A constructive data-access discussion explains what information the analysis requires and offers a usable alternative. Avoid assuming that analysts need everything or that every aggregate is harmless. Keep the purpose, approval, audience, and handling conditions visible in the same request.'),
    a='''Which fields directly support the supplied analysis? | Week, tier, eligible-case count, and late-case count | Every customer's name and phone number | Full free-text comments with unrelated details | Passwords and private payment credentials | The question concerns weekly tier-level rates, which the four specified aggregate fields can support.
What is the current approval status? | Pending | Automatic because the data is aggregated | Granted by the analyst's request | Permanent approval for every future purpose | The briefing explicitly leaves owner approval and review incomplete.
What does replacing names with stable IDs establish? | It does not automatically establish anonymity. | All access controls become unnecessary. | Re-identification is impossible in every context. | Every row can be publicly released. | Stable identifiers may still allow linkage, so name removal alone does not establish anonymity.''',
    vocabulary='''data governance | Responsibilities and rules for managing data use. | establish data governance
data steward | A role supporting defined data quality and handling responsibilities. | consult the data steward
data owner | The role accountable for specified data decisions. | obtain data-owner approval
purpose limitation | Restricting data use to defined appropriate purposes. | document the analysis purpose
data minimization | Limiting data to what the stated purpose needs. | apply data minimization
personal data | Information relating to an identifiable person under the applicable rules. | assess personal-data handling
direct identifier | A field that directly identifies a person. | remove unnecessary direct identifiers
indirect identifier | A field that may identify someone when combined with other information. | review indirect identifiers
pseudonymization | Replacing identifying details while retaining possible linkage. | assess pseudonymization safeguards
anonymization | Processing intended to prevent identification under the relevant standard. | evaluate anonymization
re-identification risk | The possibility of connecting data back to an individual. | assess re-identification risk
aggregation | Combining records into group-level summaries. | review aggregation level
small cell | A reported group with few contributing observations. | review small cells
disclosure review | Assessment of risks from releasing or sharing information. | conduct disclosure review
access scope | The specific data and actions a permission covers. | limit access scope
retention period | The duration for which data is kept under defined rules. | document the retention period
access expiry | The point when an access permission ends. | enforce access expiry
approved workspace | An environment authorized for the stated data work. | use the approved workspace
data lineage | The traceable path of data through sources and transformations. | document data lineage
data catalog | An organized inventory of datasets and their metadata. | consult the data catalog
processing purpose | The defined reason for collecting or using data. | state the processing purpose
permitted audience | The people authorized to receive a result or dataset. | define the permitted audience
export restriction | A limit on moving data outside an approved environment. | enforce export restrictions
secondary use | A use beyond the original stated purpose. | review proposed secondary use''',
    precision='The rate needs late-case count divided by eligible-case count within each week and tier. Names and contact details do not support that supplied calculation. Data minimization means enough relevant data for the purpose, not an unusably stripped dataset.',
    precision_extra='Thirty-day access is the proposed local permission duration, not a universal legal retention rule. Access expiry and data deletion are separate matters. Aggregation or stable-ID substitution does not automatically remove disclosure risks or approval requirements.',
    phrases='''Define the purpose | "We are comparing weekly late-resolution rates by tier."
Link fields to the task | "The calculation needs counts by week and tier."
Limit identifiers | "Names and contact details are unnecessary for this question."
Offer an alternative | "Use the reviewed aggregate table."
Preserve the denominator | "Include eligible-case counts as well as late-case counts."
Keep approval visible | "Owner approval is still pending."
State the environment | "The work belongs in the approved workspace."
Bound access | "The proposed access duration is thirty days."
Separate duration rules | "Access expiry is not automatically the data-retention rule."
Check group disclosure | "Small groups still need disclosure review."
Avoid an anonymity claim | "Stable IDs do not automatically make the records anonymous."
Control the audience | "Confirm who may receive the output."
Keep exports governed | "Do not assume approval permits an external export."
Address new purposes | "A different question may need a new review."
Record the source | "Keep the source and transformation lineage."
Close the request | "Submit the purpose, four fields, workspace, duration, and review conditions."''',
    notes='''Necessary | Explain the connection between each field and the question.
Aggregate | A format, not an automatic privacy determination.
Anonymous | A conclusion requiring the applicable assessment.
Pseudonymous | May still allow linkage and require protection.
Thirty days | A case-specific access proposal, not a legal rule.
Approved | State exactly which purpose, audience, and actions are covered.''',
    d='''Which request best matches the supplied need? | Reviewed weekly tier-level counts in the approved workspace, with pending approvals and 30-day access | A full customer export with unlimited future use | Names and phone numbers without case counts | Public release of stable-ID records without review | The correct request supplies the needed measures while preserving the stated handling conditions.
Why include eligible-case count? | It provides the denominator for each rate. | It identifies every customer's phone number. | It proves all small groups are anonymous. | It replaces owner approval. | A late-case count alone cannot show the proportion of eligible cases affected.
Which statement about aggregation is accurate? | It can reduce detail but still needs the stated disclosure review. | Every aggregate is automatically safe to publish. | It always preserves every individual identifier. | It removes the need for an analysis purpose. | The case explicitly requires review, including small-group risks, despite the aggregate format.
What does 30-day access specify? | The proposed duration of permission in this case | A universal legal deletion deadline | Permanent permission after the first month | Approval already granted to all employees | The briefing defines a local access proposal, not a general retention law or completed approval.''',
dialogue='''Sara | I requested the full customer export for weekly late-resolution rates by product tier. I thought extra fields would give us flexibility.
Malik | Start with the [[processing purpose::The processing purpose is the weekly tier-level comparison that determines which fields the analysis needs.]]. The supplied question needs week, tier, eligible-case count, and late-case count. Which part requires names, contact details, or unrestricted free-text comments?
Sara | Those extra fields do not enter the rate. I need late cases divided by eligible cases within each week and tier.
Malik | Then [[data minimization::Data minimization limits the request to sufficient relevant information rather than collecting unrelated personal fields for possible future use.]] supports a narrower request. We should retain what makes the analysis valid, including its denominator, without adding unrelated personal fields simply because they might be interesting later.
Sara | An aggregate table would work for this comparison. I do not need individual rows if the counts use the agreed definitions and can be traced to their source.
Malik | That [[aggregation::Aggregation supplies group-level counts without automatically resolving disclosure risks or approval requirements.]] is a useful alternative, subject to review. We still need to check the output, especially where a group is small enough to raise identification or disclosure concerns.
Sara | So a small tier in one week should not automatically be published just because its row contains counts rather than names. The audience and context still matter.
Malik | Correct. A [[disclosure review::Disclosure review assesses sharing risks, including small groups and the proposed audience.]] remains part of the proposal. Do not treat a change in table shape as an automatic conclusion that all privacy and handling conditions have disappeared.
Sara | If someone later asks for individual records, could replacing customer names with stable IDs make that request anonymous and remove the approval requirement?
Malik | That is usually a [[pseudonymization::Pseudonymization can replace direct names while preserving possible linkage; it does not automatically establish anonymity or remove controls.]] question, not an automatic anonymity claim. Stable identifiers can still support linkage, and the applicable assessment and access controls must remain explicit.
Sara | For this task, I will stay with the reviewed aggregate fields. The proposal also specifies the approved workspace rather than an unrestricted download to any location.
Malik | Keep that in the [[access scope::Access scope defines the permitted data and actions, including the approved workspace rather than an assumed unrestricted export.]]. Owner approval is still pending. A technically convenient format does not authorize an export or make the request approved before the decision is recorded.
Sara | Does thirty-day access also mean deleting the data on day thirty? I need to distinguish the permission expiry from the actual retention rule.
Malik | Exactly. [[Access expiry::Access expiry ends permission; separate approved rules govern how long the data is retained.]] and data retention are separate questions. The actual retention and deletion arrangements need their own approved basis rather than being inferred from this access duration.
Sara | I will also say who needs the results. The service manager needs the reviewed weekly comparison, but that does not imply that anyone may receive the underlying data.
Malik | Define the [[permitted audience::The permitted audience identifies who may receive the approved result and prevents internal approval from becoming an unrestricted-sharing assumption.]] and the output route. The conditions should remain attached to the analysis even after the calculations are complete and somebody wants to reuse a chart.
Sara | If we later need customer-level linkage, I will bring a new purpose and field list. This request should not become permission for unrelated analysis.
Malik | That would be a [[secondary use::Secondary use is a different use beyond the original purpose and may require a new assessment instead of inheriting approval automatically.]] review. We can assess the new need on its facts, but the current weekly-rate purpose should not become a blanket authorization for every future analysis.
Sara | My request will list the four fields, rate, workspace, thirty-day access, audience, and required reviews. Approval remains pending.
Malik | Include the [[data lineage::Data lineage records the source and transformations supporting the aggregate counts so their meaning and quality remain traceable.]] for the aggregate counts as well. That preserves both analytical trust and the handling boundary while giving you the information the actual question needs.''',
    transfer_title='A denominator is necessary; a phone number is not',
    transfer_setup='An analyst needs monthly complaint rates by region. The approved design uses month, region, complaint count, and eligible-order count. Names and phone numbers are unnecessary. Access approval is pending; proposed access lasts 14 days.',
    transfer='''Analyst: "The rate denominator is the eligible-order ___." | count | Eligible-order count provides the base for the complaint rate.
Steward: "Phone numbers are ___ for this question." | unnecessary | The briefing explicitly says phone numbers do not support the stated aggregate analysis.
Analyst: "The proposed access period is ___ days." | 14 | The supplied local proposal specifies fourteen days of access.
Steward: "Approval remains ___." | pending | The briefing says access approval has not yet been granted.'''))

BOOK['units'].append(unit(
    title='Insight Storytelling and Recommendations',
    scene='Five minutes to authorize the right investigation',
    rehearsal=['Read turns 1-10. Keep issue-ticket composition distinct from a mobile failure rate.', 'Switch roles for turns 11-20. Stress investigation only and the two-day readout.', 'Check the transfer. Read the 80% composition result with the issue-ticket denominator.'],
    skill='Lead a short briefing with a bounded action, quantified evidence, explicit limits, and a review point.',
    brief='Analyst Oren has five minutes with operations director Claudia. Two complete weeks use the same ticket definition: issue Q appears in 20 of 1,000 tickets in week one and 80 of 1,000 in week two. Seventy of the later 80 issue-Q tickets are mobile-related; the total mobile-ticket denominator is not supplied. A release occurred between weeks, but cause is unestablished. Oren requests a two-day investigation led by the service analyst, with a readout afterward. Approval is for investigation only, not a production change.',
    cast='Oren | Data analyst\nClaudia | Operations director',
    culture=('Make uncertainty actionable', 'A concise recommendation does not need an invented root cause. State the observed change, why it merits attention, and the smallest defined evidence step that supports the next decision. Acknowledge what a concentration of tickets does not tell you about the wider user population.'),
    a='''How did the issue-Q ticket rate change? | From 2% to 8%, a six-percentage-point rise | From 20% to 80%, a sixty-point rise | From 2% to 8%, a six-percent relative rise | From 8% to 2%, a decline | Twenty and eighty divided by one thousand give two and eight percent, respectively.
What does the mobile count establish? | Seventy of the eighty later issue-Q tickets are mobile-related. | 87.5% of every mobile user experienced the issue. | Every mobile ticket concerns Q. | The mobile failure rate is proven higher than desktop's. | The supplied count describes the composition of issue-Q tickets, not a mobile population failure rate.
What authorization is requested? | A two-day investigation with a subsequent readout | An immediate unreviewed production change | A declaration that the release caused Q | Permanent access to all customer records | The briefing defines a bounded investigation rather than a fix, cause conclusion, or broader permission.''',
    vocabulary='''insight | A decision-relevant interpretation supported by evidence. | state the insight
recommendation | A proposed action with a reasoned basis. | frame the recommendation
decision ask | The precise choice requested from the audience. | lead with the decision ask
headline finding | The main evidence statement in a short briefing. | sharpen the headline finding
supporting evidence | Facts that substantiate a conclusion or recommendation. | present supporting evidence
issue category | A defined class used to group reported problems. | validate the issue category
ticket mix | The composition of support records across categories or groups. | analyze the ticket mix
segment concentration | A large share of observations within a particular subgroup. | report segment concentration
base rate | The underlying frequency relative to an eligible population. | check the base rate
denominator gap | Missing information needed to compute the relevant rate. | disclose the denominator gap
descriptive finding | A statement about observed data without a causal conclusion. | distinguish descriptive findings
causal hypothesis | A proposed explanation of what produced an outcome. | test the causal hypothesis
release timing | The timing of a product or system change. | compare release timing
diagnostic follow-up | Targeted analysis to investigate an observed issue. | scope diagnostic follow-up
investigation owner | The role accountable for the defined inquiry. | assign the investigation owner
time box | A specified limit on the duration of work. | set a time box
readout | A presentation of findings and their implications. | schedule the readout
action boundary | The limit of what a decision authorizes. | state the action boundary
production change | A modification to a live operating system or service. | approve a production change
decision log | A record of choices, reasons, and responsible people. | update the decision log
priority criterion | A stated basis for ordering work. | apply the priority criterion
evidence threshold | The support required for a specified conclusion or next action. | define the evidence threshold
leading question | A question that steers toward a preferred answer. | avoid leading questions
alternative explanation | Another plausible account of an observed pattern. | examine alternative explanations''',
    precision='Issue Q rises from 2% to 8% of tickets: +6 percentage points, four times the earlier rate, or a 300% relative increase. The later mobile share is 70/80 = 87.5% of issue-Q tickets, not of mobile users.',
    precision_extra='A release between the two weeks is a possible lead, not a demonstrated cause. Investigation approval does not authorize a production change. The two-day limit creates a readout point, not a guarantee that a root cause or fix will be found.',
    phrases='''Open with the action | "I recommend a two-day investigation of issue Q."
State the evidence | "The ticket rate rose from 2% to 8%."
Name the unit | "Those rates describe tickets, not unique users."
Give the change | "That is a six-percentage-point increase."
Show the counts | "The counts are 20 of 1,000 and 80 of 1,000."
Identify the concentration | "Seventy of the later eighty issue tickets are mobile-related."
Limit the segment claim | "We do not have the total mobile-ticket denominator."
Keep cause open | "The release timing is a lead, not proof of cause."
Propose the focused check | "Examine affected mobile paths and classification consistency."
Name the owner | "The service analyst would lead the investigation."
Set the duration | "The proposed time box is two days."
Define the output | "Return with evidence, remaining uncertainty, and a next-step recommendation."
Preserve the boundary | "This request does not authorize a production change."
Avoid a discovery promise | "The readout date is not a guaranteed fix date."
Invite the actual decision | "Please approve or decline that investigation scope."
Close the briefing | "The evidence supports investigating now without pretending the cause is settled."''',
    notes='''Rose | State the measure, unit, and comparison periods.
Four times | Means a 300% increase over the original, not 400% growth.
Mostly mobile | Describes case composition, not a denominator-based failure rate.
After | Describes sequence without proving because of.
Two days | Bounds the work, not the certainty of its outcome.
Approve | Keep investigation authority separate from change authority.''',
    d='''Which opening best uses the five-minute meeting? | Approve a two-day investigation of Q; its ticket rate rose from 2% to 8%. | Here are ten unrelated tables with no action request. | The release definitely broke every mobile session. | We should change production immediately because the chart rose. | The opening connects a specific decision to the strongest supplied observation.
What is the relative increase from 2% to 8%? | 300% | 6% | 400% | 87.5% | The six-point increase divided by the two-percent original rate equals three hundred percent.
Why is 70/80 not a mobile failure rate? | Its denominator is issue-Q tickets, not all relevant mobile activity. | Seventy divided by eighty cannot be calculated. | Every issue ticket is a unique mobile user by definition. | The earlier week had no mobile users. | The supplied denominator describes issue composition and cannot substitute for the missing mobile base.
What does approval of this request authorize? | The defined two-day investigation and readout | Any immediate production change the analyst prefers | A public claim that the release caused the issue | An indefinite project without review | The stated action boundary limits approval to the investigation, not implementation or causal claims.''',
dialogue='''Claudia | We have five minutes and ten findings. Which decision needs my attention now, and what evidence supports it?
Oren | My [[recommendation::The recommendation is the proposed two-day investigation tied to the documented rise in issue-Q ticket frequency.]] is a two-day investigation of issue Q. Its share of tickets rose from two percent to eight percent across two complete weeks using the same classification.
Claudia | Give me the actual counts as well. I want to know whether the percentage changed because the ticket base became much smaller.
Oren | The [[supporting evidence::The supporting evidence supplies twenty and eighty issue tickets with the same one-thousand-ticket denominator in each week.]] is twenty of one thousand tickets, then eighty of one thousand. The bases are equal, so the rate increase is not caused by a smaller denominator here.
Claudia | That is six percentage points, and four times the earlier rate. We should not call it six-percent growth or accidentally present ticket counts as unique customers.
Oren | Correct. The [[headline finding::The headline finding states the observed ticket-rate movement with its correct units rather than implying distinct users or a causal explanation.]] is a rise in the issue's ticket rate, not proof of how many distinct people were affected or why the issue increased.
Claudia | Seventy of the eighty are mobile-related. Can I say mobile fails more often than desktop, or are we missing the denominators for that comparison?
Oren | No. That is [[segment concentration::Segment concentration describes where the issue tickets are concentrated, not the failure frequency within all mobile activity.]] within the issue tickets. We lack the total mobile-ticket denominator, so we cannot calculate the relevant mobile rate or compare it fairly with desktop.
Claudia | But the concentration still gives the investigator a useful place to start. We can inspect the mobile paths without overstating what seventy out of eighty means.
Oren | Exactly. Disclose the [[denominator gap::The denominator gap is the missing mobile base required to turn the issue composition into a mobile-specific rate.]] and keep the descriptive finding. Seventy divided by eighty is eighty-seven point five percent of these issue tickets, not of mobile users.
Claudia | A release occurred between the two weeks. That timing sounds relevant, although the current report does not show whether the release actually caused the increase.
Oren | Treat it as a [[causal hypothesis::The causal hypothesis is the possible release explanation, which needs evaluation rather than being asserted from timing alone.]]. The investigation should examine that lead and alternatives, including whether classification or affected paths changed. The sequence alone does not establish cause.
Claudia | Who would lead the work? I want a named role and a defined output, not an open request for somebody to analyze the problem someday.
Oren | The service analyst is the proposed [[investigation owner::The investigation owner is the service analyst responsible for the defined inquiry and subsequent evidence readout.]]. The output is a readout of evidence, remaining uncertainty, and a recommended next step, rather than an unsupported promise of a fix.
Claudia | Two days for an evidence readout, not a guaranteed root cause. Please make that explicit in the invitation before people start expecting a fix.
Oren | It is a [[time box::The time box limits the investigation duration and creates a review point without guaranteeing a causal conclusion or completed fix.]], not a certainty deadline. We should report what the inquiry establishes and what remains unresolved at the readout, even if the original hypothesis is not supported.
Claudia | Does approving this request also allow the analyst to change production if a likely cause appears? I want that distinction written clearly before I decide.
Oren | The [[action boundary::The action boundary restricts the approval to investigation and readout, leaving production changes subject to their separate process.]] is investigation only. Any production change would need its separate evidence, review, and authority. We are not asking this meeting to bypass that process.
Claudia | Then the decision is whether to allocate two days to a documented service issue, with the mobile concentration as a lead and the cause still open.
Oren | Yes. The [[decision ask::The decision ask is the precise approval or rejection of the defined two-day inquiry, not endorsement of an unproven cause.]] is approval of that scope. I will record your decision and preserve the ticket units, missing denominator, and causal limitation in the briefing.''',
    transfer_title='A concentration is a lead, not a rate',
    transfer_setup='Issue R appears in 10 of 500 tickets, then 30 of 500. Twenty-four of the later 30 issue tickets concern mobile. The total mobile base is unknown. The request is a one-day investigation, not a live change.',
    transfer='''Analyst: "The later issue rate is ___ percent." | six | Thirty divided by five hundred equals six percent of all tickets.
Director: "The increase is ___ percentage points." | four | The earlier rate is two percent, so the increase is four points.
Analyst: "Mobile represents ___ percent of later issue tickets." | 80 | Twenty-four divided by thirty equals eighty percent of issue tickets, not mobile users.
Director: "Approval would authorize an ___." | investigation | The supplied request is for investigation only, not a production modification.'''))
