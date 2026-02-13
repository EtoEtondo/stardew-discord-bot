# Operations, Observability, and Updates

## Logging
- Python `logging` configured in code; log level via `LOG_LEVEL` env (default INFO).
- Include `DEPLOY_VERSION` in startup logs (set during deploy) to see what is running.

## Health
- No HTTP health endpoint. Use Discord connectivity as the primary signal: if slash commands respond, the bot is healthy.
- Add a simple `/health` or heartbeat command in future if needed.

## Metrics / tracing
- Not instrumented. For now rely on logs and Discord error responses. If needed, add OpenTelemetry exporters later.

## Rate limits
- Uses Discord slash commands only; Discord enforces its own limits. We don’t add extra rate limiting yet. Consider per-user/per-guild throttling if new external APIs are added.

## Updates / deploy notices
- If `DEPLOY_VERSION` and `UPDATE_CHANNEL_ID` are set, the bot posts a one-time "updated to <version>" message on startup. Marker stored at `.state/last_deploy_version.txt` (override via `DEPLOY_MARKER_PATH`).

## Environments
- **Develop**: branch `develop` builds and pushes `:test` image to GHCR for testing.
- **Release**: tags `v*` build/push `:latest` and tagged images; deploy via SSH.

## Local caches
- `.venv`, `.uv-cache`, `.ruff_cache`, `.pytest_cache`, `.mypy_cache` are local/tooling caches. They are gitignored and not used in CI; they won’t overflow CI because runners start clean each job.

## Incident basics
- Check logs first. Re-run the bot locally with the same env to reproduce.
- Roll back by redeploying a previous image tag from GHCR if needed.
