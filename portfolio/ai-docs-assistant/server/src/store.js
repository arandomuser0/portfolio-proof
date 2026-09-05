// pgvector when DATABASE_URL set, else in-memory cosine (good for demo/eval)
import pg from 'pg'
const pool = process.env.DATABASE_URL ? new pg.Pool({ connectionString: process.env.DATABASE_URL }) : null
const mem = []
const cos = (a, b) => { let d = 0, na = 0, nb = 0; for (let i = 0; i < a.length; i++) { d += a[i] * b[i]; na += a[i] ** 2; nb += b[i] ** 2 } return d / (Math.sqrt(na) * Math.sqrt(nb) + 1e-9) }
export async function upsert({ id, text, vec }) {
  if (!pool) { const i = mem.findIndex(m => m.id === id); i >= 0 ? mem[i] = { id, text, vec } : mem.push({ id, text, vec }); return }
  await pool.query(`create extension if not exists vector; create table if not exists docs(id text primary key, text text, embedding vector(1536))`);
  await pool.query(`insert into docs(id, text, embedding) values($1,$2,$3) on conflict (id) do update set text=$2, embedding=$3`, [id, text, JSON.stringify(vec)]);
}
export async function query(vec, k = 4) {
  if (!pool) return mem.map(m => ({ ...m, score: cos(vec, m.vec) })).sort((a, b) => b.score - a.score).slice(0, k);
  const { rows } = await pool.query(`select id, text, 1 - (embedding <=> $1) as score from docs order by embedding <=> $1 limit $2`, [JSON.stringify(vec), k]);
  return rows;
}
