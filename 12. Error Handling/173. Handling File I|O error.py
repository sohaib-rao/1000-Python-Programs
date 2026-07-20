try:
    with open("missing_config.json", "r") as f:
        config = f.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"File access error: {e}")