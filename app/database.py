from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./animedex.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(bind=engine, autoflush= False, autocommit= False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()