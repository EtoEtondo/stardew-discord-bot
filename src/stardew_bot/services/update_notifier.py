from __future__ import annotations

import logging
from pathlib import Path

import discord
from discord.ext import commands

from stardew_bot.config import Settings
from stardew_bot.i18n import Translator

LOGGER = logging.getLogger(__name__)


class UpdateNotifier:
    def __init__(self, settings: Settings, translator: Translator) -> None:
        self.settings = settings
        self.translator = translator
        self._has_notified = False
        # File marker prevents duplicate posts across restarts of the same version.
        self.marker_path = Path(settings.deploy_marker_path)

    async def notify(self, bot: commands.Bot) -> None:
        # Guard: only run once per process and only when version + channel are provided.
        if self._has_notified:
            return
        if not self.settings.update_channel_id or not self.settings.deploy_version:
            return
        channel = bot.get_channel(self.settings.update_channel_id)
        if channel is None or not hasattr(channel, "send"):
            LOGGER.warning(
                "Update channel id %s not found or not a text channel",
                self.settings.update_channel_id,
            )
            return

        last_posted_version = self._read_last_posted_version()
        if last_posted_version == self.settings.deploy_version:
            LOGGER.info(
                "Deploy notification already posted for version %s", self.settings.deploy_version
            )
            return
        locale = self.settings.default_locale
        message_obj = self.translator.translate(
            "update.message",
            locale=locale,
            version=self.settings.deploy_version,
        )
        message = message_obj if isinstance(message_obj, str) else str(message_obj)
        try:
            await channel.send(message)
            self._write_last_posted_version(self.settings.deploy_version)
            self._has_notified = True
            LOGGER.info("Sent deploy notification to channel %s", self.settings.update_channel_id)
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed to send update notification: %s", exc)

    def _read_last_posted_version(self) -> str | None:
        try:
            if self.marker_path.exists():
                return self.marker_path.read_text(encoding="utf-8").strip() or None
        except OSError as exc:
            LOGGER.warning("Could not read deploy marker file %s: %s", self.marker_path, exc)
        return None

    def _write_last_posted_version(self, version: str) -> None:
        try:
            self.marker_path.parent.mkdir(parents=True, exist_ok=True)
            self.marker_path.write_text(version, encoding="utf-8")
        except OSError as exc:
            LOGGER.warning("Could not write deploy marker file %s: %s", self.marker_path, exc)
