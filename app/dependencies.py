from app.database import SessionLocal
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from app.utils import verify_token
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User

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
