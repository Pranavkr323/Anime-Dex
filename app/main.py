from fastapi import FastAPI, HTTPException, status, Depends
from app.database import engine, Base, get_db
from typing import List
from app.schemas import AnimeCreate, AnimeGet, AnimeUpdate
from sqlalchemy.orm import Session
from app import crud 

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
            "message": "Welcome to AnimeDex API"
            }

@app.get("/anime", response_model=List[AnimeGet], summary="Get all anime")

def get_anime(
    db: Session = Depends(get_db),
):
    return crud.get_anime(db)
    
@app.get("/anime/{id}",response_model= AnimeGet)

def anime_by_id(id: int, db: Session = Depends(get_db)):
    anime = crud.get_anime_by_id(db,id)
    if anime is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "Item not found!")
    return anime

@app.post("/anime", response_model= AnimeGet, status_code= status.HTTP_201_CREATED)

def create_anime(anime: AnimeCreate, db: Session = Depends(get_db)):
    return crud.create_anime(db, anime)

@app.put("/anime/{id}", response_model= AnimeGet)

def update_anime(id: int, anime: AnimeUpdate, db: Session = Depends(get_db)):
    to_update_anime = crud.update_anime(db, anime, id)
    if to_update_anime is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Anime not found")
    return to_update_anime

@app.delete("/anime/{id}", status_code= status.HTTP_200_OK)

def delete_anime(id: int, db: Session = Depends(get_db)):
    anime = crud.delete_anime(db, id)
    if anime is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found")
    return {"message": "Anime deleted successfully"}