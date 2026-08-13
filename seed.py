from app.database import SessionLocal
from app.models import Anime
from app.enums import AnimeStatus


anime_data = [
    Anime(
        title="Naruto",
        genre="Action",
        episodes=220,
        rating=8.3,
        studio="Pierrot",
        release_year=2002,
        status=AnimeStatus.COMPLETED,
    ),
    Anime(
        title="One Piece",
        genre="Adventure",
        episodes=1130,
        rating=9.0,
        studio="Toei Animation",
        release_year=1999,
        status=AnimeStatus.ONGOING,
    ),
    Anime(
        title="Attack on Titan",
        genre="Action",
        episodes=89,
        rating=9.1,
        studio="MAPPA",
        release_year=2013,
        status=AnimeStatus.COMPLETED,
    ),
    Anime(
        title="Demon Slayer",
        genre="Action",
        episodes=63,
        rating=8.6,
        studio="Ufotable",
        release_year=2019,
        status=AnimeStatus.ONGOING,
    ),
    Anime(
        title="Death Note",
        genre="Psychological",
        episodes=37,
        rating=8.7,
        studio="Madhouse",
        release_year=2006,
        status=AnimeStatus.COMPLETED,
    ),
    Anime(
        title="Jujutsu Kaisen",
        genre="Action",
        episodes=47,
        rating=8.6,
        studio="MAPPA",
        release_year=2020,
        status=AnimeStatus.ONGOING,
    ),
    Anime(
        title="Steins Gate",
        genre="Sci-Fi",
        episodes=24,
        rating=9.0,
        studio="White Fox",
        release_year=2011,
        status=AnimeStatus.COMPLETED,
    ),
    Anime(
        title="My Hero Academia",
        genre="Action",
        episodes=170,
        rating=8.0,
        studio="Bones",
        release_year=2016,
        status=AnimeStatus.COMPLETED,
    ),
    Anime(
        title="Solo Leveling",
        genre="Fantasy",
        episodes=25,
        rating=8.8,
        studio="A-1 Pictures",
        release_year=2024,
        status=AnimeStatus.ONGOING,
    ),
    Anime(
        title="Frieren",
        genre="Fantasy",
        episodes=28,
        rating=9.3,
        studio="Madhouse",
        release_year=2023,
        status=AnimeStatus.ONGOING,
    ),
]


db = SessionLocal()

try:
    db.add_all(anime_data)
    db.commit()
    print("Demo anime data inserted successfully!")

finally:
    db.close()
