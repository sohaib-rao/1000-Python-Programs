num1 = 10
num2 = 5
operator = "*"

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0: 
        print(num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Unknown operator.")