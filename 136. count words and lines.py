'''
with open('sample.txt', 'w') as f:
    f.write("Hello python\nThis is a sample text file")
'''
#Uncomment the above code if sample.txt don't exist

with open('sample.txt', 'r') as file:
    lines = file.readlines()
    
total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)
total_chars = sum(len(line) for line in lines)

print(f"Lines: {total_lines}")
print(f"Words: {total_words}")
print(f"Characters: {total_chars}")