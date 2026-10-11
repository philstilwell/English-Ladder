"""Original home-care conversations about money, access, and communication."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Count the change together",
        skill="Explain a shopping-money discrepancy, reconcile it openly, and record the actual return without blame.",
        setup="Authorized shopping: $50 provided, $34.70 total agreed purchases, $13.30 initially counted remaining. Fictional process: keep client money separate, retain itemized receipts, reconcile together, record the actual return. No tips or personal purchases are permitted. Mrs. Silva and worker Niko check the money together.",
        cast="Mrs. Silva|Client\nNiko|Care worker",
        dialogue="""Niko|Here is your shopping, Mrs. Silva. Can we check the receipt and change together? I have spotted a difference in my first count.
Mrs. Silva|Yes. We recorded fifty dollars before you left. Please use the [[cash record::The cash record starts with the fifty dollars actually handed over; it provides a shared basis for checking spending and money returned, rather than relying on memory.]] beside my shopping list, so we are both starting from the same amount.
Niko|The agreed items total thirty-four seventy, including all charges. No personal purchases are included, and I kept your money separate.
Mrs. Silva|Let me see the [[itemized receipt::The itemized receipt identifies the purchases and their charges; the total of 34.70 must relate to the agreed shopping rather than an unexplained deduction from the client's cash.]]. I want to check each purchase, not just the amount left over.
Niko|Of course. Fifty minus thirty-four seventy means fifteen thirty should remain. I have counted thirteen thirty so far, which is two dollars less than expected.
Mrs. Silva|The expected [[change::Expected change is fifty dollars less 34.70 spent, or 15.30; that calculation does not establish that the full amount has already been returned.]] is fifteen thirty. Please do not ask me to sign for that amount before it is checked and returned.
Niko|I will not. I will recount the separate shopping pouch here with you. A difference needs checking and, if unresolved, reporting through our money-handling procedure.
Mrs. Silva|Thank you. Calling it a [[shortfall::The initial shortfall is two dollars between expected change of 15.30 and the 13.30 counted; it identifies a discrepancy without proving theft or its cause.]] does not tell us why it happened. Let us check the receipt and pouch before anybody starts accusing someone.
Niko|There is a two-dollar coin inside the folded receipt. With that included, the full amount is fifteen dollars and thirty cents. Would you count it with me again?
Mrs. Silva|I count fifteen thirty too. The [[reconciliation::Reconciliation shows that 34.70 in supported purchases plus 15.30 in returned change equals the original fifty; finding the coin resolves this specific difference.]] now balances: purchases and returned money add back to the fifty I gave you.
Niko|I will record the actual amount returned and the check we completed. The first count was short, but the final count is not; both should be described accurately if required by our process.
Mrs. Silva|That is fine. I would rather hear about a count being checked than find a tidy record that says something different from what actually happened.
Niko|Please check the items against our list too. Correct change would not make an unapproved purchase acceptable.
Mrs. Silva|The items match. You can put the change in my usual envelope now. I know you cannot keep a little of it as a tip under this arrangement.
Niko|Thank you. I will return all of it. Your shopping money is not available for my travel expenses or a personal purchase unless a different, properly authorized arrangement explicitly covers that.
Mrs. Silva|If a number was already entered incorrectly, please make a traceable [[correction::A traceable correction preserves the relevant original entry and identifies the actual change under the recording process, instead of concealing the discrepancy or recording money never returned.]]. Do not ask me to confirm the original figure just to make the sheet easier to finish.
Niko|Agreed. The record should show what you actually received, with the receipt attached through our approved process. I will not sign on your behalf or invent your confirmation.
Mrs. Silva|And if we had not found the coin, we would record the amount present and notify the office, rather than quietly call the missing money a fee.
Niko|Exactly. We would follow the discrepancy procedure promptly and keep the facts clear. I would not conceal it or make a private repayment arrangement to bypass that process.
Mrs. Silva|Then we agree: fifty provided, thirty-four seventy spent, fifteen thirty returned, and the initial two-dollar difference resolved by the recount. Thank you for checking with me.""",
        transfer_title="Reconcile a second shopping trip",
        transfer_setup="A client provides $30. Authorized shopping costs $22.40 in total. The worker initially counts $5.60 remaining, then finds a separate $2 coin in the client's shopping pouch. All change is checked and returned; no fees or other spending apply.",
        transfer="""Client: The authorized purchases total $___ .|22.40|The supplied receipt total is twenty-two dollars forty, with no extra fees or spending to add.
Worker: The initial count was short by $___ .|2|The expected seven dollars sixty exceeds the initial five dollars sixty by two dollars.
Client: The coin brings the returned amount to $___ .|7.60|The initial five dollars sixty plus the located two-dollar coin totals seven dollars sixty returned.
Worker: Purchases plus returned change reconcile to the original $___ .|30|Twenty-two dollars forty spent plus seven dollars sixty returned equals the original thirty, with no other charges.""",
        reference=("SCIE: financial-abuse indicators and the importance of accurate financial records", "https://www.scie.org.uk/safeguarding/adults/introduction/types-and-indicators-of-abuse/"),
    ),
    scenario(
        title="Ask how to communicate",
        skill="Adapt the exchange to a person's stated hearing and information needs, then check a concrete misunderstanding respectfully.",
        setup="Mr. Bell has hearing loss. He prefers face-to-face clear speech and a large-print note. The television is on; his niece is visiting. Confirmed appointment: 17 November, 14:15; pickup 13:30. He wants to discuss it himself. No new information-sharing permission is supplied.",
        cast="Mr. Bell|Client\nAnika|Care worker",
        dialogue="""Anika|Mr. Bell, I have the confirmed appointment details. Is now a good time to discuss them, and what would make the conversation easier for you?
Mr. Bell|Please face me and speak clearly at your usual volume. That is my [[communication preference::The communication preference comes from Mr. Bell himself; hearing loss does not establish that shouting, written-only communication, or speaking to a relative would meet his needs.]]. Shouting from the doorway makes the words harder to follow, not easier.
Anika|Would you like the television turned down while we talk, or would something else help?
Mr. Bell|Yes, please lower the [[background noise::Background noise from the television is an identified barrier in this conversation; Mr. Bell agrees to reducing it rather than the worker changing his surroundings without asking.]]. Sit where I can see your face. You do not need to lean over me or use a childish tone.
Anika|Thank you. The appointment is on November seventeenth at two fifteen in the afternoon. The confirmed pickup is one thirty that afternoon, forty-five minutes before it.
Mr. Bell|That [[plain language::Plain language expresses the confirmed times in understandable everyday wording; it does not omit the date or blur pickup time with appointment time.]] helps. Please give me one detail at a time. I heard the seventeenth, but was the car coming at two thirty?
Anika|The car is coming at one thirty, not two thirty. I may have given you the two times too quickly. The appointment is later, at two fifteen.
Mr. Bell|Let me give a [[read-back::The read-back checks the specific date and times, allowing correction without treating a general yes or nod as proof that every detail was heard accurately.]]: November seventeenth, pickup at one thirty, appointment at two fifteen. Have I got those in the right order now?
Anika|Yes, that is exactly right. Would a large-print note with separate lines for date, pickup, and appointment help you check it again later?
Mr. Bell|Yes, [[written confirmation::Written confirmation in the requested large-print format supports Mr. Bell's access to the details; providing any written text would not necessarily meet his stated need.]] in large print, please. Correct information in tiny writing is still hard for me to use.
Anika|I will use the approved format and check that you can read it comfortably. My usual template may not meet your needs.
Mr. Bell|My niece sometimes answers for me. She means well, but please keep asking me first. I can explain what I want once I have heard the question.
Anika|Of course. A communication barrier is not a reason to stop involving you. We can ask about support you want from somebody else without making them your automatic spokesperson.
Mr. Bell|And ask for my [[consent::Consent to involve another person or share relevant information must follow the actual process; a visiting relative's presence does not automatically establish unlimited permission.]] before adding her to a discussion about my personal information. Her being in the house does not mean every conversation is for her.
Anika|I will follow the relevant permission process. For this appointment discussion, you have asked to speak directly, and we can check together what support is helpful.
Mr. Bell|Please put the communication details in the appropriate record too. I am tired of having to explain the same preferences to every new worker.
Anika|I will record the agreed needs through our approved system so the relevant team can use them. The entry should describe what helps, not label you uncooperative when a message is unclear.
Mr. Bell|That sounds right. You can check with me again if the arrangement stops working. I might need something different in a noisier place or for a longer discussion.
Anika|Agreed. We should review the support with you rather than treat today's note as fixed forever. Here is the large-print confirmation; can we check its date and two time lines together?
Mr. Bell|Yes: seventeenth of November, one-thirty pickup, two-fifteen appointment. Those are clear, and the note is readable. Please leave it in the place we agreed.""",
        transfer_title="Correct the timing without taking over",
        transfer_setup="Ms. Grant asks for clear speech and a large-print note. Confirmed appointment: 6 June at 11:00; pickup 10:15. She repeats pickup 11:15. She wants to discuss the details herself; a relative's presence does not establish information-sharing permission.",
        transfer="""Worker: The confirmed pickup is ___, not 11:15.|10:15|The supplied pickup time is ten fifteen, forty-five minutes before the eleven-o-clock appointment.
Client: The appointment date is ___ .|6 June|The stated date is the sixth of June; no other date is supplied or authorized by the exercise.
Worker: The requested note format is ___ .|large print|Ms. Grant specifically requests large print, so written information alone does not establish that the format meets her need.
Client: Please address the discussion to ___ .|me|She asks to speak for herself; the relative's presence does not automatically transfer the conversation or confer disclosure permission.""",
        reference=("NHS England: Accessible Information Standard, updated 2025", "https://www.england.nhs.uk/long-read/accessible-information-standard-requirements-dapb1605/"),
    ),
    scenario(
        title="No answer at the door",
        skill="Report a failed contact precisely and obtain an active welfare response without recording an unprovided visit as complete.",
        setup="At 08:00, Elena reaches Ms. Webb's home; agreed bell and telephone attempts get no answer. At 08:04 she calls coordinator Ben from a safe place. A no-answer procedure applies; Elena has no entry authorization. No welfare assessment or confirmed absence has occurred.",
        cast="Elena|Home care worker\nBen|Duty coordinator",
        dialogue="""Elena|Ben, I reached Ms. Webb's home at eight. The agreed bell and telephone attempts got no answer. I am calling from a safe place.
Ben|Report received at eight oh four: [[no response::No response describes the unsuccessful contact attempts; it does not establish that Ms. Webb is away, has refused care, or has been assessed as safe.]], not client out or care refused. We will follow her no-answer procedure now.
Elena|I have not seen or spoken with her. A light is visible through the window, but I cannot establish whether she is inside or how she is.
Ben|Keep that [[observation::The visible light is an observation, not proof of presence or wellbeing; the report should separate what Elena can see from conclusions she cannot support.]] separate from a conclusion. I am checking the plan's response and contacts now, while you remain connected. This is not just a routine queued message.
Elena|There is no entry authorization in my assignment. I will not try a window or ask a neighbor for a spare key as an improvised way in.
Ben|Follow the stated [[access arrangements::Access arrangements define the authorized entry process in the actual plan; an unanswered visit does not itself authorize forced entry, a borrowed key, or an improvised method.]]. Do not put yourself at risk. If immediate danger or an emergency becomes apparent, use the local emergency route without waiting for our routine process.
Elena|A neighbor says Ms. Webb might have gone out earlier. I have not verified that, and I have not shared her care details with them.
Ben|Record it as an [[unverified account::The neighbor's suggestion is attributed but unconfirmed; it should not replace direct contact or the prescribed welfare response, nor justify unnecessary disclosure of care details.]], if relevant to the procedure. It is useful context, not confirmation that she is away or that today's support is unnecessary.
Elena|My next visit is due soon. Please coordinate that schedule too, so this concern is not left open while I rush elsewhere.
Ben|I will coordinate your onward schedule and the [[welfare response::The welfare response is the active action required by the person's no-answer plan; managing the worker's next visit does not establish that this client's situation is resolved.]] separately. Receiving your call does not close this concern; I will confirm the next step.
Elena|Who is handling the next contact? I need a named person, not an unanswered office message.
Ben|I am coordinating it now under the plan and will document that ownership. I will use the designated contact and escalation route, rather than presume any relative is available to check.
Elena|For the visit record, I will enter actual arrival and contact attempts. None of the planned support has been provided, so I should not select completed care.
Ben|Exactly. [[Visit status::Visit status must distinguish arrival, attempted contact, and support actually delivered; a worker reaching the property does not mean the scheduled care tasks were completed.]] needs to remain accurate. Follow the service's recording process without inventing a refusal or recording the planned tasks as done.
Elena|If a named contact says they spoke to her, should we record their report separately from my observation?
Ben|Yes. Keep the source and time attached. We must assess what the information establishes and continue the appropriate procedure, rather than rewrite your earlier no-answer report as a personal welfare assessment.
Elena|And if I hear or see something that indicates an emergency while we are arranging the next step, I should act through that route immediately.
Ben|Yes. Do not wait for a scheduled callback in an emergency. Give the local responder the location, what you actually observed, and your contact details, following their instructions within your role.
Elena|Then my read-back is: no direct contact, no care delivered, no confirmed absence, and you are actively coordinating the no-answer response and my onward schedule.
Ben|Correct. Keep those statuses distinct. I will give you the plan's next instruction now and record the action and follow-up; this concern remains open until the appropriate response establishes otherwise.""",
        transfer_title="Arrival does not prove completed support",
        transfer_setup="At 16:00, worker Amir reaches a client but receives no answer through the agreed contacts. At 16:03 he reaches the duty coordinator. No entry, care, or welfare assessment has occurred. A neighbor's suggestion that the client is visiting family is unconfirmed. The actual no-answer procedure applies.",
        transfer="""Worker: My actual arrival was at ___ .|16:00|The worker reached the property at sixteen hundred; the later time identifies coordinator contact, not arrival.
Coordinator: The neighbor's explanation remains ___ .|unconfirmed|A suggestion about visiting family has not been verified and cannot establish the person's whereabouts or welfare.
Worker: The planned care has not been ___ .|delivered|No entry or care occurred, so reaching the address cannot be recorded as providing the scheduled support.
Coordinator: Follow the no-answer procedure, without delaying an ___ response if required.|emergency|An urgent emergency route remains available when circumstances require it; routine coordination must not be used as a reason to wait.""",
        reference=("NICE NG21: individualized care planning and prompt response to missed visits", "https://www.nice.org.uk/guidance/ng21/chapter/recommendations"),
    ),
]
