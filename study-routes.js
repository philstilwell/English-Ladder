/* Optional route navigation uses the page address, not saved learning records. */
(() => {
  'use strict';
  const data = document.querySelector('[data-study-routes]');
  const routeKey = new URL(location.href).searchParams.get('route');
  if (!data || !routeKey) return;
  let catalog;
  try { catalog = JSON.parse(data.textContent); } catch (_) { return; }
  if (!Object.hasOwn(catalog, routeKey)) return;
  const route = catalog[routeKey];
  const root = new URL(data.dataset.siteRoot, location.href);
  const level = location.pathname.match(/\/(beginner|intermediate|advanced)\.html$/)?.[1] || 'beginner';
  const guide = new URL(`study-routes.html#${routeKey}`, root).href;
  let activeIndex = -1;

  function matches(step, url) {
    const pattern = new URL(step.path.replace('{level}', level).replace('{date}', 'DATE'), root);
    const samePage = step.path.includes('{date}')
      ? /^\/news\/\d{4}-\d{2}-\d{2}\/(beginner|intermediate|advanced)\.html$/.test(url.pathname.slice(root.pathname.length - 1))
      : url.pathname === pattern.pathname;
    return samePage && (!pattern.hash || url.hash === pattern.hash);
  }
  function link(text, href, className) {
    const a = document.createElement('a');
    a.textContent = text; a.href = href;
    if (className) a.className = className;
    return a;
  }
  function showRoute() {
    const url = new URL(location.href);
    let index = route.steps.findIndex(step => matches(step, url));
    // Skip links and language controls keep the selected unit, so keep its route too.
    const anchorTarget = document.getElementById(url.hash.slice(1));
    if (index < 0 && activeIndex >= 0 && url.hash && !anchorTarget?.matches('.us-life-module, .work-module')) {
      const previous = new URL(route.steps[activeIndex].path, root);
      if (previous.pathname === url.pathname) index = activeIndex;
    }
    document.querySelectorAll('[data-route-navigation]').forEach(node => node.remove());
    document.querySelectorAll('[data-route-suppressed]').forEach(node => {
      node.hidden = false; delete node.dataset.routeSuppressed;
    });
    activeIndex = index;
    if (index < 0) return;
    const step = route.steps[index];
    const anchor = step.path.split('#')[1];
    const host = anchor ? document.getElementById(anchor) : document.querySelector('.daily-lesson');
    if (!host) return;

    // Keep the same route when switching between versions of a reading.
    document.querySelectorAll('[data-level-choice]').forEach(a => {
      const target = new URL(a.href, location.href);
      target.searchParams.set('route', routeKey); a.href = target.href;
    });
    const progress = document.createElement('p');
    progress.className = 'study-route-progress'; progress.dataset.routeNavigation = '';
    const label = document.createElement('span');
    label.textContent = `${route.title} · Activity ${index+1} of ${route.steps.length}`;
    progress.append(label, link('View all 3 activities', guide));
    if (host.tagName === 'DETAILS') host.querySelector(':scope > summary').after(progress);
    else host.prepend(progress);

    // A chosen route replaces the US-life unit's ordinary, different next step.
    host.querySelectorAll('.life-practice > a').forEach(a => {
      if (!a.hidden) { a.hidden = true; a.dataset.routeSuppressed = ''; }
    });
    const next = document.createElement('nav');
    next.className = 'study-route-next'; next.dataset.routeNavigation = '';
    next.setAttribute('aria-label', 'Next activity in your study route');
    const instruction = document.createElement('p');
    if (index + 1 < route.steps.length) {
      instruction.textContent = `When you are ready for activity ${index+2}:`;
      const following = route.steps[index+1];
      const target = new URL((following.href || following.path).replace('{level}', level), root);
      target.searchParams.set('route', routeKey);
      next.append(instruction, link(`Next: ${following.title} →`, target.href, 'primary-button'));
    } else {
      instruction.textContent = 'This is the last activity in this route. Revisit any activity whenever you like.';
      next.append(instruction, link('Back to study routes →', guide, 'primary-button'));
    }
    host.append(next);
  }
  showRoute();
  window.addEventListener('hashchange', showRoute);
})();
