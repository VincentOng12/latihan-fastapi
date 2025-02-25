from fastapi import APIRouter
from src.api.v1.endpoints import users, items

url_prefix_1 = "/api/v1"

api_router = APIRouter()
api_router.include_router(users.router, prefix=f"{url_prefix_1}/users", tags=["users"])
api_router.include_router(items.router, prefix=f"{url_prefix_1}/items", tags=["items"])
