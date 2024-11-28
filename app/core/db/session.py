from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from app.core.settings import get_settings


settings = get_settings()

engine = create_engine(str(settings.database_url), isolation_level="SERIALIZABLE")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
