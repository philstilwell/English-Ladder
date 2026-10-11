"""Additional original environmental consulting conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="One soil result, two mass bases",
        skill="Reconcile wet- and dry-weight reporting without confusing a conversion with a new test.",
        setup="Fictional soil sample S14: 10 mg/kg wet weight, 80% solids by mass. For this arithmetic exercise, dry-basis concentration equals wet-basis concentration divided by the solids fraction. The comparison table uses dry weight. No cleanup criterion or risk conclusion is supplied.",
        cast="Priya|Project consultant\nLeon|Laboratory liaison",
        dialogue="""Priya|The laboratory sheet says ten milligrams per kilogram, but our draft table says twelve point five. Have we transcribed the wrong result?
Leon|Check the [[mass basis::Mass basis identifies whether the denominator is wet sample mass or dry solids mass; identical mg/kg labels alone do not establish comparability.]] first. The laboratory's ten is per kilogram of wet sample. The draft uses kilograms of dry solids.
Priya|Both columns say milligrams per kilogram. Without wet or dry in the heading, they look like contradictory measurements of the same sample.
Leon|Exactly. The supplied [[percent solids::Percent solids is the dry-solids mass divided by wet sample mass, expressed as a percentage; eighty percent becomes 0.80 in this calculation.]] is eighty. Convert that to zero point eight before dividing the wet-basis result.
Priya|Ten divided by zero point eight is twelve point five milligrams per kilogram dry weight. We are changing the denominator, not adding contaminant.
Leon|That is the [[dry-weight concentration::The dry-weight concentration is 10 divided by 0.80, or 12.5 mg/kg; a smaller mass denominator gives a higher concentration without adding analyte.]] under the supplied conversion. Retain both the source value and the calculation so another reviewer can reconcile them.
Priya|Would multiplying by zero point eight give eight? That was the number in an earlier spreadsheet version.
Leon|It would, but that reverses this conversion. Your denominator is getting smaller, so the concentration should increase, not decrease.
Priya|The same sheet also says twenty percent moisture. Could someone mistakenly divide by zero point two instead?
Leon|Yes. [[Moisture content::Moisture content here is the twenty-percent water fraction; it is not the eighty-percent solids fraction required by the supplied conversion.]] is the water fraction here, not the solids fraction used in this calculation. Label both clearly.
Priya|I will replace the generic unit heading with milligrams per kilogram dry weight and identify the source wet-weight result in a note.
Leon|Also identify S14 and the laboratory report version. A correct formula applied to another sample's solids percentage would still give the wrong result.
Priya|For the next batch, can I apply eighty percent to every sample so the table is consistent?
Leon|No. Use the [[sample-specific value::The solids percentage belongs to the individual sample; borrowing S14's percentage for other samples would impose an unsupported conversion.]] supplied for each sample. Consistent presentation does not justify assigning identical moisture conditions to different material.
Priya|What if the laboratory already reports the next result on a dry-weight basis? The spreadsheet currently converts every row automatically.
Leon|Then that row must not be converted again. Add a basis check before the calculation rather than assuming every incoming value is wet weight.
Priya|We should distinguish a converted concentration from a fresh analysis. Nothing in this arithmetic says the material changed between tests.
Leon|Correct. Keep an [[audit trail::An audit trail retains the original result, solids fraction, basis label, calculation, and reviewed output so the conversion can be checked.]] of the original value, basis, solids fraction, and calculated output. Do not overwrite the laboratory report.
Priya|I will send the corrected table for review. The heading and calculation note should explain why ten and twelve point five can both be consistent.
Leon|Good. Reconciliation is the result of this exercise. It does not establish a cleanup classification, sampling adequacy, or a conclusion about exposure.""",
        transfer_title="Check the basis before converting",
        transfer_setup="Sample T2 has 6 mg/kg wet weight and 60% solids. Use dry concentration = wet concentration / solids fraction. Sample T3 is already reported as 9 mg/kg dry weight. No other correction applies.",
        transfer="""Consultant: T2's solids fraction in decimal form is ___.|0.60|Sixty percent equals 0.60; the forty-percent moisture fraction is not the denominator here.
Reviewer: T2 converts to ___ mg/kg dry weight.|10|Six divided by 0.60 equals ten on the stated dry-weight basis.
Consultant: T3 remains at ___ mg/kg dry weight.|9|T3 is already reported on the required basis and needs no second conversion.
Reviewer: The table must retain the reporting ___ beside mg/kg.|basis|The wet or dry basis specifies the mass denominator that the bare unit mg/kg does not distinguish.""",
        reference=("EPA: percent-solids reporting basis", "https://semspub.epa.gov/work/HQ/177924.pdf"),
    ),
    scenario(
        title="A higher limit is not a higher result",
        skill="Discuss non-detects and qualified estimates without treating reporting thresholds as measurements.",
        setup="Fictional groundwater results for X, in micrograms per litre: January <0.5, April <5.0 after dilution, July 0.3 J. This laboratory defines J as an estimated detected concentration below its routine reporting limit. No trend analysis, health threshold, or cleanup criterion is supplied.",
        cast="Nadia|Data reviewer\nOwen|Project manager",
        dialogue="""Owen|The chart climbs from zero point five in January to five in April. The client is asking why X increased tenfold.
Nadia|Those entries start with a [[less-than sign::The less-than sign identifies the reported upper threshold for a non-detect in this case; the number following it is not a measured concentration.]]. We have plotted the reporting thresholds as if they were measured concentrations.
Owen|So the April number is not a detected concentration of five. I need to remove the line implying a measured rise.
Nadia|Yes. The April [[reporting limit::The reporting limit is the stated threshold associated with this result, not a detected value; five cannot be treated as the April concentration.]] is higher, but that alone does not show that the environmental concentration rose.
Owen|The laboratory says it diluted the April sample. Does that explain why the reported threshold changed?
Nadia|The [[dilution::The laboratory's stated dilution raised the sample-specific reporting threshold; this explanation does not convert the non-detect into a measured value.]] explains the higher threshold in this supplied record. Ask for the sample-specific reporting details if they are missing from the export.
Owen|Would replacing both entries with zero solve the misleading graph? That would at least avoid inventing an increase.
Nadia|It would invent two exact zeros instead. Keep the limits and non-detect status; choose any statistical treatment through the project's documented review process.
Owen|There is a third entry: zero point three J in July. Our import routine has turned every letter-qualified result into a blank cell.
Nadia|Here J marks an [[estimated detection::The supplied laboratory legend defines 0.3 J as an estimated detected concentration, which differs from a non-detect or a missing result.]], not a missing result. Restore the value with its qualification and the laboratory's definition.
Owen|I have seen J used in other reports. Should I assume the explanation is identical across every laboratory and data-validation package?
Nadia|No. Read the applicable legend and validation notes. Preserve both the reported information and any later review qualification with their provenance.
Owen|Then our data table needs more than a single numeric field. We need the number, sign, unit, and qualification to travel together.
Nadia|Exactly. These January and April entries are [[censored results::Censored results provide a threshold rather than an exact concentration; preserving that status prevents inappropriate plotting and summary calculations.]]. A numeric-only export strips away information essential to their interpretation.
Owen|Can I still say July was cleaner than January because zero point three is smaller than zero point five?
Nadia|Not from this comparison alone. January did not supply an exact value, and the qualified July estimate needs its own review context.
Owen|The chart should show the two non-detect thresholds distinctly and the estimated July detection with its qualifier, not connect three exact values.
Nadia|Agreed. Keep [[micrograms per litre::Micrograms per litre is the shared concentration unit in this case; preserving it prevents a thousandfold error when exchanging values with mg/L tables.]] in the heading. Another table uses milligrams per litre, so the import also needs a unit check.
Owen|I will correct the three records and explain that the tenfold change is in the reporting threshold, not a demonstrated environmental increase.
Nadia|That answers the client's immediate question. We can then ask the project reviewer what comparisons these data support, without claiming a trend or a safety finding.""",
        transfer_title="Keep a result and its limit separate",
        transfer_setup="For analyte Y, one result is <2 micrograms per litre. Another is 0.7 J; the supplied legend defines J as an estimated detected concentration. An exchange table requires mg/L, and 1,000 micrograms equals 1 milligram. No trend is established.",
        transfer="""Reviewer: The <2 entry does not establish a concentration of exactly ___.|zero|A non-detect below a threshold does not prove the substance is present at exactly zero concentration.
Manager: The 0.7 J entry is an estimated ___.|detection|The supplied legend explicitly classifies this as detected but estimated, not missing or non-detected.
Reviewer: Converted to mg/L, 0.7 micrograms per litre is ___.|0.0007|Divide by one thousand to convert micrograms per litre to milligrams per litre.
Manager: The converted value must retain its ___ J.|qualifier|Changing units does not remove the original estimated-status qualification or the need to interpret it.""",
        reference=("EPA: censored data and analytical qualifications", "https://www.epa.gov/n-steps-online/data-considerations"),
    ),
    scenario(
        title="Depth is not water-level elevation",
        skill="Reconcile groundwater levels using measuring points and a common vertical reference.",
        setup="Fictional simultaneous readings: well A measuring-point elevation 104.60 m, depth to water 4.20 m; well B 100.80 m and 1.80 m. Both elevations use the same local datum. Depth is measured downward from each stated point. Screen intervals and aquifer connections have not been assessed.",
        cast="Evan|Field-data coordinator\nLina|Hydrogeologist",
        dialogue="""Evan|The summary says B has the higher groundwater level because its depth to water is only one point eight metres. Is that comparison valid?
Lina|Not on its own. [[Depth to water::Depth to water is a downward distance from a stated measuring point; different point elevations prevent direct ranking of absolute water-level elevations from depths alone.]] starts at each well's measuring point. Those points are at different elevations.
Evan|A's point is at one hundred four point six metres, and B's is at one hundred point eight. Both use our common local reference.
Lina|That shared [[vertical datum::The vertical datum is the common reference for the supplied elevations; mixing unrelated datums would invalidate their direct comparison.]] lets us compare elevations. For each well, subtract its downward depth from its own measuring-point elevation.
Evan|For A, one hundred four point six minus four point two gives one hundred point four metres. I will retain two decimal places in the table.
Lina|Correct. B is one hundred point eight minus one point eight, or ninety-nine point zero metres. The smaller depth did not make its water level higher.
Evan|Then the [[water-level elevation::Water-level elevation is 100.40 m for A and 99.00 m for B after subtracting each depth from the corresponding measuring-point elevation.]] at A is one point four metres higher, despite A having the larger depth reading.
Lina|Yes. Keep the depth and elevation columns separate. A heading that simply says water level would leave readers unsure which quantity they are comparing.
Evan|The survey sheet gives both top-of-casing and ground elevations. Which one belongs in this subtraction?
Lina|Use the actual [[measuring point::The measuring point must match the point from which the depth was recorded; substituting ground elevation for a casing reference introduces an offset error.]] named in the field record. Do not substitute ground elevation for a casing reference without the appropriate documented offset.
Evan|These are simultaneous readings. That helps avoid comparing measurements taken before and after a changing condition, but it does not settle every interpretation.
Lina|Right. Preserve the timestamps anyway. The calculation reconciles the supplied levels; the hydrogeological interpretation needs more than two numbers.
Evan|The draft map draws a flow arrow from A to B. Can I keep it because A's elevation is higher?
Lina|Not on this information alone. We have not assessed the [[screen intervals::Screen intervals identify the depths or zones open to each well; without assessing them and hydraulic connection, the two levels cannot establish a site-wide flow direction.]] or established that the wells represent the same connected unit.
Evan|And two wells do not establish a complete site-wide flow field. I will mark the arrow as unsupported instead of reversing it mechanically.
Lina|Good. We need the relevant hydrogeological evidence and spatial coverage before interpreting flow direction. A subtraction is not a substitute for that assessment.
Evan|The field team also mentioned a replacement casing cap. Could that matter even if the well identifier stayed the same?
Lina|A changed reference point can create a [[datum offset::A changed reference point can introduce an elevation offset; the identifier alone does not establish that old and new measuring-point references are interchangeable.]]. Check the survey and reference records instead of assuming the old elevation still applies.
Evan|I will correct the table to A one hundred point four and B ninety-nine metres, label the common datum, and retain the source depths.
Lina|Then send the unsupported flow arrow for technical review. The corrected levels are useful evidence, with a clear calculation and a separate interpretation question.""",
        transfer_title="Subtract from the matching reference",
        transfer_setup="On a common datum, C's measuring point is 88.40 m and its downward depth is 3.10 m; D's point is 86.00 m and depth is 1.20 m. These are simultaneous readings. Hydraulic connections are not established.",
        transfer="""Coordinator: C's water-level elevation is ___ m.|85.30|Subtracting C's depth of 3.10 from its measuring-point elevation of 88.40 gives 85.30 metres.
Reviewer: D's water-level elevation is ___ m.|84.80|Subtracting D's depth of 1.20 from its own elevation of 86.00 gives 84.80 metres.
Coordinator: C's elevation exceeds D's by ___ m.|0.50|The elevation difference is 85.30 minus 84.80, or half a metre, on the common datum.
Reviewer: These figures alone do not establish groundwater flow ___.|direction|The supplied elevations do not establish hydraulic connection or provide a complete hydrogeological interpretation of flow direction.""",
        reference=("USGS: groundwater measuring points and reference levels", "https://pubs.usgs.gov/tm/1a1/"),
    ),
]
