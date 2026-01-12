import os 
from datetime import datetime

def load_logs(file_path):
    with open(file_path, "r") as f:
        logs = [line.strip() for line in f]
    return logs

log_file = "Sample_Logs/auth.log"

stored_logs = load_logs(log_file)

print("The total number of entries is:", len(stored_logs))
print("First entry:", stored_logs[0])
print("Last entry:", stored_logs[-1])

