
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price:float
    rating:float

books: List[Book]=[]

@app.get("/")
def read_root():
    return{"message": "Welcome to Book Shope"}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book:Book):
    books.append(book)
    return book

@app.put("/books/{tea_id}")
def update_book(book_id: int,update_book:Book):
    for index,book in enumerate(books):
        if book.id == book_id:
            books[index]=update_book
            return update_book
    return {"error":"Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index,book in enumerate(books):
        if book.id == book_id:
            deleted=books.pop(index)
            return deleted
    return {"error":"Book not found"}