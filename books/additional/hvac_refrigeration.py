"""Original HVAC cooling-load, air-exchange, and refrigerant-report conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Total cooling hides the split",
        skill="Compare sensible and latent cooling separately instead of relying on one total rating.",
        setup="Fictional comparison on a consistent net-capacity basis at the same stated operating conditions: room load is 10 kW sensible plus 2 kW latent. Option A supplies 12 kW total, including 9 kW sensible; B supplies 13 kW total, including 10.4 kW sensible. Total = sensible + latent; sensible heat ratio (SHR) = sensible / total. Actual equipment selection and installation are not approved.",
        cast="Mina|Facilities manager\nTheo|HVAC estimator",
        dialogue="""Mina|Option A says twelve kilowatts, exactly the room's total load. Can I mark it as meeting the requirement before we compare the price?
Theo|We need the split. The room's [[sensible load::The supplied ten-kilowatt sensible load concerns temperature change; it must be compared with sensible capacity, not total capacity alone.]] is ten kilowatts, while A's sensible capacity is nine. Matching the totals hides a one-kilowatt shortfall.
Mina|And the other two kilowatts in the room load concern moisture removal. They aren't another two degrees of temperature reduction.
Theo|Correct. That's the [[latent load::The two-kilowatt latent load concerns the moisture-removal part of this cooling duty; it is not a temperature value in degrees.]]. Sensible cooling concerns temperature change; latent cooling here concerns condensation of water vapor removed from the air.
Mina|If A has twelve total and nine sensible, its remaining capacity is three latent. That's one more than the latent load.
Theo|Yes, but the [[total capacity::Twelve kilowatts total equals nine sensible plus three latent here; extra latent capacity does not erase the stated sensible-capacity shortfall.]] doesn't make the two parts interchangeable. The extra latent capacity doesn't establish ten kilowatts of sensible cooling at this condition.
Mina|The worksheet also lists SHR. For A, nine divided by twelve gives zero point seven five. Does that mean seventy-five percent efficiency?
Theo|No. The [[sensible heat ratio::SHR is sensible capacity divided by total capacity, nine divided by twelve or 0.75 for A; it is not output divided by electrical input.]] describes the sensible share of cooling, not electrical efficiency. We haven't been given input power for an efficiency calculation.
Mina|B gives thirteen total and ten point four sensible. Subtracting leaves two point six latent, so both supplied load components are covered numerically.
Theo|Yes, on the stated [[comparison basis::The case gives consistent net capacities at the same conditions; B's 10.4 sensible and 2.6 latent exceed the supplied ten and two loads respectively.]]. B's SHR is ten point four divided by thirteen, or zero point eight.
Mina|A bigger sensible ratio doesn't automatically mean a better unit, then. The right split depends on what the space needs, not the highest SHR.
Theo|Exactly. A room with a different [[load profile::Different combinations of temperature and moisture loads require different comparisons; the highest sensible fraction is not automatically best for every space.]] could need a different balance. We compare the relevant components and conditions, not a ratio as a universal quality score.
Mina|Can the brochure's headline capacity replace these values? It may have been rated at a different outdoor temperature and entering-air condition.
Theo|Not without checking the conditions. Use the performance data for the comparison being made, including airflow and the equipment combination, rather than swapping in a favorable headline.
Mina|The case says net capacity. If another sheet says gross coil capacity, should I use it directly because both are still in kilowatts?
Theo|No. Gross and net values can have different treatment of fan heat. Reconcile the stated basis before comparing them; identical units don't guarantee equivalent boundaries.
Mina|Then B clears this worksheet's sensible and latent checks, but we still haven't selected equipment for the actual building.
Theo|Right. Part-load behavior, controls, conditions, and the rest of the design assessment remain relevant. This arithmetic is not approval to purchase or install a system.
Mina|I'll record A as nine sensible and three latent, with a one-kilowatt sensible shortfall. B is ten point four sensible and two point six latent.
Theo|Include the load split, rating conditions, and net-capacity basis. That explains why a twelve-kilowatt total alone was not enough to settle the comparison.""",
        transfer_title="Check the components, not just the total",
        transfer_setup="Fictional like-for-like net-capacity comparison: load 6 kW sensible and 2 kW latent. Option C: 8 kW total, 6.4 kW sensible. Option D: 9 kW total, 6.3 kW sensible. Use latent = total - sensible and SHR = sensible / total. Compare only these stated figures.",
        transfer="""Manager: C's latent capacity is ___ kW.|1.6|Eight minus 6.4 equals 1.6 kW latent, below the supplied two-kilowatt latent load.
Estimator: C therefore has a latent shortfall of ___ kW.|0.4|Two minus 1.6 equals a 0.4 kW shortfall despite C matching the eight-kilowatt total load.
Manager: Option ___ covers both supplied component loads numerically.|D|D supplies 6.3 sensible and 2.7 latent, above six and two respectively; this is not installation approval.
Estimator: D's sensible heat ratio is ___ .|0.7|6.3 divided by nine equals 0.7; SHR is a capacity split, not electrical efficiency.""",
        reference=("Trane TRACE: total cooling capacity, sensible heat ratio, and rating basis", "https://trace3dplus.help.trane.com/curve_tab_14.html"),
    ),
    scenario(
        title="Circulation is not all outdoor air",
        skill="Explain an air-balance report using consistent volume, time, and outdoor-air quantities.",
        setup="Fictional steady-flow room report: volume 300 cubic meters; total supply 600 cubic meters per hour, comprising 150 outdoor and 450 recirculated. Assume these flows serve this room on the same volume basis. Ignore other air paths for this arithmetic only. Air changes per hour = hourly flow / room volume. No ventilation requirement, filtration effectiveness, or health assurance is supplied.",
        cast="Omar|Office coordinator\nLeah|Ventilation specialist",
        dialogue="""Omar|The report gives six hundred cubic meters an hour for a three-hundred-cubic-meter room. I wrote two complete fresh-air replacements every hour. Is that accurate?
Leah|Not as written. Dividing the [[total supply::Six hundred cubic meters per hour divided by a three-hundred-cubic-meter room gives two total-supply air changes per hour, including recirculated air.]] by room volume gives two air changes per hour, but the supply includes recirculated air.
Omar|Only one hundred fifty of the six hundred comes from outside. I shouldn't call all six hundred fresh outdoor air just because it enters the room.
Leah|Correct. The [[outdoor-air flow::Only 150 cubic meters per hour is outdoor air in this case; the other 450 is recirculated, not an additional outdoor-air contribution.]] is one hundred fifty cubic meters per hour. The other four hundred fifty is recirculated within the stated arrangement.
Omar|Then the outdoor-air calculation is one hundred fifty divided by three hundred, or zero point five. I need to label both results.
Leah|Yes: two total-supply and zero point five outdoor-air [[air changes per hour::ACH divides a consistently expressed hourly airflow by room volume; the total-supply result is two and the outdoor-air result is 0.5.]]. The shared unit doesn't mean the two figures represent the same air source.
Omar|If I want the percentage of supply that is outdoor air, I divide one hundred fifty by six hundred rather than by room volume.
Leah|Exactly. The [[outdoor-air fraction::Outdoor flow divided by total supply is 150/600 = 0.25, or 25 percent; this denominator is flow, not room volume.]] is one quarter, or twenty-five percent. Don't confuse that fraction with zero point five air changes per hour.
Omar|The equipment summary uses liters per second instead. Six hundred cubic meters an hour would be about one hundred sixty-six point seven liters per second?
Leah|Yes. Keep the [[time basis::A cubic meter contains one thousand liters and an hour has 3,600 seconds; 600 cubic meters per hour is about 166.7 liters per second.]] straight: multiply by one thousand, then divide by thirty-six hundred. Outdoor flow is about forty-one point seven liters per second.
Omar|Does two total air changes mean every bit of the original room air has gone after half an hour? The word replacement makes it sound that way.
Leah|No. Actual [[air mixing::An air-change quantity describes delivered volume relative to room volume; it does not guarantee complete replacement of every portion of room air in a fixed interval.]] and distribution matter, and much of this supply is recirculated. One room-volume of delivery doesn't sweep out every original molecule.
Omar|Can the recirculated portion still contribute to particle removal if the system has appropriate filtration? I don't want to say it has no possible benefit.
Leah|It can, but this report gives no filtration-effectiveness evidence for a clean-air calculation. Don't count all recirculation as clean air automatically, or call it outdoor air.
Omar|So we can't combine the two total-supply changes and the half outdoor change and advertise two and a half. The outdoor portion is already inside the total.
Leah|Exactly. That would count the outdoor flow twice. Six hundred already equals one hundred fifty plus four hundred fifty under the case's stated assumptions.
Omar|And none of these calculations says the room meets its actual ventilation requirement or makes the air safe for a particular use.
Leah|Correct. Occupancy, the applicable design requirements, distribution, filtration, and other conditions need assessment. This record alone isn't a compliance or health determination.
Omar|I'll replace fresh-air replacements with two total-supply ACH, including zero point five outdoor-air ACH, and state the twenty-five-percent outdoor fraction.
Leah|Keep the room volume and original flow units alongside those figures. That lets the reader check both the arithmetic and exactly which air quantity each result describes.""",
        transfer_title="Keep the two air-change rates apart",
        transfer_setup="Fictional room volume 240 cubic meters; total supply 720 cubic meters per hour, including 180 outdoor and 540 recirculated. Same volume basis; no other air paths in this calculation. No adequacy or safety judgment is requested.",
        transfer="""Coordinator: Total-supply air changes per hour are ___ .|three|720 divided by 240 equals three total-supply air changes per hour, including the outdoor portion.
Specialist: Outdoor-air changes per hour are ___ .|0.75|180 divided by 240 equals 0.75 outdoor-air changes per hour, not three.
Coordinator: Outdoor air forms ___ percent of the supply.|25|180 divided by 720 times one hundred equals twenty-five percent.
Specialist: Outdoor flow is ___ liters per second.|50|180 cubic meters per hour times one thousand divided by 3,600 equals fifty liters per second.""",
        reference=("CDC/NIOSH: airflow, air changes, filtration, and mixing limitations", "https://www.cdc.gov/niosh/ventilation/faq/index.html"),
    ),
    scenario(
        title="Use the right saturation reference",
        skill="Explain superheat and subcooling in a completed report without using the wrong blend reference.",
        setup="Fictional completed report for a refrigerant blend: at the vapor-reading pressure, bubble point 0 C, dew point 5 C, vapor temperature 12 C; at the liquid-reading pressure, bubble point 40 C, dew point 45 C, liquid temperature 35 C. Each reference matches its reading's pressure. Superheat = vapor minus dew; subcooling = bubble minus liquid. No targets, diagnosis, or servicing instructions are supplied.",
        cast="Sara|Service coordinator\nDev|Refrigeration technician",
        dialogue="""Sara|Dev, the completed report gives two saturation temperatures for each pressure. I used zero for the vapor calculation and got twelve degrees of superheat.
Dev|For this blend's vapor reading, use the [[dew point::The supplied vapor-side dew point is 5 C; superheat is referenced to saturated vapor at the matching pressure, not the zero-degree bubble point.]] of five degrees Celsius. Zero is the bubble point at that pressure, not the correct reference for this superheat calculation.
Sara|Then twelve minus five gives seven. I need to correct the derived result, but preserve twelve as the original vapor temperature.
Dev|Yes. The [[superheat::Twelve degrees Celsius vapor temperature minus the five-degree dew point gives a seven-kelvin temperature difference; the original temperature reading remains twelve Celsius.]] is seven kelvin, a temperature difference. We aren't changing the measured temperature or saying the vapor is at seven degrees Celsius.
Sara|The liquid-side entry gives forty bubble and forty-five dew, with liquid at thirty-five. Which reference belongs with that calculation?
Dev|Use the [[bubble point::The supplied liquid-side bubble point is 40 C; it is the saturated-liquid reference for subcooling at that reading's pressure.]] of forty degrees Celsius. The liquid calculation is referenced to saturated liquid at its corresponding pressure, not to the dew value.
Sara|Forty minus thirty-five is five. Using forty-five would give ten and overstate the result by another five.
Dev|Correct. The [[subcooling::Forty degrees Celsius bubble point minus thirty-five degrees Celsius liquid temperature gives five kelvin subcooling; using dew would incorrectly give ten.]] here is five kelvin. Don't swap the reference merely because the larger subtraction looks like a more substantial result.
Sara|Why aren't the bubble and dew points identical? I expected one saturation temperature, as though the whole change of state happened at a single value.
Dev|The blend has [[temperature glide::A blend with temperature glide has distinct bubble and dew temperatures at a given pressure; the supplied reference pairs differ by five kelvin.]]. Its bubble and dew temperatures differ at a given pressure. Keep the two reference labels instead of silently averaging them.
Sara|Both pairs in this example differ by five. Can I use the vapor-side dew point with the liquid temperature just because both numbers appear in one report?
Dev|No. Each comparison needs the [[matching pressure::The vapor and liquid readings have different pressure-specific reference pairs; a reference from the other location cannot be substituted into the calculation.]] reference for that reading and location. The report already supplies those pairings; crossing between them would invalidate the result.
Sara|Is seven kelvin a different-sized interval from seven Celsius degrees? I can see how the report's units might confuse someone reading quickly.
Dev|Those intervals are the same size. Kelvin is useful for stating a temperature difference here; it doesn't turn the seven-kelvin difference into an absolute temperature of seven kelvin.
Sara|Do seven and five tell us the system has the correct charge or that an expansion device needs adjustment? The summary asks for the service outcome.
Dev|Not from these figures alone. No applicable targets or full assessment are supplied. Correct arithmetic doesn't establish system condition, refrigerant quantity, or a remedy.
Sara|Then the handoff should distinguish corrected calculations from completed servicing. Nobody has been asked to obtain new readings or change a setting in this exercise.
Dev|Exactly. We're reviewing a completed record. Actual testing, refrigerant work, and adjustments require the relevant qualified procedures and authorization, not a language-book calculation.
Sara|I'll report vapor twelve Celsius against dew five: superheat seven kelvin. Liquid thirty-five against bubble forty: subcooling five kelvin, with the original location references retained.
Dev|That's clear. Keep the underlying readings, pressure-specific references, and unresolved assessment status visible so the corrected summary doesn't become an unsupported all-clear.""",
        transfer_title="Recalculate without changing the readings",
        transfer_setup="Completed fictional blend record: vapor temperature 11 C with matching dew 4 C and bubble -1 C; liquid temperature 31 C with matching bubble 37 C and dew 42 C. Use the correct reference for each calculation. No operating target or diagnosis is supplied.",
        transfer="""Coordinator: The vapor calculation uses the ___ point.|dew|Superheat uses the saturated-vapor dew reference at the corresponding pressure, not the bubble value.
Technician: The superheat is ___ kelvin.|seven|Eleven minus four equals seven kelvin; using minus one would incorrectly give twelve.
Coordinator: The liquid calculation uses the ___ point.|bubble|Subcooling uses the saturated-liquid bubble reference at the matching pressure, not the dew value.
Technician: The subcooling is ___ kelvin.|six|Thirty-seven minus thirty-one equals six kelvin; forty-two minus thirty-one would use the wrong reference.""",
        reference=("Parker Sporlan: dew and bubble references for refrigerant blends", "https://www.parker.com/content/dam/Parker-com/Literature/Sporlan/Sporlan-Literature-Document-Files/Sporlan-Document-Files-Educational/Form-5-490-TP-Chart_AC_Chiller_2sided.pdf"),
    ),
]
