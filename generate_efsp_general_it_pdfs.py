from __future__ import annotations

import html
from pathlib import Path

from reportlab.platypus import PageBreak, Paragraph, Spacer

from generate_efsp_guarded_activities import add_answer_key, add_cloze_exercise, bounded_activity_instruction, make_dialogue_cloze
from generate_efsp_culture_pdfs import (
    CONTENT_WIDTH,
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
                "Focus: high-level professional English for general IT teams, including service management, networks, identity, cloud, endpoints, security operations, change control, observability, and realistic workplace dialogue.",
                "Designed for advanced ESL learners who already work in IT or IT-adjacent roles and need field-specific fluency rather than basic technical vocabulary.",
            ],
            "blue",
        ),
        Spacer(1, 0.22 * 72),
        p(
            "Teaching stance: general IT is not one job. Learners need enough shared language to move across help desk, infrastructure, security, cloud, platform, vendor, and business conversations without losing precision or credibility.",
            "Small",
        ),
        PageBreak(),
    ]


COURSE_OBJECTIVES = [
    "Use general IT terminology accurately in tickets, incident calls, change reviews, access discussions, vendor meetings, and executive updates.",
    "Triage ambiguous technical problems by asking about scope, impact, timeline, evidence, dependencies, and recent changes.",
    "Explain infrastructure, identity, networking, endpoint, cloud, security, and operations issues in concise professional English.",
    "Push back on risky shortcuts using business impact, operational evidence, security principles, and customer-facing consequences.",
    "Participate in realistic IT dialogues: outage bridges, service desk escalations, access reviews, patch windows, cloud cost reviews, and post-incident reviews.",
    "Write clear workplace outputs: ticket updates, change summaries, risk statements, incident notes, root-cause language, and action items.",
]


