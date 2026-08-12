from app.database import SessionLocal
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, APIKeyHeader
from fastapi import Depends, HTTPException, status
from app.utils import verify_token, verify_password
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User
from app.crud import get_api_key_by_key_id
from app.enums import APIKeyStatus

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials  = Depends(security),
                     db: Session = Depends(get_db)):
    token = credentials.credentials
    claims = verify_token(token)
    username = claims['sub']
    statement = select(User).where(User.username == username)
    user = db.execute(statement).scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user

api_key_header = APIKeyHeader(name="X-API-Key")


def get_current_api_key(
    api_key: str = Depends(api_key_header),
    db: Session = Depends(get_db)
):
    try:
        prefix, key_id, secret = api_key.split("_", 2)

        if prefix != "ak":
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    db_api_key = get_api_key_by_key_id(db, key_id)

    if db_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    if db_api_key.status != APIKeyStatus.ACTIVE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is revoked"
        )

    if not verify_password(secret, db_api_key.hashed_apikey):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return db_api_key
