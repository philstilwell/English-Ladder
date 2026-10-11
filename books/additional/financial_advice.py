"""Additional client conversations about income changes, equity, and suspicious requests."""
from books.supplements import scenario

SCENARIOS = [
scenario(
    title='A job loss changes the next six months of planning',
    skill='Acknowledge a stressful change and gather the facts needed to reassess a plan.',
    setup='A client has lost salaried employment. Severance has been offered but its payment date is unconfirmed. Household expenses, accessible savings, insurance arrangements, and possible replacement income need review. No withdrawal or investment change is authorized.',
    cast='Chris|Client\nAmina|Financial adviser',
    dialogue='''
Chris|I lost my job yesterday. Should I stop every contribution and sell investments before things get worse?
Amina|I'm sorry. Let's first establish your immediate [[cash-flow::Cash-flow concerns the timing and amounts of money coming in and going out.]] needs rather than assume all those actions are necessary.
Chris|The company offered severance, so we may be all right for several months.
Amina|Do you have the amount, payment date, and terms in writing?
Chris|The amount is in the letter. The payment date isn't confirmed.
Amina|Then we'll keep it separate from cash already [[available::Available means accessible for the intended use now, unlike a payment with an unconfirmed date.]]. What must be paid before your next expected income?
Chris|The mortgage, household bills, and an insurance payment. I need to check their dates.
Amina|Bring those dates and the current account balances. We'll also identify money already reserved for other commitments.
Chris|I have emergency savings, but using them feels like failing.
Amina|This is a change in circumstances, not a judgment about you. Let's check what your [[reserve::Reserve is money set aside for a defined purpose, including unexpected needs or interruptions.]] can cover and which restrictions apply.
Chris|Should I count a possible consulting project as income?
Amina|Show it as a possibility until its terms and timing are confirmed. We'll keep a separate case without that income.
Chris|I don't want a plan that works only if I find another job immediately.
Amina|Then we'll test a longer [[income gap::Income gap is a period when expected income does not cover the relevant spending needs.]] and identify which assumptions change the result most.
Chris|What about the retirement contributions and investments?
Amina|We'll review them alongside liquidity, costs, taxes, and your longer-term goals before making recommendations.
Chris|Can you also tell me exactly which employer benefits continue?
Amina|We'll coordinate with the benefits contact. The [[coverage::Coverage identifies what protection an insurance or benefit arrangement provides and for how long.]] dates need confirmation from the relevant documents.
Chris|I'll bring the letter, bills, balances, and benefit information. I'm asking for a review, not authorizing a sale today.
Amina|I'll record that. We'll update the [[planning assumptions::Planning assumptions are the inputs used in an illustration; changed employment means earlier inputs may no longer fit.]] and agree the next decisions with you.
''',
    transfer_title='A possible contract is added to the base plan',
    transfer_setup='The client may receive consulting work, but no contract or payment date is confirmed. An assistant has included it as certain income.',
    transfer='''
Adviser: This consulting payment is still ___, correct?|unconfirmed|Unconfirmed preserves the uncertainty about whether and when the payment will occur.
Client: Yes. Please keep a separate case without that ___.|income|Income is the possible inflow being tested, rather than cash already received.
Adviser: We'll compare how long accessible savings cover the stated ___.|expenses|Expenses are the outflows that must be met during the income interruption.
Client: And label the result as an illustration, not a ___.|guarantee|Guarantee would promise an outcome that uncertain future events cannot establish here.
'''),
scenario(
    title='Employer shares are not the same as accessible cash',
    skill='Explain concentration and liquidity without dismissing a client\'s loyalty to an employer.',
    setup='A client holds employer shares in one account and has additional unvested equity awards. Salary also comes from that employer. The adviser has not verified award terms, trading restrictions, tax basis, or the household\'s complete portfolio.',
    cast='Rosa|Client\nEvan|Financial adviser',
    dialogue='''
Rosa|My employer's shares have done well. Why does the planning note call them a risk?
Evan|It refers to [[concentration::Concentration means a large share of relevant wealth or exposure is tied to one investment or source.]], not a prediction that the company will fail.
Rosa|I know the business better than most investors. That makes me more comfortable holding it.
Evan|Your knowledge and confidence matter, but they don't remove price risk. Your salary and part of your wealth also depend on the same company.
Rosa|The award statement shows another large amount. Can we include all of it as money available for the house?
Evan|First separate shares you hold from [[unvested awards::Unvested awards remain subject to vesting conditions; their displayed value is not automatically accessible cash.]]. We need the award conditions and dates.
Rosa|Some vest next year, but I haven't checked whether leaving the company changes them.
Evan|Then we'll review those terms before counting them toward a fixed spending commitment.
Rosa|If the shares are already mine, can I sell whenever I choose?
Evan|We must verify applicable [[trading restrictions::Trading restrictions are limits on transactions arising from relevant laws, employer policies, or award terms.]] and your circumstances. Ownership alone doesn't answer that question.
Rosa|I don't want a recommendation based only on selling everything immediately.
Evan|Nor should we assume that. We'll review the whole portfolio, your goals, the restrictions, and possible approaches before recommending an action.
Rosa|Taxes could affect what I keep from a sale.
Evan|Yes. We'll verify the [[cost basis::Cost basis is the relevant tax basis used when determining gain or loss, which should not be guessed from the current value.]] and obtain appropriate tax input where needed.
Rosa|Would holding several funds automatically eliminate the concentration?
Evan|Not necessarily. The funds may also hold your employer or similar exposures. We need to examine the underlying holdings.
Rosa|So the account labels don't tell us whether the investments are genuinely different.
Evan|Right. [[Diversification::Diversification spreads exposure across investments or risk sources; it does not guarantee against every loss.]] depends on what you own, not simply the number of statements.
Rosa|I'll provide the award documents and all the account details through the secure route.
Evan|Then we can assess [[liquidity::Liquidity concerns the ability to access or convert assets into usable funds when needed.]], concentration, and alternatives. No sale instruction is being taken from this discussion.
''',
    transfer_title='An award value appears in the household cash total',
    transfer_setup='A planning worksheet adds an unvested award to a bank balance and labels the total immediately accessible. The award terms have not been reviewed.',
    transfer='''
Adviser: Keep the award separate from the bank ___ for now.|balance|Balance refers to the actual bank amount, not the displayed value of an award.
Client: The award depends on conditions in its ___ schedule.|vesting|Vesting schedule specifies when or how rights to the award become established.
Adviser: Exactly. We'll review the conditions before treating it as available ___.|funding|Funding means money usable for the planned expense, which is not yet established.
Client: Please mark that part of the worksheet as pending ___.|verification|Verification is the review needed to establish the award's terms and practical availability.
'''),
scenario(
    title='A familiar name sends an unfamiliar transfer request',
    skill='Respond calmly to possible impersonation while preserving the client\'s control.',
    setup='A client receives an urgent message apparently from the adviser, directing a transfer to a new account. The client has not transferred funds. The adviser is reached through the firm\'s established number; the message and destination have not been verified.',
    cast='Noor|Client\nBen|Financial adviser',
    dialogue='''
Noor|I received your message about transferring money today. Why is the destination different from the account we normally use?
Ben|I didn't send that instruction. Thank you for calling through our established number before acting.
Noor|The message uses your name and a photo from the website.
Ben|Those details don't establish [[authenticity::Authenticity means a message genuinely comes from the claimed sender, which a copied name or image does not prove.]]. Have you sent funds or shared any access information?
Noor|No. It asked me to use a link, but I haven't opened it.
Ben|Don't use the message's link or telephone number to verify it. We'll follow our established [[verification::Verification checks identity and instructions through a reliable independent process, not the suspicious message itself.]] route.
Noor|It says I'll miss a special opportunity if I wait an hour.
Ben|That [[urgency::Urgency is pressure to act quickly; in this context it is a warning sign requiring careful verification.]] is another reason to pause. You don't need to make a transfer to settle whether the instruction is genuine.
Noor|Should I forward it to your normal email address?
Ben|Let me give you the firm's approved reporting route using this verified contact. We'll preserve the message without circulating it unnecessarily.
Noor|Will you need my password to inspect the account?
Ben|No. Don't share passwords or security codes. Our review follows the authorized access process.
Noor|Does this mean my account has already been compromised?
Ben|We haven't established that. We'll distinguish the suspicious message from any confirmed account [[activity::Activity means actions involving the account; receipt of a message alone does not prove unauthorized transactions.]].
Noor|I'm embarrassed that I thought it might be real.
Ben|You noticed a difference and checked before acting. That's useful information for the response team, not something to hide.
Noor|Who will keep me informed after I report it?
Ben|I'll confirm the case [[owner::Owner identifies the person responsible for coordinating the case and its follow-up.]] and the next update through our usual contact route.
Noor|I'll report it and wait for verified instructions. No money has moved.
Ben|I'll record that, along with what you've received. Any further [[safeguards::Safeguards are protective measures selected through the authorized review, not improvised instructions from the suspicious sender.]] will follow the firm's response process and your applicable account arrangements.
''',
    transfer_title='The suspicious sender calls back',
    transfer_setup='After the client reports the message, another caller claims to be the adviser and asks for a security code. The caller\'s identity is unverified.',
    transfer='''
Client: The caller wants the security ___ that just arrived.|code|Code is sensitive authentication information and should not be shared with an unverified caller.
Adviser: Don't share it. End that call and use our established contact ___.|number|Number refers to the independently known route, not one supplied by the suspicious caller.
Client: I'll report the new contact as part of the same ___.|case|Case links the related reports for coordinated review without assuming the caller's identity.
Adviser: Good. We'll distinguish reported events from verified ___.|findings|Findings are conclusions supported by review, unlike the unverified claims in the calls.
'''),
]
