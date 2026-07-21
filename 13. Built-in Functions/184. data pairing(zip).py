usernames = ["admin", "guest", "sohaib"]
passwords = ["pass123", "guest_pass", "secureXYZ"]
# zip() pairs the two lists into a dictionary
credentials = dict(zip(usernames, passwords))
print("User Credentials Database:")
print(credentials)