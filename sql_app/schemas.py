
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class Book(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


class Writer(BaseModel):
    id: int
    name: str
    books: List[Book] = []
    class Config:
        orm_mode = True
