from fastapi import APIRouter, status, HTTPException, Depends
from models.database import  db_dependency
from schemas.schemas import UserBase
from security.auth import get_current_active_user
from typing import Annotated

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get("/users/me/", response_model=UserBase)
async def read_users_me(
    current_user: Annotated[UserBase, Depends(get_current_active_user)]
):
    return current_user