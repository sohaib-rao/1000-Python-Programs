import secrets

options = ["Access Granted", "Access Denied", "Requires 2FA"]
secure_choice = secrets.choice(options)
print(f"Securely chosen option: {secure_choice}")