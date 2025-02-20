from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
def get_items():
    return {"message": "List of items"}

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"message": f"Detail of item {item_id}"}
