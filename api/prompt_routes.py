from fastapi import APIRouter
from models.prompt_model import Prompt
from utils.prompt_utils import process_prompt
from utils.config import settings

router = APIRouter()

@router.post("/gemini")
def create_prompt(prompt: Prompt):
    return process_prompt(prompt)

@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@router.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.get("/prompt/{prompt_text}")
def get_prompt(prompt_text: str):
    return {"prompt_text": prompt_text}
