from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base


class BlogNote(Base):
    __tablename__ = "blog_notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)  # "personal" или "article"
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

