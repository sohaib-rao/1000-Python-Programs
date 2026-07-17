# The standard way:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

age = 20

# The one-line way:
status = "Adult" if age >= 18 else "Minor"

print(f"The user is an {status}.")