from __future__ import annotations

from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    discord_token: str = Field(..., validation_alias="DISCORD_TOKEN")
    guild_id: int | None = Field(default=None, validation_alias="GUILD_ID")
    update_channel_id: int | None = Field(default=None, validation_alias="UPDATE_CHANNEL_ID")
    default_locale: str = Field(default="en", validation_alias="DEFAULT_LOCALE")
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")
    deploy_version: str | None = Field(default=None, validation_alias="DEPLOY_VERSION")
    deploy_marker_path: str = Field(
        default=".state/last_deploy_version.txt", validation_alias="DEPLOY_MARKER_PATH"
    )
    enable_reaction_feedback: bool = Field(
        default=True, validation_alias="ENABLE_REACTION_FEEDBACK"
    )

    @field_validator("default_locale")
    @classmethod
    def normalize_locale(cls, value: str) -> str:
        return value.lower()

    @field_validator("log_level")
    @classmethod
    def normalize_log_level(cls, value: str) -> str:
        return value.upper()


@lru_cache
def get_settings() -> Settings:
    """Cached settings loader."""
    return Settings()  # type: ignore[call-arg]