MODULES = [
    {
        "title": "Module 1. IT Service Language, Tickets, and Triage",
        "time": "90 minutes",
        "big_idea": "General IT work often starts with incomplete reports: 'VPN is broken,' 'the app is slow,' or 'users cannot log in.' Strong IT English turns vague pain into scope, impact, evidence, priority, and next action.",
        "objectives": [
            "Distinguish incident, service request, problem, change, task, and known error.",
            "Ask triage questions about impact, urgency, affected users, timeline, and recent changes.",
            "Write ticket updates that are useful to both technical teams and business stakeholders.",
        ],
        "concepts": [
            "Severity vs priority: severity describes technical or business impact; priority also includes urgency, customer importance, deadlines, and risk.",
            "SLA vs SLO: an SLA is usually a formal commitment; an SLO is an internal reliability target used to guide operations.",
            "Escalation: moving work to a higher skill group, manager, vendor, or incident process because risk, time, or authority requires it.",
        ],
        "activities": [
            "Ticket surgery: learners rewrite vague tickets with observed behavior, expected behavior, scope, evidence, and next owner.",
            "Triage interview: learners question a frustrated user without sounding robotic or dismissive.",
            "Priority debate: learners assign severity and priority to five incidents, then defend their reasoning.",
        ],
        "outputs": [
            "Ticket update template.",
            "Triage question bank.",
            "Severity/priority explanation script.",
        ],
    },
    {
        "title": "Module 2. Networks, Connectivity, and Root-Cause Hypotheses",
        "time": "90 minutes",
        "big_idea": "Network conversations require careful hypothesis language. DNS, DHCP, VPN, routing, firewall rules, certificates, proxies, and load balancers can create similar user symptoms.",
        "objectives": [
            "Explain common network components and failure modes in workplace English.",
            "Separate user-side, device-side, network-side, and application-side evidence.",
            "Use cautious root-cause language before proof is available.",
        ],
        "concepts": [
            "DNS resolution, IP addressing, DHCP lease, subnet, gateway, VPN tunnel, VLAN, firewall rule, proxy, TLS certificate, and load balancer.",
            "Packet path thinking: client, local network, VPN, firewall, DNS, load balancer, application server, database, and external dependency.",
            "Symptom does not equal root cause. 'Cannot reach the app' may be identity, DNS, network, server, certificate, or browser cache.",
        ],
        "activities": [
            "Path map: learners draw the connection path for a remote user accessing an internal HR system.",
            "Hypothesis ladder: learners rank possible causes from most likely to least likely using evidence.",
            "Network-status update: learners explain a connectivity issue without overclaiming root cause.",
        ],
        "outputs": [
            "Connectivity triage map.",
            "Network hypothesis language list.",
        ],
    },
    {
        "title": "Module 3. Identity, Access, and Permissions",
        "time": "90 minutes",
        "big_idea": "Access requests are rarely just technical. They involve identity proof, authorization, least privilege, auditability, urgency, and sometimes uncomfortable pushback to senior people.",
        "objectives": [
            "Distinguish authentication, authorization, SSO, MFA, RBAC, groups, roles, and service accounts.",
            "Explain least privilege and conditional access without sounding obstructive.",
            "Handle urgent access requests with controls, time limits, approvals, and audit trails.",
        ],
        "concepts": [
            "Authentication verifies identity; authorization determines what that identity can access.",
            "Joiner/mover/leaver process: access changes when people join, change roles, or leave.",
            "Privilege creep: users accumulate access over time unless roles are reviewed and removed.",
        ],
        "activities": [
            "Access review: learners identify excessive permissions and propose removals in diplomatic language.",
            "Urgent exception role-play: a director wants admin access immediately before a deadline.",
            "IAM explainer: learners explain MFA fatigue, conditional access, and service accounts to non-specialists.",
        ],
        "outputs": [
            "Access approval question set.",
            "Least-privilege pushback script.",
        ],
    },
    {
        "title": "Module 4. Cloud, Infrastructure, and Cost-Aware Operations",
        "time": "90 minutes",
        "big_idea": "Cloud IT conversations combine architecture, operations, cost, security, and ownership. Learners need to discuss tradeoffs without treating cloud as unlimited or invisible.",
        "objectives": [
            "Use terms such as region, availability zone, VPC, subnet, VM, storage, snapshot, autoscaling, IaC, tagging, and shared responsibility.",
            "Explain reliability, performance, security, sustainability, and cost tradeoffs.",
            "Discuss unexpected cloud spend with evidence and practical mitigation options.",
        ],
        "concepts": [
            "Shared responsibility: cloud providers and customers each own different parts of security and operations.",
            "Infrastructure as code: infrastructure defined and changed through versioned configuration rather than only manual clicks.",
            "Cost drivers: compute size, idle resources, storage retention, data transfer, logs, backups, and over-provisioning.",
        ],
        "activities": [
            "Architecture walkthrough: learners explain a small cloud workload to a finance manager.",
            "Cost spike meeting: learners identify possible causes and propose immediate and structural fixes.",
            "Risk tradeoff: learners compare manual changes, IaC, rollback plans, and approval gates.",
        ],
        "outputs": [
            "Cloud architecture explanation.",
            "Cost-spike summary email.",
        ],
    },
    {
        "title": "Module 5. Endpoints, Servers, Patching, and Configuration Management",
        "time": "90 minutes",
        "big_idea": "Endpoint and server operations require clear language about assets, baselines, patches, compatibility, exceptions, maintenance windows, rollback, and user disruption.",
        "objectives": [
            "Discuss patching and configuration risk with technical and business audiences.",
            "Explain asset inventory, MDM, EDR, encryption, baseline configuration, and policy compliance.",
            "Negotiate maintenance windows and exception requests.",
        ],
        "concepts": [
            "Patch management: identifying, testing, deploying, and verifying updates for vulnerabilities, bugs, and stability.",
            "Configuration drift: systems gradually differ from the approved baseline.",
            "Rollback plan: a prepared way to return to the previous working state if a change fails.",
        ],
        "activities": [
            "Patch window negotiation: learners balance security risk, downtime, and business deadlines.",
            "Exception review: learners decide whether a legacy system can remain unpatched and under what controls.",
            "Baseline explanation: learners explain why configuration standards matter to a skeptical team.",
        ],
        "outputs": [
            "Patch communication template.",
            "Exception risk statement.",
        ],
    },
    {
        "title": "Module 6. Security Operations, Risk, and Incident Response",
        "time": "90 minutes",
        "big_idea": "Security conversations require precision and restraint. Vulnerability, exploit, alert, event, incident, risk, compromise, and breach are not interchangeable words.",
        "objectives": [
            "Use security operations vocabulary accurately in alerts, tickets, escalations, and briefings.",
            "Explain risk using likelihood, impact, exposure, compensating controls, and evidence.",
            "Participate in incident response without creating panic or hiding uncertainty.",
        ],
        "concepts": [
            "Event vs alert vs incident: not every log event is an alert, and not every alert is a confirmed incident.",
            "Vulnerability vs exploit: a weakness is not the same as active use of that weakness by an attacker.",
            "Zero Trust principles often emphasize explicit verification, least privilege, and assuming compromise is possible.",
        ],
        "activities": [
            "Alert triage: learners decide what evidence would move an alert to an incident.",
            "Phishing response: learners guide a user, preserve evidence, and escalate if needed.",
            "Risk statement rewrite: learners convert dramatic security language into decision-grade language.",
        ],
        "outputs": [
            "Security escalation script.",
            "Risk language checklist.",
        ],
    },
    {
        "title": "Module 7. Change, Release, Problem, and Post-Incident Communication",
        "time": "90 minutes",
        "big_idea": "Mature IT teams separate fixing the current outage from understanding recurring causes. Learners need language for change records, CAB review, maintenance windows, rollback, problem management, root cause, and action items.",
        "objectives": [
            "Discuss normal, standard, emergency, and high-risk changes.",
            "Explain root cause, contributing factors, detection gaps, and corrective actions without blame.",
            "Write action items that have owners, due dates, and verification criteria.",
        ],
        "concepts": [
            "Change enablement reduces risk by making intent, impact, testing, implementation, rollback, and communications visible.",
            "Problem management looks for underlying causes and recurring patterns, not only immediate restoration.",
            "Post-incident reviews should improve systems, monitoring, process, and communication rather than punish individuals.",
        ],
        "activities": [
            "CAB simulation: learners present a risky firewall change and answer objections.",
            "Postmortem rewrite: learners remove blame and add evidence, contributing factors, and follow-up actions.",
            "Emergency change debrief: learners explain why process was shortened and how risk was controlled.",
        ],
        "outputs": [
            "Change review script.",
            "Post-incident action-item table.",
        ],
    },
    {
        "title": "Module 8. Platform, DevOps, Observability, and Kubernetes Conversations",
        "time": "90 minutes",
        "big_idea": "Even general IT staff increasingly discuss CI/CD, containers, Kubernetes, logs, metrics, traces, SLOs, and automation. Learners need enough language to participate without pretending to be specialists.",
        "objectives": [
            "Explain containers, images, registries, pods, deployments, services, ingress, and rollout behavior.",
            "Use observability terms: logs, metrics, traces, dashboards, alerts, latency, throughput, saturation, and error budget.",
            "Connect platform symptoms to business impact and incident decisions.",
        ],
        "concepts": [
            "Containers package an application and dependencies; Kubernetes orchestrates containers across a cluster using resources such as Pods, Deployments, Services, and Ingress.",
            "Observability helps teams understand what is happening from system outputs: logs, metrics, traces, and events.",
            "Automation reduces repeat work but also requires review, version control, rollback, and monitoring.",
        ],
        "activities": [
            "Kubernetes incident: learners explain crashing pods, failed readiness checks, and rollback options.",
            "Dashboard readout: learners turn metrics into a spoken incident update.",
            "Automation review: learners identify where a script or pipeline needs approval, logging, or safeguards.",
        ],
        "outputs": [
            "Platform incident update.",
            "Observability phrase bank.",
        ],
    },
]


