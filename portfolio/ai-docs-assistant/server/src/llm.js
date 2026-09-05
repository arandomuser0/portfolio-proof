// Embeddings + chat via any OpenAI-compatible API (OpenAI / Ollama / Gemini-compat / Anthropic-compat proxy)
const base = process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1'
const key = process.env.OPENAI_API_KEY || ''
const embedModel = process.env.EMBED_MODEL || 'text-embedding-3-small'
const chatModel = process.env.CHAT_MODEL || 'gpt-4o-mini'
async function j(url, body) {
  const r = await fetch(url, { method: 'POST', headers: { 'content-type': 'application/json', authorization: `Bearer ${key}` }, body: JSON.stringify(body) })
  if (!r.ok) throw new Error(`LLM ${r.status}: ${await r.text()}`)
  return r.json()
}
export const embed = async (text) => (await j(`${base}/embeddings`, { model: embedModel, input: text })).data[0].embedding
export const chat = async (system, user) => (await j(`${base}/chat/completions`, { model: chatModel, temperature: 0.2, messages: [{ role: 'system', content: system }, { role: 'user', content: user }] })).choices[0].message.content
