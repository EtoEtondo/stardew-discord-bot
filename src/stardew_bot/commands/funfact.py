from __future__ import annotations

import random
from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class FunFactCog(commands.Cog):
    def __init__(self, bot: StardewBot, translator: Translator) -> None:
        self.bot = bot
        self.translator = translator

    def _locale(self, interaction: discord.Interaction, override: str | None = None) -> str:
        """Resolve locale from interaction or override."""
        selected = override
        if selected is None and interaction.locale:
            selected = str(interaction.locale)
        if selected is None and interaction.guild_locale:
            selected = str(interaction.guild_locale)
        return self.translator.detect_locale(selected, fallback=self.bot.settings.default_locale)

    @app_commands.command(name="funfact", description="Get a fun fact about Stardew Valley")
    async def funfact(
        self,
        interaction: discord.Interaction,
        lang: str | None = None,
    ) -> None:
        """Send a random fun fact."""
        locale = self._locale(interaction, lang)
        title = self.translator.translate("funfact.title", locale=locale)
        entries = self.translator.translate("funfact.entries", locale=locale)
        if isinstance(entries, list) and entries:
            fact = random.choice(entries)
        else:
            fact = "Stardew Valley is cozy!"
        await interaction.response.send_message(f"🌾 {title}: {fact}")
