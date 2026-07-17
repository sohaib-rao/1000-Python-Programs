# Stop the loop early using break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Skip an iteration using continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Infinite loop with a break condition
x = 0
while True:
    x += 1
    if x == 5:
        break

# Empty loop using pass (placeholder)
for i in range(5):
    pass