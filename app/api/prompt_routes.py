# app/routes/prompt_routes.py

from fastapi import APIRouter
from app.models.prompt_model import Prompt
from app.controllers import prompt_controller

router = APIRouter()

@router.post("/gemini")
def create_prompt(prompt: Prompt):
    return prompt_controller.create_prompt_controller(prompt)

@router.get("/prompt/{prompt_text}")
def get_prompt(prompt_text: str):
    return prompt_controller.get_prompt_by_text(prompt_text)
