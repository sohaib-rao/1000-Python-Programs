try:
    number = int("hello")
except ValueError:
    print("ValueError: That is not a valid number.")
except TypeError:
    print("TypeError: Invalid operation.")