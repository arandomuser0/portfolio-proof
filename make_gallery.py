"""Gallery covers v2: premium dark cards, per-project accent, oversized type.
720x540, bold thumbnail-first design.
Run: py make_gallery.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "gallery")
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

F_NUM = font(200)
F_TITLE = font(46)
F_SUB = font(20, bold=False)
F_MONO = font(17)
F_TAG = font(16)
F_INDEX = font(22)

BG = (12, 14, 18)
GRID = (28, 32, 40)
WHITE = (245, 247, 250)
MUTE = (120, 130, 145)

def canvas(accent):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # subtle grid
    for x in range(0, W, 48):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 48):
        d.line([(0, y), (W, y)], fill=GRID, width=1)
    # accent bar top
    d.rectangle([0, 0, W, 10], fill=accent)
    return im, d

def tag(d, x, y, text, accent):
    w = d.textlength(text, font=F_TAG)
    d.rounded_rectangle([x, y, x + w + 28, y + 34], 17, outline=accent, width=2)
    d.text((x + 14, y + 6), text, font=F_TAG, fill=WHITE)
    return x + w + 44

def footer(d, accent, left):
    d.rectangle([0, H - 6, W, H], fill=accent)
    d.text((36, H - 56), left, font=F_MONO, fill=MUTE)

def ledgerly():
    acc = (52, 211, 153)  # emerald
    im, d = canvas(acc)
    d.text((560, 60), "01", font=F_INDEX, fill=MUTE)
    d.text((36, 120), "$84,290", font=font(112), fill=acc)
    d.text((40, 288), "LEDGERLY", font=F_TITLE, fill=WHITE)
    d.text((40, 342), "Business banking that balances itself", font=F_SUB, fill=MUTE)
    x = 40
    x = tag(d, x, 390, "TAILWIND", acc)
    x = tag(d, x, 390, "MARKETING SITE", acc)
    tag(d, x, 390, "FINTECH", acc)
    footer(d, acc, "github.com/arandomuser0/portfolio-proof  -  index.html")
    return im

def fern():
    acc = (251, 191, 36)  # amber
    im, d = canvas(acc)
    d.text((560, 60), "02", font=F_INDEX, fill=MUTE)
    # salary split bar as hero shape
    bx, bw = 40, 640
    d.rounded_rectangle([bx, 110, bx + bw, 210], 24, fill=(30, 34, 42))
    d.rounded_rectangle([bx, 110, bx + int(bw * 0.62), 210], 24, fill=acc)
    d.text((52, 140), "YOU 62%", font=font(34), fill=(20, 24, 28))
    d.text((bx + int(bw * 0.66), 140), "TAX", font=font(34), fill=(20, 24, 28))
    d.text((36, 250), "FERN", font=F_TITLE, fill=WHITE)
    d.text((36, 304), "Freelance pay, minus the panic", font=F_SUB, fill=MUTE)
    x = 40
    x = tag(d, x, 366, "CONSUMER FINTECH", acc)
    x = tag(d, x, 366, "EDITORIAL UI", acc)
    tag(d, x, 366, "SALARY SMOOTHING", acc)
    footer(d, acc, "github.com/arandomuser0/portfolio-proof  -  fern.html")
    return im

def vue():
    acc = (96, 165, 250)  # sky blue
    im, d = canvas(acc)
    d.text((560, 60), "03", font=F_INDEX, fill=MUTE)
    # stylized component blocks
    d.rounded_rectangle([40, 100, 340, 200], 18, fill=(30, 34, 42))
    d.rounded_rectangle([360, 100, 680, 200], 18, fill=(30, 34, 42))
    d.rounded_rectangle([40, 220, 680, 300], 18, fill=(30, 34, 42))
    d.text((64, 130), "<LoanCard />", font=font(38, mono=True), fill=acc)
    d.text((384, 130), "<ScoreBadge />", font=font(38, mono=True), fill=acc)
    d.text((64, 240), "Pinia - Router - Axios", font=font(34, mono=True), fill=WHITE)
    d.text((36, 330), "VUE 3 LOAN CRM", font=F_TITLE, fill=WHITE)
    d.text((36, 384), "Real components, loading and error states, mock REST API", font=F_SUB, fill=MUTE)
    x = 40
    x = tag(d, x, 428, "VUE 3", acc)
    x = tag(d, x, 428, "PINIA", acc)
    tag(d, x, 428, "REST API", acc)
    footer(d, acc, "portfolio/ledgerly-vue-crm  -  demo.gif inside")
    return im

def supabase():
    acc = (52, 211, 153)  # supabase green
    im, d = canvas(acc)
    d.text((560, 60), "04", font=F_INDEX, fill=MUTE)
    # terminal card
    d.rounded_rectangle([40, 96, 680, 316], 18, fill=(16, 18, 22), outline=(50, 56, 68), width=2)
    for i, c in enumerate(acc and [(239, 68, 68), (250, 204, 21), (52, 211, 153)]):
        d.ellipse([64 + i * 30, 118, 78 + i * 30, 132], fill=c)
    lines = [
        ("$ supabase db push", WHITE),
        ("RLS enabled on 3 tables", acc),
        ("$ functions serve stripe-webhook", WHITE),
        ("signature verified - idempotent", acc),
    ]
    for i, (t, c) in enumerate(lines):
        d.text((64, 150 + i * 40), t, font=font(26, mono=True), fill=c)
    d.text((36, 340), "SUPABASE AUDIT KIT", font=F_TITLE, fill=WHITE)
    d.text((36, 394), "RLS - pg_cron - Deno webhooks - Stripe - Slack", font=F_SUB, fill=MUTE)
    x = 40
    x = tag(d, x, 436, "POSTGRES", acc)
    x = tag(d, x, 436, "EDGE FUNCTIONS", acc)
    tag(d, x, 436, "SECURITY", acc)
    footer(d, acc, "portfolio/coach-platform-audit  -  gate-2 report template")
    return im

def rag():
    acc = (167, 139, 250)  # violet
    im, d = canvas(acc)
    d.text((560, 60), "05", font=F_INDEX, fill=MUTE)
    # citation chips as hero shape
    q = d.textlength("Q: How do refunds work?", font=font(36))
    d.rounded_rectangle([40, 100, 40 + q + 48, 168], 18, fill=(30, 34, 42))
    d.text((64, 116), "Q: How do refunds work?", font=font(36), fill=WHITE)
    a = d.textlength("A: ...with [1] [2] citations", font=font(36))
    d.rounded_rectangle([40, 184, 40 + a + 48, 252], 18, fill=(30, 34, 42), outline=acc, width=2)
    d.text((64, 200), "A: with [1] [2] citations", font=font(36), fill=acc)
    d.text((36, 286), "RAG DOCS ASSISTANT", font=F_TITLE, fill=WHITE)
    d.text((36, 340), "chunk - embed - retrieve - cite - eval", font=F_SUB, fill=MUTE)
    x = 40
    x = tag(d, x, 396, "EXPRESS", acc)
    x = tag(d, x, 396, "PGVECTOR-READY", acc)
    tag(d, x, 396, "EVALS", acc)
    footer(d, acc, "portfolio/ai-docs-assistant  -  run: npm i && npm run dev")
    return im

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in [
        ("01-ledgerly", ledgerly),
        ("02-fern", fern),
        ("03-vue-crm", vue),
        ("04-supabase-audit", supabase),
        ("05-rag-assistant", rag),
    ]:
        p = os.path.join(OUT, f"{name}.png")
        fn().save(p, optimize=True)
        print("wrote", p)
