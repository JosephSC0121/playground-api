from fastapi import APIRouter, status, HTTPException
from models.database import  db_dependency
from models.models import User

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db:db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user