import bank from './communication-bank.json' with { type: 'json' };
import { createSelfCheckHandler } from './self-check.mjs';
export const COMMUNICATION_ACTIVITIES = bank.activities;
export const communicationPrefix = activity => 'communication:' + activity.id + ':v' + activity.version;
const handlers = new Map(COMMUNICATION_ACTIVITIES.map(activity => [activity.id, createHandler(activity)]));
function createHandler(activity) {
  const prefix=communicationPrefix(activity), items=new Map(activity.items.map(item=>[item.number,item]));
  const selfCheck=createSelfCheckHandler(prefix,activity);
  return async(storage,request)=>{
    const url=new URL(request.url),state=url.pathname.endsWith('/state');
    if(request.method==='GET'||!state)return selfCheck(storage,new Request('https://feedback.internal/'+prefix+(state?'/state':'/questions'),request));
    let input;try{input=await request.json();}catch{return Response.json({error:'Please check your choice.'},{status:400});}
    if(input?.field!=='answer')return selfCheck(storage,new Request('https://feedback.internal/'+prefix+'/state',{method:request.method,body:JSON.stringify(input)}));
    if(request.method!=='PATCH'||!items.has(input.number)||!Number.isInteger(input.value)||input.value<0||input.value>3||input.version!==activity.version||
      !Number.isSafeInteger(input.revision)||input.revision<0||Object.keys(input).some(key=>!['number','field','value','revision','version'].includes(key)))return Response.json({error:'Please check your answer.'},{status:400});
    return storage.transaction(async txn=>{
      if(await txn.get('account:deleted'))return Response.json({error:'This account was deleted.'},{status:410});
      const key=prefix+':item:'+input.number,entry=await txn.get(key)||{number:input.number,finished:false,question:false,revision:0,updatedAt:null};
      if(entry.choice===input.value)return Response.json({entry});
      if(entry.revision!==input.revision)return Response.json({error:'This item changed on another page. Your saved choices have been reloaded. Please try again.'},{status:409});
      const first=entry.firstChoice===undefined?{firstChoice:input.value,firstCorrect:input.value===items.get(input.number).answer}:{};
      const updated={...entry,...first,choice:input.value,correct:input.value===items.get(input.number).answer,revision:entry.revision+1,updatedAt:new Date().toISOString()};
      await txn.put({[key]:updated});return Response.json({entry:updated});
    });
  };
}
export function handleCommunication(storage,request){
 const [, ,id,kind]=new URL(request.url).pathname.split('/');
 if(!handlers.has(id)||!['state','questions'].includes(kind))return Response.json({error:'Page not found.'},{status:404});
 return handlers.get(id)(storage,request);
}
