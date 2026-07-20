def calculate_discount(price):
    assert price >= 0, "Price cannot be negative!"
    return price * 0.9

try:
    calculate_discount(-10)
except AssertionError as e:
    print(f"Assertion Failed: {e}")