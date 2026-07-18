'''
with open('sample.txt', 'w') as f:
    f.write("File created for checking.")
'''
#Uncomment the above code if sample.txt don't exist

import os

filename = 'sample.txt'

if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")