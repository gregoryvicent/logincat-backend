from fastapi import FastAPI
from router.user import user

app = FastAPI()

app.include_router(user)
