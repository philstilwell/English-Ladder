"""Twenty-four original short pediatric conversations."""
from books.pediatricians_content import BOOK
from books.medical_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], """
The child gets the first explanation | A clinician invites a child's account before the caregiver adds detail. | Pediatrician | Child
I will ask your caregiver for details too, but first I want to hear what you noticed.
I thought only the adult was supposed to answer because they made the appointment.
Your account matters. You can describe the feeling without knowing a medical word.
Sometimes I say sore, but I mean something different from what my caregiver understands.
Then we should ask what sore means to you rather than assume the meaning.
I can describe when it happens, although I do not remember every day.
That is useful. We will keep uncertainty visible instead of asking you to guess.
Can I correct the summary if it does not sound like what I said?
Yes. Checking my understanding is part of the conversation, not a test of you.
Then I can speak first without feeling that a different adult account makes me wrong.

Two settings explain two accounts | A clinician clarifies a caregiver's observation. | Caregiver | Pediatrician
The teacher says the child struggles during class, but I do not notice the same thing at home.
Those accounts may cover different settings and demands rather than directly contradict each other.
I worried that one report must be inaccurate if the descriptions differ.
We should clarify what each person observed, when, and during which activities.
The teacher's message does not include how often the difficulty occurred.
Then frequency remains unknown; we should not turn one example into an everyday pattern.
Could the child explain the classroom experience in their own words as well?
Yes. Their account belongs alongside the adult observations, with the source of each clear.
We can collect the relevant information without assigning a diagnosis from the difference alone.
Exactly. Context and source matter before a clinical conclusion is drawn.

How long and how often are separate | A clinician checks a child's symptom description. | Pediatrician | Child
You said the feeling happens a lot. Are you describing how often it occurs or how long it lasts?
I meant that it returns several times, not that each episode lasts all day.
Thank you. Those are different details, so I will keep them separate.
I do not know the exact number, and I do not want to invent one.
You can describe what you remember and say which part is uncertain.
Would it help to explain one recent episode instead of trying to count everything?
Yes. A concrete example can clarify the sensation, timing, and effect.
I also want to say what I could still do during it.
That describes functional impact without assuming that every episode stops every activity.
Then the history can be specific even when I cannot supply an exact count.
""")
LESSONS['module-2'] = short_lesson(BOOK['units'][1], """
The percentile is not a target | A caregiver asks whether a higher number is always better. | Caregiver | Pediatrician
My child is not near the top of the growth chart. Should we aim for the highest percentile?
A percentile is a comparison position, not a grade or a universal target.
I thought a higher number always meant healthier growth.
We need the actual pattern, measurement quality, and clinical context rather than that shortcut.
Does the current point tell you how the child has changed over the past year?
Not by itself. Earlier reliable measurements help us understand the trajectory.
I would like the explanation to avoid describing my child as failing a score.
That is appropriate. The chart supports assessment; it does not grade the child.
Can we review what this particular measure compares before discussing the pattern?
Yes. Naming the measure and reference makes the rest of the explanation clearer.

A copied measurement looks like a sudden change | A clinician checks an unusual chart entry. | Pediatrician | Caregiver
This point differs from the surrounding entries, so we should verify the original measurement.
Could it be a copying error rather than a true change?
That is possible, but we should check rather than assume either explanation.
I have the earlier clinic record, although I do not know how the measurement was taken.
The date, method, units, and original entry may help clarify the comparison.
We should not diagnose a growth problem from a potentially incorrect copied number.
Correct. The actual clinical assessment needs reliable information.
If the entry is corrected, will the history of the change remain clear?
It should follow the approved record process, with the verified source identified.
Then the chart can be interpreted after the data question is resolved, not before.

Rate and position answer different questions | A caregiver asks about growth velocity. | Caregiver | Pediatrician
The percentile is one number, but the report also mentions growth velocity. Are they interchangeable?
No. The percentile describes a comparison position; velocity describes change over time.
Could two children share a percentile today but have different growth histories?
Yes. A single shared position does not mean their trajectories are identical.
Then we need the time between measurements to understand the rate.
Exactly, along with appropriate measurement quality and the actual clinical context.
I do not want to compare my child with another using one isolated screenshot.
That comparison could leave out important information about timing and the reference used.
Could you explain the reviewed pattern without implying that the highest percentile is the goal?
We should. A clear explanation separates comparison, rate, and the individual assessment.
""")
LESSONS['module-3'] = short_lesson(BOOK['units'][2], """
A screen-positive result is not a diagnosis | A caregiver asks what a questionnaire establishes. | Caregiver | Pediatrician
The form flagged a concern, and I thought that meant a diagnosis had already been made.
Screening identifies a reason for further assessment; it does not settle the diagnosis by itself.
Does that mean we should ignore the result because it is not definitive?
No. It informs the next step, which we should explain clearly.
I want to know what the assessment will explore rather than receive a label without context.
The actual pathway considers relevant history, observations, and appropriate evaluation.
Could you also explain who checks whether the referral has been received?
We should identify that responsibility and distinguish receipt from a booked appointment.
Then the concern has a concrete next step without a promised diagnostic outcome.
Exactly. Neither a guarantee of normality nor a premature diagnosis would be appropriate.

Not yet acquired and lost are different | A clinician clarifies a developmental history. | Pediatrician | Caregiver
When you say the skill is missing, was it previously present and then lost?
No. I mean the child has not yet shown it, not that it disappeared.
Thank you. Delayed acquisition and regression describe different histories.
I had used the word regression because I thought it meant any developmental concern.
We should correct the meaning without assuming a cause from either term.
Could the record distinguish what I saw from what another caregiver reported?
Yes. The source and circumstances of each account should remain clear.
I also want the child's abilities in different settings included.
That context belongs in the actual assessment rather than a conclusion from one word.
Then the referral can carry an accurate history instead of a label I used incorrectly.

More than one language belongs in the history | A caregiver asks how multilingual experience is considered. | Caregiver | Pediatrician
The child uses different words with different relatives, and I worry the form counted only English.
We need an accurate account of the languages heard and used across settings.
Does speaking more than one language automatically explain every communication concern?
No. It should be considered properly, not used as a universal explanation.
I can describe understanding in one language and expression in another.
That helps distinguish receptive and expressive abilities rather than count only one kind of response.
Could qualified language support help us describe the history accurately?
Yes, where needed, so a language barrier does not distort the assessment.
I do not want abilities ignored or a diagnosis assumed from multilingual exposure alone.
Neither would be appropriate. The actual developmental evaluation needs the relevant full context.
""")
LESSONS['module-4'] = short_lesson(BOOK['units'][3], """
After does not prove because of | A caregiver asks about an event following vaccination. | Caregiver | Pediatrician
A symptom occurred after the vaccination, so I assumed the vaccination definitely caused it.
The timing matters, but sequence alone does not establish the cause.
I do not want that distinction used to deny that the symptom happened.
It should not be. We can acknowledge the event while reviewing its explanation.
What information would help the actual assessment?
The product record, timing, symptoms, and relevant clinical history need appropriate review.
I cannot remember every detail, so I would rather say unsure than invent it.
That is more accurate than adding false precision to the account.
Then we can discuss today's recommendation without automatically copying a conclusion from the earlier event.
Yes. The current decision needs the actual history and applicable clinical guidance.

A specific worry instead of a label | A clinician invites a focused vaccine question. | Pediatrician | Caregiver
Which part of the recommendation worries you most?
I am worried about the previous reaction, not opposed to every possible vaccination.
That distinction matters, and I will not replace your concern with a broad label.
I want the benefit and possible harm explained using the actual product information.
We should discuss those in context rather than promise zero risk.
Could you also explain what is known and what remains uncertain about the earlier event?
Yes. A clear account separates an observed event from a confirmed causal reaction.
I would like time to ask a focused question before deciding.
Questions belong in an informed discussion, with actual timing and clinical requirements explained.
Then the conversation can address the concern instead of turning it into an argument about my character.

An unclear record does not prove a missed dose | A caregiver brings an outside vaccination record. | Caregiver | Pediatrician
This outside record has an abbreviation I cannot read. Does that mean the dose was missed?
An unclear entry does not establish either that it was given or that it was missed.
We should ask the originating service to clarify rather than fill in the history by guesswork.
Exactly. The actual administration record needs verification.
Could a catch-up plan be selected before that uncertainty is resolved?
Any plan requires the relevant clinical review and current guidance, not an assumption from the unclear entry.
I also want the date and product checked, not only the presence of a mark.
Those details can matter to interpreting the record accurately.
Then we can keep the entry unverified while the appropriate clarification is obtained.
Yes. Unknown should remain unknown until the supporting information is available.
""")
LESSONS['module-5'] = short_lesson(BOOK['units'][4], """
The same brand name does not verify concentration | A caregiver compares two bottles. | Caregiver | Pediatrician
The new bottle has a familiar brand name. Can I assume the old volume instruction still applies?
We need the actual current product, concentration, and verified prescription instructions.
I thought matching the name was enough to establish the same amount per milliliter.
That assumption can be unsafe; the real label must be checked.
I will not convert the amount myself from a remembered instruction.
Any dose and volume need verification with the responsible prescribing or dispensing team.
Could the pharmacist also check that the measuring device matches the instruction?
Yes. The actual product, label, and appropriate device belong together.
Then this discussion is about resolving the information, not calculating a new dose.
Correct. No dose or administration instruction should be invented from this conversation.

Milligrams and milliliters name different quantities | A clinician checks the caregiver's understanding of units. | Pediatrician | Caregiver
Please explain what you understand by milligrams and milliliters.
Milligrams describe drug mass, while milliliters describe liquid volume.
Good. What connects the two for a particular liquid product?
The actual concentration, which needs to be verified rather than guessed.
That distinction prevents the same number from being copied between different units.
I also understand that an ordinary kitchen spoon is not a reliable measuring device.
We should use the appropriate device specified for the actual verified instruction.
Could you check the markings with me after the label is confirmed?
Yes. A demonstration can check my explanation and the suitability of the tool.
Then understanding the units does not authorize me to invent a dose from incomplete information.

Two caregivers need one verified instruction | A clinician addresses conflicting home medicine messages. | Caregiver | Pediatrician
One caregiver remembers a different instruction from the one on the current label.
We should resolve that conflict with the responsible team before treating either memory as definitive.
I do not want the two caregivers to alternate between incompatible instructions.
Correct. A consistent plan needs the actual product and verified current direction.
Could we document which instruction is superseded once the review is complete?
The approved record and communication process should make that clear.
Both caregivers need the corrected explanation, not only the person who attended today.
With the appropriate permissions, we should confirm how the information reaches each responsible person.
Then a resolved prescription question also needs a completed communication step.
Exactly. Internal agreement is not enough if conflicting instructions remain in use at home.
""")
LESSONS['module-6'] = short_lesson(BOOK['units'][5], """
Private time is not a promise about every record | A teenager asks about confidentiality. | Teenager | Pediatrician
If my caregiver leaves the room, does that mean nobody can ever see what we discuss?
Privacy in the room and access to records are separate questions.
I want the limits explained before I share something sensitive.
We should discuss the actual confidentiality rules, safety duties, and communication arrangements first.
The portal account may be shared, so I do not want assumptions about who reads messages.
We need to verify the access settings rather than promise that every entry is hidden.
Could billing or letters create a different privacy issue?
They can have separate arrangements, which the service should explain accurately.
Then I can understand the boundaries without being told either that everything is secret or nothing is private.
Exactly. The explanation should be specific to the actual setting and applicable requirements.

A shared phone needs a contact check | A teenager corrects the listed communication route. | Teenager | Pediatrician
The telephone number in the record is shared with my caregiver.
Thank you for telling me. We should not assume messages to it are private.
I would prefer another route, but I do not know whether the clinic can provide it.
We need to verify the available arrangements rather than promise a method before checking.
Does asking for a private route automatically change every existing access permission?
No. Contact preference, portal access, and legal permissions are separate matters.
I want to know what is actually confirmed before a sensitive message is sent.
That is appropriate. We will explain the verified route and any relevant limitation.
Please record the preference without describing it as a completed technical change.
We should distinguish requested, arranged, and verified so the next clinician understands the status.

Safety limits need a clear explanation | A clinician explains why absolute secrecy cannot be promised. | Pediatrician | Teenager
I want to explain the relevant safety limits before asking you for sensitive information.
I appreciate that. I would rather understand them now than discover an exception afterward.
The actual duties depend on the setting and applicable rules, which we need to describe accurately.
Does that mean you will automatically share every personal concern with everyone?
No. We should explain the particular circumstances and appropriate information-sharing process.
I also want support if something does need to be shared.
We should explain what happens and involve you appropriately while following the actual duties.
A private conversation can still be useful even when confidentiality has defined limits.
Yes. Clear limits support informed participation rather than making the discussion pointless.
Then we can continue without a promise that neither of us can reliably interpret.
""")
LESSONS['module-7'] = short_lesson(BOOK['units'][6], """
The school has an older plan | A school nurse checks a document version. | School nurse | Pediatrician
The plan in our record is older than the version the family mentioned.
We need to verify the current clinician-approved document before assuming the instructions are unchanged.
I will not replace a dose from a verbal recollection or an incomplete photograph.
Correct. The actual plan and relevant permissions must be checked.
Could the current version be sent through the authorized route to the designated contact?
Yes, with the appropriate sharing arrangements and confirmation of receipt.
Receiving the file does not yet establish that staff are ready to implement it.
That distinction matters. Practical preparation and responsibilities need their own confirmation.
I will identify any outstanding arrangement rather than mark everything complete when the attachment arrives.
Then the school and clinical team will share an accurate picture of readiness.

A field trip changes practical arrangements | A school nurse discusses an off-site activity. | School nurse | Pediatrician
The student has a school plan, but the field trip uses different staff and transport.
We should check the actual off-site arrangements rather than assume the classroom setup transfers unchanged.
The family wants participation supported without an automatic exclusion.
That goal belongs in the discussion, alongside the actual clinical and school requirements.
We need to clarify who is authorized for the relevant tasks during the trip.
Yes. A plan's existence does not automatically assign responsibility to every accompanying adult.
I will not invent medicine instructions to fill a gap in the preparation.
Any clinical instruction must come from the verified plan and responsible team.
Once the arrangements are checked, we should confirm them with the appropriate people.
That closes the practical communication loop without promising a decision before review.

Permission to share is not permission to administer | A caregiver asks about two school forms. | Caregiver | Pediatrician
I signed a form allowing the school to receive information. Does that also authorize every medicine task?
Information sharing and medicine administration can require different permissions and arrangements.
I thought one signature automatically covered both because the forms arrived together.
We should explain each purpose and verify the actual requirements.
The school also asked whether my child can carry the inhaler independently.
That is another question requiring the applicable assessment and permission process.
I do not want a discussion of independence recorded as though approval is already granted.
The record should distinguish a request, review, and actual authorization.
Could we check which questions remain open and who will answer each?
Yes. Clear responsibility prevents several related forms from being mistaken for one completed decision.
""")
LESSONS['module-8'] = short_lesson(BOOK['units'][7], """
A caregiver describes a change from usual | A clinician receives a concern during an active response. | Caregiver | Pediatrician
My infant is much less responsive than usual, and the emergency team has been contacted.
We will preserve that report while the actual response continues.
I do not know the clinical word, but I can describe the difference from yesterday.
Your concrete observation matters; you do not need to choose a diagnosis first.
I also noticed poor feeding and want that detail included in the handoff.
It belongs alongside the responsiveness change, with your account clearly attributed.
Should I delay the response while I try to remember an exact time?
No. Clarify what you can without postponing the actual emergency process.
I can give an approximate sequence and identify what I am unsure about.
That is more useful than a falsely precise time or an invented explanation.

Missing measurements are not normal findings | Two clinicians correct an urgent summary. | Referrer | Receiving clinician
The handoff says observations normal, but no verified measurements accompany that statement.
We need to correct it. Missing measurements cannot support a normal finding.
The caregiver's reported change remains the current concern, and the urgent response is active.
Please keep both the source of the concern and the actual action visible.
I will identify which information is observed, reported, measured, or still unknown.
That distinction helps the receiving team understand the evidence rather than infer it.
The diagnosis has not been established in the information being transferred.
Then do not assign one simply to make the summary sound complete.
I will confirm your acknowledgment of the corrected report.
I acknowledge it, and the real clinical assessment continues without waiting for the paperwork to become perfect.

A read-back catches the wrong time | A clinician checks an urgent history correction. | Caregiver | Pediatrician
I said seven thirty was the last time the infant seemed usual, not eight thirty.
Thank you. I will correct the time and repeat it back to confirm.
Please keep it as my observation rather than a measurement by the team.
Yes. The source remains your account of the last observed usual state.
I am not saying that I know the exact moment the change began.
That is a separate question, and we should preserve the distinction.
The emergency response is continuing while we clarify the history.
It must. The language check should not delay the actual clinical care.
Then the receiving team gets the corrected time without assuming a diagnosis from it.
Correct. Read-back improves the communication; it does not replace the assessment.
""")
