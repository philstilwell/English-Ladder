"""Original cut-list, veneer-layout, and moisture-report conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Allow for the missing material",
        skill="Distinguish finished lengths from cut-width allowance in a supplied material estimate.",
        setup="Fictional desk estimate only: stock has 3,000 mm usable length after end preparation. The list requires three finished pieces of 995 mm. The worksheet specifies three cuts, each with 3 mm kerf, and no other allowances. The calculation is not a cutting sequence, tool instruction, or permission to change finished dimensions.",
        cast="Luca|Workshop coordinator\nSana|Estimator",
        dialogue="""Luca|Sana, three pieces at nine hundred ninety-five millimeters total twenty-nine eighty-five. I've written fifteen millimeters spare from the three-meter usable stock.
Sana|That leaves out the [[kerf::Kerf is the width of material removed by a cut; the supplied worksheet allows three millimeters for each of three cuts.]]. The worksheet includes three cuts at three millimeters each, so finished pieces aren't the only claim on the usable length.
Luca|Right, the cuts consume nine millimeters altogether. I should add those nine to the twenty-nine eighty-five, not subtract them from each finished piece.
Sana|Exactly. The [[finished length::Each required finished piece remains 995 millimeters; adding a material allowance does not authorize shortening that dimension.]] remains nine ninety-five per piece. Accounting for material removed doesn't change what the customer is supposed to receive.
Luca|That gives twenty-nine ninety-four required, including the three cuts. Compared with three thousand usable, there's six millimeters remaining.
Sana|Six is the [[residual::The supplied requirements total 2,994 millimeters, leaving six from 3,000; fifteen would ignore nine millimeters consumed by the cuts.]], not fifteen. Keep the cut count and assumed width beside the estimate so someone reviewing it can reproduce the total.
Luca|The three thousand is already after end preparation. Do I deduct another end-preparation amount just to be on the safe side?
Sana|Not in this stated worksheet. The [[usable length::The 3,000-millimeter figure is explicitly after end preparation; applying an additional invented end allowance would change the supplied estimate.]] already reflects that preparation. An actual plan may need other allowances, but we don't invent them or count the same allowance twice.
Luca|What if the requested pieces change to nine hundred ninety-eight? Three of those total twenty-nine ninety-four before the cuts.
Sana|Add the same nine and you need three thousand three. That's a [[shortfall::Three times 998 plus three times 3 equals 3,003 millimeters, three more than the stated 3,000 available.]] of three millimeters, even though the finished-piece total alone appears to fit.
Luca|Then silently shaving a millimeter off each finished piece would make the arithmetic fit by changing the requirement. That isn't my decision.
Sana|Correct. Refer the [[cut list::The cut list specifies quantities and finished dimensions; an unresolved material shortage calls for review, not an unauthorized size change.]] for review. Don't change the requested lengths, the cut count, or the tool assumption just to force a positive remainder.
Luca|Is three millimeters the blade plate thickness? The supplier's sheet has separate figures, and I don't want to carry over the wrong one.
Sana|Kerf and plate thickness are different specifications. Use the relevant verified cut-width information in an actual estimate, not a universal three-millimeter assumption.
Luca|And this page doesn't tell the workshop how to perform the cuts. It gives a count for arithmetic, not an operating sequence.
Sana|Yes. Qualified staff still need the actual equipment requirements, safety controls, and production review. This calculation cannot authorize tool use.
Luca|I'll show the original requirement as three times nine ninety-five plus three times three: twenty-nine ninety-four, leaving six.
Sana|Then show the proposed nine ninety-eight version separately as three thousand three required. Keeping both versions visible makes the change understandable.
Luca|No physical production or order change follows from my worksheet. I'm sending the quantity comparison for review.
Sana|Good. Label the assumptions and preserve the finished dimensions. A clear material estimate explains the constraint without quietly redesigning the parts.""",
        transfer_title="The finished lengths almost fit",
        transfer_setup="A fictional desk worksheet gives 2,400 mm usable stock after end preparation, two finished pieces of 1,198 mm, and two cuts at 3 mm each. No other allowances apply to this exercise.",
        transfer="""Coordinator: The two finished lengths total ___ millimeters.|2396|Two times 1,198 equals 2,396 millimeters before allowing for the cuts.
