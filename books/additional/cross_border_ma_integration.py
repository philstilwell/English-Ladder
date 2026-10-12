"""Three additional integration conversations on service exit, time zones, and comparable measures."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='A requested extension does not keep a transition service running',
    skill='Separate a contractual service window, a requested extension, and tested replacement capability.',
    setup='The fictional transition service agreement provides seller-operated reporting support through Friday at 18:00 New York local time. The buyer has requested an extension, but none has been agreed. A replacement report can be generated but its totals have not been reconciled. No unapproved work-around, continued seller access, or extension is authorized.',
    cast='Maya | Integration consultant\nEric | Receiving finance lead',
    dialogue='''Maya | The seller provides reporting support until Friday at six in the evening, New York time. Can your team operate independently after that?
Eric | We can generate the replacement report, but its totals have not been reconciled against the approved source.
Maya | Then generation alone does not establish [[standalone capability::Standalone capability requires the receiving operation to perform its defined function reliably without the temporary service, not merely produce an unchecked report.]]. We need to distinguish a working screen from an accepted business result.
Eric | I requested another week of support. The seller acknowledged receiving the request, so I thought we had extra time.
Maya | Receipt is not agreement to the [[extension request::An extension request proposes a change to the service period but does not establish that the other party has agreed to provide it.]]. The current end time remains the planning constraint.
Eric | I will correct the tracker. It currently says extended, which makes the replacement work look less urgent than it is.
Maya | Good. The [[service boundary::The service boundary defines the actual support included, so an extension of time would not automatically add new tasks or broader access.]] also matters. More time, if agreed, would not automatically include extra tasks.
Eric | We need the authorized owners to review any changed scope, cost, access, and support arrangements with the seller.
Maya | Yes. Meanwhile, what evidence is still missing from the replacement report, and who can verify it?
Eric | The finance owner needs the totals reconciled and the discrepancies explained. We have not completed that review.
Maya | Record those [[exit criteria::Exit criteria state the evidence required before leaving the temporary arrangement, including reconciliation rather than merely generating a replacement report.]] explicitly so the exit decision is based on the actual receiving process.
Eric | The timing is tight, but I should not certify the totals or presume continued seller access just to make the dashboard green.
Maya | Correct. Raise the [[continuity risk::The continuity risk is the possible interruption or unreliable operation after support ends, which requires authorized resolution rather than an assumed extension.]] with the decision owner while the current service is still available.
Eric | I can supply the remaining checks, their owners, and the impact if the service ends before the replacement is accepted.
Maya | That makes the escalation actionable. Keep the current contract status separate from any option being discussed.
Eric | If the parties agree an extension, the confirmed terms need to reach the receiving team before anyone changes the plan.
Maya | Exactly. Update the [[transition plan::The transition plan must reflect confirmed service arrangements and actual replacement readiness rather than a requested extension being treated as completed.]] from the authorized decision and preserve the earlier status.
Eric | For now, I will report the Friday end time, the unagreed extension request, and the unresolved reconciliation.
Maya | That is a clear account of what works, what expires, and what still needs a decision.
Eric | I will also name the next update time so neither team assumes the other is silently handling the gap.''',
    transfer_title='Acknowledged was changed to agreed', transfer_setup='The seller acknowledges an extension request but has not agreed to extend support. The original service end time still applies.',
    transfer='''Consultant: "The request was ___." | acknowledged | The seller confirmed receipt, not agreement to the changed service period.
Lead: "An extension has not been ___." | agreed | The supplied facts contain no agreement changing the service duration.
Consultant: "Keep the original end ___ visible." | time | The current service end remains relevant until an authorized change occurs.
Lead: "Escalate the continuity ___." | risk | The possible service gap needs an explicit decision rather than an assumed extension.'''),
scenario(title='One handoff instant appears on two calendar dates',
    skill='Read back a cross-border handoff using a date, time, and explicit UTC offset.',
    setup='For this fictional exercise only, the agreed handoff is 23:00 on 14 November at UTC-05:00, which is 13:00 on 15 November at UTC+09:00. Those explicit offsets define the conversion; no inference about a city\'s seasonal clock rules is needed. The tracker says November 14 without a time or zone. The receiving lead has not accepted the handoff.',
    cast='Noah | US workstream lead\nYuki | Receiving integration lead',
    dialogue='''Noah | The tracker says November fourteenth, but your calendar says the fifteenth. I assumed one of us had moved the handoff.
Yuki | We may be describing the same instant on different local dates. Let us read back the complete timestamp before changing anything.
Noah | Our agreed time is twenty-three hundred on November fourteenth at [[UTC-05:00::The originating timestamp explicitly uses UTC-05:00; the conversion depends on this supplied offset rather than an assumed seasonal city rule.]]. That is the offset written in the handoff plan.
Yuki | For my calendar, the same instant is thirteen hundred on November fifteenth at [[UTC+09:00::The receiving timestamp uses UTC+09:00, fourteen hours ahead of the supplied originating offset, placing the event on the next local date.]]. The dates differ, but the event has not moved.
Noah | Then the short date label loses information we need. It could send someone to the bridge on the wrong day.
Yuki | Exactly. Preserve the [[timestamp::A timestamp that includes the date, time, and offset identifies the intended instant more precisely than a date-only label.]] with its date, time, and offset instead of relying on an unexplained local date.
Noah | The numeric version of the date also needs care because teams may read the month and day in different orders.
Yuki | Use the agreed unambiguous format and read it back. Do not infer that everyone interprets a short numeric date the same way.
Noah | I will update the meeting invitation and tracker together so we do not leave conflicting versions in circulation.
Yuki | Good. Include the source system and the planned [[handoff window::The handoff window specifies the agreed time available for the transfer and should be communicated consistently across calendars.]] rather than only the meeting title.
Noah | We also need to check whether the receiving person can attend at that actual local time, not just whether the invitation was sent.
Yuki | Yes. A sent invitation is not my [[acceptance::Acceptance requires an explicit receiving commitment under the stated handoff process, not merely the existence of a calendar invitation.]] of the operational handoff.
Noah | The reporting pack is ready to share, but I will keep the receiving acceptance open until you confirm the required checks.
Yuki | That is appropriate. The correct timestamp solves the scheduling ambiguity, not the readiness or responsibility questions.
Noah | If the agreed event time changes, we should update both representations from one authoritative source.
Yuki | And record the [[change notice::The change notice communicates an actual schedule change, distinct from correcting two local representations of an unchanged instant.]] so nobody mistakes a formatting correction for a new operational deadline.
Noah | For this correction, the instant remains unchanged: November fourteenth at twenty-three hundred with the minus-five offset.
Yuki | Which is November fifteenth at thirteen hundred with the plus-nine offset. I will confirm availability separately from operational acceptance.
Noah | I will send the corrected record with the open acceptance item and the responsible owner.
Yuki | Good. The teams will share one event and one status, even though their calendars display different dates.''',
    transfer_title='Same instant, different local date', transfer_setup='Use only these supplied equivalents: 23:00 on 14 November at UTC-05:00 equals 13:00 on 15 November at UTC+09:00.',
    transfer='''US lead: "Our local date is November ___." | fourteenth | The originating timestamp explicitly falls on the fourteenth at the minus-five offset.
Receiving lead: "Our local date is November ___." | fifteenth | Adding the fourteen-hour offset difference crosses midnight into the fifteenth.
US lead: "The underlying instant is ___." | unchanged | The two complete timestamps are supplied representations of the same instant.
Receiving lead: "Always include the UTC ___." | offset | The offset defines the conversion without guessing local seasonal clock rules.'''),
scenario(title='Two green delivery dashboards measure different events',
    skill='Reconcile metric definitions before combining acquired and acquiring company performance.',
    setup='The acquired company labels an order on time when it leaves the warehouse by the promised dispatch time. The buyer labels it on time when it reaches the customer by the promised delivery time. In a fictional sample of 100 orders, 95 meet the dispatch promise and 82 meet the delivery promise. No common combined historical metric has yet been agreed.',
    cast='Consultant | Integration reporting lead\nOperations | US operations analyst',
    dialogue='''Consultant | Both dashboards say on-time delivery, but one reports ninety-five percent and the other reports eighty-two. Is one calculation wrong?
Operations | Not necessarily. The first checks whether the order left our warehouse on time; the second checks arrival at the customer.
Consultant | Then the [[metric definition::The metric definition specifies the event being measured, which differs between dispatch and customer arrival despite the shared dashboard label.]] differs even though the dashboard labels look identical.
Operations | Correct. In this sample, ninety-five of the hundred orders met the dispatch promise and eighty-two met the delivery promise.
Consultant | Both calculations use the same [[denominator::The denominator is the hundred orders in this sample, so the difference described here is the measured event rather than a different order count.]], but they answer different operational questions.
Operations | We should not call the thirteen-percentage-point difference a decline after acquisition. We have not established a comparable before-and-after measure.
Consultant | Exactly. We need a [[common baseline::A common baseline requires an agreed comparable definition before historical figures can support a combined trend or integration-effect claim.]] before claiming that integration improved or damaged performance.
Operations | The source records may support both measures, but we need to check the event timestamps and the promise recorded for each order.
Consultant | Document that [[data lineage::Data lineage traces the reported figure to the underlying records and transformations so the team can verify how each measure was produced.]] so the final number can be traced to the actual event and calculation.
Operations | Some orders have a dispatch timestamp but no verified customer-arrival record. That should remain a data gap, not an invented arrival.
Consultant | Yes. Missing arrival evidence must not be silently converted into a pass or treated as proof of the actual delivery time.
Operations | We also need to agree how to handle cancellations and changed promises before combining later reporting periods.
Consultant | Put those rules in the [[measurement specification::The measurement specification records the agreed event, population, exclusions, and calculation rules rather than relying on a familiar but ambiguous label.]] with the owner who can approve the reporting definition.
Operations | Until that is agreed, the steering report can show dispatch performance and arrival performance separately with accurate labels.
Consultant | That will prevent a superficial standardization from producing a misleading [[combined KPI::A combined KPI requires comparable definitions and supporting data; matching labels alone do not make two operational measures interchangeable.]] for the acquired and acquiring businesses.
Operations | Should we average ninety-five and eighty-two and call that our overall delivery score?
Consultant | Not as a substitute for a defined measure. Those percentages describe different events, so their average would answer no agreed question.
Operations | I will relabel the current figures and prepare the definition differences for the process owners to decide.
Consultant | Good. Keep the original records intact so the team can reconstruct the reporting change.
Operations | Then the integration report can explain the current results honestly while the common measurement approach is being established.''',
    transfer_title='A dispatch result became an arrival promise', transfer_setup='Of 100 orders, 95 meet the dispatch promise and 82 meet the arrival promise. The two events must remain separately labeled.',
    transfer='''Analyst: "Ninety-five percent met the ___ promise." | dispatch | The brief assigns ninety-five successful orders to dispatch timing.
Lead: "Eighty-two percent met the ___ promise." | arrival | The brief assigns eighty-two successful orders to customer-arrival timing.
Analyst: "The event definitions are ___." | different | Warehouse departure and customer arrival are distinct operational events.
Lead: "Do not infer an integration-related ___." | decline | These unlike measures do not establish a comparable historical deterioration.'''),
]
