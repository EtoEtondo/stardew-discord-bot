"""Stub service for future Steam integrations (e.g., reviews, player counts)."""

from __future__ import annotations


class SteamService:
    """Placeholder service for Steam-related lookups."""

    def __init__(self) -> None:
        pass

    async def get_reviews(self, app_id: str) -> dict | None:  # pragma: no cover - stub
        """Fetch reviews for a Steam app (to be implemented)."""
        return None

