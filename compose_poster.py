#!/usr/bin/env python3
"""Compose the 17 November 2026 world-news poster (1024x1024).

Own work: headlines researched from BBC / Al Jazeera / Reuters / AP / NPR
briefings of 17 Nov 2026; hero illustration generated for this entry;
layout and typography composed here with PIL. No copied news photos.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/hatch/workspace/fonts"
HERO = os.path.join(
    HERE, "assets",
    "media-generation-hero-bridge-strait-0-a32fb321-652e-4372-8607-8ec2a891a281.webp",
)

W, H = 1024, 1024
NAVY = (13, 27, 46)
NAVY2 = (18, 38, 62)
GOLD = (212, 160, 60)
PAPER = (247, 243, 234)
INK = (18, 24, 33)
MUTED = (90, 96, 104)
RULE = (200, 192, 172)
WHITE = (255, 255, 255)

TAG_COLORS = {
    "UKRAINE": (168, 42, 42),
    "HORMUZ": (176, 92, 12),
    "ASIA": (24, 96, 74),
    "SPACE": (58, 74, 140),
    "BANKING": (110, 60, 130),
    "EUROPE": (30, 90, 140),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


F_MAST = font("PlusJakartaSans-Bold.ttf", 58)
F_DATE = font("PlusJakartaSans-SemiBold.ttf", 30)
F_TAG = font("PlusJakartaSans-Bold.ttf", 21)
F_HEAD = font("PlusJakartaSans-Bold.ttf", 27)
F_BODY = font("PlusJakartaSans-Regular.ttf", 20)
F_FOOT = font("PlusJakartaSans-Regular.ttf", 17)

STORIES = [
    ("UKRAINE", "Kerch Bridge span collapses\nin Ukrainian strike",
     "Kyiv's river bridges hit by Russian missiles as the Crimea link is severed.",
     "BBC / Al Jazeera"),
    ("HORMUZ", "Tankers hit mines near\nthe Strait of Hormuz",
     "Two tankers catch fire; a third US carrier arrives in the Gulf.",
     "Reuters / Al Jazeera"),
    ("ASIA", "Trump lands in Manila,\nbound for Xi\u2013Putin talks",
     "ASEAN summit opens ahead of Thursday's trilateral in Shenzhen.",
     "Associated Press"),
    ("SPACE", "Vulcan rocket fails;\n40 Amazon satellites lost",
     "ULA launch anomaly destroys the Leo internet payload minutes in.",
     "Spaceflight Now"),
    ("BANKING", "JPMorgan blames software\nbug for Monday outage",
     "Online banking, branches and Zelle slowed \u2014 no cyberattack, bank says.",
     "ABC News"),
    ("EUROPE", "Estonia to shut Russia\nborder crossings",
     "From 1 December, citing a foiled plot to bomb a drone plant.",
     "NPR"),
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 122], fill=GOLD)
    d.text((48, 22), "THE WORLD IN ONE DAY", font=F_MAST, fill=WHITE)
    d.text((48, 84), "TUESDAY  \u00b7  17 NOVEMBER 2026", font=F_DATE, fill=GOLD)

    # --- hero illustration ---
    hero = Image.open(HERO).convert("RGB")
    # cover-crop to 1024x300
    tw, th = 1024, 300
    scale = max(tw / hero.width, th / hero.height)
    hero = hero.resize((int(hero.width * scale) + 1, int(hero.height * scale) + 1),
                       Image.LANCZOS)
    x0 = (hero.width - tw) // 2
    y0 = (hero.height - th) // 2
    hero = hero.crop((x0, y0, x0 + tw, y0 + th))
    img.paste(hero, (0, 122))
    d.rectangle([0, 422, W, 426], fill=GOLD)

    # --- story grid: 2 cols x 3 rows ---
    gx, gy = 48, 448
    cw, ch = 448, 168
    gapx, gapy = 32, 10
    for i, (tag, head, body, src) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (cw + gapx)
        y = gy + row * (ch + gapy)
        color = TAG_COLORS[tag]
        d.text((x, y), tag, font=F_TAG, fill=color)
        d.line([(x, y + 30), (x + 64, y + 30)], fill=color, width=3)
        yy = y + 42
        for line in head.split("\n"):
            d.text((x, yy), line, font=F_HEAD, fill=INK)
            yy += 32
        for line in wrap(d, body, F_BODY, cw):
            d.text((x, yy), line, font=F_BODY, fill=MUTED)
            yy += 25
        d.text((x, yy + 2), "Source: " + src, font=F_FOOT, fill=(140, 130, 110))
        if col == 0:
            d.line([(x + cw + 16, y + 4), (x + cw + 16, y + ch - 8)], fill=RULE, width=1)

    # --- footer ---
    d.line([(48, 994), (976, 994)], fill=RULE, width=1)
    d.text((48, 1001), "Six stories that defined the day  \u00b7  Headlines as reported 17 Nov 2026",
           font=F_FOOT, fill=MUTED)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = build()
    im = Image.open(path)
    print(path, im.size, os.path.getsize(path), "bytes")
