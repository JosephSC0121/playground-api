from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from routers import auth_router, user_router, exercises_router, chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/helloworld", response_class=HTMLResponse)
def health_checker():
    return "<p> Hola mundo!! </p>"


origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    'http://37.27.11.226:5173'
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
    uvicorn.run('main:app', host="localhost", port=8080, reload=True)

