import json

# Converts a Python dictionary into a formatted JSON string
data = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"], "active": True}
json_string = json.dumps(data, indent=4)

print("JSON String Output:")
print(json_string)