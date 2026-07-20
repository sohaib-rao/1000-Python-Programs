try:
    result = 10 / int("a")
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")