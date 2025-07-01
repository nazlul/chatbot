import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(message: str) -> str:
    message_lower = message.lower().strip()

    greetings = ["hi", "hello", "hey", "heyy", "hii", "sup", "yo", "hola", "good morning", "good evening", "good afternoon"]
    help_phrases = [
        "what can you do", "i'm confused", "i need help", "what do i do",
        "what now", "how does this work", "help me", "what services",
        "tell me more", "how to use", "faq", "support", "help"
    ]

    if any(greet in message_lower for greet in greetings):
        return "Thanks for reaching out! How can I assist you today?"

    if any(phrase in message_lower for phrase in help_phrases):
        return (
            "🤖 I'm here to help! Here's what I can assist you with:\n\n"
            "📖 *FAQ Menu*\n"
            "Reply with a number:\n"
            "1️⃣ What are your working hours?\n"
            "2️⃣ How can I cancel my appointment?\n"
            "3️⃣ What services do you offer?\n"
            "4️⃣ Is online consultation available?\n\n"
            "Or reply with 'Book' to schedule a session."
        )

    if "book" in message_lower or "appointment" in message_lower:
        return "🗓️ Sure! Please reply with your *name* and *preferred date/time*."

    if "doctor" in message_lower or "consult" in message_lower:
        return "👨‍⚕️ We have certified professionals available. Reply 'Book' to set up a consultation."

    if "pricing" in message_lower or "price" in message_lower or "cost" in message_lower:
        return "💰 Our services start at ₹999. Reply 'FAQ' to see common questions or 'Book' to schedule a session."

    if "location" in message_lower:
        return "📍 We're located at 123 Wellness Street, Health City. Google Maps: https://maps.example.com"

    if message_lower == "1":
        return "🕒 We're open Monday to Saturday, 9 AM to 6 PM."

    if message_lower == "2":
        return "❌ To cancel your appointment, reply 'Cancel + [Your Name]'. We'll confirm shortly."

    if message_lower == "3":
        return "🧾 We offer general checkups, specialist consultations, therapy sessions, and lab tests."

    if message_lower == "4":
        return "💻 Yes, we offer online video consultations. Reply 'Book' to schedule one."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant at a medical clinic."},
                {"role": "user", "content": message}
            ],
            max_tokens=120,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ OpenAI API call error:", e)  
        return "⚠️ Sorry, I couldn't understand that. You can reply with 'FAQ' or 'Book' to continue."
