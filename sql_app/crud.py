
from sqlalchemy.orm import Session
import models, schemas


def get_writer(db: Session, writer_id: int):
    return db.query(models.Writer).filter(models.Writer.id == writer_id)\
           .first()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()
