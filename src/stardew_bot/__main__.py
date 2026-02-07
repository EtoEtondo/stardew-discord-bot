from __future__ import annotations

import asyncio

from stardew_bot.bot import create_bot
from stardew_bot.config import get_settings
from stardew_bot.i18n import Translator
from stardew_bot.utils.logging import configure_logging


def main() -> None:
    """Entrypoint to configure and start the bot."""
    settings = get_settings()
    logger = configure_logging(settings.log_level)
    translator = Translator(default_locale=settings.default_locale)

    bot = create_bot(settings=settings, translator=translator)
    logger.info("Starting Stardew Helper")
    asyncio.run(bot.start(settings.discord_token))


if __name__ == "__main__":
    main()
