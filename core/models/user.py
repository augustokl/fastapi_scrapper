from decimal import Decimal

from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    category: str
    rating: int
    price: Decimal
    tax: Decimal
    currency: str
    title: str
    stock: int
    number_of_reviews: int
    description: str
