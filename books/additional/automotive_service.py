"""Original tire-marking, EV charging, and alignment-report conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Read the whole tire description",
        skill="Explain a tire quotation without confusing dimensions, rating codes, and vehicle suitability.",
        setup="Fictional quotation lists 205/55 R16 91V. Read 205 as nominal section width in millimeters, 55 as sidewall-height percentage of that width, R as radial construction, and 16 as rim diameter in inches. The service description is 91V: load index plus speed rating. Vehicle fitment and pressure requirements have not been checked. This is a document discussion, not fitting or inflation guidance.",
        cast="Alina|Customer\nMarco|Parts advisor",
        dialogue="""Alina|Marco, the quote says two-oh-five, fifty-five, R sixteen, ninety-one V. I understand it's a tire size, but which numbers should I keep when comparing another quote?
Marco|Keep the whole description. Two hundred five is the [[nominal section width::The 205 marking is nominal section width in millimeters; it is not the tread depth, circumference, or rim diameter.]] in millimeters. It isn't the depth of the tread or the diameter of the wheel.
Alina|Then fifty-five must be the sidewall height in millimeters? That's what I wrote beside it, but perhaps I've mixed a ratio with a dimension.
Marco|It's the [[aspect ratio::The 55 marking expresses sidewall height as fifty-five percent of nominal section width, not as a fifty-five-millimeter height.]]: fifty-five percent of the width. On that nominal basis, zero point five five times two hundred five is one hundred twelve point seven five millimeters.
Alina|That arithmetic explains the proportion, but it doesn't mean somebody measured this particular tire at exactly that height. What does the R add?
Marco|It denotes [[radial construction::R identifies radial construction in this size designation; it does not mean radius or rear position on the vehicle.]], not radius or rear position. We shouldn't drop the letter and treat the remaining numbers as a complete description.
Alina|And sixteen is in inches, even though the width was in millimeters. Is sixteen the diameter across the whole outside of the tire?
Marco|No, it's the [[rim diameter::Sixteen denotes the compatible rim diameter in inches, not the outside diameter of the tire; the size code mixes dimension types and units.]]. That's a different dimension from the tire's overall outside diameter. The units and the thing being measured both matter.
Alina|Now the ninety-one. Does that mean each tire is rated to carry ninety-one kilograms, or is it a code that needs a table?
Marco|It's a [[load index::Ninety-one is an index for a load-capacity rating, not a literal ninety-one-kilogram load; the applicable rating information and vehicle requirements must be checked.]], not a weight stated directly in kilograms. Its rating must be checked against the applicable information and the vehicle's requirements.
Alina|So I shouldn't compare only the first three numbers and ignore ninety-one V. The final letter is another rating, not just a product series?
Marco|Yes, V is the [[speed rating::V is the speed-rating symbol in the service description; it is not a recommended driving speed or proof that this tire is approved for the vehicle.]] symbol. It's not a recommendation to drive at that speed or proof that this tire is suitable for your vehicle.
Alina|The other quote lists a different service description with the same size. Can I call them identical just because two-oh-five, fifty-five, and sixteen match?
Marco|Not identical on that evidence. We need the complete specification and the vehicle requirements before confirming an appropriate replacement. A matching size alone doesn't settle every requirement.
Alina|I also see a maximum-pressure marking in a sidewall photograph. Is that the number the vehicle normally wants, regardless of its own label?
Marco|No. A tire's maximum marking isn't the vehicle's recommended operating pressure. The vehicle's actual placard and manufacturer information are separate references, not optional details.
Alina|Please don't turn this question into an order yet. I want the comparison clarified before anyone assumes the quoted tire has been approved for fitting.
Marco|Understood. We'll keep the quotation and fitment check distinct. This conversation explains the code; it doesn't confirm installation suitability, tire condition, or vehicle readiness.
Alina|I'll retain the full 205/55 R16 91V entry, with millimeter width, percentage aspect ratio, radial construction, inch rim size, and the two rating codes.
Marco|That's a useful readback. Send the competing full description with the vehicle reference, so the review compares actual specifications rather than a shortened version that loses important information.""",
        transfer_title="Decode a second quotation",
        transfer_setup="A fictional quote reads 225/45 R17 94W. Interpret the dimensional fields using the same definitions. No vehicle-fitment review has been completed; the different code is not a recommendation to substitute tires.",
        transfer="""Customer: The nominal section width is ___ millimeters.|225|The first number gives nominal section width, not wheel diameter or tread depth.
Advisor: The aspect ratio is ___ percent.|45|Forty-five is the sidewall-height percentage of nominal section width, not a millimeter dimension.
Customer: The rim diameter is ___ inches.|17|The number after R states rim diameter in inches; R itself denotes radial construction.
Advisor: Fitment remains ___ .|unapproved|Reading the code does not establish that this specification meets the actual vehicle requirements.""",
        reference=("Michelin: tire size, construction, load index, speed rating, and pressure markings", "https://www.michelinman.com/auto/auto-tips-and-advice/tires-101/tire-markings-explained"),
    ),
    scenario(
        title="Charge added is not wall energy",
        skill="Explain an electric-vehicle charging estimate with separate battery energy, input limits, losses, and cost.",
        setup="Fictional electric vehicle: usable battery 60 kWh, charge from 20 to 80 percent. For this simplified estimate, percentages map linearly to usable energy. Compatible AC point offers 7.4 kW; vehicle accepts at most 7.2 kW AC. Assume constant 7.2 kW wall input and 90 percent wall-to-stored-energy efficiency, including all losses. Energy-only tariff $0.25/kWh; no other charges. Actual charging time is not guaranteed.",
        cast="Ben|Vehicle owner\nNadia|Service advisor",
        dialogue="""Ben|The battery is sixty kilowatt-hours and I'm charging from twenty to eighty percent. I divided sixty by the point's seven point four kilowatts for the time.
Nadia|Start with the change in [[state of charge::The requested increase is eighty minus twenty, or sixty percentage points, rather than a full empty-to-full charge of the sixty-kilowatt-hour usable battery.]]. You're adding sixty percentage points, not charging the whole usable battery from empty.
Ben|Sixty percent of sixty is thirty-six kilowatt-hours. That is the increase stored in the battery under this worksheet's simplified percentage assumption.
Nadia|Right. Use the supplied [[usable capacity::The case gives sixty kilowatt-hours of usable capacity and a linear percentage assumption; multiplying by 0.60 gives thirty-six kilowatt-hours stored.]], not an unrelated gross-capacity figure from another model. The energy increase is thirty-six, not sixty or eighty kilowatt-hours.
Ben|The point can offer seven point four kilowatts, but the car accepts only seven point two on AC. Which one belongs in the time calculation?
Nadia|The vehicle's [[AC input limit::The compatible point offers 7.4 kW but this vehicle accepts at most 7.2 kW AC; the fictional constant-input calculation therefore uses 7.2 kW.]] is the lower figure here. Under our assumptions, we use seven point two kilowatts, not the point's higher advertised capability.
Ben|If thirty-six is stored, is thirty-six also what the meter bills? The worksheet says ninety percent reaches stored battery energy after all losses.
Nadia|No. The [[wall energy::Thirty-six kilowatt-hours stored divided by 0.90 efficiency requires forty kilowatt-hours from the wall in the supplied model.]] is thirty-six divided by zero point nine: forty kilowatt-hours. The four-kilowatt-hour difference represents the losses already included in this model.
Ben|Then adding another ten percent to forty would count the same loss assumption twice. And thirty-six times one point one wouldn't quite give the right input either.
Nadia|Exactly. The [[charging efficiency::Ninety percent means stored energy equals 0.90 times wall energy; solve by division, and do not apply a second loss allowance.]] is stored energy divided by wall energy. Divide to find input; don't add a second allowance after the forty-kilowatt-hour result.
Ben|Forty divided by seven point two is about five point five six hours. That's roughly five hours thirty-three minutes, not five hours fifty-six.
Nadia|Correct. The decimal fraction is part of an hour. The [[energy charge::Forty billed kilowatt-hours at $0.25 each gives a ten-dollar energy-only charge, excluding any other fees by the case's stated terms.]] is forty times twenty-five cents, or ten dollars, under the supplied energy-only tariff.
Ben|Would an eleven-kilowatt AC point make this car charge proportionately faster? Its label would be higher, but the car's AC limit hasn't changed.
Nadia|Not in this case. The same vehicle input limit still applies. A higher point rating doesn't make the vehicle accept more than its supported AC rate.
Ben|And I shouldn't reuse this seven-point-two figure to describe DC fast charging as though it were the same charging path and limit.
Nadia|Right. DC charging has separate vehicle capability and charging behavior. This estimate is specifically for the compatible AC arrangement and assumptions supplied here.
Ben|Could I promise the car will be ready after exactly five hours thirty-three minutes? The real charge rate might not remain constant.
Nadia|Don't promise that. Battery condition, temperature, charging controls, and other constraints can change actual time. The constant-power worksheet is an estimate, not a completion booking.
Ben|I'll report thirty-six stored kilowatt-hours, forty from the wall, about five point five six hours at seven point two, and ten dollars energy cost.
Nadia|Keep the twenty-to-eighty range and ninety-percent assumption beside it. That explains the estimate without confusing power with energy, counting losses twice, or claiming a guaranteed charging result.""",
        transfer_title="Use a different efficiency assumption",
        transfer_setup="Fictional usable capacity 40 kWh; charge 25 to 75 percent on a linear usable-energy basis. Assume constant wall input 5 kW and 80 percent wall-to-stored efficiency including all losses. Energy-only rate $0.24/kWh. No other fees or operating restrictions are modeled.",
        transfer="""Owner: The increase in stored battery energy is ___ kWh.|20|The fifty-percentage-point increase is half of forty usable kilowatt-hours, giving twenty stored.
Advisor: Required wall energy in the model is ___ kWh.|25|Twenty divided by 0.80 equals twenty-five kilowatt-hours, including the supplied loss assumption.
Owner: Modeled charging time is ___ hours.|five|Twenty-five wall kilowatt-hours divided by constant five-kilowatt wall input gives five hours.
Advisor: The energy-only charge is ___ dollars.|six|Twenty-five kilowatt-hours multiplied by $0.24 equals six dollars, not the cost of stored energy alone.""",
        reference=("US Department of Energy AFDC: charging capacity, power, and timing factors", "https://afdc.energy.gov/fuels/electricity-stations"),
    ),
    scenario(
        title="Minutes of angle are not decimals",
        skill="Read an alignment printout without confusing per-wheel values, total toe, units, and completion status.",
        setup="Fictional BEFORE report: front left toe +0 degrees 06 minutes; right +0 degrees 12 minutes. Legend: positive means toe-in; total toe is their sum. Use 60 angular minutes = 1 degree. Supplied total-toe range is +0.10 to +0.20 decimal degrees, inclusive. Left camber is -0 degrees 30 minutes. AFTER values are blank. These invented limits are for record interpretation, not vehicle adjustment.",
        cast="Rosa|Service advisor\nArun|Alignment technician",
        dialogue="""Rosa|Arun, the printout says left toe zero degrees six minutes and right zero degrees twelve minutes. I copied them as zero point zero six and zero point one two.
Arun|Those are [[angular minutes::The marks represent sixtieths of a degree, not hundredths; six angular minutes equals 0.10 decimal degree and twelve equals 0.20.]], not decimal hundredths. Divide the minutes by sixty: six becomes zero point one zero degrees, and twelve becomes zero point two zero.
Rosa|Then the sum is zero point three zero degrees. My copied decimals would have produced zero point one eight, which would change the comparison.
Arun|Yes. Convert to [[decimal degrees::Correct conversion gives 0.10 plus 0.20 = 0.30 decimal degrees; adding incorrectly copied hundredths would give a false 0.18 result.]] consistently before using the printed decimal range. Or add six and twelve minutes, then divide the eighteen by sixty.
Rosa|The limits are plus zero point one zero through plus zero point two zero. Should I compare each wheel separately against that range?
Arun|No, it is the supplied [[total toe::The stated range applies to the sum across the front axle, not to each wheel independently; total toe is positive 0.30 degree here.]] range. Each wheel and the axle total are different entries. Comparing the wrong entry could give a misleading pass statement.
Rosa|Our total is plus zero point three zero, which exceeds the upper end by zero point one zero. I shouldn't call it within range.
Arun|Correct. Preserve that result and the [[sign convention::The fictional report explicitly defines positive as toe-in; the plus signs must remain attached instead of being dropped or interpreted from another report's convention.]]. This report defines positive as toe-in. Don't drop the signs or substitute the convention from another document.
Rosa|The camber entry is minus zero degrees thirty minutes. That is minus zero point five zero degrees, not minus zero point three zero.
Arun|Exactly. Keep [[camber::Camber is a separate alignment angle; the negative thirty-minute entry converts to -0.50 degree and must not be added to the toe figures.]] separate from toe. Its negative half-degree value doesn't get added into the front total-toe calculation.
Rosa|The sheet title says alignment report, so I nearly told the customer the alignment was completed. But these figures sit in the BEFORE column.
Arun|The [[before readings::The values are initial readings and the AFTER column is blank; a report title does not establish adjustment, final results, or completed verification.]] document the initial state. With the AFTER column blank, this extract doesn't establish an adjustment or a completed result.
Rosa|So the useful explanation is that the supplied initial total is outside this fictional range, with no final result recorded. We don't need to guess what was done.
Arun|Right. Ask for the actual completed assessment and work record. Don't fill the empty column by assuming the technician adjusted the value to the middle of the range.
Rosa|Another report uses millimeters for toe. Can I simply rename zero point three degrees as zero point three millimeters to match it?
Arun|No. An angular and a linear value aren't interchangeable. A distance-based toe figure depends on the defined reference diameter and reporting convention.
Rosa|Does explaining this printout establish that wheel balancing was done too? Customers sometimes use balance and alignment as though they mean the same service.
Arun|They are different matters. This alignment extract doesn't document balancing, and interpreting these angles doesn't diagnose every vibration, tire concern, or steering complaint.
Rosa|I'll retain the original minute values, show total plus zero point three zero degrees, note the supplied range, and leave the missing AFTER result explicit.
Arun|Good. That's a records explanation, not a setting instruction or a vehicle-safety release. The actual vehicle specification, assessment, work authorization, and final verification remain separate.""",
        transfer_title="Convert another initial report",
        transfer_setup="Fictional BEFORE values: left toe +0 degrees 09 minutes and right +0 degrees 03 minutes. Positive means toe-in; total is the sum. Use 60 minutes per degree and two decimal places. The AFTER column is blank.",
        transfer="""Advisor: Left toe is +___ decimal degrees.|0.15|Nine divided by sixty equals 0.15 degree; writing 0.09 would confuse minutes with hundredths.
Technician: Right toe is +___ decimal degrees.|0.05|Three divided by sixty equals 0.05 degree, preserving the supplied positive sign.
Advisor: Total toe is +___ decimal degrees.|0.20|0.15 plus 0.05 equals 0.20 degree, equivalent to twelve angular minutes.
Technician: The final result is ___ in this extract.|unrecorded|The AFTER column is blank; converting the initial values does not establish a completed adjustment or final verification.""",
        reference=("Hunter Engineering: alignment measurement units, formats, and total toe", "https://www.hunter.com/globalassets/hunter/products/alignment-systems/winalign-standard/documents/align-winalign-ops-3850-t.pdf"),
    ),
]
