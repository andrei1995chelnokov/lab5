from pydantic_settings import BaseSettings  # Исправлено: pytandict_settings → pydantic_settings

class Settings(BaseSettings):
    class Config:
        env_file = ".env"

settings = Settings()