COURSE_OBJECTIVES = [bounded_activity_instruction(item) for item in COURSE_OBJECTIVES]
for _module in MODULES:
    _module["objectives"] = [bounded_activity_instruction(item) for item in _module["objectives"]]
    _module["activities"] = [bounded_activity_instruction(item) for item in _module["activities"]]


JARGON_GROUPS = [
    (
        "Service management",
        [
            ("Incident", "An unplanned interruption or reduction in service quality that needs restoration."),
            ("Service request", "A standard user request, such as access, equipment, information, or a routine change."),
            ("Problem", "An underlying cause or recurring pattern behind one or more incidents."),
            ("Change", "A planned modification to a service, system, configuration, process, or environment."),
            ("SLA", "A formal service-level agreement, often with customer or contractual consequences."),
            ("SLO", "A service-level objective used internally to set reliability targets and guide operations."),
            ("MTTR", "Mean time to restore or repair; a common measure of operational recovery speed."),
            ("Runbook", "A documented procedure for responding to known operational situations."),
        ],
    ),
    (
        "Networking and connectivity",
        [
            ("DNS", "The system that resolves names such as app.example.com to network addresses."),
            ("DHCP", "A service that assigns IP addresses and network configuration to clients."),
            ("VPN", "A protected tunnel that allows remote users or sites to access private resources."),
            ("VLAN", "A logical network segment used to separate traffic inside a physical network."),
            ("Subnet", "A range of IP addresses inside a larger network."),
            ("Gateway", "The route a device uses to reach networks outside its local segment."),
            ("Firewall", "A control that allows, blocks, or inspects network traffic based on rules."),
            ("Load balancer", "A component that distributes traffic across multiple backends."),
        ],
    ),
    (
        "Identity and access",
        [
            ("IAM", "Identity and access management: systems and policies controlling who can access what."),
            ("Authentication", "Verifying who a user, service, or device is."),
            ("Authorization", "Determining what the verified identity is allowed to do."),
            ("SSO", "Single sign-on: one identity session used across multiple applications."),
            ("MFA", "Multifactor authentication: two or more proof factors for identity verification."),
            ("RBAC", "Role-based access control: permissions assigned by role rather than one by one."),
            ("Least privilege", "Giving only the access required for the job, for only as long as needed."),
            ("Service account", "A non-human identity used by applications, jobs, or integrations."),
        ],
    ),
    (
        "Cloud and infrastructure",
        [
            ("VM", "Virtual machine: a software-defined server running on shared physical infrastructure."),
            ("Container", "A packaged application unit with dependencies and runtime isolation."),
            ("IaC", "Infrastructure as code: infrastructure managed through versioned configuration files."),
            ("Region", "A cloud provider geographic area containing multiple data-center locations."),
            ("Availability zone", "A separated location inside a region, used for resilience planning."),
            ("Autoscaling", "Automatically adding or removing capacity based on demand or policy."),
            ("Snapshot", "A point-in-time copy of a disk, volume, database, or system state."),
            ("Tagging", "Applying metadata labels to resources for ownership, cost, automation, or policy."),
        ],
    ),
    (
        "Endpoint and server operations",
        [
            ("Asset inventory", "A current list of hardware, software, owners, versions, and risk-relevant details."),
            ("MDM", "Mobile device management for enforcing policies on laptops, phones, and tablets."),
            ("EDR", "Endpoint detection and response tooling for monitoring and responding to endpoint threats."),
            ("Baseline", "An approved standard configuration for a system or device type."),
            ("Configuration drift", "When systems gradually differ from the approved baseline."),
            ("Patch", "A software update that fixes a bug, vulnerability, or compatibility issue."),
            ("Maintenance window", "An approved time period for work that may affect users or services."),
            ("Rollback", "A planned return to the previous working state after a failed change."),
        ],
    ),
    (
        "Security operations",
        [
            ("Vulnerability", "A weakness that could be accidentally triggered or intentionally exploited."),
            ("Exploit", "A method or action that takes advantage of a vulnerability."),
            ("CVE", "A public identifier for a known cybersecurity vulnerability."),
            ("SIEM", "Security information and event management: collects and analyzes security-relevant events."),
            ("IDS/IPS", "Intrusion detection/prevention systems that detect or block suspicious network activity."),
            ("Phishing", "A social-engineering attempt to trick a user into revealing information or taking action."),
            ("Zero Trust", "A security approach that avoids implicit trust and emphasizes verification and least privilege."),
            ("Audit log", "A record of relevant system, user, or administrative actions."),
        ],
    ),
    (
        "Observability and reliability",
        [
            ("Log", "A record of events or messages from an application, system, or device."),
            ("Metric", "A numerical measurement tracked over time, such as latency or error rate."),
            ("Trace", "A view of a request path across services and dependencies."),
            ("Alert", "A notification triggered when a condition may require human attention."),
            ("Latency", "How long a request takes to complete."),
            ("Throughput", "How much work a system handles over a period of time."),
            ("Saturation", "How close a resource is to its limit, such as CPU, memory, disk, or connection pool."),
            ("Error budget", "The acceptable amount of unreliability implied by an SLO over a period of time."),
        ],
    ),
    (
        "Backup, recovery, and continuity",
        [
            ("Backup", "A copy of data or system state kept for recovery after deletion, corruption, or failure."),
            ("Restore", "The process of recovering data or service from a backup or snapshot."),
            ("Replication", "Maintaining copies of data or systems in another location or environment."),
            ("Retention", "How long backups, logs, or records are kept before deletion."),
            ("RPO", "Recovery point objective: the maximum acceptable data loss measured in time."),
            ("RTO", "Recovery time objective: the maximum acceptable restoration time."),
            ("DR", "Disaster recovery: plans and systems for recovering after major disruption."),
            ("Failover", "Moving traffic or service to a standby system when the primary fails."),
        ],
    ),
]


