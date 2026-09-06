/* Small, optional enhancements. Lessons remain readable without browser storage. */
(() => {
  'use strict';
  const root = new URL('.', document.querySelector('script[src*="site.js"]')?.src || location.href);
  const levels = ['beginner', 'intermediate', 'advanced'];
  const LEVEL_KEY = 'english-ladder-level';
  const STORE_KEY = 'english-ladder-study-v1';
  const read = key => { try { return localStorage.getItem(key); } catch (_) { return null; } };
  const write = (key, value) => { try { localStorage.setItem(key, value); return true; } catch (_) { return false; } };
  const currentLevel = location.pathname.match(/\/(beginner|intermediate|advanced)\.html$/)?.[1];
  let level = currentLevel || read(LEVEL_KEY) || 'beginner';
  if (!levels.includes(level)) level = 'beginner';
  function applyLevel(value) {
    level = value;
    document.querySelectorAll('[data-level-link], .explore-story').forEach(a => {
      const url = new URL(a.href, location.href);
      url.pathname = url.pathname.replace(/\/(beginner|intermediate|advanced)\.html$/, `/${level}.html`);
      a.href = url.href;
    });
    const input = document.querySelector(`input[name="feature-level"][value="${level}"]`);
    if (input) {
      input.checked = true;
      const start = document.querySelector('#feature-start');
      if (start && /^(?:stories\/[a-z-]+\/)?(?:beginner|intermediate|advanced)\.html(?:#lesson-\d{4}-\d{2}-\d{2})?$/.test(input.dataset.lessonHref || "")) start.href = input.dataset.lessonHref;
    }
  }
  applyLevel(level);
  if (currentLevel) write(LEVEL_KEY, currentLevel);
  document.querySelectorAll('input[name="feature-level"]').forEach(input => input.addEventListener('change', () => {
    if (levels.includes(input.value)) { write(LEVEL_KEY, input.value); applyLevel(input.value); }
  }));
  function preserveDate() {
    document.querySelectorAll('[data-level-choice]').forEach(a => {
      const url = new URL(a.href, location.href);
      if (/^#lesson-\d{4}-\d{2}-\d{2}$/.test(location.hash)) url.hash = location.hash;
      a.href = url.href;
    });
  }
  document.querySelectorAll('[data-level-choice]').forEach(a => a.addEventListener('click', () => {
    if (levels.includes(a.dataset.levelChoice)) write(LEVEL_KEY, a.dataset.levelChoice);
  }));
  preserveDate(); window.addEventListener('hashchange', preserveDate);
  document.querySelectorAll('.daily-lesson').forEach(lesson => lesson.addEventListener('toggle', () => {
    if (window.history && lesson.open && /^lesson-\d{4}-\d{2}-\d{2}$/.test(lesson.id)) {
      window.history.replaceState(null, '', '#'+lesson.id); preserveDate();
    }
  }));

  document.querySelectorAll('[data-library]').forEach(library => {
    const search = library.querySelector('[data-library-search]');
    const category = library.querySelector('[data-library-category]');
    const levelFilter = library.querySelector('[data-library-level]');
    const cards = [...library.querySelectorAll('[data-library-item]')];
    const filter = () => {
      const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
      let count=0;
      cards.forEach(card => {
        const match = terms.every(t => card.dataset.search.toLocaleLowerCase().includes(t)) && (!category?.value || card.dataset.category===category.value) && (!levelFilter?.value || card.dataset.level?.includes(levelFilter.value));
        card.hidden=!match; if(match) count++;
      });
      library.querySelector('[data-library-count]').textContent=`${count} of ${cards.length} available`;
      library.querySelector('[data-library-empty]').hidden=count!==0;
    };
    search.addEventListener('input',filter);category?.addEventListener('change',filter);levelFilter?.addEventListener('change',filter);filter();
  });

  const fresh=()=>({enabled:false,history:[],words:[],drafts:{}});
  let saved=fresh();
  try {
    const data=JSON.parse(read(STORE_KEY));
    if(data && data.enabled===true && Array.isArray(data.history) && Array.isArray(data.words) && data.drafts && typeof data.drafts==='object' && !Array.isArray(data.drafts)) saved={...data,history:data.history.filter(item=>item && typeof item.url==='string' && typeof item.title==='string').slice(0,20),words:data.words.filter(item=>item && typeof item.term==='string' && typeof item.definition==='string').slice(0,100)};
  } catch (_) { /* Corrupt or unavailable storage does not block study. */ }
  const status=message=>document.querySelectorAll('[data-save-status]').forEach(p=>{p.textContent=message;});
  const persist=()=>{
    if (!saved.enabled) return false;
    const ok=write(STORE_KEY,JSON.stringify(saved));
    if(!ok) status('This browser could not save your work. Copy or export anything you want to keep.');
    return ok;
  };
  const safeLocal = href => {
    try { const u=new URL(href, root); return u.origin===root.origin && u.pathname.startsWith(root.pathname) && /\.html$/.test(u.pathname) ? u : null; } catch (_) { return null; }
  };
  const lessonInfo=lesson=>{
    let url=new URL(location.href);
    const date=lesson?.dataset.lessonKey;
    if(date && /^\d{4}-\d{2}-\d{2}$/.test(date))url=new URL(`news/${date}/${currentLevel||level}.html`,root);
    const title=lesson?.querySelector('.lesson-title-text')?.textContent || document.querySelector('h1')?.textContent || document.title;
    return {url:url.pathname+url.hash,title:title.trim(),date:new Date().toISOString(),complete:false};
  };
  function remember(lesson,complete=false) {
    if(!saved.enabled)return;
    const item=lessonInfo(lesson);const previous=saved.history.find(h=>h.url===item.url);
    item.complete=complete||previous?.complete||false;
    saved.history=[item,...saved.history.filter(h=>h.url!==item.url)].slice(0,20);persist();
  }
  const draftKey=input=>{
    const lesson=input.closest('.daily-lesson');
    const path=lesson ? new URL(lessonInfo(lesson).url,root).pathname : location.pathname;
    return path+':'+input.dataset.studyDraft;
  };
  document.querySelectorAll('[data-study-draft]').forEach(input=>{
    const value=saved.drafts[draftKey(input)] ?? saved.drafts[location.pathname+':'+input.dataset.studyDraft];if(saved.enabled && typeof value==='string')input.value=value.slice(0,8000);
    input.addEventListener('input',()=>{
      if(!saved.enabled)return;
      delete saved.drafts[draftKey(input)];saved.drafts[draftKey(input)]=input.value.slice(0,8000);
      const keys=Object.keys(saved.drafts);keys.slice(0,Math.max(0,keys.length-80)).forEach(key=>delete saved.drafts[key]);persist();
    });
  });
  document.querySelectorAll('[data-save-study]').forEach(input=>{
    input.checked=saved.enabled;
    input.addEventListener('change',()=>{
      saved.enabled=input.checked;
      document.querySelectorAll('[data-save-study]').forEach(other=>{other.checked=saved.enabled;});
      if(saved.enabled){
        document.querySelectorAll('[data-study-draft]').forEach(draft=>{saved.drafts[draftKey(draft)]=draft.value;});
        if(document.querySelector('.daily-lesson,.curriculum-page') || document.body.classList.contains('curriculum-page'))remember(document.querySelector('.daily-lesson[open]')||document.querySelector('.daily-lesson'));
        if(persist())status('Saving is on in this browser only.');
      } else {
        try{localStorage.removeItem(STORE_KEY);saved=fresh();status('Saving is off. The saved copy was removed; text on this page remains.');}catch(_){status('Saving is off, but the saved copy could not be removed. Use browser site-data settings.');}
      }
      renderDashboard();
    });
  });
  if(saved.enabled && (document.querySelector('.daily-lesson') || document.body.classList.contains('curriculum-page')))remember(document.querySelector('.daily-lesson[open]')||document.querySelector('.daily-lesson'));
  document.querySelectorAll('.daily-lesson').forEach(lesson=>lesson.addEventListener('toggle',()=>{if(window.document && lesson.open)remember(lesson);}));
  window.addEventListener('lesson-practiced',event=>remember(event.detail?.lesson,true));
  document.querySelector('[data-complete-study]')?.addEventListener('click',event=>{
    remember(null,true);event.target.textContent='Practiced ✓';
    document.querySelector('[data-study-status]').textContent=saved.enabled?'Marked practiced in this browser. Try using the pattern again tomorrow.':'Practiced on this page. Turn on browser saving to keep this record.';
  });
  document.querySelectorAll('.vocab-term').forEach(term=>{
    const text=term.textContent.replace(/^\s*\d+\.\s*/, '').replace(/\s*\(.*\):?\s*$/, '').trim();
    const container=term.parentElement;
    let definition=''; let next=term.nextSibling;
    while(next && next.nodeName!=='BR' && !(next.nodeType===1 && next.classList.contains('vocab-term'))){definition+=next.textContent;next=next.nextSibling;}
    definition=definition.trim();
    const button=document.createElement('button');button.type='button';button.className='save-word';button.textContent='Save word';button.setAttribute('aria-label',`Save ${text} for review`);
    button.addEventListener('click',()=>{
      if(!saved.enabled){status('Turn on browser saving to keep words for review.');document.querySelector('[data-study-controls]')?.setAttribute('open','');document.querySelector('[data-save-study]')?.focus();return;}
      saved.words=[{term:text,definition,url:location.pathname},...saved.words.filter(w=>w.term!==text)].slice(0,100);
      if(persist()){button.textContent='Saved ✓';button.disabled=true;}
    });term.after(button);
  });
  function renderDashboard(){
    const historyList=document.querySelector('[data-learning-history]');const wordsList=document.querySelector('[data-learning-words]');if(!historyList||!wordsList)return;
    historyList.replaceChildren();wordsList.replaceChildren();
    saved.history.forEach(item=>{const url=safeLocal(item.url);if(!url||typeof item.title!=='string')return;const p=document.createElement('p');const a=document.createElement('a');a.href=url.href;a.textContent=item.title;p.append(a,document.createTextNode(item.complete?' · practiced':' · continue'));historyList.append(p);});
    if(!historyList.children.length){const p=document.createElement('p');p.textContent='No saved lessons yet. Turn on saving, then open a lesson.';historyList.append(p);}
    saved.words.forEach(word=>{if(typeof word.term!=='string'||typeof word.definition!=='string')return;const details=document.createElement('details');const summary=document.createElement('summary');summary.textContent=word.term;const p=document.createElement('p');p.textContent=word.definition;const remove=document.createElement('button');remove.type='button';remove.className='secondary-button';remove.textContent='Remove word';remove.addEventListener('click',()=>{saved.words=saved.words.filter(w=>w.term!==word.term);persist();renderDashboard();});details.append(summary,p,remove);wordsList.append(details);});
    if(!wordsList.children.length){const p=document.createElement('p');p.textContent='No saved words yet. Save a word beside a lesson’s vocabulary.';wordsList.append(p);}
  }
  renderDashboard();
  document.querySelector('[data-export-study]')?.addEventListener('click',()=>{
    const url=URL.createObjectURL(new Blob([JSON.stringify(saved,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='english-ladder-learning.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  document.querySelector('[data-clear-study]')?.addEventListener('click',event=>{
    const previous=JSON.stringify(saved);
    try{localStorage.removeItem(STORE_KEY);saved=fresh();document.querySelectorAll('[data-save-study]').forEach(i=>{i.checked=false;});renderDashboard();status('Saved learning cleared. You can undo this while the page stays open.');}
    catch(_){status('Could not clear browser storage. Use browser site-data settings.');return;}
    document.querySelector('[data-undo-study]')?.remove();const undo=document.createElement('button');undo.type='button';undo.dataset.undoStudy='';undo.className='secondary-button';undo.textContent='Undo clear';
    undo.addEventListener('click',()=>{saved=JSON.parse(previous);if(saved.enabled)persist();document.querySelectorAll('[data-save-study]').forEach(i=>{i.checked=saved.enabled;});renderDashboard();undo.remove();});event.target.after(undo);
  });
})();
