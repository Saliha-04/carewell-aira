from aira.preprocessing import clean
from aira.intent_matcher import find_intent, is_exit_command
from aira.chat_session import get_response
from aira.knowledge_base import RESPONSES,GREETINGS
from aira.config import FALLBACK_MESSAGE

def test_find_intent_emergency_beats_greeting():
    assert find_intent("hi this is urgent") == "emergency"

def test_clean_lowercases():
    assert clean("HELLO") == "hello"

def test_clean_removes_punctuation():
    assert clean("Hello?!") == "hello"

def test_clean_strips_whitespace_last():
    assert clean("hello !") == "hello"

def test_clean_handles_only_punctuation():
    assert clean("?!?!") == ""

def test_find_intent_pure_greeting():
    assert find_intent("hi") == "greeting"

def test_find_intent_emergency_beats_other_intent():
    assert find_intent("book urgent appointment") == "emergency"

def test_find_intent_greeting_deferred_to_real_question():
    assert find_intent("hi what are your hours") == "hours"

def test_find_intent_unknown_word():
    assert find_intent("banana") is None

def test_find_intent_empty_text():
    assert find_intent("") is None

# --- medical ---
def test_find_intent_medical():
    assert find_intent("what dose should i take") == "medical"

def test_find_intent_medical_beats_greeting():
    assert find_intent("hi what tablets should i take") == "medical"

def test_find_intent_emergency_beats_medical():
    assert find_intent("urgent i need my tablets") == "emergency"


# --- is_exit_command ---
def test_is_exit_command_exact_match():
    assert is_exit_command("bye") is True

def test_is_exit_command_ignores_substring():
    assert is_exit_command("can i quit my appointment") is False


# --- get_response ---
def test_get_response_known_intent():
    assert get_response("hours") == RESPONSES["hours"]

def test_get_response_unknown_falls_back():
    assert get_response("banana") == FALLBACK_MESSAGE

def test_get_response_doctors_should_not_fall_back():
    # Currently FAILS: RESPONSES has no "doctors" entry yet (see note below).
    assert get_response("doctor") != FALLBACK_MESSAGE

def test_get_response_fees_should_not_fall_back():
    # Currently FAILS: RESPONSES has no "fees" entry yet (see note below).
    assert get_response("fee") != FALLBACK_MESSAGE

def test_find_intent_thanks_deferred_to_real_question():
    assert find_intent("thanks what are your hours") == "hours"

def test_find_intent_pure_thanks():
    assert find_intent("thanks") == "thanks"

def test_find_intent_low_priority_tie_break():
    assert find_intent("hi thanks") == "greeting"

def test_get_response_greeting_is_one_of_the_options():
    assert get_response("hi") in GREETINGS