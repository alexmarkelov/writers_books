
import uvicorn
from sys import argv
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
import writers_data
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/writers/{id}", response_model=schemas.Writer)
def get_writer(db: Session = Depends(get_db), id: int=1):
    db_writer = crud.get_writer(db, id)
    if not db_writer:
        raise HTTPException(status_code=404, detail="Writer not found") 
    return db_writer


def fill_database():
    db = SessionLocal()
    for writer_id, writer in enumerate(writers_data.writer_list, start=1):
        if not crud.get_writer(db, writer_id):
            db_writer = models.Writer(id=writer_id, name=writer)
            db.add(db_writer)
            db.commit()
    for book_id, author_id_name in enumerate(writers_data.books_list, start=1):
        if not crud.get_book(db, book_id):
            author_id, name = author_id_name
            db_book = models.Book(id=book_id, name=name, author_id=author_id)
            db.add(db_book)
            db.commit()
    db.close()
    pass


if __name__ == "__main__":
    if "init" in argv:
        fill_database()
    uvicorn.run(app, host="127.0.0.1", port=8000)
