from __future__ import annotations

import logging
from logging import Logger


def configure_logging(level: str = "INFO") -> Logger:
    """Configure root logger with simple console output."""
    numeric_level = logging.getLevelName(level.upper())
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    return logging.getLogger("stardew_bot")
