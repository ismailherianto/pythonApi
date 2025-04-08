# app/controllers/prompt_controller.py

from app.models.prompt_model import Prompt

def create_prompt_controller(prompt: Prompt):
    # Example processing logic
    return {
        "data": prompt,
        "message": "Prompt received successfully."
    }

def get_prompt_by_text(prompt_text: str):
    return {
        "prompt_text": prompt_text,
        "message": "Fetched by text"
    }
