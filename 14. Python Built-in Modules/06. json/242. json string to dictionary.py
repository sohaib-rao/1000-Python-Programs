import json

# Parses a JSON-formatted string back into a Python dictionary
json_data = '{"city": "New York", "temperature": 22.5, "condition": "Sunny"}'
parsed_dict = json.loads(json_data)

print("Parsed Python Dictionary:")
print(parsed_dict)
print(f"Temperature type: {type(parsed_dict['temperature'])}")