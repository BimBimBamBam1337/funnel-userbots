from pathlib import Path
from typing import Literal
from urllib.parse import quote_plus

from pydantic import BaseModel, SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    name: str = "postgres"
    username: str = "postgres"
    password: SecretStr = SecretStr("password")

    def get_url(
        self,
        scheme: Literal[
            "postgres", "postgresql", "postgresql+asyncpg"
        ] = "postgresql+asyncpg",
        db_name: str | None = None,
    ) -> SecretStr:
        # URL-encode user/pwd so reserved chars (@ / : # ? %) in rotated
        # secrets do not produce a malformed DSN asyncpg mis-parses.
        user = quote_plus(self.username)
        pwd = quote_plus(self.password.get_secret_value())
        name = db_name or self.name
        return SecretStr(f"{scheme}://{user}:{pwd}@{self.host}:{self.port}/{name}")


class BotSettings(BaseModel):
    token: str
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class Config(BaseSettings):
    root_dir: Path = Path(__file__).parent.parent.resolve()
    logging_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    db: DBSettings = DBSettings()
    bot: BotSettings = BotSettings()
    model_config = SettingsConfigDict(
        env_file=f"{root_dir}/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Config()
