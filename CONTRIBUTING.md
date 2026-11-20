# Contributing

Thanks for helping with the ThinkerBTC Autopilot website. This repository is the **user interface
only**, and contributions are about the interface: layout, visuals, animation, copy and
accessibility.

Before you start, read [DESIGN.md](DESIGN.md). It has the colours, type, components and motion
rules every change must follow.

## The one rule: log every change and who made it

Every pull request adds an entry at the top of [CHANGELOG.md](CHANGELOG.md). No entry, no merge.

Each entry records:

- **Date** (YYYY-MM-DD)
- **Contributor**: your GitHub handle. If an AI agent made the change, name the agent and model
  *and* the person who asked for it, for example `Claude Code (Claude Opus 5.5) for @someone`.
- **What changed**: one or two plain sentences a non-developer can follow.
- **Files**: the files you touched.
- **Pull request**: the PR link or number.

## Versions and backups

Every version must stay available. Read [VERSIONING.md](VERSIONING.md): never rewrite or delete
history, tags or releases; undo with a revert pull request; every merge becomes a numbered release,
and `v1.0.0` (the original) is never touched.

## Workflow

1. Fork the repository and create a branch: `feature/<short-name>` or `fix/<short-name>`.
2. Change `src/index.src.html` (and `assets/` if you add images).
3. Run `python build.py`, then check `index.html` in a browser:
   - phone width (about 375 px) and desktop width,
   - dark and light mode,
   - with reduced motion turned on.
4. Add your CHANGELOG entry, including the version your change will be released as.
5. Open a pull request against `main`. Say what you changed and why, and add before/after
   screenshots for visual changes.
6. The owner reviews and merges. Don't merge your own pull request.

## Language

Everything is in **English**: page text, code comments, commit messages, pull requests and the
changelog.

## What we want from you

- Changes that follow [DESIGN.md](DESIGN.md): tokens for every colour, the three typefaces, the
  Liquid Pill engine for every liquid or bubble effect, hold-to-confirm for trading actions.
- Small, focused pull requests, one topic each.
- Pages that work on phones first and in both themes.
- Accessible controls: labels, focus states, keyboard support.

## What we don't accept

- **Bot internals**: strategy logic, real thresholds, server addresses, API keys or secrets.
  Trades shown on the site are illustrations.
- **Features that aren't offered** (today: Telegram alerts and manual trading).
- **Fake proof**: invented testimonials, user counts, returns or performance claims.
- **Unsourced competitor claims**: use the company's own page and update the "checked on" date.
- **Weaker risk wording**: the Risk Disclosure and footer warning stay; legal text changes need the
  owner's approval.
- **Sending or storing anything** from the API key fields in this UI.
- **Other payment methods.** Payment is USDC on Solana through Solana Pay only, with a unique
  `reference` per order (see DESIGN.md). Never put a real wallet address or keys in this repository.
- **A second animation system**, new colours outside the tokens, or new fonts.
- New external scripts or stylesheets. Allowed today: Google Fonts and `qrcode-generator` 1.4.4
  from cdnjs (for the Solana Pay QR). Everything else stays inside the one file.
