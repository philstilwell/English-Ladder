"""Original fundraising, full-cost, and participant-consent conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The matching pot has a limit",
        skill="Explain matching conditions and reconcile public donations, sponsor support, and cash actually received.",
        setup="Fictional appeal: the sponsor matches eligible public donations dollar for dollar, up to $8,000, during the stated campaign window. At the review, $10,000 in eligible public donations has been received; no refunds or fees apply to this calculation. The sponsor confirms the full $8,000 match is due but has not paid it. New donations remain welcome but cannot attract further match funding under this agreement.",
        cast="Keiko|Fundraising manager\nMalik|Finance officer",
        dialogue="""Keiko|We reached ten thousand in public donations. The homepage still says every gift is doubled. I need to check that message before the next appeal email goes out.
Malik|The [[match funding::Match funding adds a sponsor contribution according to agreed terms; this offer matches eligible public gifts dollar for dollar only within its stated limit and window.]] is dollar for dollar, but the sponsor's commitment stops at eight thousand. We have already reached that limit.
Keiko|So ten thousand from the public does not produce another ten thousand from the sponsor. The maximum combined amount on these facts is eighteen thousand.
Malik|Correct. The [[matching cap::The matching cap is the sponsor's maximum additional contribution, here 8,000; it is not a cap on public gifts or on the combined total.]] limits the sponsor contribution, not what supporters may give. Public donations above the matched amount are still donations.
Keiko|We checked all ten thousand against the agreement: right window, permitted payment types, and no excluded gifts. There are no refunds in this calculation.
Malik|Keep that [[eligibility reconciliation::The eligibility reconciliation checks public transactions against the matching agreement; the exercise explicitly confirms all 10,000 qualifies before applying the 8,000 cap.]] with the sponsor confirmation. It explains why the requested match is eight thousand, not an unexplained adjustment to our public total.
Keiko|For the campaign report, may I say eighteen thousand received? The sponsor has confirmed the full match is due.
Malik|Not yet. Ten thousand is [[cash received::Cash received is money that has actually arrived; the public's 10,000 has been received, but the sponsor's confirmed 8,000 remains unpaid.]]. The other eight thousand is confirmed support awaiting payment. Do not combine those statuses under received.
Keiko|I will separate public gifts received, sponsor match confirmed, and sponsor payment pending. That also tells the team what needs following up.
Malik|Good. Check the agreed payment process and actual timing. A confirmed obligation is useful information, but it does not put the money in today's bank balance.
Keiko|The website needs a new [[donor message::The donor message must reflect the exhausted matching allocation; further gifts remain welcome, but the current agreement cannot support a promise that new gifts will also be doubled.]]. I suggest: Our matching allocation is fully used. Your gift will still support the program, but no further match is available under this appeal.
Malik|That reflects the current position. Update the scheduled email and donation-page banner as well, so the old promise does not continue in a different channel.
Keiko|I will preserve the campaign terms and version history. We should know what supporters saw rather than assume changing the homepage fixes every earlier communication.
Malik|Yes. If someone raises a concern about the promise they relied on, use the appropriate supporter-care process. Do not improvise a refund policy in this reconciliation.
Keiko|There is still time left in the [[campaign window::The campaign window sets the period for the matching offer, but remaining time does not create additional sponsor capacity after the stated cap has been exhausted.]]. We should explain that the pot can run out before the closing date, rather than imply that matching lasts until the last minute.
Malik|Exactly. Time and available match funds are separate conditions. A gift can fall within the dates and still attract no additional match once the allocation is used.
Keiko|The team is pleased with the response. We can celebrate ten thousand from supporters and the eight-thousand confirmed match without describing every gift as doubled.
Malik|That is stronger than inflating the result. Eighteen thousand in combined confirmed support is different from twenty thousand, and it is also different from eighteen thousand in cash received.
Keiko|I will correct the live and queued messages, send the sponsor reconciliation, and use the separate totals in the internal update.
Malik|I will track the payment when it arrives. Our record will then show the receipt against the already confirmed match, rather than count it as a second sponsor contribution.""",
        transfer_title="Reconcile another capped appeal",
        transfer_setup="An appeal matches eligible gifts dollar for dollar up to $5,000. Public gifts of $6,200 have been received and all qualify before the cap. The full sponsor match is confirmed but unpaid. Ignore fees and refunds.",
        transfer="""Fundraiser: The sponsor match is capped at $___ thousand.|5|The agreement limits the additional sponsor contribution to five thousand despite higher eligible public gifts.
Officer: Combined confirmed support is $___ thousand.|11.2|Six thousand two hundred plus the five-thousand match totals eleven thousand two hundred.
Fundraiser: Cash actually received is $___ thousand.|6.2|Only the public gifts have arrived; the confirmed sponsor contribution is still unpaid.
Officer: Further match capacity under this agreement is ___.|zero|The full five-thousand matching allocation has been used, leaving no capacity for additional matches.""",
        reference=("Big Give: why matching availability and eligibility matter; actual scheme terms differ", "https://biggive.org/knowledge-base/unmatched-donation/"),
    ),
    scenario(
        title="The grant budget must cover the work",
        skill="Negotiate a project budget using an explicit cost base, a realistic shared-cost allocation, and a visible funding gap.",
        setup="Fictional private-foundation proposal: direct staff costs $48,000 and materials $12,000. A documented allocation assigns $9,000 of shared support costs to the project, with no duplication. The funder will cover all $60,000 direct costs plus indirect costs limited to 10% of that direct-cost base. No other funding is approved. These are invented private-award terms, not a federal indirect-cost rule.",
        cast="Adele|NGO program director\nHugo|Foundation program officer",
        dialogue="""Adele|Thank you for reviewing the revised budget. We have sixty thousand in direct delivery costs, but the full cost of doing the work is sixty-nine thousand.
Hugo|Our offer covers the [[direct costs::Direct costs in this exercise are 48,000 staff plus 12,000 materials, totaling 60,000; the separately allocated support cost has not been included in that total.]] and a ten-percent indirect allowance. I need to understand how your nine-thousand support allocation relates to that limit.
Adele|It covers this project's documented share of finance, systems, and other shared support. Those amounts are not already charged in the staff or materials lines.
Hugo|Then the [[allocation basis::The allocation basis is the documented method assigning a share of common support to this project; it should reflect the actual method, not a label chosen merely to fit a cap.]] is important. Please show how you assigned the share, rather than moving the difference into a direct-cost line without a proper basis.
Adele|We can show that. Nine thousand on a sixty-thousand direct base is fifteen percent, but our budget starts from the actual allocation, not an assumed universal rate.
Hugo|Under this offer, the [[indirect-cost allowance::The indirect-cost allowance is ten percent of the stipulated 60,000 direct-cost base, or 6,000; the cap does not mean the actual shared costs disappear.]] is six thousand. The grant would therefore be sixty-six thousand, leaving a three-thousand difference against your full cost.
Adele|That is the issue I need us to resolve before agreement. The program cannot function without those services simply because the funding line is capped.
Hugo|I understand. Describe the [[funding gap::The funding gap is 69,000 full cost minus 66,000 offered funding, or 3,000; no other source has been approved in the supplied facts.]] explicitly in the proposal. Do not show a balanced funding plan by assuming unrestricted money that your organization has not approved.
Adele|Could we seek an exception to your limit, or revise the scope and recost the project? Either route needs an actual decision, not a hidden subsidy.
Hugo|You can submit the exception request through our process. I cannot approve it in this conversation, but I can explain what information the decision-maker needs.
Adele|We would provide the allocation, delivery implications, and the alternatives. We should also distinguish [[full-cost recovery::Full-cost recovery means obtaining funding for the direct and appropriately allocated support costs of the work; funding only the direct lines does not achieve it here.]] from merely showing a grant budget that fits your form.
Hugo|Agreed. A compliant application form and a financially viable project are different tests. The request needs to show why the costs are necessary and how the proposed work depends on them.
Adele|If our board considers using unrestricted funds, we will describe that as a deliberate contribution. We will not call it free delivery or leave it outside the decision paper.
Hugo|That would make the [[co-funding::Co-funding is a contribution from another permitted source alongside this grant; here it is only an option and must not be described as secured before authorization.]] visible. Confirm the source's availability and permission before adding it to the committed financing plan.
Adele|And if we reduce the number of sessions, we need a new cost calculation. Shared costs may not fall in the same proportion as the sessions.
Hugo|Exactly. A smaller output target does not automatically remove the full three-thousand gap. Show the revised resources and service consequences rather than applying a blanket reduction.
Adele|For now I will submit the sixty-nine-thousand full-cost budget and identify your sixty-six-thousand offer separately, with the gap unresolved.
Hugo|Please include the exception request and its evidence alongside that comparison. I will route it without representing a review request as an approved award change.
Adele|That gives both organizations a decision they can actually make. We can discuss the trade-off without implying that necessary support costs are waste.
Hugo|Yes. Keep the rate, base, allocation, grant offer, and remaining gap visible. Once a route is approved, the agreement and delivery plan should reflect the same funded scope.""",
        transfer_title="Use the specified direct-cost base",
        transfer_setup="A fictional private award covers $40,000 direct costs plus indirect costs capped at 12.5% of that base. The documented shared-cost allocation is $7,000. No other funding is secured.",
        transfer="""Director: The indirect-cost allowance is $___ thousand.|5|Twelve and a half percent of forty thousand equals five thousand, not 12.5 percent of the eventual total.
Officer: The offered grant totals $___ thousand.|45|Forty thousand direct costs plus five thousand allowed indirect costs gives forty-five thousand.
Director: The project's full cost is $___ thousand.|47|Forty thousand direct costs plus the seven-thousand actual allocation totals forty-seven thousand.
Officer: The unfunded difference is $___ thousand.|2|Forty-seven thousand in full cost minus forty-five thousand offered leaves two thousand without an approved funding source.""",
        reference=("National Council of Nonprofits: understanding overhead and mission costs", "https://www.councilofnonprofits.org/running-nonprofit/administration-and-financial-management/misunderstanding-overhead"),
    ),
    scenario(
        title="Respect the agreed use of a story",
        skill="Clarify a participant's publication choices, stop an unapproved use, and confirm the limits of withdrawal honestly.",
        setup="Fictional adult participant Rina permits a first-name-only written story in a printed annual report, excluding photos, paid ads, and social posts. An unpublished campaign draft wrongly includes her portrait and quote. She still accepts the report use but rejects the campaign. Policy protects these choices without affecting services and requires use controls and documented follow-up.",
        cast="Rina|Program participant\nEva|Communications officer",
        dialogue="""Rina|I saw the draft campaign and recognized my photograph. I agreed to the written annual-report story, not an advertisement. Can you stop this before it goes out?
Eva|Yes. I will pause the campaign draft now. Your [[consent record::The consent record specifies the participant's agreed use and exclusions; it covers a first-name-only written report story and expressly excludes the campaign's portrait and advertising use.]] covers the written report with your first name only. It does not cover the portrait or paid campaign.
Rina|I am still happy with the report story we discussed. I do not want my face used in fundraising, and I do not want that choice to affect my support.
Eva|It will not affect your services under our policy. The [[scope of permission::The scope of permission identifies exactly which material, identity details, audience, and channel are agreed; keeping one permitted use does not authorize the excluded uses.]] stays limited to what you agreed. We will not treat agreement to the report as approval for every other channel.
Rina|Please make sure the team knows this is not a request to change the wording around my picture. I do not want the picture used in that campaign at all.
Eva|Understood. The [[publication hold::A publication hold stops the draft from being released while the misuse is corrected; it is an immediate control, not a promise that an already published item has been recalled.]] applies to the campaign material using your story or image. I will also check whether it is queued anywhere else.
Rina|Thank you. I would like the record to say I still accept the first-name-only written report version. Otherwise another colleague may remove that and miss my actual concern.
Eva|I will record that distinction. Your [[informed choice::Informed choice means deciding with an understanding of the proposed use and the ability to decline it; here Rina accepts a specific report use while refusing different campaign uses.]] includes saying yes to one use and no to another. We should not force those into a single all-or-nothing answer.
Rina|Would removing my surname from the advertisement solve it? Someone suggested that, but my photograph would still be recognizable.
Eva|No. That is not [[anonymization::Anonymization concerns whether a person can be identified; removing a surname while retaining a recognizable portrait does not make Rina anonymous or authorize the excluded use.]]. You would still be identifiable, and it would not change your decision against using the photograph in this campaign.
Rina|I also do not want to be asked again by several different people until I agree. I have made the choice clearly.
Eva|I understand. I will update the permitted-use information for the relevant team and handle the follow-up through one contact. Your decision does not need to be negotiated away.
Rina|What happens if I later want the written story withdrawn too? I know printed reports cannot always be pulled back from everyone who has received one.
Eva|We would explain the [[withdrawal process::The withdrawal process records and acts on a change of permission under applicable policy and law; it must distinguish stopping controllable future uses from recalling copies already distributed.]] and what can actually be stopped or removed. I would not promise to retrieve every distributed print copy or third-party screenshot.
Rina|That is clearer. Today my request is about the unpublished campaign, so please confirm the action on that separately from the report permission.
Eva|I will confirm which draft and queued placements were stopped and what checks remain. I will not say everything has been erased while those checks are unfinished.
Rina|Will you need me to repeat the whole program experience to another team? I would rather not go through the personal details again.
Eva|No additional story details are needed for this correction. We will share the necessary use restrictions through the approved internal route, not circulate your account more widely.
Rina|Please send the confirmation to the contact address already agreed. It should say no portrait, no paid advertisement, and no social post, while retaining the specified report use.
Eva|I will do that and keep the correction traceable. Thank you for pointing it out; making the draft was our error, and receiving services did not authorize that extra publicity.""",
        transfer_title="Respect a narrower publication choice",
        transfer_setup="Participant Leo permits a first-name-only written quote in a member newsletter, but no photograph or social post. A queued social post contains his recognizable portrait. Under the fictional policy, declining publicity does not affect services.",
        transfer="""Officer: The permitted publication is the member ___.|newsletter|The consent covers that specific newsletter, not every communication produced by the organization.
Leo: The permitted material is a written ___.|quote|Leo agrees to the written quote, while the portrait is expressly excluded.
Officer: The queued social post must be ___.|stopped|Its channel and recognizable portrait both exceed the stated permission, so it cannot proceed as drafted.
Leo: Declining this publicity does not affect my ___.|services|The fictional policy explicitly separates service access from willingness to provide publicity permission.""",
        reference=("Core Humanitarian Standard 2024: informed consent, dignity, and safe information handling", "https://www.corehumanitarianstandard.org/_files/ugd/e57c40_f8ca250a7bd04282b4f2e4e810daf5fc.pdf"),
    ),
]
