from fastapi import FastAPI

BOOKS = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}