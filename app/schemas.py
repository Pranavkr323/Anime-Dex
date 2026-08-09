from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import datetime
from app.enums import AnimeStatus

CURRENT_YEAR = datetime.now().year

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

    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseModel):
    email: EmailStr


class UserLogin(UserBase):
    password: str = Field(..., min_length = 8)

class UserRegister(UserBase):
    username: str = Field(..., min_length = 2)
    password: str = Field(..., min_length = 8)

class UserResponse(UserBase):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
