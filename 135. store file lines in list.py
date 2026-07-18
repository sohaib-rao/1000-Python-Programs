'''
with open('sample.txt', 'w') as f:
    f.write("Apple\nBanana\nCherry")
'''
#Uncomment the above code if sample.txt don't exist

with open('sample.txt', 'r') as file:
    lines_list = file.readlines()
    
print(lines_list)