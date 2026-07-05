from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "whiffd"
    debug: bool = False
    ballchasing_api_key: str
    ballchasing_base_url: str = "https://ballchasing.com/api"


settings = Settings()