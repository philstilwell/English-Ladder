(() => {
    const fallbackLessons = {
        beginner: {
            headline: "International Cooperation on Naval Technology",
            brief: "The USA, UK, and Australia are working together. They will develop new underwater drones. The new drones will protect important undersea cables. The drones will also boost naval defence.",
            vocabulary: [
                { term: "technology", definition: "New machines or methods made using science." },
                { term: "military pact", definition: "An official agreement between countries about their armies." },
                { term: "undersea cables", definition: "Long wires under the ocean that carry information or power." },
                { term: "boost", definition: "To help something become better or stronger." },
                { term: "naval defence", definition: "Protection for a country's ships and navy." },
            ],
        },
        intermediate: {
            headline: "Naval Technology and International Defence Collaboration",
            brief: "The United States, United Kingdom, and Australia are planning to develop new underwater drone technology together. This initiative falls under the Aukus military pact, a security agreement among the three nations. The primary goal is to protect critical undersea data cables and boost naval defence capabilities.",
            vocabulary: [
                { term: "develop", definition: "To create something new or improve something over time." },
                { term: "technology", definition: "The application of scientific knowledge for practical purposes." },
                { term: "pact", definition: "A formal agreement or treaty." },
                { term: "aimed at", definition: "Intended for a particular purpose or goal." },
                { term: "naval defence", definition: "Protection of a country's sea borders and naval forces." },
            ],
        },
        advanced: {
            headline: "Advanced Undersea Drone Technology for Defence",
            brief: "The AUKUS security alliance has announced a significant initiative to jointly develop sophisticated underwater drone technology. The undertaking aims to safeguard critical undersea communication cables, bolster naval defence capabilities, and provide persistent surveillance in contested waters.",
            vocabulary: [
                { term: "strategic imperative", definition: "A crucial goal or need with long-term consequences." },
                { term: "bolster naval defence", definition: "To strengthen the capabilities of a navy." },
                { term: "maritime domain awareness", definition: "Understanding activities and events in the maritime environment." },
                { term: "deterring potential adversaries", definition: "Discouraging possible enemies from taking hostile action." },
                { term: "underpinning security", definition: "Providing the foundation for safety and protection." },
            ],
        },
    };

    const conceptPaths = {
        prepositions: [
            ["Concept 01", "Prepositions: in/on/at", "grammar-concepts/concept-01.html"],
            ["Concept 02", "Going places", "grammar-concepts/concept-02.html"],
            ["Concept 05", "By and through", "grammar-concepts/concept-05.html"],
            ["Concept 15", "Referencing dates", "grammar-concepts/concept-15.html"],
            ["Concept 19", "Directions and locations", "grammar-concepts/concept-19.html"],
        ],
        tense: [
            ["Concept 14", "Events and tenses", "grammar-concepts/concept-14.html"],
            ["Concept 16", "Recently and lately", "grammar-concepts/concept-16.html"],
            ["Concept 26", "Past perfect", "grammar-concepts/concept-26.html"],
            ["Concept 35", "Was able to vs could", "grammar-concepts/concept-35.html"],
        ],
        wordForm: [
            ["Concept 03", "-ing and -ed emotion words", "grammar-concepts/concept-03.html"],
            ["Concept 06", "Noun and verb confusion", "grammar-concepts/concept-06.html"],
            ["Concept 34", "Success word family", "grammar-concepts/concept-34.html"],
            ["Concept 38", "Affect and effect", "grammar-concepts/concept-38.html"],
        ],
        clauses: [
            ["Concept 04", "While and during", "grammar-concepts/concept-04.html"],
            ["Concept 09", "Causal phrases", "grammar-concepts/concept-09.html"],
            ["Concept 12", "That vs which", "grammar-concepts/concept-12.html"],
            ["Concept 18", "Position of only", "grammar-concepts/concept-18.html"],
            ["Concept 32", "Even if vs even though", "grammar-concepts/concept-32.html"],
        ],
        quantity: [
            ["Concept 21", "Uncountable nouns", "grammar-concepts/concept-21.html"],
            ["Concept 23", "All, each, every, none", "grammar-concepts/concept-23.html"],
            ["Concept 27", "Few and little", "grammar-concepts/concept-27.html"],
            ["Concept 40", "So and such", "grammar-concepts/concept-40.html"],
        ],
        usage: [
            ["Concept 11", "Go/come and bring/take", "grammar-concepts/concept-11.html"],
            ["Concept 13", "Allow vs prohibit", "grammar-concepts/concept-13.html"],
            ["Concept 17", "Recommend and suggest", "grammar-concepts/concept-17.html"],
            ["Concept 36", "Speak, talk, say, tell", "grammar-concepts/concept-36.html"],
            ["Concept 41", "Refuse vs reject", "grammar-concepts/concept-41.html"],
        ],
    };

    const diagnosticQuestions = [
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "I was in New York last week.", correct: true },
                { text: "I was at New York last week.", weakness: "prepositions" },
                { text: "I was on New York last week.", weakness: "prepositions" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "She suggested that I apply for the role.", correct: true },
                { text: "She suggested me to apply for the role.", weakness: "usage" },
                { text: "She suggested to me apply for the role.", weakness: "usage" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "The meeting was canceled because of the storm.", correct: true },
                { text: "The meeting was canceled because the storm.", weakness: "clauses" },
                { text: "The meeting was canceled during the storm was strong.", weakness: "clauses" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "I have been working a lot lately.", correct: true },
                { text: "I worked a lot lately.", weakness: "tense" },
                { text: "I am working a lot since Monday.", weakness: "tense" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "Only John called Maria.", correct: true },
                { text: "John called only Maria only.", weakness: "clauses" },
                { text: "John only called to Maria.", weakness: "prepositions" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "Few people attended the meeting.", correct: true },
                { text: "Little people attended the meeting.", weakness: "quantity" },
                { text: "Much people attended the meeting.", weakness: "quantity" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "The presentation was interesting, so I felt interested.", correct: true },
                { text: "The presentation was interested, so I felt interesting.", weakness: "wordForm" },
                { text: "The presentation was interest, so I felt interested.", weakness: "wordForm" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "The report, which includes new data, is ready.", correct: true },
                { text: "The report, that includes new data, is ready.", weakness: "clauses" },
                { text: "The report which, includes new data is ready.", weakness: "clauses" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "The project was successful.", correct: true },
                { text: "The project was success.", weakness: "wordForm" },
                { text: "The project had successful.", weakness: "wordForm" },
            ],
        },
        {
            prompt: "Choose the natural sentence.",
            options: [
                { text: "The call is on Monday at 3:00.", correct: true },
                { text: "The call is at Monday in 3:00.", weakness: "prepositions" },
                { text: "The call is in Monday on 3:00.", weakness: "prepositions" },
            ],
        },
    ];

    const phraseData = {
        disagree: {
            polite: ["I see your point, but I read the situation a little differently.", "Could we look at one more option before deciding?", "I may be missing something, but I have a concern about that approach."],
            direct: ["I disagree with that approach.", "I do not think that solves the main issue.", "I see a different risk here."],
            diplomatic: ["I understand the reasoning, and I wonder if there is a risk we should account for.", "That may work in some cases, but I am concerned about the impact on the timeline.", "Could we separate the goal from the method and compare options?"],
            firm: ["I cannot support that recommendation as it stands.", "We need to address this risk before moving forward.", "I think this decision needs more evidence."],
        },
        clarify: {
            polite: ["Could you clarify what you mean by that?", "Could you walk me through the last point again?", "I want to make sure I understood you correctly."],
            direct: ["What exactly do you mean?", "Which part is the priority?", "Can you define the next step?"],
            diplomatic: ["To make sure we are aligned, could you clarify the expected outcome?", "It would help me to understand which assumption we are using.", "Could you say a bit more about the tradeoff you see?"],
            firm: ["I need clarification before I can agree to this.", "We should define the owner and deadline now.", "The requirement is still unclear."],
        },
        pushback: {
            polite: ["I may need more time to do that well.", "Could we adjust the deadline or narrow the scope?", "I can help, but I need to reprioritize something else."],
            direct: ["That timeline is not realistic.", "I cannot take that on without dropping another task.", "The scope is too broad for this deadline."],
            diplomatic: ["I understand the urgency, and I want to be realistic about what can be delivered.", "If this is the priority, we should agree on what moves down the list.", "A narrower version would be more achievable by the deadline."],
            firm: ["I cannot commit to that deadline with the current scope.", "We need either more time or fewer requirements.", "I am not comfortable promising that outcome."],
        },
        problem: {
            polite: ["I wanted to flag a possible issue.", "There may be a problem with the current timeline.", "I noticed something we should look at."],
            direct: ["There is a problem with the current plan.", "The data does not support that conclusion.", "The deadline is at risk."],
            diplomatic: ["I want to flag a risk early so we can address it before it grows.", "There is a gap between the plan and the current status.", "This may affect delivery unless we adjust quickly."],
            firm: ["This is a blocker.", "We need a decision today to avoid further delay.", "The current plan will not work without changes."],
        },
        "bad-news": {
            polite: ["Unfortunately, we are not able to approve that request.", "I am sorry, but we need to move the deadline.", "I wish I had better news."],
            direct: ["We need to delay the launch.", "The request was not approved.", "The result did not meet the requirement."],
            diplomatic: ["After reviewing the options, we will need to adjust the timeline.", "Given the current constraints, we are not able to move forward with that request.", "The outcome is not what we hoped for, so the next step is to revise the plan."],
            firm: ["We are not moving forward with that option.", "The deadline must change.", "This does not meet the standard required for approval."],
        },
    };

    const collocationData = {
        make: {
            good: ["make a decision", "make progress", "make an effort", "make a mistake"],
            traps: ["make homework", "make a photo", "make a meeting"],
            note: "Use make for creating, deciding, progress, and mistakes.",
        },
        take: {
            good: ["take responsibility", "take notes", "take a break", "take a risk"],
            traps: ["take a decision", "take progress", "take a mistake"],
            note: "Use take for responsibility, notes, breaks, risks, and actions you accept.",
        },
        raise: {
            good: ["raise a concern", "raise a question", "raise awareness", "raise an issue"],
            traps: ["raise a mistake", "raise a decision", "raise a meeting"],
            note: "Use raise when bringing a topic into discussion.",
        },
        issue: {
            good: ["serious issue", "technical issue", "address an issue", "raise an issue"],
            traps: ["do an issue", "make an issue", "strong issue"],
            note: "Issue often means a problem, topic, or matter for discussion.",
        },
        risk: {
            good: ["reduce risk", "manage risk", "significant risk", "risk assessment"],
            traps: ["do risk", "bigly risk", "riskful plan"],
            note: "Risk combines with verbs like reduce, manage, assess, and identify.",
        },
        concern: {
            good: ["main concern", "address a concern", "express concern", "growing concern"],
            traps: ["do a concern", "make concern", "concernful"],
            note: "Concern can be a worry, a point to discuss, or something that affects someone.",
        },
        proposal: {
            good: ["submit a proposal", "review a proposal", "draft proposal", "proposal for change"],
            traps: ["do a proposal", "proposal of changing", "proposal to change about"],
            note: "Proposal often pairs with submit, review, draft, approve, reject, and for.",
        },
    };

    const state = {
        lessons: { ...fallbackLessons },
        vocabDeck: [],
        vocabIndex: 0,
        vocabRevealed: false,
        recorder: null,
        recordChunks: [],
        recordStream: null,
    };

    const $ = (selector, root = document) => root.querySelector(selector);
    const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

    function escapeHtml(value) {
        return String(value)
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;")
            .replaceAll('"', "&quot;")
            .replaceAll("'", "&#039;");
    }

    function normalizeText(value) {
        return String(value)
            .toLowerCase()
            .replace(/[^a-z0-9\s]/g, " ")
            .replace(/\s+/g, " ")
            .trim();
    }

    function sentenceCase(value) {
        const trimmed = String(value).trim();
        return trimmed ? trimmed.charAt(0).toUpperCase() + trimmed.slice(1) : "";
    }

    function splitSentences(text) {
        return String(text)
            .replace(/\s+/g, " ")
            .split(/(?<=[.!?])\s+/)
            .map((sentence) => sentence.trim())
            .filter((sentence) => sentence.length > 24)
            .slice(0, 8);
    }

    async function loadLesson(level) {
        try {
            const response = await fetch(`${level}.html`, { cache: "no-store" });
            if (!response.ok) {
                throw new Error("Lesson page unavailable");
            }
            const html = await response.text();
            const doc = new DOMParser().parseFromString(html, "text/html");
            const current = doc.querySelector(".daily-lesson");
            const headline = current?.querySelector(".lesson-title-text")?.textContent?.trim() || fallbackLessons[level].headline;
            const brief = current?.querySelector(".section p")?.textContent?.trim() || fallbackLessons[level].brief;
            const vocabulary = extractVocabulary(current?.querySelector(".vocab-box"));
            return {
                headline,
                brief,
                vocabulary: vocabulary.length ? vocabulary : fallbackLessons[level].vocabulary,
            };
        } catch (_error) {
            return fallbackLessons[level];
        }
    }

    function extractVocabulary(vocabBox) {
        if (!vocabBox) {
            return [];
        }
        const clone = vocabBox.cloneNode(true);
        clone.querySelectorAll("br").forEach((breakNode) => {
            breakNode.replaceWith("\n");
        });
        const text = clone.innerText || clone.textContent || "";
        return text
            .split(/\n+/)
            .map((line) => line.trim())
            .filter(Boolean)
            .map((line) => {
                const match = line.match(/^\d+\.\s*(.+?):\s*(.+)$/);
                if (!match) {
                    return null;
                }
                return {
                    term: match[1].replace(/\s*\([^)]*\)\s*$/, "").trim(),
                    definition: match[2].trim(),
                };
            })
            .filter(Boolean);
    }

    async function hydrateLessons() {
        const levels = ["beginner", "intermediate", "advanced"];
        const loaded = await Promise.all(levels.map((level) => loadLesson(level)));
        levels.forEach((level, index) => {
            state.lessons[level] = loaded[index];
        });
        populateSentenceSelects();
        renderVocabCard();
    }

    function populateSentenceSelects() {
        const sentences = [];
        Object.entries(state.lessons).forEach(([level, lesson]) => {
            splitSentences(lesson.brief).forEach((sentence) => {
                sentences.push({ level, sentence });
            });
        });
        const options = sentences.map(({ level, sentence }) => {
            const label = `${level.charAt(0).toUpperCase() + level.slice(1)}: ${sentence}`;
            return `<option value="${escapeHtml(sentence)}">${escapeHtml(label)}</option>`;
        }).join("");
        ["#shadow-sentence", "#dictation-sentence"].forEach((selector) => {
            const select = $(selector);
            if (select) {
                select.innerHTML = options;
            }
        });
    }

    function renderDiagnostic() {
        const container = $("#diagnostic-questions");
        if (!container) {
            return;
        }
        container.innerHTML = diagnosticQuestions.map((question, index) => `
            <article class="diagnostic-card">
                <h3>Question ${index + 1}</h3>
                <p>${escapeHtml(question.prompt)}</p>
                <div class="choice-stack">
                    ${question.options.map((option, optionIndex) => `
                        <label class="choice-row">
                            <input type="radio" name="diagnostic-${index}" value="${optionIndex}">
                            <span>${escapeHtml(option.text)}</span>
                        </label>
                    `).join("")}
                </div>
            </article>
        `).join("");
    }

    function runDiagnostic() {
        const scores = {};
        let answered = 0;
        diagnosticQuestions.forEach((question, index) => {
            const selected = $(`input[name="diagnostic-${index}"]:checked`);
            if (!selected) {
                return;
            }
            answered += 1;
            const option = question.options[Number(selected.value)];
            if (!option.correct && option.weakness) {
                scores[option.weakness] = (scores[option.weakness] || 0) + 1;
            }
        });
        const result = $("#diagnostic-results");
        if (!result) {
            return;
        }
        if (!answered) {
            result.innerHTML = `<p class="result-note">Answer at least one question to build a map.</p>`;
            return;
        }
        const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
        if (!ranked.length) {
            result.innerHTML = `
                <h3>Strong diagnostic result</h3>
                <p class="result-note">You chose the natural sentence each time. Try a higher level daily lesson, then use the Register Transformer or Collocation Builder for precision work.</p>
            `;
            return;
        }
        result.innerHTML = `
            <h3>Your study path</h3>
            <div class="result-list">
                ${ranked.map(([key, count]) => `
                    <article>
                        <strong>${escapeHtml(labelForWeakness(key))}</strong>
                        <p>${count} signal${count === 1 ? "" : "s"} from your answers.</p>
                        <div class="inline-link-list">
                            ${(conceptPaths[key] || []).slice(0, 4).map(([number, title, href]) => `<a href="${href}">${escapeHtml(number)}: ${escapeHtml(title)}</a>`).join("")}
                        </div>
                    </article>
                `).join("")}
            </div>
        `;
    }

    function labelForWeakness(key) {
        return {
            prepositions: "Prepositions and location/time phrases",
            tense: "Tense and time relationships",
            wordForm: "Word form and part of speech",
            clauses: "Clauses, logic, and sentence focus",
            quantity: "Quantity, countability, and degree",
            usage: "Verb patterns and lexical choice",
        }[key] || key;
    }

    function resetDiagnostic() {
        $$("input[name^='diagnostic-']").forEach((input) => {
            input.checked = false;
        });
        const result = $("#diagnostic-results");
        if (result) {
            result.innerHTML = "";
        }
    }

    function runSentenceRepair() {
        let revised = $("#repair-input")?.value.trim() || "";
        const level = $("#repair-level")?.value || "intermediate";
        const issues = [];

        function addIssue(label, message, href) {
            issues.push({ label, message, href });
        }

        function apply(pattern, replacement, issue) {
            if (pattern.test(revised)) {
                revised = revised.replace(pattern, replacement);
                addIssue(issue.label, issue.message, issue.href);
            }
        }

        apply(/\binteresting in\b/gi, "interested in", {
            label: "Emotion adjectives",
            message: "Use interested for the person's feeling and interesting for the thing that creates the feeling.",
            href: "grammar-concepts/concept-03.html",
        });
        apply(/\binterested in improve\b/gi, "interested in improving", {
            label: "Verb after preposition",
            message: "After in, use the -ing form: interested in improving.",
            href: "grammar-concepts/concept-03.html",
        });
        apply(/\binterested in learn\b/gi, "interested in learning", {
            label: "Verb after preposition",
            message: "After in, use the -ing form: interested in learning.",
            href: "grammar-concepts/concept-03.html",
        });
        apply(/\bsuggested me to\b/gi, "suggested that I", {
            label: "Suggest pattern",
            message: "Suggest usually takes that + subject + base verb, not object + to.",
            href: "grammar-concepts/concept-17.html",
        });
        apply(/\brecommended me to\b/gi, "recommended that I", {
            label: "Recommend pattern",
            message: "Recommended that I is often cleaner than recommended me to in formal English.",
            href: "grammar-concepts/concept-17.html",
        });
        apply(/\bdiscuss about\b/gi, "discuss", {
            label: "Verb pattern",
            message: "Discuss normally takes a direct object: discuss the issue.",
            href: "grammar-concepts/concept-07.html",
        });
        apply(/\bexplain me\b/gi, "explain to me", {
            label: "Verb pattern",
            message: "Use explain something to someone or explain to someone.",
            href: "grammar-concepts/concept-36.html",
        });
        apply(/\bat (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/gi, "on $1", {
            label: "Dates and days",
            message: "Use on with days of the week.",
            href: "grammar-concepts/concept-01.html",
        });
        apply(/\bin (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/gi, "on $1", {
            label: "Dates and days",
            message: "Use on with days of the week.",
            href: "grammar-concepts/concept-01.html",
        });
        apply(/\bon (\d{4})\b/g, "in $1", {
            label: "Years",
            message: "Use in with years.",
            href: "grammar-concepts/concept-15.html",
        });
        apply(/\bmuch people\b/gi, "many people", {
            label: "Countable nouns",
            message: "Use many or few with countable plural nouns such as people.",
            href: "grammar-concepts/concept-27.html",
        });
        apply(/\blittle people\b/gi, "few people", {
            label: "Few vs little",
            message: "Use few with countable plural nouns and little with uncountable nouns.",
            href: "grammar-concepts/concept-27.html",
        });
        apply(/\ba advice\b/gi, "some advice", {
            label: "Uncountable noun",
            message: "Advice is usually uncountable, so use some advice or a piece of advice.",
            href: "grammar-concepts/concept-21.html",
        });

        const result = $("#repair-results");
        if (!result) {
            return;
        }
        if (!revised) {
            result.innerHTML = `<p class="result-note">Enter a sentence first.</p>`;
            return;
        }
        const extra = level === "advanced"
            ? "For advanced style, also check whether your verb choice shows the exact relationship: cause, contrast, recommendation, or concession."
            : "Read the revised sentence aloud and check whether the main verb pattern feels complete.";
        result.innerHTML = `
            <h3>Repair result</h3>
            <div class="before-after">
                <p><strong>Original</strong><br>${escapeHtml($("#repair-input").value.trim())}</p>
                <p><strong>Suggested revision</strong><br>${escapeHtml(sentenceCase(revised))}</p>
            </div>
            ${issues.length ? `
                <div class="result-list">
                    ${issues.map((issue) => `
                        <article>
                            <strong>${escapeHtml(issue.label)}</strong>
                            <p>${escapeHtml(issue.message)}</p>
                            <div class="inline-link-list"><a href="${issue.href}">Open related concept</a></div>
                        </article>
                    `).join("")}
                </div>
            ` : `<p class="result-note">No high-confidence repair pattern was found. ${escapeHtml(extra)}</p>`}
        `;
    }

    function speakText(text, rate = 0.9) {
        if (!("speechSynthesis" in window)) {
            return false;
        }
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-US";
        utterance.rate = Number(rate);
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
        return true;
    }

    function playShadowModel() {
        const sentence = $("#shadow-sentence")?.value;
        const rate = $("#shadow-rate")?.value || 0.92;
        const result = $("#shadow-results");
        if (!sentence || !result) {
            return;
        }
        const spoken = speakText(sentence, rate);
        result.innerHTML = spoken
            ? `<h3>Shadowing focus</h3><p class="result-note">Listen for stressed content words, then repeat the full sentence without pausing after every word.</p><p>${escapeHtml(sentence)}</p>`
            : `<p class="result-note">This browser does not support speech playback.</p>`;
    }

    async function startRecording() {
        const result = $("#shadow-results");
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            state.recordStream = stream;
            state.recordChunks = [];
            state.recorder = new MediaRecorder(stream);
            state.recorder.addEventListener("dataavailable", (event) => {
                if (event.data.size > 0) {
                    state.recordChunks.push(event.data);
                }
            });
            state.recorder.addEventListener("stop", () => {
                const blob = new Blob(state.recordChunks, { type: "audio/webm" });
                const audio = $("#shadow-playback");
                if (audio) {
                    audio.src = URL.createObjectURL(blob);
                    audio.hidden = false;
                }
                state.recordStream?.getTracks().forEach((track) => track.stop());
                state.recordStream = null;
                $("#shadow-record").disabled = false;
                $("#shadow-stop").disabled = true;
                if (result) {
                    result.innerHTML = `<h3>Compare your recording</h3><p class="result-note">Play the model again, then play your recording. Check stress, final consonants, and whether your pauses match the sentence meaning.</p>`;
                }
            });
            state.recorder.start();
            $("#shadow-record").disabled = true;
            $("#shadow-stop").disabled = false;
            if (result) {
                result.innerHTML = `<p class="result-note">Recording...</p>`;
            }
        } catch (_error) {
            if (result) {
                result.innerHTML = `<p class="result-note">Microphone recording is not available in this browser session.</p>`;
            }
        }
    }

    function stopRecording() {
        if (state.recorder && state.recorder.state !== "inactive") {
            state.recorder.stop();
        }
    }

    function getReviewState() {
        try {
            return JSON.parse(localStorage.getItem("englishLadderVocabReview") || "{}");
        } catch (_error) {
            return {};
        }
    }

    function saveReviewState(reviewState) {
        localStorage.setItem("englishLadderVocabReview", JSON.stringify(reviewState));
    }

    function loadVocabDeck() {
        const level = $("#vocab-level")?.value || "intermediate";
        state.vocabDeck = state.lessons[level].vocabulary.map((card) => ({
            ...card,
            id: `${level}:${card.term}`,
        }));
        state.vocabIndex = 0;
        state.vocabRevealed = false;
        renderVocabCard();
    }

    function currentDueDeck() {
        const reviewState = getReviewState();
        const now = Date.now();
        return state.vocabDeck.filter((card) => !reviewState[card.id] || reviewState[card.id].due <= now);
    }

    function renderVocabCard() {
        if (!state.vocabDeck.length) {
            const level = $("#vocab-level")?.value || "intermediate";
            state.vocabDeck = fallbackLessons[level].vocabulary.map((card) => ({ ...card, id: `${level}:${card.term}` }));
        }
        const due = currentDueDeck();
        const card = due[state.vocabIndex % Math.max(due.length, 1)];
        const cardNode = $("#vocab-card");
        const result = $("#vocab-results");
        if (!cardNode) {
            return;
        }
        if (!due.length) {
            cardNode.innerHTML = `<p class="result-note">No cards are due right now.</p>`;
            if (result) {
                result.innerHTML = `<p class="tool-metric">${state.vocabDeck.length} cards scheduled for later review.</p>`;
            }
            return;
        }
        const mode = $("#vocab-mode")?.value || "term";
        const front = mode === "term" ? card.term : card.definition;
        const back = mode === "term" ? card.definition : card.term;
        cardNode.innerHTML = `
            <p class="vocab-card-label">${state.vocabIndex + 1} of ${due.length} due</p>
            <h3>${escapeHtml(front)}</h3>
            <p ${state.vocabRevealed ? "" : "hidden"}>${escapeHtml(back)}</p>
        `;
        if (result) {
            result.innerHTML = `<p class="tool-metric">${state.vocabDeck.length} cards in this deck.</p>`;
        }
    }

    function rateVocabCard(days) {
        const due = currentDueDeck();
        const card = due[state.vocabIndex % Math.max(due.length, 1)];
        if (!card) {
            return;
        }
        const reviewState = getReviewState();
        reviewState[card.id] = {
            due: Date.now() + days * 86400000,
            last: Date.now(),
        };
        saveReviewState(reviewState);
        state.vocabIndex += 1;
        state.vocabRevealed = false;
        renderVocabCard();
    }

    function resetVocabReview() {
        localStorage.removeItem("englishLadderVocabReview");
        state.vocabIndex = 0;
        state.vocabRevealed = false;
        renderVocabCard();
    }

    function buildNewsTask() {
        const level = $("#news-level")?.value || "intermediate";
        const skill = $("#news-skill")?.value || "summary";
        const lesson = state.lessons[level];
        const result = $("#news-results");
        if (!result) {
            return;
        }
        const tasks = {
            summary: [`Write a ${level === "beginner" ? "3" : "5"} sentence summary.`, "Keep the main event, main people, and reason for importance.", "Use two vocabulary words from the lesson."],
            discussion: ["Prepare three spoken answers.", "What happened?", "Why does it matter?", "What question would you ask next?"],
            opinion: ["Write one clear opinion paragraph.", "State your view, give one reason, and add one example.", "End with a cautious prediction."],
            coworker: ["Explain the story to a coworker in one minute.", "Use simple context first, then the key detail.", "End with why the coworker should care."],
            email: ["Write a short email update.", "Use a subject line, one context sentence, two key facts, and one next step.", "Keep the tone neutral and professional."],
        };
        result.innerHTML = `
            <h3>${escapeHtml(lesson.headline)}</h3>
            <p>${escapeHtml(lesson.brief)}</p>
            <div class="result-list">
                <article>
                    <strong>${escapeHtml(skillLabel(skill))}</strong>
                    <ul>${tasks[skill].map((task) => `<li>${escapeHtml(task)}</li>`).join("")}</ul>
                </article>
            </div>
        `;
    }

    function skillLabel(skill) {
        return {
            summary: "Summary task",
            discussion: "Discussion task",
            opinion: "Opinion task",
            coworker: "Coworker explanation",
            email: "Email task",
        }[skill] || "Practice task";
    }

    function updateWordCount() {
        const value = $("#news-draft")?.value || "";
        const count = normalizeText(value).split(" ").filter(Boolean).length;
        const metric = $("#news-word-count");
        if (metric) {
            metric.textContent = `${count} word${count === 1 ? "" : "s"}`;
        }
    }

    function buildPhraseCoach() {
        const scenario = $("#phrase-scenario")?.value || "disagree";
        const tone = $("#phrase-tone")?.value || "diplomatic";
        const phrases = phraseData[scenario][tone];
        const result = $("#phrase-results");
        if (!result) {
            return;
        }
        result.innerHTML = `
            <h3>${escapeHtml(scenarioLabel(scenario))}: ${escapeHtml(tone)}</h3>
            <div class="phrase-list">
                ${phrases.map((phrase) => `<button class="phrase-chip" type="button" data-copy-text="${escapeHtml(phrase)}">${escapeHtml(phrase)}</button>`).join("")}
            </div>
            <div class="result-list">
                <article>
                    <strong>Mini dialogue</strong>
                    <p>A: We should move forward today.</p>
                    <p>B: ${escapeHtml(phrases[0])}</p>
                    <p>A: What would you recommend?</p>
                    <p>B: ${escapeHtml(phrases[1])}</p>
                </article>
            </div>
        `;
    }

    function scenarioLabel(scenario) {
        return {
            disagree: "Disagree in a meeting",
            clarify: "Ask for clarification",
            pushback: "Push back on a request",
            problem: "Report a problem",
            "bad-news": "Soften bad news",
        }[scenario] || scenario;
    }

    function startCollocation() {
        const word = $("#collocation-word")?.value || "make";
        const mode = $("#collocation-mode")?.value || "quiz";
        const data = collocationData[word];
        const result = $("#collocation-results");
        if (!result) {
            return;
        }
        if (mode === "sentence") {
            const phrase = data.good[Math.floor(Math.random() * data.good.length)];
            result.innerHTML = `
                <h3>${escapeHtml(word)} sentence builder</h3>
                <p class="result-note">${escapeHtml(data.note)}</p>
                <label class="tool-field tool-field-wide">
                    <span>Use this phrase: ${escapeHtml(phrase)}</span>
                    <textarea id="collocation-sentence" rows="4"></textarea>
                </label>
                <div class="tool-actions">
                    <button class="tool-button" id="collocation-check" type="button" data-phrase="${escapeHtml(phrase)}">Check sentence</button>
                </div>
                <div id="collocation-feedback"></div>
            `;
            $("#collocation-check")?.addEventListener("click", checkCollocationSentence);
            return;
        }
        const correct = data.good[Math.floor(Math.random() * data.good.length)];
        const choices = [...data.traps.slice(0, 2), correct].sort(() => Math.random() - 0.5);
        result.innerHTML = `
            <h3>Choose the natural collocation with "${escapeHtml(word)}"</h3>
            <div class="choice-stack">
                ${choices.map((choice) => `<button class="choice-button" type="button" data-correct="${choice === correct}">${escapeHtml(choice)}</button>`).join("")}
            </div>
            <p class="result-note">${escapeHtml(data.note)}</p>
            <div id="collocation-feedback"></div>
        `;
        $$(".choice-button", result).forEach((button) => {
            button.addEventListener("click", () => {
                const feedback = $("#collocation-feedback");
                if (feedback) {
                    feedback.innerHTML = button.dataset.correct === "true"
                        ? `<p class="success-note">Correct. "${escapeHtml(button.textContent)}" is natural.</p>`
                        : `<p class="result-note">Not natural here. Try another option.</p>`;
                }
            });
        });
    }

    function checkCollocationSentence() {
        const phrase = $("#collocation-check")?.dataset.phrase || "";
        const value = $("#collocation-sentence")?.value || "";
        const feedback = $("#collocation-feedback");
        if (!feedback) {
            return;
        }
        const includesPhrase = normalizeText(value).includes(normalizeText(phrase));
        feedback.innerHTML = includesPhrase
            ? `<p class="success-note">Good. Your sentence includes the target collocation naturally enough for practice.</p>`
            : `<p class="result-note">Try again and include the full phrase "${escapeHtml(phrase)}".</p>`;
    }

    function playDictation(rate) {
        const sentence = $("#dictation-sentence")?.value;
        if (sentence) {
            speakText(sentence, rate);
        }
    }

    function playDictationWords() {
        const sentence = $("#dictation-sentence")?.value || "";
        const words = sentence.split(/\s+/).filter(Boolean);
        let index = 0;
        function next() {
            if (index >= words.length) {
                return;
            }
            speakText(words[index], 0.72);
            index += 1;
            window.setTimeout(next, 850);
        }
        next();
    }

    function checkDictation() {
        const answer = $("#dictation-sentence")?.value || "";
        const typed = $("#dictation-input")?.value || "";
        const result = $("#dictation-results");
        if (!result) {
            return;
        }
        const answerWords = normalizeText(answer).split(" ").filter(Boolean);
        const typedWords = normalizeText(typed).split(" ").filter(Boolean);
        let matches = 0;
        answerWords.forEach((word, index) => {
            if (typedWords[index] === word) {
                matches += 1;
            }
        });
        const percent = answerWords.length ? Math.round((matches / answerWords.length) * 100) : 0;
        const missing = answerWords.filter((word) => !typedWords.includes(word)).slice(0, 8);
        result.innerHTML = `
            <h3>${percent}% word-position match</h3>
            <p class="result-note">${missing.length ? `Review these words: ${escapeHtml(missing.join(", "))}.` : "Strong match. Replay at natural speed and shadow the sentence."}</p>
        `;
    }

    function showDictationAnswer() {
        const answer = $("#dictation-sentence")?.value || "";
        const result = $("#dictation-results");
        if (result) {
            result.innerHTML = `<h3>Answer</h3><p>${escapeHtml(answer)}</p>`;
        }
    }

    function transformRegister() {
        const input = $("#register-input")?.value.trim() || "";
        const target = $("#register-target")?.value || "neutral";
        const result = $("#register-results");
        if (!result) {
            return;
        }
        if (!input) {
            result.innerHTML = `<p class="result-note">Enter a sentence first.</p>`;
            return;
        }
        const base = cleanRegisterBase(input);
        const transformed = {
            casual: casualTransform(base),
            neutral: neutralTransform(base),
            academic: academicTransform(base),
            business: businessTransform(base),
            diplomatic: diplomaticTransform(base),
        }[target];
        const moves = registerMoves(target);
        result.innerHTML = `
            <h3>${escapeHtml(registerLabel(target))}</h3>
            <div class="before-after">
                <p><strong>Original</strong><br>${escapeHtml(input)}</p>
                <p><strong>Transformed</strong><br>${escapeHtml(transformed)}</p>
            </div>
            <div class="result-list">
                <article>
                    <strong>Register moves</strong>
                    <ul>${moves.map((move) => `<li>${escapeHtml(move)}</li>`).join("")}</ul>
                </article>
            </div>
        `;
    }

    function cleanRegisterBase(value) {
        return value
            .replace(/\bthis is wrong\b/gi, "this may need revision")
            .replace(/\byour team must\b/gi, "your team should")
            .replace(/\bhas problems\b/gi, "has some issues")
            .replace(/\bfix it soon\b/gi, "address it soon")
            .replace(/\bneed to fix\b/gi, "need to address")
            .replace(/\s+/g, " ")
            .trim()
            .replace(/[.!?]+$/, "");
    }

    function casualTransform(base) {
        return sentenceCase(base.replace(/\bI think\b/i, "I feel like").replace(/\bneed to\b/gi, "should")) + ".";
    }

    function neutralTransform(base) {
        return sentenceCase(base.replace(/\bmust\b/gi, "should").replace(/\bwrong\b/gi, "not accurate")) + ".";
    }

    function academicTransform(base) {
        return `The issue can be framed as follows: ${base.toLowerCase()}, which suggests that further analysis and revision may be required.`;
    }

    function businessTransform(base) {
        return `There are several points to address here: ${base.toLowerCase()}. We should align on the next steps soon.`;
    }

    function diplomaticTransform(base) {
        return `I see some areas we may want to revisit: ${base.toLowerCase()}. It would be helpful to address them together soon.`;
    }

    function registerMoves(target) {
        return {
            casual: ["Uses shorter wording.", "Sounds more conversational.", "Reduces formal distance."],
            neutral: ["Keeps the message clear.", "Avoids blame.", "Uses standard workplace wording."],
            academic: ["Adds analytical framing.", "Uses cautious claims.", "Connects the idea to evidence or revision."],
            business: ["Focuses on action and alignment.", "Names risk without sounding personal.", "Moves toward next steps."],
            diplomatic: ["Softens criticism.", "Uses shared responsibility.", "Keeps the relationship protected."],
        }[target];
    }

    function registerLabel(target) {
        return {
            casual: "Casual English",
            neutral: "Neutral English",
            academic: "Academic English",
            business: "Business English",
            diplomatic: "Diplomatic English",
        }[target] || target;
    }

    function wireEvents() {
        $("#diagnostic-submit")?.addEventListener("click", runDiagnostic);
        $("#diagnostic-reset")?.addEventListener("click", resetDiagnostic);
        $("#repair-run")?.addEventListener("click", runSentenceRepair);
        $("#shadow-speak")?.addEventListener("click", playShadowModel);
        $("#shadow-record")?.addEventListener("click", startRecording);
        $("#shadow-stop")?.addEventListener("click", stopRecording);
        $("#vocab-load")?.addEventListener("click", loadVocabDeck);
        $("#vocab-reset")?.addEventListener("click", resetVocabReview);
        $("#vocab-reveal")?.addEventListener("click", () => {
            state.vocabRevealed = true;
            renderVocabCard();
        });
        $("#vocab-again")?.addEventListener("click", () => rateVocabCard(0));
        $("#vocab-good")?.addEventListener("click", () => rateVocabCard(1));
        $("#vocab-know")?.addEventListener("click", () => rateVocabCard(7));
        $("#news-build")?.addEventListener("click", buildNewsTask);
        $("#news-draft")?.addEventListener("input", updateWordCount);
        $("#phrase-build")?.addEventListener("click", buildPhraseCoach);
        $("#phrase-scenario")?.addEventListener("change", buildPhraseCoach);
        $("#phrase-tone")?.addEventListener("change", buildPhraseCoach);
        $("#collocation-start")?.addEventListener("click", startCollocation);
        $$("[data-dictation-rate]").forEach((button) => {
            button.addEventListener("click", () => playDictation(button.dataset.dictationRate));
        });
        $("#dictation-word")?.addEventListener("click", playDictationWords);
        $("#dictation-check")?.addEventListener("click", checkDictation);
        $("#dictation-show")?.addEventListener("click", showDictationAnswer);
        $("#register-run")?.addEventListener("click", transformRegister);
        $$("[data-sample-target]").forEach((button) => {
            button.addEventListener("click", () => {
                const target = $(`#${button.dataset.sampleTarget}`);
                if (target) {
                    target.value = button.dataset.sampleValue || "";
                    target.focus();
                }
            });
        });
        document.addEventListener("click", (event) => {
            const chip = event.target.closest(".phrase-chip");
            if (!chip) {
                return;
            }
            navigator.clipboard?.writeText(chip.dataset.copyText || chip.textContent || "");
            chip.classList.add("phrase-chip-copied");
            window.setTimeout(() => chip.classList.remove("phrase-chip-copied"), 900);
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        renderDiagnostic();
        wireEvents();
        buildPhraseCoach();
        startCollocation();
        buildNewsTask();
        transformRegister();
        hydrateLessons();
    });
})();
