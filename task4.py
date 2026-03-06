import re
def hide_phone_numbers(text):
    text = re.sub(r"\+84\d{9}","[REDACTED]",text)
    text = re.sub(r"\b\d{10}\b", "[REDACTED]", text)
    return text