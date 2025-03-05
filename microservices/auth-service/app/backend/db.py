from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase


from app.config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

AsyncSession = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=True
)


async def get_session():
    async with AsyncSession() as session:
        yield session


class Base(DeclarativeBase):
    pass
