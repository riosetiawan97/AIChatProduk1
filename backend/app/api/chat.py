from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.chat_service import chat_service

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        result = chat_service.process_message(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
