from pydantic import BaseModel
from typing import Optional, List

class ConversationNodeBase(BaseModel):
    user_input: str
    agent_response: str
    parent_id: Optional[int] = None

class ConversationNodeCreate(ConversationNodeBase):
    agent_id: int

class ConversationNodeOut(ConversationNodeBase):
    id: int
    children: List['ConversationNodeOut'] = []

    class Config:
        orm_mode = True

ConversationNodeOut.update_forward_refs()
