
import os

def check_log_file(file_path):
    """
    Check if the log file exists and is not empty.
    Returns True if valid, False otherwise.
    """
    if not os.path.exists(file_path):
        print("Error: The log file does not exist.")
        return False
    elif os.path.getsize(file_path) == 0:
        print("Error: The log file is empty.")
        return False
    else:
        print("Log file loaded successfully.")
        return True


# ---------- Usage Example ----------
if __name__ == "__main__":
    file_path = "Sample_Logs/auth.log"
    valid = check_log_file(file_path)
