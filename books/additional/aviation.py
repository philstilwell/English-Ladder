"""Additional authored aviation service and coordination conversations."""

from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="A bag scan is not a delivery appointment",
        skill="Separate tracing evidence, a delivery arrangement, and a passenger's immediate needs.",
        setup="Ms Chen's checked bag has not arrived. Her bag tag ends 4821; tracing file R62 is open. The last recorded scan is at the transfer airport at 14:10 local. No onward loading or courier assignment is confirmed. She changes hotels tomorrow at noon; agent Luis can update the contact record now.",
        cast="Ms Chen|Passenger\nLuis|Baggage-services agent",
        dialogue="""Ms Chen|Your app says my bag was scanned at the transfer airport. Does that mean it is on the next flight here?
Luis|Not yet. That is the [[last recorded scan::This identifies a recorded handling event, not confirmed onward loading or the bag's present location.]] we can see, at fourteen ten local. There is no confirmed onward loading in the record.
Ms Chen|I have a small tracking device in the bag, and its map also shows that airport. Can you use the location?
Luis|Yes, please share it through our approved baggage-report channel. I will add it to the tracing information, but it does not confirm a flight or delivery time.
Ms Chen|The receipt has one long number and your email has R62. Which should I quote when I contact you?
Luis|Use R62 as the [[tracing reference::R62 identifies the open service case, while the bag tag identifies the checked item.]]. Keep the bag-tag receipt too; the tag ending four eight two one identifies the bag itself.
Ms Chen|I leave my current hotel at noon tomorrow. I do not want the bag delivered there after I have checked out.
Luis|Let us update the address and dates privately now. I will record when you leave this hotel and when the next address becomes valid.
Ms Chen|Can you book the courier for ten tomorrow morning? That would give me time to collect the bag before checkout.
Luis|I cannot confirm a [[delivery appointment::An appointment requires an actual agreed delivery arrangement, which no assigned courier supports here.]] yet. No courier has been assigned. I can record your time constraint and ask the team to contact you about the arrangement.
Ms Chen|Then please do not put ten o'clock in the email as though it were promised. I have already changed my plans once.
Luis|Understood. I will describe it as your requested time, not a confirmed slot. The address change also needs to reach the delivery team when one is assigned.
Ms Chen|I need basic toiletries and a clean shirt tonight. Should I wait until the bag is found before asking about those costs?
Luis|No; I can explain the applicable [[interim-expense claim::This is a separate request concerning necessary expenses during the delay, not evidence that the bag has been delivered.]] process now. Keep itemized receipts, and we will explain the relevant requirements without inventing a reimbursement amount.
Ms Chen|I will keep them. Please send that guidance with the report, so I know which contact route to use.
Luis|I will. We will also check any baggage-fee refund separately under the applicable rules; finding the bag does not itself answer every financial question.
Ms Chen|For the address, please use the new hotel only after noon tomorrow. Before then, my current hotel is still correct.
Luis|I have recorded that [[effective time::The effective time determines when the new address applies, preventing delivery to a superseded location.]]. Please check the two address entries and your contact number on this screen before I submit the update.
Ms Chen|Those details are correct. I will quote R62 if I call, and I understand there is not yet a delivery appointment.
Luis|Thank you. I will send the updated [[case record::The case record documents the tracing status and contact instructions; it is not proof of delivery.]] and claim guidance. We will contact you when the next verified handling or delivery information is available.""",
        transfer_title="Keep the bag tag and case reference distinct",
        transfer_setup="Bag tag 7316 is linked to tracing file R84. A transfer-airport scan is recorded; onward loading is unconfirmed. The passenger's new hotel address takes effect at 18:00 tomorrow. No courier is assigned.",
        transfer="""Agent: Quote tracing file ___ when contacting our team.|R84|R84 identifies the service case; 7316 identifies the checked bag.
Passenger: The new address takes effect at ___ tomorrow.|18:00|The supplied changeover time is eighteen hundred on the following day.
Agent: Onward loading is still ___.|unconfirmed|The transfer-airport scan does not establish that an onward flight carries the bag.
Passenger: I do not yet have a courier delivery ___.|appointment|No assigned courier or agreed delivery slot supports an appointment.""",
        reference=("US DOT: lost, delayed, or damaged baggage", "https://www.transportation.gov/lost-delayed-or-damaged-baggage"),
    ),
    scenario(
        title="An overnight report time needs a date",
        skill="Read back a time-zone conversion and reconcile transport without deciding crew-duty legality.",
        setup="A fictional station uses UTC minus four hours on the supplied dates. Crew report is 02:30 UTC on 9 October. The hotel shuttle is booked for 21:45 station-local time on 8 October. A draft hotel message incorrectly labels the report as 22:30 local on 9 October. No crew-duty or fitness assessment is supplied.",
        cast="Rina|Crew-travel coordinator\nMark|Crew-control liaison",
        dialogue="""Rina|The hotel message says report at twenty-two thirty local on the ninth. The roster says zero two thirty UTC on the ninth. Those cannot both be right.
Mark|Correct. Apply the supplied [[UTC offset::Subtracting the supplied four-hour offset converts the UTC time to this station's local clock.]] of minus four hours. We must retain the date as well as the clock time.
Rina|Zero two thirty minus four hours is twenty-two thirty on the previous day. So the local report is on the eighth, not the ninth.
Mark|Exactly. It crosses [[midnight::The conversion passes into the previous local calendar day, so retaining the UTC date would be wrong.]]. Correct the hotel message to eight October, twenty-two thirty station-local, with nine October, zero two thirty UTC alongside it.
Rina|The shuttle is already booked for twenty-one forty-five local on the eighth. Does that put it forty-five minutes before the report time?
Mark|Yes. On the common local timeline, twenty-one forty-five to twenty-two thirty is forty-five minutes. That arithmetic does not prove the journey allowance is adequate.
Rina|The hotel asked whether the shuttle booking should move to the following evening because the roster shows the ninth.
Mark|Do not move it on that basis. The booking matches the earlier [[calendar date::The shuttle occurs on 8 October locally, before the 22:30 local report on that same date.]] we just verified. Ask the hotel to acknowledge the dated correction.
Rina|For a UTC-only transport list, the pickup becomes zero one forty-five UTC on the ninth. Then both entries use the same UTC date.
Mark|That is right. Put the [[time basis::Explicitly labeling UTC versus station-local time prevents the converted number being read on the wrong clock.]] next to each entry rather than mixing the two clocks in one unlabeled column.
Rina|I will leave the original booking reference attached, so the hotel can identify which pickup we mean. I will not create a duplicate reservation.
Mark|Good. Keep the record of the correction too, especially because someone may already have forwarded the message with the wrong date.
Rina|Can I now mark the crew fit and legal for duty because the transport and report times line up?
Mark|No. A correct transport [[chronology::Chronology orders the scheduled events; it does not establish rest, duty limits, qualifications, or fitness.]] establishes none of those things. The authorized crew-control process must assess the applicable requirements separately.
Rina|Then my update will confirm only the corrected time conversion and the transport booking details that the hotel acknowledges.
Mark|Yes. Do not turn a travel coordination message into a duty approval. We still need the designated team's actual status for that separate question.
Rina|Readback: pickup eight October at twenty-one forty-five local; report eight October at twenty-two thirty local. In UTC, both are on nine October.
Mark|Correct. Their [[scheduled interval::The two scheduled local times are forty-five minutes apart; this describes elapsed time, not a guaranteed journey.]] is forty-five minutes. Whether the transport plan is workable remains subject to the relevant local coordination.
Rina|I will send the correction to the hotel and everyone who received the earlier date, then record the acknowledgements.
Mark|Thank you. Keep the UTC roster entry unchanged; we corrected its local rendering, not the underlying report time or any crew-duty decision.""",
        transfer_title="Cross midnight without shifting the booking",
        transfer_setup="A fictional station is UTC minus five hours on these dates. Report is 01:20 UTC on 12 November, equal to 20:20 local on 11 November. Pickup is 19:40 local on 11 November, equal to 00:40 UTC on 12 November. No duty approval is supplied.",
        transfer="""Coordinator: The local report date is ___ November.|11|Subtracting five hours from 01:20 UTC moves the local date back one day.
Liaison: The UTC pickup time is ___.|00:40|Adding five hours to 19:40 local gives 00:40 on the next UTC date.
Coordinator: Pickup and report are ___ minutes apart.|40|The interval from 19:40 to 20:20 on the same local date is forty minutes.
Liaison: That does not establish crew-duty ___.|approval|The supplied time conversion contains no authorized assessment of applicable duty requirements.""",
        reference=("FAA AIP: measuring and time-reference system", "https://www.faa.gov/air_traffic/publications/atpubs/aip_html/part1_gen_section_2.1.html"),
    ),
    scenario(
        title="Why the freight quote uses more kilograms",
        skill="Explain chargeable weight while keeping actual mass and other charges distinct.",
        setup="A fictional air-cargo quote covers four cartons, each 60 x 50 x 40 cm, with total actual gross mass 64 kg. Its stated tariff uses total cubic centimetres divided by 6,000, then the greater of that result and actual gross mass. The rate is $3.50/kg plus one $20 documentation fee; no other charges or rounding apply to this case.",
        cast="Owen|Shipper\nSalma|Cargo-pricing agent",
        dialogue="""Owen|The scale total is sixty-four kilograms, but your quote uses eighty. Have you added the packaging twice?
Salma|No. The sixty-four is the [[actual gross mass::Actual gross mass is the measured shipment mass including packaging, not the tariff's space-based billing quantity.]], including the cartons. The eighty is a separate billing quantity calculated under the quoted tariff.
Owen|Show me the calculation. All four cartons have the same outside dimensions: sixty by fifty by forty centimetres.
Salma|Each carton occupies one hundred twenty thousand cubic centimetres. Four cartons give four hundred eighty thousand. Dividing by the stated six thousand gives eighty kilograms of volumetric weight.
Owen|So volume becomes a weight-like number for pricing, but that does not mean the shipment actually weighs eighty kilograms.
Salma|Exactly. Under this quote, [[chargeable weight::The tariff selects the larger of actual gross mass and volumetric weight for pricing, without changing physical mass.]] is the greater of sixty-four and eighty. We use eighty for the freight calculation.
Owen|I had multiplied sixty-four by three dollars fifty and expected two hundred twenty-four dollars before the document fee.
Salma|That explains the difference. Eighty times three fifty is two hundred eighty. The [[freight charge::The freight charge is 80 chargeable kilograms times $3.50, separate from the documentation fee.]] is fifty-six dollars higher than your actual-mass calculation.
Owen|And the twenty-dollar fee is once for the shipment, not once for each of the four cartons?
Salma|Once, as stated here. The quote total is three hundred dollars: two hundred eighty freight plus twenty documentation. This example has no other charges.
Owen|Is six thousand always the divisor, whatever airline or service I use?
Salma|No. Check the applicable [[tariff basis::The divisor, rate, minimums, and other conditions depend on the governing tariff rather than this fictional quote alone.]]. We are using this quote's stated conditions, not promising the same divisor or pricing rules for every service.
Owen|Could I enter eighty as the actual weight on the shipment information, so it agrees with the billing line?
Salma|Do not substitute a pricing quantity for measured mass. Keep sixty-four kilograms as the verified actual gross mass, and identify the chargeable quantity separately in the appropriate record.
Owen|Suppose we repack before tendering the shipment. The dimensions might fall, but the gross mass could also change.
Salma|Then we need [[remeasurement::Remeasurement supplies the new dimensions and mass after repacking; the old measurements no longer establish the revised charge.]] and a revised quote under the applicable tariff. Do not retain old figures just because they produce a lower price.
Owen|Understood. For these unchanged cartons, the dimensions establish eighty volumetric kilograms and the scale establishes sixty-four actual kilograms.
Salma|Yes. Neither the price calculation nor this conversation establishes acceptance for carriage, screening status, or operational loading approval.
Owen|Please send the itemized quote with those two quantities, the rate, and the single twenty-dollar fee clearly labeled.
Salma|I will. That preserves the [[pricing breakdown::The breakdown separates actual and chargeable quantities, the freight calculation, and the one-time fee.]] so your purchasing team can reconcile the three-hundred-dollar total without mistaking billing weight for actual mass.""",
        transfer_title="When actual mass is the larger quantity",
        transfer_setup="A fictional quote covers two cartons, each 60 x 40 x 50 cm, total actual gross mass 44 kg. Divide total cubic centimetres by 6,000; charge the greater of actual and volumetric weight. Rate $4/kg, one $14 fee, no other charges or rounding.",
        transfer="""Agent: The total volume gives ___ kilograms of volumetric weight.|40|Two times sixty times forty times fifty equals 240,000; dividing by 6,000 gives forty.
Shipper: The chargeable quantity is ___ kilograms.|44|Actual mass of forty-four exceeds volumetric weight of forty under the supplied tariff.
Agent: The freight charge before the fee is ___ dollars.|176|Forty-four chargeable kilograms multiplied by four dollars gives one hundred seventy-six.
Shipper: With the one-time fee, the total is ___ dollars.|190|Adding the single fourteen-dollar fee to 176 gives 190 dollars.""",
        reference=("IATA: air-cargo tariffs and rules", "https://www.iata.org/en/publications/newsletters/iata-knowledge-hub/air-cargo-tariffs-and-rules-what-you-need-to-know/"),
    ),
]
