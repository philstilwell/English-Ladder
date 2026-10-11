"""Additional leadership situations: capacity, credit, and changing a decision."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='Two urgent launches and one shared analyst',
    skill='Negotiate priorities upward without making an impossible commitment.',
    setup='The US branch has one analyst available for six days next week. The renewal review needs four days; a new launch needs four. The director can change priorities but has not approved extra staffing.',
    cast='Mina|Branch manager\nAlex|Regional director',
    dialogue='''
Alex|Can your team add the launch analysis next week? Sales needs it by Friday.
Mina|We can take it on if we [[reprioritize::Reprioritize means change the order of importance when available capacity cannot cover everything.]]. Which deliverable should move?
Alex|I wasn't asking you to move anything. The renewal review still matters.
Mina|Understood. Together they need eight analyst days. We have six, even with my team taking over the presentation.
Alex|Could the analyst just push a little harder?
Mina|She's already covering an absence. I can ask about the estimate, but I won't commit her to eight days of work in six.
Alex|All right. What's the smallest useful launch analysis?
Mina|A two-day [[first pass::A first pass is an initial review, not the complete analysis requested originally.]] covering our two largest customer groups. It would exclude the regional breakdown.
Alex|Sales will ask for that breakdown immediately.
Mina|Then we need to choose. I recommend protecting the renewal review and sending the smaller launch analysis on Friday.
Alex|Why put renewals first?
Mina|Three contracts come up for review Monday. The launch decision is still two weeks away. That's the [[trade-off::Trade-off names the competing benefits and costs of choosing one priority over another.]].
Alex|That makes sense. Can you promise the rest by Tuesday?
Mina|Wednesday is the date I can support. Tuesday would depend on work we haven't scoped yet.
Alex|Let's use Wednesday. I need you to manage Sales' expectations.
Mina|I will. Can I say we have your [[sign-off::Sign-off means explicit approval of this revised priority and delivery plan.]] on the reduced Friday scope?
Alex|Yes. Copy me on the message, and I'll back the decision if they challenge it.
Mina|Thanks. I'll send the scope and dates today. If a new request comes in, we'll [[reopen::Reopen means return to a decision for further discussion rather than silently adding more work.]] the priority discussion.
Alex|Agreed. I don't want the analyst negotiating this alone.
Mina|Neither do I. I'll be the [[point of contact::Point of contact identifies the person who will receive questions and coordinate follow-up.]] for changes, and she'll focus on the analysis.
''',
    transfer_title='A request arrives after the agreement',
    transfer_setup='Sales now requests a third customer group in Friday\'s initial analysis. Mina needs Alex to choose between adding it and retaining the agreed deadline.',
    transfer='''
Mina: A third group is ___ the Friday scope we agreed.|outside|Outside marks the request as additional work rather than an existing commitment.
Alex: Can we include it without moving the ___?|deadline|Deadline identifies the agreed delivery time that the additional work could affect.
Mina: Only if we ___ one of the original two groups.|replace|Replace means substitute one group for another instead of adding a third.
Alex: Keep the original two. I'll ___ that decision with Sales.|confirm|Confirm means communicate the agreed decision clearly to the affected team.
'''),
scenario(
    title='When praise leaves out the people who did the work',
    skill='Address recognition and attribution without guessing a colleague\'s motives.',
    setup='A project sponsor praised a manager for an improved onboarding process. Three team members designed and tested it. The manager accepted the praise without naming them; a team lead raises the omission privately.',
    cast='Sam|Team lead\nElena|Department manager',
    dialogue='''
Sam|Do you have five minutes about the sponsor's update?
Elena|Sure. I thought it went well. Was something inaccurate?
Sam|The results were right. But when she thanked you for designing the process, you didn't mention Noor, Luis, or Priya.
Elena|I didn't mean to [[take credit::Take credit means accept recognition for work or an achievement, including work done by others.]] for their work. I thought everyone knew it was a team effort.
Sam|The sponsor doesn't work with them. They heard the update and felt their contribution had disappeared.
Elena|Thanks for telling me. What would put that right without making the next meeting awkward?
Sam|A short [[follow-up::A follow-up is a later message or action that addresses an earlier exchange.]] naming what each person did would help.
Elena|I can do that. Noor built the checklist, Luis ran the trial, and Priya gathered feedback. Have I got that right?
Sam|Yes. And Luis also trained the first group of supervisors.
Elena|I'll include that. I'd like to give them the floor at next month's review.
Sam|Please ask them first. Priya would rather share the customer findings with Noor than present alone.
Elena|Fair point. Recognition shouldn't become an unexpected [[spotlight::Spotlight means concentrated public attention; here it could make an employee uncomfortable.]].
Sam|Exactly. I don't want us to assume everyone wants the same kind of praise.
Elena|Would you check whether they'd prefer to present together?
Sam|I can ask, but the invitation should come from you. That will make the [[attribution::Attribution identifies who produced particular work rather than crediting only the manager.]] clearer.
Elena|You're right. I'll send the correction today and speak with them tomorrow.
Sam|Thank you. I worried this might sound like a complaint about you personally.
Elena|You raised a specific [[omission::Omission means something left out; here it is the contributors' names and work.]]. I needed to hear it.
Sam|Then let's add contributors' names to future project updates before they go out.
Elena|Agreed. I'll own the final check and make that part of our [[routine::Routine means an established repeated practice, not a one-time response to this incident.]].
''',
    transfer_title='Correcting the public record',
    transfer_setup='Elena calls the sponsor before sending a written correction. The sponsor has not yet shared the results with the executive team.',
    transfer='''
Elena: Before you circulate the results, I need to correct an ___ in yesterday's update.|omission|Omission identifies information that was left out without inventing a motive.
Sponsor: Do we need to change the ___ themselves?|figures|Figures means the numerical results, which the scenario says are accurate.
Elena: No. Please add the three ___ and their specific roles.|contributors|Contributors identifies the people who performed the work described in the update.
Sponsor: Send me the wording and I'll use the ___ version.|revised|Revised describes a corrected version incorporating the missing names and roles.
'''),
scenario(
    title='Reversing a decision without undermining the team',
    skill='Explain a changed decision, acknowledge its cost, and define what remains valid.',
    setup='A branch manager approved a Monday software launch. A test completed Thursday reveals that customers cannot retrieve some older records. The technical lead recommends postponement. Customer messages are prepared but have not been sent.',
    cast='Omar|Branch manager\nGrace|Technical lead',
    dialogue='''
Omar|You asked to revisit Monday. What's changed since yesterday?
Grace|The archive test failed. Current records load correctly, but some older records don't. We need to [[hold off::Hold off means postpone an action temporarily while a relevant concern is resolved.]] on the launch.
Omar|I told the leadership team the date was settled.
Grace|I know. We didn't have this result then. I'm asking you to change the decision because the evidence changed.
Omar|Could we launch and warn customers about older records?
Grace|Some use those records to complete daily work. Support doesn't have a reliable workaround yet.
Omar|How long will the fix take?
Grace|I can't give you that date today. By tomorrow noon, we can [[narrow down::Narrow down means reduce the possible causes or options through further investigation.]] the cause and estimate the repair.
Omar|Then I need a message today that doesn't sound as though the team missed an obvious check.
Grace|We can state when the test ran and what it found. The test was scheduled before release for this reason.
Omar|You're right. I shouldn't turn this into a search for someone to blame.
Grace|The immediate [[decision point::Decision point identifies the choice that must be made now, rather than every later question.]] is whether to send the launch messages.
Omar|Don't send them. I'll explain the postponement to leadership myself.
Grace|Thank you. Can we keep the completed training and documentation work?
Omar|Yes. This doesn't [[invalidate::Invalidate means make something no longer valid; the failed test does not cancel all completed work.]] those deliverables. Update only what the fix changes.
Grace|I'll tell the team that. They're likely to hear postponement as starting again.
Omar|Let's be explicit: the release is paused, not abandoned. What will you bring tomorrow?
Grace|The cause we can support, the repair estimate, and the [[release criteria::Release criteria are the conditions that must be met before the launch can proceed.]] we still need to satisfy.
Omar|Good. I'll book the review and explain that the next date depends on those checks.
Grace|I'll send the evidence first so we can use the meeting to [[make the call::Make the call means make the decision after reviewing the relevant information.]], not reconstruct the timeline.
''',
    transfer_title='A colleague asks whether everything is cancelled',
    transfer_setup='A supervisor has heard about the postponement and wants to cancel the training records and support preparation.',
    transfer='''
Supervisor: Should I cancel the whole launch ___?|plan|Plan refers to all coordinated launch work, which has not been abandoned.
Omar: No. The release is ___ while the archive issue is investigated.|paused|Paused describes a temporary stop rather than cancellation of the entire project.
Supervisor: I'll retain the completed work and flag any ___ on the fix.|dependencies|Dependencies identifies tasks whose completion or accuracy relies on the forthcoming repair.
Omar: Exactly. We'll review the remaining criteria at tomorrow's ___.|checkpoint|Checkpoint is the scheduled review where the team will assess readiness again.
'''),
]
