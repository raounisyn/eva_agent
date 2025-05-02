from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from chatbot import Chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Chatbot API",
    description="API for the AI Chatbot powered by Nemotron",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize chatbot
chatbot = Chatbot()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    conversation_history: List[Message]

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Chatbot API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Process the message
        response = chatbot.process_message(request.message)
        
        # Get conversation history
        history = chatbot.get_conversation_history()
        
        # Convert history to Message objects
        conversation_history = [
            Message(role=msg["role"], content=msg["content"])
            for msg in history
        ]
        
        return ChatResponse(
            response=response,
            conversation_history=conversation_history
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=List[Message])
async def get_history():
    try:
        history = chatbot.get_conversation_history()
        return [
            Message(role=msg["role"], content=msg["content"])
            for msg in history
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clear")
async def clear_history():
    try:
        global chatbot
        chatbot = Chatbot()  # Reinitialize the chatbot
        return {"message": "Chat history cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 