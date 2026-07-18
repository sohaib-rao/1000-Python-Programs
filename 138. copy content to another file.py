'''
with open('source.txt', 'w') as f:
    f.write("Data to be copied to another file.")
'''
#Uncomment the above code if sample.txt don't exist

with open('source.txt', 'r') as src_file, open('destination.txt', 'w') as dest_file:
    for line in src_file:
        dest_file.write(line)

print("Copied")