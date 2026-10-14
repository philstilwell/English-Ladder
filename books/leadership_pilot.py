"""Independently revised leadership pilot; never imported by live course builds."""
from copy import deepcopy
import hashlib
import random
import re

from books.cross_cultural_leadership_content import UNITS as ORIGINAL_UNITS

TITLE = 'Cross-Cultural Leadership English'
SUBTITLE = 'Clear decisions. Constructive disagreement. Trusted teams.'
AUTHOR = 'Phil Stilwell'
COPYRIGHT = '\u00a9 2026 Phil Stilwell. All rights reserved.'
NOTICE = ('No part of this publication may be reproduced, stored in a retrieval system, '
          'or transmitted in any form or by any means without prior written permission '
          'from the author, except as permitted by law.')
EDITION = 'Revised 2026 edition'
COURSE_URL = 'https://englishladder.com/efsp-cultural-leadership-us-branches.html'


def q(prompt, correct, why, *alternatives):
    """Each alternative carries its own diagnostic explanation."""
    assert len(alternatives) == 3
    items = [(correct, why, True)] + [(a, reason, False) for a, reason in alternatives]
    random.Random(int(hashlib.sha256(prompt.encode()).hexdigest()[:12], 16)).shuffle(items)
    return dict(prompt=prompt, options=[a for a, _, _ in items],
                reasons=[b for _, b, _ in items], answer=next(i for i, x in enumerate(items) if x[2]))


def dialogue(text):
    turns, gaps = [], []
    for line in text.strip().splitlines():
        speaker, words = line.split('|', 1)
        def replace(match):
            answer, reason = match.group(1).split('::', 1)
            gaps.append(dict(answer=answer, reason=reason, turn=len(turns) + 1))
            return '{{' + str(len(gaps)) + '}}'
        turns.append((speaker, re.sub(r'\[\[(.*?)\]\]', replace, words)))
    return dict(dialogue=turns, gaps=gaps)


def make_unit(index, **changes):
    unit = deepcopy(ORIGINAL_UNITS[index - 1])
    unit.update(changes)
    unit['number'] = index
    return unit


