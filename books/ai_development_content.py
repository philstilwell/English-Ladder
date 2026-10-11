"""Original, field-specific AI development communication scenarios."""
from books.authoring import unit

BOOK = dict(
    slug='ai-development', title='AI Development English',
    cover_label='Engineering teams / research to production',
    cover_title='AI Development',
    tagline='Precise language for models, evidence, and delivery.',
    audience='For AI engineers, researchers, technical leads, and product colleagues.',
    map_intro='Explain the system, question the evidence, and agree on a defensible next step.',
    notes_title='Name the claim. Name the evidence.',
    notes_intro='AI development discussions move between research, software, product, and risk. Shared words do not always carry shared meanings. Effective English makes the component, comparison, and uncertainty explicit.',
    field_notes=[
        ('Separate the system from the model', 'An application can fail in retrieval, prompting, serving, permissions, or presentation even when its model is unchanged.', '"The retrieved passage is correct; the generated answer omits the exception."'),
        ('Keep the denominator visible', 'A percentage needs a population and criterion. An average can conceal weak performance on an important slice.', '"It passed 88 of these 100 cases; that is not an estimate for all customer traffic."'),
        ('Disagree with a testable claim', 'Ablations, baselines, and matched comparisons make technical disagreement useful. A request for evidence is not necessarily a personal challenge.', '"What changes if we hold the retrieval set constant and swap only the reranker?"'),
        ('Do not turn a hypothesis into a finding', 'Use may, appears, and is consistent with when evidence is limited. State what would confirm or weaken the explanation.', '"The timing suggests a queueing issue, but we have not isolated the cause."')],
    scope_note='Fictional communication practice, not deployment, security, or compliance instructions. Use authorized review, current documentation, and approved procedures for real systems. Never place real secrets or personal data in practice exercises.',
    sources=[
        dict(title='NIST. Artificial Intelligence Risk Management Framework: Generative AI Profile (2024).', url='https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf', note='Background for the vocabulary of evaluation, information integrity, privacy, and documented risk decisions. The fictional release criteria are not NIST requirements.', checked='10 October 2026'),
        dict(title='Lewis et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020).', url='https://arxiv.org/abs/2005.11401', note='Primary research background for retrieval-augmented generation. The book does not reproduce the paper or present its results as product guarantees.', checked='10 October 2026'),
        dict(title='PyTorch. Saving and Loading Models.', url='https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html', note='Background for distinguishing model weights from the additional state needed to resume training. Exact recovery requirements depend on the training system.', checked='10 October 2026'),
        dict(title='OWASP. LLM06:2025 Excessive Agency.', url='https://genai.owasp.org/llmrisk/llm062025-excessive-agency/', note='Background for bounded tool permissions, independent authorization, and human review of consequential agent actions.', checked='10 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Speaking the AI Development Stack', scene='The answer is wrong, but which layer failed?',
    skill='Distinguish components and ask a diagnostic question without assigning blame.',
    brief='A document assistant displays the wrong refund deadline. Retrieval returned the current policy, which states 30 days, but the generated answer says 60. The interface displays the generated text unchanged. Priya owns the model integration; Alex manages the product. A demonstration is scheduled for Friday. No cause has been confirmed, and Alex cannot approve a production release alone.',
    cast='Priya | AI integration engineer\nAlex | Product manager',
    culture=('Locate the failure before naming an owner', '"The AI is broken" does not identify a component or establish responsibility. Separate the observed output from a theory about its cause. A colleague asking for the exact trace is asking for evidence, not necessarily dismissing the report.'),
    a='''Which observation is confirmed? | The generated answer says 60 days. | Retrieval found an obsolete policy. | The interface altered the number. | Production release is approved. | The briefing identifies the generated text as wrong and says the interface displays it unchanged.
Who owns the model integration? | Priya | Alex alone | The customer | The policy author | Priya's stated role covers integration; product ownership does not identify the technical owner.
What remains unknown? | Why the model produced the wrong deadline | The correct policy deadline | Whether a demonstration is scheduled | Whether the interface displays the text | The symptom and correct deadline are known, but the cause has not been established.''',
    vocabulary='''application stack | The components that together deliver an application. | map the application stack
retrieval | Finding source material relevant to a request. | inspect retrieval results
language model | A model that processes and generates language sequences. | query a language model
user interface | The part of a system a user sees and operates. | inspect the user interface
orchestration | Coordination of model, retrieval, and tool steps. | trace the orchestration flow
inference | Running a trained model to produce an output. | run inference
endpoint | An address through which a service accepts requests. | call an endpoint
payload | The data carried in a request or response. | inspect the request payload
trace | A linked record of events in a request's path. | examine a request trace
dependency | A component or condition another part relies on. | identify a service dependency
upstream | Earlier in the relevant processing path. | inspect the upstream response
downstream | Later in the relevant processing path. | assess downstream impact
symptom | An observed sign of a problem, not its cause. | describe the symptom
root cause | The underlying cause established by investigation. | verify the root cause
reproduction | Recreating a reported result under stated conditions. | obtain a reliable reproduction
request ID | An identifier used to locate a particular request. | attach the request ID
schema | A defined structure for data and its fields. | validate a response schema
tool call | A model-requested invocation of an available tool. | inspect a tool call
API | Application programming interface; a defined software interaction boundary. | document an API contract
contract | Agreed expectations between software components. | preserve the service contract
integration | Connecting components into a working system. | test the integration
observability | The ability to infer system behavior from available signals. | improve observability
triage | Initial assessment that determines priority and ownership. | triage the defect
handoff | Transfer of work and its relevant context. | prepare a clear handoff''',
    precision='A trace records events; a diagnosis explains them. A wrong answer identifies a symptom, not automatically a model defect. Keep retrieval output, model output, and displayed text separate.',
    precision_extra='An API contract defines expected interaction, not necessarily a legal contract. "Upstream" and "downstream" describe position relative to a chosen component; name that component.',
    phrases='''Locate the layer | Which component first shows the wrong value?
State the observation | The retrieved passage says 30 days; the generated answer says 60.
Limit the conclusion | That locates the mismatch, but it does not establish the cause.
Request a trace | Can you attach the request ID and the redacted trace?
Separate responsibilities | Product approval and technical diagnosis are different decisions.
Ask for reproduction | Can we reproduce it with the same payload and configuration?
Clarify a term | By "the AI," do you mean the model or the whole application?
Agree on a handoff | I will send the evidence and name the unresolved question.
Check the interface | Does the interface display the response without changing it?
Avoid blame | Let us inspect the boundary before assigning ownership.
Narrow the test | Change one component while keeping the others fixed.
Name the uncertainty | We have an observation, not a verified root cause.
Confirm a dependency | Does this test depend on the policy index being current?
Preserve the record | Please retain the configuration used for that request.
Set the update | I can commit to an update, not to a fix by that time.
Close precisely | The demonstration remains scheduled; release approval is separate.''',
    notes='''Which, not why | "Which component first shows the mismatch?" asks for location before assuming a cause.
Present evidence | "The trace shows" introduces an observation; "this suggests" introduces an interpretation.
Embedded questions | Say "Can you confirm whether the interface changes it?", not "whether does the interface change it?"
Contrast clauses | Use "retrieval returned the right passage, but generation changed the deadline" to isolate the contrast.
Limited commitments | "I will investigate by Friday" is unclear; "I will report our findings by Friday" names a deliverable.
Ownership language | "I own the investigation" accepts responsibility for the work, not blame for the incident.''',
    d='''Which question locates the first mismatch? | At which boundary does 30 become 60? | Can we assign the fault to the model because retrieval found the right passage? | Should the interface team own the cause because it displays the answer? | Can a single corrected reply establish that the issue is fixed? | Comparing values across boundaries locates the observed mismatch; the alternatives jump to cause, responsibility, or resolution without the necessary evidence.
Complete: "Could you confirm whether ___?" | the payload includes the policy | does the payload include the policy | includes the payload the policy | the payload does includes the policy | After whether, an embedded question takes statement order: subject followed by verb.
Which statement preserves uncertainty? | The trace suggests a generation issue; the cause is unconfirmed. | The trace proves the engineer caused the defect. | A correct passage guarantees a correct answer. | The demonstration authorizes production use. | Suggests reports limited evidence, while the second clause explicitly leaves causation unresolved.
Which expression means transferring work with context? | prepare a clear handoff | increase the inference | approve a symptom | retrieve the ownership | A handoff transfers work and relevant information; the other combinations do not express that action.''',
    dialogue='''Alex | The refund answer is wrong again. The policy says 30 days, but our assistant tells the customer 60. Which team should investigate first?
Priya | Do you have the [[request ID::A request ID identifies the particular request whose recorded behavior can be inspected.]]? I want to see the retrieved passage and the answer side by side.
Alex | Yes, the record is D-184. I checked the passage in that record: it says 30 days. The response underneath it says 60.
Priya | That gives us a specific [[mismatch::A mismatch is a disagreement between values that should agree; here the two deadlines differ.]]. Retrieval found the current passage. I still need to inspect exactly what reached the model.
Alex | So the model got it wrong? I need to tell the team who is picking this up.
Priya | Tell them the answer is wrong, but leave the cause open. The [[payload::The payload is the data sent in the request; it may differ from material displayed elsewhere.]] could contain another instruction or an older example.
Alex | Wait, could the interface have changed the number? We had a display issue last time.
Priya | The recorded response already says 60, and the interface displays it unchanged. That puts the first observed difference [[upstream::Upstream places the observed difference before the interface in this processing path.]] of presentation.
Alex | What would you need to distinguish a bad instruction from an unstable model answer? We should keep the Friday demonstration team informed.
Priya | The configuration and a redacted [[trace::A trace links events along the request path and helps compare what each component received or returned.]]. Then I can repeat the request and compare the inputs without changing several variables.
Alex | Is repeating one request enough to say we have fixed the problem? The same customer asked two slightly different versions of the question.
Priya | No. First we need a reliable [[reproduction::A reproduction recreates the observed problem; it is not proof that a later change solves every variation.]]. Then we test the change on both variants and related policy cases.
Alex | Please make the ownership clear in the ticket. I can coordinate the demonstration, but I cannot approve production use on my own.
Priya | I will own technical [[triage::Triage is the initial assessment of the defect and its appropriate handling, not final release approval.]]. I will also name the policy and interface owners if the evidence requires their input.
Alex | Can I tell the sales team we will have a fix by Thursday afternoon? They need to decide whether to keep the live demonstration.
Priya | I can promise findings by then, not a fix. Until we verify a [[root cause::A root cause is an established underlying explanation, not merely the first plausible theory.]], that deadline would be an unsupported commitment.
Alex | All right. I will describe the customer-visible problem and keep the demonstration decision separate. What should your update include for that decision?
Priya | The reproduction result, affected cases, remaining uncertainty, and a proposed next step. I will preserve the [[configuration::The configuration records the settings used, allowing results from different runs to be compared meaningfully.]] so the comparison is meaningful.
Alex | That works. Please send it by three on Thursday, even if the investigation is incomplete. I will confirm who can decide about Friday.
Priya | Agreed. The [[handoff::A handoff passes findings and responsibility to the next decision-maker without implying the investigation is complete.]] will say what we know, what we do not know, and which decision still needs an owner.''',
    rehearsal=["Check the dialogue, then read the 30-day source and 60-day generated answer as separate observations. Locate the mismatch before assigning its cause.","Switch roles. Ask for D-184, the redacted trace and the request configuration; retain the Thursday findings update without promising a fix.","Complete the citation-link exchange. State that the generated response contains the citation while the interface omits it, then hand over the exact request."],
    transfer_title='A missing citation in a different assistant',
    transfer_setup='A support assistant generates a correct answer with a citation ID. The interface omits the citation link. The display team needs the exact recorded request, not an assumption that retrieval failed.',
    transfer='''Engineer: "The model response contains the citation; the ___ does not display it." | user interface | The discrepancy appears in presentation because the generated response already contains the citation.
Lead: "Attach the ___ so the display team can locate that exchange." | request ID | The identifier locates the particular exchange rather than merely describing the application.
Engineer: "That is the observed ___; we have not proved why it occurred." | symptom | An omitted link is an observed sign; its underlying cause still needs investigation.
Lead: "Then send a clear ___ to the display owner." | handoff | The next team needs the evidence and unresolved question to take over the investigation.'''))

BOOK['units'].append(unit(
    title='LLMs, Transformers, Tokens, and Context', scene='A larger answer will not make the input fit',
    skill='Correct a technical misconception tactfully and negotiate a bounded alternative.',
    brief='A document-summary request reserves 4,000 output tokens. Its instructions and documents contain 29,000 input tokens. The configured total context limit is 32,000 tokens, and the request is rejected before generation. Lina proposes increasing the output allowance. Omar owns the request configuration. The team must retain the exception clauses; no larger-context model has been evaluated for this task.',
    cast='Lina | Application engineer\nOmar | Model platform engineer',
    culture=('Correct the model of the problem', 'Restate the proposal before rejecting it. Explain which limit applies and show the arithmetic. "That would increase the reservation" is more useful than "You do not understand tokens." A correction can be direct without judging the colleague.'),
    a='''What is the total requested reservation? | 33,000 tokens | 29,000 tokens | 32,000 tokens | 25,000 tokens | The input contains 29,000 tokens and the output reservation adds 4,000, giving 33,000.
Why was the request rejected? | It exceeds the configured total context limit. | The generated answer was inaccurate. | The exception clauses were false. | A larger model had already failed evaluation. | Rejection happened before generation because the combined reservation exceeds 32,000 tokens.
What must the team preserve? | The exception clauses | Every duplicate header | A 4,000-token answer in every case | The untested larger model | The briefing requires the exception clauses to remain available; it does not require duplicate material.''',
    vocabulary='''LLM | Large language model; a model that processes and generates language. | evaluate an LLM
transformer | A neural architecture built around attention mechanisms. | use a transformer architecture
token | A unit processed by a model, not necessarily a whole word. | count input tokens
tokenizer | The component that converts text into tokens. | use the model's tokenizer
context window | The amount of context a model can handle in a request. | stay within the context window
input tokens | Tokens supplied to the model before generation. | measure input tokens
output tokens | Tokens generated by the model. | reserve output tokens
token budget | An allocated number of tokens for a task or component. | allocate a token budget
system instruction | Higher-priority guidance supplied by an application's configuration. | inspect the system instruction
prompt | Instructions and other context supplied for a model response. | revise the prompt
attention | A mechanism that weights relationships between representations. | compute attention weights
parameter | A learned numerical value within a model. | update model parameters
weight | A learned numerical coefficient in a model. | load model weights
checkpoint | Saved model state from a particular stage. | select a checkpoint
truncation | Removal of content to fit a size limit. | detect silent truncation
compression | Reduction of information size, potentially losing detail. | assess compression losses
reserved capacity | Capacity set aside rather than already consumed. | reduce reserved capacity
delimiter | A marker separating sections of supplied text. | preserve clear delimiters
instruction hierarchy | Priority relationships among different instruction sources. | respect the instruction hierarchy
long-context | Able to handle relatively large input context. | evaluate long-context performance
position | A token's place within the input sequence. | vary evidence position
exception clause | Wording that limits or changes a general rule. | retain the exception clause
deduplication | Removal of repeated copies of content. | apply exact deduplication
headroom | Unused capacity left below a limit. | leave sufficient headroom''',
    precision='A token is not a word. Input size, reserved output, and total context are different quantities. The numerical limits in this case are fictional configuration facts, not specifications for a named model.',
    precision_extra='Deduplication removes repeated material; summarization changes its representation. Neither guarantees that every important exception remains visible. A larger context window does not by itself establish task accuracy.',
    phrases='''Restate a proposal | You are proposing a larger output allowance, correct?
Locate the limit | The request fails before generation because the combined reservation is too large.
Show the arithmetic | Twenty-nine thousand plus four thousand is thirty-three thousand.
Correct tactfully | I see the aim, but that change would increase the reservation.
Distinguish quantities | The allowance is a maximum, not the length already generated.
Preserve a requirement | We must retain the exception clauses in the source context.
Offer an alternative | Could we remove exact duplicates before shortening substantive text?
State a condition | A smaller output allowance is acceptable only if the summary still meets the task.
Check counting | Are those counts from the tokenizer used by this model?
Avoid a guarantee | Fitting within the limit does not prove the answer is complete.
Check a transformation | Which information would compression remove?
Reject silent loss | Please report truncation instead of silently dropping the end.
Bound a comparison | Let us compare the same documents under both configurations.
Keep a fallback | If the exceptions cannot fit, route the request for a different workflow.
Separate evaluation | The larger-context model needs its own quality check.
Read back the decision | We will remove duplicates, recount, and test coverage before changing models.''',
    notes='''Arithmetic in speech | Say "thirty-three thousand in total" after stating the two parts; listeners can check the sum.
Would versus will | "That would increase the reservation" describes the proposed change without claiming it has happened.
Only if | "Acceptable only if coverage is preserved" makes coverage a necessary condition.
Not necessarily | "A larger window is not necessarily more accurate" rejects a guarantee without claiming it is always worse.
Scope of all | "All exceptions in these documents" is bounded; "all exceptions" can imply knowledge beyond the supplied material.
Clarifying by | "By output allowance, do you mean the maximum reserved tokens?" checks a term before challenging it.''',
    d='''Which response explains the rejection? | The combined reservation is 1,000 tokens over the limit. | The output has already used 33,000 tokens. | The model generated an incorrect exception. | The tokenizer guarantees the summary is complete. | The request totals 33,000 against a 32,000 limit; generation has not begun.
Which proposal preserves the stated requirement most directly? | Remove exact duplicate headers and recount. | Delete exception clauses first. | Increase the output reservation without recounting. | Treat words and tokens as equal. | Removing exact duplicates can reduce size without intentionally deleting the required exceptions; the result still needs checking.
Complete: "We can reduce the allowance, provided that ___." | the summary still covers the required points | does the summary cover the required points | the summary covering the required points | cover the summary the required points | Provided that introduces a condition with normal subject-verb order.
Which claim is appropriately limited? | The request fits; we still need to test summary coverage. | A fitting request must produce a complete answer. | More context eliminates all reasoning errors. | Removing duplicates proves the policy is current. | Capacity compliance and content quality are separate checks; fitting does not prove coverage.''',
    dialogue='''Lina | The summary request is rejected again. I was going to increase the output allowance so the model has enough room to explain the policy.
Omar | Can we check the [[token budget::A token budget allocates capacity to the request; checking it reveals whether the proposed change fits.]] first? Your input is 29,000 tokens, and you have reserved another 4,000 for output.
Lina | That sounds close to the 32,000 limit. Are you saying the unused output allowance counts even though the model has not answered yet?
Omar | For this configuration, yes. The combined [[reservation::The reservation combines supplied input and capacity set aside for output under this case's stated rule.]] is 33,000. Increasing the output allowance would move us further over the limit.
Lina | All right, I had treated the limit as input only. Could we simply trim the final document until the request is accepted?
Omar | Not without checking what it contains. The final pages include an [[exception clause::An exception clause changes the general rule, so deleting it can change the meaning of the policy.]] that changes the refund rule for renewals.
Lina | We also repeat the same header on every page. Removing those exact copies would preserve the policy wording and reduce the input somewhat.
Omar | That is a reasonable first test. Use exact [[deduplication::Deduplication removes repeated copies; it is distinct from summarizing or deleting unique policy content.]], then count again with the tokenizer used by this model rather than a word count.
Lina | Suppose that saves only 600 tokens. We would still be 400 over the limit. Could we reserve 3,000 output tokens instead?
Omar | We could test it. That would leave 600 tokens of [[headroom::Headroom is the remaining capacity below the limit: 32,000 minus 28,400 minus 3,000 equals 600.]], but we need to verify that the shorter answer still covers the required points.
Lina | I'll check renewals and exceptions against the same checklist. Getting the request accepted won't help if the summary drops the important part.
Omar | Exactly. Also record whether the client performs [[truncation::Truncation removes content to satisfy a length limit; recording it exposes possible information loss.]]. A request can fit after important text has been removed without anyone noticing.
Lina | Someone suggested using a larger-context model instead. Would that let us keep the original request and stop spending time on these smaller adjustments?
Omar | It is another option, not an automatic solution. Its [[long-context::Long-context describes capacity for larger inputs, not a guarantee that relevant details will be used accurately.]] performance on our policy task has not been evaluated, and its cost may differ.
Lina | Then I will keep that as a separate comparison. Should the test vary where the exception appears, or is the current document order sufficient?
Omar | Vary its [[position::Position means where the evidence appears in the input; changing it can reveal sensitivity to document order.]] while keeping the wording unchanged. We want to see whether the model preserves the exception across the tested arrangements.
Lina | I'll remove the repeated headers first. If we're still over, I'll test the smaller output allowance and bring both the counts and the coverage results.
Omar | Correct. Keep the [[delimiters::Delimiters mark document or section boundaries; retaining them helps preserve the structure of the supplied context.]] between documents so the revised input does not merge separate policies into one undifferentiated block.
Lina | I will report the before-and-after counts with the coverage results. If the necessary clauses still cannot fit, I will stop rather than silently remove them.
Omar | Good. Describe the limit as a [[capacity constraint::A capacity constraint limits what fits; it is not a finding about the truth or quality of the policy answer.]], not a model-quality finding. We can then choose the next workflow using the actual test results.''',
    rehearsal=["After checking the dialogue, read the reservation calculation aloud: 29,000 input plus 4,000 reserved output equals 33,000 against a 32,000 limit.","Switch roles. Read the proposal to remove exact duplicates while retaining the exception clauses; do not treat a fitting request as proof of coverage.","Complete the appendix exchange. Check 18,000 plus 3,000 equals 21,000, then preserve unique obligations while comparing the total with the fictional 20,000 limit."],
    transfer_title='A contract summary with repeated appendices',
    transfer_setup='A fictional request has a 20,000-token total limit, 18,000 input tokens, and a 3,000-token output reservation. Repeated appendix covers may be removed; unique obligations must remain.',
    transfer='''Engineer: "The combined ___ is 21,000 tokens, so the request is too large." | reservation | Adding 18,000 input and 3,000 reserved output gives 21,000, above the case limit.
Reviewer: "Start with exact ___ of the repeated covers." | deduplication | Removing exact repeated covers targets redundancy without intentionally removing unique obligations.
Engineer: "I will preserve every unique ___ in the supplied contract." | obligation | The constraint explicitly protects unique obligations; removing them would change the source information.
Reviewer: "After recounting, test ___ rather than treating acceptance as success." | coverage | The system accepting the request does not establish that the summary includes the required obligations.'''))

BOOK['units'].append(unit(
    title='Data, Datasets, Labels, and Leakage', scene='A 94 percent score with an overlap problem',
    skill='Disclose compromised evidence and resist pressure to overstate readiness.',
    brief='A classifier scores 94 percent on 500 evaluation examples. Jules finds that 40 evaluation records have exact copies in training. The remaining records have not been re-scored separately. Morgan presents release evidence in one hour. Training and evaluation labels use the same written rubric, but six disputed labels remain unresolved. The release owner can postpone the decision.',
    cast='Jules | Data scientist\nMorgan | Evaluation lead',
    culture=('Report evidence quality before headline performance', 'Flagging contaminated evaluation data is responsible reporting, not an admission that every model result is worthless. State exactly what is affected, what cannot yet be concluded, and which decision needs a revised evidence base.'),
    a='''What does 94 percent currently describe? | The score on all 500 evaluation examples | The score on 460 nonoverlapping examples | A verified production success rate | The agreement rate on disputed labels | The reported score covers the original 500 examples; the nonoverlapping subset has not been separately scored.
What overlap has been confirmed? | Forty evaluation records have exact training copies. | Every evaluation record is in training. | Forty training labels are missing. | Six hundred records are duplicates. | The confirmed issue is exact overlap for 40 evaluation records, not contamination of every record.
What can the release owner do? | Postpone the decision | Certify the unmeasured subset score | Resolve labels without review | Turn the score into a production guarantee | The briefing explicitly allows postponement; none of the other actions creates the missing evidence.''',
    vocabulary='''dataset | A collection of records assembled for a purpose. | curate a dataset
training set | Data used to fit model parameters. | audit the training set
validation set | Data used to guide model selection or tuning. | monitor validation performance
test set | Data reserved for evaluating a finalized choice. | preserve the test set
holdout | Data kept separate from a fitting or selection process. | maintain a clean holdout
data leakage | Information crossing a boundary in a way that invalidates evaluation. | investigate data leakage
contamination | Unwanted overlap or exposure that weakens an evaluation. | quantify evaluation contamination
exact duplicate | A record identical under a stated comparison rule. | remove exact duplicates
near duplicate | A closely similar record that may share substantive content. | review near duplicates
split | A partition of data into separate subsets. | define a reproducible split
label | A target category or annotation attached to a record. | verify a disputed label
annotation | Human or machine-added information about an example. | review annotation quality
rubric | Explicit criteria for assigning or evaluating labels. | apply a shared rubric
adjudication | Resolution of a disputed judgment by a defined process. | request label adjudication
inter-rater agreement | The degree to which different raters agree. | measure inter-rater agreement
provenance | The recorded origin and history of data. | establish data provenance
sampling frame | The population or list from which records are sampled. | define the sampling frame
representativeness | How well a sample reflects the target population. | assess sample representativeness
class imbalance | Unequal frequencies among target categories. | check class imbalance
stratification | Sampling or partitioning within defined groups. | use stratified sampling
distribution shift | A difference between data distributions across settings. | detect distribution shift
deduplicate | Remove repeated records under a defined rule. | deduplicate before splitting
denominator | The total count used as the base of a rate. | state the denominator
re-score | Calculate a score again under specified conditions. | re-score the clean subset''',
    precision='A clean holdout is separate from the process it evaluates, not necessarily representative of production. Removing overlap improves separation but does not resolve label disputes or distribution differences.',
    precision_extra='Exact duplicates and near duplicates require different comparison rules. Inter-rater agreement measures agreement, not automatic correctness. Always identify the sample and denominator behind a percentage.',
    phrases='''Flag compromised evidence | The headline score includes records that overlap with training.
Quantify the issue | We found 40 exact overlaps among 500 evaluation examples.
Protect uncertainty | We have not yet calculated the score on the remaining records.
Reject unsupported subtraction | Removing eight percent of records does not tell us the new accuracy.
Separate two problems | Data overlap and disputed labels need different checks.
Request provenance | Can we trace when these records entered each split?
Name the decision impact | The current score should not be presented as an independent estimate.
Offer a bounded update | I can provide the overlap list before the meeting.
Clarify a duplicate | What comparison rule defines an exact match here?
Preserve the holdout | Do not tune against the replacement test set.
Qualify a clean result | A clean split still needs a representativeness check.
Check the rubric | Which label criterion produced the disagreement?
State the denominator | Please report both the number correct and the number evaluated.
Describe a limitation | This sample underrepresents the rare class.
Keep the record | Retain the original score with its limitation and the corrected result.
Escalate a decision | The release owner needs to decide whether to wait for the revised evidence.''',
    notes='''Includes versus consists of | "The set includes overlapping records" does not mean every record overlaps.
Not yet | "Not yet re-scored" describes incomplete work; it does not imply the corrected result will improve.
Percentage points | A change from 94 percent to 90 percent is four percentage points, not necessarily a four-percent relative decline.
Reported speech | "The slide says the holdout is independent" identifies a claim without endorsing it.
Known and unknown | Pair "we found 40 overlaps" with "we have not checked near duplicates" when both are relevant.
Accountable correction | "We need to correct the slide" directs an action without assigning unsupported personal blame.''',
    d='''Which meeting statement is supported? | The 94 percent score includes 40 training overlaps. | The clean-subset score is exactly 86 percent. | Every label is unreliable. | The model will fail in production. | The overlap is confirmed; no clean-subset score or production outcome has been established.
What does "not yet re-scored" mean? | The revised calculation remains unfinished. | The revised score must be lower. | The release has been canceled permanently. | The labels are now verified. | Not yet states timing and incompleteness, not the direction or final consequence of the result.
Which question targets a label dispute? | Which rubric criterion distinguishes these two labels? | Can we use the model's own prediction as the reference label? | Does removing duplicates prove the disputed labels are correct? | Can the headline score decide which reviewer is right? | The rubric provides criteria for adjudication. Predictions, duplicate removal and an aggregate score do not resolve what the reference category should be.
Which phrase correctly names the base of a rate? | state the denominator | approve the leakage | deploy the annotation | infer the rubric | The denominator is the total count against which the number of successes is expressed.''',
    dialogue='''Morgan | The release meeting starts in an hour. I have the 94 percent result on the slide. Is there anything material we need to add?
Jules | Yes. I found 40 exact training matches inside the 500-example evaluation set. That creates [[contamination::Contamination means the evaluation is affected by unwanted exposure or overlap with training data.]], so the independence claim needs correcting.
Morgan | Forty out of 500 is eight percent. Could I subtract eight points and present 86 percent as a conservative estimate instead?
Jules | No. We need to [[re-score::Re-scoring calculates performance on the specified remaining records; arithmetic on the overlap rate cannot supply that score.]] the remaining examples. We do not know how many of the overlapping records were answered correctly.
Morgan | Then I will remove the independent-evaluation label. Can you tell me whether the overlap came from the import process or the later cleanup?
Jules | Not yet. The [[provenance::Provenance records where data came from and how it changed; it can help identify when overlap entered the sets.]] log should help, but I have not reconstructed the sequence. I can provide the exact record list now.
Morgan | Send me that list. I'll leave the cause out of the slide for now. Is there anything else I need to flag?
Jules | Six examples have disputed labels. They need [[adjudication::Adjudication resolves disputed labels through the agreed review process rather than selecting whichever label improves the score.]] under the written rubric, independently of the overlap check.
Morgan | Could we exclude those six for this meeting? I do not want the discussion to get buried in detail that may not change the decision.
Jules | We can report an explicitly defined subset, but we must state its [[denominator::The denominator identifies how many records are included, so exclusions cannot be hidden behind an unchanged headline rate.]] and exclusions. We cannot call a selectively cleaned subset the original result.
Morgan | Agreed. The release owner can wait for better evidence. What would you recommend we say about the 94 percent figure already circulated yesterday?
Jules | Retain it with a correction: it describes the original set, not a clean [[holdout::A holdout must remain separate from the process being evaluated; the confirmed training overlap compromises that separation.]]. Replace the readiness claim rather than quietly changing the number.
Morgan | Once the duplicate records are removed, can we say the evaluation represents customer traffic? That is the next question I expect from the release owner.
Jules | Not from separation alone. We still need to check [[representativeness::Representativeness concerns whether the sample reflects the intended customer population, a separate question from overlap.]], including the rare category that appears only a few times in this sample.
Morgan | So we have three issues: overlap, disputed labels, and coverage of the target population. Which one can you resolve before today's meeting starts?
Jules | I can verify the [[exact duplicates::Exact duplicates are identical under the chosen comparison rule; verifying them does not complete a near-duplicate review.]] and document the matching rule. I cannot responsibly promise all label reviews within the hour.
Morgan | All right, the duplicate check comes first. For the replacement set, can we keep it untouched while the team tunes the model?
Jules | It should. If we repeatedly choose model settings from that set, it becomes part of [[model selection::Model selection uses evaluation results to choose a model or configuration, so that set no longer provides an untouched final test.]], and we need a separate final test.
Morgan | I will recommend postponing the readiness decision. The slide will list confirmed overlap, pending label review, and the missing clean-subset score separately.
Jules | I will send the records and a short [[limitation statement::A limitation statement specifies what the evidence cannot support, preventing the headline figure from becoming an unjustified release claim.]]. That gives the owner usable evidence without pretending the corrected outcome is already known.''',
    rehearsal=["Check the answers. Read 40 overlaps out of 500 as eight percent of records, not eight percentage points to subtract from the 94 percent score.","Switch roles. Separate the overlap list, unmeasured clean-subset score and six disputed labels in the handoff.","Complete the 80-message exchange. Retain 70 unscored nonoverlapping messages and three label disputes; do not invent a revised accuracy."],
    transfer_title='A sentiment test with repeated customer messages',
    transfer_setup='An 80-message test contains ten copies of messages used for training. The team has not scored the 70 remaining messages separately. Two reviewers disagree on three labels.',
    transfer='''Analyst: "The current test has training ___, so its independence is compromised." | overlap | Ten test messages also appeared in training, which compromises the claimed separation.
Lead: "Report the clean-subset score only after you ___ those 70 messages." | re-score | The performance on the remaining 70 cannot be inferred simply by subtracting the overlap count.
Analyst: "The three disputed labels also need ___." | adjudication | Label disagreements require a defined review decision separate from duplicate removal.
Lead: "And include the ___ with every reported percentage." | denominator | A percentage must identify its underlying number of examples, especially after exclusions.'''))

BOOK['units'].append(unit(
    title='Retrieval, Embeddings, Vector Search, and RAG', scene='More relevant passages, a slower response',
    skill='Negotiate a trade-off using matched comparisons and explicitly limited claims.',
    brief='A document assistant with reranking retrieves a relevant passage for 86 of 100 fixed test queries, compared with 78 without reranking. The reranker adds 300 milliseconds to the measured retrieval path. The generator and query set are unchanged. No user study or end-to-end answer-quality review has been completed. Sam recommends a pilot; Elena owns the evaluation plan.',
    cast='Sam | Retrieval engineer\nElena | Evaluation lead',
    culture=('Define better before agreeing', '"Better retrieval" may mean finding relevant passages, ranking them earlier, or improving final answers. Ask which measure changed. A measured technical improvement can justify another test without proving a better customer experience.'),
    a='''What improved in the fixed test? | Queries with a relevant retrieved passage rose from 78 to 86. | Every final answer became correct. | Response time fell by 300 milliseconds. | Users preferred the new experience. | The measured gain concerns retrieval relevance on 100 fixed queries; answer quality and user preference remain unchecked.
Which component stayed unchanged? | The generator | The reranker | The retrieval path timing | The number of relevant hits | The briefing holds the generator and query set constant, helping isolate the retrieval change.
Which claim needs further evidence? | The new path improves end-to-end answer quality. | The reranker adds 300 milliseconds. | Both variants use the same query set. | The test contains 100 queries. | No end-to-end answer review has been completed, so better passage retrieval does not establish that claim.''',
    vocabulary='''RAG | Retrieval-augmented generation; generating with retrieved context. | evaluate a RAG pipeline
embedding | A numerical representation used to compare or process items. | compute an embedding
vector | An ordered collection of numerical values. | compare document vectors
vector store | A store or index supporting retrieval of vector representations. | query a vector store
similarity search | Finding items close under a chosen similarity measure. | run similarity search
semantic search | Retrieval based on meaning-related representations. | assess semantic search
keyword search | Retrieval based on words or lexical matches. | combine keyword search with vectors
hybrid retrieval | Retrieval combining different search approaches. | test hybrid retrieval
chunk | A retrievable segment of a larger document. | retrieve a relevant chunk
chunk boundary | The point where one segment ends and another starts. | preserve context at chunk boundaries
overlap window | Content shared between adjacent chunks. | adjust the overlap window
reranker | A component that reorders candidates for relevance. | evaluate the reranker
candidate set | Items available for a later selection or ranking step. | inspect the candidate set
top-k | The first k results returned by a ranking. | compare top-k results
relevance | How well material addresses a specified query. | judge passage relevance
recall | The proportion of relevant items retrieved under a defined evaluation. | measure retrieval recall
precision | The proportion of retrieved items judged relevant. | improve retrieval precision
grounding | Connecting generated claims to supporting information. | check answer grounding
citation | A reference identifying a supporting source. | verify a citation
source attribution | Identification of where information came from. | preserve source attribution
index freshness | How current the indexed information is. | monitor index freshness
filter | A rule limiting eligible retrieval results. | apply a metadata filter
ablation | A comparison that removes or changes a component. | run a reranker ablation
end-to-end | Covering the complete path from request to outcome. | measure end-to-end latency''',
    precision='Retrieval relevance, answer correctness, and user preference are distinct outcomes. A citation can identify a source without proving that the source supports the exact claim. Inspect the cited passage.',
    precision_extra='Recall and precision require defined relevance judgments and denominators. The case reports query-level passage coverage, not a complete precision-recall analysis. Top-k says how many results are returned, not how many are correct.',
    phrases='''Name the measure | The improvement is passage coverage on this fixed query set.
Separate outcomes | We have not yet measured final-answer accuracy.
Quantify a trade-off | The gain comes with 300 milliseconds of added retrieval time.
Request a matched comparison | Can we hold the generator and queries constant?
Ask for an ablation | What happens when we remove only the reranker?
Limit a recommendation | These results support a bounded pilot, not a general rollout claim.
Check the source | Does the cited passage support this specific sentence?
Define the next test | Review final answers and timing on the same cases.
Inspect a miss | Was the relevant passage absent or merely ranked too low?
Check eligibility | Did a filter exclude the document before similarity search?
Preserve context | The exception and the main rule should not be separated without context.
Challenge an average | Which query types account for most of the added time?
Distinguish freshness | A relevant passage may still come from an outdated index.
Avoid causal overreach | The matched test isolates this change, not every production condition.
Compare alternatives | Let us compare reranking all queries with a defined routing policy.
Record a limitation | User preference remains unmeasured in this experiment.''',
    notes='''Compared with | State both variants: "86 queries compared with 78 without reranking." The comparison is then recoverable.
Percentage points | On this 100-query set, coverage rises by eight percentage points, not merely "eight percent better."
Not yet measured | This phrase marks missing evidence without predicting what the eventual test will show.
With versus because | "With reranking" describes a condition; "because of reranking" makes a causal claim that needs controlled evidence.
Conditional recommendations | "I recommend a pilot provided we review answer quality" attaches the condition to the action.
Question precision | "Which query types slow down?" is more diagnostic than "Is performance okay?"''',
    d='''Which comparison correctly states the observed gain? | Coverage increased by eight percentage points on the fixed set. | Users became eight percent more satisfied. | Final answers are now 86 percent accurate. | Every query returns eight more passages. | The measure rises from 78 of 100 to 86 of 100, an eight-percentage-point coverage change.
What is a reranker ablation here? | Compare the path with and without the reranker while holding other factors fixed. | Replace every component and change the queries. | Ask users to invent new relevance criteria. | Remove all supporting documents permanently. | Changing the reranker alone helps attribute differences in the matched comparison.
Which sentence preserves the limitation? | Retrieval improved on this set; final-answer quality remains unmeasured. | Better retrieval guarantees better answers. | A citation proves the answer is true. | No user study means retrieval did not improve. | The sentence separates the measured gain from an unmeasured downstream outcome.
Which question checks grounding? | Does this passage support the answer's refund exception? | Does the answer contain a citation marker in the required format? | Is the cited document present in the current index? | Does the retrieved passage share many words with the question? | Grounding concerns support for the specific claim. A marker, indexed document or lexical overlap can exist without supporting the stated exception.''',
    dialogue='''Sam | The reranker looks promising. We found a relevant passage for 86 of the same 100 queries, compared with 78 on the previous path.
Elena | Good. Before we call it better overall, what changed in the [[candidate set::The candidate set contains the retrieved items available to the reranker; changes there could affect the comparison.]]? Did you also modify the initial search or document filters?
Sam | No. The initial candidates, generator, and queries are unchanged. The reranker changes their order, and the retrieval path takes another 300 milliseconds.
Elena | Then we have a useful [[ablation::An ablation compares a component's presence or configuration while controlling other factors, helping isolate its effect.]]. It shows a retrieval gain with added time, but it does not yet show better generated answers.
Sam | I agree the answer review is unfinished. My recommendation is a small pilot, not a rollout. Which evidence would you need before approving that pilot?
Elena | First, an [[end-to-end::End-to-end review follows the whole request-to-answer path, rather than stopping at the retrieval component.]] review of the same cases. We need the final answers, their supporting passages, and the complete response times.
Sam | We can collect those. Some of the original misses had the right document in the candidates but ranked below the five passages sent to generation.
Elena | That distinction matters. A [[reranker::A reranker can reorder existing candidates; it cannot recover a document absent from the candidate set by reordering alone.]] can promote those passages, but it cannot rescue a relevant document that never entered the candidate set.
Sam | Two misses also involve a policy exception split across adjacent chunks. I do not want to alter chunking in the middle of this comparison.
Elena | Keep that separate. Log the [[chunk boundary::A chunk boundary can separate a main rule from its exception, making a retrieved segment incomplete without neighboring context.]] issue for another experiment so we can still interpret this result.
Sam | Should the answer reviewers count every displayed citation as a success? The new path tends to produce more citations, which looks reassuring in the interface.
Elena | No. They should check [[grounding::Grounding asks whether the generated claim is supported by the supplied evidence, not merely whether a citation marker appears.]] for each substantive claim. A citation can point to a real document that does not support that sentence.
Sam | Understood. I will include the exact cited passage and the answer claim together. We also need to distinguish an old policy from an irrelevant one.
Elena | Yes. Check [[index freshness::Index freshness concerns whether indexed material reflects current source information; relevance alone does not establish currency.]] separately. A highly relevant passage from a superseded policy can still produce a misleading answer.
Sam | The product lead will ask whether customers will accept the extra delay. Could we infer that from the eight-point increase in passage coverage?
Elena | No. That is a [[trade-off::A trade-off involves competing outcomes, here relevance and delay; user acceptance requires evidence beyond the retrieval score.]] we have measured technically, but customer preference remains unknown until we test it appropriately.
Sam | Then I will present the retrieval result as eight percentage points on this set. I will not call it an eight-percent increase in customer satisfaction.
Elena | Exactly. Also break down timing by [[query type::Query type identifies a meaningful subgroup; subgroup timing can reveal costs concealed by an overall average.]], because the same average can hide very different costs for simple and complex questions.
Sam | I'll bring the answer review and timing breakdown before we discuss the pilot. The chunking experiment can wait; I don't want to lose this comparison.
Elena | Good. Put the improvement on the slide, but keep the pilot recommendation [[conditional::Conditional support depends on the stated review being completed; it is not unconditional permission to deploy.]]. I want to see the actual answers before I approve it.''',
    rehearsal=['Check the dialogue. Read 78 versus 86 of 100: eight percentage points gained, with 300 milliseconds added.', 'Switch roles. Request a matched final-answer review; do not substitute retrieval coverage for answer accuracy.', 'Complete the exception exchange. Distinguish a real source from support for the specific claim.'],
    transfer_title='An answer cites the right document but the wrong section',
    transfer_setup='A benefits assistant cites the current policy but uses the standard rule instead of a stated exception. Retrieval includes both sections. A reviewer must report claim support, not count citation markers.',
    transfer='''Reviewer: "The citation identifies a real ___, but not support for this claim." | source | Identifying an authentic source does not establish that the cited material supports the particular answer.
Engineer: "Both sections were retrieved, so we should inspect answer ___." | grounding | With both sections available, the question is whether the generated claim reflects the supporting evidence.
Reviewer: "The exception is missing from the answer, although it is present in the ___." | context | The provided retrieval context contains the exception; the failure is not evidence that it was absent.
Engineer: "We will report that distinction in the ___ review." | end-to-end | The full review follows the evidence through retrieval into the final answer, preserving where the mismatch appears.'''))

BOOK['units'].append(unit(
    title='Fine-Tuning, Alignment, and Adaptation', scene='One proposal, two different failure modes',
    skill='Separate proposed remedies by mechanism and agree on a controlled experiment.',
    brief='A support summarizer sometimes returns paragraphs instead of the required fields and sometimes cites an obsolete refund policy. The obsolete wording is present in its retrieval index. Its prompt contains only one formatting example. Tessa proposes fine-tuning to solve both problems. Dev owns the experiment plan. The team has 200 permission-cleared example summaries but has not audited their label consistency.',
    cast='Tessa | Applied scientist\nDev | Technical lead',
    culture=('Challenge the scope of a remedy', 'A method can be useful without solving every problem in the discussion. Separate knowledge freshness from output behavior. Ask what mechanism would change each failure and what simpler comparison could test the claim.'),
    a='''Which fact directly concerns outdated information? | The retrieval index contains obsolete policy wording. | The prompt contains one formatting example. | The team owns an experiment plan. | The output sometimes uses paragraphs. | The index supplies obsolete source wording, which is a distinct issue from output formatting.
What is known about the 200 examples? | They are permission-cleared but consistency is unaudited. | Every label has been independently verified. | They contain the latest policy by definition. | They guarantee successful fine-tuning. | Permission to use data does not establish its consistency, currency, or training value.
What distinction should the experiment preserve? | Source freshness versus output-format behavior | Data-use permission as proof of label consistency | Required fields as proof that policy statements are current | More training examples as proof that retrieval is refreshed | The two observed failures concern source currency and output behavior. The alternatives conflate separate checks or assume an untested mechanism.''',
    vocabulary='''fine-tuning | Updating model parameters using additional training data. | evaluate a fine-tuning run
pretraining | Broad initial training before task-specific adaptation. | distinguish pretraining from adaptation
supervised fine-tuning | Training on supplied input-output examples. | prepare supervised fine-tuning data
SFT | Abbreviation for supervised fine-tuning. | compare SFT with prompting
preference data | Examples recording preferences between candidate outputs. | audit preference data
alignment | Shaping behavior toward specified goals or preferences. | define the alignment objective
RLHF | Reinforcement learning from human feedback. | discuss an RLHF workflow
DPO | Direct preference optimization; a preference-training method. | evaluate a DPO experiment
LoRA | Low-rank adaptation; a parameter-efficient adaptation method. | train a LoRA adapter
adapter | A small trainable component used for adaptation. | load a task adapter
base model | The starting model before the adaptation under discussion. | compare against the base model
training objective | The quantity a training process seeks to optimize. | specify the training objective
hyperparameter | A training or model setting selected rather than learned in that run. | document a hyperparameter choice
learning rate | A setting controlling the scale of training updates. | compare learning-rate settings
epoch | One pass through the training data. | record the epoch count
overfitting | Fitting training patterns without adequate generalization. | monitor for overfitting
generalization | Performance on relevant examples beyond those used for fitting. | test generalization
catastrophic forgetting | Loss of previously learned capabilities during further training. | assess catastrophic forgetting
format adherence | Consistency with a required output structure. | measure format adherence
structured output | Output constrained or organized into a defined structure. | validate structured output
few-shot prompting | Supplying a small set of examples in the prompt. | test few-shot prompting
behavioral target | The specified behavior an intervention aims to change. | define the behavioral target
training artifact | A saved output of training, such as weights or configuration. | version the training artifact
rollback candidate | A previously validated configuration available for reversion. | retain a rollback candidate''',
    precision='Fine-tuning changes model parameters; prompting supplies instructions at inference time; retrieval supplies external context. These interventions can interact, but they do not have interchangeable mechanisms or guarantees.',
    precision_extra='Permission-cleared examples are authorized for use, not automatically accurate or consistently labeled. Format adherence is a measurable behavioral target; it does not prove policy correctness or broad alignment.',
    phrases='''Separate failures | We have a formatting issue and a source-freshness issue.
Ask about mechanism | How would this change prevent the obsolete policy from entering the context?
Define a target | The target is consistent output in the required fields.
Propose a baseline | Let us test clearer prompting before attributing gains to training.
Check examples | Are the reference summaries consistent with the same rubric?
Limit a remedy | Fine-tuning may improve the behavior; it does not keep an index current.
Hold a variable fixed | Use the same cleaned source set for both configurations.
Agree on evidence | We will compare format adherence and factual correctness separately.
Protect evaluation | Keep the final test examples outside the training set.
State an alternative | A constrained output format may address part of this problem.
Ask for permission status | Are these examples cleared for the intended training use?
Avoid conflation | Permission, quality, and representativeness are separate checks.
Check wider effects | Does the adaptation reduce performance on other required tasks?
Keep a baseline | Retain the validated base configuration for comparison.
Bound a recommendation | I recommend an experiment, not immediate adoption.
Record the decision | We will fix the stale index and test the formatting intervention independently.''',
    notes='''May, not will | "Fine-tuning may improve adherence" expresses a hypothesis; "will fix it" promises an untested result.
Two-object contrast | "Change the source, not just the behavior" draws attention to what each intervention affects.
Before attributing | This phrase delays a causal conclusion until a comparison has been completed.
Separate adverbs | "Evaluate them separately" refers to separate measures, not necessarily separate teams.
What would | "What would count as success?" requests a criterion without presupposing success.
Provided that | Use the condition in the same sentence: "We can train, provided that the data audit passes."''',
    d='''Which action directly addresses the known stale source? | Correct the retrieval index through the approved update process. | Assume format training refreshes all documents. | Rename the output fields. | Increase the number of training epochs blindly. | The obsolete wording is in retrieval; a source update addresses that known mechanism without assuming training will refresh it.
Which is a behavioral target? | Returning the required fields consistently | Owning a permission-cleared file | Scheduling a review meeting | Having a larger office | Format adherence is an observable output behavior; the other items do not specify model behavior.
Which claim needs qualification? | Fine-tuning will solve both failures. | The prompt has one example. | The index contains obsolete wording. | The label audit is unfinished. | The proposed remedy has not been evaluated and does not directly maintain source freshness.
Which comparison best isolates the formatting intervention? | Keep sources and test cases fixed while changing the formatting method. | Change data, model, metrics, and test cases together. | Evaluate only the training examples. | Accept any output with a confident tone. | Holding sources and cases fixed makes the effect of the formatting change easier to interpret.''',
    dialogue='''Tessa | I think we should fine-tune the summarizer. It ignores our field structure and sometimes quotes the old refund policy. Training could make it more consistent.
Dev | Consistency is worth testing, but those are different [[failure modes::Failure modes identify distinct ways a system fails; wrong structure and stale factual content need not share a cause.]]. What would the training change in the source material supplied to the model?
Tessa | It would not update the retrieval index. I checked this morning, and the obsolete refund paragraph is still there. That source needs a separate correction.
Dev | Right. Let us define the formatting problem as a [[behavioral target::A behavioral target specifies the output behavior to change, here adherence to the required fields.]], then keep policy freshness as a data-maintenance issue with its own owner.
Tessa | For formatting, we have 200 example summaries cleared for training use. I can start preparing them, although we have not audited their labels yet.
Dev | Please do that audit first. Permission to use an example does not establish its [[consistency::Consistency means examples follow compatible criteria; permission alone says nothing about agreement among labels or formats.]] with the field schema or the instructions in the other examples.
Tessa | Would you want a prompting comparison before training? The current prompt includes only one example, and it does not show how to handle an absent field.
Dev | Yes. A stronger [[few-shot::Few-shot prompting supplies a small set of examples at inference time, providing a useful comparison with parameter updates.]] baseline and a structured-output option would tell us whether training adds value beyond clearer task specification.
Tessa | All right. Two work items, then: repair the index and compare formatting methods. I'll keep their results separate.
Dev | Exactly. Keep the source set fixed within the comparison, and measure [[format adherence::Format adherence measures conformity to the required structure, which must remain distinct from factual correctness.]] separately from policy correctness. An answer can pass one and fail the other.
Tessa | Should the training objective reward the presence of every field, even if the source gives no evidence for a value? That could encourage invented details.
Dev | No. The examples need an agreed representation for missing information. A complete [[schema::A schema defines the required structure and allowed fields; it does not authorize inventing unsupported values.]] does not mean every field contains a positive factual assertion.
Tessa | I will include that distinction in the rubric. After we select the method, we should evaluate on cases that were never used to tune it.
Dev | Correct. We need evidence of [[generalization::Generalization concerns performance beyond the examples used to fit or choose the method.]], including summaries with exceptions, missing details, and layouts absent from the training examples.
Tessa | If we test an adapter, I also want to check our other summary tasks. Better performance on refunds could conceal a regression in cancellation summaries.
Dev | Include those. Further training can affect existing behavior, including [[catastrophic forgetting::Catastrophic forgetting names loss of previously learned capabilities during later training; a targeted gain does not rule it out.]]. We should assess relevant capabilities rather than assuming a small adaptation has no wider effects.
Tessa | I will version the examples, configuration, and resulting adapter together. That way the team can reproduce the comparison and identify exactly what was evaluated.
Dev | Good. Retain a validated [[rollback candidate::A rollback candidate is a previously checked configuration available if the new adaptation must be withdrawn.]] as well. A successful experiment is not a reason to lose the previous working configuration.
Tessa | I'll start with the example audit and the prompting baseline. Can we review those results before we spend time on an adapter?
Dev | Yes. List the expected gains as [[hypotheses::Hypotheses are proposed explanations or outcomes to test; they are not established findings before the comparison.]] in the experiment note. If the baseline solves the problem, we may not need training.''',
    rehearsal=["After checking the answers, identify the two failures aloud: obsolete source wording and inconsistent output fields.","Switch roles. Read the proposed experiment with fixed sources and test cases; keep data-use permission separate from the unfinished label audit.","Complete the category-list exchange. Correct the six-category prompt to the stated five-category requirement, while leaving any training benefit unconfirmed."],
    transfer_title='A classifier uses an outdated category list',
    transfer_setup='A classifier is required to use five current categories. Its prompt still lists six older categories. The team has not yet tested a corrected prompt or new training data.',
    transfer='''Scientist: "The prompt supplies an obsolete ___, so we should correct that input first." | category list | The known discrepancy is the six-category instruction, not evidence that a training change is already required.
Lead: "Then compare the corrected prompt with the existing ___." | baseline | A baseline provides the reference against which the effect of the corrected prompt can be measured.
Scientist: "We will measure adherence on ___ examples, not only the demonstrations." | held-out | Examples kept outside fitting and selection provide a more independent check than examples used to demonstrate the task.
Lead: "Until then, the benefit of further training remains a ___." | hypothesis | No training comparison has been completed, so its benefit is a proposed outcome rather than a finding.'''))

BOOK['units'].append(unit(
    title='Evaluation, Benchmarks, and Regression', scene='The average is down, but one slice improved',
    skill='Present disaggregated results and challenge an oversimplified release argument.',
    brief='On the same 100-case test, the previous model passes 90 cases and the candidate passes 88. Among 20 long-document cases, passes rise from 12 to 18. Among 80 short-request cases, passes fall from 78 to 70. The scoring rubric is unchanged. Production traffic proportions and the seriousness of individual failures have not been analyzed. Noor chairs the review; Ben prepared the results.',
    cast='Noor | Evaluation manager\nBen | Machine-learning engineer',
    culture=('Do not hide the inconvenient slice', 'A favorable subgroup does not erase an overall decline, and an overall decline does not erase a useful subgroup improvement. Present both. A defensible recommendation explains what is being traded and which missing evidence could change the decision.'),
    a='''What happens to total passes? | They fall from 90 to 88. | They rise from 88 to 90. | They stay at 90. | They rise from 12 to 18 overall. | The 12-to-18 improvement applies only to long documents; total passes decline by two.
Which slice improves? | Long-document cases | Short-request cases | Every production request | All failure severities | Long-document passes rise from 12 to 18; short-request passes fall from 78 to 70.
What remains unknown? | The production mixture and seriousness of failures | The test-set size | Whether the rubric changed | The candidate's total passes | The briefing supplies test counts and an unchanged rubric, but not production proportions or severity analysis.''',
    vocabulary='''evaluation | A structured assessment against specified criteria. | design an evaluation
benchmark | A reference test used for comparison. | interpret a benchmark result
baseline | The reference system or result for a comparison. | establish a baseline
candidate | The version under consideration. | evaluate the candidate
regression | A deterioration in previously measured behavior. | investigate a regression
test case | A defined input and expected criterion or outcome. | inspect a failed test case
golden set | Curated cases used to check important behavior repeatedly. | maintain a golden set
pass rate | The fraction of evaluated cases meeting a criterion. | report the pass rate
acceptance criterion | A stated condition required for acceptance. | agree on acceptance criteria
slice | A defined subgroup within evaluation data. | analyze a performance slice
aggregate | A combined measure across multiple cases or groups. | report the aggregate score
disaggregation | Breaking a combined result into meaningful groups. | disaggregate by task type
severity | The seriousness of a failure's consequences. | assess failure severity
false positive | A positive decision when the reference outcome is negative. | inspect false positives
false negative | A negative decision when the reference outcome is positive. | review false negatives
confusion matrix | A table comparing predicted and reference categories. | examine the confusion matrix
calibration | Agreement between stated confidence and observed outcomes. | assess confidence calibration
confidence interval | A range expressing uncertainty under stated statistical assumptions. | report a confidence interval
statistical significance | Evidence against a null model under a specified statistical test. | distinguish significance from usefulness
practical significance | The importance of a difference for the actual task. | assess practical significance
paired comparison | Comparison of results on corresponding cases. | run a paired comparison
LLM-as-judge | Use of a language model to evaluate outputs. | calibrate an LLM-as-judge setup
human review | Assessment by people using defined criteria. | conduct a blinded human review
release gate | A defined decision checkpoint before release. | satisfy the release gate''',
    precision='The aggregate falls by two percentage points. Long-document performance rises from 60 to 90 percent; short-request performance falls from 97.5 to 87.5 percent. These are test-set rates, not verified production estimates.',
    precision_extra='Statistical significance is not practical importance, and an interval is not a guarantee. A pass rate treats cases according to its stated counting rule; it may conceal unequal consequences among failures.',
    phrases='''Lead with both results | Overall passes fell, while the long-document slice improved.
Show the base | Eighteen of 20 long-document cases passed.
Describe the regression | Short-request passes fell from 78 to 70 out of 80.
Request paired cases | Which previously passing cases now fail?
Separate impact | A count alone does not tell us how serious those failures are.
Check relevance | Does this test mixture resemble the traffic we plan to serve?
Limit a conclusion | We cannot infer production performance from these counts alone.
Propose the next review | Compare the changed cases and classify their failure severity.
Challenge a headline | The improved slice should not replace the overall result on the slide.
Check consistency | Were both versions scored against the same rubric?
Preserve uncertainty | We have not established whether this difference is stable across samples.
Name a gate | Which acceptance criterion applies to the short-request regression?
Avoid metric shopping | Let us agree on the criteria before selecting the winning score.
Check a judge | How closely does the automated judge match the reviewed labels?
Offer a bounded option | Routing long documents separately is a proposal to test, not an approved fix.
Close the review | We will defer the decision until the changed cases have been assessed.''',
    notes='''While for contrast | "The total fell while one slice improved" presents simultaneous but contrasting findings.
Out of | "Eighteen out of twenty" keeps the numerator and denominator audible.
Previously and now | These words make a regression concrete: "previously passed, now fails."
Cannot infer | This limits a conclusion without claiming that the proposed conclusion must be false.
Would need | "We would need a routing evaluation" names a requirement before adopting a proposed alternative.
Comparatives | Specify the object: "better on long documents" is narrower than "a better model."''',
    d='''Which summary preserves both findings? | Total passes fell by two; long-document passes rose by six. | Every task improved by six points. | Short requests improved from 70 to 78. | Production accuracy is exactly 88 percent. | The statement correctly separates the overall count from the improved subgroup and makes no production claim.
What is the candidate's long-document pass rate? | 90 percent | 18 percent | 88 percent | 60 percent | Eighteen divided by twenty equals 90 percent; 88 percent is the aggregate test rate.
Which question targets practical significance? | How serious are the newly failing cases for users? | Is the two-point difference stable across repeated samples? | Do the slice counts add up to the aggregate score? | Did both variants use the same scoring rubric? | Consequences for users address practical importance. Stability, arithmetic reconciliation and rubric consistency are also useful, but answer different questions.
Which proposed conclusion exceeds the evidence? | Long-document routing is already safe to release. | The rubric is unchanged. | The candidate passes 88 of 100 cases. | The short-request slice worsened. | No routing or severity assessment has established that a specialized release is acceptable.''',
    dialogue='''Ben | The candidate is much stronger on long documents. It passed 18 of those 20 cases, compared with 12 for the previous version. That seems release-worthy.
Noor | Show the [[aggregate::The aggregate combines all test cases, so it prevents a favorable subgroup from standing in for the whole result.]] as well. The candidate passes 88 out of 100 overall, while the previous version passes 90.
Ben | Yes. The short requests account for the decline: 70 passes out of 80, compared with 78. I should have led with both results.
Noor | Thank you. That is a meaningful [[regression::A regression is a worsening of measured behavior; here eight fewer short-request cases pass.]] to investigate, even though the long-document gain is real on this set.
Ben | Could we weight the long documents more heavily? They are harder, and the team invested most of its work in that capability during this iteration.
Noor | Difficulty alone does not determine the weight. We need the intended traffic mixture and agreed [[acceptance criteria::Acceptance criteria are the conditions for approving a version, ideally set before selecting whichever metric looks favorable.]], not weights chosen after seeing the result.
Ben | The production proportions have not been analyzed. We can say that plainly. I can also list which short-request cases changed from pass to fail.
Noor | Please do a [[paired comparison::A paired comparison examines corresponding cases across versions, revealing which individual outcomes changed rather than only comparing totals.]]. The totals do not tell us whether the new failures are harmless omissions or serious errors.
Ben | Would you want a severity category for every changed case? A refusal on a valid request and a confident false answer both count as failures now.
Noor | Exactly. The rubric can preserve its binary score while a separate [[severity::Severity describes how consequential a failure is; equal pass-fail counts need not imply equal user impact.]] review explains the impact. We should not silently change the scoring rule halfway through.
Ben | We used an automated judge for the first pass. It agreed with the reviewed labels on most examples, but I have not checked the newly failing slice.
Noor | Then check that slice with [[human review::Human review applies the stated criteria to actual outputs and can examine judge disagreements in the changed subgroup.]]. Agreement across the whole set can hide weaker judgment on the cases that matter here.
Ben | If those reviews confirm the long-document gain, could we route only long documents to the candidate and keep short requests on the previous version?
Noor | It is a useful proposal, but the routing decision becomes another component to evaluate. We have not measured its [[false positives::False positives in the proposed router would send requests into the long-document path when they do not meet its intended condition.]] or the consequences of misclassification.
Ben | So routing needs its own test. And twenty long documents isn't much evidence. Should I add an uncertainty estimate to the slide?
Noor | Yes, with appropriate assumptions and qualified analysis. Do not use [[statistical significance::Statistical significance concerns evidence under a statistical model; it does not alone establish that a difference matters operationally.]] as a synonym for business value or a guarantee of future performance.
Ben | I will revise the slide to show both counts, the shared rubric, and the missing traffic and severity analysis. The candidate's strengths will still be visible.
Noor | Good. That is [[disaggregation::Disaggregation separates the combined result into defined groups, making different patterns visible without discarding the overall result.]], not an attempt to hide the average. We want the decision-maker to see why the headline alone is insufficient.
Ben | I'll recommend waiting for the changed-case review. I still think routing is worth testing, but I won't present it as a fix today.
Noor | Agreed. The [[release gate::A release gate is the decision checkpoint whose criteria must be met; presenting an improved slice does not automatically satisfy it.]] remains open. The next update should say which criteria are met, which are not, and what evidence is still missing.''',
    rehearsal=['Check the dialogue. Read both slices: 12 to 18 of 20 long cases; 78 to 70 of 80 short cases.', 'Switch roles. State that total passes fall from 90 to 88; severity and production mixture remain unmeasured.', 'Complete the urgent-message exchange. Name the four misses as false negatives and retain the required severity review.'],
    transfer_title='A support classifier misses urgent messages',
    transfer_setup='A classifier has a high overall score but misses four of ten urgent messages. Urgent-message consequences have not been reviewed. The team must not treat aggregate success as sufficient evidence for release.',
    transfer='''Reviewer: "The overall ___ hides a weak urgent-message subgroup." | aggregate | A combined score can conceal poor results in a smaller but important subgroup.
Engineer: "Those missed urgent messages are ___ for that category." | false negatives | The messages are urgent but the classifier fails to identify them as positive urgent cases.
Reviewer: "We need a separate assessment of their ___." | severity | The seriousness of missing urgent messages cannot be inferred from the overall success count.
Engineer: "Then the ___ should remain unresolved until that review is complete." | release gate | The approval checkpoint lacks relevant evidence and should not be treated as passed.'''))

BOOK['units'].append(unit(
    title='Inference, Latency, Cost, and Deployment', scene='Faster on average is not ready for everyone',
    skill='Negotiate a staged deployment with explicit conditions and rollback ownership.',
    brief='A smaller model reduces mean response time from four seconds to two on a fixed test. Complex-answer quality and peak-load tail latency remain unchecked. Maya owns serving operations; Luis owns the product pilot. An internal pilot may use synthetic requests only. A production rollout requires a separate review. The previous configuration remains available, but rollback ownership has not been assigned.',
    cast='Maya | Serving engineer\nLuis | Product lead',
    culture=('Separate speed from service readiness', 'A faster average is a useful result, not a complete release case. Say which workload was tested and which decisions remain conditional. Agree on who can pause a pilot before pressure makes that conversation difficult.'),
    a='''Which result is measured? | Mean response time falls from four seconds to two. | Every request finishes within two seconds. | Complex answers remain equally accurate. | Peak-load tail latency improves. | The case reports a mean on a fixed test, not a guarantee for every request or an unmeasured workload.
What traffic is permitted in the internal pilot? | Synthetic requests only | All production traffic | Real customer secrets | Any request a volunteer chooses | The stated pilot boundary allows synthetic requests only; broader traffic needs separate authorization.
Which responsibility is unresolved? | Who owns rollback | Who owns serving operations | Who owns the product pilot | Whether a previous configuration exists | The case names operational and product owners and a previous configuration, but no rollback owner.''',
    vocabulary='''latency | Time taken for a request or processing step. | measure response latency
mean | The arithmetic average of observed values. | report mean latency
median | The middle value in an ordered set. | compare median response times
P95 | The 95th percentile of a measured distribution. | inspect P95 latency
tail latency | Response times toward the slow end of a distribution. | investigate tail latency
throughput | The rate at which work is completed. | measure requests per second
concurrency | Work occurring at the same time. | test concurrent requests
queueing | Waiting for resources before processing. | measure queueing delay
batching | Processing multiple requests together. | evaluate dynamic batching
streaming | Sending portions of output before the full response is complete. | enable response streaming
time to first token | Delay before the first generated token arrives. | track time to first token
token rate | The rate of generated or processed tokens. | measure output token rate
autoscaling | Automatic adjustment of resource capacity. | review autoscaling behavior
cold start | Initial startup delay before a resource is ready. | measure cold-start effects
load test | A test under specified levels of demand. | run a controlled load test
canary | A limited release used to observe behavior before expansion. | define a canary population
rollout | Gradual or full introduction of a configuration. | stage the rollout
rollback | Return to a previous configuration. | assign rollback ownership
fallback | An alternative behavior when the preferred path cannot serve. | test the fallback path
SLO | Service-level objective; a defined internal service target. | agree on an SLO
error budget | The permitted unreliability associated with a service objective. | track error-budget consumption
rate limit | A restriction on request frequency or volume. | respect a rate limit
capacity planning | Estimating resources needed for expected demand. | review capacity assumptions
cost per request | Allocated processing expense for a defined request unit. | compare cost per request''',
    precision='A mean of two seconds does not mean every request finishes within two seconds. Time to first token and time to complete answer measure different experiences. Streaming can change one without reducing the other.',
    precision_extra='A pilot, canary, and production rollout need explicit populations and authorization. A fallback is an alternate path; a rollback restores a previous configuration. Neither is a complete plan until ownership and conditions are clear.',
    phrases='''State the measured gain | Mean response time fell from four seconds to two on this test.
Protect the limitation | Complex-answer quality is still unmeasured.
Ask about the tail | What happens to the slowest requests under peak load?
Separate timings | Is that time to first token or time to complete the answer?
Define the population | The internal pilot uses synthetic requests only.
Name a stop condition | We need an agreed condition for pausing the pilot.
Assign authority | Who can initiate rollback if the condition is met?
Preserve a distinction | Pilot approval does not authorize production rollout.
Check comparability | Were both models tested under the same demand and input mix?
Qualify cost | Please include retries and fallback traffic in the cost comparison.
Ask about waiting | How much of the delay occurs before inference begins?
Bound a promise | I can provide the load-test results, not promise a two-second maximum.
Confirm readiness | Has the previous configuration been checked for restoration?
Request a runbook | Record the owner, contact route, and approved recovery procedure.
Avoid average-only reporting | Show the distribution as well as the mean.
Close the decision | We can proceed with the bounded test once the owners and conditions are confirmed.''',
    notes='''On this test | This phrase limits the measurement to the workload actually observed.
Every versus average | "Every request" is a universal claim; "on average" summarizes a distribution and permits exceptions.
Once versus until | "Proceed once ownership is confirmed" and "wait until ownership is confirmed" express the same prerequisite from opposite directions.
Authority verbs | "Can initiate rollback" names permission; "can contact the owner" names a communication ability.
Percent reduction | A mean falling from four seconds to two is a 50-percent reduction, not a two-percent reduction.
Excluding and including | State whether cost figures include retries, idle capacity, and alternate paths before comparing them.''',
    d='''Which claim is supported by the test? | Mean latency decreased by 50 percent. | Every response is twice as accurate. | P95 latency is exactly two seconds. | Peak traffic can double without risk. | The mean falls from four to two, a reduction of half; the other claims concern unmeasured outcomes.
Which question distinguishes first visible output from a finished response? | Is that first-token time or complete-answer time? | Is that average latency or the ninety-fifth percentile? | Is that queueing time or time spent running inference? | Is that single-request throughput or batch throughput? | First-token and completion times identify the two user-visible events in the question. The other comparisons describe distributions or different serving measures.
Which statement preserves authorization boundaries? | The synthetic pilot does not authorize production traffic. | Internal approval covers every later rollout. | A faster mean removes the need for review. | An available old model assigns rollback ownership. | The case explicitly separates the internal pilot from production approval.
Which expression means restoring the earlier configuration? | initiate rollback | increase concurrency | stream the output | count input tokens | Rollback returns the system to a previous configuration; the other actions change different aspects of serving.''',
    dialogue='''Luis | The smaller model cuts average response time from four seconds to two. I would like to use it in the pilot and announce the faster experience.
Maya | The mean improved on the fixed test, yes. We still need [[tail latency::Tail latency describes the slower end of the response-time distribution, which an improved average does not establish.]] under load and a quality check on complex answers before making a broader claim.
Luis | Could we call it a two-second assistant if we explain that the figure is an average? Marketing would prefer a simple phrase for the demonstration.
Maya | I would keep the qualification attached. The [[mean::The mean is an arithmetic average; it is not an upper bound on individual request times.]] does not set a maximum, and we have not tested the traffic pattern that production will bring.
Luis | Fair point. For the internal pilot we can stay with synthetic requests. Does streaming let us demonstrate a faster answer without changing the model again?
Maya | It may improve [[time to first token::Time to first token measures the initial wait, not the time needed to receive and verify the whole answer.]], but we should report completion time separately. Seeing the first words is not the same as receiving the complete response.
Luis | What do you need from product to define a useful load test? We have examples of simple and complex requests, but not a production traffic forecast.
Maya | A documented provisional mix and demand assumptions. We can vary [[concurrency::Concurrency is the amount of simultaneous work; varying it helps expose waiting and resource contention.]] and report where those assumptions are uncertain rather than presenting them as observed customer behavior.
Luis | Include the complicated cases even if they are a small share. A fast answer that loses a key exception would undermine the whole demonstration.
Maya | Agreed. We should also include retries and [[fallback::A fallback is an alternate serving path; its extra work can affect both cost and observed response time.]] traffic in the cost comparison. The headline model price alone does not describe the complete request cost.
Luis | Suppose the internal test exposes a serious quality problem. The previous configuration is still available. Is that enough to let us start today?
Maya | We also need [[rollback::Rollback restores a previous configuration; availability of that configuration does not establish who is authorized to restore it.]] ownership and an approved procedure. Someone must be explicitly authorized to pause the test and restore the checked configuration.
Luis | I can own the decision to pause the product pilot. Can serving operations own the restoration step, with you as the named contact for this test?
Maya | Yes, subject to our operational review. Record the [[stop condition::A stop condition states when the pilot should pause, avoiding an improvised decision after a concerning result appears.]] and contact route in the pilot note so both teams know how to act.
Luis | I'll keep production traffic out. When the synthetic test is done, we'll take the results to the production review. Who needs that report?
Maya | Product and serving operations, at minimum. Before a [[rollout::A rollout introduces the configuration to its intended users; it requires its own scope and approval, beyond this synthetic test.]], they need the proposed user population and service criteria as well as the test results.
Luis | Can you provide the distribution, complex-answer results, and cost assumptions by Friday? I can postpone the external claim until we have that package.
Maya | I can provide the test results and unresolved items. If [[queueing::Queueing is waiting before processing resources are available; it can dominate latency even when model inference itself is faster.]] dominates at higher demand, I will say that rather than attribute every delay to the model.
Luis | Good. The pilot note will state the synthetic-only population, the pause owner, the proposed restoration owner, and the review required before we begin.
Maya | Then we have a bounded plan. We will report the measured gain alongside its [[limitations::Limitations identify the conditions and missing evidence that constrain how widely a measured result can be applied.]], and let the evidence determine the next step instead of promising a universal two-second response.''',
    rehearsal=["Check the answers. Read four seconds to two as a 50-percent reduction in the measured mean, not a maximum for every request.","Switch roles. Keep the pilot limited to synthetic requests and ask who owns rollback; availability of the old configuration is not an assigned owner.","Complete the timing exchange. Say one second to first token and six seconds to completion, with neither treated as an approved service target."],
    transfer_title='A dashboard mixes first-token and completion times',
    transfer_setup='A demonstration shows the first token after one second, but the complete answer takes six seconds. A slide calls the response time one second. No service target has been approved.',
    transfer='''Engineer: "One second is the ___, not the time for the full response." | time to first token | The first visible token arrives at one second; the full answer takes six seconds.
Lead: "Then show ___ separately so the comparison is clear." | completion time | Completion time captures the wait for the entire answer and must not be replaced by the first-token measure.
Engineer: "Neither figure is an approved ___." | service target | The scenario explicitly says no target has been approved; measurements do not themselves authorize a promise.
Lead: "Keep that ___ attached when the slide is shared." | qualification | The limiting explanation prevents readers from treating a one-second initial display as full-answer performance.'''))

BOOK['units'].append(unit(
    title='Safety, Security, Privacy, and Governance', scene='Report the exposure without repeating the secret',
    skill='Give a precise incident account, protect evidence, and distinguish findings from scope assumptions.',
    brief='In an authorized test, an assistant repeats a fictional secret placed inside a retrieved document. The document also contains text telling the assistant to ignore its task. The test uses a synthetic account and no real customer data. Hana owns the test; Marcus coordinates security review. One reproduction is confirmed. Whether other configurations are affected is unknown. The team has an approved restricted reporting channel.',
    cast='Hana | AI safety tester\nMarcus | Security review coordinator',
    culture=('Be specific without amplifying exposure', 'A concise report names the observed behavior, environment, and unknown scope. It does not paste sensitive material into a broad discussion. Separate a confirmed test result from claims about real customers or every deployment.'),
    a='''What has been confirmed? | One reproduction in an authorized synthetic test | Exposure of real customer data | Failure of every configuration | Completion of the security review | The case confirms one synthetic-test reproduction and explicitly leaves broader scope unknown.
Where should restricted evidence go? | The approved restricted reporting channel | An unrestricted group chat | A public presentation | A customer mailing list | The case provides an approved restricted route; the other destinations expand access unnecessarily.
Which distinction must the report preserve about impact? | Synthetic exposure versus real-customer impact | A retrieved instruction as proof of every configuration's behavior | A fictional credential as proof that production credentials leaked | One reproduction as proof of the entire affected population | The test uses fictional data and one tested configuration. It demonstrates the supplied behavior without establishing real-customer exposure or wider scope.''',
    vocabulary='''prompt injection | Untrusted content attempting to redirect model behavior. | report a prompt-injection attempt
untrusted content | Material that lacks authority to issue system instructions. | isolate untrusted content
trust boundary | A separation between different levels of authority or access. | identify a trust boundary
data exfiltration | Unauthorized transfer of information from its intended boundary. | assess exfiltration risk
secret | Information intended to remain restricted. | protect a test secret
credential | Information used to establish identity or access. | avoid exposing credentials
PII | Personally identifiable information that can identify an individual. | minimize PII in evidence
redaction | Removal or masking of restricted information. | prepare a redacted report
least privilege | Limiting access to what a role requires. | apply least-privilege access
permission scope | The range of actions or resources authorized. | document permission scope
guardrail | A control intended to detect, limit, or route risky behavior. | evaluate a guardrail
red teaming | Authorized adversarial testing to discover weaknesses. | define a red-team scope
threat model | A structured account of potential threats and assumptions. | review the threat model
attack surface | The interfaces or paths through which a system may be affected. | map the attack surface
reproduction steps | A recorded sequence that recreates an observed result. | submit restricted reproduction steps
incident report | A documented account of a potentially harmful event. | file an incident report
containment | Measures to limit an event's spread or consequences. | confirm containment ownership
mitigation | A measure intended to reduce risk or impact. | evaluate a proposed mitigation
residual risk | Risk that remains after controls are applied. | document residual risk
audit trail | A record supporting review of actions and decisions. | preserve the audit trail
retention | How long information is kept under a policy. | follow the evidence-retention policy
disclosure | Communication of information to another party. | coordinate responsible disclosure
governance | Defined structures for oversight and accountable decisions. | clarify governance responsibilities
human oversight | Review or intervention by authorized people. | define human-oversight responsibilities''',
    precision='Prompt injection concerns untrusted content attempting to redirect behavior. A test secret is deliberately fictional; its exposure demonstrates a behavior without proving real-customer impact. Do not collapse attempted manipulation, observed output, and verified scope into one claim.',
    precision_extra='A mitigation reduces risk; it does not automatically eliminate it. Containment limits exposure while investigation continues. Redaction removes restricted details from a copy; the authoritative evidence still needs approved handling.',
    phrases='''Lead with the observation | In one authorized test, the assistant repeated the synthetic secret.
Bound the environment | The reproduction used a synthetic account and no customer data.
Preserve unknown scope | We have not established whether other configurations are affected.
Separate intent and result | The document attempted to redirect behavior; this output is what we observed.
Protect evidence | I will place the complete trace in the restricted channel.
Offer a safe summary | The broad update can describe the behavior without reproducing the secret.
Ask for ownership | Who owns the containment decision for this environment?
Avoid premature closure | A blocked replay is encouraging, but it does not prove the issue is resolved.
Check authorization | Does this follow-up test remain within the approved scope?
State the limitation | No real-customer impact has been established by this test.
Request review | Please review the configuration and permission boundary before wider testing.
Preserve records | Retain the original evidence according to the approved policy.
Distinguish controls | The proposed guardrail is a mitigation to evaluate, not a guarantee.
Name residual risk | Which failure paths remain after this control is applied?
Set the next update | I will report the confirmed scope and outstanding questions after review.
Close responsibly | We will keep the finding open until the authorized reviewer accepts the evidence.''',
    notes='''No evidence versus evidence of none | "We have not established customer impact" does not prove that no customer could be affected.
Observed versus attempted | "Attempted to redirect" describes the content; "repeated the secret" describes the actual output.
Passive with ownership | "Evidence will be reviewed" is incomplete for coordination; name the reviewer when the role is known.
Within scope | This phrase limits authorized testing rather than inviting experimentation on other systems.
Still open | A finding can remain open after one mitigation test passes because broader questions remain unresolved.
Reported certainty | Keep "one reproduction" in the sentence so a later summary does not silently become "every configuration fails."''',
    d='''Which headline matches the known scope? | Synthetic secret repeated in one authorized test; broader scope unconfirmed. | Prompt injection confirmed across all production configurations. | No real credential was used, so no security-relevant behavior occurred. | A proposed detector closes the finding without further testing. | The supported headline retains both the observed reproduction and its limited scope. Synthetic data do not erase the behavior, and a proposed control is not a verified resolution.
Which statement distinguishes evidence from intent? | The document attempted redirection, and the output repeated the synthetic secret. | The tester intended to expose customers. | The model wanted to break policy. | The reviewer deliberately ignored the event. | The supported statement describes observable content and output without inventing motives for people or the model.
What is a mitigation? | A measure intended to reduce risk or impact | Proof that every risk is eliminated | An unrestricted copy of sensitive evidence | A substitute for authorization | A mitigation reduces risk; effectiveness and remaining risk still require evaluation.
Which wording avoids an unsupported absence claim? | We have not established real-customer impact. | No customer could ever be affected. | One blocked replay proves complete safety. | The synthetic test certifies production privacy. | The correct statement reports the current evidence boundary without claiming that all possible impact has been excluded.''',
    dialogue='''Hana | I need to report a finding from the authorized test. The assistant repeated the fictional secret placed in a retrieved document, and I have one confirmed reproduction.
Marcus | Please keep the full trace in the [[restricted channel::The restricted channel limits access to detailed evidence under the team's approved reporting process.]]. For the initial summary, identify the environment and behavior without copying the secret into this broader discussion.
Hana | The environment uses a synthetic account and contains no customer data. The document also includes text telling the assistant to ignore its assigned task.
Marcus | That is consistent with a [[prompt-injection::Prompt injection refers to untrusted material attempting to redirect model behavior; the report must still distinguish the attempt from the observed result.]] attempt. Describe the instruction separately from the output so reviewers can see what was attempted and what actually happened.
Hana | I will say that the output repeated the synthetic value. I have not tested other configurations, and I do not want the title to imply every deployment is affected.
Marcus | Good. Preserve that [[scope limitation::A scope limitation states which environments or cases have and have not been assessed, preventing unsupported generalization.]]. One reproduction establishes a finding in this test, not the full extent of possible exposure.
Hana | Should I stop the remaining tests while the team reviews it? The current authorization covers this environment, but not production accounts or external systems.
Marcus | Stay within that authorization. I will contact the owner for the [[containment::Containment concerns limiting further consequences while investigation proceeds; its owner must make the applicable operational decision.]] decision. Do not expand testing to answer the scope question without the required approval.
Hana | I can provide a redacted summary immediately and preserve the original trace under the evidence policy. The configuration and retrieval document are versioned.
Marcus | That supports an [[audit trail::An audit trail preserves the records needed to reconstruct actions, configuration, and review decisions.]]. Make sure the summary links to the controlled record rather than becoming a competing copy with missing context.
Hana | A colleague suggested adding a detector and closing the finding if the same replay is blocked. Would that be enough evidence for the review?
Marcus | It would be evidence about a proposed [[mitigation::A mitigation is a control intended to reduce the risk; one successful replay test does not establish that every relevant variant is controlled.]], not proof of complete resolution. We need the agreed tests and a review of what the detector does not cover.
Hana | I'll leave the finding open. Do you also need the list of tools the assistant could access during the test?
Marcus | Yes, at the appropriate detail level. The [[permission scope::Permission scope identifies which resources or actions were authorized, helping reviewers assess the boundaries relevant to the finding.]] matters for assessing potential consequences, even though this reproduction did not exercise every available capability.
Hana | Understood. The broad summary will not include access details or the synthetic value itself. The restricted evidence will retain what the authorized reviewer needs.
Marcus | That is appropriate [[redaction::Redaction removes restricted detail from a shared copy while preserving necessary original evidence through approved handling.]]. Do not replace the original evidence with the redacted copy; follow the approved retention process for each.
Hana | What should the next status update say if the detector blocks the replay but variant testing and configuration review are still pending tomorrow afternoon?
Marcus | Say exactly that. Name the remaining [[residual risk::Residual risk is what remains after a control is applied; pending checks prevent a blanket claim that the risk is gone.]] questions without inventing their outcomes. A passing replay is useful but narrower than a closed finding.
Hana | I will submit the bounded report and wait for authorization before any wider testing. I will also correct anyone who describes this as confirmed customer-data exposure.
Marcus | Yes. Link me to the evidence when it's ready. I'll route the [[finding::A finding records the observed issue and its review status; it should remain open until the authorized process accepts sufficient evidence.]] to the authorized reviewer and ask who owns the remaining checks.''',
    rehearsal=["After checking the dialogue, read the finding as one authorized synthetic-test reproduction, with broader scope unconfirmed.","Switch roles. Route the complete trace to the approved restricted channel and use the printed limited summary for a broader audience.","Complete the screenshot exchange. Preserve the original in the restricted repository, redact the broad summary, and do not present a proposed detector as a safety guarantee."],
    transfer_title='A broad chat receives a sensitive screenshot',
    transfer_setup='A tester has a screenshot containing a synthetic credential and internal configuration details. A broad project chat asks for an update. The approved evidence repository has restricted access.',
    transfer='''Tester: "I will share a ___ summary in the project chat." | redacted | The broad audience needs the finding's meaning without unnecessary credential or configuration details.
Reviewer: "Place the original screenshot in the approved ___ repository." | restricted | Restricted access preserves the detailed evidence for authorized review rather than widening distribution.
Tester: "The update will state the tested environment and the unknown ___." | scope | The report must separate the assessed environment from configurations whose behavior has not been established.
Reviewer: "And do not call a proposed detector a guarantee of ___." | safety | A proposed control may reduce risk, but its effectiveness and remaining limitations require evaluation.'''))
