from fastapi import APIRouter
from src.api.v1.endpoints import users, items

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(items.router)
