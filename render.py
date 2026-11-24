#!/usr/bin/env python3
"""Render the news-image-20261124 front page (1024x1024 PNG).

Draws a newspaper front page with Pillow only. Run from the repo root:
    python3 render.py
writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
INK = (0, 0, 0)
PAPER = (255, 255, 255)
GREY = (90, 90, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if fnt.getlength(trial) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_lines(d, lines, fnt, x, y, lh, fill=INK):
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def rule(d, y, x0=36, x1=988, width=2):
    d.line([(x0, y), (x1, y)], fill=INK, width=width)
    return y + width


def kicker(d, text, x, y, size=14):
    f = SANS_B(size)
    spaced = " ".join(list(text))
    d.text((x, y), spaced, font=f, fill=INK)
    return y + size + 6


def story(d, x, y, width, kick, head, head_size, summary, sum_size):
    y = kicker(d, kick, x, y, 14)
    hf = SERIF_B(head_size)
    hl = wrap(head, hf, width)
    y = draw_lines(d, hl, hf, x, y, head_size + 8)
    y += 4
    sf = SERIF(sum_size)
    sl = wrap(summary, sf, width)
    y = draw_lines(d, sl, sf, x, y, sum_size + 7)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # outer border
    d.rectangle([10, 10, 1013, 1013], outline=INK, width=3)

    # masthead
    mf = SERIF_B(58)
    title = "THE WORLD IN ONE PAGE"
    tw = mf.getlength(title)
    d.text(((W - tw) / 2, 32), title, font=mf, fill=INK)
    y = rule(d, 118, width=3)

    # dateline
    df = SANS_B(20)
    date = "TUESDAY  24  NOVEMBER  2026"
    dw = df.getlength(date)
    d.text(((W - dw) / 2, 130), date, font=df, fill=INK)
    y = rule(d, 166, width=3)

    # ---- lead story: Nikkei ----
    y = 184
    y = kicker(d, "MARKETS", 36, y, 14)
    hf = SERIF_B(44)
    hl = wrap("Nikkei roars back as Tokyo reopens", hf, 952)
    y = draw_lines(d, hl, hf, 36, y, 52)
    y += 6
    sf = SERIF(20)
    sl = wrap(
        "Japan's Nikkei 225 jumped about 3% to near 58,000 on Tuesday as Tokyo "
        "trading resumed after a holiday, riding the global AI rally set off by "
        "Nvidia's board reinstating Jensen Huang as chief executive.",
        sf, 952)
    y = draw_lines(d, sl, sf, 36, y, 26)
    y = rule(d, y + 12)

    # ---- story 2: Saryu Kamala Express ----
    y = story(d, 36, y + 10, 952, "ASIA",
              "First India\u2013Nepal train completes maiden run", 28,
              "The Saryu Kamala Express reached Janakpur at 10am on Tuesday, "
              "completing the first direct rail link between Ayodhya and "
              "Janakpur. The return service leaves at 1pm.", 18)
    y = rule(d, y + 10)

    # ---- story 3: Beaver Supermoon ----
    y = story(d, 36, y + 10, 952, "SCIENCE",
              "Beaver Supermoon lights up the night sky", 28,
              "November's full moon \u2014 the first of four supermoons in a row "
              "\u2014 rises tonight, looking bigger and brighter as it swings "
              "closest to Earth.", 18)
    y = rule(d, y + 10)

    # ---- two columns: Champions League + COP31 divers ----
    col_w = 460
    ly = story(d, 36, y + 10, col_w, "SPORT",
               "Foxtel, Kayo win Champions League rights", 24,
               "Kayo Sports and Foxtel were named preferred bidders for "
               "Australia's UEFA Champions League media rights, rights seller "
               "UC3 announced on Tuesday.", 16)
    ry = story(d, 528, y + 10, col_w, "CLIMATE",
               "Reef divers carry ocean plea to Canberra", 24,
               "Divers from the Great Barrier Reef take calls for ocean action "
               "to Parliament House today, straight from the collapsed COP31 "
               "talks in Antalya.", 16)
    y = max(ly, ry)
    y = rule(d, y + 12)

    # ---- in brief: three short items ----
    y = kicker(d, "IN BRIEF", 36, y + 10, 13)
    bf = SERIF(16)
    briefs = [
        ("PORTUGAL", "Parliament votes on the 2027 budget today."),
        ("WEATHER", "Storms set to slam the US West Coast."),
        ("NEPAL", "Saryu Kamala return train leaves at 1pm."),
    ]
    col_x = [36, 352, 668]
    col_w2 = 300
    max_y = y
    for (kick, txt), x in zip(briefs, col_x):
        yy = y
        kf = SANS_B(13)
        d.text((x, yy), kick, font=kf, fill=INK)
        yy += 20
        bl = wrap(txt, bf, col_w2)
        yy = draw_lines(d, bl, bf, x, yy, 21)
        max_y = max(max_y, yy)
    y = rule(d, max_y + 10)

    # ---- footer ticker ----
    tf = SANS_B(15)
    tick = "NIKKEI +3%   \u2022   JANAKPUR 10AM   \u2022   SUPERMOON TONIGHT   \u2022   CHAMPIONS LEAGUE   \u2022   COP31"
    tw = tf.getlength(tick)
    d.text(((W - tw) / 2, y + 10), tick, font=tf, fill=INK)
    ff = SANS(14)
    foot = "THE WORLD IN ONE PAGE  \u2014  FIVE STORIES, ONE DAY"
    fw = ff.getlength(foot)
    d.text(((W - fw) / 2, y + 36), foot, font=ff, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