DIALOGUES = [
    {
        "title": "1. Service Desk Escalation: 'VPN Is Broken'",
        "setting": "A remote employee reports that the VPN connects, but the finance system will not load.",
        "dialogue": [
            ("User", "The VPN is broken again. I cannot get to finance."),
            ("Service desk", "I understand the impact. Can I confirm one detail: does the VPN show connected, or does the connection fail completely?"),
            ("User", "It says connected."),
            ("ESL learner", "Then we should avoid calling this a VPN outage yet. It may be DNS, routing, firewall, or the finance app itself. Are other internal sites loading?"),
            ("User", "The intranet loads, but finance times out."),
            ("ESL learner", "Thank you. I will update the ticket as 'VPN connected; finance app unreachable over VPN for one user.' I am checking whether this is user-specific or app-wide before escalating."),
        ],
        "notes": [
            "Good triage narrows the scope before assigning blame.",
            "The learner validates the user's frustration while changing the technical description.",
        ],
    },
    {
        "title": "2. P1 Incident Bridge: DNS or Application Outage?",
        "setting": "Multiple users cannot reach a customer portal after a DNS change.",
        "dialogue": [
            ("Incident commander", "We need a clear status. Is the portal down?"),
            ("Network engineer", "The application servers are healthy. DNS queries are returning the old address for some users."),
            ("ESL learner", "So the service is partially unavailable because name resolution is inconsistent after the change. The immediate mitigation is to roll back the DNS record and lower the TTL if possible."),
            ("App owner", "Can we say the application is not the cause?"),
            ("ESL learner", "We can say current evidence points to DNS propagation, not application health. We should avoid final root-cause language until we review the change timeline and resolver logs."),
        ],
        "notes": [
            "Separate service impact from component health.",
            "Use 'current evidence points to...' when the root cause is not fully confirmed.",
        ],
    },
    {
        "title": "3. Access Review: Urgent Admin Permission",
        "setting": "A senior manager asks for admin rights to fix a reporting dashboard before a board meeting.",
        "dialogue": [
            ("Manager", "Just give me admin access for today. I know what I am doing."),
            ("IT lead", "We want to help with the deadline, but permanent admin rights are not the right control."),
            ("ESL learner", "We can offer a time-limited privileged session with approval, logging, and a clear task scope. After the task, access will be removed automatically."),
            ("Manager", "That sounds slow."),
            ("ESL learner", "It is faster than a normal access change, but it still protects the company and your account. I can start the exception workflow now and stay with you until the dashboard is fixed."),
        ],
        "notes": [
            "Least privilege can be framed as protection, not obstruction.",
            "Offer a controlled path rather than only saying no.",
        ],
    },
    {
        "title": "4. Patch Window Negotiation",
        "setting": "Security wants to patch a critical vulnerability; operations worries about downtime during month-end close.",
        "dialogue": [
            ("Security", "This CVE is being actively exploited. We need the patch tonight."),
            ("Operations", "Tonight is month-end close. If the ERP system is down, finance cannot finish."),
            ("ESL learner", "We have two risks: exploitation if we wait, and business disruption if the patch fails. Can we test the patch in staging now, apply compensating controls tonight, and schedule production for the first safe window?"),
            ("Security", "What controls?"),
            ("ESL learner", "Restrict exposure, increase monitoring, block known indicators, and require rollback approval before any production change. If exploitation evidence appears, we move to emergency change."),
        ],
        "notes": [
            "High-level IT English often balances two real risks instead of pretending one side is irrational.",
            "Compensating controls reduce risk when the ideal fix is delayed.",
        ],
    },
    {
        "title": "5. Cloud Cost Spike",
        "setting": "Finance notices a 38 percent increase in monthly cloud spend.",
        "dialogue": [
            ("Finance", "Why did cloud cost jump? Did IT approve this?"),
            ("Cloud engineer", "Most of the increase is compute in the analytics environment and log retention in production."),
            ("ESL learner", "The immediate issue is spend, but the operational issue is ownership. Several resources have no cost-center tags, so we cannot assign accountability confidently."),
            ("Finance", "Can you cut it today?"),
            ("ESL learner", "We can stop idle non-production instances today, reduce excessive log retention where policy allows, and bring a tagging enforcement plan by Friday. I would not delete storage until owners confirm retention requirements."),
        ],
        "notes": [
            "Cost conversations need evidence, ownership, and guardrails.",
            "Do not promise savings by deleting resources without retention review.",
        ],
    },
    {
        "title": "6. Kubernetes Incident: Crashing Pods",
        "setting": "A containerized internal tool fails after a deployment.",
        "dialogue": [
            ("Developer", "The deployment is broken. The pods keep restarting."),
            ("Platform engineer", "The readiness probe is failing, and the logs show missing environment variables."),
            ("ESL learner", "Then the cluster is doing what it should: it is not sending traffic to unhealthy pods. The likely cause is release configuration, not Kubernetes itself."),
            ("Developer", "Should we roll back?"),
            ("ESL learner", "Yes, unless there is a faster config fix with lower risk. My recommendation is rollback now, restore service, then compare the deployment manifest with the previous version."),
        ],
        "notes": [
            "The learner distinguishes platform behavior from application configuration.",
            "Incident language should prioritize restoration, then investigation.",
        ],
    },
    {
        "title": "7. Phishing and Possible Account Compromise",
        "setting": "A user clicked a suspicious link and entered credentials.",
        "dialogue": [
            ("User", "I think I made a mistake. I entered my password on a weird page."),
            ("Service desk", "Thank you for reporting quickly. Please do not change anything else yet."),
            ("ESL learner", "We will reset your password, revoke active sessions, check sign-in logs, and confirm whether MFA prompts were accepted. Can you forward the email as an attachment to security?"),
            ("User", "Am I in trouble?"),
            ("ESL learner", "The priority is containment and evidence. Reporting quickly helps us protect your account and other users."),
        ],
        "notes": [
            "Good security communication reduces shame so users report faster.",
            "Containment steps should be specific but not overly alarming.",
        ],
    },
    {
        "title": "8. Backup Restore Test: RPO Mismatch",
        "setting": "A restore test shows that the system can recover, but with more data loss than expected.",
        "dialogue": [
            ("Business owner", "The restore worked, so are we good?"),
            ("Database admin", "The restore completed, but the latest usable backup is six hours old."),
            ("ESL learner", "That means the RTO may be acceptable, but the RPO is not. We can restore service in time, but we may lose more data than the business agreed to."),
            ("Business owner", "I did not understand that difference."),
            ("ESL learner", "RTO is how long recovery takes. RPO is how much data loss is acceptable. We need either more frequent backups, replication, or a formal acceptance of the higher data-loss risk."),
        ],
        "notes": [
            "RTO and RPO are often misunderstood; define them in business language.",
            "A successful restore can still fail the business requirement.",
        ],
    },
    {
        "title": "9. Change Advisory: Firewall Rule Request",
        "setting": "A project team wants a broad firewall opening before a launch.",
        "dialogue": [
            ("Project lead", "We need to open the firewall to the vendor range today, or the launch slips."),
            ("Security architect", "The requested range is too broad."),
            ("ESL learner", "Can we narrow by source, destination, port, protocol, and time window? If the vendor cannot provide that, we should treat this as a high-risk exception with monitoring and an expiration date."),
            ("Project lead", "What is the business impact of waiting?"),
            ("ESL learner", "Launch delay is one impact. The other impact is exposing internal services more widely than necessary. The decision should name both risks and the owner who accepts the exception."),
        ],
        "notes": [
            "A change review is not only a technical approval; it records risk ownership.",
            "Use precise constraint language: source, destination, port, protocol, duration.",
        ],
    },
    {
        "title": "10. Post-Incident Review: Blame vs Learning",
        "setting": "A failed manual change caused an outage. The team is reviewing what happened.",
        "dialogue": [
            ("Manager", "Who made the change?"),
            ("Engineer", "I did, but I followed the old runbook."),
            ("ESL learner", "The action matters, but the improvement question is broader. Why did the runbook allow a manual step without peer review, validation, or rollback verification?"),
            ("Manager", "So what should the action items be?"),
            ("ESL learner", "Update the runbook, add automated validation, require peer review for that command, and create an alert that detects the bad state within two minutes."),
        ],
        "notes": [
            "Root-cause language should include process and detection gaps.",
            "Action items need owners, due dates, and verification, not just good intentions.",
        ],
    },
    {
        "title": "11. Vendor Escalation: SaaS Degradation",
        "setting": "A critical SaaS vendor reports a regional degradation affecting SSO logins.",
        "dialogue": [
            ("Business stakeholder", "Why can't IT fix this?"),
            ("Vendor manager", "The issue is in the vendor's region. We do not control their identity gateway."),
            ("ESL learner", "Our role is mitigation and communication. We are checking alternate login paths, monitoring the vendor status page, and collecting affected-user counts so we can escalate with evidence."),
            ("Stakeholder", "When will it be fixed?"),
            ("ESL learner", "The vendor has not provided an ETA. I will give the next update in 30 minutes, or sooner if the status changes."),
        ],
        "notes": [
            "When a vendor owns the fix, IT can still own communication, impact tracking, and mitigations.",
            "Avoid inventing ETAs under pressure.",
        ],
    },
    {
        "title": "12. Executive Update: Risk, Impact, and Decision",
        "setting": "A CIO asks for a short update during a major email outage.",
        "dialogue": [
            ("CIO", "Give me the short version."),
            ("ESL learner", "Email delivery is delayed for about 40 percent of users in North America. External mail is queued, not lost. The likely dependency is the spam-filtering service. We have opened a vendor P1 and are testing a bypass for critical mailboxes."),
            ("CIO", "What decision do you need?"),
            ("ESL learner", "Approval to enable the bypass for legal and customer support if delay exceeds one hour. The risk is reduced filtering during the bypass window, so security will monitor inbound volume and suspicious attachments."),
        ],
        "notes": [
            "Executive updates should include impact, confidence, mitigation, risk, and requested decision.",
            "A short update can still be technically precise.",
        ],
    },
]


