from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(account_sid, auth_token)

def send_whatsapp_message(to_number: str, message: str):
    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=f"whatsapp:{to_number}"
    )
    return message.sid
