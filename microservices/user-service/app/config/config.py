from typing import Dict, List, Optional
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    # База данных
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/user_service'

    # Сообщения об ошибках
    ERROR_MESSAGES: Dict[str, str]

    model_config = SettingsConfigDict(
        env_file='./.env'
    )


settings = Settings()
