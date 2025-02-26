from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"Detail of user {user_id}"}

@router.post("/")
def create_user(payload: dict):
    print(payload)
    return {"message": "User created", "user": payload}
