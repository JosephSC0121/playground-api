from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    nombres : str
    apellidos : str
    email: str
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ExercisestBase(BaseModel):
    title : str
    description: str
    dificulty: str
    languaje: str

class UserBase(BaseModel):
    id : int
    username : str

class SolutionBase(BaseModel):
    user_id : int
    exersice_id : int
    code : str
    date_send : str
    result : str

class User(BaseModel):
    id : int
    nombres : str
    apellidos : str
    aboutme : str
    username : str
    email: str
    level : float
    