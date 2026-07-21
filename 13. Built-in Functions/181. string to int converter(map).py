user_input = "10, 20, 30, 40, 50"
# map() converts all string items to integers automatically
numbers = list(map(int, user_input.split(", ")))
print(f"String list converted to integers: {numbers}")