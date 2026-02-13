# Deployment & CI/CD

This project ships via GitHub Actions to an Oracle VM using Docker and GHCR.

## GHCR image
- Name: `ghcr.io/<owner>/stardew-discord-bot` (compose default owner: `etondo`; override with `GHCR_OWNER` or `IMAGE`)
- Tags: `latest` and `vX.Y.Z` (from git tags)

## GitHub Actions
- `ci.yml` runs on PR/push to `master`: lint, format check, mypy, pytest, docker build.
- `release.yml` runs on tags `v*`: repeats quality checks, builds & pushes image, then deploys via SSH.
- Default branch: `master` (update repo protection accordingly).

### Required secrets
- `DISCORD_TOKEN` (if you run integration tests that need it)
- `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY` (private SSH key), optional `DEPLOY_PORT`
- No secrets are stored in the repository.

### Deploy step (release workflow)
Uses `appleboy/ssh-action` to run on the VM:
```bash
cd /opt/stardew-bot
docker compose pull
DEPLOY_VERSION=<git tag> docker compose up -d
```
`DEPLOY_VERSION` is passed into the container for the in-bot deploy notification.
State for deploy notifications is persisted via the `.state` volume (default mapping in `docker-compose.yml`); override with `DEPLOY_MARKER_PATH` if needed.

## Manual deployment
```bash
IMAGE=ghcr.io/<owner>/stardew-discord-bot:latest
docker pull $IMAGE
DEPLOY_VERSION=$(git describe --tags --always || echo "manual") IMAGE=$IMAGE docker compose up -d
# Marker path is configurable via DEPLOY_MARKER_PATH (default .state/last_deploy_version.txt)
```

## Local docker build for testing
```bash
docker build -t stardew-helper:test .
DISCORD_TOKEN=... docker run --rm -it stardew-helper:test
```

## Repository settings checklist
- Enable Actions (required for CI/CD).
- Enable Issues and Discussions for community support.
- Enable Dependabot alerts and secret scanning (GitHub security tab).
- Protect `master`: require PR reviews + passing CI.
- Set branch protection to block force pushes to `master`.

## Discord command sync
- Set `GUILD_ID` in `.env` for fast iteration on one server.
- For production/global sync, unset `GUILD_ID`.

## Versioning
- Update `pyproject.toml` before tagging.
- Tag format: `vX.Y.Z` -> triggers release workflow and deploy.
- Update `CHANGELOG.md` with highlights per release.
