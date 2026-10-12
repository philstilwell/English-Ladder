"""Three additional nutrition dialogues with independent transfer cases."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Checking a food-allergy message before a group event',
    skill='Distinguish a reported allergy from a preference and avoid unsupported assurances about shared preparation.',
    setup='Nutrition educator Hana helps event coordinator Eli clarify a participant\'s reported food allergy. The actual allergen and clinical severity are not supplied. The venue has not confirmed its ingredients or preparation arrangements. They agree to seek the appropriate information and use the real allergy-safety process rather than promise a dish is safe.',
    cast='Hana | Nutrition educator\nEli | Event coordinator',
    dialogue='''Eli | A participant reported a food allergy, and the registration form reduced it to a general meal preference.
Hana | We need to preserve that distinction and follow the venue's actual allergy-safety process, not treat the two labels as interchangeable.
Eli | I do not have the exact allergen in this note. I should not guess from the dish they asked about.
Hana | Correct. A [[reported allergy::A reported allergy needs accurate clarification and the appropriate safety process, rather than being relabeled as an ordinary preference.]] must remain accurately attributed while the relevant information is clarified through the appropriate route.
Eli | The kitchen said it could remove a garnish. Would that be enough to tell the participant the dish is safe?
Hana | Not on these facts. We do not have verified ingredients or information about [[allergen cross-contact::Allergen cross-contact concerns unintended transfer of an allergen and is not resolved merely by removing a visible garnish.]] during actual preparation and service.
Eli | So removing something visible does not establish what happened before the plate reached the table.
Hana | Exactly. We need the responsible food-service team to explain the actual arrangements, not an assurance invented by the event office.
Eli | I will request the current recipe and product information rather than last year's sample menu.
Hana | An [[ingredient verification::Ingredient verification checks the actual ingredients and current product information rather than relying on an old menu or a dish name.]] needs current details, including any substitutions the kitchen actually plans to use.
Eli | We should also avoid promising that separate utensils are used when nobody has confirmed the preparation process.
Hana | Yes. A specific claim about [[preparation controls::Preparation controls describe actual arrangements intended to manage food-handling risks and must be verified by the responsible service.]] needs verification from the people responsible for those controls.
Eli | If the kitchen cannot provide the assurance the participant needs, we should say that plainly.
Hana | And use the actual safety and access process to discuss appropriate arrangements, without pressuring the person to accept an uncertain option.
Eli | I will keep the participant's information limited to the people who need it for this purpose.
Hana | Good. [[Purpose-limited sharing::Purpose-limited sharing restricts relevant personal information to the people and purpose for which it is legitimately needed.]] avoids turning a necessary coordination message into a general announcement about someone's health.
Eli | The final message should identify what the venue has confirmed and which question is still unresolved.
Hana | It should also make clear who the participant can contact before the event and how the real emergency procedures are handled onsite.
Eli | Then we have a factual coordination task, not permission to diagnose an allergy or improvise a clinical response.
Hana | Correct. A [[verified arrangement::A verified arrangement reflects confirmed practical facts and must not be confused with an unsupported promise that a dish is safe.]] is different from a reassuring phrase with no confirmed preparation information behind it.''',
    transfer_title='A recipe substitution was not checked',
    transfer_setup='A venue changes a packaged ingredient after an earlier menu review. The replacement product has not been checked against the participant\'s reported allergen information. No dish-safety assurance is established.',
    transfer='''Coordinator: "The recipe now uses a ___ ingredient." | replacement | The venue changed the product after the earlier review took place.
Educator: "The earlier check does not verify the new ___." | product | A check of the previous product cannot establish the replacement's ingredients.
Coordinator: "We need the responsible team's current ___." | verification | Current product and preparation information must come from the responsible service.
Educator: "We cannot offer an unsupported safety ___." | assurance | The scenario does not establish the facts needed for a dish-safety promise.'''),
scenario(title='Making a remote consultation private and usable',
    skill='Clarify consent, privacy, interpretation, and label visibility in a remote nutrition appointment.',
    setup='Dietitian Ren meets client Sofia by video. Sofia is in a shared room, her label photograph is unreadable, and she asks for qualified language support. They agree to pause detailed discussion while the service arranges an appropriate private appointment and interpreter. No urgent symptom or clinical instruction is supplied.',
    cast='Ren | Dietitian\nSofia | Client',
    dialogue='''Ren | Before discussing your record, can we check whether this is a private place where you are comfortable speaking?
Sofia | Not really. Other people can hear me, and I did not realize how much personal information we might discuss.
Ren | We can pause the details and arrange a suitable option through the service rather than asking you to speak over that concern.
Sofia | Thank you. I need [[privacy::Privacy concerns the conditions under which personal information is discussed and is not guaranteed merely because an appointment is online.]] before I can explain my routine honestly, especially when the room is shared.
Ren | Are you also comfortable using English for the appointment, or would qualified language support help?
Sofia | I would prefer a [[qualified interpreter::A qualified interpreter supports accurate communication through the service's appropriate arrangements rather than relying on an unprepared bystander.]]. I can discuss everyday food, but I lose details when the language becomes technical.
Ren | We can request the appropriate service. I will speak to you directly and leave time for complete interpretation.
Sofia | I had thought I should ask a colleague in the room, but I would rather not share my personal information that way.
Ren | That preference matters. We should explain the actual arrangements and obtain the relevant [[informed agreement::Informed agreement follows an explanation of the actual arrangements and should not be assumed simply because someone joined a video call.]] rather than assume that joining the call settled every question.
Sofia | The label photograph I sent is also blurry. I cannot tell which line you are trying to read.
Ren | Then I should not guess the amount from an unreadable picture or a similar product online.
Sofia | I can provide a [[legible label::A legible label allows the actual product information to be read instead of substituting guesses or details from another product.]] through the service's approved route when I am able to photograph it clearly.
Ren | Good. Keep the actual product and serving information visible, and avoid including unrelated personal material in the image.
Sofia | Does the technical difficulty mean you will record that I did not cooperate with the appointment?
Ren | No. A [[technical barrier::A technical barrier prevents usable communication or information access and must not be relabeled as a client's unwillingness to participate.]] and a privacy concern are practical problems, not evidence of unwillingness to participate.
Sofia | I would like to confirm the next appointment arrangement rather than leave with a vague instruction to try again.
Ren | We can identify the service contact responsible for the private appointment option and the interpreter request.
Sofia | Then I know which action is mine and which one belongs to the service.
Ren | Exactly. The [[appointment confirmation::Appointment confirmation should identify the actual agreed arrangements rather than treating a request for a new slot as a completed booking.]] needs to reflect the real booking status and language-support arrangement.
Sofia | That lets us return to the nutrition questions when we can actually hear, understand, and discuss them appropriately.''',
    transfer_title='The interpreter request is pending',
    transfer_setup='The service has offered a new appointment slot, but the requested interpreter has not been confirmed. The client has not yet accepted the slot.',
    transfer='''Service: "The appointment slot is currently ___." | offered | An offered slot is not a confirmed booking accepted by the client.
Client: "The interpreter arrangement remains ___." | pending | The service has not yet confirmed the requested language support.
Service: "We still need your ___." | acceptance | The client has not accepted the proposed appointment arrangement in this case.
Client: "Please send the actual booking ___." | status | A clear status update should distinguish offered, accepted, and confirmed arrangements.'''),
scenario(title='Reviewing an incomplete food record without filling the gaps',
    skill='Distinguish missing entries, omitted details, and confirmed absence in a follow-up conversation.',
    setup='Client Jamie returns a three-day food record. Tuesday\'s lunch field is blank because Jamie forgot to record it, not because no lunch was eaten. Monday\'s beverage entry is complete. Wednesday\'s takeout ingredients are uncertain. Nutrition professional Priya corrects the record\'s interpretation without inventing foods or exact quantities.',
    cast='Jamie | Client\nPriya | Nutrition professional',
    dialogue='''Jamie | I returned the three-day record, but I realized the blank on Tuesday might look like I did not eat lunch.
Priya | Let us clarify that before interpreting it. Does the blank mean no lunch, or no entry was made?
Jamie | No entry was made. I ate, but I cannot reconstruct the meal accurately enough now.
Priya | Then we should record [[missing data::Missing data indicates that the information was not recorded or available, which is different from a confirmed absence of intake.]] rather than convert the blank into a confirmed skipped meal.
Jamie | Monday's drink information is complete, though. I recorded every beverage I remembered at the time.
Priya | We can preserve that distinction. An [[entry status::Entry status identifies whether a particular record field is complete, missing, or uncertain rather than labeling the whole record uniformly.]] can differ across the same record instead of everything being simply complete or incomplete.
Jamie | The Wednesday takeout description is uncertain because the restaurant did not provide the ingredient details.
Priya | Mark that [[ingredient uncertainty::Ingredient uncertainty preserves the limit of what is known about the actual meal instead of replacing it with a guessed recipe.]]. A plausible recipe from another restaurant would not establish what was in your food.
Jamie | I was tempted to add exact numbers because the form looked more professional when every field was filled.
Priya | A complete-looking form is not more accurate if the numbers are invented. We can explain which amounts remain approximate.
Jamie | So the record can contain both useful information and clear limitations without becoming useless.
Priya | Yes. A [[documented limitation::A documented limitation makes an uncertainty visible so later interpretation does not treat incomplete information as established fact.]] helps the next person interpret the material correctly rather than assuming certainty that you never claimed.
Jamie | Should I go back and change the blank to no lunch just to make the form easier to process?
Priya | No. That would create a false fact. The correction should describe the missing entry and what you actually remember.
Jamie | I can explain why the field is missing, but that does not recover the lost detail.
Priya | Correct. An [[explanation of missingness::An explanation of missingness identifies why information is absent but does not supply the missing food or quantity itself.]] tells us why the gap exists; it does not magically supply the missing meal.
Jamie | At the next review, I would like to use the same definitions so the record is easier to discuss.
Priya | We can clarify the categories and timing together while keeping the recording task manageable and relevant.
Jamie | Then the revised summary will separate complete drinks, missing lunch information, and uncertain ingredients.
Priya | That is an [[accurate summary::An accurate summary preserves the different certainty levels of the source entries rather than smoothing them into an unsupported complete account.]] because it preserves the evidence levels instead of flattening every entry into a confident account.''',
    transfer_title='A blank means not recorded',
    transfer_setup='A beverage field is blank because the client forgot to record drinks. The client remembers drinking something but cannot identify the amount. No zero-intake claim is supported.',
    transfer='''Client: "The drinks were not ___." | recorded | The missing entry reflects absent recording, not proof that no drinks were consumed.
Professional: "The amount is still ___." | unknown | The client cannot identify an amount from the information supplied.
Client: "The blank must not become ___." | zero | Zero would assert no intake, which the client has not reported.
Professional: "We should preserve that ___." | distinction | Missing information and confirmed absence have different meanings in the record.'''),
]
