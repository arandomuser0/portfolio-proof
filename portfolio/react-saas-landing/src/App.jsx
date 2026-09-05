import { Nav, Footer } from './components/chrome.jsx'
import { Hero, LogoWall, Features, HowItWorks, Pricing, Testimonials, Faq, Cta } from './components/sections.jsx'

export default function App() {
  return (
    <div className="bg-white text-slate-900">
      <Nav />
      <main>
        <Hero />
        <LogoWall />
        <Features />
        <HowItWorks />
        <Pricing />
        <Testimonials />
        <Faq />
        <Cta />
      </main>
      <Footer />
    </div>
  )
}
