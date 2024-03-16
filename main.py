from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import auth

app = FastAPI()
app.include_router(auth.router)


models.Base.metadata.create_all(bind=engine)

class ExercisestBase(BaseModel):
    title : str
    description: str
    dificulty: str
    languaje: str

class UserBase(BaseModel):
    name : str
    email : str
    username : str
    hashed_password : str

class SolutionBase(BaseModel):
    user_id : int
    exersice_id : int
    code : str
    date_send : str
    result : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db:db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user