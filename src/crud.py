from sqlalchemy.orm import Session
from models import Book

def book_info_update(db: Session, change_book):
    """CRUD for update book information"""
    db.query(Book).filter(Book.id == change_book.id).update({
        Book.name: change_book.name,
        Book.year: change_book.year,
        Book.author: change_book.author,
        Book.price: change_book.price,
        Book.quantity: change_book.quantity,
        Book.description: change_book.description
    })
    db.commit()
    db.refresh(change_book)
    return change_book

def new_book_added(db: Session, new_book):
    """CRUD for create new book"""
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def delete_book(db: Session, book_id):
    """CRUD for delete book"""
    db.query(Book).filter(Book.id == book_id).delete()
    db.commit()
    return {f"message: Book deleted  successfully with book ID {book_id}."}
