number = 10
try:
    number.append(5)  # Integers don't have an 'append' method
except AttributeError as e:
    print(f"Attribute Error: {e}")