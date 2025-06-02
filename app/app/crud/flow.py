from sqlalchemy.orm import Session
from app import models, schemas

def create_node(db: Session, node: schemas.ConversationNodeCreate):
    db_node = models.ConversationNode(**node.dict())
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node

def get_node_tree(db: Session, agent_id: int):
    all_nodes = db.query(models.ConversationNode).filter(models.ConversationNode.agent_id == agent_id).all()
    node_map = {node.id: node for node in all_nodes}
    root_nodes = []

    for node in all_nodes:
        if node.parent_id:
            parent = node_map.get(node.parent_id)
            if parent:
                parent.children.append(node)
        else:
            root_nodes.append(node)

    return root_nodes
