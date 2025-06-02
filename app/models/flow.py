from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class ConversationNode(Base):
    __tablename__ = "conversation_nodes"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    parent_id = Column(Integer, ForeignKey("conversation_nodes.id"), nullable=True)

    user_input = Column(String, nullable=False)
    agent_response = Column(Text, nullable=False)

    children = relationship("ConversationNode", backref="parent", remote_side=[id])
