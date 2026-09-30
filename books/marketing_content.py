"""Original field-specific Marketing English learner-book content."""
from books.authoring import unit

BOOK = dict(
    slug='marketing', title='Marketing English',
    cover_label='Strategy / creative work / measurable outcomes',
    cover_title='Marketing', cover_size=36,
    tagline='Build a sharper brief. Defend the evidence. Make the message work.',
    audience='For brand, content, growth, campaign, and marketing-operations professionals.',
    map_intro='Move from audience insight to a credible message, coordinated delivery, and an accurate performance conversation.',
    notes_title='Persuasive does not mean imprecise.',
    notes_intro='Marketing conversations move between creative possibility and commercial accountability. You may need to challenge a favorite headline, translate a dashboard, or stop a scheduled post. These cases give you the facts and language to stay constructive while making the limits unmistakable.',
    field_notes=[
        ('Name the decision', 'A channel list is not an audience strategy, and a launch date is not an approved brief. Identify the decision the meeting must produce before debating execution.', '"Are we deciding whom to reach, what to promise, or which version to release?"'),
        ('Keep the comparison attached', 'Words such as faster, higher, and better need a comparison and a measurement basis. Removing the qualifier can change the meaning of the claim.', '"The test compared this version with our previous version, not with competitors."'),
        ('Give feedback a usable object', 'Describe the audience need, wording, evidence, or delivery requirement that needs revision. Separate a personal preference from a condition for approval.', '"The opening promises instructions, but the body only announces a product."'),
        ('Separate credit from cause', 'Reporting systems assign credit under rules. A rise after a campaign change is an observation; a defensible causal conclusion needs more than timing.', '"The campaign and the discount changed together, so this report cannot isolate their effects."')],
    scope_note='Fictional English-language practice, not legal advice or a promise of campaign results. Legal requirements, platform policies, and data permissions depend on context and location. Obtain current qualified review for actual claims, audience data, disclosures, and publication decisions.',
    sources=[
        dict(title='Google Search Central. Creating helpful, reliable, people-first content.', url='https://developers.google.com/search/docs/fundamentals/creating-helpful-content', note='Background for matching useful content to an intended audience. The editorial examples and dialogues are original teaching cases.', checked='30 September 2026'),
        dict(title='Federal Trade Commission. Advertising and Marketing.', url='https://www.ftc.gov/business-guidance/advertising-marketing', note='US guidance on truthful advertising, claims, and endorsements. The cases practice recognizing a review issue, not issuing legal clearance.', checked='30 September 2026'),
        dict(title='Federal Trade Commission. CAN-SPAM Act: A Compliance Guide for Business.', url='https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business', note='US commercial-email background. Permission records and other jurisdictions require separate review; a contact record alone is not a complete compliance assessment.', checked='30 September 2026'),
        dict(title='Microsoft Research. Patterns of Trustworthy Experimentation: Pre-Experiment Stage.', url='https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/', note='Background on defining a hypothesis, relevant metrics, and experimental design before interpreting results. The book is language practice, not statistical certification.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Marketing Strategy: Audience, Insight, Problem, Outcome', scene='The scheduling tool with an audience of everyone',
    skill='Narrow an audience brief while distinguishing the daily user, purchasing role, and evidence of need.',
    brief='A scheduling-software brief names the audience as "everyone who works in an office." Six exploratory interviews with operations coordinators at small agencies describe repeated calendar checking. No research with purchasing managers has been completed. The proposed campaign invites coordinators to book a workflow demonstration. A draft slide calls those six interviews proof of market-wide demand. Strategist Mira and product marketer Owen must revise the brief without inventing buyer research or promising that a demonstration request will become a sale.',
    cast='Mira | Marketing strategist\nOwen | Product marketer',
    culture=('Challenge the scope without dismissing the ambition', 'A broad ambition can coexist with a focused first campaign. Use "for this campaign" to narrow the decision rather than imply that no other customer matters. Asking whose problem the message solves is more productive than labeling the brief vague and stopping there.'),
    a='''Who was actually interviewed? | Six operations coordinators at small agencies | Six purchasing managers at large companies | All office workers using scheduling software | Six coordinators and their purchasing managers | The briefing identifies a small exploratory user sample and explicitly excludes completed buyer research.
What does the proposed campaign ask people to do? | Book a workflow demonstration | Approve a purchase contract | Complete a paid migration | Submit a procurement policy | The campaign action is a demonstration request, not a completed purchasing decision.
Which conclusion exceeds the evidence? | The interviews prove market-wide demand | The interviews suggest a calendar-checking problem | Buyer research remains incomplete | A focused audience needs a clearer brief | Six exploratory interviews cannot establish the prevalence of a need across the whole market.''',
    vocabulary='''target audience | The people a particular communication is intended to reach. | define the target audience
market segment | A group distinguished by relevant shared needs or characteristics. | prioritize a market segment
ideal customer profile | A description of organizations or customers considered a strong fit. | refine the ideal customer profile
buyer persona | A research-informed representation of a purchasing role. | validate a buyer persona
end user | The person who uses the product in practice. | interview the end user
economic buyer | The role controlling the relevant purchasing budget. | identify the economic buyer
buying committee | The group influencing or deciding an organizational purchase. | map the buying committee
pain point | A specific problem the audience experiences. | substantiate a pain point
customer insight | An interpretation that explains a meaningful customer pattern. | develop a customer insight
jobs to be done | A framework focused on the progress people seek in a situation. | frame the job to be done
use case | A concrete situation in which a product serves a need. | define the primary use case
value proposition | The relevant benefit and reason to choose an offering. | sharpen the value proposition
demand signal | Evidence suggesting interest or need, with limits. | evaluate a demand signal
qualitative research | Research examining experiences and meaning rather than only numerical estimates. | synthesize qualitative research
sample bias | Distortion arising from who is included in a sample. | acknowledge sample bias
purchase trigger | An event or condition prompting buying consideration. | identify a purchase trigger
decision criterion | A factor used to compare possible purchases. | clarify the decision criteria
barrier to adoption | A condition that makes initial or continued use harder. | investigate a barrier to adoption
addressable market | The market that could be served under a specified definition. | define the addressable market
penetration | Adoption or participation relative to a defined market base. | estimate market penetration
campaign objective | The particular outcome a campaign is intended to achieve. | agree the campaign objective
conversion action | The defined behavior counted as a conversion. | specify the conversion action
leading indicator | A measure that may precede a later outcome. | monitor a leading indicator
research hypothesis | A testable proposition that still requires evidence. | state a research hypothesis''',
    precision='An audience is not necessarily the buyer, and the buyer is not necessarily the person using the product daily. "Coordinators report repeated calendar checking" preserves the actual sample. "Office workers demand our product" changes both the population and the strength of the finding.',
    precision_extra='An insight interprets evidence; a hypothesis proposes something to test. Neither word makes a small sample representative. A demonstration request can be a conversion action for this campaign while remaining only a possible step toward revenue.',
    phrases='''Narrow the decision | For this campaign, which role are we trying to reach first?
Preserve the research | The interviews involved six coordinators, not the entire office market.
Separate the roles | The daily user may not control the purchasing budget.
Define the action | We want qualified coordinators to book a workflow demonstration.
Name the problem | Repeated calendar checking is the reported friction.
Limit the inference | That is an exploratory signal, not proof of market-wide demand.
Request missing evidence | We still need to understand the purchasing manager's criteria.
Close with scope | Let us revise the audience, evidence statement, and conversion action.
Test the premise | We should label the buyer assumption as a hypothesis.
Clarify the benefit | Which part of the current workflow would the demonstration address?
Avoid a false trade-off | A focused first campaign does not rule out other segments later.
Define qualification | We need an agreed meaning of qualified before reporting those requests.
Check the wording | Does the slide distinguish what people said from our interpretation?
Locate the barrier | What prevents the user from trying the workflow?
Separate outcomes | A demonstration request is not the same as a completed sale.
Preserve uncertainty | We have a useful starting point, with buyer research still open.''',
    notes='''For this campaign | This phrase narrows a current decision without making a universal market claim.
Suggest versus prove | Suggest allows a bounded inference; prove claims much stronger support.
Audience and buyer | These labels name different roles even when one person fills both.
Qualified | State the criteria rather than treating the adjective as self-explanatory.
Reported friction | Reported attributes the problem to the research participants.
From request to sale | Naming both stages avoids treating an early action as final commercial success.''',
    d='''Which revision preserves the research correctly? | Six interviewed coordinators described repeated calendar checking. | Office workers consistently demand a scheduling purchase. | Purchasing managers confirmed calendar checking as their main criterion. | The interviews established the total addressable market. | The supported statement retains the participants, observed problem, and limited scope.
Which question resolves a role ambiguity? | Who uses the tool, and who controls the purchasing budget? | Which headline can address every office worker equally? | How many sales should each interview guarantee? | Can we treat all coordinators as budget owners? | User experience and purchasing authority are distinct and both affect the brief.
Which label fits the immediate campaign action? | A booked workflow demonstration | An executed purchase agreement | A verified long-term retention outcome | A completed implementation | The stated request is to book a demonstration, not complete the later stages.
Which response challenges the overclaim constructively? | Keep the insight, narrow its scope, and label the buyer assumption for research. | Delete the research because six interviews have no use. | Retain the claim until a purchasing manager objects. | Replace the sample size with a larger target market estimate. | This response preserves useful evidence while correcting the unsupported generalization and missing buyer knowledge.''',
    dialogue='''Mira | The brief says everyone who works in an office. I understand the ambition, but which person should recognize their own problem in the first campaign?
Owen | The clearest [[target audience::The target audience specifies whom this campaign addresses; it is narrower than everyone working in an office.]] is operations coordinators at small agencies. Six interviews described repeated calendar checking when colleagues tried to find a meeting time.
Mira | That gives us a starting point. Did those same people approve software purchases, or were they describing how they would use the product?
Owen | They spoke as the [[end user::The end user performs the workflow; using software does not establish control over its purchasing budget.]]. We have not interviewed purchasing managers, so I cannot claim that the interviews establish who controls the budget.
Mira | Then the slide saying we have proved market-wide demand goes further than the research. Could we keep the finding but change its scope?
Owen | Yes. We have an exploratory [[demand signal::The interviews indicate a possible need but do not establish its prevalence throughout the wider market.]], not a market estimate. I will keep the sample description next to the finding in the revised brief.
Mira | What exactly is the problem statement? Scheduling sounds broad, and the message needs something people can connect with before we describe our features.
Owen | The reported [[pain point::The pain point is the specific repeated calendar-checking problem, not an unsupported claim about every scheduling task.]] is repeated calendar checking. We should demonstrate that workflow rather than promise to remove every administrative burden across an agency.
Mira | Good. What would we ask the coordinator to do after seeing the message? We need something more precise than engage with the brand.
Owen | Book a workflow demonstration. That is the proposed [[conversion action::The conversion action is the defined response counted by this campaign; it is not automatically a sale.]], but we still need agreed qualification criteria before calling every request a qualified opportunity.
Mira | A demonstration may interest the user without answering the purchasing manager's questions. We should avoid building that missing research into a confident buyer story.
Owen | Agreed. Our [[buyer persona::The buyer persona should be grounded in purchasing-role research, which this case says has not yet been completed.]] remains incomplete. We can list the questions for research, but we should not invent purchasing priorities to make the brief look finished.
Mira | I expect someone will say the narrower audience limits growth. How can we explain this choice without suggesting that larger organizations will never matter?
Owen | Call it the initial [[market segment::The segment defines the campaign's first focus; choosing it does not exclude all future expansion.]]. It is a focused campaign choice based on the evidence available, not a permanent boundary around the entire business.
Mira | The creative team also wants a single sentence describing why this matters. Can that connect the workflow problem with a relevant product benefit?
Owen | Yes, but the [[value proposition::The value proposition connects a relevant benefit to the audience; it must not import an unverified numerical claim.]] should stay within demonstrated capabilities. A numerical time-saving claim would need its own evidence before we add it to the message.
Mira | And when the first requests arrive, we should not present the count as proof that the revenue target has already been reached.
Owen | Correct. It can serve as a [[leading indicator::A leading indicator may precede a later outcome; it does not establish that the later outcome occurred.]]. We would still need to follow the requests through qualification and the actual purchasing process.
Mira | I will revise the brief around the coordinator, the calendar-checking problem, and the demonstration request. The remaining purchasing questions will stay visibly unresolved.
Owen | I will label each unsupported buyer assumption as a [[research hypothesis::A research hypothesis identifies a proposition to test rather than presenting it as an established customer fact.]]. That gives the next research round a clear purpose without weakening the evidence we already have.''',
    transfer_title='The user is not the purchaser',
    transfer_setup='A workplace-learning product is used by employees, but the learning director approves the purchase. A campaign invites employees to try a sample lesson; no company contract has been signed.',
    transfer='''Strategist: "Employees are the daily ___." | users | The supplied facts identify employees as the people using the learning product.
Marketer: "The learning director controls the purchasing ___." | decision | The director approves the purchase, which differs from employees trying a lesson.
Strategist: "Trying a sample is the campaign's immediate ___." | action | The invitation asks for a sample trial rather than a completed company purchase.
Marketer: "We must not report that trial as a signed ___." | contract | No company contract has been signed, so the early behavior cannot be reported as one.'''))


BOOK['units'].append(unit(
    title='Positioning, Messaging, Brand Voice, and Proof', scene='A headline that outruns its evidence',
    skill='Negotiate a compelling comparative message without extending the comparison beyond the test.',
    brief='A draft headline calls a scheduling tool "the fastest tool on the market." The only evidence is an internal test in which the current version completed one defined calendar-import task in 40 seconds; the previous version took 50 seconds under the same stated conditions. No competitors were tested, and no independent validation has occurred. Brand lead Tessa and product marketer Arun must revise the headline and its supporting explanation before the reviewer can assess the complete advertisement.',
    cast='Tessa | Brand lead\nArun | Product marketer',
    culture=('Defend the proposition, not a favorite adjective', 'Creative review can feel personal when a team has invested in a line. Acknowledge the intended effect, name the evidence problem, and propose a narrower proposition. This keeps the discussion about the communication task rather than the writer\'s ability or enthusiasm.'),
    a='''What was the actual comparator? | The previous version of the same product | Every competing scheduling tool | An independently ranked market leader | The average customer's full working day | The briefing describes a version-to-version internal task test with no competitor comparison.
What time reduction does the supplied test show? | 10 seconds, or 20% of the previous 50 seconds | 10 seconds, or 25% of the previous 50 seconds | 40 seconds, or 80% of the previous 50 seconds | 50 seconds, or 100% of the previous 50 seconds | The reduction is 50 minus 40 seconds; dividing 10 by the original 50 gives 20%.
Which statement is unsupported? | The product is the fastest on the market | The recorded task took 40 seconds in the current version | The previous version took 50 seconds in the test | No competitor testing is supplied | A market-wide superlative cannot be established by a test against only the product's earlier version.''',
    vocabulary='''positioning | How an offering is framed relative to audience needs and alternatives. | clarify the positioning
message hierarchy | The order of importance assigned to communication points. | build a message hierarchy
headline | The main line introducing an advertisement or article. | revise the headline
supporting copy | Text developing or qualifying the main message. | align the supporting copy
proof point | Specific evidence supporting a proposition. | attach a proof point
substantiation | Evidence that supports an objective advertising claim. | review claim substantiation
comparative claim | A statement comparing an offering with something else. | qualify a comparative claim
superlative | A strongest-ranking expression such as fastest or largest. | challenge an unsupported superlative
comparator | The product, group, or baseline used for comparison. | identify the comparator
test conditions | The circumstances under which a test was conducted. | disclose relevant test conditions
benchmark | A reference measure or defined test for comparison. | document the benchmark
claim scope | The range of circumstances a claim purports to cover. | narrow the claim scope
qualifier | Wording that limits or specifies a statement's meaning. | retain the necessary qualifier
net impression | The overall message an audience takes from an advertisement. | review the net impression
brand voice | The relatively consistent verbal personality of a brand. | preserve the brand voice
tone | The attitude expressed in a specific communication. | adjust the tone
reason to believe | Support that makes a promised benefit credible. | supply a reason to believe
differentiator | A relevant feature or benefit distinguishing an offering. | substantiate the differentiator
benefit statement | Wording describing a useful outcome for the audience. | sharpen the benefit statement
feature claim | A statement about a product's capability or characteristic. | verify a feature claim
message architecture | An organized structure of core and supporting messages. | maintain the message architecture
creative territory | A broad conceptual direction for creative work. | explore a creative territory
copy review | Assessment of wording and its implications before use. | complete the copy review
approval status | The recorded state of an item's review and authorization. | confirm the approval status''',
    precision='A 20% reduction in task time is not the same wording as "20% faster" across all uses. Identify the measured quantity, original value, task, comparator, and conditions. The test establishes neither a market ranking nor an improvement in every customer workflow.',
    precision_extra='A footnote does not automatically repair a headline that gives the wrong overall impression. The complete advertisement needs review. A marketer can prepare a narrower candidate statement without claiming that the reviewer has already approved it.',
    phrases='''Recognize the aim | The line creates energy, but its comparison is broader than the test.
Name the comparator | We tested the current version against our previous version.
Bound the result | The task took 40 seconds rather than 50 in this internal test.
State the calculation | That is a 20% reduction in the measured task time.
Reject the extension | We have no competitor evidence for a market-wide ranking.
Offer a revision | Let us build the message around the specific tested improvement.
Preserve the context | Keep the task and conditions with the claim.
Close with review | The complete revised advertisement still needs approval.
Separate style and fact | We can keep a confident tone without adding an unsupported superlative.
Check the impression | Would a reader infer a broader performance promise?
Avoid shorthand | I would say reduced task time, not simply faster everywhere.
Name the evidence gap | Independent validation is not part of the supplied evidence.
Mark the version | Please attach the exact tested build and test record.
Protect the benefit | The useful story is the improvement in this defined workflow.
Clarify authority | This is proposed wording, not final clearance.
Request a decision | Can we agree the proposition before polishing the headline?''',
    notes='''Compared with | This expression should identify the actual reference, not leave a reader to assume competitors.
By and to | Time fell by 10 seconds, to 40 seconds; these prepositions encode different values.
Percent and seconds | Give the original basis when converting an absolute change to a percentage.
Confident tone | Verbal confidence does not require a universal factual claim.
Proposed wording | Proposed preserves the distinction between a candidate and an approved advertisement.
Overall impression | Review how headline, image, and qualifiers work together, not just isolated sentences.''',
    d='''Which claim most closely matches the supplied measurement? | The defined task took 20% less time than in the previous version under the test conditions. | The product saves every user 20% of their working time. | The product is 20% quicker than all competing tools. | The current version is independently verified as fastest. | The supported comparison retains the measured task, time basis, earlier version, and conditions.
Which sentence uses by and to accurately? | Task time fell by 10 seconds to 40 seconds. | Task time fell by 40 seconds to 10 seconds. | Task time fell to 10 seconds from 40 seconds. | Task time fell by 20 seconds to 50 seconds. | The measured values are 50 seconds originally and 40 seconds afterward, a difference of 10.
What does the proposed revised wording still require? | Review of the complete advertisement and evidence | Only a change of headline typeface | Automatic release because the arithmetic is correct | No review if the claim has a footnote | Correct arithmetic does not settle the overall impression or the advertisement's approval status.
Which feedback is most useful? | Preserve the benefit, but narrow the comparator and task scope. | Remove all benefits because comparison is impossible. | Keep the superlative and explain it only after publication. | Describe the internal test as independent to improve trust. | The useful revision retains a meaningful tested improvement without expanding or mislabeling the evidence.''',
    dialogue='''Tessa | The creative team likes the fastest tool on the market. It is short and energetic, but I want to check exactly what supports it.
Arun | The available [[comparator::The comparator was the previous version; no competing products were included in the stated test.]] is our previous version. We tested one calendar-import task, and we have not tested competing tools or obtained independent validation.
Tessa | So fastest on the market suggests a ranking we have not established. What numbers can we actually put behind a narrower statement?
Arun | The [[benchmark::The benchmark is the defined task comparison with recorded times, not evidence of a market-wide ranking.]] recorded fifty seconds for the previous version and forty for the current one under the same stated conditions. The difference is ten seconds.
Tessa | That is twenty percent less task time, using fifty as the original base. I would avoid saying customers save twenty percent of their day.
Arun | Right. The [[claim scope::Claim scope defines what the statement covers; a single task test cannot establish all customer time savings.]] should cover that task and comparison. It does not cover every workflow, every customer, or every configuration in which the product might run.
Tessa | Could the headline simply say twenty percent faster and leave the explanation underneath? I am concerned that we are losing the useful benefit.
Arun | I would retain the measurement in the [[supporting copy::Supporting copy develops the headline, but its task-time explanation must remain consistent with the main message.]] and develop a headline that does not change it. Less time for this task is clearer than an unqualified speed promise.
Tessa | The team may suggest putting a small asterisk after fastest. Would that solve the problem if the footnote names our previous version?
Arun | Not automatically. The [[net impression::The overall impression may still imply market superiority even when a small note names a narrower comparison.]] could still be a market-wide ranking. We need the reviewer to assess the whole advertisement, rather than assume an asterisk fixes the headline.
Tessa | I want our voice to remain confident. We should not turn the message into a paragraph that sounds as if nothing useful happened.
Arun | We can preserve the [[brand voice::Brand voice concerns how the brand speaks; it does not justify adding an unsupported factual ranking.]]. The confidence can come from a specific improvement and clear evidence, without the unsupported claim that no competitor is quicker.
Tessa | Then let us agree the proposition first: the new version reduced the measured calendar-import time compared with our old version in this test.
Arun | That gives us a concrete [[proof point::The proof point is the bounded recorded improvement, not a prediction of every user's experience.]]. I will attach the test record so the reviewer can check the exact task, build, and conditions behind the wording.
Tessa | Can we call the result independently verified once the reviewer checks the copy, or would that imply a different kind of testing?
Arun | It would imply evidence we do not have. Internal copy approval does not become independent [[substantiation::Substantiation supports the factual claim; an internal wording review does not transform an internal test into independent validation.]] of the test result. We should describe the evidence as internal.
Tessa | I will ask for two tighter headline options around that proposition. Neither should suggest a universal benefit or comparison with the entire market.
Arun | And each necessary [[qualifier::A qualifier preserves the task, comparator, or conditions that limit what the evidence supports.]] must stay visible where it matters. Otherwise the shorter version may communicate something different from the result we actually measured.
Tessa | We have an evidence-aligned direction, then, not an approved advertisement. The team can revise the creative before the reviewer sees the complete version.
Arun | Exactly. I will mark its [[approval status::Approval status distinguishes a proposed revision from a version authorized for publication after the complete review.]] as pending and keep the evidence attached. We should not release a fragment just because we agreed on the direction today.''',
    transfer_title='A larger sample, not a wider claim',
    transfer_setup='A packaging team tests one box design with 80 participants. Sixty choose it over the old design. No competing brands appear, and the sample is not established as representative.',
    transfer='''Researcher: "Sixty out of eighty is ___ percent." | seventy-five | Dividing 60 by 80 gives 0.75, or 75 percent of the stated participants.
Marketer: "The ___ was our old design." | comparator | The test compared the two internal designs, not any competing brand.
Researcher: "Keep the participant ___ attached to the result." | sample | The limited, unverified sample cannot be silently expanded into a market-wide preference.
Marketer: "We cannot call this proof of market ___." | leadership | No competitor comparison or representative market ranking was established by the supplied test.'''))


BOOK['units'].append(unit(
    title='Campaign Briefs, GTM Planning, and Cross-Functional Alignment', scene='A launch date without a launch-ready brief',
    skill='Resolve ownership and release dependencies while separating a target date from authorization.',
    brief='A campaign is targeted for Monday. The calendar lists email, paid social, and a landing page, but the audience, approved message, and success measure are missing from the shared brief. Designer Ben has prepared a layout with placeholder copy. Campaign manager Priya owns the brief; the product lead owns message approval, and the operations lead owns tracking checks. No paid placement is booked. Priya and Ben must agree the sequence and handoff conditions without presenting Monday as an unconditional release commitment.',
    cast='Priya | Campaign manager\nBen | Designer',
    culture=('A blocker needs an owner and an effect', 'Saying "we are not aligned" leaves colleagues unsure what to do. Name the missing input, its owner, and the work it prevents. You can protect another team\'s time by explaining which preparation may continue and which deliverable is not yet ready for approval.'),
    a='''Who owns the shared brief? | Priya, the campaign manager | Ben, because he prepared the layout | The operations lead, because tracking is required | Every channel owner with no single accountable person | The briefing explicitly assigns ownership of the shared campaign brief to Priya.
Which work has actually been prepared? | A layout containing placeholder copy | A fully approved landing page | A booked paid-media placement | A final measurement report | Ben has a layout with temporary wording; the other deliverables are not established as complete.
How should Monday be described? | A target date subject to unresolved release conditions | An unconditional public commitment | The date all reviewers have already approved | The final performance-reporting deadline | The audience, message, and measurement dependencies remain unresolved, so release is not yet authorized.''',
    vocabulary='''go-to-market plan | A coordinated plan for bringing an offering to its intended market. | align the go-to-market plan
campaign brief | A shared statement of audience, objective, message, and delivery requirements. | complete the campaign brief
deliverable | A specified output that a person or team must supply. | define the deliverable
dependency | Something that must be available for another task to proceed. | resolve a dependency
critical path | The sequence of dependent tasks that determines earliest completion. | identify the critical path
workback schedule | A timeline planned backward from a target date. | build a workback schedule
launch readiness | The state of meeting the conditions required for release. | assess launch readiness
go/no-go decision | A decision to proceed with or stop a planned release. | hold the go/no-go review
sign-off | Recorded approval by the relevant responsible person. | obtain message sign-off
single source of truth | The agreed authoritative location for current information. | maintain a single source of truth
version control | Management of revisions so the current approved version is identifiable. | apply version control
asset specification | Requirements such as format, dimensions, or file type for an asset. | confirm the asset specification
creative brief | Direction for developing a specific creative response. | refine the creative brief
channel mix | The combination of communication channels selected. | agree the channel mix
media booking | A commitment reserving advertising inventory. | confirm the media booking
tracking plan | A description of events and identifiers used to measure behavior. | validate the tracking plan
UTM parameter | A tagged URL field used to identify campaign traffic sources. | standardize UTM parameters
acceptance criterion | A defined condition a deliverable must meet. | set acceptance criteria
handoff | Transfer of work with the context required for the next owner. | prepare a complete handoff
approver | The person authorized to accept a particular deliverable. | identify the approver
RACI matrix | A map of responsible, accountable, consulted, and informed roles. | clarify roles in a RACI matrix
scope creep | Expansion of work beyond the agreed scope without corresponding agreement. | flag scope creep
change request | A proposed alteration to an agreed deliverable or plan. | document the change request
contingency | An alternative action prepared for a possible disruption. | agree a launch contingency''',
    precision='A target expresses an intended date; a commitment adds an agreed obligation. Ready for review differs from approved for release. List the conditions explicitly so that a shared calendar does not become mistaken evidence of completed approval.',
    precision_extra='Ownership should attach to a specific object. Priya owns the brief, the product lead approves the message, and operations checks tracking. Saying everyone owns launch can hide the person who must resolve a missing input or make the go/no-go decision.',
    phrases='''Name the gap | The calendar has channels and a date, but the brief is incomplete.
Separate readiness | The layout is ready for discussion, not for publication.
Assign the owner | I own the brief; the product lead owns message approval.
Specify the dependency | Final creative depends on the audience and approved message.
Protect the work | You can check dimensions now without finalizing the copy.
Define the handoff | Please use the approved version linked from the shared brief.
Qualify the date | Monday remains the target, subject to the release conditions.
Close with conditions | We need message sign-off and tracking checks before go/no-go.
Request a measure | Which defined behavior will count as campaign success?
Keep one record | Let us record decisions in the shared brief.
Avoid false completion | A placeholder is not approved wording.
Describe the impact | A late message change will affect layout and review time.
Control revisions | Route a new message through the change request.
Confirm the next owner | Who receives the asset after the review is complete?
Separate booking | No placement has been booked, so do not report a confirmed reservation.
Summarize the sequence | Brief first, then final creative, checks, and release authorization.''',
    notes='''Depends on | This phrase explains a work sequence rather than merely saying a task is late.
Subject to | Use it with explicit conditions; alone it can conceal what remains unresolved.
Ready for | Complete the phrase with review, testing, or release to identify the actual state.
Own versus approve | Creating or coordinating an item does not automatically confer approval authority.
Target versus confirmed | Keep this distinction on the calendar and in spoken summaries.
Placeholder | Name temporary content so another team does not mistake it for approved copy.''',
    d='''Which update correctly describes the design state? | A layout exists, but it still contains placeholder copy. | Creative is approved because the layout exists. | The landing page is published but unmeasured. | All channel assets have completed sign-off. | The supplied work is a draft layout, not an approved or published set of assets.
Which sequence fits the dependencies? | Complete the brief, finalize creative, check requirements, then authorize release. | Book all media, release placeholders, then define the audience. | Approve performance, choose a metric, then draft the message. | Finalize every asset before identifying the message approver. | The audience and approved message are inputs to final creative, and checks precede release authorization.
Who should resolve message approval? | The product lead | The designer by silently selecting copy | The operations lead by testing a URL | The media seller after booking | The briefing assigns message approval to the product lead, not to the other named roles.
Which statement keeps Monday accurate? | Monday is our target; unresolved release conditions still need closure. | Monday is guaranteed because the calendar contains it. | Monday is canceled because one draft exists. | Monday is approved once any team member agrees. | A target remains possible without becoming a guarantee or an already authorized release.''',
    dialogue='''Priya | The calendar shows a Monday launch across email, paid social, and the landing page. Before we call it ready, what does your layout still need?
Ben | A complete [[campaign brief::The brief supplies audience, objective, message, and delivery context that a channel calendar alone does not provide.]]. I have placed temporary copy, but I cannot finalize the design without the audience, approved message, and the action we want people to take.
Priya | I own that document. The product lead owns message approval, and operations owns tracking checks. I will put those roles next to the missing inputs.
Ben | Good. The approved message is a [[dependency::Final design depends on the approved message because wording changes can alter layout and require further review.]] for final creative, not just something we can add at the very end without affecting the layout.
Priya | Is there useful preparation you can continue while I resolve those inputs? I do not want the whole process to stop unnecessarily.
Ben | I can check each [[asset specification::Asset specifications cover format requirements that can be checked before final wording is supplied.]], including dimensions and file formats. I will keep the temporary text labeled so nobody treats the preparation as approved campaign material.
Priya | The calendar has made Monday look definite. We should explain the remaining conditions before someone tells sales or a media partner that release is confirmed.
Ben | Let us use a [[workback schedule::A workback schedule identifies the tasks and review time needed before the target rather than treating the date as evidence of readiness.]]. Work backward from Monday and show the review time required after the final message arrives.
Priya | I will add a specific success measure to the brief. The channel list does not tell us whether we are seeking demonstration requests or something else.
Ben | And the [[tracking plan::The tracking plan defines what will be recorded; it must match the agreed campaign action rather than merely count page visits.]] must match that action. A page view and a completed request are different events, even if both appear in the dashboard.
Priya | Operations will check that once we have the measure. For message approval, I will ask the product lead to identify the exact version being accepted.
Ben | That [[sign-off::Sign-off must identify the approved content; otherwise a later or different draft may be mistaken for the accepted version.]] should link to the content itself. An approval in a chat thread is hard to use if nobody can tell which draft it covered.
Priya | We can make the shared brief the authoritative record, with links to approved content and the outstanding decisions. Will that reduce conflicting copies?
Ben | Yes, a [[single source of truth::An agreed authoritative record reduces ambiguity about which brief, decision, and asset version is current.]] helps. I will link the final asset there rather than send several files with nearly identical names to every channel owner.
Priya | What if the product lead changes the message after you have finished the design? We need to make the timing effect visible.
Ben | Treat it as a [[change request::A change request makes the new requirement and its effect on work, review, and timing explicit.]]. I will identify the affected assets and review steps before we promise that the original date still holds.
Priya | No paid placement has been booked, so we are not canceling a confirmed reservation. We are clarifying what must happen before release.
Ben | Exactly. The [[go/no-go decision::The go/no-go decision authorizes or stops release after reviewing readiness; it is separate from the target date.]] should come after the message and tracking checks, not be inferred from a date that was entered before the brief was complete.
Priya | I will update the brief and its owners today. Monday stays a target, with the unresolved conditions clearly shown to the teams.
Ben | I will prepare the design [[handoff::The handoff transfers the correct asset and context to the next owner after the required inputs and reviews are complete.]] once those inputs are ready. That gives everyone a usable sequence without calling a placeholder layout a finished campaign.''',
    transfer_title='One change, three affected assets',
    transfer_setup='An approved campaign has an email, landing page, and social post. A revised offer has been proposed but not approved. All three assets currently show the old offer.',
    transfer='''Manager: "The new offer is a proposed ___." | change | The supplied facts distinguish the proposed revision from the currently approved offer.
Designer: "It affects all three campaign ___." | assets | Each named asset contains the old offer and would need coordinated revision.
Manager: "We need the relevant ___ before release." | approval | The new offer is not approved, so a proposal cannot be treated as release authorization.
Designer: "I will then check that every version is ___." | consistent | Coordinated revision must ensure the email, page, and post communicate the same approved offer.'''))


BOOK['units'].append(unit(
    title='Content, SEO, Thought Leadership, and Editorial Judgment', scene='The how-to article that never gives instructions',
    skill='Give precise editorial feedback when a search-led article fails to deliver its stated promise.',
    brief='An article targets the query "how to create a meeting agenda." Its title promises a practical guide, but the body announces a scheduling product and lists features. The content brief requires a usable agenda example and a sequence readers can follow without buying anything. Neither is in the draft. Editor Sofia and writer Ellis must restructure the article, retain only relevant product references, and check the example before publication. No ranking improvement or numerical traffic increase has been established.',
    cast='Sofia | Content editor\nEllis | Content writer',
    culture=('Separate editorial judgment from personal taste', 'A writer can act on feedback tied to the reader\'s task, the title\'s promise, and the supplied brief. "Make it more engaging" is less usable than identifying the missing example. Be direct about the gap while preserving useful material for a more suitable format.'),
    a='''What task does the query indicate? | Learning how to create a meeting agenda | Reading a product-release announcement | Comparing subscription prices | Finding a company careers page | The query asks for instructions, which matches the practical guide promised by the title.
Which required elements are missing? | An agenda example and a usable sequence | A product-feature list and announcement | A paid-media budget and conversion forecast | A competitor ranking and an award badge | The briefing explicitly requires the example and sequence, neither of which appears in the draft.
Which outcome cannot currently be promised? | A ranking improvement or traffic increase | A revision to the article structure | A check of the example before publication | Removal of irrelevant product references | The case supplies an editorial problem, not evidence of a future search-performance result.''',
    vocabulary='''search intent | The task or purpose behind a search query. | match search intent
query | The words a person enters into a search system. | interpret the query
informational intent | A search purpose focused on learning or solving a problem. | serve informational intent
commercial intent | A search purpose involving evaluation of possible purchases. | distinguish commercial intent
keyword research | Investigation of search terms and the needs they represent. | conduct keyword research
search volume | An estimate of how often a term is searched in a defined period. | interpret search volume
SERP | Search engine results page, showing results for a query. | review the SERP
content brief | Direction specifying an article's audience, purpose, scope, and requirements. | follow the content brief
editorial angle | The specific perspective or approach of a piece. | refine the editorial angle
outline | An ordered plan of a piece's sections. | revise the outline
lead paragraph | The opening paragraph that establishes the piece's direction. | rewrite the lead paragraph
subheading | A heading within a larger piece that organizes its sections. | write descriptive subheadings
worked example | A completed example demonstrating how something is done. | include a worked example
content gap | Missing material needed to meet the audience's task. | close the content gap
internal link | A link connecting pages within the same site. | add a relevant internal link
anchor text | The visible linked wording describing a destination. | use descriptive anchor text
metadata | Information describing or supporting a page outside its main body. | review page metadata
title tag | An HTML element specifying a page's title for systems and displays. | align the title tag
meta description | A page summary that a search engine may use in a snippet. | write a useful meta description
canonical URL | The preferred representative URL for duplicate or similar pages. | specify the canonical URL
crawlability | The ability of a crawler to access page content. | check crawlability
indexability | Whether a page can be included in a search engine's index. | investigate indexability
thought leadership | Content offering a supported, useful perspective on a field. | substantiate thought leadership
editorial review | Assessment of accuracy, usefulness, structure, and publication readiness. | complete editorial review''',
    precision='Search volume describes estimated demand for a query, not whether a draft satisfies it. A how-to title makes a content promise. An announcement can be useful elsewhere while still being the wrong response to a reader seeking practical instructions.',
    precision_extra='Crawlability, indexability, and ranking are different questions. A technically accessible page is not guaranteed a high position. Likewise, a clear title or meta description does not guarantee exactly how a search system will display the result.',
    phrases='''Name the reader task | The searcher wants to create an agenda, not read a launch announcement.
Identify the gap | The title promises a guide, but the required example is missing.
Preserve useful work | The feature summary may belong in the product announcement.
Request a structure | Start with the steps, then show a completed agenda.
Check independence | Can the reader use this guidance without buying the product?
Limit promotion | Keep product references only where they help the stated task.
Avoid a forecast | We can improve the article's fit without promising a ranking increase.
Close with review | We will check the example and title against the revised body.
Make feedback concrete | Add the decision, owner, and time allocation to the agenda example.
Clarify the angle | This piece teaches a process rather than announcing availability.
Review links | Use descriptive link text that matches the destination.
Separate technical checks | Being accessible to a crawler is not the same as ranking well.
Check the promise | Does each main section help deliver what the title offers?
Retain accuracy | Do not invent usage results to make the guide sound authoritative.
Specify the opening | The first paragraph should address the reader's immediate task.
Mark the next step | Return the revised outline before polishing the final copy.''',
    notes='''Promises versus covers | Compare what a heading leads readers to expect with what the body actually supplies.
May belong | This phrase redirects usable material without calling it universally bad.
How to | A how-to title sets an expectation of practical process, not just product benefits.
Without buying | This condition makes the usefulness requirement in this particular brief concrete.
Can improve versus will rank | An editorial improvement and a guaranteed search outcome are different claims.
Relevant link | Relevance depends on the reader's task and the actual destination.''',
    d='''Which feedback most directly resolves the stated problem? | Add the required sequence and worked agenda before refining promotional copy. | Increase keyword repetition while leaving the announcement unchanged. | Replace the title with a stronger how-to promise without changing the body. | Add a traffic forecast to justify the existing draft. | The missing instructional content is the core gap between the brief, title, and draft.
Which sentence correctly limits the search claim? | Better task alignment does not guarantee a ranking increase. | A useful example guarantees first position. | Indexability proves the content is the best result. | Search volume guarantees visits to this particular page. | Content fit, technical eligibility, and actual search performance are distinct questions.
Which use of the feature summary best fits the brief? | Move the general announcement elsewhere and retain only task-relevant references. | Place every feature before the first instruction. | Treat the feature list as the complete agenda example. | Remove the required sequence to shorten the piece. | Useful promotional material can be repurposed without displacing the promised instructional content.
Which check belongs before publication? | Verify that the completed example matches the steps and title. | Assume an attractive layout confirms factual accuracy. | Call the article independently validated because it has links. | Promise traffic before the example is tested. | The case requires checking the example, and consistency with the instructions is part of that editorial task.''',
    dialogue='''Sofia | The title promises a guide to creating a meeting agenda, but the opening announces our product. What does the searcher need to do?
Ellis | The [[search intent::The query asks for practical instructions; this intended task differs from interest in a product announcement.]] is practical. Someone needs an agenda they can build and use, not simply a list of reasons to buy our scheduling product.
Sofia | Exactly. The brief requires a usable example and a sequence that works without a purchase. I cannot find either in the current draft.
Ellis | That is the central [[content gap::The absent sequence and example prevent the draft from meeting the explicitly stated instructional requirement.]]. I used the feature summary as the body, so the title now promises a kind of help the article does not deliver.
Sofia | The feature summary may still be useful for the announcement. Let us avoid discarding good material just because it is in the wrong place.
Ellis | I will revise the [[outline::The outline establishes the sequence of sections before the writer refines individual sentences or promotional details.]] around the reader's task first: define the meeting outcome, choose the topics, assign owners, and allocate time before sharing the agenda.
Sofia | Then show the result. Readers should not have to guess what that sequence produces when they try to use it for an actual meeting.
Ellis | I can add a [[worked example::A worked example demonstrates the completed output of the instructions, rather than merely naming the product's features.]] with a meeting objective, timed topics, and owners. We can check it against the steps before I polish the final wording.
Sofia | The opening should explain the immediate task and lead into that process. It does not need to announce the product's availability first.
Ellis | I will rewrite the [[lead paragraph::The lead paragraph sets the article's direction; opening with the reader's task aligns it with the guide's promise.]] so it introduces the agenda problem. The product mention can appear later only if it genuinely helps a step.
Sofia | How will you handle links? A repeated invitation to learn more does not tell the reader what they will find after leaving the guide.
Ellis | I will use descriptive [[anchor text::Anchor text is the visible linked wording; describing the destination helps readers understand the link's relevance.]] for a relevant template or related explanation. I will also check that each destination actually provides what the linked words promise.
Sofia | The keyword has a large estimated search volume. Someone may ask whether fixing the article means we can promise a specific increase in visits.
Ellis | No. [[search volume::Search volume estimates how often a query is used; it does not forecast visits to this specific article.]] describes estimated searches, not our guaranteed traffic. We can explain the editorial improvement without inventing a ranking or numerical performance result.
Sofia | The page settings also need review. I do not want the displayed promise and the revised body to drift apart during production.
Ellis | I will align the [[title tag::The title tag identifies the page to systems and displays; it should fit the actual instructional content.]] with the actual guide and check the summary text. That still does not let us dictate every search-result presentation.
Sofia | Technical colleagues will check access separately. We should not describe that check as proof that the content is useful or certain to rank.
Ellis | Agreed. [[crawlability::Crawlability concerns a crawler's access to the page, not the quality of the article or a guaranteed search position.]] answers whether a crawler can access the page. It is a different issue from whether our example gives the reader workable instructions.
Sofia | Send the revised structure and example first. We can resolve the substance before spending another round on sentence rhythm and product mentions.
Ellis | I will return those for [[editorial review::Editorial review checks the substance and publication readiness; a revised draft is not automatically a finished or approved guide.]]. The finished piece should deliver the title's promise, while the announcement carries the broader feature story in its proper place.''',
    transfer_title='A comparison page with no comparison',
    transfer_setup='A page promises to compare two service plans. The draft describes only Plan A. The current plan documents are available; neither plan has been selected for the reader.',
    transfer='''Editor: "The title promises a ___." | comparison | A two-plan comparison requires information about both plans rather than one promotional description.
Writer: "I need the relevant terms for ___ plans." | both | The supplied task covers two plans, so omitting either prevents a meaningful comparison.
Editor: "Use the current plan ___ for factual details." | documents | The current documents are the supplied factual basis, not invented benefits or assumed terms.
Writer: "I will not present one plan as the reader's completed ___." | choice | No plan has been selected for the reader, so the page should not claim an existing decision.'''))


BOOK['units'].append(unit(
    title='Paid Media, Performance Marketing, and Attribution', scene='The campaign and the discount changed together',
    skill='Explain reported performance while resisting an unsupported claim of incremental impact.',
    brief='A paid campaign reports 80 attributed orders in week one and 120 in week two, with $2,400 media spend in each week. The campaign creative changed at the start of week two, and a 20% storewide discount began that same day. The attribution model and reporting window were unchanged, but there was no control group. Analyst Darius and growth lead Mae review a slide claiming the creative caused 40 additional orders. Revenue, margin, and total acquisition costs have not been supplied.',
    cast='Darius | Marketing analyst\nMae | Growth lead',
    culture=('Correct the causal verb, not the useful result', 'A report can show a genuine increase without proving what caused it. Keep the observed result and cost calculation, then explain what is missing from the causal claim. This helps colleagues use the data without feeling that every positive result is being dismissed.'),
    a='''What is the reported cost per attributed order in week two? | $20 | $30 | $40 | $50 | Dividing the stated $2,400 media spend by 120 attributed orders gives $20 per order.
Which two factors changed together? | Creative and the storewide discount | The attribution model and reporting window | Media spend and a control-group assignment | Margin and the definition of revenue | The briefing states that new creative and a 20% discount began on the same day.
What prevents the slide's causal conclusion? | The before-and-after data do not isolate creative from the concurrent discount. | The reported order count did not increase. | The media spend increased by 50%. | A controlled experiment showed no creative effect. | Both changes occurred together without a control group, so the creative's separate causal effect is not established.''',
    vocabulary='''impression | A recorded display of advertising under a platform's definition. | count ad impressions
reach | The distinct audience estimated to have been exposed. | report unique reach
frequency | Average exposures per reached person under a defined calculation. | monitor ad frequency
click-through rate | Clicks divided by impressions on a stated basis. | compare click-through rates
cost per click | Advertising spend divided by recorded clicks. | calculate cost per click
cost per mille | Cost per thousand impressions. | compare cost per mille
cost per acquisition | Cost divided by defined acquisition actions within a stated scope. | specify the cost-per-acquisition basis
return on ad spend | Attributed revenue divided by advertising spend under a stated method. | qualify return on ad spend
attribution model | Rules or methods assigning credit for a conversion to interactions. | identify the attribution model
attribution window | The time interval in which an interaction can receive conversion credit. | confirm the attribution window
last-click attribution | A model assigning credit to the last eligible click. | interpret last-click attribution
view-through conversion | A conversion credited after an eligible ad view without a qualifying click. | separate view-through conversions
incrementality | The additional outcome caused by an intervention relative to its absence. | estimate incrementality
holdout group | A group withheld from an intervention for comparison. | define the holdout group
confounder | A factor that complicates attributing an observed relationship to one cause. | identify a possible confounder
baseline | A defined starting or comparison level. | document the baseline
conversion lag | Delay between an interaction and a recorded conversion. | account for conversion lag
deduplication | Removing duplicate records so the same event is not counted repeatedly. | apply conversion deduplication
pixel | Tracking code or a small resource used to record events. | validate the tracking pixel
bid strategy | Rules governing how advertising bids are set. | review the bid strategy
budget pacing | Management of spending across the planned campaign period. | adjust budget pacing
creative fatigue | Reduced response associated with repeated exposure to the same creative. | investigate creative fatigue
audience overlap | Shared people across two or more target groups. | measure audience overlap
blended acquisition cost | Acquisition cost calculated across a specified combined set of channels or costs. | define blended acquisition cost''',
    precision='Orders attributed to a channel are not automatically orders caused by that channel. Here, media spend per attributed order fell from $30 to $20. That arithmetic is supported; a claim that the creative generated all 40 extra orders is not.',
    precision_extra='Cost per order is not profit. Revenue, margin, returns, and costs beyond media are missing. Keep the metric label attached to the numerator and denominator, and avoid relabeling a platform cost metric as total customer-acquisition cost without the required inputs.',
    phrases='''Lead with the result | Attributed orders rose from 80 to 120 at the same media spend.
State the cost basis | Media cost per attributed order fell from $30 to $20.
Name the concurrent change | The storewide discount began when the creative changed.
Limit causality | This comparison does not isolate the effect of the creative.
Preserve the useful finding | The reported improvement is real in the stated reporting data.
Define attribution | The platform assigns credit under its model and window.
Request a stronger design | We need an appropriate comparison to estimate incremental impact.
Close with accurate wording | Report the increase without assigning all of it to the creative.
Separate profitability | We do not have the revenue or margin data for that conclusion.
Check the window | Use the same reporting window before comparing the figures.
Allow for lag | Some conversions may be recorded after the first report.
Check duplication | Confirm whether overlapping sources count the same order.
Avoid metric substitution | Media cost per order is not automatically total acquisition cost.
Identify the denominator | Are these orders, customers, or another conversion action?
Keep the discount visible | The promotion is a material part of the comparison.
Describe uncertainty | The creative may have contributed; its separate effect remains unmeasured.''',
    notes='''After versus because of | After describes timing; because of attributes causation.
Attributed versus incremental | Attributed reflects reporting credit; incremental concerns additional outcomes caused.
Per order | Keep the unit explicit, especially when repeat orders differ from new customers.
Fell from and to | Stating both endpoints makes the improvement auditable.
May have contributed | This preserves a possible explanation without declaring a measured causal effect.
Same spend | Holding one factor constant does not mean all other relevant factors were controlled.''',
    d='''Which headline matches the evidence? | Attributed orders rose 50% while creative and the discount changed together. | New creative caused a verified 50% incremental order lift. | The discount had no effect because spend was unchanged. | Profit rose 50% because attributed orders rose 50%. | Orders increased by 40 from an 80-order base, but simultaneous changes prevent isolating creative's causal effect.
Which metric can be calculated from the supplied data? | Media cost per attributed order | Net profit per acquired customer | Total lifetime customer value | Incremental return on investment | The case provides media spend and attributed orders, but not the other required inputs or causal estimate.
What does unchanged attribution establish? | The stated credit method stayed consistent, not that creative caused the increase. | The creative's causal contribution is exactly 40 orders. | The discount contributed no orders. | The reported conversions are all new customers. | A stable reporting method supports comparison but does not remove the concurrent intervention or identify customer type.
Which revision avoids overstating the result? | Replace caused with accompanied and disclose the concurrent promotion. | Keep caused but put the discount in an unrelated appendix. | Omit week one so no comparison can be checked. | Rename attributed orders as incremental orders. | The revision preserves the observation while making the competing explanation visible instead of changing the metric's meaning.''',
    dialogue='''Mae | The slide says the new creative caused forty additional orders. Orders rose from eighty to one hundred twenty, so the story looks strong.
Darius | The increase is clear in the [[attribution::Attribution assigns reporting credit; the resulting order increase does not itself establish what caused it.]] report. The problem is the word caused, because the storewide discount started on the same day as the creative change.
Mae | We kept media spend at twenty-four hundred dollars in both weeks. Does that at least support the claim that the campaign became more efficient?
Darius | On the specified [[cost per acquisition::Here the defined acquisition action is an attributed order and the stated cost scope is media spend only.]] measure, yes: media spend per attributed order fell from thirty dollars to twenty. We should keep that exact cost and action basis in the label.
Mae | I was going to call it total customer-acquisition cost. We do not have sales costs or a count of newly acquired customers, though.
Darius | Then that label would be too broad. A [[blended acquisition cost::A combined acquisition-cost measure requires its own included costs, channels, and acquisition denominator, which are not supplied here.]] requires defined included costs and a suitable denominator. The platform's attributed orders may not all represent new customers.
Mae | The report uses the same model as last week. I thought that would make it fair to credit the entire increase to the campaign change.
Darius | A stable [[attribution model::Keeping the credit-assignment method unchanged supports reporting consistency but does not separate simultaneous causal influences.]] makes the reporting method consistent. It does not remove the discount or tell us how orders would have changed without the new creative.
Mae | So the promotion is not a reason to discard the report, but it is a reason to qualify our explanation of the increase.
Darius | Exactly. It is a possible [[confounder::The concurrent discount complicates attributing the change to creative alone, because both interventions could affect orders.]]. Both changes could influence orders, and the simple before-and-after comparison cannot separate their effects.
Mae | What evidence would let us discuss the creative's additional contribution more confidently, rather than just repeat the platform's allocation of credit?
Darius | We would need a suitable design for measuring [[incrementality::Incrementality concerns outcomes added by the intervention relative to what would have occurred without it.]], with the relevant comparison and assumptions reviewed. This report alone cannot supply the outcome that would have occurred without the creative change.
Mae | Would withholding the new creative from a comparable group help, provided the promotional conditions and measurement were planned properly?
Darius | A carefully designed [[holdout group::A holdout provides a comparison, but its design and comparability must support the intended causal question.]] could be part of that approach. We would need to review assignment, exposure, and other differences before interpreting a result as causal.
Mae | For today's update, I can state the order increase and lower media cost per order. Can I also say return on ad spend improved?
Darius | We have no revenue figure, so we cannot calculate [[return on ad spend::Return on ad spend needs an appropriate revenue numerator; order counts and spend alone cannot determine it.]]. The discount also makes it especially important not to assume that more orders mean the same proportional revenue or profit increase.
Mae | I will check that we are comparing complete periods. A few late orders could change the counts if one week has had longer to mature.
Darius | Yes, check the [[conversion lag::Conversion lag can make an early reporting period incomplete relative to a more mature comparison period.]] and keep the reporting window explicit. We should also confirm duplicate-order handling before combining results from different sources.
Mae | Then the slide will say attributed orders rose fifty percent while creative and the discount changed together. Their separate effects remain unmeasured.
Darius | That preserves the improvement against the stated [[baseline::The baseline is the first week's defined comparison level, not an experimental estimate of the no-change outcome.]]. We can recommend a stronger measurement plan without turning a useful observation into a causal claim the evidence cannot support.''',
    transfer_title='Two dashboards, one order',
    transfer_setup='Two advertising platforms each claim credit for the same single order. The sales system records one order. No experiment has isolated either platform\'s incremental effect.',
    transfer='''Analyst: "The sales record contains one ___." | order | Both platform credits refer to the same single sales event in the supplied facts.
Lead: "Combining platform counts requires ___." | deduplication | Adding both credits without removing overlap would count one order twice.
Analyst: "Credit assignment is ___, not proof of cause." | attribution | The platform reports allocate credit under their rules rather than establish a separate causal effect.
Lead: "Neither report alone establishes ___." | incrementality | Without an appropriate causal comparison, neither platform's additional effect is identified.'''))


BOOK['units'].append(unit(
    title='Lifecycle, CRM, Email, Marketing Ops, and Sales Handoff', scene='A hundred contacts are not a hundred sales requests',
    skill='Clarify lifecycle status and routing rules without turning activity records into invented buying intent.',
    brief='A campaign export contains 100 contacts: 20 submitted a demonstration request, 60 downloaded a guide, and 20 have no recorded source. Contact permissions and suppression status have not been checked. The company\'s stated handoff procedure requires a verified source, a documented sales request, completed permission checks, and a named owner before a record is routed as sales-ready. Marketing-operations specialist Jules and sales-development lead Nico must correct an email calling all 100 contacts ready for sales outreach.',
    cast='Jules | Marketing-operations specialist\nNico | Sales-development lead',
    culture=('A shared label needs a shared threshold', 'Sales and marketing may use the same word for different stages. Ask what event and checks the label represents before debating lead quality. This keeps the discussion factual and avoids blaming either team for a handoff whose rules were never applied consistently.'),
    a='''How many contacts have a documented demonstration request? | 20 | 60 | 80 | 100 | The supplied export separates 20 demonstration requests from 60 guide downloads and 20 unknown-source records.
What remains unchecked across the export? | Contact permissions and suppression status | Whether all records contain a source | The existence of 20 demonstration requests | Whether a guide-download category exists | The briefing explicitly says permission and suppression checks have not yet been completed.
Can all 100 records currently be called sales-ready under the stated procedure? | No; the request, source, checks, and ownership conditions are not all met. | Yes; an email address is sufficient under the stated procedure. | Yes; downloading a guide is the same as requesting a sales call. | No; the company prohibits responding to any demonstration request. | The company's supplied criteria require more than contact details, and the case does not impose a blanket ban on responding.''',
    vocabulary='''CRM | Customer relationship management system or practice for relationship records. | update the CRM record
lifecycle stage | A defined position in a contact's relationship with the organization. | verify the lifecycle stage
lead | A potential customer record whose qualification depends on agreed criteria. | review a new lead
marketing-qualified lead | A lead meeting the organization's stated marketing qualification criteria. | define a marketing-qualified lead
sales-qualified lead | A lead meeting the organization's stated sales qualification criteria. | confirm a sales-qualified lead
lead scoring | Applying defined values to attributes or behavior to prioritize leads. | calibrate lead scoring
fit score | A score representing alignment with the target customer profile. | review the fit score
intent signal | Behavior suggesting interest without necessarily proving a buying decision. | interpret an intent signal
lead source | The recorded origin of a contact or lead. | verify the lead source
source provenance | The traceable history of how data was obtained. | preserve source provenance
consent record | A record of permission with relevant scope and context. | check the consent record
suppression list | Records excluded from specified communication activity. | apply the suppression list
unsubscribe | A request or action to stop a type of communication. | process an unsubscribe
preference center | A place where recipients manage communication choices. | update the preference center
double opt-in | A process confirming a subscription through a second action. | document the double opt-in
deliverability | The ability of messages to reach their intended inbox destination. | monitor deliverability
hard bounce | A delivery failure generally indicating a persistent address problem. | suppress a hard bounce
soft bounce | A delivery failure often associated with a temporary condition. | investigate a soft bounce
nurture sequence | A planned series of communications supporting a relationship over time. | review the nurture sequence
triggered email | A message initiated by a defined event or condition. | test the triggered email
segmentation rule | A criterion used to assign records to an audience group. | validate a segmentation rule
routing rule | A condition determining which owner receives a record or task. | apply the routing rule
service-level agreement | An agreement defining service responsibilities and response expectations. | clarify the service-level agreement
recycle reason | A recorded explanation for returning a lead to an earlier process stage. | document the recycle reason''',
    precision='A downloaded guide is a recorded action, not a stated request for a sales conversation. Qualification labels are organization-specific. This case supplies its own handoff conditions; do not replace them with an assumed universal meaning of MQL or SQL.',
    precision_extra='A permission record needs context such as channel, purpose, and status. Do not infer universal legal permission or prohibition from the presence of an address. Apply the supplied company procedure and obtain qualified review of the actual jurisdictions and communication types.',
    phrases='''Correct the count | Twenty contacts requested demonstrations; the other records have different statuses.
Separate actions | A guide download is not a documented sales request.
Name the missing check | Permissions and suppression status remain unverified.
Apply the threshold | Use the stated handoff criteria before marking a record sales-ready.
Preserve the source | Keep the original event and source history in the CRM.
Assign an owner | Each eligible handoff needs a named receiving owner.
Avoid an invented status | Unknown source should remain unknown until verified.
Close with routing | Route the verified requests through the agreed process.
Clarify the label | What conditions does qualified represent in this workflow?
Keep checks distinct | A demonstration request does not erase a separate suppression check.
Limit the batch | Do not describe the entire export as a single audience.
Check scope | Does the permission record cover this channel and purpose?
Request the trail | Please attach the source event and current status.
Explain a return | Use a specific recycle reason rather than simply rejecting the lead.
Protect the record | Do not overwrite the original source to make the export look complete.
Measure the handoff | Count records that meet the criteria, not every row in the file.''',
    notes='''Requested versus downloaded | These verbs describe different actions and must not be treated as interchangeable intent.
Qualified for what | A label needs the next action and applicable threshold.
Unknown versus absent | An unknown permission status is not evidence of either permission or a confirmed opt-out.
Pending checks | This phrase records an unfinished process without inventing its eventual result.
Every row versus eligible records | The denominator changes when a report filters by handoff conditions.
Company procedure | The supplied operational rule is not a statement of all jurisdictions' legal requirements.''',
    d='''Which handoff summary is accurate? | Twenty demonstration requests are identified, with required checks still pending. | One hundred contacts requested a sales conversation. | Sixty guide downloads prove purchase authority. | All unknown-source contacts have already opted out. | The summary preserves the known request count and does not invent results for the unfinished checks.
Which action preserves record integrity? | Retain the original source and mark unverified fields for review. | Replace all sources with demonstration request to simplify routing. | Delete suppression flags when a campaign target is missed. | Call unknown permission confirmed because an address exists. | Source history and uncertainty should remain visible rather than be overwritten to satisfy a target.
Which record fits the stated sales-ready rule? | A documented request with verified source, completed permission checks, and a named owner | Any guide download with a high engagement score | Any email address without a source | Any contact included in the export filename | Only the first description includes every handoff condition supplied in the briefing.
Which question resolves a qualification disagreement? | Which event and completed checks does this stage require? | Which team should own every unsuccessful sale? | Can we use qualified without defining it? | Should source evidence be removed to avoid delay? | Asking for the stage's concrete criteria turns an ambiguous label into a testable operational definition.''',
    dialogue='''Nico | The campaign email says we have one hundred sales-ready contacts. Before my team starts outreach, can you show me what those people actually requested?
Jules | The [[CRM::The CRM holds the relationship records, including the different events that produced this export.]] export has twenty demonstration requests, sixty guide downloads, and twenty records with no source. Those are three different situations, not one consistent sales-ready group.
Nico | The downloaders have shown interest, though. Could we describe that as enough intent for a sales call and route them with the demonstration requests?
Jules | A download is an [[intent signal::An intent signal can suggest interest without establishing the specific sales-conversation request required by this company's procedure.]], but it is not the documented sales request our procedure requires. We should preserve what happened rather than strengthen the event's meaning.
Nico | That makes sense. What about the twenty people who explicitly asked for a demonstration? Are their records ready to assign now?
Jules | Their [[lead source::The recorded demonstration-request source is one criterion, but permission, suppression, and ownership checks are separate requirements.]] is recorded, but permissions and suppression status have not been checked. The request does not by itself complete every condition in the handoff procedure.
Nico | I want to respond promptly without telling the team that all checks are finished. Can we mark the requests as awaiting the remaining verification?
Jules | Yes. Keep the [[lifecycle stage::The lifecycle stage must reflect the current process state rather than prematurely label an unchecked record sales-ready.]] accurate, with the missing checks visible. A pending state should tell the next colleague what remains, not become a place where requests disappear.
Nico | For the permission check, should we look only for a yes or no field? Some contacts have older records from another campaign.
Jules | Review the [[consent record::A consent record needs scope and context; an older permission entry may not answer the current channel or purpose question.]] with its channel, purpose, and status. An old flag without context is not a complete answer for this particular communication.
Nico | And if a current suppression record is present, the team should not assume the new export has somehow removed that restriction.
Jules | Correct. Apply the relevant [[suppression list::A suppression list excludes records from specified communication activity; exporting a record does not remove that status.]] through the approved process. We should resolve any apparent conflict through review, not silently overwrite the status to increase the handoff count.
Nico | Once a request meets the criteria, I need it assigned to a specific person. Otherwise both teams may assume the other one is responding.
Jules | The [[routing rule::A routing rule determines the receiving owner after the record meets the applicable handoff conditions.]] should identify that owner and preserve the source event. I will include the completed checks so the receiving colleague does not have to reconstruct the history.
Nico | We also need to agree how quickly eligible requests are acknowledged. That is a different conversation from inventing a deadline for unchecked records.
Jules | We can record it in the [[service-level agreement::The service-level agreement defines responsibilities and response expectations rather than supplying missing qualification evidence.]]. The agreement should name the responsible team and what happens if the record is incomplete, rather than hide those cases in an average.
Nico | Suppose sales returns a record because the requested topic is outside our service. A generic rejection makes it hard to improve the next campaign.
Jules | Use a specific [[recycle reason::A recycle reason explains why the record returns to an earlier process, making the handoff outcome usable for follow-up.]]. That distinguishes a scope mismatch from missing information or an unanswered request without blaming the contact or changing the original event.
Nico | I will correct the email: twenty demonstration requests are identified, required checks are pending, and the remaining eighty records are not equivalent requests.
Jules | I will keep the [[source provenance::Source provenance preserves how each record originated, including the unresolved history of unknown-source contacts.]] intact and investigate the unknown sources. We will count completed eligible handoffs, not relabel all one hundred rows to meet the campaign headline.''',
    transfer_title='An export does not renew a preference',
    transfer_setup='A contact is on the company\'s current suppression list for promotional email. A later event export includes the same address but supplies no new preference information. The team has not reviewed the conflict.',
    transfer='''Operator: "The export contains the same ___." | address | The case identifies one address appearing in both records, not evidence of a new person.
Lead: "It does not establish a changed ___." | preference | The later export supplies no new preference information, so the earlier status cannot be assumed reversed.
Operator: "I will preserve the existing suppression ___." | record | Preserving the current record avoids silently removing a restriction without evidence or review.
Lead: "Resolve the conflict through the approved ___." | process | The supplied facts call for review rather than treating the export as automatic authorization.'''))


BOOK['units'].append(unit(
    title='Analytics, Experimentation, Funnel Reporting, and Executive Readouts', scene='A higher click rate is not yet a declared winner',
    skill='Present absolute and relative differences while keeping statistical and commercial conclusions separate.',
    brief='An email test reports 120 unique clickers among 2,000 delivered messages for A and 140 among 2,000 for B. These are the only supplied results. The random assignment, planned stopping rule, and statistical analysis have not yet been checked. No purchase data are available. Director Anika wants to announce B as a proven winner. Analyst Mateo must explain the observed rates and their difference, then identify the checks required before a stronger claim or broader release decision.',
    cast='Anika | Marketing director\nMateo | Experimentation analyst',
    culture=('Give the clear number before the qualification', 'An executive can need a short answer without needing an overstated answer. Lead with the observed difference, then say what is not established and which check resolves it. Avoid burying the result under statistical vocabulary or letting a request for decisiveness turn an unfinished analysis into proof.'),
    a='''What are the observed unique clicker rates? | A: 6%; B: 7% | A: 12%; B: 14% | A: 60%; B: 70% | A: 6%; B: 14% | The rates are 120 divided by 2,000 and 140 divided by 2,000, respectively.
What is the absolute difference between those rates? | 1 percentage point | 1 percent relative | 20 percentage points | 16.7 percentage points | Seven percent minus six percent equals one percentage point; relative change uses a different calculation.
Which conclusion is currently unsupported? | B is a statistically established and commercially superior winner | B has 20 more observed unique clickers | Both reported delivery counts are 2,000 | B's observed clicker rate is higher | The design and statistical checks remain incomplete, and no purchase results establish commercial superiority.''',
    vocabulary='''A/B test | A comparison of two variants under a specified experimental design. | plan an A/B test
control variant | The reference experience used for comparison. | define the control variant
treatment variant | The changed experience whose effect is assessed. | describe the treatment variant
randomization | Assignment by a chance-based process intended to support comparable groups. | verify randomization
randomization unit | The entity assigned to an experiment condition. | choose the randomization unit
sample size | The number of observations or assigned units on a defined basis. | determine the sample size
sample ratio mismatch | An unexpected departure from the intended allocation proportions. | investigate a sample ratio mismatch
primary metric | The preselected main measure for evaluating an experiment. | specify the primary metric
guardrail metric | A measure used to detect unacceptable adverse effects. | monitor a guardrail metric
denominator | The quantity by which a numerator is divided. | verify the denominator
percentage point | The unit for an absolute difference between percentages. | report a percentage-point change
relative lift | Change divided by the baseline value, expressed on a relative basis. | calculate relative lift
confidence interval | A range produced by a method with a stated long-run coverage property. | report a confidence interval
p-value | Probability, under the null model, of results at least as extreme as observed. | interpret the p-value
statistical significance | A result meeting a specified statistical decision criterion. | assess statistical significance
practical significance | The size and relevance of an effect for an actual decision. | distinguish practical significance
statistical power | Probability of detecting a specified effect under an assumed design. | assess statistical power
minimum detectable effect | A target effect size a planned design aims to detect reliably. | specify the minimum detectable effect
stopping rule | A planned rule for when an experiment ends or is evaluated. | follow the stopping rule
multiple testing | Evaluation of multiple hypotheses, with associated error-control concerns. | account for multiple testing
cohort | A group defined by a shared entry period or characteristic. | compare like-for-like cohorts
funnel stage | A defined step in a progression toward an outcome. | distinguish funnel stages
drop-off | The loss of participants between specified stages. | measure stage-to-stage drop-off
executive readout | A concise presentation of findings, limits, and decision implications. | prepare the executive readout''',
    precision='A rises from 6% to B\'s 7% in this comparison: the absolute difference is one percentage point. Relative to 6%, the increase is about 16.7%. Twenty extra observed clickers, one percentage point, and 16.7% relative lift describe different aspects of the same counts.',
    precision_extra='Higher observed performance does not itself establish statistical significance or business value. A clicker is not necessarily a purchaser. Missing analysis is not evidence of no effect either: report the observation and the unresolved checks without declaring either certainty or failure.',
    phrases='''State the observation | A recorded 6% and B recorded 7% unique clicker rates.
Name the absolute change | The difference is one percentage point.
Give the relative basis | Relative to A's 6%, the observed increase is about 16.7%.
Limit the verdict | B is higher in this sample; a proven winner is not yet established.
Request the design check | Confirm assignment and the planned stopping rule.
Separate the outcome | We have click data, not purchase or revenue results.
Avoid the opposite error | Unfinished analysis does not prove that there is no effect.
Close with next steps | Finish the design and statistical checks before the stronger claim.
Keep the denominator | Each rate uses 2,000 delivered messages.
Identify the count | B has 20 more observed unique clickers.
Ask for uncertainty | Include the appropriate uncertainty estimate with the result.
Check the metric | Was this the preselected primary measure?
Protect the wider decision | Review relevant adverse outcomes before a broader release.
Keep timing visible | Are both groups measured over the same follow-up period?
Clarify the scope | This result does not describe every future audience.
Summarize for leaders | The observed direction is positive; the decision checks remain open.''',
    notes='''Percentage point | Use this for subtraction between two percentages, not for the relative ratio.
Relative to | This phrase names the baseline used in a relative-change calculation.
Observed | This qualifier distinguishes the actual sample result from a population or causal conclusion.
Not yet established | This is different from saying disproved or impossible.
Unique clickers | Count people on the stated basis, not repeated clicks by the same person.
Winner | Define the statistical and practical criteria before using the label as a decision.''',
    d='''Which sentence reports both forms of change accurately? | B is one percentage point higher, about 16.7% above A on a relative basis. | B is 16.7 percentage points higher and 1% above A. | B is one percentage point higher and therefore 1% better relatively. | B is twenty percentage points higher because it has twenty more clickers. | The absolute difference is 7% minus 6%; relative lift divides that one-point difference by 6%.
Which statement keeps the outcome scope correct? | The result concerns unique clickers, not confirmed purchases. | Every unique clicker became a paying customer. | The observed rate is a revenue margin. | Delivered messages are identical to completed orders. | The supplied results count clickers and deliveries, with no purchase data.
What is a justified next step? | Verify design, stopping rule, and statistical analysis before declaring a proven winner. | Declare significance because both groups contain 2,000 deliveries. | Stop all analysis because a larger observed count always decides the result. | State that B has no effect because analysis is unfinished. | Neither certainty nor no effect follows from incomplete checks; the case requires completing them.
Which readout is appropriately concise? | B's observed rate is higher; the statistical and commercial conclusions remain open. | B is guaranteed to increase purchases in every audience. | The test proves a 16.7-point revenue increase. | Nothing can be reported until a purchase occurs. | The observed rate can be reported now while its stronger implications remain qualified.''',
    dialogue='''Anika | B has one hundred forty clickers and A has one hundred twenty. Can the update say B wins, so we should send it to everyone?
Mateo | We can report the higher observed rate. The [[denominator::Each rate divides unique clickers by 2,000 delivered messages; a different denominator would change the metric.]] is two thousand delivered messages for each version, giving six percent for A and seven percent for B.
Anika | That sounds like a one-percent improvement. I want the slide to be simple, but I do not want to mix up the numbers.
Mateo | Say one [[percentage point::A percentage point expresses the absolute difference between 7% and 6%, rather than their relative change.]] for the absolute difference. Calling it one percent without the basis could make the audience think we mean the relative increase.
Anika | Then the relative improvement is one divided by six, or about sixteen point seven percent. That is much larger-sounding even though it is the same result.
Mateo | Correct. The [[relative lift::Relative lift divides the change by A's baseline rate; it does not create a larger absolute difference.]] is about sixteen point seven percent against A. We should show the original rates so the percentage cannot be mistaken for a large absolute change.
Anika | We have equal delivery counts. Does that mean the groups were comparable and the difference must be due to the email version?
Mateo | Equal totals do not verify [[randomization::Randomization concerns how units were assigned; equal delivered counts alone do not establish the assignment process.]]. We still need to check how recipients were assigned and whether the reporting followed the intended design for both groups.
Anika | The team looked at the dashboard several times while the send was running. I do not know whether they ended it according to the original plan.
Mateo | Then check the [[stopping rule::The planned stopping rule matters because outcome-driven early stopping can change how statistical evidence should be interpreted.]] before a statistical conclusion. Ending a test because the current result looks attractive is not the same as following the planned evaluation.
Anika | So we should not call the difference statistically significant just because B has twenty more clickers. Can we say it is probably a real winner?
Mateo | Not from these counts alone without the required analysis. [[statistical significance::Statistical significance depends on a specified method and criterion; a positive observed difference alone does not establish it.]] is a particular analytical conclusion, not a more impressive way of saying one number is higher.
Anika | We should include uncertainty rather than just a bold green arrow. What would help the reader understand the precision of the estimate?
Mateo | An appropriate [[confidence interval::A confidence interval communicates uncertainty under its method and assumptions; the current briefing supplies no calculated interval.]] can help once the analysis is checked. I will not invent an interval or imply that the missing review has already happened.
Anika | We also have no purchase results. Even a reliable click improvement might not mean that the message produces enough additional business value.
Mateo | Exactly. [[practical significance::Practical significance concerns decision-relevant magnitude and value; more clicks do not automatically establish more profitable purchases.]] is a separate question. We need the relevant downstream outcomes and costs before equating the click difference with commercial superiority.
Anika | Was unique clicker rate the main measure chosen beforehand? It should not become the success measure merely because this is the number that looks favorable.
Mateo | We need to confirm the [[primary metric::The primary metric is selected for evaluating the experiment; choosing it after seeing favorable results changes the evidential context.]] and review the other planned measures. The decision should not depend on selecting only a positive-looking result after the fact.
Anika | My readout will state six percent versus seven percent, one percentage point higher, with design and statistical checks unfinished and no purchase conclusion.
Mateo | That is an accurate [[executive readout::An executive readout gives the observed finding, its limits, and decision implications without converting incomplete analysis into proof.]]. We can be concise and decisive about the next checks without pretending that a full-release decision has already been justified.''',
    transfer_title='A bigger numerator, a lower rate',
    transfer_setup='Campaign C receives 90 requests from 1,000 visits. Campaign D receives 100 requests from 2,000 visits. These are observed totals, not a controlled test.',
    transfer='''Analyst: "C converts at ___ percent." | nine | Dividing 90 requests by 1,000 visits gives 9 percent.
Lead: "D converts at ___ percent." | five | Dividing 100 requests by 2,000 visits gives 5 percent despite the larger request count.
Analyst: "D has more requests but a lower ___." | rate | The count and rate move in different directions because D has twice as many visits.
Lead: "The totals do not establish a causal ___." | effect | The supplied comparison is observational rather than a controlled design isolating a campaign effect.'''))


BOOK['units'].append(unit(
    title='Compliance, Privacy, Claims, Influencers, Brand Safety, and Crisis Response', scene='Stopping a scheduled claim before it goes live',
    skill='Coordinate a publication hold, preserve review evidence, and communicate only verified status.',
    brief='A social post scheduled for 3 p.m. says a product is "100% private." The reviewer has requested revised wording and supporting evidence; approval is pending. A paid creator has received the same draft asset, but their publication status is unknown. No privacy incident has been reported in the case. Social lead Noor can pause the company queue, and campaign lead Caleb owns partner coordination. They must prevent unapproved publication, verify the partner\'s status, and keep a clear record without announcing an incident or clearance that has not been established.',
    cast='Noor | Social-media lead\nCaleb | Campaign lead',
    culture=('Use firm operational language without inventing a crisis', 'A pending review can justify a publication hold without proving a product failure. Name the exact asset and action required. Keep "requested," "confirmed," and "approved" separate so that a message to a partner does not become mistaken evidence that every copy has been stopped.'),
    a='''What is the company post's current approval state? | Pending, with wording and evidence changes requested | Fully approved because it is scheduled | Rejected as proof of a confirmed privacy incident | Cleared by the paid creator's receipt of the asset | The reviewer has requested changes and supporting evidence, so scheduling does not establish approval.
What is unknown? | Whether the paid creator has published the draft | Whether Noor can pause the company queue | Whether the reviewer requested a revision | Whether the draft says 100% private | The briefing specifically leaves the partner's publication status unverified.
Which statement would invent a fact? | A confirmed privacy incident has occurred | Approval remains pending | The company post is scheduled for 3 p.m. | The partner received the same draft | The case explicitly supplies no reported privacy incident, so one must not be announced as established.''',
    vocabulary='''publication hold | An instruction or control stopping release pending a condition. | place a publication hold
approval workflow | The sequence of review and authorization steps for release. | follow the approval workflow
claims register | A record of claims, evidence, owners, and review status. | update the claims register
absolute claim | A statement using an unrestricted expression such as always or completely. | review an absolute claim
material connection | A relationship that may affect how an endorsement is evaluated. | disclose a material connection
sponsored content | Content produced or distributed as part of a commercial arrangement. | identify sponsored content
endorsement | A promotional message expressing another party's opinion or experience. | review an endorsement
disclosure | Information made available to clarify a relevant fact or relationship. | assess the disclosure
usage rights | Permissions governing how content or an asset may be used. | verify usage rights
release form | A document recording permission for a specified use or participation. | check the release form
brand safety | Measures intended to avoid harmful advertising contexts. | review brand safety
brand suitability | The fit of a placement with a particular brand's standards. | assess brand suitability
exclusion list | Defined placements or categories barred from a campaign. | maintain an exclusion list
personal data | Information relating to an identifiable person under the applicable framework. | protect personal data
data minimization | Limiting collected or shared data to what is needed for the purpose. | apply data minimization
purpose limitation | Restricting data use to appropriate specified purposes. | check purpose limitation
retention period | The time for which information is kept under applicable requirements. | confirm the retention period
access control | Rules limiting who can view or change information. | enforce access control
incident triage | Initial assessment and routing of a reported event. | begin incident triage
holding statement | An initial message limited to verified facts while review continues. | prepare a holding statement
correction notice | A communication identifying and correcting an earlier error. | issue a correction notice
takedown request | A request to remove published material. | send a takedown request
escalation path | The designated route for raising an issue to the appropriate authority. | use the escalation path
audit trail | A traceable record of actions, decisions, and changes. | preserve the audit trail''',
    precision='Scheduled, approved, and published name different states. Pausing the company queue controls that queue; it does not prove what a partner has done. Record the exact asset, recipient, request, and confirmation rather than saying "everything is stopped" before verification.',
    precision_extra='A disclosure of payment does not establish the truth of a product claim. Likewise, a review concern is not proof of a privacy incident. Keep the commercial relationship, claim evidence, publication status, and incident status as separate questions.',
    phrases='''Name the release state | The asset is scheduled, but approval is still pending.
Give a precise hold | Pause this version in the company queue now.
Check the partner | Please confirm whether this exact asset has been published.
Preserve the evidence | Keep the draft, reviewer comments, and action history.
Limit the announcement | We have a claim-review issue, not a confirmed privacy incident.
Separate disclosure | A sponsorship disclosure does not substantiate the product claim.
Control the revision | Use only the version approved through the review workflow.
Close with confirmation | Record each hold request and the confirmation received.
Assign coordination | I will contact the partner and track their response.
Avoid overstatement | We have paused our queue; the partner's status remains unverified.
Scope a response | The statement should include only facts we have checked.
Protect private details | Move personal information into the approved restricted channel.
Check permission | Confirm the agreed usage rights before reusing the creator's asset.
Escalate specifically | The unresolved claim needs the designated review owner.
Distinguish removal | A takedown request is not confirmation that every copy is gone.
Release carefully | Resume publication only after the required approvals and version checks.''',
    notes='''Pause and withdraw | Pause stops a planned release; removing already published material is a different action.
Requested and confirmed | These words distinguish an instruction from evidence that it was carried out.
Same asset | Use an exact version identifier so partners do not act on a different file.
No confirmed incident | This limits what is known without asserting that a review can never find an issue.
Disclosure and proof | A relationship disclosure answers who is connected, not whether the product claim is true.
Only verified facts | This limits a holding statement while investigation or review remains unfinished.''',
    d='''Which immediate update is accurate after Noor pauses the queue? | Our queue is paused; the partner's publication status still needs confirmation. | Every copy on every channel is confirmed removed. | The product has suffered a confirmed privacy incident. | The reviewer has approved the claim because publication was paused. | Pausing one controlled queue establishes only that action, not partner status, incident facts, or claim approval.
Which message to the creator is most useful? | Hold this exact draft and confirm whether it has already been published. | Ignore the reviewer because the post is sponsored. | Confirm that the product is fully private in your own words. | Assume that receipt of the asset included publication approval. | The message specifies the affected version, requests a hold, and asks for the missing publication fact.
Which statement correctly separates two review issues? | Disclosing sponsorship does not prove the product claim. | Sponsorship disclosure makes any product claim acceptable. | A creator's popularity is the same as supporting evidence. | A publication hold confirms a privacy breach. | The commercial relationship and the evidence for the product assertion are distinct questions.
What belongs in the action record? | Asset version, review comments, hold requests, confirmations, and responsible owners | Only the original schedule, with all review comments deleted | A completed approval status before the reviewer responds | A confirmed partner takedown inferred from an unanswered email | A traceable record preserves what was requested, what is verified, and who must resolve the remaining work.''',
    dialogue='''Noor | The three o'clock post still says one hundred percent private. The reviewer asked for new wording and evidence, but the queue has not been paused.
Caleb | Put this exact version on a [[publication hold::A publication hold stops the unapproved release while the requested claim review remains unresolved.]] now. A scheduled time is not approval, and we should not let an unchanged draft go live while the review remains open.
Noor | I can pause the company queue. The paid creator received the same draft yesterday, but I cannot tell whether they have already posted it.
Caleb | I will use the partner [[escalation path::The escalation path identifies the responsible route for urgent partner coordination; it does not assume the partner has already acted.]] and ask them to hold the asset and confirm its publication status. I will not report their hold as confirmed until they respond.
Noor | I have paused our queue and saved the exact version. Should I remove the old file from the review record so it cannot be reused?
Caleb | Preserve the [[audit trail::The audit trail records the draft, review concern, and actions; deleting it would remove evidence needed to understand the decision.]] in the restricted record. We need the draft and reviewer comments to understand what happened, while clearly preventing that version from being used for publication.
Noor | The wording sounds absolute. I do not want to replace it with another broad promise before the reviewer explains which specific product facts can support a claim.
Caleb | Exactly. An [[absolute claim::An absolute claim leaves little or no qualification; substituting another unrestricted promise would not resolve the evidence gap.]] needs careful review. The team should not invent a softer-looking sentence that still communicates the same unsupported guarantee.
Noor | The creator's draft also needs the commercial relationship made clear. If that disclosure is added, does it settle the issue with the privacy wording?
Caleb | No. A [[material connection::A material connection concerns the relationship behind an endorsement; disclosing it does not substantiate the separate product assertion.]] is a separate question from the product evidence. Both need appropriate review; completing one does not automatically complete the other.
Noor | Someone suggested a public message apologizing for a privacy incident. We have no reported incident in this case, only the unresolved wording review.
Caleb | Do not announce an invented event. Any [[holding statement::A holding statement should stay within verified facts; an unresolved claim review does not establish a privacy incident.]] must stay within verified facts and follow the response process. A publication concern is not itself confirmation of a product failure.
Noor | If the creator replies that the post is already public, we will need a different action from pausing a scheduled post.
Caleb | Then coordinate the appropriate [[takedown request::A takedown request concerns already published content; sending it is not proof that removal has occurred everywhere.]] and correction review. Record what was requested and confirmed without claiming that one email has removed every possible copy.
Noor | Their contract also covers how we can use their photographs. We should not improvise a replacement advertisement with those images while this is being resolved.
Caleb | Check the [[usage rights::Usage rights define permitted uses of the creator's assets; access to a file does not establish unrestricted reuse.]] before any reuse. A file being in our shared folder does not tell us every channel, format, or duration allowed by the agreement.
Noor | I will keep partner contact details and any private review information out of the public response draft. The response team can use the protected record.
Caleb | That follows [[data minimization::Data minimization keeps unnecessary personal details out of the public communication while preserving relevant information in the appropriate record.]] for the communication. Include what the audience needs to know, not private details simply because they appear in the internal discussion.
Noor | Our queue is paused, the review record is preserved, and the partner's status remains unconfirmed. I will keep that distinction in the team update.
Caleb | I will track the response and the revised asset through the [[approval workflow::The approval workflow controls review and authorization of the revised version before publication resumes.]]. Publication resumes only when the required review and version checks are complete, not merely because the scheduled time has passed.''',
    transfer_title='A complaint is not yet a confirmed cause',
    transfer_setup='A customer publicly reports that an order arrived late and includes their address. The cause has not been checked. The support team has an approved private channel and owns the investigation.',
    transfer='''Marketer: "Acknowledge the reported ___." | delay | The customer reported lateness; acknowledging that report does not establish its cause.
Support: "Move address details to the approved private ___." | channel | The supplied private route avoids repeating the customer's address in a public exchange.
Marketer: "Do not announce an unverified ___." | cause | The briefing says the cause is unchecked, so a public explanation must not invent it.
Support: "Record our ownership and the investigation ___." | status | The team owns the investigation, and its current status should be reported without implying completion.'''))
