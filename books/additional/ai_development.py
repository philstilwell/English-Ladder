"""Additional AI conversations about annotation, training recovery, and tool use."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='The annotators disagree about what counts as a request',
    skill='Resolve a labeling disagreement by revising an operational definition.',
    setup='Two annotators labeled 100 support messages independently. They disagreed on 18, mostly messages reporting a fault without explicitly requesting help. The labeling lead and model engineer must clarify the rubric before the next training-data batch.',
    cast='Inez|Labeling lead\nCal|Model engineer',
    dialogue='''
Cal|Can we release the next batch today? Training is waiting for those labels.
Inez|Not yet. The double-labeled sample has 18 disagreements out of 100 messages.
Cal|Are those mostly careless mistakes?
Inez|No. Look at this one: "The export failed again." One annotator marked a request; the other marked a status report.
Cal|Our [[rubric::Rubric means the written criteria for assigning labels, which are unclear for this message.]] says a request asks for assistance. Neither reading seems unreasonable.
Inez|Exactly. We need to decide whether implied requests belong in that class.
Cal|For this routing model, they do. Otherwise the support queue could miss a customer who expects help without asking directly.
Inez|Then let's add a [[boundary case::A boundary case sits near the dividing line between categories and helps clarify the rule.]] showing that distinction, plus a genuine status update.
Cal|Would "The export failed, but I've fixed it" work for the second example?
Inez|Yes. It reports a resolved event and doesn't seek further action. I'll make the context requirement explicit.
Cal|Can the lead annotator just relabel the disputed 18?
Inez|We need [[adjudication::Adjudication is a defined review process for resolving disputed labels, not simply accepting the first opinion.]], then a check for the same issue in the rest of the batch.
Cal|Right. Otherwise we'd fix only the examples we happened to double-label.
Inez|I'll also keep the original labels. We need to trace which guideline version each annotator used.
Cal|How will we know the revised guidance helps?
Inez|Use a fresh [[calibration sample::A calibration sample lets annotators practice and compare judgments under the revised instructions.]] before production labeling resumes. They should label it independently first.
Cal|And compare agreement before discussing the answers?
Inez|Yes. Agreement is useful, but we'll still inspect disagreements. Two people can consistently apply an incorrect rule.
Cal|I'll put training on hold and record the [[dataset version::Dataset version identifies the particular release of examples and labels used in an experiment.]] once the corrected batch is approved.
Inez|I'll send the revised examples today. The batch's [[release status::Release status states whether the data are approved for use, rather than merely present in storage.]] stays pending until the review is finished.
''',
    transfer_title='A new annotator encounters an ambiguous message',
    transfer_setup='A new annotator cannot classify a message using the revised examples. The lead wants it routed for review without silently forcing a label.',
    transfer='''
Annotator: This message doesn't fit either example in the current ___.|guideline|Guideline is the written labeling instruction the annotator has consulted.
Lead: Add it to the ___ queue with the reason for uncertainty.|review|Review identifies the route for a judgment that needs further examination.
Annotator: Should I preserve the original text and my provisional ___?|label|Label is the tentative category assignment, distinct from the source message.
Lead: Yes. We'll record the final decision and any change to the ___.|criteria|Criteria are the rules used to assign categories consistently across examples.
'''),
scenario(
    title='The training job stopped after the last checkpoint',
    skill='Negotiate a recovery plan while distinguishing saved weights from complete training state.',
    setup='An interrupted training run reached step 12,400. The team has a complete checkpoint from step 12,000 and a weights-only export from step 12,300. The original environment configuration and data order are recorded.',
    cast='Dev|Training engineer\nRina|Research lead',
    dialogue='''
Rina|How much work did we lose when the job stopped?
Dev|Four hundred steps if we resume from the last complete [[checkpoint::Checkpoint means saved training state from a particular point, not necessarily the latest exported weights.]]. That was step 12,000.
Rina|I can see a file from 12,300. Why not use the newer one?
Dev|That's a weights-only export. It doesn't include the optimizer or scheduler state we need for the planned continuation.
Rina|So it could initialize another run, but it isn't the same recovery point?
Dev|Exactly. The complete checkpoint includes the [[optimizer state::Optimizer state stores training-update information beyond model weights, such as accumulated momentum values.]] as well as the model weights.
Rina|Is the 12,000 file intact?
Dev|Its checksum matches the saved record. I still need to load it in the approved environment and run a short recovery test.
Rina|Do that before reserving another full day of accelerators.
Dev|Agreed. I'll also verify the [[learning-rate schedule::Learning-rate schedule controls how the update rate changes as training progresses.]] resumes at the recorded point rather than starting over.
Rina|What about the examples already processed after that checkpoint?
Dev|The saved sampler position takes us back to 12,000. The replayed steps belong to the resumed run; I won't count them as new data coverage.
Rina|Can we promise exactly the same final weights as an uninterrupted run?
Dev|No. Matching the environment and random states helps [[reproducibility::Reproducibility concerns obtaining consistent results under documented conditions, not a universal guarantee of identical weights.]], but we shouldn't promise bit-for-bit identity without testing that claim.
Rina|Fair. Compare the recovery test with our saved loss trace, and flag unexpected behavior.
Dev|I'll keep the old logs and attach a new run identifier to the continuation.
Rina|Give me the estimated recovery cost after that test, including the repeated steps.
Dev|Will do. The estimate will separate compute time from the [[queue wait::Queue wait is time awaiting available resources, not time spent actively training the model.]] for the next reservation.
Rina|And the weights-only export?
Dev|Keep it labeled as an export, not a [[resume point::Resume point identifies the saved state from which the intended training process can continue.]]. That should prevent someone choosing it just because the timestamp is newer.
''',
    transfer_title='A run comparison uses different starting states',
    transfer_setup='A researcher compares a fully resumed run with a run initialized from exported weights and a fresh optimizer. The lead asks for an accurate experiment record.',
    transfer='''
Researcher: Both runs began with the same model ___, so I called them identical starts.|weights|Weights are shared, but optimizer and scheduler state can still differ.
Lead: One run used a fresh optimizer. Record that as a changed ___.|condition|Condition identifies an experimental difference that affects interpretation of the comparison.
Researcher: I'll distinguish the resumed run from the ___ run.|reinitialized|Reinitialized describes the run that reset training state instead of fully resuming it.
Lead: Good. Keep both results, but qualify the ___.|comparison|Comparison must acknowledge the different starting states rather than attributing all differences elsewhere.
'''),
scenario(
    title='A drafting assistant is about to become a sending agent',
    skill='Challenge excessive tool permissions and agree on a bounded agent workflow.',
    setup='An internal assistant drafts customer follow-up emails. A proposed update would let it send messages automatically. The product team wants a pilot; the security engineer reviews the tool permissions and approval step. No external sending has been approved.',
    cast='Nora|Product lead\nEli|Security engineer',
    dialogue='''
Nora|The drafts look good. Could we let the assistant send them during the pilot?
Eli|Sending changes the [[permission scope::Permission scope defines which actions and resources the assistant is authorized to use.]]. What exactly would it be allowed to send, and to whom?
Nora|Follow-up messages to contacts on an approved list. An employee would start each task.
Eli|Starting a task isn't approval of the final recipient and content. Could the employee review those before each send?
Nora|Yes, though we'd lose some of the time saving.
Eli|We'd still save drafting time. A [[human approval::Human approval is an explicit decision by a person about the proposed action, not merely launching the task.]] step lets the reviewer catch a wrong recipient or an unsupported promise.
Nora|Could the model skip that step if the customer email says a reply is urgent?
Eli|The tool service must enforce it. A request inside customer text doesn't authorize a send.
Nora|Then the model prepares a proposed action, and the service waits for approval?
Eli|Yes. Bind the approval to that exact recipient and message. If either changes, require a new approval.
Nora|The existing mail integration can also delete messages. We don't need that capability.
Eli|Remove it from the pilot. [[Least privilege::Least privilege limits available permissions to those needed for the defined task.]] means giving this workflow only the access it needs.
Nora|How do we test the full flow without accidentally contacting a customer?
Eli|Use a [[sandbox::Sandbox means an isolated test environment designed to prevent effects on real customer accounts.]] with test recipients and synthetic messages first.
Nora|I want the pilot report to show drafts accepted, drafts edited, and sends rejected by the control.
Eli|Add an [[audit log::Audit log is a record of actions and approvals used to reconstruct what happened.]] linking each approval to the action attempted and its outcome.
Nora|Suppose sending succeeds but the assistant times out waiting for the response. I don't want duplicate emails.
Eli|We need a tested retry policy and duplicate-prevention behavior at the service boundary. The model shouldn't guess whether to send again.
Nora|I'll narrow the pilot proposal to drafting and reviewed sends in the test environment.
Eli|Good. Keep a [[kill switch::Kill switch is a control that can stop the agent workflow promptly when needed.]] available to the named operator, and bring the evidence back before requesting external sending.
''',
    transfer_title='The approved draft changes before sending',
    transfer_setup='An employee approved an email addressed to a test contact. The assistant then revised the message to include a new promise.',
    transfer='''
Operator: The ___ no longer matches what I reviewed.|content|Content is the message text, which changed after the operator's approval.
Engineer: Then the previous approval must not authorize this ___.|send|Send is the consequential action that must match the reviewed message.
Operator: I'll request a fresh review of the exact recipient and ___.|draft|Draft is the proposed message that the reviewer must see before sending.
Engineer: Record the replacement approval and the action's final ___.|outcome|Outcome records whether the approved action succeeded, failed, or remained unresolved.
'''),
]
