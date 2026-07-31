from pydantic import BaseModel
from typing import List, Optional


class BookResponse(BaseModel):
    google_id: str
    title: str
    authors: Optional[List[str]] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None

    class Config:
        from_attributes = True