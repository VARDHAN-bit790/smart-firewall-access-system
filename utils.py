import os
from datetime import datetime

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

def log_access(user, status, details):
    filename = os.path.join(LOG_FOLDER, "access_log.txt")
    with open(filename, "a") as log_file:
        log_file.write(f"{datetime.now()} - USER: {user} - STATUS: {status} - DETAILS: {details}\n")
    print(f"[LOG] Access {status} for {user}: {details}")