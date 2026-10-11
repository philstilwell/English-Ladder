"""Original time-zone, detention-record, and truck-route conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Whose nine thirty?",
        skill="Read back an appointment with its date and time zone, then compare an arrival estimate on the same clock.",
        setup="Fictional shipment T84: receiving confirms 13 October 2026 at 09:30 Central Daylight Time (CDT, UTC-5). Dispatch uses Eastern Daylight Time (EDT, UTC-4). The parked driver's current ETA is 10:15 EDT that day. The gate requires its actual check-in process; no early entry is promised. Priya and Joel clarify the shared record.",
        cast="Priya|Driver\nJoel|Dispatcher",
        dialogue="""Priya|I'm parked and checking T84. The appointment says nine thirty, but my dispatch screen uses Eastern time. Which clock does the booking mean?
Joel|Receiving confirmed nine thirty [[CDT::The appointment is 09:30 Central Daylight Time, not 09:30 on the dispatcher's Eastern clock.]], Central Daylight Time, on thirteen October. That is their local appointment time.
Priya|Their offset is UTC minus five, and our Eastern daylight setting is UTC minus four. So our clock is an hour ahead of theirs.
Joel|Correct. The same appointment is [[10:30::09:30 at UTC-5 is the same instant as 10:30 at UTC-4, on the same date.]] on the Eastern daylight clock. Don't replace the label and keep nine thirty unchanged.
Priya|Then nine thirty Central and ten thirty Eastern are one appointment, not two slots an hour apart. We haven't asked to reschedule it.
Joel|Exactly. In [[UTC::Coordinated Universal Time gives a common reference: both local appointment times convert to 14:30 UTC.]], Coordinated Universal Time, it is fourteen thirty. Keep the date with each version.
Priya|My ETA currently reads ten fifteen Eastern daylight time on thirteen October. That should be nine fifteen on the receiving clock.
Joel|Yes. Your estimate is [[fifteen::09:15 CDT is fifteen minutes before the 09:30 CDT appointment, after both times are put on the same clock.]] minutes before the appointment, not forty-five minutes late.
Priya|I'd nearly compared ten fifteen on my screen directly with the unlabelled nine thirty in the note. That would have given the wrong impression.
Joel|The [[time zone::The time-zone label identifies which local clock a number belongs to; omitting it creates an invalid comparison.]] is part of the time, not an optional extra. Read both the number and the clock label.
Priya|Will the gate take me at nine fifteen Central if that estimate holds, or does the appointment only settle the booked time?
Joel|The [[check-in procedure::A confirmed appointment does not grant early gate entry; the actual check-in procedure remains applicable.]] still applies. We don't have a promise of early entry or a parking instruction from this time conversion.
Priya|All right. I won't treat fifteen minutes early as permission to enter or unload. I'll use the actual site directions.
Joel|And keep the ETA provisional. Converting it to another clock doesn't turn the estimate into a guaranteed arrival.
Priya|Could you keep Central as the receiving reference and put Eastern beside it? That would help when the desk calls us back.
Joel|Yes: thirteen October, zero nine thirty CDT, equivalent to ten thirty EDT. I'll retain the same shipment reference, T84.
Priya|Do we use those daylight offsets for every date? I've seen the same place described as Central standard time elsewhere.
Joel|No. Verify the location and date. Standard and daylight labels have different offsets; don't carry today's conversion into a different season without checking.
Priya|My read-back is T84, thirteen October, nine thirty CDT; ten thirty EDT; fourteen thirty UTC. ETA ten fifteen EDT is nine fifteen CDT.
Joel|That's consistent. One appointment, one provisional ETA, the same date, and no automatic early-access permission. Those are the details the next dispatcher needs.""",
        transfer_title="Put the estimate on the receiving clock",
        transfer_setup="On 14 October, receiving's appointment is 16:45 EDT (UTC-4). The driver's clock uses CDT (UTC-5), and the ETA is 15:30 CDT that same day. No early-entry agreement is supplied.",
        transfer="""Driver: The appointment on my Central daylight clock is ___ .|15:45|Eastern daylight time is one hour ahead of Central daylight time, so 16:45 EDT equals 15:45 CDT.
Dispatcher: The appointment in UTC is ___ .|20:45|Adding four hours to 16:45 EDT gives 20:45 UTC on the same date.
Driver: My ETA is ___ minutes before the appointment.|fifteen|15:30 CDT is fifteen minutes earlier than the equivalent appointment at 15:45 CDT.
Dispatcher: Early entry remains ___ .|unconfirmed|A clock conversion and early ETA do not establish permission to enter the receiving site.""",
        reference=("NIST: local time, standard/daylight labels, and UTC offsets", "https://www.nist.gov/pml/time-and-frequency-division/local-time-faqs"),
    ),
    scenario(
        title="Three clocks in a waiting bill",
        skill="Separate actual elapsed time, a contract's chargeable interval, and rounded billing units without rewriting the event record.",
        setup="Fictional completed stop: gate check-in 07:40, appointment 08:00, release 10:35, same day and zone. This contract starts 120 free minutes at the later of check-in or appointment, then charges $20 for each started 15-minute block. No other charges apply. Driver Leon and billing coordinator Farah check the calculation; it is not a duty-status or pay determination.",
        cast="Leon|Driver\nFarah|Billing coordinator",
        dialogue="""Leon|My stop record runs from seven forty to ten thirty-five. The invoice worksheet only starts at eight. Has someone changed my arrival time?
Farah|No. The [[check-in timestamp::The actual check-in remains 07:40; choosing a contractual billing start does not change when the driver arrived.]] stays seven forty. Eight is the later of your check-in and the booked appointment, which this contract uses.
Leon|So the time physically at the facility is two hours fifty-five, even though the allowance starts twenty minutes after I checked in.
Farah|Yes, the [[dwell time::From 07:40 to 10:35 is 175 elapsed minutes at the facility; that is distinct from the contractual chargeable interval.]] is one hundred seventy-five minutes on those endpoints. We keep that actual duration in the record.
Leon|The contract gives one hundred twenty minutes from eight. That takes the no-charge period to ten, rather than nine forty.
Farah|Correct. Here [[free time::The contract's 120 free minutes run from 08:00 to 10:00; free describes billing, not off-duty time or wages.]] means the contractual period without this detention charge. It does not mean you were off duty or unpaid.
Leon|Release was ten thirty-five, so thirty-five minutes fall after that allowance. Not fifty-five, which I'd get by starting the allowance at arrival.
Farah|That's the [[chargeable interval::The period after the 10:00 end of free time and before 10:35 release is 35 minutes under these fictional terms.]] under these terms. The early twenty minutes remain in the event record but don't move the billing start.
Leon|And the rate says each started fifteen-minute block. Thirty-five minutes uses two full blocks and part of a third.
Farah|So the [[billing units::Thirty-five minutes occupies three started fifteen-minute blocks; the third partial block is charged under the stated contract.]] are three blocks. At twenty dollars each, the calculated charge is sixty dollars.
Leon|Does charging three blocks mean I should change the release to ten forty-five, so the record matches forty-five billed minutes?
Farah|No. Preserve the actual [[release timestamp::The release remains 10:35; rounding the charge into three blocks does not change the actual event to 10:45.]] of ten thirty-five. Rounding belongs in the calculation, not in a fabricated event time.
Leon|Then the worksheet should show actual dwell one seventy-five, contractual chargeable interval thirty-five, and three billed blocks.
Farah|Yes. Calling all three figures waiting time without labels would make the invoice look inconsistent when each has a different purpose.
Leon|Is the two-hour allowance something I should assume for every customer, or does this contract happen to specify it?
Farah|Use this contract only for this case. Other terms may use another trigger, allowance, rate, or rounding method. Don't present our example as a universal rule.
Leon|And the sixty is the result to submit for billing review, not proof the customer has approved the invoice or that I personally receive sixty?
Farah|Correct. Customer approval and driver compensation are separate matters. This calculation establishes neither, and it doesn't classify your duty status.
Leon|I'll retain seven forty check-in, eight appointment, ten thirty-five release, plus the contract wording supporting the three-block calculation.
Farah|Good. Submit those actual records through the process. Any driving availability still needs its proper assessment; a waiting charge cannot supply extra driving time.""",
        transfer_title="A later check-in changes the start",
        transfer_setup="Appointment 13:00, actual check-in 13:10, release 16:01, same zone/day. This fictional contract gives 120 free minutes from the later time, then $20 per started 15-minute block. No other charges apply.",
        transfer="""Driver: The contractual allowance begins at ___ .|13:10|The later of the 13:00 appointment and 13:10 check-in is 13:10.
Coordinator: The chargeable interval is ___ minutes.|51|The allowance ends at 15:10; release at 16:01 is fifty-one minutes later.
Driver: That occupies ___ started fifteen-minute blocks.|four|Three blocks cover only forty-five minutes; fifty-one minutes starts a fourth.
Coordinator: The calculated charge is $___ .|80|Four blocks multiplied by twenty dollars gives eighty, without changing the actual release time.""",
        reference=("FMCSA: distinguishing facility dwell and detention", "https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations"),
    ),
    scenario(
        title="A car route is not a truck route",
        skill="Report a specific vehicle-height conflict and a proposed alternative without treating a routing suggestion as clearance.",
        setup="Fictional pre-departure call, driver safely parked at the depot: vehicle H7 has verified overall height 4.12 m. A passenger-car route suggests bridge B9, whose posted clearance is 3.90 m. Route C lists a 4.30 m clearance, but other restrictions and current suitability remain unverified. No route is authorized by this exercise.",
        cast="Rosa|Driver\nNeil|Dispatcher",
        dialogue="""Rosa|I'm checking the route before departure. The car-navigation suggestion uses B9, but H7 is four point one two meters high and the bridge says three point nine zero.
Neil|That is a [[clearance conflict::The vehicle height of 4.12 m exceeds the posted 3.90 m clearance, so the suggested route has a direct height conflict.]]. The vehicle is taller than the posted opening, not shorter. Don't use that route suggestion as clearance.
Rosa|The difference is point two two meters. I want the note to be specific rather than just say the bridge looks low.
Neil|State [[twenty-two centimeters::4.12 m minus 3.90 m equals 0.22 m, or 22 cm, by which the vehicle exceeds the posted clearance.]] above the posted clearance. The car route hasn't accounted for the dimensions we're discussing.
Rosa|The saved profile on that screen is a passenger car. The verified four-point-one-two figure is for the actual vehicle H7.
Neil|Then the [[vehicle profile::The vehicle profile must reflect the actual truck; a passenger-car profile does not establish a suitable route for H7.]] is wrong for this job. Use the carrier's process for checking vehicle data and an appropriate commercial route.
Rosa|Someone suggested route C. Its listed clearance is four point three zero meters, which is higher than H7 on those figures.
Neil|The arithmetic [[difference::4.30 m minus 4.12 m gives a nominal 0.18 m difference, not an authorization or guarantee of safe passage.]] is point one eight meters, eighteen centimeters. That number alone doesn't approve the route.
Rosa|Because we haven't checked other restrictions, the current route information, or whether that figure applies to the exact passage we'd use?
Neil|Correct. Current [[route restrictions::Route restrictions include more than a single height figure; route C's complete suitability remains unverified.]] still need review, including the relevant vehicle dimensions and weight restrictions. A higher number is not a complete route assessment.
Rosa|I'll report B9 as a conflict and C as a proposal for review, not change the dispatch note to C approved.
Neil|Keep its [[approval status::Route C is proposed and unverified, not approved merely because its listed clearance exceeds the recorded vehicle height.]] explicit. The appropriate route checks and authorization are still required before treating it as the plan.
Rosa|I'm safely parked at the depot for this discussion. We haven't reached the bridge or started trying to find a way through.
Neil|Good. This is pre-departure planning, not a maneuvering instruction. Don't improvise a passage or alter the vehicle to make a number seem workable.
Rosa|Would it help to keep both units in the note: zero point two two meters and twenty-two centimeters, with exceeds rather than spare clearance?
Neil|Yes. Direction matters. Saying twenty-two centimeters without above or below could reverse the meaning and conceal the conflict.
Rosa|And for C, I should call eighteen centimeters the nominal arithmetic difference, not a safety margin we've verified in practice.
Neil|Exactly. Actual safe and lawful suitability needs the proper assessment. A navigation result also never cancels posted restrictions or current advisories.
Rosa|My message is H7, verified height four point one two meters; B9 three point nine zero, a conflict; C four point three zero, other checks unresolved.
Neil|That's the useful read-back. Keep the vehicle identity, units, restriction source, and proposed-route status together. No departure or passage is authorized by this language exercise.""",
        transfer_title="State the direction of the difference",
        transfer_setup="Before departure, a parked driver checks a verified 4.05 m vehicle against a 3.85 m posted clearance. An alternative lists 4.20 m, but other restrictions and current suitability remain unverified. The exercise authorizes no passage.",
        transfer="""Driver: The vehicle exceeds the first posted clearance by ___ centimeters.|20|4.05 minus 3.85 equals 0.20 m, or twenty centimeters above the posted clearance.
Dispatcher: The proposed alternative lists ___ meters.|4.20|4.20 m is the alternative's listed clearance, not the vehicle's height or the first restriction.
Driver: Its nominal difference above the vehicle height is ___ centimeters.|15|4.20 minus 4.05 is 0.15 m, or fifteen centimeters, without establishing safe suitability.
Dispatcher: The alternative route's suitability is still ___ .|unverified|Other restrictions and current suitability have not been checked, so the arithmetic alone cannot approve the route.""",
        reference=("FMCSA: commercial-vehicle navigation and posted restrictions", "https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/GPS_Visor_Card_508CLN.pdf"),
    ),
]
