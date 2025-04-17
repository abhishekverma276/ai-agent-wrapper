from pydantic import BaseModel
from typing import Optional, Literal

class CreateAgentRequest(BaseModel):
    name: str
    description: str
    voice: str
    model: Optional[str]
    source: Literal["vapi", "retell"]
