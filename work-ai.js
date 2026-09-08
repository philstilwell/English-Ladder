/* Local prompt composition only: no AI requests, draft reading or storage. */
(() => {
  'use strict';
  const root = document.querySelector('[data-ai-workshop]');
  if (!root) return;
  let data;
  try { data = JSON.parse(root.querySelector('[data-ai-data]').textContent); }
  catch (_) { return; } // The complete default prompt remains available without JS.
  const mode = root.querySelector('[data-ai-mode]');
  const context = root.querySelector('[data-ai-context]');
  const level = root.querySelector('[data-ai-level]');
  const prompt = root.querySelector('[data-ai-prompt]');
  const status = root.querySelector('[data-ai-status]');
  const download = root.querySelector('[data-ai-download]');
  const link = root.querySelector('[data-ai-link]');
  let revision = 0;
  const validMode = value => data.modes.some(item => item.id === value);
  const validContext = value => data.contexts.some(item => item.id === value);
  const validLevel = value => Object.prototype.hasOwnProperty.call(data.levels, value);

  function render(announce = false) {
    const task = data.modes.find(item => item.id === mode.value);
    const reference = data.contexts.find(item => item.id === context.value);
    if (!task || !reference || !validLevel(level.value)) return;
    revision += 1;
    const original = [data.common, data.levels[level.value],
      `REFERENCE\n${data.course}\n${reference.text}\nEND REFERENCE`, task.instructions].join('\n\n');
    prompt.value = window.EnglishLadderAI?.localizePrompt(original) ?? original;
    root.querySelector('[data-ai-print]').textContent = prompt.value;
    root.querySelector('[data-ai-description]').textContent = task.short;
    const target = new URL(window.location.href);
    target.search = '';
    target.searchParams.set('ai', mode.value);
    target.searchParams.set('context', context.value);
    target.searchParams.set('level', level.value);
    target.hash = 'ai-practice';
    link.href = target.href;
    download.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(prompt.value);
    download.download = `${document.querySelector('[data-work-course]').dataset.workCourse}-${context.value}-${mode.value}-${level.value}-prompt.txt`;
    status.textContent = announce ? `${task.title}. ${reference.title}. ${level.value} prompt ready to copy.` : '';
  }

  function fromUrl() {
    const params = new URL(window.location.href).searchParams;
    mode.value = validMode(params.get('ai')) ? params.get('ai') : 'roleplay';
    context.value = validContext(params.get('context')) ? params.get('context') : 'module-1';
    level.value = validLevel(params.get('level')) ? params.get('level') : 'B2';
    render();
  }

  [mode, context, level].forEach(control => control.addEventListener('change', () => render(true)));
  root.querySelector('[data-ai-copy]').addEventListener('click', async () => {
    const text = prompt.value, copyingRevision = revision;
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      status.textContent = copyingRevision === revision
        ? 'Prompt copied. Paste it into a new chat in your preferred AI.'
        : 'The earlier prompt was copied. Copy again to use your new selection.';
    } catch (_) {
      root.querySelector('.work-ai-preview').open = true;
      prompt.focus(); prompt.select();
      status.textContent = 'Automatic copying is unavailable. The current prompt is selected; use your device’s Copy command, or save it as text.';
    }
  });

  document.querySelectorAll('[data-ai-preset]').forEach(anchor => anchor.addEventListener('click', event => {
    // Preserve native new-tab and modifier-click behavior.
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button) return;
    const target = new URL(anchor.href);
    if (target.pathname !== window.location.pathname) return;
    event.preventDefault();
    const task = target.searchParams.get('ai'), reference = target.searchParams.get('context');
    if (!validMode(task) || !validContext(reference)) return;
    mode.value = task; context.value = reference;
    render(true);
    // Update the address so the browser's Back button can return to the lesson.
    try { window.history.pushState(null, '', link.href); } catch (_) { /* File previews can restrict history. */ }
    root.scrollIntoView?.({block: 'start', behavior: 'auto'});
    mode.focus({preventScroll: true});
  }));
  window.addEventListener('popstate', fromUrl);
  window.addEventListener('ai-explanation-language-changed', () => render());
  fromUrl();
  root.querySelector('[data-ai-controls]').hidden = false;
  root.querySelector('[data-ai-actions]').hidden = false;
})();
