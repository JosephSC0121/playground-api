from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from models.database import  db_dependency, get_db
from models import querys
from schemas import schemas
from security.auth import get_current_user
from typing import Annotated

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get("/user", response_model=schemas.User)
def read_user_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = querys.get_user(db, user_id=current_user["id"])
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user