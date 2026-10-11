"""Original material-takeoff, plant-schedule, and irrigation-audit conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Area is not the order volume",
        skill="Read back area, specified depth, purchasing allowance, and whole-bag rounding as separate quantities.",
        setup="Fictional estimator's worksheet: two non-overlapping rectangles, 12 m by 2 m and 4 m by 3 m, include 4 square meters of marked exclusions. The approved new layer is 50 mm. For purchasing only, add 10% to net volume and round up to whole 50-liter bags. This is supplied estimating arithmetic, not a general mulch-depth recommendation.",
        cast="Dev|Grounds worker\nAva|Estimator",
        dialogue="""Dev|Ava, the worksheet says thirty-six square meters. I was about to use that as the number of bags, but the units don't look right.
Ava|Start with the [[gross area::The two non-overlapping rectangles have areas twenty-four and twelve square meters, totaling thirty-six before exclusions.]]: twelve times two is twenty-four; four times three is twelve. Together they give thirty-six square meters before the exclusions.
Dev|The marked exclusions total four square meters and are inside those rectangles. So I subtract four once, leaving thirty-two to cover.
Ava|That's the [[net area::Thirty-six square meters minus four square meters of exclusions leaves thirty-two square meters requiring the new layer.]]. Keep the exclusions in the takeoff; don't buy or apply material as though every part of the rectangles needs coverage.
Dev|The new layer is specified as fifty millimeters. I need meters for multiplying by square meters, so that's zero point zero five meters.
Ava|Then the net [[volume::Thirty-two square meters multiplied by 0.05 meters gives 1.6 cubic meters, equivalent to 1,600 liters.]] is thirty-two times zero point zero five: one point six cubic meters, or sixteen hundred liters.
Dev|At fifty liters per bag, the net material is thirty-two bags. But the purchasing instruction also asks for ten percent extra.
Ava|Apply the [[allowance::Ten percent of the 1,600-liter net volume is 160 liters; the purchasing target becomes 1,760 liters.]] to the net volume, not to the depth specification. Sixteen hundred plus one hundred sixty gives seventeen hundred sixty liters.
Dev|Dividing that by fifty gives thirty-five point two bags. We can't order point two of one of these bags.
Ava|So [[round up::The 35.2-bag purchasing target requires thirty-six whole bags; rounding down to thirty-five would provide only 1,750 liters.]] to thirty-six whole bags. Thirty-five would give seventeen hundred fifty liters, ten liters below the purchasing target.
Dev|Thirty-six bags gives eighteen hundred liters. That's forty liters beyond the allowance-adjusted target, because of the bag increment.
Ava|Correct. That is [[rounding surplus::The whole-bag order supplies 1,800 liters, forty above the 1,760-liter purchasing target; it is separate from the allowance itself.]], not another planned layer. Keep net requirement, allowance, and bag rounding separate in the estimate.
Dev|Could someone read thirty-six bags as an instruction to spread all thirty-six across the thirty-two square meters?
Ava|They shouldn't. Extra purchasing quantity doesn't change the approved fifty-millimeter new layer or remove the marked exclusions. Don't thicken the layer to consume leftovers.
Dev|And fifty millimeters is the specification for this fictional worksheet. It isn't a rule for every plant, site, or existing mulch condition.
Ava|Exactly. Actual depth and placement require the relevant design and site assessment. We're practicing how to explain the supplied calculation, not choosing horticultural requirements.
Dev|My estimate should therefore list thirty-two square meters net, one point six cubic meters net material, and one point seven six with allowance.
Ava|Then thirty-six fifty-liter bags as the rounded purchasing quantity. Show the bag volume so nobody substitutes a smaller bag at the same count.
Dev|I'll preserve the two rectangle dimensions and four-square-meter exclusions with it. That makes the total traceable if the drawing changes.
Ava|Good. This is a quantity calculation for review, not confirmation that material is ordered, delivered, or applied. Those statuses need their own records.""",
        transfer_title="A different bag size",
        transfer_setup="A fictional worksheet gives a net area of 18 square meters and a specified new layer of 40 mm. Add a purchasing allowance of 5% to net volume, then round up to whole 40-liter bags. Do not change the layer depth.",
        transfer="""Worker: The net volume is ___ liters.|720|Eighteen square meters times 0.04 meters equals 0.72 cubic meters, or 720 liters.
