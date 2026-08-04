from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book_schema import BookResponse
from fastapi import HTTPException, status
from sqlalchemy import select 
from app.models.book import Book
import os



async def fetch_books(db: AsyncSession) -> list[BookResponse]:
    try:
        result = await db.execute(select(Book))
        books = result.scalars().all()
        return [BookResponse(google_id=book.google_id, title=book.title) for book in books]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))