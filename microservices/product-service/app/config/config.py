from typing import List
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/product_service'
    S3_URL: str = 'http://localhost:9000'
    ALLOW_FILE_EXTENSIONS: List[str] = ['.jpg', '.png']
    ALLOW_MIME_TYPES: List[str] = ["image/jpeg", "image/png"]
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB

    model_config = SettingsConfigDict(
        env_file='./.env'
    )


settings = Settings()
