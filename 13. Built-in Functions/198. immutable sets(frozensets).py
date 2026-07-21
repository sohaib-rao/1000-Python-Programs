# frozenset() creates a set that cannot be altered after creation
allowed_roles = frozenset(["admin", "moderator", "viewer"])

print(f"Allowed roles: {allowed_roles}")

if "admin" in allowed_roles:
    print("Admin access granted.")