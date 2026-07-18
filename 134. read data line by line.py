'''
with open('sample.txt', 'w') as f:
    f.write("Line 1\nLine 2\nLine 3")
'''
#Uncomment the above code if sample.txt don't exist

with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())