from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/order_service'


settings = Settings()
