import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from app.ai import get_ai_response
from app.whatsapp import send_whatsapp_message
from dotenv import load_dotenv

load_dotenv()

print("✅ .env loaded from:", os.path.abspath(".env"))
print("✅ TWILIO_FROM (startup):", os.getenv("TWILIO_FROM"))

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    form = await request.form()
    from_number = form.get("From")
    message = form.get("Body")

    print(f"📩 Message from {from_number}: {message}")

    reply = get_ai_response(message)
    print(f"📨 Message: {reply}")

    send_whatsapp_message(from_number, reply)

    return JSONResponse(content={"status": "success"})

@app.get("/test-send")
def test_send():
    send_whatsapp_message("whatsapp:+919539665011", "Hello! This is a test from your WhatsApp bot.")
    return {"status": "test message sent"}
