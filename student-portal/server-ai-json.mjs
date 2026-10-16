export const MODEL = '@cf/openai/gpt-oss-120b';

// GPT-OSS uses the Responses API through the Workers AI binding. Read only
// the assistant's final text; reasoning, refusals and partial output are not JSON results.
export async function modelJson(ai, instructions, input, maxOutputTokens) {
  const result = await ai.run(MODEL, {
    input: [{ role: 'system', content: instructions }, { role: 'user', content: JSON.stringify(input) }],
    text: { format: { type: 'json_object' } }, max_output_tokens: maxOutputTokens,
    reasoning: { effort: 'low' }, store: false,
  });
  const invalid = () => { throw new Error('invalid_model_response'); };
  if (!result || result.error || result.status && result.status !== 'completed') invalid();
  let output;
  if (Array.isArray(result.output)) {
    const messages = result.output.filter(item => item.type === 'message' && item.role === 'assistant');
    if (messages.length !== 1 || messages[0].status && messages[0].status !== 'completed' ||
        !Array.isArray(messages[0].content) || messages[0].content.some(part => part.type !== 'output_text' || typeof part.text !== 'string')) invalid();
    output = messages[0].content.map(part => part.text).join('');
  } else output = result.response; // Compatibility with existing binding adapters.
  try { if (typeof output === 'string') output = JSON.parse(output); } catch { invalid(); }
  if (!output || typeof output !== 'object' || Array.isArray(output)) invalid();
  return output;
}
