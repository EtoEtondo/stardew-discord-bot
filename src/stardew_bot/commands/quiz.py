from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class QuizCog(commands.Cog):
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

    @app_commands.command(name="quiz", description="Play a Stardew Valley quiz (coming soon)")
    async def quiz(
        self,
        interaction: discord.Interaction,
        lang: str | None = None,
    ) -> None:
        """Placeholder for quiz command."""
        locale = self._locale(interaction, lang)
        message = self.translator.translate("quiz.placeholder", locale=locale)
        await interaction.response.send_message(message, ephemeral=True)
