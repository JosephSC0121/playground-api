from pydantic import BaseModel

class CreateUserRequest(BaseModel):
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