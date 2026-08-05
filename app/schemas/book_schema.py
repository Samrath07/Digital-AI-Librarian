from pydantic import BaseModel
from typing import List, Optional


class BookResponse(BaseModel):
    google_book_id: str
    title: str
    description: Optional[str] = None
    isbn_13: Optional[str] = None
    isbn_10: Optional[str] = None
    price: Optional[float] = None
    category: Optional[List[str]] = None
    authors: Optional[List[str]] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    pages: Optional[int] = None

    class Config:
        from_attributes = True