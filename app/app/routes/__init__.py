from . import agent
from fastapi import APIRouter
from . import flow, agent

router = APIRouter()
router.include_router(agent.router)
router.include_router(flow.router)
from . import whatsapp
router.include_router(whatsapp.router)
