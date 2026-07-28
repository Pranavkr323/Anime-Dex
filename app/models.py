from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Anime(Base):
    __tablename__ = "animes"

    id: Mapped[int] =  mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    episodes: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    studio: Mapped[str] = mapped_column(nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)