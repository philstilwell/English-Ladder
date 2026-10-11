"""Original supervision, home-language, and safeguarding conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Count children, confirm names",
        skill="Use a named handover to reconcile a group count without losing continuous supervision.",
        setup="Fictional transition under the center's approved staffing arrangements: twelve children are attending. Eleven are with Maya and Ben; Tomas is with educator Leena after a documented bathroom handover. Leena confirms his location directly. The group stays supervised while the adults check. Tomas later returns through a confirmed handover. These numbers do not establish a staffing ratio.",
        cast="Maya|Early-years educator\nBen|Colleague coordinating the transition",
        dialogue="""Maya|Ben, I have eleven children with the group. Today's attendance list shows twelve. Before we move inside, let us reconcile the names and the separate handover.
Ben|Yes. The [[headcount::The headcount is eleven in the gathered group, while twelve children are attending; the difference must be reconciled through actual named information.]] tells us how many are here, but not whether the right children are here. I will check names against faces while we maintain supervision.
Maya|Tomas is the name not in our gathered group. The handover record says Leena took responsibility for him for the bathroom visit. I need her direct confirmation of his current location.
Ben|Leena has confirmed that Tomas is with her. That is a [[named handover::The handover identifies Tomas and Leena, with direct confirmation of current responsibility; a vague assumption that someone took a child would not establish this.]], not a guess that somebody probably took him inside.
Maya|So eleven with us and one with Leena accounts for the twelve attending. We should not tick Tomas as standing here just to make our column total twelve.
Ben|Exactly. Keep [[location::Tomas is currently with Leena, not in the eleven-child group; the record must preserve where each child actually is.]] and responsibility accurate. No child is unaccounted for on these confirmed facts, but that does not mean every child has already moved with this group.
Maya|While you check the transition record, I will stay positioned with the children as agreed. I will not leave the group to go looking for paperwork.
Ben|Thank you. Our [[supervision plan::The approved supervision plan allocates adult attention and positions during the transition; paperwork and a correct total do not replace that continuous oversight.]] still applies. The counts in this exercise do not tell us which ratios, qualifications, or individual support arrangements our real setting requires.
Maya|I can see each child in our group. I will confirm each name with the actual child rather than rely on a child calling out for someone else.
Ben|That is the [[name-to-face check::A name-to-face check visually matches each child with the relevant name; hearing a reply or reaching the expected total alone is not equivalent.]] we need. Two different children could leave a total unchanged, so the number alone is not a sufficient identity check.
Maya|For the move, we will use our agreed positions and keep track of the children along the route. The check before departure is not the last check of the transition.
Ben|Right. We also verify the group at the destination and follow the center's procedure for checking the area left behind. None of that should leave the children without the required oversight.
Maya|If Leena had not confirmed Tomas's location, we would not simply deduct one and continue because the arithmetic looked tidy.
Ben|Correct. An unresolved discrepancy needs the immediate center response while supervision is maintained. We would not wait until the end of this conversation or ask the children to search independently.
Maya|Leena has now completed the return handover. I have matched Tomas by name and face and confirmed that he has rejoined us. We now have all twelve with the group.
Ben|Record the [[return handover::The return handover establishes that Tomas has actually rejoined the group; the earlier record of Leena taking responsibility did not prove his return.]] as a separate event. Do not prefill it from the earlier bathroom arrangement or assume return because enough time has passed.
Maya|I will update the location record with the actual handover details. The earlier eleven-plus-one arrangement remains part of the sequence, rather than disappearing from the record.
Ben|Good. Our current group count is twelve, and the names have been matched. We still keep watching, listening, and responding; an accurate record does not supervise the children for us.
Maya|My read-back: initially eleven with us, Tomas confirmed with Leena; now twelve reunited through the completed return handover. Current supervision responsibilities remain as agreed.
Ben|Confirmed. We can continue through the actual transition procedure, keeping each child's whereabouts and the receiving adult clear at every change.""",
        transfer_title="A split group is not an assumed absence",
        transfer_setup="Nine children are attending under approved staffing arrangements. Seven are gathered with educators; Leena directly confirms that named children Ava and Ivo are with her in the adjoining care area. Their return handover has not occurred. The group remains supervised.",
        transfer="""Educator: The gathered group contains ___ children.|seven|Seven children are physically in the gathered group; the total attendance of nine is a different count.
Colleague: Leena has confirmed responsibility for ___ children.|two|Ava and Ivo are two named children whose separate location and adult responsibility have been directly confirmed.
Educator: The two groups account for ___ attending children.|nine|Seven gathered children plus the two confirmed with Leena equals all nine attending children.
Colleague: The return handover has not yet ___ .|occurred|The facts confirm the separate care arrangement, not a completed return to the gathered group.""",
        reference=("Office of Head Start: active supervision and name-to-face checks", "https://www.headstart.gov/safety-practices/article/active-supervision"),
    ),
    scenario(
        title="Build on the language at home",
        skill="Agree concrete language-support steps with a family while separating observed English from reported home-language skills.",
        setup="Rafi joined the English-speaking preschool three weeks ago. Parent Samira reports sentences and stories in Urdu at home. Educator Anna heard him say water and more water in English and saw him use gestures. No assessment or diagnosis is supplied. They agree familiar-story support and a check-in next Friday, without withholding access to drinks or help.",
        cast="Samira|Rafi's parent\nAnna|Early-years educator",
        dialogue="""Samira|At home Rafi tells us long stories in Urdu, but I hear he is quiet here. Should we stop using Urdu so he has to practice English?
Anna|Please keep using your [[home language::Urdu is the language Samira reports using with Rafi at home; supporting English does not require abandoning that family language.]] in the conversations and stories you enjoy. We can support English here without asking you to replace the language you share naturally.
Samira|Sometimes he puts an English word into an Urdu sentence. My relative says that means he is confused. I do not know what to tell them.
Anna|Using languages within the same exchange is often called [[code-switching::Code-switching means moving between languages within communication; the mixed-language example alone does not establish confusion or a disorder.]]. That example alone does not show a disorder. We need to understand the whole language picture, not judge one mixed sentence.
Samira|He retells a familiar story and asks his grandmother questions in Urdu. I do not want that part of his communication missed.
Anna|That [[family report::Samira's account supplies information about Urdu use at home; Anna should attribute it to the family rather than record it as her own classroom observation.]] is valuable. I will attribute it to you alongside my classroom observations, not claim I personally heard the Urdu stories.
Samira|What have you actually heard in English? Quiet makes me imagine he has not said anything all day.
Anna|I heard water and more water, and saw him use gestures. Those are specific examples of [[expressive language::Expressive language conveys meaning; Anna's observed English examples should be recorded specifically rather than replaced by the broad label quiet or a claim of fluent sentences.]] in English. They do not describe everything he can understand or communicate across both languages.
Samira|Could I bring the title of a story he already knows? He might have more to show you if he recognizes what is happening.
Anna|Yes. Let us use a familiar story and pictures within our activity plan. You can help us check the names and useful Urdu words rather than leave us guessing their meaning or pronunciation.
Samira|I can show you his words for asking for help too. I want him to communicate his needs before he knows a full English sentence.
Anna|We will accept his available ways of communicating and model useful English. He does not have to produce a sentence to get water or assistance.
Samira|When he says water, should I make him repeat I would like some water, please, every time? I do not want to turn asking for a drink into a test.
Anna|A short [[expansion::An expansion adds language while preserving the child's meaning; modeling more water does not require withholding the drink until Rafi repeats a prescribed sentence.]] can model language without a demand to repeat. For example, more water when that matches his request. Respond to the need rather than withhold the drink for a performance.
Samira|And if you have a real concern about his communication, please tell me specifically. I do not want everything dismissed as just learning English either.
Anna|Agreed. We will discuss the actual observations, including the languages and situations involved, and use the appropriate assessment or specialist route when needed. Learning English neither proves nor rules out a support need.
Samira|What should we each do before the next conversation? I want a manageable plan, not a promise that he will speak by a deadline.
Anna|Share the familiar story and check the useful words with us. I will use the supports and record specific responses. Our [[review date::Next Friday is the agreed check-in date to review observations and supports, not a deadline by which Rafi must achieve a specified level of English.]] is next Friday, not a fluency deadline.
Samira|That sounds manageable. We will keep enjoying Urdu at home, and I will bring the story details. Please tell me what he communicates, not only how much English he speaks.
Anna|I will. At the check-in we can compare the specific examples and adjust support together, without turning three weeks in a new setting into a diagnosis or a prediction.""",
        transfer_title="Keep two sources visible",
        transfer_setup="Parent Luc reports that Amelie tells stories in French at home. Educator Jo has heard help and my turn in English at preschool. They agree to share a familiar song and review the support on Tuesday. No diagnosis or fluency deadline is supplied.",
        transfer="""Parent: My home-language examples are in ___ .|French|Luc reports French storytelling at home; that information should not be relabeled as observed English at preschool.
Educator: My recorded preschool speech examples are in ___ .|English|Jo heard help and my turn in English; those observations are distinct from Luc's home report.
Parent: We will share a familiar ___ .|song|The agreed support is a familiar song, not an invented assessment score or treatment.
Educator: Our check-in is on ___ .|Tuesday|Tuesday is the review date for support, not a promise that Amelie will become fluent by then.""",
        reference=("ASHA: learning more than one language and language-support concerns", "https://www.asha.org/public/speech/development/learning-more-than-one-language/"),
    ),
    scenario(
        title="Preserve the child's words",
        skill="Give an immediate, factual safeguarding report without investigating, promising secrecy, or mistaking an internal handoff for completed external reporting.",
        setup="Fictional England setting: Kit reports harm at 14:05. Educator Nora immediately alerts designated safeguarding lead Ravi, who begins the response. Kit stays supported and supervised. This later record review must not delay protective action or required external notification. Kit's exact words follow below.",
        cast="Nora|Early-years educator\nRavi|Designated safeguarding lead",
        dialogue="""Nora|Following my immediate alert, here is Kit's exact wording at fourteen oh five: I do not want to go home. Someone hurt me.
Ravi|The safeguarding response has begun. Keep that [[verbatim quotation::The quotation preserves Kit's actual words; replacing someone with a guessed person's name would add information Kit did not supply.]] separate from interpretation. Do not replace someone with a guessed name.
Nora|I listened, thanked Kit for telling me, and explained that I needed to tell someone who could help. I did not promise secrecy.
Ravi|That avoids a [[promise of secrecy::A promise of secrecy would conflict with necessary protective information sharing; Nora instead explained that an appropriate person needed to help.]]. Support the child without guaranteeing outcomes. The incomplete account still needs action.
Nora|Kit is supervised by the assigned educator while I report this. I have not left the child alone or asked other children for their versions.
Ravi|Keep the [[safeguarding concern::Kit's words raise a safeguarding concern requiring the actual protective response; an incomplete account is not a reason to postpone action until more proof is collected.]] central. Required external notification and emergency action must not wait for a polished form or this conversation.
Nora|I did not ask, Did your parent do it? Kit had not named anyone. I kept the child's words without trying to establish the full story myself.
Ravi|Avoid [[leading questions::A question suggesting a named person or expected event can shape the account; Nora should not conduct an investigation or supply missing details.]]. Listen, report, and record accurately; do not conduct an investigation or supply missing details yourself.
Nora|Should I call the family myself? I normally share the day's events at collection, but this is not a routine update.
Ravi|Do not independently confront anyone or share details in a way that increases risk. Contact decisions follow the safeguarding response and relevant agency advice.
Nora|For the time fields, fourteen oh five is when the child spoke. I will record the actual alert time and the later note time separately, without inventing a minute I cannot verify.
Ravi|Yes. The [[chronology::Chronology distinguishes when Kit spoke, when Nora alerted Ravi, and when the note was made; those separate events should not be collapsed into one invented timestamp.]] should show the sequence. If a detail is uncertain, identify that uncertainty rather than make the record appear more exact than your knowledge allows.
Nora|I will include the words I used in response and the actions I actually took. I will not turn my note into a diagnosis, a finding of guilt, or an explanation of motive.
Ravi|Exactly. Taking the child seriously and acting promptly does not require you to invent findings. Keep the factual information available to the people responsible for the protective response.
Nora|The room team needs to know the arrangements that affect care and supervision. Does every colleague need the child's full account in the group message?
Ravi|No. Use the approved secure route and share with those who need the information for protection and care. Necessary safeguarding sharing is different from circulating private details widely.
Nora|Your acceptance confirms that you received my concern. It does not, by itself, prove a social-care notification or any other required report has already been completed.
Ravi|Correct. [[External reporting::External reporting involves the required notification beyond the setting; Ravi receiving Nora's internal alert does not itself establish that this separate action has occurred.]] must be carried out promptly under the applicable requirements, with the actual action recorded. No internal process overrides a person's own reporting duties.
Nora|If I remain worried that the concern has not been acted on, I should use the appropriate escalation route rather than assume silence means it has been resolved.
Ravi|Yes. Follow the actual safeguarding and escalation procedures. Keep the child supported, preserve the factual record, and do not delay necessary protective action while waiting for an internal acknowledgement.""",
        transfer_title="Separate the report from its interpretation",
        transfer_setup="At 10:12, Jo hears child Ari say, I am scared to go back. Jo immediately alerts safeguarding lead Leena. No person or place is identified by Ari. External notification is not confirmed in the supplied facts; protective action must not wait for this exercise.",
        transfer="""Educator: The child's statement was heard at ___ .|10:12|10:12 is the stated time of Ari's words, not an invented time for every later action.
Lead: Keep the child's ___ wording in the secure record.|exact|Exact wording preserves I am scared to go back without supplying a person or place Ari did not identify.
Educator: The named lead who received the alert is ___ .|Leena|Leena is the explicitly identified safeguarding lead, distinct from an unnamed external recipient.
Lead: External notification is not yet ___ by these facts.|confirmed|An internal alert establishes receipt within the setting, not completion of a separate required external notification.""",
        reference=("NSPCC: responding to disclosures and recording concerns", "https://learning.nspcc.org.uk/child-abuse-and-neglect/recognising-and-responding-to-abuse"),
    ),
]
