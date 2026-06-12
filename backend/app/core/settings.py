from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str = "sqlite:///./workflow_legion.db"
    redis_url: str = "redis://localhost:6379/0"
    band_api_key: str | None = None
    band_room_id: str | None = None
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
