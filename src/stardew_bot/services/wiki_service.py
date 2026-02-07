from __future__ import annotations

from urllib.parse import quote

Locale = str

WIKI_BASE = {
    "en": "https://stardewvalleywiki.com",
    "de": "https://de.stardewvalleywiki.com",
}


def build_wiki_url(term: str, locale: Locale = "en") -> str:
    """Build a wiki URL for an arbitrary term, keeping locale where possible."""
    base = WIKI_BASE.get(locale, WIKI_BASE["en"])
    slug = _slugify(term)
    return f"{base}/{slug}"


def build_npc_url(name: str, locale: Locale = "en") -> str:
    """Build wiki URL for an NPC page."""
    return build_wiki_url(f"NPCs/{name}", locale)


def build_crop_url(name: str, locale: Locale = "en") -> str:
    """Build wiki URL for a crop page."""
    return build_wiki_url(f"Crops/{name}", locale)


def build_fish_url(name: str, locale: Locale = "en") -> str:
    """Build wiki URL for a fish page."""
    return build_wiki_url(f"Fish/{name}", locale)


def _slugify(term: str) -> str:
    """Normalize user input to match wiki-style title-casing and safe characters."""
    normalized = term.strip().replace("_", " ")
    titled = normalized.title().replace(" ", "_")
    return quote(titled, safe="/_")
