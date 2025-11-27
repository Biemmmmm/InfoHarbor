from __future__ import annotations

from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class Settings(BaseSettings):
    app_name: str = "InfoHarbor"
    database_url: PostgresDsn | str = "postgresql+psycopg2://user:password@localhost:5432/infoharbor"

    class Config:
        env_file = ".env"

    def _create_engine(self) -> Engine:
        return create_engine(self.database_url, echo=False, future=True)

    def configure_database(self) -> None:
        if not hasattr(self, "engine"):
            self.engine = self._create_engine()

    def dispose_database(self) -> None:
        engine: Optional[Engine] = getattr(self, "engine", None)
        if engine:
            engine.dispose()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
