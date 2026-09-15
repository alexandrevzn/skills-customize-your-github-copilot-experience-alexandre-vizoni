from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
]


@app.get("/")
def read_root():
    return {"message": "Books API is running"}


@app.get("/books")
def list_books():
    return books


# TODO: Add POST /books using the Book model.
# TODO: Add GET, PUT, and DELETE endpoints for /books/{book_id}.
