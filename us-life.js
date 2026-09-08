(() => {
    "use strict";
    const STORAGE_KEY = "english-ladder-vocabulary-language-v1";
    const LEGACY_KEY = "englishLadder.usLife.explanationLanguage";
    const languages = {
        en: { label: "English only", lang: "en" },
        ja: { label: "Japanese", lang: "ja", rememberLabel: "大切なポイント", practiceLabel: "声に出す練習" },
        ko: { label: "Korean", lang: "ko", rememberLabel: "핵심 내용", practiceLabel: "소리 내어 연습하기" },
        "zh-Hans": { label: "Simplified Chinese", lang: "zh-Hans", rememberLabel: "重点", practiceLabel: "开口练习" },
        es: { label: "Spanish", lang: "es", rememberLabel: "Puntos clave", practiceLabel: "Practica en voz alta" },
        "pt-BR": { label: "Brazilian Portuguese", lang: "pt-BR", rememberLabel: "Pontos principais", practiceLabel: "Pratique em voz alta" },
    };
    const supported = value => Object.hasOwn(languages, value) ? value : "en";
    let explanations = {};
    try {
        const parsed = JSON.parse(document.querySelector("[data-us-life-translations]")?.textContent || "{}");
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) explanations = parsed;
    }
    catch { /* The English lesson and language invitation remain available. */ }

    function savedLanguage() {
        try {
            let value = localStorage.getItem(STORAGE_KEY);
            if (value === null) {
                const legacy = localStorage.getItem(LEGACY_KEY);
                if (["en", "ja", "zh"].includes(legacy)) {
                    value = legacy === "zh" ? "zh-Hans" : legacy;
                    try { localStorage.setItem(STORAGE_KEY, value); localStorage.removeItem(LEGACY_KEY); } catch { /* This page still works. */ }
                }
            }
            return supported(value);
        } catch { return "en"; }
    }

    function createElement(tagName, className, textContent) {
        const element = document.createElement(tagName);
        if (className) element.className = className;
        if (textContent !== undefined) element.textContent = textContent;
        return element;
    }

    function renderExplanation(container, languageKey) {
        const content = container.querySelector("[data-life-explanation-content]");
        if (!content) return;
        const language = languages[languageKey];
        const unit = explanations?.[container.dataset.explanation];
        const explanation = unit?.translations?.[languageKey];
        container.hidden = languageKey === "en";
        container.closest(".us-life-module")?.classList.toggle("english-only", languageKey === "en");
        content.replaceChildren();
        content.lang = "en";
        if (languageKey === "en") {
            return;
        }
        if (!explanation || typeof explanation.heading !== "string" || !Array.isArray(explanation.points) ||
            explanation.points.length !== 3 || !explanation.points.every(point => typeof point === "string" && point.trim())) {
            content.append(createElement("p", "language-empty", `${language.label} explanations are unavailable for this unit. You can choose another language or use the English lesson.`));
            return;
        }
        content.lang = language.lang;
        const heading = createElement("h3", null, explanation.heading);
        const remember = createElement("strong", "language-subhead", language.rememberLabel);
        const list = createElement("ul", "language-points");
        explanation.points.forEach(point => list.append(createElement("li", null, point)));
        const practiceLabel = createElement("strong", "language-subhead", language.practiceLabel);
        const practice = createElement("p", "language-practice", unit.practice);
        practice.lang = "en";
        content.append(heading, remember, list, practiceLabel, practice);
    }

    let selectedLanguage = supported(document.documentElement.dataset.definitionLanguage || savedLanguage());
    function applyLanguage(value, save = false) {
        selectedLanguage = supported(value);
        if (save) {
            try { localStorage.setItem(STORAGE_KEY, selectedLanguage); } catch { /* Selection still works on this page. */ }
        }
        document.documentElement.dataset.definitionLanguage = selectedLanguage;
        document.querySelectorAll("#life-language-controls [data-definition-language]").forEach(button => {
            button.disabled = false;
            button.setAttribute("aria-pressed", String(button.dataset.definitionLanguage === selectedLanguage));
        });
        document.querySelectorAll("[data-explanation]").forEach(container => renderExplanation(container, selectedLanguage));
        const status = document.querySelector("[data-life-language-status]");
        if (status) status.textContent = selectedLanguage === "en"
            ? "Language help is optional. Choose any of the five languages if you would like it."
            : `Unit explanations and deeper AI explanations in ${languages[selectedLanguage].label}.`;
        // Keep the ready-to-copy AI prompts and vocabulary buttons on the same preference.
        window.dispatchEvent(new CustomEvent("vocabulary-language-changed", { detail: { language: selectedLanguage } }));
    }
    document.querySelectorAll("#life-language-controls [data-definition-language]").forEach(button => {
        button.addEventListener("click", () => applyLanguage(button.dataset.definitionLanguage, true));
    });
    window.addEventListener("vocabulary-language-changed", event => {
        if (supported(event.detail?.language) !== selectedLanguage) applyLanguage(event.detail?.language);
    });
    window.addEventListener("storage", event => {
        if (event.key === STORAGE_KEY || event.key === null) applyLanguage(savedLanguage());
    });
    window.addEventListener("pageshow", event => {
        if (event.persisted) applyLanguage(savedLanguage());
    });
    applyLanguage(selectedLanguage);
    const units = [...document.querySelectorAll(".us-life-module")];
    if (units.length) {
        const nav=document.createElement("nav"); nav.className="life-unit-controls"; nav.setAttribute("aria-label","Choose an everyday English unit");
        const label=document.createElement("label"); label.textContent="Study unit ";
        const select=document.createElement("select"); select.setAttribute("aria-label","Study unit");
        units.forEach((unit,index)=>{const option=document.createElement("option"); option.value=unit.id; option.textContent=`${index+1}. ${unit.querySelector("h2").textContent}`; select.append(option);});
        label.append(select);nav.append(label); document.querySelector(".us-life-module-stack").before(nav);
        const show=(id,focus=false)=>{ const active=units.find(u=>u.id===id)||units[0]; units.forEach(u=>{u.hidden=u!==active;}); select.value=active.id; if(focus){active.querySelector("h2").tabIndex=-1;active.querySelector("h2").focus();active.scrollIntoView({block:"start"});} };
        select.addEventListener("change",()=>{location.hash=select.value;});
        window.addEventListener("hashchange",()=>show(location.hash.slice(1),true));
        units.forEach((unit,index)=>{
            const practice=document.createElement("section");practice.className="life-practice";
            const heading=document.createElement("h3");heading.textContent="Try the conversation";
            const prompt=document.createElement("p");prompt.textContent="Read the dialogue with a partner or aloud on your own. Change one detail to fit your life. Then cover it and ask one useful question.";
            const model=document.createElement("p");model.textContent="Start with: "+(explanations[unit.id]?.practice||"Could you help me, please?");
            const check=document.createElement("p");check.textContent="Self-check: Did you make your request clear? Could your partner understand the detail you changed?";
            practice.append(heading,prompt,model,check);
            if(index+1<units.length){const next=document.createElement("a");next.className="primary-button";next.href="#"+units[index+1].id;next.textContent="Next unit →";practice.append(next);}
            unit.append(practice);
        });
        show(location.hash.slice(1));
    }
})();
