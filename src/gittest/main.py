from fastapi import FastAPI
from .model import Book

BOOKS = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen"),
    Book(id=5, title="The Hobbit", author="J.R.R. Tolkien"),
]
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books")
def get_all_books():
    return BOOKS

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def create_book(book: Book):
    BOOKS.append(book)
    return book