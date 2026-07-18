'''
with open('file1.txt', 'w') as f1:
    f1.write("File 1 Data\n")
with open('file2.txt', 'w') as f2:
    f2.write("File 2 Data\n")
'''
#Uncomment the above code if sample.txt don't exist

file_names = ['file1.txt', 'file2.txt']

with open('merged.txt', 'w') as outfile:
    for fname in file_names:
        with open(fname, 'r') as infile:
            outfile.write(infile.read())
            outfile.write("\n")

print("Merged")