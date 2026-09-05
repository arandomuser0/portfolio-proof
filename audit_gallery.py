"""Audit gallery covers for text overflow: measure every drawn string against canvas bounds.
Run: py audit_gallery.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 720, 540

def font(size, bold=True, mono=False):
    if mono:
        p = "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf"
    else:
        p = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    try:
        return ImageFont.truetype(p, size)
    except Exception:
        return ImageFont.load_default()

F = {
    "num200": font(200),
    "title46": font(46),
    "sub20": font(20, bold=False),
    "mono26": font(26, mono=True),
    "mono17": font(17),
    "tag16": font(16),
    "idx22": font(22),
    "big34": font(34),
    "big36": font(36),
    "mono38": font(38, mono=True),
}

ITEMS = {
    "01-ledgerly": [
        ("num200", "$84,290", 36, 96),
        ("title46", "LEDGERLY", 40, 288),
        ("sub20", "Business banking that balances itself", 40, 342),
        ("mono17", "github.com/arandomuser0/portfolio-proof  -  index.html", 36, 484),
    ],
    "02-fern": [
        ("big34", "YOU 62%", 52, 140),
        ("big34", "TAX", 436, 140),
        ("title46", "FERN", 36, 250),
        ("sub20", "Freelance pay, minus the panic", 36, 304),
        ("mono17", "github.com/arandomuser0/portfolio-proof  -  fern.html", 36, 484),
    ],
    "03-vue-crm": [
        ("mono38", "<LoanCard />", 64, 130),
        ("mono38", "<ScoreBadge />", 384, 130),
        ("big34", "Pinia - Router - Axios", 64, 240),
        ("title46", "VUE 3 LOAN CRM", 36, 330),
        ("sub20", "Real components, loading and error states, mock REST API", 36, 384),
        ("mono17", "portfolio/ledgerly-vue-crm  -  demo.gif inside", 36, 484),
    ],
    "04-supabase-audit": [
        ("mono26", "$ supabase db push", 64, 150),
        ("mono26", "RLS enabled on 3 tables", 64, 190),
        ("mono26", "$ functions serve stripe-webhook", 64, 230),
        ("mono26", "signature verified - idempotent", 64, 270),
        ("title46", "SUPABASE AUDIT KIT", 36, 340),
        ("sub20", "RLS - pg_cron - Deno webhooks - Stripe - Slack", 36, 394),
        ("mono17", "portfolio/coach-platform-audit  -  gate-2 report template", 36, 484),
    ],
    "05-rag-assistant": [
        ("big36", "Q: How do refunds work?", 64, 116),
        ("big36", "A: with [1] [2] citations", 64, 200),
        ("title46", "RAG DOCS ASSISTANT", 36, 286),
        ("sub20", "chunk - embed - retrieve - cite - eval", 36, 340),
        ("mono17", "portfolio/ai-docs-assistant  -  run: npm i && npm run dev", 36, 484),
    ],
}

TAGS = {
    "01-ledgerly": (390, ["TAILWIND", "MARKETING SITE", "FINTECH"]),
    "02-fern": (366, ["CONSUMER FINTECH", "EDITORIAL UI", "SALARY SMOOTHING"]),
    "03-vue-crm": (428, ["VUE 3", "PINIA", "REST API"]),
    "04-supabase-audit": (436, ["POSTGRES", "EDGE FUNCTIONS", "SECURITY"]),
    "05-rag-assistant": (396, ["EXPRESS", "PGVECTOR-READY", "EVALS"]),
}

measurer = ImageDraw.Draw(Image.new("RGB", (8, 8)))
problems = 0
for name, strings in ITEMS.items():
    print(f"--- {name}")
    for fk, text, x, y in strings:
        f = F[fk]
        bbox = measurer.textbbox((0, 0), text, font=f)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        status = "OK"
        if x + tw > W - 8 or y + th > H - 8 or x < 8 or y < 8:
            status = f"OVERFLOW (x+tw={x+tw}, y+th={y+th})"
            problems += 1
        print(f"  [{fk}] {text[:42]!r} w={tw} h={th} end=({x+tw},{y+th}) {status}")
    y_tags, tags = TAGS[name]
    x = 40
    for t in tags:
        tw = measurer.textbbox((0, 0), t, font=F["tag16"])[2]
        endx = x + tw + 28
        if endx > W - 8:
            print(f"  TAG OVERFLOW: {t} ends at {endx}")
            problems += 1
        x = endx + 16
print(f"\nTOTAL PROBLEMS: {problems}")
