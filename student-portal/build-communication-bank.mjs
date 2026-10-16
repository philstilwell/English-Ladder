import { readFile, writeFile } from 'node:fs/promises';
const specifications = [
 ['conversation-rescue','Conversation Rescue','Choose a helpful response when a conversation is difficult.'],
 ['meaning-switch','Meaning Switch','Compare sentences and notice how their meanings change.'],
 ['ask-right-question','Ask the right question','Choose a clear question that asks for the information you need.'],
 ['story-builder','Story builder','Put four sentences in a clear order by choosing the right sequence.'],
 ['missing-details','Missing Details','Choose what to ask when useful information is missing.'],
];
const stages=['Start','Start','Build','Build','Stretch','Stretch'];
// Stable shuffling keeps released keys reproducible without an obvious four-item cycle.
function seededRandom(text) {
 let seed=2166136261;
 for(const char of text)seed=Math.imul(seed^char.charCodeAt(0),16777619)>>>0;
 return ()=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)/4294967296;};
}
function shuffled(values,random){
 const copy=[...values];
 for(let i=copy.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[copy[i],copy[j]]=[copy[j],copy[i]];}
 return copy;
}
const activities=[];
for(const [id,name,description] of specifications){
 const lines=(await readFile(new URL('./content/'+id+'.txt',import.meta.url),'utf8')).trim().split('\n');
 const groups=[...new Set(lines.map(line=>line.split('|')[0]))];
 const random=seededRandom(id+':v1'),answerPositions=shuffled(Array.from({length:60},(_,i)=>i%4),random);
 const items=lines.map((line,index)=>{
  const cells=line.split('|'),number=index+1,group=cells[0];
  let context,prompt,options,explanation,reply,title;
  if(id==='story-builder'){
   if(cells.length!==4)throw Error(id+' row '+number+' has incorrect columns');
   title=cells[1];const sequence=cells[2].split('~');
   if(sequence.length!==4)throw Error('Story needs four sentences');
   let order;do{order=shuffled([0,1,2,3],random);}while(order.every((value,i)=>value===i));
   const letter=event=>String.fromCharCode(65+order.indexOf(event));
   context=order.map((event,i)=>String.fromCharCode(65+i)+'. '+sequence[event]).join('\n');
   prompt='Which order tells the story clearly from start to finish?';
   options=[[0,1,2,3],[1,0,2,3],[0,2,1,3],[0,1,3,2]].map(events=>events.map(letter).join(' → '));
   explanation=cells[3];
  }else{
   if(cells.length!==(id==='missing-details'?9:8))throw Error(id+' row '+number+' has incorrect columns');
   [,context,prompt,...options]=cells;explanation=options[4];reply=options[5];options=options.slice(0,4);
  }
  const answer=answerPositions[index],rotated=Array.from({length:4},(_,i)=>options[(i-answer+4)%4]);
  return {number,group,stage:stages[groups.indexOf(group)],...(title?{title}:{}),context,prompt,options:rotated,answer,explanation,...(reply?{reply}: {})};
 });
 if(items.length!==60||groups.length!==6||groups.some(group=>items.filter(i=>i.group===group).length!==10))throw Error(id+' needs six sets of ten');
 for(const item of items){
  if(new Set(item.options).size!==4||!item.context||!item.prompt||!item.explanation||!item.stage)throw Error(id+' invalid item '+item.number);
 }
 activities.push({id,name,description,version:1,groups,items});
}
await writeFile(new URL('./communication-bank.json',import.meta.url),JSON.stringify({version:1,activities},null,2)+'\n');
console.log('Built '+activities.length+' activities, '+activities.reduce((n,a)=>n+a.items.length,0)+' original items.');
