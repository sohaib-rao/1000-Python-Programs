import secrets

secure_int = secrets.randbelow(100)
print(f"Secure random integer below 100: {secure_int}")