UNITS = [
make_unit(1,
    artifact_title='Launch tracker / Wednesday, 11:00 a.m.',
    artifact_headers=['Item', 'Current record'],
    artifact_rows=[['Launch date', 'Monday, proposed'], ['Trained staff', '6 confirmed; 8 required'],
                   ['Friday training', '2 places booked; completion pending'],
                   ['Decision owner', 'Aiko, after Jordan reports the staffing check']],
    focus=[('authorization', 'au-thor-i-ZA-tion', 'We have support for the plan, but no authorization to launch.', 'Support is not permission.'),
           ('provisional', 'pro-VI-sion-al', 'Treat Monday as provisional until Friday\'s check.', 'Provisional is not confirmed.'),
           ('supersede', 'su-per-SEDE', 'This note supersedes the earlier minutes.', 'Supersede replaces a record; supplement adds to it.'),
           ('endorsement', 'en-DORSE-ment', 'Jordan endorsed the approach, not the date.', 'Name exactly what is endorsed.')],
    registers=[('To a colleague', 'So the approach works; Monday is still open?', 'In a decision record', 'The approach is supported. Launch authorization remains pending.'),
               ('Clarifying politely', 'I may have read too much into "fine."', 'Confirming formally', 'Please confirm whether your agreement includes the proposed date.')],
    checks=[
        q('Which statement can Aiko enter as confirmed now?', 'Six people have completed training.', 'The tracker confirms six completed trainees, not eight.',
          ('Eight people have places on Friday.', 'Only two places are booked for Friday; six people are already trained.'),
          ('Monday is approved subject to training.', 'The date is proposed. Aiko has not yet authorized even a conditional launch.'),
          ('Jordan has cleared the launch date.', 'Jordan checks staffing; the tracker assigns the decision to Aiko.')),
        q('Which next step preserves the decision boundary?', 'Jordan checks staffing; Aiko decides afterward.', 'Evidence gathering and authorization belong to different people here.',
          ('Jordan checks staffing and authorizes Monday.', 'Checking staffing does not transfer Aiko\'s decision right.'),
          ('Aiko authorizes now and checks Friday.', 'That reverses the stated sequence and treats a prerequisite as a later formality.'),
          ('Both trainees confirm and release the plan.', 'The trainees do not hold launch authority.')),
        q('Jordan says, "The approach is fine." Which follow-up resolves its scope?', 'Does that include Monday, or just the sequence?', 'The question separates the date from the approach without assigning a motive.',
          ('Can I tell the team you are fully aligned?', 'Fully aligned expands an ambiguous statement instead of clarifying it.'),
          ('Would a different date make you more comfortable?', 'That assumes the date is the concern before checking what Jordan meant.'),
          ('Shall I record approval and add your staffing note?', 'That labels the statement approval before establishing whether it was approval.')),
    ],
    choices=[
        q('Choose a correction to minutes that wrongly say "Monday approved."', 'Monday remains proposed; Aiko will decide after Friday\'s staffing check.', 'This corrects status, decision owner, and prerequisite together.',
          ('Monday remains approved; Jordan will add Friday\'s staffing figures.', 'It preserves the inaccurate approval status.'),
          ('Monday remains likely; the team will proceed unless someone objects.', 'Likelihood and silence do not provide the required authorization.'),
          ('Monday remains supported; the staffing check will follow the launch.', 'It reverses the sequence and leaves approval ambiguous.')),
        q('Which sentence distinguishes receipt from approval?', 'I have read the plan; I have not authorized the date.', 'Reading acknowledges receipt without implying permission.',
          ('I have read the plan; please regard the date as settled.', 'This explicitly makes the date final.'),
          ('I have accepted the plan; the date is now in place.', 'Accepted and in place suggest approval, not receipt alone.'),
          ('I have seen the plan; go ahead with the proposed date.', 'Go ahead grants the permission the sentence needs to withhold.')),
        q('Two training places are booked. What can the update say?', 'Both places are booked; completion still needs confirmation.', 'A booking is evidence of a plan, not completion.',
          ('Both people are ready; their training is scheduled Friday.', 'Ready overstates what a scheduled session establishes.'),
          ('Both people are confirmed; their assessment will follow later.', 'Confirmed leaves readiness implied before assessment.'),
          ('Both people are available; training will confirm the date.', 'Availability is not supplied, and training alone does not authorize the date.')),
        q('Aiko wants a final check without making Jordan defend his intentions. Choose her line.', 'What condition is missing from that summary?', 'It invites a factual correction without judging sincerity.',
          ('Why did you agree if you had a reservation?', 'It assumes Jordan agreed to the date, the disputed point.'),
          ('Are you committed enough to make Monday happen?', 'It shifts a staffing condition into a judgment of commitment.'),
          ('Can we leave your concern out until Friday?', 'It would hide a condition that affects the record now.')),
    ],
    **dialogue('''
Aiko|Before I send these minutes, can we check one line? I wrote "Monday launch approved." You said the plan was fine yesterday.
Jordan|The sequence was fine. I still had a [[reservation::A reservation limits Jordan's support; it does not withdraw support for the sequence.]] about staffing. I thought I mentioned that before we moved on.
Aiko|You did mention training. I took that as an update, not a condition. That was my mistake.
Jordan|We have six people trained. We need eight. Two more are booked for Friday, but booking them isn't the same as having them ready.
Aiko|Right. So Monday stays [[provisional::Provisional keeps the date open until the staffing check and decision.]]. I'll remove "approved" from the minutes.
Jordan|Thanks. I don't want the team to cancel anything yet, either. Monday could still work.
Aiko|Then I'll say we agree [[in principle::In principle expresses support for the approach without granting final approval.]] on the approach. The date remains open until Friday.
Jordan|That captures it. Who is going to tell the customer team? They've already asked me whether to send the launch notice.
Aiko|I will. Preparing the notice is fine; sending it needs my [[authorization::Authorization is permission from Aiko, who owns the launch decision.]]. We haven't reached that point.
Jordan|Good. I can give you the training results Friday afternoon. Do you need anything beyond the completion list?
Aiko|Yes, please check that all eight are available for the first shift. Training is a [[prerequisite::A prerequisite must be met before launch; it is not proof that all other conditions are met.]], not the entire readiness check.
Jordan|Understood. I'll confirm completion and first-shift availability. If one person doesn't finish, I'll flag that rather than count the booking.
Aiko|Please do. I'd rather have a clear [[go/no-go decision::A go/no-go decision explicitly determines whether the launch proceeds.]] than leave everyone interpreting "probably."
Jordan|Agreed. Could you copy me on the corrected minutes? People may still be looking at the first version.
Aiko|Yes. The new note will [[supersede::Supersede means replace the inaccurate earlier record, not add another equally valid version.]] the earlier one. I'll put that in the first sentence.
Jordan|And I'll reply to confirm the staffing wording. That isn't me signing off on the launch, though.
Aiko|Exactly. I'll keep your [[acknowledgment::Acknowledgment of receipt confirms that Jordan received the note; it is not his launch approval.]] of receipt separate from my launch decision.
Jordan|Then we're clear. Six trained today; two more pending; Monday not yet approved.
Aiko|That's the [[read-back::A read-back restates the shared record so the other person can correct it.]] I needed. Anything else I have interpreted too strongly?
Jordan|No. Once you've reviewed the Friday check, you can [[give the green light::Give the green light means authorize the launch; this verb phrase fits after can.]] or move the date. I'll wait for that message.
'''),
    transfer_title='A supplier says "looks good"',
    transfer_facts='Twelve test units are proposed for Tuesday. The supplier has acknowledged the design, but has not confirmed capacity. Maya owns the purchase decision. Ellis will check supplier capacity by Monday noon.',
    repair=[
        q('Repair the message "Twelve units approved for Tuesday."', 'Twelve units proposed; capacity and Maya\'s approval are pending.', 'The correction preserves both unresolved conditions.',
          ('Twelve units approved; Ellis will check capacity on Monday.', 'It still claims approval and treats capacity as an afterthought.'),
          ('Twelve units expected; supplier acknowledgment authorizes the order.', 'Acknowledging design does not grant purchasing authority.'),
          ('Twelve units booked; Maya will confirm receipt of the design.', 'Neither a booking nor this role for Maya is supplied.')),
        q('Ellis reports capacity is available. What can Maya now say?', 'Capacity is confirmed; I will make the purchase decision.', 'The new fact resolves capacity, not authorization.',
          ('Capacity is confirmed; your check authorizes the purchase.', 'Ellis\'s information does not itself authorize buying.'),
          ('Capacity is confirmed; Tuesday is now the agreed delivery.', 'Available capacity is not a confirmed delivery commitment.'),
          ('Capacity is confirmed; the design acknowledgment becomes approval.', 'One new fact does not change what the earlier message meant.')),
    ],
    transfer=dialogue('''
Maya|The supplier wrote "looks good." Does that cover the design or the delivery date?
Ellis|The design. Tuesday remains [[proposed::Proposed is the stated status of Tuesday; the supplier has not committed to it.]].
Maya|Then please check [[capacity::Capacity is the supplier's ability to supply the twelve units, the unresolved factual condition.]] by Monday noon.
Ellis|I will. Shall I place the order if they can supply twelve?
Maya|No. Bring the confirmation to me for [[approval::Maya retains the purchase decision even after capacity is confirmed.]].
Ellis|Understood. I'll send an update by noon, even if the supplier's answer is still [[pending::Pending means the supplier has not yet resolved the question.]].
'''),
    delivery='Stress DESIGN and DATE in the first question. Pause after "No" in Maya\'s reply, then state the next step without raising your volume.',
),
make_unit(2,
    artifact_title='Pilot proposal / workload assumptions',
    artifact_headers=['Measure', 'Proposal / available evidence'],
    artifact_rows=[['Duration', '6 weeks'], ['Staffing', '2 account managers; no extra allocation'],
                   ['Follow-up assumption', '2 hours per account per week'],
                   ['Previous trial', '4 hours per account per week'],
                   ['Open choice', 'Account count can change']],
    focus=[('premise', 'PREM-ise', 'The estimate rests on a two-hour premise.', 'A premise is an assumption, not a conclusion.'),
           ('concession', 'con-CES-sion', 'That concession does not settle the whole proposal.', 'Concede a point; do not concede to a point.'),
           ('feasibility', 'fea-si-BIL-i-ty', 'We need to check feasibility with two managers.', 'Feasible means possible within constraints, not desirable.'),
           ('extrapolate', 'ex-TRAP-o-late', 'Do not extrapolate a full rollout from this small pilot.', 'A sample may inform a decision without proving the outcome.')],
    registers=[('Spoken challenge', 'I don\'t buy the two-hour estimate.', 'Meeting record', 'The two-hour estimate was challenged on workload grounds.'),
               ('Firm boundary', 'The estimate is fair game. Personal remarks are not.', 'Return to the work', 'What count would you recommend with the same two managers?')],
    checks=[
        q('What can Mei change without requesting additional staffing?', 'The number of pilot accounts.', 'The case leaves the account count open within the same staffing allocation.',
          ('The number of assigned managers.', 'Additional staff need a separate approval.'),
          ('The hours recorded in the earlier trial.', 'Earlier evidence is not a planning variable.'),
          ('The meaning of confirmed workload.', 'Changing a label cannot establish an actual workload.')),
        q('Which comparison needs investigation before accepting the estimate?', 'Whether the two trials involve comparable follow-up.', 'The previous result matters only after checking which conditions carry over.',
          ('Whether a six-week duration implies half the effort.', 'Duration alone does not imply a reduction in weekly effort.'),
          ('Whether criticism means Chris opposes every pilot.', 'That is an inference about intent, not a workload comparison.'),
          ('Whether two managers can guarantee the outcome.', 'The case does not establish a guarantee, and the comparison is about effort.')),
        q('Which statement is a personal judgment rather than a task objection?', 'The planning team does not understand our customers.', 'It makes a broad competence judgment about people rather than identifying an estimate to test.',
          ('The follow-up estimate omits customer questions.', 'This identifies a testable omission in the estimate.'),
          ('The pilot count exceeds the current staffing limit.', 'This concerns whether the proposed work fits the available capacity.'),
          ('The earlier trial does not support this assumption.', 'This challenges the relationship between evidence and an assumption.')),
    ],
    choices=[
        q('Choose a concession that does not abandon the whole pilot.', 'The four-hour result matters; a smaller count may still work.', 'It accepts the evidence while keeping a narrower design open.',
          ('The four-hour result matters; the full pilot is therefore impossible.', 'That reaches a broader conclusion than the evidence establishes.'),
          ('The four-hour result matters; we can retain two hours for planning.', 'It acknowledges evidence without addressing the unsupported assumption.'),
          ('The four-hour result matters; we should add managers this week.', 'It commits to capacity outside Mei\'s stated authority.')),
        q('Chris questions the team\'s competence. Which response protects both people and scrutiny?', 'Keep the criticism on the estimate; show us the missing work.', 'It sets a conduct boundary and invites a substantive explanation.',
          ('Keep the criticism for later; let us approve the current estimate.', 'It postpones relevant scrutiny until after approval.'),
          ('Keep the criticism private; the team needs a united position today.', 'It suppresses the task objection in the decision meeting.'),
          ('Keep the criticism brief; your remark shows the concern is personal.', 'It guesses intent and does not set a clear behavioral boundary.')),
        q('Which conclusion is appropriately limited?', 'A smaller pilot can test workload before any wider rollout.', 'Testing provides information without guaranteeing that expansion will be justified.',
          ('A smaller pilot will validate the full rollout once it begins.', 'A smaller sample does not guarantee full-scale validity.'),
          ('A smaller pilot removes the need to monitor weekly effort.', 'Reduced scope does not eliminate measurement.'),
          ('A smaller pilot confirms the two-hour estimate is realistic.', 'The revised count supplies no evidence for the original time estimate.')),
        q('Which question invites an alternative within the stated limit?', 'What account count can the same two managers support?', 'It holds staffing fixed while opening the negotiable account count.',
          ('What headcount would preserve all the proposed pilot accounts?', 'It explores extra staffing rather than an option within this limit.'),
          ('What estimate would let us retain the current account count?', 'It invites adjustment of an estimate to fit a preferred result.'),
          ('What wording would secure approval of the existing pilot plan?', 'It focuses on persuasion without solving the capacity problem.')),
    ],
    **dialogue('''
Chris|I don't buy this estimate. Two managers cannot handle that many accounts and keep their normal work moving.
Mei|Which [[premise::Premise identifies the starting assumption Chris needs to challenge specifically.]] is wrong: two hours per account, or how many hours the managers have available?
Chris|Two hours. The last trial took four. Most of it was customer follow-up, and your new template won't remove that.
Tessa|I've got the log here. There were fewer handoffs, too, so four hours isn't an obviously inflated [[baseline::Baseline is the reference figure for comparing the new estimate with the earlier trial.]].
Mei|All right, I [[concede::Concede accepts this point while leaving the wider design open.]] the template won't halve the workload. Can we make a smaller pilot useful?
Chris|We could, but the team that wrote this clearly doesn't understand the customers.
Mei|The estimate is fair game. That [[personal remark::Personal remark names the comment about the team's competence, not the workload objection.]] isn't. Which customer tasks are missing from the sheet?
Chris|Fair correction. Follow-up calls and escalations. I should have said that rather than judging the team.
Tessa|Those are in the trial log. If we start with half the accounts, the same two managers could cover the recorded hours.
Mei|That sounds [[feasible::Feasible means workable within the two-manager limit; it describes the alternative rather than naming a new proposal.]]. What would we lose by halving the count?
Chris|Coverage. We might miss a customer type that creates more work. I wouldn't use a small sample to promise the same result everywhere.
Mei|Neither would I. We can get [[directional evidence::Directional evidence can indicate a pattern without supporting a firm general conclusion.]] without claiming it proves the full rollout will work.
Tessa|Could we include more than one customer type, then check the actual hours after week one?
Mei|Yes. Keep the two-manager limit [[non-negotiable::Non-negotiable marks staffing as fixed for this decision, unlike the account count.]] and revise the mix and count around it.
Chris|I can work with that. I'd also like a stop point if the pilot starts taking time from existing accounts.
Tessa|I'll propose a workload threshold with operations. We haven't agreed the number yet, so I'll mark it open.
Mei|Good. We have [[common ground::Common ground is the shared aim of useful evidence without overloading the team.]] on protecting existing work. We still need the count and threshold.
Chris|And I'll correct my comment when I circulate the revision. The sheet missed tasks; I had no basis to question the team's knowledge.
Mei|Thanks. Your [[pushback::Pushback is resistance to the proposal; Mei accepts the useful challenge without endorsing the personal comment.]] improved the plan. The personal part needed correcting.
Tessa|I'll update the assumptions and bring the [[counterproposal::Counterproposal is the revised pilot design offered in place of the original.]] to tomorrow's review. No expansion until we've checked the first results.
'''),
    cast=[('Mei', 'Branch manager'), ('Chris', 'Commercial lead'), ('Tessa', 'Operations analyst')],
    transfer_title='A forecast with three unconfirmed renewals',
    transfer_facts='A forecast lists ten confirmed renewals, but only seven customers have confirmed. Three are still deciding. Priya can correct the forecast; she cannot promise the remaining renewals.',
    repair=[
        q('Repair "Ten customers have committed to renew."', 'Seven have confirmed; three decisions remain open.', 'The correction separates established facts from possible outcomes.',
          ('Ten are expected; the remaining three are therefore confirmed.', 'Expected does not mean committed.'),
          ('Seven have confirmed; remove the other three permanently.', 'Unconfirmed does not mean lost.'),
          ('Ten are provisional; all seven confirmations need repeating.', 'This unnecessarily downgrades the seven established confirmations.')),
        q('Which challenge requests evidence without questioning competence?', 'What confirmations support the other three entries?', 'It asks for the missing basis of the claim.',
          ('Why did your team publish such an unrealistic number?', 'It embeds a judgment before asking for the evidence.'),
          ('Can your team guarantee all three remaining renewals?', 'A guarantee is not a substitute for current confirmations.'),
          ('Would softer wording keep the ten-renewal total approved?', 'Changing tone would not repair the underlying status error.')),
    ],
    transfer=dialogue('''
Priya|I accept the seven confirmations. The other three need a different [[status::Status separates confirmed renewals from pending decisions.]].
Noah|So you want to remove those customers from the forecast?
Priya|No. Keep them as [[pending::Pending means the customers are still deciding, not that the renewals are lost.]], not confirmed.
Noah|That's a narrower correction than I expected. I'll change the [[label::Label is the field that currently misstates the renewal status.]].
Priya|Thanks. Please keep the customer confirmations attached as [[evidence::Evidence supports the seven confirmed entries without inventing confirmations for the other three.]].
Noah|Will do. The total under discussion stays ten; the confirmed count is seven.
'''),
    delivery='Pause after "No" and contrast PENDING with CONFIRMED. Keep the distinction firm without making "you" the stressed word.',
),
make_unit(3,
    artifact_title='Two-week onboarding trial / authority card',
    artifact_headers=['Decision', 'Authority in this trial'],
    artifact_rows=[['Internal task order', 'Alex may decide'], ['Customer promises', 'Sofia must approve'],
                   ['Additional spending', 'Sofia must approve'], ['Continuation', 'Review after 2 weeks; no automatic extension']],
    focus=[('discretion', 'dis-CRE-tion', 'Use your discretion on task order, within these limits.', 'Discretion is bounded choice, not unlimited authority.'),
           ('accountability', 'ac-count-a-BIL-i-ty', 'Delegation does not remove my accountability for the trial.', 'Doing a task and answering for its result are different roles.'),
           ('remit', 'RE-mit', 'Buying software is outside this trial\'s remit.', 'Remit means assigned scope; permission concerns a particular action.'),
           ('consultation', 'con-sul-TA-tion', 'Consultation gives us input; Sofia makes the spending decision.', 'Consultation is not a vote or automatic consent.')],
    registers=[('Everyday instruction', 'You can reorder the internal tasks.', 'Authority record', 'Alex has delegated authority over internal task sequencing.'),
               ('Recommendation', 'I recommend buying the scheduling tool.', 'Authorization', 'I approve the additional purchase. These are not interchangeable.')],
    checks=[
        q('Which action is already within Alex\'s authority?', 'Move an internal check earlier in the task order.', 'Internal sequence changes are explicitly delegated.',
          ('Promise a customer an earlier completion date.', 'Customer promises require Sofia\'s approval.'),
          ('Buy a small tool to speed the trial up.', 'Additional spending is reserved, with no small-purchase exception.'),
          ('Extend the trial if the team prefers it.', 'Continuation requires a review, not a team preference alone.')),
        q('The team recommends a paid tool. What happens next?', 'Alex brings the proposal to Sofia for approval.', 'The team may recommend; spending authority remains with Sofia.',
          ('Alex buys it and informs Sofia afterward.', 'Informing after purchase would bypass the retained approval right.'),
          ('The team votes and Alex treats that as approval.', 'A vote does not change who controls spending.'),
          ('Sofia delegates all trial decisions to the vendor.', 'The case does not authorize this transfer of authority.')),
        q('What does the two-week checkpoint establish?', 'A point to review continuation, not an extension.', 'A checkpoint is a decision occasion, not advance permission.',
          ('An extension unless Sofia actively objects.', 'Silence is not the stated continuation rule.'),
          ('An end to Sofia\'s oversight of the trial.', 'Oversight has not been delegated away.'),
          ('An automatic return to the original sequence.', 'The review may choose an outcome; it is not predetermined.')),
    ],
    choices=[
        q('Which instruction delegates clearly without disappearing?', 'Choose the internal sequence; bring spending and promises back to me.', 'The line gives autonomy and names the reserved decisions.',
          ('Use your judgment; tell me later about any changes you make.', 'This leaves limits unstated and invites after-the-fact approval.'),
          ('Take full ownership; keep every customer date exactly as proposed.', 'Full ownership is ambiguous, and proposed dates are not necessarily approved.'),
          ('Consult the team; treat their agreement as permission to proceed.', 'Team agreement cannot replace Sofia\'s reserved authority.')),
        q('Alex hears "You own this." Which clarification is most useful?', 'Does that include purchases, or just the internal sequence?', 'It checks an actual decision boundary rather than a vague level of trust.',
          ('Does that mean you trust the team to handle every issue?', 'Trust is not a definition of authority.'),
          ('Does that mean I can stop sending you trial information?', 'Ownership does not imply the end of oversight.'),
          ('Does that mean customer dates no longer need documenting?', 'Documentation requirements do not disappear with ownership.')),
        q('Which escalation happens at the right time?', 'The change affects a customer promise; I need approval before offering it.', 'It asks before creating the commitment.',
          ('The change affects a customer promise; I will seek approval after acceptance.', 'The customer would already have accepted a promise.'),
          ('The change affects a customer promise; I will mention it at the final review.', 'Waiting until review delays a required prior approval.'),
          ('The change affects a customer promise; I will let the team approve it.', 'The team does not hold that approval right.')),
        q('Choose a record that distinguishes consultation from decision.', 'Alex gathered team input; Sofia will decide on the purchase.', 'It separates the information-gathering role from the approval role.',
          ('Alex gathered team input; that input authorizes the purchase.', 'Consultation does not itself grant spending authority.'),
          ('Alex gathered team input; the vendor now owns the decision.', 'Nothing in the consultation transfers authority to the vendor.'),
          ('Alex gathered team input; Sofia\'s silence will count as consent.', 'No silence-as-consent rule is supplied.')),
    ],
    **dialogue('''
Alex|Can we stop sending every tiny sequence change to you? Yesterday we waited half a day to move one internal check.
Sofia|Yes. I've made myself a bottleneck. Let's make the [[decision rights::Decision rights specify who may decide which kinds of changes.]] explicit for this two-week trial.
Alex|I'd like the team to choose the order. They see the queues before either of us does.
Sofia|That's [[within your remit::Within your remit places the internal task order inside Alex's assigned responsibility.]]. You can change the sequence without asking me each time.
Alex|Including moving a customer delivery forward if it helps the queue?
Sofia|No, that's the [[approval boundary::Approval boundary marks where delegated sequence choices stop and Sofia's approval is required.]]. Internal order is yours; customer promises still come to me.
Alex|Got it. Suppose the new order needs a paid scheduling tool?
Sofia|Recommend it, with the cost. You can [[use discretion::Use discretion means exercise judgment inside the delegated limits, not approve additional spending.]] on the internal sequence; buying the tool still needs my approval.
Alex|So I can make a recommendation, but not place an order. I'd rather know that now than find out after a purchase.
Sofia|Exactly. Those are the two guardrails: no extra spending and no changed customer promises [[without approval::Without approval states the condition required before Alex can cross either delegated limit.]].
Alex|Can I ask the team for a quick vote on the sequence?
Sofia|You can consult them. You remain the [[decision owner::Decision owner is the person who decides the internal sequence, rather than treating a vote as required authority.]] for that sequence; you don't need unanimous agreement.
Alex|That helps. I'll explain what we chose and record the concern if someone sees a risk.
Sofia|Please do. And use the existing tracker so I can [[keep oversight::Keep oversight means monitor the trial without personally approving every delegated choice.]] without becoming another approval step.
Alex|How often do you want an update? I don't want to replace ten approval requests with ten progress emails.
Sofia|One summary at the end of each week. Escalate earlier if the change [[requires approval::Requires approval identifies a spending or customer-promise decision that must come back before action.]] under either limit we just named.
Alex|Before I make the promise or spend the money, not after. And the trial ends after two weeks?
Sofia|We review it then. That [[decision gate::Decision gate is the checkpoint at which continuation is assessed, not pre-approved.]] is not automatic permission to continue.
Alex|I'll put that on the authority card. The sequence is mine; spending and promises come back to you; we review continuation together.
Sofia|Good. I'm delegating choices, not dropping [[accountability::Accountability is Sofia's continuing obligation to answer for the trial and its oversight.]]. Bring me a recommendation if the boundaries stop the trial from being useful.
'''),
    transfer_title='A venue change inside a fixed budget',
    transfer_facts='Nora may move an internal workshop between existing rooms. Any external booking requires Luis\'s approval, even if its price is low. Nora must recommend an option before Monday\'s review.',
    repair=[
        q('Repair "Any inexpensive room change is approved."', 'Existing-room changes are delegated; external bookings need Luis\'s approval.', 'The boundary concerns booking type, not price.',
          ('Low-cost external bookings are delegated; larger ones need Luis\'s approval.', 'No price threshold has been authorized.'),
          ('All room changes are delegated; Luis only reviews the final schedule.', 'This removes the stated external-booking boundary.'),
          ('Existing-room changes need approval; external options can be booked provisionally.', 'This reverses the boundary and invents provisional booking permission.')),
        q('The team favors an external room. What can Nora report?', 'The team recommends it; the booking is not yet authorized.', 'A recommendation and permission remain separate.',
          ('The team supports it; the vote authorizes the booking.', 'The vote does not transfer Luis\'s authority.'),
          ('The price is low; the external room is already within my remit.', 'Price does not change the stated booking boundary.'),
          ('The review is Monday; the room is approved until then.', 'A future review does not supply temporary approval.')),
    ],
    transfer=dialogue('''
Nora|The team recommends the external room, but I have not made a [[booking::Booking would commit to the external option, which requires Luis's approval.]].
Luis|Good. Is there an internal alternative?
Nora|Yes. Moving to room B is within my [[authority::Authority describes the delegated right to choose between existing rooms.]].
Luis|Bring both options to Monday's review. I want your [[recommendation::Recommendation is Nora's preferred option with its basis, not a completed reservation.]].
Nora|I'll include the costs and wait for your [[decision::Decision is the approval Luis retains for the external option.]] before reserving anything outside.
Luis|That works. You can still move the internal session if you need to.
'''),
    delivery='Contrast RECOMMEND with BOOK. Pause before "before reserving anything outside" so the timing of approval is clear.',
),
make_unit(4,
    artifact_title='Reporting options / all times New York local time',
    artifact_headers=['Version', 'Earliest supported delivery', 'Status'],
    artifact_rows=[['Planning estimate', 'Friday, 3 p.m.', 'Provisional; reconciliation incomplete'],
                   ['Verified figures', 'Monday, noon', 'After Monday-morning reconciliation'],
                   ['Choice owner', 'Priya', 'Can choose version, not accelerate supplier work']],
    focus=[('reconciliation', 'rec-on-cil-i-A-tion', 'Verification depends on supplier reconciliation.', 'Reconciliation checks records against one another; it is not presentation formatting.'),
           ('provisional estimate', 'pro-VI-sion-al ES-ti-mate', 'The Friday version is a provisional estimate.', 'An estimate can be useful without being verified.'),
           ('caveat', 'CA-ve-at', 'Keep the caveat attached when you forward the slide.', 'A caveat qualifies a claim; it is not a separate correction later.'),
           ('acceptance criteria', 'ac-CEP-tance cri-TE-ri-a', 'The acceptance criteria specify a labeled estimate.', 'Criteria is plural; criterion is singular.')],
    registers=[('Firm spoken limit', 'I can send an estimate Friday, not verified figures.', 'Written delivery line', 'Friday, 3 p.m. New York time: provisional planning estimate.'),
               ('Clarify the purpose', 'What does the meeting need to decide?', 'Protect a qualification', 'Please retain "provisional" wherever these figures are reused.')],
    checks=[
        q('What is available by Friday at 3 p.m. New York time?', 'An estimate labeled provisional.', 'That is the supported Friday deliverable.',
          ('Verified figures with supplier approval.', 'Supplier reconciliation finishes Monday morning, not Friday.'),
          ('A final report awaiting a cosmetic update.', 'The missing work is verification, not cosmetic formatting.'),
          ('A confirmed result with an optional caveat.', 'The estimate is not confirmed and the provisional label is required.')),
        q('Which constraint can Priya change in this case?', 'The version selected for Friday\'s meeting.', 'Priya may choose a reporting option.',
          ('The supplier reconciliation completion time.', 'She cannot make that work finish early.'),
          ('The meaning of a verified figure.', 'A preference does not make unchecked figures verified.'),
          ('The requirement to label an estimate.', 'The case requires the provisional label.')),
        q('Which detail prevents a cross-office deadline misunderstanding?', 'Friday, 3 p.m., New York local time.', 'The day, clock time, and location are explicit.',
          ('Friday afternoon, before close of business.', 'Afternoon and close of business vary by location and organization.'),
          ('Friday, before the sponsor finishes work.', 'The sponsor\'s finishing time and location are not specified.'),
          ('Friday, at the branch\'s usual reporting time.', 'The usual time is not supplied to every recipient.')),
    ],
    choices=[
        q('Choose a firm commitment Omar can support.', 'I can send a provisional estimate Friday at 3 p.m. New York time.', 'This states a feasible version and a precise delivery time.',
          ('I can send verified figures Friday if the meeting needs them urgently.', 'Urgency does not remove the Monday dependency.'),
          ('I can send a final Friday report and verify its figures on Monday.', 'Calling it final before verification misstates its status.'),
          ('I can send confirmed numbers Friday with a note about Monday\'s check.', 'A note does not turn an estimate into confirmed numbers.')),
        q('Priya says "Just do your best." What should Omar clarify?', 'I can commit to the estimate; verification still needs Monday\'s check.', 'The response turns effort language into a bounded deliverable.',
          ('I will aim for verified figures; let us leave the exact version open.', 'This preserves the misunderstanding rather than defining the commitment.'),
          ('I will treat your request as approval to skip the supplier check.', 'Best effort is not authorization to bypass verification.'),
          ('I will label the report final so that the meeting can proceed.', 'A label cannot supply missing evidence.')),
        q('Which wording preserves the caveat when figures are forwarded?', 'Retain "provisional" on the slide and in the covering message.', 'The qualification travels with the numbers in both places.',
          ('Remove "provisional" from the slide but keep it in our private notes.', 'Recipients of the slide would lose the qualification.'),
          ('Retain "provisional" until the presentation begins on Friday.', 'The meeting time does not resolve the Monday verification dependency.'),
          ('Replace "provisional" with "confirmed" if nobody raises a concern.', 'Silence provides no evidence of verification.')),
        q('Supplier reconciliation slips. What is the responsible fallback?', 'Send a status update and a revised verification time.', 'It reports the changed dependency without passing off unchecked numbers as final.',
          ('Release the estimate as verified to preserve the original deadline.', 'Meeting a deadline does not justify changing the evidence status.'),
          ('Keep Monday\'s label and send the figures without mentioning the delay.', 'This hides information recipients need to interpret the report.'),
          ('Wait for final figures and let the agreed update deadline pass.', 'The manager can still provide a timely update even if the result is delayed.')),
    ],
    **dialogue('''
Priya|I need the branch figures for Friday's planning meeting. Can you get me the final version by three?
Omar|An estimate, yes. [[Verified::Verified means checked, which cannot happen before the supplier reconciliation.]] figures, no. The supplier reconciliation won't finish until Monday morning.
Priya|We've had this meeting booked for weeks. What can I actually show the directors?
Omar|A planning estimate labeled [[provisional::Provisional marks the figures as subject to verification rather than final.]]. What decision do they need to make on Friday?
Priya|They need to choose which branches to examine first. They aren't approving the final allocation yet.
Omar|Then the estimate may serve that purpose. The [[trade-off::Trade-off describes earlier availability in exchange for figures that are not yet verified.]] is speed versus verification, not a choice between sending something and sending nothing.
Priya|Can we keep the slide simple? A large warning makes it look as if we haven't done the work.
Omar|We can keep it short, but the [[caveat::Caveat is the qualification that tells readers how to interpret the estimate.]] has to stay. "Provisional; supplier check pending" would do it.
Priya|All right. Three on Friday means my afternoon. You're in New York, correct?
Omar|Yes. Let's make the [[deadline::Deadline is the exact delivery time, not a general effort promise.]] three p.m. New York time. Does that reach you before the meeting?
Priya|It does. Could you include the other two branches while you're at it?
Omar|Not within that [[scope::Scope is the set of work covered by this agreed version.]]. I can send this branch on Friday. Adding two more means changing the date or assigning help.
Priya|Keep this branch. I'll tell the directors what is and isn't in the version.
Omar|Thanks. The supplier check is the [[dependency::Dependency is work that must finish before verified figures can be supplied.]] for Monday. More formatting time won't make it finish earlier.
Priya|Understood. Monday at noon, New York time, for the verified figures?
Omar|Yes, based on the check finishing that morning. If it slips, I'll send a status update by noon rather than an unchecked final report.
Priya|That gives me a [[contingency::Contingency is the agreed fallback if the supplier check is delayed.]]. Please put both delivery lines in the same message.
Omar|I will. Friday estimate, Monday verification or a status update if the dependency moves. Please keep the label when you forward the numbers.
Priya|Agreed. I'll use the Friday version only to [[prioritize::Prioritize means choose which branch reviews should come first, not approve the final resource allocation.]] the reviews, not as approval of the allocation.
Omar|Then we have clear [[acceptance criteria::Acceptance criteria specify what the agreed Friday deliverable must contain and how its status is identified.]]: this branch, labeled estimate, three p.m. New York time. I'll send the confirmation now.
'''),
    transfer_title='A translation deadline with two deliverables',
    transfer_facts='A client wants a six-page internal briefing Friday. Nia can send the translated text Friday at 2 p.m. New York time. Independent language review finishes Monday at 11 a.m. New York time. Friday\'s version must be labeled "review pending."',
    repair=[
        q('Repair "Reviewed translation available Friday."', 'Translation Friday; independent review completed Monday.', 'The wording separates translation from its later independent review.',
          ('Reviewed translation Friday; reviewer confirmation follows Monday.', 'It still calls the Friday version reviewed.'),
          ('Translation Monday; the Friday text must not be used internally.', 'The facts permit a labeled Friday internal version.'),
          ('Translation Friday; review becomes optional after client acceptance.', 'The case provides no waiver of review.')),
        q('Which Friday covering line preserves the limitation?', 'Internal briefing text attached; independent review is pending.', 'It names the supplied text and its unresolved review status.',
          ('Final reviewed text attached; minor language checks follow Monday.', 'It contradicts the stated review status.'),
          ('Approved text attached; please ignore any earlier review labels.', 'No approval or removal of labels has been supplied.'),
          ('Finished text attached; the reviewer has been informed of delivery.', 'Informing the reviewer does not communicate that review is incomplete.')),
    ],
    transfer=dialogue('''
Nia|I can send the translated text Friday. The independent [[review::Review is the separate quality-check stage, not the initial translation.]] finishes Monday.
Client|Can the directors use Friday's text for their internal briefing?
Nia|Yes, with "review pending" kept on that [[version::Version identifies the particular Friday text, which differs in status from Monday's reviewed text.]].
Client|Then Friday is a text delivery, not a final [[sign-off::Sign-off means approval, which the incomplete independent review cannot yet provide.]].
Nia|Exactly. I'll confirm both delivery times in New York local time, including Monday's [[checkpoint::Checkpoint is the scheduled completion of independent review, not an extra translation order.]].
Client|Please do. I'll keep the review label in the briefing pack.
'''),
    delivery='Stress TEXT in "text delivery" and FINAL in "final sign-off." Read both times with the location, even when the other person seems to know it.',
),
make_unit(5,
    artifact_title='Meeting panel / 15 minutes remaining',
    artifact_headers=['Channel', 'Information available'],
    artifact_rows=[['Room discussion', 'Ben has prepared the customer-service schedule'],
                   ['Chat: Arun', 'Routing check incomplete; concern not yet discussed'],
                   ['Launch condition', 'Routing must be checked before go-live'],
                   ['Decision owner', 'Leila']],
    focus=[('crosstalk', 'CROSS-talk', 'The remote team cannot follow the crosstalk.', 'Crosstalk is overlapping speech, not substantive disagreement.'),
           ('paraphrase', 'PAR-a-phrase', 'Let me paraphrase the routing concern.', 'Paraphrase meaning; do not replace it with your preferred interpretation.'),
           ('dissent', 'dis-SENT', 'The record should preserve Arun\'s dissent.', 'Dissent is disagreement, not personal disloyalty.'),
           ('asynchronous', 'a-SYN-chro-nous', 'Send asynchronous input before the next review.', 'The contributions need not arrive at the same time.')],
    registers=[('Taking a turn', 'Can I come in on routing before we move on?', 'Chairing a turn', 'Arun first, then Ben. We need the routing result before a decision.'),
               ('Spoken summary', 'Staffing is ready; routing is not checked yet.', 'Decision log', 'Go-live remains pending. Arun owns the routing check; Leila owns the decision.')],
    checks=[
        q('Which issue is easy to miss in the current discussion?', 'Arun\'s unaddressed routing concern in chat.', 'The concern is present but has not been heard or answered.',
          ('Ben\'s unprepared customer-service schedule.', 'The schedule is prepared; routing is the unresolved condition.'),
          ('Leila\'s completed authorization of go-live.', 'Leila owns the decision but has not made it.'),
          ('The team\'s agreed removal of routing checks.', 'No removal of the check is supplied.')),
        q('What prevents the team from treating the queue as ready?', 'The routing check is not complete.', 'The case makes that check a go-live condition.',
          ('The meeting has only fifteen minutes left.', 'Time pressure affects the discussion but does not itself establish readiness.'),
          ('The customer-service schedule is prepared.', 'Preparation of one workstream is not a reason to stop; it also cannot resolve routing.'),
          ('Arun entered the concern through chat.', 'The communication channel does not make the concern less valid.')),
        q('Who should state the go-live decision after the evidence is reviewed?', 'Leila, the named decision owner.', 'The case retains that decision with Leila.',
          ('Ben, because the service schedule is ready.', 'Owning a prepared schedule is not launch authority.'),
          ('Arun, because he checks the routing.', 'Providing technical evidence does not transfer Leila\'s authority.'),
          ('The last speaker, if nobody objects.', 'Speaking order and silence do not determine decision rights.')),
    ],
    choices=[
        q('Ben interrupts Arun. Choose an intervention that protects both turns.', 'Arun, finish the routing point. Ben, you are next.', 'It protects the current speaker while specifying a later turn for Ben.',
          ('Ben, finish quickly. Arun can add anything important by email.', 'This rewards the interruption and removes the remote speaker from the decision discussion.'),
          ('Arun, let Ben finish. We already have your concern in chat.', 'Having a chat message is not the same as hearing and resolving its point.'),
          ('Both of you, keep going. I will combine your points afterward.', 'This preserves the crosstalk that prevents people from hearing.')),
        q('Which paraphrase preserves Arun\'s concern?', 'Routing is unverified; a ready schedule does not settle it.', 'It keeps the routing condition distinct from staffing readiness.',
          ('Routing is rejected; Arun recommends canceling the entire service.', 'Unverified does not mean rejected or canceled.'),
          ('Routing is ready; Arun prefers a later launch for convenience.', 'It changes an unverified condition into readiness and invents a motive.'),
          ('Routing is routine; Arun can finish it after customers arrive.', 'This removes the before-go-live requirement.')),
        q('The discussion drifts to slide design. Which line parks it responsibly?', 'Ben, bring the slide choice Thursday; routing comes first now.', 'It assigns the deferred issue a return point while protecting the current priority.',
          ('Ben, leave the slide choice open; we will remember it later.', 'No owner or return point prevents the item from disappearing.'),
          ('Ben, settle the slide choice now; routing can wait until launch.', 'This prioritizes presentation over a prerequisite.'),
          ('Ben, drop the slide choice; it has no value to anyone here.', 'This dismisses the issue rather than deferring it with ownership.')),
        q('Which closing record is accurate before the routing result arrives?', 'Checks assigned; go-live not yet authorized.', 'Assigning checks is progress, but it is not approval.',
          ('Go-live authorized; routing information to follow.', 'It approves before the required check.'),
          ('Schedule rejected; customer-service preparation must restart.', 'The schedule is ready and has not been rejected.'),
          ('Arun dissents; his silence later will count as approval.', 'Silence cannot replace the check or Leila\'s decision.')),
    ],
    **dialogue('''
Ben|The schedule is ready, so can we confirm go-live? I need to tell the supervisors before they leave.
Arun|I've put a routing issue in chat. The check isn't finished, and one of the queues might still send cases to the old team.
Ben|We can fix a routing detail after we start. The staffing is the difficult part, and that's done.
Leila|Pause. We have [[crosstalk::Crosstalk is overlapping speech that prevents the remote contribution from being heard.]], and Arun hasn't finished. Arun, you have the floor; Ben, you're next.
Arun|Thanks. I haven't confirmed a fault. I'm saying the routing is [[unverified::Unverified means not yet checked; it does not assert that a fault has been found.]]. We need the result before we send customers into the queue.
Leila|So the schedule is ready, but readiness depends on a separate routing check. Is that a fair [[paraphrase::Paraphrase restates Arun's meaning while inviting correction.]]?
Arun|Yes. I'm not asking to redo the schedule. I need time to finish the check.
Ben|That helps. I heard "the whole launch isn't ready," and thought you wanted us to start planning again.
Leila|Let's keep the two workstreams separate. We have fifteen minutes, so I'll [[timebox::Timebox means set a limit on this discussion, not waive a required check.]] this item to five minutes to agree the next actions.
Ben|Can we also settle which slide the supervisors will see? I have two versions and the colors are confusing.
Leila|Put the slide choice in the [[parking lot::Parking lot means a deferred discussion list, not a decision to discard the issue.]]. Bring it back Thursday. First, what does Arun need to finish routing?
Arun|Access to the current mapping file. I only have yesterday's version. Ben, can you send the link you used?
Ben|Yes, now. I didn't realize we were working from different versions.
Arun|I've got it. I'll check the mapping and report the result by three p.m. New York time.
Leila|That's the [[action item::Action item is the specific check with an owner and reporting time.]]. Ben sends the file; Arun checks and reports; I make the go-live decision.
Ben|Can I tell the supervisors we're likely to start, provided the result is clear?
Leila|Tell them the [[decision is pending::Decision is pending states that preparation is complete in one area but launch authorization has not been given.]]. I'd rather not have a conditional message become "approved" as it gets passed on.
Arun|Please include that the issue was an unfinished check, not a confirmed routing failure.
Leila|I will. The [[decision log::Decision log preserves what was and was not decided, including Arun's actual concern.]] will distinguish those. Before we close, any [[unresolved question::Unresolved question invites missing information without treating silence as authorization.]] about who does what?
Ben|No. I'll [[recap the next steps::Recap the next steps is a verb phrase meaning summarize the actions, without presenting them as a launch decision.]] for the supervisors: schedule ready, routing check due at three, launch decision still with Leila.
'''),
    transfer_title='A remote colleague flags a missing translation check',
    transfer_facts='A product demonstration is prepared. Remote reviewer Ines says the Spanish labels have not been checked. Chair Noah must decide whether to release the demonstration. Pavel has prepared the slides; no release has been authorized.',
    repair=[
        q('Repair "Ines wants to delay the demonstration."', 'Ines reports an unfinished Spanish-label check.', 'It records her actual information without inferring her preference.',
          ('Ines rejects the demonstration and requests a new slide deck.', 'Neither rejection nor a new-deck request is supplied.'),
          ('Ines confirms the labels but prefers a later release.', 'It reverses the status and invents a preference.'),
          ('Ines has a translation preference that does not affect readiness.', 'The line dismisses the check without evidence.')),
        q('Which chairing line gives the missed concern a fair hearing?', 'Ines, explain the unchecked labels; Pavel, respond after her.', 'It makes space for evidence and preserves a turn for Pavel.',
          ('Pavel, finish first; Ines can send the result after release.', 'It delays relevant information until after the decision.'),
          ('Ines, summarize by email; we already understand the concern.', 'Understanding is assumed although the concern has not been heard.'),
          ('Both, discuss it separately; I will release the demonstration now.', 'It authorizes release before considering the unresolved check.')),
    ],
    transfer=dialogue('''
Noah|Ines has the [[floor::The floor is the right to speak without being cut off at this point in the meeting.]]. Pavel, I'll come to you next.
Ines|The labels are [[unchecked::Unchecked means their quality has not been verified; it does not assert that they are wrong.]], not necessarily wrong.
Pavel|Understood. I'll send the exact slide version you need.
Noah|Good. Ines, check that version. The release decision remains [[pending::Pending preserves Noah's decision until the check has been considered.]].
Ines|I'll report the result, including anything still unresolved.
Noah|I'll record the result and the decision separately in the [[recap::Recap summarizes the evidence and decision without turning one into the other.]].
'''),
    delivery='Use a calm falling tone for "Ines has the floor." Contrast UNCHECKED with WRONG, then pause before naming the next owner.',
),
make_unit(6,
    artifact_title='Report handoff / two-week record',
    artifact_headers=['Item', 'Observed record'],
    artifact_rows=[['Agreed deadline', 'Thursday, noon'], ['Week 1 arrival', 'Friday morning'],
                   ['Week 2 arrival', 'Friday morning'], ['Effect', 'Planning deferred a staffing update'],
                   ['Dependency', 'Diego needs a source file from another team; cause not yet established']],
    focus=[('attribution', 'at-tri-BU-tion', 'Calling the delay carelessness is an attribution, not an observation.', 'Describe arrival times before drawing conclusions about motive.'),
           ('bottleneck', 'BOT-tle-neck', 'The source-file handoff is a possible bottleneck.', 'Possible cause is not yet established cause.'),
           ('recurrence', 're-CUR-rence', 'An early warning may help prevent recurrence.', 'Preventing recurrence requires a changed process, not a vague promise.'),
           ('follow-through', 'FOL-low-through', 'We will check follow-through at the next review.', 'Follow-through means completing agreed action, not just agreeing to it.')],
    registers=[('Observed fact', 'Both reports arrived Friday morning.', 'Unsupported interpretation', 'You do not take the deadline seriously. Avoid presenting this as a fact.'),
               ('Concrete support', 'I will speak to the source-team manager.', 'Specific expectation', 'Flag a missing source file by Wednesday at three.')],
    checks=[
        q('Which opening is supported by the record?', 'Both reports arrived after the Thursday-noon deadline.', 'The arrival and due times are observed facts.',
          ('Diego chose to prioritize other work over the report.', 'His priorities and choices have not been established.'),
          ('The source team caused both delays through negligence.', 'There is a dependency, but cause and negligence are not established.'),
          ('Planning changed its deadline without telling Diego.', 'No changed deadline is supplied.')),
        q('Which consequence can Elena describe without adding facts?', 'Planning deferred its staffing update.', 'That is the stated effect of the late reports.',
          ('A customer contract was lost after the delay.', 'No lost contract is reported.'),
          ('The source-team manager ignored a warning.', 'No warning or response has yet been established.'),
          ('Diego received a formal disciplinary warning.', 'This is a coaching discussion, not a supplied disciplinary procedure.')),
        q('Which question investigates the missing information?', 'What happened between the source-file handoff and delivery?', 'It asks about the process without deciding the cause first.',
          ('Why did you ignore the deadline for two consecutive weeks?', 'It assumes intentional disregard.'),
          ('Can you admit that the source team failed to do its job?', 'It pressures Diego to endorse an unestablished judgment.'),
          ('Will you promise never to depend on another team again?', 'The work has a real dependency that cannot be removed by a promise.')),
    ],
    choices=[
        q('Choose feedback that separates observation from interpretation.', 'The report arrived Friday; I need to understand the delay.', 'It states what happened and asks about the cause.',
          ('The report arrived Friday; that shows you do not value planning.', 'The second clause presents an inferred attitude as fact.'),
          ('The report arrived Friday; the source team is clearly at fault.', 'It establishes blame before investigating the handoff.'),
          ('The report arrived Friday; this means the deadline was unrealistic.', 'The record alone does not establish that the deadline was impossible.')),
        q('Which agreement is measurable without pretending Diego controls the source team?', 'Flag a missing file Wednesday at three; send a Thursday-noon status update.', 'Both are actions Diego can take even if the input remains missing.',
          ('Guarantee the source file arrives Wednesday and the final figures never change.', 'Diego cannot guarantee another team\'s action or all future figures.'),
          ('Try to be more proactive and improve coordination when necessary.', 'The expectation lacks an observable trigger and reporting time.'),
          ('Wait until every figure is final before contacting planning again.', 'This repeats the silent delay rather than creating an early warning.')),
        q('Diego explains a late source file. Which response maintains the standard and investigates cause?', 'That helps explain the delay; let\'s fix the handoff and warning point.', 'It acknowledges the explanation while changing the process.',
          ('That removes your responsibility; no further update is needed from you.', 'The dependency does not remove Diego\'s communication responsibility.'),
          ('That is an excuse; the file arrival cannot affect your deadline.', 'It dismisses a relevant dependency instead of examining it.'),
          ('That proves the deadline should be canceled for all future reports.', 'One explanation does not justify abandoning the reporting standard.')),
        q('Which closing checks action rather than demanding reassurance?', 'At next Thursday\'s check-in, we will review the file and update times.', 'It specifies what evidence will be reviewed and when.',
          ('At next Thursday\'s check-in, confirm that you now care about deadlines.', 'It asks for an attitude claim rather than observable follow-through.'),
          ('At next Thursday\'s check-in, agree that the source team owns every delay.', 'It predetermines blame rather than reviewing what happened.'),
          ('At next Thursday\'s check-in, promise no report will ever arrive late.', 'An unlimited promise is not a practical review measure.')),
    ],
    **dialogue('''
Elena|Have you got ten minutes to look at the last two reports? Both were due Thursday noon and arrived Friday morning.
Diego|Yes. I know they were late. I was waiting for the source file, and I didn't want to send numbers I couldn't support.
Elena|I appreciate that. The [[impact::Impact describes the effect on planning, not an accusation about Diego's intentions.]] was that planning had to defer its staffing update. Walk me through the handoff.
Diego|The source file arrived Thursday afternoon both weeks. I checked it afterward and sent the report the next morning.
Elena|So the [[upstream input::Upstream input is the source file supplied by another team before Diego can complete his work.]] arrived after your deadline. Did anyone know you were still waiting?
Diego|I asked the source team Wednesday. I didn't tell planning. I expected the file to come through and didn't want to send another warning that went nowhere.
Elena|That explains the decision. It also leaves planning without an [[early-warning signal::Early-warning signal is notice that the deadline is at risk before it passes.]]. What warning point would actually help?
Diego|Wednesday at three. If I don't have the file then, I can say what's missing and what it affects.
Elena|Let's use that. I'll speak with the source-team manager about the [[bottleneck::Bottleneck is the handoff that is restricting timely report completion in this account.]]. You shouldn't have to negotiate their priorities alone.
Diego|Thanks. I still can't promise a verified Thursday report if the source file turns up late.
Elena|Agreed. The [[performance expectation::Performance expectation here includes timely communication, not a guarantee over another team's input.]] is a Thursday-noon report or a clear status update if the input prevents it.
Diego|With the missing items named, rather than an empty spreadsheet?
Elena|Yes. State what is confirmed, what is missing, and the next update. That measurable standard is more useful than asking you to "be proactive."
Diego|That gives me an [[action plan::Action plan names specific steps and times instead of a general promise to improve.]]: flag Wednesday at three, send a status [[update::Update is the timely communication Diego can send even if the underlying file is still missing.]] Thursday noon, and verify the figures once the file arrives.
Elena|Right. Let's check it next Thursday. We'll review the actual file-arrival and message times, not just whether everyone felt communication improved.
Diego|Can we keep the warning in the shared channel? If I message three people separately, the versions drift.
Elena|Yes. That should reduce [[rework::Rework is duplicated effort caused by inconsistent updates or changed information.]]. Tag planning and me in the same update.
Diego|I can do that. If the source team fixes its timing, should I stop the Wednesday check?
Elena|Keep the check for now. We want to see whether this prevents [[recurrence::Recurrence means the same late, unannounced handoff pattern happening again.]], not declare it solved after one good week.
Diego|Fair. I'll put the times in my calendar, and we can check [[follow-through::Follow-through means carrying out the agreed warning, update, and review actions.]] against the actual record next Thursday.
'''),
    transfer_title='Two missed customer callbacks',
    transfer_facts='A callback was promised for Tuesday at 4 p.m. and happened Wednesday at 10 a.m. on each of two weeks. Customer updates were delayed. Sal does not yet know why. Jo can control warning messages, not the arrival of every technical answer.',
    repair=[
        q('Repair "You keep ignoring customers."', 'Both callbacks happened Wednesday, after the Tuesday commitment.', 'It replaces a motive claim with the observed timing pattern.',
          ('Both callbacks were delayed because you chose easier work.', 'The cause is not established.'),
          ('Both customers misunderstood the callback time we promised.', 'The case does not support a customer misunderstanding.'),
          ('Both callbacks were late, so all technical questions must be resolved Tuesday.', 'That promises control over a dependency Jo does not necessarily have.')),
        q('Which request creates an observable early warning?', 'If the answer is missing at three, send a status message then.', 'It gives an explicit trigger and an action Jo can perform.',
          ('If the answer is missing at three, guarantee it will arrive by four.', 'Jo cannot guarantee the arrival of every technical answer.'),
          ('If the answer is missing at three, wait until it is complete to contact anyone.', 'That preserves the silence causing delayed customer updates.'),
          ('If the answer is missing at three, treat the original promise as canceled.', 'A missing answer does not silently cancel a customer commitment.')),
    ],
    transfer=dialogue('''
Sal|Both callbacks happened Wednesday. What was the [[bottleneck::Bottleneck asks about the process constraint without presuming a motive.]]?
Jo|I was waiting for technical answers. I should have sent a [[warning::Warning would have alerted the customer before the promised callback was missed.]] before four.
Sal|If the answer is missing at three, send a [[status update::Status update communicates what is known and what remains missing without pretending the answer is complete.]].
Jo|Even if the technical answer is still pending?
Sal|Yes. State the next contact time. We'll review the message times at our [[check-in::Check-in is the agreed later review of observable actions, not a guarantee that all answers arrive on time.]].
Jo|Understood. I can control that contact even when I can't control the technical answer.
'''),
    delivery='Read the two arrival times neutrally. Stress the ACTION in the agreement, not the person in the criticism.',
),
make_unit(7,
    artifact_title='Branch reporting / request and workload',
    artifact_headers=['Item', 'Current situation'],
    artifact_rows=[['Request', 'Re-enter 18 figures in a daily spreadsheet'], ['Existing record', 'Most figures already in the shared dashboard'],
                   ['Manual effort', '1 hour per day'], ['HQ purpose', 'Early warning of service failures'],
                   ['Authority', 'Nadia and Ren may change this internal process, not separate mandatory reports']],
    focus=[('cadence', 'CA-dence', 'Let\'s agree a reporting cadence that matches the decision.', 'Cadence is frequency, not the reporting deadline itself.'),
           ('threshold', 'THRESH-old', 'A threshold needs a defined trigger, not "when things look bad."', 'Crossing a threshold triggers action; it does not explain the cause.'),
           ('data lineage', 'DA-ta LIN-e-age', 'The note preserves the data lineage for the corrected figure.', 'Lineage tracks origin and transformation, not just the newest value.'),
           ('exception reporting', 'ex-CEP-tion re-PORT-ing', 'Exception reporting highlights departures from an agreed rule.', 'It still requires routine monitoring of the underlying data.')],
    registers=[('Branch concern', 'We spend an hour retyping figures you can already see.', 'Shared objective', 'We want reliable early warning with less duplicate entry.'),
               ('Technical label', 'Exception reporting', 'Plain-language explanation', 'Send an alert when the agreed service threshold is crossed.')],
    checks=[
        q('What does Ren need the information to support?', 'Early warning of service failures.', 'That is the stated purpose, not a preference for a second archive.',
          ('A second permanent archive of every dashboard figure.', 'The brief explicitly distinguishes early warning from a second archive.'),
          ('Approval to remove all mandatory reporting.', 'Separate mandatory reports are outside this process change.'),
          ('Proof that the branch is busy enough each day.', 'This motive is not established by the reporting request.')),
        q('Which proposed change falls within the supplied authority?', 'Agree a new format for this internal service update.', 'Both offices may agree the format and cadence of this process.',
          ('End every mandatory report that duplicates a dashboard field.', 'Separate mandatory reporting cannot be changed here.'),
          ('Stop monitoring service levels once the spreadsheet is removed.', 'Removing duplicate entry does not remove monitoring.'),
          ('Treat unreported dashboard fields as confirmed service failures.', 'Missing information and an established failure are different.')),
        q('Which fact best explains the branch\'s workload concern?', 'Re-entering the figures takes one hour per day.', 'It quantifies the effort without judging headquarters\' motives.',
          ('Headquarters distrusts every figure the branch supplies.', 'Distrust is not established.'),
          ('All eighteen figures are absent from the shared dashboard.', 'Most are already in the dashboard.'),
          ('The branch has permission to ignore headquarters requests.', 'No such general permission is supplied.')),
    ],
    choices=[
        q('Which opening translates the disagreement into a shared problem?', 'What decision needs an alert, and which figures support it?', 'It asks about purpose and evidence before changing the method.',
          ('Why does headquarters need so much reassurance from the branch?', 'It assumes an emotional motive and invites defensiveness.'),
          ('Can we stop all reporting now that the dashboard is available?', 'It exceeds the authority and ignores fields or needs the dashboard may not cover.'),
          ('Would a shorter spreadsheet prove that the branch is cooperative?', 'It frames the issue as attitude rather than information needs.')),
        q('Which description makes exception reporting operational?', 'Monitor routinely; alert Ren when the agreed trigger is met.', 'It preserves monitoring and names an explicit alert condition.',
          ('Monitor occasionally; alert Ren whenever the branch feels concerned.', 'Frequency and trigger are left undefined.'),
          ('Stop monitoring; send an alert if a customer discovers a problem.', 'It substitutes reactive discovery for early warning.'),
          ('Monitor routinely; treat every missing update as a confirmed failure.', 'Missing information requires clarification, not automatic reclassification.')),
        q('Which sentence protects the scope of the process change?', 'This changes the internal update, not any separate mandatory report.', 'It states what the agreement does not authorize.',
          ('This removes all reporting that overlaps with the dashboard.', 'Overlap alone does not authorize ending mandatory reports.'),
          ('This makes the dashboard owner responsible for all office decisions.', 'Owning data does not transfer every decision right.'),
          ('This ends the need to record corrections to shared figures.', 'An audit trail remains useful even without duplicate entry.')),
        q('Ren worries about losing visibility. Which reply addresses that concern?', 'Keep dashboard access and agree an alert owner and response time.', 'It preserves access and defines how exceptions will reach someone.',
          ('Keep dashboard access and assume silence means all checks passed.', 'Silence may reflect a missed alert or delayed refresh.'),
          ('Keep dashboard access but remove the branch from alert ownership.', 'An ownership gap would weaken early warning.'),
          ('Keep dashboard access and postpone all exceptions to the monthly meeting.', 'A monthly delay may defeat the stated early-warning purpose.')),
    ],
    **dialogue('''
Ren|Can the branch put the eighteen figures into the daily spreadsheet again? I didn't have a clear picture at yesterday's review.
Nadia|Can we start with the decision you needed to make? Most of those figures are already on the dashboard. The [[duplicate entry::Duplicate entry is retyping information that already exists in the shared record.]] takes us an hour a day.
Ren|I need to know when service is slipping, before a director asks me. Opening a dashboard doesn't tell me what changed overnight.
Nadia|So it's early warning, not another archive. I can work with that [[information requirement::Information requirement identifies what Ren needs to know for a particular decision.]].
Ren|Yes, but I don't want a lighter process that leaves headquarters guessing whether no news means no problem.
Nadia|Neither do I. We could keep routine monitoring and use [[exception reporting::Exception reporting sends alerts for defined deviations while routine monitoring continues.]] for the agreed service triggers.
Ren|What counts as an exception? Different teams have been using that word differently.
Nadia|Let's define the [[threshold::Threshold is the agreed trigger for an alert, rather than an unspecified feeling that something is wrong.]] together before we start. The service owner needs to confirm which measures and limits are appropriate.
Ren|And who sends the alert? Last month everyone assumed someone else had sent it.
Nadia|Name a branch owner and a backup in the process card. Give headquarters an [[acknowledgment time::Acknowledgment time sets when the recipient confirms receipt, without pretending the issue is already resolved.]] so we know the message reached somebody.
Ren|That helps. The dashboard refreshed late yesterday, though. I was looking at old figures without realizing it.
Nadia|Then the [[refresh cycle::Refresh cycle describes when the dashboard's information is updated.]] needs to be visible. We'll show the update time, and an alert will say when its source data was captured.
Ren|Can the dashboard stay the authoritative record? I don't want three different totals circulating.
Nadia|Yes. Keep one [[single source of truth::Single source of truth is the agreed authoritative record for these figures, not a promise that data is infallible.]]. The alert should link to the record, not create a new spreadsheet total.
Ren|What about corrections? If a figure changes, I need to know which version I used in the review.
Nadia|We'll preserve the [[audit trail::Audit trail records the correction and supporting history rather than silently overwriting the earlier figure.]]. Removing re-entry doesn't mean erasing revisions.
Ren|All right. Propose a reporting frequency and the alert route. We can test whether I get the early warning I need.
Nadia|I'll send a proposed [[reporting cadence::Reporting cadence is the frequency of routine updates, distinct from immediate exception alerts.]] and the owners. Separate mandatory reports stay unchanged.
Ren|Agreed. This is a change to our internal update, not permission to stop other reporting. Let's review the trial after two weeks.
Nadia|I'll include that review and the [[escalation path::Escalation path states where an unacknowledged or unresolved alert should go next.]]. The aim is less retyping, not less visibility.
'''),
    transfer_title='A daily slide deck that repeats the ticket system',
    transfer_facts='A support team spends 40 minutes daily copying ticket counts into slides. The regional lead needs immediate notice of a missed service target. The ticket system remains the authoritative record. Separate required reports remain unchanged.',
    repair=[
        q('Repair "No slides means no more reporting."', 'Routine monitoring continues; alerts replace duplicate slide entry.', 'It changes the communication method, not the responsibility to monitor.',
          ('Routine monitoring ends; customer complaints will trigger the next report.', 'This removes early detection of the missed target.'),
          ('Routine slides continue; all other required reports can now stop.', 'Separate required reports are unchanged.'),
          ('Routine monitoring continues; missing alerts prove every target was met.', 'An absent alert is not proof of a positive result.')),
        q('Which process detail is needed before the change starts?', 'The alert trigger, sender, recipient, and response expectation.', 'These make the alert route usable and testable.',
          ('The slide colors, font size, logo position, and picture choice.', 'Presentation styling does not establish how warnings will be handled.'),
          ('The assumption that every manager checks the system continuously.', 'An assumption is not an agreed monitoring or alert arrangement.'),
          ('The permission to replace all required reports with informal messages.', 'That permission is outside the supplied authority.')),
    ],
    transfer=dialogue('''
Rae|The ticket system stays the [[authoritative record::Authoritative record is the agreed source for the counts, not a second slide total.]].
Lin|Then I need an alert when the agreed [[trigger::Trigger is the defined missed-service-target condition that requires notice.]] is met.
Rae|We'll name the sender and backup. Who confirms [[receipt::Receipt acknowledges the alert has arrived; it does not mean the service issue is resolved.]] on your side?
Lin|I do, with my deputy covering absences.
Rae|Good. We'll record that and leave the separate required reports [[unchanged::Unchanged preserves the boundary of this internal process revision.]].
Lin|Agreed. Let's review whether alerts arrive in time, not just whether the slides disappeared.
'''),
    delivery='Contrast LESS RETYPING with LESS VISIBILITY. Explain "authoritative record" once, then use the plain label "ticket system."',
),
make_unit(8,
    artifact_title='Meeting record / correction needed',
    artifact_headers=['Observed event', 'Record needing repair'],
    artifact_rows=[['Daniel interrupted Lena twice', 'Her explanation of customer risk was unfinished'],
                   ['Minutes describe a timing preference', 'Lena had raised a customer risk'],
                   ['Lena reports feeling dismissed', 'Daniel has not yet corrected the shared record'],
                   ['Business issue', 'Risk remains unresolved; no outcome promised']],
    focus=[('mischaracterize', 'mis-CHAR-ac-ter-ize', 'I mischaracterized your risk concern as a preference.', 'Naming the inaccurate description is stronger than saying there was confusion.'),
           ('retraction', 're-TRAC-tion', 'I will issue a retraction of the unsupported claim.', 'Retract withdraws a claim; clarify may merely explain it.'),
           ('defensiveness', 'de-FEN-sive-ness', 'An excuse at the start can sound like defensiveness.', 'Explaining intent does not erase an action\'s effect.'),
           ('procedural fairness', 'pro-CE-dur-al FAIR-ness', 'An uninterrupted review protects procedural fairness.', 'A fair hearing does not guarantee a preferred decision.')],
    registers=[('Own the action', 'I cut you off twice and recorded your point incorrectly.', 'Avoid distancing language', 'There seems to have been a misunderstanding. This leaves the actor unnamed.'),
               ('Concrete repair', 'I will correct the minutes in the same group.', 'Bounded commitment', 'I will give the risk a full hearing, not promise a predetermined decision.')],
    checks=[
        q('What must the corrected record preserve?', 'Lena raised a customer risk, not a timing preference.', 'The minutes mischaracterized the nature of her concern.',
          ('Lena approved the launch but disliked the meeting time.', 'Neither approval nor a meeting-time preference is supplied.'),
          ('Daniel resolved the customer risk before Lena spoke.', 'The risk remains unresolved.'),
          ('The project decision must now favor Lena\'s recommendation.', 'A repair does not predetermine the business outcome.')),
        q('Which action is Daniel in a position to promise?', 'Correct the minutes and give the concern a full hearing.', 'These are concrete process repairs within his role.',
          ('Guarantee Lena will feel reassured by the next meeting.', 'He cannot control Lena\'s feelings or timetable for trust.'),
          ('Guarantee that no customer risk will materialize later.', 'A communication repair cannot establish that outcome.'),
          ('Guarantee approval of Lena\'s preferred project option.', 'That would predetermine a decision before reviewing the risk.')),
        q('Which statement acknowledges an action rather than disputing its impact?', 'I interrupted you twice and left your risk explanation unfinished.', 'It owns a specific observable action.',
          ('I am sorry if you took my efforts to help in the wrong way.', 'It conditions the apology on her interpretation and centers his intent.'),
          ('I interrupted because the meeting needed a more positive tone.', 'It supplies a justification rather than acknowledging the harm.'),
          ('I think we both contributed equally to the confusion in the minutes.', 'Equal responsibility is not established by the case.')),
    ],
    choices=[
        q('Choose the strongest opening repair.', 'I cut you off twice, and I recorded your concern incorrectly.', 'It names the actor, behavior, and record error without demanding reassurance.',
          ('I am sorry you felt cut off while I was trying to help.', 'It centers her feeling and his intention rather than owning the action.'),
          ('I am sorry if the meeting format caused some misunderstanding.', 'It makes the harm conditional and assigns agency to the format.'),
          ('I am sorry, but we had agreed to keep the discussion positive.', 'The qualification turns the apology into a defense and invents a constraint.')),
        q('Which correction addresses the original audience?', 'Send the corrected risk description to the same meeting group.', 'The people who received the inaccurate description need the correction.',
          ('Send Lena a private apology and leave the shared minutes unchanged.', 'The public misunderstanding remains even if the relationship improves privately.'),
          ('Send a new schedule without mentioning the earlier risk description.', 'A schedule does not correct the mischaracterized concern.'),
          ('Send a general reminder that everyone should communicate more clearly.', 'It diffuses responsibility and leaves the specific false record intact.')),
        q('Lena is not ready to reassure Daniel. Which response respects that?', 'You do not need to settle this now; I will make the correction today.', 'It allows time while committing to a concrete repair.',
          ('You do not need to settle this now; I will wait to correct the record.', 'It makes factual correction depend on emotional resolution.'),
          ('You do not need to settle this now; please confirm we are fine before leaving.', 'The second clause contradicts the permission by demanding reassurance.'),
          ('You do not need to settle this now; the apology should close the issue.', 'It declares the impact resolved on Daniel\'s timetable.')),
        q('Which promise protects a fair process without fixing the outcome?', 'I will hear the risk fully before we make the project decision.', 'It promises consideration, not approval.',
          ('I will approve your recommendation to show that the apology is sincere.', 'It trades a business outcome for reassurance before review.'),
          ('I will remove the risk from the record to avoid further discomfort.', 'It erases relevant information rather than repairing its treatment.'),
          ('I will describe the risk as resolved so the team can move forward.', 'The case says it remains unresolved.')),
    ],
    **dialogue('''
Daniel|Could we talk about yesterday's review? I cut you off twice, and the minutes describe your risk concern as a preference about timing. That was wrong.
Lena|Yes. It felt as if you'd decided what I meant before I'd finished. Then the record made it look like I was just asking for more time.
Daniel|I [[mischaracterized::Mischaracterized names the inaccurate description of Lena's concern, not merely a difference in tone.]] your point. I was watching the clock, but that doesn't make the summary accurate.
Lena|The time pressure was real. So was the customer risk. We can't fix the second one by apologizing for the first.
Daniel|Agreed. I want to [[acknowledge::Acknowledge explicitly recognizes the reported impact without disputing Lena's experience.]] the impact and correct the record. I won't pretend that settles the risk.
Lena|What would you change in the minutes?
Daniel|I'd withdraw the "timing preference" line and replace it with your actual concern. Can you check the wording before I [[circulate::Circulate means send the corrected wording to the meeting group, rather than merely acknowledge it privately.]] it?
Lena|I can. But it needs to go to the same group. A private note to me won't change what they think I said.
Daniel|Yes. I'll take [[ownership::Ownership means accepting responsibility for the interruption and inaccurate record.]] of the error in that message. I won't make it sound as if you changed your position afterward.
Lena|Thank you. And I need enough time to explain the risk at the next review, without being asked to fit it into the last thirty seconds.
Daniel|I'll put it first and protect your turn. That's a [[process commitment::Process commitment promises a fair hearing, not a predetermined business outcome.]], not a promise that the project decision will go your way.
Lena|I understand. I'm not asking you to approve my recommendation because the meeting went badly. I'm asking for the evidence to be heard.
Daniel|Then let's make that our [[working agreement::Working agreement states how the next discussion will be conducted and how meaning will be checked.]]: you finish the explanation; I check my summary with you before we decide.
Lena|And if there's a real time limit, tell me at the start. I can prioritize the key facts instead of getting cut off halfway through.
Daniel|That's fair. My [[intent::Intent is what Daniel meant to achieve; he distinguishes it from what actually happened.]] was to keep the meeting moving. The effect was that your concern disappeared from the record.
Lena|It did. I appreciate you saying that. I'm still frustrated, though.
Daniel|You don't have to reassure me. I'll send the correction today. We can have a brief [[follow-up::Follow-up is a later check on whether the promised repair actually happened.]] after the next review to see whether the new approach worked.
Lena|All right. Send me the wording first, and I'll check whether it captures the risk rather than just the delay.
Daniel|I will. The remedy is an accurate record and [[a full hearing::A full hearing gives Lena time to explain the evidence without interruption; it does not promise approval.]]. Neither requires you to say everything is fine today.
Lena|That's enough for now. Let's deal with the risk properly and rebuild [[trust::Trust is confidence supported by later actions, not something an apology can require immediately.]] through what happens next.
'''),
    transfer_title='A contributor was left out of an executive update',
    transfer_facts='Mara presented an accurate result but omitted Chen\'s analysis from the credits. Executives have not yet forwarded the update. Mara can correct the attribution today; she cannot promise a promotion or Chen\'s immediate reassurance.',
    repair=[
        q('Repair "I am sorry if you wanted more attention."', 'I omitted your analysis from the credits; I will correct that today.', 'It owns the omission and promises a relevant repair.',
          ('I omitted your name because the executives prefer short presentations.', 'This explains away the omission rather than repairing it.'),
          ('I omitted your name, so I will guarantee your promotion this month.', 'The proposed remedy is outside Mara\'s stated authority.'),
          ('I omitted your name, but everyone probably knew you contributed.', 'The assumed audience knowledge does not correct the record.')),
        q('Which follow-up repairs the specific record?', 'Send executives the revised credits before they forward the update.', 'The correction reaches the recipients of the original omission in time.',
          ('Ask Chen to tell the executives privately if recognition matters to him.', 'This shifts responsibility for Mara\'s omission onto Chen.'),
          ('Promise to mention someone else\'s work at a future presentation.', 'It does not repair Chen\'s missing credit in this update.'),
          ('Withdraw the accurate result so no one can use the presentation.', 'The result is accurate; only attribution needs correction.')),
    ],
    transfer=dialogue('''
Mara|The result was accurate, but the [[attribution::Attribution identifies who contributed the analysis; it is the part of the update that needs repair.]] was incomplete.
Chen|Yes. The executives won't know which analysis came from me.
Mara|I'll send a [[correction::Correction adds the missing credit to the existing record.]] today, before they forward it.
Chen|Please name the analysis, not just "thanks to the team."
Mara|I will. That's the specific [[omission::Omission is the information missing from the credits, not an error in the numerical result.]] I need to repair.
Chen|Thank you. Let's check the [[revised record::Revised record is the corrected update that should carry the accurate contribution forward.]] before it goes out.
'''),
    delivery='Stress "I omitted" rather than "you wanted." Make a small pause before the promised correction, and avoid rushing the other person toward reassurance.',
),
]

