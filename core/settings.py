from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")
