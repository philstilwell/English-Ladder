from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, bounded_activity_instruction, make_dialogue_cloze
from generate_efsp_culture_pdfs import (
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
                "Focus: high-level professional English for marketing workplaces, including customer insight, positioning, campaign briefs, content, SEO, paid media, lifecycle marketing, analytics, attribution, compliance, brand risk, and realistic marketing dialogue.",
                "Designed for advanced ESL learners who already work in marketing, product marketing, growth, content, brand, marketing operations, demand generation, social, agency, or marketing-adjacent roles.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: marketing English is persuasion under constraint. Learners need to be clear, creative, evidence-aware, compliance-aware, and commercially useful. This course teaches professional language and judgment, not a guarantee that a campaign, channel, claim, or tactic will work in every market.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use marketing terminology accurately in campaign briefs, creative reviews, channel plans, analytics readouts, content planning, product launches, agency meetings, and executive updates.",
    "Translate vague growth goals into audience, insight, positioning, message, channel, offer, budget, measurement, and decision criteria.",
    "Discuss brand, content, SEO, paid media, lifecycle marketing, marketing operations, attribution, experimentation, and funnel performance in precise professional English.",
    "Push back on unclear briefs, unsupported claims, vanity metrics, weak test design, misleading attribution, poor audience fit, and risky compliance shortcuts.",
    "Participate in realistic marketing dialogues: positioning debates, campaign planning, legal review, sales handoff disputes, agency budget negotiations, social response, and executive performance reviews.",
    "Write clear marketing outputs: creative briefs, message maps, channel rationales, test plans, campaign readouts, MQL definitions, compliance notes, and stakeholder updates.",
]