# Additional cases remain distinct from the eight web-aligned core lessons.
from books.supplements import load_supplements
SUPPLEMENTS = deepcopy(load_supplements('cultural-leadership-us-branches'))
for s in SUPPLEMENTS:
    s['title'] = s['scene']
    s['setup'] = s['brief']
SUPPLEMENTS[0]['setup'] = ('Mina has six analyst-days of capacity available across the team next week. '
    'The renewal review needs four; the full launch analysis needs four. '
    'A two-day first pass can cover the two largest customer groups but not the regional breakdown. '
    'Director Alex can change priorities, but no extra staffing is approved.')
SUPPLEMENTS[0]['title'] = 'Two urgent launches and six analyst-days'
SUPPLEMENTS[0]['dialogue'][3] = ('Mina', 'Together they need eight analyst-days. We have six across the team, even with me taking over the presentation. What should move?')
SUPPLEMENTS[0]['dialogue'][4] = ('Alex', 'Could the team just push a little harder?')
SUPPLEMENTS[0]['dialogue'][5] = ('Mina', 'We are already covering an absence. I can check the estimate, but I will not promise eight analyst-days from six available.')
SUPPLEMENTS[0]['dialogue'][13] = ('Mina', 'I can commit to a scheduling update Tuesday. I need to scope the regional breakdown before I can give you a completion date.')
SUPPLEMENTS[0]['dialogue'][14] = ('Alex', 'Then send the update Tuesday. I need you to explain the reduced Friday scope to Sales today.')
SUPPLEMENTS[0]['dialogue'][18] = ('Alex', 'Agreed. I do not want individual analysts negotiating a new scope with Sales on their own.')
SUPPLEMENTS[0]['dialogue'][19] = ('Mina', 'Neither do I. I will be the {{6}} for changes, and the analysts can focus on the agreed work.')
SUPPLEMENTS[0]['transfer']['setup'] = ('Sales requests a third customer group in Friday\'s first pass. It fits only if it replaces one of the original two. Alex must choose; Mina cannot add work silently.')

