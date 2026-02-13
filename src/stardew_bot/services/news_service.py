"""Stub service for future news/patchnotes sources."""

from __future__ import annotations

from typing import Iterable


class NewsService:
    """Placeholder service to list news sources and fetch updates."""

    def __init__(self, sources: Iterable[str] | None = None) -> None:
        self.sources = list(sources or [])

    def list_sources(self) -> list[str]:  # pragma: no cover - stub
        """Return configured news sources."""
        return self.sources

