import test from 'node:test';
import assert from 'node:assert/strict';
import { modelJson, MODEL } from '../server-ai-json.mjs';

test('GPT-OSS uses the Responses contract and reads only completed assistant JSON', async () => {
  const result = await modelJson({ run: async (model, input) => {
    assert.equal(model, MODEL); assert.equal(input.messages, undefined); assert.equal(input.max_tokens, undefined);
    assert.equal(input.max_output_tokens, 4000); assert.equal(input.store, false);
    assert.equal(input.input[0].content, 'Return JSON.'); assert.equal(input.input[1].content, '{"example":true}');
    assert.deepEqual(input.text, { format: { type: 'json_object' } });
    return { status: 'completed', output: [
      { type: 'reasoning', content: [{ type: 'reasoning_text', text: '{"approved":false}' }] },
      { type: 'message', role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: '{"approved":true}' }] },
    ] };
  } }, 'Return JSON.', { example: true }, 4000);
  assert.deepEqual(result, { approved: true });
});

test('partial, refused, malformed and non-object model replies fail closed', async () => {
  const message = { type: 'message', role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: '{"approved":true}' }] };
  for (const reply of [
    { status: 'incomplete', output: [message] }, { status: 'failed', output: [message] },
    { output: [{ ...message, status: 'incomplete' }] }, { output: [message, message] },
    { output: [{ ...message, content: [{ type: 'refusal', refusal: 'No.' }] }] },
    { output: [{ ...message, content: [{ type: 'output_text', text: 'not JSON' }] }] },
    { output: [] }, { response: [] }, { response: 'null' }, { error: 'failed', response: { approved: true } },
  ]) await assert.rejects(modelJson({ run: async () => reply }, '', {}, 4000), /invalid_model_response/);
});


test('model diagnostics distinguish truncation without exposing content and accept only an entire JSON fence',async()=>{
  const ai={run:async()=>({status:'incomplete',incomplete_details:{reason:'max_output_tokens'},output:[]})};
  await assert.rejects(modelJson(ai,'',{},10),error=>error.message==='invalid_model_response'&&error.modelIssue==='output_limit');
  assert.deepEqual(await modelJson({run:async()=>({response:'```json\n{"approved":true}\n```'})},'',{},4000),{approved:true});
  await assert.rejects(modelJson({run:async()=>({response:'Extra text ```json\n{"approved":true}\n```'})},'',{},4000),error=>error.modelIssue==='invalid_json');
});
