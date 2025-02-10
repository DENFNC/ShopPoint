import mimetypes
import magic
import asyncio

from pathlib import Path
from fastapi import UploadFile, HTTPException, status


from app.config import settings


class FileValidator:
    def __init__(self, file: UploadFile):
        self.file = file

    async def file_validate(self):
        await asyncio.gather(
            asyncio.to_thread(self.check_size),
            asyncio.to_thread(self.check_extension),
        )
        await self.check_magic()
        await self.file.seek(0)

    def check_extension(self):
        suffix = Path(self.file.filename).suffix

        if suffix not in settings.ALLOW_FILE_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def check_size(self):
        file_size = self.file.size

        if file_size > settings.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
            )

    async def check_magic(self):
        mime_detector = magic.Magic(mime=True)
        file = await self.file.read(1024)

        mimetype = mime_detector.from_buffer(buf=file)

        if mimetype not in settings.ALLOW_MIME_TYPES:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
