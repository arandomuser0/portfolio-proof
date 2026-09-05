import { useState } from 'react'
import { ArrowRight, Bot, Check, Inbox, Play, Search, ShieldCheck, Sparkles, Zap } from 'lucide-react'
import { Reveal } from './chrome.jsx'

export function Hero() {
  return (
    <section className="relative overflow-hidden" id="top">
      <div className="relative mx-auto grid min-h-[calc(100dvh-68px)] max-w-7xl items-center gap-12 px-5 pb-12 pt-16 lg:grid-cols-2 lg:pb-16 lg:pt-24">
        <div>
          <p className="inline-flex items-center gap-2 rounded-full border border-blue-200 bg-blue-50 px-3 py-1.5 text-[11px] font-semibold uppercase tracking-[0.18em] text-blue-800">
            <Sparkles size={13} /> New: cited answers
          </p>
          <h1 className="mt-5 text-4xl font-extrabold leading-[1.02] tracking-tighter md:text-5xl lg:text-6xl">
            Support tickets that resolve themselves
          </h1>
          <p className="mt-4 max-w-[46ch] text-base leading-relaxed text-slate-600 lg:text-lg">
            Pulseboard answers from your docs with citations, then escalates with full context.
          </p>
          <div className="mt-7 flex flex-wrap gap-3">
            <a href="#cta" className="rounded-full bg-[#1677ff] px-7 py-3.5 text-[15px] font-semibold text-white transition hover:bg-[#0b5fd9]">
              Start free
            </a>
            <a href="#how" className="rounded-full border border-slate-200 px-7 py-3.5 text-[15px] font-semibold text-slate-800 transition hover:bg-slate-50">
              <Play size={15} className="mr-1 inline" /> Watch 2 min demo
            </a>
          </div>
          <dl className="mt-8 grid max-w-md grid-cols-3 gap-4">
            {[['62%', 'deflected'], ['38s', 'median reply'], ['4.9/5', 'CSAT']].map(([v, l]) => (
              <div key={l}>
                <dt className="sr-only">{l}</dt>
                <dd className="font-mono text-2xl font-semibold tracking-tight">{v}</dd>
                <dd className="text-[12.5px] text-slate-500">{l}</dd>
              </div>
            ))}
          </dl>
        </div>
        <Reveal className="relative">
          <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-[0_24px_60px_-24px_rgba(22,119,255,.25)]">
            <div className="flex items-center justify-between border-b border-slate-200 px-5 py-4">
              <p className="text-[14px] font-semibold">Inbox: 3 need review</p>
              <span className="rounded-full bg-emerald-50 px-2.5 py-1 font-mono text-[11px] font-medium text-emerald-800">AI ONLINE</span>
            </div>
            <ul className="divide-y divide-slate-100 text-[13.5px]">
              {[
                ['Refund timeline?', 'Cited 2 docs, draft ready', true],
                ['SSO setup steps', 'Resolved in 41s', false],
                ['Invoice copy request', 'Resolved in 26s', false],
              ].map(([t, s, hot]) => (
                <li key={t} className="flex items-center gap-3 px-5 py-3.5">
                  <span className={`grid h-8 w-8 place-items-center rounded-full ${hot ? 'bg-blue-50 text-[#1677ff]' : 'bg-slate-100 text-slate-600'}`}>
                    {hot ? <Bot size={16} /> : <Check size={16} />}
                  </span>
                  <span className="flex-1">
                    <span className="block font-semibold leading-tight">{t}</span>
                    <span className="text-[12px] text-slate-500">{s}</span>
                  </span>
                  {hot && <ArrowRight size={16} className="text-slate-400" />}
                </li>
              ))}
            </ul>
          </div>
        </Reveal>
      </div>
    </section>
  )
}

export function LogoWall() {
  return (
    <section className="border-y border-slate-200 bg-slate-50/60" aria-label="Customers">
      <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-center gap-x-10 gap-y-4 px-5 py-8 text-slate-500">
        {['Northwind', 'Fieldset', 'Hexlab', 'Bloomco', 'Orbital', 'Framework'].map((n) => (
          <span key={n} className="font-bold">{n}</span>
        ))}
      </div>
    </section>
  )
}

const FEATURES = [
  { icon: Search, title: 'Retrieval with receipts', body: 'Every answer cites the exact doc chunk it came from. No blind completions reach customers.' },
  { icon: Inbox, title: 'Escalation with context', body: 'Unsure cases route to humans with the full thread, draft reply, and confidence score.' },
  { icon: Zap, title: 'Live in an afternoon', body: 'Connect docs, embed one snippet, watch deflection climb the same week.' },
]

