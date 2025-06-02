from fastapi import FastAPI
from app.routes import agent

app = FastAPI(title="Agent Builder API")
app.include_router(agent.router, prefix="/api/v1", tags=["Agents"])