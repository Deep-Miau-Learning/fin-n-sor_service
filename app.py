from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from db_connection import get_collection


class PromptDto(BaseModel):
    prompt: str

app = FastAPI()

@app.post("/api/prompt-response/")
def create_prompt_response(prompt_dto: PromptDto):
    prompt_collection = get_collection("prompt_response")

    prompt_response = {
        "prompt": prompt_dto.prompt,
        "response": "",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    prompt_collection.insert_one(prompt_response)

    return {"response": ""}

