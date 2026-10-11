"""Additional school operations conversations, individually authored and reviewed."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The approved extra time is missing from the room booking',
        skill='Translate an approved examination arrangement into an accurate operational handover.',
        setup='A fictional school examination starts at 09:00 and normally lasts 80 minutes. A learner has an approved plan for 25% extra working time in Room B. No rest breaks are specified. The room and invigilator are currently booked only until 10:20. The assessment itself is unchanged.',
        cast='Jules|Examinations officer\nFarah|Learning-support coordinator',
        dialogue='''Jules|Room B is on the timetable, but the invigilator is due elsewhere at ten twenty. Have I missed something in the arrangement?
Farah|Yes. The approved [[access arrangement::The access arrangement changes how this learner takes the examination, not the knowledge or marking standard assessed.]] includes twenty-five percent extra working time. The room entry has the ordinary finish time instead.
Jules|The standard paper is eighty minutes. So the additional time is twenty minutes, giving one hundred minutes altogether.
Farah|That is right. Starting at nine means a ten-forty finish, assuming the examination starts on time and there is no interruption.
Jules|Could the learner take those twenty minutes as a break in the middle instead? That might leave the invigilator's next booking intact.
Farah|No. Extra working time and a [[rest break::A rest break pauses work under its own arrangements; it does not replace the approved additional working time.]] are different arrangements. This plan specifies the former, and we cannot substitute the latter for scheduling convenience.
Jules|Understood. I will extend the booking and ask the staffing coordinator to resolve the overlap. I have not confirmed a replacement invigilator yet.
Farah|Please check that before sending the final timetable. A room booking alone does not provide the required supervision through the finish.
Jules|The exam-room notice can show the start and finish. Does the invigilator also need the learner's full assessment history?
Farah|They need the approved [[implementation instructions::Implementation instructions tell the invigilator what to provide; unrelated assessment history is not needed for this operational handover.]], not the whole support file. Use the restricted handover channel and include only what this examination requires.
Jules|I also found a note suggesting fewer questions because the learner has extra time. That does not sound like the approved arrangement.
Farah|Remove it. The [[assessment demands::Assessment demands remain unchanged in this case; additional working time does not authorize removing questions or changing the marking standard.]] remain the same. The learner answers the same paper under the same marking criteria.
Jules|I will correct the note without changing the paper. Shall we check the learner's timetable privately as well?
Farah|Yes. They should know the room and expected finish before the day, without their individual arrangements being announced to the whole class.
Jules|If the start is delayed, staff will need to record the actual start rather than simply collecting everything at ten forty.
Farah|Exactly. The [[working-time allowance::The working-time allowance is one hundred minutes here; the planned clock time must not silently shorten that entitlement after a delayed start.]] is one hundred minutes. The invigilator follows the examination procedure for any disruption and records what happened.
Jules|I will ask for confirmation of Room B and supervision through the full session, then replace the timetable entry.
Farah|Send me the revised handover so I can check it against the approved plan before it is issued.
Jules|The correction is twenty extra working minutes, unchanged questions, a ten-forty planned finish, and a staffing overlap to resolve.
Farah|Yes. Keep that [[booking conflict::The booking conflict concerns the invigilator's overlapping commitments; it remains unresolved until suitable coverage is confirmed.]] visible until coverage is confirmed. Do not mark the arrangements ready just because the finish time has been corrected.''',
        transfer_title='Calculate working time, not a break',
        transfer_setup='A fictional 60-minute examination starts at 13:00. The approved individual plan provides 50% extra working time, the same questions, and no rest breaks. Supervision is currently booked only until 14:00.',
        transfer='''Officer: "The additional working time is ___ minutes."|thirty|Fifty percent of sixty is thirty additional working minutes, not thirty minutes total.
Coordinator: "The planned finish must therefore be ___."|14:30|Ninety working minutes from thirteen hundred ends at fourteen thirty.
Officer: "The questions remain ___."|unchanged|The approved time arrangement does not authorize a different assessment paper.
Coordinator: "The supervision booking needs an ___."|extension|The existing booking ends thirty minutes before the learner's planned finish.''',
        reference=('Ofqual: access arrangements and reasonable adjustments', 'https://www.gov.uk/government/publications/what-people-working-in-schools-and-colleges-need-to-know-before-exams-and-assessments/what-people-working-in-schools-and-colleges-need-to-know-before-exams-and-assessments'),
    ),
    scenario(
        title='A free teacher is not a complete cover plan',
        skill='Resolve timetable dependencies and read back a precise class-cover handover.',
        setup='A teacher is absent for Period 3 mathematics. Daria is qualified but already teaching English then. Eli is qualified and available. The class has 28 learners. Room 204 holds 24; Room 208 holds 32 and is confirmed available and accessible. The school requires a named teacher, suitable room, register, and lesson pack.',
        cast='Omar|Cover coordinator\nBeth|Deputy principal',
        dialogue='''Omar|I can put Daria into Period Three mathematics. She covered the class last month and knows the students.
Beth|Check her [[teaching commitment::The teaching commitment is Daria's existing English class in the same period, which prevents treating her as available cover.]] first. She already has English in that slot. Moving her name would leave that class uncovered.
Omar|You are right. I was looking at yesterday's timetable. Eli is qualified for mathematics and shows as available today.
Beth|Use today's version and confirm the assignment with Eli. Which room are you planning to use?
Omar|Room Two Oh Four is closest. There are twenty-eight students, and that room has space for twenty-four.
Beth|Then the [[room capacity::The room capacity is twenty-four, below the class of twenty-eight; proximity does not make the room suitable.]] does not meet the class size. Room Two Oh Eight is available, accessible, and holds thirty-two.
Omar|I will use Two Oh Eight. I will not move four students elsewhere just to make the smaller room fit.
Beth|Good. Keep the class together under the supplied plan. Check that Eli receives the material before the period starts.
Omar|The absent teacher uploaded today's worksheet and the worked solutions. I can send both through the staff system.
Beth|Include the [[lesson pack::The lesson pack supplies the planned teaching material and worked solutions, distinct from the attendance register or room assignment.]] with the task sequence. Eli should not have to reconstruct the lesson from a worksheet title at the door.
Omar|The student list in the old folder is from last term. I will use the current class record instead.
Beth|Send the current [[attendance register::The attendance register identifies the learners in today's class and supports recording attendance, rather than relying on an outdated list.]]. The room change should not result in attendance being marked against the wrong group.
Omar|Should I tell families? This is a one-period internal cover change, and the class time itself is unchanged.
Beth|Follow our normal internal notification process for this change. Tell the affected students and relevant staff the room and teacher; do not circulate the colleague's reason for absence.
Omar|Eli has now accepted the assignment. I have updated the room entry, but a printed notice still says Two Oh Four.
Beth|Replace that notice. We need a [[single current timetable::A single current timetable means the approved current information is consistent across the notices and systems students and staff actually use.]] across the places people check, not conflicting instructions at opposite ends of the corridor.
Omar|Let me read it back: Period Three mathematics, twenty-eight learners, Eli teaching in Two Oh Eight, current register and lesson pack supplied.
Beth|Correct. Who will meet students who go to the old room before they see the corrected notice?
Omar|I will stand there at changeover and direct them to Two Oh Eight. Eli will receive the class there.
Beth|That closes the [[handover::The handover confirms the teacher, room, records, materials, and transition responsibility, not merely the name entered in the cover system.]]. Record the confirmed assignment and keep the corrected information available to reception as well.''',
        transfer_title='Match the person, period, and room',
        transfer_setup='A class has 26 learners. Qualified teacher Noor is free in Period 4; qualified teacher Ben is already teaching then. Room C holds 22. Available, accessible Room D holds 30. A current register and lesson pack are ready.',
        transfer='''Coordinator: "The available teacher is ___."|Noor|Noor is qualified and free; Ben already has a simultaneous teaching commitment.
Deputy: "The suitable room is ___."|Room D|Room D accommodates twenty-six learners, while Room C falls four places short.
Coordinator: "The room has ___ spare places."|four|Thirty available places minus twenty-six learners leaves four spare places.
Deputy: "Send the current register and the ___."|lesson pack|The supplied plan requires both attendance information and the prepared teaching materials.''',
    ),
    scenario(
        title='A familiar face at the reunification desk',
        skill='Maintain a safe release boundary while reassuring an anxious family member.',
        setup='After a fictional precautionary evacuation, all learners are accounted for at the designated site. Staff member Imani speaks with Mr. Chen, an uncle who has identification but is not on the current authorized-pickup list. Local procedure sends exceptions to the duty administrator; students remain supervised until release is verified.',
        cast='Imani|Reunification staff member\nMr. Chen|Family member',
        dialogue='''Mr. Chen|I am here for my niece. She knows me, and I have collected her before. I brought my identification.
Imani|Thank you. We are using the [[reunification procedure::The reunification procedure governs verified release after this evacuation, rather than allowing adults to collect children directly from the supervised group.]]. All learners are accounted for. Please stay with me while we check this pickup.
Mr. Chen|Here is my name. My sister called and asked me to come because she cannot get away from work.
Imani|I understand. Your identification confirms your name, but I cannot find it on the current pickup list for this learner.
Mr. Chen|Could you ask my niece? She will tell you I am her uncle. We do not need to hold everyone up.
Imani|Recognizing you does not complete the [[release verification::Release verification checks authority for this pickup; recognition and identification alone do not establish that authority under the supplied procedure.]]. The duty administrator handles changes and exceptions. I will refer this now rather than make an informal exception.
Mr. Chen|Does that mean she is in trouble, or that you think something is wrong with my identification?
Imani|No. This is about confirming collection arrangements. It is not a disciplinary issue, and I am not questioning the name on your identification.
Mr. Chen|I can give you a number for my sister. Should I call her and hand you the phone?
Imani|The administrator will use the [[verified contact record::The verified contact record provides the established contact route for checking the request; a newly supplied number alone does not authenticate authorization.]] and follow our local process. I will tell them your sister is expecting contact, but I cannot skip that check.
Mr. Chen|All right. Can I wait beside the children while that happens? I think seeing me would reassure her.
Imani|Please use the [[family waiting area::The family waiting area keeps adults within the designated process while students remain supervised until the release check is completed.]] here. A staff member remains with the learners. I will pass on your request for reassurance through the team.
Mr. Chen|The queue is moving. I am worried that someone will mark her collected just because I have signed in.
Imani|Your arrival is not a completed collection. We record the actual handover separately after the necessary checks.
Mr. Chen|What happens if the administrator cannot reach my sister straight away? I do not want to leave without knowing what to do.
Imani|The [[exception referral::The exception referral remains with the duty administrator when routine verification cannot be completed; it does not authorize an automatic release.]] stays open. Your niece remains supervised, and the administrator decides the next permitted step under the plan.
Mr. Chen|Please tell them I can wait here and that my sister asked me to collect her. I would appreciate an update even if there is a delay.
Imani|I will pass on exactly that. I have not been given a confirmed completion time, so I will not promise a number of minutes.
Mr. Chen|Thank you. Once approval is verified, I should wait for staff to bring her through the collection point rather than go into the group.
Imani|Yes. Staff will complete the [[handover record::The handover record documents the actual verified release, including the required collection details, rather than treating arrival or a request as completion.]] at release. For now, please remain in the waiting area while the administrator checks the arrangement.''',
        transfer_title='Check-in is not collection',
        transfer_setup='At a fictional reunification site, a neighbor shows identification but is not listed for pickup. The duty administrator has received the exception referral but has not yet verified release. The learner remains supervised.',
        transfer='''Staff: "The identification establishes the adult\'s ___."|identity|Identification can establish who the adult is without establishing collection authority.
Neighbor: "The pickup authority still needs ___."|verification|The administrator has received the request but has not verified release.
Staff: "The learner must remain ___."|supervised|The supplied process keeps the learner supervised while the release check remains incomplete.
Neighbor: "My arrival is not a completed ___."|handover|Check-in records arrival, whereas a handover records the actual verified collection.''',
        reference=('U.S. Department of Education: Families as Partners in School Emergency Management (2007)', 'https://cdpsdocs.state.co.us/safeschools/Resources/REMS%20Helpful%20Hints/HH_Vol2Issue7,1.pdf'),
    ),
]
