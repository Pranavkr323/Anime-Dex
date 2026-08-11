from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import select, func
from app.enums import AnimeStatus
from app.utils import hash_password, verify_password
import logging

logger = logging.getLogger(__name__)

# get all Animes
def get_anime(
    db: Session,
    genre: str | None = None,
    studio: str | None = None,
    status: AnimeStatus | None = None,
):
    statement = select(models.Anime)
    if genre:
        statement = statement.where(models.Anime.genre == genre)
    if studio:
        statement = statement.where(models.Anime.studio == studio)
    if status:
        statement = statement.where(models.Anime.status == status)
    return db.execute(statement).scalars().all()


# Get Anime by id
def get_anime_by_id(db: Session, anime_id: int):
    try:
        statement = select(models.Anime).where(models.Anime.id == anime_id)
        return db.execute(statement).scalar_one_or_none()
    except Exception:
        logger.exception("Failed to get anime by id: %s", anime_id)
        raise

# Get Random Anime
def random_anime(db: Session):
    # all_animes = get_anime(db)
    # if not all_animes:
    #     return None
    # return random.choice(all_animes)
    statement = select(models.Anime).order_by(func.random()).limit(1)
    return db.execute(statement).scalar_one_or_none()

#  Top 10 Anime
def top_ten(db:Session):
    statement = select(models.Anime).order_by(models.Anime.rating.desc()).limit(10)
    return db.execute(statement).scalars().all()

# Get list of Genre
def anime_genre(db: Session):
    try:
        statement = select(models.Anime.genre).distinct()
        return db.execute(statement).scalars().all()
    except Exception:
        logger.exception("Failed to get list of genres")
        raise

# Get list of Studio
def anime_studio(db: Session):
    try:
        statement = select(models.Anime.studio).distinct()
        return db.execute(statement).scalars().all()
    except Exception:
        logger.exception("Failed to get list of studios")
        raise

# Get list of Status
def anime_status(db: Session):
    statement = select(models.Anime.status).distinct()
    return db.execute(statement).scalars().all()

# Create Anime
def create_anime(db: Session, anime: schemas.AnimeCreate):
    try:
        new_anime = models.Anime(**anime.model_dump())
        db.add(new_anime)
        db.commit()
        db.refresh(new_anime)
        return new_anime
    except Exception:
        db.rollback()
        logger.exception("Failed to create new anime")
        raise

def update_anime(db: Session, anime: schemas.AnimeUpdate, anime_id: int):
    try:
        requested_anime = get_anime_by_id(db, anime_id)
        if requested_anime is None:
            return None
        update_data = anime.model_dump()
        for key, value in update_data.items():
            setattr(requested_anime, key, value)
        db.commit()
        db.refresh(requested_anime)
        return requested_anime
    except Exception:
        db.rollback()
        logger.exception("Failed to update anime with id %s", anime_id)
        raise

def delete_anime(db: Session, anime_id: int):
    try:
        requested_anime = get_anime_by_id(db, anime_id)
        if requested_anime is None:
            return None
        db.delete(requested_anime)
        db.commit()
        return requested_anime
    except Exception:
        db.rollback()
        logger.exception("Failed to delete anime with id %s", anime_id)
        raise

def create_user(db: Session, user: schemas.UserRegister):
    try:
        new_user = models.User(
            username = user.username,
            email = user.email,
            hashed_password = hash_password(user.password),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        db.rollback()
        logger.exception("Failed to create user with email: %s", user.email)
        raise

def get_user_by_email(db: Session, email:str):
    try:
        statement = select(models.User).where(models.User.email == email)
        return db.execute(statement).scalar_one_or_none()
    except Exception:
        logger.exception("Failed to get user by email: %s", email)
        raise

def verify_user(db: Session, user: schemas.UserLogin):
    requested_user = get_user_by_email(db, user.email)
    if requested_user is None:
        return None
    if verify_password(user.password, requested_user.hashed_password):
        return requested_user
    else:
        return None
