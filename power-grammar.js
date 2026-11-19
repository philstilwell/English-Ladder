/* Native accordions work without JavaScript. Open ancestors for shared links. */
(() => {
  'use strict';
  const openLinkedExercise = () => {
    const id = location.hash.slice(1);
    if (!/^power-grammar-(?:set-)?\d+$/.test(id)) return;
    const target = document.getElementById(id);
    if (!target) return;
    let parent = target.closest('details.pg-set');
    if (parent) parent.open = true;
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  };
  openLinkedExercise();
  window.addEventListener('hashchange', openLinkedExercise);
})();
