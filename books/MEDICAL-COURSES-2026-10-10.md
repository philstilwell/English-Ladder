# Six Medical-Profession Courses

Added six independently authored courses to the existing 66-course collection.
The books and webpages share the same specialty material. These are fictional
professional-English teaching cases, not clinical guidance, clinical training,
or a professional-content certification.

## Scope

| Course | Eight core situations | Additional extended conversations |
| --- | --- | --- |
| General practitioners | Visit agenda; symptom history; medicine reconciliation; uncertain results; antibiotic expectations; screening; mental-health discussion; referral follow-up | Qualified interpretation; a work note and privacy; an unanswered result call |
| Oncologists | New diagnosis; stage and grade; biomarkers; treatment intent; urgent symptom handoff; response assessment; trial consent; palliative care | Second-opinion records; hospital-to-clinic handoff; financial burden |
| Cardiologists | Urgent handoff; rhythm monitoring; ejection fraction; atrial-fibrillation treatment goals; angiography consent; heart-failure plan; risk communication; rehabilitation | Device alerts; conflicting medicine instructions; advanced-care priorities |
| X-ray technicians | Identity and laterality; movement limitations; pregnancy-screening privacy; child cooperation; portable examinations; image-quality review; reporting boundaries; labeling near miss | Interpreted positioning instructions; a downtime worklist; a request to stop |
| Pediatricians | Child and caregiver histories; growth charts; developmental screening; vaccine concerns; liquid-medicine units; adolescent privacy; a school asthma plan; urgent infant change | Transition to adult services; school-report sharing; feeding-history sources |
| Obstetricians | Pregnancy history and dating; prenatal screening; urgent symptoms; gestational-diabetes testing; birth preferences and consent; labor handoff; postpartum concerns; confirmed pregnancy loss | Private interpreted discussion; contraception priorities; an uncertain ultrasound referral |

## Material Per Course

- One 114-page learner book with embedded fonts, English Ladder branding,
  Phil Stilwell's copyright, a linked contents page, and a vocabulary index.
- Eight 20-turn core dialogues and three additional 20-turn dialogues.
- Eleven separately situated four-turn follow-up exchanges.
- 192 vocabulary/collocation entries: 144 specialty entries plus six core
  communication terms repeated across eight lessons, giving 150 distinct terms.
- 128 phrase entries, including repeated reusable communication frames.
- 100 explained choice questions and 98 extended-dialogue gaps on the webpage.
- 24 separately written ten-turn webpage conversations, closed by default.
- Four primary-source references for terminology and communication context.
- One original native-generated profession illustration used in the directory,
  category list, course heading, sticky menu, and book cover.

The books retain the established A-F sequence, uniform 160-point printed
blanks, shuffled word banks, short ordered keys, and page-linked explanations.
No open-ended writing response is required. The site's optional AI prompt
previews remain read-only, and no learner progress or answer memory is added.

## Editorial Checks

The cases distinguish reported information from verified findings, uncertainty
from reassurance, screening from diagnosis, and receipt from accepted handoff.
Urgent scenarios keep the relevant response active; a language task must not
delay care. No exercise supplies a treatment regimen, clinical cutoff, or dose
calculation for clinical use. Privacy and consent examples retain jurisdiction
and setting qualifications rather than asserting a universal rule.

The cardiology risk comparison is explicitly fictional arithmetic, not an
intervention estimate: 40 versus 30 events per 1,000 over five years gives a
one-percentage-point absolute difference and a 25% relative reduction. The
follow-up uses 20 versus 15, with the same relative but a different absolute
difference. Denominators and periods are kept explicit.

The final language pass removed classroom-only phrasing from selected spoken
turns. The regression tests also identified and corrected 14 answer
explanations that referred to an option's original position before shuffling.
The explanations now describe the relevant meaning rather than a position.

Sources include AHRQ, AAFP, CDC, NCI, the American Heart Association, AAP's
HealthyChildren, ACOG, ASRT, and RadiologyInfo. The source titles, links, scope
notes, and check date appear in the books. These references do not endorse the
fictional cases. No clinical specialist certification is claimed.

## Verification Record

The structural PDF audit checks every page, all embedded fonts, branded
footers, internal links, uniform blank geometry, vocabulary, phrases, and
explained keys. Public PDFs are compared with the rebuilt master copies.
See `docs/medical-pdf-audit-2026-10-10.json` for file hashes and results.

Visual PDF review covers pages 1, 4, 5, 7, 10, 11, 12, 76, 77, 86, 101,
and 114 of each book, supplemented by the answer pages changed during review.
This is a visual sample, not a claim that all 684 pages received a separate
manual visual inspection.

The browser audit checks all 79 work directory/category/course pages at
320, 390, 768, and 1280 pixels, expanded lessons, choice and cloze feedback,
reset controls, keyboard navigation, deep links, copying, and reading without
JavaScript. New checks verify both course icons, equal collage cells, and
the sticky lesson menu at the prompt section. Screenshots of all six new
courses and the directory were reviewed at mobile and desktop widths.
See `docs/medical-browser-audit-2026-10-10.json`.

## Rebuild

Build the six slugs with `build_industry_books.py`; publish them with
`work_books.publish_books(MEDICAL_SLUGS)`; then run
`generate_efsp_web_pages.py`. Run `audit_work_books.py --published` with the
same six slugs, `tests.test_work_medical`, the regular test suites, and
`audit_work_browser.cjs`. The browser audit accepts `AUDIT_OUTPUT` and
`AUDIT_REPORT` to avoid replacing another review's evidence.
