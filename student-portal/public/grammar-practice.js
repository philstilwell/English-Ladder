(() => {
  'use strict';
  const PAGE_SIZE = 10;
  function answerSentence({ prompt, answer }) {
    // Braces hold source instructions, not part of the sentence. Multi-gap
    // answers use slash-separated words in the same order as the blanks.
    const sentence = prompt.replace(/\{[^}]*\}/g, '').trim();
    const gaps = sentence.match(/_+/g) || [];
    if (gaps.length) {
      const parts = gaps.length > 1 ? answer.split(/\s*\/\s*/) : [answer];
      let index = 0;
      return sentence.replace(/_+/g, () => parts[index++]).replace(/\s+([.,!?;:])/g, '$1');
    }
    const completed = sentence ? sentence + ' ' + answer : answer;
    return /[.!?]$/.test(completed) ? completed : completed + '.';
  }
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  window.GrammarPractice = {
    create({ root, api, expired }) {
      // All interaction stays in this page's memory. There is no save endpoint.
      let revision = 0, active = false, items = [], page = 0;
      function clear() {
        revision++; active = false; items = []; page = 0;
        root.replaceChildren(); root.hidden = true; root.removeAttribute('aria-busy');
      }
      function render(focus = false) {
        const start = page * PAGE_SIZE, end = Math.min(start + PAGE_SIZE, items.length);
        const range = index => `${index * PAGE_SIZE + 1}–${Math.min((index + 1) * PAGE_SIZE, items.length)}`;
        const intro = element('p', `${items.length} items, from easier to harder. Choose any group.`, 'field-hint');
        const picker = element('div', '', 'grammar-picker');
        const label = element('label', 'Choose items'); label.htmlFor = 'grammar-group';
        const select = element('select'); select.id = 'grammar-group';
        for (let index = 0; index < Math.ceil(items.length / PAGE_SIZE); index++) {
          const option = element('option', range(index)); option.value = String(index); select.append(option);
        }
        select.value = String(page);
        select.addEventListener('change', () => { page = Number(select.value); render(true); });
        picker.append(label, select);
        const heading = element('h4', `Items ${range(page)}`, 'grammar-heading'); heading.tabIndex = -1;
        const list = element('ol', '', 'grammar-items'); list.start = start + 1;
        for (const item of items.slice(start, end)) {
          const row = element('li', '', 'grammar-item');
          const prompt = element('p', '', 'grammar-prompt'); prompt.setAttribute('aria-live', 'polite');
          const sentence = element('q', item.prompt); sentence.id = 'grammar-sentence-' + item.number; prompt.append(sentence);
          const options = element('ul', '', 'grammar-options'); options.setAttribute('aria-label', 'Choices for item ' + item.number);
          for (const text of item.options) { const option = element('li'); option.append(element('q', text)); options.append(option); }
          const reveal = element('label', '', 'grammar-reveal');
          const checkbox = element('input'); checkbox.type = 'checkbox'; checkbox.autocomplete = 'off';
          checkbox.setAttribute('aria-label', 'Show answer for item ' + item.number);
          checkbox.setAttribute('aria-controls', sentence.id);
          checkbox.addEventListener('change', () => {
            sentence.textContent = checkbox.checked ? answerSentence(item) : item.prompt;
            prompt.classList.toggle('is-revealed', checkbox.checked);
          });
          reveal.append(checkbox, element('span', 'Show answer'));
          row.append(prompt, options, reveal); list.append(row);
        }
        const controls = element('div', '', 'grammar-controls');
        const previous = element('button', 'Previous 10', 'secondary-button'); previous.type = 'button'; previous.disabled = page === 0;
        const next = element('button', 'Next 10', 'secondary-button'); next.type = 'button'; next.disabled = end === items.length;
        previous.addEventListener('click', () => { if (page > 0) { page--; render(true); } });
        next.addEventListener('click', () => { if (end < items.length) { page++; render(true); } });
        controls.append(previous, next);
        root.replaceChildren(intro, picker, heading, list, controls);
        if (focus) { heading.focus(); heading.scrollIntoView?.({ block: 'start' }); }
      }
      async function open() {
        if (active) return;
        active = true; const current = ++revision;
        root.hidden = false; root.setAttribute('aria-busy', 'true');
        const loading = element('p', 'Loading grammar practice…'); loading.setAttribute('role', 'status'); root.replaceChildren(loading);
        try {
          const data = await api('/api/grammar-practice');
          if (current !== revision) return;
          if (!Array.isArray(data.items) || !data.items.length || data.items.length > 1000 || data.items.some((item, index) =>
            item?.number !== index + 1 || typeof item.prompt !== 'string' || !item.prompt.trim() ||
            typeof item.answer !== 'string' || !item.answer.trim() || !Array.isArray(item.options) || item.options.length !== 4 ||
            item.options.some(option => typeof option !== 'string' || !option.trim()) || !item.options.includes(item.answer) ||
            ((item.prompt.match(/_+/g) || []).length > 1 && item.answer.split(/\s*\/\s*/).length !== item.prompt.match(/_+/g).length))) throw new Error('Invalid practice items');
          items = data.items; page = 0; root.removeAttribute('aria-busy'); render();
        } catch (error) {
          if (current !== revision || expired(error)) return;
          root.removeAttribute('aria-busy');
          const message = element('p', 'Grammar practice could not load. Please try again.'); message.setAttribute('role', 'alert');
          const retry = element('button', 'Try again', 'secondary-button'); retry.type = 'button';
          retry.addEventListener('click', () => { active = false; open(); });
          root.replaceChildren(message, retry);
        }
      }
      return { open, clear };
    },
  };
})();
