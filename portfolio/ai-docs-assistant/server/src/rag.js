export function buildPrompt(question, hits) {
  const ctx = hits.map((h, i) => `[${i + 1}] (${h.id} | ${h.score.toFixed(3)})\n${h.text}`).join('\n\n')
  return {
    system: 'Answer ONLY from the context. If unknown, say "I don\'t know from these docs." Always cite [1],[2] inline.',
    user: `Context:\n${ctx}\n\nQuestion: ${question}`
  }
}
