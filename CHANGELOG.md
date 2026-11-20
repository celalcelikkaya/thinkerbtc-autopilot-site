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

## 2026-11-20 — Binance settings in the Connect step
- Version: v1.1.0
- Contributor: Claude Code (Claude Opus 5.5) for @celalcelikkaya
- What changed: The Connect step now asks users to set position mode to One-way and keep USDT in the
  USDⓈ-M Futures wallet (both required), recommends Single-Asset mode, and explains that margin type
  and leverage are set by the bot. Added a matching FAQ answer. Gold buttons (Start autopilot,
  Continue and others) now rest with the same foam, plain bubbles and coin bubbles as the other buttons,
  and fill more slowly on hover (1.4 s); plan cards fill in 0.9 s.
- Files: src/index.src.html, index.html, DESIGN.md, CHANGELOG.md
- Pull request: see the v1.1.0 release

## 2026-11-20 — Initial import
- Version: v1.0.0 (the original)
- Contributor: Claude Code (Claude Opus 5.5) for @celalcelikkaya
- What changed: First version of the website and the contributor documentation.
- Files: all
- Pull request: none (initial commit)
