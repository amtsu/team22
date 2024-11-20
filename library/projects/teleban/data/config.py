import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def database_url_asyncpg(self) -> str:
        """Возвращает URL подключения к БД для драйвера asyncpg"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_psycopg(self) -> str:
        """Возвращает URL подключения к БД для драйвера psycopg"""
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # model_config = SettingsConfigDict(env_file="../.env")
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "../.env"))


# Создаём экземпляр настроек, чтобы использовать в приложении
settings = Settings()
