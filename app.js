function checkAnswer(btn) {
    const optionsContainer = btn.parentElement;

    Array.from(optionsContainer.children).forEach((button) => {
        button.style.backgroundColor = "#fff";
        button.setAttribute("aria-pressed", "false");
    });

    btn.style.backgroundColor = btn.dataset.bg;
    btn.setAttribute("aria-pressed", "true");
    const feedbackDiv = optionsContainer.nextElementSibling;
    feedbackDiv.textContent = sanitizeFeedback(btn.dataset.feedback || "");
    feedbackDiv.style.color = btn.dataset.color;
}

function sanitizeFeedback(feedback) {
    const temp = document.createElement("div");
    temp.innerHTML = feedback;
    return temp.textContent.trim();
}

const DEFAULT_RELEASE_HOUR_UTC = 10;

function formatElapsedAge(releaseDate) {
    const now = new Date();
    const elapsedMs = Math.max(0, now.getTime() - releaseDate.getTime());
    const days = Math.floor(elapsedMs / 86400000);
    const hours = Math.floor((elapsedMs % 86400000) / 3600000);
    const dayLabel = days === 1 ? "day" : "days";
    const hourLabel = hours === 1 ? "hour" : "hours";
    return `[${days} ${dayLabel}, ${hours} ${hourLabel} old]`;
}

function parseFallbackReleaseDate(dateText) {
    const fallbackDate = new Date(`${dateText} ${DEFAULT_RELEASE_HOUR_UTC.toString().padStart(2, "0")}:00:00 UTC`);
    return Number.isNaN(fallbackDate.getTime()) ? null : fallbackDate;
}

function extractLessonParts(summary) {
    const dateNode = summary.querySelector(".lesson-date-text");
    const titleNode = summary.querySelector(".lesson-title-text");
    if (dateNode && titleNode) {
        return {
            dateText: dateNode.textContent.trim(),
            titleText: titleNode.textContent.trim(),
        };
    }

    let summaryText = summary.textContent.trim();
    if (summaryText.startsWith("📅")) {
        summaryText = summaryText.slice(1).trim();
    }

    const separatorIndex = summaryText.indexOf(" - ");
    if (separatorIndex === -1) {
        return null;
    }

    return {
        dateText: summaryText.slice(0, separatorIndex).trim(),
        titleText: summaryText.slice(separatorIndex + 3).trim(),
    };
}

function ensureSummaryMarkup(summary, parts) {
    if (summary.querySelector(".lesson-date-text") && summary.querySelector(".lesson-title-text")) {
        return;
    }

    summary.textContent = "";

    const prefix = document.createElement("span");
    prefix.className = "lesson-date-prefix";
    prefix.textContent = "📅";

    const dateSpan = document.createElement("span");
    dateSpan.className = "lesson-date-text";
    dateSpan.textContent = parts.dateText;

    const ageSpan = document.createElement("span");
    ageSpan.className = "lesson-age";

    const separator = document.createElement("span");
    separator.className = "lesson-separator";
    separator.textContent = "-";

    const titleSpan = document.createElement("span");
    titleSpan.className = "lesson-title-text";
    titleSpan.textContent = parts.titleText;

    summary.append(prefix, document.createTextNode(" "), dateSpan, document.createTextNode(" "), ageSpan, document.createTextNode(" "), separator, document.createTextNode(" "), titleSpan);
}

function updateLessonAges() {
    document.querySelectorAll("summary.lesson-date").forEach((summary) => {
        const parts = extractLessonParts(summary);
        if (!parts) {
            return;
        }

        ensureSummaryMarkup(summary, parts);

        const releaseIso = summary.dataset.releaseIso;
        const releaseDate = releaseIso ? new Date(releaseIso) : parseFallbackReleaseDate(parts.dateText);
        if (!releaseDate || Number.isNaN(releaseDate.getTime())) {
            return;
        }

        const ageSpan = summary.querySelector(".lesson-age");
        if (ageSpan) {
            ageSpan.textContent = formatElapsedAge(releaseDate);
        }
    });
}

