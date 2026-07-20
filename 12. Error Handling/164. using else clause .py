try:
    result = 10 / 2
except ZeroDivisionError:
    print("Divided by zero!")
else:
    print(f"Success! The result is {result}")