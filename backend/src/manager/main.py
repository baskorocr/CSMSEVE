# main.py
from fastapi import FastAPI
from manager.controllers.status import router as status_router


app = FastAPI()

app.include_router(status_router)  # Prefix is optional
