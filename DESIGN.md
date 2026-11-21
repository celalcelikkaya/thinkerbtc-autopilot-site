# Design system: "Night desk"

Everything a contributor needs to keep the ThinkerBTC Autopilot website consistent. If something
you need is not covered here, follow the closest existing pattern in `src/index.src.html` and ask
in your pull request. The previous look (v1.x) stays available in Releases and git history.

**The idea:** the page is a trading desk after hours. One instrument, the live trade chart with its
entry, stop-loss and take-profit lines, runs the width of the first screen and tells the story.
Everything else is set like the desk's printed reference sheet: a strict 12-column grid, hairline
rules instead of boxes, tabular numbers, black with market green and red. No glowing gradients, no grids of icon
cards, no floating toasts.

## 1. Brand

- Name: **ThinkerBTC** (one word). The wordmark is `THINKER` + `BTC`, with `BTC` in green, set in
  Anton with wide letter-spacing (.045em).
- Logo: `assets/logo.png`, always round (`border-radius: 50%`) with a 1px `--line2` ring.
- Personality: calm, precise, trustworthy. Energy comes from the chart and the liquid engine, never
  from decoration.

## 2. Colour

Dark theme only (`color-scheme: dark`). All colours are custom properties on `:root`; use the
tokens, never a raw hex value in a component.

| Token | Value | Use |
|---|---|---|
| `--bg` | `#08090A` | Page background (near-black, never `#000`). |
| `--bg2` | `#0D0E10` | Insets: inputs, summary tiles, the readout's chart well. |
| `--card` | `#111214` | Panels: the trade chart, setup panel, compare table, dialogs. |
| `--card2` | `#181A1D` | Raised controls: plan cards, chips, idle pills, buttons. |
| `--line` | `#232529` | Hairline rules and panel borders. |
| `--line2` | `#34373D` | Stronger rules: input borders, ghost buttons, focusable outlines. |
| `--fg` | `#EDEEF0` | Main text. |
| `--fg2` | `#A4A7AE` | Secondary text (7:1 or better on every surface). |
| `--fg3` | `#868991` | Captions, hints, axis labels (4.9:1 or better on every surface). |
| `--up` | `#16C784` | **Market green: price up, gain, take profit.** Fills and lines. |
| `--down` | `#EA3943` | **Market red: price down, loss, stop loss, errors.** Fills and lines. |
| `--up-ink` / `--down-ink` | `#2AD58E` / `#FF5A64` | **Text** for gain / loss (9:1 and 6:1 on `--bg`). |
| `--acc` | `var(--up)` | **The one action colour is the market green.** Primary buttons, the selected state, the label tick, liquid fills, focus ring, the hero accent word. |
| `--acc2` / `--acc-ink` | `#3DDC97` / `var(--up-ink)` | Lighter green; small green text. |
| `--ink` / `--on-acc` | `#03140B` | Text on green surfaces (8.6:1). |
| `--blue` | `#7896F0` | Informational only: the "SL and TP on Binance" log icon, "payment found". |

The page, the dashboard and the illustrations share one green. Liquid colours: `gold` (the
accent green; the key name is historical), `deep` (`#0E9F67`, button hover), `up`, `down`, and
`mid` (`--fg2`, for the medium margin share and the pause button).

Rules:
- Green means up and is the one action colour; red means down (loss, stop loss, errors). Red is
  never a button, a selection or decoration.
- A state that is neither up nor down stays white or grey: the current step, pending, paused, the
  profit lock line, a medium margin share. Zero P&L is neutral.
- Text on a green fill is `--ink`; text on a red fill is white.
- One accent. If you need a tint, use `color-mix(in srgb, var(--token) N%, transparent)`.
- Body and caption text at least 4.5:1, large text at least 3:1.
- Depth comes from rules and surface steps (`--bg` → `--card` → `--card2`), not shadows or glows.
  `--shadow` is only for floating things: dialogs, the dashboard toast, the phone start bar.

## 3. Type

| Role | Family | Settings | Token |
|---|---|---|---|
| Display (headlines, wordmark, panel titles, menu links) | Anton | 400 (its only weight; never set it bolder) | `--f-display` |
| Body and UI | The system font (SF Pro on Apple devices, Segoe UI / Roboto elsewhere) | 400–650 | `--f-body` |
| Numbers, prices, tickers, codes | JetBrains Mono | 500–700 + `tabular-nums` | `--f-mono` |

Anton (Vernon Adams, SIL Open Font License, `assets/fonts/Anton-OFL.txt`) is embedded in the page from
`assets/fonts/Anton-Regular.woff2`, a Latin subset (16 KB) built into the page with `{{FONT:path}}`. Display rules set
`font-synthesis: none` so the browser never fakes a bold. If a headline needs a character outside the subset,
re-subset from the full font. Text uses the platform's own font, as Apple advises: it ships optical sizing and
tracking, and nothing has to load. JetBrains Mono (`500;600;700`) loads from Google Fonts.

