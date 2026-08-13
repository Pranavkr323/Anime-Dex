from fastapi import FastAPI
from app.database import engine, Base
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import anime, user, apikey_route
from app.middleware import TimerMiddleware
import logging

app = FastAPI()

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    style="%",
    datefmt="%Y-%m-%d %H:%M",
)

@app.get(
    "/",
    summary="API Home",
    description="Returns a welcome message to verify that the AnimeDex API is running.",
    tags=["General"],
)
def home():
    return {"message": "Welcome to AnimeDex API"}

app.add_middleware(TimerMiddleware)
app.include_router(anime.router)
app.include_router(user.router)
app.include_router(apikey_route.router)
