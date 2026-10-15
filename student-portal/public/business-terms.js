(() => {
  'use strict';
  const blanks = /⎛#([1-6])⎞/g;
  const node = (tag, text, className) => {
    const el = document.createElement(tag);
    if (text) el.textContent = text;
    if (className) el.className = className;
    return el;
  };
  function validItems(items) {
    if (!Array.isArray(items) || !items.length || items.length > 5000) return false;
    return items.every((item, index) => {
      if (!Number.isInteger(item?.number) || item.number < 1 || index && item.number <= items[index - 1].number ||
          typeof item.term !== 'string' || !item.term.trim() ||
          !Array.isArray(item.sentences) || item.sentences.length !== 3 || item.sentences.some(s => typeof s !== 'string' || !s.trim()) ||
          !Array.isArray(item.answers) || item.answers.length !== 6 || item.answers.some(s => typeof s !== 'string' || !s.trim()) ||
          !Array.isArray(item.options) || item.options.length !== 6 || item.options.some(s => typeof s !== 'string' || !s.trim())) return false;
      const ids = item.sentences.flatMap(s => [...s.matchAll(blanks)].map(match => match[1])).sort();
      const compare = values => values.map(s => s.toLowerCase()).sort().join('|');
      return ids.join() === '1,2,3,4,5,6' && compare(item.answers) === compare(item.options);
    });
  }
  window.BusinessTerms = {
    create({ root, api, expired }) {
      let revision = 0, active = false, items = [], position = 0;
      function clear() {
        revision++; active = false; items = []; position = 0;
        root.replaceChildren(); root.hidden = true; root.removeAttribute('aria-busy');
      }
      function render(focus = false) {
        const item = items[position];
        const intro = node('p', `${items.length.toLocaleString('en')} exercises, from easier to harder. Choose any item.`, 'field-hint');
        const jump = node('form', '', 'terms-jump');
        const label = node('label', 'Go to item'); label.htmlFor = 'terms-number';
        const number = node('input'); number.id = 'terms-number'; number.type = 'number'; number.inputMode = 'numeric';
        number.min = '1'; number.max = String(items.at(-1).number); number.step = '1'; number.required = true;
        number.value = String(item.number); number.autocomplete = 'off'; number.setAttribute('aria-describedby', 'terms-jump-status');
        const go = node('button', 'Go', 'secondary-button'); go.type = 'submit';
        const status = node('p', '', 'field-hint'); status.id = 'terms-jump-status'; status.setAttribute('role', 'status');
        jump.append(label, number, go);
        jump.addEventListener('submit', event => {
          event.preventDefault();
          const next = items.findIndex(entry => entry.number === Number(number.value));
          if (next === -1) { status.textContent = 'This item is not available. Try another number.'; return; }
          position = next; render(true);
        });
        const title = node('h4', `Item ${item.number} · “${item.term}”`, 'terms-heading'); title.tabIndex = -1;
        const wordHeading = node('p', 'Words to use', 'terms-label');
        const words = node('ul', '', 'terms-words'); words.setAttribute('aria-label', 'Six words in alphabetical order');
        for (const word of item.options) { const entry = node('li'); entry.append(node('q', word)); words.append(entry); }
        const hint = node('p', 'Use each word once. If a word is shown twice, use it twice.', 'field-hint');
        const sentences = node('ol', '', 'terms-sentences'); sentences.id = 'terms-sentences'; sentences.setAttribute('aria-live', 'polite');
        function showAnswers(revealed) {
          sentences.replaceChildren(); sentences.classList.toggle('is-revealed', revealed);
          for (const sentence of item.sentences) {
            const quote = node('q');
            if (revealed) {
              let offset = 0;
              for (const match of sentence.matchAll(blanks)) {
                quote.append(sentence.slice(offset, match.index), node('span', item.answers[Number(match[1]) - 1], 'terms-answer'));
                offset = match.index + match[0].length;
              }
              quote.append(sentence.slice(offset));
            } else {
              quote.textContent = sentence.replace(blanks, (_, id) => `____ (${id})`);
            }
            const line = node('li'); line.append(quote); sentences.append(line);
          }
        }
        showAnswers(false);
        const reveal = node('label', '', 'terms-reveal');
        const checkbox = node('input'); checkbox.type = 'checkbox'; checkbox.autocomplete = 'off'; checkbox.setAttribute('aria-controls', sentences.id);
        checkbox.addEventListener('change', () => showAnswers(checkbox.checked));
        reveal.append(checkbox, node('span', 'Show answers'));
        const controls = node('div', '', 'terms-controls');
        const previous = node('button', 'Previous', 'secondary-button'); previous.type = 'button'; previous.disabled = position === 0;
        const next = node('button', 'Next', 'secondary-button'); next.type = 'button'; next.disabled = position === items.length - 1;
        previous.addEventListener('click', () => { if (position > 0) { position--; render(true); } });
        next.addEventListener('click', () => { if (position < items.length - 1) { position++; render(true); } });
        controls.append(previous, next);
        root.replaceChildren(intro, jump, status, title, wordHeading, words, hint, sentences, reveal, controls);
        if (focus) { title.focus(); title.scrollIntoView?.({ block: 'start' }); }
      }
      async function open() {
        if (active) return;
        active = true; const current = ++revision;
        root.hidden = false; root.setAttribute('aria-busy', 'true');
        const loading = node('p', 'Loading business terms…'); loading.setAttribute('role', 'status'); root.replaceChildren(loading);
        try {
          const data = await api('/api/business-terms');
          if (current !== revision) return;
          if (!validItems(data.items)) throw new Error('Incomplete practice content');
          items = data.items; position = 0; root.removeAttribute('aria-busy'); render();
        } catch (error) {
          if (current !== revision || expired(error)) return;
          root.removeAttribute('aria-busy');
          const message = node('p', 'Business terms could not load. Please try again.'); message.setAttribute('role', 'alert');
          const retry = node('button', 'Try again', 'secondary-button'); retry.type = 'button';
          retry.addEventListener('click', () => { active = false; open(); }); root.replaceChildren(message, retry);
        }
      }
      return { open, clear };
    },
  };
})();
