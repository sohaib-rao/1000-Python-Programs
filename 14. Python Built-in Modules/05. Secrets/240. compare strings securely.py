import secrets

user_token = "abc123xyz"
valid_token = "abc123xyz"

is_match = secrets.compare_digest(user_token, valid_token)
print(f"Do the tokens match? {is_match}")

