from pathlib import Path
from typing import Dict, List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost/product_service'
    S3_PUBLIC_PRODUCTS_URL: str = 'http://127.0.0.1:9000'
    BASE_FILE_PATH: Path = Path(__file__).resolve().parents[1] / 'static'
    ALLOW_FILE_EXTENSIONS: List[str] = ['.jpg', '.png']
    ALLOW_MIME_TYPES: List[str] = ["image/jpeg", "image/png"]
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB

    ERROR_MESSAGE: Dict[str, str] = {
        "PRODUCT_NOT_FOUND": "Product not found.",
        "DUPLICATE_PRODUCT_NAME": "Product name already exists.",
        "INVALID_PRICE": "Invalid price.",
        "MISSING_NAME": "Name is required.",
        "MISSING_PRICE": "Price is required.",
        "INVALID_SUPPLIER_ID": "Invalid supplier ID.",
        "INVALID_PRODUCT_ID": "Invalid product ID.",
        "PRODUCT_INACTIVE": "Product is inactive.",
        "INVALID_DATA_FORMAT": "Invalid data format.",
        "DATABASE_ERROR": "Database error.",
        "FOREIGN_KEY_VIOLATION": "Foreign key violation.",
        "UNIQUE_CONSTRAINT_VIOLATION": "Unique constraint error.",
        "INVALID_DATETIME_FORMAT": "Invalid datetime format.",
        "SOFT_DELETE_ERROR": "Soft delete failed.",
        "UPDATE_FAILED": "Update failed.",
        "CREATION_FAILED": "Creation failed.",
        "DESCRIPTION_TOO_LONG": "Description too long.",
        "IMAGE_URL_INVALID": "Invalid image URL.",
        "IMAGE_TYPE_INVALID": "Unsupported file format",
        "IMAGE_SIZE_INVALID": "The file size is too large",
        "CATEGORY_ASSIGNMENT_FAILED": "Category assignment failed."
    }

    NOTIFICATION_MESSAGE: Dict[str, str] = {
        "PRODUCT_CREATED": "Product created successfully.",
        "PRODUCT_UPDATED": "Product updated successfully.",
        "PRODUCT_DELETED": "Product deleted successfully.",
        "CATEGORY_ASSIGNED": "Category assigned successfully.",
        "CATEGORY_UNASSIGNED": "Category unassigned successfully.",
        "SUPPLIER_ADDED": "Supplier added successfully.",
        "SUPPLIER_UPDATED": "Supplier updated successfully.",
        "SUPPLIER_DELETED": "Supplier deleted successfully.",
        "PRICE_UPDATED": "Price updated successfully.",
        "PRODUCT_ACTIVATED": "Product activated successfully.",
        "PRODUCT_DEACTIVATED": "Product deactivated successfully.",
        "DATA_IMPORTED": "Data imported successfully.",
        "DATA_EXPORTED": "Data exported successfully.",
        "EMAIL_SENT": "Email sent successfully.",
        "PASSWORD_CHANGED": "Password changed successfully.",
        "PROFILE_UPDATED": "Profile updated successfully.",
        "ORDER_PLACED": "Order placed successfully.",
        "ORDER_SHIPPED": "Order shipped successfully.",
        "ORDER_CANCELLED": "Order cancelled successfully."
    }

    class Config:
        env_file = ".env"


settings = Settings()
