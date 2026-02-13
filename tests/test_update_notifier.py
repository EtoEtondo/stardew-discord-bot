from __future__ import annotations

from types import SimpleNamespace

import pytest

from stardew_bot.services.update_notifier import UpdateNotifier


class DummyChannel:
    def __init__(self) -> None:
        self.sent: list[str] = []

    async def send(self, message: str) -> None:
        self.sent.append(message)


class TranslatorStub:
    def translate(self, key: str, *, locale: str, version: str) -> str:  # noqa: D401
        return f"{locale}:{version}"


@pytest.mark.asyncio
async def test_notify_posts_once_and_persists(tmp_path) -> None:
    marker = tmp_path / "last_version.txt"
    settings = SimpleNamespace(
        update_channel_id=123,
        deploy_version="1.2.3",
        default_locale="en",
        deploy_marker_path=str(marker),
    )
    channel = DummyChannel()
    bot = SimpleNamespace(get_channel=lambda _: channel)
    notifier = UpdateNotifier(settings=settings, translator=TranslatorStub())

    await notifier.notify(bot)
    # Marker written and message sent
    assert channel.sent == ["en:1.2.3"]
    assert marker.read_text().strip() == "1.2.3"

    await notifier.notify(bot)
    # No duplicate send
    assert channel.sent == ["en:1.2.3"]
