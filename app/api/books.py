from typing import Annotated, Sequence

from fastapi import APIRouter, Query
from sqlmodel import select

from app.core.db.session import SessionDep
from app.core.models import Book


router = APIRouter()


@router.get("/books/", tags=["books"], response_model=Sequence[Book])
async def read_books(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Book]:
    return session.exec(select(Book).offset(offset).limit(limit)).all()
