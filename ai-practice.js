/* Copy published, inspectable prompt text. No AI requests, account, or draft access. */
(() => {
  'use strict';
  const languages = { en: 'English', ja: 'Japanese', ko: 'Korean', 'zh-Hans': 'Simplified Chinese', es: 'Spanish', 'pt-BR': 'Brazilian Portuguese' };
  const languageKey = 'english-ladder-vocabulary-language-v1';
  const supported = value => Object.hasOwn(languages, value) ? value : 'en';
  function savedLanguage() {
    try { return supported(localStorage.getItem(languageKey)); } catch { return 'en'; }
  }
  let language = supported(document.documentElement.dataset.definitionLanguage || savedLanguage());
  function localizePrompt(original) {
    if (language === 'en') return original;
    const name = languages[language];
    return original + `\n\nEXPLANATION LANGUAGE AND DEPTH
My explanation language is ${name}. Use ${name} for teaching guidance, hints, feedback, and deeper explanations. This replaces requests above for English-only or plain-English explanations, brief explanations, or an explanation-only word limit. Keep the specified number of activities and practice turns.

Keep target English words, example sentences, reading passages, dialogue lines, and answer options in English at the supplied study level. Add a ${name} gloss where it clarifies meaning, without replacing the English practice. Deeper explanation must not make the English practice harder.

Explain the relevant teaching point step by step in clear, natural ${name}, using short paragraphs or bullets. Connect the meaning to this lesson's context. For vocabulary, explain useful word partners and a likely near-synonym confusion. For grammar, explain how the form changes meaning and compare two short English examples. For dialogue or writing, explain tone, politeness, and register: when wording sounds casual, neutral, or formal. For reading, distinguish what the passage states from an inference or something it leaves uncertain. Choose only the explanations relevant to the current activity; do not deliver all of these lessons at once.

After my attempt, explain why my actual choice or wording works or needs revision, and clarify a likely misunderstanding in ${name}. Before an attempt or retry, give only the permitted hint; do not reveal an answer that the activity asks you to withhold. Preserve the original response format, multiple-choice rules where specified, one-question-at-a-time pacing, and stop-and-wait instructions. Keep all evidence limits, factual qualifications, and course boundaries. Do not infer my nationality, culture, or English ability from this language choice.`;
  }
  // Both the workplace chooser and static cards use the same authored guidance.
  window.EnglishLadderAI = Object.freeze({ localizePrompt });
  const prompts = [...document.querySelectorAll('[data-ai-copy-text], [data-copy-finished]')].map(button => {
    const node = document.getElementById(button.dataset.aiCopyText || button.dataset.copyFinished);
    const status = button.closest('[data-ai-card], .finished-prompt')?.querySelector('[data-ai-copy-status], [data-finished-status]');
    return node ? { node, original: node.textContent, status } : null;
  }).filter(Boolean);
  const notices = [...document.querySelectorAll('.ai-extension-body, [data-ai-workshop], .finished-prompts, .finished-dialogue-library')].map(section => {
    const notice = document.createElement('p');
    notice.className = 'ai-extension-note';
    notice.dataset.aiLanguageNotice = '';
    section.querySelector('p')?.after(notice);
    return notice;
  });
  function renderLanguage() {
    prompts.forEach(({ node, original, status }) => {
      node.textContent = localizePrompt(original);
      if (status) status.textContent = '';
    });
    notices.forEach(notice => {
      notice.textContent = language === 'en' ? 'AI explanations in English.' : `Deeper AI explanations in ${languages[language]}; practice stays in English.`;
    });
    window.dispatchEvent(new CustomEvent('ai-explanation-language-changed'));
  }
  function changeLanguage(value) {
    const next = supported(value);
    if (next === language) return;
    language = next;
    renderLanguage();
  }
  window.addEventListener('vocabulary-language-changed', event => changeLanguage(event.detail?.language));
  window.addEventListener('storage', event => {
    if (event.key === languageKey || event.key === null) changeLanguage(savedLanguage());
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted) changeLanguage(savedLanguage());
  });
  renderLanguage();
  document.querySelectorAll('[data-ai-copy-text]').forEach(button => {
    const card = button.closest('[data-ai-card]');
    const prompt = document.getElementById(button.dataset.aiCopyText);
    const status = card?.querySelector('[data-ai-copy-status]');
    if (!prompt || !status) return;
    button.hidden = false;
    button.addEventListener('click', async () => {
      const text = prompt.textContent;
      button.disabled = true;
      status.textContent = '';
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(text);
        status.textContent = text === prompt.textContent
          ? 'Prompt copied. Paste it into your chosen AI.'
          : 'The earlier prompt was copied. Copy again to use your new language selection.';
      } catch (_) {
        prompt.closest('details').open = true;
        prompt.focus();
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(prompt);
        selection?.removeAllRanges(); selection?.addRange(range);
        status.textContent = 'Automatic copying is unavailable. The prompt is selected: press Ctrl+C or Command+C, or use your device’s Copy command.';
      } finally {
        button.disabled = false;
      }
    });
  });
})();
