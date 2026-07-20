try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File does not exist.")
finally:
    print("Execution finished. (Cleanup would happen here)")