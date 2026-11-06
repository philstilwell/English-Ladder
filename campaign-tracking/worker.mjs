import {browserTracker} from './client.mjs';
const SITES = new Set(['englishladder.com','slugfester.com']);
const HEADERS = {'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex, nofollow'};
const UUID = /^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$/i;
export function validTarget(site, path) {
  if (typeof path !== 'string' || path.length > 200 || /[?#%\\\s]/.test(path)) return false;
  if (site === 'englishladder.com') return /^\/(?:grammar-concepts\/concept-\d+\.html|efsp(?:-[a-z0-9-]+)?\.html|us-life\.html|(?:beginner|intermediate|advanced)\.html)$/.test(path);
  return site === 'slugfester.com' && (path === '/' || /^\/debate\/[a-z0-9]+(?:-[a-z0-9]+)*\/$/.test(path));
}
export function bucketFor(request, campaign) {
  const url = new URL(request.url);
  const cookie = request.headers.get('Cookie') || '';
  if (['draft','test'].includes(campaign.status) || url.searchParams.get('traffic') === 'test' || /(?:^|;\s*)campaign_traffic=test(?:;|$)/.test(cookie)) return 'test';
  if (/(?:^|;\s*)campaign_traffic=internal(?:;|$)/.test(cookie)) return 'internal';
  const cf = request.cf || {};
  if (cf.botManagement?.verifiedBot || (typeof cf.botManagement?.score === 'number' && cf.botManagement.score < 30)
      || /bot|crawler|spider|preview|facebookexternalhit|headless|curl|wget|python|monitor|check/i.test(request.headers.get('User-Agent') || '')
      || /prefetch|prerender/i.test(request.headers.get('Sec-Purpose') || request.headers.get('Purpose') || '')) return 'bot';
  return 'audience';
}
function text(body, status=200, extra={}) { return new Response(body,{status,headers:{...HEADERS,'Content-Type':'text/plain; charset=utf-8',...extra}}); }
function safeJson(value) { return JSON.stringify(value).replaceAll('<','\\u003c'); }
function escapeHtml(value) { return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function trafficPage(request) {
  const mode = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)campaign_traffic=(internal|test)(?:;|$)/)?.[1] || 'ordinary';
  return new Response(`<!doctype html><html lang="en"><meta name="viewport" content="width=device-width"><title>Campaign traffic settings</title><style>body{font:18px system-ui;max-width:45rem;margin:3rem auto;padding:1rem;line-height:1.6}button{font:inherit;padding:.7rem;margin:.3rem}a{color:#1757a8}</style><h1>Campaign traffic settings</h1><p>This browser is classified as <strong>${mode}</strong> on ${new URL(request.url).hostname}.</p><p>Internal and test visits are recorded separately and excluded from campaign audience and engagement totals. This setting applies only to this browser on this site. Existing general Cloudflare request totals are unchanged.</p><form method="post"><button name="mode" value="internal">Mark this browser internal</button><button name="mode" value="test">Mark this browser for tests</button><button name="mode" value="ordinary">Clear exclusion</button></form><p><a href="/campaign/privacy">What campaign tracking records</a></p></html>`,{headers:{...HEADERS,'Content-Type':'text/html; charset=utf-8'}});
}
async function event(request, env, host) {
  if (request.method !== 'POST') return text('Method not allowed',405);
  if (request.headers.get('Origin') !== `https://${host}`) return text('Origin not allowed',403);
  if (!request.headers.get('Content-Type')?.startsWith('application/json')) return text('JSON required',415);
  if (Number(request.headers.get('Content-Length') || 0) > 1500) return text('Too large',413);
  const raw = await request.text();
  if (raw.length > 1500) return text('Too large',413);
  let data; try { data=JSON.parse(raw); } catch { return text('Invalid JSON',400); }
  if (!UUID.test(data.visit || '') || !['arrival','engaged'].includes(data.event)) return text('Invalid event',400);
  const row = await env.DB.prepare('SELECT v.*,c.site FROM visits v JOIN campaigns c ON c.id=v.campaign WHERE v.id=?').bind(data.visit).first();
  const age = Date.now()-(row?.created_at || 0);
  if (!row || row.site !== host || age < 0 || age > 7200000) return text('Expired or unknown visit',400);
  // Reclassify detected test automation before any audience counter is advanced.
  if (data.test === true && row.bucket === 'audience' && row.arrived === 0) {
    await env.DB.prepare("UPDATE visits SET bucket='test' WHERE id=? AND arrived=0 AND bucket='audience'").bind(data.visit).run();
  }
  if (!Number.isFinite(data.visibleMs) || data.visibleMs < 1000 || age < 900) return text('Visibility interval not met',400);
  if (data.event === 'engaged' && (!row.arrived || age < 10000 || data.visibleMs < 10000 || data.interacted !== true)) return text('Engagement interval not met',400);
  const field = data.event === 'arrival' ? 'arrived' : 'engaged';
  await env.DB.prepare(`UPDATE visits SET ${field}=1 WHERE id=? AND ${field}=0`).bind(data.visit).run();
  return new Response(null,{status:204,headers:HEADERS});
}
export default {
  async fetch(request,env) {
    const url = new URL(request.url), host=url.hostname;
    if (!SITES.has(host)) return text('Unknown site',404);
    try {
      if (url.pathname === '/campaign/event') return await event(request,env,host);
      if (url.pathname === '/campaign/traffic') {
        if (request.method === 'GET') return trafficPage(request);
        if (request.method !== 'POST' || request.headers.get('Origin') !== url.origin) return text('Origin or method not allowed',403);
        const mode=(await request.formData()).get('mode');
        if (!['internal','test','ordinary'].includes(mode)) return text('Invalid mode',400);
        return new Response(null,{status:303,headers:{...HEADERS,Location:'/campaign/traffic','Set-Cookie':`campaign_traffic=${mode==='ordinary'?'':mode}; Path=/; Max-Age=${mode==='ordinary'?0:31536000}; Secure; HttpOnly; SameSite=Lax`}});
      }
      if (url.pathname === '/campaign/privacy') return text('Campaign links measure which public resource and post brought a visit. An arrival requires the page to remain visible for at least one second. Engagement requires ten visible seconds and a browser-reported interaction. These are indicators of likely readership, not proof of a unique human. Internal, test and recognized bot traffic are separated. Browser Do Not Track and Global Privacy Control preferences disable browser-event collection. We store a random visit reference for at most 30 days and aggregate post totals thereafter. We do not store IP addresses, full user-agent strings, names, practice answers or cross-site visitor identifiers in this database. A first-party exclusion cookie is set only when someone chooses internal or test mode. Cloudflare may separately process connection data to provide hosting.');
      if (!['GET','HEAD'].includes(request.method)) return text('Method not allowed',405);
      const id=url.pathname.match(/^\/campaign\/([a-z0-9][a-z0-9-]{5,99})\/?$/)?.[1];
      if (!id) return text('Unknown campaign',404);
      const campaign=await env.DB.prepare('SELECT * FROM campaigns WHERE id=? AND site=?').bind(id,host).first();
      if (!campaign || !validTarget(host,campaign.target)) return text('Unknown campaign',404);
      const resource=new URL(campaign.target,url.origin);
      if (request.method === 'HEAD') return new Response(null,{status:200,headers:HEADERS});
      // Do not forward a visitor's credentials, cookies, query parameters, or IP.
      const upstream=await fetch(resource,{headers:{'User-Agent':'Campaign resource fetch/1.0','Accept':'text/html'},redirect:'manual'});
      if (!upstream.ok || !upstream.headers.get('Content-Type')?.includes('text/html')) return text(`This resource could not be loaded. Please visit ${resource.href}`,503);
      const visit=crypto.randomUUID();
      const bucket=bucketFor(request,campaign);
      await env.DB.prepare('INSERT INTO visits(id,campaign,bucket,created_at) VALUES(?,?,?,?)').bind(visit,id,bucket,Date.now()).run();
      const config={visit,campaign:id,target:campaign.target,source:campaign.source};
      const injection=`<base href="${escapeHtml(resource.href)}"><script data-campaign-tracker>(${browserTracker.toString()})(${safeJson(config)});</script>`;
      let response=new Response(upstream.body,upstream);
      response.headers.delete('Content-Length'); response.headers.delete('ETag');
      response.headers.delete('Set-Cookie');
      for (const [key,value] of Object.entries(HEADERS)) response.headers.set(key,value);
      response.headers.set('Link',`<${resource.href}>; rel="canonical"`);
      response=new HTMLRewriter().on('head',{element(el){el.prepend(injection,{html:true});}}).transform(response);
      return response;
    } catch (error) { console.error('Campaign tracking unavailable:',error?.message); return text('Campaign tracking is temporarily unavailable. Please open the main site.',503); }
  },
  async scheduled(_event,env) {
    await env.DB.prepare('DELETE FROM visits WHERE created_at < ?').bind(Date.now()-30*86400000).run();
  }
};
