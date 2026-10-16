(() => {
  'use strict';
  const ids = ['conversation-rescue','meaning-switch','ask-right-question','story-builder','missing-details'];
  const el = (tag, text = '', cls = '') => { const node=document.createElement(tag); node.textContent=text; node.className=cls; return node; };
  const validItems = items => Array.isArray(items) && items.length>0 && items.length<=5000 && items.every((item,index)=>
    Number.isInteger(item.number)&&item.number>0&&(!index||item.number>items[index-1].number)&&['context','prompt','group','stage','explanation'].every(key=>typeof item[key]==='string'&&item[key].trim())&&
    Array.isArray(item.options)&&item.options.length===4&&item.options.every(option=>typeof option==='string'&&option.trim())&&new Set(item.options).size===4&&Number.isInteger(item.answer)&&item.answer>=0&&item.answer<4);
  function exercise(item) {
    const card=el('article','','communication-item');card.tabIndex=-1;
    card.append(el('h3','Item '+item.number+(item.title?' · '+item.title:''),'communication-heading'),el('p',item.stage+' · '+item.group,'field-hint'),el('p',item.context,'communication-context'),el('p',item.prompt,'communication-task'));
    const choices=el('div','','communication-choices');choices.setAttribute('role','group');choices.setAttribute('aria-label','Answer choices for item '+item.number);
    const buttons=item.options.map((option,index)=>{const button=el('button',option,'communication-option');button.type='button';button.setAttribute('aria-pressed','false');choices.append(button);return button;});
    const feedback=el('div','','communication-feedback');feedback.setAttribute('role','status');feedback.hidden=true;
    const reveal=el('label','','grammar-reveal'),checkbox=el('input');checkbox.type='checkbox';checkbox.autocomplete='off';checkbox.setAttribute('aria-label','Show answer for item '+item.number);
    const answer=el('div','','communication-answer');answer.hidden=true;
    answer.append(el('p','Answer: '+item.options[item.answer],'communication-key'),el('p',item.explanation));
    if(item.reply)answer.append(el('p','The reply: “'+item.reply+'”'));
    if(item.title)answer.append(el('p','Try saying the story in your own words.','field-hint'));
    checkbox.addEventListener('change',()=>{answer.hidden=!checkbox.checked;});reveal.append(checkbox,el('span','Show answer'));
    const actions=el('div','','grammar-actions');
    const copy=window.PracticePrompt.create({label:' for item '+item.number,prompt:window.PracticePrompt.text(
      'English practice:\n'+item.context+'\n\n'+item.prompt+'\nChoices:\n'+item.options.map((option,i)=>'Choice '+(i+1)+': '+option).join('\n')+'\nAnswer key: '+item.options[item.answer]+'\nExplanation: '+item.explanation+(item.reply?'\nReply after clarification: '+item.reply:''),
      'Explain why the answer fits this situation. Explain why each other choice does not fit, or what different question it would answer. Treat this as practice, not an assessment of a person.')});
    actions.append(copy.controls);card.append(choices,feedback,reveal,answer,actions,copy.status);
    function showChoice(choice) {
      buttons.forEach((button,index)=>button.setAttribute('aria-pressed',String(index===choice)));
      feedback.replaceChildren();feedback.hidden=!Number.isInteger(choice);
      if(!feedback.hidden){feedback.append(el('strong',choice===item.answer?'Correct.':'Not quite. You can try again.'),el('p',item.explanation));if(item.reply)feedback.append(el('p','The reply: “'+item.reply+'”'));}
    }
    return {card,actions,buttons,showChoice};
  }
  function review(item, teacherView=true){
    const view=exercise(item);view.buttons.forEach((button,index)=>{button.disabled=!teacherView;if(teacherView)button.addEventListener('click',()=>view.showChoice(index));});
    view.card.classList.toggle('is-finished',Boolean(item.progress?.finished));
    const saved=el('div','','communication-saved');
    if(Number.isInteger(item.progress?.firstChoice))saved.append(el('p','First saved choice: “'+item.options[item.progress.firstChoice]+'” · '+(item.progress.firstCorrect?'Correct':'Needs practice')));
    if(Number.isInteger(item.progress?.choice))saved.append(el('p','Latest saved choice: “'+item.options[item.progress.choice]+'”'));
    if(teacherView)saved.append(el('p','Teacher view: trying the choices here does not change the student’s saved work.','field-hint'));view.card.prepend(saved);
    return view.card;
  }
  window.CommunicationPractice={ids,validItems,review,create({root,api,expired}){
    let generation=0,active=null,teacher=false,bank=null,progress=new Map(),number=null,hideFinished=false,preferencesRevision=0,busy=false,listOpen=false,preview=new Map(),bookmark=null;
    const path=()=>'/api/communication/'+active+'/state';
    async function request(path,options={}){
      const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),10000);
      try{return await api(path,{...options,signal:controller.signal});}finally{clearTimeout(timer);}
    }
    let pending = Promise.resolve(), questionsView = false;
    function clear(){generation++;pending=Promise.allSettled([pending,bookmark?.settled()]).then(()=>undefined);bookmark?.clear();active=null;bank=null;progress.clear();preview.clear();number=null;busy=false;listOpen=false;hideFinished=false;preferencesRevision=0;root.replaceChildren();root.hidden=true;root.removeAttribute('aria-busy');}
    function readState(data){
      if(!Array.isArray(data.entries)||data.entries.some(entry=>!bank.items.some(item=>item.number===entry.number)||typeof entry.finished!=='boolean'||typeof entry.question!=='boolean'||!Number.isSafeInteger(entry.revision)||entry.revision<0||entry.choice!==undefined&&(!Number.isInteger(entry.choice)||entry.choice<0||entry.choice>3)))throw Error('Invalid saved choices');
      const pref=data.preferences||{hideFinished:false,revision:0};if(typeof pref.hideFinished!=='boolean'||!Number.isSafeInteger(pref.revision)||pref.revision<0)throw Error('Invalid preference');
      progress=new Map(data.entries.map(entry=>[entry.number,entry]));hideFinished=pref.hideFinished;preferencesRevision=pref.revision;
    }
    const visible=()=>hideFinished?bank.items.filter(item=>!progress.get(item.number)?.finished):bank.items;
    function render(message='',focus=false,remember=false){
      const items=visible();if(!items.some(item=>item.number===number))number=items.find(item=>item.number>=number)?.number||items.at(-1)?.number||number;
      const intro=el('p',bank.items.length+' items in six topic sets. Later sets are more demanding. Choose an answer to see an explanation.','field-hint');
      const help=el('p',teacher?'Teacher view: your answers and navigation here do not change saved work.':'Your first and latest choices are saved. Finish and Questions are separate choices; click again to undo them.','field-hint');
      const status=el('p',message,'communication-save-status');status.setAttribute('role','status');
      const filter=el('label','','practice-filter'),check=el('input');check.type='checkbox';check.checked=hideFinished;check.disabled=busy;check.autocomplete='off';check.addEventListener('change',()=>save('hideFinished',check.checked));filter.append(check,el('span','Hide finished items'));
      const questions=el('details','','grammar-questions');questions.open=listOpen;questions.addEventListener('toggle',()=>{listOpen=questions.open;});
      const flagged=bank.items.filter(item=>progress.get(item.number)?.question);questions.append(el('summary','Questions list ('+flagged.length+')'));
      const links=el('ul','','grammar-question-links');
      for(const item of flagged){const li=el('li'),button=el('button','Item '+item.number+' · '+(item.title||item.context.slice(0,90))+(progress.get(item.number)?.finished?' · Finished':''),'secondary-button');button.type='button';button.disabled=busy;button.addEventListener('click',()=>{const hidden=hideFinished&&progress.get(item.number)?.finished;if(hidden)hideFinished=false;number=item.number;listOpen=false;render(hidden?'Showing all items so you can view this question.':'',true,true);});li.append(button);links.append(li);}
      questions.append(flagged.length?links:el('p','No questions yet. Choose “Questions” on an item to add it here.','field-hint'));
      root.replaceChildren(intro,help,filter,status,bookmark.notice,questions);
      if(!items.length){root.append(el('p','All items are finished. Uncheck “Hide finished items” to see them again.','practice-empty'));return;}
      const item=items.find(item=>item.number===number),entry=progress.get(number),picker=el('div','','grammar-picker');
      const groupLabel=el('label','Topic set'),groups=el('select');groups.id='communication-group';groupLabel.htmlFor=groups.id;groups.disabled=busy;
      for(const group of bank.groups){const inGroup=items.filter(item=>item.group===group);if(!inGroup.length)continue;const option=el('option',group);option.value=group;groups.append(option);}groups.value=item.group;
      groups.addEventListener('change',()=>{number=items.find(item=>item.group===groups.value).number;render('',true,true);});
      const itemLabel=el('label','Item'),select=el('select');select.id='communication-item-picker';itemLabel.htmlFor=select.id;select.disabled=busy;
      for(const candidate of items.filter(other=>other.group===item.group)){const option=el('option',String(candidate.number));option.value=candidate.number;select.append(option);}select.value=number;select.addEventListener('change',()=>{number=Number(select.value);render('',true,true);});picker.append(groupLabel,groups,itemLabel,select);
      const view=exercise(item);view.card.classList.toggle('is-finished',Boolean(entry?.finished));
      const choice=teacher&&preview.has(number)?preview.get(number):entry?.choice;view.showChoice(choice);
      if(teacher&&Number.isInteger(entry?.firstChoice))view.card.prepend(el('p','First saved choice: “'+item.options[entry.firstChoice]+'” · '+(entry.firstCorrect?'Correct':'Needs practice'),'communication-saved'));
      view.buttons.forEach((button,index)=>{button.disabled=busy;button.addEventListener('click',()=>{if(teacher){preview.set(item.number,index);view.showChoice(index);}else save('answer',index);});});
      const finish=el('button',entry?.finished?'Finished':'Finish','secondary-button'),question=el('button',entry?.question?'Saved to Questions':'Questions','secondary-button question-button');finish.type=question.type='button';
      for(const [button,field] of [[finish,'finished'],[question,'question']]){button.disabled=teacher||busy;button.setAttribute('aria-pressed',String(Boolean(entry?.[field])));button.addEventListener('click',()=>save(field,!progress.get(item.number)?.[field]));}
      view.actions.prepend(finish,question);
      const controls=el('div','','grammar-controls'),previous=el('button','Previous item','secondary-button'),next=el('button','Next item','secondary-button');previous.type=next.type='button';const index=items.indexOf(item);
      previous.disabled=busy||index===0;next.disabled=busy||index===items.length-1;
      previous.addEventListener('click',()=>{number=items[index-1].number;render('',true,true);});next.addEventListener('click',()=>{number=items[index+1].number;render('',true,true);});controls.append(previous,next);root.append(picker,view.card,controls);
      if(remember)bookmark.remember(number);if(focus){view.card.focus();view.card.scrollIntoView?.({block:'start'});}
    }
    async function save(field,value){
      if(busy)return;
      if(teacher){if(field==='hideFinished'){hideFinished=value;render();}return;}
      const current=generation,entry=progress.get(number),itemNumber=number;
      const body=field==='hideFinished'?{field,value,revision:preferencesRevision}:{number,field,value,revision:entry?.revision||0,...(field==='answer'?{version:bank.version}:{})};
      busy=true;const controls=[...root.querySelectorAll('button,input,select')].map(node=>[node,node.disabled]);for(const[node]of controls)node.disabled=true;
      root.querySelector('.communication-save-status').textContent='Saving…';
      let refresh=false,message='';
      try{
        const saving=request(path(),{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});pending=Promise.allSettled([pending,saving]).then(()=>undefined);const data=await saving;
        if(current!==generation)return;
        if(field==='hideFinished'){if(typeof data.preferences?.hideFinished!=='boolean'||!Number.isSafeInteger(data.preferences.revision))throw Error('Missing preference');hideFinished=data.preferences.hideFinished;preferencesRevision=data.preferences.revision;}
        else{if(data.entry?.number!==itemNumber||!Number.isSafeInteger(data.entry.revision))throw Error('Missing choice');progress.set(itemNumber,data.entry);}
        message=field==='answer'?'Your answer is saved.':'Your choice is saved.';refresh=true;
      }catch(error){
        if(current!==generation||expired(error))return;
        if(error.status===409){try{const data=await request(path());if(current!==generation)return;readState(data);refresh=true;message='Your saved choices changed on another page. Check them and try again.';}catch(reloadError){if(current!==generation||expired(reloadError))return;message='Your saved choices could not reload. Leave this activity and open it again.';}}
        else message='Your change could not be saved. Please try again.';
      }finally{if(current===generation){busy=false;if(refresh)render(message,false,field==='finished'&&hideFinished);else{for(const[node,disabled]of controls)node.disabled=disabled;root.querySelector('.practice-filter input').checked=hideFinished;root.querySelector('.communication-save-status').textContent=message;}}}
    }
    async function open(id,teacherView=false,showQuestions=false){
      if(active===id){if(questionsView!==showQuestions){questionsView=showQuestions;listOpen=showQuestions;if(bank)render();}return;}clear();questionsView=showQuestions;listOpen=showQuestions;if(!ids.includes(id))return;active=id;teacher=teacherView;const current=generation;
      bookmark=window.PracticePosition.create({api,expired,path:path()});root.hidden=false;root.setAttribute('aria-busy','true');root.append(el('p','Loading practice…'));
      try{
        await pending;if(current!==generation)return;
        const[data,state]=await Promise.all([request('/api/communication/'+id),request(path())]);if(current!==generation)return;
        if(data.id!==id||data.version!==1||!validItems(data.items)||!Array.isArray(data.groups)||data.items.some(item=>!data.groups.includes(item.group)))throw Error('Invalid activity');
        bank=data;readState(state);number=bookmark.read(state.position,!teacher)||bank.items[0].number;root.removeAttribute('aria-busy');render();
      }catch(error){if(current!==generation||expired(error))return;root.removeAttribute('aria-busy');const retry=el('button','Try again','secondary-button');retry.type='button';retry.addEventListener('click',()=>{active=null;open(id,teacherView,showQuestions);});root.replaceChildren(el('p','This activity could not load. Please try again.'),retry);}
    }
    return {open,clear};
  }};
})();
