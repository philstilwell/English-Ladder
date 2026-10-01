"""Original Pharmacy Technician learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='pharmacy-technicians',
    title='Pharmacy Technician English',
    cover_label='ENGLISH FOR ACCURATE PHARMACY COMMUNICATION',
    cover_title='Pharmacy\nTechnician',
    cover_size=38,
    tagline='Check the detail. Explain the next step.',
    audience='For pharmacy technicians and pharmacy support staff communicating with patients, pharmacists, prescribers, insurers, and suppliers.',
    map_intro='Eight pharmacy conversations: clarify an order, explain a claim response, track a renewal, qualify a stock estimate, hand off a label question, handle a private collection request, compare recall details, and correct a mistaken readiness message.',
    notes_title='Small wording differences carry important meaning.',
    notes_intro='Pharmacy communication connects exact product information with patient expectations. Keep a request separate from approval, a delivery estimate separate from stock on hand, and a queue entry separate from completed pharmacist review. Give the person a useful next step without inventing a clinical answer.',
    field_notes=[
        ('Do not fill a gap with a guess', 'A familiar package, remembered color, or usual prescription does not resolve an unclear current order. Identify the missing detail and use the appropriate pharmacist clarification route.', '"The strength field is unclear; the pharmacist needs to clarify it before we can confirm the order."'),
        ('Translate status, not certainty', 'Explain what a claim response or work-queue status actually means. A request for prior authorization does not by itself establish permanent exclusion, approval, or a confirmed patient price.', '"The plan is asking for prior authorization; no decision has arrived yet."'),
        ('Keep a handoff accountable', 'Name the person who accepted the question, what remains unresolved, and the next contact you can genuinely commit to. Do not turn an update window into a promise of supply.', '"Jo will call between three and four with the status, not a guaranteed collection time."'),
        ('Correct a wrong message plainly', 'If an earlier readiness statement was wrong, say what was wrong, give the verified status, and act promptly on its practical effect. Preserve the correction and actual contact outcome in the record.', '"I told you it was ready; that was incorrect. Pharmacist review is still pending."'),
    ],
    scope_note='All medicines, patients, orders, claims, lot references, and timelines in the scenarios are fictional. This book teaches workplace English, not prescribing, dose selection, clinical counseling, legal advice, or certification. Follow current local law, actual role authorization, pharmacist direction, privacy procedures, and the real recall notice. Urgent clinical concerns require the appropriate prompt response; a routine update window is not a safety clearance. United States source examples are not universal rules.',
    sources=[
        dict(title='Pharmacy Technician Certification Board. Guidebook: Code of Conduct.',
             url='https://myaccount.ptcb.org/guidebook/general-policies?print=1',
             note='United States credentialing context for truthful communication, confidentiality, supervision, and practice limits. Fictional role assignments do not establish universal technician duties.', checked='1 October 2026'),
        dict(title='HealthCare.gov. Prior Authorization.',
             url='https://www.healthcare.gov/glossary/prior-authorization/',
             note='United States insurance terminology. The original claim scenario does not establish any specific plan decision, response deadline, coverage, or patient charge.', checked='1 October 2026'),
        dict(title='U.S. Department of Health and Human Services. Prescription Pickup by a Friend or Family Member.',
             url='https://www.hhs.gov/hipaa/for-professionals/faq/can-a-patient-have-a-friend-or-family-member-pick-up-a-prescription/index.html',
             note='United States privacy guidance permits appropriate pickup using pharmacist judgment. The fictional unresolved request is not a blanket ban or universal written-authorization requirement.', checked='1 October 2026'),
        dict(title='U.S. Food and Drug Administration. Understanding Drug Recalls.',
             url='https://www.fda.gov/drugs/drug-recalls/understanding-drug-recalls-what-know-and-what-do',
             note='Background on matching recall details and obtaining appropriate guidance. The fictional lot comparison supplies no affected-stock finding or patient medication instructions.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Prescription intake without assumptions',
    scene='A familiar label does not resolve an unclear strength',
    skill='Identify an ambiguous order field and arrange pharmacist clarification without selecting a strength from memory or appearance.',
    brief='Patient Ellis asks technician Nia to complete a prescription order whose strength field is unclear. Ellis remembers a blue label and says the prescriber usually orders the same thing. Nia cannot select the strength. Pharmacist Maya can take the clarification, but no completion time is known. Nia must distinguish remembered information from verified current instructions, explain the unresolved field, and route the question. No medicine name, dose, or numerical strength is provided in this teaching case, and the exercise does not ask the learner to infer one.',
    cast='Ellis | Patient\nNia | Pharmacy technician',
    culture=('Accuracy can sound helpful rather than obstructive', 'A person who takes a medicine regularly may expect recognition to be enough. Acknowledge that familiarity and explain the exact unresolved detail. Give a pharmacist route instead of asking the patient to guess the prescription or treating the uncertainty as their fault.'),
    a='''Which field is unclear? | Strength | Confirmed pickup time | A verified recall lot | A completed insurance decision | The current order has an unclear strength field, which requires appropriate clarification.
What does Ellis remember? | A blue label and a usual prescription pattern | A verified current strength in the supplied facts | A confirmed pharmacist approval | A guaranteed completion time | The remembered label and pattern are reported context, not verified current instructions.
Who can take the clarification? | Pharmacist Maya | Nia by selecting the most common strength | Another patient with a similar label | The blue label alone | Maya is the identified pharmacist route, while Nia cannot choose the strength.''',
    vocabulary='''prescription | An authorized order for a medicine under the applicable rules. | verify a prescription
intake | Receiving and organizing information needed to process an order. | complete prescription intake
prescriber | A professional authorized to prescribe the relevant medicine. | contact the prescriber
pharmacist | A qualified medicines professional with the relevant practice authority. | refer to the pharmacist
strength | The amount of active ingredient in a stated unit or quantity of the product. | clarify the strength
dose | The amount prescribed for a particular administration. | distinguish dose from strength
dosage form | The physical form of the product, such as a tablet or liquid. | verify the dosage form
active ingredient | The substance intended to produce the medicine's therapeutic effect. | identify the active ingredient
concentration | The amount of a substance within a specified quantity of a preparation. | verify the concentration
route | The specified way a medicine is taken or applied. | verify the route
frequency | How often a prescribed action or administration occurs. | clarify the frequency
directions for use | The authorized instructions for taking or using the medicine. | verify directions for use
quantity | The amount of product specified for supply. | confirm the quantity
days supply | The period the supplied quantity is intended to cover under the verified directions. | verify days supply
brand name | A trade name for a particular product. | confirm the brand name
generic name | The recognized nonproprietary name of the medicine substance. | identify the generic name
product identifier | A code or reference identifying a specified product. | verify the product identifier
NDC | National Drug Code; a United States drug product identification system. | check the NDC
order field | A defined part of the order record. | clarify an order field
ambiguous entry | Information that permits more than one interpretation. | flag an ambiguous entry
clarification request | A request to resolve an unclear or missing instruction. | route a clarification request
current order | The order presently being processed, distinct from past records. | verify the current order
historical record | Information about a previous order or event. | consult the historical record
verified instruction | A direction confirmed through the appropriate process. | preserve the verified instruction''',
    precision='Strength and dose are not synonyms. A product may contain a particular amount per unit, while the prescribed administration uses a specified amount and schedule. This unit supplies neither and does not authorize calculation or selection from a remembered label.',
    precision_extra='Previous records may provide relevant context for the pharmacist, but they do not automatically resolve an unclear current order. Preserve what is uncertain and who supplied each detail. A familiar color, usual routine, or urgent request is not a verified instruction.',
    phrases='''Name the unresolved field | The strength field on this order is unclear.
Acknowledge familiarity | I understand that you usually receive the same medicine.
Separate memory and confirmation | The label color is useful context, but it does not confirm the current strength.
State the role | I cannot select a strength from an unclear entry.
Offer the next step | Pharmacist Maya can take the clarification.
Avoid blame | We need the order clarified; I am not asking you to guess it.
Preserve the source | I will record that you remember a blue label.
Distinguish terms | Strength describes the product; dose concerns the prescribed amount used.
Check the current order | We need the current instructions confirmed, not just an earlier pattern.
Route history appropriately | The pharmacist can review the relevant previous record.
Avoid a time promise | I do not yet have a confirmed completion time.
Keep status accurate | The clarification is pending, not completed.
Ask about the accepted handoff | Can Maya confirm receipt of this question?
Keep clinical advice separate | Any question about how to take it should go to the pharmacist.
Report an urgent concern | Please tell the pharmacist about any concern that needs prompt attention.
Close with a clear boundary | We will use the verified instruction rather than fill the gap with a guess.''',
    notes='''This order | Anchors the question to the current prescription rather than a general habit.
Useful context, but | Acknowledges the patient's contribution while preserving its evidential limit.
Cannot select | Names the specific prohibited action in this role.
Not asking you to guess | Avoids shifting the uncertainty onto the patient.
Do not yet have | Preserves timing uncertainty without inventing a deadline.
Verified instruction | Identifies the required result of clarification, not the technician's preferred answer.''',
    d='''Which reply is accurate? | The strength is unclear; Maya can clarify it, and no completion time is confirmed. | A blue label always identifies one strength. | The most common strength must be correct. | A previous order automatically overrides the current one. | The reply identifies the unresolved detail, appropriate route, and genuine timing uncertainty.
Which distinction is correct? | Strength describes product content per unit or quantity; dose describes the prescribed amount used. | Strength and dose always mean the same thing. | Label color is a universal product identifier. | Days supply can be confirmed without relevant directions. | These terms describe different information and cannot be substituted without creating ambiguity.
What should happen to the patient's recollection? | Record it as reported context for the pharmacist, not verified current instructions. | Erase it because patients never remember anything. | Treat it as the final prescription. | Use it to choose a strength independently. | The recollection may help clarification while remaining distinct from an authorized current instruction.
What must Nia avoid promising? | A completion time that has not been confirmed | A route to the available pharmacist | An accurate description of the unclear field | That the question remains pending | The brief provides no known completion time, so a definite timing promise would be unsupported.''',
    dialogue='''Ellis | Nia, this should be the same prescription I usually collect. I remember the blue label, so can you finish it while I wait?
Nia | I understand, but the [[strength::Strength identifies product content per unit or quantity, and the current unclear field cannot be resolved from label color.]] field on this order is unclear. I cannot select it from the color or usual pattern; pharmacist Maya can take the clarification.
Ellis | I do not know the number from memory. I would rather not guess and give you the wrong information just to make the conversation move faster.
Nia | You do not need to guess the [[current order::The current order is the prescription being processed now, which needs its actual instructions clarified.]]. I will explain the specific missing detail and pass on what you remember as context, not ask you to choose between possible entries.
Ellis | The prescriber has ordered the same thing for a long time. Would looking at the previous record settle it?
Nia | A [[historical record::A historical record may provide context for the pharmacist but does not automatically replace unclear current instructions.]] may help the pharmacist review the question, but it does not automatically replace unclear current instructions. We need the appropriate clarification rather than assume no change could have occurred.
Ellis | I sometimes mix up strength and dose. Are those two words referring to the same part of the prescription?
Nia | No. The [[dose::Dose concerns the prescribed amount used for an administration, while strength describes the product's content per unit or quantity.]] is the prescribed amount used, while strength describes the product content per unit or quantity. I cannot determine either missing instruction from the label color.
Ellis | That explains why my description was not enough. I can tell Maya what I remember, but I cannot verify what the prescriber intended this time.
Nia | I will route a [[clarification request::The clarification request identifies the unresolved field and asks the appropriate professional to establish the intended current information.]] with that distinction intact. Your recollection can be included without being converted into a confirmed direction or a numerical value you did not provide.
Ellis | Please make sure the question goes to Maya rather than just sit in a general note. I do not want to repeat everything at another counter.
Nia | I can give the [[pharmacist::The pharmacist is the identified professional route for resolving the order question rather than leaving the technician to select a strength.]] the exact question and check that it is received. A handoff should identify who has the clarification, not merely say that someone will look at it.
Ellis | Can you tell me how long that will take? I need to decide whether to wait here or arrange another trip.
Nia | I do not have a confirmed completion time for this [[ambiguous entry::The ambiguous entry remains unresolved, and its clarification process has no confirmed completion time in the supplied facts.]]. I can ask about the update route, but I should not promise a collection time before the relevant information is verified.
Ellis | I would rather hear that clearly than be told ten minutes and then discover the question has not even been answered.
Nia | Agreed. A [[verified instruction::A verified instruction is the appropriately confirmed direction needed to resolve the order, not an expected answer or timing promise.]] is still needed. We will distinguish receiving the question, completing clarification, and completing the remaining pharmacy checks instead of treating them as one event.
Ellis | If I have a question about how to take the medicine once the order is clarified, should I ask Maya that as well?
Nia | Yes. Questions about the [[directions for use::Directions for use concern the authorized use of the medicine and should be addressed through the pharmacist's appropriate clinical discussion.]] need the pharmacist's appropriate explanation. Resolving the strength field does not mean every question about your medicine has already been answered.
Ellis | Thank you. Please tell Maya that I remember a blue label and a usual pattern, but that I have not supplied a confirmed current strength.
Nia | I will preserve that in [[intake::Intake organizes the current request and its sources while keeping the unresolved field visible for the proper clarification process.]]. The strength remains unclear, Maya is the clarification route, and no completion time is confirmed. We will not fill the gap with an assumption.''',
    transfer_title='Clarify an unclear dosage form',
    transfer_setup='A current order has an unclear dosage-form field. The patient remembers a white box. Pharmacist Ren accepts the clarification. No product form or completion time has been confirmed.',
    transfer='''Technician: "The unclear field concerns the ___." | dosage form | The unresolved field is the product's physical form, not a verified strength.
Patient: "I remember a ___." | white box | The white box is reported memory and does not establish the product form.
Technician: "The clarification was accepted by ___." | Ren | Ren is the named pharmacist who accepted the question.
Technician: "Completion timing remains ___." | unconfirmed | The brief supplies no confirmed completion time for the clarification or order.''',
))

BOOK['units'].append(unit(
    title='Insurance claims in plain English',
    scene='Prior authorization required is not a final exclusion',
    skill='Explain an insurance response accurately and connect the patient with an accepted status query without promising coverage.',
    brief='Patient Morgan sees the response "prior authorization required" for a pharmacy claim and believes the medicine is permanently excluded. No authorization decision or accepted claim has arrived. Technician Alex can explain the recorded status without promising coverage, a price, or a deadline. Billing colleague Inez has accepted the status query and can explain the request route. The conversation should distinguish the plan requirement, any later decision, and the current pharmacy status. No particular insurance policy, appeal outcome, clinical alternative, or patient payment amount is established in the scenario.',
    cast='Morgan | Patient\nAlex | Pharmacy technician',
    culture=('Translate the message without softening its meaning', 'A short insurer response can sound like a permanent refusal. Explain the actual status in ordinary language while preserving what remains unknown. Avoid both a hopeless conclusion and reassurance that approval is merely a formality.'),
    a='''What does the current response say? | Prior authorization required | Permanent exclusion confirmed | Claim accepted and paid | No further plan process exists | The response identifies a prior-authorization requirement rather than a final permanent exclusion.
What is still absent? | An authorization decision and an accepted claim | Any recorded response | An accepted status-query owner | A patient question | The brief explicitly leaves the decision and claim acceptance unconfirmed.
Who accepted the status query? | Inez | The patient as plan decision-maker | The wholesaler | An unnamed courier | Inez is the identified billing colleague handling the query and explaining its route.''',
    vocabulary='''prior authorization | Plan approval that may be required before specified care or a prescription is covered. | request prior authorization
health plan | The insurance arrangement with defined benefits and rules. | verify the health plan
claim | A request submitted for payment or benefit processing. | submit a claim
claim response | The result or message returned for a submitted claim. | explain the claim response
adjudication | The process of evaluating a claim under the applicable plan rules. | check claim adjudication
response code | A coded message identifying a claim-processing result or requirement. | clarify the response code
rejected claim | A claim not accepted as submitted under the returned response. | investigate a rejected claim
accepted claim | A claim accepted under the relevant processing response. | verify an accepted claim
coverage decision | The plan's determination about the relevant coverage request. | confirm the coverage decision
coverage exclusion | A benefit or service not covered under the applicable plan terms. | verify a coverage exclusion
formulary | A plan's list of medicines and their coverage-related conditions. | check the formulary
benefit tier | A plan category that may affect coverage conditions and cost sharing. | identify the benefit tier
copayment | A fixed patient payment for a covered service under the plan. | verify the copayment
coinsurance | A patient share calculated as a percentage under the applicable benefit. | explain coinsurance
deductible | The amount a person may need to pay before specified plan benefits apply. | verify the deductible
out-of-pocket cost | The amount the person pays rather than the plan. | confirm out-of-pocket cost
pharmacy network | Pharmacies participating under a plan's arrangements. | verify pharmacy network status
PBM | Pharmacy benefit manager; an organization administering defined pharmacy-benefit functions. | identify the relevant PBM
member identifier | The plan reference identifying the insured member. | verify the member identifier
step therapy | A plan requirement to try specified treatment steps under its rules. | clarify a step-therapy requirement
quantity limit | A plan or order restriction on the amount supplied under specified conditions. | verify a quantity limit
exception request | A request for an exception under the plan's defined process. | route an exception request
appeal | A request to review a relevant adverse decision through the applicable process. | clarify the appeal route
status query | A request to establish the current stage, requirement, or result. | accept a status query''',
    precision='Prior authorization required states a plan requirement. It does not by itself establish permanent exclusion, approval, an accepted claim, or the final patient price. Explain the actual response and have the appropriate colleague clarify the applicable request route.',
    precision_extra='A coverage decision and claim processing can involve different information and stages. Do not promise that one status automatically resolves every payment condition. Plan rules differ; use the actual response and verified benefit information rather than a rule remembered from another patient.',
    phrases='''Read the status | The response says prior authorization required.
Explain the term | The plan is asking for its approval process to be completed.
Correct an inference | That message alone does not establish a permanent exclusion.
Avoid false reassurance | It also does not mean approval is guaranteed.
Name what is missing | We do not yet have an authorization decision or an accepted claim.
Identify the owner | Inez has accepted the status query.
Offer the route | Inez can explain how the request is handled for this plan.
Keep the price unconfirmed | I cannot confirm your final payment from this response alone.
Separate stages | A request sent is not a decision received.
Preserve the original response | We should keep the exact message in the query.
Clarify responsibility | Who is providing the information the plan needs?
Avoid a clinical substitution | Any medicine-alternative question needs the pharmacist.
Keep deadlines honest | No response deadline has been confirmed in this conversation.
Do not pre-judge an appeal | The relevant next process depends on the actual decision and plan rules.
Check understanding | The requirement is identified, but the outcome remains open.
Close with a useful next step | I will connect your question with Inez and the verified request route.''',
    notes='''That message alone | Limits the conclusion to what the available response establishes.
Also does not mean | Corrects overoptimism as well as an overly negative inference.
Has accepted | Names a real handoff owner rather than a vague future referral.
From this response alone | Explains why a final price cannot yet be promised.
Request sent versus decision received | Separates activity from outcome.
Depends on the actual decision | Avoids inventing the right appeal or exception process before the facts are known.''',
    d='''Which explanation is accurate? | The plan requires prior authorization; no decision or accepted claim has arrived. | The medicine is excluded forever. | Approval is certain once someone submits a form. | The pharmacy can ignore the response code. | The explanation preserves the actual requirement and open outcome without inventing permanent denial or approval.
Which statement overstates the billing handoff? | Inez accepted the query, so the claim is now approved. | Inez can explain the request route. | The original response should be preserved. | No final patient price is established. | Accepting a status query is an administrative action and does not establish a plan decision.
Which pair must remain distinct? | Request submitted and authorization granted | Copayment and every possible payment term as identical | Formulary and every medicine ever prescribed as identical | Claim response and physical medicine stock as identical | Submitting a request begins or advances a process but does not establish the result.
What should happen to a question about a different medicine? | Refer it to the pharmacist for appropriate clinical discussion. | Choose one solely because another plan covered it. | Let the claim code prescribe a replacement. | Promise that every cheaper medicine is equivalent. | A payment response does not authorize the technician to make a clinical substitution.''',
    dialogue='''Morgan | Alex, this message says prior authorization required. Does that mean my medicine is excluded permanently and there is no point asking the plan anything else?
Alex | It identifies a [[prior authorization::Prior authorization is the plan approval requirement stated in the response, not a completed decision or permanent exclusion.]] requirement, not a permanent exclusion by itself. We do not yet have the plan's authorization decision or an accepted claim, so the outcome remains open.
Morgan | Then is approval just a formality? I have heard people say the pharmacy only needs to send a form and the problem disappears.
Alex | I cannot promise that [[coverage decision::The coverage decision is the plan's actual determination, which has not arrived and cannot be assumed from submitting a form.]]. The request has to follow the actual plan process, and the result is not established merely because someone starts gathering or sending information.
Morgan | I want to understand the message without hearing that everything is impossible or already sorted.
Alex | We should preserve the exact [[claim response::The claim response is the recorded message requiring prior authorization; it should be explained without changing its meaning.]] and explain its current meaning. It tells us what requirement was returned, but it does not confirm the final price, supply status, or a favorable decision.
Morgan | Who is looking into that requirement? I do not want my question to be passed from person to person without anyone knowing what happens next.
Alex | Inez has accepted the [[status query::The status query has an identified owner, Inez, but accepting it does not resolve the coverage requirement.]]. She can explain the request route for this plan and identify the information needed, rather than leave you with a general instruction to contact somebody.
Morgan | If Inez speaks with the plan, will that automatically make the claim accepted, or could more information still be needed afterward?
Alex | An [[accepted claim::An accepted claim is a processing result that must be verified separately from a colleague's inquiry or contact attempt.]] is a separate status that needs verification. A telephone conversation or a submitted request does not, by itself, show that the claim has been accepted.
Morgan | I also need to know what I might pay. Can you read the current message and tell me my final amount now?
Alex | This response does not establish your [[out-of-pocket cost::Out-of-pocket cost is the patient's payment amount, which cannot be calculated or guaranteed from this requirement message alone.]]. The applicable benefit information and claim result need to be checked, and I should not supply a number that the record does not support.
Morgan | My friend has the same medicine on a different plan and pays a small fixed amount. Does that tell us what my plan will do?
Alex | Their [[copayment::A copayment is a fixed payment under a particular benefit, not evidence of another patient's coverage or charge.]] does not establish yours. Plans and individual benefit circumstances can differ, so we need your actual plan information rather than copy another person's experience.
Morgan | Should I immediately appeal, then, or is that a different step from the requirement we are looking at now?
Alex | An [[appeal::An appeal reviews a relevant adverse decision under the applicable process; the current requirement does not establish that this is already the right step.]] depends on the relevant decision and process. Inez can clarify the current route; I should not skip to an appeal or promise a particular outcome before that is established.
Morgan | If another medicine might be an option, I would like that question answered too. I do not want to make a medical decision from an insurance message.
Alex | The [[pharmacist::The pharmacist is the appropriate route for a clinical alternatives question; insurance processing does not authorize the technician to choose treatment.]] should discuss any clinical alternative with you through the appropriate process. We can keep that question separate from Inez's work on the claim requirement.
Morgan | Please tell Inez that I understand the requirement is not a permanent exclusion, but I still need the route, outstanding information, and actual next step.
Alex | I will. The [[health plan::The health plan's actual rules and decision govern the coverage process; the technician's explanation does not create approval or a deadline.]] process remains unresolved, no final charge is confirmed, and Inez owns the status query. We will explain verified developments without turning them into a guarantee.''',
    transfer_title='Explain a different unresolved claim requirement',
    transfer_setup='A response says quantity limit exceeded. No exception decision or accepted claim is available. Billing colleague Sam accepts the query; the pharmacist handles questions about changing treatment.',
    transfer='''Technician: "The returned requirement concerns a ___." | quantity limit | The response specifically identifies a quantity limit rather than a completed exception decision.
Patient: "The billing query is with ___." | Sam | Sam is the colleague who accepted the status query.
Technician: "Any clinical change should be discussed with the ___." | pharmacist | The supplied role assigns treatment questions to the pharmacist, not the billing response.
Technician: "The exception outcome remains ___." | unconfirmed | No exception decision or accepted claim has arrived, so the outcome is still open.''',
))

BOOK['units'].append(unit(
    title='Refill requests and response windows',
    scene='A status call is not a promise of supply',
    skill='Explain an unresolved renewal and make a reliable communication commitment without promising prescriber response or medicine availability.',
    brief='At 11:00, patient Casey asks technician Jo about a refill. The record shows no refills remaining. A renewal request was sent to the prescriber at 09:00, but no response has arrived. Jo can call Casey between 15:00 and 16:00 with a status update. No prescriber response time, supply, or collection time is confirmed. Jo needs to explain what was sent, what remains pending, and what the call will cover. Any concern about running out or interrupted treatment should be referred promptly to the pharmacist rather than treated as safe to wait for the update.',
    cast='Casey | Patient\nJo | Pharmacy technician',
    culture=('Give certainty about the action you control', 'Patients often hear we will call as it will be ready. Name the purpose of the call and repeat the distinction without sounding evasive. A clear update commitment can be useful even when the pharmacy cannot promise another professional\'s response.'),
    a='''What does the refill record show? | No refills remaining | An approved new supply | A confirmed pickup time | A completed prescriber response | The available record has no remaining refills and the renewal response is pending.
When was the renewal request sent? | 09:00 | 11:00 | 15:00 | 16:00 | The brief gives 09:00 as the sent time and 11:00 as the current inquiry time.
What can Jo commit to? | A status call between 15:00 and 16:00 | Guaranteed medicine supply at 15:00 | A prescriber answer at 16:00 | A clinical instruction to wait regardless of need | Jo controls the stated update call, not the prescriber's response or supply outcome.''',
    vocabulary='''refill | A further supply under an existing prescription when permitted and available. | request a refill
refills remaining | The number of further supplies recorded as authorized under the prescription. | check refills remaining
renewal | A request or authorization for a further prescription when the existing authorization is insufficient. | request a prescription renewal
renewal request | A message asking the prescriber to authorize the relevant further prescription. | send a renewal request
prescriber response | The actual reply from the prescribing professional or practice. | await the prescriber response
authorization pending | A status in which the required approval has not yet been received. | explain authorization pending
request timestamp | The time recorded for sending or receiving the request. | verify the request timestamp
transmission confirmation | Evidence that a message was sent or delivered through a system, not that it was approved. | check transmission confirmation
response window | A stated period for an expected or promised response whose status must be clear. | qualify the response window
callback window | The agreed period in which a return call will be made. | confirm the callback window
status call | A call providing current information rather than guaranteeing an outcome. | make a status call
collection time | The time at which an order is confirmed available for pickup. | confirm collection time
supply authorization | The permission needed for the particular medicine supply under applicable rules. | verify supply authorization
partial fill | Supply of less than the prescribed quantity where permitted under applicable arrangements. | refer a partial-fill question
emergency supply | A medicine supply considered under specific legal and clinical requirements. | refer an emergency-supply question
prescription transfer | Movement of prescription information between pharmacies where permitted. | clarify prescription-transfer requirements
refill too soon | A processing response indicating that the requested supply is earlier than the applicable rules allow. | explain a refill-too-soon response
remaining quantity | The amount still available or authorized under the relevant record. | verify the remaining quantity
adherence | Taking medicine in accordance with the agreed clinical instructions. | discuss an adherence concern
treatment interruption | A break in the prescribed treatment that may require clinical advice. | report a treatment interruption
continuity of therapy | Maintaining appropriate treatment under qualified guidance. | support continuity of therapy
follow-up owner | The person responsible for the specified next contact or action. | name the follow-up owner
contact outcome | Whether and how a communication attempt reached the intended person. | record the contact outcome
pending response | A reply still awaited rather than received. | track a pending response''',
    precision='A transmission confirmation may show that the request left the system or reached a destination. It is not a prescriber approval. Similarly, a status call between 15:00 and 16:00 is a communication commitment, not a guaranteed collection window.',
    precision_extra='No refills remaining does not authorize the technician to invent a supply or advise the person to interrupt treatment. Questions about immediate need, emergency supply, partial fills, or alternatives require the pharmacist and applicable rules; the examples confer no entitlement.',
    phrases='''State the record | The record shows no refills remaining.
Give the sent time | We sent the renewal request at nine this morning.
State the current time | As of eleven, no response has arrived.
Keep stages separate | Sending the request does not mean the renewal is approved.
Own the follow-up | I will call you with the status between three and four.
Explain the call | That is an update window, not a confirmed collection time.
Avoid a prescriber promise | I cannot guarantee when the prescriber will respond.
Keep supply unconfirmed | No further supply has been confirmed yet.
Route immediate need | Please discuss any concern about running out with the pharmacist now.
Do not advise interruption | I cannot tell you to stop or change treatment while waiting.
Clarify the update content | I will tell you whether a response has arrived and what remains pending.
Preserve an unsuccessful attempt | If I cannot reach you, I will record the attempt through our process.
Verify contact | Let us confirm the appropriate contact details.
Avoid assuming denial | No response is not the same as a refusal.
Identify the next owner | I am responsible for the agreed status call.
Close accurately | The request is pending, and I will update you even if it is still unresolved.''',
    notes='''As of eleven | Establishes the time boundary of the reported status.
Does not mean approved | Separates transmission from authorization.
With the status | Specifies the call's purpose instead of implying readiness.
Even if unresolved | Makes the update commitment useful without guaranteeing an external result.
No response versus refusal | Distinguishes silence from a negative decision.
Now | Keeps a current clinical need separate from a later routine update.''',
    d='''Which update is accurate at 11:00? | The 09:00 renewal request is unanswered; Jo will give a status update between 15:00 and 16:00. | The renewal is approved because two hours have passed. | Pickup is guaranteed at 15:00. | No response proves permanent refusal. | The accurate version preserves the request time, unresolved response, and separate communication commitment.
What does a successful transmission not prove? | Prescriber authorization | That a system recorded transmission | A reason to retain the request timestamp | The need to check for an actual reply | Transmission records communication activity rather than the clinical or legal authorization sought.
What should happen to a concern about running out? | Refer it promptly to the pharmacist for appropriate assessment. | Tell the patient to wait regardless until 16:00. | Promise an emergency supply automatically. | Recommend borrowing another person's medicine. | The pharmacist must address the actual need and applicable options; the status-call window is not clinical advice.
Who owns the promised call? | Jo | The patient automatically | An unidentified prescriber receptionist | The wholesaler | Jo explicitly commits to the status call and should record its actual contact outcome.''',
    dialogue='''Casey | Jo, I asked for a refill earlier. It is eleven now, and I would like to know whether I can come and collect it this afternoon.
Jo | The record shows no [[refills remaining::Refills remaining describes existing authorization in the record; zero means the requested further supply is not already authorized there.]]. We sent a renewal request at nine, but no response has arrived as of eleven, so I cannot confirm collection yet.
Casey | Does that mean the prescriber refused it? I am worried that no reply means they have decided I should not have it anymore.
Jo | A [[pending response::A pending response means no reply has arrived; it does not establish a refusal or a change in treatment.]] is not the same as a refusal. I can report what the record shows, but I should not invent a decision or a reason for the delay.
Casey | Was the request actually sent, though? Sometimes people say requested when they only mean they have added something to a list.
Jo | The [[request timestamp::The request timestamp records nine o'clock as the sending time and separates an actual sent request from a planned action.]] is nine this morning. We should distinguish that sent event from a task waiting to be sent, while also keeping it separate from a completed authorization.
Casey | If the system says the message went through, why can that not count as approval? It seems as though the practice must have received it.
Jo | [[Transmission confirmation::Transmission confirmation can establish message movement but does not establish that the prescriber reviewed and approved the renewal.]] concerns the message, not the decision. Even when delivery is confirmed, the actual response and any remaining pharmacy checks still need to be established.
Casey | What can you tell me about this afternoon? I do not want to travel here on the assumption that a phone call means the order is ready.
Jo | I can promise a [[status call::The status call provides current information and does not guarantee that the order will be ready for collection.]] between three and four. I will tell you whether a response has arrived and what remains pending; that is not a guaranteed collection time.
Casey | So if there is still no answer by then, you will call anyway rather than wait silently until the order is eventually finished?
Jo | Yes. I own that [[callback window::The callback window is Jo's agreed three-to-four communication period, independent of whether the renewal has been resolved.]]. The update should happen within it even if the status is unchanged, so you know what has and has not been confirmed.
Casey | I also have a concern about how much medicine I have left. I do not want the later call to be treated as advice that waiting is definitely safe.
Jo | Please discuss that possible [[treatment interruption::Treatment interruption can raise a clinical concern that needs prompt pharmacist assessment rather than a routine update assumption.]] with the pharmacist now. I cannot advise you to stop, change, or wait without the appropriate clinical guidance.
Casey | Could the pharmacist discuss whether any immediate supply route is possible? I understand you cannot promise one just because I ask.
Jo | The pharmacist can assess the actual need and rules around any [[emergency supply::Emergency supply depends on the applicable clinical and legal requirements and is not automatically available from a technician's promise.]] or other appropriate option. I cannot authorize that independently or guarantee that a particular route applies.
Casey | Please use my verified contact details for the update. If you cannot reach me, I would not want the note to say I was fully informed.
Jo | I will record the actual [[contact outcome::Contact outcome distinguishes a successful conversation from an attempt or message, so the record does not falsely imply the patient was informed.]]. A call attempt is not the same as speaking with you, and any further action must follow our communication process.
Casey | Thank you. I understand the renewal is still pending, no supply time is confirmed, and you will update me between three and four.
Jo | Correct. I am the [[follow-up owner::The follow-up owner is Jo for the agreed status call, not the person who can guarantee the prescriber's response.]] for that call. We will keep your immediate concern with the pharmacist and keep the later update separate from any promise of prescriber response or medicine availability.''',
    transfer_title='Explain a later renewal update window',
    transfer_setup='No refills remain. A request sent at 10:30 has no reply at 12:30. Technician Mei owns a status call between 16:00 and 17:00. No collection time is confirmed.',
    transfer='''Technician: "The request was sent at ___." | 10:30 | The supplied sending time is 10:30, not the current inquiry time.
Patient: "The current status at 12:30 is ___." | no reply | No prescriber reply has arrived at the stated current time.
Technician: "Mei will call between ___." | 16:00 and 17:00 | That is the agreed communication window, not a collection guarantee.
Patient: "The collection time remains ___." | unconfirmed | The brief supplies no confirmed collection time despite the promised status call.''',
))

BOOK['units'].append(unit(
    title='Stock enquiries and delivery estimates',
    scene='Wednesday is an estimate, not a collection promise',
    skill='Explain a stock shortage, qualify a supplier forecast, and route alternative-treatment questions without choosing a substitute.',
    brief='The pharmacy has no stock for patient Robin\'s order. The wholesaler estimates delivery on Wednesday, but shipment has not been confirmed. Technician Lee can check the next supplier update on Tuesday at 16:00. The pharmacist handles questions about alternatives or immediate clinical need. Lee must separate no stock now, a future delivery estimate, dispatch confirmation, actual receipt, and readiness for collection. No exact arrival hour, guaranteed quantity, substitute medicine, or patient collection time is established. A forecast must not become a clinical instruction to wait.',
    cast='Robin | Patient\nLee | Pharmacy technician',
    culture=('A useful estimate includes its source and limits', 'A patient may turn Wednesday into I can collect Wednesday morning. Keep the timing qualification attached each time it is repeated. Explain what will be checked and where the patient can raise an immediate need instead of giving vague reassurance.'),
    a='''What is the current local stock position? | No stock for this order | A confirmed full quantity ready for collection | A verified substitute already selected | A shipment already received | The brief states that the pharmacy has no stock for the patient's order.
What does Wednesday describe? | The wholesaler's unconfirmed delivery estimate | A guaranteed morning collection time | A completed pharmacist review | A prescribed treatment interruption | Wednesday is a forecast from the supplier, with shipment still unconfirmed.
When can Lee check the supplier update? | Tuesday at 16:00 | Wednesday at 09:00 guaranteed | Immediately after a confirmed receipt already recorded | Monday at noon | The stated next information checkpoint is Tuesday at 16:00.''',
    vocabulary='''stock on hand | Product physically held at the location under the relevant inventory record. | verify stock on hand
available stock | Stock actually available for the intended use after relevant restrictions and checks. | confirm available stock
stockout | A situation in which the required product is not available in stock. | report a stockout
backorder | An order awaiting stock rather than immediately fulfilled. | track a backorder
wholesaler | A business supplying products to pharmacies or other authorized customers. | contact the wholesaler
supplier estimate | A forecast given by the supplying organization. | qualify the supplier estimate
shipment confirmation | Verification that the relevant shipment has actually been arranged or sent as specified. | obtain shipment confirmation
dispatch | Sending goods from the supplier or distribution point. | confirm dispatch
carrier tracking | Recorded information about movement of a shipment. | check carrier tracking
receipt | Actual arrival of the relevant goods at the destination. | confirm receipt
delivery window | The period in which a delivery is expected or committed, with status specified. | clarify the delivery window
allocation | A quantity assigned to a particular order or customer. | verify the allocation
lead time | The period between an order or request and the relevant delivery or completion. | qualify the lead time
supply disruption | An interruption affecting the availability or movement of a product. | report a supply disruption
regional shortage | Limited availability across a defined area rather than one pharmacy alone. | verify a regional shortage
product availability | Whether a specified product can actually be obtained under the relevant conditions. | confirm product availability
generic substitution | Supply of an eligible equivalent generic product under applicable rules and authority. | refer a generic-substitution question
therapeutic alternative | A different treatment option requiring appropriate clinical consideration. | discuss a therapeutic alternative
interchangeability | Whether products may replace one another under relevant clinical and legal requirements. | verify interchangeability
order allocation | The part of stock or supply assigned to the particular order. | check order allocation
supplier checkpoint | An agreed time to obtain updated supplier information. | confirm the supplier checkpoint
collection readiness | Confirmation that the order has completed the relevant steps for pickup. | verify collection readiness
partial delivery | Receipt of less than the ordered quantity. | identify a partial delivery
unconfirmed forecast | An expected outcome that has not been established as a commitment or event. | label an unconfirmed forecast''',
    precision='No stock at one pharmacy does not by itself prove a regional or national shortage. Likewise, an expected delivery day does not confirm dispatch, the full requested quantity, pharmacy receipt, or collection readiness. Name the status actually known.',
    precision_extra='A possible alternative is not automatically interchangeable with the prescribed product. Route clinical and substitution questions to the pharmacist under actual rules. The supplier checkpoint is a communication step, not a recommendation about whether the person can safely wait.',
    phrases='''State current availability | We do not currently have stock for your order.
Attribute the estimate | The wholesaler estimates Wednesday delivery.
Qualify dispatch | Shipment has not yet been confirmed.
Avoid a collection promise | I cannot confirm a pickup time from that estimate alone.
Name the checkpoint | I can check the supplier update Tuesday at sixteen hundred.
Separate stages | Dispatch, receipt, and readiness for collection are different statuses.
Avoid overstating shortage | This confirms our local stock position, not availability everywhere.
Check quantity | We need the quantity for this order confirmed as well as timing.
Route alternatives | The pharmacist can discuss appropriate alternatives with you.
Do not substitute independently | I cannot choose another medicine from the stock shelf.
Address immediate need | Please tell the pharmacist about any concern that needs prompt attention.
Preserve the uncertainty | Wednesday remains an estimate, not a guarantee.
Request a useful supplier update | Has this order been allocated and dispatched, or is it still awaiting confirmation?
Keep receipt factual | A tracking movement does not mean the pharmacy has received the product.
Explain remaining work | Receipt still needs the relevant pharmacy checks before collection is confirmed.
Close the message | No stock now; Wednesday estimated; shipment unconfirmed; supplier check Tuesday at four.''',
    notes='''Currently | Describes the present stock position without making it permanent.
The wholesaler estimates | Identifies the source and forecast status.
From that estimate alone | Explains why collection timing remains uncertain.
For this order | Prevents a general supply update from being mistaken for allocated stock.
Appropriate alternatives | Leaves clinical suitability and legal substitution with the pharmacist.
Still needs | Makes later required steps visible without inventing their completion time.''',
    d='''Which statement preserves the facts? | We have no stock; Wednesday is estimated, shipment is unconfirmed, and Lee will check Tuesday at 16:00. | Wednesday morning collection is guaranteed. | A supplier forecast means the order has arrived. | A local stockout proves every pharmacy is out. | The statement separates the current shortage, supplier forecast, shipment gap, and information checkpoint.
What does carrier movement not establish by itself? | Collection readiness at the pharmacy | That a carrier event was recorded | A reason to check the specific order | Possible progress in transport | Transport progress does not establish receipt and completion of the remaining pharmacy steps.
Who should address an alternative medicine question? | The pharmacist under the applicable process | Lee by selecting a similar-looking box | The carrier driver | The patient by copying a neighbor's medicine | Alternative treatment or substitution requires the appropriate professional and legal process.
What does Tuesday at 16:00 represent? | A supplier information check, not guaranteed supply or clinical advice to wait | A confirmed delivery to the patient | An automatic approval to change treatment | A promised Wednesday arrival hour | The brief gives a checkpoint for information and does not establish a supply outcome or safe waiting period.''',
    dialogue='''Robin | Lee, I was told there was no stock for my order. Has that changed, or are you still waiting for a delivery?
Lee | We still have a [[stockout::The stockout describes the pharmacy's current lack of the required product, not a confirmed shortage at every pharmacy.]] for this order. The wholesaler estimates Wednesday delivery, but shipment is not confirmed, so I cannot tell you the order is available now.
Robin | When I hear Wednesday, I assume I can come in first thing that morning. Is that what the supplier has actually promised?
Lee | No. It is a [[supplier estimate::The supplier estimate forecasts Wednesday delivery without guaranteeing a morning arrival or a patient collection time.]], without a confirmed hour or shipment. I should not turn that into a Wednesday-morning collection promise when the information does not establish one.
Robin | Does no shipment confirmation mean the supplier definitely cannot provide it, or only that you do not yet have confirmation?
Lee | We do not yet have [[shipment confirmation::Shipment confirmation has not arrived; that gap is not itself a definite cancellation or completed dispatch.]]. That is different from a confirmed cancellation. I will keep the uncertainty clear rather than replace it with either a guarantee or an unsupported refusal.
Robin | When will you next be able to check? I do not want to call repeatedly if there is a particular update point.
Lee | The [[supplier checkpoint::The supplier checkpoint is Tuesday at sixteen hundred, when Lee can check updated information rather than guarantee delivery.]] is Tuesday at sixteen hundred. I can check the latest status then, including whether the order has been allocated, dispatched, or remains unconfirmed.
Robin | If the tracking page starts showing movement, would that be enough for you to tell me I can collect it?
Lee | [[Carrier tracking::Carrier tracking records shipment movement and does not establish that the product has reached the pharmacy or completed its checks.]] may show progress in transit, but it is not the same as pharmacy receipt. The actual product and order status still need to be verified.
Robin | I also want to know whether the whole quantity is coming. A general statement about a delivery might not mean my full order is included.
Lee | Correct. We need the [[order allocation::Order allocation identifies the quantity assigned to this particular order rather than a general delivery or stock announcement.]] confirmed for your order. A shipment to the pharmacy does not automatically prove that the requested quantity is included or complete.
Robin | If only some arrives, I suppose that is another question rather than a reason to tell me the entire order has been fulfilled.
Lee | Yes. A [[partial delivery::A partial delivery contains less than the ordered quantity and should not be reported as complete fulfillment.]] should be described accurately. Any decision about what may be supplied to you must follow the pharmacist's process and applicable requirements, not my assumption.
Robin | What about a different medicine? I would like to discuss options if waiting is a problem, but I do not want a substitute chosen just because it is on the shelf.
Lee | The pharmacist can discuss a [[therapeutic alternative::A therapeutic alternative is a clinical option requiring appropriate assessment rather than a technician's stock-based replacement choice.]] or other appropriate route. Please raise any immediate need with them now; the delivery estimate is not advice that you should interrupt treatment or wait without guidance.
Robin | Does your stock problem mean the product is unavailable across the region? That would affect how I understand the situation.
Lee | We have not established a [[regional shortage::A regional shortage concerns availability across an area and cannot be inferred solely from this pharmacy's local stockout.]]. The fact I can confirm is our current local stock position. A broader claim needs its own verified information.
Robin | Thank you. I will not treat Wednesday as a pickup appointment. Please keep the supplier's estimate and any later confirmed facts separate.
Lee | I will. [[Collection readiness::Collection readiness requires the relevant receipt and pharmacy checks, not just a supplier forecast or movement in transit.]] comes after the appropriate steps are confirmed. For now: no stock, Wednesday estimated, shipment unconfirmed, and the supplier checkpoint Tuesday at four.''',
    transfer_title='Explain a Friday estimate without promising pickup',
    transfer_setup='No stock is available for an order. The supplier estimates Friday delivery, but dispatch is unconfirmed. Technician Bea can check Thursday at 11:00. The pharmacist handles alternative-treatment questions.',
    transfer='''Technician: "Estimated delivery is ___." | Friday | Friday is the supplier's forecast, not a guaranteed collection time.
Patient: "Dispatch is still ___." | unconfirmed | The brief explicitly leaves dispatch unconfirmed despite the estimate.
Technician: "The supplier check is ___." | Thursday at 11:00 | Thursday 11:00 is the stated information checkpoint, not a collection promise.
Patient: "An alternative-treatment question goes to the ___." | pharmacist | The pharmacist is the appropriate route for the clinical alternatives discussion.''',
))

BOOK['units'].append(unit(
    title='Pickup questions and pharmacist consultations',
    scene='The label question has a named pharmacist',
    skill='Recognize an auxiliary-label question and complete a clear pharmacist handoff without interpreting or changing the instruction.',
    brief='At pickup, patient Arden asks technician Kit what an auxiliary label means. Kit can identify the label but is not authorized to interpret its instruction. Pharmacist Ravi is available at the consultation counter and has accepted the question. No instructions are changed in this scenario, and the actual label wording is not supplied as a clinical direction. Kit should acknowledge the uncertainty, explain the handoff, and help Arden reach Ravi without implying that a label is optional or that handing over the package has already answered the question.',
    cast='Arden | Patient\nKit | Pharmacy technician',
    culture=('A question at pickup is part of the visit', 'A queue can make someone reluctant to ask about medicine instructions. Acknowledge the question without rushing the person or suggesting that familiar wording is obvious. A named pharmacist handoff is more helpful than pointing vaguely toward another counter.'),
    a='''What does Arden ask about? | An auxiliary label | A confirmed recall lot | The wholesaler's route | A final insurer appeal | The question concerns the meaning of an additional label on the medicine package.
Who has accepted the question? | Pharmacist Ravi | Kit as independent clinical interpreter | The next patient in line | An unidentified prescriber | Ravi is available at the consultation counter and has accepted the handoff.
What changes to the instructions are established? | None | A new dose chosen by Kit | Removal of every warning | An automatic change in frequency | The scenario explicitly states that no instructions are changed.''',
    vocabulary='''auxiliary label | An additional label providing a relevant medicine instruction or caution. | identify the auxiliary label
dispensing label | The pharmacy label with the relevant patient and medicine directions. | verify the dispensing label
patient counseling | A professional discussion helping the patient understand the medicine and its use. | arrange patient counseling
consultation counter | The designated place for the pharmacist discussion. | direct to the consultation counter
medication guide | Patient information supplied for certain medicines under relevant requirements. | provide the medication guide
patient information leaflet | Written product information intended for the patient. | identify the patient information leaflet
package insert | Product information supplied with the medicine, with audience and purpose varying by format. | identify the package insert
warning | Information drawing attention to a relevant risk or required caution. | clarify a warning
precaution | A condition or measure requiring care in using a medicine. | ask about a precaution
contraindication | A circumstance in which a medicine or treatment may be inappropriate. | refer a contraindication question
interaction | A relevant effect arising from a medicine used with another substance or condition. | ask about an interaction
food interaction | A possible effect involving medicine use and food. | refer a food-interaction question
alcohol interaction | A possible effect involving medicine use and alcohol. | refer an alcohol-interaction question
drowsiness | A tendency to feel sleepy or less alert. | report drowsiness
storage condition | A requirement for keeping a product appropriately. | clarify storage conditions
refrigeration | Storage under specified refrigerated conditions when required. | clarify a refrigeration instruction
light protection | Storage or handling intended to limit relevant light exposure. | clarify light-protection wording
measuring device | A device intended to measure an appropriate quantity accurately. | identify the supplied measuring device
administration device | Equipment used to deliver a medicine under the specified directions. | identify the administration device
privacy | Protection of personal information and conversation from inappropriate exposure. | protect privacy
teach-back | A check in which the person explains their understanding so the professional can clarify it. | use teach-back appropriately
accepted handoff | A transfer of a question or task acknowledged by the receiving person. | confirm an accepted handoff
instruction interpretation | Explanation of what a direction means for the person's medicine use. | refer instruction interpretation
counseling completion | Confirmation that the actual professional discussion occurred, not merely that it was offered. | record counseling completion''',
    precision='An auxiliary label adds information; it is not optional merely because it is separate from the main label. The technician can identify which label prompted the question while the pharmacist explains its meaning for the actual medicine and patient.',
    precision_extra='Offered counseling, accepted handoff, and completed counseling describe different events. Ravi accepting the question gives it an owner. It does not prove that the discussion has happened, that the person understands, or that any instruction has changed.',
    phrases='''Welcome the question | Thank you for asking about that label.
Identify the item | You are referring to the auxiliary label beside the main dispensing label.
State the boundary | I can identify it, but I cannot interpret the instruction for you.
Name the pharmacist | Ravi has accepted your question.
Give a clear location | Ravi is available at the consultation counter.
Keep the wording intact | I will pass on the exact label and your question.
Avoid an optionality claim | An additional label is not automatically optional.
Do not change instructions | I am not changing any direction on this package.
Explain the handoff | The pharmacist will discuss what the instruction means for your medicine.
Respect privacy | We can use the practice's appropriate private discussion arrangement.
Clarify the uncertainty | Please tell Ravi which part is unclear.
Invite checking understanding | You can explain what you understood and ask Ravi to clarify it.
Avoid a false completion | The question is accepted; the consultation has not yet been completed.
Route device questions | Ravi can address the appropriate use of the supplied device within the consultation.
Keep pickup and counseling distinct | Handing over a package does not itself answer a clinical question.
Close with the owner | I will connect you with Ravi, who has accepted the question.''',
    notes='''Thank you for asking | Makes clarification welcome rather than an interruption to the queue.
Beside the main label | Identifies the physical source without interpreting it.
Has accepted | Gives the question a confirmed professional owner.
Not automatically optional | Corrects an inference without supplying a clinical instruction.
Explain what you understood | Supports clarification instead of testing the patient's intelligence.
Not yet completed | Keeps the handoff distinct from the actual consultation.''',
    d='''Which response completes the appropriate handoff? | Ravi has accepted your auxiliary-label question and is available at the consultation counter. | Ignore the extra label because it is not the main one. | I will invent an interpretation to keep the queue moving. | Collecting the package means counseling is complete. | The response identifies the question, confirmed pharmacist owner, and practical location without changing the instruction.
What does Ravi's acceptance establish? | The question has a receiving pharmacist, not a completed consultation. | The patient already understands every instruction. | A dose change has been prescribed. | The label can be removed. | Acceptance confirms the handoff while the actual discussion and understanding remain separate.
Which statement is inappropriate? | The auxiliary label is always optional. | The exact question should reach Ravi. | No instruction has been changed here. | Device questions can be raised with the pharmacist. | An additional label can contain important directions or cautions and cannot be dismissed as optional by category.
What should the patient be encouraged to clarify? | The actual unclear wording and their understanding during the pharmacist discussion | An invented dose supplied by the technician | Another patient's instructions as a substitute | The meaning of an unnamed medicine without a professional review | The pharmacist needs the real instruction and question to provide an appropriate explanation.''',
    dialogue='''Arden | Kit, before I finish collecting this, what does the extra label mean? I recognize the words, but I am not sure how they apply to me.
Kit | Thank you for asking. You are referring to the [[auxiliary label::The auxiliary label is the additional label prompting the question; identifying it is different from interpreting its instruction.]] beside the main label. I can identify it, but pharmacist Ravi needs to explain the instruction for your medicine.
Arden | I assumed that if it was important, everything would be on the main label. Is an extra sticker just general advice I can ignore?
Kit | It is not automatically optional. Ravi can explain how the [[dispensing label::The dispensing label and additional information may have different functions; the main label does not make every auxiliary instruction optional.]] and additional information apply together. A label's position on the package is not a reason to disregard it.
Arden | Can you explain it quickly here? I can see there is a queue, and I do not want to hold everyone up with a long question.
Kit | Your question deserves proper [[patient counseling::Patient counseling is the professional discussion needed to understand the instruction, not a hurried interpretation by an unauthorized technician.]]. Ravi has accepted it and is available. I will connect you with him; I am not authorized to interpret the instruction.
Arden | Where should I go? I want to know the person is expecting me and understands the question.
Kit | Ravi is at the [[consultation counter::The consultation counter gives Arden a specific location for the pharmacist who has accepted the question.]]. I will make clear that your question is about this auxiliary label, so the handoff includes the issue rather than only your arrival.
Arden | That helps. Does accepting the question mean somebody has already checked everything with me, or simply that Ravi is going to discuss it?
Kit | It is an [[accepted handoff::An accepted handoff confirms that Ravi will receive the question, not that the counseling discussion has already occurred.]], not a completed discussion. We should not record counseling as finished just because the question was passed on or a package reached the pickup counter.
Arden | The leaflet uses another phrase. I would like to understand how it relates to the label rather than choose an instruction myself.
Kit | Bring the [[patient information leaflet::The patient information leaflet is another information source the pharmacist can discuss in relation to the actual label and question.]] into the consultation question. Ravi can address the actual wording and context; I should not resolve an apparent difference by choosing an instruction for you.
Arden | There is a device with the package too. Could I ask about it in the pharmacist conversation?
Kit | Yes. A question about the [[administration device::An administration device relates to delivering the medicine and should be discussed within the appropriate pharmacist consultation and role.]] belongs in the appropriate consultation. I will not assume that recognizing the package means you have already been shown or understand the device.
Arden | I would prefer to ask the more personal part somewhere people in the queue cannot easily hear. Is that possible through the pharmacy's arrangements?
Kit | We can protect your [[privacy::Privacy means handling the personal question through appropriate discussion arrangements rather than exposing it to the queue.]]. I will tell Ravi that you would like a private discussion without announcing your question to everyone here.
Arden | Once Ravi explains it, I may need to repeat what I understood. Sometimes I say yes because I heard the words, but the meaning is still unclear.
Kit | That kind of [[teach-back::Teach-back checks the person's understanding so the professional can clarify the explanation; it is not proof of understanding from a simple yes.]] can help Ravi clarify the explanation. You can say what you understood and ask about anything that does not fit, rather than feel obliged to pretend.
Arden | Thank you. Please keep the original directions unchanged and connect me with Ravi. I want the meaning clarified, not a new instruction guessed at this counter.
Kit | No direction has been changed. We will distinguish the handoff from [[counseling completion::Counseling completion concerns the actual professional discussion, which must not be recorded merely because the referral or package handover occurred.]], and Ravi will address the question through the consultation. I will preserve the label reference and your request for a clear explanation.''',
    transfer_title='Hand off a storage-label question',
    transfer_setup='Patient Drew asks about storage wording. The technician cannot interpret it. Pharmacist Noor accepts the question and is available in the consultation area. No instruction is changed.',
    transfer='''Technician: "The question concerns the ___ wording." | storage | The supplied question concerns storage, not an invented change to dosing.
Patient: "The pharmacist who accepted it is ___." | Noor | Noor is the identified pharmacist who accepted the question.
Technician: "Please use the ___ area." | consultation | The pharmacist is available in the specified consultation area.
Technician: "The directions remain ___." | unchanged | The scenario explicitly states that no instruction has been changed.''',
))

BOOK['units'].append(unit(
    title='Private collection and contact preferences',
    scene='A neighbor at the counter',
    skill='Explain a private verification step without accusing the collector or disclosing a patient medication list.',
    brief='Pavel asks to collect a prescription for a neighbor. Technician Vera has not yet verified the collection arrangement under the pharmacy process. Pavel asks Vera to read the neighbor\'s medicines aloud so he can recognize the correct package. Lead pharmacist Maya is available to review the request privately. No pickup decision or contact permission has been established. The task is not to announce a universal ban on friends collecting prescriptions. Vera must protect information, avoid an improvised identity test, and give the request a clear next step.',
    cast='Pavel | Neighbor requesting collection\nVera | Pharmacy technician',
    culture=('Explain the process without implying wrongdoing', 'A verification question can sound like an accusation when a collector believes they are helping. Acknowledge that purpose, identify the unresolved arrangement, and name the person who can review it. Privacy is not a reason to shame someone publicly.'),
    a='''What is unresolved? | The collection arrangement under the pharmacy process | Whether friends are universally prohibited from collecting | Whether Pavel has committed an offense | Whether every medicine may be read aloud | The case establishes an unverified arrangement, not wrongdoing or a universal prohibition.
Who can review the request privately? | Lead pharmacist Maya | An unidentified person in the queue | Pavel acting alone | A delivery driver outside | Maya is the available pharmacist identified to review this request.
Which requested action should Vera avoid? | Reading the medication list aloud as an improvised identification test | Acknowledging Pavel's reason for coming | Explaining that review is needed | Connecting Pavel with Maya | Naming medicines publicly would reveal information without resolving the collection arrangement through the appropriate process.''',
    vocabulary='''collection arrangement | The agreed or permitted process for another person to collect an item. | verify the collection arrangement
designated collector | Person identified to collect on someone else's behalf. | confirm the designated collector
identity verification | Checking a person's identity using the applicable process. | complete identity verification
authority to collect | Basis on which a person may receive another person's prescription. | clarify authority to collect
professional judgment | Qualified assessment using relevant facts and applicable standards. | exercise professional judgment
reasonable inference | Conclusion supported by circumstances rather than certainty from a single claim. | make a reasonable inference
disclosure | Making information available to another person. | limit the disclosure
confidentiality | Duty to protect information from inappropriate access or sharing. | maintain confidentiality
patient preference | A person's expressed choice about care or communication. | record a patient preference
contact permission | Established basis for contacting or sharing through a particular person or channel. | verify contact permission
preferred channel | Communication method the patient has chosen where appropriate. | confirm the preferred channel
alternate contact | Another person or destination used when authorized and suitable. | verify an alternate contact
voicemail | Recorded message left when a call is unanswered. | check voicemail preferences
callback number | Number to use for a return call after appropriate verification. | verify the callback number
relationship claim | Statement that someone has a particular connection to a patient. | assess the relationship claim
pickup request | Request to receive a prepared prescription from the pharmacy. | review a pickup request
private review | Assessment conducted with appropriate protection from public hearing. | arrange a private review
public counter | Customer-facing space where other people may hear a conversation. | avoid details at the public counter
medication list | Record of medicines associated with a patient. | protect the medication list
relevant information | Details needed for the specific permitted purpose. | share relevant information
identity mismatch | Difference between identifying details that requires clarification. | resolve an identity mismatch
authorization record | Documentation relevant to permission for a specified action. | check an authorization record
third party | Person or organization other than the main parties to a matter. | verify a third-party request
verified destination | Contact address or number checked through the appropriate process. | use a verified destination''',
    precision='Identity, relationship, and authority answer different questions. Knowing a person is a neighbor does not by itself settle every disclosure. Nor does uncertainty create a universal ban on third-party collection. Apply the actual pharmacy process and qualified judgment.',
    precision_extra='US health-privacy guidance allows professional judgment in appropriate friend or family prescription pickups; it does not impose advance written authorization in every case. This exercise concerns a still-unresolved request, not a new legal rule for every pharmacy or country.',
    phrases='''Acknowledge the purpose | I understand that you have come to help your neighbor.
Name the unresolved step | We have not yet verified the collection arrangement.
Avoid an accusation | I am checking the arrangement, not accusing you of anything.
Protect the list | I cannot use a public reading of the medication list as an identification test.
Offer the next step | Maya can review the request privately.
Avoid a blanket ban | I am not saying friends can never collect prescriptions.
Separate identity and authority | Confirming who you are does not answer every collection question.
Keep the patient central | We need to handle the patient's information through the appropriate process.
Check the channel | We have not established permission to use that contact method.
Do not improvise a test | Please let us follow the pharmacy's verification process.
Limit the conversation | We can discuss the request without announcing medicine names here.
Clarify the decision status | A collection decision has not yet been made.
Refer the judgment | Maya can assess the relevant circumstances.
Protect contact details | I will not read out another person's contact information.
Make the handoff concrete | I will connect you with Maya and explain the unresolved collection request.
Close courteously | Thank you for waiting while we resolve this privately.''',
    notes='''Have not yet | States an unresolved step rather than a permanent refusal.
Not accusing | Repairs an interpersonal misunderstanding without abandoning verification.
As an identification test | Explains why the proposed disclosure is inappropriate.
Can review | Offers a practical next step without promising approval.
Not saying friends can never | Avoids turning a local uncertainty into a universal legal claim.
Relevant circumstances | Leaves professional judgment tied to actual evidence.''',
    d='''Pavel says, "So friends are never allowed to collect?" Which response is accurate? | That is not what I am saying; Maya can review this unresolved request privately. | Correct, every friend is prohibited everywhere. | Any claimed friendship automatically permits every disclosure. | We can settle it by announcing all the medicines. | The response distinguishes this unresolved request from a universal rule and gives a confirmed review route.
Which pair must remain distinct? | Knowing a person's identity and establishing the collection arrangement | A medicine name and a public announcement as identical actions | A claimed relationship and automatic unlimited access | A preferred channel and any convenient number | Identity alone does not determine every collection or disclosure decision.
What can Vera promise now? | Connection with Maya for private review | Approval of the collection | Disclosure of the medication list | Permission to contact any relative | Maya is available to review; the decision and contact permissions remain unestablished.
Which note is factual? | Neighbor collection requested; arrangement unresolved; referred to Maya privately. | Unauthorized stranger confirmed to be stealing medicines. | Written authorization is legally mandatory in every pickup. | Patient consented to every contact method. | The note records established events without inventing wrongdoing, legal requirements, or patient permission.''',
    dialogue='''Pavel | I am collecting for my neighbor. She asked me to stop here on my way home, but I do not know which package I need.
Vera | I understand. We need to verify the [[collection arrangement::The collection arrangement remains unresolved, so Vera names the process needing review rather than inventing approval or misconduct.]] through our process. I can ask lead pharmacist Maya to review your request privately.
Pavel | Could you just read out her medicines? I will probably recognize one of the names, and that would save us both some time.
Vera | I cannot use the [[medication list::The medication list contains patient information and should not be read publicly as an improvised identity test.]] as a public identification test. We can take the request forward without announcing those names to everyone at the counter.
Pavel | Are you suggesting that I am making this up? I am trying to do someone a favor, not ask for her entire medical history.
Vera | No. I am not accusing you. The [[pickup request::A pickup request records the action Pavel wants; its existence does not establish that the collection decision is complete.]] needs review, and Maya is available to handle it with you. I appreciate why you have come.
Pavel | Does that mean friends and neighbors are never allowed to collect, or just that you have not settled the arrangement for this visit?
Vera | It means this request is unresolved. I am not announcing a blanket ban. Maya can use the applicable process and [[professional judgment::Professional judgment applies relevant circumstances and rules; uncertainty does not justify inventing a universal ban on friend pickups.]] in reviewing it.
Pavel | I can tell you my name and explain the relationship. Is proving who I am the same thing as proving that I can collect?
Vera | Those are related but distinct. [[identity verification::Identity verification concerns who Pavel is; it does not independently resolve every question about receiving another person's prescription.]] addresses who you are. The appropriate review also needs to resolve the collection arrangement without using medicine names as a guessing game.
Pavel | Would calling her help? I have a number on my phone, but I do not know what contact details or preferences your pharmacy holds.
Vera | We should use the appropriate process for [[contact permission::Contact permission must be established through the actual process rather than assumed from a number offered by another person.]] and verified details. I will not assume that every number or channel offered at the counter is suitable.
Pavel | All right. I would also prefer not to explain the personal circumstances within hearing of the queue. Could we move the discussion somewhere appropriate?
Vera | Yes. Maya can provide a [[private review::A private review moves the unresolved request to an appropriate setting without promising that collection will be approved.]]. I will pass on the collection question without describing your neighbor's medicines or circumstances to the waiting customers.
Pavel | Please make sure she knows that I am here to collect, rather than telling her that I asked for permission to see every record.
Vera | I will keep the [[relevant information::Relevant information is limited to the actual request and unresolved arrangement, not an invented demand for unrestricted patient records.]] accurate: you requested collection for your neighbor, and we have not yet resolved the arrangement. That is the issue Maya will receive.
Pavel | Thank you. I can wait for that conversation. I mainly needed to know whether there was a next step instead of simply being turned away.
Vera | There is. We will protect [[confidentiality::Confidentiality requires appropriate protection of information while the request follows its proper review route, not public accusation or disclosure.]] while Maya reviews it. I cannot promise the outcome before that review, but I can connect you with her.
Pavel | Then please do that. I understand that you have not approved or refused the collection yet and that we should discuss the details privately.
Vera | Exactly. The [[authority to collect::Authority to collect is the unresolved basis for receiving the prescription; it must not be assumed from the request alone.]] will be addressed through the appropriate review. I will explain where the request stands and introduce you to Maya.''',
    transfer_title='Clarify an alternate contact request',
    transfer_setup='Collector Sam supplies a new telephone number. Contact permission is unverified. Pharmacist Ellis accepts the private review. No patient information has been disclosed.',
    transfer='''Technician: "The new ___ has not been verified." | telephone number | The supplied number needs verification through the actual contact process.
Collector: "Contact permission is still ___." | unverified | The facts do not establish permission to use this contact.
Technician: "Pharmacist ___ has accepted the review." | Ellis | Ellis is the pharmacist explicitly identified as the receiving owner.
Technician: "No patient information has been ___." | disclosed | The scenario states that patient information has not been disclosed.''',
))

BOOK['units'].append(unit(
    title='Precise inventory and quality queries',
    scene='AB41 is not AB14',
    skill='Read back product identifiers and distinguish an unverified stock match from a confirmed recall assessment.',
    brief='A fictional recall notice names lot AB41. The delivery record shows AB14, but nobody has checked the label on the stock itself. Technician Emil brings the discrepancy to pharmacist Maya, who owns the recall assessment. The team must compare the actual product and lot with the complete notice through its approved process. Neither affected-stock status nor patient exposure has been established. A different number in one record does not prove the shelf is clear. No disposal, release, patient-contact, or treatment decision is supplied.',
    cast='Emil | Pharmacy technician\nMaya | Lead pharmacist',
    culture=('Read identifiers, not impressions', 'A familiar-looking code can be misheard when colleagues are busy. Read the exact sequence, name the source, and ask for a read-back. Correcting AB41 to AB14 is a factual distinction, not a criticism of the other person.'),
    a='''Which source has not been checked? | The label on the actual stock | The delivery record showing AB14 | The notice naming AB41 | The identity of the assessment owner | The case explicitly states that the stock label has not been checked.
What can be concluded now? | A discrepancy needs assessment; affected-stock status is not established. | All stock is unaffected. | Every patient received recalled medicine. | The notice must be wrong. | The two records differ, but actual stock and full notice scope still need review.
Who owns the recall assessment? | Pharmacist Maya | Emil acting beyond the agreed process | The patient queue | An unidentified supplier driver | Maya is the named professional responsible for this assessment.''',
    vocabulary='''recall notice | Formal communication identifying a product problem and applicable actions. | review the recall notice
lot number | Identifier for a defined production group. | read back the lot number
batch | Defined quantity produced under a specified manufacturing process. | trace the batch
serial number | Identifier assigned to a particular individual item or package. | verify a serial number
product identifier | Code or set of details identifying a product. | match the product identifier
National Drug Code | US identifier commonly abbreviated NDC for a listed drug product. | compare the National Drug Code
manufacturer | Organization responsible for making a product. | confirm the manufacturer
expiration date | Date after which a product should not be used under its labeling. | check the expiration date
delivery record | Documentation of goods delivered to a location. | reconcile the delivery record
physical stock | Actual inventory present rather than entries in a system. | inspect the physical stock
stock reconciliation | Comparison of records with actual inventory to resolve differences. | complete stock reconciliation
traceability | Ability to follow product history and movement through records. | preserve traceability
quarantine | Controlled segregation or status preventing use pending an authorized decision. | apply the quarantine process
affected stock | Inventory confirmed to fall within the relevant notice or problem scope. | identify affected stock
recall scope | Defined products, lots, dates, or other limits of a recall. | establish the recall scope
disposition | Authorized decision about what happens to a product. | record the disposition
return authorization | Permission or reference required for an approved product return. | obtain return authorization
destruction record | Documentation that product was destroyed through the authorized process. | retain a destruction record
release decision | Authorized decision allowing stock to become available for its intended use. | document a release decision
patient exposure | Situation in which a patient received or used a relevant product. | assess patient exposure
first-expiry-first-out | Stock rotation using items with the earliest expiry first; often FEFO. | apply first-expiry-first-out
temperature excursion | Temperature outside specified storage limits. | report a temperature excursion
tamper evidence | Visible feature intended to show that packaging may have been interfered with. | check tamper evidence
quality defect | Product problem affecting conformity with relevant quality requirements. | report a quality defect''',
    precision='Lot, serial, and product identifiers are not interchangeable. A product code identifies the product category or configuration; a lot identifies a production group. The complete recall notice determines which details matter. A matching fragment is not the full assessment.',
    precision_extra='Quarantine, return, destruction, and release are different controlled actions. Use the actual notice and pharmacy procedures, not this language exercise as an operational instruction. Questions about a patient taking medicine belong with the appropriate professional; a recall is not universal advice to stop treatment.',
    phrases='''Name the document | The notice names lot AB41.
Read the second source | The delivery record shows AB14.
Read back precisely | That is A, B, four, one on the notice.
State the missing check | The actual stock label has not yet been checked.
Avoid premature clearance | The record difference does not establish that the shelf is unaffected.
Name the owner | Maya owns the recall assessment.
Compare the full scope | We need the complete product details and notice scope.
Separate records and stock | A delivery entry is not a physical-stock check.
Keep exposure unconfirmed | Patient exposure has not been established.
Protect traceability | Preserve the original references and the results of each check.
Avoid an invented disposition | No disposal or release decision has been supplied.
Follow the real procedure | Use the actual notice and the approved pharmacy process.
Report a mismatch | These identifiers differ; the reason is not yet known.
Keep actions distinct | Holding stock is not the same as destroying it.
Route clinical questions | A pharmacist must address questions about taking the medicine.
Close the record accurately | Record the findings and authorized decision when they are established.''',
    notes='''Shows versus confirms | A record shows an entry; confirmation requires the appropriate verification.
Not yet checked | Names the missing work without implying the result.
Four, one | Reads the actual sequence rather than a vague resemblance.
Has not been established | Prevents uncertainty from becoming either reassurance or an alarm.
Complete product details | Expands the comparison beyond one code fragment.
When established | Keeps later decisions out of the current factual record.''',
    d='''Which read-back preserves the notice code? | A, B, four, one | A, B, one, four | A, B, fourteen on both documents | A, B, forty-one on the delivery record | AB41 belongs to the notice; AB14 belongs to the delivery record.
Which statement overstates the evidence? | The shelf is clear because the delivery record shows a different lot. | The actual stock label has not been checked. | Maya owns the assessment. | Full notice scope must be compared. | A delivery entry alone does not prove which lot is physically present or whether stock falls within scope.
What should be preserved? | The source identifiers, actual findings, and authorized decisions | Only the newest number with the earlier one deleted | An assumed exposure conclusion | An invented disposal instruction | Traceability depends on accurate source references and a record of what was actually checked and decided.
Which patient-facing claim is unsupported? | Every recall means you should stop taking medicine immediately. | A pharmacist should address treatment questions. | The actual notice determines the relevant scope. | Patient exposure is not established here. | Treatment actions depend on the specific recall and professional advice, not a universal instruction invented from the word recall.''',
    dialogue='''Emil | Maya, I have a code discrepancy on the recall paperwork. The notice and delivery record look similar, but the final two characters are reversed.
Maya | Start with the [[recall notice::The recall notice is the source naming AB41; its identifier must remain distinct from the different delivery entry.]]. Read its lot exactly, then name the second source. We should not let a familiar-looking code substitute for an exact comparison.
Emil | The notice says A, B, four, one: AB41. The delivery record says A, B, one, four: AB14. I have not checked the shelf label.
Maya | The [[lot number::A lot number identifies the production group and must be read in the correct character order to support matching.]] on the notice is AB41; the record shows AB14. Thank you for separating them. The physical label is still an outstanding check.
Emil | Could I mark the stock unaffected because the delivery entry is different, or would that jump ahead of what we have actually verified?
Maya | It would jump ahead. The [[delivery record::The delivery record documents an entry but does not alone establish the identifier on the stock physically present.]] is one source. It does not establish which lot is on the shelf or complete the assessment against the notice.
Emil | Then I will not tell the counter team that the shelf is clear. What should I include when I describe the unresolved query?
Maya | Name both sources and the unchecked [[physical stock::Physical stock is the inventory actually present; checking it is distinct from reading a delivery entry.]]. Also identify me as the assessment owner so colleagues know where findings and questions must go.
Emil | The product has other identifying details as well. I assume the lot code alone is not a reason to skip the product and manufacturer comparison.
Maya | Correct. We need the complete [[recall scope::Recall scope defines the relevant products and limits; a single similar code does not replace the complete notice comparison.]] and applicable product details. Follow the actual notice and our approved process rather than infer the scope from two letters and two digits.
Emil | If we find a match, should I immediately describe it as proof that a patient received the affected product, or is that another question?
Maya | That is another question. [[Patient exposure::Patient exposure concerns whether someone received or used relevant product and is not established merely by an inventory query.]] has not been established. Stock findings and patient-related assessment must be recorded accurately without turning one into an unsupported conclusion about the other.
Emil | I will keep the original codes visible in the record. Correcting the summary should not erase the source that created the query.
Maya | Exactly. Preserve [[traceability::Traceability depends on retaining source references and verified findings so product history and decisions can be followed.]] through the source references and actual findings. Anyone reviewing the matter needs to see what was checked, what differed, and what remains unresolved.
Emil | I also want to avoid using hold, return, and destroy as if they were the same action. The required action depends on the actual instructions.
Maya | Yes. [[Quarantine::Quarantine controls availability pending an authorized decision; it is not automatically a return, destruction, or final release decision.]] and final disposition are distinct. Use the applicable process and notice; do not invent disposal or release instructions from this discrepancy.
Emil | If a patient asks whether to stop taking a medicine while we check this, I should connect that question with the appropriate pharmacist advice.
Maya | Correct. Do not turn an inventory query into a treatment instruction. An authorized [[disposition::Disposition is the decision about the product's handling; it does not authorize a technician to invent patient treatment advice.]] for stock and clinical advice for a patient are different matters.
Emil | My summary will say AB41 on the notice, AB14 in the delivery record, stock label unchecked, and assessment with Maya. No affected-stock conclusion yet.
Maya | That is accurate. The [[release decision::A release decision requires the authorized assessment and cannot be inferred from the differing delivery code alone.]] is not established either. Bring the verified findings through our process, and keep the pending status clear until the responsible decision is recorded.''',
    transfer_title='Read back a different lot discrepancy',
    transfer_setup='Notice lot CD27 differs from delivery entry CD72. Actual stock is unchecked. Pharmacist Noor owns the assessment. No affected-stock conclusion has been reached.',
    transfer='''Technician: "The notice names ___." | CD27 | CD27 is the notice identifier, not the different delivery entry.
Pharmacist: "The delivery entry is ___." | CD72 | CD72 is the delivery identifier and must not be transposed.
Technician: "The actual stock is still ___." | unchecked | No check of actual stock has yet been established.
Pharmacist: "The assessment owner is ___." | Noor | Noor is the explicitly named owner of this assessment.''',
))

BOOK['units'].append(unit(
    title='Corrected messages and shift handoffs',
    scene='Correcting a ready message',
    skill='Correct an inaccurate status promptly, acknowledge its effect, and hand over a named follow-up without promising collection.',
    brief='At 14:00, technician Jo told patient Asha that a prescription was ready after misreading a queue entry. At 14:10, Jo confirms that pharmacist review is still pending. Asha is already traveling to the pharmacy. Jo owns the correction call now and a status update at 16:00. No collection time is confirmed. Jo must clearly withdraw the earlier ready statement, explain the verified status, acknowledge the disruption, and preserve an accurate record. The team must distinguish an attempted call, successful contact, and a completed correction.',
    cast='Jo | Pharmacy technician\nAsha | Patient',
    culture=('Apologize with the corrected fact', 'A vague apology can leave the original message intact. State what was wrong and what is now verified before describing follow-up. Taking responsibility for a misread queue entry is more useful than blaming the system or defending the original wording.'),
    a='''What was wrong with the 14:00 message? | It said ready although pharmacist review was still pending. | It correctly guaranteed collection at 16:00. | It confirmed a patient had already collected. | It documented a completed correction call. | The ready statement was based on a misread queue entry and must be withdrawn.
Which time is an update commitment? | 16:00 | 14:00 as a new pickup slot | Any assumed arrival time | A guaranteed review completion time | Jo owns a 16:00 status update, not a guaranteed collection or review completion.
What must a handoff distinguish? | Attempted contact and a correction actually communicated | A queue entry and automatic readiness | An apology and a clinical decision | Travel already started and guaranteed supply | An attempted call does not establish that the patient received the corrected information.''',
    vocabulary='''queue entry | Item displayed in a workflow waiting for a processing step. | check the queue entry
workflow stage | Defined point within a sequence of work. | verify the workflow stage
status correction | Replacement of an inaccurate status with the verified one. | issue a status correction
ready notification | Message stating that an item is ready for collection. | withdraw a ready notification
pharmacist review | Professional review by the pharmacist within the dispensing process. | await pharmacist review
final check | Required final verification under the applicable dispensing process. | confirm the final check
in progress | Started but not completed. | mark the task in progress
pending | Awaiting an event, action, or decision. | show the review as pending
dispensed | Prepared or supplied through the relevant dispensing process; usage must be clear. | distinguish dispensed from collected
collected | Received by the person collecting the item. | record the item as collected
timestamp | Recorded time associated with an event or entry. | preserve the timestamp
contact attempt | Effort to reach someone without assuming contact succeeded. | record a contact attempt
successful contact | Confirmed communication with the intended person through the appropriate process. | document successful contact
message delivered | Information actually conveyed, not merely prepared or queued. | confirm the message was delivered
acknowledgment | Response showing receipt or recognition of information. | obtain acknowledgment
correction owner | Person responsible for communicating and recording a correction. | name the correction owner
update commitment | Promise to provide information at a stated time or trigger. | keep the update commitment
readiness estimate | Forecast of when an item may be ready, not confirmation. | qualify a readiness estimate
handoff record | Written account transferring relevant facts and responsibility. | complete the handoff record
open action | Task that remains unfinished. | assign the open action
closed-loop handoff | Transfer in which receipt and responsibility are confirmed. | use a closed-loop handoff
service recovery | Actions addressing a service failure and its effects. | support service recovery
audit trail | Preserved sequence showing events and changes to a record. | maintain the audit trail
verified status | State established through the appropriate check. | communicate the verified status''',
    precision='Ready, in progress, dispensed, and collected may appear close together in a system but describe different events. Use the pharmacy definitions and verified workflow state. Seeing an entry in a queue does not prove that review or release is complete.',
    precision_extra='A correction is not complete merely because someone drafted a message or attempted a call. Record the actual contact result and remaining action. Preserve the earlier event and correction in the appropriate record instead of silently rewriting history.',
    phrases='''Open the correction | I need to correct the ready message I gave you at 14:00.
State the verified position | Pharmacist review is still pending.
Take responsibility | I misread the queue entry and gave you an inaccurate status.
Apologize plainly | I am sorry that my message caused this disruption.
Withdraw the promise | Please do not rely on my earlier statement that it was ready.
Avoid a replacement guess | I cannot confirm a collection time now.
Define the update | I will provide a status update at 16:00.
Keep the distinction | That is an update time, not a pickup appointment.
Check receipt | Can I confirm that you received the corrected status?
Respect safe contact | Please respond only when it is safe and appropriate.
Record the actual outcome | Record whether contact succeeded and what was communicated.
Name the owner | I own the correction and the 16:00 follow-up.
Make the handoff explicit | Any transfer must include the open action and an accepting owner.
Preserve the earlier event | Keep the original message and the correction visible in the record.
Do not claim clinical completion | I cannot speak as though pharmacist review has finished.
Close with the next fact | The current status is pending review, with an update at 16:00.''',
    notes='''I need to correct | Signals that the earlier information must be replaced.
I misread | Takes responsibility without inventing a system fault.
Do not rely on | Explicitly withdraws the earlier claim rather than merely adding a vague caution.
Update time, not pickup | Prevents a new expectation from replacing the old mistake.
Whether contact succeeded | Separates effort from result in the record.
Accepting owner | Makes a shift handoff a confirmed transfer rather than a name in a note.''',
    d='''Which opening most clearly repairs the error? | I need to correct my 14:00 ready message: pharmacist review is still pending. | There might have been some confusion, but come anyway. | Everything is fine because I sent a message. | Ready probably means ready enough. | The response explicitly replaces the inaccurate statement with the verified pending status.
Which promise is supported? | Jo will provide a status update at 16:00. | The prescription will be ready at 16:00. | Review is guaranteed to finish before Asha arrives. | Asha has already received the medicine. | The supplied commitment concerns information at 16:00, not dispensing completion or receipt.
If the call is unanswered, what should the record show? | An attempted contact with the correction action still unresolved | A completed correction communicated to Asha | Asha's agreement to the revised status | A confirmed collection time | An unanswered call does not establish delivery or acknowledgment of the correction.
Which handoff is complete in principle? | Verified status, actual contact outcome, open follow-up, and accepting owner | A new name with no acknowledged responsibility | An erased original message | Only the word sorry | A closed-loop handoff preserves facts, outstanding work, and confirmed responsibility.''',
    dialogue='''Jo | Asha, this is Jo at the pharmacy. Is it safe and appropriate to speak now? I need to correct the ready message I gave you earlier.
Asha | I can speak. I am already traveling because your [[ready notification::The ready notification prompted travel, so the correction must explicitly replace that earlier claim rather than offer a vague apology.]] said I could collect. What has changed?
Jo | At 14:10 I checked the status and confirmed that pharmacist review is still pending. I misread the queue entry when I spoke to you at 14:00.
Asha | Then the [[verified status::The verified status is pending pharmacist review, not ready for collection; it replaces the earlier inaccurate message.]] is that it is not confirmed ready. I need you to say that clearly because I arranged my afternoon around collecting it.
Jo | Yes. Please do not rely on my earlier ready statement. I am sorry that my inaccurate message caused this disruption. I cannot confirm a collection time now.
Asha | Can you explain the difference between seeing it in the system and knowing it has completed [[pharmacist review::Pharmacist review is the outstanding professional step and must not be represented as complete merely because a queue entry exists.]]? That seems to be where the message went wrong.
Jo | I treated a queue entry as though it established readiness. It did not. I should have checked the actual stage before giving you a collection message.
Asha | I appreciate you owning the mistake. What is the [[update commitment::The update commitment concerns a 16:00 status report; it is not a replacement guarantee that collection will be possible then.]] now, and does that tell me when I can collect?
Jo | I own the correction call now and a status update at 16:00. That is a time for information, not a confirmed pickup appointment or promise that review will be complete.
Asha | Then please do not describe 16:00 as a [[readiness estimate::A readiness estimate forecasts availability, whereas the only supplied 16:00 commitment is to report status.]] if you do not have evidence for one. I would rather have an honest status than another trip based on a guess.
Jo | Agreed. I cannot supply a readiness time. At 16:00 I will report the verified position, including anything still pending, rather than turn the update into another collection promise.
Asha | Will the record show that you actually reached me? I would not want a later colleague to confuse an attempted call with [[successful contact::Successful contact means the communication actually reached the intended person, unlike an unanswered call or prepared message.]] and assume I had been told.
Jo | Yes. I will record the actual contact result and the corrected information communicated through our process. An unanswered call would not mean that the correction had reached you.
Asha | If someone else takes over later, I want the [[open action::The open action is the unfinished follow-up and must remain visible with an owner rather than disappear at a shift change.]] to stay visible. Otherwise I may need to explain the entire problem again.
Jo | I remain responsible for the follow-up. If a transfer becomes necessary, it must include the verified status, what I communicated, the outstanding action, and a colleague who accepts responsibility.
Asha | That sounds like a [[closed-loop handoff::A closed-loop handoff confirms receipt and ownership, not merely a note naming someone who may never have accepted the task.]], rather than leaving a name in the system and hoping they notice.
Jo | Exactly. I will also preserve the original message and its correction appropriately. We should not erase the earlier event and leave a record that suggests the error never occurred.
Asha | Keep the [[audit trail::The audit trail preserves the original event and subsequent correction so later reviewers can understand the sequence accurately.]]. I have received the correction: review is pending, there is no collection time, and you will update me at 16:00.
Jo | That is correct. Thank you for confirming receipt. I am sorry for the disruption. I will keep the follow-up assigned and communicate the verified status at the agreed time.
Asha | All right. Please make the [[status correction::The status correction replaces the inaccurate ready statement while preserving the pending review and the separate follow-up commitment.]] clear to anyone handling my enquiry, so the original ready message is not repeated when I next contact the pharmacy.''',
    transfer_title='Correct a queued message',
    transfer_setup='At 10:05, technician Erin discovers an inaccurate ready message prepared for patient Leo. It has not been sent. Review is pending. Erin owns correcting the queued message before release.',
    transfer='''Erin: "The inaccurate message has not been ___." | sent | The message is prepared but has not reached the patient.
Colleague: "The verified review status is ___." | pending | Review remains pending, so readiness must not be asserted.
Erin: "The correction owner is ___." | Erin | Erin explicitly owns correcting the queued message before release.
Colleague: "Correct it before message ___." | release | The message must be corrected before it is released to the patient.''',
))
