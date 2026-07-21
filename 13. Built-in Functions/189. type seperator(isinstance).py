mixed_data = [10, "hello", 3.14, "world", 42, 9.99]
strings = [item for item in mixed_data if isinstance(item, str)]
numbers = [item for item in mixed_data if isinstance(item, (int, float))]
print(f"Strings: {strings}")
print(f"Numbers: {numbers}")