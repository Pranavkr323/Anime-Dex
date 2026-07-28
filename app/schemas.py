from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum

CURRENT_YEAR = datetime.now().year

class AnimeStatus(Enum):
    ONGOING = "Ongoing"
    COMPLETED = "Completed"

class AnimeBase(BaseModel):
    title: str = Field(..., min_length=2)
    genre: str = Field(..., min_length=3)
    episodes: int = Field(..., gt=0)
    rating: float = Field(..., ge=0,le=10)
    studio: str = Field(..., min_length=2)
    release_year: int = Field(..., ge=1900, le= CURRENT_YEAR)
    status: AnimeStatus

class AnimeCreate(AnimeBase):
    pass

class AnimeUpdate(AnimeBase):
    pass

class AnimeGet(AnimeBase):
    id: int
    pass

    model_config = ConfigDict(from_attributes=True)