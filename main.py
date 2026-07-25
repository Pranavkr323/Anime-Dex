from fastapi import FastAPI, HTTPException, status
from data import anime_list
from random import choice

app = FastAPI()

@app.get("/")
def home():
    return {
            "message": "Welcome to AnimeDex API"
            }

@app.get("/anime")

def get_anime(
    genre: str = None,
    anime_status: str = None,
    studio: str = None,
):
    
    if genre is None and anime_status is None and studio is None:
        return anime_list

    res = []

    for anime in anime_list:
        if genre and anime["genre"] != genre:
            continue

        if anime_status and anime["status"] != anime_status:
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

@app.get("/anime/random")

def get_anime():
    return choice(anime_list)

@app.get("/anime/top10")

def top_animes():
    sorted_list = sorted(anime_list, key=lambda x: x['rating'], reverse=True)
    return sorted_list[:10]

@app.get("/anime/genres")

def all_genres():

    genre = []

    for anime in anime_list:
        genre.append(anime['genre'])

    return sorted(set(genre))

@app.get("/anime/status")

def all_status():

    status = []

    for anime in anime_list:
        status.append(anime['status'])

    return sorted(set(status))

@app.get("/anime/studio")

def all_studio():

    studio = []

    for anime in anime_list:
        studio.append(anime['studio'])

    return sorted(set(studio))
        
@app.get("/anime/{id}")

def anime_by_id(id: int):

    for anime in anime_list:
        if anime['id'] == id:
            return anime
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = "Item not found!")
        
