# Design system

Everything a contributor needs to keep the ThinkerBTC Autopilot website consistent. If something
you need is not covered here, follow the closest existing pattern in `src/index.src.html` and ask
in your pull request.

## 1. Brand

- Name: **ThinkerBTC** (one word). The wordmark is written `THINKER` + `BTC`, with `BTC` in BTC orange.
- Logo: `assets/logo.png`, always shown round (`border-radius: 50%`).
- Personality: confident, lively, trustworthy. Playful motion lives inside the brand colours;
  no neon, casino or arcade looks.

## 2. Colour

All colours are CSS custom properties on `:root`. Use the tokens, never a raw hex value in a
component. Every token has a dark and a light value; both themes must work.

### Brand and signal colours (same in both themes)

| Token | Value | Use |
|---|---|---|
| `--gold` | `#F7931A` | **Bitcoin orange.** Primary buttons, liquid fills, highlights, the `BTC` in the wordmark, big headline accents. |
| `--gold2` | `#FFA940` | Top of the gold button gradient. |
| `--ink` | `#1B1300` | Text and icons on gold surfaces. |
| `--up` | `#089981` | Profit, long, success. TradingView candle green. |
| `--down` | `#F23645` | Loss, short, errors. TradingView candle red. |
| `--blue` | `#3B74FF` dark / `#0052FF` light | Informational accents only (for example the "SL and TP on Binance" note). |
| `--acc` | `#578BFA` dark / `#0052FF` light | **Subscriber dashboard only**: selected tabs, chart line, links (investor-portal look). |

Hover fill on gold buttons: `#E2761B` (deeper BTC orange).

### Text colour for gold

| Token | Dark | Light | Use |
|---|---|---|---|
| `--gold-ink` | `#F7931A` | `#B8640C` | **Small** gold text: eyebrows, links, tags, labels. The light value keeps it readable. |

Large display text (the hero headline accent, the wordmark) uses `--gold`, not `--gold-ink`.

### Neutrals

| Token | Dark | Light | Use |
|---|---|---|---|
| `--bg` | `#06070C` | `#F5F6FB` | Page background. |
| `--bg2` | `#0B0D16` | `#ECEEF6` | Inset areas: inputs, tape, summary boxes. |
| `--card` | `#11141F` | `#FFFFFF` | Cards and panels. |
| `--card2` | `#1A1E2D` | `#E8EBF4` | Raised controls on cards: chips, idle pills, plan cards. |
| `--line` | `#242A3D` | `#D9DDEA` | Borders and dividers. |
| `--fg` | `#F3F4FA` | `#0E1120` | Main text. |
| `--fg2` | `#A9AFC6` | `#4A5170` | Secondary text. |
| `--fg3` | `#6E7591` | `#7E859F` | Captions, hints, axis labels. |

`--glow` (`rgba(247,147,26,.18)` dark, `.16` light) and `--shadow` are for soft depth only.

### Rules

- Green means up or profit, red means down or loss. Never use them for anything else.
- Don't introduce new hues. If you need a tint, use `color-mix(in srgb, var(--token) N%, transparent)`.
- Check contrast on both themes. Small text on light backgrounds must not use `--gold`.

## 3. Type

| Role | Family | Weights | Token |
|---|---|---|---|
| Display (headings, wordmark, big numbers on the site) | Unbounded | 600 / 700 / 800 | `--f-display` |
| Body and UI | Inter | 400–800 (dashboard numbers 900) | `--f-body` |
| Numbers, prices, codes | JetBrains Mono | 500 / 700 | `--f-mono` + `font-variant-numeric: tabular-nums` |

Fonts load from Google Fonts with system fallbacks. Scale in use:

- Hero headline: `clamp(36px, 5.6vw, 66px)`, weight 800, line-height 1.02.
- Section heading (`.sh h2`): `clamp(28px, 3.6vw, 44px)`, weight 800.
- Panel heading: 22px / 700. Card heading: 16–18px / 700.
- Body: 16px (lead 17–19px). Secondary: 14–15px. Captions: 12–13px.
- Eyebrow: 12px, weight 600, uppercase, letter-spacing .14em, `--gold-ink`.
- Headings use `text-wrap: balance`; keep running text under about 65 characters wide.

## 4. Layout and shape

- Content width: `.wrap` max 1180px, side gutter `max(16px, env(safe-area-inset-*))`.
- Sections: 96px top padding; the sticky bar is 68px high.
- Radii: buttons and chips `999px`; pills 16px; cards 22–28px; panels 28px; big bands 36px.
- Use flex/grid `gap`, not margins between siblings.
- Must work at phone width (375px) with no sideways page scroll. Wide tables scroll inside their
  own container.
- Safe areas: sticky things use `env(safe-area-inset-*)`.

## 5. Components

- **Primary button** `.btn.gold`: gold gradient, `--ink` text, pill shape, height 52 (big 64,
  small 40). Hover fills it with deeper orange liquid.
