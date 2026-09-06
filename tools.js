(() => {
    const fallbackLessons = {
        beginner: {headline: "A different way to work · practice scenario", brief: "Mina usually takes the bus to work. Today she rides her bike. The weather is dry, and she has time. Tomorrow she may take the bus again."},
        intermediate: {headline: "Choosing a morning journey · practice scenario", brief: "Mina usually commutes by bus, but today she cycles because the weather is dry. She leaves early so she can travel at a comfortable pace. She will decide how to travel tomorrow after checking the weather."},
        advanced: {headline: "A flexible commute · practice scenario", brief: "Although Mina normally commutes by bus, dry weather gives her an opportunity to cycle today. Leaving earlier lets her avoid rushing. Her choice is provisional: she will check tomorrow's conditions before deciding whether to cycle again."},
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
                { text: "A few person attended the meeting.", weakness: "quantity" },
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

    const state = {
        lessons: { ...fallbackLessons },
        recorder: null,
        recordChunks: [],
        recordStream: null,
        recordingUrl: null,
        recordingPending: false,
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

    function shuffled(values) {
        const result = [...values];
        for (let index = result.length - 1; index > 0; index -= 1) {
            const swapIndex = Math.floor(Math.random() * (index + 1));
            [result[index], result[swapIndex]] = [result[swapIndex], result[index]];
        }
        return result;
    }

    function splitSentences(text) {
        return String(text)
            .replace(/\s+/g, " ")
            .split(/(?<=[.!?])\s+/)
            .map((sentence) => sentence.trim())
            .filter((sentence) => sentence.length > 24)
            .slice(0, 8);
    }

    async function hydrateLessons() {
        if (state.hydrated) return;
        if (state.lessonLoading) return state.lessonLoading;
        state.lessonLoading = (async () => {
            try {
                const response = await fetch("lesson-data.json");
                if (!response.ok) throw new Error("Lesson data unavailable");
                const data = await response.json();
                if (!["beginner", "intermediate", "advanced"].every(level => typeof data[level]?.brief === "string" && typeof data[level]?.headline === "string")) throw new Error("Incomplete lesson data");
                for (const level of ["beginner", "intermediate", "advanced"]) state.lessons[level] = data[level];
                state.hydrated = true;
            } catch (_) { /* The explicitly fictional practice scenario remains available. */ }
            populateSentenceSelects();
        })();
        try { await state.lessonLoading; } finally { state.lessonLoading = null; }
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
        const shadowSelect = $("#shadow-sentence");
        if (shadowSelect) {
            shadowSelect.innerHTML = options;
        }
    }

    function renderDiagnostic() {
        const container = $("#diagnostic-questions");
        if (!container) {
            return;
        }
        container.innerHTML = diagnosticQuestions.map((question, index) => {
            const options = shuffled(question.options.map((option, optionIndex) => ({ ...option, optionIndex })));
            return `
            <article class="diagnostic-card">
                <h3>Question ${index + 1}</h3>
                <p>${escapeHtml(question.prompt)}</p>
                <div class="choice-stack">
                    ${options.map((option) => `
                        <label class="choice-row">
                            <input type="radio" name="diagnostic-${index}" value="${option.optionIndex}">
                            <span>${escapeHtml(option.text)}</span>
                        </label>
                    `).join("")}
                </div>
            </article>
        `;
        }).join("");
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
        if (answered < diagnosticQuestions.length) {
            const errors = Object.values(scores).reduce((sum, count) => sum + count, 0);
            result.innerHTML = `<h3>Keep going</h3><p>${answered} of ${diagnosticQuestions.length} answered; ${answered - errors} correct so far. Answer the remaining questions to see suggested topics.</p>`;
            return;
        }
        const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
        if (!ranked.length) {
            result.innerHTML = `
                <h3>All 10 questions correct</h3>
                <p class="result-note">You answered this short practice check correctly. It is not a placement test. Choose a lesson that feels useful and try applying the grammar in your own writing.</p>
            `;
            return;
        }
        result.innerHTML = `
            <h3>Your study path</h3>
            <div class="result-list">
                ${ranked.map(([key, count]) => `
                    <article>
                        <strong>${escapeHtml(labelForWeakness(key))}</strong>
                        <p>${escapeHtml(diagnosticFeedback(key, count))}</p>
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

    function diagnosticFeedback(key, count) {
        const missed = `You missed ${count} question${count === 1 ? "" : "s"}`;
        return {
            prepositions: `${missed} about choosing the right preposition for places, dates, days, or exact times.`,
            tense: `${missed} about matching verb tense to time, such as past events, recent actions, or ongoing situations.`,
            wordForm: `${missed} about choosing the correct word form, such as noun vs verb or -ing vs -ed adjectives.`,
            clauses: `${missed} about connecting ideas in a sentence, including words like while, because, that, which, even if, and only.`,
            quantity: `${missed} about countable and uncountable nouns, including words like few, little, many, much, so, and such.`,
            usage: `${missed} about natural verb patterns and word choice, such as suggest, recommend, say, tell, refuse, and reject.`,
        }[key] || `${missed} in this skill area.`;
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
        const original = $("#repair-input")?.value.trim() || "";
        let revised = original;
        const level = $("#repair-level")?.value || "intermediate";
        const issues = [];

        function addIssue(label, message, href) {
            issues.push({ label, message, href });
        }

        function apply(pattern, replacement, issue) {
            if (pattern.test(revised)) {
                addIssue(issue.label, issue.message + " Possible wording: “" + revised.replace(pattern, replacement) + "” Check that this keeps your meaning.", issue.href);
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
        apply(/\b(suggested|recommended) that (I|you|he|she|we|they) to ([a-z]+)\b/gi, "$1 that $2 $3", {
            label: "Verb pattern after suggested/recommended",
            message: "After suggested or recommended that + subject, use the base verb without to: suggested that I apply.",
            href: "grammar-concepts/concept-17.html",
        });
        apply(/\bsuggested me to\b/gi, "suggested that I", {
            label: "Verb pattern after suggested",
            message: "Use suggested that + subject + base verb: suggested that I apply.",
            href: "grammar-concepts/concept-17.html",
        });
        apply(/\brecommended me to\b/gi, "recommended that I", {
            label: "Verb pattern after recommended",
            message: "Use recommended that + subject + base verb: recommended that I apply.",
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
        if (/\blittle people\b/i.test(original)) {
            addIssue("Few or little?", "Little people can mean small people. If you mean a small number of people, use few people or a few people. Keep little if size is your meaning.", "grammar-concepts/concept-27.html");
        }
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
            ? "Also check whether the verb shows the exact relationship: cause, contrast, recommendation, or concession."
            : "Read the example aloud. Make sure the verb pattern and preposition fit the meaning.";
        result.innerHTML = `
            <h3>Sentence feedback</h3>
            <div class="before-after">
                <p><strong>Your sentence</strong><br>${escapeHtml($("#repair-input").value.trim())}</p>
                <p><strong>Check the suggestions below</strong><br>Your original text is unchanged. This tool checks a small set of patterns; it does not assess every sentence.</p>
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
            ` : `<p class="result-note">None of this tool’s limited patterns matched. This does not certify the sentence as correct. ${escapeHtml(extra)}</p>`}
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
        if (state.recordingPending || state.recorder?.state === "recording") return;
        state.recordingPending = true;
        state.recordingCancelled = false;
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            if (state.recordingCancelled) {
                stream.getTracks().forEach((track) => track.stop());
                return;
            }
            state.recordStream = stream;
            state.recordChunks = [];
            const mimeType = ["audio/webm;codecs=opus", "audio/mp4", "audio/webm"].find((type) => MediaRecorder.isTypeSupported?.(type));
            state.recorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);
            state.recorder.addEventListener("error", releaseRecording);
            state.recorder.addEventListener("dataavailable", (event) => {
                if (event.data.size > 0) {
                    state.recordChunks.push(event.data);
                }
            });
            state.recorder.addEventListener("stop", () => {
                if (state.recordingCancelled) { releaseRecording(); return; }
                const blob = new Blob(state.recordChunks, { type: state.recorder.mimeType || state.recordChunks[0]?.type || "" });
                const audio = $("#shadow-playback");
                if (audio) {
                    if (state.recordingUrl) URL.revokeObjectURL(state.recordingUrl);
                    state.recordingUrl = URL.createObjectURL(blob);
                    audio.src = state.recordingUrl;
                    audio.hidden = false;
                }
                releaseRecording();
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
            releaseRecording();
            if (result) {
                result.innerHTML = `<p class="result-note">Microphone recording is not available in this browser session.</p>`;
            }
        } finally { state.recordingPending = false; }
    }

    function releaseRecording() {
        state.recordStream?.getTracks().forEach((track) => track.stop());
        state.recordStream = null;
        if ($("#shadow-record")) $("#shadow-record").disabled = false;
        if ($("#shadow-stop")) $("#shadow-stop").disabled = true;
    }
    window.addEventListener("pagehide", () => {
        state.recordingCancelled = true;
        releaseRecording();
        if (state.recordingUrl) URL.revokeObjectURL(state.recordingUrl);
        state.recordingUrl = null;
    });

    function stopRecording() {
        if (state.recorder && state.recorder.state !== "inactive") {
            state.recorder.stop();
        }
    }

    async function buildNewsTask() {
        await hydrateLessons();
        const level = $("#news-level")?.value || "intermediate";
        const skill = $("#news-skill")?.value || "summary";
        const lesson = state.lessons[level];
        const result = $("#news-results");
        if (!result) {
            return;
        }
        const tasks = {
            summary: [`Write a ${level === "beginner" ? "1–2" : "2–3"} sentence summary.`, "Use only information in the story. Leave out details it does not give.", "Preserve words such as may or might when the outcome is uncertain."],
            discussion: ["Prepare three spoken answers.", "What happened?", "Why does it matter?", "What question would you ask next?"],
            opinion: ["Write one clear opinion paragraph.", "Label your view as an opinion, give one reason, and add an example.", "Separate your own prediction from what the story reports."],
            coworker: ["Explain the story to a coworker in one minute.", "Use simple context first, then the key detail.", "End with why the coworker should care."],
            email: ["Write a short email update.", "Use a subject line and a brief summary. Do not invent facts or official advice.", "Keep the tone neutral and professional."],
        };
        result.innerHTML = `
            <h3>${escapeHtml(lesson.headline)}</h3>
            ${state.hydrated ? "" : `<p class="result-note">The latest news could not be loaded. This fictional scenario is available for practice.</p>`}
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
        const examples = {
            "I think this plan has problems and we need to fix it soon.": {
                casual: "I think there are problems with this plan. We need to fix them soon.",
                neutral: "I think this plan has problems that we need to address soon.",
                academic: "In my view, this plan has problems that require prompt attention.",
                business: "I think we need to address the problems in this plan soon.",
                diplomatic: "I think there are problems with this plan that we need to address soon."
            },
            "This is wrong and your team must change it.": {
                casual: "This is wrong. Your team must change it.",
                neutral: "This is incorrect, and your team must change it.",
                academic: "This is incorrect and must be changed by your team.",
                business: "Your team must change this because it is incorrect.",
                diplomatic: "This is incorrect. Please make the required change with your team."
            }
        };
        const transformed = examples[input]?.[target] || input;
        const supported = Boolean(examples[input]);
        const moves = registerMoves(target);
        result.innerHTML = `
            <h3>${escapeHtml(registerLabel(target))}</h3>
            <div class="before-after">
                <p><strong>Original</strong><br>${escapeHtml(input)}</p>
                <p><strong>${supported ? "One possible version" : "Your wording, preserved"}</strong><br>${escapeHtml(transformed)}</p>
            </div>
            <div class="result-list">
                <article>
                    <strong>${supported ? "Compare the choices" : "Guidance for your sentence"}</strong><p>${supported ? "Compare the wording and decide which fits your audience." : "Custom sentences are not automatically rewritten. Use these prompts to revise your own text, or select Use sample to compare edited examples."}</p>
                    <ul>${moves.map((move) => `<li>${escapeHtml(move)}</li>`).join("")}</ul>
                </article>
            </div>
        `;
    }

    function registerMoves(target) {
        return {
            casual: ["Uses shorter wording.", "Sounds more conversational.", "Keep obligations such as must if they matter."],
            neutral: ["Keeps the message clear.", "Avoids blame.", "Uses standard workplace wording."],
            academic: ["Use precise words; longer words are not automatically better.", "Keep names, facts, and the original degree of certainty.", "Add evidence only when you have it."],
            business: ["Focuses on action and alignment.", "Names risk without sounding personal.", "Moves toward next steps."],
            diplomatic: ["Softens criticism.", "Do not change who is responsible.", "Keeps the relationship protected."],
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
        const toolPanels = $$(".tool-panel");
        toolPanels.forEach((panel) => {
            panel.addEventListener("toggle", () => {
                if (!panel.open) {
                    return;
                }
                if (panel.id === "shadowing-studio") hydrateLessons();
                toolPanels.forEach((otherPanel) => {
                    if (otherPanel !== panel) {
                        otherPanel.open = false;
                    }
                });
            });
        });
        $("#diagnostic-submit")?.addEventListener("click", runDiagnostic);
        $("#diagnostic-reset")?.addEventListener("click", resetDiagnostic);
        $("#repair-run")?.addEventListener("click", runSentenceRepair);
        $("#shadow-speak")?.addEventListener("click", playShadowModel);
        $("#shadow-record")?.addEventListener("click", startRecording);
        $("#shadow-stop")?.addEventListener("click", stopRecording);
        $("#news-build")?.addEventListener("click", buildNewsTask);
        $("#news-draft")?.addEventListener("input", updateWordCount);
        $("#phrase-build")?.addEventListener("click", buildPhraseCoach);
        $("#phrase-scenario")?.addEventListener("change", buildPhraseCoach);
        $("#phrase-tone")?.addEventListener("change", buildPhraseCoach);
        $$(".tools-jump-grid a[href^='#']").forEach((link) => {
            link.addEventListener("click", () => {
                const targetId = link.getAttribute("href")?.slice(1);
                const target = targetId ? document.getElementById(targetId) : null;
                if (target?.tagName.toLowerCase() === "details") {
                    target.open = true;
                }
            });
        });
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
        populateSentenceSelects();
        transformRegister();
    });
})();
