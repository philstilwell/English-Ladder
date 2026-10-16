(() => {
  'use strict';
  function copyFallback(text) {
    const previous = document.activeElement, buffer = document.createElement('textarea');
    buffer.className = 'practice-copy-buffer'; buffer.value = text; buffer.readOnly = true; buffer.tabIndex = -1;
    buffer.setAttribute('aria-hidden', 'true'); document.body.append(buffer);
    try {
      buffer.select();
      if (!document.execCommand('copy')) throw new Error('Copy unavailable');
    } finally {
      buffer.remove();
      if (previous?.isConnected) previous.focus({ preventScroll: true });
    }
  }
  window.PracticePrompt = {
    text(exercise, task) {
      return 'Help me understand this English practice item. Use short, simple English for an adult learner.\n\n' +
        exercise + '\n\n' + task + '\nExplain any grammar terms with a short example. If an answer is ambiguous or the supplied key seems wrong, explain that clearly. ' +
        'Give two short, new example sentences. Then give me one similar practice question. Wait for my reply before giving its answer.';
    },
    create({ prompt, label = '' }) {
      const button = document.createElement('button'), status = document.createElement('p');
      button.type = 'button'; button.className = 'secondary-button practice-copy-button';
      button.title = 'Copy a prompt, then paste it into an AI chat.';
      status.className = 'field-hint practice-copy-status'; status.setAttribute('role', 'status'); status.hidden = true;
      const controls = document.createElement('span'), sites = document.createElement('span');
      controls.className = 'practice-prompt-actions'; sites.className = 'practice-ai-sites';
      sites.setAttribute('role', 'group'); sites.setAttribute('aria-label', 'Choose an AI chat');
      for (const [name, href, logo] of [
        ['ChatGPT', 'https://chatgpt.com/', '/chatgpt-logo.svg'],
        ['Gemini', 'https://gemini.google.com/app', '/gemini-logo.png'],
        ['Claude', 'https://claude.ai/', '/claude-logo.png'],
        ['Microsoft Copilot', 'https://copilot.microsoft.com/', '/copilot-logo.svg'],
      ]) {
        const link = document.createElement('a'), image = document.createElement('img');
        link.className = 'practice-ai-link'; link.href = href; link.target = '_blank';
        link.rel = 'noopener noreferrer'; link.referrerPolicy = 'no-referrer';
        link.title = name + ' (new tab)'; link.setAttribute('aria-label', 'Open ' + name + ' (new tab)');
        image.src = logo; image.alt = ''; image.width = 14; image.height = 14;
        link.append(image); sites.append(link);
      }
      controls.append(button, sites);
      let copying = false, revision = 0;
      function setCopied(copied) {
        button.textContent = copied ? 'AI prompt copied' : 'Copy AI prompt';
        button.setAttribute('aria-label', button.textContent + label); button.classList.toggle('is-copied', copied);
      }
      setCopied(false);
      button.addEventListener('click', async () => {
        if (copying || !button.isConnected) return;
        const current = revision;
        copying = true; button.setAttribute('aria-busy', 'true'); setCopied(false); status.hidden = true;
        try {
          const text = typeof prompt === 'function' ? prompt() : prompt;
          if (typeof text !== 'string' || !text.trim()) throw new Error('Empty prompt');
          if (navigator.clipboard?.writeText) {
            try { await navigator.clipboard.writeText(text); }
            catch (error) { if (!button.isConnected || current !== revision) return; copyFallback(text); }
          } else copyFallback(text);
          if (!button.isConnected || current !== revision) return;
          setCopied(true); status.textContent = 'Choose an AI chat. Paste the prompt there.'; status.hidden = false;
        } catch {
          if (!button.isConnected || current !== revision) return;
          status.textContent = 'The prompt could not be copied. Please try again.'; status.hidden = false;
        } finally {
          copying = false; button.removeAttribute('aria-busy');
        }
      });
      return { button, status, controls, reset() { revision++; setCopied(false); status.hidden = true; status.textContent = ''; } };
    },
  };
})();
