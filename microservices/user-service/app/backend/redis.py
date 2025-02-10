from redis.asyncio import Redis, ConnectionPool


REDIS_POOL = ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=10
)


async def get_redis():
    return Redis(connection_pool=REDIS_POOL)
