from pathlib import Path
from typing import Dict, List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/product_service'
    S3_PUBLIC_PRODUCTS_URL: str = 'http://127.0.0.1:9000'
    # BASE_FILE_PATH: Path = Path(__file__).resolve().parents[1] / 'static'
    ALLOW_FILE_EXTENSIONS: List[str] = ['.jpg', '.png']
    ALLOW_MIME_TYPES: List[str] = ["image/jpeg", "image/png"]
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB

    class Config:
        env_file = ".env"


settings = Settings()