Estimator: The two cuts consume ___ millimeters.|six|Two cuts at three millimeters each consume six millimeters in the stated worksheet.
Coordinator: The total material requirement is ___ millimeters.|2402|Adding the six-millimeter allowance to 2,396 gives 2,402, not 2,400.
Estimator: That is ___ millimeters more than the usable stock.|two|The 2,402-millimeter requirement exceeds 2,400 by two; the finished dimensions cannot be silently shortened.""",
        reference=("DEWALT: distinction between kerf and blade plate thickness", "https://support.dewalt.com/hc/en-us/articles/26537650571405-DWE7485-Type-3-Blades-DWA181424-DWA181440"),
    ),
    scenario(
        title="Matching is not the panel order",
        skill="Describe veneer-leaf matching and panel placement without confusing the two.",
        setup="Fictional approved mockup M uses book-matched veneer; unapproved alternative N uses slip matching. Viewed from the finished front, the elevation specifies P11 left, P12 center, P13 right. The recorded layout from that same viewpoint is P13, P12, P11. No substitute finish or physical alteration is authorized.",
        cast="Anika|Designer\nJoel|Joinery coordinator",
        dialogue="""Anika|Joel, the layout photograph looks different from mockup M. Can we separate the veneer pattern from the order of the three panels before discussing a correction?
Joel|Yes. M uses [[book matching::Book matching alternates consecutive veneer leaves by turning them over, producing paired mirror-like grain patterns rather than simple repeats.]]: alternating leaves turn over to form paired, mirror-like patterns. That's the approved appearance reference in this case.
Anika|The supplier also showed N, where the grain repeats alongside itself. Someone called that another version of the same matching, but it looks different.
Joel|N uses [[slip matching::Slip matching places successive leaves alongside one another in the same face orientation to repeat the grain pattern; N is not the approved mockup.]]. Successive leaves sit alongside each other in the same face orientation. We shouldn't record it as approval of M or as an interchangeable name.
Anika|Now the elevation says P11 left, P12 center, P13 right. The photograph labels read P13, P12, P11. Are we definitely looking from the same side?
Joel|The record confirms the [[viewing direction::Both the required elevation order and photographed order are specified from the finished front, removing a front-versus-back reversal explanation.]] is the finished front in both. This isn't a back-view photograph making an otherwise correct order look reversed.
Anika|Then P12 is in the listed center position, but the two outer panel identifiers are reversed. That's a different issue from leaf matching within a panel.
Joel|Exactly. The [[panel sequence::The specified sequence is P11-P12-P13 from the finished front; the recorded P13-P12-P11 layout reverses the outer panels.]] doesn't match the elevation. A correct matching method inside each panel wouldn't by itself put those panels in the required order.
Anika|Should we turn the outer panels around? I'm wary of giving a quick instruction from a photograph without checking faces, arrows, and the workshop record.
Joel|We need their [[orientation::Orientation includes which face and direction a panel is intended to present; the label-order discrepancy alone does not authorize turning or altering panels.]] checked against those records. A panel label discrepancy doesn't tell us that physically turning a panel is the appropriate remedy.
Anika|Please keep M attached to the query. If the message only says oak veneer, someone could answer about the species and miss the pattern requirement.
Joel|I'll identify the [[approved mockup::Mockup M is the stated approved reference; N is an unapproved slip-matched alternative, not an equally authorized selection.]] as M and the elevation order separately. Species, leaf matching, panel identity, and position are distinct parts of the review.
Anika|So we aren't rejecting every panel or claiming the veneer is defective. We have a pattern reference and a documented placement discrepancy to resolve.
Joel|Correct. The case doesn't establish a manufacturing defect, the actual grain on every face, or the necessary corrective work. Those need the relevant review.
Anika|Could the same wood species show different grain even with the requested method? I don't want a promise that every panel will be visually identical.
Joel|It can. The matching description organizes the appearance; it doesn't promise identical natural grain or cancel the requirement to compare the agreed sample.
Anika|I'll ask the workshop to reconcile the panel labels, front-view order, and M reference. No permission to substitute N is implied by that question.
Joel|And no instruction to refinish, re-veneer, or rotate installed work. The review must determine the actual action rather than infer it from our wording.
Anika|Read-back: book-matched M is approved; slip-matched N isn't. P12 is centered as listed, while P11 and P13 appear in opposite outer positions.
Joel|That's the distinction we need. I'll preserve the photograph viewpoint and original identifiers so the response addresses both the appearance reference and the sequence.""",
        transfer_title="Check the center and right labels",
        transfer_setup="A fictional front elevation requires P21 left, P22 center, P23 right. The recorded finished-front order is P21, P23, P22. Mockup Q calls for paired mirror-like grain from alternately turned consecutive leaves, not same-face repeats.",
        transfer="""Designer: The required center panel is ___ .|P22|The elevation puts P22 in the center even though the recorded layout places it on the right.
