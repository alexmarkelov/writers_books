
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Writer(Base):
    '''Table for keeping information about writres'''
    __tablename__ = "writers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", back_populates="author")


class Book(Base):
    '''Table for keeping information about books'''
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    author_id = Column(Integer, ForeignKey("writers.id"))
    author = relationship("Writer", back_populates="books")
