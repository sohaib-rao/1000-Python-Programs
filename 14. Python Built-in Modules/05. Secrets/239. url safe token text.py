import secrets

url_token = secrets.token_urlsafe(32)
print(f"URL-safe Token: {url_token}")