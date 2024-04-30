from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database import Base


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    login: Mapped[str]
    name: Mapped[str]
    url: Mapped[str]
    email = mapped_column(String, unique=True, index=True, nullable=True)
    public_repos: Mapped[int]
    public_gists: Mapped[int]
    followers: Mapped[int]
    following: Mapped[int]
