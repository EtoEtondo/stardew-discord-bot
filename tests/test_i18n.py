from stardew_bot.i18n import Translator


def test_translate_fallback_to_default_locale() -> None:
    translator = Translator(default_locale="en")
    result = translator.translate("bot.about", locale="fr")
    assert "Stardew Helper" in result


def test_translate_includes_formatting() -> None:
    translator = Translator(default_locale="en")
    message = translator.translate("wiki.result", locale="en", term="Parsnip", url="https://example.com")
    assert "Parsnip" in message
    assert "https://example.com" in message
