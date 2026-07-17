# Generate a multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# Print a right-angled triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Print a square pattern of numbers
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()