CHECKPOINTS = [
    dict(after=2, title='Review 1 / A launch memo under pressure',
         facts='Lena\'s memo says "Thursday approved." The sponsor actually said "The approach is sensible." Four reviewers are confirmed; six are required. Two bookings are pending. A colleague says the capacity assumption is weak. Lena owns the launch decision.',
         questions=[
             q('Which label belongs on Thursday?', 'Proposed; reviewer readiness and authorization are still open.', 'Neither support for the approach nor a booking grants final approval.',
               ('Approved; the sponsor liked the general approach.', 'Support for an approach does not authorize the date.'),
               ('Canceled; two reviewers have not yet confirmed.', 'Pending confirmations do not establish cancellation.'),
               ('Confirmed; the bookings complete the reviewer requirement.', 'A pending booking is not a confirmed reviewer.')),
             q('Which question tests the criticism instead of guessing a motive?', 'Which workload assumption needs different evidence?', 'It focuses the challenge on a testable premise.',
               ('Why are you resisting the sponsor\'s chosen direction?', 'It infers resistance and assumes the sponsor selected a direction.'),
               ('Can you support the team by withholding the concern?', 'It suppresses useful scrutiny.'),
               ('Would a more positive tone remove the capacity problem?', 'Tone cannot establish staffing capacity.')),
             q('Choose the accurate distinction.', 'Acknowledgment records understanding; authorization permits action.', 'These functions should not be merged in a decision record.',
               ('Acknowledgment permits action; authorization records receipt.', 'This reverses the functions.'),
               ('Acknowledgment and authorization both mean final approval.', 'Receipt or understanding is not necessarily approval.'),
               ('Acknowledgment is opposition; authorization is tentative support.', 'Neither definition captures the actual function.')),
             q('Which response accepts scrutiny and sets a boundary?', 'Test the capacity estimate; leave judgments about the team out.', 'It preserves criticism of the plan while limiting personal judgments.',
               ('Test the team\'s loyalty before reviewing the capacity estimate.', 'It turns a task objection into a loyalty judgment.'),
               ('Leave both the estimate and the team out of the discussion.', 'It suppresses the substantive problem along with the personal one.'),
               ('Accept the estimate first; challenge its authors privately later.', 'It approves before testing and redirects criticism toward people.')),
         ]),
    dict(after=4, title='Review 2 / A presentation and a purchase',
         facts='Eva may change an internal presentation sequence. External design purchases require Malik\'s approval. A paid design can be recommended Friday, but a checked cost estimate will not be available until Monday. The Friday meeting can review a provisional estimate.',
         questions=[
             q('Which action can Eva take now?', 'Reorder the internal presentation without buying external design.', 'Sequence changes are delegated; spending is not.',
               ('Buy the design if the team agrees with the recommendation.', 'Team support is not Malik\'s approval.'),
               ('Approve the vendor because a checked estimate is due Monday.', 'A future estimate provides no current spending authority.'),
               ('Promise payment Friday and ask Malik to approve it Monday.', 'That creates a commitment before required approval.')),
             q('Which Friday message is accurate?', 'Design recommended; cost estimate provisional; purchase approval pending.', 'It distinguishes recommendation, evidence status, and authorization.',
               ('Design purchased; cost estimate provisional; approval follows Monday.', 'It implies an unauthorized purchase and delayed approval.'),
               ('Design approved; cost estimate checked; payment can proceed Friday.', 'None of these final statuses is supplied.'),
               ('Design rejected; cost unavailable; Friday\'s review must be canceled.', 'A provisional review is explicitly possible.')),
             q('The sponsor asks for a "final" Friday estimate. Choose the reply.', 'Friday can be provisional; the check finishes Monday.', 'The version can be clarified without promising an impossible check.',
               ('Friday can be final if we keep the Monday check private.', 'Hiding a pending check does not make the estimate final.'),
               ('Friday can be final because a recommendation implies approval.', 'Recommendation and approval are separate.'),
               ('Friday can be verified as long as the label is removed later.', 'Changing labels cannot supply verification.')),
             q('Which item belongs in the written commitment?', 'Version, delivery time, time zone, and pending dependency.', 'These details define what is promised and what still limits it.',
               ('Version, a hopeful completion date, and assumed approval.', 'Hope and assumed approval leave key commitments ungrounded.'),
               ('Presentation style, meeting preference, and implied authority.', 'These do not resolve delivery or decision boundaries.'),
               ('General effort, informal reassurance, and no stated limitation.', 'Best-effort language without boundaries preserves ambiguity.')),
         ]),
    dict(after=6, title='Review 3 / A quiet voice and a late file',
         facts='Remote analyst Ava posted that the cost file had not arrived. Nobody responded. The chair summarized her concern as dislike of the schedule. Two previous reports arrived a day late. The file delay is a possible cause, not a confirmed explanation of both incidents.',
         questions=[
             q('Which chairing action comes first?', 'Give Ava an uninterrupted turn to explain the missing file.', 'The missed contribution needs to be heard before its meaning is summarized.',
               ('Ask Ava to agree with the recorded schedule preference.', 'That pressures her to accept the inaccurate interpretation.'),
               ('Explain that chat messages count as agreement unless marked urgent.', 'No such agreement rule is supplied, and the message raised a concern.'),
               ('Move to the next topic because the file is outside the agenda.', 'The missing file affects the work being discussed.')),
             q('Which wording separates observation from cause?', 'Two reports arrived late; we need to trace the handoff.', 'It states the observed pattern and investigates the explanation.',
               ('Two reports arrived late; the source team caused both delays.', 'That cause has not been established for both incidents.'),
               ('Two reports arrived late; Ava did not care about the deadline.', 'It assigns a motive without evidence.'),
               ('Two reports arrived late; the agreed deadline must have changed.', 'Late arrival does not prove the deadline changed.')),
             q('Choose the most useful early-warning agreement.', 'If the file is missing at the agreed checkpoint, send a status update.', 'The trigger and action can be observed even when the input is outside Ava\'s control.',
               ('If the file is missing, guarantee the source team will finish on time.', 'Ava cannot guarantee another team\'s outcome.'),
               ('If the file is missing, wait until the final report can be completed.', 'That preserves silence while others depend on an update.'),
               ('If the file is missing, treat the report deadline as silently canceled.', 'Dependencies do not cancel commitments without communication.')),
             q('Which correction belongs in the minutes?', 'Ava reported a missing input; the cause of past delays remains under review.', 'It corrects her concern and preserves uncertainty about the earlier incidents.',
               ('Ava disliked the schedule; the file was the confirmed cause of both delays.', 'It retains the mischaracterization and overstates cause.'),
               ('Ava approved the schedule; the missing file no longer affects the report.', 'Neither approval nor removal of the dependency is supplied.'),
               ('Ava withdrew her concern; the chair considers both delays resolved.', 'Nothing establishes withdrawal or resolution.')),
         ]),
    dict(after=8, title='Review 4 / The shared dashboard dispute',
         facts='A branch proposes replacing duplicate slides with alerts from a shared dashboard. The headquarters lead interrupts the branch analyst and records the proposal as "stop monitoring." In fact, monitoring would continue, alerts need agreed triggers, and mandatory reports stay unchanged.',
         questions=[
             q('Which correction accurately states the proposal?', 'Retain monitoring; replace duplicate slides with defined alerts.', 'The method changes, not the obligation to monitor.',
               ('Remove monitoring; rely on customers to report exceptions.', 'That is not the proposed process.'),
               ('Retain slides; remove all separate mandatory reports.', 'Mandatory reports remain unchanged.'),
               ('Remove alerts; treat silence as proof that performance is normal.', 'Silence is not verification and alerts are part of the proposal.')),
             q('Which apology owns the specific error?', 'I interrupted you and recorded your proposal incorrectly.', 'It identifies the behavior and record error without a conditional apology.',
               ('I am sorry if your proposal was difficult for us to follow.', 'It shifts the focus to the analyst\'s clarity.'),
               ('I am sorry, but headquarters needs stronger cooperation.', 'It justifies the behavior and implies an unsupported attitude problem.'),
               ('I am sorry the dashboard caused an unfortunate misunderstanding.', 'It gives the dashboard responsibility for a human interruption and summary.')),
             q('Which agreement must precede the alert trial?', 'Define triggers, owners, acknowledgment times, and an escalation route.', 'These make the new process explicit and accountable.',
               ('Assume the dashboard is always current and alerts are never missed.', 'Assumptions cannot replace operational checks.'),
               ('Approve the trial because an apology creates agreement on the process.', 'Repairing an interaction does not approve a business proposal.'),
               ('Eliminate separate mandatory reports to compensate for the interruption.', 'A conduct repair does not authorize changing unrelated requirements.')),
             q('Which promise repairs the process without predetermining the result?', 'Correct the record and review the proposal on its actual merits.', 'It restores a fair hearing without promising approval.',
               ('Approve the proposal immediately to prove the apology is sincere.', 'It exchanges the outcome for reassurance before review.'),
               ('Keep the original minutes so that no one loses face publicly.', 'It preserves the false account received by others.'),
               ('Require the analyst to say trust is restored before reopening the issue.', 'It makes a fair hearing conditional on reassurance.')),
         ]),
]


