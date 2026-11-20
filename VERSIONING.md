# Versions and backups

Every version of the website must stay available, so the owner can compare versions and switch
back at any time. These rules protect that.

## Rules for every contributor

1. **Never rewrite or delete history.** No force-push, no `git reset` on shared branches, no
   deleting tags, releases or merged branches. To undo something, open a pull request that reverts
   it (`git revert`).
2. **Never change a released version.** A tag points at one exact version forever.
3. **Every merged pull request becomes a release.** After merging, the owner (or the agent the
   owner asks) creates a tag and a GitHub Release:
   - Tag: `vMAJOR.MINOR.PATCH`
     - `PATCH` (v1.0.1): fixes and small visual tweaks.
     - `MINOR` (v1.1.0): new sections, features or flows.
     - `MAJOR` (v2.0.0): redesigns or changes to the overall look.
   - Release title: the version and a short name, for example `v1.1.0 — Solana Pay receipts`.
   - Release notes: the CHANGELOG entry.
   - Attach that version's built `index.html` to the release, so it can be opened without Git.
4. **Put the version in your CHANGELOG entry** (the next version number your change will get).
5. **Before a big redesign**, make sure the current version is released first, so the old look is
   one click away.

## The original

`v1.0.0` is the original version of the site. It is never edited, moved or deleted.

## Switching between versions

- **Look at a version**: open the repository's **Releases** page, pick the version and download its
  `index.html`, then open it in a browser.
- **Compare two versions**: on GitHub, open
  `https://github.com/celalcelikkaya/thinkerbtc-autopilot-site/compare/v1.0.0...v1.1.0`
  (any two tags).
- **Work from an older version**: `git checkout -b my-branch v1.0.0`.
- **Make an older version current again**: open a pull request that restores it (revert the later
  changes, or copy the older `src/index.src.html` back), then release it as a new version. The
  newer versions stay in history and in Releases.
