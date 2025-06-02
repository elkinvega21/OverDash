from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.whatsapp_service import send_whatsapp_message
from app.services.flow_service import get_full_flow

router = APIRouter(prefix="/webhook", tags=["WhatsApp"])

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    user_message = form.get("Body")
    from_number = form.get("From").replace("whatsapp:", "")

    # Usamos un agente ficticio con ID 1 por ahora
    flow_tree = get_full_flow(db, agent_id=1)

    def search_response(nodes, input_text):
        for node in nodes:
            if node.user_input.lower() in input_text.lower():
                return node.agent_response
            response = search_response(node.children, input_text)
            if response:
                return response
        return None

    reply = search_response(flow_tree, user_message) or "No entendí, ¿puedes repetirlo?"
    send_whatsapp_message(from_number, reply)
    return "OK"
