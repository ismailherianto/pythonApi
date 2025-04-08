from fastapi import FastAPI
from api import prompt_routes

app = FastAPI()
app.include_router(prompt_routes.router)
