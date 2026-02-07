from stardew_bot.services import wiki_service


def test_build_wiki_url_defaults_to_en() -> None:
    url = wiki_service.build_wiki_url("Parsnip")
    assert url.startswith("https://stardewvalleywiki.com/")
    assert "Parsnip" in url


def test_build_wiki_url_respects_locale() -> None:
    url = wiki_service.build_wiki_url("Parsnip", locale="de")
    assert url.startswith("https://de.stardewvalleywiki.com/")


def test_slugify_title_cases_terms() -> None:
    url = wiki_service.build_wiki_url("clint")
    assert url.endswith("Clint")
