from fastapi import FastAPI

from src.config.logger_config import logger

from src.api.v1 import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}
