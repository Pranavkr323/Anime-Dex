from pwdlib import PasswordHash
from joserfc import jwt, jwk
from joserfc.errors import JoseError, ClaimError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from app.config import settings
from joserfc.jwt import JWTClaimsRegistry

JWT_ALGORITHM = settings.JWT_ALGORITHM
SECRET_KEY = settings.SECRET_KEY
ACCESS_TOKEN_EXPIRY_MINUTES = settings.ACCESS_TOKEN_EXPIRY_MINUTES
JWT_KEY = jwk.import_key(SECRET_KEY, "oct")
password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password,hashed_password)

def create_access_token(data: dict):
    header = {"alg": JWT_ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy()
    payload.update({'exp': expire})
    return jwt.encode(header, payload, JWT_KEY)

def verify_token(token: str):
    try:
        token_obj = jwt.decode(token, JWT_KEY,
                               algorithms=[JWT_ALGORITHM])
        claims_registry = JWTClaimsRegistry(
            exp={"essential": True},
            sub={"essential": True}
        )

        claims_registry.validate(token_obj.claims)

        return dict(token_obj.claims)
    except (JoseError, ClaimError):
        raise HTTPException(
            status_code = 401,
            detail = "Couldn't Validate Credentials")
