from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_prefix="colibri_", env_file=".env")


config = Config()
