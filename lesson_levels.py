"""Shared editorial guidance for daily-lesson drafting and independent review.

These are English Ladder's teaching policies, informed by the Council of Europe's
CEFR Companion Volume (2020), vocabulary range and sociolinguistic appropriateness:
https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2020/16809ea0d4
They are contextual editorial judgements, not an automatic CEFR certification or
an assertion that every word has a single fixed proficiency level.
"""

LANGUAGE_POLICY_VERSION = '2026-09-07'
LEVEL_CHECKS = ('vocabulary', 'register', 'teaching_language', 'challenge')

COMMON_LANGUAGE_POLICY = (
    'Apply the target level to every learner-facing field: title, overview, reading, '
    'vocabulary definitions, grammar explanations, quiz questions, all three options, '
    'every feedback explanation, prediction and discussion prompts. '
    'Judge each term by its meaning and use in this context, familiarity, word partners '
    'and learning value. Word length, syllable counts and proper names alone do not '
    'establish difficulty. Essential news terms may need brief explanations near first '
    'use; avoid building a beginner reading around many unexplained specialist terms. '
    'Definitions must clarify the contextual sense using language the learner can '
    'understand, without circular definitions or a harder unexplained synonym. '
    'Choose a consistent register appropriate to the situation: neutral reporting for '
    'news, natural conversation for dialogue, and clear supportive language for teaching. '
    'Preserve distinctions such as suspected versus proven and possible versus certain '
    'at every level. Respect teen and adult learners; avoid baby talk, sensationalism, '
    'patronising praise and gratuitous slang. '
    'Different levels should offer different learning value through meaning, useful '
    'word combinations, sentence structure and reasoning. Essential words may recur '
    'across levels when useful; simply lengthening the same lesson or replacing ordinary '
    'words with rare synonyms does not create appropriate progression. '
    'Meet all sentence, vocabulary and quiz minimums without padding or abandoning '
    'the language policy. If the evidence supports too little suitable material, '
    'reject the draft rather than invent details or force irrelevant terminology.'
)

LANGUAGE_PROFILES = {
    'beginner': {
        'vocabulary': (
            'Target A1-A2, with a supported A2 news reading. Prefer common, concrete '
            'words and short, useful expressions that learners can reuse in daily life. '
            'Select vocabulary worth learning at this stage. Use familiar alternatives '
            'for nonessential technical terms, abstract nouns and opaque idioms. '
            'An indispensable news term is acceptable with a simple explanation; '
            'names, numbers and lists of rare subject terms must not fill the word list.'
        ),
        'register': (
            'Use straightforward, neutral everyday English suitable for adults. '
            'Prefer direct verbs and explicit subjects. Avoid bureaucratic phrasing, '
            'compressed headline language, idioms requiring cultural knowledge and '
            'sarcasm. Keep polite conversation natural and easy to reuse.'
        ),
        'teaching_language': (
            'Use short clauses and familiar connectors such as and, but, because and so. '
            'Aim for at most 18 words per reading sentence as an editing guide, not a '
            'reason to split an incomplete thought into fragments. Define grammar terms '
            'briefly or demonstrate the pattern with an example. Make instructions, '
            'options and feedback as accessible as the reading. Include a simple '
            'sentence frame in one discussion prompt and a hypothetical alternative '
            'to sharing personal experience.'
        ),
        'challenge': (
            'Test the main idea, clearly stated details, basic meaning in context and '
            'one useful grammar pattern. Use short, plausible answer choices. Avoid '
            'dense reasoning, double negatives, trick wording and dependence on '
            'outside cultural or specialist knowledge.'
        ),
    },
    'intermediate': {
        'vocabulary': (
            'Target B1-B2. Select useful general news and work vocabulary, common '
            'phrasal verbs, word combinations and moderately abstract terms that '
            'support explaining causes, comparisons and consequences. Give clear '
            'contextual definitions. Explain unfamiliar domain terms. Avoid a list '
            'dominated by elementary everyday words or unexplained specialist jargon.'
        ),
        'register': (
            'Use natural, neutral news English with clear connections between ideas. '
            'Introduce useful formal or informal expressions when the context warrants '
            'them, and identify their tone in the explanation when it affects use. '
            'Maintain a consistent voice; avoid unexplained shifts into slang or '
            'overly academic language.'
        ),
        'teaching_language': (
            'Use varied but manageable sentences, clear pronoun references, and '
            'cause, contrast and result links. Explain grammar in everyday language '
            'with a precise example. Keep definitions, questions and feedback clear '
            'enough that understanding the instructions is not the hardest part. '
            'Develop discussion beyond one-word answers without requiring expert knowledge.'
        ),
        'challenge': (
            'Combine comprehension with relationships between details, vocabulary '
            'in context, common word partnerships and grammar transfer to a new '
            'situation. Supported, clearly signalled inference is appropriate. '
            'Provide more development than a beginner paraphrase while preserving '
            'the source’s uncertainty and limits.'
        ),
    },
    'advanced': {
        'vocabulary': (
            'Target C1+. Prioritise precise, transferable terms, collocations, '
            'multiple meanings, connotations and expressions whose register matters. '
            'A familiar word can be valuable when its contextual sense or usage '
            'offers a meaningful advanced distinction. Avoid elementary dictionary '
            'glosses as filler and rare, inflated synonyms selected merely to sound '
            'difficult. Explain necessary specialist language clearly.'
        ),
        'register': (
            'Use polished, natural reporting and analysis with accurate attribution '
            'and calibrated certainty. Formality must serve the subject and audience. '
            'Advanced English can be neutral, conversational or formal as appropriate; '
            'it is not automatically academic or ornate. Explain meaningful register '
            'contrasts, connotations or diplomatic phrasing when relevant.'
        ),
        'teaching_language': (
            'Use controlled complex sentences and cohesive arguments while keeping '
            'definitions and feedback concise and illuminating. Explain subtle '
            'differences in meaning, emphasis, implication or word partnership; do '
            'not merely exchange one difficult word for another. Discuss grammar '
            'or style through its effect on meaning in the actual passage.'
        ),
        'challenge': (
            'Develop supported inference, stance, qualification, cause and effect, '
            'and distinctions between near-synonyms or registers. Use plausible '
            'distractors and explain why each fails. Include substantive learning '
            'beyond recall of elementary facts; never require unsupported assumptions '
            'or make every question difficult through convoluted wording.'
        ),
    },
}


def format_language_policy(level):
    profile = LANGUAGE_PROFILES[level['name'].lower()]
    return (f"Language policy {LANGUAGE_POLICY_VERSION} for {level['name']} ({level['cefr']}):\n"
            + COMMON_LANGUAGE_POLICY + '\n'
            + '\n'.join(f'{name}: {profile[name]}' for name in LEVEL_CHECKS))
