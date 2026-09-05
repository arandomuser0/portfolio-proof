import express from 'express'
import cors from 'cors'
import 'dotenv/config'
import { upsert, query } from './store.js'
import { embed, chat } from './llm.js'
import { buildPrompt } from './rag.js'

const app = express()
app.use(cors()); app.use(express.json({ limit: '1mb' }))
app.get('/api/health', (_, res) => res.json({ ok: true }))

app.post('/api/ingest', async (req, res) => {
  const { id, text } = req.body || {}
  if (!id || !text) return res.status(400).json({ error: 'id + text required' })
  const chunks = text.match(/[\s\S]{1,800}/g) || []
  for (const [i, c] of chunks.entries()) {
    const vec = await embed(c)
    await upsert({ id: `${id}#${i}`, text: c, vec })
  }
  res.json({ ok: true, chunks: chunks.length })
})

app.post('/api/ask', async (req, res) => {
  const { question } = req.body || {}
  if (!question) return res.status(400).json({ error: 'question required' })
  const qvec = await embed(question)
  const hits = await query(qvec, 4)
  const { system, user } = buildPrompt(question, hits)
  const answer = await chat(system, user)
  res.json({ answer, citations: hits.map(h => ({ id: h.id, score: +h.score.toFixed(3), snippet: h.text.slice(0, 220) })) })
})

app.listen(process.env.PORT || 8787, () => console.log('RAG on :8787'))
