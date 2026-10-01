from typing import List
from db import engine
from sqlalchemy import Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    """Base class for all models."""

class User(Base):
    """User Model"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String)
    user_type: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean)

    books: Mapped[List["Book"]] = relationship("Book", back_populates="users")

class Book(Base):
    """Book Model"""
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(30))
    year: Mapped[int] = mapped_column(Integer)
    author: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(100))

    user: Mapped[List["User"]] = relationship("User", back_populates="books")

Base.metadata.create_all(bind=engine)

# User.books = relationship("Book", order_by=Book.id, back_populates="users")

# class Order(Base):
#     """Order Model"""
#     __tablename__ = "orders"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
#     book_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'))
#     quantity: Mapped[int] = mapped_column(Integer)
#     total_price: Mapped[float] = mapped_column(Float)

#     book: Mapped[List["Book"]] = relationship("Book", back_populates="orders")
