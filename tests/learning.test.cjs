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
  for (const level of ["beginner", "intermediate", "advanced"]) {
    dom.window.document.querySelector(`input[value="${level}"]`).click();
    assert.equal(dom.window.document.querySelector("#feature-start").getAttribute("href"), `stories/city-trees/${level}.html`);
  }
  dom.window.close();
});

for (const file of ["beginner.html", "intermediate.html", "advanced.html", ...["city-trees", "food-market"].flatMap(story => ["beginner", "intermediate", "advanced"].map(level => `stories/${story}/${level}.html`))]) {
  test(`${file}: word help, answer correction, navigation, notes, and completion work together`, () => {
    const dom = load(file);
    const document = dom.window.document;
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
    const notes = panels[2].querySelector("textarea");
    notes.value = "One thing I learned today.";
    lesson.querySelector(".learning-flow button").click();
    lesson.querySelector(".learning-flow button:last-child").click();
    assert.equal(notes.value, "One thing I learned today.");
    panels[2].querySelector(".stage-actions button:last-child").click();
    assert.equal(panels[2].querySelector(".completion-message").hidden, false);
    assert.equal(dom.window.localStorage.length, 0, "Optional notes must not be stored");
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
    await new Promise(resolve => setImmediate(resolve));
    assert.ok(dom.window.document.querySelector(".site-header"));
    if (file === "efsp.html") {
      const search = dom.window.document.querySelector("[data-efsp-search]");
      search.value = "Finance English";
      search.dispatchEvent(new dom.window.Event("input"));
      const count = dom.window.document.querySelector("[data-efsp-directory-count]").textContent;
      assert.match(count, /1 track/);
    }
    if (file === "tools.html") {
      assert.ok(dom.window.document.querySelector("#diagnostic-questions").children.length);
      assert.ok(dom.window.document.querySelector("#shadow-sentence").options.length);
    }
    dom.window.close();
  }
});