- **Secondary button** `.btn.ghost`: transparent with a `--line` outline.
- **Chips** `.chip`: 38px pills on `--card2`; the selected chip is inverted (`--fg` background).
- **Plan cards** `.plan`: `--card2`; the selected card fills with gold liquid; "Best value" has a
  gold outline.
- **Inputs** `.inp`: 54px high on `--bg2`, gold focus ring, green ring when valid, red when invalid.
- **Tick boxes** `.pm`: rounded square that turns green when ticked.
- **Toasts**: small cards with a 30px icon tile tinted by meaning (green, gold or blue).
- **Side panel** (Risk Disclosure): slides in from the right on desktop, up from the bottom on phones.
- **Subscriber dashboard**: follows the investor-portal look (greeting + LIVE status, coin tape,
  big centred balance, area chart in `--acc`, status strip, Positions / Performance / History
  segment, three stat tiles, position rows). Bottom tab bar on phones, left sidebar from 960px.

## 6. Motion: the Liquid Pill engine

All liquid and bubble motion comes from **one engine**: `liquid(element, options)`. Never add a
second bubble or particle system; extend the engine instead, so everything moves the same way.

- **Liquid**: fills left to right with three wave layers (colour back wave, white sheen, main body).
  Optional foam at the front edge.
- **Bubbles**: a depth value `d = random^1.4` decides everything: most bubbles are far away (small,
  slow, faint); a few are close (big, fast, sharp).
  - Coin bubble diameter: `11 + d^1.8 × 27` px, times the container scale.
  - Plain bubble diameter: `2 + d^2.2 × 9` px (empty cards: `2 + d^1.5 × 15`).
  - Coin bubbles are glass: bright spot top-left, clear middle, light rim, coin logo inside at 62%
    that gently wobbles. They rise with a sway, grow slightly and **pop at a random height** with a
    ring, the coin popping out and small droplets.
  - **Density comes in waves**: every 1.4–6 s the rate switches between almost still, normal and busy.
- **Rest states**:
  - Start buttons ("Hold to start autopilot") rest at about 16% fill with foam, plain bubbles and
    coin bubbles. They never drain to empty in view.
  - Selected plan card: gold fill, **coin bubbles only**.
  - Unselected plan cards: no liquid, **clear glass bubbles only** (grey rim, white glint).
  - Background fields (hero, final band): no liquid, coin and plain bubbles, lowered opacity.
- **Hold to confirm** `holdable()`: anything that starts, stops or pauses trading needs a 1.2 s hold.
  The liquid follows the hold; releasing early drains it; completing it bursts bubbles.
- Liquid labels switch to white (or `--ink` on gold) once the fill passes about 55%.
- **Reduced motion**: with `prefers-reduced-motion` on, the engine stops spawning and nothing loops.
- **No jumps**: don't rebuild animated elements on updates; change text in place.

## 7. Writing

- English only. Plain, short sentences. Name things the way users know them.
- Buttons say exactly what happens ("Continue", "Hold to start autopilot").
- Only describe features the service really offers. Not offered today: Telegram alerts, manual
  trading.
- No invented testimonials, user counts, returns or performance figures. Illustrations must look
  like illustrations.
- Competitor facts need the company's own page as the source and a "checked on" date.
- Risk wording stays visible and is never softened.

## 8. Payments

- **One method: USDC on the Solana network, through Solana Pay.**
- Each order gets a fresh random **reference** public key, put in the payment QR
  (`solana:<receiver>?amount=<price>&spl-token=<USDC mint>&reference=<ref>&label=ThinkerBTC&message=<plan>&memo=<order>`).
  The server finds the transaction by that reference, checks amount, token and receiver, and
  activates the plan, so payments are matched to users automatically.
- USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. The receiving wallet is set by the
  owner on the server; the UI only shows a placeholder.
- The payment screen shows: amount, plan, order id, QR (white tile), status
  (waiting → found → paid), network, token, a shortened reference, "Open in wallet" and "Copy
  payment link".
- Launching the bot requires sign-in (Google or Apple) and a paid plan.

## 9. Live numbers

- The subscriber pool reads the real count from `GET /api/public/stats` (`{"subscribers": n}`),
  every 15 s and when the tab gets focus. A rise pours more liquid, bursts coins and rolls the
  number (odometer). The fill shows progress to the next milestone (100, 250, 500, 1,000 …).
- Until the endpoint answers, it shows the empty state ("Be one of the first") at the resting level.
- **Never hard-code or invent a count.**

## 10. Accessibility

- Visible focus ring (`:focus-visible`, gold outline) on everything interactive.
- Every control has a label; icon-only buttons get `aria-label`.
- Dialogs: `role="dialog"`, `aria-modal`, Escape closes, focus returns to where it came from.
- Hold-to-confirm also works from the keyboard (Space or Enter held down).
