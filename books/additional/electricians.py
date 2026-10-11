"""Original lighting-estimate, enclosure-rating, and power-report conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Watts saved are not the bill",
        skill="Explain a lighting estimate with separate power, energy, tariff, and simple-payback figures.",
        setup="Fictional estimate: 12 existing fittings use 40 W each; 12 proposed fittings use 24 W each, including drivers. Assume constant full-power operation for 10 hours on 250 days yearly and an energy-only rate of $0.20/kWh. Added project cost is $480. Exclude demand charges, maintenance, financing, and other changes; lighting performance and replacement approval remain separate.",
        cast="Asha|Electrical estimator\nBen|Client",
        dialogue="""Ben|The proposal says sixteen watts saved. Is that for the whole room, and does it mean sixteen dollars off each electricity bill?
Asha|Sixteen watts is the difference per fitting. With twelve fittings, the modeled [[power reduction::Twelve times the sixteen-watt difference gives 192 watts, equivalent to 0.192 kilowatts, not a bill amount.]] is one hundred ninety-two watts, or zero point one nine two kilowatts.
Ben|The existing total is four hundred eighty watts, and the proposed total is two hundred eighty-eight. Both figures already include the drivers?
Asha|Yes. Keep the [[system input::The supplied forty- and twenty-four-watt figures include their drivers; adding another driver allowance would count power twice.]] basis consistent. We don't add a second driver allowance to figures that already include it.
Ben|The schedule assumes ten hours a day for two hundred fifty days. That is twenty-five hundred hours a year, not every hour of the calendar year.
Asha|Multiply the kilowatt difference by those hours for the estimated [[energy saving::0.192 kilowatts multiplied by 2,500 hours equals 480 kilowatt-hours per year under the supplied assumptions.]]: four hundred eighty kilowatt-hours yearly. Watts describe a rate; kilowatt-hours describe energy over time.
Ben|So sixteen watts per fitting becomes four hundred eighty kilowatt-hours for the annual comparison, not four hundred eighty kilowatts of power.
Asha|Correct. At the supplied [[energy tariff::The fictional energy-only rate is twenty cents per kilowatt-hour; multiplying 480 by $0.20 gives $96 per year.]] of twenty cents per kilowatt-hour, the modeled energy-cost reduction is ninety-six dollars a year.
Ben|And the extra project cost is four hundred eighty dollars. Dividing that by ninety-six gives five years, but what kind of payback figure is that?
Asha|A [[simple payback::The additional $480 divided by $96 annual modeled energy savings equals five years, without financing, discounting, or other cost changes.]] estimate. It ignores financing, discounting, maintenance differences, and any other benefits or costs excluded from this worksheet.
Ben|Could I put guaranteed five-year return in the budget note? It sounds cleaner than listing all these assumptions, but perhaps too certain.
Asha|Don't turn the estimate into a [[guarantee::The result depends on operating hours, stated power, tariff, and exclusions; the calculation is not a guaranteed bill reduction or investment return.]]. Actual hours and tariff terms can change, and the worksheet doesn't model every part of a bill.
Ben|If the building has a demand charge, can I assume the one-hundred-ninety-two-watt difference also reduces that charge by the same proportion?
Asha|No. The demand charge and how the building's billing peak is determined need their own assessment. This example models energy charges only.
Ben|What if the room uses dimming or occupancy control? The full-power schedule might overstate how long each fitting runs at the listed power.
Asha|Exactly. We'd need a supported operating profile for that estimate. We shouldn't keep the same hours and claim an additional control saving without checking overlap.
Ben|And a favorable cost comparison doesn't show that the alternative gives the right light on the desks or works with the specified controls.
Asha|Those requirements still need review. A power-and-cost calculation doesn't approve substitution, establish compatibility, or instruct anyone to replace electrical equipment.
Ben|I'll report one hundred ninety-two watts less under the model, four hundred eighty kilowatt-hours a year, ninety-six dollars energy saving, and five-year simple payback.
Asha|Include the twelve fittings, twenty-five hundred hours, and twenty-cent rate beside that summary. Then a reviewer can see what drives the result and what it leaves out.""",
        transfer_title="Change the operating hours",
        transfer_setup="Fictional comparison: 8 fittings change from 50 W to 30 W each, with drivers included. Assume 1,500 full-power hours yearly, energy-only rate $0.25/kWh, and added cost $180. Use only these assumptions.",
        transfer="""Client: The total power reduction is ___ watts.|160|Eight times the twenty-watt difference gives 160 watts, or 0.16 kilowatts.
