const { test, afterEach } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { JSDOM } = require("jsdom");
const root = path.join(__dirname, "..");
const openWindows = new Set();
afterEach(() => { for (const dom of openWindows) dom.window.close(); openWindows.clear(); });

function load(file, hash = "") {
  const dom = new JSDOM(fs.readFileSync(path.join(root, file), "utf8"), {
    url: `https://englishladder.com/${file}${hash}`, runScripts: "dangerously",
  });
  openWindows.add(dom);
  dom.window.HTMLElement.prototype.scrollIntoView = function () {};
  dom.window.eval(fs.readFileSync(path.join(root, "app.js"), "utf8"));
  dom.window.eval(fs.readFileSync(path.join(root, "learning.js"), "utf8"));
  return dom;
}

test("homepage level choice opens the same story at all three levels", () => {
  const dom = load("index.html");
  const date = dom.window.document.querySelector(".feature-story time").getAttribute("datetime");
  for (const level of ["beginner", "intermediate", "advanced"]) {
    dom.window.document.querySelector(`input[value="${level}"]`).click();
    assert.equal(dom.window.document.querySelector("#feature-start").getAttribute("href"), `${level}.html#lesson-${date}`);
  }
  dom.window.close();
});

test("feature selector uses the newly published date and rejects an external destination", () => {
  const dom = load("index.html");
  const input = dom.window.document.querySelector('input[value="advanced"]');
  input.dataset.lessonHref = "advanced.html#lesson-2030-01-02";
  input.click();
  const link = dom.window.document.querySelector("#feature-start");
  assert.equal(link.getAttribute("href"), "advanced.html#lesson-2030-01-02");
  input.dataset.lessonHref = "https://example.com/";
  input.dispatchEvent(new dom.window.Event("change"));
  assert.equal(link.getAttribute("href"), "advanced.html#lesson-2030-01-02");
});

for (const file of ["beginner.html", "intermediate.html", "advanced.html", ...["city-trees", "food-market"].flatMap(story => ["beginner", "intermediate", "advanced"].map(level => `stories/${story}/${level}.html`))]) {
  test(`${file}: word help, answer correction, navigation, speaking activities, and completion work together`, () => {
    const dom = load(file);
    const document = dom.window.document;
    assert.equal(document.querySelector('.lesson-title-label'), null);
    const lesson = document.querySelector(".daily-lesson");
    lesson.open = true;
    const panels = [...lesson.querySelectorAll(".learning-panel")];
    assert.deepEqual(panels.map(p => p.hidden), [false, true, true]);
    const word = lesson.querySelector(".word-button");
    assert.ok(word, "The reading should offer a vocabulary definition");
    word.click();
    assert.equal(word.getAttribute("aria-expanded"), "true");
    assert.equal(document.getElementById(word.getAttribute("aria-controls")).hidden, false);
    word.dispatchEvent(new dom.window.KeyboardEvent("keydown", { key: "Escape" }));
    assert.equal(word.getAttribute("aria-expanded"), "false");
    panels[0].querySelector(".stage-actions button").click();
    assert.deepEqual(panels.map(p => p.hidden), [true, false, true]);
    const question = panels[1].querySelector(".quiz-question");
    question.querySelector('[data-bg="#e6ffe6"]').click();
    assert.match(question.querySelector(".feedback").textContent, /^Correct:/);
    assert.match(panels[1].querySelector(".practice-progress").textContent, /1 of \d+ questions answered · 1 correct/);
    question.querySelector('[data-bg="#ffe6e6"]').click();
    assert.match(question.querySelector(".feedback").textContent, /^Incorrect:/);
    assert.equal(question.querySelectorAll('[aria-pressed="true"]').length, 1);
    assert.match(panels[1].querySelector(".practice-progress").textContent, /1 of \d+ questions answered · 0 correct/);
    panels[1].querySelector(".stage-actions button:last-child").click();
    assert.deepEqual(panels.map(p => p.hidden), [true, true, false]);
    assert.equal(panels[2].querySelector("textarea,.note-hint"), null);
    const activities = panels[2].querySelector('.discussion-activities').textContent;
    assert.equal(panels[2].querySelectorAll('.discussion-activities > li').length, 6);
    lesson.querySelector(".learning-flow button").click();
    lesson.querySelector(".learning-flow button:last-child").click();
    assert.equal(panels[2].querySelector('.discussion-activities').textContent, activities);
    panels[2].querySelector(".stage-actions button:last-child").click();
    assert.equal(panels[2].querySelector(".completion-message").hidden, false);
    assert.equal(dom.window.localStorage.length, 0, "Speaking activities must not create stored answers");
    dom.window.close();
  });
}

