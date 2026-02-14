#!/usr/bin/env bash

# Fail fast and surface first failing tool.
set -euo pipefail

# Keep uv caches local to the repo to avoid permission issues.
: "${UV_CACHE_DIR:=.uv-cache}"
export UV_CACHE_DIR

# Ensure local package is importable without installing an editable wheel.
export PYTHONPATH="src:${PYTHONPATH:-}"

echo "==> Running formatter"
uv sync --dev >/dev/null
uv run ruff format .

echo "==> Linting"
uv run ruff check .

echo "==> Type checking"
uv run mypy .

echo "==> Tests"
uv run pytest
