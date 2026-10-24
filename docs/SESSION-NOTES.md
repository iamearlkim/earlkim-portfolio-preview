# Portfolio build — session notes (Oct 21–23, 2026)

Handoff for future Claude sessions. Start with the `portfolio-case-study` / `case-study-motion` skills, then read this.

## Setup
- **Draft:** Claude Design canvas "Earl Kim Portfolio" — https://claude.ai/artifact/V9K9r3r53vV6yxDuFyAfbc (Earl edits there; always read a board before changing it).
- **Preview:** https://iamearlkim.github.io/earlkim-portfolio-preview/ (this repo; static build from the canvas).
- **Final:** earlkim.me in Framer — Earl rebuilds approved pages there.
- **Toolkit:** `tools/` in this repo (see `tools/README.md`).

## Home page
- Instrument Sans only, 5 sizes (Display / Heading / Title 22 / Body 16 / Label 13). Accent #1F3FD1.
- Case studies (7): Samsung e-commerce, Doosan, Clerro, Google Cloud docs, Samsung platforms (hub), Hanon, Financial planning & analysis (BHP + JG Summit).
- More use cases: Sugar AI, Microsoft Research Health Futures, SAP BTP, Data analytics (Emart, Samsung Sales — details [ADD]), Food delivery, Gogoro.
- Next-link chain: Ecom → Doosan → Clerro → Google Cloud → Samsung hub → Hanon → FPA → Ecom.

## Samsung hub (5 projects)
Procurement / N-ERP (done; 42.5% figure from résumé — Earl to confirm), ESG carbon footprint (done; English Fiori Horizon redesign pending), DS cloud, DX risk management (data-analytics dashboards), Shipment — the last three are stubs waiting for Earl's content.

## Google Cloud documentation (UW HCDE capstone) — current focus
Boards: v1 (first draft), v2 (from Earl's own draft), **v3 (combined — the one Earl is editing)**. Home card still links to v2; switch to v3 when approved.
v3 order: hero (video) → pull quote → 01 Context (Write the Docs / Google Cloud Next stats) → 02 Challenge → 03 Discover (first-person findings; Earl plans to hide supporting points behind a toggle — not done yet) → 04 Research (7 of 9 = 78% AI-first; P5/P6/P7 quotes) → 05 Pivot → 06 Solution: Documentation Skills (anatomy video + cards, library, Skill on doc page) → 07 Solution: Multiple entry points (console, Google Search, Gemini, docs site) → 08 Outcomes (delivered counts, UMUX-Lite/SEQ scorecard U1–U3, proposed HEART metrics) → prototype link → 09 Usability testing → 10 Iteration.

Open items:
- Anatomy cards on the page still say "Configure details"; the video uses **05 Work environment — "Which agent will run it?"** and **06 Call to execute — "How do I execute it right away?"**. Update the cards to match.
- Put the four entry-point videos into the 07 cards (replacing the grey placeholders).
- Library screenshots show "Auto-detected IAM gaps" (a dropped feature) — Earl to decide whether to blur.
- v3 is ~13,300 px tall; canvas boards max 8000 px — view in Play, or split into two boards.
- Earl's own role/contributions vs. team work: confirm before using "I" for team activities.

## Videos delivered (Google Cloud)
| Piece | Files | Spec |
|---|---|---|
| Hero | gcd-hero.mp4 / gcd-hero-alpha.webm | 1920×1200, 12 s, "/403 error" → Skills list → Skill detail |
| Anatomy of a Skill | gcd-anatomy.mp4 / gcd-anatomy-alpha.webm | 1920×1200, 30 s, gradient-outline frame, transparent outside |
| Entry 01 Console | gcd-console.mp4 / .webm | 1440², 10 s, from skill-terminal-demo prototype (names → alex / orbit-ml-417203) |
| Entry 02 Gemini | gcd-gemini.mp4 / .webm | 1440², 11.6 s, recreated Gemini app ("Hi Earl"), ends on docs page |
| Entry 03 Google Search | gcd-search.mp4 / .webm | 1440², 11.8 s, recreated Search + AI Overview, ends on docs page |
| Entry 04 Docs site | gcd-docsite.mp4 / .webm | 1440², 16 s, Home → Skills intro → Library (filter) → doc page → Skill detail (Execute pop-up) |
WebM transparency doesn't show in Safari; MP4s are the fallback.

## Other pending work
- ESG: English screens on SAP Fiori Horizon, built in Figma file `BW2LX9o5EDnfcFMSi37Squ` (new page "EN – Horizon", Samsung logo in shell bar) once the Figma write connector is available. Glossary agreed (Product Master Management, Consumption entry, Footprint calculation, …).
- Hanon redesign (stronger results and design story) — Earl to supply material.
- earlkim.me: BHP page Challenge section contains Hanon/Doosan text (bug on live site).
- Framer handoff spec doc (artifact) — sections 6–10 unfinished.

## How Earl likes to work
- Supervises; Claude drafts. Show sample frames before full video renders; change only what was asked on revisions.
- Compare versions side by side on the canvas instead of overwriting.
- Facts: verbatim quotes, P/U participant labels, exact fractions, proposed metrics labelled, no invented numbers; flag conflicts instead of picking silently.
- Uses established terminology (e.g. HEART, UMUX-Lite) with a short explanation.
