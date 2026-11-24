[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Pazri580/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Pazri580/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Built for make.fun's [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)

# The World in One Page — 24 November 2026

A newspaper front page summing up Tuesday 24 November 2026 in one image.

## The image

`entry.png` is a 1024x1024 RGB PNG drawn with Pillow: masthead "THE WORLD IN ONE PAGE",
dated "Tuesday 24 November 2026", with five stories, an IN BRIEF strip, and a footer ticker.

## The five stories (all verified as 24 November 2026)

1. **LEAD — Nikkei roars back as Tokyo reopens (Markets).** Tokyo trading resumed on
   Tuesday after Monday's Labour Thanksgiving Day holiday; the Nikkei 225 jumped
   about 3% to near 58,000, riding the global AI rally set off by Nvidia's board
   reinstating Jensen Huang as chief executive. Sources: arznab.com Nikkei 225
   index page (24 Nov 2026, +3.35% to 57,976), asiadaily.org, forex.com.
2. **First India–Nepal train completes maiden run (Asia).** The Saryu Kamala Express
   reached Janakpur Dham at 10am on Tuesday, completing the first direct rail link
   between Ayodhya and Janakpur; the return service leaves at 1pm. Sources:
   thedailyjagran.com, qncnews.com, travelbiz.biz.
3. **Beaver Supermoon lights up the night sky (Science).** November's full moon — the
   first of four supermoons in a row — rises on 23–24 November, looking bigger and
   brighter as it swings closest to Earth. Sources: skyatnightmagazine.com,
   ABC News Australia.
4. **Foxtel, Kayo win Champions League rights (Sport).** Kayo Sports and Foxtel were
   named preferred bidders for Australia's UEFA Champions League media rights,
   rights seller UC3 announced on Tuesday. Source: mediaweek.com.au.
5. **Reef divers carry ocean plea to Canberra (Climate).** Divers from the Great
   Barrier Reef take calls for ocean action to Parliament House on 24–25 November,
   straight from the collapsed COP31 talks in Antalya. Source: medianet environment
   hub (dated Tuesday 24 November 2026).

IN BRIEF: Portugal's parliament votes on the 2027 budget; storms set to slam the
US West Coast as Thanksgiving travel peaks; the Saryu Kamala return train leaves
Janakpur at 1pm.

Note: Monday 23 November was the bigger news day (Nvidia/Huang reinstatement,
COP31 collapse, Murmansk governor detained, and more all broke on 23 Nov). Every
story above was checked against a dated source and is genuinely 24 November —
events first reported on earlier dates were excluded.

## How it works

- `main.py` (Python 3.13, stdlib only) copies the fixed `entry.png` held in this
  repo to `/output/entry.png`. No network, no randomness — every run writes the
  same bytes.
- `render.py` is the Pillow script that drew `entry.png` (run once at build time;
  it is kept in the repo so the image's origin is transparent).
- Determinism verified: `main.py` run three times produced byte-identical output
  (sha256 `2e653135199c25a446c659e560e50802ef20b8c799180843143a8ed9ad3a6324`).

## Image

- File: `entry.png` — 1024x1024, RGB, 107,489 bytes (< 1 MiB)
- sha256: `2e653135199c25a446c659e560e50802ef20b8c799180843143a8ed9ad3a6324`
