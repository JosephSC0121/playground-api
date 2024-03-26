from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from models.database import  db_dependency, get_db
from models import querys
from schemas import schemas
from security.auth import get_current_user
from typing import Annotated, List

router = APIRouter(
    prefix='/exercises',
    tags=['exercises']
)

@router.get("/exercises", response_model=List[schemas.ExercisesBase])
def read_exercises(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    exercises = querys.get_exercises(db)
    if not exercises:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay ejercicios")
    return exercises


@router.post("/exercises", response_model=schemas.ExercisesBase)
def create_exercise(exercise: schemas.ExercisesBase, db: Session = Depends(get_db)):
    return querys.create_exercise(db=db, exercise=exercise)