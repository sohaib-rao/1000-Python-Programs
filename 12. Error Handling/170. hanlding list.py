items = ["apple", "banana"]
try:
    print(items[5])
except IndexError:
    print("Error: List index is out of range.")