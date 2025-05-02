from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.llm import get_llm
import os
from typing import Optional

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    model_name: Optional[str] = "nemotron"

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        llm = get_llm(model_name=request.model_name)
        response = llm.invoke(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 