from fastapi import APIRouter, HTTPException, status, Depends
from app.dependencies import get_db
from app import crud
from sqlalchemy.orm import Session
from app.schemas import UserResponse, UserRegister, UserLogin, TokenResponse
from app.utils import create_access_token

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

@router.post("/login",
          response_model = TokenResponse,
          status_code=status.HTTP_200_OK,
          description=(
                "Login a user after verifying the credentials"
                ),
          )

def login_user(user: UserLogin, db: Session = Depends(get_db)):
    response = crud.verify_user(db,user)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token({'sub': response.username})
    data = {
            "access_token": access_token,
            "token_type": "bearer"
        }
    return data
