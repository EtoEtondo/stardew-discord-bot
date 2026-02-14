# Stardew Helper

A friendly Discord bot for Stardew Valley fans. Slash commands only, minimal permissions, community-made.

## What it can do
| Command | What it does | Notes |
| --- | --- | --- |
| `/wiki <term> [lang]` | Sends an official Stardew Valley wiki link with a tidy embed. | Supports English & German; cleans up the term for you. |
| `/crop`, `/fish`, `/npc` | Quick shortcuts to the right wiki pages so players land correctly. | Locale-aware links. |
| `/tooling` | Shares trusted planning and helper tools for farmers. | Curated external links only. |

Other traits:
- Optional update pings so your server sees when the bot was refreshed.
- Privacy-friendly: no message-content intent, no data scraping—just slash commands.

## Want the bot?
- Run your own copy and invite it to your server. The step-by-step guide (local, Docker, CI/CD) lives in `docs/getting-started.md`, and Discord-side setup is in `docs/discord-setup.md`.
- If a public invite becomes available later, it will be linked here: https://github.com/etondo/stardew-discord-bot
  - And in the lightweight landing page for GitHub Pages

## Status
- Experimental and looking for feedback.
- Roadmap: polish wiki shortcuts, ship the quiz flow, add more locales.

## Branches
- Default branch: `master`; open PRs against it.
- `develop` publishes the `:test` container image for pre-release testing.

## Notes
- Fun fact and quiz cogs are planned but currently disabled to keep the MVP quiet; enable them when ready.
- The ⭐ reaction on `/wiki` responses can be toggled via `ENABLE_REACTION_FEEDBACK=false` if servers prefer fewer reactions.
- Avoid forgetting formatting: link the helper hook once with `ln -s ../../scripts/git-pre-commit.sh .git/hooks/pre-commit`.

## License
MIT. Not affiliated with or endorsed by ConcernedApe. Attribution rules and data notes are in `docs/data-licensing.md`.
