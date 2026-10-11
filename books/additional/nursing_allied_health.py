"""Original interprofessional conversations for nursing and allied health."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Speaking up about an unfamiliar device assignment',
        skill='State a competence limit clearly and request safe coverage without abandoning responsibility.',
        setup='In a simulation, a nurse is assigned a device-related task requiring documented local competency. The nurse has used another model but has not completed the assessment for this one. The charge nurse must arrange a safe response through the local process. No device operating instructions are provided.',
        cast='Tara|Staff nurse\nMalik|Charge nurse',
        dialogue='''Tara|I need to raise a concern before taking that task. I have used the previous model, but I am not assessed on this one.
Malik|Thank you for saying so. Let us check your [[competency record::The competency record documents the relevant assessed ability; experience with a different model does not automatically establish it.]] and arrange appropriate coverage rather than assume the devices work identically.
Tara|The ward is busy, and I do not want this to sound like I am refusing to help the team.
Malik|You are identifying a specific limit. Tell me which assigned tasks you can safely continue while I address this one.
Tara|I can continue the work already within my role and competence. This particular task needs someone with the required assessment.
Malik|Agreed. [[Scope of practice::Scope of practice defines the professional activities permitted within a role; individual competence and local requirements must also be considered.]] and competence both matter. A staffing gap does not remove either boundary.
Tara|Could watching someone once count as the assessment? I do not want a quick demonstration mistaken for authorization to work independently.
Malik|A demonstration may support learning, but it does not replace our [[competency assessment::A competency assessment checks and documents performance against the required standard, rather than merely recording that a demonstration occurred.]]. We must follow the actual requirement.
Tara|Then please identify who will take responsibility for the task now. I do not want it left between us while training is discussed.
Malik|I will assign suitable coverage and confirm the [[accountability::Accountability identifies who is responsible for the assigned work and decisions; discussing training does not leave the current task ownerless.]]. Keep any immediate patient concern on the appropriate clinical response route.
Tara|If suitable coverage is not available, what should I do next?
Malik|Use the local [[escalation pathway::The escalation pathway provides the defined route for obtaining a higher-level response when the immediate arrangement cannot safely resolve the issue.]] with me. Do not improvise device use or leave the concern unacknowledged.
Tara|I would like to complete the training so this does not remain a recurring gap in future assignments.
Malik|We can arrange [[supervised practice::Supervised practice is learning under an appropriate supervisor and agreed conditions, not automatic permission for independent work.]] and assessment through the education team, separate from today's coverage decision.
Tara|Should I document that I raised the concern and the arrangement we agree?
Malik|Yes, through the appropriate record. Keep it factual: the specific competency gap, the person informed, and the confirmed response.
Tara|I will avoid writing that every device task is outside my role. The issue is this model and the outstanding local assessment.
Malik|That precision helps us address the real gap without misrepresenting your wider skills or the work you are continuing.
Tara|Please confirm the coverage before we finish this handover. I want the next action clear, not just an agreement that training would be useful.
Malik|I will. The task needs a safe, named arrangement now; the training plan addresses what changes for future assignments.''',
        transfer_title='Attendance is mistaken for demonstrated competence',
        transfer_setup='A colleague attended a device demonstration but has not completed the required local competency assessment. Independent use is being proposed.',
        transfer='''Nurse: Attendance confirms a demonstration, not the required ___.|assessment|The supplied facts distinguish attending instruction from completing the competency assessment.
Lead: Check the documented requirement before assigning independent ___.|use|Independent use must not be inferred from attendance alone under the stated local requirement.
Nurse: Arrange appropriate coverage for the current ___.|task|The immediate task still needs a safe arrangement while the competency gap is addressed.
Lead: Record the training plan separately from today's coverage ___.|decision|The future learning plan and present responsibility arrangement are different decisions.'''),
    scenario(
        title='Difficulty finding words is not absence of a preference',
        skill='Agree communication support while avoiding assumptions about comprehension or decision-making.',
        setup='In a simulation, a patient with documented aphasia has difficulty producing words. The nurse wants to confirm a preference during routine care. The speech-language pathologist has assessed communication supports, but no conclusion about decision-making capacity is supplied. The conversation concerns communication, not a new diagnosis.',
        cast='June|Speech-language pathologist\nAlex|Ward nurse',
        dialogue='''Alex|I asked about a preference, but he could not get the words out. I do not want to record that he has no view.
June|Good. His [[word-finding difficulty::Word-finding difficulty affects access to spoken words; it does not establish that the person has no preference or understanding.]] tells us something about expression, not that he has nothing to communicate.
Alex|He sometimes nods quickly. Can I take a nod as agreement and move on?
June|Not without checking the individual communication plan. We need to consider the [[reliability::Reliability concerns how consistently the response conveys the intended meaning; a nod alone is not universal proof of agreement.]] of that response in this situation.
Alex|I may have asked two questions at once. That probably made it harder to tell what the nod referred to.
June|Keep the question clear and allow the assessed [[processing time::Processing time is the time needed to understand and respond; rushing can make the person's communication appear less effective.]]. Do not fill every pause by adding more questions.
Alex|There is a board by the bed. I was unsure whether it was for this patient or left from an earlier admission.
June|Verify that before using it. The assessed [[communication aid::A communication aid supports expression or understanding; its suitability must be checked for the individual rather than assumed from its presence.]] needs to match his abilities and the intended purpose.
Alex|Would using pictures always be easier than written words?
June|Not necessarily. Aphasia affects people differently. Follow the assessed supports and tell us if the method is not working in the care interaction.
Alex|I also caught myself speaking mainly to his daughter because she answered quickly.
June|Address him directly and include his chosen support appropriately. [[Supported communication::Supported communication helps the person express and understand messages without replacing their participation with someone else's assumptions.]] should enable his participation, not replace it.
Alex|If the daughter supplies an answer, I should distinguish her account from his own response.
June|Exactly. Record who communicated what and how you checked the meaning, especially when the answer affects the next step.
Alex|Does the aphasia diagnosis itself tell us he cannot make the decision?
June|No. [[Decision-making capacity::Decision-making capacity is a separate, context-specific assessment; a language impairment alone does not establish its absence.]] cannot be inferred from difficulty speaking. Use the appropriate decision process and communication support.
Alex|For today's note, I can describe the question, the aid used, his response, and what remained unclear.
June|That is more useful than "unable to communicate." If a particular message could not be established, say so without generalizing to every situation.
Alex|I will review the current communication plan and contact you if the support does not work for this interaction.
June|Please do. We need feedback from actual care conversations so the team can refine support without assuming silence means agreement.''',
        transfer_title='A family answer is recorded as the patient\'s choice',
        transfer_setup='A relative answers a routine preference question while the patient with aphasia has not yet communicated a clear response.',
        transfer='''Nurse: The answer came from the relative, not yet from the ___.|patient|The source of the answer must remain clear rather than be attributed to another person.
Therapist: Use the assessed support to establish the patient's own ___.|preference|Communication support should help the patient express their view where possible.
Nurse: I will not treat difficulty speaking as proof of absent ___.|capacity|Language impairment alone does not establish inability to make a particular decision.
Therapist: Record the method, response, and any remaining ___.|uncertainty|The record should preserve what was established and what was still unclear.'''),
    scenario(
        title='Half a tray is not half the daily nutritional requirement',
        skill='Clarify intake documentation and report barriers for qualified nutritional review.',
        setup='In a simulation, a food chart says "50% eaten" for lunch. It does not identify the items consumed, portion sizes, or any assistance. The nurse observed that two containers were hard for the patient to open. The dietitian needs usable intake information; no nutrition prescription or swallowing change is authorized by this exchange.',
        cast='Leena|Dietitian\nOwen|Ward nurse',
        dialogue='''Leena|The lunch entry says fifty percent. Does that mean half of every item, or half of the tray judged overall?
Owen|It is unclear. The [[intake chart::The intake chart records food and fluid actually consumed; an unexplained percentage may be insufficient for nutritional assessment.]] does not identify which items were eaten, and I did not observe the whole meal.
Leena|Then we should not convert it into an exact energy total. What did you directly observe?
Owen|Two containers were difficult for the patient to open. That may be an [[access barrier::An access barrier prevents food from being practically available to eat, such as packaging the person cannot open.]], rather than evidence that the patient disliked the food.
Leena|Useful distinction. Record that observation and what help was offered or provided, without guessing the rest of the meal.
Owen|I will. Should the record include the [[portion size::Portion size is the amount served and helps interpret how much was consumed; a percentage without a base can mislead.]] as well as the amount left?
Leena|Use our recording method, including enough detail to interpret the intake. Half of a small serving is not the same amount as half of a large one.
Owen|Someone described fifty percent of lunch as half the patient's daily requirement. That does not follow from this entry, does it?
Leena|No. [[Nutritional requirements::Nutritional requirements concern the person's assessed needs; one unqualified meal percentage does not measure how much of those needs was met.]] are a separate assessment. We need the relevant intake and clinical information.
Owen|The patient also said one item was unfamiliar. I should ask about preferences rather than infer them from cultural background.
Leena|Exactly. Capture the stated preference and discuss suitable options within the current plan. Do not substitute foods that conflict with established restrictions.
Owen|If the patient reports difficulty eating or swallowing, I should not quietly change the prescribed texture to encourage intake.
Leena|Correct. Route that concern promptly to the appropriate clinical team. Any [[texture modification::Texture modification changes food consistency and requires the appropriate individualized assessment and plan rather than an improvised substitution.]] must follow the assessed plan and authorized process.
Owen|What should I write about the part of lunch that nobody observed?
Leena|Mark what is unknown under the documentation procedure. A complete-looking estimate is not better than an honest limit on observation.
Owen|For the next meal, I will make sure the relevant support needs reach the team and that the record uses our agreed method.
Leena|Thank you. That improves the [[dietetic assessment::Dietetic assessment evaluates nutritional needs and intake using relevant evidence; clearer observations support but do not replace it.]] without asking staff to invent nutrient calculations at the bedside.
Owen|I will correct the unsupported daily-requirement statement and preserve the original record as our process requires.
Leena|And tell us what changes after the access support is in place. We need the actual intake pattern, not an assumption that one intervention solved everything.
Owen|I will hand over the support needs and the recording gaps so the next shift continues that observation consistently.''',
        transfer_title='An unopened container is labeled a disliked food',
        transfer_setup='A food container remains unopened because the patient reports difficulty opening the lid. No dislike of the food has been stated.',
        transfer='''Nurse: Record the reported difficulty with the lid as an access ___.|barrier|The supplied explanation concerns opening the packaging, not dislike of the food.
Dietitian: Do not infer a food ___ that the patient has not expressed.|preference|An unopened container does not establish what the patient likes or dislikes.
Nurse: Document what assistance was actually ___.|provided|The record should distinguish completed assistance from help merely planned or offered.
Dietitian: Keep any unobserved amount of intake marked as ___.|unknown|An unobserved amount must not become a fabricated consumption estimate.'''),
]
