from sqlalchemy import Column, ForeignKey, Integer
from app.database.database import Base


class BookCategory(Base):
    __tablename__ = "book_category"

    book_id = Column(
        Integer,
        ForeignKey("books.id", ondelete="CASCADE"),
        primary_key=True,
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE"),
        primary_key=True,
    )