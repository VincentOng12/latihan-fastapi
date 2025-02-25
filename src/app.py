from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config.logger_config import logger

from src.config.pg_config import engine
from src.models import Base
from src.config.app_config import settings

from src.api.v1 import api_router

app = FastAPI(title=f"FastAPI - {settings.APP_ENV}")

# Pastikan tabel sudah ada di database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Aplikasi dimulai!")  # Ini menggantikan @app.on_event("startup")
    await init_db()
    yield
    print("Aplikasi dimatikan!")  # Ini menggantikan @app.on_event("shutdown")

app.include_router(api_router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}
