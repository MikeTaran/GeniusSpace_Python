import uuid
from pydantic import BaseModel, Field
from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class ImageProcessionOptions(BaseModel):
    resize: Optional[str] = Field(None, description="Example: 1980x1200")
    convert_to: Optional[str] = Field(None, description="png, jpg, webp")
    grayscale: Optional[bool] = Field(None, description="Convert to greyscale")
    flip: Optional[str] = Field(None, description="horizontal or vertical")
