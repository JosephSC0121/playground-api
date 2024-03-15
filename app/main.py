from fastapi import FastAPI
from v1.endpoints.auth import router as auth_router
from v1.endpoints.user import router as user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
