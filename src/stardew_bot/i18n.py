from __future__ import annotations

import json
import logging
from collections.abc import Mapping
from dataclasses import dataclass
from importlib import resources
from typing import Any, cast

LOGGER = logging.getLogger(__name__)


@dataclass
class LocaleData:
    code: str
    strings: Mapping[str, object]


class Translator:
    """Simple JSON-based translation helper with locale fallback."""

    def __init__(self, default_locale: str = "en") -> None:
        self.default_locale = default_locale
        self._locales: dict[str, LocaleData] = {}
        self.reload()

    def reload(self) -> None:
        """Reload locale JSON files from package resources."""
        self._locales.clear()
        locales_path = resources.files("stardew_bot") / "locales"
        for entry in locales_path.iterdir():
            filename = entry.name
            if not filename.endswith(".json"):
                continue
            code = filename.removesuffix(".json").lower()
            strings = self._load_locale_file(entry)
            self._locales[code] = LocaleData(code=code, strings=strings)
            LOGGER.debug("Loaded locale %s with %d entries", code, len(strings))
        if self.default_locale not in self._locales:
            LOGGER.warning("Default locale %s missing, falling back to en", self.default_locale)
            self.default_locale = "en"

    def translate(
        self,
        key: str,
        locale: str | None = None,
        **kwargs: object,
    ) -> str | list[str]:
        """Return translated string/list with optional format substitution."""
        locale_code = (locale or self.default_locale).lower()
        text = self._get_text(locale_code, key)
        if text is None and locale_code != self.default_locale:
            text = self._get_text(self.default_locale, key)
        if text is None:
            LOGGER.debug("Missing translation for key %s", key)
            return key
        if isinstance(text, list):
            return [str(item) for item in text]
        text_str = str(text)
        try:
            return text_str.format(**kwargs)
        except Exception:  # noqa: BLE001
            return text_str

    def _get_text(self, locale: str, key: str) -> object | None:
        locale_data = self._locales.get(locale)
        if not locale_data:
            return None
        return locale_data.strings.get(key)

    def available_locales(self) -> dict[str, LocaleData]:
        """Return loaded locale map."""
        return self._locales

    def detect_locale(self, interaction_locale: str | None, fallback: str | None = None) -> str:
        """Pick the best locale based on interaction/guild with fallback to default."""
        raw_locale = interaction_locale or fallback or self.default_locale
        locale_code = raw_locale.split("-")[0].lower()
        if locale_code in self._locales:
            return locale_code
        return self.default_locale

    def _load_locale_file(self, path: Any) -> Mapping[str, object]:
        with path.open("r", encoding="utf-8") as handle:
            return cast(Mapping[str, object], json.load(handle))
