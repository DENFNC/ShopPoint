import aio_pika
from aio_pika.abc import AbstractChannel as Channel
from typing import Any, AsyncGenerator

from fastapi import HTTPException


from app.config import settings


async def get_rabbit() -> AsyncGenerator[Channel, Any]:
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
    channel = await connection.channel()
    try:
        yield channel
    except aio_pika.exceptions.AMQPError:
        raise HTTPException(
            status_code=500, detail="Не удалось подключиться к RabbitMQ"
        )
    finally:
        await channel.close()
        await connection.close()
