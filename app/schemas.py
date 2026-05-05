from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    # Shared properties for books, used for data validation
    title: str = Field(..., example="The Clean Coder")
    author: str = Field(..., example="Robert C. Martin")
    description: Optional[str] = None
    year: int = Field(..., gt=1800, le=2026)

class BookCreate(BookBase):
    # Schema for creating a new book (no ID required from user)
    pass

class Book(BookBase):
    # Schema for returning book data to the client (includes DB ID)
    id: int

    class Config:
        # Tells Pydantic to read data even if it's not a dict (like an ORM model)
        orm_mode = True