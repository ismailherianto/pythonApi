# app/controllers/prompt_controller.py

from app.models.prompt_model import Prompt
from app.utils.gemini_helper import ask_gemini

def create_prompt_controller(prompt: Prompt):
    # Example processing logic
    answer = ask_gemini(prompt.prompt)
    return {
        "prompt": prompt.prompt,
        "response": answer,
    }

def get_prompt_by_text(prompt_text: str):
    return {
        "prompt_text": prompt_text,
        "message": "Fetched by text"
    }
