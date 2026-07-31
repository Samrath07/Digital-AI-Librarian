from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book


router = APIRouter()

router.get("/", response_model=list[Book])
async def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books