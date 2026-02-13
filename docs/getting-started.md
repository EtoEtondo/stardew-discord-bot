# Getting Started

Practical setup notes for running and testing Stardew Helper on your own Discord server.

## Requirements
- Python 3.12+ (system or virtual env)
- `uv` as package/env manager is recommended; fallback to `python -m venv` works too
- Discord Application + Bot token (no privileged intents needed)
- Optional: Docker + docker compose for containerized runs

## Local quickstart
1) Copy the example env file and fill in your secrets:
   ```bash
   cp .env.example .env
   # set DISCORD_TOKEN, optional GUILD_ID, UPDATE_CHANNEL_ID
   ```
2) Install dependencies (dev tools included):
   ```bash
   uv sync --dev
   # or: python -m venv .venv && source .venv/bin/activate && pip install uv && uv sync --dev
   ```
3) Run the bot locally:
   ```bash
   uv run stardew-bot
   ```
4) Command sync speed-up: set `GUILD_ID` to a single server ID while you iterate. Commands register instantly in that guild and still sync globally afterward; remove it when you want a wide rollout.

## Tests and linting
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest
```
These are the same checks that run in CI.

## Docker / compose
- `docker compose up --build` builds from the repo and tags it as `ghcr.io/<owner>/stardew-discord-bot:latest` unless you override `IMAGE`.
- The `image:` line also allows pulling a prebuilt image (useful in production). Push rights stay limited to collaborators with `packages:write` on GitHub; others cannot push to your GHCR namespace.
- Environment comes from `.env`; `DEPLOY_VERSION` is passed through for deploy notifications. State is stored in `./.state`.

## CI/CD overview
- `.github/workflows/ci.yml` runs Ruff lint + format check, mypy, and pytest on pushes/PRs to `master`, then performs a Docker build check.
- `.github/workflows/release.yml` repeats quality checks on tags `v*`, builds and pushes the GHCR image, and deploys via SSH.

## Tech stack
- Python 3.12, `discord.py`
- Configuration via `pydantic-settings` and `.env`
- Tooling: Ruff, mypy, pytest, Docker; package/build backend via `hatchling`

## Data and licensing
- Code is MIT-licensed (see `LICENSE`).
- No Stardew wiki text is bundled; we only link out. Attribution notes live in `docs/data-licensing.md`.

## More documentation
- Discord app setup: `docs/discord-setup.md`
- Deployment notes: `docs/deployment.md`
- Architecture overview: `docs/architecture.md`
- Operations/observability: `docs/ops.md`
