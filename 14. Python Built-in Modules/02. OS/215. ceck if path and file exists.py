import os

path = "sample.txt"
if os.path.exists(path):
    print("Is file:", os.path.isfile(path))
    print("Is directory:", os.path.isdir(path))