"""Original payroll-query, internal-mobility, and workforce-reporting conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The time record shows six hours the payslip does not',
        skill='Acknowledge a pay discrepancy, explain a bounded calculation, and arrange prompt follow-up.',
        setup='In this simplified US case, an employee covered by federal overtime rules and not exempt from them worked 46 hours in one workweek. Payroll has confirmed a $24 regular hourly rate with no other pay elements affecting it. Only 40 hours at $24 were paid. The employee and HR adviser discuss the missing gross amount; applicable correction deadlines and any additional requirements still need payroll review.',
        cast='Sam|Employee\nAda|HR adviser',
        dialogue='''Sam|My time record shows forty-six hours, but the payslip only includes forty. I need to know whether the extra six hours have been lost.
Ada|I am sorry this has happened. Let us link the approved [[time record::The time record provides the hours actually worked in the relevant workweek and is compared with the payroll entry.]] to this payslip and raise the discrepancy with payroll promptly.
Sam|My supervisor says the extra work was not approved in advance. Does that mean those hours can simply disappear from the record?
Ada|No. Record the hours actually worked. A question about prior authorization must not be used to erase time or withhold pay that is due.
Sam|Payroll confirmed my regular rate is twenty-four dollars. How much is missing in this example before taxes and other deductions?
Ada|For the stated case, the [[overtime rate::The overtime rate in this case is one and one-half times the confirmed $24 regular rate, or $36 per overtime hour.]] is thirty-six dollars. Six unpaid overtime hours therefore account for two hundred sixteen dollars of gross pay.
Sam|So the full gross amount for that workweek should be nine hundred sixty plus two hundred sixteen, or eleven hundred seventy-six dollars?
Ada|Yes, on the facts supplied. [[Gross pay::Gross pay is the amount before deductions; the calculated $1,176 is not a promise of the same amount being deposited.]] is different from the amount deposited after the applicable deductions.
Sam|Could someone just call the difference a discretionary bonus? I would like the correction to show which hours were missing.
Ada|The [[pay adjustment::The pay adjustment should accurately correct the missing earnings and their basis, rather than disguise them under an unrelated payment label.]] needs the correct earnings description and record. Payroll should preserve the connection to this workweek and the original error.
Sam|When will I receive it? I have a bill due, and waiting until the next normal payday could be difficult.
Ada|I will flag the urgency and ask payroll for the required correction timing, including any [[off-cycle payment::An off-cycle payment is processed outside the normal payroll run; its availability and timing need confirmation rather than a casual promise.]] arrangement. I cannot promise a payment date before they confirm it.
Sam|Please do not let the case close just because a ticket has been created. I need an answer I can plan around.
Ada|Agreed. I will give you a status update today and identify the owner. The case remains open until the correction and employee communication are resolved.
Sam|Do you need my full bank statement to check this? It contains unrelated transactions I would rather not share.
Ada|Do not send that unnecessarily. We will use the relevant payroll records and the designated secure route for any information actually needed.
Sam|I can check the corrected statement against the hours and amount once it is issued. Will the original entry remain traceable?
Ada|Yes. The [[audit trail::The audit trail connects the original entry, identified error, correction, and resulting payment without silently rewriting the earlier record.]] should show what changed and why, including confirmation of the actual payment.
Sam|Thank you. Please send the case reference and today\'s update time so I know whom to contact if I hear nothing.
Ada|I will. We will address the missing pay promptly and keep any separate discussion about scheduling approval from obscuring the earnings issue.''',
        transfer_title='A gross correction is mistaken for a promised deposit',
        transfer_setup='Payroll confirms that a $180 gross earnings correction is due. The final deductions and payment date have not yet been confirmed.',
        transfer='''Adviser: The confirmed correction is a gross earnings ___.|amount|Gross earnings are stated before deductions and do not establish the exact deposit.
Employee: Please confirm the payment date rather than just the ticket ___.|status|An open ticket does not tell the employee when the money will actually be paid.
Adviser: Payroll must identify the applicable deductions and net ___.|payment|The net payment reflects the relevant deductions rather than automatically matching the gross correction.
Employee: Keep the correction linked to the original pay ___.|record|The original record and correction should remain connected in the audit trail.''',
        reference=('US Department of Labor: Overtime Pay', 'https://www.dol.gov/agencies/whd/overtime')),
    scenario(
        title='Selected for the role, but the transfer date is still open',
        skill='Clarify an internal move without confusing selection, approved terms, and handover arrangements.',
        setup='An internal candidate has been selected for a permanent analyst vacancy. The formal terms and transfer date have not been approved. The receiving manager proposes November 2, while the current manager requests a four-week handover. The recruiter and receiving manager must resolve the outstanding points without presenting either manager\'s preference as an agreed condition.',
        cast='Leah|Internal recruiter\nKofi|Receiving manager',
        dialogue='''Kofi|The panel selected Amira. I would like to announce that she joins us on November second so the team can start assigning work.
Leah|Please wait. The [[selection decision::The selection decision identifies the preferred candidate; it does not by itself establish approved terms or an agreed transfer date.]] is recorded, but the formal terms and transfer date are still open.
Kofi|I thought an internal move would be simpler than an external hire. Her current manager is now asking for a four-week handover.
Leah|That is a request to discuss, not an agreed [[release date::The release date identifies the agreed transition out of the current role; a manager's preferred timing does not establish it unilaterally here.]]. We need Amira and the relevant decision makers included in the timing conversation.
Kofi|The vacancy is permanent. Someone has started calling it a secondment because the start date is uncertain.
Leah|Correct that. A [[secondment::A secondment is a temporary assignment with its own terms; uncertainty about timing does not convert a permanent move into one.]] is a different arrangement. We should not change the nature of the role just to describe an unfinished handover.
Kofi|What is still needed on compensation? The role has a salary range, but I have not made an individual offer.
Leah|The approved [[offer terms::Offer terms specify the actual employment or assignment conditions being offered, rather than only the role's general salary range.]], including the relevant pay and conditions. Please do not let an informal conversation become a promise before that review is complete.
Kofi|Understood. Can I at least discuss the work she would take on and the training she would need?
Leah|Yes, explain the role accurately and hear her questions. Keep preparation distinct from assigning work under a transfer that has not taken effect.
Kofi|Her current team says only Amira knows one monthly report. I do not want the handover to become an indefinite reason to delay her.
Leah|Ask for a bounded [[transition plan::A transition plan identifies the work, knowledge transfer, owners, and timing needed for the move rather than leaving release indefinitely undefined.]]. Identify the report, a receiving owner, and practical training needs, then escalate unresolved timing through the applicable process.
Kofi|We should also avoid asking her to do both full roles for several weeks. That would hide the capacity problem rather than solve it.
Leah|Agreed. Make any overlap duties and limits explicit. The two managers need to resolve competing assignments instead of leaving Amira to negotiate them alone.
Kofi|Who should confirm the final arrangement to her? At the moment she has three different messages from us.
Leah|Let us coordinate one written [[confirmation::Confirmation communicates the actual agreed terms and effective date; it should replace conflicting informal messages without inventing an outcome.]] once the relevant approvals and her response are complete. I will coordinate it and keep both managers informed.
Kofi|I will pause the announcement and send you the proposed first-month responsibilities. November second will stay a proposal for now.
Leah|Thank you. I will arrange the timing discussion and tell Amira what remains outstanding, with a clear date for the next update.
Kofi|When we do announce it, we should use the agreed title and date, not repeat the earlier secondment description.
Leah|Exactly. A clear internal move needs consistent terms, a workable handover, and the employee included in the decisions affecting the transition.''',
        transfer_title='A manager announces a date the employee has not agreed',
        transfer_setup='A manager proposes December 1 for an internal transfer. Formal terms and the employee\'s response are still outstanding.',
        transfer='''Recruiter: December first is proposed, not yet ___.|agreed|The supplied facts establish a suggested date rather than a completed agreement.
Manager: I will pause the announcement while we resolve the ___.|terms|Outstanding formal terms must not be hidden by announcing a settled move.
Recruiter: Include the employee in the transition ___.|discussion|The employee should be involved rather than receiving conflicting decisions from separate managers.
Manager: Send one accurate confirmation after the required ___.|approvals|The final communication should reflect actual approvals and the agreed position.''',
        reference=('EEOC: Recruiting, Hiring, and Promoting Employees', 'https://www.eeoc.gov/employers/small-business/3-im-recruiting-hiring-or-promoting-employees')),
    scenario(
        title='Twelve employees do not equal twelve full-time equivalents',
        skill='Explain workforce measures and reject unsupported conclusions about staffing capacity.',
        setup='A department has eight employees scheduled for 40 hours a week and four scheduled for 20 hours. For this internal report, one full-time equivalent equals 40 scheduled weekly hours. Two additional positions are vacant. A draft shows 14 employees and 14 full-time equivalents. No skill coverage, absence, or productivity data is supplied.',
        cast='Ravi|People analyst\nJune|Department director',
        dialogue='''June|The staffing slide says fourteen people and fourteen full-time equivalents. That sounds like enough coverage, but the team says we are stretched.
Ravi|The [[headcount::Headcount counts people in the defined population; the department has twelve employees, while its two vacancies are not employees.]] is twelve. The two vacancies belong in a separate field because there are no employees occupying them.
June|Eight people work forty hours and four work twenty. Can you show how that becomes a capacity figure without losing the number of people?
Ravi|That is four hundred [[scheduled hours::Scheduled hours total the planned weekly hours: eight times forty plus four times twenty equals four hundred.]] a week: three hundred twenty from the eight full-time schedules and eighty from the four part-time schedules.
June|So four hundred divided by forty gives ten full-time equivalents. The four people on half-time schedules contribute two full-time equivalents, but they remain four people.
Ravi|Exactly. The [[FTE::FTE means full-time equivalent; four hundred scheduled hours divided by the stated forty-hour basis gives ten FTE.]] is ten under this definition. I will correct the arithmetic and keep the basis beside the result.
June|Does the ten tell us how many productive hours the department actually delivered last week?
Ravi|No. This uses scheduled hours. [[Actual hours::Actual hours describe recorded time for the specified period and are different from the scheduled-hours basis used in this example.]], absence, training, and the work performed would need their own data and definitions.
June|Then the slide should not claim that filling two vacancies automatically gives us twelve full-time equivalents either.
Ravi|Right. We need the approved hours for those positions before adding any projected capacity. A [[vacancy::A vacancy is an unfilled position, not an existing employee or a confirmed amount of staffed capacity.]] does not supply hours merely because it appears on the organization chart.
June|One of the open roles requires a specialist qualification. General additional hours would not necessarily cover that work.
Ravi|That is why the [[skills coverage::Skills coverage considers whether the required capabilities are available, which an aggregate FTE figure cannot establish on its own.]] view matters alongside the total. Ten FTE does not mean every required task or shift is covered.
June|Can you split the report into employees, scheduled FTE, vacancies, and the outstanding capability questions?
Ravi|Yes. I will also give the reporting date and population so another department does not compare it with a month-average figure by mistake.
June|We use a different hours basis in one external return. Should we force this internal calculation into that form as well?
Ravi|No. Follow each report\'s applicable definition and explain the difference. A familiar label does not make two calculation methods interchangeable.
June|The corrected slide will therefore show twelve employees, ten scheduled FTE, and two vacancies with hours still to confirm.
Ravi|Correct. It will not infer a productivity result, a sufficient staffing level, or a hiring decision from those totals alone.
June|Please include the skill gap as an open question for our workforce review. That is the discussion the original fourteen-person headline obscured.
Ravi|I will. We can make the staffing decision clearer by keeping people, hours, vacant positions, and required capabilities visible separately.''',
        transfer_title='Three half-time roles are counted as three FTE',
        transfer_setup='For this internal calculation, one FTE is 40 scheduled hours a week. Three employees each work 20 scheduled hours a week.',
        transfer='''Director: The headcount is three ___.|employees|Headcount counts the three people rather than converting them into full-time units.
Analyst: Their scheduled weekly hours total ___.|sixty|Three employees multiplied by twenty hours equals sixty scheduled hours.
Director: On a forty-hour basis, that gives one point five ___.|FTE|Sixty divided by forty equals one and one-half full-time equivalents.
Analyst: That figure alone does not establish actual ___.|productivity|A scheduled-hours measure does not show how much useful work was actually completed.'''),
]
