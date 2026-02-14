# Architecture

Short map of where things live and what they do.

## Top-level
- `src/`: bot code.
- `tests/`: pytest suites for config, i18n, wiki service, update notifier.
- `docs/`: how-tos (Discord setup, deployment, data licensing, getting started, ops).
- `public/`: static landing page assets for GitHub/GitLab Pages.
- `docker-compose.yml`: run or deploy via Docker.
- `Dockerfile`: production image build.
- `pyproject.toml`: project metadata, dependencies, lint/test config.
- `uv.lock`: locked dependency versions for reproducible installs.
- `.env.example`: sample configuration.
- `.github/`: CI/CD, issue/PR templates, Dependabot.

## src/
- `stardew_bot/bot.py`: bot client, loads cogs, syncs commands (global + optional guild for faster dev).
- `stardew_bot/config.py`: env settings via `pydantic-settings`.
- `stardew_bot/i18n.py` + `locales/`: translations (JSON per locale).
- `stardew_bot/commands/`: slash command cogs (`wiki`, `tooling`, `npc`, `crop`, `fish`; `funfact` + `quiz` are placeholders and stay unloaded by default).
- `stardew_bot/services/`: helpers (wiki URL builder, update notifier; future stubs for news/social/steam).
- `stardew_bot/__main__.py`: entrypoint for `uv run stardew-bot`.

## docs/
- `getting-started.md`: run/test/deploy quickstart (local, Docker, CI/CD overview).
- `discord-setup.md`: create app/bot, permissions, invite link.
- `deployment.md`: prod deployment (Oracle VM) steps.
- `data-licensing.md`: attribution rules.
- `ops.md`: observability, health, updates (see below).
- `marketing-checklist.md`: launch/readiness list.

## public/
Static one-pager for Pages with CTA + command list; uses `style.css` and `script.js`.

## Docker & Compose
- Compose pulls or builds image `ghcr.io/<owner>/stardew-discord-bot:latest` (override `IMAGE`).
- Volume `.state/` keeps deploy markers; env via `.env`.

## CI/CD overview
- `ci.yml`: lint/format/mypy/pytest + Docker build check on pushes/PRs; pushes `:test` image to GHCR on `develop` branch.
- `release.yml`: same checks on tags `v*`, then build/push `:latest` + tag, deploy via SSH.

## Notes on branches
- `develop`: publishes `:test` image for pre-release testing.
- `master`: main line; releases happen from tags `v*`.

## Future ideas (kept short)
- Quiz engine, more locales, small helper views (buttons/selects).
