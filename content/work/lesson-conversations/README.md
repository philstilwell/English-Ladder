# Lesson Conversations

Each course JSON file contains `module-1` through `module-8`, matching the existing lesson order in `work_curriculum.load_tracks()`.

Each module contains:

- Three original fictional `conversations`, each with a descriptive `title`, a specific `setting`, and exactly ten `turns`. Each turn is `[professional role, speech]`, not a visual line whose length depends on the screen.
- One `additional_scenario` with a title, brief, two role instructions, a possible opening, three success checks, and a complication. This supplements the existing lesson case; it does not replace it.

`work_lesson_conversations.py` validates and renders the material. The webpages use native, initially collapsed `details` elements. The workbook and conversation lab print the same scripts in full. Teacher guides list the conversations and include the second scenario for facilitation.

Rebuild the guides and webpages with `npm run build:work`. All four PDF covers use the original profession artwork from `assets/work/professional-icons.png`; English Ladder branding and embedded fonts remain in place.

The scripts are language-learning examples, not transcripts, operational instructions, or individualized professional advice. New scenario facts must be stated clearly and remain consistent throughout an exchange.

## Selected Terminology Checks

- The pharmaceutical distinction between routinely collected health data and evidence derived from its analysis was checked against the [FDA's real-world evidence definitions](https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence).
- The AI-development examples distinguish untrusted document instructions from authorized tasks and do not claim that prompts alone guarantee protection, consistent with [OWASP's prompt-injection guidance](https://genai.owasp.org/llmrisk/llm01-prompt-injection/).
- Financial-advice disclosure terminology was checked against Investor.gov's descriptions of [Form CRS](https://www.investor.gov/introduction-investing/investing-basics/glossary/form-crs) and [Form ADV](https://www.investor.gov/introduction-investing/investing-basics/glossary/form-adv). The former is a relationship summary; Form ADV also contains registration and other adviser disclosures, including the client brochure.
- The insurance course's definitions of policy and claim were corrected to their insurance senses, using the [NAIC consumer explanation](https://content.naic.org/consumer/how-does-insurance-work) and [insurance glossary](https://content.naic.org/glossary-insurance-terms).
