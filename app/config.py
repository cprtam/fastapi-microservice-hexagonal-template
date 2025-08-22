"""Configuration settings for the application using Pydantic's BaseSettings."""

from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    # Application metadata
    app_name: str = Field(..., validation_alias="APP_NAME")
    app_summary: str = Field(..., validation_alias="APP_SUMMARY")
    app_description: str = Field(..., validation_alias="APP_DESCRIPTION")
    app_version: str = Field(..., validation_alias="APP_VERSION")
    debug: bool = Field(False, validation_alias="DEBUG")
    secret_key: str = Field(..., validation_alias="SECRET_KEY")

    # Database configuration
    db_user: str = Field(..., validation_alias="POSTGRES_USER")
    db_password: str = Field(..., validation_alias="POSTGRES_PASSWORD")
    db_host: str = Field(..., validation_alias="POSTGRES_HOST")
    db_port: str = Field(..., validation_alias="POSTGRES_PORT")
    db_name: str = Field(..., validation_alias="POSTGRES_DB")
    database_url: str = Field(..., validation_alias="DATABASE_URL")

    # Auth and security
    access_token_expire_minutes: int = Field(
        ..., validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    algorithm: str = Field(..., validation_alias="ALGORITHM")

    # CORS
    cors_allow_origins: str = Field(..., validation_alias="CORS_ALLOW_ORIGINS")
    cors_allow_credentials: bool = Field(..., validation_alias="CORS_ALLOW_CREDENTIALS")
    cors_allow_methods: str = Field(..., validation_alias="CORS_ALLOW_METHODS")
    cors_allow_headers: str = Field(..., validation_alias="CORS_ALLOW_HEADERS")


settings = Settings()