Scale:
- Hero headline: `clamp(48px, 5.7vw, 82px)`, line-height 1.02.
- Section heading (`.sh h2`): `clamp(34px, 4.1vw, 56px)`, line-height 1.1, max 22ch. Closing band: `clamp(40px, 5vw, 72px)`.
- Panel heading: 24px Anton, letter-spacing .01em. Card heading: system font 15.5–16.5px / 650 (Anton is for display sizes).
- Body 16px (lede 17.5px). Secondary 14–15px. Captions 12–13px.
- **Label** (`.label`): 12.5px, 600, uppercase, letter-spacing .1em, `--fg2`, with a 14×2px green
  tick before it. Labels sit in the margin column beside a heading, not stacked above it.
- Every money figure, price, percentage and count is set in JetBrains Mono.
- Headings use `text-wrap: balance`; running text stays under about 62ch.

## 4. Layout and shape

- Wrap: `--wrap` 1200px content, gutter `--gutter` `clamp(16px, 4vw, 40px)` plus safe areas.
- **12-column grid** inside sections. Section header `.sh`: label in columns 1–3, heading and lede in
  4–12. Setup: step rail 1–3, panel 4–12. Below 1024px everything stacks to one column.
- Sections: `--section` 120px top padding (84px on phones). Menu bar: `--bar-h` 56px. Ticker: `--tick-h` 40px.
- **Coin ticker** (`body > .tape`): pinned to the top of the screen on every page width, always in view while
  scrolling; a Liquid Glass strip (see Material) that content scrolls under, with a soft lower edge instead of a rule.
  Anchored headings land just below it.
- **Menu bar** (`header.bar`): floats at the bottom of the screen, centred. A Liquid Glass capsule holds the
  logo, wordmark and the section links (system font, 14px, sentence case); "Start autopilot" is its own green
  capsule of the same height at the right edge. The menu opens upward from it on a spring. The page keeps bottom padding so nothing ends under it.
- Radii (Apple-style, concentric: an inner corner is the outer one minus the padding): `--r-sm` 10px,
  `--r-ctl` 14px (inputs, tiles), `--r-card` 20px (plan cards), `--r-panel` 24px (panels, chart), `--r-band`
  28px (dialogs, sheets, closing band). Buttons, chips, tags, segmented controls and tab bars are capsules
  (`--r-pill`); round icon buttons are circles.
- Lists of facts are ruled lists (a 1px top rule per item), not cards. Nested boxes are not allowed.
- Touch targets: at least `--tap` (44px) on touch screens.
- Breakpoints: the pill shows all links from 1280px; below that it holds the logo and a menu button. Grids
  stack below 1024px. Under 600px the pill and the start block sit side by side in the centre; under 440px
  the pill shows the logo without the wordmark. Phones use full-width buttons in the content.
- No sideways page scroll at 320px and up. Wide tables scroll inside `.cmpw`.

## 4a. Material: Liquid Glass

Glass is the floating layer only: the ticker, the menu bar and its menu, dialogs, the reading sheet, the app's
toast and its tab bar, and the secondary button. Content (the trade chart, plan cards, panels, lists, the
dashboard's numbers) stays solid so it reads first. Never put glass on glass.

- One recipe, in tokens: a tint (`--glass-tint`, thicker `--glass-thick` where you read: menu, dialogs, sheet;
  `--glass-strip` for the ticker), `--glass-fx` (blur 24px, saturate 185%), a specular rim (`--glass-rim`, a 1px
  gradient border that is brightest top-left), a sheen (`--glass-sheen`) that follows a real pointer, and
  `--glass-depth` (a lit top edge plus a soft drop shadow). Add `.glass` to give something new the material.
- Motion: springs as CSS `linear()` curves. `--spring` (critically damped, response .35s, run 600ms) for things
  that appear without a gesture: the menu, dialogs. `--spring-bounce` (damping .8, run 700ms) only for the toast,
  which arrives with momentum. Reduced motion turns both into short fades.
- Fallbacks: no `backdrop-filter` support, `prefers-reduced-transparency` and `prefers-contrast: more` all turn
  the same shapes solid (`#181A1D`); higher contrast also draws a grey rim.

## 5. Components

- **Primary button** `.btn.gold`: a green capsule with a lit top edge (`::before`), `--ink` text, 48px (big 60,
  small 40). The liquid engine fills it with deeper green on hover.
- **Secondary** `.btn.ghost`: a clear glass capsule (see Material). `.btn.dark`: `--bg` with an
  outline, used for the closing hold button.
- **Trade chart** `.desk`: the hero instrument. Header row (pair, timeframe, an "Illustration" tag,
  live P&L in mono), the canvas, then the four steps as a ruled row whose top rule turns white for
  the current step and green for finished ones.
- **Readout** `.readout`: the bot's market reading (price, indicators, Long/Short liquid pills, bias
  bar). **Trade log** `.log`: the trade's four events as ruled rows; the current event is full
  strength, the rest at half.