Estimator: The annual energy reduction is ___ kilowatt-hours.|240|0.16 kilowatts multiplied by 1,500 hours gives 240 kilowatt-hours.
Client: The modeled energy-cost reduction is ___ dollars yearly.|60|240 kilowatt-hours at $0.25 each gives sixty dollars per year.
Estimator: The simple payback is ___ years.|three|The $180 added cost divided by $60 annual modeled savings is three years, not a guaranteed financial return.""",
        reference=("Virginia Cooperative Extension: power, operating hours, and energy-cost estimates", "https://www.pubs.ext.vt.edu/2901/2901-9014/2901-9014.html"),
    ),
    scenario(
        title="Read the two protection digits",
        skill="Explain an enclosure rating without turning a larger code into blanket approval.",
        setup="Fictional procurement review: proposed enclosure A is marked IP65; alternative B is marked IP67 only. The project asks for evidence covering dust and water-jet exposure. No other test claims or approval are supplied. First digit 6 means dust-tight; water digit 5 covers jets, while 7 covers temporary immersion under specified conditions. Suitability of the complete installation remains for review.",
        cast="Marta|Buyer\nOwen|Electrical coordinator",
        dialogue="""Marta|Owen, the alternative enclosure says IP67 and the specified option says IP65. Can I record sixty-seven as better protection and approve the substitution?
