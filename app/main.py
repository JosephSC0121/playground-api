from fastapi import FastAPI
import routers.auth_router as auth

app = FastAPI()
app.include_router(auth.router)





