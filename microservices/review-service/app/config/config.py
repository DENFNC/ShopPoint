from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    BASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/review_service'

    model_config = SettingsConfigDict(
        env_file='./.env'
    )


settings = Settings()
