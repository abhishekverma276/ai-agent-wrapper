from fastapi import FastAPI, HTTPException
from app.schemas import CreateAgentRequest
from app.services.vapi_service import create_vapi_agent
from app.services.retell_service import create_retell_agent

app = FastAPI()

@app.post("/create-agent")
async def create_agent(request: CreateAgentRequest):
    if request.source == "vapi":
        return await create_vapi_agent(request)
    elif request.source == "retell":
        return await create_retell_agent(request)
    else:
        raise HTTPException(status_code=400, detail="Invalid source specified.")
