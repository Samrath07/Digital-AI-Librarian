from fastapi import FastAPI
from app.routers import books


app = FastAPI(title="Digital AI Librarian", 
              description="Digital AI Librarian is an AI powered application",
              version="1.0.0")

app.include_router(books.router)
