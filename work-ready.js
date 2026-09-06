(() => {
  'use strict';
  document.querySelectorAll('[data-copy-finished]').forEach(button => {
    const id = button.dataset.copyFinished;
    const text = document.getElementById(id);
    const status = document.querySelector(`[data-finished-status="${id}"]`);
    if (!text || !status) return;
    button.hidden = false;
    button.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(text.textContent);
        status.textContent = 'Complete prompt copied. Paste it into a new AI chat exactly as it is.';
      } catch (_) {
        text.focus();
        const selection = window.getSelection(), range = document.createRange();
        range.selectNodeContents(text); selection.removeAllRanges(); selection.addRange(range);
        status.textContent = 'The complete prompt is selected. Use your device’s Copy command, then paste it into a new AI chat.';
      }
    });
  });
})();