Owen|Don't compare them as one score. An [[IP code::The two characteristic numerals describe different protection categories; sixty-seven is not a single overall score that automatically replaces sixty-five.]] has separate characteristic digits. We need to read what each position says and what exposure the project requires.
Marta|Both start with six. Does that mean they make the same stated dust claim, even though the second digits differ?
Owen|Yes, six denotes [[dust-tight::The first digit six states dust-tight protection under the applicable classification conditions; it is not an airtight or universal safety guarantee.]] protection under the classification conditions. It doesn't mean airtight, chemically resistant, or suitable for every environment.
Marta|The project asks for water-jet evidence. A ends in five. What does that part of its rating cover?
Owen|It covers [[water jets::The second digit five addresses water jets under the specified test conditions; it does not establish unlimited pressure, temperature, or immersion resistance.]] under specified test conditions. It isn't a promise of resistance to every pressure, cleaning chemical, or water temperature.
Marta|B ends in seven, which concerns immersion. Doesn't immersion automatically include passing the lower-numbered jet tests too?
Owen|No. [[Temporary immersion::The second digit seven concerns temporary immersion conditions and does not automatically establish the separate jet-resistance claims of digits five or six.]] is a different exposure. An IP67-only statement doesn't by itself establish the jet evidence requested for this review.
Marta|Then we should ask for the relevant test evidence rather than assume the extra two in the number settles it. We can't mark B accepted yet.
Owen|Correct. A product may have a [[dual rating::A product can state separately demonstrated jet and immersion classifications; the dialogue supplies only IP67 for B, not an additional jet rating.]] if both claims are supported. We aren't supplied that additional evidence for B.
Marta|The vendor also calls it waterproof. I suppose that word doesn't resolve which exposure, duration, or configuration the product was assessed for.
Owen|Exactly. We need the [[declared configuration::Protection claims apply to the relevant enclosure configuration; entries, fittings, seals, and assembly conditions must be checked rather than inferred from a bare-box label.]] and supporting documentation. Cable entries, fittings, seals, and assembly conditions matter to the complete arrangement.
Marta|So A's IP65 marking answers the code-description question, but doesn't by itself prove the installed assembly meets everything the project needs.
Owen|Right. The actual specification, environment, manufacturer requirements, and technical review still apply. Neither this comparison nor the label authorizes installation.
Marta|Could I translate IP65 directly into a NEMA enclosure type for the purchasing system? It has a field for each.
Owen|Don't invent a one-to-one equivalent. The classification systems have different scopes; record a NEMA claim only when the relevant product evidence supports it.
Marta|I'll keep A as IP65 and B as IP67 only, with the jet evidence for B unresolved. I won't replace either with the general word waterproof.
Owen|Good. And don't suggest testing them with a hose on site to settle the paperwork. This is a documentation review, not a test instruction.
Marta|The request to the vendor is for supported jet classification and the rated configuration, with the substitution still pending review.
Owen|That's specific. It preserves the distinction between dust protection, jet resistance, immersion, and acceptance of the actual project arrangement.""",
        transfer_title="A rating is not one score",
        transfer_setup="A fictional data sheet lists IP66; a proposed alternative lists IP67 only. For this exercise, first digit 6 means dust-tight, water digit 6 means powerful-water-jet protection, and water digit 7 means temporary-immersion protection under specified conditions. No other evidence is supplied.",
        transfer="""Buyer: The shared first digit describes ___ protection.|dust-tight|Both first digits are six, which addresses dust-tight protection under the classification conditions.
Coordinator: IP66 declares the stated ___ category.|powerful-water-jet|The second six refers to powerful water jets, not an immersion classification.
Buyer: IP67 declares the stated ___ category instead.|temporary-immersion|The second seven concerns temporary immersion under specified conditions.
Coordinator: The alternative's separate jet evidence remains ___ .|unconfirmed|An IP67-only claim does not itself establish IP66 jet classification or authorize the substitution.""",
        reference=("Rittal: protection categories under IEC 60529 and NEMA", "https://www.rittal.com/uk-en/service/Technical-Information/Protection-categories"),
    ),
    scenario(
        title="Power factor is not efficiency",
        skill="Read a completed electrical report while keeping active power, apparent power, energy, and efficiency distinct.",
        setup="Fictional completed report for one single-phase load: RMS voltage 230 V, RMS current 10 A, active input power 1.84 kW, constant for 2 hours. RMS means root mean square. Use apparent power = RMS volts x RMS amperes / 1,000 in kVA; power factor = kW/kVA. No output-power, circuit-capacity, or authorization data are supplied.",
        cast="Sofia|Facilities coordinator\nRavi|Electrician",
        dialogue="""Sofia|Ravi, I multiplied two hundred thirty volts by ten amperes and got twenty-three hundred. I nearly put two point three kilowatts in the summary.
Ravi|That product gives [[apparent power::For the supplied single-phase RMS values, 230 times 10 equals 2,300 VA, or 2.3 kVA; it is not automatically 2.3 kW.]]: twenty-three hundred volt-amperes, or two point three kVA. It doesn't automatically give the active kilowatt value.
Sofia|The completed report separately records one point eight four kilowatts. So I shouldn't replace that reading with the voltage-current product.
Ravi|Correct. One point eight four is the [[active power::The supplied active input power is 1.84 kW; it is a separate quantity from the 2.3 kVA apparent-power calculation.]] figure here. Preserve both quantities with their units instead of treating kW and kVA as interchangeable labels.
Sofia|Then one point eight four divided by two point three is zero point eight. That's the ratio the report calls PF?
Ravi|Yes, [[power factor::Power factor is active power divided by apparent power; 1.84 divided by 2.3 equals 0.8, a dimensionless ratio.]]. It's a dimensionless ratio, not another power value. The stated calculation gives zero point eight for this report.
Sofia|Does zero point eight mean the machine is eighty percent efficient and loses twenty percent of its input as heat?
Ravi|No. [[Efficiency::Efficiency compares useful output with input, which is different from power factor; the report supplies no useful-output figure from which to calculate it.]] compares useful output with input. We don't have the machine's output here, so that conclusion isn't available from PF.
Sofia|The report says the active input stayed constant for two hours. For energy, should I multiply one point eight four by two?
Ravi|Yes. That gives three point six eight [[kilowatt-hours::Constant active input of 1.84 kW for two hours gives 3.68 kWh; using 2.3 kVA would not calculate this active-energy quantity.]] of active energy. Multiplying two point three kVA by two would describe a different quantity, not this kWh result.
Sofia|So power is the rate, energy includes the time, and power factor is the ratio between two power quantities. They're three different parts of the explanation.
Ravi|Exactly. Keep the [[measurement basis::The case uses completed single-phase RMS readings and a stated constant two-hour period; it does not supply a three-phase calculation or operating procedure.]] visible: single-phase, the supplied RMS values, and the stated period. Don't transplant the arithmetic into a different system without the right assessment.
Sofia|Can the ten-ampere figure tell us the circuit has enough spare capacity for another machine? The owner asked whether we could add one.
Ravi|No. A recorded current for this load doesn't establish the full installation requirements or spare capacity. Those need the appropriate technical assessment.
Sofia|Would increasing the power factor to one guarantee a twenty-percent reduction in the electricity bill? That sounds like another tempting shortcut.
Ravi|It wouldn't follow from these figures. The load behavior, losses, tariff, and any proposed change need review. We aren't recommending correction equipment or predicting a saving.
Sofia|And this discussion doesn't ask anyone to obtain new readings, open equipment, or connect a test instrument. We're interpreting the completed report.
Ravi|Correct. It supplies no testing method or operating permission. The actual qualified procedures remain separate from this language and arithmetic exercise.
Sofia|I'll report two point three kVA apparent, one point eight four kW active, PF zero point eight, and three point six eight kWh over the stated two hours.
Ravi|That's accurate. Leave efficiency and spare capacity unestablished, and retain the original readings and time basis so the summary can be checked.""",
        transfer_title="Read a second completed report",
        transfer_setup="A fictional single-phase report gives 120 V RMS, 5 A RMS, and constant active input of 0.48 kW for 3 hours. Use the same formulas. Useful output is not supplied. Do not infer circuit capacity or operating permission.",
        transfer="""Coordinator: Apparent power is ___ kVA.|0.6|120 times 5 equals 600 VA, or 0.6 kVA.
Electrician: Power factor is ___ .|0.8|0.48 kW divided by 0.6 kVA gives the dimensionless ratio 0.8.
Coordinator: Active energy for the period is ___ kWh.|1.44|Constant 0.48 kW multiplied by three hours equals 1.44 kWh.
Electrician: Useful-output efficiency remains ___ .|unknown|No useful-output figure is supplied, so the power-factor ratio cannot establish efficiency.""",
        reference=("Schneider Electric: true power factor and displacement power factor", "https://blog.se.com/energy-management-energy-efficiency/2020/02/20/distortion-displacement-and-the-truth-understanding-true-power-factor/"),
    ),
]
