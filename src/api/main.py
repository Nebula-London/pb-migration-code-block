from enum import Enum
from typing import Optional
from fastapi import FastAPI, Depends
from session import get_db
from sqlalchemy.orm import Session
from models import Book
from pydantic import BaseModel
from crud import book_info_update, new_book_added, delete_book

class UserType(str, Enum):
    """User Type"""
    ADMIN = "admin"
    USER = "user"

class BookResponse(BaseModel):
    """Book return type"""
    id: int
    user_id: int
    name: str
    year: int
    author: str
    price: float
    quantity: int
    description: str

class BookReq(BaseModel):
    """Book request type"""
    id: Optional[int]
    user_id: Optional[int]
    name: Optional[str]
    year: Optional[int]
    author: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    description: Optional[str]

app = FastAPI()

@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    """Get all books."""
    return db.query(Book).all()

@app.get("/book/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a book by their ID. book_id is automatically converted to int."""
    return db.query(Book).filter(Book.id == book_id).all()

# @app.get("/books/{book_id}/orders/{order_id}")
# def get_user_order(book_id: int, order_id: int, db: Session = Depends(get_db)):
#     """get a specific order for a specific book"""
#     return db.query(Book).filter(Book.id == book_id).filter(Order.id == order_id).all()

@app.post("/book/", response_model=BookResponse)
def create_book_endpoint(book_detail: BookReq, db: Session = Depends(get_db)):
    """Create new book"""
    new_book = Book(
        name=book_detail.name,
        year=book_detail.year,
        author=book_detail.author,
        price=book_detail.price,
        quantity=book_detail.quantity,
        description=book_detail.description
    )
    added_book = new_book_added(db, new_book)
    return added_book

@app.patch("/books/{book_id}", response_model=BookResponse)
def update_book_endpoint(book_detail: BookReq, db: Session = Depends(get_db)):
    """Change the book information"""
    change_book = Book(
        name=book_detail.name,
        year=book_detail.year,
        author=book_detail.author,
        price=book_detail.price,
        quantity=book_detail.quantity,
        description=book_detail.description)
    changed_book = book_info_update(db, change_book)
    return changed_book

@app.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by their ID."""
    return delete_book(db, book_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)