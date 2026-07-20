user = {"name": "Alice"}
try:
    print(user["age"])
except KeyError:
    print("Error: That key is missing from the dictionary.")