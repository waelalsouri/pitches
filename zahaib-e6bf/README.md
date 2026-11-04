# Zahaib Webinar Funnel · unaware mode

Pitch site for **Zahaib Sayeed (@zahaibco) · Muslim Marketing Academy**. Opens in `unaware` mode by default (`index.html`, or `?mode=funnel`).

## Page order
Hero → **Why listen to me** (credibility) → **Four things holding the $1M back** (bottlenecks) → Quick wins (7 fixes) → offer → funnel → deck → ads → emails → Book a call.

## What's inside
| # | Deliverable | Path |
|---|---|---|
| 1 | High-ticket offer · Rizq Agency Accelerator | `offer/` |
| 2 | Registration page (countdown, 3 pillars, host, gift, Stripe proof, videos) | `register/` |
| 3 | Thank-you page (prep video, calendar, Gmail reply-YES, WhatsApp) | `thank-you/` |
| 4 | Replay + working Typeform (5 Qs) → gated Calendly | `replay/` |
| 5 | Masterclass deck · 80 slides · 14 Fladlien steps | `deck/` |
| 6 | 5 video ad scripts | `ad-scripts/` |
| 7 | 7-slide carousel (swipeable phone mock) | `carousel/phone/` |
| 8 | Pre (9) · post (7) · pre-call (6) emails | `pre-webinar/` `post-webinar/` `pre-call/` |
| 9 | Quick wins · 7 prioritised fixes | `audit/` |
| — | Dossier + offer deck + gift covers | `research/` |

## Swap before sending
1. **{{HERO_VIDEO}}** · record the Loom, paste the share URL into `PITCH_CONFIG.heroEmbed` in `index.html` (hero shows an empty player until then).
2. Deck slide 22: `{{SWAP}}` early-days photo of Zahaib (none public).
3. Pre-call email 2: swap in a real student story.

## Loom beats
1. Credibility: what you've built, Abu Lahya does ~$1M/mo selling an influencer marketing agency programme (not even AI). Positioning wins.
2. The 4 bottlenecks: inconsistency, content not built for one buyer, packaging, offer positioning ($1M hidden, reads like another AI course).
3. The fix: his own mechanism (Trust Network) + the Rizq Agency Accelerator. Maths: 20.7K audience → 6/mo → $24k at $4k. $100k is the ads-on version.
4. Stress objection: one 90-min call a week, a team takes the sales calls.
5. Walk the deliverables. Ask: 20-min discovery call. **Expect two calls.**

## [CONFIRM] list
Zahaib's $1M agency revenue (timeframe) · "1,800+ helped" · guarantee terms · price band · masterclass date (set Sun 22 Nov, 7pm London) · Skool paid tier · team photo + Righteous Retreats stat (reused from the Zain pitch).

## Run / deploy
```bash
python3 -m http.server 8000
```
Drop the folder on Vercel/Netlify or into the `pitches` GitHub Pages repo. Every page is `noindex`.
