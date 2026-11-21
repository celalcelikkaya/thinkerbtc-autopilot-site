# Changelog

Every change to this repository is logged here, newest first, with who made it.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules.

Format:

```
## YYYY-MM-DD — short title
- Version: vX.Y.Z (see VERSIONING.md)
- Contributor: @github-handle  (AI agents: "Agent (model) for @handle")
- What changed: one or two plain sentences.
- Files: list of files
- Pull request: #number
```

---

## 2026-11-20 — Redesign: "Night desk"
- Version: v2.0.0 (see VERSIONING.md; release v1.1.0 first so the previous look stays one click away)
- Contributor: Claude Code (Claude Opus 5.5) for @sharmanathan96-max
- What changed: A new look with every word of content kept. The first screen is now the headline and one
  instrument, the trade chart with its entry, SL, TP and profit lock, with the four steps beneath it as a
  ruled row that lights up as the trade moves. Sections sit on a 12-column grid with the label in the margin;
  facts are ruled lists instead of icon cards; the hero phone became a market readout beside a trade log.
  Black dark theme only with the two market colours (the dashboard's blue is gone), the system font for text
  and JetBrains Mono for every number; no glows. The liquid and bubble
  engine stays where it means something, with the background bubble fields made faint. The trade chart now
  carries an "Illustration" tag. DESIGN.md, AGENTS.md, CONTRIBUTING.md and the README page map describe the
  new system.
  The coin ticker is pinned to the top of the screen and stays in view while scrolling; the menu became a floating
  bar centred at the bottom (logo and links in a pill, "Start autopilot" as its own block), and the separate phone
  start bar is retired because the floating bar carries that button.
  A new "On your phone" section after "What the bot does" shows four phone screens (choose a plan, a trade, Solana
  Pay, the dashboard), embedded as WebP through a new `{{IMG:path}}` placeholder in build.py, with a note that the
  screens show illustrative data.
  Headlines, the wordmark and the menu links are set in Anton (SIL Open Font License), embedded as a 16 KB Latin
  subset through a new `{{FONT:path}}` placeholder, at its real weight with no faked bold.
  The phone images were re-taken to match.
  Illustrations from the ThinkerBTC Autopilot SVG pack mark key moments: beside the Connect, Margin and Launch
  steps, above "ThinkerBTC is trading for you" (replacing the green tick), on the closing band, and in the
  dashboard's empty positions and history states. A new hero illustration, Autopilot taking the trade
  line (made for this page, in the pack's style), sits top right beside the headline and above the label on
  phones, small enough that the trade chart still leads. They are all decorative.
  Colour: green is the price going up and also the one action colour (buttons, selection, focus, the hero word,
  the wordmark's BTC); red is the price going down (losses, stop loss, errors) and is never a button. States that
  are neither stay white or grey: the current step, pending, paused, the trade chart's profit lock line, the medium
  margin share. Text on green is dark, text on red white; all text passes contrast. The illustrations' orange
  accents are recoloured green, and the phone images and mockups were taken in the new colours. On the trade chart
  the Entry tag hides while the lock's tag sits on top of it.
  Apple design language: the floating layer (ticker, menu bar and menu, dialogs, reading sheet, the app's toast
  and tab bar, the secondary button) is Liquid Glass, a blurred, tinted material with a lit rim and a sheen that
  follows the pointer, while content stays solid. Buttons, chips, segmented controls and tab bars are capsules,
  corners are larger and concentric, the app's tab bar floats, text uses the system font (SF Pro on Apple
  devices; Archivo no longer loads), and the menu, dialogs and toast arrive on springs. Reduced transparency,
  higher contrast and browsers without backdrop blur get the same shapes solid.
  The animated coin bubbles behind the hero and the closing band are replaced by a still "market glow": green
  light top left and red light bottom right under a fine frosted grain, drawn in CSS (no canvas, nothing moving).
  "Get started" is rebuilt as a checkout: the four steps became a glass capsule beside the heading (the empty step
  column is gone), the plans a list where the chosen one is outlined in green instead of filled, and a glass "Your
  autopilot" receipt sits beside each step, filling in as you choose and showing what is due or paid. The
  hold-to-start button moved into the receipt and stays locked until the last step and the Risk Disclosure; the
  old four-box summary on the Launch step is gone. Headings no longer show a focus ring when a step opens.
  Scrolling feels fluid: mouse-wheel notches glide as one smooth movement (trackpads and touch keep their own
  momentum), the hero eases in once on load, and each section's content rises softly into place as it scrolls into
  view, tied to the scroll so it never stays hidden. Reduced motion turns all of it off.
  The page now opens on a face: the client's interactive ASCII portrait, recoloured to green characters on black
  (brightest where the light hits) over a soft green and red glow. It fills the first screen under the ticker and
  turns to follow the pointer; a "Scroll" cue leads to the hero, which now carries the id `intro`. Its head was
  rebuilt as an original android: armour plates with seams and a crest, slanted eye slits that glow, a vent grille,
  sensor discs, a segmented neck and plated shoulders.
- Files: src/index.src.html, index.html, build.py, assets/phones/*.webp, assets/fonts/Anton-Regular.woff2,
  assets/fonts/Anton-OFL.txt, assets/illustrations/*.svg, mockups/*.png, DESIGN.md, AGENTS.md,
  CONTRIBUTING.md, README.md, CHANGELOG.md
- Pull request: to be opened

## 2026-11-20 — Responsive polish: one design from phone to desktop
- Version: v1.1.0 (see VERSIONING.md)
- Contributor: Claude Code (Claude Opus 5.5) for @sharmanathan96-max
- What changed: Below 1080px the section links move into a menu button with a panel, so tablets no longer squeeze
  the bar and phones can reach every section. Caption grey, small gold text and small green/red figures now pass
  contrast in both themes (new `--up-ink`, `--down-ink` and `--on-acc` tokens, darker light-theme shades of the same
  hues). Every button, chip, plan card and step answers a press; touch targets are at least 44px (FAQ rows,
  dashboard "See all" and "Hide amounts", close buttons); the desktop hero headline gets more width. The dashboard's
  idle notification no longer peeks in at the top, the subscriber pool only says "Live" once the real count has
  loaded, and reduced motion now stops tapes, tickers and pulses and turns slides into fades. New tokens for radii,
  layout and motion are documented in DESIGN.md. Accessibility: holding Space or Enter on the start button now
  passes the same sign-in and payment checks as a mouse hold; Tab stays inside open dialogs; a skip link leads to
  the content; focus follows the setup steps and dashboard tabs instead of dropping to the page; key errors are
  announced and tied to their fields; the hidden phone bar is out of the tab order. Also: the phone step strip
  scrolls to the current step and lands below the bar, wizard buttons stack full width on phones, the subscriber
  pool's labels sit on its gold liquid in ink, the "Withdrawals off" tick says plainly what it confirms, zero P&L
  is neutral instead of green, and "up to 1 trades" reads "up to 1 trade". `index.html` is rebuilt from the current source, which also
  brings the Subscribers section and its menu link into the built page (the committed build predated them).
- Files: src/index.src.html, index.html, DESIGN.md, CHANGELOG.md
- Pull request: to be opened

## 2026-11-20 — Initial import
- Version: v1.0.0 (the original)
- Contributor: Claude Code (Claude Opus 5.5) for @celalcelikkaya
- What changed: First version of the website and the contributor documentation.
- Files: all
- Pull request: none (initial commit)
