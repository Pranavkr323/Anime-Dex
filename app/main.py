from fastapi import FastAPI
from app.database import engine, Base
from app.routers import anime, user


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get(
    "/",
    summary="API Home",
    description="Returns a welcome message to verify that the AnimeDex API is running.",
    tags=["General"],
)
def home():
    return {"message": "Welcome to AnimeDex API"}


app.include_router(anime.router)
app.include_router(user.router)
