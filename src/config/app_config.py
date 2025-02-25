import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Pilih mode aplikasi (default: dev)
APP_ENV = os.getenv("APP_ENV", "dev")

# Muat file .env berdasarkan mode
env_file = f".env.{APP_ENV}"
load_dotenv(env_file)

class Settings(BaseSettings):
    APP_ENV: str = os.getenv("APP_ENV")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_URL_SYNC: str = os.getenv("DATABASE_URL_SYNC") # for alembic
    APP_NAME: str = os.getenv("APP_NAME")
    DEBUG: bool = os.getenv("DEBUG") == "True"

    class Config:
        env_file = env_file  

settings = Settings()

print(f"Loaded config from {env_file}: ENV={settings.APP_ENV}, DEBUG={settings.DEBUG}")