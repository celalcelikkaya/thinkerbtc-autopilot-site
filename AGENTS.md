# Notes for AI agents

You are working on the ThinkerBTC Autopilot **website** (user interface only). Read
[CONTRIBUTING.md](CONTRIBUTING.md) and [DESIGN.md](DESIGN.md) before changing anything.

## Required on every change

1. **Log it in [CHANGELOG.md](CHANGELOG.md)**, newest entry first, in the format shown there.
   Record the date, the agent and model, the person you work for (their GitHub handle), what
   changed in plain words, and the files touched. A change without a changelog entry is not
   finished.
2. **Write in English**: page text, comments, commits, pull requests and the changelog.
3. **Follow DESIGN.md**: colour tokens only, the three typefaces, the one Liquid Pill engine
   (`liquid()`), hold-to-confirm (`holdable()`) for trading actions, both themes, phone first,
   reduced motion respected.
4. **Rebuild** with `python build.py` and commit `src/index.src.html` and `index.html` together.
5. **Work through a pull request.** Don't push to `main` and don't merge your own pull request.
6. **Keep every version.** Follow [VERSIONING.md](VERSIONING.md): never force-push, reset, or delete
   tags, releases or branches; undo with a revert; `v1.0.0` is the original and is never touched.

## Never

- Add bot code, trading logic, real strategy thresholds, server addresses, keys or secrets.
- Advertise features that aren't offered (Telegram alerts and manual trading are not offered).
- Invent testimonials, statistics or performance numbers.
- Weaken the Risk Disclosure or other risk wording.
- Add a second animation system, new colours or new fonts.
- Add payment methods other than USDC on Solana (Solana Pay), or any real wallet address or key.

## Where things are

- Source: `src/index.src.html` (HTML, CSS and JavaScript in one file). Images: `assets/`.
  Output: `index.html`.
- Tokens: the `:root` blocks at the top of the `<style>` element.
- Engine: `liquid(el, options)`; hold-to-confirm: `holdable(el, state, onDone)`.
- Subscriber dashboard: `#app`, opened at `#dashboard`.
