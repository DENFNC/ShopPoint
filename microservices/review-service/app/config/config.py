from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/review_service'


settings = Settings()