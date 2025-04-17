import httpx
from app.config import VAPI_API_KEY
from app.schemas import CreateAgentRequest

async def create_vapi_agent(request: CreateAgentRequest):
    url = "https://api.vapi.ai/assistants"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": request.name,
        "description": request.description,
        "voice": request.voice,
        "model": request.model
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
