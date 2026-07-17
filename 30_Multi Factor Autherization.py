# User data
username = "Admin"
password = "SecretPassword123"
is_two_factor_verified = True

if username == "Admin":
    if password == "SecretPassword123":
        if is_two_factor_verified:
            print("Access Granted: Welcome to the system.")
        else:
            print("Access Denied: Please complete 2FA.")
    else:
        print("Access Denied: Incorrect password.")
else:
    print("Access Denied: Username not found.")