MODULES = [
    {
        "title": "Module 1. Marketing Strategy: Audience, Insight, Problem, Outcome",
        "time": "90 minutes",
        "big_idea": "Marketing conversations often fail because the team jumps to tactics before agreeing on audience, problem, insight, desired behavior, and business outcome.",
        "objectives": [
            "Distinguish goal, audience, segment, ICP, persona, insight, problem, offer, and channel.",
            "Ask strategy questions that turn vague requests into usable briefs.",
            "Explain the difference between awareness, demand, pipeline, retention, and brand equity goals.",
        ],
        "concepts": [
            "Audience: the group being addressed; segment: a meaningful subset; ICP: the best-fit customer profile; persona: a useful humanized model, not a stereotype.",
            "Insight: a tension or truth about the customer that can guide message, offer, and creative.",
            "Outcome: the measurable behavior or business result the campaign is designed to influence.",
        ],
        "activities": [
            "Brief triage: learners diagnose a vague campaign request and identify missing strategy elements.",
            "Audience split: learners separate buyer, user, influencer, approver, and blocker in a B2B scenario.",
            "Outcome ladder: learners map awareness, engagement, lead, pipeline, revenue, retention, and advocacy goals.",
        ],
        "outputs": [
            "Marketing strategy question bank.",
            "Audience and outcome map.",
            "Brief clarification email.",
        ],
    },
    {
        "title": "Module 2. Positioning, Messaging, Brand Voice, and Proof",
        "time": "90 minutes",
        "big_idea": "Strong marketing language says who the product is for, what problem it solves, why it is different, and what proof supports the claim. Weak marketing language only sounds positive.",
        "objectives": [
            "Use positioning and message architecture terms accurately.",
            "Write value propositions, proof points, CTAs, and objection-handling language.",
            "Distinguish brand voice from vague preference or personal taste.",
        ],
        "concepts": [
            "Positioning: the strategic place a product, service, or brand should occupy in the customer's mind relative to alternatives.",
            "Value proposition: the specific value promised to a specific audience, supported by proof.",
            "Proof point: evidence that makes a claim credible, such as data, customer story, demo, benchmark, or third-party validation.",
        ],
        "activities": [
            "Message rewrite: learners turn generic copy into audience-specific value propositions.",
            "Proof audit: learners identify claims that need evidence before publication.",
            "Creative feedback drill: learners give feedback based on brief, brand voice, audience, and objective instead of taste.",
        ],
        "outputs": [
            "Messaging hierarchy.",
            "Proof point checklist.",
            "Creative feedback phrase bank.",
        ],
    },
    {
        "title": "Module 3. Campaign Briefs, GTM Planning, and Cross-Functional Alignment",
        "time": "90 minutes",
        "big_idea": "Campaigns sit between strategy and execution. Learners need language for goals, target audience, offer, channel mix, timeline, assets, sales handoff, launch tier, dependencies, and decision rights.",
        "objectives": [
            "Write and discuss a campaign brief with enough detail for creative, channel, sales, and analytics teams.",
            "Run alignment conversations among product, sales, legal, customer success, and agency partners.",
            "Use tradeoff language when timeline, budget, quality, compliance, and scope conflict.",
        ],
        "concepts": [
            "GTM plan: coordinated plan for bringing a product, feature, offer, or campaign to market.",
            "Launch tier: level of investment and cross-functional support based on expected business impact.",
            "Sales enablement: materials, messaging, training, and tools that help sales use campaign demand effectively.",
        ],
        "activities": [
            "Brief build: learners create a campaign brief from a messy stakeholder request.",
            "Alignment meeting: learners negotiate scope, timeline, and dependencies across teams.",
            "Launch readiness check: learners decide whether to launch, delay, or reduce scope.",
        ],
        "outputs": [
            "Campaign brief template.",
            "GTM alignment script.",
            "Launch readiness checklist.",
        ],
    },
    {
        "title": "Module 4. Content, SEO, Thought Leadership, and Editorial Judgment",
        "time": "90 minutes",
        "big_idea": "Content marketing is not filling a calendar. Good content connects audience intent, search behavior, expertise, brand credibility, distribution, and conversion path.",
        "objectives": [
            "Discuss SEO, content strategy, editorial calendars, keyword intent, internal linking, metadata, and content quality.",
            "Explain when a piece is meant to educate, rank, convert, nurture, or support sales.",
            "Push back on thin content, keyword stuffing, unsupported claims, and content that lacks a distribution plan.",
        ],
        "concepts": [
            "Search intent: what the searcher likely wants to accomplish, such as learn, compare, buy, or troubleshoot.",
            "Content quality: usefulness, clarity, relevance, credibility, originality, and alignment with audience need.",
            "Distribution: the plan for how the audience will actually find or receive the content.",
        ],
        "activities": [
            "Intent mapping: learners match keywords to audience stage and content format.",
            "SEO/legal review: learners revise a claim-heavy article so it remains useful and compliant.",
            "Editorial critique: learners identify whether a content idea has audience, angle, proof, and distribution.",
        ],
        "outputs": [
            "Content brief.",
            "SEO intent map.",
            "Editorial feedback script.",
        ],
    },
    {
        "title": "Module 5. Paid Media, Performance Marketing, and Attribution",
        "time": "90 minutes",
        "big_idea": "Performance marketing requires disciplined language around targeting, bidding, budget, CPA, CAC, ROAS, incrementality, attribution windows, landing-page quality, and diminishing returns.",
        "objectives": [
            "Use paid media metrics and channel terms accurately.",
            "Explain why platform-reported conversions may not equal business impact.",
            "Discuss budget shifts, testing, audience saturation, creative fatigue, and incrementality.",
        ],
        "concepts": [
            "Attribution: assigning credit to touchpoints, channels, or campaigns for an outcome.",
            "Incrementality: whether marketing caused additional outcomes that would not have happened otherwise.",
            "ROAS vs profit: revenue return on ad spend does not automatically include margin, overhead, retention, or customer quality.",
        ],
        "activities": [
            "Metric debate: learners compare CPA, CAC, ROAS, LTV, payback, and pipeline quality.",
            "Attribution dispute: learners explain why last-click, platform, and CRM numbers disagree.",
            "Budget recommendation: learners decide whether to scale, pause, or test a paid channel.",
        ],
        "outputs": [
            "Paid media readout template.",
            "Attribution explanation script.",
            "Budget recommendation memo.",
        ],
    },
    {
        "title": "Module 6. Lifecycle, CRM, Email, Marketing Ops, and Sales Handoff",
        "time": "90 minutes",
        "big_idea": "Lifecycle marketing depends on definitions and trust. Marketing and sales must agree on lead stages, qualification criteria, nurture logic, consent, deliverability, handoff, and feedback loops.",
        "objectives": [
            "Use lifecycle terms such as lead, MQL, SQL, nurture, segmentation, suppression, deliverability, and UTM accurately.",
            "Discuss email metrics with caveats, including open-rate limitations and click-quality questions.",
            "Negotiate MQL criteria and sales follow-up expectations without turning the meeting into blame.",
        ],
        "concepts": [
            "Lifecycle stage: a shared category for where a contact or account sits in the marketing and sales process.",
            "MQL: marketing-qualified lead, usually based on fit and engagement criteria that sales agrees are worth follow-up.",
            "Deliverability: whether emails reach inboxes and avoid filtering, complaints, and reputation damage.",
        ],
        "activities": [
            "Lead-definition workshop: learners define MQL and SQL for a sample B2B company.",
            "Email readout: learners explain open rate, click rate, unsubscribe rate, and conversion rate with caveats.",
            "Sales handoff role-play: learners respond when sales says the leads are low quality.",
        ],
        "outputs": [
            "Lifecycle definition table.",
            "Email performance readout.",
            "Marketing-sales feedback script.",
        ],
    },
    {
        "title": "Module 7. Analytics, Experimentation, Funnel Reporting, and Executive Readouts",
        "time": "90 minutes",
        "big_idea": "Marketing analytics is not only reporting numbers. Learners must explain source, definition, confidence, attribution, sample size, funnel movement, and what the business should do next.",
        "objectives": [
            "Discuss dashboards, KPIs, funnel conversion, cohort analysis, A/B tests, lift, sample size, and statistical caution.",
            "Separate vanity metrics from decision metrics.",
            "Present executive readouts that connect activity, learning, pipeline, revenue, and next action.",
        ],
        "concepts": [
            "KPI: a metric tied to a strategic objective or decision, not just any available number.",
            "A/B test: a controlled comparison that requires a clear hypothesis, sufficient sample, and decision rule.",
            "Sourced vs influenced pipeline: different ways to describe marketing's relationship to sales opportunities.",
        ],
        "activities": [
            "Dashboard cleanup: learners remove vanity metrics and add decision metrics.",
            "Test readout: learners explain an inconclusive A/B test without pretending there is a winner.",
            "Executive summary: learners write a one-page campaign readout for CFO and CRO audiences.",
        ],
        "outputs": [
            "Analytics readout template.",
            "Experiment design worksheet.",
            "Executive marketing update.",
        ],
    },
    {
        "title": "Module 8. Compliance, Privacy, Claims, Influencers, Brand Safety, and Crisis Response",
        "time": "90 minutes",
        "big_idea": "Marketing teams need persuasive language that stays truthful, substantiated, permission-aware, and brand-safe. Under pressure, the best marketers can protect both growth and trust.",
        "objectives": [
            "Use compliance language for claim substantiation, endorsements, disclosures, consent, opt-out, privacy, and brand safety.",
            "Push back on risky copy, dark patterns, undisclosed incentives, fake urgency, and unsupported testimonials.",
            "Respond to social backlash or reputational risk with calm, approved, audience-aware language.",
        ],
        "concepts": [
            "Claim substantiation: evidence supporting express or implied advertising claims before they are made.",
            "Material connection: a relationship such as payment, employment, or free product that may need clear disclosure in endorsements.",
            "Crisis response: coordinated communication that names known facts, avoids speculation, and protects customers and trust.",
        ],
        "activities": [
            "Compliance review: learners revise ad copy with unsupported claims and unclear disclosures.",
            "Influencer disclosure role-play: learners explain why a creator must disclose compensation or free product.",
            "Social response simulation: learners draft holding statements, internal updates, and escalation notes.",
        ],
        "outputs": [
            "Marketing compliance checklist.",
            "Influencer disclosure script.",
            "Crisis response language bank.",
        ],
    },
]


