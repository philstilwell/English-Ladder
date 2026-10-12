"""Original nutrition consultations, food-access discussions, and professional handoffs."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='nutrition-dietetics', title='Nutrition and Dietetics English',
    balanced_answer_columns=True,
    category='Health & life sciences', cover_label='ENGLISH FOR NUTRITION PROFESSIONALS',
    cover_title='Nutrition and\nDietetics', cover_size=34,
    tagline='Understand the routine. Make the language usable.',
    audience='For nutritionists, dietitians, nutrition educators, and professionals supporting food-related conversations within their authorized roles.',
    roles='nutritionists, registered dietitians, nutrition educators, community nutrition staff',
    summary='Practical English for dietary histories, food labels, culturally responsive meal planning, nutrient discussions, supplement questions, referrals, and follow-up.',
    map_intro='Eight consultations move from understanding an eating routine to explaining labels, adapting plans, discussing nutrients, clarifying referrals, reviewing supplements, agreeing on a change, and coordinating support.',
    notes_title='A useful plan starts with an accurate conversation.',
    notes_intro='Food decisions involve time, money, culture, health, and personal preference. Precise nutrition language should make those constraints easier to discuss, not turn an appointment into a test of willpower.',
    field_notes=[
        ('Ask before interpreting', 'A skipped meal may reflect a work schedule, cost, symptoms, or preference. Establish the actual circumstances before choosing language such as restriction or nonadherence.', '"When you say you missed lunch, was there no break or no food available?"'),
        ('Separate the label from the person', 'A serving size is a label reference, not a personalized prescription. Explain the amount actually eaten before comparing nutrient amounts.', '"These figures describe one serving; you ate two servings from this package."'),
        ('Respect familiar food', 'Ask about ingredients, preparation, access, and meaning. Do not describe an entire cuisine as unhealthy or assume that every family eats the same way.', '"Which parts of this meal would you most like to keep?"'),
        ('Name your professional scope', 'Nutritionist, dietitian, and related titles do not carry identical qualifications or permissions everywhere. Identify the actual role and refer clinical questions appropriately.', '"I can explain this label; the medication interaction needs review by your pharmacist."'),
    ],
    scope_note=FICTION + 'This is professional English practice, not medical advice, a diet prescription, or clinical certification. Titles, credentials, and permission to provide medical nutrition therapy differ by jurisdiction. Use qualified clinical review for disease treatment, suspected deficiency, allergies, eating disorders, supplement interactions, and urgent symptoms. Do not calculate a dose or infer a diagnosis from these exercises. Protect client information and follow actual local procedures.',
    sources=[
        source('Academy of Nutrition and Dietetics. About RDNs and NDTRs.', 'https://www.eatright.org/about-rdns-and-ndtrs', 'Background for distinguishing nutrition credentials and professional roles; local rules must still be checked.'),
        source('FDA. Serving Size on the Nutrition Facts Label.', 'https://www.fda.gov/food/nutrition-facts-label/serving-size-nutrition-facts-label', 'Supports distinguishing label serving amounts from the amount a person actually eats.'),
        source('FDA. Added Sugars on the Nutrition Facts Label.', 'https://www.fda.gov/food/nutrition-facts-label/added-sugars-nutrition-facts-label', 'Supports the distinction between added sugars and total sugars in label conversations.'),
        source('NIH Office of Dietary Supplements. Frequently Asked Questions.', 'https://ods.od.nih.gov/HealthInformation/ODS_Frequently_Asked_Questions.aspx', 'Background on supplement evidence, product claims, and the need for appropriate clinical review of interactions.')], units=[])

BOOK['units'].append(unit(
    title='Taking a dietary history without judgment', scene='Lunch depends on the break',
    skill='Use neutral follow-up questions to distinguish eating patterns from assumptions about motivation.',
    brief='Rina works rotating warehouse shifts. On yesterday\'s late shift she ate toast before work, had no scheduled meal break, bought noodles after work, and drank two mugs of tea. She cannot recall the mug size. Maya, a nutrition professional, is collecting a dietary history, not diagnosing a deficiency or prescribing a diet. Rina says a typical week is different from yesterday.',
    cast='Maya | Nutrition professional\nRina | Client',
    culture=('Curiosity before judgment', 'Ask about practical circumstances. Words such as cheats, bad food, and failed imply a judgment that the supplied history does not support.'),
    a='''Which record is being discussed first? | Yesterday's intake | A verified average week | A prescribed meal plan | A laboratory assessment | Rina describes one day and explicitly says other days differ.
What explains the missed meal in this account? | No scheduled meal break | A stated weight-loss target | A diagnosed food intolerance | A lack of nutrition knowledge | The supplied explanation is the work schedule, not a clinical finding.
Which quantity remains uncertain? | The size of each mug | The number of mugs | Whether tea was consumed | Whether toast was eaten | Rina remembers two mugs but cannot specify their volume.''',
    vocabulary='''dietary history | Account of usual food and drink intake and relevant circumstances. | take a dietary history
24-hour recall | Structured account of food and drink consumed during a specified day. | complete a 24-hour recall
meal pattern | Timing and arrangement of eating occasions. | describe the meal pattern
shift work | Work scheduled outside or across conventional daytime hours. | accommodate rotating shift work
eating occasion | Any episode of consuming food or drink. | identify each eating occasion
portion estimate | Approximate amount actually consumed. | clarify a portion estimate
household measure | Familiar container or utensil used to describe an amount. | use a household measure
beverage intake | Drinks consumed during the relevant period. | record beverage intake
snacking | Eating between the person's main meals. | ask about snacking
appetite | Desire to eat, distinct from the opportunity to eat. | describe changes in appetite
satiety | Sense of fullness after eating. | describe satiety after a meal
meal omission | Absence of a meal from the eating pattern. | explore a meal omission
recall bias | Inaccuracy arising from what someone remembers or reports. | acknowledge recall bias
usual intake | Eating pattern over time rather than one isolated day. | distinguish usual intake
weekend variation | Difference between weekday and weekend routines. | explore weekend variation
preparation method | Way a food is cooked or otherwise prepared. | clarify the preparation method
food record | Account of foods and drinks recorded over a period. | review a food record
neutral probe | Nonjudgmental follow-up question that elicits detail. | use a neutral probe''',
    precision='One recalled day cannot establish the usual pattern. A missing meal does not identify its cause until the client explains the circumstances.',
    precision_extra='Keep uncertain quantities approximate. Two mugs is a count, not a verified volume, and no nutrient deficiency follows from this brief account.',
    phrases='''Open neutrally | Could you walk me through what you ate yesterday?
Clarify timing | Was that before your shift or after you got home?
Explore access | What happens when there is no meal break?
Clarify quantity | Which cup or container did you use?
Allow uncertainty | An approximate amount is useful; you do not need to guess an exact number.
Check representativeness | How does that compare with a more usual day?
Avoid judgment | I am trying to understand the routine, not grade your choices.
Summarize accurately | The missed meal was linked to the break schedule.''',
    notes='''Usually versus yesterday | Usually describes a pattern; yesterday identifies one day. Preserve the distinction when summarizing intake.
No break versus no appetite | One describes access to time; the other describes desire to eat. Neither can replace the other without evidence.
About | About marks a quantity as approximate, preventing a remembered estimate from looking measured.''',
    d='''Which follow-up best tests whether yesterday was typical? | How does that compare with your other shifts? | Why do you always skip meals? | So that is your weekly average? | You must not have felt hungry? | Comparing shifts checks representativeness without assuming a pattern or motive.
Which summary preserves the uncertainty? | Two mugs; volume not recalled | Two measured cups | Exactly half a liter | No drinks recorded | The count is known, while container volume is not supplied.
Which wording is least judgmental? | What made a meal difficult during that shift? | Why did you fail to eat properly? | Why ignore the plan? | Why choose a bad routine? | This question asks about circumstances without alleging failure or misconduct.
Which distinction matters when interpreting this record? | Intake on one day versus usual intake | Tea versus any beverage | Toast versus any food | Yesterday versus a calendar date | The central limitation is that one day's account cannot establish the usual pattern.''',
    dialogue='''Maya | Could you walk me through yesterday, starting with what you had before your shift?
Rina | Toast and tea. I can manage this [[24-hour recall::A 24-hour recall concerns a specified day, not an assumed average across the week.]], but yesterday was not a normal day for me.
Maya | That is useful to know. We will compare it with other days after we get the sequence clear.
Rina | My [[shift work::Shift work changes the timing of work and can affect opportunities to eat.]] rotates, so breakfast sometimes happens when other people are having dinner.
Maya | When you said you missed lunch, did you mean you were not hungry or could not take a break?
Rina | There was no meal break. My [[appetite::Appetite concerns the desire to eat, which is different from having time or access to food.]] was fine; I simply could not leave the floor.
Maya | Thanks for separating those. What was the next thing you ate, including anything between meals?
Rina | Noodles after work. My [[portion estimate::A portion estimate describes the approximate amount actually eaten rather than a prescribed amount.]] would be one takeout container, although I left some broth.
Maya | Do you remember how full it was, or would the restaurant's container help us describe it?
Rina | A container would help. A [[household measure::A household measure uses a familiar container or utensil to make an amount easier to describe.]] is easier than trying to guess the weight.
Maya | And drinks across the whole shift, not only the drink that came with your food?
Rina | Two mugs of tea. That is my remembered [[beverage intake::Beverage intake includes drinks across the stated period, not just drinks taken with meals.]], but I cannot tell you the mug size.
Maya | I will leave the volume uncertain. Was there anything small that we have not mentioned?
Rina | No, not yesterday. My [[meal pattern::A meal pattern describes the timing and arrangement of eating occasions rather than judging food choices.]] is different when I work mornings.
Maya | Then we should not turn yesterday into a description of every week. What changes on mornings?
Rina | I get a proper break. My [[usual intake::Usual intake is the pattern over time and cannot be established from one unusual day alone.]] includes a meal at work, not just food after the shift.
Maya | That helps. I am understanding the routine rather than deciding whether you made good or bad choices.
Rina | I appreciate that. A [[neutral probe::A neutral probe elicits detail without implying blame or assuming why the person acted.]] feels easier to answer than asking why I skipped food again.
Maya | We can review a few different days next time using the record format we agree on.
Rina | I can bring a [[food record::A food record documents foods and drinks over a stated period and can capture differences between shifts.]] from both shift types, without pretending that each amount was measured.''',
    rehearsal=['Read the corrected exchange and stress yesterday, usual, and approximate.', 'Change roles and repeat the questions that distinguish appetite from break access.'],
    transfer_title='A cup was not a measuring cup',
    transfer_setup='A client recorded one cup of soup but meant a large mug, not a measured cup. The exact volume remains unknown; the container can be checked next time.',
    transfer='''Professional: "Your word cup referred to a ___." | mug | The client meant a drinking container rather than a standardized measure.
Client: "The exact volume is still ___." | unknown | No measurement is supplied, so the precise volume remains uncertain.
Professional: "The record needs that ___." | clarification | Clarifying the container prevents the entry from appearing precisely measured.
Client: "Next time I can show you the ___." | container | Seeing the actual container can help describe the amount more accurately.'''))

BOOK['units'].append(unit(
    title='Explaining serving sizes and label comparisons', scene='The package contains two servings',
    skill='Explain label arithmetic and distinguish included nutrients from additional amounts.',
    brief='An invented yogurt package contains two servings. Per serving, its label lists 12 grams of total sugars, including 5 grams of added sugars. Jordan eats the whole package. Nutrition educator Lee explains the printed figures without setting a personal sugar target. A second product uses a different serving weight, so a direct per-serving comparison may be misleading.',
    cast='Jordan | Client\nLee | Nutrition educator',
    culture=('Numbers need a reference amount', 'Check whether the listener means one serving or the whole package. Familiar packaging can hide an unfamiliar reference amount.'),
    a='''How many servings did Jordan eat? | Two | One | Five | Twelve | Jordan ate the entire package, which contains two stated servings.
How much added sugar was in the whole package? | 10 grams | 5 grams | 24 grams | 34 grams | Two servings multiplied by five grams gives ten grams of added sugars.
Why should the second product's serving weight be checked? | The reference amounts differ | Its color changes the sugar total | All labels use identical portions | Added sugar is always extra to total sugar | Different reference amounts can make a per-serving comparison misleading.''',
    vocabulary='''Nutrition Facts panel | Standardized nutrition information displayed on a US food label. | read the Nutrition Facts panel
serving size | Label reference amount used for the listed nutrient figures. | check the serving size
servings per container | Number of label servings within the package. | multiply by servings per container
total sugars | All sugars included in the stated label amount. | compare total sugars
added sugars | Sugars added during processing or preparation under the relevant labeling rules. | identify added sugars
naturally occurring sugars | Sugars present in the food's ingredients without being added as sweeteners. | distinguish naturally occurring sugars
percent Daily Value | Label percentage showing contribution to a general daily reference amount. | interpret percent Daily Value
dual-column label | Panel presenting nutrition information for two stated reference amounts. | read a dual-column label
reference amount | Quantity against which a label or comparison is expressed. | align the reference amounts
per-serving value | Nutrient amount for one stated label serving. | use the per-serving value
per-container value | Nutrient amount for the complete package. | calculate the per-container value
ingredient list | Ingredients listed under applicable labeling requirements. | examine the ingredient list
nutrient density | Nutrient content relative to an amount of food or its energy content. | discuss nutrient density
sodium content | Amount of sodium in the specified quantity. | compare sodium content
dietary fiber | Food components classified as fiber under applicable definitions. | identify dietary fiber
saturated fat | Type of fat reported separately in nutrition labeling. | check saturated fat
label rounding | Permitted rounding of figures displayed on a label. | allow for label rounding
like-for-like comparison | Comparison using equivalent quantities and definitions. | make a like-for-like comparison''',
    precision='The five grams of added sugars are included in the twelve grams of total sugars per serving. Do not add them again. The whole package contains twenty-four grams total, including ten grams added.',
    precision_extra='A label reference amount is not a personalized eating recommendation. Percent Daily Value is also not the percentage of a person\'s entire diet supplied by that food.',
    phrases='''Locate the reference | These figures are for the serving shown here.
Scale the amount | For the whole package, multiply each per-serving amount by two.
Explain inclusion | Added sugars are included in total sugars, not added on top.
Compare fairly | Let us put both labels on the same quantity basis.
Avoid prescription | The label does not set your individual portion.
Clarify percentage | This percentage refers to the label's daily reference value.
Check the container | How much of the package did you actually eat?
Correct arithmetic | The total is twenty-four, not thirty-four grams.''',
    notes='''Including | Including marks a subset: added sugars form part of total sugars, not a separate amount to add again.
Per | Per identifies the denominator or reference amount. Per serving and per package can produce different figures.
Twice as much | Twice as much scales an amount by two; it does not mean two grams more.''',
    d='''Which statement explains the whole package correctly? | 24 grams total sugars, including 10 grams added | 34 grams total sugars, including 10 grams added | 12 grams total sugars, including 10 grams added | 10 grams total sugars, including 24 grams added | Both per-serving amounts double, while added sugars remain part of total sugars.
What does including signal? | A quantity within the total | An amount to add to the total | A recommended personal target | A second container | Including identifies a subset and prevents double-counting the same nutrient amount.
Which comparison is most defensible? | Compare equivalent amounts before interpreting the figures | Compare unlike servings without checking weight | Compare package colors | Treat each product name as a nutrition score | Equivalent reference amounts are necessary for a meaningful quantity comparison.
Which statement avoids turning the label into a prescription? | This is the label's reference serving, not your individualized portion | Everyone must eat exactly one serving | Two servings always prove overeating | The package decides your daily needs | The label reports nutrition information and does not prescribe an individual's intake.''',
    dialogue='''Jordan | I thought the yogurt had twelve grams of sugar, but my colleague says it had thirty-four.
Lee | Let us check the [[Nutrition Facts panel::The Nutrition Facts panel provides the serving reference and nutrient amounts needed to resolve the disagreement.]] together before deciding which calculation fits what you ate.
Jordan | I ate the entire package. The front of it looked like something sold for one person.
Lee | The [[servings per container::Servings per container tells us that the full package contains two of the label's reference servings.]] entry says two, so the printed per-serving amounts need to be doubled here.
Jordan | That would make the twelve grams twenty-four. Where does the extra five fit into the calculation?
Lee | Those are [[added sugars::Added sugars are included within the stated total sugars and must not be counted a second time.]]. The word including means they are already part of the twelve, not an extra five.
Jordan | Then the complete package contains ten grams added, inside the twenty-four grams total. Is that right?
Lee | Exactly. You have kept the [[per-container value::The per-container value describes the whole package, unlike the figures printed for one serving.]] separate from the amount listed for one serving.
Jordan | Does that mean the label is telling me I was supposed to eat only half the package?
Lee | No. The [[serving size::Serving size supplies a reference for the label figures and is not an individualized prescription for the client.]] explains the figures; it does not determine your individual portion or nutritional needs.
Jordan | The other yogurt looks lower in sugar per serving. Could I compare those two printed numbers directly?
Lee | First check the [[reference amount::The reference amount is the quantity behind each number, and unequal quantities can distort a comparison.]]. Its stated serving is a different weight, so the numbers are not yet comparable.
Jordan | We would need equivalent amounts, not just two columns that happen to use the word serving.
Lee | Yes, a [[like-for-like comparison::A like-for-like comparison uses equivalent quantities and definitions so the difference has a meaningful basis.]] keeps the quantity consistent before interpreting the difference between products.
Jordan | What about the percentage beside the number? I assumed that meant a percentage of everything I ate today.
Lee | [[Percent Daily Value::Percent Daily Value uses a general label reference amount rather than measuring the person's actual intake that day.]] uses a general daily reference. It is not a measurement of your actual diet today.
Jordan | I also noticed an ingredient list. Would that answer a different question from these nutrient amounts?
Lee | Yes. The [[ingredient list::The ingredient list identifies ingredients, while the nutrition panel reports amounts of specified nutrients.]] tells you what the food contains, while this panel gives the specified nutrient figures.
Jordan | I understand now: check how much I ate, identify the reference, and avoid adding the included sugars twice.
Lee | Correct. Keep the [[per-serving value::The per-serving value applies to one stated label serving and must be scaled when a different amount is eaten.]] attached to its serving whenever you explain the calculation to someone else.''',
    rehearsal=['Read the corrected exchange, emphasizing per serving, whole package, and including.', 'Swap roles and state the two correct totals without turning the label into a personal target.'],
    transfer_title='Three servings in a bottle', transfer_setup='An invented bottle contains three servings. Each serving lists 4 grams total sugars, including 1 gram added. A client drinks the entire bottle. No personal target is supplied.',
    transfer='''Client: "The bottle contains ___ servings." | three | The package explicitly lists three servings, all of which were consumed.
Educator: "The whole bottle has ___ grams of total sugars." | twelve | Three servings multiplied by four grams gives twelve grams total.
Client: "Added sugars are ___ in that total." | included | Added sugars are a subset of total sugars, not an extra amount.
Educator: "The label does not set a personal ___." | target | The scenario gives label quantities but no individualized nutrition target.'''))

BOOK['units'].append(unit(
    title='Adapting plans to food access and culture', scene='Keep the rice; fix the logistics',
    skill='Negotiate feasible food options without dismissing cultural preferences or access constraints.',
    brief='Ana shares a kitchen and has one refrigerator shelf. She wants to keep rice and beans in her meals. Her food budget is limited, the nearest shop is a small market, and she has no freezer space. Nutrition professional Sam discusses two feasible shopping options with her. No clinical restriction or individualized nutrient target is supplied.',
    cast='Ana | Client\nSam | Nutrition professional',
    culture=('Familiar food is information, not an obstacle', 'A culturally responsive discussion asks what the meal means and what is available. Do not assume that changing cuisine is the goal.'),
    a='''Which food preference is explicit? | Keeping rice and beans | Removing all grains | Buying only imported produce | Replacing every familiar meal | Ana explicitly wants to preserve rice and beans in her meals.
Which storage option is unavailable? | Freezer space | One refrigerator shelf | A shared kitchen | Shelf-stable storage in principle | The brief states that Ana has no freezer space available.
What kind of decision is being discussed? | Feasible shopping options | A prescribed clinical restriction | A diagnosed deficiency | A guaranteed health outcome | The discussion concerns access and feasibility, not an individualized clinical prescription.''',
    vocabulary='''food access | Practical ability to obtain suitable food. | assess food access
food insecurity | Limited or uncertain access to adequate food. | discuss food insecurity sensitively
food budget | Money available for food over a stated period. | work within a food budget
staple food | Regularly eaten food central to a person's meals. | retain a familiar staple food
cultural preference | Food choice connected with personal or community traditions. | respect a cultural preference
shared kitchen | Cooking space used by more than one household or person. | plan around a shared kitchen
storage capacity | Space and conditions available for keeping food. | check storage capacity
shelf-stable | Able to be stored unopened without refrigeration under stated conditions. | choose a shelf-stable option
perishable | Likely to spoil unless stored and used appropriately. | plan for perishable ingredients
batch cooking | Preparing several portions in one cooking session. | discuss batch cooking realistically
food waste | Food discarded rather than consumed. | reduce avoidable food waste
unit price | Cost expressed for a standard quantity. | compare unit prices
seasonal produce | Fruits or vegetables available in their relevant growing season. | compare seasonal produce
substitution | Replacement chosen for a particular purpose or constraint. | agree on a feasible substitution
preparation time | Time needed to make a food ready to eat. | estimate preparation time
equipment access | Availability of the tools needed for preparation. | establish equipment access
community food resource | Local service supporting access to food. | identify a community food resource
acceptability | Whether an option fits the person's preferences and circumstances. | check meal acceptability''',
    precision='A cheaper large package is not necessarily the practical choice when storage is limited. Do not treat a preferred staple as the problem simply because it is unfamiliar to the professional.',
    precision_extra='Shelf-stable describes storage under stated conditions, usually before opening; check the actual product instructions. This conversation does not authorize ignoring food-safety guidance.',
    phrases='''Preserve preference | Which familiar foods would you like to keep?
Ask about equipment | What can you actually use in the shared kitchen?
Check storage | Would there be space to store that after opening?
Compare costs | The unit price is lower, but the upfront cost is higher.
Offer a choice | Which of these two options fits your week better?
Respect limits | A plan that needs a freezer would not fit your situation.
Ask permission | Would you like information about local food resources?
Confirm feasibility | Let us check cost, storage, and preparation time together.''',
    notes='''Would fit | Would fit presents compatibility with the stated circumstances rather than a moral judgment about the choice.
Cheaper per unit | A lower unit price does not imply a lower total purchase cost or less waste.
Prefer versus need | Prefer identifies a choice; need may identify a constraint. Ask which meaning the speaker intends.''',
    d='''Which suggestion best respects the stated storage limit? | Compare manageable packages and shelf-stable options | Buy frozen food in bulk | Add a second freezer to the plan | Store every opened item at room temperature | Manageable packages and appropriate shelf-stable options can be discussed without assuming unavailable freezer space.
Which question checks acceptability? | Which option would you actually want to eat? | Which cuisine should you give up? | Why keep your old habits? | Why not copy my meals? | Acceptability concerns the client's preferences, not conformity to the professional's meals.
What does a lower unit price establish? | Lower cost for the comparison quantity | Lower total cost in every case | Adequate storage in every home | No risk of food waste | Unit price compares equivalent quantities but does not settle total cost or practicality.
Which resource offer preserves choice? | Would you like information about local food support? | I enrolled you without asking | Your preferences must change first | You cannot manage food independently | Asking permission offers practical support without making an unsupported judgment or decision.''',
    dialogue='''Ana | I brought the suggested shopping list, but I cannot store half of it in our shared kitchen.
Sam | Let us start with your [[storage capacity::Storage capacity concerns the actual space and conditions available for food, which constrain a feasible shopping plan.]] instead of assuming that everyone has a full refrigerator and freezer.
Ana | One refrigerator shelf, no freezer space, and a cupboard. I also want to keep rice and beans.
Sam | We can keep that [[staple food::A staple food is central to familiar meals and need not be removed merely because the professional suggests changes.]] combination in the discussion. Which ingredients do you normally buy at the nearby market?
Ana | Small bags of rice and canned beans. The bigger packages look cheaper, but the checkout total matters.
Sam | The [[unit price::Unit price compares cost for a standard quantity and does not by itself describe the full amount paid at checkout.]] may be lower for a large package while the upfront cost is higher.
Ana | Exactly. I also cannot keep a giant opened container cold just because it was good value.
Sam | Then [[shelf-stable::Shelf-stable describes storage under specified conditions, and opening the package can change the storage requirements.]] options still need a check of what happens after opening. We should use the actual instructions.
Ana | I can cook twice a week, but the kitchen is busy most evenings and I have only one saucepan.
Sam | That [[equipment access::Equipment access identifies the preparation tools actually available rather than assuming a fully equipped private kitchen.]] matters. A plan requiring three pans at once would not fit the routine you described.
Ana | People keep suggesting batch cooking, but they seem to imagine a freezer full of labeled containers.
Sam | [[Batch cooking::Batch cooking means preparing multiple portions together, but its feasibility depends on safe storage and available space.]] is only useful when preparation and safe storage are feasible. We do not have to build around it.
Ana | Could we compare smaller packages of fresh vegetables with the canned options at my market?
Sam | Yes, and check [[acceptability::Acceptability asks whether the available option suits the person's preferences and circumstances, not merely whether it is available.]] too. Which would you actually enjoy alongside your rice and beans?
Ana | I would use both, depending on the price. I dislike buying a large bag and throwing most away.
Sam | Then avoiding [[food waste::Food waste is food discarded rather than eaten, which can make a seemingly economical purchase impractical.]] belongs in the comparison, alongside the price and what you can store safely.
Ana | That feels more realistic. I am not trying to change everything I eat or buy special ingredients.
Sam | Your [[cultural preference::A cultural preference informs the plan and should not be treated as an obstacle or a defect in the client.]] is part of the plan. We are adapting the logistics, not replacing your familiar meals.
Ana | I would also like information about local support, as long as asking does not commit me to anything.
Sam | I can explain a [[community food resource::A community food resource is a local support option whose access arrangements and suitability should be checked with the client.]] and its actual access arrangements. You can decide whether you would like to follow up.''',
    rehearsal=['Read the corrected exchange and stress the constraints on space, equipment, and cost.', 'Swap roles and repeat the two-choice comparison while preserving the client\'s preferred staple foods.'],
    transfer_title='A lower unit price is not a lower bill', transfer_setup='A small package costs $3; a larger package costs $8 and has a lower unit price. The client has $5 available for this purchase and cannot store the larger package safely.',
    transfer='''Client: "My available budget is ___ dollars." | five | The brief gives five dollars as the amount available for this purchase.
Professional: "The larger package costs ___ dollars upfront." | eight | Eight dollars exceeds the stated amount available at the checkout.
Client: "I also lack safe ___." | storage | The larger package cannot be stored safely in the supplied situation.
Professional: "The lower unit price does not settle ___." | feasibility | Cost at checkout and safe storage both affect whether the purchase is practical.'''))

BOOK['units'].append(unit(
    title='Discussing nutrient sources without a one-food solution', scene='Plant-based does not describe the whole pattern',
    skill='Explain nutrient-source terminology while distinguishing dietary preference from a verified deficiency.',
    brief='Dev has recently started eating a fully plant-based diet and asks whether every plant-based drink has the same nutrients as dairy milk. Dietitian Noor compares two invented labels: Drink A lists added calcium and vitamin B12; Drink B lists neither. No blood results, symptoms, quantities consumed, or personal requirements are supplied. The conversation concerns sources and labels, not a diagnosis or supplement dose.',
    cast='Dev | Client\nNoor | Dietitian',
    culture=('A dietary label is not a complete assessment', 'Ask what a person actually eats. Vegan, vegetarian, and plant-based can describe different choices and do not establish adequacy or deficiency by themselves.'),
    a='''Which product lists added calcium and vitamin B12? | Drink A | Drink B | Both products | Neither product | Only Drink A lists those added nutrients in the supplied labels.
What has not been supplied? | Individual nutrient requirements | Two label descriptions | Dev's stated preference | The absence of listed B12 in Drink B | The case contains label facts but no individualized requirement assessment.
What can the discussion establish from the labels alone? | The listed nutrient differences | A confirmed B12 deficiency | A safe supplement dose | Complete dietary adequacy | The labels support a product comparison, not a clinical conclusion about Dev.''',
    vocabulary='''plant-based pattern | Eating pattern centered on plant foods, with the exact exclusions needing clarification. | clarify a plant-based pattern
vegan diet | Dietary pattern excluding animal-derived foods. | assess a vegan diet
vegetarian diet | Pattern excluding meat, with other exclusions varying by type. | clarify a vegetarian diet
macronutrient | Nutrient required in relatively large amounts, such as protein or carbohydrate. | explain a macronutrient
micronutrient | Vitamin or mineral needed in relatively small amounts. | identify a micronutrient
protein source | Food contributing protein to the diet. | vary the protein sources
amino acid | Building block of proteins. | explain an amino acid
legume | Plant food group including beans, peas, and lentils. | include familiar legumes
fortification | Addition of nutrients to a food product. | check for fortification
calcium | Mineral involved in bone structure and other body functions. | identify a calcium source
vitamin B12 | Vitamin needed for normal blood and nervous-system functions. | identify a reliable vitamin B12 source
iron | Mineral involved in oxygen transport and other functions. | discuss dietary iron sources
heme iron | Form of dietary iron found in animal tissues. | distinguish heme iron
non-heme iron | Form of dietary iron found in plant foods and other sources. | explain non-heme iron
bioavailability | Extent to which an ingested substance is available for use by the body. | discuss nutrient bioavailability
nutrient adequacy | Whether intake meets relevant nutritional needs. | assess nutrient adequacy
dietary variety | Range of foods included over time. | explore dietary variety
enrichment | Addition of specified nutrients, often to restore amounts lost in processing. | distinguish enrichment from a product claim''',
    precision='Fortified is a product description, not a promise that every nutritional need is met. Neither the dietary label nor the two drink labels establish a deficiency.',
    precision_extra='Clarify actual foods, quantities, and any appropriate clinical information before interpreting adequacy. This exercise does not provide supplement recommendations or treatment instructions.',
    phrases='''Clarify the pattern | What does plant-based mean in your meals?
Compare products | These drinks have different nutrient profiles despite similar packaging.
Explain fortification | This product has specified nutrients added to it.
Avoid a leap | That label difference does not diagnose a deficiency.
Ask for the actual item | Could we look at the brand and current label you use?
Broaden the account | Let us look at the whole pattern rather than one food.
Explain a source | A source contributes a nutrient; it does not automatically meet every need.
Preserve scope | Any individualized recommendation needs the appropriate assessment.''',
    notes='''Contains versus meets needs | Contains identifies a nutrient in a product; meets needs requires a broader individualized assessment.
Source of | Source of identifies a contribution and should not be expanded into the only source of or a complete solution.
Not listed | Not listed describes the supplied label, not a laboratory test of the person's nutrient status.''',
    d='''Which explanation is accurate? | Drink A lists added B12; Drink B does not | Both drinks must be nutritionally identical | Drink B proves Dev has a deficiency | Drink A meets all of Dev's needs | The supplied labels establish a difference between products, not Dev's nutritional status.
Which question clarifies the dietary label? | Which foods do you include and exclude? | Why refuse every nutrient? | You must eat the same meals daily? | Does vegan mean you need no assessment? | Asking about actual foods clarifies what the person's dietary label means in practice.
What does bioavailability refer to? | Availability of an ingested substance for bodily use | Availability of a product in a shop | The product's retail price | The person's willingness to buy it | Bioavailability concerns uptake and use, not shopping access or preference.
Which conclusion needs more information? | Whether the whole pattern meets Dev's needs | Which drink lists added B12 | Whether two labels were supplied | Whether the case gives a blood result | Assessing nutrient adequacy needs information beyond the two product descriptions supplied.''',
    dialogue='''Dev | I switched to plant-based meals, and I assumed these two drinks would be more or less interchangeable.
Noor | Before comparing them, could you explain your [[plant-based pattern::A plant-based pattern can mean different food choices, so the professional asks which foods are actually included or excluded.]] and which foods you now include or leave out?
Dev | I no longer eat animal-derived foods. I use beans, lentils, grains, vegetables, and whichever drink is available.
Noor | That describes a [[vegan diet::A vegan diet excludes animal-derived foods, but that label alone does not describe the person's complete nutrient intake.]]. It tells me the exclusions, but not everything about quantities or nutrient sources.
Dev | I can see calcium on one label. Does that mean it occurs in all drinks made from plants?
Noor | No. This one lists [[fortification::Fortification is the addition of specified nutrients to a product and cannot be assumed for every product in the same category.]], while the other label does not list those added nutrients.
Dev | So I should check the actual product, not treat the words plant-based as a complete nutrition statement.
Noor | Exactly. Drink A lists [[vitamin B12::Vitamin B12 is one of the added nutrients explicitly listed for Drink A in this fictional comparison.]] and calcium; Drink B does not list either in the information we have.
Dev | Does choosing Drink B yesterday mean I have a deficiency, or is that jumping ahead of the evidence?
Noor | It is a jump. [[Nutrient adequacy::Nutrient adequacy concerns whether the overall intake meets relevant needs, which cannot be determined from one product choice alone.]] needs an assessment of the broader pattern and any relevant clinical information.
Dev | People also tell me that only one particular food can supply enough protein. That sounds restrictive.
Noor | We can identify each [[protein source::A protein source contributes protein, but no single food must be assumed to describe the entire dietary pattern.]] you actually eat before treating one food as the answer to every question.
Dev | Beans and lentils are already familiar to me. I would rather discuss those than an expensive specialty product.
Noor | Those are [[legumes::Legumes include beans and lentils, making the term directly relevant to the foods the client already eats.]]. Familiar foods are useful starting points when we discuss the variety of your meals.
Dev | I saw the word bioavailability in an article and thought it meant whether a shop had the product.
Noor | [[Bioavailability::Bioavailability describes how an ingested substance becomes available for bodily use, not whether a retailer stocks a food.]] concerns how a substance becomes available for use by the body, not availability on a shelf.
Dev | Then two foods can contain a nutrient without every question about that nutrient being identical.
Noor | Right. We can explain that distinction without turning this label comparison into a claim about your [[micronutrient::A micronutrient is a vitamin or mineral needed in relatively small amounts; the conversation does not establish the client's status.]] status or prescribing a supplement.
Dev | I will bring the labels I actually use and a record of my meals to the next appointment.
Noor | That will help us discuss [[dietary variety::Dietary variety concerns the range of foods eaten over time and provides more context than a single dietary label.]] with real examples rather than assuming that every vegan diet looks the same.''',
    rehearsal=['Read the exchange and distinguish contains, source, and meets needs.', 'Swap roles and explain the difference between the two supplied labels without diagnosing a deficiency.'],
    transfer_title='The brand changed', transfer_setup='A client switches from a drink listing added B12 to a new brand whose label does not list B12. No symptoms or test results are supplied.',
    transfer='''Client: "I changed the ___ I buy." | brand | The change concerns the actual product, not merely a different package size.
Dietitian: "We need to check its current ___." | label | The current label provides the product information needed for the comparison.
Client: "A nutrient difference does not establish a ___." | deficiency | No clinical assessment or test result establishes a deficiency in this case.
Dietitian: "We also need the wider dietary ___." | pattern | Overall intake provides context that cannot be supplied by one product label.'''))

BOOK['units'].append(unit(
    title='Clarifying a clinical referral and assessment', scene='A flagged result is not a complete explanation',
    skill='Distinguish a referral question, a reported laboratory flag, and the conclusions an assessment can support.',
    brief='Dr Chen refers Morgan to registered dietitian Ellis for a nutrition assessment after an electronic result is flagged outside its laboratory reference range. The actual test, value, diagnosis, and treatment plan are not supplied. Morgan asks whether the flag proves poor eating caused the result. Ellis requests the authorized referral information and explains the nutrition assessment while leaving medical interpretation to the appropriate clinician.',
    cast='Morgan | Client\nEllis | Registered dietitian',
    culture=('A referral is a question to clarify', 'Do not present the client as a problem to fix. Explain why information is being collected and which professional answers each question.'),
    a='''What does the supplied result establish? | A laboratory flag was reported | A named disease is confirmed | Food caused the result | A specific diet is prescribed | Only a reported flag is supplied; the actual test and interpretation are absent.
Who requested the nutrition assessment? | Dr Chen | Morgan's employer | A food manufacturer | An anonymous advertiser | Dr Chen is explicitly named as the referring clinician in the case.
Which question requires appropriate clinical interpretation? | What the flagged test means medically | Who sent the referral | Whether an assessment was requested | Whether Morgan has a question | Interpreting an unspecified test medically requires the actual result and qualified clinical review.''',
    vocabulary='''referral question | Specific issue the referring professional asks another service to address. | clarify the referral question
nutrition assessment | Systematic collection and interpretation of nutrition-related information. | complete a nutrition assessment
medical nutrition therapy | Clinical nutrition services for a condition within an appropriately qualified professional's scope. | explain medical nutrition therapy
laboratory reference range | Comparison interval supplied by a laboratory for a test. | check the laboratory reference range
abnormal flag | Marker that a reported result falls outside a stated reference or alert criterion. | clarify an abnormal flag
biochemical data | Laboratory information considered in an assessment. | review biochemical data
anthropometric data | Body measurements considered with their context and limitations. | interpret anthropometric data
clinical interpretation | Qualified explanation of findings in the person's clinical context. | request clinical interpretation
nutrition diagnosis | Nutrition-related problem identified through an appropriate assessment framework. | distinguish a nutrition diagnosis
medical diagnosis | Identification of a disease or clinical condition by an authorized professional. | distinguish a medical diagnosis
etiology | Cause or contributing origin of a problem, when established. | avoid assuming etiology
signs and symptoms | Observed findings and reported experiences relevant to assessment. | distinguish signs and symptoms
care coordination | Organization of information and responsibilities across services. | support care coordination
informed permission | Agreement after the relevant purpose and process have been explained. | seek informed permission
record access | Authorized ability to view relevant information. | confirm record access
assessment finding | Result established through the actual assessment process. | document an assessment finding
clinical context | Relevant health circumstances needed to interpret information. | preserve clinical context
follow-up question | Unresolved issue requiring a later response or review. | assign a follow-up question''',
    precision='A laboratory flag does not establish a dietary cause. Nutrition and medical diagnoses are not interchangeable labels; actual assessment and professional authority matter.',
    precision_extra='Do not insert a plausible test, value, or disease to make the case sound complete. The missing information is precisely what the referral discussion must identify.',
    phrases='''Clarify the purpose | What question did the referring clinician ask us to address?
Avoid blame | The flag does not show that you caused the result through food choices.
Identify missing data | I do not yet have the actual result and its clinical context.
Explain assessment | We will review relevant intake, history, and available information.
Separate roles | Your clinician needs to explain the medical interpretation.
Seek permission | May I request the relevant information through the authorized route?
Limit conclusions | That conclusion would go beyond the information we have.
Assign follow-up | Let us confirm who will answer the outstanding test question.''',
    notes='''Because versus after | After states sequence; because asserts a causal connection. A referral after a result does not establish its cause.
Flagged versus diagnosed | Flagged describes a laboratory marker; diagnosed describes a clinical conclusion requiring appropriate evidence.
Nutrition versus medical | The two modifiers identify different professional meanings and must not be silently dropped.''',
    d='''Which sentence avoids an unsupported cause? | You were referred after a flagged result | Your food caused the result | The flag proves a nutrient deficiency | The referral confirms disease | After preserves the sequence without asserting an unestablished dietary cause.
What should Ellis request? | The actual referral question and authorized relevant information | A guessed test result | A replacement diagnosis from the exercise | The employer's opinion about eating | The missing referral detail and actual record are needed before interpreting the assessment task.
Which distinction should remain explicit? | Nutrition diagnosis and medical diagnosis | Appointment and calendar | Clinician and any adult | Label and packaging color | Those diagnostic terms concern different professional meanings and cannot be used interchangeably.
Which reply best addresses Morgan's concern? | The flag alone does not tell us that food caused it | Yes, any flag proves poor choices | No test can ever relate to nutrition | We can ignore the referring clinician | The reply rejects unsupported blame without denying that nutrition may be relevant after assessment.''',
    dialogue='''Morgan | My result was flagged, and the referral came straight afterward. Does that mean I caused it by eating badly?
Ellis | An [[abnormal flag::An abnormal flag marks a result against a laboratory criterion but does not establish a dietary cause or diagnosis by itself.]] does not tell us that. I also do not yet have the actual test or its context.
Morgan | I only saw a colored mark in the portal. Nobody has explained what the test was measuring.
Ellis | We need the [[clinical interpretation::Clinical interpretation explains the actual finding in the person's health context and requires appropriate professional review.]] from the appropriate clinician, rather than guessing from the color of a portal message.
Morgan | Then what would happen in this appointment, and how is it different from repeating that medical explanation?
Ellis | A [[nutrition assessment::A nutrition assessment collects and interprets relevant nutrition information rather than replacing medical interpretation of an unspecified test.]] looks at relevant intake, history, and available information within my professional role.
Morgan | Should I bring every document I have, or is there a particular question you need answered?
Ellis | First I will clarify the [[referral question::The referral question states what the referring professional wants the receiving service to assess or address.]] so we know what Dr Chen is asking this service to address.
Morgan | The portal mentions a reference range. I thought anything outside it automatically named a disease.
Ellis | A [[laboratory reference range::A laboratory reference range is a comparison interval and does not independently supply a complete clinical diagnosis.]] is a comparison interval, not a complete diagnosis. The actual result needs proper clinical context.
Morgan | Could we request the information instead of my trying to remember a number I did not understand?
Ellis | Yes, through authorized [[record access::Record access must be authorized and directed toward the relevant information rather than unrestricted sharing of personal records.]] and the appropriate permission process. We should not ask you to invent a missing value.
Morgan | I have also seen nutrition diagnosis in a form. Is that simply another name for a medical diagnosis?
Ellis | No. A [[nutrition diagnosis::A nutrition diagnosis identifies a nutrition-related problem through an appropriate assessment framework and is not interchangeable with a medical diagnosis.]] has a specific nutrition-assessment meaning; the two terms are not interchangeable.
Morgan | So we should not label the cause before either professional has reviewed the information needed for their role.
Ellis | Correct. [[Etiology::Etiology concerns the cause or origin of a problem, which has not been established by the referral sequence in this case.]] should not be assumed simply because the nutrition appointment followed the flagged result.
Morgan | I would like one clear route for the unanswered medical question, rather than being passed between services.
Ellis | That is part of [[care coordination::Care coordination organizes responsibilities across services so an unanswered clinical question has an appropriate owner and response route.]]. We can confirm which clinician will explain the test and how the response reaches you.
Morgan | Then today we can clarify the assessment without describing a disease or diet that has not been established.
Ellis | Exactly. We will document each actual [[assessment finding::An assessment finding must come from the assessment performed, not from invented details added to fill gaps in the referral.]] and keep the outstanding questions visible until the right professional answers them.''',
    rehearsal=['Read the corrected dialogue and emphasize after rather than because when describing the referral.', 'Swap roles and distinguish the assessment purpose from the unresolved medical interpretation.'],
    transfer_title='A referral lacks its question', transfer_setup='A referral says nutrition review but provides no question or actual test results. The receiving service requests clarification from the referrer through the authorized channel.',
    transfer='''Receiver: "The referral question is ___." | missing | The words nutrition review do not specify the question to be addressed.
Referrer: "I will provide the relevant test ___." | information | The actual relevant information is needed rather than a guessed result.
Receiver: "We will use the authorized ___." | channel | The scenario explicitly requires an authorized route for sharing relevant information.
Referrer: "The referral alone is not a confirmed ___." | diagnosis | The incomplete referral does not independently establish any named clinical condition.'''))

BOOK['units'].append(unit(
    title='Handling supplement claims and interaction questions', scene='Natural is not an interaction check',
    skill='Explain evidence limits and route product-specific safety questions without endorsing an advertising claim.',
    brief='Client Alex brings an online advertisement for a supplement blend described as natural and clinically tested. The advertisement does not identify the tested formulation, study population, or outcomes. Alex also takes a prescription medicine, but no medicine name or supplement dose is supplied. Nutrition professional Quinn asks for the actual product information and arranges appropriate pharmacist or prescriber review; no stop, start, or dose instruction is given.',
    cast='Alex | Client\nQuinn | Nutrition professional',
    culture=('Respect the question without endorsing the claim', 'A person may have invested money or hope in a product. Acknowledge the question, then examine what the claim actually establishes.'),
    a='''What is missing from the advertisement? | Details of the tested formulation and outcomes | The word natural | The phrase clinically tested | A product category | The brief states that essential details behind the testing claim are absent.
Why is an interaction review needed? | Alex also takes a prescription medicine | All natural products are harmless | The advertisement guarantees compatibility | The exercise supplies a safe dose | Product and medicine details need qualified review; the advertising language cannot establish compatibility.
Which instruction is not supplied? | A stop or start direction | A request for actual product information | A need for appropriate review | A concern about evidence | No treatment or supplement change is authorized by the facts of this exercise.''',
    vocabulary='''dietary supplement | Product intended to supplement the diet under the relevant regulatory definition. | discuss a dietary supplement
Supplement Facts panel | US label panel listing specified supplement ingredients and amounts. | inspect the Supplement Facts panel
active ingredient | Ingredient intended to produce a relevant effect. | identify an active ingredient
proprietary blend | Mixture marketed under a product-specific blend designation. | clarify a proprietary blend
formulation | Specific composition and form of a product. | compare the tested formulation
health claim | Statement connecting a product or substance with a health-related outcome under applicable rules. | examine a health claim
structure/function claim | Claim about supporting a body structure or function under applicable labeling rules. | distinguish a structure/function claim
evidence quality | Strength and reliability of the information supporting a conclusion. | assess evidence quality
study population | People included in a research study. | identify the study population
outcome measure | Defined result used to evaluate a study or intervention. | clarify the outcome measure
randomized trial | Study assigning participants to groups through a random process. | describe a randomized trial
systematic review | Structured synthesis of relevant research using explicit methods. | consult a systematic review
interaction | Effect of one substance or treatment on another's action or safety. | check for an interaction
adverse effect | Unwanted harmful effect associated with a product or intervention. | report an adverse effect
contraindication | Circumstance making an intervention inappropriate under the relevant clinical assessment. | verify a contraindication
product variability | Differences in composition or characteristics between products or batches. | acknowledge product variability
third-party testing | Testing conducted by an organization separate from the manufacturer. | interpret third-party testing
pharmacist review | Assessment by a pharmacist of relevant medicine or product questions. | request pharmacist review''',
    precision='Clinically tested does not state what was tested or whether a meaningful benefit was demonstrated. Natural does not establish safety, and a quality-testing mark does not prove clinical effectiveness.',
    precision_extra='The actual product, medicine, and clinical circumstances are needed for interaction review. Do not use the exercise to start, stop, or change a supplement or prescription.',
    phrases='''Acknowledge interest | I can see why that claim caught your attention.
Ask for specifics | Which formulation was tested, and in whom?
Separate evidence | Being studied is not the same as showing a useful benefit.
Clarify safety | Natural does not tell us whether an interaction is possible.
Check the actual product | Could we review the full label rather than the advertisement alone?
Explain certification limits | A quality check does not establish effectiveness for your situation.
Route the question | The pharmacist or prescriber needs the exact product and medicine details.
Avoid an instruction | I am not giving a start, stop, or dose direction here.''',
    notes='''Tested versus effective | Tested says an investigation occurred; effective requires evidence of the relevant benefit in the relevant context.
May interact | May flags a possibility for review without claiming that an interaction has already been demonstrated in this client.
This formulation | This formulation narrows the statement to the actual product composition, not every item with a similar marketing name.''',
    d='''Which question best evaluates clinically tested? | What formulation, population, and outcome were studied? | How attractive is the packaging? | How many followers shared it? | Does the name sound scientific? | The tested product, participants, and outcomes are needed to understand what the claim supports.
What does natural establish here? | An advertising description, not verified compatibility | No possible interaction | A safe dose with any medicine | Proven effectiveness for Alex | The word natural does not supply the missing safety or interaction assessment.
Which distinction is accurate? | Quality testing and clinical effectiveness answer different questions | Any testing proves all advertised benefits | A seal replaces medicine review | A blend name identifies every dose | Product-quality checks do not themselves establish clinical benefit or individual compatibility.
Which next step stays within the supplied facts? | Obtain product details for appropriate pharmacist or prescriber review | Recommend a guessed dose | Stop the prescription immediately | Promise that no interaction exists | The scenario calls for qualified review using actual details, not a treatment instruction.''',
    dialogue='''Alex | The advertisement says natural and clinically tested. I thought that made the supplement a fairly safe bet.
Quinn | I can see why it sounded reassuring. Could we look at the full [[Supplement Facts panel::The Supplement Facts panel gives relevant product ingredients and amounts that an advertisement may omit.]] rather than relying on those two phrases?
Alex | The front says it is a blend, and I cannot tell whether the study used this exact product.
Quinn | The [[formulation::Formulation identifies the actual product composition and form, which must match the evidence being discussed.]] matters. A study of one ingredient does not automatically test every combination sold under a similar name.
Alex | The advertisement also does not say who took it. Would that change how we interpret the results?
Quinn | Yes. The [[study population::The study population identifies the people researched and affects how far the findings can be applied to another person.]] helps us judge whether the evidence is relevant to the person asking the question.
Alex | It says people felt better, but I cannot find what they measured or what they compared it with.
Quinn | We need the [[outcome measure::An outcome measure defines what result the study assessed, allowing a vague benefit claim to be examined more precisely.]], along with the study design, before treating that phrase as a demonstrated benefit.
Alex | I take a prescription medicine. The salesperson told me natural ingredients cannot interfere with it.
Quinn | Natural does not rule out an [[interaction::An interaction concerns one substance affecting another's action or safety and cannot be ruled out by the word natural.]]. The actual medicine and product need qualified review together.
Alex | I have not brought the medicine name or the exact amount of supplement. I should not guess those.
Quinn | Correct. A useful [[pharmacist review::Pharmacist review needs accurate product and medicine information rather than invented names or amounts.]] depends on accurate details, not an approximate reconstruction of an unfamiliar label.
Alex | There is also a testing seal. I assumed that meant the product had been shown to work for everyone.
Quinn | [[Third-party testing::Third-party testing may address specified quality questions but does not automatically prove clinical effectiveness or individual safety.]] can address particular quality questions. It is not proof of effectiveness for every person or purpose.
Alex | So even a well-made product and a persuasive study headline leave several different questions unanswered.
Quinn | Exactly. [[Evidence quality::Evidence quality concerns the strength and reliability of the support for a claim, not the confidence of its advertising language.]] depends on the actual research, not how confidently the advertisement presents it.
Alex | I would rather check properly than ask you to promise a benefit or tell me a dose from this picture.
Quinn | That is sensible. We should also use the appropriate reporting route for any suspected [[adverse effect::An adverse effect is an unwanted harmful effect that warrants the appropriate clinical response and reporting process.]], rather than dismissing it because the product is sold as natural.
Alex | I will provide the complete product and medicine details for the appropriate professional to review.
Quinn | Then the [[health claim::A health claim must be examined against its actual evidence and applicable meaning rather than treated as a personalized treatment recommendation.]] can be assessed properly before anyone gives you a personalized recommendation about the product.''',
    rehearsal=['Read the corrected dialogue and stress tested versus effective and natural versus safe.', 'Swap roles and request the missing evidence and product details without giving treatment instructions.'],
    transfer_title='A quality seal has a limited meaning', transfer_setup='A product advertises independent testing for specified quality characteristics. The advertisement provides no clinical outcome study. A client asks whether the seal proves benefit for their condition.',
    transfer='''Client: "The seal refers to specified product ___." | quality | The brief describes quality characteristics as the stated purpose of testing.
Professional: "That is different from clinical ___." | benefit | A quality check does not by itself establish benefit for a condition.
Client: "The outcome study is not ___." | supplied | No clinical outcome study is provided in the advertisement described here.
Professional: "We should not turn the seal into a ___." | guarantee | The limited testing claim cannot justify a guaranteed personal health outcome.'''))

BOOK['units'].append(unit(
    title='Agreeing on a small, measurable change', scene='One prepared lunch, not a perfect week',
    skill='Use collaborative language to agree on a bounded action and a meaningful review measure.',
    brief='Taylor wants a more predictable lunch routine but has not agreed to a weight target or a calorie prescription. Nutrition professional Jo offers two options: prepare lunch on one chosen workday, or identify one affordable ready-to-eat option near work. Taylor chooses to prepare lunch on Tuesday. They will review whether preparation and the lunch break were feasible, not grade the week as a success or failure.',
    cast='Jo | Nutrition professional\nTaylor | Client',
    culture=('The client chooses the action', 'A practical goal is an agreement, not a command disguised as a question. Avoid assuming that uncertainty means lack of motivation.'),
    a='''Which action does Taylor choose? | Prepare lunch for Tuesday | Prepare every meal for a month | Follow a new calorie prescription | Reach a specified weight by Friday | Taylor selects one prepared lunch on Tuesday from the two supplied options.
What will the review examine? | Preparation and break feasibility | Whether the whole week was perfect | A promised weight change | A diagnosis from lunch choice | The agreed review concerns whether the specific action fitted the routine.
Which target is absent? | A weight target | A chosen day | A lunch action | A review topic | No weight target or calorie prescription is agreed in this case.''',
    vocabulary='''collaborative goal | Action target chosen through a shared discussion. | agree on a collaborative goal
readiness | Current willingness or preparedness to attempt a change. | explore readiness without pressure
ambivalence | Mixed feelings about a proposed change. | acknowledge ambivalence
reflective listening | Restating the meaning heard to check understanding. | use reflective listening
autonomy | Person's ability to make their own informed choices. | respect client autonomy
implementation intention | Specific plan connecting an action with a situation or cue. | form an implementation intention
action plan | Concrete arrangement for carrying out an agreed step. | confirm the action plan
behavioral goal | Target expressed as an action rather than an assumed outcome. | define a behavioral goal
outcome goal | Target expressed as a desired result. | distinguish an outcome goal
confidence rating | Person's stated estimate of confidence in carrying out an action. | ask for a confidence rating
barrier | Circumstance making an action more difficult. | identify a practical barrier
facilitator | Circumstance making an action easier. | identify a facilitator
contingency plan | Agreed alternative for a specified disruption. | agree on a contingency plan
self-monitoring | Recording one's own relevant actions or experiences. | use focused self-monitoring
process measure | Indicator of whether an action or step occurred. | select a process measure
review point | Agreed occasion for checking progress or fit. | set a review point
goal revision | Adjustment of an agreed goal after new information. | discuss goal revision
nonjudgmental feedback | Response describing facts without blame or moral grading. | give nonjudgmental feedback''',
    precision='Preparing one lunch is a behavioral goal. It is not a promise of weight change, and missing it does not prove unwillingness. Review the actual barrier before changing the plan.',
    precision_extra='Use the supplied choices and facts during practice. A confidence rating helps a conversation; it is not a clinical test or a score of personal worth.',
    phrases='''Reflect the tension | You want a steadier routine, but evenings are already crowded.
Offer bounded options | Would preparing once or identifying a nearby option fit better?
Respect choice | Which option would you prefer to try?
Make it specific | Which day and which preparation step are you choosing?
Check confidence | How confident do you feel about that particular action?
Plan for disruption | What is the agreed alternative if the shift changes?
Review neutrally | What made the action easier or harder this time?
Separate outcome | We are checking whether the action worked, not promising a weight change.''',
    notes='''Try versus promise | Try acknowledges an attempt under real constraints; promise can overstate control over the outcome.
On Tuesday | A named day makes the behavioral target specific without expanding it to every day.
What got in the way | This asks about a barrier and does not assume that the person deliberately ignored the agreement.''',
    d='''Which goal matches the agreement? | Prepare lunch for Tuesday and review feasibility | Never miss lunch again | Lose a stated amount this week | Follow the professional's entire routine | The agreement is a single chosen action with a practical review, not a universal rule.
Which question explores a barrier without blame? | What got in the way of the preparation step? | Why did you fail again? | Why are you unmotivated? | Why ignore everything we discussed? | This question seeks a concrete obstacle rather than attributing a negative motive.
Which is the most relevant process measure? | Whether the lunch was prepared and a break was available | A guaranteed change in body weight | Whether every meal was identical | Whether Taylor pleased Jo | The selected measure directly examines the agreed action and its practical conditions.
How should mixed feelings be described? | Ambivalence about the proposed change | Proof of dishonesty | A confirmed medical diagnosis | Automatic refusal of all help | Ambivalence describes mixed feelings without turning them into blame or an unsupported diagnosis.''',
    dialogue='''Jo | You want a steadier lunch routine, but you have said that evenings already feel crowded. Have I understood?
Taylor | Yes. That [[reflective listening::Reflective listening restates the client's meaning so it can be confirmed or corrected before a plan is chosen.]] is closer to what I mean than telling me I need more discipline.
Jo | We have two options today: prepare lunch once, or identify one affordable ready-to-eat option near work.
Taylor | I feel some [[ambivalence::Ambivalence means mixed feelings about the change, not a refusal to engage or a diagnosis.]]. I like preparing food, but a whole week of packed lunches feels too much.
Jo | We do not have to start with a whole week. Which option would you prefer to try first?
Taylor | Preparing one lunch. That feels like a [[collaborative goal::A collaborative goal is chosen through discussion and reflects the client's preference rather than an imposed instruction.]] I have actually chosen, rather than another rule someone has assigned.
Jo | Which workday would fit best, and what preparation step would make it possible in your current routine?
Taylor | Tuesday. My [[action plan::An action plan specifies the practical arrangements for carrying out the agreed step, here preparing lunch for Tuesday.]] is to prepare it on Monday evening while I am already in the kitchen.
Jo | That names a clear action and a time. How confident do you feel about that particular step?
Taylor | More confident than about five lunches. The main [[barrier::A barrier is a circumstance that makes the action harder; here it is a possible change in work timing.]] would be an unexpected late shift on Monday.
Jo | Then let us keep the alternative visible rather than pretend that your shift can never change.
Taylor | My [[contingency plan::A contingency plan provides an agreed alternative for a specified disruption rather than treating the disruption as personal failure.]] can use the nearby option we discussed if that happens, within the actual budget.
Jo | At the review, we can ask whether preparation worked and whether you had a break to eat.
Taylor | That [[process measure::A process measure checks whether the agreed action and its practical steps occurred rather than assuming a health outcome.]] makes sense. It tells us something useful about the routine, not just whether I tried hard.
Jo | Exactly. We have not agreed to a weight target, and this one lunch cannot promise a particular result.
Taylor | So this is a [[behavioral goal::A behavioral goal is stated as an action, such as preparing lunch, rather than a guaranteed weight or health outcome.]], not a test of whether my body changes by the next appointment.
Jo | Correct. If the action does not fit, we can look at what happened and adjust the agreement.
Taylor | A [[goal revision::Goal revision changes an agreed target in response to information about its fit, rather than automatically treating difficulty as failure.]] would feel more useful than calling the whole week unsuccessful because Tuesday went differently.
Jo | We will review the facts together and keep your choice central. You can also say that an option no longer fits.
Taylor | That [[autonomy::Autonomy means the client retains an informed choice about the action rather than being required to accept the professional's preference.]] makes the small step easier to own. Tuesday lunch is the action I want to try.''',
    rehearsal=['Read the exchange and identify the chosen action, timing, barrier, and review measure.', 'Swap roles and practice the neutral review question without adding a weight target.'],
    transfer_title='The shift changed', transfer_setup='Taylor prepared Tuesday lunch, but an unexpected shift change removed the planned break. The next review distinguishes preparation from the opportunity to eat.',
    transfer='''Client: "The lunch was ___." | prepared | The preparation step occurred, so it should not be recorded as absent.
Professional: "The planned break became ___." | unavailable | The changed shift removed the planned opportunity to eat the lunch.
Client: "Those are separate parts of the ___." | process | Preparation and break access are different practical steps in the agreed action.
Professional: "We can review the barrier without ___." | blame | The scenario supports a practical review, not a negative judgment about motivation.'''))

BOOK['units'].append(unit(
    title='Coordinating follow-up and practical food support', scene='A referral is not a delivered meal',
    skill='Give a concise nutrition-support handoff that distinguishes requests, eligibility checks, and confirmed arrangements.',
    brief='Dietitian Amira and community coordinator Ben discuss client Pat, who has consented to a relevant information exchange. Pat reports difficulty shopping while recovering at home. A community meal-service referral has been sent, but eligibility, start date, and delivery have not been confirmed. No diet order or swallowing assessment is supplied. Amira and Ben agree who will check the referral status and contact Pat.',
    cast='Amira | Dietitian\nBen | Community coordinator',
    culture=('Distinguish the administrative step from the lived result', 'Sent, accepted, scheduled, and delivered are different states. A person can still lack food after a referral has been entered.'),
    a='''What is already complete? | Sending the referral | Confirming eligibility | Delivering the first meal | Establishing a diet order | Only referral submission is complete in the facts supplied here.
What concern has Pat reported? | Difficulty shopping during recovery at home | A diagnosed swallowing problem | A specific food allergy | A prescribed texture level | Pat reports a practical shopping difficulty; no clinical diet instruction is supplied.
What permission is stated? | Consent to the relevant information exchange | Consent to public sharing | Blanket access for every organization | Permission to invent clinical instructions | The case limits permission to the relevant exchange between the services involved.''',
    vocabulary='''discharge nutrition plan | Nutrition-related arrangements communicated when a person leaves a care setting. | clarify a discharge nutrition plan
community referral | Request for support from a community service. | track a community referral
eligibility criteria | Conditions a person must meet to access a service. | confirm eligibility criteria
service capacity | Amount of support a service can currently provide. | check service capacity
referral acceptance | Confirmation that the receiving service has accepted a request. | verify referral acceptance
delivery schedule | Agreed timing of deliveries. | confirm the delivery schedule
waiting list | Record of people awaiting access to a service. | explain waiting-list status
interim arrangement | Temporary support while a longer-term arrangement is pending. | confirm an interim arrangement
consent to share | Permission for a defined information exchange under applicable requirements. | document consent to share
minimum necessary information | Relevant information limited to the purpose and applicable rules. | share minimum necessary information
diet order | Authorized clinical instruction specifying a dietary requirement. | verify a diet order
texture modification | Change in food texture under an appropriate assessed plan. | clarify prescribed texture modification
swallowing assessment | Evaluation of swallowing by appropriately qualified professionals. | request a swallowing assessment
contact attempt | Effort to reach someone, distinct from successful contact. | record a contact attempt
confirmed contact | Verified communication with the intended person. | document confirmed contact
continuity of support | Ongoing availability and coordination of needed assistance. | maintain continuity of support
service handoff | Transfer of relevant information and responsibilities between services. | complete a service handoff
closed-loop referral | Referral process that checks receipt, action, and relevant outcome. | complete a closed-loop referral''',
    precision='Referral sent does not mean service started. Confirm the actual stage and responsible contact without supplying a diet order or swallowing instruction that the case does not contain.',
    precision_extra='If actual food access or health needs require urgent action, follow the real local process. A routine referral status check must not substitute for appropriate immediate support.',
    phrases='''State the practical concern | Pat reports difficulty getting to the shops during recovery.
Separate stages | The referral is sent; acceptance and delivery are not confirmed.
Limit information | I will share only what is relevant through the authorized route.
Avoid an invented order | No verified diet order is included in this handoff.
Assign the check | Who will confirm eligibility and the possible start date?
Check contact | Was that a contact attempt or a completed conversation?
Keep support visible | What is the actual arrangement while the referral is pending?
Close the loop | Please confirm the status and who will update Pat.''',
    notes='''Sent versus accepted | Sent describes the sender's action; accepted requires confirmation from the receiving service.
Scheduled versus delivered | A planned delivery is not evidence that food reached the person.
Attempted versus reached | An attempted call must not be recorded as a completed conversation with the client.''',
    d='''Which handoff states the current position accurately? | Referral sent; eligibility and start date unconfirmed | Meals have started | Eligibility is approved | The first delivery was received | The supplied facts establish submission only, with the later stages still unresolved.
Which instruction must not be added? | A texture-modified diet order | Pat's reported shopping difficulty | The existence of consent | The pending referral status | No swallowing assessment or authorized diet order is supplied in the scenario.
Which question checks a real outcome? | Has the service confirmed a start date and informed Pat? | Was a form opened on screen? | Was a draft message typed? | Does the team hope delivery happened? | Confirmation and client communication provide stronger evidence than internal administrative activity alone.
Which statement distinguishes contact states? | A voicemail is an attempt, not confirmed contact | Leaving a message proves understanding | No reply means consent | A sent text proves delivery of food | A contact attempt does not establish that the intended person received and understood the message.''',
    dialogue='''Amira | Pat has agreed to this relevant information exchange and reports difficulty shopping while recovering at home.
Ben | Thank you. Has the [[community referral::A community referral requests support from a service, but sending it does not establish acceptance or delivery.]] been sent, or has the meal service already confirmed an arrangement?
Amira | It has been sent. I do not have confirmation of eligibility, a start date, or a first delivery.
Ben | I will check the [[eligibility criteria::Eligibility criteria are the service's access conditions and must be verified rather than inferred from referral submission.]] with the actual service instead of assuming that submission means approval.
Amira | Please also ask what support they can currently offer. We should not promise something outside their capacity.
Ben | Agreed. [[Service capacity::Service capacity concerns what support is currently available and can affect whether or when a referral can be acted on.]] may affect timing even when someone meets the access conditions.
Amira | Pat needs a clear account of what is pending, not a message that meals have started when they have not.
Ben | I will distinguish [[referral acceptance::Referral acceptance confirms that the receiving service has accepted the request; it is separate from the first delivery.]] from the later delivery arrangement when I give the update.
Amira | There is no verified diet order in this handoff. Please do not infer one from the name of my service.
Ben | Understood. A [[diet order::A diet order is an authorized clinical instruction and cannot be invented from a referral or professional job title.]] would need the actual authorized instruction, not a guess based on the referral source.
Amira | The same applies to food texture. This case does not contain a swallowing assessment or related instruction.
Ben | I will not add [[texture modification::Texture modification changes food consistency under an appropriate assessed plan and is not supplied by this scenario.]] to the request unless the appropriate verified information is provided through the real process.
Amira | We should keep the information exchange limited to what the service needs for this purpose.
Ben | Yes. [[Consent to share::Consent to share concerns a defined information exchange and does not automatically permit unrestricted distribution of the client's records.]] does not mean unrestricted sharing of every record with every organization.
Amira | When you contact Pat, please distinguish leaving a message from actually speaking with the client.
Ben | I will record a [[contact attempt::A contact attempt is an effort to reach someone and must not be confused with verified successful communication.]] separately if there is no answer, and follow the appropriate process for the unresolved need.
Amira | Who will confirm the start date and check what the actual arrangement is while the referral is pending?
Ben | I will own that check and report the [[delivery schedule::The delivery schedule must be confirmed with the service rather than assumed from the date the referral was sent.]] only when the service confirms it. Any immediate need follows the real support pathway.
Amira | Then the next update should tell us the status, what Pat has been told, and what remains outstanding.
Ben | That will make this a [[closed-loop referral::A closed-loop referral checks receipt, action, and relevant outcomes rather than ending when the request leaves the sender.]] rather than an administrative task that ends as soon as a form is submitted.''',
    rehearsal=['Read the corrected handoff and distinguish sent, accepted, scheduled, and delivered.', 'Swap roles and repeat the ownership and contact statements without adding clinical diet instructions.'],
    transfer_title='The service accepted, but the client has not been reached', transfer_setup='The meal service accepts a referral and proposes Thursday as a start date. The coordinator leaves a voicemail for the client but has not spoken with them. No delivery has occurred.',
    transfer='''Coordinator: "The referral is now ___." | accepted | The service has confirmed acceptance, which is a completed step in this update.
Colleague: "Thursday is the ___ start date." | proposed | The date is proposed, not evidence that delivery has already happened.
Coordinator: "The voicemail was a contact ___." | attempt | Leaving voicemail does not establish a completed conversation with the client.
Colleague: "A delivery has not yet ___." | occurred | The brief explicitly states that no delivery has taken place.'''))
