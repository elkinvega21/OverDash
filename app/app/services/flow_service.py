from sqlalchemy.orm import Session
from app.crud import flow
from app.schemas import flow as flow_schema

def create_flow_node(db: Session, node_data: flow_schema.ConversationNodeCreate):
    return flow.create_node(db, node_data)

def get_full_flow(db: Session, agent_id: int):
    return flow.get_node_tree(db, agent_id)
