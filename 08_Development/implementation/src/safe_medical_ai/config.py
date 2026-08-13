"""Environment-driven configuration skeleton.

Per TECH_STACK.md, configuration is environment-variable driven with an
`.env.example` template and no committed secrets. This module defines only
the configuration skeleton required for the development scaffolding; it
does not implement retrieval, storage, or LLM-provider connectivity.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables / `.env`.

    All fields have safe, non-secret defaults so the configuration can be
    loaded in any environment (including CI/test) without requiring a
    populated `.env` file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="SMA_",
        extra="ignore",
    )

    app_name: str = "safe-medical-ai-oncology"
    environment: str = "development"
    log_level: str = "INFO"

    # PostgreSQL is the locked structured-runtime-storage *direction*
    # (TECH_STACK.md §1); exact schema and connectivity are deferred and
    # not implemented by this scaffolding. This field exists only so the
    # configuration surface is ready to accept a connection string later.
    database_url: str | None = None


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
