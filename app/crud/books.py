from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book_schema import BookResponse
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.book import Book

async def fetch_books(db: Session):
    try:
        result = await db.query(Book).all()
        books = result.fetchall()
        return [BookResponse(google_id=book.google_id, title=book.title) for book in books]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))