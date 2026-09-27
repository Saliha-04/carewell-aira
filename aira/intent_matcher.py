# aira/intent_matcher.py
# PROCESS step of IPO: turns cleaned text into an intent name.

from aira.config import EXIT_COMMANDS
from aira.knowledge_base import KEYWORDS

def find_intent(text):
    """Return the intent for the text, or None.

    Priority order:
    1. Emergency words always win, wherever they appear.
    2. Any other known intent (hours, fees, medical, ...).
    3. Greeting or thanks, only if nothing more useful was found.
       Whichever of the two appears first in the message wins.
    """
    words = text.split()

    # Pass 1: SAFETY FIRST. Scan every word for an emergency.
    for word in words:
        if KEYWORDS.get(word) == "emergency":
            return "emergency"

    # Pass 2: normal matching. Greeting/thanks are remembered, not
    # returned immediately, so "hi, what are your timings?" answers
    # the real question instead of just greeting back.
    found_low_priority = None

    for word in words:
        intent = KEYWORDS.get(word)
        if intent in ["greeting", "thanks"]:
            if found_low_priority is None:
                found_low_priority = intent
        elif intent is not None:
            return intent

    if found_low_priority is not None:
        return found_low_priority

    return None


def is_exit_command(text):
    """Return True if the whole (cleaned) message is an exit command."""
    return text in EXIT_COMMANDS