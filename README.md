# Stardew Helper (stardew-discord-bot)

Community-made, experimental Discord bot for Stardew Valley. Slash commands only, minimal permissions, open source. Built with human + AI pair-programming. Not affiliated with or endorsed by ConcernedApe.

## Features (MVP)
- Slash commands: `/help`, `/wiki <term> [lang]`, `/tooling`, `/funfact`, `/quiz` (placeholder), `/npc`, `/crop`, `/fish`
- i18n with English + German (`locales/` JSON, fallback to `en`)
- Wiki + resource links only (no scraping, no bundled wiki data). Terms are title-cased before linking for better hits.
- Update notification hook (posts “✅ Updated to …” when `DEPLOY_VERSION` + `UPDATE_CHANNEL_ID` are set)
- Docker + GitHub Actions CI (lint, type-check, test, docker build)

## Tech Stack (end-user focused)
- Python 3.12+, `uv` package/env manager
- `discord.py` 2.x (slash commands / interactions)
- Config via `pydantic-settings` + `.env`
- Tooling: Ruff (lint+format), mypy, pytest, docker
- Built with AI assistance plus manual review

## Requirements
- Python 3.12+
- Discord Application & Bot token with permissions:
  - Privileged intents: none (no message content intent)
  - Required permissions: Send Messages, Embed Links, Read Message History (optional), Use Application Commands
- `uv` is recommended; if system Python is “externally managed” (PEP 668), use a venv or `pipx install uv`.

## Quickstart (local, no server needed)
1) Clone repo, copy env (never commit tokens):
   ```bash
   cp .env.example .env
   # fill DISCORD_TOKEN, optional GUILD_ID, UPDATE_CHANNEL_ID
   ```
2) Install deps (dev):
   ```bash
   # if uv is installed
   uv sync --dev
   # if uv is not installed and system Python is locked:
   python3 -m venv .venv && source .venv/bin/activate
   pip install uv
   uv sync --dev
   ```
3) Run bot:
   ```bash
   uv run stardew-bot
   ```
4) Optional: limit command sync to a dev guild by setting `GUILD_ID` (faster iteration).

## Testing (local)
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest
```
If `uv` is unavailable, activate your venv and run the tools via `python -m`.

## Docker / Compose
Build + run locally:
```bash
docker compose up --build
```
Runtime env comes from `.env`. Image name defaults to `ghcr.io/<owner>/stardew-discord-bot:latest` (override with `IMAGE=`).
GHCR owner default in compose is `etondo`; override with `GHCR_OWNER=myuser` if you fork.

## CI/CD
- `.github/workflows/ci.yml`: lint (ruff), format check, mypy, pytest, docker build check on PRs/push to `main`.
- `.github/workflows/release.yml`: on tags `v*` -> repeat quality checks, build & push image to GHCR, deploy to Oracle VM via SSH + `docker compose pull/up`.
- Secrets expected: `DISCORD_TOKEN` (not stored in repo), `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`, optional `DEPLOY_PORT`.

## Configuration (.env)
- `DISCORD_TOKEN` (required)
- `GUILD_ID` (optional, speeds up command sync for dev servers)
- `UPDATE_CHANNEL_ID` (optional deploy notice target)
- `DEFAULT_LOCALE` (`en`/`de`, fallback `en`)
- `LOG_LEVEL` (`INFO` default)
- `DEPLOY_VERSION` (set during deploy for notification)

## Architecture
- `src/stardew_bot/bot.py`: bot client + cog wiring
- `commands/`: slash command cogs
- `services/wiki_service.py`: build wiki URLs (no scraping)
- `services/update_notifier.py`: startup deploy notice
- `i18n.py` + `locales/`: simple JSON-based translations
- `config.py`: env handling via `pydantic-settings`
- `utils/logging.py`: basic logging setup

### How it works (user-facing)
- Commands build and return links/short responses using the official Stardew wiki domains (en/de). Inputs are normalized to title case before linking. If the wiki page does not exist, the link may 404; no scraping is performed. Empty inputs are rejected politely.
- `/funfact` pulls from a small in-repo list (see locales). `/quiz` is a placeholder for now.
- Update notifications: if `DEPLOY_VERSION` and `UPDATE_CHANNEL_ID` are set, the bot posts “✅ Updated to …” in that channel on startup.

## Data & Licensing
- Code: MIT (see `LICENSE`).
- No bundled Stardew wiki text. External data goes to `data_external/` (future) with separate attribution. Wiki content is licensed separately (see https://stardewvalleywiki.com/Stardew_Valley_Wiki:Copyrights) and is not shipped here.
- External tools/APIs linked from commands keep their own licenses/ToS; users should review them.
- Stardew Helper is community-made; **not affiliated with or endorsed by ConcernedApe**.

## Contribution
- See `CONTRIBUTING.md` + `CODE_OF_CONDUCT.md`.
- Preferred flow: fork -> branch -> PR. Lint/test before pushing.
- Issues/Discussions enabled for roadmap + feedback.

## Deployment (Oracle VM outline)
- Target: Oracle Cloud Always Free VM with Docker + docker compose.
- Expected server path: `/opt/stardew-bot` containing `docker-compose.yml` + `.env`.
- GHCR image: `ghcr.io/<owner>/stardew-discord-bot:<tag>` (+ `latest`).
- Deploy command (used in workflow): `cd /opt/stardew-bot && docker compose pull && DEPLOY_VERSION=<tag> docker compose up -d`
- Detailed guides: `docs/oracle-setup.md`, `docs/deployment.md`, `docs/discord-setup.md`.

## Marketing (snapshot)
See `docs/marketing-checklist.md` for a phased checklist (foundation → visibility → community → growth).

## Status
Experimental / WIP. Roadmap: richer quiz engine, more locales, button-based detail views, top.gg listing, marketing checklist.
