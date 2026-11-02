// No advertising IDs, fingerprinting, IP collection, or cross-site visitor storage.
export function browserTracker(config) {
  'use strict';
  try {
    const target = new URL(config.target, location.origin);
    target.searchParams.set('utm_source', config.source);
    target.searchParams.set('utm_medium', 'social');
    target.searchParams.set('utm_campaign', 'post-outreach');
    target.searchParams.set('utm_content', config.campaign);
    history.replaceState(history.state, '', target.pathname + target.search + location.hash);
  } catch (_) { /* The base element still resolves the resource's relative assets. */ }
  if (navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true) return;
  let attempts = 0;
  let visible = 0, last = performance.now(), interacted = false;
  let arrived = false, engaged = false, sending = false;
  const test = navigator.webdriver === true;
  for (const type of ['pointerdown','keydown','scroll']) {
    addEventListener(type, event => { if (event.isTrusted) interacted = true; }, {passive:true});
  }
  async function send(event) {
    attempts++;
    try {
      const res = await fetch('/campaign/event', {
        method:'POST', credentials:'same-origin', keepalive:true,
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({visit:config.visit, event, test, visibleMs:Math.floor(visible), interacted})
      });
      return res.ok;
    } catch (_) { return false; }
  }
  const timer = setInterval(async () => {
    const now = performance.now();
    if (document.visibilityState === 'visible') visible += Math.min(now-last, 1500);
    last = now;
    if (sending) return;
    sending = true;
    try {
      if (!arrived && visible >= 1000) arrived = await send('arrival');
      if (arrived && !engaged && visible >= 10000 && interacted) engaged = await send('engaged');
      if (engaged || attempts >= 6 || visible > 1800000) clearInterval(timer);
    } finally { sending = false; }
  }, 1000);
}
