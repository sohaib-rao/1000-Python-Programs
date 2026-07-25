import json

# Serializes and writes a Python object directly to an external file
user_settings = {"theme": "dark", "notifications": True, "volume_level": 80}

with open("settings.json", "w") as file:
    json.dump(user_settings, file, indent=4)

print("Successfully wrote settings data to settings.json")