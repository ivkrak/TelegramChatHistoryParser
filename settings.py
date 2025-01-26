from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    API_ID: int
    API_HASH: str
    PHONE_NUMBER: str
    CLOUD_PASSWORD: str | None = None

    API_KEY: str


settings = Settings()
