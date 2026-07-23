import os

file_path = "example.py"
if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    name, ext = os.path.splitext(file_path)
    print(f"Size: {size} bytes, Ext: {ext}")