PHRASE_BANK = {
    "Triage and scope": [
        "Can we separate user impact from component health?",
        "How many users, which locations, and which business process are affected?",
        "What changed recently: deployment, configuration, certificate, DNS, firewall, identity policy, or vendor status?",
        "Do we have logs, timestamps, screenshots, error messages, and a reproducible path?",
    ],
    "Cautious root-cause language": [
        "Current evidence points to DNS, but we have not confirmed root cause yet.",
        "This appears to be a configuration issue rather than a platform outage.",
        "We have restored service; the contributing factors are still under review.",
        "I would avoid saying 'breach' until security confirms unauthorized access or data exposure.",
    ],
    "Pushback and risk": [
        "I understand the urgency, but broad admin access is not the right control.",
        "The shortcut reduces delivery risk today but increases security and audit risk.",
        "Can we approve a time-limited exception with monitoring and an expiration date?",
        "Before we make this change, we need a rollback plan and a communication owner.",
    ],
    "Incident bridge language": [
        "The immediate goal is service restoration; root-cause analysis comes after stabilization.",
        "The mitigation is in progress, and the next checkpoint is in 15 minutes.",
        "We need one owner for customer communication and one owner for technical recovery.",
        "Please post only confirmed facts in the incident channel; hypotheses should be labeled as hypotheses.",
    ],
    "Security and identity": [
        "Authentication succeeded, but authorization failed because the user lacks the required role.",
        "Least privilege protects the user, the system, and the audit trail.",
        "We should revoke sessions, reset credentials, and review sign-in logs before closing the incident.",
        "A vulnerability is confirmed, but we do not yet have evidence of exploitation.",
    ],
    "Business-facing explanations": [
        "RTO is how long recovery takes; RPO is how much data loss the business can tolerate.",
        "The application is healthy, but users cannot reach it because name resolution is inconsistent.",
        "The cost increase is mostly idle compute and longer log retention, not user growth.",
        "The change is technically simple, but the blast radius is large if it fails.",
    ],
}


