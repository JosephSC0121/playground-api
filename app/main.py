from fastapi import FastAPI
import uvicorn
from routers import auth_router, user_router, exercises_router, chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(exercises_router.router)
app.include_router(chatbot.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=80, reload=True)

