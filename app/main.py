from fastapi import FastAPI
from routers import books


app = FastAPI("Digital AI Librarian", 
              version="1.0.0", 
              description="Digital AI Librarian is an AI powered application"
              )

app.include.router(books, prefix="/books", tags=["Books"])
