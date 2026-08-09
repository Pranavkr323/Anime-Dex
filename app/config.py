from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRY_MINUTES: int

    class Config:
        env_file = '.env'

settings = Settings()
