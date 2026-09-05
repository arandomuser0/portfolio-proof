-- Core tables + RLS + pg_cron. Review-first: no service_role in frontend, anon locked by RLS.
create table if not exists participants (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  slack_user_id text,
  stripe_customer_id text,
  created_at timestamptz default now()
);
create table if not exists enrollments (
  id uuid primary key default gen_random_uuid(),
  participant_id uuid references participants(id) on delete cascade,
  program text default 'flagship-90d',
  status text default 'active' check (status in ('active','paused','done','refunded')),
  stripe_session_id text unique,
  created_at timestamptz default now()
);
create table if not exists messages (
  id bigint generated always as identity primary key,
  enrollment_id uuid references enrollments(id) on delete cascade,
  day int not null,
  channel text default 'slack',
  payload jsonb not null,
  sent_at timestamptz,
  created_at timestamptz default now()
);
alter table participants enable row level security;
alter table enrollments enable row level security;
alter table messages enable row level security;
-- Admin-only by default (service_role bypasses RLS; anon gets nothing until explicit policy)
-- Example read-own policy to add per app: create policy "own" on enrollments for select using (auth.uid() = participant_id);

-- Daily 09:00 UTC sender (idempotent: only unsent, one claim per row)
select cron.schedule('send-daily-coaching', '0 9 * * *', $$
  update messages set sent_at = now()
  where sent_at is null and day <= 90
  and enrollment_id in (select id from enrollments where status = 'active');
$$);