WORKBOOK_TASKS = [
    "A user reports, 'Everything is down.' Rewrite the ticket with scope, impact, evidence, affected business process, and next owner.",
    "A remote user can connect to VPN but cannot reach one internal app. Write five triage questions and three likely hypotheses.",
    "A senior employee wants broad access to a financial database for one afternoon. Write a least-privilege response that still helps them finish the work.",
    "Cloud spend increases sharply after a new analytics environment launches. Prepare a short update with evidence, immediate actions, and longer-term controls.",
    "Security wants an urgent patch, but the business owner rejects downtime. Write a compromise plan with risk language and decision points.",
    "A phishing victim reports quickly. Write your first five sentences to the user and your first technical update to security.",
    "A firewall change is requested with vague source and destination information. Write clarification questions and a risk statement.",
    "A restore test meets the RTO but misses the RPO. Explain the problem to a non-technical business owner and recommend next steps.",
]


SOURCES = [
    "NIST Computer Security Resource Center Glossary and Cybersecurity Framework terminology.",
    "AWS Well-Architected Framework pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.",
    "Microsoft Learn Zero Trust and Microsoft Entra identity/access management guidance.",
    "Kubernetes documentation for Pods, Deployments, Services, Ingress, and container orchestration concepts.",
    "Google Site Reliability Engineering book chapters on SLOs, error budgets, incident response, and reliability tradeoffs.",
    "PeopleCert ITIL 4 practice areas for incident management, change enablement, service request management, and problem management.",
]


def add_course_opening(story: list) -> None:
    story += h1("Purpose and Teaching Position")
    story.append(
        p(
            "This EFSP curriculum is for high-level ESL learners working in general IT: service desk specialists, system administrators, network technicians, endpoint engineers, cloud operations staff, security analysts, technical support leads, IT managers, and IT-adjacent project or business partners."
        )
    )
    story.append(
        p(
            "The course is not a beginner computer class. It assumes learners know the work but need more precise English for live troubleshooting, escalations, risk discussions, documentation, post-incident reviews, vendor conversations, and cross-functional meetings."
        )
    )
    story.append(
        box(
            "Core language challenge",
            [
                "General IT English is full of compressed phrases: P1 bridge, DNS propagation, least privilege, conditional access, rollback plan, open a vendor severity case, noisy alert, RTO miss, firewall exception, and error-budget burn. Learners need to understand the words, but more importantly they need the workplace moves around the words: clarify, narrow scope, ask for evidence, protect users, state risk, and recommend a next step."
            ],
            "amber",
        )
    )
    story.append(h2("Course objectives"))
    story.append(bullets(COURSE_OBJECTIVES))


