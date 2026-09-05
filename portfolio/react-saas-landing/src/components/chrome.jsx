import { useEffect, useRef, useState } from 'react'
import { Menu, X } from 'lucide-react'

export function useReveal() {
  const ref = useRef(null)
  useEffect(() => {
    const el = ref.current
    if (!el) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      el.classList.add('in')
      return
    }
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && (e.target.classList.add('in'), io.unobserve(e.target))),
      { threshold: 0.12 }
    )
    io.observe(el)
    return () => io.disconnect()
  }, [])
  return ref
}

export function Reveal({ children, className = '' }) {
  const ref = useReveal()
  return (
    <div ref={ref} className={`reveal ${className}`}>
      {children}
    </div>
  )
}

const LINKS = [
  ['Features', '#features'],
  ['How it works', '#how'],
  ['Pricing', '#pricing'],
  ['FAQ', '#faq'],
]

export function Nav() {
  const [open, setOpen] = useState(false)
  return (
    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/85 backdrop-blur">
      <nav className="mx-auto flex h-[68px] max-w-7xl items-center justify-between gap-6 px-5" aria-label="Primary">
        <a href="#top" className="flex shrink-0 items-center gap-2">
          <span className="grid h-8 w-8 place-items-center rounded-[10px] bg-[#1677ff] font-extrabold text-white">P</span>
          <span className="text-[17px] font-bold tracking-tight">Pulseboard</span>
        </a>
        <div className="hidden items-center gap-8 whitespace-nowrap text-[14.5px] font-medium text-slate-600 lg:flex">
          {LINKS.map(([label, href]) => (
            <a key={href} href={href} className="hover:text-slate-900">
              {label}
            </a>
          ))}
        </div>
        <div className="flex shrink-0 items-center gap-3">
          <a href="#cta" className="hidden px-3 py-2 text-[14.5px] font-semibold text-slate-700 hover:text-slate-900 sm:inline-flex">
            Sign in
          </a>
          <a href="#cta" className="rounded-full bg-[#1677ff] px-5 py-2.5 text-[14.5px] font-semibold text-white transition hover:bg-[#0b5fd9]">
            Start free
          </a>
          <button
            className="grid h-10 w-10 place-items-center rounded-full border border-slate-200 lg:hidden"
            onClick={() => setOpen((v) => !v)}
            aria-expanded={open}
            aria-label="Toggle menu"
          >
            {open ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </nav>
      {open && (
        <div className="border-t border-slate-200 bg-white px-5 py-4 lg:hidden">
          {LINKS.map(([label, href]) => (
            <a key={href} href={href} onClick={() => setOpen(false)} className="block py-2.5 font-medium text-slate-700">
              {label}
            </a>
          ))}
        </div>
      )}
    </header>
  )
}

export function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-50/60">
      <div className="mx-auto flex max-w-7xl flex-col items-start justify-between gap-6 px-5 py-10 md:flex-row md:items-center">
        <div className="flex items-center gap-2">
          <span className="grid h-7 w-7 place-items-center rounded-lg bg-[#1677ff] text-[13px] font-extrabold text-white">P</span>
          <span className="font-bold tracking-tight">Pulseboard</span>
          <span className="ml-2 text-[13px] text-slate-400">2026 Concept demo</span>
        </div>
        <nav className="flex flex-wrap gap-x-6 gap-y-2 text-[13.5px] font-medium text-slate-500" aria-label="Footer">
          <a href="#features" className="hover:text-slate-900">Features</a>
          <a href="#pricing" className="hover:text-slate-900">Pricing</a>
          <a href="#faq" className="hover:text-slate-900">FAQ</a>
          <a href="#cta" className="hover:text-slate-900">Contact</a>
        </nav>
      </div>
    </footer>
  )
}
