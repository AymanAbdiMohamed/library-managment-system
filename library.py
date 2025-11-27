from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', published_year={self.published_year})>"


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Author(name='{self.name}', birth_year={self.birth_year})>"



book1 = Book(title="1984", author="George Orwell", published_year=1949)
author1 = Author(name="George Orwell", birth_year=1903)
print(book1)
print(author1)