def add_general_it_principles(story: list) -> None:
    story += h1("General IT Communication Principles")
    story.append(h2("Translate symptoms into evidence"))
    story.append(
        p(
            "Users naturally describe pain, not architecture. 'The internet is down' may mean a browser issue, Wi-Fi issue, DNS issue, proxy issue, SaaS outage, identity failure, expired certificate, or local device problem. Strong IT English respects the user experience while converting the report into testable evidence."
        )
    )
    story.append(h2("Separate restoration from investigation"))
    story.append(
        bullets(
            [
                "During an incident, say what is affected, what is being mitigated, who owns the next action, and when the next update will arrive.",
                "After restoration, discuss root cause, contributing factors, detection gaps, process gaps, and durable corrective actions.",
                "Do not use final root-cause language while the team is still working from hypotheses.",
                "Use exact uncertainty: 'we have not seen evidence of data loss' is stronger and safer than 'there is no data loss' when logs are incomplete.",
            ]
        )
    )
    story.append(h2("Use decision-grade risk language"))
    story.append(
        table(
            [
                ["Weak sentence", "Decision-grade IT sentence"],
                ["It is risky.", "The risk is broad network exposure from an unrestricted source range; mitigation would require a narrower rule, monitoring, and an expiration date."],
                ["The patch can wait.", "The patch can wait only if we apply compensating controls, document risk acceptance, and schedule production within the agreed window."],
                ["The cloud bill is too high.", "Compute in non-production increased 42 percent, and untagged resources prevent owner accountability; we can stop idle instances today and enforce tags this sprint."],
                ["The user needs access.", "The user needs read-only access to customer reports until Friday, approved by the data owner and removed automatically after the review."],
            ],
            [2.2 * 72, 4.8 * 72],
        )
    )


def add_jargon_sections(story: list) -> None:
    story += h1("Nomenclature and Jargon")
    story.append(
        p(
            "Teach these terms as working vocabulary. Learners should be able to define the term, use it in a realistic sentence, ask one clarification question about it, and explain the business consequence."
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
                    "When learners say a system is down, slow, broken, unsafe, or fixed, ask for scope, evidence, timestamp, business impact, owner, and confidence level. The goal is not more English; it is more operational usefulness."
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
                "Learner explains their current IT role in 90 seconds, including users supported, systems owned, common incidents, and escalation paths.",
                "Learner defines twelve common IT terms and uses six in realistic workplace sentences.",
                "Learner handles a short role-play: a business stakeholder asks whether an outage is fixed and whether data was lost.",
            ]
        )
    )
    story.append(h2("Performance rubric"))
    story.append(
        table(
            [
                ["Skill", "Developing", "Proficient", "Strong"],
                ["Terminology", "Recognizes terms but uses them loosely.", "Uses common terms accurately in context.", "Defines terms, notices misuse, and adjusts for audience."],
                ["Triage", "Collects symptoms but misses scope or impact.", "Asks about impact, timeline, evidence, and recent changes.", "Builds hypotheses and assigns next owners clearly."],
                ["Risk language", "Uses vague risk words or alarmist language.", "Names likelihood, impact, exposure, and mitigation.", "Frames risk as a decision with controls and owner accountability."],
                ["Incident communication", "Gives long technical explanations during pressure.", "Reports impact, mitigation, owner, and next update.", "Controls bridge language and separates facts from hypotheses."],
                ["Documentation", "Writes updates that are hard to act on.", "Writes clear ticket and change notes.", "Writes concise operational records usable for review and audit."],
            ],
            [1.2 * 72, 1.9 * 72, 1.95 * 72, 1.95 * 72],
        )
    )
    story.append(h2("Capstone simulation"))
    story.append(
        p(
            "Learners lead a 25-minute incident and recovery scenario. A SaaS login problem affects a regional sales team, the vendor status page is ambiguous, some users report MFA loops, and a senior stakeholder asks for a workaround that may weaken security. The learner must triage scope, communicate impact, propose mitigations, push back on unsafe shortcuts, and write a final incident summary."
        )
    )
    story.append(h2("Source orientation for instructors"))
    story.append(bullets(SOURCES))


def instructor_guide() -> Path:
    story = cover(
        "General IT English",
        "Instructor guide for high-level ESL learners working in IT operations, service management, infrastructure, cloud, security, and support",
        "Audience: instructors, coaches, technical English trainers, IT learning partners, and team leads",
    )
    add_course_opening(story)
    add_general_it_principles(story)
    add_jargon_sections(story)
    add_module_details(story)
    add_assessment(story)
    return build_pdf(
        "efsp-general-it-english-instructor-guide.pdf",
        "EFSP General IT English - Instructor Guide",
        story,
    )


