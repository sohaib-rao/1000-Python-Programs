password = "SecurePassword123"
conditions = [
    len(password) >= 8,
    any(char.isdigit() for char in password),
    any(char.isupper() for char in password)
]
if all(conditions):
    print("Password is Valid and Strong!")
else:
    print("Weak Password!")