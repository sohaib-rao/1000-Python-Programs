num = int(input("Enter number: "))

if num  % 2 == 0:
    print("Even")
else:
    print("Odd")

#OR
print("Even") if num % 2 == 0 else print("Odd")