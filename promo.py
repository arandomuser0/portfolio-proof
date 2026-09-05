"""Ledgerly promo video - pure Python (Pillow + numpy + OpenCV).
Run: py promo.py   -> outputs ledgerly_promo.mp4 (1280x720, 30fps, ~12s)
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1280, 720, 30
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledgerly_promo.mp4")

WHITE = (255, 255, 255)
INK = (15, 23, 42)
MUTED = (71, 85, 105)
EMERALD = (4, 120, 87)
EMERALD_LT = (236, 253, 245)
BG = (247, 250, 249)
LINE = (226, 232, 240)


def load_font(size, bold=False):
    for p in [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


F_TITLE = load_font(84, True)
F_SUB = load_font(34)
F_BIG = load_font(110, True)
F_MED = load_font(44, True)
F_SMALL = load_font(26)
F_PILL = load_font(24, True)


def canvas():
    return Image.new("RGB", (W, H), WHITE)


def pill(d, xy, wh, fill, outline=None):
    x, y = xy
    w, h = wh
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill, outline=outline, width=2)


def ease(t):
    return 1 - (1 - t) ** 3  # easeOutCubic


def text_center(d, y, s, font, fill):
    bb = d.textbbox((0, 0), s, font=font)
    d.text(((W - (bb[2] - bb[0])) / 2, y), s, font=font, fill=fill)


# ---- scenes (each returns PIL image given local progress 0..1) ----
def scene_hero(p):
    img = canvas()
    d = ImageDraw.Draw(img)
    e = ease(min(1, p * 1.4))
    d.rectangle([0, 0, W, 10], fill=EMERALD)
    # pill badge slides up
    yo = int((1 - e) * 40)
    pill(d, ((W - 330) // 2, 120 + yo), (330, 52), EMERALD_LT, EMERALD)
    bb = d.textbbox((0, 0), "NEW - INSTANT PAYOUTS", font=F_PILL)
    d.text(((W - (bb[2] - bb[0])) / 2, 134 + yo), "NEW - INSTANT PAYOUTS", font=F_PILL, fill=EMERALD)
    text_center(d, 210, "Ledgerly", F_BIG, INK)
    text_center(d, 340, "Banking that balances itself", F_MED, EMERALD)
    text_center(d, 420, "Checking, cards, invoicing and books in one calm place.", F_SUB, MUTED)
    # CTA button pops in
    s = ease(max(0, (p - 0.35) / 0.65))
    bw, bh = int(260 * s), 72
    if bw > 10:
        pill(d, ((W - 260) // 2 + (260 - bw) // 2, 500), (bw, bh), EMERALD)
        if s > 0.8:
            bb2 = d.textbbox((0, 0), "Start free", font=F_MED)
            d.text(((W - (bb2[2] - bb2[0])) / 2, 508), "Start free", font=F_MED, fill=WHITE)
    return img


def scene_stats(p):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    text_center(d, 90, "Loved by modern teams", F_MED, INK)
    stats = [("$4.2B", "processed yearly"), ("28k", "businesses"), ("99.99%", "uptime"), ("41s", "month-end close")]
    for i, (v, l) in enumerate(stats):
        x = 90 + i * 285
        # staggered rise
        lp = max(0, min(1, (p - i * 0.12) / 0.5))
        yo = int((1 - ease(lp)) * 60)
        d.rounded_rectangle([x, 220 + yo, x + 245, 480 + yo], radius=24, fill=WHITE, outline=LINE, width=2)
        bb = d.textbbox((0, 0), v, font=F_MED)
        d.text((x + (245 - (bb[2] - bb[0])) / 2, 290 + yo), v, font=F_MED, fill=EMERALD)
        bb2 = d.textbbox((0, 0), l, font=F_SMALL)
        d.text((x + (245 - (bb2[2] - bb2[0])) / 2, 360 + yo), l, font=F_SMALL, fill=MUTED)
    return img


def scene_features(p):
    img = canvas()
    d = ImageDraw.Draw(img)
    text_center(d, 80, "Everything money touches", F_MED, INK)
    feats = [
        ("Instant payouts", "Vendors paid in seconds", EMERALD_LT, EMERALD),
        ("Smart team cards", "Limits + auto receipts", WHITE, INK),
        ("Books close themselves", "Reconciled in 41s", WHITE, INK),
    ]
    for i, (t, s, fill, col) in enumerate(feats):
        lp = max(0, min(1, (p - i * 0.15) / 0.5))
        xo = int((1 - ease(lp)) * -140)
        y = 200 + i * 150
        d.rounded_rectangle([140 + xo, y, W - 140 + xo, y + 120], radius=20, fill=fill,
                            outline=LINE if fill == WHITE else EMERALD, width=2)
        d.ellipse([170 + xo, y + 35, 220 + xo, y + 85], fill=EMERALD)
        d.text((245 + xo, y + 24), t, font=F_MED, fill=col)
        d.text((245 + xo, y + 72), s, font=F_SMALL, fill=MUTED)
    return img


def scene_cta(p):
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    e = ease(min(1, p * 1.5))
    yo = int((1 - e) * 50)
    text_center(d, 200 + yo, "Open your account", F_BIG, WHITE)
    text_center(d, 330 + yo, "in 10 minutes", F_BIG, (110, 231, 183))
    text_center(d, 470 + yo, "Free to start. No card required.", F_SUB, (148, 163, 184))
    s = ease(max(0, (p - 0.4) / 0.6))
    bw = int(280 * s)
    if bw > 10:
        pill(d, ((W - 280) // 2 + (280 - bw) // 2, 550), (bw, 72), EMERALD)
        if s > 0.8:
            bb = d.textbbox((0, 0), "Start free", font=F_MED)
            d.text(((W - (bb[2] - bb[0])) / 2, 558), "Start free", font=F_MED, fill=WHITE)
    return img


SCENES = [(scene_hero, 3.2), (scene_stats, 3.0), (scene_features, 3.2), (scene_cta, 3.0)]
FADE = 0.45  # crossfade seconds


def main():
    total = sum(d for _, d in SCENES)
    nframes = int(total * FPS)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    vw = cv2.VideoWriter(OUT, fourcc, FPS, (W, H))
    assert vw.isOpened(), "could not open VideoWriter"
    # precompute boundaries
    bounds = []
    t = 0.0
    for f, dur in SCENES:
        bounds.append((t, t + dur, f))
        t += dur
    for n in range(nframes):
        ts = n / FPS
        # find scene
        idx = next(i for i, (a, b, _) in enumerate(bounds) if ts < b or i == len(bounds) - 1)
        a, b, fn = bounds[idx]
        lp = (ts - a) / (b - a)
        frame = fn(min(1, max(0, lp)))
        # progress bar
        d = ImageDraw.Draw(frame)
        d.rectangle([0, H - 8, W, H], fill=LINE)
        d.rectangle([0, H - 8, W * ts / total, H], fill=EMERALD)
        vw.write(cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
        if n % 60 == 0:
            print(f"{n}/{nframes} frames", flush=True)
    vw.release()
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
