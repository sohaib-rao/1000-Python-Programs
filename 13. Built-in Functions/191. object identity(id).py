# id() returns the unique memory address of an object
text1 = "Hello"
text2 = "Hello"
text3 = "World"

print(f"Memory address of text1: {id(text1)}")
print(f"Memory address of text2: {id(text2)} (Same as text1 because of string interning)")
print(f"Memory address of text3: {id(text3)} (Different)")