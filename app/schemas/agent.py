from pydantic import BaseModel

class AgentBase(BaseModel):
    name: str
    description: str
    personality: str
    knowledge_base_url: str

class AgentCreate(AgentBase):
    pass

class AgentOut(AgentBase):
    id: int

    class Config:
        orm_mode = True