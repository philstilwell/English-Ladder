export const MODEL = '@cf/openai/gpt-oss-120b';

// GPT-OSS uses the Responses API through the Workers AI binding. Read only
// the assistant's final text; reasoning, refusals and partial output are not JSON results.
export async function modelJson(ai, instructions, input, maxOutputTokens) {
  const invalid = (modelIssue = 'invalid_message') => { throw Object.assign(new Error('invalid_model_response'), { modelIssue }); };
  let result;
  try { result = await ai.run(MODEL, {
    input: [{ role: 'system', content: instructions }, { role: 'user', content: JSON.stringify(input) }],
    text: { format: { type: 'json_object' } }, max_output_tokens: maxOutputTokens,
    reasoning: { effort: 'low' }, store: false,
  }); } catch (error) {
    // Inspect provider errors transiently; never retain messages or response bodies.
    const message = String(error?.message || '');
    invalid(/\b3036\b|daily free allocation|neuron.{0,40}limit|exceeded.{0,40}neuron/i.test(message) ? 'provider_quota' : /time.?out|timed out/i.test(message) ? 'provider_timeout' : /rate.?limit|too many requests|\b429\b/i.test(message) ? 'provider_rate_limit' : /context.{0,30}(length|limit)|input.{0,30}(too long|too large)/i.test(message) ? 'provider_context_limit' : 'provider_error');
  }
  if (!result || result.error) invalid('provider_error');
  if (result.status && result.status !== 'completed') invalid(result.incomplete_details?.reason === 'max_output_tokens' ? 'output_limit' : 'incomplete');
  let output;
  if (Array.isArray(result.output)) {
    const messages = result.output.filter(item => item.type === 'message' && item.role === 'assistant');
    if (!messages.length) invalid('missing_output');
    if (messages.some(message => Array.isArray(message.content) && message.content.some(part => part.type === 'refusal'))) invalid('refused');
    if (messages.length !== 1 || messages[0].status && messages[0].status !== 'completed' ||
        !Array.isArray(messages[0].content) || messages[0].content.some(part => part.type !== 'output_text' || typeof part.text !== 'string')) invalid();
    output = messages[0].content.map(part => part.text).join('');
  } else output = result.response; // Compatibility with existing binding adapters.
  try {
    if (typeof output === 'string') {
      const fenced = output.match(/^\s*```(?:json)?\s*([\s\S]*?)\s*```\s*$/i);
      output = JSON.parse(fenced ? fenced[1] : output);
    }
  } catch { invalid('invalid_json'); }
  if (!output || typeof output !== 'object' || Array.isArray(output)) invalid('invalid_object');
  return output;
}
