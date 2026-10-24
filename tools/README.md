# Portfolio toolkit

Scripts used to build Earl Kim's case-study pages and motion pieces with Claude (Oct 2026).
The **Claude Design canvas is the source of truth** for page content — Earl edits there.
`site/canvas-snapshot/` is only a snapshot and may be older than the live canvas.

- Canvas: "Earl Kim Portfolio" — https://claude.ai/artifact/V9K9r3r53vV6yxDuFyAfbc
- Test site: https://iamearlkim.github.io/earlkim-portfolio-preview/
- Final site: earlkim.me (Framer)
- How-to: the `portfolio-case-study` and `case-study-motion` skills, and `../docs/SESSION-NOTES.md`

Requirements: Python 3 + Pillow, Node + Playwright (Chromium), ffmpeg.

## site/ — case-study pages
| File | What it does |
|---|---|
| `gen/tpl.py` | Page building blocks (hero, cover, stats, split, cards, figure, gallery, quote, video, next band…) in the house type scale. Images are referenced by name through `blobs.json`. |
| `gen/pages.py` | Every generated page. `python3 gen/pages.py <canvas/project>` writes the `.dc.html` boards. ⚠ Pages Earl has edited in the canvas (e.g. Google Cloud v3) must be edited from the live file, not regenerated. |
| `blobs.json` | Image name → canvas asset id (`/_blob/<id>`). |
| `build_site.py` | `python3 build_site.py <repo dir>` turns canvas boards into the static preview (maps `.dc.html` → `.html`, `{{accent}}` → #1F3FD1, `/_blob/` → `images/`). Needs the images in a local `img/` folder. |
| `check.js`, `shot.js` | Playwright screenshots at desktop and 390 px; reports horizontal overflow. |

## video/ — motion pieces
Common: `cap.js` renders an animation page frame by frame.
`VWW=<w> VHH=<h> DSF=<scale> [ALPHA=1] [S=start] N=<frames> node cap.js <page.html> <outdir> frames`
(`stills` mode with `TS=1.0,2.5,…` renders sample frames.) Each page exposes `render(t)`.

| Folder | Piece | Output |
|---|---|---|
| `hero/` | Prompt box: type "/403 error" → Skills list → click → Skill detail page | 1920×1200, 12 s, MP4 + transparent WebM |
| `anatomy/` | Zoom through the 6 parts of the Skill detail page with spotlight + footer labels. `cap2.js` captures `detail@3x.png` + `rects.json` from the prototype. | 1920×1200 (render 1536×960 @1.25), 30 s |
| `console/` | Entry point 01. `patch_demo.py` prepares the prototype, `rec.js` records it 12× slowed with timestamps, `compose.py` crops/re-times into a square video with cursor. | 1440×1440, 10 s |
| `gemini/` | Entry point 02, recreated Gemini app: type → answer → Skill card → Open in docs → docs page | 1440×1440 (1200 @1.2), 11.6 s |
| `search/` | Entry point 03, recreated Google Search: type → suggestions → AI Overview with Skill card → docs page | 1440×1440, 11.8 s |
| `docsite/` | Entry point 04, tour of the docs site. `cap.js` captures the screens/states, `compose.py` builds the flow with slides + cursor | 1440×1440, 16 s |

Encode:
```
# transparent WebM (Framer)
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 30 -row-mt 1 -auto-alt-ref 0 out.webm
# MP4 (canvas / Safari), white behind transparent corners
ffmpeg -f lavfi -i color=c=white:s=1920x1200:r=30 -framerate 30 -i frames/f%04d.png -filter_complex "[0][1]overlay=shortest=1,format=yuv420p" -c:v libx264 -crf 22 -preset slow -movflags +faststart out.mp4
```
Large captures (`detail@3x.png`, recordings, frames) are not committed — recapture from the prototypes:
`https://jimnidev.github.io/google-cloud-docs-capstone/pages/` and `https://jimnidev.github.io/skill-terminal-demo/`.

## fiori/ — SAP Fiori renders (Samsung ESG redesign, in progress)
UI5 Web Components v2 bundle (`npm install`, then esbuild `entry.js` → `screens/fiori.bundle.js`) and `render.js <screen> <theme> <out.png>`. The plan is to build the English Horizon screens in Figma once the Figma write connector is available.
