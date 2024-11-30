from enum import Enum
from fastapi_users import schemas
from pydantic import BaseModel, Field
from typing import Optional
import uuid


class ConversionType(str, Enum):
    XLSX_TO_CSV = "xlsx_to_csv"
    CSV_TO_XLSX = "csv_to_xlsx"
    DOCX_TO_PDF = "docx_to_pdf"
    PDF_TO_DOCX = "pdf_to_docx"


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class ImageProcessingOptions(BaseModel):
    resize: Optional[str] = Field(None, description="Example: 1980x1200")
    convert_to: Optional[str] = Field(None, description="png, jpg, webp")
    grayscale: Optional[bool] = Field(None, description="Convert to grayscale")
    flip: Optional[str] = Field(None, description="horizontal or vertical")


class FileProcessingOptions(BaseModel):
    conversion_type: Optional[ConversionType] = Field(None, description="Type of conversion")
