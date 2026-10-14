"""Line edits keep teaching disclaimers outside the fictional speakers' mouths.

The source case and publication scope still identify invented data and retain
the professional boundaries. Test exercises inside a real workplace scenario
(for example a disaster-recovery drill) are not removed.
"""

LINES = {
    'automotive-service': {(11, 13): "So the initial total is outside the specified range, and we haven't recorded a final result. I'll explain that without guessing what work was done."},
    'banking-operations': {
        (9, 18): "Right. The {{6}} is recorded in the account history. That doesn't promise when a different hold will clear. Include the snapshot time when you explain the balance.",
        (11, 19): "The corrected charge is five hundred eighty-three dollars and thirty-three cents. We changed the principal intervals, not the rate."},
    'baristas-cafe-staff': {(10, 7): "That gives twenty-two point five percent. It's an estimate based on the beverage we measured, not a perfect account of everything removed from the grounds."},
    'cardiologists': {(7, 14): "Yes. {{7}} is 0.75 in this illustration. The relative reduction is 0.25, or twenty-five percent. Those are different ways of describing the same comparison."},
    'carpentry-remodeling': {(11, 8): "That's the {{4}}. Keep each sample's result visible. This interval comes from our project specification; it isn't a rule for every wood product."},
    'childcare-early-education': {(9, 8): "Thank you. Our {{4}} still applies. Before changing the staffing plan, we need to check the required ratios, staff qualifications, and each child's support arrangements."},
    'data-analytics-business-intelligence': {(5, 15): "Both orders in this extract have payments. But the full report must still include an order without a payment if it belongs in the reporting population."},
    'energy-utilities': {
        (3, 14): "Use the official notice and {{7}} to check the proceeding details. We still need the filing number and participation deadline; don't guess either one.",
        (7, 15): "We need to correct the savings claim too. We don't have the rates, fixed charges, credits, demand charges, or other billing details for this account."},
    'cybersecurity': {
        (2, 16): "An update, not a working service. The {{8}} is at nine forty-five. We'll report what changed, what remains unresolved, and the next actions. That time isn't a restoration estimate."},
    'environmental-consulting': {(9, 20): "Good. The figures now reconcile. That doesn't settle the cleanup classification, whether our sampling is adequate, or what the results mean for exposure."},
    'housekeeping-commercial-cleaning': {
        (10, 14): "Correct. The marker result doesn't measure {{6}}. We haven't done a microbial culture or another organism-specific test.",
        (11, 16): "Exactly. Shared equipment, obstructions, and access limits could change the time needed. We shouldn't turn this planning rate into a universal speed requirement."},
    'hvac-refrigeration': {(11, 17): "Then I'll make the handoff clear: we've corrected the calculations, not completed servicing. We haven't obtained new readings or changed a setting."},
    'insurance': {
        (9, 10): "Neither is included here. This adjustment reconciles the estimated and audited exposure using the stated formula. It isn't a penalty or a charge for claims.",
        (10, 6): "Under these terms, the {{3}} is released after the repair conditions are verified. It's separate from the deductible you retain."},
    'investment-management-banking': {
        (3, 7): "They cover the same year and use the same currency. The methodology note identifies which deductions are included in net.",
        (5, 12): "The deal terms determine {{6}}. This bridge uses ten. We still need to verify that against the agreed definitions before relying on the closing calculation."},
    'landscaping-grounds': {
        (9, 15): "And fifty millimeters is the depth specified on this worksheet. It isn't a rule for every plant, site, or existing mulch condition.",
        (9, 16): "Exactly. We've checked the quantity calculation. The depth and placement still need to match the design and site assessment."},
    'manufacturing': {
        (6, 6): "Exactly. {{3}} needs the approved process for this equipment. We can't fill the gap by improvising an isolation procedure.",
        (6, 19): "Then this step stays on hold until the reviewed instruction is available. I'll make sure nobody mistakes our clarification for permission to start cleaning."},
    'medical-laboratory-technicians': {
        (9, 9): "Can we call this a trend? We've only reviewed one observation, not a sequence moving upward.",
        (9, 20): "That gives the next reviewer a usable record. It doesn't authorize an analyzer adjustment or the release of patient results.",
        (11, 16): "Yes. Follow our reporting procedure and obtain the authorized review. Don't change the report fields before that check.",
        (11, 17): "I understand the distinction between detection and quantification. I still need to check our reporting policy; those definitions don't establish a clinical decision threshold."},
    'office-administrative-assistants': {(9, 6): "Use the stated {{3}}. Forty-eight goes into the eligible employee-paid amount; the policy excludes the twenty."},
    'pharmacy-technicians': {(9, 13): "I'll check the claim entry against the plan and pharmacy rules with you. This calculation alone doesn't tell us which billing rule applies."},
    'software-developers': {(11, 18): "Good. This contract describes our current implementation. We still need the approved financial rules for each jurisdiction before making a compliance claim."},
    'truck-delivery-drivers': {(11, 20): "That's the read-back I need: vehicle, units, restriction source, and proposed route. The route still needs approval before departure."},
}

SPOKEN_WORDING = {
    'in the supplied record': 'in the record we have',
    'the supplied information': 'the information we have',
    'the supplied evidence': 'the evidence we have',
    'the supplied assessment': 'the assessment we have',
    'the supplied task': 'the requested task',
    'the supplied question': 'the reporting question',
    'the supplied result': 'the reported result',
    'the supplied note': 'the note we received',
    'the supplied rollout rule': 'our agreed rollout rule',
    'the supplied priority': 'our agreed priority',
    'under these supplied assumptions': 'under these assumptions',
    'under the supplied assumptions': 'under the assumptions we agreed',
    'on the supplied facts': 'based on what we know',
    'the fictional secret placed': 'the test secret placed',
}


def revise(book):
    scenes = book['units'] + book['supplements']
    for (scene, turn), line in LINES.get(book['slug'], {}).items():
        speaker, _ = scenes[scene - 1]['dialogue'][turn - 1]
        scenes[scene - 1]['dialogue'][turn - 1] = (speaker, line)
    for scene in scenes:
        polished = []
        for speaker, line in scene['dialogue']:
            for before, after in SPOKEN_WORDING.items():
                line = line.replace(before, after)
            polished.append((speaker, line))
        scene['dialogue'] = polished
