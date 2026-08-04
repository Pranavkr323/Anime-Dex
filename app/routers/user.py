from fastapi import APIRouter, HTTPException, status, Depends
from app.database import get_db
from app import crud
from sqlalchemy.orm import Session
from app.schemas import UserResponse, UserRegister

router = APIRouter(
    prefix= "/user",
    tags=["User"]
)

@router.post("/register",
          response_model = UserResponse,
          status_code=status.HTTP_201_CREATED,
          description=(
                "Creates a new user if the email is not already registered."
                ),
          )

def register_user(user: UserRegister, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db,user.email) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail= "Email is already registered.")
    return crud.create_user(db,user)