Estimator: Including five percent, the purchasing target is ___ liters.|756|Five percent of 720 is 36; adding it gives a target of 756 liters.
Worker: The rounded order quantity is ___ bags.|nineteen|756 divided by 40 is 18.9, which rounds upward to nineteen whole bags.
Estimator: Whole bags provide ___ liters beyond that purchasing target.|four|Nineteen forty-liter bags supply 760 liters; subtracting 756 leaves four liters of rounding surplus.""",
        reference=("Iowa State University Extension: area, depth, volume, and bag calculations", "https://yardandgarden.extension.iastate.edu/how-to/how-determine-amount-mulch-needed-garden-bed"),
    ),
    scenario(
        title="Read the whole plant name",
        skill="Check a plant schedule against delivered labels while keeping species, cultivar, quantity, and container volume distinct.",
        setup="Fictional planting schedule L3 calls for 12 Lavandula angustifolia 'Hidcote', in containers labeled 2 L. Delivery labels show 8 'Hidcote' in 2 L containers and 4 'Munstead' in 2 L containers, all Lavandula angustifolia. No substitution is approved. Health, identity verification beyond labels, and planting suitability remain for the qualified lead.",
        cast="Tomas|Grounds worker\nImani|Landscape lead",
        dialogue="""Tomas|Imani, the delivery has twelve English lavenders, so the count looks right. But four labels don't have the same name as schedule L3.
