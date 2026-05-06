from pydantic import BaseModel
from typing import Optional

# Base class for common fields
class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    year: int

# Used when creating a book (what the user sends)
class BookCreate(BookBase):
    pass

# Used when returning a book (what the API sends back, including the ID)
class Book(BookBase):
    id: int

    class Config:
        from_attributes = True # Allows compatibility with SQLAlchemy models