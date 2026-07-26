from fastapi import FastAPI, HTTPException, status
from data import anime_list
from random import choice
from models import Anime, AnimeCreate, AnimeStatus
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {
            "message": "Welcome to AnimeDex API"
            }

@app.get("/anime", response_model= List[Anime], summary="Get all anime or filter by genre, studio, and status")

def get_anime(
    genre: str = None,
    anime_status: AnimeStatus = None,
    studio: str = None,
):
    
    if genre is None and anime_status is None and studio is None:
        return anime_list

    res = []

    for anime in anime_list:
        if genre and anime["genre"] != genre:
            continue

        if anime_status and anime["status"] != anime_status.value:
            continue

        if studio and anime["studio"] != studio:
            continue

        res.append(anime)

    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No anime found matching the given filter(s)."
        )

    return res

@app.get("/anime/random",response_model= Anime)

def get_anime():
    return choice(anime_list)

@app.get("/anime/top10",response_model= List[Anime])

def top_animes():
    sorted_list = sorted(anime_list, key=lambda x: x['rating'], reverse=True)
    return sorted_list[:10]

@app.get("/anime/genres",response_model= List[str])

def all_genres():

    genre = []

    for anime in anime_list:
        genre.append(anime['genre'])

    return sorted(set(genre))

@app.get("/anime/status",response_model= List[str])

def all_status():

    status = []

    for anime in anime_list:
        status.append(anime['status'])

    return sorted(set(status))

@app.get("/anime/studio",response_model= List[str])

def all_studio():

    studio = []

    for anime in anime_list:
        studio.append(anime['studio'])

    return sorted(set(studio))
        
@app.get("/anime/{id}",response_model= Anime)

def anime_by_id(id: int):

    for anime in anime_list:
        if anime['id'] == id:
            return anime
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = "Item not found!")

@app.post("/anime", response_model= Anime, status_code= status.HTTP_201_CREATED)
def create_anime(new_anime: AnimeCreate):
    largest_item = max(anime_list, key = lambda x: x['id'])
    largest_id = largest_item['id']
    new_id = largest_id + 1
    new_anime_dic = new_anime.model_dump()
    new_anime_dic['id'] = new_id
    created_anime = Anime(**new_anime_dic)
    anime_list.append(created_anime.model_dump())
    return created_anime 

@app.put("/anime/{id}", response_model= Anime, status_code= status.HTTP_200_OK)
def update_anime(id: int, updated_anime: AnimeCreate):
    for index,anime in enumerate(anime_list):
        if anime['id'] == id:
            updated_anime_dict = updated_anime.model_dump()
            updated_anime_dict['id'] = id
            updated = Anime(**updated_anime_dict)
            anime_list[index] = updated.model_dump()
            return updated
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Anime not found")

@app.delete("/anime/{id}", status_code= status.HTTP_200_OK)
def delete_anime(id: int):
    for index,anime in enumerate(anime_list):
        if anime['id'] == id:
            anime_list.pop(index)
            return {"message": "Anime deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found")