from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app  = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message": "Hello world"}

@app.get("/books/{id}")
def showBook(id: int):
    return {"data": id}

@app.post("/books")
def insertBook(book: Book):
    return {"message": f"book {book.title} created"}
