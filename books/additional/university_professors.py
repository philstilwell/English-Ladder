"""Additional faculty conversations on privacy, references, and teaching observation."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Responding to a parent request without disclosing a student record',
    skill='Offer useful general information while routing a request for individual records through the authorized process.',
    setup='A parent contacts Professor Harris, says they pay their adult child\'s tuition, and asks for the student\'s grades and attendance. The professor has not verified the caller or any consent or applicable disclosure basis. The fictional institution requires this request to go through its student-records process. The professor can explain that route and public course information without confirming the individual record.',
    cast='Parent | Caller\nProfessor Harris | Instructor',
    reference=('US Department of Education. Postsecondary parent access to education records.', 'https://studentprivacy.ed.gov/faq/must-postsecondary-institutions-provide-parent-access-eligible-students-education-records'),
    dialogue='''Parent | I pay my child's tuition, and I need to know the current grade and whether they are attending your class.
Professor Harris | I understand you want to support them. I cannot disclose an individual record through this unverified call.
Parent | I assumed paying the fees meant the university could immediately tell me anything about their academic progress.
Professor Harris | Payment alone does not establish the [[disclosure basis::The disclosure basis is the actual authorization or applicable exception for sharing records, not an assumption based only on who pays tuition.]] for this request. We need to use the institution's proper process.
Parent | Are you saying a parent can never receive information, even when the student wants us involved?
Professor Harris | No. [[Consent::Consent may provide a basis for sharing under the relevant requirements, but its existence and scope must be verified rather than assumed.]] and applicable exceptions need to be assessed through the authorized process, not decided from this call alone.
Parent | My child told me generally that I could speak to the university, but I have no verified record of that permission here.
Professor Harris | Then the [[student-records office::The student-records office is the designated route in this fictional institution for verifying the request and any relevant authority to disclose.]] can explain the actual requirements and review the request appropriately.
Parent | Could you at least confirm whether the student is enrolled in your particular section while we sort that out?
Professor Harris | I should not disclose or confirm individual record details through an unverified request while the relevant basis remains unchecked.
Parent | I do not want the process to prevent me from helping. Is there general information you can provide now?
Professor Harris | I can point you to [[public course information::Public course information can explain general course arrangements without revealing an individual student's protected academic record.]] and the appropriate support contacts without discussing an individual student's grades or attendance.
Parent | That would help me understand how the course normally communicates assessment and where students can seek support.
Professor Harris | I can also explain the [[verification process::The verification process checks identity, authority, and the relevant request under institutional requirements before an individual record is shared.]] for your records inquiry, so you know which office handles the next step.
Parent | I will contact that office rather than keep asking you to confirm details before the authorization question is resolved.
Professor Harris | Thank you. That keeps the [[privacy boundary::The privacy boundary protects individual record information while allowing appropriate support and properly authorized requests to proceed.]] clear without treating your wish to help as improper.
Parent | Once the appropriate process has been completed, any information shared should stay within the permission or other applicable basis.
Professor Harris | Exactly. The relevant scope matters; one authorized disclosure should not be treated as unrestricted access to every record.
Parent | Please send me the public information and the correct office contact, without including the student's private results.
Professor Harris | I can provide those general resources. The records request itself will follow the institution's actual verification and disclosure process.''',
    transfer_title='A general permission was treated as unlimited access', transfer_setup='A verified authorization permits sharing one specified progress report. A requester asks for unrelated records as well. No basis for the additional disclosure is supplied.',
    transfer='''Instructor: "The verified authorization has a defined ___." | scope | The supplied authorization concerns one specified report, not every student record.
Requester: "The additional records are outside that ___." | permission | The case supplies no authorization covering the unrelated additional records.
Instructor: "The broader request needs separate ___." | review | The additional disclosure requires the appropriate institutional assessment rather than assumption.
Requester: "I will use the designated records ___." | process | The broader request should follow the actual authorized review route.'''),
scenario(title='Agreeing to a recommendation within the evidence available',
    skill='Offer a supportive reference without claiming observations the professor has not made.',
    setup='Student Isabel asks Professor Mensah for a strong internship recommendation. Mensah taught Isabel in one seminar and directly observed her evidence-based presentations and reliable group contributions. Mensah did not supervise her laboratory research. Isabel asks whether the letter can describe her as an outstanding laboratory researcher. The professor explains the evidence limit and confirms the actual submission requirements before committing to a deadline.',
    cast='Isabel | Student\nProfessor Mensah | Faculty referee',
    dialogue='''Isabel | Would you write a strong recommendation for my internship? I hoped it could emphasize that I am an outstanding laboratory researcher.
Professor Mensah | I can discuss your seminar work positively, but I did not supervise your laboratory research and should not imply that I did.
Isabel | You saw my presentations and group work, while my lab supervisor observed the research activities I want to highlight.
Professor Mensah | That distinction defines the [[basis of assessment::The basis of assessment identifies what the referee actually observed, preventing supportive language from implying nonexistent direct supervision.]] for my letter and helps you decide whether I am the right referee.
Isabel | Could you focus on how I evaluated evidence and responded to questions during the seminar presentations?
Professor Mensah | Yes. Those are [[direct observations::Direct observations concern work the professor actually witnessed, unlike laboratory performance outside the professor's experience.]] I can support with specific examples rather than a broad claim about work I did not see.
Isabel | I would prefer an accurate letter with examples to an impressive label that the reader could misunderstand.
Professor Mensah | That is a sound approach. A [[specific endorsement::A specific endorsement supports an identified strength with evidence instead of relying on an ungrounded superlative.]] can be persuasive without describing you as the best researcher I have ever supervised.
Isabel | The internship also values collaboration. You observed me coordinating the evidence table for our group presentation.
Professor Mensah | I can describe that contribution and distinguish your role from the group's collective work.
Isabel | Should I send my current résumé and the internship description, so you can see what the position requires?
Professor Mensah | Please send those materials through the appropriate channel, along with the [[submission requirements::Submission requirements identify how and when the reference must be delivered, which need checking before a reliable commitment can be made.]] and the actual deadline.
Isabel | The portal asks for the referee to submit directly. I should not assume that receiving an email draft completes that step.
Professor Mensah | Correct. We need to distinguish a prepared letter from a completed submission through the requested route.
Isabel | I also need to know whether you can meet the deadline before I enter your name as a confirmed referee.
Professor Mensah | I will check the details and give you a clear [[availability confirmation::Availability confirmation establishes whether the professor can undertake the request within the actual requirements rather than leaving the student to assume acceptance.]] rather than leave you relying on an uncertain possibility.
Isabel | If the position needs a judgment specifically about laboratory research, I should also approach the person who supervised that work.
Professor Mensah | Yes. That would provide the relevant [[evidential scope::Evidential scope limits the claims a reference can responsibly make based on the referee's actual knowledge and observations.]] rather than asking one letter to cover experience its writer does not have.
Isabel | I will send the materials and ask you to emphasize the seminar strengths you directly observed, without extending them into laboratory claims.
Professor Mensah | That lets me be supportive and accurate. Once I confirm the request, we can keep the preparation and submission status clear.''',
    transfer_title='Prepared is not submitted', transfer_setup='A professor has completed a recommendation letter, but the required direct portal submission has not yet occurred. The actual deadline remains relevant.',
    transfer='''Student: "The letter has been ___." | prepared | The document is complete, but that does not establish delivery through the required route.
Professor: "The portal submission is still ___." | pending | The case states that the required direct submission has not occurred.
Student: "We should keep the actual deadline ___." | visible | An unfinished submission requires continued attention to the real deadline.
Professor: "I will confirm the completed ___." | submission | Confirmation should concern the actual delivery event rather than document preparation alone.'''),
scenario(title='Reviewing a peer teaching observation',
    skill='Use observed classroom evidence to discuss participation while separating observation, interpretation, and a proposed change.',
    setup='In a twenty-minute seminar observation, Wu records eight responses: six from one student and one each from two others. Wu and Lewis discuss wait time and turn-taking. Silence does not establish disengagement, and a proposed pause has no guaranteed effect. Their agreed meeting is developmental, not a personnel evaluation.',
    cast='Professor Lewis | Observed instructor\nProfessor Wu | Peer observer',
    dialogue='''Professor Lewis | The class seemed engaged to me, but your note says one student gave most of the responses. What exactly did you observe?
Professor Wu | In the twenty-minute segment, I recorded eight verbal responses: six from one student and one each from two others.
Professor Lewis | That is useful detail. It does not tell us what every silent student was thinking or whether they understood the material.
Professor Wu | Correct. The [[observation record::The observation record captures the responses actually seen and heard, not an inferred account of every student's engagement or understanding.]] should stay separate from interpretations that the data do not establish.
Professor Lewis | I may have treated quick replies as evidence that the whole room was ready to move on.
Professor Wu | The response distribution suggests a question about [[participation pattern::The participation pattern describes how contributions were distributed and invites inquiry without proving that silent participants were disengaged.]], not a conclusion that the other students learned nothing.
Professor Lewis | Could a slightly longer pause after the question give more people time to formulate an answer?
Professor Wu | That is a plausible [[teaching adjustment::A teaching adjustment is a proposed change to practice whose effect needs checking rather than being guaranteed by the suggestion.]] to try under your course arrangements, provided we state what we want to observe.
Professor Lewis | We could keep the question type similar and note whether a wider range of students contributes after the pause.
Professor Wu | Yes. That makes the proposed comparison more specific without pretending it is a controlled causal study.
Professor Lewis | I also want to invite a second response before I summarize, so the first contribution does not close the discussion.
Professor Wu | We can include that in the [[follow-up focus::The follow-up focus identifies what a subsequent observation will examine, preventing the discussion from expanding into an undefined judgment of the whole course.]] and record the actual sequence of invitations and responses.
Professor Lewis | Our agreement described this as developmental feedback. I do not want the notes to become an unexpected personnel rating.
Professor Wu | We should keep the [[observation agreement::The observation agreement defines the purpose and handling of this developmental visit, which should not be silently changed into another evaluative use.]] and the institution's actual process clear, including who receives the notes.
Professor Lewis | Then the summary should say that verbal participation was concentrated in the observed segment, not that the entire class was disengaged.
Professor Wu | Exactly. It should also avoid implying that one short segment represents every session or every form of participation.
Professor Lewis | After trying the pause, I can bring a comparable record and discuss what changed without announcing success in advance.
Professor Wu | That gives us a [[developmental feedback cycle::A developmental feedback cycle links observation, a bounded change, and subsequent review rather than treating advice as proof of improved learning.]] grounded in evidence and your stated teaching goal.
Professor Lewis | I appreciate the distinction between a concrete observation and a broad judgment about my students or my teaching.
Professor Wu | The concrete record makes the conversation more useful. It gives us something to inspect and test while preserving what remains unknown.''',
    transfer_title='Silence was labeled disengagement', transfer_setup='A note records that four students did not speak during one observed segment. No information about their thinking or understanding is supplied.',
    transfer='''Observer: "The recorded fact concerns verbal ___." | participation | The note describes whether students spoke, not their entire mental engagement.
Instructor: "It does not establish their ___." | understanding | The supplied observation contains no direct evidence of what those students understood.
Observer: "The broader claim is an ___." | interpretation | Calling silence disengagement adds an inference beyond the recorded behavior.
Instructor: "We should keep the observation appropriately ___." | bounded | One segment and one behavior cannot establish every student's overall learning state.'''),
]
