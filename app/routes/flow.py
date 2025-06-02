from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import flow_service
from app.schemas.flow import ConversationNodeCreate, ConversationNodeOut
from typing import List

router = APIRouter(prefix="/flow", tags=["Flow"])

@router.post("/", response_model=ConversationNodeOut)
def create_node(node: ConversationNodeCreate, db: Session = Depends(get_db)):
    return flow_service.create_flow_node(db, node)

@router.get("/{agent_id}", response_model=List[ConversationNodeOut])
def get_flow(agent_id: int, db: Session = Depends(get_db)):
    return flow_service.get_full_flow(db, agent_id)
