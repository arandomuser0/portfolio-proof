"""Token-free portfolio GIFs - pure PIL, no API keys, no servers.
Outputs (800x450, ~3s, 10fps):
  portfolio/ledgerly-vue-crm/demo.gif
  portfolio/coach-platform-audit/demo.gif
  portfolio/ai-docs-assistant/demo.gif
Run: py make_gifs.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 800, 450, 10

def font(big=28, mono=False):
    # Windows fonts, fallback to default
    cands = ["C:/Windows/Fonts/arialbd.ttf" if not mono else "C:/Windows/Fonts/consola.ttf",
             "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/consolab.ttf"]
    for c in cands:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, big)
            except Exception: pass
    return ImageFont.load_default()

F_TITLE = font(30); F_BODY = font(20); F_MONO = font(17, True); F_SMALL = font(15)

def base(bg, title, sub):
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 86], fill=(255, 255, 255) if bg != (9, 9, 11) else (24, 24, 27))
    d.text((28, 18), title, font=F_TITLE, fill=(17, 24, 39) if bg != (9, 9, 11) else (255, 255, 255))
    d.text((28, 52), sub, font=F_SMALL, fill=(100, 116, 139))
    return im, d

def save(frames, out):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=int(1000 / FPS), loop=0, optimize=True)
    print("wrote", out, len(frames), "frames")

def gif_vue():
    frames = []
    cards = [("Maya Chen", "$48,000", "Prime · 742", (22, 163, 74)), ("Jonas Weber", "$12,000", "Near-prime · 658", (202, 138, 4))]
    for f in range(30):
        im, d = base((241, 245, 249), "Ledgerly Vue CRM", "Vue 3 + Pinia + Axios - mock API, no backend needed")
        # filter pills animate
        for i, label in enumerate(["all", "pending", "review"]):
            x = 28 + i * 110
            active = (f // 10) % 3 == i
            d.rounded_rectangle([x, 100, x + 96, 132], 20, fill=(15, 23, 42) if active else (255, 255, 255), outline=(203, 213, 225))
            d.text((x + 18, 107), label, font=F_SMALL, fill=(255, 255, 255) if active else (71, 85, 105))
        # cards slide in
        for ci, (name, amt, badge, col) in enumerate(cards):
            off = max(0, 12 - f + ci * 4) * 14
            y = 152 + ci * 140 - min(f * 2, 0)
            y0 = 152 + ci * 140 + off
            d.rounded_rectangle([28, y0, W - 28, y0 + 120], 14, fill=(255, 255, 255), outline=(226, 232, 240))
            d.text((48, y0 + 14), name, font=F_BODY, fill=(15, 23, 42))
            d.text((48, y0 + 42), f"{amt} · Updated Sep 2026", font=F_SMALL, fill=(100, 116, 139))
            bw = 170
            d.rounded_rectangle([W - 48 - bw, y0 + 14, W - 48, y0 + 42], 10, fill=col)
            d.text((W - 40 - bw, y0 + 18), badge, font=F_SMALL, fill=(255, 255, 255))
            d.text((48, y0 + 72), "GET /applications → 200 in 412ms · loading / empty / error states", font=F_SMALL, fill=(71, 85, 105))
        d.text((28, H - 30), "npm run mock-api  →  json-server :3001  ·  no token needed", font=F_SMALL, fill=(100, 116, 139))
        frames.append(im)
    return frames

def gif_audit():
    lines = ["$ supabase start", "$ supabase db push  →  0001_core.sql OK", "$ functions serve stripe-webhook", "✓ RLS on  ✓ signature check  ✓ idempotency", "P0 RLS  P1 cron  P2 indexes → AUDIT-REPORT.md"]
    frames = []
    for f in range(30):
        im, d = base((9, 9, 11), "Coach Audit Kit", "Supabase + Stripe + Slack - local check, no prod keys")
        d.rounded_rectangle([28, 100, W - 28, H - 44], 12, fill=(24, 24, 27), outline=(63, 63, 70))
        n = min(len(lines), 1 + f // 5)
        for i in range(n):
            col = (52, 211, 153) if lines[i].startswith("✓") or "OK" in lines[i] else (228, 228, 231)
            d.text((48, 122 + i * 44), lines[i][: int(4 + (f % 6) * 8) if i == n - 1 else 99], font=F_MONO, fill=col)
        # progress bar
        p = (f + 1) / 30
        d.rounded_rectangle([48, H - 70, W - 48, H - 60], 5, fill=(63, 63, 70))
        d.rounded_rectangle([48, H - 70, 48 + int((W - 96) * p), H - 60], 5, fill=(52, 211, 153))
        frames.append(im)
    return frames

def gif_react():
    frames = []
    for f in range(30):
        im, d = base((255, 255, 255), "Pulseboard React Landing", "React 18 + Vite + Tailwind - 10 sections, npm run build passes")
        d.rounded_rectangle([28, 100, W - 28, 210], 14, fill=(15, 28, 46))
        d.text((48, 116), "Support tickets that", font=F_TITLE, fill=(255, 255, 255))
        d.text((48, 150), "resolve themselves", font=F_TITLE, fill=(147, 197, 253))
        bw = 150 + int(6 * (f % 5))
        d.rounded_rectangle([W - 48 - bw, 150, W - 48, 182], 20, fill=(22, 119, 255))
        d.text((W - 40 - bw, 156), "Start free", font=F_SMALL, fill=(255, 255, 255))
        labels = ["Features", "How", "Pricing", "FAQ"]
        for i, label in enumerate(labels):
            x = 48 + i * 180
            on = (f // 7) % 4 == i
            d.rounded_rectangle([x, 230, x + 160, 330], 12, fill=(22, 119, 255) if on else (241, 245, 249), outline=(203, 213, 225))
            d.text((x + 16, 244), label, font=F_BODY, fill=(255, 255, 255) if on else (15, 23, 42))
            d.text((x + 16, 276), "OK" if on else "···", font=F_SMALL, fill=(255, 255, 255) if on else (100, 116, 139))
        d.text((28, H - 30), "App.jsx wires 8 section components - mobile menu, accordion, form state", font=F_SMALL, fill=(100, 116, 139))
        frames.append(im)
    return frames

def gif_rag():
    q = "How do refunds work?"
    a = "Refunds issue in 5-10 days [1]. Late invoices add fees [2]."
    frames = []
    for f in range(30):
        im, d = base((9, 9, 11), "Docs Assistant", "RAG: chunk → embed → cite - Ollama local, no key needed")
        d.rounded_rectangle([28, 100, W - 28, 160], 12, fill=(24, 24, 27), outline=(63, 63, 70))
        d.text((48, 116), "Q: " + q[: max(1, int(len(q) * min(1, f / 10)))], font=F_BODY, fill=(255, 255, 255))
        if f > 10:
            d.rounded_rectangle([28, 176, W - 28, 330], 12, fill=(20, 40, 32), outline=(52, 211, 153))
            shown = a[: max(1, int(len(a) * (f - 10) / 14))]
            d.text((48, 196), shown, font=F_BODY, fill=(209, 250, 229))
            if f > 24:
                d.text((48, 280), "[1] refunds.md#0 · 0.87   [2] billing.md#1 · 0.81", font=F_SMALL, fill=(110, 231, 183))
        d.text((28, H - 30), "POST /api/ask → { answer, citations } · in-memory fallback", font=F_SMALL, fill=(161, 161, 170))
        frames.append(im)
    return frames

if __name__ == "__main__":
    save(gif_vue(), os.path.join(HERE, "portfolio", "ledgerly-vue-crm", "demo.gif"))
    save(gif_audit(), os.path.join(HERE, "portfolio", "coach-platform-audit", "demo.gif"))
    save(gif_rag(), os.path.join(HERE, "portfolio", "ai-docs-assistant", "demo.gif"))
    save(gif_react(), os.path.join(HERE, "portfolio", "react-saas-landing", "demo.gif"))