SECOND_TAKES = [
    q('New fact: the supplier confirms capacity, but Maya has not approved the order. Choose Ellis\'s update.',
      'Capacity is confirmed; purchase approval is still pending.', 'The new fact changes one status, not both. Read the sentence with stress on confirmed and pending.',
      ('Capacity is confirmed; the twelve units are now ordered.', 'No order has been authorized or placed.'),
      ('Capacity is confirmed; Tuesday delivery is now guaranteed.', 'Capacity does not guarantee a delivery date.'),
      ('Capacity is confirmed; Maya no longer needs to decide.', 'The new fact does not remove her approval role.')),
    q('New fact: one of the three pending customers confirms. Choose the revised forecast line.',
      'Eight renewals are confirmed; two remain pending.', 'Seven plus one is eight; the remaining two decisions are still open. Keep the two statuses distinct.',
      ('Ten renewals are confirmed; two confirmations will arrive later.', 'It counts the remaining two before they have confirmed.'),
      ('Eight renewals are forecast; the other two are lost.', 'Pending is not lost, and the eight are confirmed, not merely forecast.'),
      ('Seven renewals are confirmed; the new reply changes nothing.', 'It fails to incorporate the additional confirmation.')),
    q('New fact: Luis approves the external room for this workshop only. Choose Nora\'s read-back.',
      'I may book this room for this workshop, not future sessions.', 'The approval is specific to one event, not a general extension of authority.',
      ('I may book any external room while the price remains low.', 'It turns a specific approval into an unapproved price-based rule.'),
      ('I may book this room for every workshop in the coming year.', 'Future events are explicitly outside this approval.'),
      ('I may only recommend the room; no booking has been approved.', 'It ignores the new, specific authorization.')),
    q('New fact: the independent reviewer is delayed. Choose Nia\'s Monday update.',
      'Review is still pending; I will send a revised completion time.', 'The message keeps status accurate and provides a next step instead of relabeling unchecked work.',
      ('Review is now complete because Monday was the agreed deadline.', 'A deadline does not complete the missing work.'),
      ('Review is unnecessary because Friday\'s text reached the directors.', 'Delivery does not waive the review.'),
      ('Review is confidential; keep calling Friday\'s text the final version.', 'It hides the limitation and misstates the earlier version.')),
    q('New fact: Ines finds no label errors, but Noah has not decided on release. Choose Pavel\'s update.',
      'The label check is complete; release awaits Noah\'s decision.', 'The check supplies evidence; the decision remains separate.',
      ('The label check is complete; Ines has authorized the release.', 'Ines owns the check, not the release decision.'),
      ('The label check is complete; no further release decision is needed.', 'The decision right remains with Noah.'),
      ('The label check is incomplete until Noah approves every label.', 'This confuses evidence completion with the later decision.')),
    q('New fact: Jo sends the three-o\'clock warning, but the technical answer arrives Wednesday. Choose Sal\'s feedback.',
      'The warning was on time; the technical dependency still needs attention.', 'It recognizes the completed communication action without declaring the whole issue solved.',
      ('The answer was late, so the warning counts as late as well.', 'It collapses two separate measures.'),
      ('The warning was on time, so the original customer promise was fully met.', 'A timely warning does not mean the original callback commitment was met.'),
      ('The answer was late, so Jo must have ignored the agreed warning point.', 'The new fact explicitly says Jo sent the warning.')),
    q('New fact: an alert is sent, but neither Lin nor the deputy acknowledges it within the agreed time. Choose Rae\'s next step.',
      'Use the agreed escalation route and preserve the alert record.', 'The missing acknowledgment activates the escalation arrangement, not an assumption that someone acted.',
      ('Assume the issue is resolved because the message was delivered.', 'Delivery is not acknowledgment or resolution.'),
      ('Delete the original alert and wait for the monthly review.', 'That loses the record and delays the early-warning process.'),
      ('Treat the missing reply as permission to stop monitoring targets.', 'No reply does not waive ongoing monitoring.')),
    q('New fact: the credits are corrected, but Chen remains upset. Choose Mara\'s response.',
      'The correction is done; you do not need to reassure me now.', 'It separates an observable repair from the other person\'s timetable for trust.',
      ('The correction is done, so the matter is closed for you too.', 'Mara cannot decide that Chen\'s frustration has ended.'),
      ('The correction is done, so please confirm I did nothing wrong.', 'It asks him to erase the original omission.'),
      ('The correction is done, so your promotion is now guaranteed.', 'It adds an outcome Mara cannot promise.')),
]
for u, second in zip(UNITS, SECOND_TAKES, strict=True):
    u['second_take'] = second

