import worker from '../worker.mjs';
import { FeedbackStore } from '../feedback.mjs';
import { feedback, assessment, quiz } from './fixture.mjs';
export const origin = 'https://ab26.englishladder.com';
export function env() {
 const objects = new Map();
 return {
  STUDENT_ACCOUNTS:JSON.stringify({ab26:{name:'Alex Brown',nickname:'Alex the Explorer',password:'student-test'},cd26:{name:'Casey Drew',password:'other-test'}}),
  TEACHER_PASSWORD:'teacher-test',SESSION_SECRET:'test-session-key-'.repeat(4),
  LOGIN_LIMITER:{limit:async()=>({success:true})},ACCOUNT_LIMITER:{limit:async()=>({success:true})},
  ASSETS:{fetch:async()=>new Response('public shell')},
  FEEDBACK_STORE:{
   idFromName:id=>id,
   get(id){
    if(!objects.has(id)){
     const values = new Map();
     let queue = Promise.resolve();
     const storage = {
      async transaction(fn){
       const run=queue.then(async()=>{
        const snapshot=new Map([...values].map(([k,v])=>[k,structuredClone(v)]));
        try{return await fn(storage);}catch(error){values.clear();for(const [k,v] of snapshot)values.set(k,v);throw error;}
       });
       queue=run.catch(()=>{});return run;
      },
      async get(key){return structuredClone(values.get(key));},
      async put(data){for(const [key,value] of Object.entries(data)) values.set(key,structuredClone(value));},
      async delete(key){return values.delete(key);},
      async list({prefix='',reverse,limit,end}={}){
       let keys=[...values.keys()].filter(k=>k.startsWith(prefix)&&(!end||k<end)).sort();
       if(reverse)keys.reverse();
       return new Map(keys.slice(0,limit).map(k=>[k,structuredClone(values.get(k))]));
      }
     };
     objects.set(id,new FeedbackStore({storage}));
    }
    return objects.get(id);
   }
  }
 };
}
export function call(e,path,options={},host=origin){return worker.fetch(new Request(host+path,options),e);}
export async function login(e,password='student-test',host=origin) {
 const r=await call(e,'/api/login',{method:'POST',headers:{Origin:host,'Content-Type':'application/json'},body:JSON.stringify({password})},host);
 return {response:r,cookie:r.headers.get('set-cookie').split(';')[0]};
}
export async function seedQuiz() {
 const e=env(),student=await login(e),teacher=await login(e,'teacher-test');
 const publish=(path,body)=>call(e,path,{method:'PUT',headers:{Cookie:teacher.cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)});
 await publish('/api/feedback/'+feedback.id,feedback);
 await publish('/api/assessment',{...assessment,quiz});
 const state=await (await call(e,'/api/quiz/state',{headers:{Cookie:student.cookie}})).json();
 return {e,student,teacher,state,publish};
}
