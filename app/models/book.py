from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from app.database import Base


class BookDB(Base):

    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True),
    title = Column(String, index=True, nullable=False),
    description = Column(String, index=True),
    price = Column(Float, index=True, nullable=False),
    category = Column(String, index=True, nullable=False),
    pages = Column(Integer, index=True, nullable=False),
    publisher = Column(String, index=True, nullable=False),
    publish_date = Column(String, index=True, nullable=False),