COURSE_OBJECTIVES = [bounded_activity_instruction(item) for item in COURSE_OBJECTIVES]
for _module in MODULES:
    _module["objectives"] = [bounded_activity_instruction(item) for item in _module["objectives"]]
    _module["activities"] = [bounded_activity_instruction(item) for item in _module["activities"]]


JARGON_GROUPS = [
    (
        "Strategy and customer insight",
        [
            ("Segment", "A meaningful subset of the market based on shared traits, needs, behavior, or value."),
            ("ICP", "Ideal customer profile; the type of account or customer most likely to succeed and create value."),
            ("Persona", "A model of a target user, buyer, or influencer used to guide messaging and content."),
            ("JTBD", "Jobs to be done; what the customer is trying to accomplish in a situation."),
            ("Insight", "A non-obvious customer truth or tension that can guide strategy or creative work."),
            ("TAM", "Total addressable market; the broad revenue opportunity if the product served the whole market."),
            ("Positioning", "How a brand or product should be understood relative to alternatives."),
            ("Value proposition", "Specific value promised to a specific audience, supported by proof."),
        ],
    ),
    (
        "Brand, messaging, and creative",
        [
            ("Brand promise", "The core expectation a brand creates for customers."),
            ("Messaging hierarchy", "Ordered structure of headline, value proposition, pillars, proof points, and CTA."),
            ("Proof point", "Evidence that supports a claim, such as data, customer story, demo, or benchmark."),
            ("Tone of voice", "The brand's consistent style of expression across channels."),
            ("CTA", "Call to action; the requested next step for the audience."),
            ("Creative brief", "Document that guides creative work with audience, objective, insight, message, mandatories, and constraints."),
            ("Campaign idea", "The central creative concept connecting message, audience, and execution."),
            ("Brand consistency", "Maintaining recognizable identity, tone, and promise across touchpoints."),
        ],
    ),
    (
        "GTM and product marketing",
        [
            ("GTM", "Go-to-market plan for launching or growing a product, feature, offer, or market motion."),
            ("Launch tier", "Level of launch investment and support based on business impact and complexity."),
            ("Buyer journey", "Stages a buyer moves through from awareness to evaluation, decision, purchase, and adoption."),
            ("Sales enablement", "Materials and training that help sales communicate value and move opportunities forward."),
            ("Use case", "A specific situation where a customer uses the product to solve a problem."),
            ("Competitive positioning", "How the product is framed against alternatives or status quo."),
            ("Objection handling", "Language and proof used to respond to buyer concerns."),
            ("Win-loss insight", "Learning from deals won or lost to improve positioning, product, or sales execution."),
        ],
    ),
    (
        "Content and SEO",
        [
            ("Search intent", "The likely goal behind a search query."),
            ("SERP", "Search engine results page."),
            ("Keyword", "A word or phrase targeted because people search for it."),
            ("Metadata", "Page title, description, and other information that helps describe content."),
            ("Internal linking", "Links between pages on the same site to help users and search engines navigate."),
            ("Backlink", "A link from another site to your site."),
            ("Canonical", "Signal indicating the preferred version of similar or duplicate pages."),
            ("Content brief", "Instructions for a content asset, including audience, intent, angle, claims, proof, and CTA."),
        ],
    ),
    (
        "Paid media and acquisition",
        [
            ("CPM", "Cost per thousand impressions."),
            ("CPC", "Cost per click."),
            ("CTR", "Click-through rate; clicks divided by impressions."),
            ("CPA", "Cost per acquisition or action, depending on the defined conversion."),
            ("CAC", "Customer acquisition cost; total acquisition cost divided by new customers, depending on definition."),
            ("ROAS", "Return on ad spend; revenue attributed to ads divided by ad spend."),
            ("Retargeting", "Advertising to people who previously interacted with the brand or site."),
            ("Creative fatigue", "Declining performance when the audience has seen the same creative too often."),
        ],
    ),
    (
        "Lifecycle, CRM, and email",
        [
            ("Lead", "A person or account showing some level of interest or fit."),
            ("MQL", "Marketing-qualified lead based on agreed fit and engagement criteria."),
            ("SQL", "Sales-qualified lead accepted or qualified by sales for active pursuit."),
            ("Nurture", "Planned communication that develops interest or readiness over time."),
            ("Segmentation", "Dividing contacts or accounts into groups for relevant communication."),
            ("Deliverability", "Ability of email to reach inboxes and avoid filtering or complaints."),
            ("Open rate", "Percentage of delivered emails recorded as opened, with known measurement limitations."),
            ("Suppression list", "List of contacts excluded from campaigns because of opt-out, risk, irrelevance, or policy."),
        ],
    ),
    (
        "Analytics and measurement",
        [
            ("Attribution", "Assigning credit to marketing touchpoints for an outcome."),
            ("Incrementality", "Additional outcome caused by marketing that would not have happened otherwise."),
            ("Lift test", "Experiment estimating causal impact by comparing exposed and control groups."),
            ("Cohort", "Group of users or customers sharing a time period, behavior, or trait."),
            ("Funnel conversion", "Rate at which people move from one stage to the next."),
            ("Sourced pipeline", "Pipeline credited to marketing as the original source, depending on model."),
            ("Influenced pipeline", "Pipeline where marketing touched the opportunity, depending on model."),
            ("Vanity metric", "Metric that looks impressive but does not support a real decision."),
        ],
    ),
    (
        "Compliance, privacy, and brand safety",
        [
            ("Substantiation", "Evidence supporting express or implied advertising claims before launch."),
            ("Material connection", "Relationship such as payment, employment, or free product that may require disclosure."),
            ("Disclosure", "Clear communication of information needed to avoid misleading the audience."),
            ("Consent", "Permission or legal basis for certain marketing communications or data use."),
            ("Opt-out", "Process allowing people to stop receiving certain communications."),
            ("Dark pattern", "Design that manipulates or misleads users into choices they may not intend."),
            ("Brand safety", "Controls to reduce placement near harmful or unsuitable content."),
            ("Holding statement", "Short approved response used while facts are still being confirmed."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Campaign Brief: 'We Need Awareness'",
        "setting": "A VP asks for a campaign but cannot define the target audience or business outcome.",
        "dialogue": [
            ("VP", "We need a big awareness campaign next month."),
            ("Marketing lead", "Awareness among whom, and what should they do after seeing it?"),
            ("ESL learner", "Before we brief creative, we need to define the audience, insight, message, channel, budget, and measurement. Awareness for executives is different from awareness for end users."),
            ("VP", "Just make noise in the market."),
            ("ESL learner", "We can create visibility, but to spend responsibly we need a specific audience and a signal of success, such as branded search lift, site visits from target accounts, or sales conversations."),
        ],
        "notes": [
            "Good marketers turn vague requests into strategic questions.",
            "Awareness should still have audience, channel, and measurement discipline.",
        ],
    },
    {
        "title": "2. Positioning Debate: Product Feature vs Customer Problem",
        "setting": "Product wants the homepage headline to lead with a technical feature.",
        "dialogue": [
            ("Product manager", "The headline should say 'AI-powered orchestration layer.' That is the feature."),
            ("Content lead", "Customers may not know why that matters."),
            ("ESL learner", "Can we lead with the customer problem and use the feature as proof? The buyer cares about reducing manual handoffs and missed approvals. 'AI-powered orchestration' supports the claim, but it should not be the whole message."),
            ("Product manager", "But competitors say similar things."),
            ("ESL learner", "Then the proof matters even more: workflow examples, time saved, integration depth, and customer evidence."),
        ],
        "notes": [
            "Positioning should connect product capability to customer value.",
            "A feature can be a proof point, not necessarily the main message.",
        ],
    },
    {
        "title": "3. Paid Search: ROAS Looks Good, Sales Quality Is Weak",
        "setting": "Marketing reports strong ad-platform ROAS, but sales says leads are poor.",
        "dialogue": [
            ("Performance marketer", "Google Ads shows a 5.2 ROAS. We should scale budget."),
            ("Sales director", "The leads are not converting to qualified opportunities."),
            ("ESL learner", "Platform ROAS is useful, but we need to reconcile it with CRM revenue, lead quality, and sales-cycle stage. Are these conversions high-intent demo requests or low-intent content downloads?"),
            ("Performance marketer", "Mostly webinar registrations."),
            ("ESL learner", "Then I would not scale yet. Let's separate acquisition cost by conversion type and optimize toward qualified pipeline, not only form fills."),
        ],
        "notes": [
            "ROAS can be misleading if conversion quality is weak.",
            "Marketing and sales need shared definitions for conversion and quality.",
        ],
    },
    {
        "title": "4. Attribution Fight: Last Click vs Influenced Pipeline",
        "setting": "The CFO questions whether marketing really created pipeline.",
        "dialogue": [
            ("CFO", "Sales says they sourced this opportunity. Marketing says it influenced it. Which is true?"),
            ("Marketing ops", "Both can be true under different attribution models."),
            ("ESL learner", "Last-click attribution shows the final touch before conversion. Influenced pipeline shows that marketing touched the account during the buying journey. Neither model alone proves causality."),
            ("CFO", "So what should I trust?"),
            ("ESL learner", "Trust the model for the question it can answer. For budget decisions, we should combine attribution, incrementality tests, sales feedback, and pipeline quality."),
        ],
        "notes": [
            "Attribution explains credit rules, not necessarily causal impact.",
            "Executive language should clarify what the model can and cannot prove.",
        ],
    },
    {
        "title": "5. Creative Review: Taste vs Brief",
        "setting": "A senior stakeholder dislikes a social ad concept because it does not match their personal taste.",
        "dialogue": [
            ("Stakeholder", "I do not like this. It feels too informal."),
            ("Designer", "The brief asked for approachable and direct."),
            ("ESL learner", "Can we evaluate it against the brief? The target audience is first-time managers, the objective is webinar registration, and the tone is meant to reduce intimidation. The question is whether this creative makes the next step feel accessible."),
            ("Stakeholder", "But our brand is premium."),
            ("ESL learner", "Agreed. We can preserve premium through layout and proof, while keeping the language human enough for the audience."),
        ],
        "notes": [
            "Creative feedback should reference audience, brief, objective, and brand system.",
            "Taste language is weaker than criteria-based feedback.",
        ],
    },
    {
        "title": "6. MQL Definition: Marketing and Sales Disagree",
        "setting": "Sales rejects many leads that marketing counts as MQLs.",
        "dialogue": [
            ("Sales manager", "These MQLs are not ready. They downloaded one guide and never replied."),
            ("Demand gen", "They meet the scoring threshold."),
            ("ESL learner", "Then the score may be overweighting engagement and underweighting fit or buying intent. We should define MQL as fit plus behavior, and create a recycle path for leads that are interested but not sales-ready."),
            ("Sales manager", "What changes?"),
            ("ESL learner", "Add firmographic fit, require stronger intent for handoff, and create feedback reasons when sales rejects a lead."),
        ],
        "notes": [
            "Lifecycle definitions need shared ownership.",
            "A rejected lead should produce feedback, not only blame.",
        ],
    },
    {
        "title": "7. SEO and Legal Review: Claim Too Strong",
        "setting": "A content article uses a bold claim that legal says is unsupported.",
        "dialogue": [
            ("SEO manager", "This headline will rank and convert."),
            ("Legal", "The claim 'cuts costs in half' needs substantiation."),
            ("ESL learner", "Can we keep the search intent but adjust the claim? For example, 'ways to reduce support costs' is safer than promising a specific result unless we have evidence that result is typical."),
            ("SEO manager", "Will that weaken the headline?"),
            ("ESL learner", "Maybe, but an unsupported claim creates regulatory and trust risk. We can strengthen the article with a case study, methodology, and clearer qualifiers."),
        ],
        "notes": [
            "SEO pressure does not remove claim-substantiation requirements.",
            "Good revision protects usefulness and compliance.",
        ],
    },
    {
        "title": "8. Email Readout: Open Rate Is Up, Revenue Is Flat",
        "setting": "Lifecycle marketing reviews an email campaign with a high open rate but low revenue impact.",
        "dialogue": [
            ("Lifecycle marketer", "Open rate increased by 12 percent after the new subject line."),
            ("VP Marketing", "Did it produce more revenue?"),
            ("ESL learner", "Open rate is a weak success metric by itself, especially with privacy-related measurement noise. Click rate, conversion, unsubscribe rate, and downstream revenue tell us more about intent."),
            ("Lifecycle marketer", "So was the test a failure?"),
            ("ESL learner", "Not necessarily. The subject line improved attention, but the offer or landing page may not have moved people to action."),
        ],
        "notes": [
            "Email metrics require caveats.",
            "Open rate can be useful, but it should not be the only decision metric.",
        ],
    },
    {
        "title": "9. Influencer Campaign: Disclosure and Authenticity",
        "setting": "A brand manager wants an influencer to make the post feel organic.",
        "dialogue": [
            ("Brand manager", "Can the creator avoid saying it is sponsored? It performs better if it feels natural."),
            ("Social lead", "That creates disclosure risk."),
            ("ESL learner", "If there is payment, free product, or another material connection, the audience needs a clear disclosure. We can still make the content authentic, but not hidden."),
            ("Brand manager", "Will that hurt engagement?"),
            ("ESL learner", "Possibly, but undisclosed sponsorship creates legal and trust risk. Let's optimize the creative, not hide the relationship."),
        ],
        "notes": [
            "Influencer language should separate authenticity from undisclosed advertising.",
            "Material connection disclosure is a key compliance concept.",
        ],
    },
    {
        "title": "10. Agency Budget: More Spend or Better Brief?",
        "setting": "An agency asks for more paid budget after campaign performance stalls.",
        "dialogue": [
            ("Agency", "We are seeing diminishing returns. Additional budget will help us find new audiences."),
            ("Client", "Why should we spend more if performance is worse?"),
            ("ESL learner", "Before increasing spend, let's diagnose the constraint: audience saturation, creative fatigue, landing page conversion, offer relevance, or targeting. More budget may amplify the same problem."),
            ("Agency", "We can test new creative."),
            ("ESL learner", "Good. Please bring a test plan with hypothesis, audience, budget, decision rule, and what we will pause if the test underperforms."),
        ],
        "notes": [
            "Budget requests need diagnosis and decision criteria.",
            "A test plan should include what will change after the result.",
        ],
    },
    {
        "title": "11. A/B Test: Inconclusive Result",
        "setting": "A landing-page test shows a small lift but insufficient sample size.",
        "dialogue": [
            ("Growth marketer", "Variant B is up 6 percent. Let's ship it."),
            ("Analyst", "The sample is too small to call a winner."),
            ("ESL learner", "The direction is promising, but the result is inconclusive. We can extend the test, combine it with qualitative review, or ship only if the implementation cost is low and downside risk is minimal."),
            ("Growth marketer", "I need a decision today."),
            ("ESL learner", "Then frame it as a business decision under uncertainty, not a proven test result."),
        ],
        "notes": [
            "A test readout should protect the difference between signal and proof.",
            "Sometimes the decision is practical, but the evidence label must stay honest.",
        ],
    },
    {
        "title": "12. Social Backlash: Holding Statement",
        "setting": "A campaign receives criticism for appearing insensitive.",
        "dialogue": [
            ("Community manager", "Negative comments are accelerating. Do we delete them?"),
            ("Comms lead", "Not unless they violate policy. We need a response path."),
            ("ESL learner", "First, pause scheduled promotion, capture examples, confirm facts, and align with legal and customer support. The public holding statement should acknowledge concern without speculating or blaming."),
            ("VP", "What can we say now?"),
            ("ESL learner", "We are listening to the feedback, reviewing the campaign, and will share an update when we have confirmed next steps. Internally, we need an owner for response timing and approval."),
        ],
        "notes": [
            "Crisis language should be calm, factual, and coordinated.",
            "Do not delete or respond impulsively without policy and escalation guidance.",
        ],
    },
]


PHRASE_BANK = {
    "Strategy and brief clarification": [
        "Who exactly is the audience, and what behavior do we want to change?",
        "Is the goal awareness, demand capture, pipeline, retention, or brand trust?",
        "What customer insight is the campaign built on?",
        "Before we brief creative, we need the audience, message, offer, channel, budget, and measurement plan.",
    ],
    "Positioning and creative feedback": [
        "Can we lead with the customer problem and use the feature as proof?",
        "The claim is clear, but the proof is not strong enough yet.",
        "Let's evaluate the creative against the brief, not personal taste.",
        "The tone can be more human without losing premium brand cues.",
    ],
    "Paid media and attribution": [
        "Platform ROAS is useful, but we need to reconcile it with CRM revenue and lead quality.",
        "Last-click attribution answers a different question from influenced pipeline.",
        "This metric shows activity, not necessarily incrementality.",
        "Before scaling spend, we should diagnose audience saturation, creative fatigue, and landing-page conversion.",
    ],
    "Lifecycle and sales alignment": [
        "The MQL definition should include both fit and intent.",
        "A rejected lead should create a feedback reason, not only a disagreement.",
        "Open rate improved, but click rate and downstream conversion tell us more about intent.",
        "This nurture path may be too sales-heavy for leads still in the education stage.",
    ],
    "Analytics and testing": [
        "The result is directionally promising, but not conclusive.",
        "We should define the hypothesis, sample size, decision rule, and risk before launch.",
        "That is a vanity metric unless it changes a budget, message, or channel decision.",
        "The dashboard should separate leading indicators from business outcomes.",
    ],
    "Compliance and brand safety": [
        "We need substantiation before making that claim.",
        "If there is a material connection, the disclosure needs to be clear.",
        "The copy creates urgency, but it may overstate scarcity.",
        "Let's pause scheduled promotion while we confirm facts and align on the response.",
    ],
}


WORKBOOK_TASKS = [
    "A VP asks for a broad awareness campaign but cannot name the audience. Write five clarification questions and a brief reply that protects strategy without sounding obstructive.",
    "Product wants to lead with a technical feature. Rewrite the message so it starts with customer pain, then uses the feature as proof.",
    "A campaign brief has audience, timeline, budget, and success metric gaps. Write a brief clarification email to the project owner.",
    "An SEO article uses a strong claim that legal says is unsupported. Rewrite the headline and explain what proof would be needed.",
    "Paid media ROAS looks strong, but sales says leads are low quality. Write a channel readout that separates platform results from business impact.",
    "Sales rejects many MQLs. Write a meeting agenda and opening statement for redefining MQL criteria without blame.",
    "An A/B test shows a small lift but insufficient sample size. Write a test readout that gives a recommendation without overstating evidence.",
    "A social campaign receives criticism for being insensitive. Draft an internal escalation note and a short holding statement.",
]


SOURCES = [
    "Federal Trade Commission advertising and marketing guidance, including claim substantiation, endorsements, reviews, testimonials, and CAN-SPAM guidance.",
    "Google Search Central SEO Starter Guide and Search Essentials for search, content quality, and technical SEO language.",
    "Google Ads attribution documentation for conversion credit and attribution-model vocabulary.",
    "HubSpot lifecycle-stage documentation for lead stage, funnel, and marketing-sales alignment language.",
    "Mailchimp guidance on open rates, click rates, and email reporting limitations.",
    "Platform, CRM, analytics, legal, privacy, and brand guidelines used by the learner's own organization.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in marketing environments: brand marketers, product marketers, content strategists, SEO specialists, performance marketers, lifecycle marketers, marketing operations staff, demand generation teams, social media managers, agency staff, and marketing-adjacent business partners."
        )
    )
    story.append(
        p(
            "The course is not an introduction to advertising. It trains professional English for marketing work: clarifying strategy, writing usable briefs, giving creative feedback, challenging metrics, explaining attribution, aligning with sales, protecting compliance, and communicating campaign performance under uncertainty."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "Marketing teams compress judgment into short phrases: ICP, persona, positioning, proof point, CTA, ROAS, CAC, MQL, SQL, attribution window, incrementality, creative fatigue, search intent, deliverability, claim substantiation, material connection, and holding statement. Learners need the vocabulary and the conversational habits around it: clarify audience, challenge assumptions, connect metrics to decisions, and protect trust."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_marketing_communication_principles(story: list) -> None:
    story += h1("Marketing Communication Principles")
    story.append(h2("Start with audience, not tactic"))
    story.append(
        p(
            "Marketing requests often arrive as tactics: make a video, run ads, send an email, post on social, write a blog. Strong marketing English asks what audience the tactic serves, what problem or desire the audience has, what action should change, and how the team will know whether the work mattered."
        )
    )
    story.append(h2("Use evidence without killing creative work"))
    story.append(
        bullets(
            [
                "Use 'the insight suggests' when connecting customer research to messaging.",
                "Use 'the claim needs substantiation' when creative language makes a factual promise.",
                "Use 'directionally promising but inconclusive' when test evidence is weak.",
                "Use 'platform-reported' when ad data may not match CRM or finance data.",
                "Use 'brand risk' when a tactic may create short-term attention but damage trust.",
            ]
        )
    )
    story.append(h2("Turn vague marketing requests into answerable questions"))
    story.append(
        table(
            [
                ["Vague request", "Stronger marketing question"],
                ["We need awareness.", "Awareness among which audience, for which problem, in which channel, measured by which signal?"],
                ["Make it more premium.", "Which brand cue is missing: tone, proof, layout, imagery, offer, or audience fit?"],
                ["Scale the campaign.", "What is the constraint: audience size, creative fatigue, CPA, conversion rate, or lead quality?"],
                ["Marketing sourced this deal.", "Which attribution model, touchpoints, CRM rules, and sales feedback support that claim?"],
            ],
            [2.15 * 72, 4.85 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask a clarification question, and explain the business consequence. Because marketing terms vary by platform, company, funnel model, and reporting setup, learners should ask which definition is being used."
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
        story.append(bullets([bounded_activity_instruction(activity) for activity in module["activities"]], numbered=True))
        story.append(h3("Learner outputs"))
        story.append(bullets(module["outputs"]))
        story.append(
            box(
                "Facilitator note",
                [
                    "When learners jump to a tactic or metric, ask: who is the audience, what insight supports it, what proof is needed, which channel is appropriate, what decision will the metric inform, and what compliance or brand risk exists?"
                ],
                "blue",
            )
        )


def add_assessment(story: list) -> None:
    story += h1("Assessment and Coaching")
    story.append(h2("Pre-course diagnostic"))
    story.append(
        bullets(
            [
                "Learner explains their marketing role in 90 seconds, including audience, channels, metrics, stakeholders, and highest-risk conversations.",
                "Learner defines twelve marketing terms and uses six in realistic workplace sentences.",
                "Learner handles a short role-play: a senior stakeholder asks for a campaign with unclear audience and unrealistic timeline.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses marketing terms accurately in context.", "Defines terms, asks which reporting model applies, and adjusts by audience."],
                ["Strategic clarity", "Accepts vague requests as given.", "Clarifies audience, objective, insight, channel, and success metric.", "Turns ambiguity into a brief that teams can execute."],
                ["Measurement", "Reports metrics without caveats.", "Explains source, definition, confidence, and business impact.", "Connects measurement to budget, message, channel, or sales action."],
                ["Cross-functional communication", "Gets pulled into taste or blame debates.", "Uses brief, criteria, and shared definitions.", "Guides stakeholders toward decision and accountability."],
                ["Compliance and trust", "Misses unsupported claims or risky disclosures.", "Flags claim, consent, endorsement, and brand-safety issues.", "Protects growth and trust under pressure with calm escalation."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a campaign planning and performance review for a product launch. The brief is vague, product wants feature-heavy messaging, legal rejects a claim, paid media shows strong platform ROAS but weak CRM quality, sales rejects MQLs, and social feedback turns negative. The learner must clarify strategy, revise messaging, explain measurement, align stakeholders, and write an executive update."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "Marketing English",
        "Instructor guide for high-level ESL learners working in brand, product marketing, growth, content, SEO, lifecycle, marketing ops, demand generation, social, and agency roles",
        "Audience: instructors, marketing English coaches, corporate learning teams, agency trainers, and advanced professional English programs",
    )
    add_course_opening(story)
    add_marketing_communication_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-marketing-english-instructor-guide.pdf",
        "EFSP Marketing English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "Marketing English",
        "Participant workbook: strategy, messaging, briefs, SEO, paid media, lifecycle, analytics, compliance, and marketing dialogue practice",
        "Audience: advanced ESL learners working in marketing, product marketing, growth, content, SEO, lifecycle, demand generation, social, agency, and related roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise and useful in marketing conversations. The goal is not to use more buzzwords. The goal is to clarify audience, insight, message, channel, proof, measurement, and risk so that creative and commercial decisions can move forward."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which marketing conversations are hardest for you: briefs, creative reviews, analytics readouts, sales alignment, legal review, agency calls, or executive updates?",
                "Which marketing terms do you understand when reading but avoid when speaking?",
                "When someone asks for a campaign without enough context, do you become too agreeable, too technical, too indirect, or too blunt?",
                "What is one recent marketing meeting you wish you had handled more clearly?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("Marketing Workstream Language")
    story.append(
        table(
            [
                ["Area", "Useful verbs", "Example sentence"],
                ["Strategy", "segment, target, prioritize, position, validate", "We need to validate the audience before choosing channels."],
                ["Messaging", "frame, claim, substantiate, differentiate, simplify", "The feature is useful, but the message should start with the buyer pain."],
                ["Campaigns", "brief, launch, coordinate, sequence, localize", "The campaign can launch only after creative, legal, and sales enablement are ready."],
                ["Channels", "optimize, bid, rank, nurture, retarget", "The channel is efficient for form fills but weak for qualified pipeline."],
                ["Analytics", "attribute, compare, test, segment, reconcile", "The platform data and CRM data answer different questions."],
                ["Risk", "review, disclose, pause, escalate, approve", "The claim needs substantiation before publication."],
            ],
            [1.15 * 72, 2.15 * 72, 3.7 * 72],
        )
    )
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
        "efsp-marketing-english-participant-workbook.pdf",
        "EFSP Marketing English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "Marketing Dialogue Lab",
        "Realistic marketing-workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners",
        "Audience: instructors, marketing English coaches, marketing teams, agency teams, and peer practice cohorts",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: marketing speaker, stakeholder, observer.",
                "Read the model dialogue once. Then replay it with a different audience, channel, metric, risk, or stakeholder pressure.",
                "The observer listens for audience clarity, strategic questions, evidence, metric caveats, compliance awareness, and decision language.",
                "After each role-play, replay the hardest 30 seconds with a more precise marketing sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners hide behind buzzwords. Ask them to define the audience, decision, metric source, proof, channel rationale, and compliance or brand risk."
            ],
            "amber",
        )
    )
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
        story.append(
            bullets(
                [
                    "Did the learner clarify audience, goal, and decision before discussing tactics?",
                    "Did the learner use marketing terms accurately and define metrics when needed?",
                    "Did the learner connect creative, channel, or budget advice to evidence?",
                    "Did the learner identify compliance, brand, data, or trust risk when relevant?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-marketing-dialogue-lab.pdf",
        "EFSP Marketing Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "Marketing Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise marketing vocabulary and meeting language",
        "Audience: advanced ESL learners in brand, product marketing, growth, content, SEO, lifecycle, demand generation, marketing operations, social, and agency roles",
    )
    story += h1("How to Use Marketing Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it makes the marketing decision more precise.",
                "Pair jargon with audience, objective, channel, metric definition, proof, and risk.",
                "Define metrics across systems; platform, analytics, CRM, and finance reports may not count the same way.",
                "Avoid unsupported claims, hidden endorsements, manipulative urgency, and performance overstatement.",
            ]
        )
    )
    add_jargon_sections(story)
    story += h1("Common Meeting Moves")
    for title, phrases in PHRASE_BANK.items():
        story.append(h2(title))
        story.append(bullets(phrases))
    story += h1("Fast Contrast Pairs")
    story.append(
        table(
            [
                ["Do not confuse", "Working contrast"],
                ["Audience vs persona", "Audience is the real group addressed; persona is a model used to guide decisions."],
                ["Feature vs benefit", "Feature is what the product has or does; benefit is why that matters to the customer."],
                ["Claim vs proof", "Claim is what marketing says; proof is the evidence that supports it."],
                ["Traffic vs qualified demand", "Traffic is visits; qualified demand shows fit, intent, and potential business value."],
                ["ROAS vs profit", "ROAS uses attributed revenue over ad spend; profit considers margin, cost, retention, and quality."],
                ["Attribution vs incrementality", "Attribution assigns credit; incrementality asks whether marketing caused additional outcomes."],
                ["Open rate vs engagement", "Open rate records opens with limitations; engagement requires clicks, replies, conversions, or meaningful action."],
                ["Creative fatigue vs bad strategy", "Fatigue means performance declines from repeated exposure; bad strategy means the audience, offer, or message may be wrong."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-marketing-jargon-quick-reference.pdf",
        "EFSP Marketing Jargon Field Guide",
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
