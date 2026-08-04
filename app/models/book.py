from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from app.database.database import Base
from sqlalchemy.orm import relationship


class Book(Base):

    __tablename__ = "books"
    google_book_id = Column(String, unique=True, nullable=False, index=True)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    isbn_13 = Column(String, unique=True, nullable=True, index=True)
    isbn_10 = Column(String, unique=True, nullable=True, index=True)
    price = Column(Float, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    pages = Column(Integer, index=True, nullable=False)
    language = Column(String(10))
    publisher = Column(String, index=True, nullable=False)
    publish_date = Column(String, index=True, nullable=False)
    authors = relationship("Author", secondary="book_authors", back_populates="books")
    categories = relationship("Category", secondary="book_categories", back_populates="books")






