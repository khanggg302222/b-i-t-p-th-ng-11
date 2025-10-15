from fastapi import APIRouter
from backend.model import User
import backend.service as service

# Tạo router riêng cho user
router = APIRouter()


@router.post("/users")
def create_user(user: User):
    return service.create_user(user)

@router.get("/users")
def get_users():
    return service.get_all_users()

@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return service.update_user(user_id, user)

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id)
