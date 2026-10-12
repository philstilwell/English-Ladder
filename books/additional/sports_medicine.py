"""Three additional sports-medicine dialogues and explained transfer exchanges."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Clarifying a therapeutic use exemption request',
    skill='Distinguish medical treatment questions from anti-doping authorization and application status.',
    setup='Athlete Remy has a prescription from the treating clinician and asks team physician Dr Noor whether that automatically establishes permission under the relevant anti-doping rules. The actual medicine, sport, athlete classification, and rules are not supplied. A therapeutic use exemption question must be checked through the responsible anti-doping process; no medicine change or exemption outcome is authorized by this case.',
    cast='Remy | Athlete\nDr Noor | Team physician',
    dialogue='''Remy | I have a prescription from my treating clinician. Does that automatically settle the anti-doping permission question as well?
Dr Noor | Not automatically. The clinical prescription and the applicable sporting requirements are distinct questions that need their proper review.
Remy | I have heard of a therapeutic use exemption, but I do not know whether my actual situation requires one.
Dr Noor | A [[therapeutic use exemption::A therapeutic use exemption concerns permission under the applicable anti-doping process and is not automatically established by a prescription alone.]] question needs the actual medicine, rules, athlete classification, and responsible organization's process.
Remy | Then I should not rely on a teammate who said every prescribed medicine is automatically permitted in every sport.
Dr Noor | Correct. We need the current applicable requirements rather than a general claim that ignores the actual details.
Remy | The online form says my request was received. I was about to describe that as exemption approved.
Dr Noor | [[Application receipt::Application receipt confirms that a request arrived and does not itself establish approval of the exemption being requested.]] is not approval. We should check the actual status and any outstanding information through the responsible process.
Remy | There is also a question about the level at which I compete. Why does that matter to the inquiry?
Dr Noor | The [[athlete classification::Athlete classification can affect the relevant anti-doping process and responsible organization, so it must be established rather than guessed.]] helps identify the relevant requirements and organization. We should use the actual category, not assume it from the team name.
Remy | I can provide the current medicine information and the documents requested through the proper channel.
Dr Noor | Good. Keep the clinical information accurate and limited to the authorized purpose; missing details should not be invented to complete a form.
Remy | If the status is pending, I should say pending rather than reassure the coach that every requirement is settled.
Dr Noor | Exactly. A [[pending decision::A pending decision means the relevant determination has not been completed and must not be presented as a favorable outcome.]] needs to remain visible, along with who is responsible for answering the regulatory question.
Remy | Should I change my medicine because the administrative question is unresolved?
Dr Noor | Do not use this conversation as a medicine-change instruction. Treatment questions belong with the appropriate treating professional and actual clinical process.
Remy | So the next step is an accurate inquiry, not a guess about a banned list or an exemption outcome.
Dr Noor | Yes. The [[responsible anti-doping organization::The responsible anti-doping organization handles the applicable sporting process, which must be identified from the actual athlete and rule context.]] needs to be identified so the question goes to the correct authority.
Remy | I will explain the status as a request requiring review and avoid saying the prescription itself grants sporting permission.
Dr Noor | That preserves the [[authorization distinction::The authorization distinction separates the clinical prescription from permission under sporting rules, preventing one decision from being treated as the other.]] without interrupting necessary clinical care or inventing a regulatory result.''',
    transfer_title='Received is not approved', transfer_setup='An exemption portal confirms receipt of an application. It asks for further information and gives no approval decision. The athlete reports the status to the team.',
    transfer='''Athlete: "The application has been ___." | received | The portal confirms arrival of the application, not its approval.
Clinician: "Further information is still ___." | requested | The portal asks for additional information before the matter is resolved.
Athlete: "Approval has not been ___." | given | No approval decision appears in the supplied status update.
Clinician: "We should report the actual application ___." | status | Accurate status language prevents a receipt notice from becoming a false authorization.'''),
scenario(title='Handing over care before overseas travel',
    skill='Transfer verified rehabilitation information across teams and time zones without losing responsibility or emergency routes.',
    setup='Physiotherapist Erin hands athlete Jules\'s care to destination clinician Dr Kim before an overseas event. The current rehabilitation plan is available through an authorized channel. Travel dates are confirmed, but the receiving appointment is only requested. No new participation authorization or exercise instruction is supplied. They clarify document versions, contact times, and the pending appointment.',
    cast='Erin | Referring physiotherapist\nDr Kim | Destination clinician',
    dialogue='''Erin | Jules travels on the confirmed itinerary, but the receiving appointment is still a request rather than a completed booking.
Dr Kim | Thank you for separating those. Travel confirmation does not mean our clinical service has already accepted an appointment time.
Erin | I will send the current rehabilitation plan through the authorized channel with its date and revision clearly identified.
Dr Kim | That [[document provenance::Document provenance identifies the origin and version of the plan, helping the receiving clinician distinguish current instructions from older copies.]] matters because the athlete may also carry an older handout with different wording.
Erin | The plan does not authorize a new activity simply because the athlete is traveling to a sporting event.
Dr Kim | Agreed. The [[travel purpose::Travel purpose explains why the person is attending the event and does not establish clinical authorization to participate in every activity there.]] is not a substitute for the actual participation information and clinical decision.
Erin | I can identify the clinician responsible for the present plan and the outstanding review question.
Dr Kim | Please do, and make the [[handoff responsibility::Handoff responsibility identifies who owns each part of the ongoing care and communication rather than assuming a sent document transfers every duty.]] explicit while the receiving arrangements are still being confirmed.
Erin | We also need a time for questions before departure. The proposed message simply says call at nine.
Dr Kim | Add the date and [[time zone::A time zone makes a cross-border contact time interpretable and prevents identical clock numbers from referring to different moments.]]. Otherwise the same clock time could refer to different moments in our locations.
Erin | I will also distinguish a routine professional contact from the athlete's actual urgent-care route at the destination.
Dr Kim | Yes. A routine inbox should not become the assumed emergency route merely because it appears on the handoff sheet.
Erin | The athlete needs a clear account of the appointment status, rather than discovering on arrival that nobody confirmed it.
Dr Kim | I will check our [[booking status::Booking status distinguishes a requested appointment from an accepted or confirmed booking and should be communicated accurately before travel.]] and tell you which arrangements we can actually confirm.
Erin | If the appointment time changes, we should update the athlete and both relevant teams rather than only our own calendar.
Dr Kim | Exactly. A corrected internal schedule does not automatically reach the person relying on the appointment.
Erin | I will keep the shared information limited to the purpose and actual permission for this clinical handoff.
Dr Kim | That supports [[continuity of care::Continuity of care depends on connected information and responsibilities across services, not simply on sending a complete-looking document before travel.]] while respecting the applicable information-sharing requirements in both settings.
Erin | Then the open items are appointment confirmation, the named contact time, and receipt of the verified current plan.
Dr Kim | Correct. We will close those items explicitly without adding a diagnosis, exercise change, or sport authorization that has not been made.''',
    transfer_title='Nine in which time zone?', transfer_setup='A handoff proposes a call at 09:00 but omits the date and time zone. Both teams agree the call is not yet fully specified. The clinical plan is unchanged.',
    transfer='''Referrer: "The call still needs a date and time ___." | zone | The clock time alone is ambiguous when the teams work across locations.
Receiver: "The proposed contact time is not fully ___." | specified | The missing date and zone prevent a complete shared understanding of the appointment.
Referrer: "The clinical plan remains ___." | unchanged | Clarifying a contact time does not alter any clinical instruction.
Receiver: "We will confirm the complete call ___." | details | A usable confirmation must include the missing information needed by both teams.'''),
scenario(title='Discussing a return setback without assigning blame',
    skill='Describe a reported difficulty during rehabilitation and request review without diagnosing failure or concealing the concern.',
    setup='Athlete Noor reports difficulty during a permitted rehabilitation task and fears being labeled unmotivated. Physiotherapist Alex asks what happened and keeps the actual clinical response separate from performance pressure. The task, symptoms, measurements, and clinical interpretation are not supplied. They agree to report the relevant facts to the responsible clinician through the current plan\'s route.',
    cast='Noor | Athlete\nAlex | Physiotherapist',
    dialogue='''Noor | I had difficulty during the task, but I almost left it out because I thought everyone would call it a setback I caused.
Alex | I would rather hear an accurate account than have you hide a concern to make the progress report look better.
Noor | I can describe what happened, but I do not know whether it changes the injury or the plan.
Alex | Keep the [[event description::An event description records what occurred without automatically assigning a diagnosis, cause, or change to the rehabilitation plan.]] separate from its clinical meaning. We need the actual facts before the appropriate review can interpret them.
Noor | The coach keeps asking whether I am trying hard enough, and I worry that uncertainty sounds like an excuse.
Alex | [[Performance pressure::Performance pressure can influence how an athlete reports concerns, but it should not replace accurate communication or the clinical response.]] can make this harder to discuss, but it should not determine what you feel able to report.
Noor | Should I say the rehabilitation failed, or does that label go beyond what I actually know?
Alex | It goes beyond the facts. A reported [[task difficulty::Task difficulty describes a problem performing the activity and does not by itself establish treatment failure or a new structural injury.]] does not by itself establish failure of the plan or a new injury.
Noor | I also do not want the summary to say everything was fine just because the details are not yet interpreted.
Alex | Correct. Uncertainty is not reassurance. We should describe what is known and use the actual clinical response route.
Noor | I can identify when the difficulty happened and what I was doing, without making up a test result.
Alex | That helps the [[responsible reviewer::The responsible reviewer needs accurate information to assess the concern and should be identified rather than replaced by an informal team opinion.]] assess the concern through the current plan, rather than relying on an informal team conclusion.
Noor | Who will explain any decision afterward so I do not hear different versions from different people?
Alex | We should identify the communication owner and ensure the athlete receives the verified outcome, not only the staff discussion.
Noor | If the plan changes, I want to know which earlier instruction is no longer current.
Alex | A [[plan clarification::A plan clarification makes the actual instruction and any authorized change understandable without asking the athlete to resolve conflicting versions alone.]] should make that explicit and correct any conflicting message through the appropriate process.
Noor | Then I do not need to choose between sounding positive and telling the truth about the difficulty.
Alex | Exactly. We can acknowledge effort without asking you to minimize a concern or promise a recovery date.
Noor | I will give the factual account and follow the actual clinical instructions for reporting and response.
Alex | That supports [[nonjudgmental reporting::Nonjudgmental reporting describes relevant facts without attributing blame or motive, helping the clinical team receive information needed for an appropriate response.]] while leaving diagnosis, urgency, and any plan change to the appropriate clinical process.''',
    transfer_title='A missed entry concealed a concern', transfer_setup='An athlete omitted a reported difficulty from a progress form because they feared blame. The team corrects the record and routes the actual concern for clinical review; no diagnosis is supplied.',
    transfer='''Athlete: "The progress entry was ___." | incomplete | Omitting the reported difficulty left the progress record without relevant information.
Clinician: "We need the factual ___." | account | The review needs what actually happened rather than an invented interpretation.
Athlete: "A diagnosis is not yet ___." | established | The scenario provides a report and review route but no clinical diagnosis.
Clinician: "We can correct the record without assigning ___." | blame | A nonjudgmental correction preserves the facts without attributing an unsupported negative motive.'''),
]
