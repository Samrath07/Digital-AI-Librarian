from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import dotenv
import os

dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("database", DATABASE_URL)  # Debugging line to check if the environment variable is loaded correctly

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/books_db", echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
Base = declarative_base()

async def get_db(): 
    async with AsyncSessionLocal() as session:
        yield session