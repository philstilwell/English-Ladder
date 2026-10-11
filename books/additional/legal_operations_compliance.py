"""Original legal billing, preservation, and notice-administration cases."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Review the bill line by line",
        skill="Challenge a billing discrepancy precisely while separating proposed adjustments from payment authorization.",
        setup="Fictional engagement: associate $300/hour, partner $500/hour. Invoice: associate 12 hours at $325; partner four hours at $500, including a disputed one-hour duplicate; $150 allowed expense. No tax or discount. Counsel confirms the duplicate should be removed. Legal operations checks the correction; the matter owner approves payment.",
        cast="Amal|Legal operations analyst\nTheo|Law firm billing coordinator",
        dialogue="""Amal|I have two queries on the matter's invoice: the associate rate and a partner entry that appears twice. Can we reconcile them before the matter owner approves payment?
Theo|Certainly. Let us use the [[engagement terms::The agreed engagement terms set the associate rate at 300 dollars and partner rate at 500; the invoice cannot replace those terms with an unapproved rate.]] as the starting point. The associate rate is three hundred per hour, although this invoice used three hundred twenty-five.
Amal|Twelve hours at the billed rate gives three thousand nine hundred. At the agreed rate, the same twelve hours comes to three thousand six hundred.
Theo|That creates a [[rate adjustment::Twelve hours multiplied by the 25-dollar rate difference produces a 300-dollar reduction; the hours themselves are unchanged.]] of three hundred dollars. I will correct the rate, not reduce the recorded hours to force the same total.
Amal|The partner line totals two thousand for four hours. One hour appears duplicated, but I do not want to delete a genuine separate task on appearance alone.
Theo|Counsel has checked the underlying entries and confirmed a [[duplicate entry::Counsel has confirmed that one of the four partner hours is duplicated, supporting a separate 500-dollar removal rather than an assumption based only on similar text.]]. Removing that one hour leaves three hours at five hundred, or fifteen hundred.
Amal|So the two corrections are separate: three hundred for the associate rate and five hundred for the duplicate. The allowed expense is still one hundred fifty.
Theo|Correct. The [[revised invoice::The revised invoice is 3,600 associate fees plus 1,500 partner fees plus 150 expense, totaling 5,250, with no tax or discount in the exercise.]] should total five thousand two hundred fifty. That is eight hundred less than the original six thousand fifty, without changing the allowed expense.
Amal|Please retain the original invoice number and identify how the replacement relates to it. Accounts payable must not treat both versions as separate bills to pay.
Theo|I will follow our correction process and reference the superseded version. The corrected lines will show what changed; we will not simply send an unexplained lower total.
Amal|One description combines a call, document review, and drafting into a single time entry. Our billing guidelines require separate tasks. Can counsel supply the actual breakdown?
Theo|I will query that [[block billing::Block billing combines multiple tasks in one time entry; this fictional client's guidelines require a factual task breakdown, not invented allocations to make the entry pass review.]]. We should obtain the recorded detail, not invent equal fractions for each task because the total happens to reconcile.
Amal|That clarification may affect review status. The arithmetic correction alone does not prove that every service description meets the client's billing requirements.
Theo|Understood. We will keep the narrative query open and distinguish the corrected amount from a fully cleared invoice. Any further adjustment needs its own supported basis.
Amal|For the reporting dashboard, I will label the eight hundred as a proposed invoice reduction until the corrected bill is accepted. It is not money already recovered.
Theo|And the [[matter owner::The matter owner holds payment-approval responsibility in the supplied workflow; legal operations checking arithmetic does not itself authorize payment.]] still needs to approve payment. Your review documents the discrepancies and reconciliation, rather than replacing that approval.
Amal|Exactly. I will send the rate comparison, confirmed duplicate, expense support, and outstanding narrative question together so the reviewer sees the whole position.
Theo|I will return the linked corrected invoice and response through the agreed billing channel. We can then reconcile the payable record without losing the original history.
Amal|Our read-back is five thousand two hundred fifty on the stated corrections, with the task breakdown still being clarified and payment approval outstanding.
Theo|Agreed. I will not mark it paid or fully approved merely because the corrected arithmetic now matches the engagement rates.""",
        transfer_title="Separate rate and duplicate corrections",
        transfer_setup="Agreed rate $200/hour. An invoice bills ten hours at $220, including two confirmed duplicate hours, plus an allowed $100 expense. No tax or discount. Correct the rate on all ten hours first, then remove duplicates at the agreed rate. Payment approval is outstanding.",
        transfer="""Analyst: The rate correction alone reduces the bill by $___ .|200|Ten hours times the twenty-dollar rate difference equals two hundred dollars before duplicate hours are removed.
Coordinator: Removing the two duplicates at the agreed rate reduces it by another $___ .|400|Two hours at the corrected two-hundred-dollar rate equal four hundred, avoiding double-counting the rate adjustment.
Analyst: Eight valid hours plus the expense produce a corrected total of $___ .|1700|Eight times two hundred equals sixteen hundred, plus the allowed hundred-dollar expense gives seventeen hundred.
Coordinator: Correct arithmetic does not establish payment ___ .|approval|The facts leave payment approval outstanding even though the corrected rate and hours can be reconciled.""",
        reference=("CLOC: financial management, firm management, and practice operations", "https://cloc.org/cloc-core-12/"),
    ),
    scenario(
        title="Preserve before deletion",
        skill="Coordinate a scoped legal hold across people and systems without confusing acknowledgment, preservation, and disclosure.",
        setup="Fictional hold H27: preserve named custodians' relevant Project Cedar email, chat, and shared files from 1 March onward, including new material. Chat deletion is tonight; one custodian leaves tomorrow. Counsel owns scope and release; IT implements and verifies protection. Some acknowledgments are missing.",
        cast="Leah|Legal operations coordinator\nSam|IT records administrator",
        dialogue="""Leah|Counsel issued H27 this morning. Project Cedar chat is due for routine deletion tonight, and one named employee leaves tomorrow. Which preservation steps are actually in place?
Sam|The email hold is active, but chat and shared files are still being configured. I will not mark [[preservation::Preservation means protecting the relevant information from loss or alteration; an active email hold alone does not establish that chat and shared files are protected.]] complete across all three sources just because the first system is covered.
Leah|The notice covers relevant material from March first onward, including new records. It is not a snapshot ending today.
Sam|I need to confirm the [[custodian list::The custodian list identifies the people whose relevant records fall within the supplied hold; names and accounts must be matched rather than assuming one mailbox covers every source.]] against actual accounts and locations. The departing employee's chat identity differs from the email username, so that mapping needs attention.
Leah|Please contact the responsible administrators now. Confirm scoped protection before tonight's deletion and tomorrow's departure processes run.
Sam|I will coordinate the necessary [[deletion suspension::Deletion suspension stops the relevant scheduled removal within the hold's scope; sending a notice or opening a ticket is not evidence that the technical protection is effective.]] and verify its effect. I will report any source we cannot protect in time to counsel promptly, not leave an unanswered ticket overnight.
Leah|The departure workflow normally removes access and later deletes the account. We still need to protect records without leaving the employee authorized to use company systems.
Sam|Those are separate settings. We can arrange authorized access removal while retaining the scoped records. I will check the platform-specific behavior instead of assuming disabling an account preserves everything.
Leah|Three acknowledgments are missing. The dashboard colors the whole matter green because most are back.
Sam|That is misleading. An [[acknowledgment::An acknowledgment confirms receipt or the specified response to a hold notice; it does not prove technical preservation or resolve missing responses from other custodians.]] is one part of follow-through. It is not a substitute for system verification or a reason to ignore the three outstanding responses.
Leah|I will follow up through the approved route and tell counsel about any missing person or source. Employees should identify relevant locations without collecting from accounts they cannot access.
Sam|Yes. The [[scope::The scope defines the relevant subject, custodians, dates, and sources; uncertainty about another location requires clarification rather than unauthorized collection or silent exclusion.]] comes from counsel. If we discover a relevant shared workspace outside the current mapping, we should raise it rather than silently exclude it.
Leah|Can you send the preserved material directly to the other side once the hold is confirmed? That would save another handoff later.
Sam|No. Preserving information does not authorize its disclosure. Collection, relevance and privilege review, and any production must follow the legal team's instructions and permissions.
Leah|Understood. For today's status, I need each source, responsible administrator, action taken, verification result, and any unresolved limitation, with actual timestamps.
Sam|I will provide that record and distinguish a requested setting change from a verified one. If something was already deleted, I will state that fact and escalate recovery options without promising restoration.
Leah|The business expects settlement next week. Should we schedule the hold to disappear automatically on Friday if nobody contacts us?
Sam|No. We need an authorized [[hold release::A hold release requires the authorized legal decision in this scenario; an expected settlement date does not end preservation or override another applicable hold or retention duty.]]. Counsel must confirm release, and we must check for other holds or retention requirements before resuming the relevant deletion process.
Leah|Then the immediate priorities are chat protection, the departing custodian's records, the remaining sources, and the missing acknowledgments, all kept separately visible.
Sam|Agreed. I will send verified status and unresolved risks today. The record will show what is protected, not merely what we have asked people to do.""",
        transfer_title="An account can close while records remain",
        transfer_setup="Hold H44 covers relevant email and chat for employee Jo. Jo leaves tomorrow. Email preservation is verified; chat protection is requested but unverified. Counsel has not released H44. Jo's access must end through the authorized departure process.",
        transfer="""Coordinator: Verified preservation currently covers ___ only.|email|The stated evidence confirms email preservation, while the requested chat setting has not yet been verified.
Administrator: The unresolved source requiring urgent follow-through is ___ .|chat|Chat is within the hold but lacks verified protection, so the pending request is not sufficient evidence of completion.
Coordinator: Ending Jo's access is distinct from deleting Jo's ___ .|records|Access removal concerns authorization to use systems; relevant records remain subject to the active preservation instructions.
Administrator: The departure itself does not authorize a hold ___ .|release|Counsel has not released H44, and an employee's departure does not end the stated preservation requirement.""",
        reference=("Federal Rule of Civil Procedure 37(e): U.S. background on lost electronically stored information", "https://www.law.cornell.edu/rules/frcp/rule_37"),
    ),
    scenario(
        title="Send the right notice",
        skill="Distinguish non-renewal, termination, dispatch, and receipt under an explicit notice clause.",
        setup="Fictional contract: term ends 30 November, otherwise renews one year. Non-renewal must reach notices@vendor.example by 31 October, 17:00 UTC. Internal signatory approval is required. A salesperson received an informal email yesterday; today is 29 October. These are supplied terms, not general legal rules.",
        cast="Ravi|Business contract owner\nCelia|Contract administrator",
        dialogue="""Ravi|I emailed our sales contact yesterday: no additional year. Can you close the reminder, or is something else needed?
Celia|Check the [[notice clause::The notice clause specifies receipt at the designated address by 31 October at 17:00 UTC; an informal email to a salesperson is not confirmed compliance with those supplied terms.]]. The contract specifies a different recipient and a receipt deadline. Your sales email is not confirmed compliant notice.
Ravi|We want service through November thirtieth, but no additional year. I am not asking to stop service this week.
Celia|That is [[non-renewal::Non-renewal prevents the next contract term under the applicable terms, whereas ending service before the current term expires would be a different termination question.]], not immediate termination. The wording should preserve the current term through November without requesting an earlier stop.
Ravi|My department approved the decision. The checklist also requires the authorized signatory's approval, which I do not yet have.
Celia|That [[approval requirement::The supplied internal approval requirement remains unmet; the department's decision does not by itself establish the authorized signatory's approval.]] remains outstanding. Contact the signatory through the urgent route today; department approval does not cover every step.
Ravi|The notice must reach notices at vendor dot example by October thirty-first at seventeen hundred UTC. Should I enter the end of November as the deadline instead?
Celia|No. The [[notice deadline::The notice deadline is 31 October at 17:00 UTC, distinct from the current term ending on 30 November; using the term end would miss the supplied notice requirement.]] is in October. The term end belongs in a separate field. One controls the notice action; the other identifies when this service period finishes.
Ravi|The account manager said they would forward my message. I have no confirmation that it reached the specified mailbox.
Celia|Keep the forwarding assurance as part of the history, not proof of [[receipt::Receipt concerns the notice reaching the specified recipient under the clause; an intention to forward or a sent-message record alone does not establish that event.]]. We need the approved notice delivered through the specified route and evidence relevant to the actual receipt condition.
Ravi|What should the formal message identify so the vendor does not apply it to another agreement? We have two services with similar product names.
Celia|Use the correct contracting entity, agreement identifier, intended non-renewal, and current term end, with the approved wording and signatory process. Preserve the final version and its supporting record.
Ravi|I will ask the signatory today and prepare the approved notice. If the email bounces, we should not let the reminder close just because our system says sent.
Celia|Correct. Escalate a failed delivery immediately. Any alternative method or disputed interpretation needs legal review; we should not invent a replacement route and call it contractually equivalent.
Ravi|Once the vendor acknowledges the notice, can I describe this as cancellation with nothing more to pay? Finance is asking about the remaining service charges.
Celia|Not on that basis alone. [[Remaining obligations::Remaining obligations can include the current term's agreed charges and other contractual duties; a non-renewal notice does not automatically waive them or establish a final settlement.]] need their own review. Non-renewal is not automatically a fee waiver or confirmation that every account balance is settled.
Ravi|Then the handoff to finance should say current term continues to November thirtieth, with the notice and final charges tracked separately.
Celia|Yes. Keep service continuity, notice status, and any exit duties visible. The business decision and operational offboarding plan are related, but neither substitutes for the notice evidence.
Ravi|I will leave the task open until we have the required approval, final message, delivery record, and confirmation appropriate to the receipt clause.
Celia|Good. We can then record the supported status and archive the evidence without rewriting yesterday's informal email as something it has not been shown to accomplish.""",
        transfer_title="Do not substitute the term-end date",
        transfer_setup="Fictional terms: current service ends 31 August. Non-renewal notice must reach renewals@provider.example by 31 July at 12:00 UTC. Approved notice sent to that address bounced. No alternative delivery method has been confirmed. The business wants service through August.",
        transfer="""Owner: The intended action is ___, not immediate termination.|non-renewal|The business wants the current term to continue through August but does not want the following term to begin.
Administrator: The specified notice deadline is 31 July at ___ UTC.|12:00|The notice clause expressly sets noon UTC on 31 July, not the later service-end date.
Owner: The bounced email does not establish ___ .|receipt|A failed delivery does not show the notice reached the contractually specified recipient, even though a send attempt exists.
Administrator: We must urgently resolve delivery rather than close the ___ .|reminder|The receipt requirement remains unfulfilled on the supplied facts, so the task needs urgent follow-through rather than administrative closure.""",
        reference=("CLOC: practice operations and information governance", "https://cloc.org/cloc-core-12/"),
    ),
]
