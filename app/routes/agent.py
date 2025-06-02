from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.agent import AgentCreate, AgentOut
from app.crud.agent import create_agent, get_agent, get_all_agents, delete_agent
from app.database import get_db

router = APIRouter()

@router.post("/agents", response_model=AgentOut)
def create(agent: AgentCreate, db: Session = Depends(get_db)):
    return create_agent(db, agent)

@router.get("/agents/{agent_id}", response_model=AgentOut)
def read(agent_id: int, db: Session = Depends(get_db)):
    db_agent = get_agent(db, agent_id)
    if not db_agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.get("/agents", response_model=list[AgentOut])
def read_all(db: Session = Depends(get_db)):
    return get_all_agents(db)

@router.delete("/agents/{agent_id}")
def remove(agent_id: int, db: Session = Depends(get_db)):
    deleted = delete_agent(db, agent_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Deleted successfully"}
