'''
with open('sample.txt', 'w') as f:
    f.write("Hello World!\nWelcome to Python file handling.")
'''
#Uncomment the above code if sample.txt don't exist

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)