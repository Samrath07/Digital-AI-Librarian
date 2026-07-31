from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.book_schema import BookResponse
from app.models.book import Book
from app.crud.books import fetch_books


router = APIRouter(prefix='/books', tags=['Books'])

@router.get("/", response_model=list[BookResponse],status_code=status.HTTP_200_OK)
async def get_books(db: Session = Depends(get_db)):
    try:
        books = await fetch_books(db)
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))