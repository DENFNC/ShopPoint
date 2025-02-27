from fastapi import File, UploadFile
import magic


from app.core.core_utils import FileValidator
from app.backend import S3Storage


async def get_file_validator(file: UploadFile) -> FileValidator:
    return FileValidator(file=file)


async def get_s3() -> S3Storage:
    return S3Storage()


async def get_mimetype_file(file: UploadFile = File(...)):
    mime_detector = magic.Magic(mime=True)
    read_file = await file.read(4096)

    mimetype = mime_detector.from_buffer(buf=read_file)

    await file.seek(0)
    return mimetype
