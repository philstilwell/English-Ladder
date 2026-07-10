from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer, Table, TableStyle

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, make_dialogue_cloze
from generate_efsp_culture_pdfs import (
    CONTENT_WIDTH,
    PALETTE,
    S,
    box,
    build_pdf,
    bullets,
    h1,
    h2,
    h3,
    lines,
    p,
    rule,
    table,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "pdf" / "efsp"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def cover(title: str, subtitle: str, audience: str) -> list:
    return [
        Spacer(1, 0.95 * 72),
        p("EFSP Auxiliary ESL Curriculum", "CoverKicker"),
        Paragraph(esc(title), S["CoverTitle"]),
        Paragraph(esc(subtitle), S["CoverSub"]),
        Spacer(1, 0.25 * 72),
        box(
            audience,
            [
                "Focus: high-level professional English for AI development teams, including technical vocabulary, engineering discussion patterns, research/product tradeoffs, evaluation language, risk communication, and realistic workplace dialogue.",
                "Designed for advanced ESL learners who already work with software, data, or AI systems and need field-specific fluency rather than basic grammar instruction.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: AI language changes quickly. Teach learners to ask precise clarification questions, define terms in context, and distinguish research claims, implementation details, benchmark results, and product promises.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use common AI-development terms accurately in meetings, tickets, design reviews, and technical updates.",
    "Explain model behavior, data issues, evaluation results, and deployment tradeoffs in concise professional English.",
    "Participate in discussions about LLMs, RAG, agents, embeddings, fine-tuning, inference, safety, observability, and product risk.",
    "Ask high-quality clarification questions when requirements, metrics, or model outputs are ambiguous.",
    "Describe failures without exaggeration: hallucination, regression, drift, leakage, prompt injection, latency spikes, and retrieval misses.",
    "Deliver realistic AI-development updates to engineers, product managers, researchers, customers, and executives.",
]


MODULES = [
    {
        "title": "Module 1. Speaking the AI Development Stack",
        "time": "90 minutes",
        "big_idea": "AI teams use a layered vocabulary: model, data, prompt, retrieval, tools, serving, evaluation, monitoring, and product experience. Learners need to locate a problem in the stack before they can discuss it clearly.",
        "objectives": [
            "Name the layer where an AI issue occurs.",
            "Distinguish model capability from application behavior.",
            "Use concise stack language in standups and tickets.",
        ],
        "concepts": [
            "Model vs application: the model generates outputs; the application wraps prompts, retrieval, tools, policy, UI, logging, and fallback behavior around it.",
            "Pipeline: a sequence of steps such as ingest, chunk, embed, retrieve, rerank, prompt, generate, validate, and log.",
            "System boundary: what belongs to the model provider, the app team, the data team, or the platform team.",
        ],
        "activities": [
            "Stack map: learners place 24 terms in the correct layer.",
            "Ticket rewrite: learners turn vague issue reports into stack-specific bug reports.",
            "Standup drill: learners give a 45-second AI feature update with blocker, evidence, and next step.",
        ],
        "outputs": [
            "AI stack vocabulary map.",
            "Three polished standup updates.",
        ],
    },
    {
        "title": "Module 2. LLMs, Transformers, Tokens, and Context",
        "time": "90 minutes",
        "big_idea": "High-level AI communication often depends on explaining what the model sees: tokens, messages, context window, instructions, examples, retrieved text, and tool results.",
        "objectives": [
            "Explain tokens, context window, prompts, and attention in workplace English.",
            "Discuss prompt changes without implying that prompting is magic.",
            "Describe context limits, truncation, and cost/latency tradeoffs.",
        ],
        "concepts": [
            "Tokenization: text is split into model-readable units; tokens affect context length, cost, and latency.",
            "Context window: the information available to the model at generation time.",
            "Instruction hierarchy: system/developer instructions, user request, retrieved context, examples, and tool outputs may compete.",
        ],
        "activities": [
            "Plain-English explainer: learners explain tokenization to a product manager.",
            "Prompt review: learners critique a prompt for ambiguity, hidden assumptions, and missing output constraints.",
            "Context budget negotiation: learners decide what to include or remove when a prompt is too large.",
        ],
        "outputs": [
            "Prompt review checklist.",
            "Context budget explanation script.",
        ],
    },
    {
        "title": "Module 3. Data, Datasets, Labels, and Leakage",
        "time": "90 minutes",
        "big_idea": "AI systems are shaped by data quality. Teams need precise language for dataset splits, annotation guidelines, leakage, imbalance, representativeness, and privacy constraints.",
        "objectives": [
            "Describe a dataset and its limitations without overclaiming.",
            "Explain labels, ground truth, noisy labels, and inter-annotator agreement.",
            "Raise leakage and privacy concerns clearly.",
        ],
        "concepts": [
            "Train/validation/test split: different data subsets serve different purposes in model development and evaluation.",
            "Ground truth: the expected answer or label, often created or verified by humans.",
            "Data leakage: information from the target, test set, or future state accidentally enters training or evaluation.",
        ],
        "activities": [
            "Dataset card discussion: learners summarize source, coverage, bias, limitations, and risk.",
            "Annotation meeting: learners negotiate ambiguous labeling guidelines.",
            "Leakage hunt: learners identify possible leakage in five project descriptions.",
        ],
        "outputs": [
            "Dataset limitation statement.",
            "Annotation guideline clarification questions.",
        ],
    },
    {
        "title": "Module 4. Retrieval, Embeddings, Vector Search, and RAG",
        "time": "90 minutes",
        "big_idea": "Many production AI apps combine retrieval with generation. Learners need to discuss chunking, embeddings, vector stores, recall, reranking, grounding, citations, and retrieval misses.",
        "objectives": [
            "Explain embeddings, semantic search, vector stores, and RAG.",
            "Diagnose retrieval failures separately from generation failures.",
            "Discuss chunking, metadata, reranking, and grounding in design reviews.",
        ],
        "concepts": [
            "Embedding: a vector representation of text or other data designed to preserve useful meaning for tasks such as search or clustering.",
            "RAG: retrieval brings external context into the generation step so the system can answer from documents rather than only from model parameters.",
            "Grounding: connecting output claims to retrieved or otherwise verified source material.",
        ],
        "activities": [
            "RAG failure triage: learners decide whether the bug is ingestion, chunking, retrieval, reranking, prompt, or generation.",
            "Retrieval metrics discussion: learners compare recall, precision, MRR, and answer faithfulness.",
            "Architecture explanation: learners explain a RAG pipeline to a non-technical stakeholder.",
        ],
        "outputs": [
            "RAG troubleshooting flow.",
            "Stakeholder explanation of retrieval vs generation.",
        ],
    },
    {
        "title": "Module 5. Fine-Tuning, Alignment, and Adaptation",
        "time": "90 minutes",
        "big_idea": "Teams often confuse prompt changes, RAG, fine-tuning, adapters, supervised fine-tuning, preference tuning, and RLHF. The language goal is to recommend the right adaptation method for the problem.",
        "objectives": [
            "Differentiate prompt engineering, RAG, fine-tuning, LoRA/adapters, SFT, DPO, and RLHF at a practical level.",
            "Discuss when fine-tuning is not the right solution.",
            "Explain cost, data, evaluation, and maintenance tradeoffs.",
        ],
        "concepts": [
            "Fine-tuning changes model weights; prompting and RAG change the information or instructions around the model.",
            "PEFT/LoRA/adapters: parameter-efficient approaches that adjust a smaller number of parameters than full fine-tuning.",
            "Alignment and preference tuning: training or optimizing models to follow desired behavior patterns, policies, or preferences.",
        ],
        "activities": [
            "Method selection: learners choose between prompt fix, retrieval fix, fine-tune, or product constraint.",
            "Tradeoff pitch: learners defend an adaptation method to engineering and product.",
            "Risk statement: learners describe what could get worse after fine-tuning.",
        ],
        "outputs": [
            "Adaptation decision matrix.",
            "Fine-tuning recommendation memo.",
        ],
    },
    {
        "title": "Module 6. Evaluation, Benchmarks, and Regression",
        "time": "90 minutes",
        "big_idea": "AI teams need language for uncertainty. 'It looks better' is not enough. Learners need to discuss offline evals, online evals, golden sets, human review, model-graded evals, regression, pass rate, and confidence.",
        "objectives": [
            "Explain evaluation design and limitations.",
            "Report metrics with context and uncertainty.",
            "Push back on weak benchmarks or misleading averages.",
        ],
        "concepts": [
            "Golden set: a curated set of representative examples used for repeated evaluation.",
            "Regression: a previously working behavior gets worse after a change.",
            "LLM-as-judge: a model evaluates outputs, useful but requiring calibration and human spot checks.",
        ],
        "activities": [
            "Eval readout: learners present a metric change, sample failures, and release recommendation.",
            "Metric critique: learners find blind spots in an eval plan.",
            "Regression triage: learners decide whether to block a release.",
        ],
        "outputs": [
            "Evaluation readout template.",
            "Release recommendation script.",
        ],
    },
    {
        "title": "Module 7. Inference, Latency, Cost, and Deployment",
        "time": "90 minutes",
        "big_idea": "AI development is also systems engineering. Learners need vocabulary for inference paths, throughput, batching, caching, rate limits, GPUs, quantization, streaming, fallbacks, and SLOs.",
        "objectives": [
            "Explain latency and cost drivers in AI applications.",
            "Discuss deployment constraints without losing product trust.",
            "Use incident and observability language for model-serving issues.",
        ],
        "concepts": [
            "Inference: running a trained model to produce outputs.",
            "Latency vs throughput: response time for one request vs volume handled over time.",
            "Fallback: a planned behavior when the preferred model, tool, or retrieval path fails.",
        ],
        "activities": [
            "Latency budget: learners explain where time is spent in a request.",
            "Cost tradeoff: learners compare a larger model, smaller model, caching, batching, and retrieval changes.",
            "Incident update: learners write a status update for a model-serving degradation.",
        ],
        "outputs": [
            "Latency/cost explanation.",
            "AI incident update template.",
        ],
    },
    {
        "title": "Module 8. Safety, Security, Privacy, and Governance",
        "time": "90 minutes",
        "big_idea": "AI teams must discuss risk precisely: hallucination, prompt injection, jailbreaks, PII, data retention, bias, harmful output, policy enforcement, audit logs, and human-in-the-loop review.",
        "objectives": [
            "Name safety and security risks without dramatic overstatement.",
            "Explain guardrails, validation, red-teaming, and monitoring.",
            "Escalate privacy or policy concerns with evidence.",
        ],
        "concepts": [
            "Prompt injection: untrusted content attempts to override or manipulate system behavior.",
            "Guardrail: a policy, model, validation layer, or product control designed to reduce unsafe or unwanted behavior.",
            "Human-in-the-loop: a workflow where humans review, approve, correct, or audit model behavior.",
        ],
        "activities": [
            "Risk register: learners write risk, trigger, impact, mitigation, owner, and review cadence.",
            "Red-team debrief: learners report adversarial testing results clearly.",
            "Privacy escalation: learners decide when to pause launch and involve legal/security.",
        ],
        "outputs": [
            "AI risk register entry.",
            "Safety escalation script.",
        ],
    },
]


JARGON_GROUPS = [
    (
        "Core model terms",
        [
            ("LLM", "Large language model; a model trained to process and generate language-like sequences."),
            ("Transformer", "A neural architecture based on attention mechanisms, common in modern language models."),
            ("Parameter", "A learned numerical value in a model; not the same as an API parameter."),
            ("Checkpoint", "A saved version of model weights at a point in training or fine-tuning."),
            ("Foundation model", "A broadly trained model adapted to many downstream tasks."),
            ("Multimodal", "Able to handle more than one data type, such as text, image, audio, or video."),
        ],
    ),
    (
        "Prompt and context terms",
        [
            ("Prompt", "The instructions, examples, user request, and context given to a model."),
            ("System prompt", "High-priority instructions that guide model behavior inside an application."),
            ("Few-shot", "Including examples in the prompt to show the desired pattern."),
            ("Context window", "The amount of input and generated text the model can consider in one request."),
            ("Token", "A unit of text processed by the model; token count affects cost, context, and latency."),
            ("Temperature", "A generation setting that affects output variability."),
        ],
    ),
    (
        "Retrieval and RAG terms",
        [
            ("Embedding", "A vector representation used for similarity search, clustering, classification, and related tasks."),
            ("Vector store", "A database or index for storing and searching embeddings."),
            ("Chunking", "Splitting documents into retrievable pieces."),
            ("Reranker", "A model or step that reorders retrieved results for relevance."),
            ("RAG", "Retrieval-augmented generation: retrieve relevant context, then generate an answer using it."),
            ("Grounding", "Tying model output to retrieved, cited, or verified source information."),
        ],
    ),
    (
        "Training and adaptation terms",
        [
            ("Fine-tuning", "Updating model weights on task- or domain-specific data."),
            ("SFT", "Supervised fine-tuning with input-output examples."),
            ("RLHF", "Reinforcement learning from human feedback; training with human preference signals."),
            ("DPO", "Direct preference optimization; preference tuning without a separate reward model in common workflows."),
            ("LoRA", "Low-rank adaptation; a parameter-efficient fine-tuning method."),
            ("Adapter", "A small trainable module inserted into or attached to a pretrained model."),
        ],
    ),
    (
        "Evaluation terms",
        [
            ("Eval", "A test or evaluation suite for model or system behavior."),
            ("Benchmark", "A standardized test used to compare systems, often imperfect for a product use case."),
            ("Golden set", "Curated examples used repeatedly to test important behavior."),
            ("Regression", "A behavior that gets worse after a change."),
            ("Pass rate", "The percentage of eval cases meeting the success criterion."),
            ("LLM-as-judge", "Using a model to evaluate outputs, usually with calibration and human review."),
        ],
    ),
    (
        "Production terms",
        [
            ("Inference", "Running a trained model to produce an output."),
            ("Latency", "How long a request takes to return a result."),
            ("Throughput", "How many requests a system can handle in a period of time."),
            ("Batching", "Processing multiple requests together for efficiency."),
            ("Streaming", "Sending partial output to the user as it is generated."),
            ("Fallback", "A backup behavior when the preferred path fails."),
        ],
    ),
    (
        "Safety and security terms",
        [
            ("Hallucination", "A generated claim that is unsupported, false, or not grounded in the provided context."),
            ("Prompt injection", "Untrusted input tries to manipulate model instructions or tool use."),
            ("Jailbreak", "A prompt or interaction that tries to bypass safety constraints."),
            ("Guardrail", "A control that detects, blocks, changes, or routes risky behavior."),
            ("PII", "Personally identifiable information."),
            ("Red team", "A structured effort to find failures, vulnerabilities, or unsafe behavior."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Standup: RAG Latency Spike",
        "setting": "Morning standup for a document assistant.",
        "dialogue": [
            ("PM", "Are we still on track for the pilot on Friday?"),
            ("Engineer", "Functionally, yes. The blocker is latency. P95 went from 4.2 seconds to 8.7 after we added reranking."),
            ("ESL learner", "So the answer quality improved, but the serving path is too slow. Is the bottleneck retrieval, reranking, or generation?"),
            ("Engineer", "Mostly reranking. The generator time is stable."),
            ("ESL learner", "Then my proposal is to keep reranking for high-risk queries only and use the faster path for simple FAQ queries. I can bring an ablation by end of day."),
        ],
        "notes": [
            "P95 means the 95th percentile request latency.",
            "Ablation means testing the effect of removing or changing one component.",
        ],
    },
    {
        "title": "2. Design Review: Prompt Fix or Fine-Tune?",
        "setting": "Design review for a customer-support summarizer.",
        "dialogue": [
            ("Researcher", "We should fine-tune. The model keeps missing refund-policy exceptions."),
            ("Product manager", "Would fine-tuning actually solve that, or is the policy changing too often?"),
            ("ESL learner", "I would separate style from facts. If the issue is current policy knowledge, RAG may be safer. If the issue is summary format, a prompt or fine-tune could help."),
            ("Researcher", "Good point. The examples show both problems."),
            ("ESL learner", "Let's run two eval slices: factual policy coverage and format compliance. Then we can choose the adaptation method with evidence."),
        ],
        "notes": [
            "Eval slice means a subset of test cases focused on one behavior.",
            "Adaptation method means the way the team changes model behavior: prompt, retrieval, fine-tuning, or product logic.",
        ],
    },
    {
        "title": "3. Data Meeting: Label Ambiguity",
        "setting": "Annotation guideline meeting for safety classification.",
        "dialogue": [
            ("Data lead", "Annotators disagree on whether this is medical advice or general wellness information."),
            ("ESL learner", "The guideline needs a decision rule. If the answer recommends dosage, diagnosis, or treatment, we label it medical advice. If it gives general prevention information, we label it wellness."),
            ("Reviewer", "What about borderline cases?"),
            ("ESL learner", "We should add a borderline tag and route those to expert review. Otherwise the ground truth will be noisy."),
        ],
        "notes": [
            "Noisy labels are labels that are inconsistent, wrong, or ambiguous.",
            "Ground truth should be as consistent as possible, but it is often a human-created artifact.",
        ],
    },
    {
        "title": "4. Incident Update: Tool-Calling Failure",
        "setting": "Incident channel after an agent booked duplicate appointments.",
        "dialogue": [
            ("Support", "Customers are seeing duplicate calendar events."),
            ("ESL learner", "We found the immediate cause. The model retried the booking tool after a timeout, but the first call had actually succeeded."),
            ("Engineering manager", "Mitigation?"),
            ("ESL learner", "We disabled automatic retries for non-idempotent tool calls and added an idempotency key. We are checking logs for affected users now."),
            ("Support", "What should we tell customers?"),
            ("ESL learner", "Say the system may have created a duplicate event during a retry window. We are removing duplicates and will confirm by email."),
        ],
        "notes": [
            "Non-idempotent means repeating the action can create a different or duplicate result.",
            "An idempotency key helps the system recognize that a retry belongs to the same intended action.",
        ],
    },
    {
        "title": "5. Eval Readout: Better Average, Worse Edge Cases",
        "setting": "Release meeting for a model upgrade.",
        "dialogue": [
            ("PM", "The average score is up. Can we ship?"),
            ("ESL learner", "I recommend a hold. The overall pass rate improved from 86% to 89%, but the legal-disclaimer slice regressed by 11 points."),
            ("Researcher", "Is that statistically meaningful?"),
            ("ESL learner", "The sample is small, so I would not overclaim. But the failures are severe enough to block release until we inspect them."),
            ("PM", "What is the next step?"),
            ("ESL learner", "Human review of the failed slice today, then a targeted prompt or policy fix before we rerun the regression suite."),
        ],
        "notes": [
            "Do not report a metric without explaining the subset, sample size, and severity of failures.",
            "A release can be blocked by a small number of severe failures.",
        ],
    },
    {
        "title": "6. Security Review: Prompt Injection",
        "setting": "Security review for a browsing agent.",
        "dialogue": [
            ("Security engineer", "The page contains text telling the agent to ignore the system instructions."),
            ("ESL learner", "That is prompt injection from untrusted content. The model should treat page text as data, not instructions."),
            ("Developer", "Can we just add a stronger system prompt?"),
            ("ESL learner", "A stronger prompt helps, but it is not enough. We need tool permissions, allowlists, confirmation for risky actions, and logging for suspicious instructions."),
        ],
        "notes": [
            "Prompt injection is a system-design problem, not only a wording problem.",
            "Untrusted content should not be allowed to silently change goals or permissions.",
        ],
    },
    {
        "title": "7. Customer Call: Hallucination Report",
        "setting": "Customer reports that the assistant invented a policy.",
        "dialogue": [
            ("Customer", "The answer cited a policy that does not exist."),
            ("ESL learner", "Thank you. We should call that an unsupported answer, not a confirmed policy source. Can you share the prompt, output, and timestamp?"),
            ("Customer", "Yes. Does this mean the model is unreliable?"),
            ("ESL learner", "It means our grounding failed in this case. We will check whether retrieval missed the right document, whether the prompt allowed unsupported claims, or whether the citation validator failed."),
        ],
        "notes": [
            "Use calm, precise failure language with customers.",
            "Do not blame the model before investigating retrieval, prompt, validation, and UI layers.",
        ],
    },
    {
        "title": "8. Product Planning: Model Choice",
        "setting": "Planning meeting for a high-volume summarization feature.",
        "dialogue": [
            ("Finance", "The larger model is too expensive for this volume."),
            ("ESL learner", "We can test a smaller model with a stricter prompt and a post-generation validator. The question is whether quality remains above the release threshold."),
            ("PM", "What would you measure?"),
            ("ESL learner", "Summary faithfulness, key-point coverage, latency, cost per thousand requests, and human escalation rate."),
            ("Finance", "Can you bring options?"),
            ("ESL learner", "Yes. I will compare three paths: larger model, smaller model with validation, and hybrid routing for complex cases."),
        ],
        "notes": [
            "Hybrid routing sends different requests to different models or paths based on complexity or risk.",
            "Cost discussions should include quality and operational risk, not only token price.",
        ],
    },
    {
        "title": "9. Research Sync: Benchmark vs Product Eval",
        "setting": "Research team proposes a model because it performs well on a public benchmark.",
        "dialogue": [
            ("Researcher", "This checkpoint is strong on the benchmark."),
            ("ESL learner", "That is promising, but the benchmark may not represent our user traffic. We need a product eval before we switch."),
            ("Researcher", "What gap do you expect?"),
            ("ESL learner", "Our users ask mixed-language, document-grounded questions with messy formatting. The public benchmark may not test retrieval grounding or citation quality."),
        ],
        "notes": [
            "Benchmark strength is useful evidence, not a release decision by itself.",
            "Product evals should resemble the actual distribution of user tasks.",
        ],
    },
    {
        "title": "10. Executive Briefing: Risk and Confidence",
        "setting": "Briefing a VP before an AI feature launch.",
        "dialogue": [
            ("VP", "Are we confident enough to launch?"),
            ("ESL learner", "We are confident for the internal beta, not for general availability. The main remaining risks are unsupported answers in long-tail documents and latency during peak usage."),
            ("VP", "What controls are in place?"),
            ("ESL learner", "We have source citations, a refusal path for low-confidence retrieval, human review for escalations, and daily sampling of traces."),
            ("VP", "What would make you stop the beta?"),
            ("ESL learner", "A severe unsupported answer, repeated privacy exposure, or P95 latency above ten seconds for more than one hour."),
        ],
        "notes": [
            "Executives need decision-grade confidence, not all technical detail.",
            "Name launch scope: internal beta, limited pilot, general availability, or rollback.",
        ],
    },
]


PHRASE_BANK = {
    "Clarifying architecture": [
        "Which layer do we think is failing: retrieval, prompt, generation, validation, or UI?",
        "Is this a model behavior issue or an application orchestration issue?",
        "Can we separate the model output from the wrapper logic?",
    ],
    "Discussing data": [
        "What is the source and coverage of this dataset?",
        "Do we have evidence of label noise or annotator disagreement?",
        "Could there be leakage between the training set and the eval set?",
    ],
    "Reporting evals": [
        "The overall metric improved, but one high-risk slice regressed.",
        "The sample size is small, so I would treat this as a warning, not a conclusion.",
        "We should inspect failure examples before making a release decision.",
    ],
    "Explaining RAG": [
        "The model did not have the right context, so the generation step was answering from weak evidence.",
        "The retriever found similar text, but not the text that actually answered the question.",
        "We need better chunking, metadata, or reranking before changing the model.",
    ],
    "Pushing back": [
        "I do not think fine-tuning is the first fix here; the failure looks like retrieval or policy logic.",
        "A benchmark win is not enough unless it transfers to our product eval.",
        "We should not ship until the severe failure slice is understood.",
    ],
    "Customer-safe language": [
        "The answer was unsupported by the available source material.",
        "We are investigating whether the issue came from retrieval, grounding, or validation.",
        "We have paused that workflow while we review the affected traces.",
    ],
}


WORKBOOK_TASKS = [
    "A bug report says, 'The AI is bad.' Rewrite it into a stack-specific issue with observed behavior, expected behavior, evidence, and likely owner.",
    "Explain to a product manager why adding more retrieved context can increase cost and latency without improving answer quality.",
    "Write five clarification questions for a dataset that may have label noise, class imbalance, and privacy restrictions.",
    "Diagnose a RAG answer that cites the wrong document. Separate retrieval, reranking, prompt, generation, and citation validation hypotheses.",
    "Choose between prompt update, RAG, fine-tuning, and product logic for a model that refuses too often in safe cases.",
    "Present an eval result where the average improves but one high-risk slice regresses.",
    "Explain a latency spike caused by reranking and propose two mitigations.",
    "Write a safety escalation for a prompt-injection attempt found in a third-party webpage.",
]


SOURCES = [
    "OpenAI API documentation: embeddings, tools/function calling, structured outputs, evals, and agent eval guidance.",
    "OpenAI Cookbook examples on evaluation and RAG workflows.",
    "Hugging Face documentation: Transformers, Tokenizers, PEFT, Evaluate, and Hub concepts.",
    "Google Machine Learning Glossary and Responsible AI glossary.",
    "Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, NeurIPS 2020.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners who work in AI development or closely adjacent roles: engineers, data scientists, researchers, product managers, technical program managers, QA specialists, solutions engineers, and AI safety or governance staff."
        )
    )
    story.append(
        p(
            "The course is not an introduction to programming or machine learning. It is a professional English course for people who need to participate in AI design reviews, standups, incident discussions, eval readouts, customer escalations, research/product debates, and launch decisions."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "AI teams often compress complex concepts into short jargon: RAG miss, eval slice, context budget, LoRA, P95, grounding failure, non-idempotent tool call, prompt injection, or model regression. Learners need both the vocabulary and the conversational moves around it: clarify, challenge, qualify, summarize, and recommend."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_ai_communication_principles(story: list) -> None:
    story += h1("AI Team Communication Principles")
    story.append(h2("Separate layers before blaming the model"))
    story.append(
        p(
            "In AI product work, 'the model failed' is often too vague. The failure may be in ingestion, chunking, embeddings, retrieval, reranking, prompt construction, tool calling, validation, UI, logging, or release configuration. Strong AI English names the layer, the evidence, the user impact, and the next diagnostic step."
        )
    )
    story.append(h2("Qualify claims"))
    story.append(
        bullets(
            [
                "Use 'the current eval suggests...' rather than 'the model is better' when the evidence is limited.",
                "Use 'this slice regressed' rather than 'the release is bad' when one subset has a problem.",
                "Use 'unsupported answer' or 'grounding failure' when the issue is a false claim without source support.",
                "Use 'we need a product eval' when a public benchmark may not match real user traffic.",
            ]
        )
    )
    story.append(h2("Ask engineering-grade clarification questions"))
    story.append(table([
        ["Weak question", "Stronger AI-development question"],
        ["Why is it wrong?", "Which expected behavior did it violate, and do we have the prompt, output, trace, and retrieved context?"],
        ["Can we fine-tune it?", "Is the problem missing knowledge, wrong style, policy behavior, tool choice, or reasoning under context?"],
        ["Is the model good?", "Which eval set, which metric, which slice, and what are the severe failure examples?"],
        ["Can it be faster?", "Where is the latency: retrieval, reranking, model inference, tool call, validation, or network?"],
    ], [2.45 * 72, 4.55 * 72]))


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a sentence, ask a clarification question about it, and explain its business consequence."
        )
    )
    for title, items in JARGON_GROUPS:
        story.append(h2(title))
        rows = [["Term", "Working meaning"]]
        rows.extend([[term, definition] for term, definition in items])
        story.append(table(rows, [1.55 * 72, 5.45 * 72]))


def add_module_details(story: list) -> None:
    story += h1("Instructor Module Plans")
    for module in MODULES:
        story.append(h2(f"{module['title']} ({module['time']})"))
        story.append(p(module["big_idea"]))
        story.append(h3("Learning objectives"))
        story.append(bullets(module["objectives"]))
        story.append(h3("Core concepts"))
        story.append(bullets(module["concepts"]))
        story.append(h3("Activities"))
        story.append(bullets(module["activities"], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "Push learners toward evidence. When they use a broad term such as better, broken, hallucinated, unsafe, or slow, ask: compared with what, measured how, in which slice, and with what user impact?"
                ],
                "blue",
            )
        )


def add_assessment(story: list) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Pre-course diagnostic"))
    story.append(bullets([
        "Learner explains their current AI project in 90 seconds, including model, data, user, risk, and release stage.",
        "Learner defines ten common AI-development terms and uses five in realistic workplace sentences.",
        "Learner handles a short role-play: a product manager asks whether a model upgrade is ready to ship.",
    ]))
    story.append(h2("Performance rubric"))
    story.append(table([
        ["Skill", "Developing", "Proficient", "Strong"],
        ["Terminology", "Recognizes terms but uses them loosely.", "Uses common terms accurately in context.", "Defines terms, asks precise questions, and notices misuse."],
        ["Technical clarity", "Explains everything as a model issue.", "Names likely stack layer and evidence.", "Separates hypotheses and proposes diagnostic steps."],
        ["Eval communication", "Reports metrics without limitations.", "Reports metric, slice, sample, and failure examples.", "Connects eval evidence to release recommendation."],
        ["Dialogue control", "Waits passively in technical debate.", "Clarifies, summarizes, and pushes back politely.", "Guides mixed technical/product discussion toward decision."],
        ["Risk language", "Overstates or minimizes AI risks.", "Names risk and mitigation clearly.", "Escalates with evidence, owner, and review cadence."],
    ], [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72]))
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a release-readiness meeting for an AI document assistant. The system has improved average answer quality, but one legal-policy slice regressed; latency also increased after reranking. The learner must explain the evidence, ask for missing information, recommend ship/hold/limited beta, and write the follow-up summary."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "AI Development English",
        "Instructor guide for high-level ESL learners working in AI engineering, research, product, safety, and deployment",
        "Audience: instructors, coaches, technical English trainers, and learning partners",
    )
    add_course_opening(story)
    add_ai_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-ai-development-english-instructor-guide.pdf",
        "EFSP AI Development English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "AI Development English",
        "Participant workbook: jargon, dialogues, technical updates, eval readouts, and AI-development discussion practice",
        "Audience: advanced ESL learners working in AI development or AI-adjacent technical roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise in AI-development conversations. The goal is not to use more jargon. The goal is to use the right term, define it when needed, ask useful questions, and explain technical risk in English that your team can act on."
        )
    )
    story.append(h2("Your starting point"))
    story.append(bullets([
        "Which AI-development conversations are hardest for you: standups, design reviews, eval readouts, customer calls, incidents, or executive updates?",
        "Which terms do you understand when reading but avoid when speaking?",
        "When you disagree technically in English, do you become too vague, too quiet, too detailed, or too blunt?",
        "What is one AI failure you recently had to explain?",
    ]))
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("AI Stack Language")
    story.append(
        table([
            ["Layer", "Useful verbs", "Example sentence"],
            ["Data", "ingest, clean, label, split, anonymize", "We need to check whether the eval set leaked into training."],
            ["Retrieval", "chunk, embed, retrieve, rerank, ground", "The retriever found similar chunks but missed the answer-bearing section."],
            ["Prompt", "specify, constrain, format, include, truncate", "The prompt does not specify what to do when evidence is missing."],
            ["Model", "generate, refuse, summarize, classify, infer", "The model follows the format but over-refuses safe requests."],
            ["Serving", "cache, batch, stream, throttle, fallback", "P95 latency increased after we added the reranker."],
            ["Evaluation", "measure, slice, regress, calibrate, inspect", "The average improved, but the high-risk slice regressed."],
        ], [1.15 * 72, 2.15 * 72, 3.7 * 72]))
    story += h1("Practice Pages")
    answer_key: list[dict[str, str]] = []
    for index, module in enumerate(MODULES):
        dialogue = DIALOGUES[index % len(DIALOGUES)]
        story.append(PageBreak())
        story.append(h2(module["title"]))
        story.append(p(module["big_idea"]))
        story.append(h3("What you should be able to do"))
        story.append(bullets(module["objectives"]))
        add_cloze_exercise(story, make_dialogue_cloze(dialogue), answer_key)
    story.append(PageBreak())
    story += h1("Phrase Bank")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-ai-development-english-participant-workbook.pdf",
        "EFSP AI Development English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "AI Development Dialogue Lab",
        "Realistic workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners in AI teams",
        "Audience: instructors, coaches, peer practice groups, and technical English cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(bullets([
        "Use groups of three: speaker, counterpart, observer.",
        "Read the model dialogue once. Then replay it using the same situation but new details from the learner's work.",
        "The observer listens for terminology accuracy, clarification questions, evidence, risk language, and decision clarity.",
        "After each role-play, replay the hardest 30 seconds with a more precise sentence.",
    ], numbered=True))
    story.append(box("Facilitator guardrail", [
        "Do not let learners hide behind jargon. Ask them to define the term in plain English and connect it to a user, metric, risk, or engineering decision."
    ], "amber"))
    answer_key: list[dict[str, str]] = []
    for item in DIALOGUES:
        story.append(PageBreak())
        story.append(Paragraph(esc(item["title"]), S["CardTitle"]))
        story.append(rule())
        story.append(box("Setting", [item["setting"]], "blue"))
        rows = [["Speaker", "Line"]]
        rows.extend([[speaker, line] for speaker, line in item["dialogue"]])
        story.append(table(rows, [1.25 * 72, 5.75 * 72]))
        story.append(h3("Language notes"))
        story.append(bullets(item["notes"]))
        add_cloze_exercise(story, make_dialogue_cloze(item), answer_key, show_context=False)
        story.append(h3("Observer checklist"))
        story.append(bullets([
            "Did the learner use the key terms accurately?",
            "Did the learner ask for evidence rather than making assumptions?",
            "Did the learner distinguish model, data, retrieval, prompt, evaluation, or serving issues?",
            "Did the learner make a clear recommendation or next step?",
        ]))
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-ai-development-dialogue-lab.pdf",
        "EFSP AI Development Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "AI Development Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise AI-development vocabulary and meeting language",
        "Audience: advanced ESL learners in AI engineering, research, product, deployment, safety, and support",
    )
    story += h1("How to Use Jargon Well")
    story.append(bullets([
        "Use the term only when it locates the problem more precisely.",
        "Pair jargon with evidence: metric, trace, log, example, user impact, or source document.",
        "Define the term when speaking to product, support, legal, sales, or executives.",
        "Avoid vague AI blame. Name the layer and the next diagnostic step.",
    ]))
    add_jargon_sections(story)
    story += h1("Common Meeting Moves")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Fast Contrast Pairs")
    story.append(table([
        ["Do not confuse", "Working contrast"],
        ["Prompting vs fine-tuning", "Prompting changes instructions/context; fine-tuning changes model weights."],
        ["RAG vs training", "RAG retrieves external context at inference time; training changes what the model has learned."],
        ["Benchmark vs product eval", "A benchmark is general comparison evidence; a product eval tests your actual use case."],
        ["Hallucination vs retrieval miss", "Hallucination is unsupported output; retrieval miss is failure to fetch needed context."],
        ["Latency vs throughput", "Latency is one request's wait time; throughput is system volume over time."],
        ["Safety vs security", "Safety reduces harmful outputs; security protects systems, data, tools, and permissions."],
    ], [2.25 * 72, 4.75 * 72]))
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-ai-development-jargon-quick-reference.pdf",
        "EFSP AI Development Jargon Field Guide",
        story,
    )


def main() -> None:
    paths = [
        instructor_guide(),
        participant_workbook(),
        dialogue_lab(),
        quick_reference(),
    ]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
