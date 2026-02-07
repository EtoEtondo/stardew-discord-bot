from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from stardew_bot.i18n import Translator
from stardew_bot.services import wiki_service

if TYPE_CHECKING:
    from stardew_bot.bot import StardewBot


class CropCog(commands.Cog):
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

    @app_commands.command(name="crop", description="Get quick info about a crop")
    async def crop(
        self,
        interaction: discord.Interaction,
        name: str,
        lang: str | None = None,
    ) -> None:
        """Send a crop embed with wiki link and a ⭐ reaction for feedback."""
        locale = self._locale(interaction, lang)
        name = name.strip()
        if not name:
            error_message = self.translator.translate("error.empty_term", locale=locale)
            await interaction.response.send_message(error_message, ephemeral=True)
            return
        url = wiki_service.build_crop_url(name, locale=locale)
        description = self.translator.translate("crop.response", locale=locale, name=name, url=url)
        embed = discord.Embed(
            title=f"🌾 {name.title()}",
            description=description,
            url=url,
            color=discord.Color.green(),
        )
        embed.set_footer(text="Source: Stardew Valley Wiki")
        await interaction.response.send_message(embed=embed)
        response_message = await interaction.original_response()
        await self._add_reaction(response_message)

    @staticmethod
    async def _add_reaction(message: discord.Message) -> None:
        """Add a star reaction to gauge interest; ignore failures."""
        try:
            await message.add_reaction("⭐")
        except discord.HTTPException:
            return
