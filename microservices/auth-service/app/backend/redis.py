from redis.asyncio import Redis as AsyncRedis
from redis.asyncio import ConnectionPool


from app.config import settings


connection_pool = ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    max_connections=20
)

redis_client = AsyncRedis(connection_pool=connection_pool)


def get_redis():
    return redis_client
