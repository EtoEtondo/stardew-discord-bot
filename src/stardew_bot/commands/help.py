from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class HelpCog(commands.Cog):
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

    @app_commands.command(name="help", description="Show help and bot info")
    async def help_command(
        self,
        interaction: discord.Interaction,
        lang: str | None = None,
    ) -> None:
        """Send a quick help embed with links."""
        locale = self._locale(interaction, lang)
        about = self.translator.translate("bot.about", locale=locale)
        footer = self.translator.translate(
            "help.footer",
            locale=locale,
            repo="https://github.com/EtoEtondo/stardew-discord-bot",
        )
        commands_line = "/wiki, /tooling, /funfact, /quiz, /npc, /crop, /fish"
        embed = discord.Embed(
            title="🌱 Stardew Helper",
            description=f"{about}\n\nCommands: {commands_line}",
            color=discord.Color.green(),
        )
        embed.set_footer(text=footer)
        await interaction.response.send_message(embed=embed, ephemeral=True)
