import string


def clean_text(text):
    """Preprocess the text."""
    # Lowercase and replace punctuation with whitespace.
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.lower().translate(translator)
    # Remove excess whitespace and return.
    return " ".join(text.split())
