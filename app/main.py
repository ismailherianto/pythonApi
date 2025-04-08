from fastapi import FastAPI
from app.api import prompt_routes

app = FastAPI()
app.include_router(prompt_routes.router)
