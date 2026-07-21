user_message = "This is a dummy message with a scam link."
banned_words = ["scam", "hack", "phishing"]
# Checks if ANY banned word is in the message
if any(word in user_message.lower() for word in banned_words):
    print("Warning: Malicious content detected!")
else:
    print("Message is safe.")