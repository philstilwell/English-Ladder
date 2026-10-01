# Learner-Book Expansion

Requested scope: all 65 courses other than the approved Cross-Cultural
Leadership book. Work is sequential; the user declined parallel assistants.

## Completed

- AI Development English: 102 pages, eight original 20-turn dialogues,
  192 vocabulary entries, 128 phrases, 112 uniform-width bank gaps,
  56 multiple-choice questions, and explained keys for all 168 items.
  Output: `output/pdf/ai-development-english-book.pdf`.
- General IT English: 102 pages with the same counts and explained keys,
  eight field-specific extended conversations, and the matching illustration.
  Output: `output/pdf/general-it-english-book.pdf`.
- Law English: 102 pages with the same counts and explained keys, covering
  intake, litigation, discovery, research, contracts, investigations, and
  settlement alongside factual and legal precision.
  Output: `output/pdf/law-english-book.pdf`.
- Finance English: 102 pages with the same counts and explained keys,
  covering financial commentary, close, forecasting, treasury, performance,
  credit, controls, and valuation with explicit calculation bases.
  Output: `output/pdf/finance-english-book.pdf`.
- Financial Advice English: 102 pages with the same counts and explained keys,
  covering discovery, fees, risk, retirement illustrations, portfolio reviews,
  product comparisons, family roles, and substantive complaint responses.
  Output: `output/pdf/financial-advice-english-book.pdf`.
- Marketing English: 102 pages with the same counts and explained keys,
  covering audience strategy, evidence-backed messaging, campaign coordination,
  editorial decisions, attribution, lead handoffs, test results, and publication holds.
  Output: `output/pdf/marketing-english-book.pdf`.
- Real Estate English: 102 pages with the same counts and explained keys,
  covering representation, objective searches, comparable sales, fair-housing
  language, offer conditions, inspection findings, closing, and maintenance follow-up.
  Output: `output/pdf/real-estate-english-book.pdf`.
- Corporate Strategy English: 102 pages with the same counts and explained keys,
  covering mandates, trade-offs, market boundaries, unit economics, capital allocation,
  acquisition logic, scenarios, and bounded board decisions.
  Output: `output/pdf/corporate-strategy-english-book.pdf`.
- Pharmaceutical English: 102 pages with the same counts and explained keys,
  covering development evidence, regulatory questions, trial documents, readouts,
  safety intake, batch review, promotional claims, and access evidence.
  Output: `output/pdf/pharmaceutical-english-book.pdf`.
- Healthcare Administration English: 102 pages with the same counts and explained keys,
  covering scheduling, claims, capacity, safety reviews, privacy, patient communication,
  care coordination, and accurate board reporting.
  Output: `output/pdf/healthcare-administration-english-book.pdf`.
- Nursing and Allied Health English: 102 pages with the same counts and explained keys,
  covering handoffs, escalation, allergy discrepancies, teach-back, interprofessional
  rounds, objective records, family communication, and fair safety reviews.
  Output: `output/pdf/nursing-allied-health-english-book.pdf`.

- Biotechnology English: 102 pages with the same counts and explained keys,
  covering platform evidence, assay reproducibility, biomarker claims, preclinical
  findings, scale-up, intellectual property, board updates, and partnering terms.
  Output: `output/pdf/biotechnology-english-book.pdf`.

- Medical Devices English: 102 pages with the same counts and explained keys,
  covering design inputs, risk distinctions, verification and validation, usability,
  regulatory status, complaints, material holds, and training-scope boundaries.
  Output: `output/pdf/medical-devices-english-book.pdf`.

- Manufacturing English: 102 pages with the same counts and explained keys,
  covering output measures, lean trials, scrap and rework, root-cause evidence,
  maintenance scheduling, safety clarification, drawing revisions, and shift handoffs.
  Output: `output/pdf/manufacturing-english-book.pdf`.

- Supply Chain and Logistics English: 102 pages with the same counts and explained keys,
  covering forecast bias, supplier commitments, stock availability, order balances,
  freight estimates, customs records, backup readiness, and executive planning decisions.
  Output: `output/pdf/supply-chain-logistics-english-book.pdf`.

- Human Resources English: 102 pages with the same counts and explained keys,
  covering job-related hiring, onboarding, factual feedback, employee concerns,
  pay calculations, adjustment requests, task disputes, and restructuring messages.
  Output: `output/pdf/human-resources-english-book.pdf`.

- Project Management English: 102 pages with the same counts and explained keys,
  covering scope, dependencies, risk and issues, governance, change decisions,
  executive reporting, acceptance evidence, and measurable delivery improvements.
  Output: `output/pdf/project-management-english-book.pdf`.

- Engineering English: 102 pages with the same counts and explained keys,
  covering measurable requirements, tolerance evidence, failure investigations,
  prototype claims, cost trade-offs, compliance scope, field updates, and interfaces.
  Output: `output/pdf/engineering-english-book.pdf`.

- Semiconductor English: 102 pages with the same counts and explained keys,
  covering fabrication stages, CD measurement, process windows, yield comparisons,
  contamination evidence, tool matching, qualification status, and foundry handoffs.
  Output: `output/pdf/semiconductor-english-book.pdf`.

- Software Product Management English: 102 pages with the same counts and explained keys,
  covering discovery, prioritization, acceptance criteria, funnel interpretation,
  experiment decisions, release readiness, API trade-offs, and executive recommendations.
  Output: `output/pdf/software-product-management-english-book.pdf`.

- Cybersecurity English: 102 pages with the same counts and explained keys,
  covering alert triage, containment, vulnerability priorities, vendor access,
  threat models, control evidence, phishing intake, and executive risk briefings.
  Output: `output/pdf/cybersecurity-english-book.pdf`.

- Data Analytics and Business Intelligence English: 102 pages with the same counts and explained keys,
  covering metric definitions, data quality, executive dashboards, causal claims,
  SQL joins, experiment results, data access, and evidence-based recommendations.
  Output: `output/pdf/data-analytics-business-intelligence-english-book.pdf`.

- Education Administration English: 102 pages with the same counts and explained keys,
  covering admissions, assessment alignment, support records, guardian communication,
  rubric calibration, student-record access, review evidence, and staffing trade-offs.
  Output: `output/pdf/education-administration-english-book.pdf`.

- Higher Education and Research English: 102 pages with the same counts and explained keys,
  covering study design, pilot aims, laboratory discrepancies, research ethics,
  authorship, peer review, reproducible data, and conference challenges.
  Output: `output/pdf/higher-education-research-english-book.pdf`.

## Remaining

41 books remain. The next course in the canonical inventory is `hospitality-tourism`.
Use `work_curriculum.load_tracks()` for the complete course list and module
order. No other course should be represented as converted or complete.

## Checks and Publication

The new renderer reuses the approved design, embedded fonts, English Ladder
branding, existing course illustrations, uniform blanks, and page references.
The leadership book remains unchanged. The new books are stored separately from
published website downloads, which have not been replaced.

Run `python3 -m unittest discover -s tests -p '*book*.py' -v` for the shared
and book-specific checks. Render and inspect every completed book before
marking it complete. Keep content sources separate and field-specific.
