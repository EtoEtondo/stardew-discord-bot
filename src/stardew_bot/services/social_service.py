"""Stub service for future social integrations (e.g., tweets, posts)."""

from __future__ import annotations


class SocialService:
    """Placeholder service for social media link posting or fetches."""

    def __init__(self) -> None:
        pass

    async def post_link(self, url: str) -> bool:  # pragma: no cover - stub
        """Post a link to a future social channel (to be implemented)."""
        return False

