from app.database import Base
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.enums import AnimeStatus

class Anime(Base):
    __tablename__ = "animes"

    id: Mapped[int] =  mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique = True)
    genre: Mapped[str] = mapped_column(nullable=False)
    episodes: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    studio: Mapped[str] = mapped_column(nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[AnimeStatus] = mapped_column(Enum(AnimeStatus), nullable=False)