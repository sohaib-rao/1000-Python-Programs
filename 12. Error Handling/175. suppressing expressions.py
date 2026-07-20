import contextlib
import os

# Tries to remove the file, but silently ignores it if the file doesn't exist
with contextlib.suppress(FileNotFoundError):
    os.remove("temporary_file.txt")
print("Program continues normally.")