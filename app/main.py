# from .database import SessionLocal, engine
# from . import models, crud

# TODO: Create tables (if not using Alembic for initial creation, but Alembic is recommended)
# models.Base.metadata.create_all(bind=engine)

def main():
    # db = SessionLocal()
    
    print("--- Library Management System ---")
    
    # TODO: Call your CRUD functions here to test them
    
    # Example:
    # print("Creating a book...")
    # new_book = crud.create_book(db, title="The Great Gatsby", author="F. Scott Fitzgerald")
    # print(f"Created: {new_book.title}")
    
    # print("Listing books...")
    # books = crud.get_books(db)
    # for book in books:
    #     print(f"- {book.title}")

    # db.close()
    pass

if __name__ == "__main__":
    main()
