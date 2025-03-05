from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    # Postgres
    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/auth_service"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # JWT
    PRIVATE_KEY: Path = Path(__file__).parent / 'keys' / 'private.pem'
    PUBLIC_KEY: Path = Path(__file__).parent / 'keys' / 'public.pem'
    ALGORITHM: str = 'RS256'
    JWT_ACCESS_EXPIRES_TIME_DELTA: int = 180
    JWT_REFRESH_EXPIRES_TIME_DELTA: int = 2592000

    @property
    def public_key(self):
        return self.PUBLIC_KEY.read_text()

    @property
    def private_key(self):
        return self.PRIVATE_KEY.read_text()

    model_config = SettingsConfigDict(
        env_file='./.env'
    )


settings = Settings()
