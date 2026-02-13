# Contributing to Stardew Helper

Thanks for your interest in contributing! This project is experimental and community-driven. Please help us keep it welcoming, secure, and easy to review.

## Ways to contribute
- Report bugs or suggest features via Issues.
- Improve docs (README, deployment).
- Add commands, locales, tests, tooling.
- Triage discussions and help others.

## Development setup
1) Install Python 3.12+ and `uv` (`pip install uv`).
2) Clone the repo and copy env:
   ```bash
   cp .env.example .env
   ```
3) Install deps:
   ```bash
   uv sync --dev
   ```
4) Run quality checks before pushing:
   ```bash
   uv run ruff check .
   uv run ruff format --check .
   uv run mypy .
   uv run pytest
   ```
5) Start the bot locally:
   ```bash
   uv run stardew-bot
   ```

## Branch & PR guidelines
- Fork + feature branches (e.g., `feat/quiz-engine`, `fix/wiki-term`).
- Keep PRs focused and small; include tests where possible.
- Describe changes, risks, and testing in the PR template.
- Avoid committing secrets. Tokens belong in local `.env` and GitHub Secrets.

## Coding standards
- Python 3.12+, type-hinted. Prefer readability over cleverness.
- Slash commands are the primary interface (no prefix commands).
- Follow Ruff and mypy guidance; keep line length ≤100.
- Logging via stdlib `logging`.
- For data from external wikis, keep it minimal and clearly attributed; avoid importing large wiki texts into the repo.

## Security & privacy
- No Discord tokens or API keys in code or fixtures.
- Use `.env` locally and GitHub Secrets in CI/CD.
- Avoid collecting user data; do not enable message content intent.
- If you find a vulnerability, please follow `SECURITY.md`.

## Releases
- Versioning: SemVer. Tags `vX.Y.Z` trigger the release workflow (GHCR push + deploy).
- Changelog in `CHANGELOG.md`; keep entries brief and link PRs.

## Community standards
- Be kind and constructive. Follow `CODE_OF_CONDUCT.md`.
- Non-affiliation statement: “Community-made; not affiliated with or endorsed by ConcernedApe.”
