from datetime import datetime

def get_log_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

print(f"{get_log_timestamp()} [INFO] Server started successfully.")
print(f"{get_log_timestamp()} [ERROR] Connection timed out.")