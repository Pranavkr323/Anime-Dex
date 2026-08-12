from fastapi import APIRouter, Depends
from app.schemas import ApiKeyResponse, CreateApiKey
from app.dependencies import get_current_user
from app.utils import create_api_key
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app import crud

router = APIRouter(
    prefix= "/api_key",
    tags=["API Key"]
)

@router.post(
    "/api_keys",
    response_model=ApiKeyResponse
)
def create_apikey(
    data: CreateApiKey,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    apikey = create_api_key()
    crud.apikey(db, apikey['key_id'],
                    apikey['hashed_api_key'],
                    current_user.id,
                    data.name)
    return {"api_key": f"ak_{apikey['key_id']}_{apikey['api_key']}"}
