from sqlalchemy.orm import Session
from . import models
from schemas.schemas import ExercisesBase
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_exercises(db: Session):
    print(db.query(models.Exercise))
    return db.query(models.Exercise)

def create_exercise(db: Session, exercise: ExercisesBase):
    db_exercise = models.Exercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise