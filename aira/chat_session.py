# Runs the conversation: INPUT -> PROCESS -> OUTPUT, again and again.

from aira.config import BOT_NAME, CLINIC_NAME, FALLBACK_MESSAGE,CLINIC_PHONE
from aira.preprocessing import clean
from aira.intent_matcher import find_intent, is_exit_command
from aira.knowledge_base import RESPONSES,GREETINGS
import random

def get_response(text):
    """Return Aira's reply for already-cleaned text.

    PROCESS only: no input() and no print(), so it is easy to test.
    """
    intent = find_intent(text)

    if intent == "greeting":
        return random.choice(GREETINGS)

    return RESPONSES.get(intent, FALLBACK_MESSAGE)


def run_chat():
    """Run Aira's conversation loop until the user types an exit command."""
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}, the FAQ assistant for {CLINIC_NAME}.")

    user_name = input(f"{BOT_NAME}: What's your name? ").strip()

    if user_name == "":
        user_name = "there"

    print(f"{BOT_NAME}: Nice to meet you, {user_name}! Type 'bye' to exit.")

    awaiting_department = False

    while True:
        # INPUT
        user_input = input("You: ")

        # PROCESS
        text = clean(user_input)

        if is_exit_command(text):
            print(f"{BOT_NAME}: Goodbye! Take care.")
            break

        if text == "":
            print(f"{BOT_NAME}: Please type a question, for example 'What are your hours?'")
            continue

        if awaiting_department:
            print(f"{BOT_NAME}: Got it — I've noted {user_input.strip()} for your appointment. Please call {CLINIC_PHONE} to confirm a time.")
            awaiting_department = False
            continue

        intent = find_intent(text)

        if intent == "appointment":
            print(f"{BOT_NAME}: Sure — which department is this for (e.g. general, dental, pediatrics)?")
            awaiting_department = True
            continue

        response = get_response(text)

        # OUTPUT
        print(f"{BOT_NAME}: {response}")