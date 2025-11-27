from sqlalchemy.orm import Session
# from . import models

# TODO: Implement CRUD operations

def create_book(db: Session, title: str, author: str):
    """
    Create a new book record.
    """
    # db_book = models.Book(title=title, author=author)
    # db.add(db_book)
    # db.commit()
    # db.refresh(db_book)
    # return db_book
    pass

def get_books(db: Session):
    """
    Retrieve all books.
    """
    # return db.query(models.Book).all()
    pass

def get_book(db: Session, book_id: int):
    """
    Retrieve a single book by ID.
    """
    # return db.query(models.Book).filter(models.Book.id == book_id).first()
    pass

# TODO: Add update and delete functions for Book

# TODO: Add CRUD functions for Member
