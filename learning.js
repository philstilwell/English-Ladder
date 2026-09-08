/* Progressive enhancement: every story remains readable without JavaScript. */
(() => {
  "use strict";
  const stages = ["read", "practice", "discuss"];
  const definitionLanguages = { en: "English", ja: "Japanese", ko: "Korean", "zh-Hans": "Chinese", es: "Spanish", "pt-BR": "Portuguese" };
  const languageKey = "english-ladder-vocabulary-language-v1";
  const vocabularyViews = [];
  function supportedLanguage(value) {
    return Object.hasOwn(definitionLanguages, value) ? value : "en";
  }
  function savedLanguage() {
    try { return supportedLanguage(localStorage.getItem(languageKey)); } catch { return "en"; }
  }
  let definitionLanguage = savedLanguage();
  document.documentElement.dataset.definitionLanguage = definitionLanguage;
  function changeDefinitionLanguage(language, save = false) {
    definitionLanguage = supportedLanguage(language);
    if (save) {
      try { localStorage.setItem(languageKey, definitionLanguage); } catch { /* The controls still work on this page. */ }
    }
    vocabularyViews.forEach(update => update(definitionLanguage));
    document.documentElement.dataset.definitionLanguage = definitionLanguage;
    window.dispatchEvent(new CustomEvent("vocabulary-language-changed", { detail: { language: definitionLanguage } }));
  }
  window.addEventListener("storage", (event) => {
    if (event.key === languageKey || event.key === null) changeDefinitionLanguage(savedLanguage());
  });
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) changeDefinitionLanguage(savedLanguage());
  });
  const featureStart = document.querySelector("#feature-start");
  document.querySelectorAll('input[name="feature-level"]').forEach((input) => {
    input.addEventListener("change", () => {
      if (featureStart && ["beginner", "intermediate", "advanced"].includes(input.value)) {
        const href = input.dataset.lessonHref;
        if (href && /^(?:stories\/[a-z-]+\/)?(?:beginner|intermediate|advanced)\.html(?:#lesson-\d{4}-\d{2}-\d{2})?$/.test(href)) {
          featureStart.setAttribute("href", href);
        }
      }
    });
  });

  document.querySelectorAll(".daily-lesson").forEach((lesson, lessonIndex) => {
    const panels = stages.map((stage) => lesson.querySelector(`[data-stage="${stage}"]`));
    if (panels.some((panel) => !panel)) return;
    const content = lesson.querySelector(".lesson-content");
    const nav = document.createElement("nav");
    nav.className = "learning-flow";
    nav.setAttribute("aria-label", "Lesson steps");
    const stepButtons = stages.map((stage, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = `${index + 1}. ${stage[0].toUpperCase() + stage.slice(1)}`;
      panels[index].id = `learning-${lessonIndex}-${stage}`;
      button.setAttribute("aria-controls", panels[index].id);
      button.addEventListener("click", () => showStage(index, true));
      nav.append(button);
      return button;
    });
    content.prepend(nav);
    function showStage(index, focus) {
      panels.forEach((panel, panelIndex) => {
        panel.hidden = panelIndex !== index;
        if (panelIndex === index) stepButtons[panelIndex].setAttribute("aria-current", "step");
        else stepButtons[panelIndex].removeAttribute("aria-current");
      });
      if (focus) {
        const heading = panels[index].querySelector("h2, h3");
        if (heading) {
          heading.tabIndex = -1;
          heading.focus({ preventScroll: true });
        }
        nav.scrollIntoView({ block: "start", behavior: "auto" });
      }
    }
    panels.forEach((panel, index) => {
      const actions = document.createElement("div");
      actions.className = "stage-actions";
      if (index > 0) {
        const back = document.createElement("button");
        back.type = "button";
        back.className = "secondary-button";
        back.textContent = "← " + (index === 1 ? "Read again" : "Back to practice");
        back.addEventListener("click", () => showStage(index - 1, true));
        actions.append(back);
      }
      const next = document.createElement("button");
      next.type = "button";
      next.className = "primary-button";
      next.textContent = ["Check your understanding →", "Discuss the story →", "Finish lesson ✓"][index];
      if (index === 2) {
        next.dataset.finishLesson = "";
        next.setAttribute("aria-pressed", "false");
      }
      next.addEventListener("click", () => {
        if (index < 2) showStage(index + 1, true);
        else {
          const message = panel.querySelector(".completion-message");
          const completed = next.getAttribute("aria-pressed") !== "true";
          message.hidden = false;
          message.textContent = completed ? "Lesson marked complete." : "Lesson marked unfinished.";
          message.dataset.completionState = completed ? "complete" : "unfinished";
          next.textContent = completed ? "Completed ✓" : "Finish lesson ✓";
          next.setAttribute("aria-pressed", String(completed));
          window.dispatchEvent(new CustomEvent("lesson-practiced", { detail: { lesson, completed } }));
          if (completed && !panel.querySelector(".next-study")) {
            const link = document.createElement("a"); link.className = "next-study text-link";
            const root = new URL(document.querySelector("script[src*=\"site.js\"]")?.src || "site.js", location.href);
            link.href = new URL("archive.html", root).href; link.textContent = "Choose another story →";
            panel.append(link);
          }
          if (!completed) panel.querySelector(".next-study")?.remove();
        }
      });
      actions.append(next);
      panel.append(actions);
    });

    // Definitions come from this lesson's own vocabulary, never from remote text.
    const vocabulary = new Map();
    lesson.querySelectorAll(".vocab-term").forEach((term) => {
      const label = term.textContent.replace(/^\s*\d+\.\s*/, "").replace(/\s*\(.*\):?\s*$/, "").trim();
      let definition = "";
      let sibling = term.nextSibling;
      while (sibling && sibling.nodeName !== "BR" && !(sibling.nodeType === 1 && sibling.classList.contains("vocab-term"))) {
        definition += sibling.textContent;
        sibling = sibling.nextSibling;
      }
      const span = term.nextElementSibling?.classList.contains("vocab-definition") ? term.nextElementSibling : null;
      const definitions = { en: span ? span.textContent.trim() : definition.trim() };
      if (span) {
        try {
          const translations = JSON.parse(span.dataset.translations || "{}");
          for (const language of Object.keys(definitionLanguages).filter(value => value !== "en")) {
            if (typeof translations?.[language] === "string" && translations[language].trim()) definitions[language] = translations[language];
          }
        } catch { /* Damaged or missing translations leave the English definition readable. */ }
      }
      if (label && definitions.en) vocabulary.set(label.toLowerCase(), { definitions, span, popups: [] });
    });
    const reading = panels[0].querySelector(".section");
    let wordCount = 0;
    reading?.querySelectorAll("p strong").forEach((word, index) => {
      const entry = vocabulary.get(word.textContent.trim().toLowerCase());
      if (!entry) return;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "word-button";
      button.textContent = word.textContent;
      button.setAttribute("aria-expanded", "false");
      const explanation = document.createElement("span");
      explanation.className = "word-definition";
      explanation.id = `word-${lessonIndex}-${index}`;
      explanation.textContent = ` (${entry.definitions.en}) `;
      explanation.lang = "en";
      entry.popups.push(explanation);
      explanation.hidden = true;
      button.setAttribute("aria-controls", explanation.id);
      button.addEventListener("click", () => {
        explanation.hidden = !explanation.hidden;
        button.setAttribute("aria-expanded", String(!explanation.hidden));
      });
      button.addEventListener("keydown", (event) => {
        if (event.key === "Escape") { explanation.hidden = true; button.setAttribute("aria-expanded", "false"); }
      });
      word.replaceWith(button, explanation);
      wordCount += 1;
    });
    const vocabularyBox = lesson.querySelector(".vocab-box");
    if (vocabularyBox && [...vocabulary.values()].some(entry => entry.span)) {
      vocabularyBox.id = `vocabulary-${lessonIndex}`;
      const controls = document.createElement("div");
      controls.className = "vocabulary-languages";
      controls.setAttribute("role", "group");
      controls.setAttribute("aria-label", "Definition language");
      const languageButtons = Object.entries(definitionLanguages).map(([language, label]) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "vocabulary-language";
        button.dataset.definitionLanguage = language;
        button.textContent = label;
        button.setAttribute("aria-controls", vocabularyBox.id);
        if (language === "zh-Hans" || language === "pt-BR") {
          button.title = language === "zh-Hans" ? "Simplified Chinese" : "Brazilian Portuguese";
          button.setAttribute("aria-label", button.title);
        }
        button.addEventListener("click", () => changeDefinitionLanguage(language, true));
        controls.append(button);
        return button;
      });
      const status = document.createElement("p");
      status.className = "vocabulary-language-status";
      status.setAttribute("role", "status");
      status.setAttribute("aria-live", "polite");
      status.setAttribute("aria-atomic", "true");
      vocabularyBox.before(controls, status);
      function updateVocabulary(language) {
        let missing = 0;
        for (const entry of vocabulary.values()) {
          const actualLanguage = entry.definitions[language] ? language : "en";
          if (actualLanguage !== language) missing += 1;
          if (entry.span) {
            entry.span.textContent = entry.definitions[actualLanguage];
            entry.span.lang = actualLanguage;
          }
          for (const popup of entry.popups) {
            popup.textContent = ` (${entry.definitions[actualLanguage]}) `;
            popup.lang = actualLanguage;
          }
        }
        languageButtons.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.definitionLanguage === language)));
        const label = { "zh-Hans": "Simplified Chinese", "pt-BR": "Brazilian Portuguese" }[language] || definitionLanguages[language];
        status.textContent = missing ? `${label}: ${missing} ${missing === 1 ? "definition is" : "definitions are"} unavailable. English is shown instead.` : `Definitions in ${label}.`;
      }
      vocabularyViews.push(updateVocabulary);
      updateVocabulary(definitionLanguage);
    }
    const hint = panels[0].querySelector("[data-word-hint]");
    if (hint && wordCount) {
      hint.hidden = false;
      reading.before(hint);
    }
    lesson.addEventListener("click", (event) => {
      if (!event.target.closest(".quiz-card button")) return;
      const questions = [...panels[1].querySelectorAll(".quiz-question")];
      const answered = questions.filter((q) => q.querySelector('[aria-pressed="true"]'));
      const correct = answered.filter((q) => q.querySelector('[aria-pressed="true"]')?.dataset.bg === "#e6ffe6");
      const progress = panels[1].querySelector(".practice-progress");
      if (progress) progress.textContent = `${answered.length} of ${questions.length} questions answered · ${correct.length} correct. You can try again.`;
    });
    showStage(0, false);
  });
  function openLinkedLesson() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const lesson = id ? document.getElementById(id) : null;
    if (lesson?.classList.contains("daily-lesson")) {
      lesson.open = true;
      lesson.scrollIntoView({ block: "start", behavior: "auto" });
    }
  }
  openLinkedLesson();
  window.addEventListener("hashchange", openLinkedLesson);
})();
