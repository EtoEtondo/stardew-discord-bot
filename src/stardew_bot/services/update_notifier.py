from __future__ import annotations

import logging

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

    async def notify(self, bot: commands.Bot) -> None:
        if self._has_notified:
            return
        if not self.settings.update_channel_id or not self.settings.deploy_version:
            return
        channel = bot.get_channel(self.settings.update_channel_id)
        if not isinstance(channel, discord.TextChannel):
            LOGGER.warning(
                "Update channel id %s not found or not a text channel",
                self.settings.update_channel_id,
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
            self._has_notified = True
            LOGGER.info("Sent deploy notification to channel %s", self.settings.update_channel_id)
        except Exception as exc:  # noqa: BLE001
            LOGGER.error("Failed to send update notification: %s", exc)
