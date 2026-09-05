# Coach Platform Audit Kit (Supabase + Stripe + Slack)
Junior/mid audit starter — shows I can review a vibe-coded Supabase backend without breaking prod.

## Layout
- `supabase/migrations/0001_core.sql` — participants, enrollments, messages, RLS on, pg_cron daily scheduler
- `supabase/functions/stripe-webhook/index.ts` — Deno: verify Stripe signature, idempotent enrolment
- `supabase/functions/slack-onboard/index.ts` — invite + welcome sequence trigger
- `docs/AUDIT-REPORT.md` — prioritized findings template (P0/P1/P2) with estimates
- `docs/TESTING.md` — how I tested webhooks locally with Stripe CLI

## Run / check
```bash
supabase start
supabase db push
supabase functions serve stripe-webhook --env-file .env
stripe listen --forward-to localhost:54321/functions/v1/stripe-webhook
```

## What I audit first (Gate 2 order)
1. Backups + RLS (any `policy permissive`? any table without RLS?)
2. Stripe webhook: signature verified? idempotency key? replay safe?
3. pg_cron: overlapping runs? timezone UTC? failure alerting?
4. Slack: token scopes minimal? rate-limit retries?
5. Lovable → Supabase: anon key exposed? service_role never in frontend?

See `docs/AUDIT-REPORT.md` for the full checklist I fill per client.
