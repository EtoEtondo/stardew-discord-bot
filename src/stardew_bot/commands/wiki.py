from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator
from stardew_bot.services import wiki_service

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class WikiCog(commands.Cog):
    def __init__(self, bot: StardewBot, translator: Translator) -> None:
        self.bot = bot
        self.translator = translator
        self.reactions_enabled = bot.settings.enable_reaction_feedback

    def _locale(self, interaction: discord.Interaction, override: str | None = None) -> str:
        """Resolve locale from interaction or override."""
        selected = override
        if selected is None and interaction.locale:
            selected = str(interaction.locale)
        if selected is None and interaction.guild_locale:
            selected = str(interaction.guild_locale)
        return self.translator.detect_locale(selected, fallback=self.bot.settings.default_locale)

    @app_commands.command(name="wiki", description="Get a Stardew Valley wiki link for a term")
    async def wiki(
        self,
        interaction: discord.Interaction,
        term: str,
        lang: str | None = None,
    ) -> None:
        """Return a wiki link embed and add a ⭐ reaction for feedback."""
        locale = self._locale(interaction, lang)
        term = term.strip()
        if not term:
            error_message = self.translator.translate("error.empty_term", locale=locale)
            await interaction.response.send_message(error_message, ephemeral=True)
            return
        url = wiki_service.build_wiki_url(term, locale=locale)
        description = self.translator.translate(
            "wiki.result",
            locale=locale,
            term=term,
            url=url,
        )
        embed = discord.Embed(
            title=f"📖 {term.title()}",
            description=description,
            url=url,
            color=discord.Color.green(),
        )
        await interaction.response.send_message(embed=embed)
        if self.reactions_enabled:
            response_message = await interaction.original_response()
            await self._add_reaction(response_message)

    @staticmethod
    async def _add_reaction(message: discord.Message) -> None:
        """Add a star reaction to gauge interest; ignore failures."""
        try:
            await message.add_reaction("⭐")
        except discord.HTTPException:
            return
