from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class ToolingCog(commands.Cog):
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

    @app_commands.command(name="tooling", description="Show useful Stardew Valley tooling links")
    async def tooling(
        self,
        interaction: discord.Interaction,
        lang: str | None = None,
    ) -> None:
        """List useful external tools."""
        locale = self._locale(interaction, lang)
        header = self.translator.translate("tooling.list", locale=locale)
        entries = self.translator.translate("tooling.entries", locale=locale)
        if isinstance(entries, list):
            body = "\n".join(f"• {item}" for item in entries)
        else:
            body = str(entries)
        embed = discord.Embed(
            title="🧰 Stardew tooling",
            description=f"{header}\n{body}",
            color=discord.Color.blurple(),
        )
        await interaction.response.send_message(embed=embed)
