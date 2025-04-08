from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/gemini") 
def create_prompt(prompt: Prompt):
    return {"data": prompt, "message": "Prompt send successfully."}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/prompt/{prompt_text}")
def get_prompt(prompt_text: str):
    return {"prompt_text": prompt_text}
