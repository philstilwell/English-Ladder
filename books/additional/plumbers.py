"""Original plumbing pressure, water-heater rating, and drainage-level conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Pressure is not flow",
        skill="Explain a completed water-supply report without confusing pressure, flow, and diagnosis.",
        setup="Fictional completed report at point S1: no-flow pressure 4.0 bar; pressure during flow 2.6 bar; collected volume 6 liters in 30 seconds during that flow observation. For this report, static means no-flow pressure; flowing pressure means pressure while water is flowing. Use 1 bar = 100 kPa. No cause, minimum performance requirement, or remedial work is established.",
        cast="Rina|Customer\nAdam|Plumbing coordinator",
        dialogue="""Rina|The report says four bar, which sounds strong. Why does the next line say two point six? Did the technician write down two different answers?
Adam|They describe different conditions. Four bar is the [[static pressure::The supplied static reading is the pressure with no flow at S1; it is not the pressure recorded during the flow observation.]], with no water flowing at that point. Two point six was recorded during flow.
Rina|So neither number replaces the other. The report also says six liters in thirty seconds. Is that another way of stating the pressure?
Adam|No. Volume over time gives the [[flow rate::Flow rate describes volume per unit time; six liters over thirty seconds is a different quantity from pressure in bar.]]. Pressure and flow are related in a system, but they aren't interchangeable measurements or units.
Rina|I nearly copied six into the liters-per-minute column. Thirty seconds is only half a minute, so the rate needs a conversion.
Adam|Right. Six liters in half a minute gives twelve [[liters per minute::Six divided by half a minute equals twelve liters per minute; copying the six-liter volume would halve the reported rate.]]. It doesn't mean twelve liters were collected during those thirty seconds.
Rina|And if the form wants liters per second, six divided by thirty is zero point two. The units change, not the recorded delivery.
Adam|Exactly. Keep the [[flowing pressure::The 2.6-bar value belongs to the same stated flow observation; retaining that condition prevents substitution of the four-bar no-flow reading.]] beside that observation: two point six bar at the reported flow, not four bar under those conditions.
Rina|The other report uses kilopascals. I need comparable units before I send both to the reviewer. Four bar would be four hundred?
Adam|Yes, four hundred [[kilopascals::At one hundred kilopascals per bar, four bar equals four hundred kPa and 2.6 bar equals 260 kPa.]]. The flowing reading is two hundred sixty kilopascals, using one hundred kilopascals for each bar.
Rina|The difference is one point four bar, or one hundred forty kilopascals. Does that prove a blockage somewhere between the supply and the outlet?
Adam|No. It records a difference between [[operating conditions::The observations differ in flow condition; the numerical pressure difference alone does not identify a blockage, leak, pump fault, or required remedy.]], not a diagnosis. These figures alone don't establish a blockage, leak, pump fault, or required remedy.
Rina|I was going to ask for a larger pump because the second pressure is lower. That would be jumping ahead of the assessment, then.
Adam|Yes. A pressure comparison doesn't select equipment. The system, intended use, relevant requirements, and causes need assessment before any recommendation is made.
Rina|The appliance leaflet asks for pressure during flow. Can I enter the higher static number because it gives us a more favorable comparison?
Adam|No. Compare the quantity and conditions the actual requirement specifies. Using a no-flow value for a flowing requirement would misrepresent the available evidence.
Rina|Could twelve liters per minute here tell us what every outlet would deliver with several taps running? The report only names S1.
Adam|It couldn't establish that. The point and conditions matter. Don't extend this single record into a whole-building performance claim.
Rina|I'll retain S1, four bar static, two point six bar during the stated flow, and twelve liters per minute, equivalent to zero point two liters per second.
Adam|That preserves the record. We're interpreting completed observations, not directing a new test, changing equipment, or promising that the supply meets an unspecified requirement.""",
        transfer_title="Convert a second completed record",
        transfer_setup="Completed fictional record at S2: 9 liters collected in 45 seconds; static pressure 3.2 bar and flowing pressure 2.1 bar. Use 1 bar = 100 kPa. Complete the arithmetic without diagnosing a fault.",
        transfer="""Customer: The reported flow rate is ___ liters per minute.|12|Nine liters in three-quarters of a minute equals twelve liters per minute.
Coordinator: The same flow is ___ liters per second.|0.2|Nine divided by forty-five equals 0.2 liters per second.
Customer: The static pressure is ___ kilopascals.|320|3.2 bar multiplied by one hundred equals 320 kPa.
Coordinator: The difference between the pressure readings is ___ kilopascals.|110|3.2 minus 2.1 equals 1.1 bar, or 110 kPa; this difference does not diagnose a cause.""",
        reference=("Salamander Pumps: Aquascan pressure and flow terminology", "https://www.salamanderpumps.co.uk/wp-content/uploads/2024/07/Aquascan-User-Guide.pdf"),
    ),
    scenario(
        title="Tank size and first-hour delivery",
        skill="Compare water-heater ratings while keeping storage, rated delivery, and installation approval separate.",
        setup="Fictional storage-heater comparison under the same rating conditions: A has a 40-US-gallon tank and first-hour rating of 68 US gallons; B has a 50-US-gallon tank and first-hour rating of 62 US gallons. The supplied peak-hour hot-water target is 66 US gallons, not a mixed-water volume. Ratings begin with a fully heated tank. Suitability, installation, and running costs are not assessed.",
        cast="Nora|Customer\nEli|Plumbing estimator",
        dialogue="""Nora|I chose the fifty-gallon option because the tank is larger. That should make B the stronger choice for our sixty-six-gallon peak hour, shouldn't it?
Eli|Not on tank size alone. The forty and fifty are [[storage volumes::The forty- and fifty-gallon figures describe tank storage, not the separate amounts delivered during the rated first hour.]]. The first-hour delivery figures are sixty-eight for A and sixty-two for B.
Nora|How can a forty-gallon tank have a sixty-eight-gallon delivery figure? I thought the specification couldn't offer more water than the tank holds.
Eli|The [[first-hour rating::First-hour rating describes rated hot-water delivery during an hour beginning with a fully heated tank, including delivery supported by reheating during that hour.]] covers an hour beginning with the tank fully heated. Reheating during that period contributes to the amount supplied.
Nora|Then sixty-eight doesn't mean the tank secretly holds sixty-eight gallons. Nor should I add forty to sixty-eight and call the result one hundred eight.
Eli|Correct. Adding the tank volume would [[double-count::The first-hour figure already reflects delivery from the initially heated tank and reheating; adding its stored volume again overstates the rated amount.]] part of that delivery. The stated first-hour figure is the quantity to compare with this target.
Nora|A is two gallons above sixty-six, while B is four below it. The smaller tank has the higher rating in the supplied comparison.
Eli|Yes. Against this [[peak-hour target::The fictional target is sixty-six US gallons of hot water in the peak hour; A exceeds it by two and B falls short by four.]], A clears the arithmetic comparison and B doesn't. That conclusion depends on the supplied, like-for-like rating basis.
Nora|Does A then deliver sixty-eight gallons every hour indefinitely? I'd like to describe it that way when I send the options to the owner.
Eli|No. First-hour delivery is not a [[continuous delivery rate::A first-hour rating includes an initially heated tank; it does not promise that the same volume can be supplied in every later hour indefinitely.]]. It starts with stored hot water already available, so it isn't an unlimited repeated-hour promise.
Nora|The owner gave us sixty-six gallons of hot-water demand, not total shower water after cold water is mixed in. That distinction needs to stay on the sheet.
Eli|Yes. Keep the [[comparison basis::The case supplies hot-water demand and comparable rating conditions; substituting mixed-water demand or different units would change the comparison.]] consistent: US gallons, hot-water volume, and the stated rating conditions. Don't silently substitute mixed-water use.
Nora|Could I call A approved on that basis? I can see how the numbers work, but we haven't reviewed the actual installation.
Eli|Call it the option meeting this supplied numerical target. Available space, services, manufacturer requirements, applicable rules, and technical suitability still need review.
Nora|And a higher first-hour rating doesn't necessarily mean it costs less to run. That would require a different comparison.
Eli|Exactly. Efficiency, energy source, operating conditions, and tariff matter to cost. The two delivery figures don't establish an annual bill or a saving.
Nora|What if someone suggests changing the temperature setting to make a chosen model meet the target? That isn't part of this estimate, is it?
Eli|No. This is a rating comparison, not a setting adjustment or operating instruction. We use the actual supported specifications and the appropriate technical assessment.
Nora|I'll write A: forty-gallon tank, sixty-eight first-hour gallons, two above target. B: fifty-gallon tank, sixty-two first-hour gallons, four below.
Eli|Add that neither option is approved for installation by this worksheet. That keeps the useful comparison without turning a rating into a promise of performance in every condition.""",
        transfer_title="Compare two more specifications",
        transfer_setup="Fictional comparable ratings: C has a 40-US-gallon tank and 58-gallon first-hour rating; D has a 50-US-gallon tank and 72-gallon first-hour rating. The supplied peak-hour hot-water target is 70 US gallons. No installation assessment has been completed.",
        transfer="""Customer: Option ___ meets this numerical target.|D|D's first-hour rating is seventy-two, above seventy; C's fifty-eight is below the target.
Estimator: That option's tank volume is ___ US gallons.|50|D stores fifty gallons; seventy-two is its first-hour delivery rating, not tank volume.
Customer: Its first-hour rating exceeds the target by ___ gallons.|two|Seventy-two minus seventy equals two gallons on the supplied rating basis.
Estimator: Installation remains ___ .|unapproved|Meeting this numerical target does not complete a technical assessment or authorize installation.""",
        reference=("ENERGY STAR: first-hour rating and water-heater product criteria", "https://www.energystar.gov/products/water_heaters/residential_water_heaters_key_product_criteria"),
    ),
    scenario(
        title="A fall is not a rising level",
        skill="Read back a drainage drawing with the correct direction, units, and elevation reference.",
        setup="Fictional desk review only: a drainage drawing specifies a 12 m horizontal run falling 1 in 80 downstream, from upstream invert level 50.300 m on a common datum. Fall = horizontal run / 80; percent gradient = 100 / 80. A copied downstream label says 50.450 m. No pipe diameter, ground level, installation permission, or compliance decision is supplied.",
        cast="Tariq|Plumber\nLena|Drawing coordinator",
        dialogue="""Tariq|Lena, the copied downstream label is fifty point four five zero meters. That is higher than the upstream level, although the drawing says the drain falls.
Lena|Let's compare it with the stated [[horizontal run::The twelve-meter dimension is the horizontal run used in the supplied fall calculation; it is not a vertical drop or an unspecified sloping length.]] of twelve meters. The one-in-eighty notation means one unit of fall for eighty horizontal units.
Tariq|So I divide twelve meters by eighty and get zero point one five meters. That would be one hundred fifty millimeters, not eighty millimeters.
Lena|Yes. The [[gradient::A one-in-eighty fall is one divided by eighty, or 1.25 percent; it is neither eighty percent nor an angle of 1.25 degrees.]] is also one point two five percent. It isn't eighty percent, and the percentage isn't an angle in degrees.
Tariq|The downstream level should be lower. Starting at fifty point three zero zero, I subtract zero point one five rather than add it.
Lena|That [[fall::The required fall is 0.150 m; subtracting it from upstream invert 50.300 m gives downstream invert 50.150 m.]] gives fifty point one five zero meters. The copied fifty point four five zero label goes in the opposite direction.
Tariq|Before I change the query, I need the right word for what those elevations describe. They're not the ground surface or the top of the pipe.
Lena|They're the [[invert level::Invert level is the elevation of the inside bottom of the pipe, distinct from the ground, pipe crown, centerline, or outside bottom.]], meaning the inside bottom of the pipe at each endpoint. Keep that reference attached to both numbers.
Tariq|If one level came from a different site reference, subtraction might look tidy and still give us a misleading result.
Lena|Correct. The case supplies a common [[datum::A common datum is the shared elevation reference needed to compare the two levels; unrelated references cannot be subtracted without reconciliation.]]. Actual records must use reconciled references. Don't combine elevations merely because both happen to be written in meters.
Tariq|Then the copied label represents a one-hundred-fifty-millimeter increase downstream. It is not just a different way of displaying the same fall.
Lena|Right, it's a [[rise::50.450 m is 0.150 m above 50.300 m, so that copied label rises downstream rather than showing the specified fall.]]. Our query should show the supplied run and gradient, the calculated lower endpoint, and the conflicting copied label.
Tariq|At eight meters along a uniform one-in-eighty fall, the drop would be one hundred millimeters and the invert fifty point two zero zero.
Lena|Yes, within this stated uniform-gradient example. The remaining four meters contribute another fifty millimeters, giving the same total of one hundred fifty.
Tariq|Does the calculated endpoint also tell us how much ground cover there is over the pipe? The drawing extract doesn't show a ground level.
Lena|No. We lack the required ground and pipe geometry. Invert is the inside bottom, so it isn't itself a depth-of-cover figure.
Tariq|And confirming this arithmetic doesn't tell us whether one in eighty is suitable for the actual drain, its diameter, or the applicable requirements.
Lena|Exactly. The gradient was supplied for interpretation, not selected or approved here. Hydraulic design, coordination, and compliance remain separate checks.
Tariq|I'll flag the copied fifty point four five zero label and state that the supplied calculation gives fifty point one five zero on the common datum.
Lena|Send it as a drawing query for review, not an instruction to lay or alter pipework. Include meters and the downstream direction so the correction is unambiguous.""",
        transfer_title="Read another supplied fall",
        transfer_setup="Desk calculation: a 9 m horizontal run falls 1 in 60 downstream from invert 12.800 m. Use fall = 9/60 m and percent gradient = 100/60, rounded to two decimals. Both endpoints share a datum. This does not approve a design or instruct installation.",
        transfer="""Plumber: The fall over the run is ___ millimeters.|150|Nine divided by sixty equals 0.150 m, or 150 mm.
Coordinator: The downstream invert is ___ meters.|12.650|Subtract the 0.150 m fall from upstream invert 12.800 m; adding would produce a rise.
Plumber: The gradient is ___ percent to two decimal places.|1.67|One divided by sixty times one hundred equals 1.6667 percent, rounded to 1.67 percent.
Coordinator: Invert identifies the pipe's ___ .|inside bottom|Invert concerns the inside bottom elevation, not the ground surface, crown, or outside bottom.""",
        reference=("Autodesk: pipe invert, crown, cover, and slope terminology", "https://help.autodesk.com/cloudhelp/2022/ENU/Civil3D-UserGuide/files/GUID-89EBD4E9-E3D4-4A9D-968C-5F274AD86CBA.htm"),
    ),
]
