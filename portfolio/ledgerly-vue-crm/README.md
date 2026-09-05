# Ledgerly Vue CRM — loan applications mini-CRM
Vue 3 CRM slice that mirrors the loan/scorecard job: Figma → components → REST.

**Stack:** Vue 3 + Vite + Vue Router + Pinia + Axios + Bootstrap 5

## Run
```bash
npm i
npm run dev
# mock API: npm run mock-api (json-server on :3001)
```

## What it proves
- `src/components/LoanCard.vue`, `ScoreBadge.vue` — reusable, prop-typed, responsive
- `src/stores/applications.js` — Pinia store with loading/error/auth states
- `src/api/client.js` — Axios instance with token interceptor + 401 refresh + error normalizer
- `src/views/` — Dashboard (metrics, no card-soup), Applications (filter + skeleton + empty + error), ApplicationDetail (score timeline)
- Pixel discipline: 8pt spacing, tabular-nums for money, WCAG AA contrast on CTAs

## API contract used
`GET /applications?status=` → `[{id, applicant, amount, score, risk, status, updatedAt}]`
`GET /applications/:id` → detail + `scoreHistory[]` + `documents[]`
`POST /applications/:id/decision` → `{decision: approved|rejected, note}` (auth required)

Point it at any REST backend by changing `VITE_API_URL`.