function setupConceptImageLightbox() {
    const trigger = document.querySelector(".grammar-image-trigger");
    const lightbox = document.querySelector(".image-lightbox");

    if (!trigger || !lightbox) {
        return;
    }

    const image = lightbox.querySelector(".image-lightbox-image");
    const closeElements = lightbox.querySelectorAll("[data-lightbox-close]");
    const closeButton = lightbox.querySelector(".image-lightbox-close");

    function closeLightbox() {
        lightbox.hidden = true;
        document.body.classList.remove("lightbox-open");
        if (image) {
            image.removeAttribute("src");
        }
        document.removeEventListener("keydown", handleKeydown);
        trigger.focus();
    }

    function handleKeydown(event) {
        if (event.key === "Escape") {
            closeLightbox();
        }
    }

    trigger.addEventListener("click", () => {
        if (!image) {
            return;
        }

        image.src = trigger.dataset.lightboxSrc || "";
        image.alt = trigger.dataset.lightboxAlt || trigger.querySelector("img")?.alt || "";
        lightbox.hidden = false;
        document.body.classList.add("lightbox-open");
        document.addEventListener("keydown", handleKeydown);
        if (closeButton) {
            closeButton.focus();
        }
    });

    closeElements.forEach((element) => {
        element.addEventListener("click", closeLightbox);
    });
}

function setupEfspDirectorySearch() {
    const search = document.querySelector("[data-efsp-search]");
    const links = Array.from(document.querySelectorAll("[data-efsp-directory-link]"));
    const count = document.querySelector("[data-efsp-directory-count]");

    if (!search || links.length === 0) {
        return;
    }

    function updateDirectory() {
        const query = search.value.trim().toLowerCase();
        let visibleCount = 0;

        links.forEach((link) => {
            const haystack = (link.dataset.search || link.textContent || "").toLowerCase();
            const visible = !query || haystack.includes(query);
            link.hidden = !visible;
            if (visible) {
                visibleCount += 1;
            }
        });

        if (count) {
            count.textContent = `${visibleCount} ${visibleCount === 1 ? "track" : "tracks"} shown`;
        }
    }

    search.addEventListener("input", updateDirectory);
    updateDirectory();
}

