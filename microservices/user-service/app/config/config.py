from typing import Dict, List, Optional
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # База данных
    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost/user_service"
    RABBITMQ_URL: str = 'amqp://guest:guest@localhost/'

    # REDIS
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None

    # Токены
    ACCESS_TOKEN: str = 'access'
    REFRESH_TOKEN: str = 'refresh'
    JWT_ALGORITHM: str = 'RS256'
    JWT_ACCESS_EXPIRES_TIME_DELTA: int = 3 * 60
    JWT_REFRESH_EXPIRES_TIME_DELTA: int = 30 * 24 * 60 * 60

    # Пути к ключам
    BASE_PATH: Path = Path(__file__).resolve().parent
    PRIVATE_KEY_PATH: Path = BASE_PATH / './keys/private.key'
    PUBLIC_KEY_PATH: Path = BASE_PATH / './keys/public.key'

    # Загрузка ключей
    @property
    def private_key(self) -> str:
        return self.PRIVATE_KEY_PATH.read_text()

    @property
    def public_key(self) -> str:
        return self.PUBLIC_KEY_PATH.read_text()

    # Хеширование паролей
    PASSWORD_HASH_SCHEMES: List[str] = ['bcrypt']
    PASSWORD_HASH_ROUNDS: int = 12

    # Аутентификация
    TOKEN_URL: str = '/api/v1/auth/token'

    # Сообщения об ошибках
    ERROR_MESSAGES: Dict[str, str] = {
        "token_expired": "Token expired",
        "invalid_token": "Invalid token",
        "invalid_credentials": "Username or password not valid",
        "invalid_token_type": "Invalid token type",
    }

    class Config:
        env = '.env'


settings = Settings()
oauth2_schema = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)