export function Features() {
  return (
    <section id="features" className="mx-auto max-w-7xl scroll-mt-20 px-5 py-16 lg:py-24">
      <Reveal>
        <h2 className="max-w-[22ch] text-3xl font-extrabold leading-tight tracking-tighter md:text-[40px]">
          Everything support touches, answered once
        </h2>
      </Reveal>
      <div className="mt-8 grid gap-4 md:grid-cols-3">
        {FEATURES.map((f, i) => (
          <Reveal key={f.title} className={i === 0 ? 'rounded-2xl bg-slate-900 p-7 text-white' : 'rounded-2xl border border-slate-200 bg-white p-7'}>
            <f.icon size={28} className={i === 0 ? 'text-blue-300' : 'text-slate-800'} />
            <h3 className="mt-4 text-xl font-bold tracking-tight">{f.title}</h3>
            <p className={`mt-2 text-[14.5px] ${i === 0 ? 'text-slate-300' : 'text-slate-600'}`}>{f.body}</p>
          </Reveal>
        ))}
      </div>
    </section>
  )
}

const STEPS = [
  ['01', 'Connect docs', 'Help center, PDFs, past tickets. Chunked and embedded automatically.'],
  ['02', 'Review drafts', 'Approve cited replies for a week while the model learns your tone.'],
  ['03', 'Flip to auto', 'Resolved tickets close themselves. You watch CSAT, not queues.'],
]

