from __future__ import annotations

import logging

import discord
from discord.ext import commands

from stardew_bot import __version__
from stardew_bot.commands.crop import CropCog
from stardew_bot.commands.fish import FishCog
from stardew_bot.commands.funfact import FunFactCog
from stardew_bot.commands.help import HelpCog
from stardew_bot.commands.npc import NPCCog
from stardew_bot.commands.quiz import QuizCog
from stardew_bot.commands.tooling import ToolingCog
from stardew_bot.commands.wiki import WikiCog
from stardew_bot.config import Settings
from stardew_bot.i18n import Translator
from stardew_bot.services.update_notifier import UpdateNotifier

LOGGER = logging.getLogger(__name__)


class StardewBot(commands.Bot):
    """Discord bot client for Stardew Helper."""

    def __init__(self, settings: Settings, translator: Translator) -> None:
        intents = discord.Intents.default()
        intents.message_content = False
        super().__init__(command_prefix="!", intents=intents)
        self.settings = settings
        self.translator = translator
        self.update_notifier = UpdateNotifier(settings=settings, translator=translator)

    async def setup_hook(self) -> None:
        await self._load_cogs()
        await self._sync_tree()

    async def _load_cogs(self) -> None:
        await self.add_cog(HelpCog(self, self.translator))
        await self.add_cog(WikiCog(self, self.translator))
        await self.add_cog(ToolingCog(self, self.translator))
        await self.add_cog(FunFactCog(self, self.translator))
        await self.add_cog(QuizCog(self, self.translator))
        await self.add_cog(NPCCog(self, self.translator))
        await self.add_cog(CropCog(self, self.translator))
        await self.add_cog(FishCog(self, self.translator))

    async def _sync_tree(self) -> None:
        target_guild: discord.Object | None = None
        if self.settings.guild_id:
            target_guild = discord.Object(id=self.settings.guild_id)
            await self.tree.sync(guild=target_guild)
            LOGGER.info("Synced commands to guild %s", self.settings.guild_id)
        await self.tree.sync(guild=None)
        LOGGER.info("Synced global commands")

    async def on_ready(self) -> None:
        LOGGER.info("Logged in as %s (%s)", self.user, __version__)
        await self.update_notifier.notify(self)


def create_bot(settings: Settings, translator: Translator) -> StardewBot:
    return StardewBot(settings=settings, translator=translator)
