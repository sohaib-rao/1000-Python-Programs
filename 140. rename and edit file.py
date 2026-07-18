'''
with open('old_name.txt', 'w') as f1:
    f1.write("Rename me")
with open('to_delete.txt', 'w') as f2:
    f2.write("Delete me")
'''
#Uncomment the above code if sample.txt don't exist

import os

if os.path.exists('old_name.txt'):
    os.rename('old_name.txt', 'new_name.txt')
    print("Renamed")

if os.path.exists('to_delete.txt'):
    os.remove('to_delete.txt')
    print("Deleted")