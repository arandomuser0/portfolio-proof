# Audit report (fill per client) — Gate 2 deliverable
## P0 (fix before scale)
- [ ] RLS: list tables with RLS OFF → `select tablename from pg_tables where schemaname='public'` + check policies
- [ ] Stripe webhook: signature verified? idempotency on `stripe_session_id`? tested with `stripe trigger checkout.session.completed`?
- [ ] Keys: `service_role` in Lovable/frontend bundle? rotate if yes
## P1
- [ ] pg_cron overlaps (add `for update skip locked` claim pattern), timezone pinned UTC
- [ ] Slack scopes minimal (`chat:write`, `users:read` only?), retry with backoff on `ratelimited`
- [ ] Backups: PITR on? restore tested?
## P2 — docs, indexes on (enrollment_id, sent_at), monitoring/alerts, multi-program readiness
Estimate each P0 at 2-4h, P1 at 1-2h. Stop/continue gate after this file is approved.
