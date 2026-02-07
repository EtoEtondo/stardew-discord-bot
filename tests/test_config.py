from pytest import MonkeyPatch

from stardew_bot.config import Settings


def test_settings_normalize_locale_and_level(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("DISCORD_TOKEN", "dummy")
    monkeypatch.setenv("DEFAULT_LOCALE", "DE")
    monkeypatch.setenv("LOG_LEVEL", "debug")
    settings = Settings()  # type: ignore[call-arg]
    assert settings.default_locale == "de"
    assert settings.log_level == "DEBUG"