- **Phone screens** `.phones` (section `#phone`): four WebP images of the real site in a generic phone frame
  (`assets/phones/*.webp`, 560px wide with transparent edges), four across on desktop, a swipeable snap row
  below 860px, each with a short mono label and the "Screens show illustrative data" note under the row.
  Re-take them when the screens change.
- **Illustrations** `.art` (`assets/illustrations/*.svg`, from the ThinkerBTC Autopilot SVG pack): the ivory
  Autopilot capsule, decorative (`alt=""`, `aria-hidden`), static, one per moment. Placed: in the hero,
  `.hero-art` (`hero-trade-line.svg`, Autopilot taking the trade line), top right beside the headline's short
  second line, behind the text, its line fading toward the buttons through a mask; at 680px and below it moves
  into the flow above the label, cropped to Autopilot and the start of its line. It stays an accent (at most
  400px wide) so the trade chart still leads the first screen. Also beside the Connect, Margin and Launch step headings (`.pane-h`), above "ThinkerBTC
  is trading for you", on the right of the closing band, and in the dashboard's "No open positions" and "No closed
  trades" states. Do not add them to lists, cards or every section; a new one needs a moment it actually depicts.
  The pack's orange accents were recoloured to the site green (same hue as `--up`); new artwork must use green
  `#16C784` (light `#6FE3B0`-ish highlights, dark `#0F9461`-ish shadows) in place of orange.
- **Chips** `.chip`: 38px, radius 8px, 1px inset rule; the selected chip is inverted (`--fg` ground).
- **Plan cards** `.plan`: `--card2` with a 1px rule; selected fills with green liquid; "Best value"
  has a green outline.
- **Inputs** `.inp`: 52px on `--bg2`, `--line2` rule, green focus ring, green when valid, red when not.
- **Tick boxes** `.pm`: 20px square that turns green when ticked.
- **Summary tiles** `.sum`: a single ruled grid, tiles separated by 1px lines.
- **Compare table**: ThinkerBTC column tinted green with a 2px green top rule.
- **FAQ**: two ruled columns of `details`, green `+` that turns to `×`.
- **Section menu** `.menu-b` + `.menu` (below 1280px): the 44px button in the pill opens a panel upward,
  above the bar, with large links and the start button; the page dims behind it.
- **Dialogs**: Risk Disclosure slides in from the right (up from the bottom on phones); sign-in and
  payment are centred cards. All `--card` with a 1px rule.
- **Subscriber dashboard**: same tokens and type. Left sidebar from 960px, bottom tab bar below.
  Balance in large mono, chart line in green, stats as one ruled grid, segment switch with the
  selected option in green.

## 6. Motion

- **The liquid engine stays** (`liquid(el, options)`): it is the only bubble and liquid system.
  Use it where it means something: button hover fills, plan selection, hold-to-start, the margin
  tank, the subscriber pool. Never add a second particle system, and no coin or bubble backgrounds.
- **Market glow** `.glow` (hero, closing band): the background is still light, not particles. Green
  (`--up`) glows top left, red (`--down`) bottom right, a faint green top right, all under a fine
  frosted grain (an inline SVG noise at 9%, overlay). In the hero it fades out over the lower third.
- Engine rules carried over: depth-scaled bubbles, coin bubbles pop with a ring, density comes in
  waves, labels switch to white (white on red, `--ink` on green) past about 55% fill, start buttons rest at
  about 16% fill, no rebuilding animated elements on updates.
- **Hold to confirm** `holdable()`: anything that starts, stops or pauses trading needs a 1.2s hold;
  pointer and keyboard pass the same sign-in, payment and Risk Disclosure checks.
- Interface motion tokens: `--ease-out` `cubic-bezier(.23,1,.32,1)`, `--ease-drawer`
  `cubic-bezier(.32,.72,0,1)`, `--t-press` 160ms, `--t-ui` 200ms, `--t-panel` 350ms.
- Press feedback: buttons, chips, plan cards and steps scale to .97 while pressed (hold button .985).
  Hover effects only with a real pointer (`@media (hover:hover) and (pointer:fine)`).
- No scroll-triggered fade-ins, no parallax.
- **Reduced motion**: the engine stops spawning; tapes, tickers and pulses stop; panels, dialogs and
  steps fade instead of sliding.

## 7. Writing

- English only. Plain, short sentences. Name things the way users know them.
- Buttons say exactly what happens ("Continue", "Hold to start autopilot").
- Only describe features the service really offers. Not offered today: Telegram alerts, manual trading.
- No invented testimonials, user counts, returns or performance figures. Illustrations are labelled
  as illustrations.
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

## 9. Accessibility

- Visible focus ring (`:focus-visible`, 2px green outline) on everything interactive; a skip link first.
- Every control has a label; icon-only buttons get `aria-label`.
- Dialogs: `role="dialog"`, `aria-modal`, Tab stays inside, Escape closes, focus returns to where it came from.
- Hold-to-confirm also works from the keyboard (Space or Enter held down).
- Focus follows the setup steps and dashboard tabs when the control that had it disappears.
