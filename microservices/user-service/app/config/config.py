from typing import Dict, List, Optional
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    # База данных
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/user_service'
    # RABBITMQ_URL: str

    # Redis
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None

    # Токены
    ACCESS_TOKEN: str
    REFRESH_TOKEN: str
    JWT_ALGORITHM: str
    JWT_ACCESS_EXPIRES_TIME_DELTA: int
    JWT_REFRESH_EXPIRES_TIME_DELTA: int

    # Пути к ключам
    PRIVATE_KEY_PATH: Path
    PUBLIC_KEY_PATH: Path

    @property
    def public_key(self):
        return self.PUBLIC_KEY_PATH.read_text()

    @property
    def private_key(self):
        return self.PRIVATE_KEY_PATH.read_text()

    # Хеширование паролей
    PASSWORD_HASH_SCHEMES: List[str]
    PASSWORD_HASH_ROUNDS: int

    # Аутентификация
    TOKEN_URL: str

    # Сообщения об ошибках
    ERROR_MESSAGES: Dict[str, str]

    model_config = SettingsConfigDict(
        env_file='./.env'
    )


settings = Settings()