Imani|Read the [[botanical name::The botanical name Lavandula angustifolia identifies the species here; the schedule also specifies a particular cultivar within it.]] in full, including the cultivar. L3 calls for Lavandula angustifolia Hidcote, twelve plants in containers labeled two liters.
Tomas|Eight labels say Hidcote. Four say Munstead. They all say Lavandula angustifolia, so the species wording matches.
Imani|But the [[cultivar::Hidcote and Munstead are different named cultivars; matching species and common name do not make the delivered selection identical.]] doesn't match on those four. Hidcote and Munstead aren't interchangeable names just because both are English lavender.
Tomas|Then I'd report twelve plants physically delivered, with eight matching the specified cultivar label and four labeled differently. Not simply twelve correct.
Imani|Yes. That's a [[specification discrepancy::Four delivered plants carry Munstead labels rather than the specified Hidcote, even though the overall plant count is twelve.]], not a total-count shortage. We are four short of the specified cultivar on the label evidence.
Tomas|All the containers are marked two liters. Does that tell us the plants are the specified height as well?
Imani|No. That's [[container volume::The 2 L marking describes the stated container volume, not plant height, mature spread, or a guarantee of overall quality.]], not a height measurement. It doesn't tell us mature spread or establish that every plant meets every requirement.
Tomas|So two liters isn't two meters, and a two-liter container doesn't mean the plant will stay that size as it grows.
Imani|Correct. Keep count, plant identity, and size information in their own fields. A matching [[container label::The container-size marking matches the supplied 2 L requirement but does not resolve the different cultivar labels.]] does not cancel the cultivar discrepancy.
Tomas|Could the four Munstead be accepted as substitutes if someone says the flower color looks close enough?
Imani|A [[substitution::Using Munstead in place of Hidcote would be a change to the specified selection and requires the actual approval process.]] needs the actual review and approval. Similar appearance isn't permission to change the planting schedule.
Tomas|I'll leave the original L3 specification visible. I shouldn't edit Hidcote out of it so that the delivery appears to match.
Imani|Exactly. Preserve what was requested and what the labels show. That gives the supplier a clear discrepancy to address.
Tomas|Should I call the eight Hidcote plants fully accepted, since their labels and two-liter containers match the schedule?
Imani|Not yet. The case only establishes label matches. Plant health, actual identity checks, and the other acceptance requirements still need the qualified review.
Tomas|I'll keep the labels with the delivery record, not rewrite them or plant the four differently labeled ones to keep the job moving.
Imani|Good. The review needs both cultivar names, quantities, container information, and schedule reference L3. Don't shorten it to lavender problem.
Tomas|Read-back: twelve delivered; eight Hidcote, four Munstead, all labeled Lavandula angustifolia in two-liter containers; twelve Hidcote requested; no substitute approved.
Imani|That's precise. We can resolve the specification question from that record without confusing a correct total with a fully matching delivery.""",
        transfer_title="Separate variety and container size",
        transfer_setup="A fictional schedule requires 10 Lavandula angustifolia 'Munstead' in containers labeled 3 L. Delivery labels show 6 'Munstead' in 3 L, 2 'Munstead' in 2 L, and 2 'Hidcote' in 3 L. No alternatives are approved; other quality checks remain.",
        transfer="""Worker: ___ plants match both the specified cultivar and container label.|six|Only the six Munstead plants in three-liter containers match both supplied requirements.
Lead: Two Munstead plants have a ___ discrepancy.|container size|Those two have the requested cultivar but two-liter rather than three-liter containers.
Worker: Two three-liter plants have a ___ discrepancy.|cultivar|The Hidcote plants have the stated container size but not the specified Munstead cultivar.
Lead: The total delivered count is ___ .|ten|Six plus two plus two equals ten delivered plants, despite only six matching both label requirements.""",
        reference=("Royal Horticultural Society: the Hidcote cultivar of English lavender", "https://www.rhs.org.uk/plants/96353/lavandula-angustifolia-hidcote/details"),
    ),
    scenario(
        title="An average can hide dry spots",
        skill="Explain measured application rate and lower-quarter distribution uniformity without confusing either with a watering prescription.",
        setup="Fictional completed irrigation audit: 16 equally representative catch positions measured during the same 20-minute test; four readings each of 10, 12, 14, and 16 mm. Use mean depth divided by minutes times 60 for mm/hour. Lower-quarter uniformity equals the lowest-quarter mean divided by the overall mean. No watering schedule or fault diagnosis is supplied.",
        cast="Leila|Grounds worker\nMarco|Irrigation lead",
        dialogue="""Leila|Marco, the audit sheet has sixteen readings. Four are ten millimeters, four twelve, four fourteen, and four sixteen. They all came from the same twenty-minute test.
Marco|Then the [[mean depth::Four readings at each of 10, 12, 14, and 16 mm total 208 mm; dividing by sixteen gives a mean of 13 mm.]] is thirteen millimeters. Each group has the same number of readings, so averaging those four group values also gives thirteen.
Leila|That's what accumulated during twenty minutes. To express the application rate per hour, I multiply thirteen by three.
Marco|Correct. The measured average [[precipitation rate::Thirteen millimeters in twenty minutes corresponds to thirty-nine millimeters per hour under the measured test conditions.]] is thirty-nine millimeters per hour under those test conditions. It doesn't mean thirty-nine millimeters fell during the test.
Leila|And thirteen is only the mean. The lowest positions collected ten and the highest sixteen, so the coverage wasn't the same everywhere.
Marco|That's why we also examine [[distribution uniformity::Distribution uniformity describes how evenly water is applied; an average rate alone can hide differences among positions.]]. An acceptable-looking average can't tell you whether the whole area received similar amounts.
Leila|For the lower quarter, I take four of the sixteen readings. The lowest four are all ten millimeters.
Marco|Their [[lower-quarter mean::One quarter of sixteen is four; the four lowest readings are all ten, giving a lower-quarter mean of ten millimeters.]] is ten millimeters. Divide ten by the overall mean of thirteen, not by the highest reading of sixteen.
Leila|Ten divided by thirteen is about zero point seven six nine. Expressed as a percentage, that's about seventy-seven percent.
Marco|Yes, to the nearest whole percent. Keep the unrounded [[ratio::The ratio is 10 divided by 13, approximately 0.769; multiplying by one hundred converts it to about 77 percent.]] in the calculation and round the reported percentage at the end.
Leila|Does that mean seventy-seven percent of the water reached the roots and twenty-three percent was wasted?
Marco|No. That's not an [[application efficiency::This uniformity ratio compares catch depths; it does not measure the fraction of supplied water stored usefully in the root zone.]] result. These catch readings don't tell us how much water the soil stored in the root zone.
Leila|Could I tell the customer to run the system longer so the dry positions catch up? The numbers don't tell me the plants' needs.
Marco|Don't prescribe a schedule from this alone. Soil, plant needs, weather, restrictions, and the actual system assessment matter. More run time doesn't itself correct uneven distribution.
Leila|And the spread of readings doesn't prove which nozzle or component is faulty. We have measurements, not the cause.
Marco|Right. Preserve the position identifiers and test conditions for review. A repair decision needs the relevant inspection rather than a guessed component failure.
Leila|The note should say thirteen millimeters mean depth in twenty minutes, equivalent average rate thirty-nine per hour, lower-quarter uniformity about seventy-seven percent.
Marco|That's accurate, with the units stated. Keep the sixteen readings available so the mean doesn't hide the low and high positions.
Leila|I'll report those findings as the completed measurement review, not say every part received thirteen millimeters or that a new schedule is approved.
Marco|Exactly. The measurements describe this test. They don't certify the entire installation, diagnose a fault, or authorize a controller change.""",
        transfer_title="Compare a second set of readings",
        transfer_setup="A fictional 30-minute test has 16 equally representative positions: four readings each of 6, 8, 10, and 12 mm. Use the same mean-rate and lower-quarter formulas. Round the final uniformity percentage to one decimal place.",
        transfer="""Worker: Mean collected depth is ___ millimeters.|nine|The equally sized groups average (6 + 8 + 10 + 12) divided by four, or nine millimeters.
Lead: The average application rate is ___ millimeters per hour.|eighteen|Nine millimeters in thirty minutes is eighteen millimeters per hour, not eighteen collected during the test.
Worker: The lowest-quarter mean is ___ millimeters.|six|The lowest four of sixteen readings are all six millimeters, so their mean is six.
Lead: Lower-quarter uniformity is ___ percent.|66.7|Six divided by nine times one hundred is 66.666... percent, rounded to 66.7, not a root-zone efficiency measurement.""",
        reference=("University of Florida IFAS: lower-quarter irrigation uniformity", "https://ask.ifas.ufl.edu/publication/AE194"),
    ),
]
