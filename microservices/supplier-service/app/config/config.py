from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/supplier_service'


settings = Settings()
