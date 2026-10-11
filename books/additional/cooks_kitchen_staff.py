"""Original recipe-scaling, yield-cost, and recall-tracing conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="More guests, smaller portions",
        skill="Explain a recipe conversion using both portion count and portion size, with consistent units.",
        setup="Fictional calculation check: the approved soup recipe yields twelve 250 mL portions. The event requires thirty 200 mL portions. Two listed ingredients are 900 g prepared carrots and 2.4 L stock in the base recipe. This excerpt is not a complete recipe or a production authorization; the lead must confirm the adjusted process and equipment.",
        cast="Asha|Prep cook\nMateo|Kitchen lead",
        dialogue="""Asha|I was about to multiply the soup recipe by two and a half for thirty guests, but the event sheet says smaller portions. Can we check the basis first?
Mateo|Yes. The original [[recipe yield::Twelve portions at 250 mL each give a 3,000 mL, or 3 L, base yield.]] is twelve portions at two hundred fifty milliliters each: three liters altogether.
Asha|The new portions are two hundred milliliters, and we need thirty. That makes six thousand milliliters, or six liters.
Mateo|Correct. The [[scaling factor::The required 6 L divided by the original 3 L gives a scaling factor of 2, not the count-only ratio 2.5.]] is six divided by three: two. Thirty divided by twelve would ignore the changed serving size.
Asha|So the two-and-a-half calculation would make seven and a half liters at the old portion size. That is not this event's stated target.
Mateo|Right. Keep the [[portion size::The new portion size is 200 mL, so the target is thirty smaller servings rather than thirty original-size servings.]] visible beside the count. More guests does not mean we can ignore what each guest receives.
Asha|For the carrots, nine hundred grams times two is eighteen hundred grams. I will write one point eight kilograms if the production sheet uses kilograms.
Mateo|Yes, and keep the prepared form stated. Those are [[prepared carrots::The ingredient amount is for carrots in the recipe's prepared form; it is not automatically the amount to purchase before trimming.]], not an instruction to buy one point eight kilograms before any trimming loss.
Asha|The stock starts at two point four liters. Twice that is four point eight liters, not four hundred eighty milliliters.
Mateo|Correct. The [[unit conversion::4.8 L equals 4,800 mL; switching unit labels without converting the number would change the quantity.]] to milliliters would be four thousand eight hundred. Say the number and unit together when you read it back.
Asha|Those two lines are only part of the recipe. I still need the complete approved ingredient list rather than treat carrots and stock as the whole formula.
Mateo|Exactly. Check every line through the approved conversion. Keep this arithmetic check separate from permission to start production.
Asha|Should the cooking time also be doubled? That would be an easy rule to remember, but I am not sure it follows.
Mateo|It does not follow from doubling ingredients. [[Process time::Process time depends on the approved method and equipment; an ingredient scaling factor does not automatically multiply cooking time.]] and equipment loading need their own approved checks, not an automatic times-two rule.
Asha|We may need more than one preparation cycle if the equipment cannot take the whole quantity. Six liters required does not specify one vessel.
Mateo|Right. I will confirm the production arrangement, including the complete recipe, capacity, method, and applicable controls before authorizing the work.
Asha|My calculation read-back: twelve at two hundred fifty is three liters; thirty at two hundred is six liters; factor two.
Mateo|And the two ingredient lines?
Asha|One point eight kilograms prepared carrots and four point eight liters stock. The target is six liters finished yield, not the sum of two unrelated unit labels.
Mateo|Confirmed for the calculation. Keep the complete adjusted recipe and process checks with the production sheet, then begin only under the actual approved arrangement.""",
        transfer_title="Change both count and size",
        transfer_setup="A fictional base recipe yields twenty 150 mL portions. The new target is thirty-six 125 mL portions. Its base celery line is 600 g prepared celery. Calculate quantities only; the full recipe and production controls still require review.",
        transfer="""Cook: The base yield is ___ liters.|3|Twenty times 150 mL equals 3,000 mL, or 3 L.
Lead: The new target yield is ___ liters.|4.5|Thirty-six times 125 mL equals 4,500 mL, or 4.5 L.
Cook: The conversion factor is ___ .|1.5|The new 4.5 L target divided by the 3 L base equals 1.5; portion count alone gives the wrong factor.
Lead: The adjusted prepared celery is ___ grams.|900|The 600 g base ingredient multiplied by 1.5 gives 900 g in the same prepared form.""",
        reference=("BC Cook Articulation Committee: recipe conversion and portion-size changes", "https://opentextbc.ca/basickitchenandfoodservicemanagement/chapter/convert-and-adjust-recipes-and-formulas/"),
    ),
    scenario(
        title="Buying weight is not usable yield",
        skill="Read a trimming test, calculate purchase quantity, and explain cost per usable kilogram.",
        setup="Fictional trimming test: 8 kg as-purchased carrots yields 6.4 kg prepared carrots at the specified stage. Planning assumes that 80% yield for a 10 kg prepared-carrot requirement. Purchase cost is $1.60 per kg, with no credit assigned to trim and no other costs included. These are case figures, not universal carrot yields.",
        cast="Ben|Prep cook\nLina|Kitchen lead",
        dialogue="""Ben|The prep requirement is ten kilograms of prepared carrots. I was going to request ten kilograms from stores, but our yield sheet suggests that will not be enough.
Lina|Check the [[as-purchased weight::The test starts with 8 kg in purchased form, before the specified trimming stage.]] against the usable output. We started the test with eight kilograms and finished with six point four.
Ben|Six point four divided by eight is zero point eight. That means eighty percent reached the prepared form specified on this sheet.
Lina|Yes. That is the [[yield percentage::6.4 kg of prepared output divided by 8 kg input, multiplied by 100, equals 80% for this defined trimming stage.]]. It describes this trimming stage, not a guarantee for every delivery or the final cooked dish.
Ben|Then ten kilograms before trimming would give eight kilograms prepared if this yield holds. We would be two kilograms short of the requirement.
Lina|Correct. Our [[edible portion::The requirement is 10 kg of prepared usable carrots, often described as the edible portion, not 10 kg of untrimmed purchased input.]] requirement is ten kilograms. To work back to purchase weight, divide ten by zero point eight.
Ben|That gives twelve point five kilograms to request. I should not just add twenty percent to ten and stop at twelve.
Lina|Exactly. Twelve multiplied by eighty percent produces nine point six kilograms. It still leaves a [[shortfall::Adding 20% to 10 kg produces 12 kg input and only 9.6 kg usable output at 80%, a 0.4 kg shortfall.]] of four hundred grams.
Ben|The purchase rate is one dollar sixty per kilogram. Twelve point five kilograms would cost twenty dollars at that rate.
Lina|Right. With no trim credit in this case, the [[cost per usable kilogram::The $20 purchase cost divided by 10 kg prepared output is $2 per usable kilogram, before labor and other costs.]] is twenty divided by ten: two dollars.
Ben|So one dollar sixty is the purchased-kilogram rate, and two dollars is the prepared-kilogram ingredient cost. They are not competing quotes for the same form.
Lina|That is the distinction to explain. The preparation loss changes how much usable product the purchase buys; it does not mean the supplier raised the price.
Ben|For a recipe needing two hundred fifty grams of these prepared carrots, the ingredient cost would be fifty cents at two dollars per kilogram.
Lina|Yes. Convert two hundred fifty grams to zero point two five kilograms before multiplying. That is a [[portion ingredient cost::0.25 kg at $2 per usable kg costs $0.50; this covers only the carrot ingredient, not the complete dish or its selling price.]] for carrots only.
Ben|It is not the menu price or the cost of the entire dish. Labor, other ingredients, and other costs are outside this calculation.
Lina|Correct. Also, this sheet assigns no value to the trim. If another approved costing method gives usable by-products a credit, we would need that stated separately.
Ben|I will not describe every gram outside the prepared-carrot output as spoiled food. This test records a preparation yield, not the condition of every removed piece.
Lina|Good. Keep the actual trimming and waste records accurate, and use only the kitchen's approved handling arrangements. Do not invent a salvage value or use.
Ben|My request is twelve point five kilograms in purchased form to plan for ten kilograms prepared, assuming the recorded eighty-percent yield.
Lina|Confirmed. Record the actual input and output when the job is done. If the yield differs, report it; do not change the serving specification to conceal the difference.""",
        transfer_title="Use the decimal yield",
        transfer_setup="A fictional preparation has 75% usable yield. The required usable amount is 9 kg. Purchase cost is $3 per kg, with no trim credit or other costs in this example.",
        transfer="""Cook: The required purchased amount is ___ kilograms.|12|Nine kilograms usable divided by 0.75 equals 12 kg purchased.
Lead: The purchase cost is ___ dollars.|36|Twelve kilograms at $3 per purchased kilogram costs $36.
Cook: The cost per usable kilogram is ___ dollars.|4|The $36 purchase cost divided by 9 kg usable output equals $4 per usable kilogram.
Lead: A 200 g usable portion costs ___ dollars for this ingredient.|0.80|Two hundred grams is 0.2 kg; multiplying by $4 per usable kilogram gives $0.80.""",
        reference=("BC Cook Articulation Committee: yield testing and usable-product costing", "https://opentextbc.ca/basickitchenandfoodservicemanagement/chapter/yield-testing/"),
    ),
    scenario(
        title="Trace the ingredient into the dish",
        skill="Link a recalled supplier lot to kitchen batches and report known quantities without declaring the recall complete.",
        setup="Fictional Australian kitchen: a verified recall notice names sauce lot Q17 for undeclared sesame. Lead Nia has immediately stopped its use and service, isolated remaining stock and related dressing batches D9/D10, and begun the recall response. This later record check must not delay protective action or required notifications. Prior service is still being investigated.",
        cast="Cole|Cook checking preparation records\nNia|Kitchen lead coordinating the response",
        dialogue="""Cole|The receiving record shows four bottles of the recalled sauce, lot Q seventeen. I have two sealed bottles, one partly used bottle, and the label from the emptied fourth.
Nia|Keep the [[lot code::Q17 is the recalled supplier lot, linking the specific sauce receipt and containers; a brand name alone is not the full identifier.]] with each entry. The stop-use and stop-service response is already in effect; this count must not delay it.
Cole|The two sealed bottles and the remaining contents of the opened bottle are identified and separated. The empty bottle's label is retained with the record.
Nia|That records three bottles containing [[remaining stock::Two sealed bottles and one partly used bottle contain remaining sauce; an empty fourth bottle is not a full bottle available for recovery.]]. Do not list the empty bottle as a full unit recovered.
Cole|I cannot give a total volume recovered until the actual remaining quantities are established. Four received does not mean four full bottles still exist.
Nia|Correct. Keep container count and contents quantity separate. Preserve the receipt, labels, and preparation information through our response process.
Cole|The preparation sheet links the emptied bottle to dressing batch D nine. The partly used bottle is linked to D ten.
Nia|Those [[batch records::The kitchen batch records link supplier sauce lot Q17 to dressings D9 and D10, extending the check beyond the original bottles.]] explain why we have stopped service of both dressings. Do not check only the storeroom and overlook food already made with the ingredient.
Cole|Both dressing batches have been identified and held. I have not recorded disposal or return; neither outcome has been confirmed to me.
Nia|Keep their [[disposition::Disposition is the actual decision and outcome for held material, such as authorized return or disposal; holding alone does not establish either.]] pending until the applicable instructions are carried out and recorded. Nobody should put the food back into service on their own.
Cole|Another case has the same brand but lot Q eighteen. It is not the lot named in the notice we have.
Nia|Record that distinction and check the full current recall identifiers and any updates. A different lot code is not a blanket safety certificate for every product or use.
Cole|Some dressing may have been served earlier. The service records are still being checked, so I cannot honestly say nobody received it.
Nia|Report that [[traceability gap::Earlier service is still under investigation; the incomplete trail cannot support a claim that no guest received affected food.]] immediately through the response. Required external action and guest-protection decisions must not wait for us to produce a neat final tally.
Cole|I will give you the verified links and clearly mark the uncertain service history. I will not fill missing quantities from memory and present them as measured.
Nia|Good. Keep the source of each quantity visible. An estimate, a preparation entry, and a physically measured remainder are different kinds of information.
Cole|The new message from the supplier has been received. I have not checked whether it changes the affected lots or the action instructions.
Nia|Review that [[recall update::A recall update may change scope or instructions; merely receiving it does not establish that the earlier interpretation remains current.]] promptly and communicate any change to the affected teams. Keep the response aligned with the current notice and enforcement advice.
Cole|My handoff is four Q seventeen bottles received, three with remaining contents, one emptied, and links to D nine and D ten. Prior service remains unresolved.
Nia|Accepted. Continue the assigned record checks while the protective response remains active. Counts and an internal handoff do not mean the recall, notifications, or guest follow-up are complete.""",
        transfer_title="Do not lose the prepared batch",
        transfer_setup="A verified fictional recall names ingredient lot R6. Immediate protective action is already under way. Five tubs were received: three remain sealed and two were fully used in batch S4. S4 is held; earlier service is unresolved. An empty tub is not recovered ingredient.",
        transfer="""Cook: The recalled supplier lot is ___ .|R6|R6 identifies the supplier lot in the verified notice, not the kitchen's prepared-batch identifier.
Lead: The sealed tubs containing remaining ingredient number ___ .|three|Three tubs still contain sealed stock; the two fully used tubs do not add recovered ingredient.
Cook: The preparation record links the used ingredient to batch ___ .|S4|S4 is the prepared batch that must remain visible alongside the supplier-lot and container records.
Lead: Earlier service remains ___ .|unresolved|No completed service-history check is supplied, so the team cannot claim that nobody received affected food.""",
        reference=("FSANZ: identifying and separating recalled food and maintaining traceability", "https://www.foodstandards.gov.au/business/food-recalls"),
    ),
]
