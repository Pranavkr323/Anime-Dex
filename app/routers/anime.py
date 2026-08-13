from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from app.schemas import AnimeCreate, AnimeGet, AnimeUpdate, AnimePatch
from sqlalchemy.orm import Session
from app import crud
from app.enums import AnimeStatus
from app.dependencies import get_db, get_current_user, get_current_api_key

router = APIRouter(
    prefix= "/anime",
    tags=["Anime"]
)

@router.get(
    "/",
    response_model=List[AnimeGet],
    summary="Get all anime",
    description=(
        "Retrieve all anime from the database. "
        "Optionally filter the results by genre, studio, and status "
        "using query parameters."
    ),
)
def get_anime(
    genre: str | None = None,
    studio: str | None = None,
    status: AnimeStatus | None = None,
    db: Session = Depends(get_db),
):
    """Retrieve all anime with optional filters."""
    return crud.get_anime(db, genre, studio, status)


@router.get(
    "/random",
    response_model=AnimeGet,
    summary="Get a random anime",
    description="Returns a randomly selected anime from the database.",
)
def random_anime(db: Session = Depends(get_db)):
    """Retrieve a Random Anime from database."""
    anime = crud.random_anime(db)
    if anime is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!"
        )
    return anime


@router.get(
    "/top10",
    response_model=List[AnimeGet],
    summary="Get top 10 anime",
    description="Returns the top 10 anime sorted by rating in descending order.",
)
def top_ten(db: Session = Depends(get_db)):
    """Retrieve a list of Top 10 anime."""
    lst = crud.top_ten(db)
    return lst

@router.get(
    "/genres",
    response_model=List[str],
    summary="Get all genres",
    description="Returns a list of all unique anime genres available in the database.",
)
def anime_genre(db: Session = Depends(get_db)):
    """Retrieve all genres from database."""
    return crud.anime_genre(db)

@router.get(
    "/studios",
    response_model=List[str],
    summary="Get all studios",
    description="Returns a list of all unique animation studios available in the database.",
)
def anime_studio(db: Session = Depends(get_db)):
    """Retrieve all studios from database."""
    return crud.anime_studio(db)

@router.get(
    "/statuses",
    response_model=List[AnimeStatus],
    summary="Get all statuses",
    description="Returns all unique anime statuses available in the database.",
)
def anime_status(db: Session = Depends(get_db)):
    """Retrieve all statuses from database."""
    return crud.anime_status(db)

@router.get(
    "/{id}",
    response_model=AnimeGet,
    summary="Get anime by ID",
    description="Retrieve a single anime using its unique ID.",
)
def anime_by_id(id: int, db: Session = Depends(get_db)):
    """Retrieve an anime by its ID."""
    anime = crud.get_anime_by_id(db, id)
    if anime is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!"
        )
    return anime


@router.post(
    "/",
    response_model=AnimeGet,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new anime",
    description="Adds a new anime to the database and returns the created resource.",
    dependencies=[Depends(get_current_user)]
)
def create_anime(anime: AnimeCreate,
                 db: Session = Depends(get_db)):
    """Create a new anime."""
    return crud.create_anime(db, anime)


@router.put(
    "/{id}",
    response_model=AnimeGet,
    summary="Update an anime",
    description="Replaces all fields of an existing anime with the provided data.",
    dependencies=[Depends(get_current_user)]
)
def update_anime(id: int, anime: AnimeUpdate,
                 db: Session = Depends(get_db)):
    """Update an existing anime by replacing all of its fields."""
    to_update_anime = crud.update_anime(db, anime, id)
    if to_update_anime is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found"
        )
    return to_update_anime

@router.patch(
    "/{id}",
    status_code= status.HTTP_200_OK,
    summary= "Update only desired field",
    description= "Updates only requested field, instead of asking for whole"
)

def patch_anime(id: int, anime: AnimePatch,
                db: Session = Depends(get_db),
                user = Depends(get_current_user),
                api_user = Depends(get_current_api_key)):
    """Update an existing anime by replacing desired fields."""
    if api_user.user_id == user.id:
        to_update_anime = crud.patch_anime(db, anime, id)
        if to_update_anime is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found"
            )
        return to_update_anime
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail= "Invalid API Key")

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete an anime",
    description="Deletes the anime with the specified ID from the database."
)
def delete_anime(id: int, db: Session = Depends(get_db),
                 user = Depends(get_current_user),
                 api_user = Depends(get_current_api_key)):
    """Delete the selected anime by id."""
    if api_user.user_id == user.id:

        anime = crud.delete_anime(db, id)
        if anime is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found"
            )
        return {"message": "Anime deleted successfully"}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail= "Invalid API Key")
