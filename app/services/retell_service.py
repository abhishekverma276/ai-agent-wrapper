import httpx
from app.config import RETELL_API_KEY
from app.schemas import CreateAgentRequest

async def create_retell_agent(request: CreateAgentRequest):
    url = "https://api.retellai.com/agents"
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "agent_name": request.name,
        "voice_id": request.voice,
        "response_engine": {
            "type": "retell-llm",
            "llm_id": request.model
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
