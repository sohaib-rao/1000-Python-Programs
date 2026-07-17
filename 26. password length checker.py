new_password = "apple"

if len(new_password) < 8:
    print("Error: Password is too short. It must be at least 8 characters.")
elif len(new_password) > 20:
    print("Error: Password is too long. It must be 20 characters or fewer.")
else:
    print("Success: Password accepted!")