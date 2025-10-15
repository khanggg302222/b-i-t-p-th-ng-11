from fastapi import HTTPException
from backend.model import User
import backend.repository as repository

def create_user(user: User):
    data = user.dict()
    result = repository.create_user(data)
    return repository.get_user(str(result.inserted_id))  

def get_users(): 
    return repository.get_users()

def get_user(user_id: str): 
    user = repository.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(user_id: str, user: User):
    result = repository.update_user(user_id, user.dict())
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return repository.get_user(user_id) 
def delete_user(user_id: str):
    result = repository.delete_user(user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deletion successful"}
