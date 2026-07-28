rows = 5
i = 1

while i <= rows:
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
    i += 1