user_database = {
    "user_1": "sohaib",
    "user_3": "admin",
    "user_5": "guest"
}

# We want to extract values for these specific keys, but only if they exist in the dictionary.
# The walrus operator captures the dictionary lookup result to check if it's not None.
keys_to_check = ["user_1", "user_2", "user_3", "user_4"]

valid_users = [username for key in keys_to_check if (username := user_database.get(key)) is not None]

print(f"Found active users: {valid_users}")
