expression = input("Enter any math expression (e.g., 5+10*2): ")
try:
    result = eval(expression)
    print(f"Result: {result}")
except Exception as e:
    print("Invalid Expression!")