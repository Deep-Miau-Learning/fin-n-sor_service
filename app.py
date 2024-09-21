from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from db_connection import get_collection


class PromptDto(BaseModel):
    prompt: str

class PromptResponseEntity():
    def __init__(self, user_id: str, prompt: str, response: str, created_at: datetime, updated_at: datetime):
        self.user_id = user_id
        self.prompt = prompt
        self.response = response
        self.created_at = created_at
        self.updated_at = updated_at

class FinancialProfileEntity():
    def __init__(self, user_id: str, output: str, created_at: datetime, updated_at: datetime):
        self.user_id = user_id
        self.output = output
        self.created_at = created_at
        self.updated_at = updated_at

app = FastAPI()

@app.post("/api/prompt-response/")
def create_prompt_response(prompt_dto: PromptDto):
    prompt_collection = get_collection("prompt_response")

    prompt_response = PromptResponseEntity(
        "1", 
        prompt_dto.prompt,
        "",
        datetime.now(),
        datetime.now()
    )

    prompt_collection.insert_one(prompt_response)

    return {"response": ""}

@app.get("/api/financial-profile/{user_id}")
def get_financial_profile(user_id: str):
    financial_profile_collection = get_collection("financial_profile")
    prompt_response_collection = get_collection("prompt_response")

    prompt_responses = prompt_response_collection.find({"user_id": user_id})

    financial_profile = FinancialProfileEntity(
        user_id,
        "",
        datetime.now(),
        datetime.now()
    )

    financial_profile_collection.insert_one(financial_profile)

    return financial_profile
