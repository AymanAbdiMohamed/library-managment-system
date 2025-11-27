from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO: Define your database URL here
# For SQLite, it looks like: "sqlite:///./library.db"
DATABASE_URL = "sqlite:///./library.db"

# TODO: Create the SQLAlchemy engine
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # Hint: connect_args is needed for SQLite

# TODO: Create a SessionLocal class
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TODO: Create a Base class for your models to inherit from
# Base = declarative_base()

def get_db():
    """
    Generator function to get a database session.
    This is useful for dependency injection or context management.
    """
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
    pass
