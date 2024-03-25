from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.database import Base
from alembic import op

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    aboutme = Column(String(255), default="Soy nuevo")
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    level = Column(Float, default=0)
    hashed_password = Column(String(70))

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(70))
    description = Column(String(255))
    dificulty = Column(String(20))
    languaje = Column(String(30))

class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, primary_key=True, index=True) 
    user_id = Column(ForeignKey("users.id"))
    exercise_id = Column(ForeignKey("exercises.id"))
    code = Column(String(1000))
    date_send = Column(String(50))
    result = Column(String(20))
