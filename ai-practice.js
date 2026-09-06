/* Copy published, inspectable prompt text. No AI requests, account, or draft access. */
(() => {
  document.querySelectorAll('[data-ai-copy-text]').forEach(button => {
    const card = button.closest('[data-ai-card]');
    const prompt = document.getElementById(button.dataset.aiCopyText);
    const status = card?.querySelector('[data-ai-copy-status]');
    if (!prompt || !status) return;
    button.hidden = false;
    button.addEventListener('click', async () => {
      button.disabled = true;
      status.textContent = '';
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(prompt.textContent);
        status.textContent = 'Prompt copied. Paste it into your chosen AI.';
      } catch (_) {
        prompt.closest('details').open = true;
        prompt.focus();
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(prompt);
        selection?.removeAllRanges(); selection?.addRange(range);
        status.textContent = 'Automatic copying is unavailable. The prompt is selected: press Ctrl+C or Command+C, or use your device’s Copy command.';
      } finally {
        button.disabled = false;
      }
    });
  });
})();
