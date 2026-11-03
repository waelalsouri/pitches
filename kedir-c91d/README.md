# Kedir Webinar Funnel (Dialed) · pitch site

Built with the carbon-pitch skill in **unaware mode** on the **webinar** mechanism.
Open `index.html` (it defaults to `?mode=unaware`). Serve locally with `python3 -m http.server`.

## What's inside
| Folder | Deliverable |
|---|---|
| `index.html` | Pitch site: hero, 4-beat bridge, all deliverables, Book a call |
| `offer/` | The Dialed Accelerator, the designed high-ticket offer (12 weeks, $3k to $5k band) |
| `register/` `thank-you/` `replay/` | The 3-page webinar funnel (replay has the working Typeform, then Calendly) |
| `deck/` | 79-slide live presentation, Fladlien's 14 steps, click or arrow keys |
| `static-ad/` `carousel/phone/` `ad-scripts/` | Static ad, 7-slide carousel (both in an iPhone feed), 5 video ad scripts |
| `pre-webinar/` `post-webinar/` `pre-call/` | 9, 5 and 6 email sequences |
| `research/` | Dossier, offer deck, source images, gift covers |

The 3 pillars, used word for word everywhere: **The 3-signal product filter · The one-weekend brand launch · The image-ad testing method.**

## Swaps before sending
1. `{{HERO_VIDEO}}`: record your Loom and set `heroEmbed` in `index.html` (`PITCH_CONFIG`). Beats: the problem (his price ladder) → the transition story → the maths → "that sounds like more work" → walk the deliverables.
2. `calendly` in `PITCH_CONFIG`: your real Calendly link (the placeholder shows a 404).
3. Agency branding (optional): `brand` in `PITCH_CONFIG`. Left blank on purpose.
4. `{{SWAP: prep video}}` (thank-you) and `{{SWAP: replay video}}` (replay): currently thumbnails from his channel.
5. Beat 02 uses the model in the abstract. Add your own transition case to `house/HOUSE.md` if you have one.

## [CONFIRM] before it goes to Kedir
1. **Identity:** every photo is the person with locs (often in a beanie), matched to his IG photo. Two thumbnails of someone else were excluded.
2. His revenue figures ($582K / 30 days, $412,384 / month) come from his video titles.
3. Community size: the site says 1,500+, 1,000+ and 500+ in different places.
4. "$150M+" member revenue (the site marks it "last updated Dec. 25").
5. "B" = Brandon Payton? (shown together in `kedir-brandon.jpg`).
6. Accelerator price band, guarantee and 20-seat cap are **designed**, not existing.
7. Both free gifts (3-Signal Product Sheet, Image-Ad Swipe File) need building by his team.
8. Webinar slot is mocked as Thursdays 8pm ET.

Expect **two calls** (unaware prospect): discovery first, the plan second.

## Deploy
Static site, drop the folder on Vercel or Netlify. All pages are `noindex`.
