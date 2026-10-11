"""Distinct hotel payment, accessibility, and group-billing situations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The banking app still shows the hotel hold',
        skill='Explain pending and completed card transactions without promising a bank-controlled release time.',
        setup='After checkout, a guest sees a $350 pending hotel authorization and a $280 posted payment. The final bill is room $240, supplied tax $24, and parking $16. Hotel records show one completed $280 payment and a request to release the unused authorization. The issuer has not confirmed its display or release timing.',
        cast='Ms Bennett|Guest\nIdris|Front-desk supervisor',
        dialogue='''Ms Bennett|My receipt says two hundred eighty dollars, but my banking app also shows three hundred fifty. Have you charged me twice?
Idris|Let us check the entries separately. The three hundred fifty appears as an [[authorization hold::An authorization hold reserves funds or credit temporarily; its pending display is not proof of a second completed payment.]], while the two hundred eighty is posted. I will compare that with our payment record.
Ms Bennett|The larger amount was there when I checked in. I assumed it was the room payment, so I was surprised to see another entry today.
Idris|Our record shows the check-in authorization and one completed payment at checkout. I understand why the two entries together are concerning.
Ms Bennett|Can you show what makes up the two hundred eighty? I did not buy anything from the minibar.
Idris|Here is the [[itemized folio::The itemized folio lists the room, tax, and parking charges, allowing the guest to reconcile the $280 total.]]: room two hundred forty, tax twenty-four, and parking sixteen. There is no minibar charge on this bill.
Ms Bennett|Those add to two hundred eighty. The parking is correct. What happened to the remaining seventy from the larger amount?
Idris|That difference is not an extra charge on your folio. We have asked for the unused authorization to be released; that is not a seventy-dollar refund of a completed payment.
Ms Bennett|So your records show two hundred eighty paid, rather than six hundred thirty paid in total?
Idris|Correct. There is one [[settled payment::The settled payment is the completed $280 checkout transaction in the supplied record, not the sum of a posted payment and pending authorization.]] in our record. The pending entry can still affect what you have available while it is being resolved.
Ms Bennett|I need to use the card for another hotel tonight. Can you remove the pending entry before I get there?
Idris|I can check the [[release request::The release request is the hotel's instruction concerning unused authorization; it does not confirm when the issuer will update available funds or its display.]] and provide its recorded details. I cannot control when your card provider updates the account or guarantee that it will happen today.
Ms Bennett|I would appreciate something I can give them. Please do not just tell me to wait without checking whether the request went through.
Idris|I will verify the request with our payments team and send you the final folio through our approved private channel. We can also supply the relevant transaction reference securely.
Ms Bennett|Should I send you a screenshot of the entire banking screen? It includes the card number and several other purchases.
Idris|Do not send the full screen or card number by ordinary email. Use our secure process for any details needed, and contact your [[card issuer::The card issuer maintains the card account and can check how the pending authorization affects it; the hotel cannot promise its processing time.]] through its verified contact channel.
Ms Bennett|The available amount is lower, even though you say the second entry is pending. That is the part causing the problem for me.
Idris|I understand. A hold can reduce your available funds or credit without being a second completed charge. We should not dismiss that practical effect.
Ms Bennett|Please send the verified documents and tell me what the payments team confirms. I will ask my issuer about the pending entry and what I can use tonight.
Idris|I will follow up with the verified status. Ask the issuer about your [[available balance::The available balance reflects what the guest can currently use; it can be affected by a hold even when only one payment has settled.]], not just the posted total. If another completed charge appears, let us investigate it rather than assume it is still the same hold.''',
        transfer_title='Do not add pending to posted as a final bill',
        transfer_setup='A guest sees a $220 pending authorization and a $180 posted hotel payment. The itemized final folio totals $180. The hotel has requested release of the unused authorization, but the issuer has not confirmed when it will disappear.',
        transfer='''Guest: "The final itemized bill is ___ dollars."|180|The supplied folio and posted payment both total one hundred eighty dollars.
Agent: "The separate authorization is still labeled ___."|pending|The banking display identifies the authorization as pending, not another posted payment.
Guest: "The forty-dollar difference is not automatically a cash ___."|refund|An unused authorization is released rather than refunded as though it were a completed charge.
Agent: "The issuer must confirm the release ___."|timing|The hotel has submitted the request but cannot guarantee the issuer's processing time.''',
        reference=('Hilton: payment and authorization-hold explanations', 'https://www.hilton.com/en/hilton-honors/payment-security/'),
    ),
    scenario(
        title='Accessible describes features, not one standard room',
        skill='Check a guest\'s required features and complete a reservation without substituting assumptions.',
        setup='Ms Diaz needs two separate beds and a roll-in shower with a fixed seat. For her dates, the hotel has verified Room A with one king bed and a roll-in shower, Room B with two beds and a tub, and Room C with two queen beds and the requested shower and seat. Room C is available.',
        cast='Ms Diaz|Guest\nOwen|Reservations agent',
        dialogue='''Ms Diaz|Your website lists several accessible rooms, but I cannot tell which has two beds and a roll-in shower with a fixed seat.
Owen|Let me check those [[specific features::Specific features identify what this guest needs; a general accessible label does not establish the bed or bathing arrangement.]] for your dates. I will describe what is verified rather than assume every accessible room is the same.
Ms Diaz|Thank you. I am traveling with a companion, so one king bed will not work. We need separate beds.
Owen|Room A has a roll-in shower but one king bed. That does not meet the bed requirement. Room B has two beds, but its bathroom has a tub.
Ms Diaz|A tub with grab bars would not replace the shower I asked for. Is there a room with both features together?
Owen|Yes. Room C has two queen beds and a [[roll-in shower::The roll-in shower is the verified bathing feature in Room C; a tub with grab bars is not the requested substitute.]] with a fixed seat. Its current feature record confirms both, and it is available for your dates.
Ms Diaz|That sounds right. I also need to know whether there is a step-free route from the entrance to that room.
Owen|I will verify the route details with our on-site team before you decide. I have the room features, but I do not want to invent information about the route.
Ms Diaz|Could you also send the bathroom layout? A description of accessible does not tell me where the seat is in relation to the controls.
Owen|I can request the current [[layout::The layout shows the arrangement of the bathroom features, helping the guest assess suitability without the agent asking for a diagnosis.]] and any verified measurements you need. You can tell me which details matter; you do not need to explain a medical diagnosis.
Ms Diaz|Please check the seat and control positions. I will assess whether the layout works for me from that information.
Owen|Certainly. Your [[access needs::Access needs concern the practical features the guest requires, not a presumed limitation based on a broad disability label.]] guide what we verify. I will keep the actual features in the reservation notes, not substitute a general label.
Ms Diaz|If I reserve it, could another guest be given that room and leave me with the tub room at check-in?
Owen|We must preserve the confirmed required features in the booking. I will follow the room-blocking process, not treat either of the other room types as an equivalent replacement.
Ms Diaz|Please send the route and layout details first. Once I have checked them, I would like to complete the booking for Room C.
Owen|That is fine. This conversation has confirmed availability, but it has not yet completed your [[reservation::The reservation is the actual booking, distinct from an availability discussion; it will be completed after the requested details and the guest's decision.]]. I will make that status clear in my message.
Ms Diaz|And please show the room rate and cancellation terms in that message too. I need the same booking information as for any other room.
Owen|Of course. I will include the verified features, the requested route and layout information once checked, and the applicable rate and terms together.
Ms Diaz|Good. Do not switch me to a one-bed room to preserve the shower, or a tub room to preserve the beds. I need both.
Owen|Understood. The [[bed configuration::The bed configuration is two separate queen beds in Room C, which must be preserved together with the requested shower features.]] and shower requirements are linked in this request. I will follow up with the missing information so you can make an informed choice.''',
        transfer_title='Check the combination, not the label',
        transfer_setup='A guest requires two separate beds and a roll-in shower. Room 1 has one king bed and that shower. Room 2 has two beds and a tub. Available Room 3 has two beds and a roll-in shower. Route information still needs checking before the guest decides.',
        transfer='''Agent: "The verified feature match is Room ___."|3|Only Room 3 combines both the requested bed arrangement and shower type.
Guest: "Two beds with a tub are not an equivalent ___."|combination|Room 2 meets the bed requirement but fails the separately stated shower requirement.
Agent: "The remaining information concerns the ___."|route|The brief identifies route information as the detail still requiring verification.
Guest: "Availability alone does not complete my ___."|reservation|The guest has not yet decided or completed a booking in this scenario.''',
        reference=('U.S. Department of Justice: lodging reservations and accessible features', 'https://www.ada.gov/law-and-regs/regulations/title-iii-regulations/'),
    ),
    scenario(
        title='Room and tax to the organizer, extras to the guest',
        skill='Translate group billing instructions into accurate charge routing and a reconciled readback.',
        setup='A fictional group agreement makes the organizer responsible for room and supplied room tax only. Each guest pays parking and breakfast. One two-night folio shows room $150 per night, tax $15 per night, parking $20 total, and breakfast $30 total. The current routing incorrectly sends everything to the organizer. No payment has been settled.',
        cast='Inez|Group coordinator\nCal|Hotel cashier',
        dialogue='''Inez|The organizer's draft bill includes parking and breakfast. Our agreement says room and tax only. Could we check the routing before checkout?
Cal|Yes. The [[master account::The master account is the organizer's group billing account; the agreement permits room and tax there, not every guest charge.]] is receiving all charge codes at present. That is wider than the signed billing instructions.
Inez|For this reservation, the room is one hundred fifty per night for two nights, with fifteen tax each night.
Cal|That makes three hundred in room charges and thirty in room tax. The organizer's share should be three hundred thirty for this guest.
Inez|Parking is twenty total and breakfast is thirty total. Those are guest-paid, not thirty dollars of breakfast on each night.
Cal|Understood. The [[individual folio::The individual folio should carry the guest's $20 parking and $30 breakfast charges, totaling $50 in this supplied example.]] should carry fifty dollars. I will keep the two-night room amounts separate from the supplied total extras.
Inez|The total bill is still three hundred eighty. We are changing who pays, not removing the parking or breakfast charge.
Cal|Exactly. The revised split must reconcile to the same total. A transfer between folios is not a discount or a refund.
Inez|Will changing the instructions affect only tonight's new charges, or also the items already posted on this draft?
Cal|I will check both. The [[routing instructions::Routing instructions define which charge categories go to which account; existing postings also need checking rather than assuming an edit moves them correctly.]] need correction, and the existing postings must be reviewed under our system's adjustment process.
Inez|Please retain a record of the transfer. The organizer will ask why the revised statement differs from the draft they saw this morning.
Cal|I will preserve the [[audit trail::The audit trail records the original postings and authorized transfers, so the corrected payer split remains explainable without deleting charges.]] and use the approved correction method. We should not delete the extras and re-enter an unexplained lump sum.
Inez|One guest says their manager told them breakfast would be covered. I do not have written approval changing the group agreement.
Cal|We will refer that discrepancy to the authorized group contact. I cannot expand the master-account scope based on an unverified verbal message.
Inez|For now, can reception explain the written arrangement at checkout without making the guest feel accused of charging the wrong account?
Cal|Yes. We can say room and tax are covered by the organizer, with these listed extras payable individually. If the guest raises a [[billing dispute::A billing dispute records disagreement about who should pay or what is due; it should be reviewed without presenting unverified approval as fact.]], we will record it and seek the required decision.
Inez|No money has been taken yet. Please do not call the fifty-dollar correction a refund in the email to the organizer.
Cal|Agreed. It is a correction to the unpaid folio allocation. We will issue the appropriate final statements once the split and any dispute are resolved.
Inez|Read back this one for me: three hundred thirty to the organizer, fifty to the guest, three hundred eighty altogether.
Cal|That reconciles. I will complete the [[charge transfer::The charge transfer moves the $50 extras to the proper unpaid guest folio while preserving the $380 total and the recorded history.]] and verify the revised statements before settlement. The corrected instructions must also reach the next cashier.''',
        transfer_title='A payer change does not change the total',
        transfer_setup='An unpaid two-night bill has room $120 per night, room tax $12 per night, and guest-paid parking $18 total. The organizer covers room and tax only. No other charges apply.',
        transfer='''Coordinator: "The organizer pays ___ dollars."|264|Two room nights total $240 and two tax amounts total $24, producing $264.
Cashier: "The guest pays ___ dollars."|18|The supplied parking total belongs to the guest under the stated agreement.
Coordinator: "The combined bill remains ___ dollars."|282|Adding the organizer's $264 and the guest's $18 preserves the $282 total.
Cashier: "Changing the unpaid allocation is not a ___."|refund|No payment has settled, so correcting the payer allocation does not return money already paid.''',
        reference=('Oracle OPERA Cloud: reservation routing instructions', 'https://docs.oracle.com/en/industries/hospitality/opera-cloud/21.5/ocsuh/c_managing_reservations_routing_instructions.htm'),
    ),
]