# Keep the additional transfers semantically demanding: each bank contains phrases
# that occupy the same broad grammatical position, rather than four word classes.
SUPPLEMENT_TRANSFERS = [
    dialogue('''
Mina|A third customer group is [[outside the agreed scope::The third group was not in the approved two-group Friday first pass.]].
Alex|Can it fit if we replace one of the first two groups?
Mina|Yes. Substitution is [[within the same capacity::The case says replacing a group fits; adding a third does not.]].
Alex|Keep the original two groups. A third-group request remains [[subject to a new decision::A future scope change needs a fresh priority decision rather than silent addition.]].
Mina|I'll tell Sales. Friday's first pass is [[separate from the full analysis::The reduced Friday deliverable does not include the unscoped regional breakdown.]].
Alex|Good. Send the scheduling update Tuesday; don't invent a completion date for the rest.
'''),
    dialogue('''
Elena|The numerical results are [[accurate as reported::The case says the results are correct; the problem is missing credit.]].
Sponsor|Then what needs changing before I forward the update?
Elena|The credits are [[incomplete as written::The three contributors and their roles were omitted.]]. Noor built the checklist; Luis ran the trial and trained supervisors; Priya gathered feedback.
Sponsor|I'll use a version with those contributions [[explicitly attributed::Explicitly attributed identifies who did which work rather than merely thanking an unspecified team.]].
Elena|Thank you. That correction is [[needed before circulation::The sponsor has not yet forwarded the results, so the corrected credits should travel with them.]].
Sponsor|Send it today. I'll hold the update until it is corrected.
'''),
    dialogue('''
Supervisor|Do I cancel the training records and support preparation?
Omar|No. The release is [[temporarily paused::The failed test postpones release; it does not abandon all launch work.]].
Supervisor|So the completed preparation is [[still usable::Completed work remains valid unless the eventual fix changes it.]], unless the fix affects it.
Omar|Correct. Flag anything that is [[dependent on the repair::A dependency needs review when the technical repair is understood.]].
Supervisor|And the new release date is [[not yet confirmed::The next date depends on unresolved repair work and release checks.]].
Omar|Exactly. Tomorrow we review the evidence and remaining criteria, not a date we have already promised.
'''),
]
for s, transfer in zip(SUPPLEMENTS, SUPPLEMENT_TRANSFERS, strict=True):
    s['pilot_transfer'] = transfer


def validate():
    assert len(UNITS) == 8 and len(SUPPLEMENTS) == 3
    assert [u['title'] for u in UNITS] == [u['title'] for u in ORIGINAL_UNITS]
    for u in UNITS:
        assert len(u['vocabulary']) == 24 and len(u['phrases']) == 16
        assert len(u['dialogue']) == 20 and len(u['gaps']) == 10, (u['number'], len(u['gaps']))
        assert len(u['checks']) == 3 and len(u['choices']) == 4 and len(u['repair']) == 2
        assert len(u['focus']) == 4 and len(u['transfer']['gaps']) == 4
        for scene in (u, u['transfer']):
            tokens = re.findall(r'\{\{(\d+)\}\}', ' '.join(t for _, t in scene['dialogue']))
            assert list(map(int, tokens)) == list(range(1, len(scene['gaps']) + 1))
            assert len({g['answer'].casefold() for g in scene['gaps']}) == len(scene['gaps'])
        for item in u['checks'] + u['choices'] + u['repair']:
            assert len(item['options']) == len(item['reasons']) == len(set(item['options'])) == 4
            assert all(item['reasons']) and 0 <= item['answer'] < 4
    return True