Coordinator: The required right panel is ___ .|P23|P23 belongs on the right; its presence in the center is a sequence discrepancy.
Designer: Q specifies ___ .|book matching|Alternately turning consecutive leaves creates the paired mirror-like pattern described in Q.
Coordinator: Same-face grain repeats describe ___ instead.|slip matching|Slip matching repeats successive leaves alongside each other without the alternating face turnover described for Q.""",
        reference=("Timber Veneer Association of Australia: veneer assembling methods", "https://timberveneer.asn.au/methods-of-assembling/"),
    ),
    scenario(
        title="A percentage needs its basis",
        skill="Explain wood moisture on a dry-mass basis and keep sample screening distinct from installation approval.",
        setup="Fictional completed laboratory results: sample A originally 132 g, oven-dry 120 g; B originally 90 g, oven-dry 80 g. Moisture content = (original minus dry mass) / dry mass x 100. This project's screening range is 8-12% inclusive for each sample. No laboratory procedure or installation approval is provided.",
        cast="Noor|Joinery coordinator\nMarcus|Quality lead",
        dialogue="""Noor|Marcus, A lost twelve grams and B lost ten. I nearly described B as the drier sample, but their original sizes are different.
Marcus|Compare [[moisture content::Wood moisture content here is water mass divided by oven-dry wood mass, expressed as a percentage, not the absolute grams of water alone.]], not just the grams lost. For A, subtract one hundred twenty from one hundred thirty-two, then divide the twelve by one hundred twenty.
Noor|That gives zero point one, or ten percent. The denominator is the dry mass, not the original one hundred thirty-two grams.
Marcus|Yes, the [[dry-mass basis::The supplied formula uses the 120-gram oven-dry mass for A; dividing by the original mass would answer a different question.]] matters. A percentage without its basis could make a correct-looking report refer to the wrong calculation.
Noor|For B, ninety minus eighty is ten grams. Ten divided by eighty is zero point one two five, so twelve point five percent.
Marcus|Correct. B has a higher [[percentage::B is 12.5 percent and A is 10 percent on the same dry-mass basis, despite B containing fewer absolute grams of water.]] even though it contains fewer grams of water. The samples have different dry masses, so the absolute losses aren't directly comparable as percentages.
Noor|Our project sheet says eight to twelve percent inclusive for each sample. A is inside that interval, but B is half a percentage point above the upper limit.
Marcus|That's the [[screening result::A meets the fictional 8-12 percent sample interval; B at 12.5 percent does not, without establishing a cause or overall installation fitness.]]. Keep each sample's result visible. The interval belongs to this exercise's project specification, not every wood product.
Noor|Their simple average is eleven point two five. Could someone use that number to say the samples pass together?
Marcus|Not under this [[individual limit::The stated requirement applies to each sample, so averaging 10 and 12.5 to 11.25 cannot erase B's individual result above twelve.]]. Averaging can hide B's failure to meet the stated range; it doesn't change the requirement from each sample to the mean.
Noor|The site email also says relative humidity. A at ten percent doesn't mean the room air was ten percent relative humidity, does it?
Marcus|No. [[Relative humidity::Relative humidity describes the surrounding air, whereas wood moisture content describes water relative to dry wood mass; their percentages are not interchangeable.]] is an air condition. Wood moisture is a different quantity, and neither of these two sample percentages supplies the room's air reading.
Noor|What about equilibrium moisture content? Does leaving boards in a room for two days establish that they've reached it?
Marcus|No fixed two-day rule is supplied. Equilibrium concerns balance with the surrounding conditions, including temperature and humidity, not simply elapsed time.
Noor|Then the note shouldn't say the whole delivery is acclimated and ready because one sample meets the range. We have only the supplied sample results.
Marcus|Exactly. The actual sampling plan, material requirements, site conditions, and qualified review still matter. Passing this arithmetic check isn't permission to install.
Noor|And B's result doesn't identify why it is higher or prove that the material has decay. It tells us how it compares with this stated interval.
Marcus|Correct. Report the values and refer the discrepancy; don't invent a cause, a drying method, or a structural conclusion from these two numbers.
Noor|I'll record A: ten percent, within range; B: twelve point five, above range; both calculated using oven-dry mass. Overall release remains unconfirmed.
Marcus|Good. Keep the original and dry masses with the results. That makes the calculation traceable while leaving the actual material decision to the appropriate review.""",
        transfer_title="Different masses, same basis",
        transfer_setup="Completed fictional results: C originally 165 g, oven-dry 150 g; D originally 113 g, oven-dry 100 g. Use (original minus dry) / dry x 100. Each sample must meet this project's 8-12% inclusive screening interval; overall release is not supplied.",
        transfer="""Coordinator: C contains ___ grams of water in the reported calculation.|15|The original 165 grams minus 150 grams oven-dry gives fifteen grams of water.
Lead: C has ___ percent moisture on the dry-mass basis.|10|Fifteen divided by the 150-gram dry mass, multiplied by one hundred, is ten percent.
Coordinator: D has ___ percent moisture on the same basis.|13|The thirteen-gram difference divided by one hundred dry grams gives thirteen percent.
Lead: D is ___ the stated screening interval.|above|Thirteen exceeds the fictional upper limit of twelve; C's passing result cannot make D meet it.""",
        reference=("US Department of Energy, PNNL: wood moisture content and dry-weight basis", "https://basc.pnnl.gov/redcalc/tool/wood-moisture-content"),
    ),
]
