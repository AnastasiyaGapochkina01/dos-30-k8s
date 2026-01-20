from sqlalchemy import text
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import Base, engine, get_db
from . import models, schemas

app = FastAPI(
    title="Downhill Diary API",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
    # создаём таблицы, если их нет
    Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["system"])
def health_check(db: Session = Depends(get_db)):
    """
    Healthcheck:
    - выполняет SELECT 1 через SQLAlchemy text()
    - возвращает "I AM ALIVE" если всё ок, иначе 500
    """
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=500, detail="I AM DEAD")
    return "I AM ALIVE"


@app.post("/notes", response_model=schemas.BlogNoteRead, tags=["notes"])
def create_note(note: schemas.BlogNoteCreate, db: Session = Depends(get_db)):
    db_note = models.BlogNote(
        title=note.title,
        content=note.content,
        category=note.category,
    )
    db.add(db_note)
    db.flush()  # чтобы получить id
    db.refresh(db_note)
    return db_note


@app.get("/notes", response_model=List[schemas.BlogNoteRead], tags=["notes"])
def list_notes(
    category: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.BlogNote)
    if category:
        cat = category.strip().lower()
        if cat not in {"personal", "article"}:
            raise HTTPException(status_code=400, detail="Unknown category")
        query = query.filter(models.BlogNote.category == cat)
    return query.order_by(models.BlogNote.created_at.desc()).all()


@app.get("/notes/latest", response_model=schemas.BlogNoteRead | None, tags=["notes"])
def latest_note(db: Session = Depends(get_db)):
    note = (
        db.query(models.BlogNote)
        .order_by(models.BlogNote.created_at.desc())
        .limit(1)
        .one_or_none()
    )
    return note

