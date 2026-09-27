# knowledge_base.py
# Aira's knowledge: what she knows and how she answers.

from aira.config import CLINIC_NAME, CLINIC_ADDRESS, CLINIC_PHONE, CLINIC_EMAIL

GREETINGS = [
    f"Hello! I'm Aira, the assistant for {CLINIC_NAME}. How can I help you?",
    f"Hi there! I'm Aira from {CLINIC_NAME}. What can I do for you?",
    f"Welcome to {CLINIC_NAME}! I'm Aira — how can I help today?",
]
# Each intent (key) maps to Aira's answer (value)
RESPONSES = {
    "hours": f"{CLINIC_NAME} is open Monday to Saturday, 9 AM to 8 PM. We are closed on Sundays.",
    "appointment": f"You can book an appointment by calling {CLINIC_PHONE} or visiting the reception desk.",
    "location": f"{CLINIC_NAME} is located at {CLINIC_ADDRESS}.",
    "contact": f"You can reach us at {CLINIC_PHONE} or email us at {CLINIC_EMAIL}.",
    "thanks": "You're welcome! If you have any more questions, feel free to ask.",
    "emergency": "If this is an emergency, please call your local emergency number immediately or go to the nearest hospital.",
    "medical": (
        "I'm sorry, I can't give medical advice or suggest medicines. "
        f"Please book an appointment or call us at {CLINIC_PHONE} to speak with a doctor. "
        "If this is an emergency, please call your local emergency number right away."
    ),
    "doctors": f"Our doctors are available by appointment. Call {CLINIC_PHONE} to check availability for a specific specialist.",
    "fees": f"For current consultation fees, please call {CLINIC_PHONE} or ask at reception.",
}

# Each word a user might type (key) maps to an intent (value)
# Each word a user might type (key) maps to an intent (value)
KEYWORDS = {
    # greeting
    "hi": "greeting",
    "hello": "greeting",
    "hey": "greeting",
    "salam": "greeting",

    # hours
    "timings": "hours",
    "timing": "hours",
    "open": "hours",
    "hours": "hours",
    "closed": "hours",
    "sunday": "hours",

    # location
    "where": "location",
    "address": "location",
    "location": "location",
    "located": "location",

    # appointment
    "appointment": "appointment",
    "book": "appointment",
    "booking": "appointment",
    "schedule": "appointment",

    # doctors
    "doctor": "doctors",
    "doctors": "doctors",
    "dentist": "doctors",
    "specialist": "doctors",

    # fees
    "fee": "fees",
    "fees": "fees",
    "cost": "fees",
    "charges": "fees",
    "price": "fees",

    # contact
    "phone": "contact",
    "contact": "contact",
    "number": "contact",
    "email": "contact",

    # thanks
    "thanks": "thanks",
    "thank": "thanks",
    "shukriya": "thanks",

    # emergency
    "emergency": "emergency",
    "urgent": "emergency",
    "ambulance": "emergency",
    "accident": "emergency",
    "bleeding": "emergency",

    # medical
    "medicine": "medical",
    "medicines": "medical",
    "medication": "medical",
    "tablet": "medical",
    "tablets": "medical",
    "dose": "medical",
    "dosage": "medical",
    "prescribe": "medical",
    "prescription": "medical",
    "symptoms": "medical",
    "treatment": "medical",
}