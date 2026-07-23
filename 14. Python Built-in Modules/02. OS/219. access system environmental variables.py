import os

user = os.environ.get("USER") or os.environ.get("USERNAME")
path_env = os.environ.get("PATH")

print("User:", user)
print("PATH:", path_env)