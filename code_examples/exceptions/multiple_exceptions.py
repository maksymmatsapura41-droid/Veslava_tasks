try:
    # Attempting to read a number from a file
    with open("config.txt", "r") as f:
        content = f.read()
        db_port = int(content)
except (FileNotFoundError, ValueError) as e:
    # 'e' captures the specific error message from Python
    print(f"Configuration failed: {e}")