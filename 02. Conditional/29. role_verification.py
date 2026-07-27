role = "admin"
allowed_roles = ["admin", "moderator"]
if role in allowed_roles:
    print("Access allowed")