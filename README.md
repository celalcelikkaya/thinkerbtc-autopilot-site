# ThinkerBTC Autopilot — website

The subscription website for ThinkerBTC Autopilot: a landing page, a four-step sign-up
(plan → sign in with Google or Apple → pay in USDC on Solana → Binance API keys → margin per trade → hold to start), a comparison with other trading bots,
a risk disclosure, and the subscriber dashboard that opens after launch.

**This repository is the user interface only.** It contains no bot code, no trading strategy,
no server details and no keys. Everything the page shows about trades (positions, P&L, the trade
chart, the dashboard) is an illustration that runs in the browser.

## Run it

Open `index.html` in a browser. It is one self-contained file.

Or serve it locally:

```bash
python -m http.server 8000
```

then open http://localhost:8000.

## Change it

1. Edit `src/index.src.html` (HTML, CSS and JavaScript all live in this one file).
2. Images go in `assets/` (`assets/logo.png`; coin icons in `assets/coins/<SYMBOL>.svg`).
3. Rebuild the page:

   ```bash
   python build.py
   ```

4. Commit both `src/index.src.html` and the rebuilt `index.html`.

Placeholders in the source: `{{LOGO}}`, `{{COIN:BTC}}` (any coin file name) and `{{COINS}}`.

## Page map

| Section | Selector | Notes |
|---|---|---|
| Top bar | `.bar` | Menu and gold start button. Becomes "My dashboard" once a user has launched. |
| Hero | `.hero` | Coin bubbles, a phone showing the bot's Long/Short reading, and a trade story. |
| What the bot does | `#bot` | Animated trade chart (illustrative values) and four steps. |
| Set up in four steps | `#setup` | Plan, Connect (keys can be skipped), Margin, Launch (Risk Disclosure must be accepted). |
| Compare | `#compare` | Competitor facts with sources and the date they were checked. |
| Subscribers | `#members` | Live subscriber count in a liquid pool; syncs from `GET /api/public/stats` → `{"subscribers": n}` every 15 s. |
| Questions | `#faq` | |
| Final band | `.final` | Hold-to-start button. |
| Sign in | `#si` | Google or Apple only (no password). Opens after the Plan step and before launch. |
| Payment | `#pay` | Solana Pay QR for USDC with a unique reference per order; status updates when paid. |
| Risk Disclosure | `#rd` | Side panel; its tick box syncs with the Launch step. |
| Subscriber dashboard | `#app` (`#dashboard`) | Investor-portal look: Dashboard, Positions, Performance, History, Account. |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [DESIGN.md](DESIGN.md) (colours, type, components, motion) first. **Every change must be logged in
[CHANGELOG.md](CHANGELOG.md) together with who made it.** AI agents: also read [AGENTS.md](AGENTS.md).

## Versions

Every merged change is released as a numbered version (see [VERSIONING.md](VERSIONING.md)).
`v1.0.0` is the original. Open **Releases** to see or download any version.
