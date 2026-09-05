# AI Docs Assistant — minimal RAG
Ask questions over your own docs with citations. Junior AI-integration proof.

**Stack:** Node 22 + Express + pgvector-ready (`pg`) with in-memory fallback + any OpenAI-compatible chat/embeddings API + single-file Tailwind UI. Dockerfile included.

## Run
```bash
cd server
cp .env.example .env  # set OPENAI_API_KEY + OPENAI_BASE_URL (OpenAI, Anthropic-compat, Gemini-compat, or Ollama)
npm i
npm run dev  # :8787, serves ../web + API
```

## Endpoints
- `POST /api/ingest {id, text, meta?}` — chunks (~800 chars), embeds, upserts
- `POST /api/ask {question}` — embeds query, cosine top-k (default 4), builds cited prompt, calls chat model, returns `{answer, citations:[{id, score, snippet}]}`
- `GET /api/health`

## What it proves
- Chunk → embed → store → retrieve → cited answer (no blind completion)
- Function separation: `embeddings.js`, `store.js` (pgvector SQL when `DATABASE_URL` set, else memory), `rag.js` (prompt builder with anti-hallucination: "answer only from context, say unknown otherwise")
- Eval: `npm run eval` runs 5 golden Q&As, reports hit-rate

Not claiming fine-tuning / K8s / senior MLOps. This is the honest junior slice: API + retrieval + evals + Docker.
