(() => {
    'use strict';
    let active = null;
    let request = 0;
    function stop() {
        request += 1;
        if (!active) return;
        active.audio.pause();
        active.panel.hidden = true;
        active = null;
    }
    document.querySelectorAll('[data-pronunciation]').forEach(link => {
        link.addEventListener('click', event => {
            // Keep normal open/save-link behavior for modified clicks.
            if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
            const panel = link.closest('.module-block')?.querySelector('[data-pronunciation-player]');
            const audio = panel?.querySelector('audio');
            if (!audio || typeof audio.play !== 'function') return;
            event.preventDefault();
            stop();
            const token = request;
            const term = link.dataset.pronunciation;
            const status = panel.querySelector('[data-pronunciation-status]');
            panel.querySelector('[data-pronunciation-fallback]').href = link.href;
            audio.src = link.href;
            audio.setAttribute('aria-label', `Pronunciation of ${term}`);
            panel.hidden = false;
            status.textContent = `Listen: ${term}`;
            active = {audio, panel};
            const failed = () => {
                if (request === token) status.textContent = `Unable to play ${term} here. Try Open audio file.`;
            };
            audio.onerror = failed;
            try { Promise.resolve(audio.play()).catch(failed); }
            catch { failed(); }
        });
    });
    window.addEventListener('hashchange', stop);
    window.addEventListener('pagehide', stop);
})();
