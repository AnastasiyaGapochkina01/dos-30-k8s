from datetime import datetime
from pydantic import BaseModel, field_validator


class BlogNoteBase(BaseModel):
    title: str
    content: str
    category: str  # "personal" | "article"

    @field_validator("category")
    @classmethod
    def validate_category(cls, v: str) -> str:
        allowed = {"personal", "article"}
        v = v.strip().lower()
        if v not in allowed:
            raise ValueError(f"category must be one of {allowed}")
        return v


class BlogNoteCreate(BlogNoteBase):
    pass


class BlogNoteRead(BlogNoteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

