function checkAnswer(btn) {
    const optionsContainer = btn.parentElement;

    Array.from(optionsContainer.children).forEach((button) => {
        button.style.backgroundColor = "#fff";
    });

    btn.style.backgroundColor = btn.dataset.bg;
    const feedbackDiv = optionsContainer.nextElementSibling;
    feedbackDiv.innerHTML = btn.dataset.feedback;
    feedbackDiv.style.color = btn.dataset.color;
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

updateLessonAges();
window.setInterval(updateLessonAges, 300000);
