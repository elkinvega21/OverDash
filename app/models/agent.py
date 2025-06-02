from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    personality = Column(Text, nullable=True)
    knowledge_base_url = Column(String, nullable=True)