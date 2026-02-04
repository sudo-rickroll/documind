from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "DocuMind"
    API_CURRENT: str = "/api/v1"
    MODE: str = "DEV"

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int = 0
    REDIS_PASSWD: Optional[str] = None

    class Config:
        env_file = ".env"
        env_ignore_missing = True
        case_sensitive = True
    
settings = Settings()
