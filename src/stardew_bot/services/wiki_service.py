from __future__ import annotations

from urllib.parse import quote

Locale = str

WIKI_BASE = {
    "en": "https://stardewvalleywiki.com",
    "de": "https://de.stardewvalleywiki.com",
}


def build_wiki_url(term: str, locale: Locale = "en") -> str:
    """
    Build a wiki URL for any term.

    Wiki pages are case-insensitive, but mixed-case looks nicer.
    `_slugify` title-cases words, keeps slashes for nested pages, and URL-encodes.
    """
    base = WIKI_BASE.get(locale, WIKI_BASE["en"])
    slug = _slugify(term)
    return f"{base}/{slug}"


def build_npc_url(name: str, locale: Locale = "en") -> str:
    """
    Build wiki URL for an NPC page.

    Uses the same slug as generic pages so `/npc` can render a tailored embed
    while still hitting the canonical wiki URL (e.g., /Clint, /Maru).
    """
    return build_wiki_url(name, locale)


def build_crop_url(name: str, locale: Locale = "en") -> str:
    """
    Build wiki URL for a crop page.

    Crops are also top-level on the wiki (e.g., /Corn). We keep the helper so
    the crop command can diverge later (different embed/layout) without changing URLs.
    """
    return build_wiki_url(name, locale)


def build_fish_url(name: str, locale: Locale = "en") -> str:
    """Build wiki URL for a fish page (top-level slug, same rationale as crops/NPCs)."""
    return build_wiki_url(name, locale)


def _slugify(term: str) -> str:
    """
    Normalize user input to match wiki-style title-casing and safe characters.

    - Strips surrounding whitespace.
    - Replaces underscores with spaces, title-cases, then swaps spaces for underscores.
    - URL-encodes everything except slashes/underscores so multi-word and nested terms work.
    """
    normalized = term.strip().replace("_", " ")
    titled = normalized.title().replace(" ", "_")
    return quote(titled, safe="/_")