def participant_workbook() -> Path:
    story = cover(
        "General IT English",
        "Participant workbook: service language, infrastructure discussion, security risk, incident updates, and IT workplace practice",
        "Audience: advanced ESL learners working in IT operations, support, infrastructure, cloud, security, or adjacent roles",
    )
    story += h1("How to Use This Workbook")
    story.append(
        p(
            "This workbook helps you sound precise and credible in general IT conversations. The goal is not to use more jargon. The goal is to use the right term, ask better questions, explain risk calmly, and write updates that help people act."
        )
    )
    story.append(h2("Your starting point"))
    story.append(
        bullets(
            [
                "Which conversations are hardest for you: user calls, incident bridges, access reviews, change meetings, security escalations, vendor calls, or executive updates?",
                "Which IT terms do you understand when reading but avoid when speaking?",
                "When someone pressures you for a risky shortcut, do you become too indirect, too blunt, or too technical?",
                "What is one recent ticket or incident you wish you had explained more clearly?",
            ]
        )
    )
    story.append(p("Use the guided dialogue activities below. Every item has four choices and a rationale in the answer key; no open-ended writing is required."))
    story += h1("IT Stack Language")
    story.append(
        table(
            [
                ["Layer", "Useful verbs", "Example sentence"],
                ["User/device", "report, reproduce, capture, reset, verify", "The user can reproduce the issue only on the managed laptop."],
                ["Network", "resolve, route, block, allow, tunnel, inspect", "DNS resolves to the old address for some remote users."],
                ["Identity", "authenticate, authorize, grant, revoke, audit", "Authentication succeeded, but authorization failed because the user lacks the role."],
                ["Server/cloud", "provision, scale, patch, snapshot, restore", "The instance scaled up, but the storage volume is near saturation."],
                ["Application", "deploy, roll back, validate, monitor, log", "The application is healthy, but the load balancer health check is failing."],
                ["Security", "detect, contain, investigate, remediate, report", "We contained the account compromise and are reviewing sign-in logs."],
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
        "efsp-general-it-english-participant-workbook.pdf",
        "EFSP General IT English - Participant Workbook",
        story,
    )


def dialogue_lab() -> Path:
    story = cover(
        "General IT Dialogue Lab",
        "Realistic workplace dialogues, role-play cards, and debrief prompts for advanced ESL learners in IT teams",
        "Audience: instructors, coaches, peer practice groups, technical English cohorts, and IT teams",
    )
    story += h1("How to Run the Dialogue Lab")
    story.append(
        bullets(
            [
                "Use groups of three: IT speaker, counterpart, observer.",
                "Read the model dialogue once. Then replay it using the same situation but different facts from the learner's work.",
                "The observer listens for terminology accuracy, triage questions, evidence, risk language, audience awareness, and decision clarity.",
                "After each role-play, replay the hardest 30 seconds with a more precise sentence.",
            ],
            numbered=True,
        )
    )
    story.append(
        box(
            "Facilitator guardrail",
            [
                "Do not let learners hide behind vague technical nouns. Ask them to name the user impact, the evidence, the likely owner, the next action, and the confidence level."
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
                    "Did the learner name the issue precisely instead of repeating a vague symptom?",
                    "Did the learner ask for scope, evidence, timeline, impact, and recent changes?",
                    "Did the learner use risk language without panic or overconfidence?",
                    "Did the learner make a clear recommendation, owner, or next step?",
                ]
            )
        )
    story.append(PageBreak())
    add_answer_key(story, answer_key)
    return build_pdf(
        "efsp-general-it-dialogue-lab.pdf",
        "EFSP General IT Dialogue Lab",
        story,
    )


def quick_reference() -> Path:
    story = cover(
        "General IT Jargon Field Guide",
        "Quick reference for high-level ESL learners who need precise IT vocabulary and workplace meeting language",
        "Audience: advanced ESL learners in IT operations, service desk, infrastructure, cloud, endpoint, security, and platform roles",
    )
    story += h1("How to Use Jargon Well")
    story.append(
        bullets(
            [
                "Use the term only when it locates the issue more precisely.",
                "Pair jargon with evidence: log, metric, timestamp, screenshot, ticket, trace, affected user count, or business process.",
                "Define the term when speaking to non-technical stakeholders.",
                "Avoid vague IT blame. Name the layer, the owner, the business impact, and the next diagnostic step.",
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
                ["Incident vs problem", "An incident restores service; problem management investigates underlying cause or recurrence."],
                ["Severity vs priority", "Severity describes impact; priority combines impact, urgency, deadline, and business context."],
                ["Authentication vs authorization", "Authentication verifies identity; authorization determines allowed actions."],
                ["Vulnerability vs exploit", "A vulnerability is a weakness; an exploit is a way to use that weakness."],
                ["Alert vs incident", "An alert signals possible attention; an incident is confirmed service, security, or business impact requiring response."],
                ["RTO vs RPO", "RTO is acceptable recovery time; RPO is acceptable data loss measured in time."],
                ["Rollback vs roll forward", "Rollback returns to the previous known state; roll forward fixes by moving to a newer corrected state."],
                ["Logs vs metrics vs traces", "Logs are event records; metrics are measurements; traces follow a request across systems."],
            ],
            [2.25 * 72, 4.75 * 72],
        )
    )
    story += h1("Source Orientation")
    story.append(bullets(SOURCES))
    return build_pdf(
        "efsp-general-it-jargon-quick-reference.pdf",
        "EFSP General IT Jargon Field Guide",
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
