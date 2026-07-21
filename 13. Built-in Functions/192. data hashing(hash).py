# hash() generates a fixed-size integer for immutable objects, often used in dictionaries
username = "admin_sohaib"
config_tuple = ("192.168.1.1", 8080)

print(f"Hash of string: {hash(username)}")
print(f"Hash of tuple: {hash(config_tuple)}")