"""Configuration module for external services and environment variables."""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for external services and environment configuration."""

    post_service_url: str
    log_level: str = "INFO"

    model_config = ConfigDict(env_file=".env")


settings = Settings()
