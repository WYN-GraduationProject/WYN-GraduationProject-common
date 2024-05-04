from pydantic import BaseModel
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import mapped_column, Mapped
from utils.tools.SqlManager import SqlManager


class PostModel(SqlManager.Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)


class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
