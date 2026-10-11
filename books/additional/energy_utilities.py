"""Additional utility billing and storage-language conversations."""

from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Lower energy use, higher demand charge",
        skill="Explain an interval-based demand charge without confusing kilowatts and kilowatt-hours.",
        setup="A fictional business tariff charges $0.10/kWh plus $12/kW for the month's highest 15-minute average demand, with no ratchet or other charges. Monthly energy fell from 10,000 to 9,000 kWh. The highest interval energy rose from 15 to 18 kWh. All other intervals were lower; the two months use the same tariff.",
        cast="Asha|Business customer\nBen|Utility account specialist",
        dialogue="""Asha|We used a thousand fewer kilowatt-hours, but this month's bill is higher. I thought using less electricity would necessarily make the total fall.
Ben|The tariff has two components. Your [[energy charge::The energy charge follows total monthly kWh, giving $900 this month rather than the previous $1,000.]] fell from a thousand dollars to nine hundred. The demand component changed in the other direction.
Asha|I see eighteen on the interval report. Is that eighteen kilowatts, or eighteen kilowatt-hours? The column heading says energy.
Ben|It is eighteen kilowatt-hours within the highest [[demand interval::The stated demand interval is fifteen minutes, or one quarter of an hour, over which average power is calculated.]]. Fifteen minutes is a quarter of an hour, so eighteen divided by a quarter gives seventy-two kilowatts.
Asha|Last month's highest interval was fifteen kilowatt-hours. Dividing by a quarter gives sixty kilowatts, not fifteen.
Ben|Correct. Those are the two monthly [[billing-demand values::The fictional tariff uses the maximum fifteen-minute average: 60 kW previously and 72 kW now, with no ratchet.]] under this tariff: sixty and seventy-two. The interval report confirms that no other interval was higher.
Asha|At twelve dollars per kilowatt, last month's demand charge was seven hundred twenty dollars. This month's is eight hundred sixty-four.
Ben|Yes, an increase of a hundred forty-four dollars. The hundred-dollar energy saving is smaller, so the combined total rises by forty-four dollars.
Asha|Then the totals are seventeen hundred twenty before and seventeen hundred sixty-four now. That reconciles, even though monthly energy fell ten percent.
Ben|Exactly. Your [[peak demand::Peak demand here is the highest interval-average power, not total monthly energy or a momentary equipment reading.]] rose twenty percent, from sixty to seventy-two kilowatts. A reduction in total energy does not determine that peak.
Asha|Could one brief equipment start-up be the whole explanation? Someone showed me a momentary reading from a machine display.
Ben|That display alone cannot establish this fifteen-minute average. We need the interval timestamp and relevant site records before attributing the peak to a particular event.
Asha|We are discussing moving some equipment use to a different time. Would that guarantee a lower demand charge?
Ben|No. [[Load shifting::Load shifting changes when demand occurs; it may move rather than reduce the highest billed interval.]] could create a different peak. The authorized site team needs to assess any change, and we can then examine its effect under the actual tariff.
Asha|So I should not add the individual equipment ratings and assume that total was the measured maximum at the meter.
Ben|Right. Ratings, simultaneous use, measured interval demand, and billing demand are different quantities. This case gives us the measured intervals and a simple tariff rule.
Asha|You mentioned no ratchet. What does that mean for the calculation you just showed me?
Ben|A [[demand ratchet::A demand ratchet can link billed demand to earlier demand or another contractual floor; the fictional tariff expressly excludes it.]] can carry a previous peak or other tariff basis into later billing. We have explicitly excluded that feature here; other tariffs may use it.
Asha|Please send the two component calculations and the timestamp of the highest interval, so our facilities team can review the actual event.
Ben|I will. The supported result is lower monthly energy, higher interval demand, and a forty-four-dollar increase under these supplied terms, not evidence of a faulty meter or a known equipment cause.""",
        transfer_title="Convert the quarter-hour quantity first",
        transfer_setup="A fictional tariff charges $0.10/kWh plus $12/kW for the highest 15-minute average, with no other charges or ratchet. Monthly use is 8,000 kWh. The highest 15-minute interval contains 20 kWh; all other intervals are lower.",
        transfer="""Specialist: The highest average demand is ___ kW.|80|Twenty kilowatt-hours divided by one quarter-hour equals eighty kilowatts.
Customer: The monthly energy component is $___.|800|Eight thousand kilowatt-hours at ten cents each gives eight hundred dollars.
Specialist: The demand component is $___.|960|Eighty billed kilowatts multiplied by twelve dollars gives nine hundred sixty dollars.
Customer: The combined total is $___.|1,760|Eight hundred plus nine hundred sixty equals seventeen hundred sixty dollars.""",
        reference=("PG&E: demand charges and bill components", "https://www.pge.com/en/account/billing-and-assistance/understand-your-bill.html"),
    ),
    scenario(
        title="An actual water reading reconciles earlier estimates",
        skill="Explain a cumulative meter register and a catch-up quantity without inventing when the water was used.",
        setup="A fictional property meter read 1,000 cubic metres on 1 January, actually measured. Its 1 March reading of 1,030 was estimated; 30 cubic metres were already billed. An actual 1 April reading is 1,060. The same meter, register units, and multiplier of one are verified; no rollover or replacement occurred. Rates and other charges are not supplied.",
        cast="Mara|Property manager\nIdris|Water-account adviser",
        dialogue="""Mara|The new statement uses a reading of one thousand sixty. Surely our building did not use that much water in one month?
Idris|That number is the [[cumulative register::The cumulative register records the meter's running total; period usage comes from a difference between comparable readings.]], not the month's consumption. We need the difference between comparable readings and then account for what was already billed.
Mara|The last actual reading was one thousand on the first of January. The first-of-March figure was one thousand thirty, but it was marked estimated.
Idris|Correct. The new [[actual reading::The 1 April figure of 1,060 is measured, unlike the estimated intermediate figure of 1,030.]] gives sixty cubic metres since that January measurement. It does not tell us the exact split between individual months.
Mara|Thirty cubic metres have already been billed using the March estimate. Does the new statement charge all sixty again?
Idris|No. After the [[previously billed quantity::Thirty cubic metres have already been billed; subtracting them from sixty leaves thirty to reconcile rather than charging sixty again.]] is accounted for, thirty cubic metres remain to reconcile. We are not adding sixty on top of the earlier thirty.
Mara|So can I tell the tenants that March's actual use was exactly thirty cubic metres?
Idris|Not from these readings. The intermediate figure was an estimate. The new actual reading establishes the January-to-April total, not exactly when within those months the water passed through the meter.
Mara|That means the additional thirty may include a correction to earlier estimated use as well as water used after the estimate date.
Idris|Yes. Call it a [[catch-up adjustment::A catch-up adjustment reconciles the cumulative actual total with earlier estimated billing; it does not establish one month's measured usage.]], with the dates and earlier estimate visible. Avoid relabeling it as independently measured March consumption.
Mara|Before we accept the numbers, could this be a different meter or a change of units? We have several properties on the account.
Idris|For this case, the meter identity, units, and multiplier of one are verified, with no replacement or rollover. Those checks matter before comparing register values.
Mara|The register is in cubic metres, while a tenant asked for litres. What is the whole January-to-April difference in litres?
Idris|Sixty cubic metres is sixty thousand litres. Keep that [[unit conversion::One cubic metre equals one thousand litres; sixty cubic metres therefore equals sixty thousand litres.]] separate from billing: the quantity still covers the full period between the two actual readings.
Mara|Does the larger-than-estimated reading prove there is a leak, or that the meter is faulty?
Idris|Neither conclusion follows from the catch-up calculation alone. We can route a consumption or meter concern for the appropriate review without guessing its cause from an underestimated bill.
Mara|Please show the reconciliation in writing, including the estimate label. I also need to know whether the amount due is correct, not just the volume.
Idris|The [[billing calculation::The monetary calculation requires applicable rates, billing periods, and other charges; the supplied volume alone does not determine the amount due.]] needs the applicable rates and charges, which are not supplied in this language example. We must check those separately for a real account.
Mara|Then my summary is sixty cubic metres measured between January and April, thirty already billed, and thirty left to reconcile, with no exact monthly split.
Idris|That is accurate. I will retain the actual and estimated labels and refer any disputed account details through the proper review route, without treating this reconciliation as a leak diagnosis.""",
        transfer_title="Reconcile the running total once",
        transfer_setup="The same verified meter reads 3,000 cubic metres actually on 1 January, an estimated 3,025 on 1 March, and an actual 3,038 on 1 April. Twenty-five cubic metres were billed. Multiplier one; no replacement, rollover, rates, or other charges are supplied.",
        transfer="""Adviser: Actual use between January and April totals ___ cubic metres.|38|The difference between the actual readings is 3,038 minus 3,000, or thirty-eight.
Manager: The remaining quantity to reconcile is ___ cubic metres.|13|Thirty-eight total minus twenty-five previously billed leaves thirteen, without billing the earlier quantity twice.
Adviser: The intermediate March figure was ___.|estimated|The supplied March register figure was estimated rather than independently measured.
Manager: These readings do not establish an exact ___ split.|monthly|Two actual readings with an estimated point between them do not determine each month's actual usage.""",
        reference=("NYC DEP: actual and estimated water readings", "https://www.nyc.gov/site/dep/pay-my-bills/water-sewer-bills-frequently-asked-questions.page"),
    ),
    scenario(
        title="Battery power is not duration",
        skill="Distinguish storage power, energy, usable output, and a conditional duration calculation.",
        setup="Fictional battery ratings: 20 MW and 80 MWh. Engineers supply 60 MWh usable AC energy, net of losses and reserves. Assume constant 20 MW output and no further derating. No dispatch authorization or backup capability is established. A separate measured cycle used 75 MWh to deliver 60 MWh.",
        cast="Joel|Utility program manager\nNina|Storage analyst",
        dialogue="""Joel|The presentation says this twenty-megawatt battery provides twenty hours of backup. I cannot find the calculation behind that sentence.
Nina|There is no valid calculation in that statement. [[Power capacity::Power capacity describes the rate of output, in MW; it cannot by itself specify how many hours the battery can deliver energy.]] is twenty megawatts, while the separate nameplate energy rating is eighty megawatt-hours.
Joel|If we divide eighty megawatt-hours by twenty megawatts, the nameplate ratio is four hours. That is already very different from twenty.
Nina|Use the supplied [[usable energy::Usable energy is the 60 MWh engineers make available at the AC boundary after losses and reserves, not the 80 MWh nameplate figure.]] for this case: sixty megawatt-hours at the AC boundary, already net of losses and reserves.
Joel|At a constant twenty-megawatt output, sixty divided by twenty gives three hours under those assumptions. Is that the calculation we should show?
Nina|Exactly. Label it a conditional [[discharge duration::The conditional duration is usable energy divided by constant output: 60 MWh divided by 20 MW equals three hours.]], not a site backup guarantee. Actual availability and the operating arrangement still require the relevant engineering assessment.
Joel|The separate cycle used seventy-five megawatt-hours to deliver sixty. That ratio is eighty percent, so should I multiply the usable sixty by eighty percent again?
Nina|No. The usable AC figure already allows for losses. The measured cycle's [[round-trip efficiency::Round-trip efficiency compares delivered energy with charging input; 60 divided by 75 is 80%, not another deduction from already-net usable energy.]] is sixty divided by seventy-five: eighty percent, not another deduction.
Joel|So eighty percent efficiency is not eighty percent state of charge, or a twenty-percent reduction in the power rating.
Nina|Correct. Keep the measurement boundary explicit. Energy losses, charge state, and power limits describe different quantities.
Joel|Suppose the illustrative output were ten megawatts instead, still with sixty usable megawatt-hours and no other constraints. The simple duration would be six hours.
Nina|Yes, under that simplified constant-output assumption. Do not describe it as extra stored energy; the same energy is being delivered at a lower rate.
Joel|Our customer asks for twenty-five megawatts. Could we promise a shorter run because sixty divided by twenty-five still gives a number?
Nina|No. That requested rate exceeds the stated [[power limit::The 25 MW request exceeds the 20 MW power rating; dividing energy by an unsupported output rate cannot establish capability.]] of twenty megawatts. A duration calculation cannot authorize or establish operation beyond the supplied capability.
Joel|We also have not established islanding or the customer's critical-load arrangement. Calling the three hours backup would hide those missing conditions.
Nina|Exactly. Having stored energy does not by itself establish a functioning backup supply. The actual connection, controls, loads, and authorized operating plan need their own basis.
Joel|I will show both nameplate ratings and a separate planning line for sixty usable megawatt-hours at a constant twenty-megawatt output.
Nina|Keep the [[operating assumptions::Operating assumptions state the supplied usable-energy boundary, constant output, and absence of further derating; the calculated duration is conditional on them.]] beside the three-hour result. That prevents someone reusing it for a different state, output, or site without checking.
Joel|And the measured eighty-percent round-trip efficiency belongs in its own line, with seventy-five input and sixty delivered, rather than another deduction.
Nina|Correct. Remove twenty hours and the unsupported backup promise. The revised slide will distinguish power, energy, the conditional duration, and measured efficiency without supplying a dispatch instruction.""",
        transfer_title="Use net available energy once",
        transfer_setup="A fictional system has a 6 MW output limit and 15 MWh usable AC energy already net of losses and reserves. Assume constant 6 MW output and no further derating. A measured cycle used 20 MWh charging energy to deliver 15 MWh. No actual operating permission is supplied.",
        transfer="""Analyst: The conditional duration is ___ hours.|2.5|Fifteen usable megawatt-hours divided by six megawatts gives two and a half hours.
Manager: That duration equals ___ minutes.|150|Two and a half hours multiplied by sixty gives one hundred fifty minutes.
Analyst: The measured round-trip efficiency is ___ percent.|75|Fifteen delivered megawatt-hours divided by twenty charging megawatt-hours equals seventy-five percent.
Manager: Applying that efficiency again would ___ the losses.|double-count|The fifteen-MWh usable figure is already net of the stated losses, so another deduction repeats them.""",
        reference=("EIA: battery power, energy, and duration", "https://www.eia.gov/todayinenergy/detail.php?id=51798"),
    ),
]
