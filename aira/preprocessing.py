def clean(text):
    text = text.lower()
    # Remove punctuation marks one by one
    punctuation = "?!.,':)"
    for mark in punctuation:
        text = text.replace(mark, "")
    text = text.strip()
    return text