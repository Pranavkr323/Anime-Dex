from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import select

# get all Animes
def get_anime(db: Session):
    statement = select(models.Anime)
    return db.execute(statement).scalars().all()

# Get Anime by id
def get_anime_by_id(db: Session, anime_id: int):
    statement = select(models.Anime).where(models.Anime.id == anime_id)
    return db.execute(statement).scalar_one_or_none()

# Create Anime
def create_anime(db: Session, anime: schemas.AnimeCreate):
    new_anime = models.Anime(**anime.model_dump())
    db.add(new_anime)
    db.commit()
    db.refresh(new_anime)
    return new_anime

def update_anime(db: Session, anime: schemas.AnimeUpdate, anime_id: int):
    requested_anime = get_anime_by_id(db, anime_id)
    if requested_anime is None:
        return None
    update_data = anime.model_dump()
    for key, value in update_data.items():
        setattr(requested_anime, key, value)
    db.commit()
    db.refresh(requested_anime)
    return requested_anime

def delete_anime(db: Session, anime_id: int):
    requested_anime = get_anime_by_id(db, anime_id)
    if requested_anime is None:
            return None
    db.delete(requested_anime)
    db.commit()
    return requested_anime
