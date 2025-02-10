import asyncio
from aioboto3.session import Session
from contextlib import asynccontextmanager


from app.config import settings


class S3Storage:
    def __init__(self):
        self.config = {
            'aws_access_key_id': 'XI1UIr0o8FdIOjyYnf12',
            'aws_secret_access_key': 'arZziGakt35B9mOqnL5E1ReXFzFHc6EaCpABo4Fe'
        }
        self.session = Session(**self.config)
        self.url = settings.S3_PUBLIC_PRODUCTS_URL

    @asynccontextmanager
    async def get_session(self):
        async with self.session.client('s3', endpoint_url=self.url) as session:
            yield session

    async def upload_object(
        self,
        body: bytes,
        bucket_name: str,
        content_type: str,
        key: str
    ):
        async with self.get_session() as session:
            await session.put_object(
                Body=body,
                Bucket=bucket_name,
                Key=key,
                ContentType=content_type
            )

    async def delete_object(
        self,
        bucket_name: str,
        key: str
    ):
        async with self.get_session() as session:
            await session.delete_object(
                Bucket=bucket_name,
                Key=key
            )