function setupEfspIndustryPage() {
    const dataNode = document.querySelector("#efsp-page-data");
    const workbench = document.querySelector("[data-efsp-workbench]");

    if (!dataNode || !workbench) {
        return;
    }

    let data;
    try {
        data = JSON.parse(dataNode.textContent || "{}");
    } catch {
        return;
    }

    const modules = Array.isArray(data.modules) ? data.modules : [];
    const jargon = Array.isArray(data.jargon) ? data.jargon : [];
    if (modules.length === 0) {
        return;
    }

    let activeModule = 0;
    let activeCard = 0;
    const moduleButtons = workbench.querySelector("[data-module-buttons]");
    const title = workbench.querySelector("[data-module-title]");
    const focus = workbench.querySelector("[data-module-focus]");
    const goals = workbench.querySelector("[data-module-goals]");
    const clozeTitle = workbench.querySelector("[data-cloze-title]");
    const clozeSetting = workbench.querySelector("[data-cloze-setting]");
    const clozeLines = workbench.querySelector("[data-cloze-lines]");
    const clozeOptions = workbench.querySelector("[data-cloze-options]");
    const clozeFeedback = workbench.querySelector("[data-cloze-feedback]");
    const clozeRationale = workbench.querySelector("[data-cloze-rationale]");
    const clozeNotes = workbench.querySelector("[data-cloze-notes]");
    const cardTerm = workbench.querySelector("[data-card-term]");
    const cardDefinition = workbench.querySelector("[data-card-definition]");
    const modelLine = workbench.querySelector("[data-model-line]");
    const notes = workbench.querySelector("[data-language-notes]");
    const progressItems = Array.from(workbench.querySelectorAll("[data-progress-item]"));
    const progressMeter = workbench.querySelector("[data-progress-meter]");
    const progressLabel = workbench.querySelector("[data-progress-label]");

    function renderModuleButtons() {
        if (!moduleButtons) {
            return;
        }
        moduleButtons.textContent = "";
        modules.forEach((module, index) => {
            const button = document.createElement("button");
            button.type = "button";
            button.className = "efsp-module-button";
            button.textContent = `${index + 1}. ${module.title}`;
            button.setAttribute("aria-pressed", index === activeModule ? "true" : "false");
            button.addEventListener("click", () => {
                activeModule = index;
                renderModule();
            });
            moduleButtons.append(button);
        });
    }

    function renderList(node, items) {
        if (!node) {
            return;
        }
        node.textContent = "";
        items.forEach((item) => {
            const li = document.createElement("li");
            li.textContent = item;
            node.append(li);
        });
    }

    function renderCard() {
        if (!cardTerm || !cardDefinition) {
            return;
        }
        const card = jargon[activeCard % Math.max(jargon.length, 1)];
        if (!card) {
            cardTerm.textContent = "No terms available";
            cardDefinition.textContent = "";
            return;
        }
        cardTerm.textContent = card.term;
        cardDefinition.textContent = card.definition;
        cardDefinition.hidden = true;
    }

    function renderCloze() {
        const module = modules[activeModule];
        const cloze = module.cloze || {};
        const options = Array.isArray(cloze.options) ? cloze.options : [];
        const turns = Array.isArray(cloze.turns) ? cloze.turns : [];
        if (clozeTitle) {
            clozeTitle.textContent = cloze.title || "Guided dialogue completion";
        }
        if (clozeSetting) {
            clozeSetting.textContent = cloze.setting || module.scenario || "";
        }
        if (clozeLines) {
            clozeLines.textContent = "";
            turns.forEach((turn) => {
                const row = document.createElement("div");
                row.className = "efsp-dialogue-line";
                const speaker = document.createElement("strong");
                speaker.textContent = turn[0] || "Speaker";
                const line = document.createElement("span");
                line.textContent = turn[1] || "";
                row.append(speaker, line);
                clozeLines.append(row);
            });
        }
        if (clozeOptions) {
            clozeOptions.textContent = "";
            options.forEach((option, index) => {
                const button = document.createElement("button");
                button.type = "button";
                button.className = "efsp-choice-button";
                button.textContent = `${String.fromCharCode(65 + index)}. ${option}`;
                button.addEventListener("click", () => {
                    const correct = index === cloze.correct_index;
                    clozeOptions.querySelectorAll("button").forEach((choice, choiceIndex) => {
                        choice.dataset.state = choiceIndex === cloze.correct_index ? "correct" : choiceIndex === index ? "incorrect" : "";
                        choice.setAttribute("aria-pressed", choiceIndex === index ? "true" : "false");
                    });
                    if (clozeFeedback) {
                        clozeFeedback.textContent = correct
                            ? `Correct. ${cloze.explanation || ""}`
                            : `Not quite. The correct answer is ${String.fromCharCode(65 + cloze.correct_index)}. ${cloze.answer || ""}. ${cloze.explanation || ""}`;
                    }
                    if (clozeRationale) {
                        clozeRationale.textContent = cloze.explanation || "";
                    }
                });
                clozeOptions.append(button);
            });
        }
        if (clozeFeedback) {
            clozeFeedback.textContent = "";
        }
        if (clozeRationale) {
            clozeRationale.textContent = "Choose an option to see the workplace rationale.";
        }
        renderList(clozeNotes, module.notes || []);
    }

    function renderProgress() {
        if (!progressMeter || !progressLabel) {
            return;
        }
        const completed = progressItems.filter((item) => item.checked).length;
        progressMeter.value = completed;
        progressLabel.textContent = `${completed} of ${progressItems.length} complete`;
    }

    function renderModule() {
        const module = modules[activeModule];
        if (title) {
            title.textContent = module.title;
        }
        if (focus) {
            focus.textContent = module.focus;
        }
        renderList(goals, module.goals || []);
        if (modelLine) {
            modelLine.textContent = module.model;
        }
        renderList(notes, module.notes || []);
        renderModuleButtons();
        renderCloze();
    }

    workbench.querySelectorAll("[data-action]").forEach((button) => {
        button.addEventListener("click", () => {
            const action = button.dataset.action;
            if (action === "reveal-card" && cardDefinition) {
                cardDefinition.hidden = !cardDefinition.hidden;
            }
            if (action === "next-card") {
                activeCard = (activeCard + 1) % Math.max(jargon.length, 1);
                renderCard();
            }
        });
    });

    progressItems.forEach((item) => {
        item.addEventListener("change", renderProgress);
    });

    renderModuleButtons();
    renderModule();
    renderCard();
    renderProgress();
}

updateLessonAges();
window.setInterval(updateLessonAges, 300000);
setupConceptImageLightbox();
setupEfspDirectorySearch();
setupEfspIndustryPage();
