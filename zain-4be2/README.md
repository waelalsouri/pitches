# Zain Webinar Funnel · unaware mode

Pitch site for **Zain Bilal (@_zain.bilal) · Muslim Sales Accelerator**. Opens in `unaware` mode by default (`index.html`, or `?mode=funnel` for the aware version).

## What's inside
| # | Deliverable | Path |
|---|---|---|
| 1 | High-ticket offer · Noble Circle Accelerator | `offer/` |
| 2 | Registration page (countdown, 3 pillars, host, gift, proof, videos) | `register/` |
| 3 | Thank-you page (prep video, calendar, Gmail reply-YES, WhatsApp) | `thank-you/` |
| 4 | Replay + working Typeform (5 qualifying Qs) → gated Calendly | `replay/` |
| 5 | Webinar deck · 82 slides · all 14 Fladlien steps | `deck/` |
| 6 | Static ad (IG phone mock) | `static-ad/` |
| 7 | 5 video ad scripts | `ad-scripts/` |
| 8 | 7-slide carousel (swipeable phone mock) | `carousel/phone/` |
| 9 | Pre-webinar (9) · post-webinar (7) · pre-call (6) emails | `pre-webinar/` `post-webinar/` `pre-call/` |
| 10 | Quick wins · 7 prioritised fixes | `audit/` |
| — | Research dossier + filled offer deck | `research/` |

## Swap before sending
1. **Calendly** in `index.html` → `PITCH_CONFIG.calendly` (currently the placeholder, shows a 404).
2. **{{HERO_VIDEO}}** · record the Loom, paste the share URL into `PITCH_CONFIG.heroEmbed`.
3. **Bridge beat 02** names Shelby Sapp with a visible `[CONFIRM]`. Verify or rewrite before sending.
4. Deck slides 21–22: `{{SWAP}}` photos of Zain at uni / dropout period (none public).

## Loom beats (unaware order)
1. Transition: "the biggest names in remote sales sell on a live webinar, nobody's doing it for Muslims."
2. The maths: 14,800 subs → 6 a month → $21k at $3,500. $100k is the ads-on version.
3. Stress objection: one 90-min Noble Circle call a week, setters + a closer take the sales calls.
4. Walk the deliverables, then the 7 quick wins (YouTube congruency, Shorts, IG name/highlights/pins, setters on every DM, webinar qualifies instead of the free course, Noble Circle on Skool, podcast + hijrah creator partnerships).
5. Ask: 20-min discovery call. **Expect two calls** (discovery, then the plan).

## [CONFIRM] list
Zain's $20k month, $7k week and age 22 · mentorship price today · Noble Circle platform + call day · IG followers · guarantee terms · Placement Desk partners · closer commission range (10–20%) · Shelby Sapp reference · webinar date (set to Sun 15 Nov, 7pm Sydney).

## Run / deploy
```bash
python3 -m http.server 8000
```
Drop the folder on Vercel or Netlify. Every page is `noindex`.