test("a homepage news link opens the requested lesson, including later hash navigation", () => {
  const dom = load("beginner.html");
  const lessons = [...dom.window.document.querySelectorAll(".daily-lesson")];
  const target = lessons[2];
  dom.window.location.hash = target.id;
  dom.window.dispatchEvent(new dom.window.HashChangeEvent("hashchange"));
  assert.equal(target.open, true);
  assert.equal(lessons[0].open, false);
  dom.window.close();
});

test("without JavaScript, all learning content and alternative level links remain available", () => {
  const dom = new JSDOM(fs.readFileSync(path.join(root, "stories/city-trees/beginner.html"), "utf8"));
  const panels = [...dom.window.document.querySelectorAll(".learning-panel")];
  assert.equal(panels.length, 3);
  assert.equal(panels.some(panel => panel.hidden), false);
  assert.equal(dom.window.document.querySelector(".daily-lesson").open, true);
  assert.equal(dom.window.document.querySelectorAll(".story-levels a").length, 3);
  dom.window.close();
});

test("all tool, workplace, grammar, and language scripts still initialize", async () => {
  for (const file of ["tools.html", "efsp.html", "efsp-finance.html", "grammar-concepts/concept-01.html", "us-life.html"]) {
    const dom = load(file);
    dom.window.fetch = async (url) => ({ ok: true, text: async () => fs.readFileSync(path.join(root, url), "utf8") });
    if (file === "tools.html" || file === "us-life.html") {
      dom.window.eval(fs.readFileSync(path.join(root, file === "tools.html" ? "tools.js" : "us-life.js"), "utf8"));
    }
    if (file.startsWith("efsp")) dom.window.eval(fs.readFileSync(path.join(root, "work.js"), "utf8"));
    await new Promise(resolve => setImmediate(resolve));
    assert.ok(dom.window.document.querySelector(".site-header"));
    if (file === "efsp.html") {
      const search = dom.window.document.querySelector("[data-course-search]");
      search.value = "finance";
      search.dispatchEvent(new dom.window.Event("input"));
      const visible = dom.window.document.querySelectorAll("[data-work-course-link]:not([hidden])");
      assert.ok(visible.length > 0 && visible.length < 41);
      assert.equal(dom.window.document.querySelector('a[href="efsp-finance.html"][data-work-course-link]').hidden, false);
    }
    if (file === "tools.html") {
      assert.ok(dom.window.document.querySelector("#diagnostic-questions").children.length);
      assert.ok(dom.window.document.querySelector("#shadow-sentence").options.length);
    }
    dom.window.close();
  }
});

for (const [level, minimum] of [["beginner", 6], ["intermediate", 8], ["advanced", 10]]) {
  test(`${level}: every daily quiz meets its minimum and all questions update the score`, () => {
    const dom = load(`${level}.html`);
    const lessons = [...dom.window.document.querySelectorAll(".daily-lesson")];
    for (const lesson of lessons) {
      const questions = [...lesson.querySelectorAll(".quiz-question")];
      assert.ok(questions.length >= minimum, `${lesson.dataset.lessonKey} needs ${minimum}+ questions`);
      const progress = lesson.querySelector(".practice-progress");
      assert.match(progress.textContent, new RegExp(`^0 of ${questions.length} questions answered`));
    }
    const lesson = lessons[0]; lesson.open = true;
    lesson.querySelectorAll(".learning-flow button")[1].click();
    const questions = [...lesson.querySelectorAll(".quiz-question")];
    const total = questions.length;
    const progress = lesson.querySelector(".practice-progress");
    questions.at(-1).querySelector('[data-bg="#e6ffe6"]').click();
    assert.match(progress.textContent, new RegExp(`1 of ${total} questions answered · 1 correct`));
    for (const question of questions) question.querySelector('[data-bg="#e6ffe6"]').click();
    assert.match(progress.textContent, new RegExp(`${total} of ${total} questions answered · ${total} correct`));
    questions.at(-1).querySelector('[data-bg="#ffe6e6"]').click();
    assert.match(progress.textContent, new RegExp(`${total} of ${total} questions answered · ${total - 1} correct`));
  });
}