export function HowItWorks() {
  return (
    <section id="how" className="border-y border-slate-200 bg-slate-50/70">
      <div className="mx-auto grid max-w-7xl gap-10 px-5 py-16 lg:grid-cols-[.85fr_1.15fr] lg:py-24">
        <Reveal>
          <h2 className="text-3xl font-extrabold leading-tight tracking-tighter md:text-[40px]">Live by Friday, calm by Monday</h2>
          <a href="#cta" className="mt-6 inline-block rounded-full bg-slate-900 px-6 py-3 text-[14.5px] font-semibold text-white">
            Start free
          </a>
        </Reveal>
        <ol className="divide-y divide-slate-200 border-y border-slate-200">
          {STEPS.map(([n, t, b]) => (
            <li key={n} className="flex gap-4 py-5">
              <span className="font-mono font-semibold text-[#1677ff]">{n}</span>
              <div>
                <p className="font-bold">{t}</p>
                <p className="text-[14px] text-slate-600">{b}</p>
              </div>
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}

const PLANS = [
  { name: 'Starter', price: '$0', note: 'For solo founders.', feats: ['100 resolutions / mo', '1 knowledge base', 'Email support'], hot: false },
  { name: 'Growth', price: '$24', note: 'For teams with a queue.', feats: ['Unlimited resolutions', 'Slack + Zendesk', 'CSAT analytics', 'Human review flow'], hot: true },
  { name: 'Scale', price: 'Custom', note: 'For platforms.', feats: ['SSO + audit log', 'Dedicated manager', 'Custom retention'], hot: false },
]

export function Pricing() {
  return (
    <section id="pricing" className="mx-auto max-w-7xl scroll-mt-20 px-5 py-16 lg:py-24">
      <Reveal>
        <h2 className="text-3xl font-extrabold tracking-tighter md:text-[40px]">Two plans, no fine print</h2>
      </Reveal>
      <div className="mt-8 grid items-stretch gap-4 md:grid-cols-3">
        {PLANS.map((p) => (
          <Reveal
            key={p.name}
            className={`relative flex flex-col rounded-2xl border p-7 ${p.hot ? 'border-2 border-[#1677ff] shadow-[0_20px_50px_-24px_rgba(22,119,255,.35)]' : 'border-slate-200 bg-white'}`}
          >
            {p.hot && (
              <span className="absolute -top-3 left-7 rounded-full bg-[#1677ff] px-3 py-1 text-[11.5px] font-bold text-white">
                MOST POPULAR
              </span>
            )}
            <p className="font-bold">{p.name}</p>
            <p className="mt-2 font-mono text-4xl font-semibold tracking-tight">{p.price}</p>
            <p className="mt-1 text-[13.5px] text-slate-500">{p.note}</p>
            <ul className="mt-5 flex-1 space-y-2.5 text-[14px] text-slate-700">
              {p.feats.map((f) => (
                <li key={f} className="flex gap-2">
                  <Check size={16} className="mt-1 shrink-0 text-[#1677ff]" /> {f}
                </li>
              ))}
            </ul>
            <a
              href="#cta"
              className={`mt-6 rounded-full py-3 text-center text-[14.5px] font-semibold ${p.hot ? 'bg-[#1677ff] text-white hover:bg-[#0b5fd9]' : 'border border-slate-200 hover:bg-slate-50'}`}
            >
              Start free
            </a>
          </Reveal>
        ))}
      </div>
    </section>
  )
}

const QUOTES = [
  ['Deflection hit 60% in week two. The citations sold our compliance team.', 'Maya Chen, Support Lead, Fieldset'],
  ['Escalations arrive with drafts attached. Agents edit, not author.', 'Jonas Weber, COO, Hexlab'],
  ['Setup was one snippet. Our docs did the rest.', 'Priya Nair, Founder, Bloomco'],
]

export function Testimonials() {
  return (
    <section id="testimonials" className="border-y border-slate-200">
      <div className="mx-auto max-w-7xl px-5 py-16 lg:py-20">
        <Reveal>
          <h2 className="text-3xl font-extrabold tracking-tighter md:text-[40px]">Loved by support teams</h2>
        </Reveal>
        <div className="mt-8 divide-y divide-slate-200 border-y border-slate-200">
          {QUOTES.map(([q, a]) => (
            <figure key={a} className="grid items-baseline gap-3 py-7 md:grid-cols-[1fr_220px]">
              <blockquote className="text-[17px] leading-snug tracking-tight">“{q}”</blockquote>
              <figcaption className="text-[13.5px] text-slate-500">{a}</figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  )
}

const FAQS = [
  ['Does it hallucinate answers?', 'Drafts that fall below the confidence bar route to humans instead of sending. Every auto-reply carries citations.'],
  ['Which helpdesks connect?', 'Zendesk, Intercom, and Freshdesk today, plus any docs site or PDF export.'],
  ['Can we leave anytime?', 'Yes. Export every resolution and citation as CSV. No lock-in.'],
]

export function Faq() {
  const [open, setOpen] = useState(0)
  return (
    <section id="faq" className="mx-auto max-w-3xl scroll-mt-20 px-5 py-16">
      <Reveal>
        <h2 className="text-3xl font-extrabold tracking-tighter">Questions</h2>
      </Reveal>
      <div className="mt-6 divide-y divide-slate-200 border-y border-slate-200">
        {FAQS.map(([q, a], i) => (
          <div key={q} className="py-5">
            <button onClick={() => setOpen(open === i ? -1 : i)} className="flex w-full cursor-pointer items-center justify-between text-left font-bold" aria-expanded={open === i}>
              {q}
              <span className={`text-xl leading-none text-[#1677ff] transition-transform ${open === i ? 'rotate-45' : ''}`}>+</span>
            </button>
            {open === i && <p className="mt-2 max-w-[52ch] text-[14.5px] text-slate-600">{a}</p>}
          </div>
        ))}
      </div>
    </section>
  )
}

export function Cta() {
  const [sent, setSent] = useState(false)
  return (
    <section id="cta" className="mx-auto max-w-7xl scroll-mt-20 px-5 pb-16 lg:pb-24">
      <Reveal className="rounded-2xl bg-slate-900 p-7 text-white lg:p-12">
        <div className="grid items-center gap-8 lg:grid-cols-2">
          <div>
            <h2 className="flex items-center gap-2 text-3xl font-extrabold tracking-tighter">
              <ShieldCheck size={30} className="text-blue-300" /> Resolve your first 100 tickets free
            </h2>
            <p className="mt-2 text-[14.5px] text-slate-300">Live the same afternoon. No card required.</p>
          </div>
          <form
            className="space-y-3"
            onSubmit={(e) => {
              e.preventDefault()
              setSent(true)
            }}
          >
            <label htmlFor="cta-email" className="mb-1.5 block text-[13px] font-semibold">
              Work email
            </label>
            <input
              id="cta-email"
              type="email"
              required
              placeholder="you@company.com"
              className="w-full rounded-lg border border-white/20 bg-white/10 px-4 py-3 text-[14.5px] text-white placeholder:text-slate-400 focus:outline-2 focus:outline-blue-400"
            />
            <button className="w-full rounded-full bg-[#1677ff] py-3.5 text-[15px] font-semibold transition hover:bg-[#0b5fd9]" type="submit">
              Start free
            </button>
            {sent && <p className="rounded-xl bg-emerald-500/15 px-4 py-3 text-[13.5px] font-medium text-emerald-200">Check your inbox. Your workspace link is on its way.</p>}
          </form>
        </div>
      </Reveal>
    </section>
  )
}
