from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "fast_api_info"}  # если не указывать, то будет схема public

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    __table_args__ = {"schema": "fast_api_info"}  # если не указывать, то будет схема public

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("fast_api_info.users.id"))  # для public схему не указывать

    owner = relationship("User", back_populates="items")
