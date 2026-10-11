"""Original espresso measurement, strength, and group-order conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Read the shot, not just the timer",
        skill="Distinguish dose, beverage yield, ratio, time, and sensory observations during a recipe check.",
        setup="Fictional bar check by trained staff: the house target is 18 g dry coffee to 36 g espresso. Recorded shot A is 18 g in, 36 g out, 28 seconds; B is 18 g in, 45 g out, also 28 seconds. The time uses the same starting point. These are records to discuss, not equipment-operation instructions.",
        cast="Imani|Barista\nLeo|Coffee lead",
        dialogue="""Imani|Both shots took twenty-eight seconds, so I nearly marked both as matching the recipe. Then I noticed the second cup weighed more.
Leo|Start with the [[dose::Dose is the dry ground coffee input, 18 g in each recorded shot, not the beverage collected.]]. We used eighteen grams of dry coffee in each. What came out into the cups?
Imani|Thirty-six grams for A and forty-five for B. Those are the drink weights after excluding the cups, not water added to the machine.
Leo|Right. That is the [[beverage yield::Beverage yield is the mass of espresso collected: 36 g for A and 45 g for B, excluding the cup.]]. The common time does not make those two outputs equal.
Imani|For A, thirty-six divided by eighteen is two. I would describe it as one part dry coffee to two parts espresso by mass.
Leo|Exactly: a [[one-to-two ratio::18 g dry coffee to 36 g beverage simplifies to 1:2; it is not a percentage extraction measurement.]], written one colon two. That matches the stated mass target for this house recipe.
Imani|For B, forty-five divided by eighteen is two point five. So B is one to two point five, even though the timer shows the same value.
Leo|Yes. Keep [[brew time::Brew time is the elapsed measurement, here 28 seconds from the same starting point; it does not by itself specify dose or output.]] beside the input and output figures. It gives us another observation, not a substitute for weighing.
Imani|I described B as sharper when we tasted it. Should I write under-extracted in the result column because of that?
Leo|Write the [[sensory observation::Sharper is the barista's sensory observation; it does not alone prove a measured extraction percentage or a single cause.]] first. That describes what you perceived without pretending we measured extraction percentage or proved the cause.
Imani|We have not measured dissolved solids for either shot, so I should not invent an extraction percentage from the ratio.
Leo|Correct. The mass ratio and extraction percentage answer different questions. A larger drink weight does not tell us the complete sensory result either.
Imani|I also need to make clear when the timer starts. Otherwise another barista could record a different time for the same run.
Leo|Yes. Use the agreed starting point and record the actual coffee, recipe, and settings. A useful comparison needs consistent definitions.
Imani|For the next check, should we change the dose, grind, and output target together?
Leo|Not for a [[controlled comparison::Changing one planned factor while holding the others consistent makes the resulting comparison easier to interpret; changing everything obscures the cause.]]. We will agree one planned change, keep the other targets consistent, and follow the approved equipment procedure.
Imani|Then I will retain both original records. I will not edit B down to thirty-six just because that was the target.
Leo|Exactly. A target is what we intended; the recorded output is what happened. Both are useful when we compare the next shot.
Imani|My handover: A matches eighteen in and thirty-six out; B has the same dose and time but forty-five out. My taste description stays separate.
Leo|That is clear. We can now choose the next approved check from the evidence rather than from the timer alone.""",
        transfer_title="Separate output from elapsed time",
        transfer_setup="Recorded shots C and D both use 20 g dry coffee. C produces 40 g espresso in 27 seconds; D produces 50 g in 27 seconds. Compare dose-to-beverage mass ratios. No dissolved-solids reading is supplied.",
        transfer="""Barista: The dry-coffee dose is ___ grams in both shots.|20|The dose is the input coffee mass, not the larger beverage weight.
Lead: C has a dose-to-beverage ratio of ___ .|1:2|Forty grams beverage divided by twenty grams dry coffee equals two.
Barista: D has a dose-to-beverage ratio of ___ .|1:2.5|Fifty divided by twenty equals 2.5, despite the same elapsed time.
Lead: The extraction percentage remains ___ .|unmeasured|The supplied mass ratios and times do not establish a dissolved-solids measurement or extraction percentage.""",
        reference=("La Marzocco: dose, beverage yield, and brew time", "https://home.lamarzoccousa.com/how-to-make-espresso/"),
    ),
    scenario(
        title="Strength is not extraction",
        skill="Explain concentration and a practical beverage-based extraction estimate without confusing them with taste or caffeine.",
        setup="Fictional paper-filtered brew: 30 g dry coffee, 550 g brew-water input, 500 g collected beverage, measured 1.35% coffee TDS. Use the simplified beverage-based estimate EY% = beverage mass x TDS% / dry dose. A later arithmetic example adds 100 g water after brewing, with no coffee-solids loss and negligible added solids. This is a calculation exercise, not a universal recipe.",
        cast="Maya|Barista\nNoor|Coffee lead",
        dialogue="""Maya|The brew sheet has five hundred fifty grams of water and five hundred grams of coffee collected. Which figure belongs in this extraction calculation?
Noor|Use the collected [[beverage mass::The specified beverage-based calculation uses 500 g collected coffee, not the 550 g water originally poured into the brewer.]]: five hundred grams. The water input is a different measurement, and some liquid remains with the grounds and filter.
Maya|The refractometer result is one point three five percent TDS. That means concentration, not one point three five percent of the grounds extracted?
Noor|Correct. [[Total dissolved solids::Total dissolved solids, or TDS, expresses beverage concentration here; it is not the percentage of the dry coffee dose recovered.]] describes the coffee concentration in the beverage for this reading.
Maya|So I multiply five hundred by zero point zero one three five. That gives six point seven five grams of dissolved coffee material in the collected drink.
Noor|Yes, using the supplied measurement. Then divide that by the [[dry dose::The denominator for the specified extraction estimate is the 30 g dry coffee dose, not the water input or beverage mass.]] of thirty grams and multiply by one hundred.
Maya|That gives twenty-two point five percent. I should call it the beverage-based estimate in this exercise, not a perfect measurement of everything removed from the grounds.
Noor|Right. That practical [[extraction yield::The specified estimate is 500 x 1.35 / 30 = 22.5%; it is distinct from the 1.35% beverage concentration.]] estimate excludes any additional accounting for dissolved material in retained liquid.
Maya|And the number alone does not say whether everyone will like the cup. We still have to describe what we taste.
Noor|Exactly. Nor is TDS a caffeine test. Keep strength, estimated extraction, sensory description, and customer preference separate.
Maya|Now suppose we add one hundred grams of water to all five hundred grams after brewing. Nothing else is added or lost in the example.
Noor|Then the total becomes six hundred grams. This is [[dilution::Dilution adds water after brewing, lowering concentration without extracting more material from the coffee grounds.]], not another extraction through the grounds.
Maya|The dissolved coffee material is still six point seven five grams. Dividing it by six hundred and multiplying by one hundred gives one point one two five percent.
Noor|Yes. The [[concentration::The calculated concentration falls to 1.125% because 6.75 g of dissolved coffee is spread through 600 g beverage.]] falls, while the calculated mass of recovered coffee material stays the same.
Maya|Then six hundred times one point one two five, divided by thirty, still gives twenty-two point five percent for our beverage-based estimate.
Noor|Correct. A lower concentration after adding water does not mean we reversed the original extraction or removed coffee material.
Maya|Would the instrument necessarily display all three decimal places in one point one two five?
Noor|No. That is the arithmetic result, not a promise of instrument resolution or accuracy. Actual measurement needs the specified calibration, sample preparation, and reporting precision.
Maya|I will label the measured one point three five separately from the calculated diluted value, and keep both beverage weights with them.
Noor|Good. That makes the comparison reproducible without calling a calculation a new measurement or treating a preferred flavor as a universal target.""",
        transfer_title="Calculate the diluted concentration",
        transfer_setup="For a simplified beverage-based calculation, a 25 g dose produces 400 g collected coffee at 1.25% TDS. Add 100 g water after brewing, assuming negligible added solids and no coffee-solids loss. EY% = beverage mass x TDS% / dry dose.",
        transfer="""Barista: Dissolved coffee material in the original drink is ___ grams.|5|Four hundred grams multiplied by 0.0125 gives 5 g of dissolved coffee material.
Lead: The beverage-based extraction estimate is ___ percent.|20|Five grams divided by the 25 g dry dose, multiplied by 100, gives 20%.
Barista: The diluted beverage mass is ___ grams.|500|The original 400 g plus 100 g added water gives 500 g total beverage.
Lead: The calculated diluted TDS is ___ percent.|1.00|Five grams divided by 500 g, multiplied by 100, is 1.00%; the same recovered solids still imply 20% by the stated formula.""",
        reference=("Specialty Coffee Association: distinguishing brew strength, extraction, and sensory preference", "https://sca.coffee/sca-news/25/issue-13/towards-a-new-brewing-chart-xpj8t"),
    ),
    scenario(
        title="Twelve cups, overlapping choices",
        skill="Turn a group order into mutually exclusive drink counts while keeping coffee and milk choices attached to each cup.",
        setup="Fictional advance office order: twelve small hot lattes, all without syrup. Four require decaf; three require oat drink; two require both. All remaining milk is dairy and remaining coffee non-decaf. No allergy has been reported. Named drink details are available. Requested pickup is 08:30; shift-lead capacity confirmation is pending.",
        cast="Amina|Counter barista\nBen|Barista preparing the order list",
        dialogue="""Amina|The office wants twelve lattes. Four are decaf and three are oat. I initially added those to twelve, but that cannot be right.
Ben|Those are [[modifiers::Modifiers change specified drinks within the twelve-cup order; they are not additional cups to add to the total.]] within the order, not extra drinks. Do we know how many people want both decaf and oat?
Amina|Yes, two names have both choices. Every drink is small, hot, and without syrup. The other milk choice is dairy.
Ben|Then start with the [[overlap::The overlap is the two drinks that are both decaf and oat; counting them twice would distort the totals.]]: two decaf oat lattes. Put those two names in that group once each.
Amina|Four drinks are decaf in total. After the two with oat, that leaves two decaf drinks with dairy milk.
Ben|Correct. And of the three [[oat drinks::Three drinks use oat in total; two are decaf, leaving one non-decaf oat drink.]], two are already in the combined group. That leaves one oat latte with non-decaf coffee.
Amina|So far we have two decaf oat, two decaf dairy, and one non-decaf oat. That accounts for five cups.
Ben|The [[remaining seven::Twelve minus the five drinks in the other three distinct groups leaves seven non-decaf dairy lattes.]] are non-decaf dairy lattes. Two plus two plus one plus seven makes twelve.
Amina|Let me cross-check by coffee choice: four decaf and eight non-decaf. By milk: three oat and nine dairy.
Ben|Both checks agree. Keep the [[named list::The named list preserves the combination assigned to each person; correct overall totals alone do not guarantee the right drink for each recipient.]] beside those group counts so we do not swap somebody's choices while preparing labels.
Amina|Would it be enough to put oat on three cups and decaf on four cups independently?
Ben|Not unless the right two cups receive both. The totals could look correct while individual drinks are wrong. Check each label against its person's combined request.
Amina|No allergy is reported on this order. I will not label oat as allergy-safe or assume that it means the person cannot have dairy.
Ben|Right. If an allergy is disclosed, use the actual allergy process. Milk preference and a verified allergy arrangement are not interchangeable.
Amina|The organizer wants pickup at eight thirty. Can I send a message saying that is confirmed now that the numbers add up?
Ben|Not yet. That is the [[requested pickup::08:30 is the requested time; the shift lead has not yet confirmed capacity, so the accurate drink count does not confirm the schedule.]]. The lead still needs to confirm capacity alongside the other orders.
Amina|I will send the complete twelve-drink breakdown to the lead, including the two decaf oat cups, and ask about that pickup time.
Ben|Good. Keep the common details on every group: small, hot, no syrup. Grouping the coffee and milk choices must not drop those instructions.
Amina|My final check is two decaf oat, two decaf dairy, one non-decaf oat, seven non-decaf dairy; twelve named drinks. Eight thirty remains a request.
Ben|That is ready for the capacity check. Once the arrangement is confirmed, communicate it to the organizer and keep any later changes attached to the same order.""",
        transfer_title="Count each combination once",
        transfer_setup="A ten-latte order includes five decaf drinks and four oat drinks. Three drinks are both decaf and oat. All others use non-decaf coffee or dairy milk as applicable. An 09:00 pickup has been requested but not confirmed.",
        transfer="""Counter: Decaf with dairy accounts for ___ cups.|two|Five decaf drinks minus three decaf oat drinks leaves two decaf dairy drinks.
Bar: Non-decaf with oat accounts for ___ cup.|one|Four oat drinks minus the three that are also decaf leaves one non-decaf oat drink.
Counter: Non-decaf with dairy accounts for ___ cups.|four|Ten minus three decaf oat, two decaf dairy, and one non-decaf oat leaves four cups.
Bar: The 09:00 pickup time remains ___ .|requested|Correct counts do not turn a requested pickup into a confirmed production commitment.""",
        reference=("US Bureau of Labor Statistics: taking, preparing, and coordinating food-service orders", "https://www.bls.gov/ooh/food-preparation-and-serving/food-and-beverage-serving-and-related-workers.htm"),
    ),
]
