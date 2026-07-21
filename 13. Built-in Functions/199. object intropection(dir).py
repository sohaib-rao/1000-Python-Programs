sample_list = [1, 2, 3]

print("Available methods for a Python list:")
# Filtering out dunder (double underscore) methods for a cleaner output
clean_methods = [method for method in dir(sample_list) if not method.startswith("__")]
print(clean_methods)