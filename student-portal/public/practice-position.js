(() => {
  'use strict';
  function valid(position) {
    if (!position || (position.number !== null && (!Number.isInteger(position.number) || position.number < 1)) ||
        !Number.isSafeInteger(position.revision) || position.revision < 0) throw new Error('Invalid saved place');
    return position;
  }
  window.PracticePosition = {
    create({ api, expired, path }) {
      let current = null, pending = Promise.resolve();
      const notice = document.createElement('p'); notice.className = 'field-hint practice-position-status'; notice.setAttribute('role', 'status'); notice.hidden = true;
      const message = document.createElement('span'), retry = document.createElement('button'); retry.type = 'button'; retry.className = 'secondary-button'; retry.textContent = 'Try again';
      notice.append(message, ' ', retry);
      function show(state, text = '', canRetry = false, label = 'Try again') {
        if (current !== state) return;
        message.textContent = text; notice.hidden = !text; retry.hidden = !canRetry; retry.textContent = label;
      }
      async function request(options) {
        const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 10000);
        try { return await api(path, { ...options, signal: controller.signal }); } finally { clearTimeout(timer); }
      }
      async function drain(state) {
        state.busy = true;
        try {
          while (state.desired !== state.saved) {
            const number = state.desired;
            show(state, 'Saving your place…');
            try {
              const data = await request({ method: 'PATCH', keepalive: true, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ field: 'position', value: number, revision: state.revision }) });
              const position = valid(data.position);
              state.saved = position.number; state.revision = position.revision;
            } catch (error) {
              if (current === state && expired(error)) return;
              if (error.status === 409) {
                // Read the newer revision, but require another user action before replacing it.
                try {
                  const data = await request(), position = valid(data.position);
                  state.saved = position.number; state.revision = position.revision;
                } catch (readError) {
                  if (current === state && expired(readError)) return;
                }
                show(state, 'Your place changed on another page.', true, 'Save this place');
              } else show(state, 'Your place could not be saved.', true);
              return;
            }
          }
          show(state);
        } finally { state.busy = false; }
      }
      function save(state) {
        if (!state?.writable || state.busy || state.desired === null) return;
        pending = drain(state);
      }
      retry.addEventListener('click', () => save(current));
      return {
        notice,
        settled: () => pending,
        read(position = { number: null, revision: 0 }, writable = false) {
          valid(position);
          current = { saved: position.number, desired: position.number, revision: position.revision, writable, busy: false };
          show(current);
          return position.number;
        },
        remember(number) {
          if (!current?.writable || !Number.isInteger(number) || number < 1) return;
          current.desired = number; save(current);
        },
        clear() {
          // Already requested places finish saving, but cannot change a closed or newer view.
          current = null; notice.hidden = true; message.textContent = ''; retry.hidden = true;
        },
      };
    },
  };
})();
