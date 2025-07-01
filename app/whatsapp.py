import os
from dotenv import load_dotenv
import requests

load_dotenv()

def send_whatsapp_message(to: str, message: str):
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM")

    print("Using TWILIO_FROM:", from_number)  

    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
    data = {
        "From": from_number,
        "To": to,
        "Body": message
    }

    response = requests.post(url, data=data, auth=(sid, token))

    print(response.status_code, response.text)
