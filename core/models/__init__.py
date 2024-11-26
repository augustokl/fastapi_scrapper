from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from ..settings import get_settings

# models
from .user import *  # noqa


engine = create_engine(str(get_settings().database_url), isolation_level="SERIALIZABLE")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
